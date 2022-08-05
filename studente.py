from pyswip import Prolog
import destinazione as d
import funzionalita as f

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista completa degli studenti 
def studentList():
    
    myTrueQuery= "studente(ID,IDONEO,DESTINAZIONE)"
    f.outputResult(myTrueQuery, True)

#mostra la lista degli studenti idonei
def suitableStudentList():
    
    myTrueQuery= "studente(ID,si,DESTINAZIONE)"
    f.outputResult(myTrueQuery, True)
    
#mostra la lista degli studenti non idonei
def notSuitableStudentList():
    
    myTrueQuery= "studente(ID,no,DESTINAZIONE)"
    f.outputResult(myTrueQuery, True)
    
#dato l'ID, cerca uno studente
def findStudent():
    
    studentID = input("Inserisci la matricola dello studente che vuoi cercare:\n")
    myTrueQuery= "studente("+str(studentID)+",IDONEO,DESTINAZIONE)"
    f.outputResult(myTrueQuery, True)
    
#inserisce uno studente
def addStudent():
    
    studentID = ""

    #controllo numero caratteri della matricola inserita
    while(studentID == "" ):
       
        studentID = input("Inserisci matricola nuovo studente:\n")
        queryCheck = "studente("+str(studentID)+",IDONEO,DESTINAZIONE)"
        
        if((not len(str(studentID)) == 5 ) or (not studentID.isdigit())):
            print("Valore inserito non valido. Max 5 caratteri e solo valori numerici!")
            studentID = ""    
  
    #controllo presenza id nel database
    if(not f.outputResult(queryCheck, False)):

        studentSuitability = ""
        
        #controllo inserimento 'si' o 'no'
        while(studentSuitability != 'si' and studentSuitability != 'no'):
            
            studentSuitability = input("Inserisci se e' idoneo o meno(si/no): ").lower()
            
            if(studentSuitability != 'si' and studentSuitability != 'no'):
                
                print("Valore inserito non valido, inserire \"si\" o \"no\".\n")
                
    
        #inserimento della destinazione solo in caso di idoneità
        if(studentSuitability == 'si'): 
            
            #controllo presenza destinazione nel database
            destinationFound = False
            
            while(not destinationFound):
                
                studentDestination = input("Inserisci l'ID della destinazione: ")
                checkDestination = "destinazione("+str(studentDestination)+",FACOLTA,DISPONIBILITA)"
                destinationFound = f.outputResult(checkDestination, False)
                
                if (not destinationFound):
                    print("Valore inserito non valido, inserire una destinazione presente nel database.\n") 
                else:
                    if(d.modifyAvailability(str(studentDestination), 0)):
                        queryCheck = "studente("+str(studentID)+","+studentSuitability+","+str(studentDestination)+")"
                    else:
                        print("Disponibilita' posti non sufficente \n") 
                                     
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
    if(f.outputResult(queryCheck, False)):
        
        lista=list(prolog.query(queryCheck))
        oldDestination = d.extractDestination(lista, 2)
           
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
                destinationFound = f.outputResult(checkDestination, False)
                
                if (not destinationFound):
                    
                    print("Valore inserito non valido, inserire una destinazione presente nel database.\n") 
                else:
                    #diminuizione della disponibilità nuova destinazione
                    if(d.modifyAvailability(str(studentDestination),0)):
                        #aumento disponibilità vecchia destinazione
                        queryCheck = "studente("+str(studentID)+","+studentSuitability+","+str(studentDestination)+")"
                    else:
                        print("Disponibilita' posti non sufficente \n")         
            
        else:
            
            queryCheck = "studente("+str(studentID)+","+studentSuitability+", null)"
         
        d.modifyAvailability(str(oldDestination), 1)       
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
        if(f.outputResult(queryCheck, False)):
            prolog.retractall(queryCheck)
  
