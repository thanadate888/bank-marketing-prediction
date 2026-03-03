import streamlit as st

st.title("📊 Machine Learning Model Explanation")

st.header("1. Dataset Source")

st.write("""
Dataset: Bank Marketing Dataset  
Source: UCI Machine Learning Repository  
https://archive.ics.uci.edu/ml/datasets/Bank+Marketing
""")

st.header("2. Dataset Description")

st.write("""
This dataset contains customer information collected from a bank marketing campaign.
The goal is to predict whether a client will subscribe to a term deposit.
""")

st.header("3. Important Features")

st.write("""
- age: Age of client  
- job: Type of job  
- marital: Marital status  
- education: Education level  
- balance: Account balance  
- housing: Has housing loan or not  
- loan: Has personal loan or not  
- campaign: Number of contacts performed during this campaign  
- y: Target variable (yes/no)
""")

st.header("4. Data Preparation")

st.write("""
Steps performed:
1. Replaced 'unknown' with missing values
2. Removed rows with missing values
3. Converted target variable into numeric format
4. Applied One-hot Encoding for categorical features
5. Split data into Train (80%) and Test (20%)
""")

st.header("5. Ensemble Model")

st.write("""
The model is an Ensemble Learning approach using VotingClassifier (Soft Voting).
It combines:
- Random Forest
- Gradient Boosting
- Logistic Regression

Soft Voting averages probabilities from each model to improve prediction accuracy.
""")
st.header("Model Theory")

st.markdown("""
### Random Forest
Ensemble of decision trees using bagging technique.

### Gradient Boosting
Sequential ensemble technique reducing residual errors.

### Logistic Regression
Linear model for binary classification using sigmoid function.

### Soft Voting
Averages prediction probabilities from all base models.
""")