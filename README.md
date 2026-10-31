# AI381 Lab 2 — Customer Churn Prediction API

A tested FastAPI service that predicts customer churn using a scikit-learn pipeline.

## CI Status

![CI](https://github.com/farahalshaman/ai381-lab2/actions/workflows/ci.yml/badge.svg)

## Run with Docker

    docker run --rm -p 8000:8000 ghcr.io/farahalshaman/ai381-lab2:c8adeb12799127543a8d1cb45d1a309ac1720e56

Open http://localhost:8000/docs for interactive API documentation.

## Health Check

    curl http://localhost:8000/health

## Predict Customer Churn

    curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"tenure_months":5,"monthly_charges":89.9,"contract":"month-to-month","internet_service":"fiber","support_calls":3}'

## Docker Image

- Image: `ghcr.io/farahalshaman/ai381-lab2`
- Commit tag: `c8adeb12799127543a8d1cb45d1a309ac1720e56`
- Image digest: `sha256:fdd5a756638382d8ab743332633693cc5809efc84e577b068420df40c36501e0`

## Tests

GitHub Actions runs Ruff and pytest, builds the Docker image, scans it with Trivy for HIGH and CRITICAL vulnerabilities, and publishes the image to GitHub Container Registry after successful checks on main.
