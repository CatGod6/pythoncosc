# In this file we add on some functionality to try the blocked code and except any error.


import sqlite3 

conn = sqlite3.connect("new.db")

try:
	with conn as connection :
		c = connection.cursor()
		cities = [
		('Boston', 'MA', 600000),
		('Chicago', 'IL', 2700000),
		('Houston', 'TX', 2100000),
		('Dallas', 'TX', 4200000)
		]
		c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

except sqlite3.OperationError:
	print ("Oops! Something went wrong. Try again...")

#Close the database connection
conn.close()