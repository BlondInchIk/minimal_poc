FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY poc.py .

ENV TARGET_URL=http://web:8000

CMD ["python", "poc.py"]
