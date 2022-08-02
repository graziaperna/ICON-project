import studente as s
import pandas as pd
from tabulate import tabulate

#funzioni dei vari comandi disponibili
def studenti():
    s.studentList()
    lolaHelp()

def idonei():
    s.suitableStudentList()
    lolaHelp()

def non_idonei():
    s.notSuitableStudentList()
    lolaHelp()

def cerca_studente():
    s.findStudent()
    lolaHelp()

def aggiungi_studente():
    s.addStudent()
    lolaHelp()

def modifica_studente():
    s.modifyStudent()
    lolaHelp()

def destinazioni():
    lolaHelp()

def aggiungi_destinazione():
    lolaHelp()

def dipartimenti():
    lolaHelp()

def aggiungi_dipartimento():
    lolaHelp()

def rimuovi_dipartimento():
    lolaHelp()

def probabilita_idoneita():
    lolaHelp()

def finanziamento():
    lolaHelp()

def precisione_classificatore():
    lolaHelp()

def esci():
    print("\nE' un dispiacere vederti andare via! Alla prossima! ")

def lolaHelp():
    print("\nBisogno di aiuto? Per visualizzare la lista dei comandi digita: -1 ")

def default():
    print("\nValore non valido. Inserire un numero corretto.")

#messaggio di benvenuto  
def firstMessage():
    print("Benvenuto nel portale ErasmusManager, io sono Lola l'assistente di questo portale.\n"
          "Grazie al mio aiuto potrai consultare numerose informazioni riguardanti il progetto Erasmus+.")
    
#menu per visualizzare i comandi disponibili
def mainMenu():
    table = [["COMANDO","DESCRIZIONE COMANDO"],
            ["",""],
            ["    ","STUDENTI"],
            ["1","Mostra la lista di tutti gli studenti (idonei e non)"],
            ["2","Mostra la lista di tutti gli studenti idonei"],
            ["3","Mostra la lista di tutti gli studenti non idonei"],
            ["4","Mostra le informazioni dello studente selezionato"],
            ["5","Aggiunge un nuovo studente"],
            ["6","Modifica uno studente esistente"],
            ["",""],
            ["    ","DESTINAZIONI"],
            ["7","Mostra la lista delle destinazioni"],
            ["8","Aggiunge una nuova destinazione"],
            ["",""],
            ["    ","DIPARTIMENTI"],
            ["9","Mostra i dipartimenti aderenti al programma"],
            ["10","Aggiunge un nuovo dipartimento aderente"],
            ["11","Rimuove un dipartimento aderente"],
            ["",""],
            ["    ","FUNZIONALITA'"],
            ["12","Mostra la probabilita' di idoneita' al programma"],
            ["13","Mostra la borsa spettante allo studente"],
            ["14","Calcola il margine di precisione del classificatore"],
            ["0","Terminare l'esecuzione del programma"]]
    
    print(tabulate(table, tablefmt="pretty", numalign="center"))
    
    print("\nDigita il numero del comando a cui sei interessato.              \n")
    
