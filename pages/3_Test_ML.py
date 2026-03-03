import streamlit as st
import joblib
import pandas as pd

st.title("🧪 Test Machine Learning Model")

# Input fields
age = st.number_input("Age", 18, 100, 30)
balance = st.number_input("Balance", 0.0, 100000.0, 1000.0)
campaign = st.number_input("Campaign Contacts", 1, 50, 3)

model = joblib.load("ml_model.pkl")
columns = joblib.load("ml_columns.pkl")

if st.button("Predict ML"):

    input_dict = dict.fromkeys(columns, 0)

    input_dict["age"] = age
    input_dict["balance"] = balance
    input_dict["campaign"] = campaign

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    prob_no = probability[0] * 100
    prob_yes = probability[1] * 100

    st.subheader("Result")

    if prediction == 1:
        st.success("Client will Subscribe (YES)")
    else:
        st.error("Client will NOT Subscribe (NO)")

    st.write(f"Subscribe Probability: {prob_yes:.2f}%")
    st.progress(int(prob_yes))

    chart_df = pd.DataFrame({
        "Outcome": ["Not Subscribe", "Subscribe"],
        "Probability (%)": [prob_no, prob_yes]
    })

    st.bar_chart(chart_df.set_index("Outcome"))