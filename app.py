from flask import Flask, Response, jsonify
import random
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return jsonify({"status": "ok", "message": "CloudForge running"})

@app.route('/api/simulate-error')
def simulate_error():
    if random.random() < 0.5:
        return Response("Internal Server Error", status=500)
    return jsonify({"status": "ok"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)