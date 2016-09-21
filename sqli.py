#This script joind together two databases in the "SELECT" command

import sqlite3 

conn = sqlite3.connect("new.db")


with conn as connection :
	c = connection.cursor()

	c.execute("""SELECT DISTINCT population.city, 
		population.population,
		regions.region FROM population, regions
		WHERE population.city = regions.city ORDER by 
		population.city ASC""")

	rows = c.fetchall()

	for r in rows:
		print ("City: " + r[0])
		print ("population: : " + str(r[1]))
		print ("Region: " + r[2])
		print()