:- dynamic(student/5).
:- dynamic(destination/4).
:- dynamic(department/3).

% ---REGOLE---

% La nostra base di conoscenza sarà organizzata come mostrato di seguito:
% STUDENTE(nome, cognome, matricola, idoneo, codiceDiDestinazione)
% DIPARTIMENTO(facolta, indirizzo, coordinatore)
% DESTINAZIONE(codiceDestinazione, citta, paese, facolta, disponibilita)

% Definisce se è presente il numero di posti disponibili necessari per gli studenti che vogliono partire in una destinazione 
student(name, surname, ID, suitable, destinationCode):- destination(destinationCode, city, nation, nameDep, freePlaces), freePlaces >= 1.

% Definisce se il dipartimento inserito come attributo di destination sia disponibile 
destination(destinationCode, city, nation, nameDep, freePlaces):- department(nameDep, address, coordinator).

% Definisce se la destinazione inserita come attributo di student sia disponibile 
student(name, surname, ID, suitable, destinationCode):- destination(destinationCode, city, nation, nameDep, freePlaces).

% Definisce se la nuova destinazione inserita non sia già presente nella lista
destination(X, city, nation, nameDep, freePlaces):- X != destinationCode.

% Definisce se il nuovo dipartimento inserito non sia già presente nella lista
department(X, address, coordinator):- X != nameDep.

% Definisce se il nuovo studente inserito non sia già presente nella lista
student(name, surname, X, suitable, destinationCode):- X != ID.
%-------------------------------------------------------------------------------------------------------------------------------------
%---DATI---

%---LISTA DIPARTIMENTI---
department(Lingue, Via Rossi, Falco).
department(Informatica, Via Blu,  Bianchi).
department(Medicina, Via Gramsci, Dignazio).
department(Arte, Via Ruvo, Comero).
department(Psicologia, Via Baracca, Scioscia).
department(Matematica, Via Rorri, Valenzano).

%---LISTA STUDENTI---
student(Maria, Rossi, 90678, si, 133).
student(Giovanna, Marini, 90478, si, 556).
student(Serena, Vino, 90633, no, null).
student(Michele, Reni, 93678, si, 211).
student(Alessio, Grassi, 91678, no, null).
student(Sonia, Altopina, 90448, no, null).
student(Massimo, Giovini, 90078, si, 325).
student(Giorgio, Verdi, 91258, si, 332).

%---LISTA DESTINAZIONI---
destination(133, Valencia, Spagna, Informatica, 2).
destination(122, Eindhoven, Olanda, Lingue, 3).
destination(455, Vienna, Austria, Arte, 2).
destination(332, Barcellona, Spagna, Psicologia, 1).
destination(556, Monaco, Germania, Matematica, 1).
destination(006, Valencia, Spagna, Medicina, 4).
