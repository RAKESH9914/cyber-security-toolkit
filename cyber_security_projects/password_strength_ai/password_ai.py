import pandas as pd
import random
import string
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# =====================================
# FIXED CSV FILE PATH (IMPORTANT)
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "passwords.csv")

# Load dataset
data = pd.read_csv(csv_path)

# Train ML model
vector = CountVectorizer()
X = vector.fit_transform(data["password"])

model = LogisticRegression()
model.fit(X, data["label"])

# =====================================
# STRONG PASSWORD GENERATOR
# =====================================
def suggest():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(12))

# =====================================
# RULE BASED PASSWORD CHECK (REALISTIC)
# =====================================
def rule_based_strength(pwd):
    score = 0

    if len(pwd) >= 8:
        score += 1
    if len(pwd) >= 12:
        score += 1
    if re.search(r"[A-Z]", pwd):
        score += 1
    if re.search(r"[a-z]", pwd):
        score += 1
    if re.search(r"[0-9]", pwd):
        score += 1
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", pwd):
        score += 1

    if score <= 2:
        return "weak"
    elif score <= 4:
        return "medium"
    else:
        return "strong"

# =====================================
# FINAL PASSWORD CHECK FUNCTION
# =====================================
def check_password_strength(pwd):

    # ML prediction
    test = vector.transform([pwd])
    ml_result = model.predict(test)[0]

    # Rule-based prediction
    rule_result = rule_based_strength(pwd)

    # Combine both (take stronger evaluation)
    if "strong" in [ml_result, rule_result]:
        return "Strong password"
    elif "medium" in [ml_result, rule_result]:
        return "Medium strength password"
    else:
        return f"Weak password. Suggested strong password: {suggest()}"

