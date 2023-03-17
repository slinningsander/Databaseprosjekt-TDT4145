import sqlite3

def getTogruter(stasjon, ukedag):
    con = sqlite3.connect('Jernbane.db')
    cursor = con.cursor()
    cursor.execute(
        """SELECT DagerTogruterKjører.RuteID FROM DagerTogruterKjører 
        INNER JOIN 'Stasjon på rute' ON DagerTogruterKjører.RuteID = 'Stasjon på rute'.RuteID 
        WHERE Ukedag =:dag AND JernbanestasjonNavn =:navn""",
        {"dag": ukedag, "navn": stasjon}
        )
    
    togruter = cursor.fetchall()
    


    con.close()
    print(togruter)

