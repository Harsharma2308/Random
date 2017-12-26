# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
##input=fh.read()
##print(input.upper())
##fh.seek(0)
for line in fh:
        print((line.rstrip()).upper())
fh.close()
