from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 1. Carichiamo il dataset Iris
iris = datasets.load_iris()
X = iris.data
X = iris.data[:, :2]
y = iris.target

# 2. Dividiamo in Train (Allenamento) e Test (Verifica)
# Usiamo il 30% dei dati per il test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Creazione e addestramento del modello
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 5. Facciamo le predizioni sui dati di TEST (quelli che il modello non ha mai visto)
y_pred = model.predict(X_test)

# B. Precision, Recall e F1-Score
print("REPORT DI CLASSIFICAZIONE")
print("="*30)
print(classification_report(y_test, y_pred, target_names=iris.target_names))