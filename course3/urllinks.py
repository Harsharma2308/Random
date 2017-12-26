from urllib.request import urlopen
from bs4 import BeautifulSoup
url= input('Enter URL: ')  #http://python-data.dr-chuck.net/known_by_Ayah.html
num= int(input('Enter count: '))  #7
pos= int(input('Enter position: '))#18
for i in range(num):
    try:
        html = urlopen(url).read()
    except:
        print('Sorry bro!, there is nothing like that on the web!')
        exit()	
    soup = BeautifulSoup(html.decode("utf-8",'ignore'),"lxml")
    tags = soup('a')
    url=tags[pos-1].get('href', None)
    print('Retrieving: {0}'.format(url))
    #print(tags[pos-1].contents[0])
print(tags[pos-1].contents[0])
