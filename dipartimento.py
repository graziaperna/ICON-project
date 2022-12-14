from pyswip import Prolog
from tabulate import tabulate
import destinazione as d
import funzionalita as f

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista completa dei dipartimenti
def departmentList():
    
    myTrueQuery= "dipartimento(FACOLTA,INDIRIZZO,COORDINATORE)"
    f.outputResult(myTrueQuery, True)

#utile per aggiungere un nuovo dipartimento
def addDepartment():
     
    departmentFaculty = ""
    
  #messaggio errore nel caso sono presenti dei numeri nella facolta inserita  
    while(departmentFaculty == ""):
       
        departmentFaculty = input("Inserisci la facolta':\n").lower()
        queryCheck = "dipartimento("+str(departmentFaculty)+",INDIRIZZO,COORDINATORE)"
            
        if(any(chr.isdigit() for chr in str(departmentFaculty))): 
            departmentFaculty=""
            print("Valore inserito non valido. Inserire solo lettere!\n")
    
   
    #controllo presenza facolta' nel database
    if(not f.outputResult(queryCheck, False)):
        
        address = input("Inserisci l'indirizzo della facolta': ")
        
        address = f.convertSpace(address)
        
        coordinator = input("Inserisci il coordinatore: ").lower()
        
        for letter in address:
            if(letter != " "):
                if(not letter.isdigit()): 
                    address = address.replace(letter,letter.lower())
            else:
                address = address.replace(letter,"_")

        
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
    if(f.outputResult(queryCheck, False)):
        prolog.retractall(queryCheck)
        print("Il dipartimento e' stato eliminato correttamente.\n")
        
        d.removeDestination(departmentFaculty)
    else:
        print("Dipartimento non presente nel database.\n")
        