from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from model import analyze
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///history.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class ScanHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False)
    risk_indicators = db.Column(db.Text, nullable=False)
    scanned_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form["url"]
    analysis = analyze(url)

    if analysis["verdict"] == "Dangerous":
        entry = ScanHistory(
            url=url,
            risk_indicators=" | ".join(analysis["risk_indicators"])
        )
        db.session.add(entry)
        db.session.commit()

    return render_template("result.html", url=url, analysis=analysis)

@app.route("/history")
def history():
    entries = ScanHistory.query.order_by(ScanHistory.scanned_at.desc()).all()
    return render_template("history.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)