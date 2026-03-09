from models import Abbonamento, Servizio, Utente, db

# Creiamo una lista vuota per registrare le funzioni
FUNZIONI_REGISTRATE = {}

def mostra_menu():
    print(f"{'ID':<5} | {'NOME':<10} | {'DESCRIZIONE'}")
    print("-" * 40)
    for id_f, info in FUNZIONI_REGISTRATE.items():
        print(f"{id_f:<5} | {info['nome']:<10} | {info['desc']}")

def registra_funzione(funzione):
    """Questo è il decoratore: aggiunge la funzione al nostro dizionario"""
    indice = len(FUNZIONI_REGISTRATE) + 1
    FUNZIONI_REGISTRATE[indice] = {
        "nome": funzione.__name__,
        "desc": funzione.__doc__.strip() if funzione.__doc__ else "",
        "func": funzione
    }
    return funzione  # Restituisce la funzione originale intatta        

@registra_funzione
def getAllUsers():
    """Esegue la query per ottenere tutti gli utenti"""

    print("--- Tutti gli utenti ---")
    try:
        with db:
            # Seleziona tutti gli utenti ordinati alfabeticamente per nome
            utenti = (Utente
                .select()
                #.where(Utente.nome % 'A%')
                .order_by(Utente.nome)
            )
            
            for u in utenti:
                print(f"ID: {u.id} - Nome: {u.nome} - Cognome: {u.cognome}")

    except Exception as e:
        print(f"Errore: {e}")

@registra_funzione
def getAllServices():
    """Esegue la query per ottenere tutti i servizi"""

    print("--- Tutti i servizi ---")
    try:
        with db:
            # Seleziona tutti i record
            servizi = Servizio.select().order_by(Servizio.nome)
            for s in servizi:
                print(f"ID: {s.id} - Nome: {s.nome}")

    except Exception as e:
        print(f"Errore: {e}")

@registra_funzione
def getUserServices():
    """Esegue la query per ottenere tutti i servizi di un utente"""

    print("--- Servizi di un utente ---")
    try:
        with db:
            id_utente = int(input("Inserisci l'ID dell'utente: "))
            utente: Utente = Utente.get_by_id(id_utente)

            # 1. Query con backref
            # se voglio ordindare per nome o comunque per un altro attributo della tabella servizio
            # devo fare il join()
            query = (utente.abbonamenti
                     .join(Servizio)
                     .order_by(Servizio.nome))

            # 2. Query DIRETTA: "Cerca tutti gli Abbonamenti che puntano a questo Utente"
            # nota: posso ordinare
            query = (Abbonamento
                     .select()
                     .join(Servizio)
                     .where(Abbonamento.utente == id_utente)
                     .order_by(Servizio.nome))
            
            if not query.exists():
                print(f"Non ci sono abbonamenti")
            else:
                for a in query:
                    print(f"ID: {a.servizio.id} - Nome: {a.servizio.nome} - Data iscrizione: {a.data_iscrizione}")

    except Utente.DoesNotExist:
        print(f"Errore: L'utente con ID {id_utente} non esiste.")
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    mostra_menu()
    try:
        scelta = int(input("Inserisci l'ID della funzione che vuoi eseguire: "))
        if scelta in FUNZIONI_REGISTRATE:
            FUNZIONI_REGISTRATE[scelta]["func"]()
        else:
            print("Errore: ID non presente in elenco.")
    except ValueError:
        print("Errore: Inserisci un numero intero valido.")
    