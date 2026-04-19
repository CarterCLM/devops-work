from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "No Chill API v3 is running"

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/metrics")
def metrics():
    return jsonify(
        cpu="low",
        memory="stable",
        version=os.getenv("APP_VERSION", "1.0")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)