FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STUDENT_NAME="Juan Pablo Montealegre"
ENV BARRIO="El Jardin"

WORKDIR /app

RUN mkdir -p /var/log/app
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl --fail http://127.0.0.1:8080/health || exit 1

CMD ["python", "app.py"]
