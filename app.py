import streamlit as st
import joblib
import pandas as pd

# -------------------------
# ตั้งค่าหน้าเว็บ
# -------------------------
st.set_page_config(page_title="Bank Marketing Predictor", layout="wide")

st.title("🏦 Bank Marketing Prediction System")

st.markdown("""
### 📌 วิธีการทำงานของโมเดล
1. ผู้ใช้กรอกข้อมูล Age, Balance และ Campaign
2. ระบบจะส่งข้อมูลเข้า Machine Learning Model
3. โมเดลจะคำนวณความน่าจะเป็น (Probability)
4. แสดงผลลัพธ์เป็น Subscribe (YES) หรือ NOT Subscribe (NO)
""")

st.divider()

# -------------------------
# โหลด Model (Cache)
# -------------------------
@st.cache_resource
def load_model():
    model = joblib.load("ml_model.pkl")
    columns = joblib.load("ml_columns.pkl")
    return model, columns

try:
    model, columns = load_model()
except:
    st.error("❌ ไม่พบไฟล์โมเดล กรุณาตรวจสอบ ml_model.pkl และ ml_columns.pkl")
    st.stop()

# -------------------------
# รับค่า Input (จัด layout ให้ดูดี)
# -------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    balance = st.number_input("Balance", 0.0, 100000.0, 1000.0)

with col2:
    campaign = st.number_input("Campaign Contacts", 1, 50, 3)

st.divider()

# -------------------------
# กดปุ่ม Predict
# -------------------------
if st.button("🔍 Predict"):

    # สร้าง dictionary ให้ครบทุก column
    input_dict = dict.fromkeys(columns, 0)

    input_dict["age"] = age
    input_dict["balance"] = balance
    input_dict["campaign"] = campaign

    input_df = pd.DataFrame([input_dict])

    # ทำนายผล
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    prob_no = probability[0] * 100
    prob_yes = probability[1] * 100

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.success("✅ Client will Subscribe (YES)")
    else:
        st.error("❌ Client will NOT Subscribe (NO)")

    st.write("### 📈 Probability")

    st.write(f"Subscribe: {prob_yes:.2f}%")
    st.progress(int(prob_yes))

    st.write(f"Not Subscribe: {prob_no:.2f}%")
    st.progress(int(prob_no))

    # แสดงกราฟ
    chart_df = pd.DataFrame({
        "Outcome": ["Not Subscribe", "Subscribe"],
        "Probability (%)": [prob_no, prob_yes]
    })

    st.bar_chart(chart_df.set_index("Outcome"))