import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1. CARICHIAMO IL FILE (Qui 'df' prende vita!)
# Assicurati che il nome tra virgolette sia identico a quello salvato
cartella_corrente = os.path.dirname(os.path.abspath(__file__))
percorso_file = os.path.join(cartella_corrente, 'ordini_ecommerce.csv')
df = pd.read_csv(percorso_file)

# 2. PREPARIAMO I DATI
# X sono le caratteristiche (tutto tranne la colonna truffa)
X = df.drop('truffa', axis=1) 
# y è la risposta corretta
y = df['truffa']

# 3. SPLIT (Allenamento e Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. IL MODELLO
# l'argomento class_weight:
# Default (None) Unweighted	"Tutti sono uguali". Rischio di ignorare le truffe perché sono poche.
# 'balanced'	Cost-Sensitive	"Le minoranze contano". Il modello diventa un detective molto più attento ai casi rari.
#
# con 'balanced' se ci sono 10 volte più onesti che truffatori, ogni errore commesso su una truffa "fà male" al modello 10 volte di più di un errore su un onesto.
model = LogisticRegression(random_state=42)
#model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# 5. RISULTATI
y_pred = model.predict(X_test)

# Invece di y_pred = model.predict(X_test)
# Prendiamo le probabilità della classe 1 (la seconda colonna)
probabilita = model.predict_proba(X_test)[:, 1]

# Abbassiamo la soglia a 0.3 (Sii molto sospettoso)
soglia = 0.3
y_pred_nuovo = (probabilita > soglia).astype(int)

print(f"Analisi completata su {len(df)} righe caricate dal file CSV")
print(classification_report(y_test, y_pred))
#print(classification_report(y_test, y_pred_nuovo))