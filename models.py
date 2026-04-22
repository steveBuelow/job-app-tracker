from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    hashed_pw = generate_password_hash(password)
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
        conn.commit()

def find_user(username, password):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, password FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user and check_password_hash(user['password'], password):
                return user['id']
        return None

def create_job(company_name, job_title, status, job_url, notes, user_id):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO applications (company_name, job_title, status, job_url, notes, user_id) VALUES (%s,%s,%s,%s,%s,%s)",
                (company_name, job_title, status, job_url, notes, user_id)
            )
        conn.commit()

def delete_job(job_id, user_id):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM applications WHERE id=%s AND user_id=%s", (job_id, user_id))
        conn.commit()