% ---REGOLE---

% La nostra base di conoscenza sarà organizzata come mostrato di seguito:

% STUDENTE(matricola, idoneo, codiceDidestinazione) (3)
% DIPARTIMENTO(facolta, indirizzo, coordinatore) 
% DESTINAZIONE(codiceDestinazione, facolta, disponibilita) (2)


% Definisce se è presente il numero di posti disponibili necessari per gli propi che vogliono partire in una destinazione 
prop(id, suitable, destination):- prop(destination, nameDep, freePlaces), freePlaces >= 1.

% Definisce se il dipartimento inserito come attributo di prop sia disponibile 
prop(destination, nameDep, freePlaces):- prop(nameDep, address, coordinator).

% Definisce se la destinazione inserita come attributo di prop sia disponibile 
prop(id, suitable, destination):- prop(destination, nameDep, freePlaces).

% Definisce se la nuova destinazione inserita non sia già presente nella lista
% prop(X, nameDep, freePlaces):- X != destination.

% Definisce se il nuovo dipartimento inserito non sia già presente nella lista
% prop(X, address, coordinator):- X != nameDep.

% Definisce se il nuovo prope inserito non sia già presente nella lista
% prop(X, suitable, destination):- X != id.

%-------------------------------------------------------------------------------------------------------------------------------------
%---DATI---

%---LISTA DIPARTIMENTI---
prop('Lingue', 'Via Rossi', 'Falco').
prop('Informatica', 'Via Blu',  'Bianchi').
prop('Medicina', 'Via Gramsci', 'Dignazio').
prop('Arte', 'Via Ruvo', 'Comero').
prop('Psicologia', 'Via Baracca', 'Scioscia').
prop('Matematica', 'Via Rorri', 'Valenzano').

%---LISTA STUDENTI---
prop(90678, 'si', 133).
prop(90478, 'si', 556).
prop(90633, 'no', null).
prop(93678, 'si', 211).
prop(91678, 'no', null).
prop(90448, 'no', null).
prop(90078, 'si', 325).
prop(91258, 'si', 332).

%---LISTA DESTINAZIONI---
prop(133, 'Informatica', 2).
prop(122, 'Lingue', 3).
prop(455, 'Arte', 2).
prop(332, 'Psicologia', 1).
prop(556, 'Matematica', 1).
prop(006, 'Medicina', 4).
