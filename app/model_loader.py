import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_model():
    model_path = os.path.join(BASE_DIR, "model", "churn_model.pkl")
    scaler_path = os.path.join(BASE_DIR, "model", "scaled_model.pkl")
    featured_path = os.path.join(BASE_DIR, "model", "features_name.pkl")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature = joblib.load(featured_path)

    return model, scaler, feature
