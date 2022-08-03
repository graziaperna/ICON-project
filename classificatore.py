from statistics import mean
from tabulate import tabulate
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
import codecs

competenze = read_csv('borsadistudio.csv')
X = competenze.drop(columns=['borsadistudio'])
y = competenze['borsadistudio']

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)
loo = LeaveOneOut()
#result = cross_val_score(modello, X, y, scoring='accuracy', cv = loo)

def classifier():
    mean = 0
    isee = 0
    regular = -1
    #result = True
    while (mean < 1 or mean > 5):
        
        table = [["MEDIA","FASCIA"],
                ["18-20,5","1"],
                ["20,6-23","2"],
                ["23,1-26","3"],
                ["26,1-28","4"],
                ["28,1-30","5"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        
        mean = int(input("Inserisci la tua media ponderata dei voti, seguendo la tabella sopra riportata: \n"))
       
        if(mean < 1 or mean > 5):
            print("Media inserita non valida. Inserire un valore compreso tra 1 e 5")
            
    while (isee < 1 or isee > 3):
        
        table = [["ISEE","FASCIA"],
                ["13.000 < ISEE <= 26.000","1"],
                ["26.000 < ISEE <= 40.000","2"],
                ["ISEE > 40.000","3"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        isee = int(input("Inserisci il tuo ISEE, seguendo questa tabella: "))
        
        if(isee < 1 or isee > 3):
            print("ISEE inserito non valido. Inserire un valore >= di 13.000")
            
    while (regular != 0 and regular != 1 ):
        regularAnswer = input("Sei in corso(c) o fuori corso(fc)?: ").lower()
        if(regularAnswer=='c'):
            regular=1
        elif(regularAnswer=='fc'):
            regular=0
        else:
            regular=-1
            print("Il valore che hai inserito non e' corretto. Inserisci 'c' se sei in corso e 'fc' se non sei in corso")
            
    borsadistudio = modello.predict([[mean, isee, regular]])
    for elem in borsadistudio:
        print("La borsa di studio che potrai attenere e': " + elem + "\n")


#def accuratezza():
    #print("L'accuratezza del sistema e': %.3f" % mean(result))
    #print("{}".format(result))


