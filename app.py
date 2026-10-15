import os
from flask import Flask, jsonify

app = Flask(__name__)

PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Flask on Rivervo</title><style>*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:#0f1923;color:#f5f3ef}main{max-width:560px;padding:32px;text-align:center}h1{font-size:2.5rem;margin:0 0 12px}p{color:#b8c1c9;line-height:1.6}</style></head><body><main><h1>It works</h1><p>Your application is live on Rivervo. Edit the code, push to GitHub, and the new version is deployed automatically.</p></main></body></html>"""


@app.get("/")
def index():
    return PAGE


@app.get("/api/health")
def health():
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
