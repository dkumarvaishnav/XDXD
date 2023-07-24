import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from "DigiDB_digimonlist.csv" into the 'df' DataFrame
df = pd.read_csv('DigiDB_digimonlist.csv')

# Select the columns you want to plot
columns_to_plot = ['Lv50 SP', 'Lv50 Atk', 'Lv50 Def', 'Lv50 Int', 'Lv50 Spd']

# Set the pastel color palette
sns.set_palette("pastel")

# Create the boxplot
sns.boxplot(data=df[columns_to_plot])

# Set plot title and labels
plt.title('Boxplot of Lv50 SP, Atk, Def, Int, and Spd')
plt.xlabel('Attributes')
plt.ylabel('Values')

# Show the plot
plt.show()
