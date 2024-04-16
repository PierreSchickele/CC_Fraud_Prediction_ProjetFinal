import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import ConfusionMatrixDisplay, roc_curve, auc
from sklearn.compose import ColumnTransformer
from sklearn.discriminant_analysis import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
import io
import pickle
from plotly.subplots import make_subplots

### CONFIG
st.set_page_config(
    page_title="Fraud Detector",
    page_icon="💳",
    layout="wide"
)

st.title("Fraud Detector")

st.markdown("""
            👋 Hello there!
            Welcome to this simple fraud detector app.
            """)

# ### LOAD DATA
# DATA_URL = ('../src/fraud test.csv')

# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     return data

# data_load_state = st.text('Loading data...')
# N = 1000
# data = load_data(N)
# data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

# ## Run the below code if the check is checked ✅
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data) 

### LOAD MODEL
def load_model():
    with open('xgboost.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def load_preprocessor():
    with open('preprocess.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    return preprocessor

st.header("Fraud Detector")

TEST_URL = ('test.csv')
REAL_URL = ('test_sol.csv')

def load_test():
    data = pd.read_csv(TEST_URL)
    return data

def load_sol():
    data = pd.read_csv(REAL_URL)
    return data

# Chargement du modèle, du preprocess et des données
model = load_model()
preprocessor = load_preprocessor()
test = load_test()
sol = load_sol()

test_pr = preprocessor.transform(test)

pred = model.predict(test_pr)
real = sol['is_fraud']

# Matrice de confusion
st.subheader('Matrice de confusion')
fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_estimator(model, test_pr, real, ax=ax)
st.pyplot(fig)

# # Courbe ROC
# st.subheader('Courbe ROC')
# fig, ax = plt.subplots()
# roc_curve(test_pr, real)
# st.pyplot(fig)

# Histogramme des prédictions
# st.subheader('Histogramme des prédictions')
# fig, ax = plt.subplots()
# ax.hist(pred, bins=20, color='blue', alpha=0.7, label='Prédictions')
# ax.hist(real, bins=20, color='red', alpha=0.7, label='Vrais résultats')
# ax.set_xlabel('Classe')
# ax.set_ylabel('Fréquence')
# ax.legend(loc='upper right')
# st.pyplot(fig)

# Histogramme des prédictions
st.subheader('Histogramme des prédictions')
pred_correct = (pred == real).astype(int)
correct_count = np.sum(pred_correct)
incorrect_count = len(pred_correct) - correct_count
bardf = pd.DataFrame({
    'Prédiction': ['Incorrect', 'Correct'],
    'Fréquence': [incorrect_count, correct_count]
})
fig, ax = plt.subplots()
ax.barh(bardf['Prédiction'], bardf['Fréquence'], color=['red', 'green'])
ax.set_xlabel('Fréquence')
ax.set_title('Prédictions')
st.pyplot(fig)