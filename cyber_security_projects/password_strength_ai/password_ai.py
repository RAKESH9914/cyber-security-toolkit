import pandas as pd
import random
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("password_strength_ai/passwords.csv")

# Train model
vector = CountVectorizer()
X = vector.fit_transform(data["password"])

model = LogisticRegression()
model.fit(X, data["label"])

# Suggest strong password
def suggest():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(chars) for _ in range(12))

# Function for Streamlit
def check_password_strength(pwd):
    test = vector.transform([pwd])
    result = model.predict(test)[0]

    if result == "weak":
        return f"Weak password. Suggested strong password: {suggest()}"
    elif result == "medium":
        return "Medium strength password"
    else:
        return "Strong password"
