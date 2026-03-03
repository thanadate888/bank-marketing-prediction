import streamlit as st
import joblib
import numpy as np
from tensorflow.keras.models import load_model

st.title("🧪 Test Neural Network Model")

# Load model + vectorizer
nn_model = load_model("nn_model.h5")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

text_input = st.text_area("Enter text for prediction")

if st.button("Predict NN"):

    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        transformed = vectorizer.transform([text_input])
        prediction = nn_model.predict(transformed)[0][0]

        probability = prediction * 100

        st.subheader("Result")

        st.write(f"Positive Probability: {probability:.2f}%")
        st.progress(int(probability))