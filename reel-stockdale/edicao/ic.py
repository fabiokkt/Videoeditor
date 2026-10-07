import json,sys,urllib.request,urllib.parse
def post(url,b):
    r=urllib.request.Request(url,data=json.dumps(b).encode(),headers={"Content-Type":"text/plain"})
    return json.load(urllib.request.urlopen(r))
guid,out=sys.argv[1],sys.argv[2]
res=post("https://ckdatabasews.icloud.com/database/1/com.apple.photos.cloud/production/public/records/resolve",{"shortGUIDs":[{"value":guid}]})["results"][0]
a=res["anonymousPublicAccess"]; z=res["zoneID"]
print("root:",{k:v["value"] for k,v in res["rootRecord"]["fields"].items() if not isinstance(v["value"],dict)})
url=a["databasePartition"]+"/database/1/com.apple.photos.cloud/production/"+res["databaseScope"].lower()+"/records/query?remapEnums=true&getCurrentSyncToken=true&publicAccessAuthToken="+urllib.parse.quote(a["token"])
q=post(url,{"query":{"recordType":"CPLAssetAndMasterByAssetDateWithoutHiddenOrDeleted","filterBy":[{"fieldName":"startRank","fieldValue":{"type":"INT64","value":0},"comparator":"EQUALS"},{"fieldName":"direction","fieldValue":{"type":"STRING","value":"ASCENDING"},"comparator":"EQUALS"}]},"zoneID":z,"resultsLimit":20})
for r in q["records"]:
    f=r["fields"]
    print(r["recordType"], [(k,v["value"].get("size")) for k,v in f.items() if isinstance(v.get("value"),dict) and "downloadURL" in v["value"]])
    for k in ("resOriginalRes",):
        if k in f and f[k]["value"].get("downloadURL"):
            u=f[k]["value"]["downloadURL"].replace("${f}","video.mov")
            urllib.request.urlretrieve(u,out); print("saved",out); sys.exit(0)
