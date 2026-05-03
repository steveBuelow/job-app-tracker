# JobTracker Pro

## [LINK FOR WEBSITE APPLICATION](https://jobtrackerpro-bmff.onrender.com)

A secure, full-stack web application designed for the modern job seeker. This tool centralizes your pipeline, tracks application statuses, and maintains critical job data in a persistent cloud environment with sorting features. The app will display a follow-up reminder for jobs created >7 days ago to remind you to follow-up.

 Production deployment on Render with enviroment-secured PostgreSQL - not local host.


Built out of a desire to move beyond local storage and explore cloud-based data persistence and secure backend architecture.
\## Demo

![Job Tracker Demo](Screenshots/job-tracker-demo.gif)

### Dashboard (w follow-up reminder sorting all applications)
<img width="877" height="802" alt="Screenshot 2026-04-25 at 1 40 21 PM" src="https://github.com/user-attachments/assets/d22c70fd-05d1-488a-b044-09ef0d9de6a1" />


## Project Overview

JobTracker Pro allows users to:

* Track job applications in a centralized dashboard
* Create, edit, and delete job entries (full CRUD)
* View simple data analytics dashboard
* Monitor application statuses in real time
* Persist data securely using a backend database
* Generate recommended follow-up emails
* Secured with Werkzeung Security

This project was built to simulate a real-world SaaS product, manipulate secure data, all while strengthening full-stack engineering skills. Production deployment on Render with enviroment-secured PostgreSQL - not local host.

---

## Tech Stack

**Frontend:**

* HTML, CSS, JavaScript (Vanilla JS)

**Backend:**

* Python
* Flask

**Database:**

* PostgreSQL

**Other Tools:**

* Git & GitHub
* REST APIs
* Environment Variables (.env)
* `Psycopg-2-binary`
* PBKDF2 password hashing (via Werkzeung)

---

## Key Features

* User authentication & session management
* Full CRUD functionality (Create, Read, Update, Delete)
* Data analytics and simple calculations
* Real-time UI updates without page reloads
* Persistent cloud database storage
* Global loading states for async operations
* Features weekly in-app follow-up updates

---

## Project Structure

```
JobApplicationTracker/
│
├── app.py              # Server configuration and entry point
├── routes.py           # REST API endpoints and session management
├── models.py           # Business logic and SQL CRUD operations
├── db.py               # PostgreSQL connection and database helper
├── requirements.txt    # Python dependencies
│
└── templates/
│    └── index.html      # Frontend UI (HTML, CSS, and JS)
│
└── static/
    ├── jt-logo.png      # Application Logo
    └── date-71.png      # 'Applied' icon
```
---

## Challenges & What I Learned

* Managing frontend-backend communication using fetch and REST APIs
* Handling authentication and session persistence
* Debugging deployment issues related to environment variables and database connections
* Resolving Git conflicts and understanding real-world version control workflows

---

## Future Improvements

### v1

* [x] Migrate from SQLite database to persistent PostgreSQL
* [x] Add filtering and sorting (date and type) for job applications
* [x] Implement analytics (e.g., application success rate)
* [ ] Add email notifications or reminders
* [ ] Improve accessibility via Kanban Board

### v2 (end of summer)

* [ ] Scrape job URL to upload information (playwright, selenium, dedicated API)
* [ ] Improve UI/UX with a modern frontend framework (React)
* [ ] Implement Anthropic API

---

## About Me

I'm a first-year Computer Science student at NDSU
building production-ready full-stack applications. Currently 
pursuing software engineering internships while developing 
projects that go beyond coursework — focusing on real deployment, 
secure backend architecture, and clean user experience.

---

## Resume Bullet

Developed and deployed a full-stack job tracking application used to track 80+ applications across a live PostgreSQL database built with Flask, implementing secure authentication, full CRUD operations, and real-time UI updates, while resolving deployment and version control challenges in a production environment.

---

## Why This Project Matters

This project marks a shift from simple projects to building scalable applications that reflect industry practices, including backend architecture, database design, and deployment workflows.

---

## Local Installation

```bash
git clone https://github.com/your-username/jobtracker-pro.git
cd jobtracker-pro
pip install -r requirements.txt
python app.py
```

—
## Development Timeline

**April 2026**

* Finalized full CRUD cycle, enabling users to edit and delete entries with real-time UI updates
* Implemented global loading spinners for improved UX during async operations
* Resolved Git branch divergence and optimized merge workflows for stable deployment

