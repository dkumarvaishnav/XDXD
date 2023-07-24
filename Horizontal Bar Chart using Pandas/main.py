import pandas as pd
import matplotlib.pyplot as plt

# Assuming "DigiDB_digimonlist.csv" is in the same directory
data = pd.read_csv('DigiDB_digimonlist.csv')

# Select the first five rows and relevant columns 'Digimon', 'Lv50 Atk', and 'Lv50 Spd'
selected_data = data.loc[:4, ['Digimon', 'Lv50 Atk', 'Lv50 Spd']]

# Set the 'Digimon' column as the index
selected_data.set_index('Digimon', inplace=True)

# Create the horizontal bar chart using Pandas
selected_data.plot.barh()
plt.xlabel('Stats')
plt.title('Lv50 Atk and Lv50 Spd for the First Five Digimon')
plt.show()
