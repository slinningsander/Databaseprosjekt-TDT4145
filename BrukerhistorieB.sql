/* Data for operatører */

INSERT INTO Operatør
VALUES ("SJ");

/* Data for togruter */

INSERT INTO Togrute
VALUES ("Dagtog fra Trondheim til Bodø", "SJ");

INSERT INTO Togrute
VALUES ("Nattog fra Trondheim til Bodø", "SJ");

INSERT INTO Togrute
VALUES ("Morgentog fra Mo i Rana til Trondheim", "SJ");


/* Lager en ny tabell som lagrer date for hvilke dager hver togrute kjører */

CREATE TABLE DagerTogruterKjører (
	"RuteID"	TEXT,
	"Ukedag"	TEXT CHECK("Ukedag" = "mandag" OR "Ukedag" = "tirsdag" OR "Ukedag" = "onsdag" OR "Ukedag" = "torsdag" OR "Ukedag" = "fredag" OR "Ukedag" = "lørdag" OR "Ukedag" = "søndag"),
	FOREIGN KEY("RuteID") REFERENCES "Togrute"("RuteID") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("RuteID","Ukedag")
);


/* Data for hvilke dager togruter kjører */

/* Dagtog fra Trondheim til Bodø */

INSERT INTO DagerTogruterKjører
VALUES ("Dagtog fra Trondheim til Bodø", "mandag");

INSERT INTO DagerTogruterKjører
VALUES ("Dagtog fra Trondheim til Bodø", "tirsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Dagtog fra Trondheim til Bodø", "onsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Dagtog fra Trondheim til Bodø", "torsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Dagtog fra Trondheim til Bodø", "fredag");

/* Nattog fra Trondheim til Bodø */

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "mandag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "tirsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "onsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "torsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "fredag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "lørdag");

INSERT INTO DagerTogruterKjører
VALUES ("Nattog fra Trondheim til Bodø", "søndag");

/* Morgentog fra Mo i Rana til Trondheim */

INSERT INTO DagerTogruterKjører
VALUES ("Morgentog fra Mo i Rana til Trondheim", "mandag");

INSERT INTO DagerTogruterKjører
VALUES ("Morgentog fra Mo i Rana til Trondheim", "tirsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Morgentog fra Mo i Rana til Trondheim", "onsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Morgentog fra Mo i Rana til Trondheim", "torsdag");

INSERT INTO DagerTogruterKjører
VALUES ("Morgentog fra Mo i Rana til Trondheim", "fredag");

/* Data for hvilke stasjoner som kjører når på hvilke togruter */

/* Dagtog fra Trondheim til Bodø */

INSERT INTO "Stasjon på rute"
Values ("Trondheim", "Dagtog fra Trondheim til Bodø", NULL, "07:49", 1);

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Dagtog fra Trondheim til Bodø", "09:51", "09:51", 2);

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Dagtog fra Trondheim til Bodø", "13:20", "13:20", 3);

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Dagtog fra Trondheim til Bodø", "14:31", "14:31", 4);

INSERT INTO "Stasjon på rute"
Values ("Fauske", "Dagtog fra Trondheim til Bodø", "16:49", "16:49", 5);

INSERT INTO "Stasjon på rute"
Values ("Bodø", "Dagtog fra Trondheim til Bodø", "17:34", NULL, 6);

/* Nattog fra Mo i Rana til Bodø */

INSERT INTO "Stasjon på rute"
Values ("Trondheim", "Nattog fra Trondheim til Bodø", NULL, "23:05", 1);

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Nattog fra Trondheim til Bodø", "00:57", "00:57", 2);

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Nattog fra Trondheim til Bodø", "04:41", "04:41", 3);

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Nattog fra Trondheim til Bodø", "05:55", "05:55", 4);

INSERT INTO "Stasjon på rute"
Values ("Fauske", "Nattog fra Trondheim til Bodø", "08:19", "08:19", 5);

INSERT INTO "Stasjon på rute"
Values ("Bodø", "Nattog fra Trondheim til Bodø", "09:05", NULL, 6);

/* Morgentog fra Mo i Rana til Trondheim */

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Morgentog fra Mo i Rana til Trondheim", NULL, "08:11", 4);

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Morgentog fra Mo i Rana til Trondheim", "09:14", "09:14", 3);

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Morgentog fra Mo i Rana til Trondheim", "12:31", "12:31", 2);

INSERT INTO "Stasjon på rute"
Values ("Trondheim", "Morgentog fra Mo i Rana til Trondheim", "14:13", NULL, 1);




/* Data for hvilke vognmodeller som finnes, i dette tilfellet, vognmodellene til SJ. */

INSERT INTO Vognmodell
VALUES('SJ-sittevogn-1', 'SJ', 3, 4, NULL);


INSERT INTO Vognmodell
VALUES('SJ-sovevogn-1', 'SJ', NULL, NULL, 4);


/* Data for vognforekomster til forskjellige vognmodeller. */
INSERT INTO Vognforekomst
VALUES('SJ-sittevogn-1', 1);


INSERT INTO Vognforekomst
VALUES('SJ-sittevogn-1', 2);


INSERT INTO Vognforekomst
VALUES('SJ-sittevogn-1', 3);


INSERT INTO Vognforekomst
VALUES('SJ-sovevogn-1', 4);


INSERT INTO Vognforekomst
VALUES('SJ-sittevogn-1', 5);


/* Data for vognoppsettene til forskjellige togruter */
INSERT INTO Vognoppsett
VALUES('Dagtog fra Trondheim til Bodø', 'SJ-sittevogn-1', 1, 1);


INSERT INTO Vognoppsett
VALUES('Dagtog fra Trondheim til Bodø', 'SJ-sittevogn-1', 2, 2);


INSERT INTO Vognoppsett
VALUES('Nattog fra Trondheim til Bodø', 'SJ-sittevogn-1', 3, 1);


INSERT INTO Vognoppsett
VALUES('Nattog fra Trondheim til Bodø', 'SJ-sovevogn-1', 4, 2);


INSERT INTO Vognoppsett
VALUES('Morgentog fra Mo i Rana til Trondheim', 'SJ-sittevogn-1', 5, 1);


/* Data for delstekninger på Banestrekningene */

INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '1', '120.0', 'Dobbeltspor', 'Trondheim', 'Steinkjer');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '2', '280.0', 'Enkeltspor', 'Steinkjer', 'Mosjøen');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '3', '90.0', 'Enkeltspor', 'Mosjøen', 'Mo i Rana');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '4', '170.0', 'Enkeltspor', 'Mo i Rana', 'Fauske');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '5', '60.0', 'Enkeltspor', 'Fauske', 'Bodø');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '6', '90.0', 'Enkeltspor', 'Mo i Rana', 'Mosjøen');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '7', '280.0', 'Enkeltspor', 'Mosjøen', 'Steinkjer');


INSERT INTO Delstrekning
VALUES ('Nordlandsbanen', '8', '120.0', 'Dobbeltspor', 'Steinkjer', 'Trondheim');


/* Data for hvilke delstrekninger togrutene kjører på */

INSERT INTO "Kjøres på"
VALUES ('Dagtog fra Trondheim til Bodø', 'Nordlandsbanen', '1');


INSERT INTO "Kjøres på"
VALUES ('Dagtog fra Trondheim til Bodø', 'Nordlandsbanen', '2');


INSERT INTO "Kjøres på"
VALUES ('Dagtog fra Trondheim til Bodø', 'Nordlandsbanen', '3');


INSERT INTO "Kjøres på"
VALUES ('Dagtog fra Trondheim til Bodø', 'Nordlandsbanen', '4');


INSERT INTO "Kjøres på"
VALUES ('Dagtog fra Trondheim til Bodø', 'Nordlandsbanen', '5');


INSERT INTO "Kjøres på"
VALUES ('Nattog fra Trondheim til Bodø', 'Nordlandsbanen', '1');


INSERT INTO "Kjøres på"
VALUES ('Nattog fra Trondheim til Bodø', 'Nordlandsbanen', '2');


INSERT INTO "Kjøres på"
VALUES ('Nattog fra Trondheim til Bodø', 'Nordlandsbanen', '3');


INSERT INTO "Kjøres på"
VALUES ('Nattog fra Trondheim til Bodø', 'Nordlandsbanen', '4');


INSERT INTO "Kjøres på"
VALUES ('Nattog fra Trondheim til Bodø', 'Nordlandsbanen', '5');


INSERT INTO "Kjøres på"
VALUES ('Morgentog fra Mo i Rana til Trondheim', 'Nordlandsbanen', '6');


INSERT INTO "Kjøres på"
VALUES ('Morgentog fra Mo i Rana til Trondheim', 'Nordlandsbanen', '7');


INSERT INTO "Kjøres på"
VALUES ('Morgentog fra Mo i Rana til Trondheim', 'Nordlandsbanen', '8');