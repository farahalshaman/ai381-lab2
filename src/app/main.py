from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).resolve().parents[2] / "model.joblib"
model = joblib.load(MODEL_PATH)

app = FastAPI(title="AI381 Lab 2 API", version="1.0.0")


class PredictRequest(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    contract: str = Field(min_length=1)
    internet_service: str = Field(min_length=1)
    support_calls: int = Field(ge=0)


class PredictResponse(BaseModel):
    prediction: int
    churn_probability: float


@app.get("/health")
def health():
    return {"status": "ok", "model_version": "1.0.0"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    customer = pd.DataFrame([request.model_dump()])
    prediction = int(model.predict(customer)[0])
    probability = float(model.predict_proba(customer)[0][1])

    return {
        "prediction": prediction,
        "churn_probability": round(probability, 4),
    }
