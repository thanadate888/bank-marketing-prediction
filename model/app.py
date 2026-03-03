import joblib
import pandas as pd
import numpy as np

model = joblib.load("ml_model.pkl")
columns = joblib.load("ml_columns.pkl")

# สร้าง dictionary เต็มก่อน
input_dict = dict.fromkeys(columns, 0)

# ใส่ค่าที่ผู้ใช้กรอก
input_dict["age"] = age
input_dict["balance"] = balance
input_dict["campaign"] = campaign

# แปลงเป็น DataFrame
input_df = pd.DataFrame([input_dict])

prediction = model.predict(input_df)[0]