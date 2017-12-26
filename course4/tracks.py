#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:13:46 2017
@author: harsh
"""
import sqlite3
import xml.etree.ElementTree as ET

con=sqlite3.connect('trackdb.sqlite')
cur=con.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
              
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

fname=input('Enter file:')
if len(fname)<1: fname='Library.xml'
stuff=ET.parse('Library.xml')
all_songs=stuff.findall('dict/dict/dict')
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True    
    return None
for entry in all_songs:
    if(lookup(entry,'Track ID')) is None :
        continue
    
    name= lookup(entry, 'Name')
    artist=lookup(entry, 'Artist')
    album=lookup(entry, 'Album')
    genre= lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    if name is None or artist is None or album is None or genre is None: 
        continue


    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES(?)''',(artist,))
    cur.execute('''SELECT id from Artist where name=?''',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ?)''', ( genre, ) )
    cur.execute('SELECT id FROM genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? ,?)''', 
        ( name, album_id, genre_id, length, rating, count ) )

    con.commit()