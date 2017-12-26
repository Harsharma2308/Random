fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = {};lst=[]
for line in fh:
    if not line.startswith('From:'): continue
    words=line.split()
    count[words[1]]=count.get(words[1],0)+1
for k,v in count.items():
    lst.append((v,k))
lst.sort(reverse=True)
print(lst[0][1],lst[0][0])
##cwen@iupui.edu 5
