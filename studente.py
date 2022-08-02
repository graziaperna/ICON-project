from pyswip import Prolog
import pandas as pd
from tabulate import tabulate

prolog = Prolog()
prolog.consult("KB.pl") 

#mostra la lista degli studenti 
def studentList():
    
    myTrueQuery= "studente(X,Y,Z)"
    generalList(myTrueQuery, 1)

#mostra la lista degli studenti idonei
def suitableStudentList():
    
    myTrueQuery= "studente(X,si,Z)"
    generalList(myTrueQuery, 2)
    
def notSuitableStudentList():
    
    myTrueQuery= "studente(X,no,Z)"
    generalList(myTrueQuery, 3)
    
def generalList(myTrueQuery, nQuery):
    myList = list(prolog.query(myTrueQuery))
    for elem in myList:
        
        if(nQuery==1):
            print(str(elem["X"]) + " " + str(elem["Y"])+ " " + str(elem["Z"]))
        elif(nQuery==2):
            print(str(elem["X"]) + " " + "si" + " " + str(elem["Z"]))
        else:
            print(str(elem["X"]) + " " + "no" + " " + str(elem["Z"]))
  
        
        
