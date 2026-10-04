#!/usr/bin/env node
// Render em PARTES para máquinas com pouca memória (MacBook Air 8 GB): o renderizador local trava
// ("Sequential screenshot capture stalled") depois de ~800 quadros numa mesma sessão do Chrome.
// Cada parte é uma cópia do index.html com os tempos deslocados:
//   - elementos temporizados: data-start -= A (o que começa antes vira 0 e avança data-media-start)
//   - vídeos fora da janela são removidos (o wrapper fica, as animações seguem válidas); áudio removido
//   - animações: a timeline original é tocada de A a B por um tween (tl.tweenFromTo), então todo
//     estado anterior (splits, sets, Ken Burns) chega correto ao 1º quadro da parte
// Cada parte vira renders/chunks/chunk-NN.mp4 (só vídeo). Depois: node scripts/render-chunks.mjs --join
// uso: node scripts/render-chunks.mjs [--size 600] [--only N,M] [--join]
import fs from 'node:fs';
import { execFileSync, spawnSync } from 'node:child_process';
const FPS = +(process.argv[process.argv.indexOf('--fps') + 1] || 30) || 30;
const args = process.argv.slice(2);
const SIZE = +(args[args.indexOf('--size') + 1] || 600) || 600;
const only = args.includes('--only') ? args[args.indexOf('--only') + 1].split(',').map(Number) : null;
const html = fs.readFileSync('index.html', 'utf8');
const attr = (t, k) => (t.match(new RegExp(`(?<![\\w-])${k}="([^"]*)"`)) || [])[1];
const TOTAL = +attr(html.match(/<div[^>]*id="root"[^>]*>/)[0], 'data-duration');
const TOTAL_F = Math.ceil(TOTAL * FPS - 1e-6);
const r4 = x => Math.round(x * 10000) / 10000;
// kit v3: versao do HyperFrames e workers por variavel (render-par.sh). Padrao = a combinacao antiga validada no Air de 8 GB.
// No Air M4 de 16 GB: HF_VERSION=0.8.111 HF_WORKERS=3 com 2 partes em paralelo = ~26 s/parte (x ~40 s sustentado no modo antigo).
const HFV = process.env.HF_VERSION || '0.8.48', HFW = process.env.HF_WORKERS || '1';
const N = Math.ceil(TOTAL_F / SIZE);

function chunkHtml(k, R) {
  const F0 = R ? R[0] : k * SIZE, F1 = R ? R[1] : Math.min(TOTAL_F, F0 + SIZE);
  const A = F0 / FPS, B = F1 / FPS, D = r4(B - A);
  let h = html;
  // áudio fora (o áudio final vem do render completo)
  h = h.replace(/\n?[ \t]*<audio\b[^>]*><\/audio>[^\n]*/g, '');
  // vídeos: remover fora da janela, deslocar os de dentro
  h = h.replace(/<video\b[^>]*data-start="[^"]*"[^>]*><\/video>/g, tag => {
    const s = +attr(tag, 'data-start'), d = +attr(tag, 'data-duration'), ms = +(attr(tag, 'data-media-start') || 0);
    const e = s + d;
    if (e <= A + 1e-4 || s >= B - 1e-4) return '';
    let ns = s - A, nd = d, nms = ms;
    if (ns < 0) { nd = d + ns; nms = ms + (-ns); ns = 0; }
    nd = Math.min(nd, D - ns);
    return tag.replace(/data-start="[^"]*"/, `data-start="${r4(ns)}"`).replace(/data-duration="[^"]*"/, `data-duration="${r4(nd)}"`)
      .replace(/data-media-start="[^"]*"/, `data-media-start="${r4(nms)}"`);
  });
  // divs temporizados (legendas, callouts, grafismos): deslocar; fora da janela → escondidos para sempre
  h = h.replace(/<div\b(?![^>]*id="root")[^>]*data-start="[^"]*"[^>]*>/g, tag => {
    const s = +attr(tag, 'data-start'), d = +attr(tag, 'data-duration');
    const e = s + d;
    if (e <= A + 1e-4 || s >= B - 1e-4) return tag.replace(/data-start="[^"]*"/, `data-start="${r4(D + 5)}"`).replace(/data-duration="[^"]*"/, 'data-duration="0.1"');
    let ns = s - A, nd = d;
    if (ns < 0) { nd = d + ns; ns = 0; }
    nd = Math.min(nd, D - ns);
    return tag.replace(/data-start="[^"]*"/, `data-start="${r4(ns)}"`).replace(/data-duration="[^"]*"/, `data-duration="${r4(nd)}"`);
  });
  h = h.replace(/(id="root"[^>]*data-duration=")[^"]*(")/, `$1${D}$2`);
  // sub-composicoes (data-composition-src, ex.: compositions/mg.html — nasceu no reel ALAN MULALLY): a timeline delas comeca no
  // 0 local; sem isto, numa parte que comeca em A a camada mostrava o estado de (t - A). Cada parte ganha uma copia da
  // sub-composicao cuja timeline toca de A a B, como a principal.
  h = h.replace(/data-composition-src="([^"]+)"/g, (m, src) => {
    const sub = fs.readFileSync(src, 'utf8');
    const reg = sub.match(/window\.__timelines\["([^"]+)"\] = tl;/);
    if (!reg) throw new Error(`registro da timeline nao encontrado em ${src}`);
    const dst = src.replace(/([^/]+)\.html$/, `_chunk-${F0}-$1.html`);
    fs.writeFileSync(dst, sub.replace(reg[0], `var __sc = gsap.timeline({ paused: true }); __sc.add(tl.tweenFromTo(${r4(A)}, ${r4(B)}, { ease: "none" }), 0); window.__timelines["${reg[1]}"] = __sc;`));
    return `data-composition-src="${dst}"`;
  });
  // timeline: toca a original de A a B
  const reg = 'window.__timelines["main"] = tl;';
  if (!h.includes(reg)) throw new Error('registro da timeline não encontrado');
  h = h.replace(reg, `const __chunk = gsap.timeline({ paused: true });\n      __chunk.add(tl.tweenFromTo(${r4(A)}, ${r4(B)}, { ease: "none" }), 0);\n      window.__timelines["main"] = __chunk;`);
  return { h, F0, F1, A, B };
}

if (!args.includes('--join')) {
  for (let k = 0; k < N; k++) {
    if (only && !only.includes(k)) continue;
    const out = `renders/chunks/chunk-${String(k).padStart(2, '0')}.mp4`;
    if (fs.existsSync(out) && !only) { console.log(`parte ${k}: já existe`); continue; }
    const SPLIT = args.includes('--split') ? +args[args.indexOf('--split') + 1] : 1;
    if (SPLIT > 1) {
      // parte que trava sempre no mesmo quadro: renderiza em pedacos menores (sessoes novas) e une
      const k0 = k * SIZE, k1 = Math.min(TOTAL_F, k0 + SIZE), step = Math.ceil((k1 - k0) / SPLIT), subs = [];
      for (let j = 0; j < SPLIT; j++) {
        const R = [k0 + j * step, Math.min(k1, k0 + (j + 1) * step)];
        const { h } = chunkHtml(k, R); const file = `render-chunk-${k}-${j}.html`; fs.writeFileSync(file, h);
        const so = `renders/chunks/sub-${String(k).padStart(2, '0')}-${j}.mp4`;
        console.log(`parte ${k + 1} pedaco ${j + 1}/${SPLIT}: quadros ${R[0]}–${R[1] - 1}`);
        const r = spawnSync('npx', ['--yes', `hyperframes@${HFV}`, 'render', '-c', file, '--sdr', '-f', String(FPS), '-q', 'delivery',
          '-o', so, '--workers', HFW, '--video-frame-format', 'jpg', '--no-best-effort', '--browser-timeout', '300',
          ...(process.env.RENDER_EXTRA ? process.env.RENDER_EXTRA.split(' ') : [])], { encoding: 'utf8', maxBuffer: 1 << 28 });
        fs.writeFileSync(so.replace('.mp4', '.log'), (r.stdout || '') + (r.stderr || '')); fs.rmSync(file, { force: true });
        const ok = fs.existsSync(so) && /Render complete/.test((r.stdout || '') + (r.stderr || ''));
        console.log(`  ${ok ? 'OK' : 'FALHOU'}`); if (!ok) process.exit(1);
        // cada pedaco sai com +1 quadro (copia do ultimo) — corta no numero exato antes de unir
        // (reel Andy Grove: sem isso a parte unida deu 357/354 e o script abortava)
        const st = so.replace('.mp4', '-t.mp4');
        execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-i', so, '-frames:v', String(R[1] - R[0]), '-c', 'copy', st]);
        subs.push(st);
      }
      fs.writeFileSync(`renders/chunks/sub-${k}.txt`, subs.map(p => `file '${process.cwd()}/${p}'`).join('\n'));
      execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', `renders/chunks/sub-${k}.txt`, '-c', 'copy', out]);
      const fr = +execFileSync('/opt/homebrew/bin/ffprobe', ['-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out], { encoding: 'utf8' }).trim();
      console.log(`  parte ${k + 1} unida: ${fr}/${k1 - k0} quadros`); if (fr !== k1 - k0) process.exit(1);
      continue;
    }
    const { h, F0, F1 } = chunkHtml(k);
    const file = `render-chunk-${String(k).padStart(2, '0')}.html`;
    fs.writeFileSync(file, h);
    console.log(`parte ${k + 1}/${N}: quadros ${F0}–${F1 - 1} (${F1 - F0})`);
    const t0 = Date.now();
    const r = spawnSync('npx', ['--yes', `hyperframes@${HFV}`, 'render', '-c', file, '--sdr', '-f', String(FPS), '-q', 'delivery',
      '-o', out, '--workers', HFW, '--video-frame-format', 'jpg', '--no-best-effort', '--browser-timeout', '300', ...(process.env.RENDER_EXTRA ? process.env.RENDER_EXTRA.split(' ') : [])],
      { encoding: 'utf8', maxBuffer: 1 << 28 });
    fs.writeFileSync(`renders/chunks/chunk-${String(k).padStart(2, '0')}.log`, (r.stdout || '') + (r.stderr || ''));
    fs.rmSync(file, { force: true });
    const ok = fs.existsSync(out) && /Render complete/.test((r.stdout || '') + (r.stderr || ''));
    const frames = ok ? +execFileSync('/opt/homebrew/bin/ffprobe', ['-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out], { encoding: 'utf8' }).trim() : 0;
    console.log(`  ${ok ? 'OK' : 'FALHOU'} em ${((Date.now() - t0) / 60000).toFixed(1)} min · ${frames}/${F1 - F0} quadros`);
    if (!ok || frames !== F1 - F0) process.exit(1);
  }
} else {
  const parts = Array.from({ length: N }, (_, k) => `renders/chunks/chunk-${String(k).padStart(2, '0')}.mp4`);
  for (const p of parts) if (!fs.existsSync(p)) throw new Error(`falta ${p}`);
  fs.writeFileSync('renders/chunks/lista.txt', parts.map(p => `file '${process.cwd()}/${p}'`).join('\n'));
  execFileSync('/opt/homebrew/bin/ffmpeg', ['-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', 'renders/chunks/lista.txt', '-c', 'copy', '-an', 'renders/chunks/_video.mp4']);
  console.log('vídeo unido: renders/chunks/_video.mp4');
}
