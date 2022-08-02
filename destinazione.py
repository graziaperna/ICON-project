#["7","Mostra la lista delle destinazioni"],
#["8","Aggiunge una nuova destinazione"],
from pyswip import Prolog
import pandas as pd
from tabulate import tabulate

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista completa degli studenti 
def destinationList():
    
    myTrueQuery= "destinazione(ID,FACOLTA,DISPONIBILITA)"
    outputResult(myTrueQuery, True)
    
def addDestination():
    
    destinationID = ""
    
    #controllo numero caratteri della matricola inserita
    while(not 1 <= len(str(destinationID)) <= 3):
       
        destinationID = input("Inserisci codice destinazione:\n")
        queryCheck = "destinazione("+str(destinationID)+",FACOLTA,DISPONIBILITA)"
        
        if(not 1 <= len(str(destinationID)) <= 3):
            print("Valore inserito non valido. Max 3 caratteri!\n")
    
    #controllo presenza id nel database
    if(not outputResult(queryCheck, False)):

        faculty = "" 
        
        faculty = input("Inserisci la facolta': ").lower()
            
        availabilty = input("Inserisci la disponibilita': ")
        
        queryCheck = "destinazione("+str(destinationID)+","+faculty+","+availabilty+")"
        prolog.assertz(queryCheck)
        
        print("Destinazione inserita nel database.")
        
    else:
        print("Destinazione gia' presente nel database.\n")
        
#restituisce risultati query    
def outputResult(myTrueQuery, printable):
    
    myList = list(prolog.query(myTrueQuery))
    
    if not myList:
        if printable:
            print("Nessun risultato trovato.\n") 
        return False
    
    else:
        if printable:
            print(tabulate(myList, headers='keys', tablefmt="pretty", numalign="center"))
        return True
    
          