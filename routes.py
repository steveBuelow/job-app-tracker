import re
import random
from datetime import datetime, timedelta

import psycopg2
from flask import jsonify, render_template, request, session

from db import get_db
from models import (
    create_job,
    create_user,
    delete_job,
    find_user,
    toggle_followup,
    update_job,
)

# ─── Constants ────────────────────────────────────────────────────────────────

ALLOWED_STATUSES = {"Applied", "Interviewing", "Offer", "Rejected"}

# ─── Sanitisation helpers ─────────────────────────────────────────────────────

def _strip(val, max_len=None):
    """Coerce to str, strip whitespace, optionally enforce max length."""
    if val is None:
        return ""
    val = str(val).strip()
    if max_len:
        val = val[:max_len]
    return val


def _safe_url(url):
    """Return True if url is empty or starts with http/https."""
    if not url:
        return True
    return bool(re.match(r"^https?://", url, re.IGNORECASE))


def _validate_job_payload(d):
    """
    Validate and sanitise all job fields.
    Returns (cleaned_dict, error_str | None).
    """
    company = _strip(d.get("company_name"), 120)
    title   = _strip(d.get("job_title"),    120)
    status  = _strip(d.get("status"),        30)
    url     = _strip(d.get("job_url"),      500)
    notes   = _strip(d.get("notes"),        2000)

    if not company:
        return None, "Company name is required."
    if not title:
        return None, "Job title is required."
    if status not in ALLOWED_STATUSES:
        return None, f"Status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}."
    if url and not _safe_url(url):
        return None, "Job URL must start with http:// or https://."

    return dict(company_name=company, job_title=title,
                status=status, job_url=url, notes=notes), None


def _require_int_id(data, key="id"):
    """Pull an integer ID from a dict; return (id, error_response | None)."""
    val = data.get(key)
    if not isinstance(val, int) or val <= 0:
        return None, (jsonify({"error": "Invalid ID."}), 400)
    return val, None


# ─── Route registration ───────────────────────────────────────────────────────

def register_routes(app):

    # Security headers on every response
    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        # Disallow caching for JSON API responses
        if response.content_type and "json" in response.content_type:
            response.headers["Cache-Control"] = "no-store"
        return response

    # ── Pages ─────────────────────────────────────────────────────────────────

    @app.route("/")
    def index():
        return render_template("index.html")

    # ── Auth ──────────────────────────────────────────────────────────────────

    @app.route("/signup", methods=["POST"])
    def signup():
        data     = request.get_json(silent=True) or {}
        username = _strip(data.get("username"), 50)
        password = _strip(data.get("password"))

        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400
        if len(username) < 3:
            return jsonify({"error": "Username must be at least 3 characters."}), 400
        if not re.match(r"^[A-Za-z0-9_.\-]+$", username):
            return jsonify({"error": "Username may only contain letters, numbers, underscores, dots, or hyphens."}), 400
        if len(password) < 8:
            return jsonify({"error": "Password must be at least 8 characters."}), 400

        try:
            create_user(username, password)
            return jsonify({"message": "Account created!"}), 201
        except psycopg2.IntegrityError:
            return jsonify({"error": "That username is already taken."}), 409

    @app.route("/login", methods=["POST"])
    def login():
        data     = request.get_json(silent=True) or {}
        username = _strip(data.get("username"), 50)
        password = _strip(data.get("password"))

        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400

        user_id = find_user(username, password)
        if user_id:
            session.permanent = True
            session["user_id"] = user_id
            return jsonify({"status": "Logged in!"}), 200
        return jsonify({"error": "Invalid username or password."}), 401

    @app.route("/logout", methods=["POST"])
    def logout():
        session.clear()
        return jsonify({"status": "Logged out."}), 200

    # ── Jobs ──────────────────────────────────────────────────────────────────

    @app.route("/tasks")
    def get_tasks():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM applications WHERE user_id = %s ORDER BY date_applied DESC",
                    (session["user_id"],),
                )
                return jsonify({"tasks": cur.fetchall()})

    @app.route("/add-job", methods=["POST"])
    def add_job():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json(silent=True) or {}
        cleaned, err = _validate_job_payload(data)
        if err:
            return jsonify({"error": err}), 400

        create_job(
            cleaned["company_name"], cleaned["job_title"],
            cleaned["status"],       cleaned["job_url"],
            cleaned["notes"],        session["user_id"],
        )
        return jsonify({"success": True}), 201

    @app.route("/remove-job", methods=["DELETE"])
    def remove_job():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json(silent=True) or {}
        job_id, err = _require_int_id(data)
        if err:
            return err

        delete_job(job_id, session["user_id"])
        return jsonify({"success": True}), 200

    @app.route("/update-job", methods=["PUT"])
    def update_job_route():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json(silent=True) or {}
        job_id, err = _require_int_id(data)
        if err:
            return err

        cleaned, err = _validate_job_payload(data)
        if err:
            return jsonify({"error": err}), 400

        update_job(
            job_id,               session["user_id"],
            cleaned["company_name"], cleaned["job_title"],
            cleaned["status"],    cleaned["job_url"],
            cleaned["notes"],
        )
        return jsonify({"success": True}), 200

    @app.route("/toggle-followup", methods=["POST"])
    def toggle_followup_route():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data = request.get_json(silent=True) or {}
        job_id, err = _require_int_id(data)
        if err:
            return err

        new_state = toggle_followup(job_id, session["user_id"])
        return jsonify({"success": True, "followed_up": new_state}), 200

    # ── Reminders ─────────────────────────────────────────────────────────────

    @app.route("/reminders")
    def get_reminders():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401 
        
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, company_name, job_title, date_applied
                    FROM applications
                    WHERE user_id     = %s
                      AND status      = 'Applied'
                      AND followed_up = FALSE
                      AND date_applied <= NOW() - INTERVAL '7 days'
                    """,
                    (session["user_id"],),
                )
                return jsonify({"reminders": cur.fetchall()})

    # ── AI Follow-up generation ───────────────────────────────────────────────

    @app.route("/generate-followup", methods=["POST"])
    def generate_followup():
        if "user_id" not in session:
            return jsonify({"error": "Unauthorized"}), 401

        data    = request.get_json(silent=True) or {}
        company = _strip(data.get("company"), 120)
        role    = _strip(data.get("role"),    120)

        if not company or not role:
            return jsonify({"error": "Company and role are required."}), 400

        # Try real AI generation first; fallback to curated templates.
        # API key lives server-side only — never exposed to the client.
        try:
            import anthropic
            client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
            msg = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[{
                    "role": "user",
                    "content": (
                        f"Write a short, professional follow-up email body for a job application. "
                        f"Company: {company}. Role: {role}. "
                        f"Keep it under 80 words. Friendly but professional tone. "
                        f"Do NOT include a subject line. End with 'Best regards,' on its own line."
                    ),
                }],
            )
            email_text = msg.content[0].text.strip()
        except Exception:
            templates = [
                f"Hi {company} team,\n\nI wanted to follow up on my application for the {role} position. I remain very interested and would appreciate any updates when available.\n\nBest regards,",
                f"Hello {company},\n\nI'm checking in on my {role} application. I'm still excited about this opportunity and happy to provide anything else you might need.\n\nBest regards,",
                f"Dear {company} Hiring Team,\n\nI wanted to reiterate my strong interest in the {role} role. Please don't hesitate to reach out if you need anything further from me.\n\nBest regards,",
            ]
            email_text = random.choice(templates)

        return jsonify({"email": email_text})