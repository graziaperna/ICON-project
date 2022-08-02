import funzionalita as f
import studente as s
     
#dizionario per definire i comandi disponibili
switcher = {
    "1": f.studenti,
    "2": f.idonei,
    "3": f.non_idonei,
    "4": f.cerca_studente,
    "5": f.aggiungi_studente,
    "6": f.modifica_studente,
    "7": f.destinazioni,
    "8": f.aggiungi_destinazione,
    "9": f.dipartimenti,
    "10": f.aggiungi_dipartimento,
    "11": f.rimuovi_dipartimento,
    "12": f.probabilita_idoneita,
    "13": f.finanziamento,
    "14": f.precisione_classificatore,
    "-1": f.mainMenu
    }

#funzione per accedere al dizionario
def switch(command):
    return switcher.get(command, f.default)()

#funzione iniziale main
if __name__ == '__main__':
    f.firstMessage()
    f.lolaHelp()
    command = "1"
    
    while (command != "0"):
        command = input("Comando inserito -> ")
        
        if(command != "0"):
            switch(command)
    
    f.esci()
        