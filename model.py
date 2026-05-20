import pickle
import pandas as pd

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def extract_features(url):
    return {
        "url_length": len(url),
        "has_at_symbol": 1 if "@" in url else 0,
        "has_ip_address": 1 if any(part.isdigit() for part in url.split(".")) else 0,
        "subdomain_count": url.count("."),
        "has_https": 1 if url.startswith("https") else 0,
        "has_suspicious_words": 1 if any(word in url.lower() for word in ["login", "verify", "secure", "account", "update"]) else 0,
    }

def analyze(url):
    features = extract_features(url)

    risk_indicators = []
    positive_signals = []

    if not features["has_https"]:
        risk_indicators.append("Uses insecure HTTP instead of HTTPS")
    else:
        positive_signals.append("Uses secure HTTPS connection")

    if features["has_at_symbol"]:
        risk_indicators.append("Contains '@' symbol — can mask the real destination")

    if features["has_ip_address"]:
        risk_indicators.append("Uses an IP address instead of a domain name")

    if features["url_length"] > 75:
        risk_indicators.append("Unusually long URL")
    else:
        positive_signals.append("Reasonable URL length")

    if features["subdomain_count"] > 3:
        risk_indicators.append("Excessive number of subdomains")

    if features["has_suspicious_words"]:
        suspicious = [w for w in ["login", "verify", "secure", "account", "update"] if w in url.lower()]
        risk_indicators.append(f"Contains phishing-related keywords: {', '.join(suspicious)}")

    X = pd.DataFrame([features])
    prediction = model.predict(X)[0]

    if prediction == "bad" and len(risk_indicators) > 0:
        verdict = "Dangerous"
    else:
        verdict = "Likely Safe"

    return {
        "verdict": verdict,
        "risk_indicators": risk_indicators,
        "positive_signals": positive_signals,
    }