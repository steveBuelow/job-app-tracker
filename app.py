from flask import Flask, jsonify
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

from routes import register_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

is_prod = os.getenv("FLASK_ENV") == "production"

# BUG FIX: original had SESSION_COOKIE_SECURE=is_prod as a bare expression
# (comma made it a tuple, not a config line), then overrode it to always True.
# Now correctly env-aware.
app.config.update(
    SESSION_COOKIE_SAMESITE='Lax',
    SESSION_COOKIE_SECURE=is_prod,   # True in prod, False in dev (allows HTTP)
    SESSION_COOKIE_HTTPONLY=True,    # JS cannot touch the session cookie
    PERMANENT_SESSION_LIFETIME=timedelta(days=7),
)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found."}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error."}), 500

register_routes(app)

if __name__ == "__main__":
    app.run(debug=not is_prod)