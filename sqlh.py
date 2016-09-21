#This script joind together two databases in the "SELECT" command

import sqlite3 

conn = sqlite3.connect("new.db")


with conn as connection :
	c = connection.cursor()

	c.execute("""SELECT population.city, population.population,
		regions.region FROM population, regions
		WHERE population.city = regions.city""")

	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1], r[2])
