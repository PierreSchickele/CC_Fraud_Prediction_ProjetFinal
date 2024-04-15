#Importation des librairies


import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt
import re
import os
import seaborn as sns
import warnings
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

## CONFIG
st.set_page_config(
    page_title="E-commerce",
    page_icon="💸",
    layout="centered"
  )


#Lecture du dataset

data = pd.read_csv("src/dfm_all.csv")


fraud_by_sector = data.groupby('job_sector')['is_fraud'].count().reset_index().sort_values(by='is_fraud', ascending=True)
st.bar_chart(data=fraud_by_sector, x='is_fraud', y='job_sector', color='is_fraud', width=1000, height=3000) #use_container_width=True)




# Viz 1 

# # Calculer la moyenne des is_fraud pour chaque genre
# fraud_by_sector = dfm_all.groupby('job_sector')['is_fraud'].count().reset_index().sort_values(by='is_fraud', ascending=True)

# # Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque genre
# fig = px.bar(fraud_by_sector, x='is_fraud', y='job_sector', color = 'is_fraud',
#              labels={'job_sector': 'job sector', 'is_fraud': 'Proportion de fraudes'},
#              title='Proportion de fraudes par secteur de job')

# # Mettre à jour la mise en page
# fig.update_layout(width=1000, height=3000)

# # Afficher le graphique
# fig.show()

# # nombre d'occurence ou j'ai 0 ou 1

# # On constate que les catégories de métiers plus à risque d'être victimes de fraude sont les Engineer ainsi que les officer



# viz 2


# # Calculer la moyenne des fraudes pour chaque jour de la semaine
# fraud_by_day_of_week = dfm_all.groupby('day_of_the_week')['is_fraud'].mean().reset_index()



# fig = px.bar(fraud_by_day_of_week, x='day_of_the_week', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'day_of_the_week': 'Jour de la semaine'},
#              title='Proportion de fraudes par jour de la semaine')

# # Mettre à jour la mise en page
# fig.update_layout(width=800, height=600)

# # Afficher le graphique
# fig.show()


# viz 3

# # 3) Calculer la moyenne des fraudes pour chaque mois
# fraud_by_month = dfm_all.groupby('month')['is_fraud'].mean().reset_index()



# fig = px.bar(fraud_by_month, x='month', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'month': 'Mois'},
#              title='Proportion de fraudes par mois')

# # Mettre à jour la mise en page
# fig.update_layout(width=800, height=600)

# # Afficher le graphique
# fig.show()


# viz 4

# # 4) Calculer la somme des fraudes pour chaque heure de la journée
# fraud_by_hour = dfm_all.groupby('hour')['is_fraud'].sum().reset_index().sort_values(by='is_fraud', ascending=True)



# fig = px.bar(fraud_by_hour, x='hour', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'hour': 'Heure'},
#              title='Proportion de fraudes par heure de la journée')

# # Mettre à jour la mise en page
# fig.update_layout(width=800, height=800)

# # Afficher le graphique
# fig.show()


# viz 5

# # 5) Calculer la moyenne des fraudes pour chaque état
# fraud_by_state = dfm_all.groupby('state')['is_fraud'].mean().reset_index()

# # Trier les données par ordre croissant de la proportion de fraudes
# fraud_by_state_sorted = fraud_by_state.sort_values(by='is_fraud', ascending=False)



# fig = px.bar(fraud_by_state_sorted, x='state', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'state': 'État'},
#              title='Proportion de fraudes par état')

# # Mettre à jour la mise en page
# fig.update_layout(width=1000, height=600)

# # Afficher le graphique
# fig.show()


# viz 6

# # 6) Créer un histogramme pour chaque genre avec les données côte à côte
# fig = px.histogram(dfm_all, x="gender", color="is_fraud", barmode='group',
#                    category_orders={"gender": dfm_all['gender'].value_counts().index.to_list()},
#                    labels={'is_fraud': 'Fraude', 'gender': 'Genre'},
#                    title='Distribution des fraudes par genre')

# # Ajouter les étiquettes de données sur chaque barre
# fig.update_traces(texttemplate='%{y}', textposition='outside')

# # Mettre à jour la mise en page
# fig.update_layout(width=1000)

# # Afficher le graphique
# fig.show()


# viz 7


# # 7) Remplacer les valeurs 0 et 1 par des étiquettes
# dfm_all['is_fraud_label'] = dfm_all['is_fraud'].map({0: 'Transaction normale', 1: 'Transaction frauduleuse'})

# # Créer un graphique à dispersion avec les nouvelles étiquettes
# fig = px.box(dfm_all, x='amt', y='is_fraud_label')

# # Mettre à jour la mise en page
# fig.update_layout(
#     title=go.layout.Title(text='Répartition des montants', x=0.5),
#     showlegend=False,
#     height=700, width=1200
# )

# # Afficher le graphique
# fig.show()










# VIZUALISATION VERSION STREAMLIT


# Viz 1

# # Calculer le nombre d'occurrences de fraudes pour chaque secteur d'emploi
# fraud_by_sector = dfm_all.groupby('job_sector')['is_fraud'].count().reset_index().sort_values(by='is_fraud', ascending=True)

# # Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque secteur d'emploi
# fig = px.bar(fraud_by_sector, y='job_sector', x='is_fraud', color='is_fraud',
#              labels={'job_sector': 'Secteur d\'emploi', 'is_fraud': 'Nombre d\'occurrences de fraudes'},
#              title='Nombre d\'occurrences de fraudes par secteur d\'emploi')

# # Ajouter des annotations pour indiquer les secteurs d'emploi à risque
# fig.add_annotation(x=0, y=fraud_by_sector['job_sector'].iloc[0],
#                    text='Les métiers les plus à risque sont : Engineer et Officer',
#                    showarrow=False, font=dict(size=12, color='red'))

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 2


# # Calculer la moyenne des fraudes pour chaque jour de la semaine
# fraud_by_day_of_week = dfm_all.groupby('day_of_the_week')['is_fraud'].mean().reset_index()

# # Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque jour de la semaine
# fig = px.bar(fraud_by_day_of_week, x='day_of_the_week', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'day_of_the_week': 'Jour de la semaine'},
#              title='Proportion de fraudes par jour de la semaine')

# # Ajouter des informations directement dans le graphique
# info_text = "Les jours avec la plus grande proportion de fraudes sont : " + ", ".join(fraud_by_day_of_week.sort_values(by='is_fraud', ascending=False)['day_of_the_week'].head(3))
# fig.add_annotation(xref='paper', yref='paper', x=0.5, y=-0.2, text=info_text, showarrow=False)

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 3 


# # Calculer la moyenne des fraudes pour chaque mois
# fraud_by_month = dfm_all.groupby('month')['is_fraud'].mean().reset_index()

# # Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque mois
# fig = px.bar(fraud_by_month, x='month', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'month': 'Mois'},
#              title='Proportion de fraudes par mois')

# # Ajouter des informations directement dans le graphique
# info_text = "Les mois avec la plus grande proportion de fraudes sont : " + ", ".join(fraud_by_month.sort_values(by='is_fraud', ascending=False)['month'].head(3))
# fig.add_annotation(xref='paper', yref='paper', x=0.5, y=-0.2, text=info_text, showarrow=False)

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 4

# # Calculer la somme des fraudes pour chaque heure de la journée
# fraud_by_hour = dfm_all.groupby('hour')['is_fraud'].sum().reset_index().sort_values(by='is_fraud', ascending=True)

# # Créer un graphique à barres pour visualiser la somme des fraudes pour chaque heure de la journée
# fig = px.bar(fraud_by_hour, x='hour', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Somme des fraudes', 'hour': 'Heure'},
#              title='Somme des fraudes par heure de la journée')

# # Ajouter des informations directement dans le graphique
# info_text = "Les heures de la journée avec la plus grande somme de fraudes sont : " + ", ".join(fraud_by_hour.sort_values(by='is_fraud', ascending=False)['hour'].head(3).astype(str))
# fig.add_annotation(xref='paper', yref='paper', x=0.5, y=-0.2, text=info_text, showarrow=False)

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 5

# # Calculer la moyenne des fraudes pour chaque État
# fraud_by_state = dfm_all.groupby('state')['is_fraud'].mean().reset_index()

# # Trier les données par ordre croissant de la proportion de fraudes
# fraud_by_state_sorted = fraud_by_state.sort_values(by='is_fraud', ascending=False)

# # Créer un graphique à barres pour visualiser la proportion des fraudes pour chaque État
# fig = px.bar(fraud_by_state_sorted, x='state', y='is_fraud', color='is_fraud',
#              labels={'is_fraud': 'Proportion de fraudes', 'state': 'État'},
#              title='Proportion de fraudes par état')

# # Ajouter des informations directement dans le graphique
# info_text = "Les États avec la plus grande proportion de fraudes sont : " + ", ".join(fraud_by_state_sorted.head(3)['state'])
# fig.add_annotation(xref='paper', yref='paper', x=0.5, y=-0.2, text=info_text, showarrow=False)

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 6


# # Créer un histogramme pour chaque genre avec les données côte à côte
# fig = px.histogram(dfm_all, x="gender", color="is_fraud", barmode='group',
#                    category_orders={"gender": dfm_all['gender'].value_counts().index.to_list()},
#                    labels={'is_fraud': 'Fraude', 'gender': 'Genre'},
#                    title='Distribution des fraudes par genre')

# # Ajouter les étiquettes de données sur chaque barre
# fig.update_traces(texttemplate='%{y}', textposition='outside')

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)

# Viz 7


# # Remplacer les valeurs 0 et 1 par des étiquettes
# dfm_all['is_fraud_label'] = dfm_all['is_fraud'].map({0: 'Transaction normale', 1: 'Transaction frauduleuse'})

# # Créer un graphique à boîtes avec les nouvelles étiquettes
# fig = px.box(dfm_all, x='amt', y='is_fraud_label')

# # Mettre à jour la mise en page
# fig.update_layout(
#     title='Répartition des montants',
#     showlegend=False,
#     height=700, width=1200
# )

# # Afficher le graphique dans Streamlit
# st.plotly_chart(fig, use_container_width=True)
