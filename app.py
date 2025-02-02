import streamlit as st
import joblib
import numpy as np

# Chargeons le modèle entraîné
model = joblib.load("house_price_model.pkl")

st.title("🏡 Prédiction du Prix des Maisons")

# Création des champs d'entrée pour les caractéristiques
surface = st.number_input("Surface en pieds carrés", min_value=500, max_value=5000, step=50)
chambres = st.number_input("Nombre de chambres", min_value=1, max_value=10, step=1)
sdb = st.number_input("Nombre de salles de bain", min_value=1, max_value=5, step=1)
garage = st.number_input("Nombre de garages", min_value=0, max_value=5, step=1)
annee_construction = st.number_input("Année de construction", min_value=1900, max_value=2024, step=1)

# Préparons les données sous forme de tableau numpy
features = np.array([[surface, chambres, sdb, garage, annee_construction]])

# Bouton pour prédire
if st.button("Prédire le Prix 💰"):
    prediction = model.predict(features)
    st.success(f"💵 Le prix estimé de la maison est : {prediction[0]:,.2f} $")
