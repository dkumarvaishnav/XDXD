import matplotlib.pyplot as plt
import pandas as pd

# Assuming "iris.data" is in the same directory
data = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

setosa_data = data[data['species'] == 'Iris-setosa']
versicolor_data = data[data['species'] == 'Iris-versicolor']
virginica_data = data[data['species'] == 'Iris-virginica']

plt.scatter(setosa_data['sepal_length'], setosa_data['sepal_width'], label='Setosa', c='r')
plt.scatter(versicolor_data['sepal_length'], versicolor_data['sepal_width'], label='Versicolor', c='g')
plt.scatter(virginica_data['sepal_length'], virginica_data['sepal_width'], label='Virginica', c='b')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs. Sepal Width by Species')
plt.legend()
plt.show()
