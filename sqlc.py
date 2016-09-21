#This is the most efficient way to put in values into a database!


import sqlite3 

conn = sqlite3.connect("new.db")

with conn as connection :
	c = connection.cursor()
	cities = [
	('Boston', 'MA', 600000),
	('Chicago', 'IL', 2700000),
	('Houston', 'TX', 2100000),
	]

	c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)