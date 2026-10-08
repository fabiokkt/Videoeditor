# busca na NASA Image and Video Library (images-api.nasa.gov, dominio publico) -> lista nasa_id | data | titulo | descricao curta
import json,sys,urllib.request,urllib.parse
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 40
extra=sys.argv[3] if len(sys.argv)>3 else ""
u="https://images-api.nasa.gov/search?media_type=image&q="+urllib.parse.quote(q)+extra
d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
it=d["collection"]["items"]; print("#",q,"hits",d["collection"]["metadata"]["total_hits"])
for x in it[:n]:
    m=x["data"][0]
    print(m["nasa_id"],"|",m.get("date_created","")[:10],"|",m["title"][:70],"|",(m.get("description","") or "")[:230].replace("\n"," "))
