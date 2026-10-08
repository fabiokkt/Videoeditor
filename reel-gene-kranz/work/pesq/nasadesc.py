import json,sys,urllib.request,urllib.parse
for i in sys.argv[1:]:
    u="https://images-api.nasa.gov/search?nasa_id="+urllib.parse.quote(i)
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30))
    for x in d["collection"]["items"][:1]:
        m=x["data"][0]; print("==",i,m.get("date_created","")[:10],m["title"]); print((m.get("description","") or "")[:900]); print()
