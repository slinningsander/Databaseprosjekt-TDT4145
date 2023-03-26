import datetime
import sqlite3
con = sqlite3.connect('Jernbane.db')
cursor = con.cursor()

# Funksjon for brukerhistorie C
def getTogruter(stasjon, ukedag):
    cursor.execute(
        """SELECT DagerTogruterKjører.RuteID FROM DagerTogruterKjører 
        INNER JOIN 'Stasjon på rute' ON DagerTogruterKjører.RuteID = 'Stasjon på rute'.RuteID 
        WHERE Ukedag =:dag AND JernbanestasjonNavn =:navn""",
        {"dag": ukedag, "navn": stasjon}
    )

    togruter = cursor.fetchall()

    print(togruter)


# Funksjon for brukerhistorie E
def addKunde(navn, epost, telefon):
    con = sqlite3.connect('Jernbane.db')
    cursor = con.cursor()
    cursor.execute(
        """INSERT INTO Kunde (Navn, 'E-postadresse', Mobilnummer) VALUES (:navn, :epost, :telefon)""",
        {"navn": navn, "epost": epost, "telefon": telefon}
    )
    con.commit()


# Funksjon for brukerhistorie D
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
        return

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
    

# Funksjon for brukerhistorie H
def finnInformasjon(kundenummer):
    cursor.execute(
        """SELECT BillettID, Kjøpstid, TogruteDato, Seteplass, Sengeplass, Vognummer, FraStasjon, TilStasjon  FROM Kundeordre
        INNER JOIN Billeter USING (Ordrenummer)
        WHERE KundeID =:kundenummer AND Billett.Dato >= strftime('%d/%m/%y', 'now')""",
        {"kundenummer": kundenummer}
    )
    print("Her er dine fremtidige reiser: ")
    for i in cursor.fetchall():
        infoList = i.split(",")
        print("BillettID: ", infoList[0], "Kjøpstid: ", infoList[1], "TogruteDato: ", infoList[2], "Seteplass: ", infoList[3], "Sengeplass: ", infoList[4], "Vognnummer: ", infoList[5], "FraStasjon: ", infoList[6], "TilStasjon: ", infoList[7])


def opprettOrdre(kundenummer):
    cursor.execute(
        """SELECT * FROM Kunde
        WHERE kundenummer =:kundenummer""",
        {"kundenummer": kundenummer}
    )
    if (len(cursor.fetchall()) == 0):
        print("Kunden finnes ikke")
        return

    kjøpstid =  datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    cursor.execute("""INSERT INTO "Kundeordre"
                    ("Kjøpstid", "Kundenummer")
                    VALUES (:Kjøpstid, :kundenummer);""",
                    {"Kjøpstid": kjøpstid, "kundenummer": kundenummer})
    
    con.commit()

    cursor.execute("""SELECT Ordrenummer FROM Kundeordre
                    WHERE Kjøpstid = :Kjøpstid AND Kundenummer = :kundenummer""",
                    {"Kjøpstid": kjøpstid, "kundenummer": kundenummer})
    ordrenummer = cursor.fetchall()[0][0]
    
    return ordrenummer


# Funksjon for brukerhistorie G
def kjøpBillett(ordreNummer, dato, RuteID, FraStasjon, TilStasjon):
    retning = 1

    cursor.execute(
        """SELECT DISTINCT stasjonsnummer FROM 'Stasjon på rute'
        WHERE JernbanestasjonNavn =:FraStasjon""",
        {"FraStasjon": FraStasjon}
    )
    fraStasjonNummer = cursor.fetchall()[0][0]

    cursor.execute(
        """SELECT DISTINCT stasjonsnummer FROM 'Stasjon på rute'
        WHERE JernbanestasjonNavn =:TilStasjon""",
        {"TilStasjon": TilStasjon}
    )
    tilStasjonNummer = cursor.fetchall()[0][0]
    
    
    if fraStasjonNummer>tilStasjonNummer:
        retning = 0
    elif fraStasjonNummer<tilStasjonNummer:
        retning = 1
    else:
        print("Startstasjon og endestasjon er like")
        return
    
    
    
    cursor.execute(
        """SELECT * FROM Togruteforekomst
        WHERE Dato =:Dato AND RuteID =:RuteID""",
        {"RuteID": RuteID, "Dato": dato}
    )
    if (len(cursor.fetchall()) == 0):
        print("Toget kjører ikke på den oppgitte datoen.")
        return
    
    cursor.execute(
        """SELECT VognNavn, vognnummer FROM Togruteforekomst
        INNER JOIN vognoppsett USING (RuteID)
        where Dato =:Dato AND RuteID =:RuteID""",
        {"RuteID": RuteID, "Dato": dato}
    )
    vognList = cursor.fetchall()
    print("Her er vognene som er ledige på denne togruten: ")
    for i in vognList:
        print("Vognnavn: ", i[0], "Vognnummer: ", i[1])
    vognnummer = int(input("Hvilken vogn vil du reise i? "))
    vognnavn = ""

    for i in vognList:
        if i[1] == vognnummer:
            vognnavn = i[0]
    
    print(vognnavn)

    cursor.execute(
        """SELECT AntallRader, AntallSeterPerRad, AntallKupéer  FROM vognmodell
        WHERE Navn =:vognnavn""",
        {"vognnavn": vognnavn}
    )
   
    
    tuppel = cursor.fetchall()[0]
    maxAntallPlasser = tuppel[0] * tuppel[1]
    maxAntallSengePlasser = tuppel[2]

    ledigeSeteplasser = []
    ledigeSengePlasser = []
    for i in range(1,maxAntallPlasser+1):
        ledigeSeteplasser.append(i)
    
    for i in range(1,maxAntallSengePlasser+1):
        ledigeSengePlasser.append(i)

    if len(maxAntallSengePlasser) == 0:
        if retning == 1:
            cursor.execute(
                """SELECT Seteplass FROM Billett
                INNER JOIN 'Stasjon på rute' s1 ON s1.RuteID = Billett.RuteID AND Billett.FraStasjon = s1.JernbanestasjonNavn
                INNER JOIN 'Stasjon på rute' s2 ON s2.RuteID = Billett.RuteID AND Billett.TilStasjon = s2.JernbanestasjonNavn
                WHERE (s1.Stasjonsnummer >= :fraStasjonnummer AND s2.Stasjonsnummer <= :tilStasjonnummer) OR (s2.Stasjonsnummer >= :tilStasjonnummer AND s2.Stasjonsnummer <= :tilStasjonnummer) OR (s1.Stasjonsnummer >= :fraStasjonnummer AND s1.Stasjonsnummer <= :fraStasjonnummer) """,
                {"RuteID": RuteID, "Dato": dato, "vognnummer": vognnummer, "fraStasjonnummer": fraStasjonNummer, "tilStasjonnummer": tilStasjonNummer}
            )
        else:
            cursor.execute(
                """SELECT Seteplass FROM Billett
                INNER JOIN 'Stasjon på rute' s1 ON s1.RuteID = Billett.RuteID AND Billett.FraStasjon = s1.JernbanestasjonNavn
                INNER JOIN 'Stasjon på rute' s2 ON s2.RuteID = Billett.RuteID AND Billett.TilStasjon = s2.JernbanestasjonNavn
                WHERE (s1.Stasjonsnummer <= :fraStasjonnummer AND s2.Stasjonsnummer >= :tilStasjonnummer) OR (s2.Stasjonsnummer <= :tilStasjonnummer AND s2.Stasjonsnummer >= :tilStasjonnummer) OR (s1.Stasjonsnummer <= :fraStasjonnummer AND s1.Stasjonsnummer >= :fraStasjonnummer) """,
                {"RuteID": RuteID, "Dato": dato, "vognnummer": vognnummer, "fraStasjonnummer": fraStasjonNummer, "tilStasjonnummer": tilStasjonNummer}
            )
        result = cursor.fetchall()
        print (result)
        for i in result:
            if i[0] in ledigeSeteplasser:
                ledigeSeteplasser.remove(i[0])
        if(len(ledigeSeteplasser) == 0):
            print("Det er ingen ledige seteplasser på denne vognen")
            return
        else:
            print("Her er seteplassene som er ledige på denne vognen: ")
            print(ledigeSeteplasser)
            seteplass = int(input("Hvilken seteplass vil du reise i? "))
            if seteplass not in ledigeSeteplasser:
                print("Seteplassen er ikke ledig")
                return
        cursor.execute(
        """INSERT INTO Billett (Seteplass, Vognnummer, Ordrenummer, FraStasjon, TilStasjon, RuteID, TogruteDato)
            VALUES (:Seteplass, :Vognnummer, :Ordrenummer, :FraStasjon, :TilStasjon, :RuteID, :TogruteDato)""",
            {"Seteplass": seteplass, "Vkjøp ognnummer": vognnummer, "Ordrenummer": ordreNummer, "FraStasjon": FraStasjon, "TilStasjon": TilStasjon, "RuteID": RuteID, "TogruteDato": dato}
        )
        con.commit()
            
    elif len(maxAntallPlasser)==0:
        if retning == 1:
            cursor.execute(
                """SELECT Sengeplass FROM Billett
                INNER JOIN 'Stasjon på rute' s1 ON s1.RuteID = Billett.RuteID AND Billett.FraStasjon = s1.JernbanestasjonNavn
                INNER JOIN 'Stasjon på rute' s2 ON s2.RuteID = Billett.RuteID AND Billett.TilStasjon = s2.JernbanestasjonNavn
                WHERE (s1.Stasjonsnummer >= :fraStasjonnummer AND s2.Stasjonsnummer <= :tilStasjonnummer) OR (s2.Stasjonsnummer >= :tilStasjonnummer AND s2.Stasjonsnummer <= :tilStasjonnummer) OR (s1.Stasjonsnummer >= :fraStasjonnummer AND s1.Stasjonsnummer <= :fraStasjonnummer) """,
                {"RuteID": RuteID, "Dato": dato, "vognnummer": vognnummer, "fraStasjonnummer": fraStasjonNummer, "tilStasjonnummer": tilStasjonNummer}
            )
        else:
            cursor.execute(
                """SELECT Sengeplass FROM Billett
                INNER JOIN 'Stasjon på rute' s1 ON s1.RuteID = Billett.RuteID AND Billett.FraStasjon = s1.JernbanestasjonNavn
                INNER JOIN 'Stasjon på rute' s2 ON s2.RuteID = Billett.RuteID AND Billett.TilStasjon = s2.JernbanestasjonNavn
                WHERE (s1.Stasjonsnummer <= :fraStasjonnummer AND s2.Stasjonsnummer >= :tilStasjonnummer) OR (s2.Stasjonsnummer <= :tilStasjonnummer AND s2.Stasjonsnummer >= :tilStasjonnummer) OR (s1.Stasjonsnummer <= :fraStasjonnummer AND s1.Stasjonsnummer >= :fraStasjonnummer) """,
                {"RuteID": RuteID, "Dato": dato, "vognnummer": vognnummer, "fraStasjonnummer": fraStasjonNummer, "tilStasjonnummer": tilStasjonNummer}
            )
        result = cursor.fetchall()
        print (result)
        for i in result:
            if i[0] in ledigeSengePlasser:
                ledigeSengePlasser.remove(i[0]) #fjerner ledige seteplasser som er reservert, må legge til slik at den andre sengeplassen i samme kupé også blir fjernet
        if(len(ledigeSengePlasser) == 0):
            print("Det er ingen ledige sengeplasser på denne vognen")
            return
        else:
            print("Her er sengeplassene som er ledige på denne vognen: ")
            print(ledigeSengePlasser)
            sengeplass = int(input("Hvilken sengeplass vil du reise i? "))
            if sengeplass not in ledigeSengePlasser:
                print("Sengeplassen er ikke ledig")
                return
        cursor.execute(
        """INSERT INTO Billett (Sengeplass, Vognnummer, Ordrenummer, FraStasjon, TilStasjon, RuteID, TogruteDato)
            VALUES (:Sengeplass, :Vognnummer, :Ordrenummer, :FraStasjon, :TilStasjon, :RuteID, :TogruteDato)""",
            {"Sengeplass": sengeplass, "Vkjøp ognnummer": vognnummer, "Ordrenummer": ordreNummer, "FraStasjon": FraStasjon, "TilStasjon": TilStasjon, "RuteID": RuteID, "TogruteDato": dato}
        )
        con.commit()
            

    



# Hovedprogram
print("Hei! Velkommen til vårt Jernbaneprogram \n")
svar = ""
while svar != "avslutt":

    svar = input("""Hva vil du gjøre? 
            \n Skriv 'finn stasjon' for å få alle togruter som går på den oppgitte stasjonen på den oppgitte dagen.
            \n Skriv 'registrer bruker' for å registrere en ny bruker.
            \n Skriv 'finn rute' for å finne en togrute basert på en startstasjon og en sluttstasjon, med utgangspunkt i en dato og et klokkeslett.
            \n Skriv 'finn informasjon' for å finne informasjon om fremtidige reiser.
            \n Skriv 'kjøp billett' for å kjøpe en billett.
            \n Skriv 'avslutt' for å avslutte programmet.\n""")

    # Brukerhistorie C
    if svar == "finn stasjon":
        stasjon = input("Hvilken stasjon vil du finne? ")
        dag = input("Hvilken dag vil du finne? ")
        print("Her er alle togruter som går på stasjonen", stasjon, "på", dag)
        getTogruter(stasjon, dag)


    # Brukerhistorie E
    elif svar == "registrer bruker":
        navn = input("Skriv ditt fullstendige navn: ")
        epost = input("Skriv din epost: ")
        telefon = input("Skriv ditt telefonnummer: ")
        addKunde(navn, epost, telefon)
        print("Kunde registrert")
        cursor.execute("""SELECT * FROM Kunde""")
        print(cursor.fetchall())

    # Brukerhistorie D
    elif svar == "finn rute":
        startstasjon = input("Hvilken startstasjon vil du søke for? ")
        endestasjon = input("Hvilken endestasjon vil du søke for? ")
        dato = input("Hvilken dag vil du søke for? ")
        klokkeslett = input("Hvilken klokkeslett vil du søke for? ")
        finnRuter(startstasjon, endestasjon, dato, klokkeslett)

    # Brukerhistorie H
    elif svar == "finn informasjon":
        kundenummer = input("Hvilket kundenummer vil du søke for? ")
        finnInformasjon(kundenummer)
    
    # Brukerhistorie G
    elif svar == "kjøp billett":
        kundenummer = input("Hva er ditt kundenummer? ")
        ordrenummer = opprettOrdre(kundenummer)
        antallBilletter = input("Hvor mange billetter vil du kjøpe? ")
        for i in range(int(antallBilletter)):
            togruteID = input("Hvilken togrute vil du kjøpe billett for? For eksempel: 'Dagtog fra Trondheim til Bodø'. ")
            dato = input("Hvilken dato vil du reise på? For eksempel: '03/04/23'. ")
            FraStasjon = input("Hvilken stasjon vil du reise fra? ")
            TilStasjon = input("Hvilken stasjon vil du reise til? ")
            kjøpBillett(ordrenummer, dato, togruteID, FraStasjon, TilStasjon)

    elif svar == "avslutt":
        con.close()
        print("Programmet avsluttes")
        break
