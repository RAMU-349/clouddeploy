from flask import Flask, render_template, jsonify
from datetime import datetime, timezone
import os
import platform

app = Flask(__name__)

START_TIME = datetime.now(timezone.utc)


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name="CloudDeploy",
        environment=os.getenv("APP_ENV", "Development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        current_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudDeploy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": "CloudDeploy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("APP_ENV", "Development"),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "uptime_seconds": int(
            (datetime.now(timezone.utc) - START_TIME).total_seconds()
        ),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)