fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = {};lst=[]
for line in fh:
    if not line.startswith('From '): continue
    words=line.split()
    hour=words[5][0:2]
    count[hour]=count.get(hour,0)+1

for k,v in count.items():
    lst.append((k,v))
lst.sort()
for item in lst:
    print(item[0],item[1])
