import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

st.set_page_config(
    page_title="Bank Marketing Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Marketing Prediction System")
st.markdown("### Machine Learning & Neural Network Demo")

# Sidebar
model_option = st.sidebar.selectbox(
    "Select Model",
    ["Machine Learning", "Neural Network"]
)

# Load Models
if model_option == "Machine Learning":
    model = joblib.load("ml_model.pkl")
else:
    model = tf.keras.models.load_model("nn_model.keras")

# Input Section
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)

with col2:
    balance = st.number_input("Balance", 0.0, 100000.0, 1000.0)

campaign = st.number_input("Campaign Contacts", 1, 50, 3)

# Predict Button
if st.button("Predict"):
    input_data = np.array([[age, balance, campaign]])

    if model_option == "Machine Learning":
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]
    else:
        prob = model.predict(input_data)[0][0]
        prediction = 1 if prob > 0.5 else 0

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("Client will Subscribe (YES)")
    else:
        st.error("Client will NOT Subscribe (NO)")

    st.metric("Confidence", f"{prob*100:.2f}%")
    st.progress(int(prob*100))