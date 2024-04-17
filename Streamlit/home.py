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

    Nous avons fait le constat que la fraude par carte bleue était la fraude la plus fréquente en 2023. 
    Nous nous sommes demandés comment on pourrait prédire le caractère frauduleux d'une transaction. Nous avons travaillé sur le dataset suivant :""")
st.markdown("""https://www.kaggle.com/datasets/kelvinkelue/credit-card-fraud-prediction""")
st.markdown("""Nous avons effectué des modèles de Machine Learning non supervisé et supervisé afin d'identifier les facteurs les plus pertinents dans la détection de fraude.""")
# @st.cache_data
# def load_data():
#     data_cluster = joblib.load('data.joblib')
#     base_data_cluster = joblib.load('base_data.joblib')

#     return data