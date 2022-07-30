
#messaggio di benvenuto  
def firstMessage():
    print("Benvenuto nel portale ErasmusManager, io sono Lola l'assistente di questo portale.\n"
          "Grazie al mio aiuto potrai consultare numerose informazioni riguardanti il progetto Erasmus+.")
    
#menu per visualizzare i comandi disponibili
def mainMenu():
    print("\n\t\t\t\t\tSTUDENTI\t\t\t\t\t|\n"
          "studenti -> mostra la lista di tutti gli studenti (idonei e non)                             \n"
          "idonei -> mostra la lista di tutti gli studenti idonei                                       \n"
          "non_idoeni -> mostra la lista di tutti gli studenti non idonei                               \n"
          "cerca_studente -> mostra le informazione dello studente selezionato                          \n"
          "aggiungi_studente -> aggiunge un nuovo studente                                              \n"
          "modifica_studente -> modifica uno studente esistente                                         \n"
          "\n\t\t\t\t\tDESTINAZIONI\t\t\t\t\t|\n"
          "destinazioni -> mostra la lista delle destinazioni                                           \n"
          "aggiungi_destinazione -> aggiunge una nuova destinazione                                     \n"
          "\n\t\t\t\t\tDIPERTIMENTI\t\t\t\t\t|\n"
          "dipartimenti -> mostra i dipartimenti aderenti al programma                                  \n"
          " aggiungi_dipartimento -> aggiunge un nuovo dipartimento aderente                            \n"
          " rimuovi_dipartimento -> rimuove un dipartimento aderente                                    \n"
          "\n\t\t\t\t\tFUNZIONALITA'\t\t\t\t\t|\n"
          "probabilita_idoneita' -> mostra la probabilita' di idoneità al programma \n"
          "finanziamento-> mostra la borsa spettante allo studente                                      \n"
          "precisione_classificatore -> calcola il margine di precisione del classificatore             \n"
          "esci -> termina il programma                                                                 \n")
    
#mostra il comando da inserire per visualizzare i comandi
def lolaHelp():
    print("\nBisogno di aiuto? Per visualizzare la lista dei comandi digita 'menu/lola/help' ")