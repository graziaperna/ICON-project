from pyswip import Prolog

prolog = Prolog()
prolog.consult("KBErasmusManager.pl")

#mostra la lista dei dipendenti, il loro numero e la lista delle posizioni non ricoperte
def studentsList():

    myTrueQuery = "prop(X,no,Y)"
    myList = list(prolog.query(myTrueQuery))
    print("\nLista studenti: ")
    for elem in myList:
        queryProjects = "- "+elem["X"]+elem["Y"]+elem["Z"]
        print(queryProjects)
    