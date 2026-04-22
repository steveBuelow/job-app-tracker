from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

print(f"DEBUG: DATABASE_URL is {os.environ.get('DATABASE_URL')}")

from routes import register_routes

app = Flask(__name__)
app.secret_key = "super_secret_key"

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)