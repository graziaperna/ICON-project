from pyswip import Prolog
import pandas as pd
from tabulate import tabulate

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista degli studenti 
def studentList():
    
    myTrueQuery= "studente(ID,IDONEO,DESTINAZIONE)"
    generalList(myTrueQuery)

#mostra la lista degli studenti idonei
def suitableStudentList():
    
    myTrueQuery= "studente(ID,si,DESTINAZIONE)"
    generalList(myTrueQuery)
    
def notSuitableStudentList():
    
    myTrueQuery= "studente(ID,no,DESTINAZIONE)"
    generalList(myTrueQuery)
    
def generalList(myTrueQuery):
    myList = list(prolog.query(myTrueQuery))

    print(tabulate(myList, headers='keys',numalign="center"))
 
        
        
