#Although it looks like it's tough a lot this script is easy an updates a cities population efficiently


import sqlite3 

conn = sqlite3.connect("new.db")

with conn as connection :
	c = connection.cursor()
	
	#Changes and SETS the population to a specified unit WHERE the city is declared
	c.execute("UPDATE population SET population = 9000000 WHERE city= 'New York City'")

	#executes the above feild and deletes the original name
	c.execute("DELETE FROM population WHERE city='Boston'")

	print ("\nNew Date:\n")

	# Selects the appropiate field and displays results
	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for r in rows:
		print (r[0], r[1], r[2])

#For extra scripts, refer to Homework on page 72