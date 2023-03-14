INSERT INTO Jernbanestasjon
VALUES ("Trondheim",  5.1);

INSERT INTO Jernbanestasjon
VALUES ("Steinkjer",  3.6);

INSERT INTO Jernbanestasjon 
VALUES ("Mosjøen",  6.8);

INSERT INTO Jernbanestasjon 
VALUES ("Mo i Rana",  3.5);

INSERT INTO Jernbanestasjon 
VALUES ("Fauske",  34.0);

INSERT INTO Jernbanestasjon 
VALUES ("Bodø",  4.1);

INSERT INTO Jernbanestrekning
VALUES ("Nordlandsbanen",  "Diesel", "Trondheim", "Bodø");

INSERT INTO Delstrekning
VALUES ("Nordlandsbanen",  1, 120, "Dobbeltspor",  "Trondheim", "Steinkjer");

INSERT INTO Delstrekning
VALUES ("Nordlandsbanen",  2, 280, "Enkeltspor",  "Steinkjer", "Mosjøen");

INSERT INTO Delstrekning
VALUES ("Nordlandsbanen",  3, 90, "Enkeltspor",  "Mosjøen", "Mo i Rana");

INSERT INTO Delstrekning
VALUES ("Nordlandsbanen",  4, 170, "Enkeltspor",  "Mo i Rana", "Fauske");

INSERT INTO Delstrekning
VALUES ("Nordlandsbanen",  5, 60, "Enkeltspor",  "Fauske", "Bodø");

