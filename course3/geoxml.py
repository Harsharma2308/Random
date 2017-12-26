import xml.etree.ElementTree as ET
import urllib.request
serviceurl='http://python-data.dr-chuck.net/comments_353468.xml'
uh= urllib.request.urlopen(serviceurl)
data=uh.read().decode("utf-8")
try: tree=ET.fromstring(data)
except:
    print("Failure to retrieve")
#print(ET.dump(xml_object))
lst=tree.findall('comments/comment')
sum=0;
for item in lst:
    sum+= int(item.find('count').text)
print(sum)
