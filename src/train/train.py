
"""Train and save the customer churn prediction model."""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "churn_v1.csv"
MODEL_PATH = ROOT / "model.joblib"

NUMERIC_FEATURES = [
    "tenure_months",
    "monthly_charges",
    "support_calls",
]
CATEGORICAL_FEATURES = ["contract", "internet_service"]
TARGET = "churn"


def train_model() -> None:
    """Fit the model using churn_v1.csv and save it."""
    data = pd.read_csv(DATA_PATH)

    features = NUMERIC_FEATURES + CATEGORICAL_FEATURES
    X = data[features]
    y = data[TARGET]

    preprocessing = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), NUMERIC_FEATURES),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("prep", preprocessing),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)

    print(f"Training complete. Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
