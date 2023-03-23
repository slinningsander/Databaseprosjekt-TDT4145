import sqlite3
con = sqlite3.connect('Jernbane.db')
cursor = con.cursor()

cursor.execute("""INSERT INTO 'Togruteforekomst' VALUES('Nattog fra Trondheim til Bodø', '04/04/23')""")

con.commit()

cursor.execute("""SELECT * FROM 'Togruteforekomst'""")

print(cursor.fetchall())
con.close()