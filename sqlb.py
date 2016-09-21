#add data to the existing database!

#import the sqlite3 library
import sqlite3

#create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

#insert data!
cursor.execute("INSERT INTO population VALUES('New York City', \
	'NY', 8200000)")

cursor.execute("INSERT INTO population VALUES('San Francisco', \
	'CA', 800000)")

conn.commit()

conn.close()