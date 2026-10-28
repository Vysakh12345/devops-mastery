import os
import time

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "DevOps Mastery Challenge"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/db-health")
def db_health():
    config = {
        "host": os.getenv("DB_HOST", "db"),
        "port": int(os.getenv("DB_PORT", "5432")),
        "dbname": os.getenv("DB_NAME", "devopsdb"),
        "user": os.getenv("DB_USER", "appuser"),
        "password": os.getenv("DB_PASSWORD", "devops_password"),
        "connect_timeout": 3,
    }

    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
        return jsonify({"database": "connected"}), 200
    except psycopg.OperationalError:
        return jsonify({"database": "unavailable"}), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
