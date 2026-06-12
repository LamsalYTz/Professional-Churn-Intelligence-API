# 🔮 Churn Intelligence API

A production-ready ML-powered REST API that predicts customer churn
for telecom businesses — built with FastAPI and Scikit-learn.

<!-- ## 🚀 Live Demo
🔗 https://your-render-url.onrender.com/docs -->

## 📊 What it does
- Predicts whether a customer will churn: **Yes / No**
- Returns **confidence score** (0.0 – 1.0)
- Returns **risk level**: High / Medium / Low
- Returns an **action message** for the business
- Secured with **API key authentication**

## 🛠️ Tech Stack
Python · FastAPI · Scikit-learn · Pandas · Pydantic · Render

## ⚡ Quick Start
```bash
git clone https://github.com/YOUR_USERNAME/churn-api
cd churn-api
pip install -r requirements.txt
python train_on_start.py
uvicorn app.main:app --reload
```

## 📬 Sample Request
**POST** `/predict` with header `X-API-Key: your-key`

**Response:**
```json
{
  "churn_prediction": "Yes",
  "confidence": 0.847,
  "risk_level": "High",
  "message": "This customer is very likely to churn. Immediate action recommended."
}
```

## 👤 Author
Built by [@SANDY](https://github.com/LamsalYTz)
Open to freelance ML & API projects!