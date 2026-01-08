import json
from variabiliGlobali import*
#input 
def input_scelta():
    scelta = input("Inserisci il genere che vuoi analizzare: ")
    if(scelta not in generi):
        print("Genere non valido")
        
    return scelta


#funzione per aggiungere i film        
def aggiungi():
    for elem in oggetto_python:
        titolo=elem["title"]
        #print (titolo)
        for genere_s in elem["listed_in"]:
            if genere_s in generi:
                generi[genere_s].append(titolo)
                #print("serie aggiunta")
            else:
                continue   


#funzione per stampare le serie divise per genere
def stampa():
    chiave = input_scelta().strip()
    if chiave in generi:
        print(f"\nSerie nel genere '{chiave}':")
        for serie in generi[chiave]:
            print(f"- {serie}")
    else:
        print("Genere non trovato.")


#lista dei generi
def lista(count):
    chiavi = list(generi.keys())
    for i in range(min(count, len(chiavi))):
        print(chiavi[i])

def menu():
    print("Lista: per visualizzare i generi\n" \
          "Stampa: per stampare le serie di un genere\n"\
          "Esci: per uscire\n")


# main
nome_file = "serie.json"
with open(nome_file, "r") as file:
    stringa_json = file.read()
    oggetto_python = json.loads(stringa_json)
aggiungi()
switch = {
    "lista": lambda:lista(20),
    "stampa": stampa
}

while True:
    menu()
    funzione = input("Inserisci la funzione: ").lower().strip()
    if funzione in switch:
        switch[funzione]()   
    elif funzione == "esci":
        print("Uscita dal programma.")
        break
    else:
        print("Funzione non valida.")

