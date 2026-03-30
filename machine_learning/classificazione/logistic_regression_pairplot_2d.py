import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# 1. Carichiamo i dati
iris = datasets.load_iris()
# Usiamo solo le ultime due colonne (Petal Length, Petal Width) per il grafico 2D
X = iris.data[:, [2, 3]] 
y = iris.target

model = LogisticRegression(random_state=42)
model.fit(X, y)

plt.figure(figsize=(10, 6))
plot_decision_regions(X, y, clf=model, legend=2)

plt.xlabel('Lunghezza Petalo (cm)')
plt.ylabel('Larghezza Petalo (cm)')
plt.title('Confini di Decisione della Logistic Regression')
plt.show()
