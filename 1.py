import json

file=open('saveFile.txt','r')
js=file.read()
dic=json.loads(js)
print(dic)
file.close()

js=json.dumps(dic)
file=open('saveFile.txt','w+')
file.write(js)
file.close()


