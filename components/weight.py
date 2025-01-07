import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

# Charger les données depuis le fichier CSV
file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

sns.histplot(data=df.loc[:][['Gender', 'Average Birth Weight (g)']], hue='Gender', x='Average Birth Weight (g)')
plt.xlabel('Average weight of birth')
plt.ylabel('Count')
plt.title('Distribution of Average Birth Weight by Gender')

# Display the plot
plt.show()