from flask import Flask, request
from prometheus_client import generate_latest
from metrics import REQUEST_COUNT, REQUEST_LATENCY, APP_UP
import time, random, os

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    start = time.time()
    if random.random() < 0.1:
        REQUEST_COUNT.labels("GET", "/", "500", VERSION).inc()
        return "Error", 500

    time.sleep(random.random())
    REQUEST_COUNT.labels("GET", "/", "200", VERSION).inc()
    REQUEST_LATENCY.labels("/", VERSION).observe(time.time() - start)
    return "OK"

@app.route("/metrics")
def metrics():
    APP_UP.set(1)
    return generate_latest()

app.run(host="0.0.0.0", port=5000)
