CREATE TABLE "Jernbanestasjon" (
	"Navn"	TEXT,
	"Moh"	INTEGER NOT NULL CHECK("Moh" > 0),
	PRIMARY KEY("Navn")
);

CREATE TABLE "Operatør" (
	"Navn"	TEXT,
	PRIMARY KEY("Navn")
);

CREATE TABLE "Kunde" (
	"Kundenummer"	INTEGER CHECK("Kundenummer" > 0),
	"Navn"	TEXT NOT NULL,
	"E-postadresse"	TEXT NOT NULL,
	"Mobilnummer"	INTEGER NOT NULL CHECK(LENGTH("Mobilnummer") = 8),
	PRIMARY KEY("Kundenummer")
);

CREATE TABLE "Jernbanestrekning" (
	"Navn"	TEXT,
	"Fremdriftsenergi"	TEXT NOT NULL CHECK("Fremdriftsenergi" = "Elektrisk" OR "Fremdriftsenergi" = "Diesel"),
	"Startstasjon"	TEXT,
	"Endestasjon"	TEXT,
	PRIMARY KEY("Navn"),
	FOREIGN KEY("Endestasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("Startstasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE "Delstrekning" (
	"JernbanestrekningNavn"	TEXT,
	"Strekningsnummer"	INTEGER CHECK("Strekningsnummer" > 0),
	"Lengde"	REAL NOT NULL CHECK("Lengde" > 0),
	"Sportype"	INTEGER NOT NULL CHECK("Sportype" = "Enkeltspor" OR "Sportype" = "Dobbeltspor"),
	"Startstasjon"	TEXT NOT NULL,
	"Endestasjon"	TEXT NOT NULL,
	PRIMARY KEY("JernbanestrekningNavn","Strekningsnummer"),
	FOREIGN KEY("JernbanestrekningNavn") REFERENCES "Jernbanestrekning"("Navn") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Startstasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Endestasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Vognmodell" (
	"Navn"	TEXT,
	"EierNavn"	TEXT NOT NULL,
	"AntallRader"	INTEGER CHECK("AntallRader" > 0),
	"AntallSeterPerRad"	INTEGER CHECK("AntallSeterPerRad" > 0),
	"AntallKupéer"	INTEGER CHECK("AntallKupéer" > 0),
	PRIMARY KEY("Navn"),
	FOREIGN KEY("EierNavn") REFERENCES "Operatør"("Navn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Vognforekomst" (
	"Navn"	TEXT,
	"Produksjonsnummer"	INTEGER,
	PRIMARY KEY("Navn","Produksjonsnummer"),
	FOREIGN KEY("Navn") REFERENCES "Vognmodell"("Navn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Kundeordre" (
	"Ordrenummer"	INTEGER CHECK("Ordrenummer" > 0),
	"Kjøpstid"	TEXT NOT NULL,
	"Kundenummer"	INTEGER NOT NULL,
	PRIMARY KEY("Ordrenummer"),
	FOREIGN KEY("Kundenummer") REFERENCES "Kunde"("Kundenummer") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Togrute" (
	"RuteID"	TEXT,
	"OperatørNavn"	TEXT,
	"MedHovedretning"	INTEGER,
	FOREIGN KEY("OperatørNavn") REFERENCES "Operatør"("Navn") ON DELETE SET NULL ON UPDATE CASCADE,
	PRIMARY KEY("RuteID")
);

CREATE TABLE "Togruteforekomst" (
	"RuteID"	TEXT,
	"Dato"	TEXT,
	PRIMARY KEY("RuteID","Dato"),
	FOREIGN KEY("RuteID") REFERENCES "Togrute"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Billett" (
	"BillettID"	INTEGER CHECK("BillettID" > 0),
	"Seteplass"	INTEGER,
	"Sengeplass"	INTEGER,
	"Vognnummer"	INTEGER NOT NULL,
	"Ordrenummer"	INTEGER,
	"FraStasjon"	TEXT NOT NULL,
	"TilStasjon"	TEXT NOT NULL,
	"RuteID"	TEXT NOT NULL,
	"TogruteDato"	TEXT NOT NULL,
	PRIMARY KEY("BillettID"),
	FOREIGN KEY("TogruteDato") REFERENCES "Togruteforekomst"("Dato") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("RuteID") REFERENCES "Togruteforekomst"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Ordrenummer") REFERENCES "Kundeordre"("Ordrenummer") ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY("FraStasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("TilStasjon") REFERENCES "Jernbanestasjon"("Navn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Vognoppsett" (
	"RuteID"	TEXT,
	"VognNavn"	TEXT,
	"Produksjonsnummer"	TEXT,
	"Vognnummer"	INTEGER NOT NULL CHECK("Vognnummer" > 0),
	PRIMARY KEY("RuteID","VognNavn","Produksjonsnummer"),
	FOREIGN KEY("VognNavn") REFERENCES "Vognforekomst"("Navn") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("RuteID") REFERENCES "Togrute"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Produksjonsnummer") REFERENCES "Vognforekomst"("Produksjonsnummer") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "Stasjon på rute" (
	"JernbanestasjonNavn"	TEXT,
	"RuteID"	TEXT,
	"Ankomsttid"	TEXT,
	"Avgangstid"	TEXT,
	"Stasjonsnummer"	INTEGER,
	FOREIGN KEY("RuteID") REFERENCES "Togrute"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("JernbanestasjonNavn") REFERENCES "Jernbanestasjon"("Navn") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("JernbanestasjonNavn","RuteID")
);

CREATE TABLE "Kjøres på" (
	"RuteID"	TEXT,
	"JernbanestrekningNavn"	TEXT,
	"Delstrekningsnummer"	INTEGER,
	PRIMARY KEY("RuteID","JernbanestrekningNavn","Delstrekningsnummer"),
	FOREIGN KEY("JernbanestrekningNavn") REFERENCES "Delstrekning"("JernbanestrekningNavn") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("RuteID") REFERENCES "Togrute"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY("Delstrekningsnummer") REFERENCES "Delstrekning"("Strekningsnummer") ON DELETE CASCADE ON UPDATE CASCADE
);
