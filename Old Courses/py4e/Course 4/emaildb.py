import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    email.strip()
    #print('email is',email)
    email = email.split('@')                            #YAHA PAR KAAM KIYA HAI, JO LAST ME LINES 34 AUR SAB COMMENTS ME HAI WOHI LOGIC HAI
    email = email[1]
    org = email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

cur.execute('SELECT * FROM Counts ORDER BY count')


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

#lst = list()

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
#    rr = lst.append(str(row[0]))

#print(lst)
#for word in lst :
#    word = word.split('@')
#    print(word[1])


cur.close()
