import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# 1. Load the dataset
df = pd.read_csv("phishing_site_urls.csv")

# 2. Extract features from each URL
def extract_features(url):
    return {
        "url_length": len(url),
        "has_at_symbol": 1 if "@" in url else 0,
        "has_ip_address": 1 if any(part.isdigit() for part in url.split(".")) else 0,
        "subdomain_count": url.count("."),
        "has_https": 1 if url.startswith("https") else 0,
        "has_suspicious_words": 1 if any(word in url.lower() for word in ["login", "verify", "secure", "account", "update"]) else 0,
    }

# 3. Build feature matrix
print("Extracting features...")
features = df["URL"].apply(extract_features)
X = pd.DataFrame(features.tolist())
y = df["Label"]

# 4. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train the model
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Test accuracy
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

# 7. Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to model.pkl")