import streamlit as st

st.set_page_config(page_title="คำอธิบาย Neural Network", layout="wide")

st.title("🧠 คำอธิบายโมเดล Neural Network")

st.header("1️⃣ ลักษณะของปัญหา")

st.markdown("""
เป็นปัญหาการจำแนกข้อความ (Text Classification)
เพื่อทำนายว่าข้อความของลูกค้ามีแนวโน้มสมัครผลิตภัณฑ์หรือไม่
""")

st.header("2️⃣ การเตรียมข้อมูลข้อความ")

st.markdown("""
ใช้เทคนิค TF-IDF (Term Frequency - Inverse Document Frequency)

เพื่อแปลงข้อความให้เป็นตัวเลข
โดยคำนวณความสำคัญของคำแต่ละคำในเอกสาร
""")

st.header("3️⃣ โครงสร้างของ Neural Network")

st.markdown("""
โครงสร้างของโมเดลประกอบด้วย:

Input Layer  
→ Hidden Layer (ReLU)  
→ Hidden Layer (ReLU)  
→ Output Layer (Sigmoid)

Loss Function: Binary Crossentropy  
Optimizer: Adam  
Evaluation Metric: Accuracy
""")

st.header("4️⃣ เหตุผลที่เลือกใช้ Neural Network")

st.markdown("""
Neural Network เหมาะสำหรับ:
- ข้อมูลที่มีความสัมพันธ์แบบไม่เป็นเชิงเส้น (Non-linear)
- ข้อมูลที่มีมิติสูง เช่น ข้อความ
- การเรียนรู้รูปแบบที่ซับซ้อน
""")

st.header("5️⃣ ฟังก์ชันกระตุ้น (Activation Function)")

st.subheader("ReLU")
st.markdown("""
ช่วยให้โมเดลเรียนรู้ความสัมพันธ์ที่ไม่เป็นเชิงเส้น
และลดปัญหา Vanishing Gradient
""")

st.subheader("Sigmoid")
st.markdown("""
แปลงค่าออกมาเป็นความน่าจะเป็นระหว่าง 0 ถึง 1
เหมาะกับปัญหา Binary Classification
""")

st.markdown("---")
st.info("โครงงานนี้แสดงการประยุกต์ใช้ Deep Learning สำหรับการวิเคราะห์ข้อความ พร้อมการนำไปใช้งานผ่านเว็บแอปพลิเคชัน")
st.header("6️⃣ วิธีการใช้งานโมเดลในระบบ")

st.markdown("""
ขั้นตอนการทำงานของโมเดล Neural Network มีดังนี้:

1️⃣ ผู้ใช้กรอกข้อความของลูกค้า

2️⃣ ระบบจะทำการแปลงข้อความเป็นตัวเลข
โดยใช้ TF-IDF Vectorizer

3️⃣ ข้อมูลตัวเลขจะถูกส่งเข้า Neural Network

4️⃣ โมเดลจะคำนวณความน่าจะเป็นด้วย Sigmoid
ซึ่งให้ค่าอยู่ระหว่าง 0 ถึง 1

5️⃣ แสดงผล:
- ผลการจำแนก (Positive / Negative)
- ค่าความน่าจะเป็น (%)
- กราฟแสดงผลลัพธ์
""")

st.subheader("ตัวอย่างการเรียกใช้งานในโค้ด")

st.code("""
vector = vectorizer.transform([text]).toarray()
prediction = model.predict(vector)
""", language="python")