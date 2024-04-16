#Importation des librairies
import streamlit as st
import pandas as pd
import plotly.express as px

#CONFIG
st.set_page_config(  page_title="dashboard",
  page_icon="💸",
  layout="centered"
  )



#Lecture du dataset
data = pd.read_csv("src/dfm_all.csv")

# Afficher les données dans Streamlit
st.write("Données échantillonnées (20%) :")
st.write(data)

# Viz 1 Top 10 des secteurs fraudés

# Calculer le nombre d'occurrences de fraudes par secteur d'emploi
fraud_by_sector = data.groupby('job_sector')['is_fraud'].count().reset_index()

# Sélectionner les 10 premiers secteurs avec le plus grand nombre de fraudes
top_10_fraud_by_sector = fraud_by_sector.sort_values('is_fraud', ascending=True).head(10)

# Créer le graphique avec Plotly Express
fig = px.bar(top_10_fraud_by_sector, y='job_sector', x='is_fraud', color='is_fraud',
            labels={'job_sector': "Secteur d'emploi", 'is_fraud': "Nombre d'occurrences de fraudes"},
            title="Top 10 des secteurs d'emploi avec le plus grand nombre de fraudes")

# Afficher le graphique dans Streamlit
st.plotly_chart(fig)

# Viz 2  

# Calculer la moyenne des fraudes pour chaque jour de la semaine
fraud_by_day_of_week = data.groupby('day_of_the_week')['is_fraud'].mean().reset_index()

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque jour de la semaine
fig = px.bar(fraud_by_day_of_week, x='day_of_the_week', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'day_of_the_week': 'Jour de la semaine'},
             title='Proportion de fraudes par jour de la semaine')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 3 

# Calculer la moyenne des fraudes pour chaque mois
fraud_by_month = data.groupby('month')['is_fraud'].mean().reset_index()

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque mois
fig = px.bar(fraud_by_month, x='month', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'month': 'Mois'},
             title='Proportion de fraudes par mois')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 4

# Calculer la somme des fraudes pour chaque heure de la journée
fraud_by_hour = data.groupby('hour')['is_fraud'].sum().reset_index().sort_values(by='is_fraud', ascending=True)

# Créer un graphique à barres pour visualiser la somme des fraudes pour chaque heure de la journée
fig = px.bar(fraud_by_hour, x='hour', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Somme des fraudes', 'hour': 'Heure'},
             title='Somme des fraudes par heure de la journée')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 5

# Calculer la moyenne des fraudes pour chaque État
fraud_by_state = data.groupby('state')['is_fraud'].mean().reset_index()

# Trier les données par ordre croissant de la proportion de fraudes
fraud_by_state_sorted = fraud_by_state.sort_values(by='is_fraud', ascending=False)

# Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque État
fig = px.bar(fraud_by_state_sorted, x='state', y='is_fraud', color='is_fraud',
             labels={'is_fraud': 'Proportion de fraudes', 'state': 'État'},
             title='Proportion de fraudes par état')

# Afficher le graphique dans Streamlit
st.plotly_chart(fig, use_container_width=True)

# Viz 6

fig = px.histogram(data, x="gender", color="is_fraud", barmode='group',
                   category_orders={"gender": data['gender'].value_counts().index.to_list()},
                   labels={'is_fraud': 'Fraude', 'gender': 'Genre'},
                   title='Distribution des fraudes par genre')

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