import sqlite3
con = sqlite3.connect('Jernbane.db')
cursor = con.cursor()
# Funksjon for brukerhistorie c)


def getTogruter(stasjon, ukedag):
    cursor.execute(
        """SELECT DagerTogruterKjører.RuteID FROM DagerTogruterKjører 
        INNER JOIN 'Stasjon på rute' ON DagerTogruterKjører.RuteID = 'Stasjon på rute'.RuteID 
        WHERE Ukedag =:dag AND JernbanestasjonNavn =:navn""",
        {"dag": ukedag, "navn": stasjon}
    )

    togruter = cursor.fetchall()

    print(togruter)

# Funksjon for brukerhistorie e)


def addKunde(navn, epost, telefon):
    con = sqlite3.connect('Jernbane.db')
    cursor = con.cursor()
    cursor.execute(
        """INSERT INTO Kunde (Navn, 'E-postadresse', Mobilnummer) VALUES (:navn, :epost, :telefon)""",
        {"navn": navn, "epost": epost, "telefon": telefon}
    )
    con.commit()


def finnRuter(startstasjon, endestasjon, ukedag, klokkeslett):
    datoer = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
    nesteDag = datoer[(datoer.index(ukedag)+1) % 7]
    cursor.execute(
        """SELECT DISTINCT * from Togrute
        INNER JOIN 'Kjøres på' using(RuteID)
        INNER JOIN Delstrekning ON ('Kjøres på'.Delstrekningsnummer = Delstrekning.Strekningsnummer)
        INNER JOIN DagerTogruterKjører Using (ruteid)
        WHERE (startstasjon =:startstasjon OR endestasjon =:endestasjon) AND (ukedag =:ukedag)
        GROUP by RuteID
        HAVING COUNT(ruteid) = 2""",
        {"startstasjon": startstasjon, "endestasjon": endestasjon,
        "ukedag": ukedag, "klokkeslett": klokkeslett}
    )
    print(cursor.fetchall())
    cursor.execute(
        """SELECT DISTINCT * from Togrute
        INNER JOIN 'Kjøres på' using(RuteID)
        INNER JOIN Delstrekning ON ('Kjøres på'.Delstrekningsnummer = Delstrekning.Strekningsnummer)
        INNER JOIN DagerTogruterKjører Using (ruteid)
        WHERE (startstasjon =:startstasjon OR endestasjon =:endestasjon) AND (ukedag =:ukedag)
        GROUP by RuteID
        HAVING COUNT(ruteid) = 2""",
        {"startstasjon": startstasjon, "endestasjon": endestasjon,
        "ukedag": nesteDag, "klokkeslett": klokkeslett}
    )
    print(cursor.fetchall())


print("Hei! Velkommen til vårt Jernaneprogram")

svar = ""

while svar != "avslutt":

    svar = input("""Hva vil du gjøre? 
            \n Skriv 'finn stasjon' for å få alle togruter som går på den oppgitte stasjonen på den oppgitte dagen.
            \n Skriv 'registrer bruker' for å registrere en ny bruker.
            \n Skriv 'finn rute' for å finne en togrute basert på en startstasjon og en sluttstasjon, med utgangspunkt i en dato og et klokkeslett. 
            \n Skriv 'avslutt' for å avslutte programmet.\n""")

    if svar == "finn stasjon":
        stasjon = input("Hvilken stasjon vil du finne? ")
        dag = input("Hvilken dag vil du finne? ")
        print("Her er alle togruter som går på stasjonen", stasjon, "på", dag)
        getTogruter(stasjon, dag)

    elif svar == "registrer bruker":
        navn = input("Skriv ditt fullstendige navn: ")
        epost = input("Skriv din epost: ")
        telefon = input("Skriv ditt telefonnummer: ")
        addKunde(navn, epost, telefon)
        print("Kunde registrert")
        cursor.execute("""SELECT * FROM Kunde""")
        print(cursor.fetchall())

    elif svar == "finn rute":
        startstasjon = input("Hvilken startstasjon vil du søke for? ")
        endestasjon = input("Hvilken endestasjon vil du søke for? ")
        dato = input("Hvilken dag vil du søke for? ")
        klokkeslett = input("Hvilken klokkeslett vil du søke for? ")
        finnRuter(startstasjon, endestasjon, dato, klokkeslett)

    elif svar == "avslutt":
        con.close()
        print("Programmet avsluttes")
        break
