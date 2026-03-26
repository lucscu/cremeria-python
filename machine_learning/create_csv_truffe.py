import pandas as pd
import numpy as np
import os

# Impostiamo un seme per rendere i dati riproducibili
np.random.seed(42)

data_size = 1000

# Generiamo dati fittizi
data = {
    'importo': np.random.uniform(10, 2000, data_size), # Da 10 a 2000 Euro
    'ora_notturna': np.random.randint(0, 2, data_size), # 0=Giorno, 1=Notte
    'nuovo_utente': np.random.randint(0, 2, data_size) # 0=Storico, 1=Nuovo
}

df = pd.DataFrame(data)

# Queste due righe sono il "motore" del nostro esempio.
# SOLO per questa simulazione, nella realta' le etichette le assegnaremo consapevolmente.
# Servono a creare una correlazione artificiale tra i dati e l'etichetta "truffa", in modo che l'algoritmo abbia effettivamente qualcosa da imparare.
# Senza queste righe, i dati sarebbero puramente casuali e nessun algoritmo al mondo riuscirebbe a trovare un senso.
punteggio_rischio = (df['nuovo_utente'] * 0.4) + \
                    (df['ora_notturna'] * 0.3) + \
                    (df['importo'] / 2000 * 0.3)

df['truffa'] = (punteggio_rischio + np.random.normal(0, 0.1, data_size) > 0.7).astype(int)

# Salviamo in CSV
cartella_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_file = os.path.join(cartella_corrente, 'ordini_ecommerce.csv')
df.to_csv(percorso_file, index=False)
print("CSV creato con successo!")
