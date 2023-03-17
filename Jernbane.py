import sqlite3

# Funksjon for brukerhistorie c)
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


print("Hei! Velkommen til vårt Jernaneprogram")

svar = input("Hva vil du gjøre? \n Skriv 'finn stasjon' for å få alle togruter som går på den oppgitte stasjonen på den oppgitte dagen.")

if svar == "finn stasjon":
    stasjon = input("Hvilken stasjon vil du finne?")
    dag = input("Hvilken dag vil du finne?")
    print("Her er alle togruter som går på stasjonen", stasjon, "på", dag)
    getTogruter(stasjon, dag)