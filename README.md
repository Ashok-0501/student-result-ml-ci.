# Student Result Prediction — MLOps Practical Series

This repository contains the Student Result Prediction practical sequence (Practicals 2–11).

## Model and dataset
A reproducible 300-row synthetic classroom dataset is generated from attendance, internal marks, assignment marks, and previous score. A Logistic Regression pipeline predicts PASS (1) or FAIL (0) using the weighted-score rule.

## Practical progression
- Practical 2: train and evaluate the ML model; save model and metrics.
- Practical 3: enforce the minimum 0.85 accuracy quality gate.
- Practical 4: upload model, metrics, and CSV as GitHub Actions artifacts.
- Practical 5: Flask prediction API.
- Practical 6: Dockerize the Flask application.
- Practical 7: build and smoke-test Flask Docker image in GitHub Actions.
- Practical 8: publish tested container images to GitHub Container Registry (GHCR).
- Practical 9: automate training, tests, Docker builds, smoke tests, and GHCR publishing on pushes to main.
- Practical 10: Render image deployment blueprint is provided in `render.yaml`; create the service from your Render account after the GHCR package is public.
- Practical 11: FastAPI service adds request IDs, duration logs, validation/error logging, and dedicated tests.

## Run locally
```bash
pip install -r requirements.txt
python train_model.py
python quality_gate.py
python -m unittest test_ml_pipeline -v
python -m unittest test_app -v
python -m unittest test_fastapi -v
```

## Services
- Flask (Practicals 5–9): `python app.py`, port 5000.
- FastAPI (Practicals 10–11): see `deployment/fastapi/README.md`, port 8000.

## Container images
The workflow publishes:
- Flask: `ghcr.io/ashok-0501/student-result-prediction:flask`
- FastAPI: `ghcr.io/ashok-0501/student-result-prediction:latest`

## Render deployment
1. Make the GHCR package public in GitHub Packages (or configure registry credentials in Render).
2. In Render, create a new Blueprint and select this repository, or create a Web Service using the FastAPI image above.
3. Set the health check path to `/health` and environment variable `PORT=8000`.
4. Wait for the first successful deploy and copy the public Render URL.

Render account authorization and the final service creation/public URL must be completed by the repository owner.

## Security and data
The dataset is synthetic. Never commit GitHub PATs, tokens, passwords, Render credentials, or real student personal data. GHCR publishing uses the workflow-provided `GITHUB_TOKEN`.
