import sqlite3

with sqlite3.connect("test_database.db") as connection :
    c = connection.cursor()
    c.executescript(""" DROP TABLE IF EXISTS People;
                                 CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);""")
    people_values = (( "Catrell" , "Washington" , 18) ,
                           ( "Cameron" , "Pearson" , 22) ,
                           (" Christine" , "Williams" , 55))
    c.executemany("INSERT INTO People VALUES (? ,? ,?)" , people_values)
    for row in c.fetchall() :
        print(row)
