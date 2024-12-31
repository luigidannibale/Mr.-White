import configparser
import json
import os
import random


def clear():
    os.system("clear")


# Funzione per caricare la configurazione dal file .conf
def carica_configurazione():
    config = configparser.ConfigParser()
    config.read('config.conf')

    # Controlla se tutte le chiavi necessarie sono presenti
    if 'DEFAULT' not in config:
        raise KeyError("La sezione [DEFAULT] non è presente nel file di configurazione.")

    numero_civili = int(config['DEFAULT']['numero_civili'])
    numero_undercover = int(config['DEFAULT']['numero_undercover'])
    numero_mr_white = int(config['DEFAULT']['numero_mr_white'])
    giocatori = config['DEFAULT']['giocatori'].split(', ')

    return numero_civili, numero_undercover, numero_mr_white, giocatori


# Funzione per caricare una parola casuale da un file JSON
def carica_parole_da_json():
    with open("parole.json", "r") as f:
        parole = json.load(f)

    # Seleziona una riga casuale
    parola_casuale = random.choice(parole)

    return parola_casuale


# Funzione per eseguire il controllo di validità
def verifica_validita(numero_civili, numero_undercover, numero_mr_white, giocatori):
    numero_giocatori = len(giocatori)
    if numero_civili + numero_undercover + numero_mr_white != numero_giocatori:
        print("Errore", "La somma dei ruoli (civili + undercover + mr. white) non corrisponde al numero di giocatori.")
        return False
    return True


# Funzione per la gestione dell'assegnazione delle parole
def assegnazione_parole(giocatori, parole, numero_civili, numero_undercover, numero_mr_white):
    # Creiamo 3 gruppi distinti (buoni, undercover, mr_white)
    ruoli = ['buoni'] * numero_civili + ['undercover'] * numero_undercover + ['mr_white'] * numero_mr_white

    # Mescoliamo i ruoli in modo casuale
    random.shuffle(ruoli)

    mappatura = { }

    for i, giocatore in enumerate(giocatori):
        if ruoli[i] == 'buoni':
            mappatura[giocatore] = { 'ruolo': 'Buono', 'parola': parole["buoni"] }
        elif ruoli[i] == 'undercover':
            mappatura[giocatore] = { 'ruolo': 'Undercover', 'parola': parole["undercover"] }
        else:
            mappatura[giocatore] = { 'ruolo': 'Mr. White', 'parola': "" }  # Mr. White non ha parola

    return mappatura


def scrivi_mappatura(mappatura):
    with open("mappatura_ruoli.txt", "w") as file:
        for giocatore, info in mappatura.items():
            file.write(f"{giocatore}: {info['ruolo']}, Parola: {info['parola']}\n")
    print("Mappatura scritta su 'mappatura_ruoli.txt'.")


# Funzione per avanzare al prossimo giocatore
def avanti(giocatori, mappatura, index):
    if index < len(giocatori):
        giocatore = giocatori[index]
        info = mappatura[giocatore]

        if info['ruolo'] == 'Mr. White':
            # Messaggio specifico per i Mr. White
            print(f"Giocatore {giocatore}", "Sei Mr. White")
        else:
            parola = info['parola']
            print(f"Giocatore {giocatore}: La tua parola è: {parola}")


# Funzione per mostrare il dialog per ogni giocatore
def mostra_dialog():
    # Carichiamo i dati dal file di configurazione
    numero_civili, numero_undercover, numero_mr_white, giocatori = carica_configurazione()

    # Verifica la validità dei dati
    if not verifica_validita(numero_civili, numero_undercover, numero_mr_white, giocatori):
        return

    # Carichiamo le parole da file JSON
    parole = carica_parole_da_json()

    # Assegniamo i gruppi (ruoli casuali) ai giocatori
    mappatura = assegnazione_parole(giocatori, parole, numero_civili, numero_undercover, numero_mr_white)

    index = 0  # Indice del giocatore corrente
    print("Prossimo giocatore: " + giocatori[0])
    input("Avanti...")
    clear()
    for i in range(len(giocatori)):
        # Aggiungiamo il nome del prossimo giocatore
        avanti(giocatori, mappatura, i)
        input("Avanti...")
        clear()
        print("Prossimo giocatore: " + giocatori[min(i + 1, len(giocatori) - 1)])
        input("Avanti...")
        clear()
    print("Fine", "Tutti i giocatori hanno ricevuto la loro parola.")
    scrivi_mappatura(mappatura)
    exit()


# Avviare la GUI
if __name__ == "__main__":
    mostra_dialog()
