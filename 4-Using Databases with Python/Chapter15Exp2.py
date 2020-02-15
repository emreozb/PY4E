import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    genre_name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    album_title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    track_title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Asking the user to input XML file name (Library.xml) 
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'


# The structure of the XML object is the following:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>


# Defining a function to lookup the value of a 'key' tag
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Opening and parsing the file
stuff = ET.parse(fname)

# Selecting the 'dict' tags in the third depth and counting them
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# Looping through all result elements 'dict'
for entry in all:
   
    # Trying to look up the different data fields. If not found, moving on to the next element
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # If a data field is not found, then move on to the next element
    if name is None or artist is None or genre is None or album is None : 
        continue

    # Printing the data field of the search result element for the user
    print(name, artist, genre, album, count, rating, length)

    # Inserting and updating the relevant tables with the data field of the search result element
    cur.execute('''INSERT OR IGNORE INTO Artist (artist_name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE artist_name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (genre_name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE genre_name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (album_title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE album_title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (track_title, genre_id, album_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, genre_id, album_id, length, rating, count ) )
    
    # Committing the changes
    conn.commit()