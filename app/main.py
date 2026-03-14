from fastapi import FastAPI
import joblib
import numpy as np
from app.schema import CustomerFeatures

app = FastAPI(title="Retail Churn Prediction API")

# Load model and scaler once at startup
#model = joblib.load( r"D:\ML Projects\Dunnhumby_Project\models\logistic_model.pkl")
#scaler = joblib.load( r"D:\ML Projects\Dunnhumby_Project\models\scaler.pkl")

model = joblib.load("models/logistic_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.post("/predict_churn")
def predict_churn(data: CustomerFeatures):

    features = np.array([[
        data.frequency,
        data.monetary,
        data.total_quantity,
        data.avg_spend
    ]])

    features_scaled = scaler.transform(features)

    churn_probability = model.predict_proba(features_scaled)[0][1]

    prediction = int(churn_probability > 0.1)

    return {
        "churn_probability": float(churn_probability),
        "prediction": prediction
    }


import pandas as pd

transactions = pd.read_csv("data/transaction_data.csv")
latest_date = transactions['DAY'].max()


def compute_customer_features(household_key):

    customer_txn = transactions[
        transactions['household_key'] == household_key
    ]

    if customer_txn.empty:
        return None

    last_purchase = customer_txn['DAY'].max()

    frequency = customer_txn.shape[0]
    monetary = customer_txn['SALES_VALUE'].sum()
    total_quantity = customer_txn['QUANTITY'].sum()
    avg_spend = monetary / frequency

    return {
        "frequency": frequency,
        "monetary": monetary,
        "total_quantity": total_quantity,
        "avg_spend": avg_spend
    }


@app.get("/predict_customer_churn/{household_key}")
def predict_customer_churn(household_key: int):

    features = compute_customer_features(household_key)

    if features is None:
        return {"error": "Customer not found"}

    data = np.array([[
        features["frequency"],
        features["monetary"],
        features["total_quantity"],
        features["avg_spend"]
    ]])

    data_scaled = scaler.transform(data)

    prob = model.predict_proba(data_scaled)[0][1]

    prediction = int(prob > 0.1)

    return {
        "household_key": household_key,
        "churn_probability": float(prob),
        "prediction": prediction
    }