#!/usr/bin/env node
// Gera a edição completa (vídeo + voz J-cut + B-rolls + legendas + callouts +
// light-leaks + SFX + trilha) a partir de assets/edit-plan.json e injeta em
// index.html entre <!-- EDIT:BEGIN -->...<!-- EDIT:END --> e // EDIT-TWEENS:BEGIN...END.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const plan = JSON.parse(fs.readFileSync(path.join(ROOT, 'assets/edit-plan.json'), 'utf8'));
const FPS = plan.fps || 30;
const F = n => n / FPS;
const r3 = x => Math.round(x * 1000) / 1000;

const LEAD_FRAMES = plan.jcutLeadFrames ?? 5;
const XFADE_FRAMES = plan.jcutCrossfadeFrames ?? LEAD_FRAMES;
const LEAD = F(LEAD_FRAMES);   // J-cut: voz entra antes do corte (timeline)
const XFADE = F(XFADE_FRAMES); // crossfade entre as duas faixas de voz
const LEAK_DUR = 0.7;   // light-leak 21 frames
const LEAK_PRE = F(10); // leak começa 10 frames antes do corte
const RATE = plan.rate || 1;

// ---- segmentos → linha do tempo ----
let t = 0;
const segs = plan.segments.map((s, i) => {
  const sourceDur = r3((s.out - s.in) / RATE);
  const lead = i === 0 ? 0 : Math.min(LEAD, sourceDur - F(10));
  // O conteúdo falado do take começa `lead` antes do corte visual. Para manter
  // lip-sync, os primeiros `lead` segundos do VÍDEO ficam cobertos pelo take
  // anterior e a janela visual deste segmento fica menor na mesma medida.
  const dur = r3(sourceDur - lead);
  if (dur <= F(10)) throw new Error(`Segmento ${i} (${s.label}) curto demais`);
  const tStart = r3(t);
  const seg = {
    ...s,
    i,
    lead,
    sourceDur,
    dur,
    tStart,
    audioStart: r3(tStart - lead),
    tEnd: r3(tStart + dur),
  };
  t = r3(t + dur);
  return seg;
});
const TOTAL = r3(t);
const rateAttr = RATE !== 1 ? ` data-playback-rate="${RATE}"` : '';
const volTweens = [];

// ---- vídeo do apresentador (track 0, mudo, dentro do wrapper) ----
// videoTail (source sec): o VÍDEO deste take corta antes do fim (desvio de olhar);
// o vídeo do PRÓXIMO take entra adiantado com pré-rolo (L-cut) enquanto a voz termina.
// Lip-sync preservado: quando a imagem do take entra em tStart, ela já avançou
// o mesmo `lead` que o áudio avançou durante o J-cut.
const earlyDelta = segs.map(s => s.videoTail ? r3((s.out - s.videoTail) / RATE) : 0);
// Janela de um B-roll na timeline. preStart antecipa a janela inteira; span [f0, f1] recorta
// uma fração dela (vários B-rolls seguidos dentro do mesmo trecho de fala, um a cada ~4 s).
const brollWin = b => {
  const w0 = r3(segs[b.fromSeg].tStart - (b.preStart || 0));
  const w1 = segs[b.toSeg].tEnd;
  const [f0, f1] = b.span || [0, 1];
  return [r3(w0 + (w1 - w0) * f0), r3(w0 + (w1 - w0) * f1)];
};
const fullWins = (plan.broll || []).filter(b => b.mode !== 'split').map(brollWin);
const coveredFull = (a, b) => fullWins.some(([w0, w1]) => w0 <= a + 0.02 && b <= w1 + 0.02);
// presenterZoom: "corte seco com zoom" no apresentador — a escala alterna a cada corte de take e,
// dentro de takes longos, a cada `maxHold` s no máximo (ritmo: algo muda na tela a cada <= 4 s).
// Não mexe no lip-sync: cada pedaço é o mesmo vídeo, só com outro enquadramento.
const PZ = plan.presenterZoom || null;
// O corte com zoom NÃO duplica elementos <video> (o Chrome só carrega ~75 players por aba e a
// composição ficava com a tela preta no preview): a escala é aplicada por tl.set no wrapper
// #presenter-zoom, nos mesmos instantes em que o enquadramento deveria trocar.
const zoomCuts = [];
const videoCutTimes = [];
let zoomIdx = 0;
const videoClips = segs.map(s => {
  const dPrev = s.i > 0 ? earlyDelta[s.i - 1] : 0;
  const vStart = r3(s.tStart - dPrev);
  const vEnd = r3(s.tEnd - earlyDelta[s.i]);
  const vDur = r3(vEnd - vStart);
  const vMedia = r3(s.in + (s.lead - dPrev) * RATE);
  if (vMedia < 0) throw new Error(`seg${s.i}: pré-rolo estoura o início do source`);
  if (PZ) {
    const n = coveredFull(vStart, vEnd) ? 1 : Math.max(1, Math.ceil(vDur / PZ.maxHold - 1e-6));
    for (let p = 0; p < n; p++) {
      zoomCuts.push({ t: r3(vStart + (vDur * p) / n), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    }
  }
  videoCutTimes.push(vStart);
  return `      <video id="v${s.i}" class="clip" src="${plan.src}" data-start="${vStart}" data-duration="${vDur}" data-media-start="${vMedia}"${rateAttr} data-track-index="0" muted playsinline preload="auto"></video> <!-- ${s.label} -->`;
}).join('\n');
const presenterClips = plan.bakedAroll === false ? videoClips
  : `      <video id="aroll" class="clip" src="assets/aroll.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="0" muted playsinline preload="auto"></video> <!-- corte do apresentador (${segs.length} takes + L-cuts + ${RATE}x) gerado por scripts/bake.py -->`;
// presenterZoom.mode "scene" (ritmo de ~4 s): em vez de trocar o zoom em TODO corte de take (a cada ~2 s),
// troca uma vez em cada aparicao do apresentador (janela entre B-rolls de tela cheia) e, se a aparicao
// passar de `sceneMax` s, mais uma vez no corte de take mais proximo do meio dela.
if (PZ && PZ.mode === 'scene') {
  zoomCuts.length = 0; zoomIdx = 0;
  const fw = [...fullWins].sort((a, b) => a[0] - b[0]);
  const vis = []; let c0 = 0;
  for (const [a, b] of fw) { if (a > c0 + 0.05) vis.push([c0, a]); c0 = Math.max(c0, b); }
  if (TOTAL > c0 + 0.05) vis.push([c0, TOTAL]);
  const cuts = videoCutTimes;
  for (const [a, b] of vis) {
    zoomCuts.push({ t: r3(a), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    // no split a troca de imagem do topo ja e o evento: sem zoom extra no meio
    const inSplit = (plan.broll || []).some(x => x.mode === 'split' && (() => { const [w0, w1] = brollWin(x); return w0 < b && w1 > a; })());
    if (!inSplit && b - a > (PZ.sceneMax ?? 4.6)) {
      const mid = (a + b) / 2;
      const cand = cuts.filter(t => t > a + 1.8 && t < b - 1.8).sort((x, y) => Math.abs(x - mid) - Math.abs(y - mid))[0];
      zoomCuts.push({ t: r3(cand ?? mid), scale: PZ.scales[zoomIdx++ % PZ.scales.length] });
    }
  }
}
volTweens.push(`tl.set("#presenter-zoom", { transformOrigin: "${PZ ? PZ.origin || '50% 42%' : '50% 42%'}" }, 0);`);
zoomCuts.forEach(z => volTweens.push(`tl.set("#presenter-zoom", { scale: ${z.scale} }, ${z.t});`));

// ---- voz ----
// BAKED (padrão): o J-cut inteiro (42 clipes + crossfades) é renderizado OFFLINE por
// scripts/mixaudio.py em assets/voz-mix.m4a e entra como UM elemento <audio>. Motivo: o Chrome
// carrega ~75 players de mídia por aba; com um clipe por take a composição passava de 160
// elementos e o preview ficava preto. O mix vem do mesmo edit-plan.json (work/mix-plan.json).
// Emenda ponta a ponta (reel Atul Gawande): a voz de cada take vai ate o inicio da voz do take seguinte
// (+ XFADE de crossfade, que cai no silencio do tail `aout`); nada de duas vozes somadas durante o lead.
// O video do take continua os 5 quadros de lead depois disso (out = aout + lead*rate): J-cut.
const mixVoice = segs.map((s, i) => {
  const next = segs[i + 1];
  const dur = next ? r3(next.audioStart - s.audioStart + XFADE) : s.sourceDur;
  return { label: s.label, start: s.audioStart, dur, in: s.in, out: r3(s.in + dur * RATE), first: s.i === 0, xfade: XFADE };
});
const voiceClips = plan.bakedAudio === false
  ? segs.map(s => {
      const start = s.audioStart, dur = s.sourceDur, end = r3(start + dur), track = 10 + (s.i % 2);
      if (s.i === 0) volTweens.push(`tl.fromTo("#voz${s.i}", { volume: 1 }, { volume: 1, duration: ${r3(dur - XFADE)}, ease: "none" }, 0);`);
      else volTweens.push(`tl.fromTo("#voz${s.i}", { volume: 0 }, { volume: 1, duration: ${r3(XFADE)}, ease: "none" }, ${start});`);
      volTweens.push(`tl.to("#voz${s.i}", { volume: 0, duration: ${r3(XFADE)}, ease: "none" }, ${r3(end - XFADE)});`);
      return `    <audio id="voz${s.i}" src="${plan.voiceSrc || plan.src}" data-start="${start}" data-duration="${dur}" data-media-start="${r3(s.in)}"${rateAttr} data-track-index="${track}"></audio> <!-- ${s.label} -->`;
    }).join('\n')
  : `    <audio id="voz-mix" src="assets/voz-mix.m4a" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="10"></audio> <!-- voz com J-cut ${LEAD_FRAMES}f/${XFADE_FRAMES}f (gerada por scripts/mixaudio.py) -->`;

// ---- B-rolls ----
// mode "full": cobre a tela toda; mode "split": faixa de 44% do topo.
// Tomadas SEGUIDAS da mesma cena (janelas contíguas e mesmo modo) entram como UM elemento
// <video>, apontando para o arquivo concatenado por scripts/concat_broll.py — o movimento de
// câmera de cada tomada já vem gravado pelo make_broll.py. Isso derruba o número de players.
const shots = (plan.broll || []).map((b, k) => { const [t0, t1] = brollWin(b); return { ...b, k, t0, t1, dur: r3(t1 - t0) }; });
const groups = [];
shots.forEach(sh => {
  const last = groups[groups.length - 1];
  if (last && last.mode === sh.mode && Math.abs(last.t1 - sh.t0) < 0.02 && !sh.objectPosition && !last.objectPosition) {
    last.shots.push(sh); last.t1 = sh.t1;
  } else groups.push({ mode: sh.mode, t0: sh.t0, t1: sh.t1, shots: [sh] });
});
const brollClips = [];
const splitWindows = [];
groups.forEach((g, gi) => {
  const dur = r3(g.t1 - g.t0);
  const file = !g.shots[0].file ? '' : g.shots.length === 1 ? g.shots[0].file : `assets/broll/_cena${String(gi).padStart(2, '0')}.mp4`;
  g.file = file;
  const op = g.shots[0].objectPosition ? ` style="object-position: ${g.shots[0].objectPosition}"` : '';
  const nomes = g.shots.map(x => x.file.split('/').pop()).join(' + ');
  if (g.mode === 'split') {
    // kit v3: split com file "" = a faixa de cima e desenhada pela camada de motion (compositions/mg.html, splitIn/splitOut);
    // aqui fica so o wrapper (o apresentador continua sendo arrastado pelo split). Sem <video>: render mais leve.
    if (!g.shots[0].file) brollClips.push(`    <div class="broll-split-wrap" id="bsw${gi}"></div> <!-- split desenhado pela camada de motion -->`);
    else brollClips.push(`    <div class="broll-split-wrap" id="bsw${gi}"><video id="broll${gi}" class="clip" src="${file}" data-start="${g.t0}" data-duration="${dur}" data-media-start="0" data-track-index="${2 + (gi % 2)}"${op} muted playsinline preload="auto"></video></div> <!-- ${nomes} -->`);
    const last = splitWindows[splitWindows.length - 1];
    if (last && Math.abs(last.end - g.t0) < 0.02) { last.end = g.t1; last.lastK = gi; }
    else splitWindows.push({ start: g.t0, end: g.t1, firstK: gi, lastK: gi });
  } else if (plan.bakedBroll) {
    // bakedBroll: todas as cenas de tela cheia estao gravadas em assets/broll-full.mp4 (scripts/bake.py
    // brollfull), no tempo exato da timeline. Aqui so liga/desliga a camada na janela da cena.
    // Motivo: com um <video> por cena (27) + um por light-leak (29) o Chrome do Fabio esgotava os
    // decoders e os B-rolls sumiam no preview (a timeline mostrava os clipes, a imagem nao).
    volTweens.push(`tl.set("#bfw-all", { autoAlpha: 1 }, ${g.t0});`);
    volTweens.push(`tl.set("#bfw-all", { autoAlpha: 0 }, ${g.t1});`);
  } else {
    brollClips.push(`    <div class="broll-full-wrap" id="bfw${gi}"><video id="broll${gi}" class="clip" src="${file}" data-start="${g.t0}" data-duration="${dur}" data-media-start="0" data-track-index="${2 + (gi % 2)}"${op} muted playsinline preload="auto"></video></div> <!-- ${nomes} -->`);
    // Ken Burns só quando o arquivo não tem movimento próprio (make_broll já grava a câmera)
    if (plan.brollKenBurns) volTweens.push(`tl.fromTo("#bfw${gi}", { scale: 1 }, { scale: 1.07, duration: ${dur}, ease: "none" }, ${g.t0});`);
  }
});
if (plan.bakedBroll && groups.some(g => g.mode !== 'split')) {
  const nFull = groups.filter(g => g.mode !== 'split').length;
  brollClips.unshift(`    <div class="broll-full-wrap" id="bfw-all"><video id="broll-full" class="clip" src="assets/broll-full.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="2" muted playsinline preload="auto"></video></div> <!-- ${nFull} cenas de tela cheia (gerada por scripts/bake.py brollfull) -->`);
}
fs.writeFileSync(path.join(ROOT, 'work/broll-groups.json'), JSON.stringify(groups.map(g => ({
  file: g.file, mode: g.mode, t0: g.t0, t1: g.t1,
  shots: g.shots.map(x => ({ file: x.file, dur: x.dur })),
})), null, 1));

// Transição tela cheia ⇄ split: apresentador é "arrastado" pra baixo enquanto o
// B-roll do topo desce junto revelando o split; na saída, ambos sobem de volta.
const SPLIT_Y = plan.splitShiftY ?? 710;
const TRANS = 0.55;
volTweens.push(`tl.set("#presenter-wrap", { transformOrigin: "50% 38%" }, 0);`);
splitWindows.forEach(w => {
  if (w.start === 0) {
    volTweens.push(`tl.set("#presenter-wrap", { y: ${SPLIT_Y} }, 0);`);
  } else {
    volTweens.push(`tl.fromTo("#presenter-wrap", { y: 0 }, { y: ${SPLIT_Y}, duration: ${TRANS}, ease: "power3.inOut" }, ${w.start});`);
    volTweens.push(`tl.fromTo("#bsw${w.firstK}", { yPercent: -100 }, { yPercent: 0, duration: ${TRANS}, ease: "power3.inOut" }, ${w.start});`);
  }
  volTweens.push(`tl.to("#presenter-wrap", { y: 0, duration: ${TRANS}, ease: "power3.inOut" }, ${r3(w.end - TRANS)});`);
  volTweens.push(`tl.to("#bsw${w.lastK}", { yPercent: -100, duration: ${TRANS}, ease: "power3.inOut" }, ${r3(w.end - TRANS)});`);
});
// Push-in lento no encerramento (CTA)
const ctaSegIdx = plan.ctaSeg ?? 12;
const ctaStart = segs[ctaSegIdx] ? segs[ctaSegIdx].tStart : null;
if (ctaStart != null) volTweens.push(`tl.fromTo("#presenter-wrap", { scale: 1 }, { scale: 1.05, duration: ${r3(TOTAL - ctaStart)}, ease: "none" }, ${ctaStart});`);

// ---- legendas (palavra-a-palavra → chunks de até 3 palavras) ----
const meta = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(ROOT, 'assets/chunks/meta.json'), 'utf8')).map(m => [m.i, m]));
const norm = w => w.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');
function segWords(seg) {
  const ch = seg.chunk;
  const off = meta[ch].off;
  const j = JSON.parse(fs.readFileSync(path.join(ROOT, `assets/chunks/ch${String(ch).padStart(2, '0')}-words.json`), 'utf8'));
  const words = [];
  for (const e of j.transcription) {
    const text = e.text.trim();
    if (!text || /^\[.*\]$/.test(text)) continue;
    const src = off + e.offsets.from / 1000;
    const srcEnd = off + e.offsets.to / 1000;
    // legenda so ate o fim da VOZ do take (aout): o video segura o lead e pode conter o comeco do take seguinte
    if (srcEnd < seg.in - 0.05 || src > (seg.aout ?? seg.out) + 0.05) continue;
    words.push({ text, t: r3(Math.max(seg.audioStart, seg.audioStart + (src - seg.in) / RATE)) });
  }
  return words;
}
const capDivs = [];
const typingSfx = [];
const bigDivs = [];
let capId = 0, bigId = 0, typingDone = false;
const impacts = plan.impacts || [];
// janelas com B-roll na tela (split ou full): legenda fica no centro (44%);
// apresentador sozinho em tela cheia: legenda desce (cap-low) pra não cobrir o rosto
const brollWindows = (plan.broll || []).map(brollWin);
const overBroll = (a, b) => brollWindows.some(([w0, w1]) => (a + b) / 2 >= w0 && (a + b) / 2 < w1);
segs.forEach(seg => {
  if (seg.chunk === undefined) return;
  const words = segWords(seg);
  if (!words.length) return;
  // hookSeg: o gancho aparece INTEIRO desde o frame 0 (capa do reel), numa caixa só.
  // Padrão do formato: hookSeg = 0. Para desligar (voltar às legendas de 3 palavras no gancho),
  // usar "hookSeg": null no plano.
  if ((plan.hookSeg === undefined ? 0 : plan.hookSeg) === seg.i) {
    const hookEnd = segs[seg.i + 1]?.audioStart ?? seg.tEnd;
    const hookStart = seg.i === 0 ? 0 : seg.audioStart;
    const hookDur = r3(hookEnd - hookStart);
    capDivs.push(`    <div id="cap${capId++}" class="clip cap cap-hook" data-start="${hookStart}" data-duration="${hookDur}" data-track-index="5"><span id="hook-box" class="hook-box"><span class="hook-shine" id="hook-shine"></span><span class="hook-text">${words.map(w => w.text).join(' ')}</span></span></div>`);
    // Efeitos do gancho (seek-safe, no timeline): caixa completa já no frame 0 (capa);
    // pulso suave de escala + brilho atravessando a caixa duas vezes.
    const half = r3(hookDur / 4);
    volTweens.push(`tl.fromTo("#hook-box", { scale: 1 }, { scale: 1.018, duration: ${half}, ease: "sine.inOut", repeat: 3, yoyo: true }, ${hookStart});`);
    volTweens.push(`tl.fromTo("#hook-shine", { xPercent: -160 }, { xPercent: 260, duration: 0.9, ease: "power2.inOut" }, ${r3(hookStart + 0.5)});`);
    volTweens.push(`tl.fromTo("#hook-shine", { xPercent: -160 }, { xPercent: 260, duration: 0.9, ease: "power2.inOut", immediateRender: false }, ${r3(hookStart + Math.max(1.6, hookDur - 1.6))});`);
    return;
  }
  // Durante o J-cut há duas falas em crossfade. A legenda nova ganha prioridade:
  // a legenda do take anterior encerra assim que a próxima voz começa.
  const segTextEnd = segs[seg.i + 1]?.audioStart ?? seg.tEnd;
  // localizar frases de impacto neste segmento
  const wnorm = words.map(w => norm(w.text));
  const zones = [];
  for (const imp of impacts) {
    if (imp.seg !== undefined && imp.seg !== seg.i) continue; // callout preso a um segmento
    const pw = imp.phrase.split(/\s+/).map(norm);
    for (let i = 0; i + pw.length <= wnorm.length; i++) {
      if (pw.every((p, k) => wnorm[i + k] === p)) {
        const start = words[i].t;
        const endW = words[i + pw.length]; // início da palavra seguinte (ou fim do seg)
        const supEnd = r3(endW ? Math.min(endW.t, segTextEnd) : segTextEnd); // supressão só durante a frase
        const end = r3(Math.min(segTextEnd, supEnd + (imp.hold ?? 0.7))); // callout segura o hold
        zones.push({ start, supEnd, end, imp });
        break;
      }
    }
  }
  // chunks normais (até 3 palavras, quebra em pontuação), pulando as zonas de impacto
  const inZone = tt => zones.some(z => tt >= z.start - 0.001 && tt < z.supEnd);
  let group = [];
  const flush = nextT => {
    if (!group.length) return;
    const start = group[0].t;
    const end = r3(Math.min(segTextEnd, nextT));
    if (end - start < 0.1) { group = []; return; }
    const text = group.map(w => w.text).join(' ');
    const yellow = (plan.yellowCapSegs || []).includes(seg.i) ? ' cap-yellow' : '';
    // capLowSegs: força a legenda baixa mesmo sobre B-roll — usado quando o B-roll
    // tem informação importante na faixa dos 44% (ex.: logotipo no meio do quadro).
    const forceLow = (plan.capLowSegs || []).includes(seg.i);
    // reel HERB KELLEHER: dentro do SPLIT a legenda fica sempre na divisa (44%) — a 76% ela cai na boca do
    // apresentador (a faixa de baixo e o rosto). capLowSegs so vale sobre B-roll de TELA CHEIA.
    const mid = (start + end) / 2;
    const inSplitWin = splitWindows.some(w => Math.min(end, w.end) - Math.max(start, w.start) > 0.08);
    const overFull = fullWins.some(([w0, w1]) => mid >= w0 && mid < w1);
    const low = inSplitWin ? '' : (overFull ? (forceLow ? ' cap-low' : '') : (overBroll(start, end) ? '' : ' cap-low'));
    const capTrack = 5 + 2 * (seg.i % 2); // 5/7 pingue-pongue para captions sobrepostos pelo J-cut
    capDivs.push(`    <div id="cap${capId++}" class="clip cap${yellow}${low}" data-start="${start}" data-duration="${r3(end - start)}" data-track-index="${capTrack}">${text}</div>`);
    group = [];
  };
  words.forEach((w, i) => {
    if (inZone(w.t)) { flush(w.t); return; }
    group.push(w);
    const punct = /[.,!?;:]$/.test(w.text);
    const next = words[i + 1];
    const nextT = next ? next.t : segTextEnd;
    if (group.length >= 3 || punct || !next || inZone(nextT)) flush(nextT);
  });
  // callouts grandes
  for (const z of zones) {
    const lines = (z.imp.lines || [z.imp.phrase.toUpperCase()]).map(l => l.toUpperCase());
    const html = lines.join('<br/>');
    const dur = r3(z.end - z.start);
    if (z.imp.style === 'typing' && !typingDone) {
      typingDone = true;
      // spans por caractere para o efeito de digitação
      const chars = [];
      let ci = 0;
      for (const line of lines) {
        for (const c of line) chars.push(`<span class="tc" id="tc${ci++}">${c === ' ' ? '&nbsp;' : c}</span>`);
        chars.push('<br/>');
      }
      chars.pop();
      // impacts[].top tambem no callout de digitacao (o B-roll pode ter rosto na faixa dos 30%)
      const topT = z.imp.top != null ? ` style="top: ${z.imp.top}%"` : '';
      bigDivs.push(`    <div id="big${bigId}" class="clip cap-big"${topT} data-start="${z.start}" data-duration="${dur}" data-track-index="6"><span class="inner">${chars.join('')}</span></div>`);
      // reel KAZUO INAMORI: callout de digitacao curto (1,1 s, fecha o take) — a digitacao tem que acabar a tempo do pulso (0,14 s) fechar antes da saida
      const typeDur = Math.min(1.35, dur * 0.7, Math.max(0.3, dur - 0.2 - 0.14 - F(2)));
      const per = r3(typeDur / ci);
      volTweens.push(`for (let i = 0; i < ${ci}; i++) tl.set("#tc" + i, { autoAlpha: 1 }, ${z.start} + ${per} * i);`);
      // settle: pulso de escala quando a digitação completa + saída suave
      const tEndType = r3(z.start + typeDur);
      volTweens.push(`tl.fromTo("#big${bigId} .inner", { scale: 1 }, { scale: 1.06, duration: 0.14, ease: "power2.out" }, ${tEndType});`);
      // o settle tem que FECHAR antes da saída começar (1 quadro de folga): com duração fixa
      // de 0,21 s ele invadia a saída em callout curto e o linter acusava tweens concorrentes
      const tExit = r3(z.start + dur - 0.2);
      // callout curto (a frase fecha o take e a voz seguinte entra logo): sem espaco para o settle,
      // a saida parte direto da escala 1.06 (reel Atul Gawande, "NAO ERRA POR BURRICE": 1,27 s)
      const settleRoom = r3(Math.min(0.21, tExit - (tEndType + 0.15) - F(1)));
      if (settleRoom >= 0.06) volTweens.push(`tl.to("#big${bigId} .inner", { scale: 1, duration: ${settleRoom}, ease: "power2.inOut" }, ${r3(tEndType + 0.15)});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { autoAlpha: 0, scale: 1.1, duration: 0.2, ease: "power2.in" }, ${tExit});`);
      volTweens.push(`tl.set("#big${bigId} .inner", { autoAlpha: 0 }, ${r3(z.start + dur)});`);
      // drum-fill simulando a digitação
      typingSfx.push({ file: 'assets/sfx/drum-fill.m4a', start: z.start, dur: 1.43, vol: 0.3, nome: 'drum-fill do callout de digitação' });
    } else {
      // impacts[].top: altura do callout em % (padrao 30%) — quando o B-roll tem o rosto na faixa dos 30%
      const topSt = z.imp.top != null ? ` style="top: ${z.imp.top}%"` : '';
      bigDivs.push(`    <div id="big${bigId}" class="clip cap-big"${topSt} data-start="${z.start}" data-duration="${dur}" data-track-index="6"><span class="inner">${html}</span></div>`);
      // pop fluido: entra com back-ease + leve rotação, cresce devagar, sai limpo
      // deixa 1 frame de folga antes da saída para evitar tweens concorrentes
      const grow = Math.max(0.12, r3(dur - 0.42 - 0.24));
      volTweens.push(`tl.fromTo("#big${bigId} .inner", { scale: 0.5, rotation: -5, y: 44, autoAlpha: 0 }, { scale: 1, rotation: 0, y: 0, autoAlpha: 1, duration: 0.42, ease: "back.out(2.4)" }, ${z.start});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { scale: 1.07, duration: ${grow}, ease: "power1.inOut" }, ${r3(z.start + 0.43)});`);
      volTweens.push(`tl.to("#big${bigId} .inner", { autoAlpha: 0, scale: 1.14, duration: 0.22, ease: "power2.in" }, ${r3(z.start + dur - 0.22)});`);
      volTweens.push(`tl.set("#big${bigId} .inner", { autoAlpha: 0 }, ${r3(z.start + dur)});`);
      // punch-in no apresentador quando o callout estoura em tela cheia (sem B-roll)
      if (!overBroll(z.start, z.start)) {
        volTweens.push(`tl.to("#presenter-wrap", { scale: 1.07, duration: 0.18, ease: "power3.out" }, ${z.start});`);
        volTweens.push(`tl.to("#presenter-wrap", { scale: 1, duration: 0.45, ease: "power2.inOut" }, ${r3(z.start + 0.2)});`);
      }
    }
    bigId++;
  }
});

// ---- light-leaks + whoosh nas transições de cena ----
// Pontos de transição: cortes de seção (plan.sections) + entradas e saídas de cada cena de
// B-roll. Cada um leva um light-leak (0,7 s, começando 10f antes) e um one-shot de whoosh /
// swoosh / whoosh-transition alternados. Espaçamento mínimo `leakMinGap` para não virar
// cama rítmica sobre a fala (regra de ouro do mix).
const LEAK_MIN_GAP = plan.leakMinGap ?? 2.4;
const pontos = [];
plan.sections.forEach(sec => pontos.push({ t: segs[sec.afterSegment].tEnd, nome: sec.name }));
groups.forEach(g => {
  pontos.push({ t: g.t0, nome: `entra ${g.file.split('/').pop()}` });
  // cortes DENTRO da cena concatenada também levam transição (sem isso o trecho lia como
  // "um B-roll só, sem nada" — reclamação real do usuário no trecho 42-56 s)
  let t = g.t0;
  g.shots.slice(0, -1).forEach(sh => { t = r3(t + sh.dur); pontos.push({ t, nome: `corte ${sh.file.split('/').pop()}` }); });
  pontos.push({ t: g.t1, nome: `sai ${g.file.split('/').pop()}` });
});
const trans = [];
pontos.sort((x, y) => x.t - y.t).forEach(p => {
  if (p.t < 0.5 || p.t > TOTAL - 0.4) return;
  const last = trans[trans.length - 1];
  if (last && p.t - last.t < LEAK_MIN_GAP) return;
  trans.push(p);
});
const leaks = [], leakTimes = [], sfxEvents = [...typingSfx];
trans.forEach((p, k) => {
  const start = r3(Math.max(0, p.t - LEAK_PRE));
  leakTimes.push({ start, nome: p.nome });
  if (!plan.bakedLeaks) leaks.push(`    <video id="leak${k}" class="clip leak" src="assets/transicao-light-leak.mp4" data-start="${start}" data-duration="${LEAK_DUR}" data-track-index="4" muted playsinline preload="auto"></video> <!-- ${p.nome} @${r3(p.t)}s -->`);
  const pick = [['whoosh', 1.2], ['swoosh', 0.98], ['whoosh-transition', 2.1]][k % 3];
  sfxEvents.push({ file: `assets/sfx/${pick[0]}.mp3`, start, dur: pick[1], vol: 0.18, nome: p.nome });
});

if (plan.bakedLeaks) leaks.push(`    <video id="leaks" class="clip leak" src="assets/leaks.mp4" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="4" muted playsinline preload="auto"></video> <!-- ${leakTimes.length} light-leaks (gerada por scripts/bake.py leaks) -->`);
fs.writeFileSync(path.join(ROOT, 'work/leaks.json'), JSON.stringify({ total: TOTAL, dur: LEAK_DUR, file: 'assets/transicao-light-leak.mp4', leaks: leakTimes }, null, 1));

// ---- SFX fixos (todos vão para a faixa pronta assets/bed.m4a) ----
const climaxSec = plan.sections.find(s => /cl[ií]max/i.test(s.name));
const climaxT = climaxSec ? segs[climaxSec.afterSegment].tEnd : null;
sfxEvents.push({ file: 'assets/sfx/intro-cinematic-opening.mp3', start: 0, dur: 3.2, vol: 0.25, nome: 'intro opening' });
sfxEvents.push({ file: 'assets/sfx/intro-when-emphasizing-riser.mp3', start: 0, dur: 3.2, vol: 0.22, nome: 'intro riser' });
sfxEvents.push({ file: 'assets/sfx/boom-cinematic.mp3', start: 4.8, dur: 4, vol: 0.12, nome: 'boom' });
// reel SUN TZU: o callout de digitacao caiu em 7,7 s — dois drum-fills sobrepostos embolam; o da digitacao fecha a intro sozinho
if (!typingSfx.some(e => e.start > 5.5 && e.start < 9.5))
  sfxEvents.push({ file: 'assets/sfx/drum-fill.m4a', start: 7.0, dur: 1.43, vol: 0.166, nome: 'drum-fill da intro' });
if (climaxT != null) {
  sfxEvents.push({ file: 'assets/sfx/riser.mp3', start: r3(Math.max(0, climaxT - 3)), dur: 3, vol: 0.2, nome: 'riser do clímax' });
  sfxEvents.push({ file: 'assets/sfx/impact-hit.mp3', start: climaxT, dur: 2.5, vol: 0.3, nome: 'impact do clímax' });
}

// ---- trilha + bed ----
// trilhaLoop: quando o reel é mais longo que a trilha (164 s), a 2ª cópia entra em `at` recuada
// `back` s (nº inteiro de compassos: batida em fase), com crossfade `xfade`.
// A trilha e todos os SFX são renderizados OFFLINE em assets/bed.m4a (scripts/mixaudio.py):
// um elemento <audio> em vez de ~20 (limite de players do Chrome).
const TRILHA_VOL = plan.trilhaVol ?? 0.079;
const loop = plan.trilhaLoop && TOTAL > plan.trilhaLoop.at ? plan.trilhaLoop : null;
const trilhaMix = { file: 'assets/trilha-epic-cinematic-corporate.mp3', vol: TRILHA_VOL, loop, fadeLow: 0.045, lowAt: r3(Math.max((loop ? loop.at : 0) + 3, TOTAL - 9)), endFade: 0.7 };
const trilha = `    <audio id="bed" src="assets/bed.m4a" data-start="0" data-duration="${TOTAL}" data-media-start="0" data-track-index="17"></audio> <!-- trilha + ${sfxEvents.length} SFX (gerada por scripts/mixaudio.py) -->`;
fs.writeFileSync(path.join(ROOT, 'work/mix-plan.json'), JSON.stringify({
  total: TOTAL, fps: FPS, rate: RATE, voiceSrc: plan.voiceSrc || plan.src,
  voice: mixVoice, sfx: sfxEvents.sort((x, y) => x.start - y.start), trilha: trilhaMix,
}, null, 1));

const block = [
  `    <!-- EDIT:BEGIN (gerado por scripts/build-edit.mjs — não editar à mão) -->`,
  `    <!-- Duração total: ${TOTAL}s (${Math.round(TOTAL * FPS)} frames @${FPS}fps) · rate ${RATE}x -->`,
  `    <div id="presenter-wrap"><div id="presenter-zoom">`,
  presenterClips,
  `    </div></div>`,
  `    <!-- Voz independente com J-cut (lead ${LEAD_FRAMES}f) + crossfade ${XFADE_FRAMES}f -->`,
  voiceClips,
  `    <!-- B-rolls -->`,
  ...brollClips,
  ...(plan.mg ? [`    <!-- Motion graphics (sub-composição ${plan.mg.src}, skill showreel-interface): por cima do apresentador e do B-roll, abaixo dos light-leaks e das legendas -->`,
    `    <div id="mg-host" data-composition-id="${plan.mg.id}" data-composition-src="${plan.mg.src}" data-start="0" data-duration="${TOTAL}" data-track-index="8" data-width="1080" data-height="1920" style="position:absolute;left:0;top:0;width:1080px;height:1920px;z-index:30"></div>`] : []),
  `    <!-- Legendas -->`,
  ...capDivs,
  ...bigDivs,
  `    <!-- Transições light-leak -->`,
  ...leaks,
  `    <!-- Trilha + SFX (faixa pronta) -->`,
  trilha,
  `    <!-- EDIT:END -->`,
].join('\n');

const idx = path.join(ROOT, 'index.html');
let html = fs.readFileSync(idx, 'utf8');
html = html.replace(/ {4}<!-- EDIT:BEGIN[\s\S]*?<!-- EDIT:END -->/, block);
const jsBlock = [`      // EDIT-TWEENS:BEGIN (gerado — crossfades, splits, callouts, trilha)`, ...volTweens.map(l => `      ${l}`), `      // EDIT-TWEENS:END`].join('\n');
html = html.replace(/ {6}\/\/ EDIT-TWEENS:BEGIN[\s\S]*?\/\/ EDIT-TWEENS:END/, jsBlock);
html = html.replace(/(id="root"[^>]*data-duration=")[^"]*(")/, `$1${TOTAL}$2`);
fs.writeFileSync(idx, html);

// ---- passes de camada para o pacote conformável (NLE) ----
// Mesma composição, com uma classe no <html> que liga/desliga camadas via CSS.
// Deterministas: nenhum estado de runtime, só o seletor muda.
// OPT-IN (`--passes`): na raiz eles contam como composições-raiz duplicadas e o
// `hyperframes check` reprova. Gerar só na hora do export e apagar depois.
const PASSES = process.argv.includes('--passes');
for (const layer of PASSES ? ['clean', 'gfx', 'leaks'] : []) {
  const passHtml = html.replace(/<html\b([^>]*)>/, (m, attrs) =>
    /class="/.test(attrs)
      ? `<html${attrs.replace(/class="([^"]*)"/, `class="$1 layers-${layer}"`)}>`
      : `<html${attrs} class="layers-${layer}">`);
  fs.writeFileSync(path.join(ROOT, `pass-${layer}.html`), passHtml);
}

if (PASSES) console.log('passes de camada: pass-clean.html, pass-gfx.html, pass-leaks.html');
console.log(`OK: ${segs.length} segs, ${TOTAL}s, ${brollClips.length} cenas de broll (${shots.length} tomadas), ${sfxEvents.length} sfx, ${capId} legendas, ${bigId} callouts, ${leakTimes.length} leaks, J-cut ${LEAD_FRAMES}f/${XFADE_FRAMES}f.`);
