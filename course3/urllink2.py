from urllib.request import urlopen
from bs4 import BeautifulSoup
url =  'http://python-data.dr-chuck.net/comments_353471.html' #input('Enter - ')
try:
    html = urlopen(url).read()
    soup = BeautifulSoup(html.decode('utf-8', 'ignore'),"lxml")
except: print('Sorry bro!')
    

# Retrieve all of the anchor tags
tags = soup('span')
sum_=0

try:
    for tag in tags:
        sum_+=int(tag.contents[0])
    print('Count: {0}\nSum: {1}'.format(len(tags),sum_))
except: print('No span tags with numeric values')
