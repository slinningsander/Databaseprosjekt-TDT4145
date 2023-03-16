import sqlite3
con = sqlite3.connect('Jernbane.db')

cursor = con.cursor()
cursor.execute("SELECT * FROM Jernbanestasjon")
rows = cursor.fetchall()
print(rows)


cursor.execute("SELECT * FROM 'Stasjon på rute'")
rows2 = cursor.fetchall()
print(rows2)



con.close()