# JobTracker Pro

## [LINK FOR WEBSITE APPLICATION](https://jobtrackerpro-bmff.onrender.com)

### Dashboard
<img width="1784" height="1629" alt="dashboard-job-tracker" src="https://github.com/user-attachments/assets/52a6f60c-98ae-4afd-83e3-96c6d7775852" />

### Login Screen
<img width="877" height="275" alt="Screenshot 2026-04-22 at 8 47 23 PM" src="https://github.com/user-attachments/assets/7778c0e3-858f-4458-928f-7f5e3973c791" />

A secure, full-stack web application designed for the modern job seeker. This tool centralizes your pipeline, tracks application statuses, and maintains critical job data in a persistent cloud environment with sorting features.

Built out of a desire to move beyond local storage and explore cloud-based data persistence (PostgreSQL) and secure backend architecture.


## Features
* **Secure Authentication:** User accounts are protected using industry-standard password hashing via werkzeug.security.

* **Cloud Persistence:** Migrated from a local-only SQLite setup to a robust PostgreSQL (Supabase) backend for 24/7 data availability.

* **Decoupled Architecture:** Clean separation of concerns with a RESTful Flask API and a dynamic Vanilla JavaScript frontend.

* **Session Management:** Secure server-side session handling to ensure users only see their own application data.

* **Responsive Pipeline:** Includes dynamic filtering, real-time UI updates, and loading states for a seamless user experience.

* **Input Sanitization:** Client-side escaping to prevent XSS and parameterized SQL queries to block SQL Injection.

## Technical Stack
* **Backend:** Python 3.14+, Flask

* **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3

* **Database:** PostgreSQL (via Supabase)

* **Libraries** `psycopg2-binary` `python-dotenv` `Flask-Session`

* **Deployment:** Optimized for cloud platforms like Render or Railway

## Project Structure
* `app.py`: Server configuration & entry point
* `routes.py`: REST API endpoints & session logic
* `models.py`: Database operations & business logic
* `db.py`: PostgreSQL connection & server management
* `templates/`: Frontend HTML/CSS/JS
* `.env`: Environment variables (Ignored by Git)

## Getting Started
* Clone the repository:
`git clone https://www.github.com/steveBuelow/job-app-tracker.git`
`cd job-app-tracker`

* Install dependencies:
`pip install flask`

* Run the application:
`python app.py`
\ (`python3 app.py` on mac)

* Access the app at `http://127.0.0.1:5000/` in your browser.

## Future Roadmap
[x] Implement data persistence via PostgreSQL (Supabase/Neon).

[ ] Add visual data analytics (dashboards for application response rates).

[ ] Add automated follow-up reminders based on application dates.

[ ] Extract job details from uploaded job descriptions

[ ] Add buffer bar / Improve UI 
