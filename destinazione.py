#["7","Mostra la lista delle destinazioni"],
#["8","Aggiunge una nuova destinazione"],
from pyswip import Prolog
from tabulate import tabulate
import studente as s
import re

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
       
        destinationID = input("Inserisci codice destinazione:\n").lower()
        
            
        queryCheck = "destinazione("+str(destinationID)+",FACOLTA,DISPONIBILITA)"
       
        #messaggio errore nel caso la lunghezza dell'ID non rovesse rientrare nel range (1-3)   
        if(not 1 <= len(str(destinationID)) <= 3):
            print("Valore inserito non valido. Max 3 caratteri!\n")
         
        #messaggio errore nel caso sono presenti dei numeri nell'ID inserito   
        if(any(chr.isdigit() for chr in str(destinationID))): 
            destinationID=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
            
    #controllo presenza id nel database
    if(not outputResult(queryCheck, False)):

        faculty = "" 
        
        faculty = input("Inserisci la facolta': ").lower()
            
        availabilty = input("Inserisci la disponibilita': ").lower()
        
        queryCheck = "destinazione("+str(destinationID)+","+faculty+","+availabilty+")"
        prolog.assertz(queryCheck)
        
        print("Destinazione inserita nel database.")
        
    else:
        print("Destinazione gia' presente nel database.\n")
        
#rimuove una destinazione in seguito alla rimozione di un dipartimento
def removeDestination(departmentFaculty):
    destinationID=""
    queryCheck = "destinazione(ID,"+str(departmentFaculty)+",DISPONIBILITA)"
    
    #controllo presenza facolta' nel database
    if(outputResult(queryCheck, False)):
        
        destination=list(prolog.query("destinazione(ID,"+str(departmentFaculty)+",_)"))
       
        outputResult(queryCheck, True)
        
        for elem in destination:
            destinationID = str(destination[0]).split("'")
            s.removeStudentForDestination(destinationID[3])
            prolog.retractall(queryCheck)

def modifyAvailability(ID,operation):
    
    queryCheck = "destinazione("+str(ID)+",FACOLTA,DISPONIBILITA)"
    destination=list(prolog.query(queryCheck))
    #salvataggio occorrenze di FACOLTA' e DISPONIBILITA'
    for elem in destination:
        infoDestination = extractDestination(destination, operation)

        if(infoDestination[1] != 0):
            prolog.retractall(queryCheck)
            prolog.assertz("destinazione("+str(ID)+","+str(infoDestination[0])+","+str(infoDestination[1])+")")
            return True
        else:
            return False
    
def extractDestination(list, operation):
        listInfo=[]
        destinationID = str(list[0]).split("'")
        listInfo.append(destinationID[3])
        
        if(operation == 0):
            listInfo.append(int(destinationID[6][destinationID[6].find(' ')+1:destinationID[6].find('}')]) - 1)
            return listInfo

        elif(operation == 1):
            listInfo.append(int(destinationID[6][destinationID[6].find(' ')+1:destinationID[6].find('}')]) + 1)
            return listInfo
        
        else:
            return destinationID[7]
            
        
            
        
        
        

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
    
    
    