# Voivodship Data Map
(C) Jarema Piekutowski 2024

## Overview

This application is a Streamlit-based web app that allows users to create a map of Polish voivodships with user-defined numerical data. The map visually represents the data using color coding, and includes annotations for the regions.

## Features
- Input numerical data for each Polish voivodship.
- Customize the map title.
- Generate a choropleth map with annotations.

## Requirements
- Python 3.x
- Streamlit
- pandas
- matplotlib
- geopandas

## Installation

1) Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

2) Install required libraries:

```bash
pip install streamlit pandas matplotlib geopandas
```

3) Ensure you have the shapefile for Polish voivodships:

The shapefile should be located in a directory named map and named Województwa.shp.

Example directory structure:

```arduino
<repository_directory>/
├── map/
│   └── Województwa.shp
└── app.py
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

### Interacting with the app:

- Open your web browser and navigate to the provided local URL (typically http://localhost:8501).
- Input the numerical data for each voivodship in the provided fields.
- Enter a title for your map.
- Click the "Generate Map" button to create and display the map.

