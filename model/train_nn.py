import pandas as pd
import joblib
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load text dataset
df = pd.read_csv("data/customer_text_dataset.csv")
df.dropna(inplace=True)

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

df['customer_comment'] = df['customer_comment'].apply(clean_text)

# Convert label
df['label'] = df['label'].map({'yes':1, 'no':0})

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['customer_comment'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Neural Network
model = Sequential([
    Dense(128, activation='relu', input_shape=(X.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train.toarray(), y_train, epochs=5, batch_size=32)

# Save model + vectorizer
model.save("nn_model.keras")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("NN Model Saved!")