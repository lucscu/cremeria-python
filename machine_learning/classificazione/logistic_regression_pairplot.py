import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carichiamo il dataset Iris direttamente da Seaborn
# (Seaborn lo ha già pulito e pronto all'uso come DataFrame)
iris = sns.load_dataset('iris')

# 2. Creiamo il Pairplot
# 'hue' è il parametro magico: dice a Python di colorare i punti in base alla specie
sns.pairplot(iris, hue='species', palette='bright')

# 3. Mostriamo il grafico
plt.show()
