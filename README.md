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

[Previous data analysis content remains unchanged...]

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