import sqlite3
con = sqlite3.connect('Jernbane.db')

cursor = con.cursor()
cursor.execute("SELECT * FROM Jernbanestasjon")
rows = cursor.fetchall()
print(rows)

con.close()