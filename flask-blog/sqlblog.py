import sqlite3

with sqlite3.connect("blog.db") as connection :
	c = connection.cursor()

	c.execute("""CREATE TABLE post
		(title TEXT, post TEXT)"""
		)

	c.execute('INSERT INTO post VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO post VALUES("Well", "I\'m well.")')
	c.execute('INSERT INTO post VALUES("Excellent", "I\'m Excellent.")')
	c.execute('INSERT INTO post VALUES("Okay", "I\'m Okay.")')