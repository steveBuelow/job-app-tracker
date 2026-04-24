from flask import request, session, jsonify, render_template
import psycopg2
from db import get_db
from models import *

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        try:
            create_user(data.get('username'), data.get('password'))
            return jsonify({"message": "Account created!"}), 201
        except psycopg2.IntegrityError:
            return jsonify({"error": "User exists"}), 409

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user_id = find_user(data.get('username'), data.get('password'))
        if user_id:
            session.permanent = True
            session['user_id'] = user_id
            return jsonify({"status": "Logged in!"}), 200
        return jsonify({"error": "Invalid login"}), 401

    @app.route('/tasks')
    def get_tasks():
        if 'user_id' not in session: return jsonify({"error": "Unauthorized"}), 401
        with get_db() as conn:
            with conn.cursor() as cur:
                # Use %s instead of ?
                cur.execute("SELECT * FROM applications WHERE user_id = %s", (session['user_id'],))
                rows = cur.fetchall()
                # Rows are already dicts because of RealDictCursor in db.py
                return jsonify({"tasks": rows})

    @app.route('/add-job', methods=['POST'])
    def add_job():
        if 'user_id' not in session: 
            return jsonify({"error": "Unauthorized"}), 401
        
        d = request.get_json()

        create_job(d['company_name'], d['job_title'], d['status'], d['job_url'], d['notes'], session['user_id'])
        return jsonify({"success": True}), 201

    @app.route('/remove-job', methods=['DELETE'])
    def remove_job():
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized"}), 401
        
        job_id = request.json.get('id')
        delete_job(job_id, session.get('user_id'))
        return jsonify({"success": True}), 200