import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

# 1. Caricamento Dati
iris = datasets.load_iris()
X = iris.data  # Usiamo tutte e 4 le colonne qui per massima precisione!
X = iris.data[:, :2]
y = iris.target

# 2. Dividiamo in Train (Allenamento) e Test (Verifica)
# Usiamo il 30% dei dati per il test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Allenamento Modello
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 5. Predizione
y_pred = model.predict(X_test)

# 6. Matrice di Confusione
cm = confusion_matrix(y_test, y_pred)

# 7. Visualizzazione
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(cmap='Blues', ax=ax)

plt.title('Matrice di Confusione: Quante volte il modello si è "confuso"?')
plt.xlabel('Previsione del Modello')
plt.ylabel('Realtà (Specie Vera)')
plt.show()
