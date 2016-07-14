import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
cur.executescript(""" DROP TABLE IF EXISTS Pets
					CREATE TABLE Pets (Id INT , Name TEXT , Price INT);
					INSERT INTO Pets VALUES(1,'CAT',400);
					INSERT INTO Pets VALUES(2,'DOG',500);""")
pets = ((3,'rappit',200),
		(4,'goat',500),
		(5,'bird',100))

cur.executemany	("INSERT INTO Pets VALUES(?,?,?)",pets)
con.commit()

cur.execute("SELECT * FROM Pets")

data = cur.fetchall()

for row in data : 
	print row 
