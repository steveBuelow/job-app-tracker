from flask import Flask, jsonify
from dotenv import load_dotenv
import os
load_dotenv()
from routes import register_routes

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "This route does not exist"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error. Our bad!"}), 500

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)