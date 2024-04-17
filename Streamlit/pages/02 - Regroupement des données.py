import joblib
import streamlit as st
import pandas as pd
import pydeck as pdk
import hdbscan

## CONFIG (Call this only once at the beginning)
st.set_page_config(
    page_title="Clustering",
    page_icon="🗺️",
    layout="centered"
)

# PAGE CLUSTERING
# Sidebar section for clustering model
st.markdown("""
    Le but du modèle présent était de regrouper les transactions selons leur positionnement géographique via un modèle HDBSCAN.
    Par la suite, nous avons regardé le pourcentage de transactions frauduleuses parmis les clusters.
    Nous sommes donc arrivés sur un modèle qui pouvait regroupé les fraudes par clusters avec une précision de 55,65 %
""")

st.title('Clustering des transactions (HDBSCAN)')

st.sidebar.header("Modèle de clustering")
st.sidebar.write("Cette section affiche les résultats du modèle de clustering HDBSCAN.")
st.sidebar.markdown("---")

# Chargement des datas et modèle
data = joblib.load('data.joblib')
model = joblib.load('hdb.joblib')
base_data = joblib.load('base_data.joblib')

# if 'data' in st.session_state:
#     data = st.session_state.data
    
# transformation du data
model.fit(data)

cluster_labels = model.labels_.astype('int64')

base_data.loc[:, 'cluster'] = cluster_labels
data_geo_assigned = base_data[base_data['cluster'] != -1]

# Définir le centre de la carte et le niveau de zoom pour afficher toutes les données
center_longitude = data_geo_assigned['merch_long'].mean()
center_latitude = data_geo_assigned['merch_lat'].mean()
zoom_level = 2

# Créer une carte interactive avec pydeck
layer = pdk.Layer(
    'ScatterplotLayer',
    data_geo_assigned,
    get_position='[merch_long, merch_lat]',
    get_fill_color='[cluster, 0, 255, 255]',
    get_radius=20000,
    pickable=True
)

view_state = pdk.ViewState(
    longitude=center_longitude,
    latitude=center_latitude,
    zoom=zoom_level
)

# Créer une carte Mapbox
map_hdb = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style='mapbox://styles/mapbox/light-v9',
)

# Afficher la carte interactive
st.pydeck_chart(map_hdb)

# Calculer le nombre total de fraudes par cluster
fraud_count = data_geo_assigned.groupby('cluster')['is_fraud'].sum()

# Calculer le pourcentage de fraudes pour chaque cluster
fraud_percentage = data_geo_assigned.groupby('cluster')['is_fraud'].mean() * 100

# Créer un DataFrame à partir des résultats pour faciliter la visualisation avec Plotly Express
fraud_data_hdb = pd.DataFrame({'Cluster': fraud_count.index, 
                            'Nombre de fraudes': fraud_count.values,
                            'Pourcentage de fraudes': fraud_percentage.values})

# Trier les données par nombre de fraudes décroissant
fraud_data_hdb = fraud_data_hdb.sort_values(by='Nombre de fraudes', ascending=False)

# Créer l'application Streamlit
st.title('Pourcentage de fraudes par cluster (HDBSCAN)')
st.write('Visualisation du pourcentage de fraudes dans chaque cluster détecté par HDBSCAN.')

# Afficher le graphique à barres avec Streamlit
st.bar_chart(fraud_data_hdb.set_index('Cluster')['Pourcentage de fraudes'])

# Afficher le DataFrame des données de fraude pour référence
st.write('Données de fraude par cluster :')
st.write(fraud_data_hdb)

