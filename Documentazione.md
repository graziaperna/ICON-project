# Documentazione Erasmus Manager

## **Sommario**

1. Introduzione
2. Requisiti funzionali
3. Interfaccia utente
4. Meccaniche principali
5. Sviluppo
6. Conclusioni

<br>

***
## **Introduzione**
<br>
Lo scopo di questo documento è quello di spiegare in maniera tecnica le funzionalità del programma **Erasmus Manager**.

Tale software è stato implementato da : 

- **Maria Elena Zaza** (Matricola: 717052)

- **Grazia Perna** (Matricola: 719284)

Il software in questione è stato implementato al fine di organizzare le mobilità Erasmus degli studenti universitari e di gestire le componenti:
1. Studenti
2. Dipartimenti
3. Destinazioni

Inoltre si occupa di fare una stima della borsa di studio spettante ad un utente (attraverso l'uso di un classificatore) e di calcolare la probabilità di poter partecipare al progetto in base ad alcune informazioni.

<br>

***
## **Requisiti funzionali**
<br>
Il programma per essere avviato necessita di alcuni pacchetti, installabili attraverso i seguenti comandi:

1. 'pybbn' -> ```pip install pybbn``` utile per la predizione;
2. 'pandas' -> ```pip install pandas``` utile per il classificatore e per il layout delle tabelle;
3. 'sklearn.tree' -> ```pip install scikit-learn``` utile per il classificatore; 
4. 'pyswip' -> ```pip install pyswip``` per la base di conoscenza in Prolog;
5.  bisognerà anche installare Swi-Prolog:
    - andare nel sito ufficiale;
    - recarsi nella sezione di download;
    - selezionare ```stable release```, scaricare la versione adatta al proprio sistema operativo;
    - successivamente installare il programma sulla propria macchina ```Add swipl to the system PATH for current user```.

<br>

***
## **Interfaccia utente**
<br>
Una volta avviato il programma verrà visualizzato un messaggio di benvenuto:

<br>
<center>

```Benvenuto nel portale ErasmusManager, io sono Lola l'assistente di questo portale.```

```Grazie al mio aiuto potrai consultare numerose informazioni riguardanti il progetto Erasmus+.```
</center>
<br>
E inoltre comparirà un messaggio di default a ogni interazione con l'assistente :

<br>
<center>

```Bisogno di aiuto? Per visualizzare la lista dei comandi digita: -1 ```

</center>
<br>
La lista dei comandi che l'utente potrà utilizzare è la seguente:

<br>
<center><img src = "comandi.PNG"></center>

<br>
Al termine dell'esecuzione comparirà tale messaggio e l'applicazione verrà chiusa:

<br>
<center>

```Lola ti saluta, alla prossima!```

</center>

<br>
All'interno del programma inoltre vengono effettuati dei controlli riguardo l'input dell'utente. Nel caso in cui dovesse inserire un comando o una parola errata apparirà un messaggio di errore.

<br>

***

## **Meccaniche principali**
<br>

Nel nostro applicativo software si è scelto di utilizzare:

1. Una **base di conoscenza**, all'interno del quale sono presenti le liste dei dipartimenti, delle destinazioni e degli studenti, scritta in Prolog dai componenti del gruppo.

2. Un **classificatore** in grado di restituire l'ipotetica borsa di studio dello studente in base alla media dei voti, all'ISEE e se lo studenti è fuori corso o in corso.

<center><img src = "esempioclassificatore.PNG"></center>
<br>
Inoltre abbiamo utilizzato il Linear Kernel Cross Validation per la precisione del classificatore poichè i dati a nostra disposizione erano pochi. 

Abbiamo utilizzato un file CSV all'interno del quale ci saranno le informazioni su:
* **Media**;
* **ISEE**;
* **Fuori corso/in corso**.

Ad ogni campo sono stati associati dei numeri interi:

<center><img src = "esempioborsa.PNG"></center>

Rispettivamente:
* Nel campo media è presente un numero che identificherà la fascia della media in cui si trova l'utente, i valori vanno da 1 a 12;
* Nel campo ISEE è presente un numero che identificherà la fascia ISEE in cui si trova l'utente, i valori vanno da 1 a 3;
* Nel campo C_FC è presente un numero che identificherà che l'utente è in corso(1) o fuori corso(0).
* Per quanto riguarda la borsa di studio abbiamo calcolato un possibile range.Abbiamo attribuito ad ogni possibile fascia/valore un punteggio. La somma dei punteggi costituiva una determinata fascia di borsa.

3. Per predire la probabilità di partecipazione al programma Erasmus è stata usata una  **rete bayesiana**. Utile per avere una stima generale 
quando è presente un certo grado di incertezza. A tal fine l'utente dovra' rispondere ad alcune domande.

<center><img src = "esempioprob.PNG"></center>

<br>

In base alla percentuale restituita:
* percentuale ```< 30%``` fascia ```bassa```;
* percentuale ```< 45%``` fascia ```medio-bassa```;
* percentuale ```< 60%``` fascia ```media```;
* percentuale ```< 80%``` fascia ```medio-alta```;
* percentuale ```>= 80%``` fascia ```alta```.

<br>

Ogni risposta è pesata differentemente e queste percentuali sono determinate da:

* **Lingua Inglese**: quale livello d'inglese possiede lo studente;  
* **Altre lingue**: se l'utente conosce altre lingue oltre all'inglese;
* **Conoscenza lingue**: contiene ```Lingua inglese``` e ```Altre lingue```;
* **Altri Erasmus**: se l'utente ha fatto altri Erasmus in passato;
* **Traferimento**: se l'utente preferisce vivere in Italia o all'estero;
* **Adattamento**: contiene ```Altri Erasmus``` e ```Futuro```;
* **Abilità Estere**: contiene```Conoscenza Lingue``` e di ```Adattamento```;
* **Permanenza**: tempo permanenza voluta dall'utente;
* **Anni studio**: se l'utente è in corso o fuori corso;
* **Merito**: contiene ```Anni Studio``` e ```Permanenza```;
* **Previsione partecipazione**: contiene ```Abilità Estere``` e ```Merito```;

<br>

***

## **Sviluppo**

<br>

Il gruppo ha sviluppato tale progetto a partire da Luglio 2022 fino a metà Agosto 2022 in remoto utilizzando la piattaforma gitHub e come ambiente di lavoro Eclipse.

<br>

***

## **Conclusioni**

<br>

Tale progetto è stato molto interessante in quanto i membri del gruppo, in previsione di una specializzazione futura in Intelligenza Artificiale, hanno avuto la possibilità in gettare le prime basi in questo ambito.

<br>

<center>

Il gruppo, **[ERASMUS MANAGER](https://github.com/graziaperna/ICON-project.git)**

</center>
