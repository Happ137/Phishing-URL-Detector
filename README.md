# Phishing URL Detector

A machine learning powered web app that analyzes URLs for phishing patterns.

## Features
- Detects phishing URLs using a model trained on 549,000 real URLs
- Shows detailed risk indicators and positive signals
- Logs all dangerous URLs in a danger log

## Tech Stack
- Python, Flask
- scikit-learn, pandas
- SQLite, SQLAlchemy
- HTML, CSS

## Run Locally

1. Clone the repository
   git clone https://github.com/Happ137/Phishing-URL-Detector.git
   cd Phishing-URL-Detector

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Train