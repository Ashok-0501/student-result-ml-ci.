FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY deployment/fastapi ./fastapi_app
COPY student_result_model.pkl .
COPY metrics.json .

EXPOSE 5000 8000

CMD ["python", "app.py"]
