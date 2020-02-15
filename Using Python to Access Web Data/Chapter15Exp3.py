import json
import sqlite3


# Creating and connecting to database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup (Creating the tables)
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Asking the user to input Json file name (roster_data.json) 
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# The structure of the Json object is the following:
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# Opening and reading the file and putting it into a Json object
str_data = open(fname).read()
json_data = json.loads(str_data)

# Looping through the Json object
for entry in json_data:

    # Looking up the different data fields
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Printing the data field of the search result Json object for the user
    print((name, title, role))

    # Inserting and updating the relevant tables with the data field of the search result Json object
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role) )

    # Committing the changes
    conn.commit()

# Showing the results from a query
sqlstr = '''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1''' # Modified the original query so that only first result shown 

for row in cur.execute(sqlstr):
    print(str(row[0]))

#close cursor
cur.close()
