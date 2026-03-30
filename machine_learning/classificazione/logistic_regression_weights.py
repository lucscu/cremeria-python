import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. Carichiamo il dataset
iris = load_iris()
X = iris.data  # Le 4 dimensioni (Sepal L, Sepal W, Petal L, Petal W)
y = iris.target # Le 3 specie
feature_names = iris.feature_names

# 2. Creiamo e addestriamo il modello
# Usiamo 'multi_class' per gestire le 3 specie di Iris
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 3. Estraiamo i pesi (coefficienti)
# Il modello crea una riga di pesi per ogni specie (One-vs-Rest)
weights = pd.DataFrame(model.coef_, 
                       columns=feature_names, 
                       index=iris.target_names)

print("Pesi assegnati dall'algoritmo per ogni dimensione:")
print(weights)

# 4. Estraiamo il Bias (Intercetta)
# Scikit-learn ne calcola uno per ogni classe (Setosa, Versicolor, Virginica)
bias = pd.DataFrame(model.intercept_, 
                    index=iris.target_names, 
                    columns=['Bias'])

print("\nBias (Intercetta) per ogni specie:")
print(bias)
