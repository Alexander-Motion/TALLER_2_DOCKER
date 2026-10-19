FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

# Usamos gunicorn para servir la aplicación Flask (app.py) en el puerto 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]