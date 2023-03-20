import sqlite3
con = sqlite3.connect('Jernbane.db')
cursor = con.cursor()

cursor.execute("""INSERT INTO 'Kjøres på' VALUES('Morgentog fra Mo i Rana til Trondheim', 'Nordlandsbanen', 8)""")

con.commit()

cursor.execute("""SELECT * FROM 'Kjøres på'""")

print(cursor.fetchall())
con.close()