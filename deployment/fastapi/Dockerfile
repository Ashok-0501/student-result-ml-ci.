FROM python:3.11-slim

WORKDIR /app

COPY deployment/fastapi/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY deployment/fastapi/app.py ./deployment/fastapi/app.py
COPY student_result_model.pkl ./student_result_model.pkl

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn deployment.fastapi.app:app --host 0.0.0.0 --port ${PORT:-8000}"]
