import pandas as pd
from plotnine import ggplot, aes, geom_histogram, scale_fill_gradient, labs, theme_minimal

# Assuming "DigiDB_digimonlist.csv" is in the same directory
df = pd.read_csv('DigiDB_digimonlist.csv')

# Rename the column with spaces to a valid column name
df = df.rename(columns={'Lv 50 HP': 'Lv50_HP'})

# Create the histogram using plotnine
(ggplot(df, aes(x='Lv50_HP', fill='..count..'))
 + geom_histogram(binwidth=10, color='black')
 + scale_fill_gradient(low='cyan', high='blue')
 + labs(title='Histogram of Lv 50 HP', x='Lv 50 HP', y='Count')
 + theme_minimal()
).draw()
