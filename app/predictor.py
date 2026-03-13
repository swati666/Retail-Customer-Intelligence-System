import joblib
import numpy as np

MODEL_PATH = r"D:\ML Projects\Dunnhumby_Project\models\churn_model.pkl"
SCALER_PATH = r"D:\ML Projects\Dunnhumby_Project\models\scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_churn(frequency, monetary, total_quantity, avg_spend):

    data = np.array([[frequency, monetary, total_quantity, avg_spend]])

    data_scaled = scaler.transform(data)

    prob = model.predict_proba(data_scaled)[0][1]

    return prob