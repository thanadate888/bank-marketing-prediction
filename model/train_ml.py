import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("data/bank-full.csv", sep=";")

# Replace unknown with NaN and drop
df.replace("unknown", None, inplace=True)
df.dropna(inplace=True)

# Convert target
df['y'] = df['y'].map({'yes':1, 'no':0})

# One-hot encoding
df = pd.get_dummies(df, drop_first=True)

# Split
X = df.drop("y", axis=1)
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
rf = RandomForestClassifier()
gb = GradientBoostingClassifier()
lr = LogisticRegression(max_iter=1000)

ensemble = VotingClassifier(
    estimators=[
        ('rf', rf),
        ('gb', gb),
        ('lr', lr)
    ],
    voting='hard'
)

# Train
ensemble.fit(X_train, y_train)

# Evaluate
pred = ensemble.predict(X_test)
print(classification_report(y_test, pred))

# Save model + feature columns
joblib.dump(ensemble, "ml_model.pkl")
joblib.dump(X.columns.tolist(), "ml_columns.pkl")

print("ML Model Saved!")