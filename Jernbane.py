import datetime
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


def finnRuter(startstasjon, endestasjon, dato, klokkeslett):
    dagInt = datetime.datetime.strptime(dato, "%d/%m/%y").weekday()
    dager = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"]
    ukedag = dager[dagInt]
    nesteDag = dager[(dagInt+1) % 7]

    cursor.execute(
        """SELECT DISTINCT Stasjonsnummer FROM 'Stasjon på rute'
        WHERE JernbanestasjonNavn =:startstasjon""", {"startstasjon": startstasjon}
    )
    startStasjonsnummer = cursor.fetchall()[0]

    cursor.execute(
        """SELECT DISTINCT Stasjonsnummer FROM 'Stasjon på rute'
        WHERE JernbanestasjonNavn =:endestasjon""", {"endestasjon": endestasjon}
    )
    endeStasjonsnummer = cursor.fetchall()[0]

    retning = 1

    if startStasjonsnummer>endeStasjonsnummer:
        retning = 0
    elif startStasjonsnummer<endeStasjonsnummer:
        retning = 1
    else:
        print("Startstasjon og endestasjon er like")

    cursor.execute(
    """SELECT Togrute.RuteID, s1.JernbanestasjonNavn AS Startstasjon, s1.Avgangstid, s2.JernbanestasjonNavn AS Endestasjon, s2.Ankomsttid FROM Togrute
    INNER JOIN 'Stasjon på rute' AS s1 USING (RuteID)
    INNER JOIN 'Stasjon på rute' AS s2 USING (RuteID)
    INNER JOIN DagerTogruterKjører USING (RuteID)
    WHERE Ukedag = :ukedag AND s1.JernbanestasjonNavn = :startstasjon AND s2.JernbanestasjonNavn = :endestasjon AND MedHovedretning=:retning AND s1.Avgangstid > :klokkeslett
    ORDER BY s1.Avgangstid ASC""",
    {"ukedag": ukedag, "startstasjon": startstasjon, "endestasjon": endestasjon, "retning": retning, "klokkeslett": klokkeslett}
    )

    print("Her er alle togruter som går fra", startstasjon, "til", endestasjon, "på", ukedag, "og", nesteDag)
    for rute in cursor.fetchall():
        print("Rute:" + rute[0] + " Startstasjon: " + rute[1] + " Avgangstid: " + rute[2] + " Endestasjon: " + rute[3] + " Ankomsttid: " + rute[4])
    cursor.execute(
    """SELECT Togrute.RuteID, s1.JernbanestasjonNavn AS Startstasjon, s1.Avgangstid, s2.JernbanestasjonNavn AS Endestasjon, s2.Ankomsttid FROM Togrute
    INNER JOIN 'Stasjon på rute' AS s1 USING (RuteID)
    INNER JOIN 'Stasjon på rute' AS s2 USING (RuteID)
    INNER JOIN DagerTogruterKjører USING (RuteID)
    WHERE Ukedag = :ukedag AND s1.JernbanestasjonNavn = :startstasjon AND s2.JernbanestasjonNavn = :endestasjon AND MedHovedretning=:retning AND s1.Avgangstid > :klokkeslett
    ORDER BY s1.Avgangstid ASC""",
    {"ukedag": nesteDag, "startstasjon": startstasjon, "endestasjon": endestasjon, "retning": retning, "klokkeslett": klokkeslett}
    )
    for rute in cursor.fetchall():
        print("Rute:" + rute[0] + " Startstasjon: " + rute[1] + " Avgangstid: " + rute[2] + " Endestasjon: " + rute[3] + " Ankomsttid: " + rute[4])
    
def finnInformasjon(kundenummer):
    cursor.execute(
        """SELECT BillettID, Kjøpstid, TogruteDato, Seteplass, Sengeplass, Vognummer, FraStasjon, TilStasjon  FROM Kundeordre
        INNER JOIN Billeter USING (Ordrenummer)
        WHERE KundeID =:kundenummer AND Dato >= strftime('%d/%m/%y', 'now')""",
        {"kundenummer": kundenummer}
    )
    print("Her er dine fremtidige reiser: ")
    for i in cursor.fetchall():
        infoList = i.split(",")
        print("BillettID: ", infoList[0], "Kjøpstid: ", infoList[1], "TogruteDato: ", infoList[2], "Seteplass: ", infoList[3], "Sengeplass: ", infoList[4], "Vognnummer: ", infoList[5], "FraStasjon: ", infoList[6], "TilStasjon: ", infoList[7])


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
    
    elif svar == "finn informasjon":
        kundenummer = input("Hvilket kundenummer vil du søke for? ")
        finnInformasjon(kundenummer)

    elif svar == "avslutt":
        con.close()
        print("Programmet avsluttes")
        break
