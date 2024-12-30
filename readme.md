# Mr. White - Gioco di Ruoli

Un semplice gioco basato su ruoli segreti, ispirato al classico gioco da tavolo in cui i giocatori devono cercare di scoprire chi è "Mr. White". Ogni giocatore riceve una parola segreta, ma solo i "buoni" e gli "undercover" conoscono una parola, mentre "Mr. White" non riceve alcuna parola.

## Funzionamento del Gioco

1. **Ruoli**:
   - **Buoni**: I giocatori che ricevono una parola segreta.
   - **Undercover**: I giocatori che ricevono una parola segreta, ma leggermente diversa da quella dei "buoni".
   - **Mr. White**: Un giocatore che non riceve alcuna parola e deve cercare di confondere gli altri.

2. **Obiettivo**:
   I giocatori devono cercare di scoprire chi è Mr. White in base alle parole che riceveranno.

## Come Funziona

1. **Configurazione**:
   Il gioco richiede un file di configurazione `config.conf` dove puoi specificare il numero di giocatori, il numero di buoni, undercover e Mr. White, nonché i nomi dei giocatori.
   
2. **File delle Parole**:
   Le parole per i giocatori vengono estratte da un file JSON (`parole.json`), che contiene una lista di coppie di parole (una per i "buoni" e una per gli "undercover").
   
3. **Assegnazione Ruoli**:
   I ruoli (buoni, undercover, Mr. White) vengono assegnati casualmente ai giocatori. Le parole vengono associate ai giocatori in modo che i "buoni" e gli "undercover" ricevano una parola segreta, mentre i "Mr. White" non ricevono nulla.

4. **Interazione**:
   Durante il gioco, ai giocatori viene mostrato un dialogo con la loro parola segreta. Ogni volta che un giocatore vede la propria parola, può premere il tasto "Avanti" o semplicemente premere il tasto **Invio** per passare al prossimo giocatore.

5. **Scrittura della Mappatura**:
   Al termine del gioco, viene scritta una mappatura dei ruoli e delle parole assegnate ai giocatori in un file `mappatura_ruoli.txt`.

## Requisiti

Assicurati di avere Python 3.x installato. Il gioco usa la libreria `tkinter` per la GUI.

### Librerie necessarie:

1. **tkinter**: per la GUI.
2. **json**: per caricare il file delle parole.
3. **configparser**: per caricare la configurazione del gioco.

Per installare le librerie necessarie, esegui:

```bash
pip install tkinter
