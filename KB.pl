:- dynamic(studente/3).
:- dynamic(dipartimento/3).
:- dynamic(destinazione/3).

%---REGOLE---

% studente(id, idoneo, destinazione).
% dipartimento(facolta, indirizzo, coordinatore).
% destinazione(codiceDestinazione, facolta, disponibilita).

%---DATI---

%---LISTA STUDENTI---
studente(90678, si, 133).
studente(90478, si, 556).
studente(90633, no, null).
studente(93678, si, 211).
studente(91678, no, null).
studente(90448, no, null).
studente(90078, si, 325).
studente(91258, si, 332).

%---LISTA DIPARTIMENTI---
dipartimento('Lingue', 'Via Rossi', 'Falco').
dipartimento('Informatica', 'Via Blu',  'Bianchi').
dipartimento('Medicina', 'Via Gramsci', 'Dignazio').
dipartimento('Arte', 'Via Ruvo', 'Comero').
dipartimento('Psicologia', 'Via Baracca', 'Scioscia').
dipartimento('Matematica', 'Via Rorri', 'Valenzano').

%---LISTA DESTINAZIONI---
destinazione(133, 'Informatica', 2).
destinazione(122, 'Lingue', 3).
destinazione(455, 'Arte', 2).
destinazione(332, 'Psicologia', 1).
destinazione(556, 'Matematica', 1).
destinazione(006, 'Medicina', 4).
