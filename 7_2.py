# Use the file name mbox-short.txt as the file name
import os
os.chdir(os.getcwd()+'/course2')
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count+=1
    words=line.split()
    total+= float(words[1])
print(('Average spam confidence: {0}').format(round(total/count,12)))
fh.close()
