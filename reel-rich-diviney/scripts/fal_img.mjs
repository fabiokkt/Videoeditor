#!/usr/bin/env node
// Gera UMA imagem-conceito no fal.ai (so quando o Fabio pede uma imagem encenada — ex.: capa do reel).
// Uso: node scripts/fal_img.mjs <modelo> <saida.jpg> <aspect> "<prompt>"
import fs from 'node:fs';
const env = Object.fromEntries(fs.readFileSync(process.env.REEL_ENV || `${process.env.HOME}/Claude/reel-auto/.env`, 'utf8').split('\n').filter(l => l.includes('=')).map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim()]));
const [model, out, aspect, prompt] = process.argv.slice(2);
const H = { Authorization: `Key ${env.FAL_KEY}`, 'Content-Type': 'application/json' };
const body = model.includes('flux') ? { prompt, aspect_ratio: aspect, raw: true, output_format: 'jpeg', safety_tolerance: '5' }
  : { prompt, aspect_ratio: aspect, num_images: 1, output_format: 'jpeg', resolution: '2K' };
const sub = await (await fetch(`https://queue.fal.run/${model}`, { method: 'POST', headers: H, body: JSON.stringify(body) })).json();
if (!sub.status_url) { console.error(JSON.stringify(sub)); process.exit(1); }
for (let i = 0; i < 120; i++) {
  await new Promise(r => setTimeout(r, 3000));
  const st = await (await fetch(sub.status_url, { headers: H })).json();
  if (st.status === 'COMPLETED') break;
  if (st.status && !['IN_QUEUE', 'IN_PROGRESS'].includes(st.status)) { console.error(JSON.stringify(st)); process.exit(1); }
}
const res = await (await fetch(sub.response_url, { headers: H })).json();
const url = res.images?.[0]?.url; if (!url) { console.error(JSON.stringify(res).slice(0, 500)); process.exit(1); }
fs.writeFileSync(out, Buffer.from(await (await fetch(url)).arrayBuffer()));
console.log(out, res.images[0].width, res.images[0].height);
