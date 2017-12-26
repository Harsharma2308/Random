import json
import urllib.request,urllib.parse

while True:
    address=input('Enter location -  ')
    if len(address) < 1 : break 

    serviceurl='http://python-data.dr-chuck.net/geojson?'
    url=serviceurl+urllib.parse.urlencode({'sensor':'false','address':address})

    uh=urllib.request.urlopen(url)
    data=uh.read().decode("utf-8")


    try: js=json.loads(data)
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        continue

    #print(json.dumps(js,indent=4))
    print(js['results'][0]['place_id'])
    
    
