from sklearn.model_selection import train_test_split
from numpy import mean
from tabulate import tabulate
from pandas import read_csv
from sklearn import svm


competenze = read_csv('borsadistudio.csv')
X = competenze.drop(columns=['borsadistudio'])

y = competenze['borsadistudio']
# Divisione dei dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=0)
modello = svm.SVC(kernel='linear', C=1, random_state=0)
modello.fit(X_train.values, y_train.values)
result = modello.score(X_train.values, y_train.values)

def classifier():
    mean = 0
    isee = 0
    regular = -1
    #result = True
    while (mean < 1 or mean > 11):
        
        table = [["MEDIA","FASCIA"],
                ["18-19","1"],
                ["19.1-20","2"],
                ["20,1-21","3"],
                ["21,1-22","4"],
                ["22,1-23","5"],
                ["23,1-24","6"],
                ["24,1-25","7"],
                ["25,1-26","8"],
                ["26,1-27","9"],
                ["27,1-28","10"],
                ["28,1-29","11"],
                ["29,1-30","12"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        
        intInserted = False
        while(not intInserted):
            mean = input("Inserisci la tua media ponderata dei voti, seguendo la tabella sopra riportata: \n")
        
            intInserted = controlInput(mean)
        mean=int(mean)
        if(mean < 1 or mean > 11):
            print("Media inserita non valida. Inserire un valore compreso tra 1 e 12")
            
    while (isee < 1 or isee > 3):
        
        table = [["ISEE","FASCIA"],
                ["13.000 < ISEE <= 26.000","1"],
                ["26.000 < ISEE <= 40.000","2"],
                ["ISEE > 40.000","3"]]
        print(tabulate(table, tablefmt="pretty", numalign="center"))
        
        
        intInserted = False
        while(not intInserted):
            
            isee = input("Inserisci il tuo ISEE, seguendo questa tabella: ")
        
            intInserted = controlInput(isee)
        isee=int(isee)
        
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


def accuratezza():
    print("L'accuratezza del sistema e': %0.3f" % mean(result))
    
def controlInput(user_input):

    try:
        int(user_input)
        it_is = True
        
    except ValueError:
        it_is = False
        print("Inserire solo valori numerici.\n")
        
    return it_is



