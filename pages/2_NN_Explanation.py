import streamlit as st

st.title("🧠 Neural Network Model Explanation")

st.header("1. Dataset Type")

st.write("""
This model uses Unstructured Data (Text Data).
Text data was transformed into numerical format using TF-IDF Vectorization.
""")

st.header("2. Data Preparation")

st.write("""
1. Text cleaning
2. Tokenization
3. TF-IDF Vectorization
4. Train/Test split
""")

st.header("3. Neural Network Architecture")

st.write("""
The Neural Network was designed with:
- Input Layer
- Hidden Dense Layers (ReLU activation)
- Output Layer (Sigmoid activation)

Loss Function: Binary Crossentropy  
Optimizer: Adam  
Evaluation Metric: Accuracy
""")

st.header("4. Why Neural Network?")

st.write("""
Neural Networks are powerful for capturing complex relationships in data,
especially unstructured data such as text.
""")