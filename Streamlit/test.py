import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

from math import radians, sin, cos, sqrt, atan2

from sklearn.preprocessing import  OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans, DBSCAN, MeanShift, estimate_bandwidth
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import silhouette_score

## CONFIG (Call this only once at the beginning)
st.set_page_config(
    page_title="E-commerce",
    page_icon="wide",
    layout="centered"
)

### TITLE AND TEXT
st.title("Build dashboards with Streamlit 🎨")

st.markdown("""
    Welcome to this awesome `streamlit` dashboard. This library is great to build very fast and
    intuitive charts and application running on the web. Here is a showcase of what you can do with
    it. Our data comes from an e-commerce website that simply displays samples of customer sales. Let's check it out.
    Also, if you want to have a real quick overview of what streamlit is all about, feel free to watch the below video 👇
""")

#

df = pd.read_csv("fraud test.csv")
df.describe(include="all")

# Séparation des données en deux dataset selon le coté frauduleux de la transaction
df_frauds = df[df['is_fraud'] == 1]
sample = df[df['is_fraud'] == 0]

# Échantillonnage du dataset de transactions non frauduleuses pour avoir la même taille que le dataset de transactions frauduleuses
dsam = sample.sample(2145, random_state=0)

# Fusion des deux datasets
frames = [df_frauds, dsam]
result = pd.concat(frames)

# Mélange des données dans le dataset
result = result.sample(frac = 1)

# Définition des colonnes à enlever pour le modèle de clustering
to_drop = ['cc_num', 'first', 'last', 'street', 'city' ,'state', 'zip', 'trans_num']
clean_data = result.drop(columns=to_drop)

data_geo = clean_data[["merch_lat", "merch_long", "is_fraud"]]

# Première répartition des transactions

# Créer une palette de couleurs personnalisée avec le rouge pour les valeurs de is_fraud égales à 1
color_scale = px.colors.diverging.RdYlBu_r

# Modifier la couleur pour les valeurs de is_fraud égales à 1 en rouge
color_scale[0] = 'blue'

# Définir le centre de la carte et le niveau de zoom pour afficher toutes les données
center_longitude = data_geo['merch_long'].mean()  # Utiliser la moyenne des longitudes comme centre
center_latitude = data_geo['merch_lat'].mean()  # Utiliser la moyenne des latitudes comme centre
zoom_level = 2  # Niveau de zoom pour afficher toutes les données

# Filtrer les données frauduleuses et non frauduleuses
df_fraud = df[df['is_fraud'] == 1]
df_non_fraud = df[df['is_fraud'] == 0]

# Créer la carte avec Plotly Express
fig = px.scatter_mapbox(df_non_fraud, lat="merch_lat", lon="merch_long", color_discrete_sequence=["blue"], zoom=2, mapbox_style="open-street-map")
fig.add_scattermapbox(lat=df_fraud["merch_lat"], lon=df_fraud["merch_long"], marker=dict(color="red"), name="Fraudulent")

# Afficher la carte dans Streamlit
st.plotly_chart(fig)

fig = px.scatter_mapbox(
        data_geo,
        lat="merch_lat",
        lon="merch_long",
        color="is_fraud",
        mapbox_style="carto-positron",
        title="Répartition géographiques de l'échantillon des transactions",
        color_continuous_scale=color_scale,
        center=dict(lon=center_longitude, lat=center_latitude), 
        zoom=zoom_level
)

fig.show()