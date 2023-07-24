import random
import csv

def generate_dataset():
    """Generates a dataset of sepal length and sepal width for three species of iris."""
    setosa_data = []
    versicolor_data = []
    virginica_data = []
    for _ in range(50):
        setosa_data.append(('setosa', random.uniform(4.3, 5.1), random.uniform(2.0, 2.8)))
        versicolor_data.append(('versicolor', random.uniform(5.1, 7.0), random.uniform(2.3, 3.2)))
        virginica_data.append(('virginica', random.uniform(5.8, 7.9), random.uniform(2.7, 3.8)))
    return setosa_data + versicolor_data + virginica_data

def export_dataset(dataset, filename):
    """Exports a dataset to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Species', 'Sepal Length', 'Sepal Width'])
        for species, sepal_length, sepal_width in dataset:
            writer.writerow([species, sepal_length, sepal_width])


dataset = generate_dataset()
export_dataset(dataset, 'dataset.csv')
