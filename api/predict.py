from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

app = FastAPI()


model = joblib.load("optimized_risk_classifier_model.pkl")
vectorizer = joblib.load("optimized_tfidf_vectorizer.pkl")


class PredictionRequest(BaseModel):
    description: str
    age: int
    credit_amount: float
    duration: int
    job: int
    saving_account: str
    checking_account: str
    purpose: str

@app.post("/predict")
def predict(data: PredictionRequest):
    try:
        description_tfidf = vectorizer.transform([data.description]).toarray()

        saving_account_encoded = [1 if data.saving_account == "little" else 0] 
        checking_account_encoded = [1 if data.checking_account == "moderate" else 0]
        purpose_encoded = [1 if data.purpose == "car" else 0]

        numerical_features = np.array([data.age, data.credit_amount, data.duration, data.job])
        input_features = np.hstack((
            description_tfidf,
            numerical_features,
            saving_account_encoded,
            checking_account_encoded,
            purpose_encoded
        ))

        prediction = model.predict([input_features])[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al realizar la predicción: {str(e)}")
