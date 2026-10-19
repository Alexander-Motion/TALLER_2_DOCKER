from flask import Flask, request
import os
import datetime

app = Flask(__name__)
LOG_FILE = "/var/log/app/visitas.log"

def log_request(path):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] Petición recibida en {path} desde {request.remote_addr}\n")

@app.route('/')
def home():
    log_request("/")
    return "Hola, soy Yoselin Cardona y vivo en Las Vegas de Comfandi"

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)