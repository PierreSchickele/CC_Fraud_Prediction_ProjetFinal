#Importation des librairies
import streamlit as st
import pandas as pd
import plotly.express as px

#CONFIG
st.set_page_config(  page_title="Exploration et analyses des données",
  page_icon="🔬",
  layout="centered"
  )

st.markdown("""
            👋 Bienvenue dans l'exploration et analyses des données !
            """)

#Lecture du dataset
data = pd.read_csv("dfm_all.csv")

# Afficher les données dans Streamlit
st.write("Données échantillonnées (5%) :")
st.write(data)

# Viz 1 Top 10 des secteurs fraudés

# Calculer le nombre total d'occurrences pour chaque secteur d'emploi
total_by_sector = data['job_sector'].value_counts().reset_index()
total_by_sector.columns = ['job_sector', 'total_occurrences']

# Calculer le nombre d'occurrences de fraudes par secteur d'emploi
fraud_by_sector = data.groupby('job_sector')['is_fraud'].mean().reset_index()
fraud_by_sector.columns = ['job_sector', 'fraud_proportion']

# Fusionner les deux DataFrames pour obtenir les proportions de fraudes et les totaux
fraud_by_sector = pd.merge(fraud_by_sector, total_by_sector, on='job_sector')

# Sélectionner les 10 premiers secteurs par proportion de fraudes
top_10_fraud_by_sector = fraud_by_sector.sort_values('fraud_proportion', ascending=False).head(10)

# Inverser l'ordre des données pour que les valeurs aillent du plus grand au plus petit
top_10_fraud_by_sector = top_10_fraud_by_sector[::-1]

# Créer le graphique avec Plotly Express
fig = px.bar(top_10_fraud_by_sector, y='job_sector', x='fraud_proportion', color='fraud_proportion',
            labels={'job_sector': "Secteur d'emploi", 'fraud_proportion': "Proportion de fraudes"},
            title="Top 10 des secteurs d'emploi par proportion de fraudes",
            orientation='h')  # Orienté horizontalement

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

# Viz 2  

# Créer un dictionnaire de correspondance entre les chiffres des mois et leurs noms
day_of_the_week_names = {
    0: 'Lundi',
    1: 'Mardi',
    2: 'Mercredi',
    3: 'Jeudi',
    4: 'Vendredi',
    5: 'Samedi',
    6: 'Dimanche'
}

# Remplacer les chiffres des mois par leurs noms correspondants dans le DataFrame
data['day_of_the_week'] = data['day_of_the_week'].map(day_of_the_week_names)

# Définir l'ordre des catégories pour la colonne des mois
ordered_day_of_the_weeks = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
data['day_of_the_week'] = pd.Categorical(data['day_of_the_week'], categories=ordered_day_of_the_weeks, ordered=True)

# Calculer la proportion des fraudes pour chaque jour de la semaine
fraud_by_day_of_week = data.groupby('day_of_the_week')['is_fraud'].mean().reset_index()

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque jour de la semaine
fig = px.bar(fraud_by_day_of_week, x='day_of_the_week', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'day_of_the_week': 'Jour de la semaine'},
             title='Proportion de fraudes par jour de la semaine')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 3 

# Créer un dictionnaire de correspondance entre les chiffres des mois et leurs noms
month_names = {
    6: 'Juin',
    7: 'Juillet',
    8: 'Août',
    9: 'Septembre',
    10: 'Octobre',
    11: 'Novembre',
    12: 'Décembre'
}

# Remplacer les chiffres des mois par leurs noms correspondants dans le DataFrame
data['month'] = data['month'].map(month_names)

# Définir l'ordre des catégories pour la colonne des mois
ordered_months = ['Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
data['month'] = pd.Categorical(data['month'], categories=ordered_months, ordered=True)

# Calculer la proportion des fraudes pour chaque mois
fraud_by_month = data.groupby('month')['is_fraud'].mean().reset_index()

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque mois
fig = px.bar(fraud_by_month, x='month', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'month': 'Mois'},
             title='Proportion de fraudes par mois')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 4

# Calculer la somme des fraudes pour chaque heure de la journée
fraud_by_hour = data.groupby('hour')['is_fraud'].mean().reset_index().sort_values(by='is_fraud', ascending=True)

# Créer un graphique à barres pour visualiser la somme des fraudes pour chaque heure de la journée
fig = px.bar(fraud_by_hour, x='hour', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Somme des fraudes', 'hour': 'Heure'},
             title='Proportion de fraudes par heure de la journée')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 5

# Calculer la proportion des fraudes pour chaque État
fraud_by_state = data.groupby('state')['is_fraud'].mean().reset_index()

# Trier les données par ordre croissant de la proportion de fraudes
fraud_by_state_sorted = fraud_by_state.sort_values(by='is_fraud', ascending=False).head(10)

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque État
fig = px.bar(fraud_by_state_sorted, x='state', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'state': 'État'},
             title='Top 10 des États par proportions de fraudes')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 6

fig = px.histogram(data, x="gender", color="is_fraud", barmode='group',
                   category_orders={"gender": data['gender'].value_counts().index.to_list()},
                   labels={'is_fraud': 'Fraude', 'gender': 'Genre'},
                   title='Distribution de fraudes par genre')

# Ajouter les étiquettes de données sur chaque barre
fig.update_traces(texttemplate='%{y}', textposition='outside')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 7

data['is_fraud_label'] = data['is_fraud'].map({0: 'Transaction normale', 1: 'Transaction frauduleuse'})

# Créer un graphique à boîtes avec les nouvelles étiquettes
fig = px.box(data, x='amt', y='is_fraud_label')

# Mettre à jour la mise en page
fig.update_layout(
    title='Répartition des montants',
    showlegend=False,
    height=700, width=1200
)

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)