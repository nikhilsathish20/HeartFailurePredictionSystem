# predictor/ml_model.py
import joblib # type: ignore
import os

# Get the absolute path of the model and scaler
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'heart_failure_pipeline.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

# Load the model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict(input_data):
    # input_data should be a list or array of feature values
    input_data_scaled = scaler.transform([input_data])
    prediction = model.predict(input_data_scaled)
    probability = model.predict_proba(input_data_scaled)[0][1]
    return prediction[0], probability
