from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

# Costruizione Rete Bayesiana Percentuale Partecipazione

#conoscenza della lingua inglese
livelloInglese = BbnNode(Variable(0, 'linguaInglese', ['b2', 'b1', 'a2']), [0.70, 0.25, 0.05])

#conoscenza altre lingue
altreLingue = BbnNode(Variable(1, 'altreLingue', ['si', 'no']), [0.85, 0.15])

#nodo di conoscenza delle lingue dell'utente(0-1)
conoscenzaLingue = BbnNode(Variable(2, 'conoscenza lingue', ['ottima', 'scarsa']),
                          [0.98, 0.02, 0.75, 0.25, 0.6, 0.4, 0.51, 0.49, 0.15, 0.85, 0.05, 0.95])

#esperienze precedenti in erasmus universitari
altriErasmus= BbnNode(Variable(3, 'altriErasmus', ['no', 'si']), [0.85, 0.15])

#trasferimento all'estero
trasferimento = BbnNode(Variable(4, 'futuro', ['estero', 'italia']), [0.71, 0.29])

#nodo di adattamento dell'utente (3-4)
adattamento = BbnNode(Variable(5, 'adattamento', ['ottimo', 'scarso']), [0.99, 0.01, 0.72, 0.28,
                                                                         0.32, 0.68, 0.02, 0.98])

#nodo di abilita' dello studente (2-5)
abilitaEstere = BbnNode(Variable(6, 'abilita', ['ottimo', 'scarso']), [0.93, 0.07, 0.83, 0.17,
                                                                        0.52, 0.48, 0.12, 0.88])

#tempo di permanenza
permanenza = BbnNode(Variable(7, 'tempoMobilita', ['6 mesi', '1 anno']), [0.95, 0.05])

#preferisci college o residenza privata
anniStudio = BbnNode(Variable(8, 'anniStudio', ['in corso', 'fuori corso']), [0.85, 0.15])

#nodo per il merito dello studente in base alla media(7-8)
merito = BbnNode(Variable(10, 'merito', ['ottimo', 'scarso']), [0.92, 0.08, 0.77, 0.23,
                                                                0.39, 0.61, 0.16, 0.84])

#previsione finale della % di poter partecipare al progetto (6-10)
previsionePartecipazione = BbnNode(Variable(11, 'previsione partecipazione', ['si', 'no']), [0.95, 0.05, 0.68, 0.32, 
                                                                                             0.51, 0.49, 0.06, 0.94])

bbn = Bbn() \
    .add_node(livelloInglese) \
    .add_node(altreLingue) \
    .add_node(conoscenzaLingue) \
    .add_node(altriErasmus) \
    .add_node(trasferimento) \
    .add_node(adattamento) \
    .add_node(abilitaEstere) \
    .add_node(permanenza) \
    .add_node(anniStudio) \
    .add_edge(Edge(livelloInglese, conoscenzaLingue, EdgeType.DIRECTED)) \
    .add_edge(Edge(altreLingue, conoscenzaLingue, EdgeType.DIRECTED)) \
    .add_edge(Edge(altriErasmus, adattamento, EdgeType.DIRECTED)) \
    .add_edge(Edge(trasferimento, adattamento, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaLingue, abilitaEstere, EdgeType.DIRECTED)) \
    .add_edge(Edge(adattamento, abilitaEstere, EdgeType.DIRECTED)) \
    .add_edge(Edge(permanenza, merito, EdgeType.DIRECTED)) \
    .add_edge(Edge(anniStudio, merito, EdgeType.DIRECTED)) \
    .add_edge(Edge(merito, previsionePartecipazione, EdgeType.DIRECTED)) \
    .add_edge(Edge(abilitaEstere, previsionePartecipazione, EdgeType.DIRECTED))

# Conversione da bbn ad albero
treeCopy = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#domande da porre all'utente
def questionsForPrediction():
    tree = treeCopy.__copy__()

    while True:
        value = input(
            "Indicare il proprio livello di inglese:\n"
            "Risposte possibili: (a2) (b1) (b2) (non so)\n").lower()
        if value in ["a2", "b1", "b2"]:
            insertDefinedValue(tree, "linguaInglese", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(0)

    while True:
        value = input(
            "Indicare se si conoscono altre lingue:\n"
            "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "altreLingue", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(1)

    while True:
        value = input("Hai partecipato ad altri Erasmus universitari?:\n"
                      "Risposte possibili: (si) (no) (non so)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "altriErasmus", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(2)

    while True:
        value = input("Dove ti vedi in futuro?:\n"
                      "Risposte possibili: (italia) (estero) (non so)\n").lower()
        if value in ["italia", "estero"]:
            insertDefinedValue(tree, "futuro", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(3)
            
    while True:
        value = input("Quanto tempo vorresti essere in mobilita'?\n"
                      "Risposte possibili: (6 mesi) (1 anno) (non so)\n").lower()
        if value in ["6 mesi", "1 anno"]:
            insertDefinedValue(tree, "tempoMobilita", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(4)

    while True:
        value = input("Sei in corso o fuori corso?\n"
                      "Risposte possibili: (in corso) (fuori corso) (non so)\n").lower()
        if value in ["in corso", "fuori corso"]:
            insertDefinedValue(tree, "anniStudio", value, 1.0)
            break
        elif value in ["non so"]:
            infoMessage(5)
            
    print("Lola sta analizzando le tue risposte...")
    outputPrediction(tree)



#stampa la probabilita' di partecipare in base alla probabilita' ottenuta
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'previsione partecipazione':
            max, min = posteriors.items()
            print(f'[{node} : {max[1]*100:.0f}%]')
            if max[1] < 0.3:
                print("Probabilita' di partecipazione: bassa.\n")
            elif max[1] < 0.45:
                print("Probabilita' di partecipazione: medio-bassa.\n")
            elif max[1] < 0.6:
                print("Probabilita'  di partecipazione: media.\n")
            elif max[1] < 0.8:
                print("Probabilita'  di partecipazione: medio-alta.\n")
            else:
                print("Probabilita'  di partecipazione: alta.\n")


def infoMessage(number):
    if number == 0:
        print("Devi inserire il tuo livello di inglese, se non hai una certificazione scegli un livello approssimativo.\n")
    elif number == 1:
        print("Devi indicare se conosci altre lingue.\n")
    elif number == 2:
        print("Devi indicare se hai avuto altre esperienze di mobilita' Erasmus durante il periodo universitario.\n")
    elif number == 3:
        print("Devi indicare in quale posto vorresti essere nel tuo futuro tra estero e Italia.\n")
    elif number == 4:
        print("Devi indicare quanto tempo vorerresti essere in mobilita' Erasmus.\n")
    elif number == 5:
        print("Devi indicare se sei in corso o fuori corso.\n")


