import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


# Function to create a map
def create_map(df, title):
    fig, ax = plt.subplots(1, figsize=(8, 8))
    df.plot(column='value', ax=ax, cmap='RdYlBu', linewidth=0.8, edgecolor='gray', legend=True)
    ax.axis('off')
    for idx, row in df.iterrows():
        if row["value"] > 0.9 * max(df["value"]) or row["value"] < 2 * min(df["value"]):
            annot_color = "white"
        else:
            annot_color = "black"
        text = f"{row['region']}\n{round(row['value'])}"
        plt.annotate(text=text, xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                     horizontalalignment='center', size=8, color=annot_color)
    plt.title(title)
    st.pyplot(fig)


# Streamlit app
st.title("Mapa województw z danymi")

# Input for numerical data for each voivodship
st.subheader("Wpisz dane dla każdego województwa:")
data = {
    "voivodship": ["dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie", "małopolskie",
                   "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie", "śląskie",
                   "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"],
    "value": [st.number_input(region, min_value=0) for region in [
        "dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie", "małopolskie",
        "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie", "śląskie",
        "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"]]
}

# Input for map title
map_title = st.text_input("Wpisz tytuł mapy")

# Button to generate the map
if st.button("Generate Map"):
    # Create a DataFrame from the input data
    df_input = pd.DataFrame(data)

    # Read map file
    mapa_woj = gpd.read_file("map/Województwa.shp")

    # Rename columns to match
    mapa_woj = mapa_woj.rename(columns={"JPT_KOD_JE": "TERYT", "JPT_NAZWA_": "region"})
    mapa_woj.region = mapa_woj.region.str.lower()

    # Merge the input data with the map data
    df_input = df_input.rename(columns={"voivodship": "region"})
    df_map = mapa_woj.merge(df_input, how="left", on="region")

    # Add coords for annotation
    df_map['coords'] = df_map['geometry'].apply(lambda x: x.representative_point().coords[:])
    df_map['coords'] = [coord[0] for coord in df_map['coords']]

    # Create and display the map
    create_map(df_map, map_title)
