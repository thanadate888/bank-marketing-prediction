import streamlit as st

st.set_page_config(page_title="คำอธิบาย Machine Learning", layout="wide")

st.title("📊 คำอธิบายโมเดล Machine Learning")

st.header("1️⃣ ภาพรวมของปัญหา")

st.markdown("""
โครงงานนี้เป็นปัญหา **Binary Classification (การจำแนกแบบสองคลาส)**  
เพื่อทำนายว่า ลูกค้าจะสมัครผลิตภัณฑ์เงินฝากประจำหรือไม่

ผลลัพธ์มี 2 ค่า:
- 0 = ไม่สมัคร
- 1 = สมัคร
""")

st.header("2️⃣ ชุดข้อมูล (Dataset)")

st.markdown("""
ใช้ชุดข้อมูล Bank Marketing Dataset

ตัวอย่างตัวแปรที่ใช้ เช่น:
- อายุ (age)
- ยอดเงินคงเหลือ (balance)
- จำนวนครั้งที่ติดต่อ (campaign)
- ระยะเวลาการโทร (duration)
- จำนวนครั้งที่เคยติดต่อก่อนหน้า (previous)

ตัวแปรเป้าหมาย (Target Variable):
- y (yes / no)
""")

st.header("3️⃣ โมเดลที่ใช้ (Ensemble Learning)")

st.subheader("🔹 Logistic Regression")
st.markdown("""
โมเดลเชิงเส้นที่ใช้ฟังก์ชัน Sigmoid
เพื่อคำนวณความน่าจะเป็นของการเกิดเหตุการณ์แบบสองกลุ่ม
""")

st.subheader("🔹 Random Forest")
st.markdown("""
เป็นโมเดลที่รวมต้นไม้ตัดสินใจหลายต้น (Decision Trees)
โดยใช้เทคนิค Bagging
ช่วยลดปัญหา Overfitting และเพิ่มความแม่นยำ
""")

st.subheader("🔹 Gradient Boosting")
st.markdown("""
เป็นเทคนิค Boosting
ที่สร้างโมเดลทีละตัวเพื่อแก้ไขข้อผิดพลาดของโมเดลก่อนหน้า
ช่วยเพิ่มประสิทธิภาพในการพยากรณ์
""")

st.subheader("🔹 Soft Voting (Ensemble)")
st.markdown("""
นำผลความน่าจะเป็นจากทุกโมเดลมาหาค่าเฉลี่ย
แล้วตัดสินผลลัพธ์สุดท้ายจากค่าที่ได้

ข้อดี:
- เพิ่มความแม่นยำ
- ลดความผันผวนของโมเดลเดี่ยว
- ทำให้โมเดลมีความเสถียรมากขึ้น
""")

st.header("4️⃣ เหตุผลที่เลือกใช้ Ensemble")

st.markdown("""
เนื่องจากแต่ละโมเดลมีจุดแข็งแตกต่างกัน  
การรวมหลายโมเดลเข้าด้วยกันช่วยให้:

- ลดความผิดพลาด (Error)
- ลด Overfitting
- เพิ่มความแม่นยำโดยรวมของระบบ
""")

st.markdown("---")
st.info("โครงงานนี้แสดงการประยุกต์ใช้ Machine Learning ในงานธุรกิจจริง พร้อมการพัฒนาเว็บแอปพลิเคชันด้วย Streamlit")
st.header("5️⃣ วิธีการใช้งานโมเดลในระบบ")

st.markdown("""
ขั้นตอนการทำงานของระบบมีดังนี้:

1️⃣ ผู้ใช้กรอกข้อมูลลูกค้า เช่น
- อายุ
- ยอดเงินคงเหลือ
- ระยะเวลาการโทร
- จำนวนครั้งที่ติดต่อ

2️⃣ ระบบจะนำข้อมูลมาจัดรูปแบบ (Preprocessing)
ให้ตรงกับรูปแบบที่ใช้ตอนฝึกโมเดล
เช่น การจัดเรียงคอลัมน์ให้ตรงกัน

3️⃣ โมเดล Ensemble จะทำการคำนวณ:
- Logistic Regression
- Random Forest
- Gradient Boosting

4️⃣ ระบบจะนำค่าความน่าจะเป็นจากทุกโมเดล
มาหาค่าเฉลี่ย (Soft Voting)

5️⃣ แสดงผลลัพธ์:
- ผลการทำนาย (สมัคร / ไม่สมัคร)
- ค่าความน่าจะเป็น (%)
- กราฟแสดงโอกาสของแต่ละคลาส
""")

st.subheader("ตัวอย่างการเรียกใช้งานในโค้ด")

st.code("""
prediction = model.predict(input_data)
probability = model.predict_proba(input_data)
""", language="python")