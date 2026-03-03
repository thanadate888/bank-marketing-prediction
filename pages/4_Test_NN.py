import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

st.title("🧠 Test Neural Network Model")

@st.cache_resource
def load_nn():
    model = load_model("nn_model.h5")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

nn_model, vectorizer = load_nn()

text_input = st.text_area("Enter customer comment")

if st.button("Predict Text"):

    if text_input.strip() == "":
        st.warning("Please enter text")
    else:
        transformed = vectorizer.transform([text_input])
        prediction = nn_model.predict(transformed)[0][0]

        prob_positive = prediction
        prob_negative = 1 - prediction

        st.subheader("Prediction Result")

        if prob_positive > 0.5:
            st.success("Positive / Subscribe Intent")
        else:
            st.error("Negative / No Subscribe Intent")

        fig, ax = plt.subplots()
        ax.bar(["Negative", "Positive"],
               [prob_negative*100, prob_positive*100])
        ax.set_ylabel("Probability (%)")
        st.pyplot(fig)

        st.metric("Positive Probability",
                  f"{prob_positive*100:.2f}%")