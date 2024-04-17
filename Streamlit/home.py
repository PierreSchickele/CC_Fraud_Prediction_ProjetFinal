import joblib
import streamlit as st
import pandas as pd
import pydeck as pdk
import hdbscan
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import ConfusionMatrixDisplay, roc_curve, auc
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
import io
import pickle


def main():
    st.set_page_config(
        page_title="Accueil",
        page_icon="💳",
        layout="centered"
    )

st.title("Bienvenue sur notre application Streamlit")

st.markdown("""
    Comment pouvons nous prédire des transactions victimes de fraudes à la carte bancaire ?
    Cette application présente le projet que nous avons fait pour Jedha.
""")



### SIDEBAR
st.sidebar.header("Build dashboards with Streamlit")
st.sidebar.markdown("""
    * [EDA](#load-and-showcase-data)
    * [Modèle de prédiction](#simple-bar-chart-built-directly-with-streamlit)
    * [Modèle de clustering](#simple-bar-chart-built-with-plotly)
    * [Input Data](#input-data)
""")
e = st.sidebar.empty()
e.write("")
st.sidebar.write("Made with 💖 by [Jedha](https://jedha.co)")

# @st.cache_data
# def load_data():
#     data_cluster = joblib.load('data.joblib')
#     base_data_cluster = joblib.load('base_data.joblib')

#     return data