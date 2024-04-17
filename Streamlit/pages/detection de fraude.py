import streamlit as st
import pandas as pd
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

### CONFIG
st.set_page_config(
    page_title="Fraud Detector",
    page_icon="💳",
    layout="centered"
)

st.title("Fraud Detector")

st.markdown("""
            👋 Bienvenue dans cette application de détections de fraudes !
            """)

### LOAD MODEL
def load_model():
    with open('xgboost.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def load_preprocessor():
    with open('preprocess.pkl', 'rb') as f:
        preprocessor = pickle.load(f)
    return preprocessor

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

st.header("Formulaire")

with st.form("transaction_form"):
    st.write("Veuillez entrer le numéro de la transaction")
    index = st.number_input("Identifiant de la transaction", min_value=0, max_value=len(test)-1, step=1)
    submit = st.form_submit_button(label="Vérifier la fraude")
    if submit:
        line = test.iloc[index,:]
        line_df = pd.DataFrame(line).T
        st.write("Infos de la transaction :")
        st.write(line_df)
        line_pr = preprocessor.transform(line_df)
        is_fraud = model.predict(line_pr)
        st.write("Prédiction du modèle :")
        if(is_fraud == 1):
            st.write("FRAUDE DETECTEE !")
        else:
            st.write("Pas de fraude détectée")

st.header("Statistiques")

test_pr = preprocessor.transform(test)

pred = model.predict(test_pr)
real = sol['is_fraud']

# Matrice de confusion
st.subheader('Matrice de confusion')
plt.figure(figsize=(3, 3))
fig, ax = plt.subplots()
ConfusionMatrixDisplay.from_estimator(model, test_pr, real, ax=ax)
st.pyplot(fig, use_container_width=True)

# Histogramme des prédictions
st.subheader('Histogramme des prédictions')
pred_correct = (pred == real).astype(int)
correct_count = np.sum(pred_correct)
incorrect_count = len(pred_correct) - correct_count
bardf = pd.DataFrame({
    'Prédiction': ['Correct', 'Incorrect'],
    'Fréquence': [correct_count, incorrect_count]
})
plt.figure(figsize=(3, 3))
fig, ax = plt.subplots()
bars = ax.bar(bardf['Prédiction'], bardf['Fréquence'], color=['green', 'red'])
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom')
ax.set_xlabel('Fréquence')
ax.set_title('Prédictions')
st.pyplot(fig, use_container_width=True)