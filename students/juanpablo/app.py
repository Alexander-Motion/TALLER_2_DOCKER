import os
from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

STUDENT_NAME = os.getenv("STUDENT_NAME", "Juan Pablo Montealegre")
BARRIO = os.getenv("BARRIO", "El Jardin")

LOG_DIR = "/var/log/app"
LOG_FILE = os.path.join(LOG_DIR, "visitas.log")

os.makedirs(LOG_DIR, exist_ok=True)


def log_visit():
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} {request.method} {request.path} {STUDENT_NAME}\n")


@app.before_request
def before_request():
    log_visit()


@app.route("/")
def home():
    return f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}", 200


@app.route("/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
