#!/usr/bin/env node
// Busca no Google Imagens (Serper /images, chave em ~/Claude/reel-auto/.env, ou no arquivo apontado por $REEL_ENV) — imprime os resultados
// com tamanho, dominio e links. Uso: node scripts/gimg.mjs "consulta" [n=20]   (filtro de tamanho grande: tbs=isz:l)
import fs from 'node:fs';
const env = Object.fromEntries(fs.readFileSync(process.env.REEL_ENV || `${process.env.HOME}/Claude/reel-auto/.env`, 'utf8').split('\n').filter(l => l.includes('=')).map(l => [l.slice(0, l.indexOf('=')).trim(), l.slice(l.indexOf('=') + 1).trim()]));
const q = process.argv[2]; const n = +(process.argv[3] || 20);
const r = await fetch('https://google.serper.dev/images', { method: 'POST', headers: { 'X-API-KEY': env.SERPER_API_KEY, 'Content-Type': 'application/json' }, body: JSON.stringify({ q, num: n, tbs: 'isz:l' }) });
if (!r.ok) { console.error('serper', r.status, await r.text()); process.exit(1); }
const j = await r.json();
for (const [i, x] of (j.images || []).entries()) console.log(JSON.stringify({ i, w: x.imageWidth, h: x.imageHeight, dom: x.domain, title: x.title, img: x.imageUrl, page: x.link }));
