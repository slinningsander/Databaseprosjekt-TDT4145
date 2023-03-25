import sqlite3
con = sqlite3.connect('Jernbane.db')
cursor = con.cursor()

cursor.execute("""INSERT INTO Billett VALUES (3, 3, NULL, 1, 1, "Mo i Rana", "Bodø", "Dagtog fra Trondheim til Bodø", "03/04/23")""")

con.commit()

cursor.execute("""SELECT * FROM 'Billett'""")

print(cursor.fetchall())
con.close()