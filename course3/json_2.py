import json
import urllib.request
url='http://python-data.dr-chuck.net/comments_353472.json'
uh=urllib.request.urlopen(url)
data=uh.read().decode("utf-8")
js=json.loads(data)

sum=0;
for item in js["comments"]:
    sum+=item["count"]
print(sum)
