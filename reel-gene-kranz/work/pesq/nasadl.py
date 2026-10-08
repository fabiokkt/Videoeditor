# baixa da NASA Image Library (dominio publico) a versao ~large (ou ~orig se large faltar) -> nasa/<id>.jpg + licencas.tsv
import json,sys,os,urllib.request,urllib.parse,time
os.makedirs("nasa",exist_ok=True)
H={"User-Agent":"Mozilla/5.0"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=60)
for i in sys.argv[1:]:
    out=f"nasa/{i}.jpg"
    if os.path.exists(out): print("ja",i); continue
    try:
        man=json.load(get("https://images-api.nasa.gov/asset/"+urllib.parse.quote(i)))
        hrefs=[x["href"] for x in man["collection"]["items"]]
        pick=None
        for suf in ("~orig.jpg","~large.jpg","~orig.tif","~medium.jpg"):
            c=[h for h in hrefs if h.lower().endswith(suf)]
            if c: pick=c[0]; break
        pick=pick.replace("http://","https://").replace(" ","%20")
        data=get(pick).read(); open(out,"wb").write(data)
        meta=json.load(get("https://images-api.nasa.gov/search?nasa_id="+urllib.parse.quote(i)))["collection"]["items"][0]["data"][0]
        with open("licencas.tsv","a") as f: f.write(f"{i}\t{meta.get('date_created','')[:10]}\t{meta['title']}\tNASA (dominio publico)\t{pick}\n")
        print("ok",i,len(data)//1024,"KB",pick.rsplit('/',1)[-1])
    except Exception as e: print("ERRO",i,e)
