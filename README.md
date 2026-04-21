# JobTracker Pro
A secure, full-stack web application designed to help job seekers manage their pipeline, track application statuses, and maintain job links—all in one place.

## Features
* **Secure Authentication:** User accounts are protected using industry-standard password hashing via werkzeug.security.

* **State Management:** Persistent session handling using localStorage ensures a seamless user experience across page refreshes.

* **RESTful Architecture:** Decoupled frontend/backend communication using JSON-based API endpoints.

* **Responsive UI:** Includes loading states, toast notifications, and dynamic filtering to manage growing application lists.

* **Security First:** Implemented XSS protection through client-side input escaping.

## Technical Stack
* Backend: Python / Flask

* Frontend: Vanilla JavaScript (ES6+), HTML5, CSS3

* Database: SQLite with SQLAlchemy/DB-API

* Deployment: Designed for cloud platforms (e.g., Render)

## Project Structure
* app.py: Main entry point and server configuration.

* routes.py: API route definitions and session handling.

* db.py: Database schema and connection management.

* models.py: Data models and business logic (user/job handling).

* /templates/index.html: Main frontend application.

## Getting Started
* Clone the repository:

Bash
`git clone https://www.github.com/steveBuelow/job-app-tracker.git`
`cd job-app-tracler`
* Install dependencies:

Bash
`pip install flask`
* Run the application:

Bash
`python app.py`
\ (`python3 app.py` on mac)
* Access the app at http://127.0.0.1:5000/ in your browser.

## Future Roadmap
[ ] Implement data persistence via PostgreSQL (Supabase/Neon).

[ ] Add visual data analytics (dashboards for application response rates).

[ ] Add automated follow-up reminders based on application dates.
