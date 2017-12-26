import socket
import re
pattern='^\r(.*)';string=''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
##mysock.connect(('www..com', 80))
mysock.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    string+=data.decode('utf-8','ignore')
mysock.close()
match=re.search('\r\n\r\n',string)
pos=match.end()
print(string[pos:len(string)-1])

