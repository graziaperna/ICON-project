from pyswip import Prolog
from tabulate import tabulate

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista completa degli studenti 
def studentList():
    
    myTrueQuery= "studente(ID,IDONEO,DESTINAZIONE)"
    outputResult(myTrueQuery, True)

#mostra la lista degli studenti idonei
def suitableStudentList():
    
    myTrueQuery= "studente(ID,si,DESTINAZIONE)"
    outputResult(myTrueQuery, True)
    
#mostra la lista degli studenti non idonei
def notSuitableStudentList():
    
    myTrueQuery= "studente(ID,no,DESTINAZIONE)"
    outputResult(myTrueQuery, True)
    
#dato l'ID, cerca uno studente
def findStudent():
    
    studentID = input("Inserisci la matricola dello studente che vuoi cercare:\n")
    myTrueQuery= "studente("+str(studentID)+",IDONEO,DESTINAZIONE)"
    outputResult(myTrueQuery, True)
    
#inserisce uno studente
def addStudent():
    
    studentID = ""
    
    #controllo numero caratteri della matricola inserita
    while(not 1 <= len(str(studentID)) <= 5):
       
        studentID = input("Inserisci matricola nuovo studente:\n")
        queryCheck = "studente("+str(studentID)+",IDONEO,DESTINAZIONE)"
        
        if(not 1 <= len(str(studentID)) <= 5):
            print("Valore inserito non valido. Max 5 caratteri!\n")
    
    #controllo presenza id nel database
    if(not outputResult(queryCheck, False)):

        studentSuitability = ""
        
        #controllo inserimento 'si' o 'no'
        while(studentSuitability != 'si' and studentSuitability != 'no'):
            
            studentSuitability = input("Inserisci se e' idoneo o meno(si/no): ").lower()
            
            if(studentSuitability != 'si' and studentSuitability != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
    
        #inserimento della destinazione solo in caso di idoneità
        if(studentSuitability == 'si'): 
            
            destinationFound = False
            #controllo presenza destinazione nel database
            destinationFound = False
            
            while(not destinationFound):
                
                studentDestination = input("Inserisci l'ID della destinazione: ")
                checkDestination = "destinazione("+str(studentDestination)+",FACOLTA,DISPONIBILITA)"
                destinationFound = outputResult(checkDestination, False)
                if (not destinationFound):
                    print("Valore inserito non valido, inserire una destinazione presente nel database.\n") 
                   
            queryCheck = "studente("+str(studentID)+","+studentSuitability+","+str(studentDestination)+")"
        
        else:
            
            queryCheck = "studente("+str(studentID)+","+studentSuitability+", null)"
            
        prolog.assertz(queryCheck)
        
        print("Studente inserito nel database.")
        
    else:
        print("Studente gia' presente nel database.\n")
       
    
#modifica un progetto esistente
def modifyStudent():
    
    studentID = input("Inserisci matricola dello studente da modificare:\n")
    queryCheck = "studente("+str(studentID)+",IDONEO,DESTINAZIONE)"
    
    #controllo presenza id nel database
    if(outputResult(queryCheck, False)):
        
        prolog.retractall(queryCheck)
        
        studentSuitability = ""
        
        #controllo inserimento 'si' o 'no'
        while(studentSuitability != 'si' and studentSuitability != 'no'):
            
            studentSuitability = input("Inserisci se e' idoneo o meno(si/no): ").lower()
            
            if(studentSuitability != 'si' and studentSuitability != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
        #inserimento della destinazione solo in caso di idoneità
        if(studentSuitability == 'si'): 
            destinationFound = False
            #controllo presenza destinazione nel database
            while(not destinationFound):
                
                studentDestination = input("Inserisci l'ID della destinazione: ")
                checkDestination = "destinazione("+str(studentDestination)+",FACOLTA,DISPONIBILITA)"
                destinationFound = outputResult(checkDestination, False)
                
                if (not destinationFound):
                    print("Valore inserito non valido, inserire una destinazione presente nel database.\n") 
                    
            queryCheck = "studente("+str(studentID)+","+studentSuitability+","+str(studentDestination)+")"
            
        else:
            
            queryCheck = "studente("+str(studentID)+","+studentSuitability+", null)"
                
        prolog.assertz(queryCheck)
        
        print("Studente modificato correttamente.")
        
    else:
        print("Studente non presente nel database.\n")
        
#rimuove uno studente in seguito alla rimozione di una destinazione
def removeStudentForDestination(destinationID):
    
    queryCheck = "studente(ID,IDONEO,"+str(destinationID)+")"
    student=list(prolog.query(queryCheck))
    
    for elem in student:
        
        #controllo presenza facolta' nel database
        if(outputResult(queryCheck, False)):
            prolog.retractall(queryCheck)

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
    
 
        
        
