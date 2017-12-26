import sqlite3
conn=sqlite3.connect('testdb.sqlite')
cur=conn.cursor();
cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts(org text,count integer)''')
fh=open('mbox.txt')
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email=pieces[1]
    pos = email.find('@')
    org=email[pos+1:len(email)]
    cur.execute('SELECT count from counts where org=?',(org,))
    
    try:
        count=cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    except: cur.execute('''INSERT INTO counts (count,org) values (1,?)''',(org,))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])
cur.close()

    
