import logging
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

STUDENT_NAME = os.getenv("STUDENT_NAME", "Alexander")
BARRIO = os.getenv("BARRIO", "Palmira_Chapinero_Sur")
LOG_PATH = "/var/log/app/visitas.log"

os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
visit_logger = logging.getLogger("visitas")
visit_logger.setLevel(logging.INFO)
visit_logger.addHandler(logging.FileHandler(LOG_PATH, encoding="utf-8"))


@app.after_request
def log_request(response):
    visit_logger.info(
        "%s %s %s %s",
        request.remote_addr or "-",
        request.method,
        request.path,
        response.status_code,
    )
    return response


@app.get("/")
def index():
    return f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}", 200, {
        "Content-Type": "text/plain; charset=utf-8"
    }


@app.get("/health")
def health():
    return jsonify(ok=True), 200
