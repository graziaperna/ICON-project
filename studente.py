from pyswip import Prolog

prolog = Prolog()
prolog.consult("KB.pl")

#mostra la lista degli studenti
def studentsList():

    myTrueQuery = "studente(X,Y,Z)"
    myList = list(prolog.query(myTrueQuery))
    print("\nLista studenti: ")
    for elem in myList:
        queryProjects = "- "+ str(elem["X"])+ " " + elem["Y"] + " "+ str(elem["Z"])
        print(queryProjects)
    