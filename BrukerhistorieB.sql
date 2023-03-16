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
Values ("Trondheim", "Dagtog fra Trondheim til Bodø", NULL, "07:49");

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Dagtog fra Trondheim til Bodø", "09:51", "09:51");

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Dagtog fra Trondheim til Bodø", "13:20", "13:20");

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Dagtog fra Trondheim til Bodø", "14:31", "14:31");

INSERT INTO "Stasjon på rute"
Values ("Fauske", "Dagtog fra Trondheim til Bodø", "16:49", "16:49");

INSERT INTO "Stasjon på rute"
Values ("Bodø", "Dagtog fra Trondheim til Bodø", "17:34", NULL);

/* Nattog fra Mo i Rana til Bodø */

INSERT INTO "Stasjon på rute"
Values ("Trondheim", "Nattog fra Trondheim til Bodø", NULL, "23:05");

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Nattog fra Trondheim til Bodø", "00:57", "00:57");

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Nattog fra Trondheim til Bodø", "04:41", "04:41");

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Nattog fra Trondheim til Bodø", "05:55", "05:55");

INSERT INTO "Stasjon på rute"
Values ("Fauske", "Nattog fra Trondheim til Bodø", "08:19", "08:19");

INSERT INTO "Stasjon på rute"
Values ("Bodø", "Nattog fra Trondheim til Bodø", "09:05", NULL);

/* Morgentog fra Mo i Rana til Trondheim */

INSERT INTO "Stasjon på rute"
Values ("Mo i Rana", "Morgentog fra Mo i Rana til Trondheim", NULL, "08:11");

INSERT INTO "Stasjon på rute"
Values ("Mosjøen", "Morgentog fra Mo i Rana til Trondheim", "09:14", "09:14");

INSERT INTO "Stasjon på rute"
Values ("Steinkjer", "Morgentog fra Mo i Rana til Trondheim", "12:31", "12:31");

INSERT INTO "Stasjon på rute"
Values ("Trondheim", "Morgentog fra Mo i Rana til Trondheim", "14:13", NULL);






    