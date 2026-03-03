import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Bank Marketing Predictor")

st.title("🏦 Bank Marketing Prediction")

# -------------------------
# 1️⃣ รับค่า Input ก่อน
# -------------------------

age = st.number_input("Age", 18, 100, 30)
balance = st.number_input("Balance", 0.0, 100000.0, 1000.0)
campaign = st.number_input("Campaign Contacts", 1, 50, 3)

# -------------------------
# 2️⃣ โหลด Model
# -------------------------

model = joblib.load("ml_model.pkl")
columns = joblib.load("ml_columns.pkl")

# -------------------------
# 3️⃣ กดปุ่มแล้วค่อย Predict
# -------------------------

if st.button("Predict"):

    input_dict = dict.fromkeys(columns, 0)

    input_dict["age"] = age
    input_dict["balance"] = balance
    input_dict["campaign"] = campaign

    input_df = pd.DataFrame([input_dict])

    # Predict class
    prediction = model.predict(input_df)[0]

    # Predict probability
    probability = model.predict_proba(input_df)[0]

    prob_no = probability[0] * 100
    prob_yes = probability[1] * 100

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success(f"Client will Subscribe (YES)")
    else:
        st.error(f"Client will NOT Subscribe (NO)")

    st.write("### Probability")

    st.write(f"Subscribe: {prob_yes:.2f}%")
    st.progress(int(prob_yes))

    st.write(f"Not Subscribe: {prob_no:.2f}%")
    st.progress(int(prob_no))

    # Bar chart
    chart_df = pd.DataFrame({
        "Outcome": ["Not Subscribe", "Subscribe"],
        "Probability (%)": [prob_no, prob_yes]
    })

    st.bar_chart(chart_df.set_index("Outcome"))