from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import CustomerData, PredictionResponse
from app.model_loader import load_model
from app.preprocessor import preprocess_input
from app.auth import verify_api_key
from fastapi import HTTPException

app = FastAPI(
    title="🔮 Churn Intelligence API",
    description="""
    ## Customer Churn Prediction API

    Predict whether a telecom customer will churn using Machine Learning.

    ### Features
    - ✅ Churn prediction (Yes / No)
    - ✅ Confidence score (0.0 – 1.0)
    - ✅ Risk level (High / Medium / Low)
    - ✅ API key authentication

    ### Authentication
    Pass your API key in the request header as `X-API-Key`.
    """,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model, scaler, feature_names = load_model()

@app.get("/", tags=["General"])
def root():
    return {
        "name": "Churn Intelligence API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", tags=["General"])
def health():
    return {"status": "ok", "model": "loaded", "features": len(feature_names)}

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict_churn(
    customer: CustomerData,
    api_key: str = Security(verify_api_key)
):
    try:
        data = customer.dict()
        processed = preprocess_input(data, scaler, feature_names)
        prediction = model.predict(processed)[0]
        probability = float(model.predict_proba(processed)[0][1])

        churn = "Yes" if prediction == 1 else "No"
        confidence = round(probability if prediction == 1 else 1 - probability, 3)

        if probability >= 0.7:
            risk = "High"
            message = "This customer is very likely to churn. Immediate action recommended."
        elif probability >= 0.4:
            risk = "Medium"
            message = "This customer shows moderate churn risk. Consider a retention offer."
        else:
            risk = "Low"
            message = "This customer is likely to stay. Keep up the good service!"

        return PredictionResponse(
            churn_prediction=churn,
            confidence=confidence,
            risk_level=risk,
            message=message
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")