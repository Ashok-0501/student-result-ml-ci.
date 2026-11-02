# Student Result Prediction — MLOps Practical Series

This repository implements the Student Result Prediction practical sequence (Practicals 2–11).

## Model and dataset
A reproducible 300-row synthetic classroom dataset is generated with attendance, internal marks, assignment marks, and previous score. A Logistic Regression pipeline predicts PASS (1) or FAIL (0) using the weighted-score rule from Practical-2.

## Practical progression
- Practical 2: model training, evaluation, saved model/metrics, automated tests.
- Practical 3: 0.85 minimum-accuracy quality gate.
- Practical 4: preserve model, metrics, and CSV as a GitHub Actions artifact.
- Practical 5: Flask prediction API and release-candidate artifact.
- Practical 6: Dockerize the validated Flask application.
- Practical 7: build and smoke-test the Docker image in GitHub Actions.
- Practical 8: publish the tested image to GHCR.
- Practical 9: automate build, test, and GHCR publishing.
- Practical 10: deploy the GHCR image to Render (requires a Render account/service setup).
- Practical 11: add safe logging and error tracking to the deployed FastAPI service (the guide changes serving framework/port to FastAPI/8000; see `deployment/fastapi`).

## Run ML pipeline locally
```bash
pip install -r requirements.txt
python train_model.py
python quality_gate.py
python -m unittest test_ml_pipeline -v
python -m unittest test_app -v
```

## API
Flask API (Practicals 5–7): `python app.py`, port 5000.
FastAPI API (Practicals 10–11): see `deployment/fastapi/README.md`, port 8000.

## Security and data
The dataset is synthetic classroom data. Never commit GitHub PATs, tokens, passwords, Render credentials, or real student personal data. GHCR publication uses the workflow's `GITHUB_TOKEN`.
