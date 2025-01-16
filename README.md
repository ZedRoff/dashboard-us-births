# 📊 US Birth Data Visualization

This project provides a suite of graphs to visualize and analyze US Births data from 2016 to 2021. The visualizations include pie charts, bar charts, choropleth maps, and more to show the distribution of births across the US. These tools aim to present meaningful insights into trends and patterns in US Birth Data.

---

## 📖 Table of Contents

1. [Developers](#developers)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)

---

## 👨‍💻 Developers

- **Aman GHAZANFAR**  
- **Justine HAKIM**

We are two students at **ESIEE Paris**, and this project was created for educational purposes as part of the *"Python E3FI Program"* directed by **Daniel COURIVAUD**.

---

## ✨ Features

- Multiple visualizations, including pie charts, bar charts, and heatmaps.
- Choropleth maps for analyzing geographic trends across US states.
- Interactive dashboards powered by Plotly and Dash.
- Easily extensible and modular code structure for scalability.

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

---

## 📥 Installation

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

## 🚀 Usage

Here is a link to the video showcasing the dashboard: [Demo Video Link](#)

To run the application locally, execute:
```bash 
    python main.py
``` 
Access the dashboard in your browser at `http://127.0.0.1:8050`

<hr />

🌟 Happy Visualizing!
