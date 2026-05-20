# Phishing URL Detector

A machine learning powered web app that analyzes URLs for phishing patterns — instantly and privately.

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

### 1. Clone the repository
git clone https://github.com/Happ137/Phishing-URL-Detector.git
cd Phishing-URL-Detector

### 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Get the dataset
Download phishing_site_urls.csv from:
https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls

Place it in the project root folder.

### 5. Train the model
python train.py

This generates model.pkl which the app needs to run.

### 6. Run the app
python app.py

### 7. Open in browser
http://127.0.0.1:5000