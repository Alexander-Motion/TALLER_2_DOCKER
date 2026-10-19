import os
from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

STUDENT_NAME = os.getenv("STUDENT_NAME", "Angie Valencia")
BARRIO = os.getenv("BARRIO", "San Antonio")
LOG_PATH = "/var/log/app/visitas.log"

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


@app.after_request
def log_request(response):
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} {request.method} {request.path} {response.status_code}\n")
    return response


@app.get("/")
def index():
    message = f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}"
    return message, 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.get("/health")
def health():
    return jsonify(ok=True), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
