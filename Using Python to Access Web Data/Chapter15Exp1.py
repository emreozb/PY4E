import sqlite3

# Creating and connecting to database
conn = sqlite3.connect('Chapter15_org.sqlite')
cur = conn.cursor()


# Do some setup (Creating the table)
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Asking the user to input text file name (mbox.txt) 
fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'

# Opening and reading the file and putting it into a text object
fh = open(fname)
for line in fh:
    # Skipping the irrelevant lines

    if not line.startswith('From: '):
        continue

    # Splitting the lines, taking the split with the e-mail, then splitting the e-mail to get the domain
    pieces = line.split('@')
    domain_name = pieces[1]

    # Getting the current count value from the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain_name,))
    row = cur.fetchone()

    # If the e-mail is not yet in the database, then adding it
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain_name,))

    # Otherwise updating the count value in the database
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain_name,))

# Committing the changes to the database
conn.commit()

# https://www.sqlite.org/lang_select.html
# Showing the results from a query
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
