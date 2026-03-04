import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Test Neural Network", layout="wide")

st.title("🤖 Neural Network Prediction")

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_nn_model():
    model = load_model("nn_model.h5")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_nn_model()

# ----------------------------
# Text Input
# ----------------------------
st.subheader("Enter Customer Text")

user_input = st.text_area("Customer Message")

if st.button("Predict") and user_input:

    # Transform text
    input_vector = vectorizer.transform([user_input]).toarray()

    # Predict
    prediction = model.predict(input_vector)[0][0]

    st.divider()

    # Result
    if prediction > 0.5:
        st.success("Prediction: Positive Response")
    else:
        st.error("Prediction: Negative Response")

    # Probability Chart
    prob_df = pd.DataFrame({
        "Class": ["Negative", "Positive"],
        "Probability": [1 - prediction, prediction]
    })

    st.subheader("Prediction Probability")
    st.bar_chart(prob_df.set_index("Class"), use_container_width=True)