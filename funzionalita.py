import studente as s
import destinazione as d
import dipartimento as dp
import classificatore as c
import probabilita as p
import pandas as pd
from tabulate import tabulate

#funzioni dei vari comandi disponibili
def studenti():
    print("\n-------------------------------LISTA STUDENTI-------------------------------\n\n")
    s.studentList()
    lolaHelp()

def idonei():
    print("\n-------------------------------LISTA STUDENTI IDONEI-------------------------------\n\n")
    s.suitableStudentList()
    lolaHelp()

def non_idonei():
    print("\n-------------------------------LISTA STUDENTI NON IDONEI-------------------------------\n\n")
    s.notSuitableStudentList()
    lolaHelp()

def cerca_studente():
    print("\n-------------------------------RICERCA STUDENTE-------------------------------\n\n")
    s.findStudent()
    lolaHelp()

def aggiungi_studente():
    print("\n-------------------------------AGGIUNTA STUDENTI-------------------------------\n\n")
    s.addStudent()
    lolaHelp()

def modifica_studente():
    print("\n-------------------------------MODIFICA STUDENTI-------------------------------\n\n")
    s.modifyStudent()
    lolaHelp()

def destinazioni():
    print("\n-------------------------------LISTA DESTINAZIONI-------------------------------\n\n")
    d.destinationList()
    lolaHelp()

def aggiungi_destinazione():
    print("\n-------------------------------AGGIUNTA DESTINAZIONE-------------------------------\n\n")
    d.addDestination()
    lolaHelp()

def dipartimenti():
    print("\n-------------------------------LISTA DIPARTIMENTI-------------------------------\n\n")
    dp.departmentList()
    lolaHelp()


def aggiungi_dipartimento():
    print("\n-------------------------------AGGIUNTA DIPARTIMENTO-------------------------------\n\n")
    dp.addDepartment()
    lolaHelp()

def rimuovi_dipartimento():
    print("\n-------------------------------RIMOZIONE DIPARTIMENTO-------------------------------\n\n")
    dp.removeDepartment()
    lolaHelp()

def probabilita_idoneita():
    print("\n-------------------------------PROBABILITA' IDONEITA'-------------------------------\n\n")
    p.prediction()
    lolaHelp()

def finanziamento():
    print("\n-------------------------------CLASSE BORSA DI STUDIO-------------------------------\n\n")
    c.classifier()
    lolaHelp()

def precisione_classificatore():
    print("\n-------------------------------PRECISIONE CLASSIFICATORE-------------------------------\n\n")
    c.accuratezza()
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
    
