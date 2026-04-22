from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
from routes import register_routes

app = Flask(__name__)
app.secret_key = "super_secret_key"

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)