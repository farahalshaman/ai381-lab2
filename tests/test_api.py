
from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)

SAMPLE_CUSTOMER = {
    "tenure_months": 5,
    "monthly_charges": 89.9,
    "contract": "month-to-month",
    "internet_service": "fiber",
    "support_calls": 3,
}


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_rejects_empty_features():
    response = client.post("/predict", json={})

    assert response.status_code == 422


def test_predict_returns_expected_schema():
    response = client.post("/predict", json=SAMPLE_CUSTOMER)

    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "churn_probability" in response.json()
    assert 0 <= response.json()["churn_probability"] <= 1


def test_predict_rejects_wrong_input_type():
    customer = {**SAMPLE_CUSTOMER, "tenure_months": "not-a-number"}
    response = client.post("/predict", json=customer)

    assert response.status_code == 422


def test_prediction_is_deterministic():
    first = client.post("/predict", json=SAMPLE_CUSTOMER)
    second = client.post("/predict", json=SAMPLE_CUSTOMER)

    assert first.status_code == 200
    assert first.json() == second.json()

