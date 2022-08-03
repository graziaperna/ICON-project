from pyswip import Prolog
from tabulate import tabulate
import destinazione as d

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista completa dei dipartimenti
def departmentList():
    
    myTrueQuery= "dipartimento(FACOLTA,INDIRIZZO,COORDINATORE)"
    outputResult(myTrueQuery, True)

#utile per aggiungere un nuovo dipartimento
def addDepartment():
       
    departmentFaculty = input("Inserisci la facolta':\n").lower()
    
            
    queryCheck = "dipartimento("+str(departmentFaculty)+",INDIRIZZO,COORDINATORE)"
         
    #messaggio errore nel caso sono presenti dei numeri nella facolta inserita  
    if(any(chr.isdigit() for chr in str(departmentFaculty))): 
        departmentFaculty=""
        print("Valore inserito non valido. Inserire solo lettere!\n")
    
    #controllo presenza facolta' nel database
    if(not outputResult(queryCheck, False)):
        
        address = input("Inserisci l'indirizzo della facolta': ").lower()
            
        coordinator = input("Inserisci il coordinatore: ").lower()
        
        queryCheck = "dipartimento("+str(departmentFaculty)+","+str(address)+","+str(coordinator)+")"

        prolog.assertz(queryCheck)
        
        print("Dipartimento inserito nel database.")
        
    else:
        print("Dipartimento gia' presente nel database.\n")
        
#rimuove un dipartimento esistente
def removeDepartment():
    
    departmentFaculty = input("Inserisci la facolta' da eliminare:\n").lower()
    queryCheck = "dipartimento("+str(departmentFaculty)+",INDIRIZZO,COORDINATORE)"
    
    #controllo presenza facolta' nel database
    if(outputResult(queryCheck, False)):
        prolog.retractall(queryCheck)
        print("Il dipartimento e' stato eliminato correttamente.\n")
        
        d.removeDestination(departmentFaculty)
    else:
        print("Dipartimento non presente nel database.\n")
        
        
        
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
    
          