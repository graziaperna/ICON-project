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
dipartimento('lingue', 'via Rossi', 'falco').
dipartimento('informatica', 'via Blu',  'bianchi').
dipartimento('medicina', 'via Gramsci', 'dignazio').
dipartimento('arte', 'via Ruvo', 'comero').
dipartimento('psicologia', 'via Baracca', 'scioscia').
dipartimento('matematica', 'via Rorri', 'valenzano').

%---LISTA DESTINAZIONI---
destinazione('vbc', 'informatica', 2).
destinazione('pow', 'lingue', 3).
destinazione('lsk', 'arte', 2).
destinazione('sdd', 'psicologia', 1).
destinazione('qwe', 'matematica', 1).
destinazione('azx', 'medicina', 4).
