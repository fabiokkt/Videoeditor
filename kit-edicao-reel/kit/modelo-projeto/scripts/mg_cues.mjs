#!/usr/bin/env node
// MOTOR (kit v3). Le compositions/mg.html e devolve os cues de SFX que os componentes registraram com cue()
// (window.__mgCues), SEM navegador: roda o <script> da camada num vm com um gsap de mentira.
// Saida: work/mg-cues-auto.json (lido pelo scripts/mg_sfx.py).   uso: node scripts/mg_cues.mjs
import fs from 'node:fs';
import vm from 'node:vm';
const html = fs.readFileSync('compositions/mg.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
if (!scripts.length) throw new Error('compositions/mg.html sem <script>');
const nada = new Proxy(function () {}, { get: (t, k) => (k === Symbol.toPrimitive ? () => 0 : nada), apply: () => nada });
const gsap = { timeline: () => nada, set: () => nada, to: () => nada, fromTo: () => nada, from: () => nada, registerPlugin: () => {} };
const window = { __timelines: {} };
vm.runInNewContext(scripts.join('\n'), { window, gsap, Math, console, document: nada });
const cues = (window.__mgCues || []).sort((a, b) => a.t - b.t);
fs.mkdirSync('work', { recursive: true });
fs.writeFileSync('work/mg-cues-auto.json', JSON.stringify(cues, null, 0));
const cont = cues.reduce((m, c) => ((m[c.som] = (m[c.som] || 0) + 1), m), {});
console.log(`${cues.length} cues da camada de motion -> work/mg-cues-auto.json`, JSON.stringify(cont));
