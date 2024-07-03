FROM python:3.10-slim
LABEL authors="Alvaro8317"

WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]