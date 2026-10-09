// uso: node work/mg/teste/shoot.mjs saida.jpg t1,t2,...   (servidor http na raiz do projeto, porta 8766)
import { createRequire } from 'module'; const { chromium } = createRequire('/opt/node22/lib/node_modules/')('playwright');
import { execFileSync } from 'child_process';
const [out, ts] = process.argv.slice(2); const T = ts.split(',').map(Number);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--ignore-certificate-errors'] });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
p.on('pageerror', e => console.log('ERRO', e.message));
await p.goto('http://127.0.0.1:8766/work/mg/teste/harness.html'); await p.evaluate(() => window.__ready);
const files = [];
for (const t of T) { await p.evaluate(t => window.seek(t), t); await p.waitForTimeout(60); const f = `/tmp/mgshot_${t}.png`; await p.screenshot({ path: f }); files.push(f); }
await b.close();
const py = `
import sys
from PIL import Image, ImageDraw
fs=sys.argv[2:]; W=360; H=640; cols=min(6,len(fs)); rows=(len(fs)+cols-1)//cols
S=Image.new('RGB',(cols*W,rows*(H+30)),(15,15,15)); d=ImageDraw.Draw(S)
for k,f in enumerate(fs):
    im=Image.open(f).convert('RGB').resize((W,H)); x=(k%cols)*W; y=(k//cols)*(H+30); S.paste(im,(x,y+30)); d.text((x+8,y+8),f.split('_')[-1][:-4]+' s',fill=(255,255,0))
S.save(sys.argv[1],quality=86)`;
execFileSync(process.env.HOME + '/Claude/.venv-reel/bin/python', ['-c', py, out, ...files]);
console.log(out);
