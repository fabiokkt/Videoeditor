#!/usr/bin/env node
// Sincronia A/V por dados. Para cada take, compara o envelope de energia do ÁUDIO DO MP4 FINAL
// com o áudio do bruto no instante de source que o VÍDEO do apresentador mostra naquele ponto.
// lag ≈ 0 ms => boca e voz alinhadas.  uso: node scripts/sync-check.mjs <final16k.wav> <bruto16k.wav>
import fs from 'node:fs';
const plan = JSON.parse(fs.readFileSync('assets/edit-plan.json', 'utf8'));
const RATE = plan.rate || 1, FPS = plan.fps || 30, F = n => n / FPS;
const LEAD = F(plan.jcutLeadFrames ?? 5);
const r3 = x => Math.round(x * 1000) / 1000;
let t = 0; const segs = plan.segments.map((s, i) => {
  const sd = r3((s.out - s.in) / RATE); const lead = i === 0 ? 0 : Math.min(LEAD, sd - F(10));
  const d = r3(sd - lead); const o = { i, in: s.in, lead, tStart: r3(t), dur: d }; t = r3(t + d); return o;
});
const early = segs.map(s => (plan.segments[s.i].videoTail ? r3((plan.segments[s.i].out - plan.segments[s.i].videoTail) / RATE) : 0));
segs.forEach(s => { const dPrev = s.i > 0 ? early[s.i - 1] : 0; s.vStart = r3(s.tStart - dPrev); s.vMedia = r3(s.in + (s.lead - dPrev) * RATE); });
const rd = f => fs.readFileSync(f);
const A = rd(process.argv[2]), S = rd(process.argv[3]), SR = 16000, W = 160;
const env = (b, t0, secs, speed = 1) => { const o = []; for (let k = 0; k < secs * 100; k++) { const off = Math.round((t0 + k * 0.01 * speed) * SR); let s = 0; for (let i = 0; i < W; i++) { const j = 44 + 2 * (off + i); if (j + 1 < b.length && j >= 44) { const v = b.readInt16LE(j) / 32768; s += v * v; } } o.push(Math.sqrt(s / W)); } return o; };
const corr = (a, b) => { const ma = a.reduce((x, y) => x + y, 0) / a.length, mb = b.reduce((x, y) => x + y, 0) / b.length; let n = 0, da = 0, db = 0; for (let i = 0; i < a.length; i++) { n += (a[i] - ma) * (b[i] - mb); da += (a[i] - ma) ** 2; db += (b[i] - mb) ** 2; } return n / Math.sqrt(da * db + 1e-12); };
const rows = [];
for (const s of segs) {
  if (s.dur < 1.0) continue;
  const tt = r3(s.tStart + Math.min(1.2, s.dur * 0.4));
  const src = r3(s.vMedia + (tt - s.vStart) * RATE);
  const ref = env(S, src, 1.2, RATE);
  let best = { lag: 0, r: -1 };
  for (let lag = -15; lag <= 15; lag++) { const r = corr(ref, env(A, tt + lag * 0.01, 1.2)); if (r > best.r) best = { lag, r }; }
  rows.push({ i: s.i, t: tt, lagMs: best.lag * 10, r: +best.r.toFixed(2) });
}
console.log(rows.map(r => `  seg${String(r.i).padStart(2)}@${String(r.t).padStart(6)}s  lag ${String(r.lagMs).padStart(4)} ms  (r=${r.r})`).join('\n'));
const good = rows.filter(r => r.r > 0.6).map(r => r.lagMs).sort((a, b) => a - b);
console.log(`\n${good.length}/${rows.length} pontos com correlação > 0.6 · lag mediano ${good[good.length >> 1]} ms · faixa ${good[0]}..${good.at(-1)} ms (1 quadro = 33 ms)`);
