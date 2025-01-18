# 📊 US Birth Data Visualization

This project provides a suite of graphs to visualize and analyze US Births data from 2016 to 2021. The visualizations include pie charts, bar charts, choropleth maps, and more to show the distribution of births across the US. These tools aim to present meaningful insights into trends and patterns in US Birth Data.

---

## 📖 Table of Contents

1. [Developers](#developers)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [User Guide](#user-guide)
6. [Developer Guide](#developer-guide)
7. [Data Analysis](#data-analysis)
8. [Data](#data)
9. [Usage](#usage)
10. [Copyright](#copyright)

---

## 👨‍💻 Developers

- **Aman GHAZANFAR**  
- **Justine HAKIM**

We are two students at **ESIEE Paris**, and this project was created for educational purposes as part of the *"Python E3FI Program"* directed by **Daniel COURIVAUD**.

---

## ✨ Features

- Multiple visualizations, including pie charts, bar charts, and heatmaps
- Choropleth maps for analyzing geographic trends across US states
- Interactive dashboards powered by Plotly and Dash
- Easily extensible and modular code structure for scalability

---

## 🗂️ Project Structure

```
.
├── README.md
├── assets
│   ├── image.png
│   ├── style.css
│   └── temp_map.html
├── components
│   ├── age_glob.py
│   ├── age_loc.py
│   ├── education_gender_glob.py
│   ├── education_gender_loc.py
│   ├── education_glob.py
│   ├── education_loc.py
│   ├── gender_glob.py
│   ├── gender_loc.py
│   ├── heatmap_loc.py
│   ├── histogramme_loc.py
│   ├── legend_code.py
│   ├── mother_age_glob.py
│   ├── mother_age_loc.py
│   ├── tendance_glob.py
│   ├── tendance_loc.py
│   ├── us_map.py
│   ├── weight_glob.py
│   └── weight_loc.py
├── data
│   ├── us-states.json
│   └── us_births_2016_2021.csv
├── main.py
├── requirements.txt
└── views
    ├── age.py
    ├── births.py
    ├── education.py
    ├── gender.py
    ├── glob.py
    ├── global_stats.py
    ├── header.py
    ├── homepage.py
    ├── local.py
    └── weight.py

5 directories, 36 files
```

---

## ⚙️ Requirements

To run this project, ensure you have:

- **Python 3.7** or higher
- The following Python libraries:
  - `pandas`
  - `plotly`
  - `shapely`
  - `json`
  - `dash`
  - `dash_bootstrap_components`
  - `numpy`

---

## 📥 User Guide

1. Clone the repository:

```bash
git clone https://git.esiee.fr/ghazanfa/dashboard-us-births.git
cd dashboard-us-births
```

2. Install the dependencies:
```bash 
pip install -r requirements.txt
``` 

3. Ensure the `data` folder contains the required files:
   - `us_births_2016_2020.csv`
   - `us-states.json`
   
If the files are missing, run the `get_data.py` file

---

## 🛠️ Developer Guide

In order to add a new graph, you have to create a new component inside the `components` folder. Please take note that graphs inside this project must be developed in `plotly` for full compatibility with dash. You have to create a `generate()` function inside it, create your `fig` with all it's `update_layout` functions for instance. Then once the `fig` variable is fully setuped, you have to return it. We have two use cases:

- Either it's a global graph: 
    - If it fits one of our categories, simply import your module and call `dcc.Graph(figure=your_component.generate())`. In this case do not forget to go to `views/glob.py` and add the ref to the sidebar. And finally, go to `main.py` file and change the `callback` part to Input and Output the right things as the other global prefixed views do.
    - If not, then create your own view and follow the pattern of other files to create something similar.
- Or it's a local graph:
    - Then you have to modify the `payload()` function inside the `main.py` file. Input a new div block that has the className `graph_block` inside the `graphs_block` class. The procedure to call your component is the same as a global graph. Just follow the patterns of other blocks.

In order to add a new page to the website, you have to create a new view inside the `views` folder. This file can have whatever function you'd like, but it has to return a well-structured dash page. Then, go to `main.py` and change the `callback` part of this file such that the Input and Output are structured the same as the other ones that are put inside this file. 

---

## 📈 Data Analysis

We did data analysis about US Births from 2016 to 2021. And these are the conclusions we got:

We did data analysis about US Births from 2016 to 2021. And these are the conclusions we got : 
- Data shows a strong link between education levels and birth rates. Level 3 leads with 5,775,918 births, likely due to its large population and family-starting age. Levels 6 and 4 follow with 4,653,184 and 4,425,269 births, reflecting career-family balance or paused education for family life. Lower levels (1, 2) and higher levels (7, 8) have fewer births, with level 8 (627,705) likely reflecting delayed childbearing due to extended education. Overall, intermediate education levels dominate births, driven by demographic and life-stage factors.
- Graphs shows a clear trend: higher education levels are associated with older maternal age at childbirth. Mothers with a doctorate or professional degree have the highest average age at 33.7 years, followed by master's (32.8 years) and bachelor's (31.2 years). Those with an associate degree average 29.9 years, while high school graduates average 26.5 years, and those without a diploma are youngest at 25.1 years. This suggests that higher education delays parenthood, likely due to extended studies and career focus, while lower education levels may lead to earlier childbirth, influenced by economic or cultural factors.
- Graphs shows that the peak of births occurs in the [26, 28] age range with 6,511,376 births, followed by the [30, 32] and [28, 30] ranges. Births decline in older age groups, with fewer births in the [22, 24] and [34, 36] ranges, suggesting that the optimal childbirth age is between 26 and 32. Younger women may delay motherhood for education or career, while older women face fertility challenges or have already started families.
- Graphs enlightened the average age of mothers with a median of 29.6 years. The interquartile range (IQR) is between 27 and 32 years, covering the central 50% of ages. The whiskers extend from 24 to 36 years, indicating the full age range without outliers. The plot is slightly right-skewed, suggesting more older mothers. Overall, it shows a moderate distribution, with most mothers between 24 and 36 years, and a median around 30.
- Our dashboard also shows the gender distribution (M: Male, F: Female) from 2016 to 2021. The gender proportions are consistent across the years, with a slight male majority. In 2016, the distribution was M: 51.1% and F: 48.9%, and remained nearly the same in the following years. The variations are minimal, ranging from 0.1% to 0.2%, indicating a stable gender distribution over the six years. The data highlights a slight male majority with no significant gender imbalances during the period analyzed.
- The histogram shows the distribution of average birth weights, ranging from 2600 g to 3600 g, with most births between 3100 g and 3400 g. Boys dominate the higher weight ranges (3400 g to 3600 g), while girls are more common in the 3000 g to 3400 g range. The highest total weight is around 3200 g to 3300 g, with girls being slightly heavier in this range. Overall, boys tend to be slightly heavier in the higher weight ranges.
- The map shows U.S. states colored based on birth numbers, with light beige representing low births and dark red indicating high births. States like Texas (TX) and California (CA) are marked in dark red, reflecting over 400k births, while states like Wyoming (WY) and Alaska (AK) are in light beige, indicating fewer than 50k births. Densely populated states on the East and West coasts have higher birth numbers, while less populated states in the Midwest and Rocky Mountains show lower figures.
- From 2016 to 2020, births steadily declined from around 4 million to 3.5 million, likely due to decreasing birth rates and socio-economic factors. However, in 2021, there was a slight recovery, possibly reflecting post-pandemic effects or birth rate support policies. This decline aligns with a global trend of lower birth rates, economic impacts, and sociocultural shifts, such as delayed childbearing. The increase in 2021 warrants further analysis to understand potential recovery patterns.


---

## 📊 Data

The data in this dataset was obtained using CDC's WONDER retrieval tool on the CDC Natality page.
Here is a link to the kaggle page for more information: [Link](https://www.kaggle.com/datasets/danbraswell/temporary-us-births/data)

---

## 🚀 Usage

Here is a link to the video showcasing the dashboard: [Demo Video Link](#)

To run the application locally, execute:
```bash 
python main.py
``` 
Access the dashboard in your browser at `http://127.0.0.1:8050`

---

## ⚖️ Copyright

I hereby declare on my honor that the code provided was produced by myself/ourselves.

🌟 Happy Visualizing!