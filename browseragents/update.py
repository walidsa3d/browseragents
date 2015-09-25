import json

with open('useragentdata.json', 'r+') as f:
    j = json.loads(f.read())
    unwanted = ["appName", "appVersion", "platform"]
    for k in j:
        for u in unwanted:
            if u in k:
                del k[u]
    print j[0]

f = open('useragentdata.json','w')
f.write(json.dumps(j))
