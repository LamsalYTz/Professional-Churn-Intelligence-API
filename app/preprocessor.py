import pandas as pd
import numpy as np


ENCODING_MAP = {
    "gender":            {"Female": 0, "Male": 1},
    "Partner":           {"No": 0, "Yes": 1},
    "Dependents":        {"No": 0, "Yes": 1},
    "PhoneService":      {"No": 0, "Yes": 1},
    "MultipleLines":     {"No": 0, "No phone service": 1, "Yes": 2},
    "InternetService":   {"DSL": 0, "Fiber optic": 1, "No": 2},
    "OnlineSecurity":    {"No": 0, "No internet service": 1, "Yes": 2},
    "OnlineBackup":      {"No": 0, "No internet service": 1, "Yes": 2},
    "DeviceProtection":  {"No": 0, "No internet service": 1, "Yes": 2},
    "TechSupport":       {"No": 0, "No internet service": 1, "Yes": 2},
    "StreamingTV":       {"No": 0, "No internet service": 1, "Yes": 2},
    "StreamingMovies":   {"No": 0, "No internet service": 1, "Yes": 2},
    "Contract":          {"Month-to-month": 0, "One year": 1, "Two year": 2},
    "PaperlessBilling":  {"No": 0, "Yes": 1},
    "PaymentMethod":     {
        "Bank transfer (automatic)": 0,
        "Credit card (automatic)": 1,
        "Electronic check": 2,
        "Mailed check": 3
    },
}

def preprocess_input(data: dict, scaler, feature_names: list):
    df = pd.DataFrame([data])

    # Apply fixed encoding maps
    for col, mapping in ENCODING_MAP.items():
        if col in df.columns:
            df[col] = df[col].map(mapping)

    # Ensure correct column order matching training
    df = df[feature_names]

    # Check for any unmapped (NaN) values
    if df.isnull().any().any():
        bad_cols = df.columns[df.isnull().any()].tolist()
        raise ValueError(f"Encoding failed for columns: {bad_cols}")

    scaled = scaler.transform(df)
    return scaled