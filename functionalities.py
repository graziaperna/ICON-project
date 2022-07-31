#funzioni dei vari comandi disponibili
def studenti():
    lolaHelp()

def idonei():
    lolaHelp()

def non_idonei():
    lolaHelp()

def cerca_studente():
    lolaHelp()

def aggiungi_studente():
    lolaHelp()

def modifica_studente():
    lolaHelp()

def destinazioni():
    lolaHelp()

def aggiungi_destinazione():
    lolaHelp()

def dipartimenti():
    lolaHelp()

def aggiungi_dipartimento():
    lolaHelp()

def rimuovi_dipartimento():
    lolaHelp()

def probabilita_idoneita():
    lolaHelp()

def finanziamento():
    lolaHelp()

def precisione_classificatore():
    lolaHelp()

def esci():
    print("\nE' un dispiacere vederti andare via! Alla prossima! ")

def lolaHelp():
    print("\nBisogno di aiuto? Per visualizzare la lista dei comandi digita: -1 ")

def default():
    print("\nValore non valido. Inserire un numero corretto.")

#messaggio di benvenuto  
def firstMessage():
    print("Benvenuto nel portale ErasmusManager, io sono Lola l'assistente di questo portale.\n"
          "Grazie al mio aiuto potrai consultare numerose informazioni riguardanti il progetto Erasmus+.")
    
#menu per visualizzare i comandi disponibili
def mainMenu():
    print("Questa e' la lista dei comandi disponibili, "
          "digita il numero del comando a cui sei interessato.              \n"
          
          "\n\t\t\t\t\tSTUDENTI\t\t\t\t\t                                   \n"
          "1  -> Mostra la lista di tutti gli studenti (idonei e non)       \n"
          "2  -> Mostra la lista di tutti gli studenti idonei               \n"
          "3  -> Mostra la lista di tutti gli studenti non idonei           \n"
          "4  -> Mostra le informazione dello studente selezionato          \n"
          "5  -> Aggiunge un nuovo studente                                 \n"
          "6  -> Modifica uno studente esistente                            \n"
          
          "\n\t\t\t\t\tDESTINAZIONI\t\t\t\t\t                               \n"
          "7  -> Mostra la lista delle destinazioni                         \n"
          "8  -> Aggiunge una nuova destinazione                            \n"
          
          "\n\t\t\t\t\tDIPARTIMENTI\t\t\t\t\t                               \n"
          "9  -> Mostra i dipartimenti aderenti al programma                \n"
          "10 -> Aggiunge un nuovo dipartimento aderente                    \n"
          "11 -> Rimuove un dipartimento aderente                           \n"
          
          "\n\t\t\t\t\tFUNZIONALITA'\t\t\t\t\t                              \n"
          "12 -> Mostra la probabilita' di idoneita' al programma           \n"
          "13 -> Mostra la borsa spettante allo studente                    \n"
          "14 -> Calcola il margine di precisione del classificatore        \n"
          
          "\nDigitare 0 per terminare...                                    \n")
    
