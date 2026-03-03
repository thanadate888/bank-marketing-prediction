import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Test ML Model", layout="wide")

st.title("🧠 Machine Learning Prediction")

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("ml_model.pkl")
    columns = joblib.load("ml_columns.pkl")
    return model, columns

model, model_columns = load_model()

# ----------------------------
# Input Form
# ----------------------------
st.subheader("Enter Customer Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    balance = st.number_input("Balance", value=1000)
    duration = st.number_input("Call Duration (seconds)", value=100)

with col2:
    campaign = st.number_input("Campaign Contacts", value=1)
    previous = st.number_input("Previous Contacts", value=0)

# ----------------------------
# Prediction Button
# ----------------------------
if st.button("Predict"):

    # Create dataframe from input
    input_data = pd.DataFrame([{
        "age": age,
        "balance": balance,
        "duration": duration,
        "campaign": campaign,
        "previous": previous
    }])

    # Ensure columns match training
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()

    # ----------------------------
    # Show Result
    # ----------------------------
    if prediction == 1:
        st.success("Prediction: Customer WILL Subscribe")
    else:
        st.error("Prediction: Customer will NOT Subscribe")

    # ----------------------------
    # Probability Chart
    # ----------------------------
    prob_df = pd.DataFrame({
        "Class": ["No", "Yes"],
        "Probability": probability
    })

    st.subheader("Prediction Probability")
    st.bar_chart(prob_df.set_index("Class"), use_container_width=True)