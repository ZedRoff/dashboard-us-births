import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

file_path = "us_births_2016_2021.csv"  # Remplacez par le chemin vers votre fichier
df = pd.read_csv(file_path)

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,5),facecolor="#FFFFFF")
FACECOLOR = 'xkcd:very light pink'


a=df.groupby('Education Level Code')['Number of Births'].sum().reset_index()

#-9 in x axis create a problem
edu_codes=a['Education Level Code'].unique()
edu_codes_str = list( map(str,edu_codes) )

#ax1.grid(axis='y',zorder=0)
ax1.bar(edu_codes_str,a['Number of Births'],color='purple',edgecolor="black")
ax1.set_facecolor(FACECOLOR)
#ax1.set_ylim([3,5])
ax1.set_xlabel("Education Level Code")
ax1.set_ylabel("Avg Baby Births")
ax1.set_title("Avg Baby Births by Mother's Education Level",loc='left') 

# Create table beside the plot to serve as legend. Use matplotlib table method.
table_cells = np.array([df['Education Level Code'].unique(),
                        df["Education Level of Mother"].unique()]).transpose()

# Level 8 string (PhD etc) is too long, insert a line break.
table_cells[7,1] = 'Doctorate (PhD, EdD) or \nProfessional Degree (MD, DDS, DVM, LLB, JD)'

table_headers = ["Code","Education Level"]
cell_colors = np.array([["pink"]*9,[FACECOLOR]*9]).transpose()
col_header_colors = ["lightblue"]*2

table = ax2.table(cellText=table_cells,colLabels=table_headers,colWidths=[0.1,0.9],cellColours=cell_colors,
                  cellLoc='center',colColours=col_header_colors,bbox=[0,0,1,1])
table.set_fontsize(22)
ax2.axis('off')
fig.suptitle("Averaged over all states, gender, and years (2016-2021)",fontsize=22)
plt.subplots_adjust(top=0.85)

plt.show()