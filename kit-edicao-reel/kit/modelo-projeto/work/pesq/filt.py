import sys,json
bad=("shutterstock","getty","alamy","istock","dreamstime","123rf","depositphotos","vecteezy","freepik","pinterest","pinimg","stock.adobe","agefotostock","bigstock","canstock","superstock","pond5","megapixl","masterfile","lookandlearn","bridgeman","artstation","lovepik","pngtree","gettyimages","westend61","stockcake")
for l in sys.stdin:
  x=json.loads(l)
  w,h=x.get("w") or 0,x.get("h") or 0
  if min(w,h)<900: continue
  if any(b in (x["dom"]+x["img"]).lower() for b in bad): continue
  print(x["i"], "%dx%d"%(w,h), x["dom"], "|", x["title"][:60], "|", x["img"], "|", x["page"])
