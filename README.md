# JobTracker Pro

## [LINK FOR WEBSITE APPLICATION](https://jobtrackerpro-bmff.onrender.com)

A secure, full-stack web application designed for the modern job seeker. This tool centralizes your pipeline, tracks application statuses, and maintains critical job data in a persistent cloud environment with sorting features. The app will display a follow-up reminder for jobs created >7 days ago to remind you to follow-up.

Built out of a desire to move beyond local storage and explore cloud-based data persistence (PostgreSQL) and secure backend architecture.

### Dashboard (w follow-up reminder sorting all applications)
<img width="877" height="802" alt="Screenshot 2026-04-25 at 1 40 21 PM" src="https://github.com/user-attachments/assets/d22c70fd-05d1-488a-b044-09ef0d9de6a1" />

### Login Screen
<img width="877" height="275" alt="Screenshot 2026-04-22 at 8 47 23 PM" src="https://github.com/user-attachments/assets/7778c0e3-858f-4458-928f-7f5e3973c791" />

## Project Overview

JobTracker Pro allows users to:

* Track job applications in a centralized dashboard
* Create, edit, and delete job entries (full CRUD)
* Monitor application statuses in real time
* Persist data securely using a backend database

This project was built to simulate a real-world SaaS product while strengthening full-stack engineering skills.

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

---

## Key Features

* User authentication & session management
* Full CRUD functionality (Create, Read, Update, Delete)
* Real-time UI updates without page reloads
* Persistent cloud database storage
* Global loading states for async operations

---

## Project Structure

JobApplicationTracker/
├── app.py              # Server configuration and entry point
├── routes.py           # REST API endpoints and session management
├── models.py           # Business logic and SQL CRUD operations
├── db.py               # PostgreSQL connection and database helper
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys, DB URLs)
└── templates/
    └── index.html      # Frontend UI (HTML, CSS, and JS)

---

## Development Timeline

**April 2026**

* Finalized full CRUD cycle, enabling users to edit and delete entries with real-time UI updates
* Implemented global loading spinners for improved UX during async operations
* Resolved Git branch divergence and optimized merge workflows for stable deployment

---

## Challenges & What I Learned

* Managing frontend-backend communication using fetch and REST APIs
* Handling authentication and session persistence
* Debugging deployment issues related to environment variables and database connections
* Resolving Git conflicts and understanding real-world version control workflows

---

## Future Improvements

* Add filtering and sorting for job applications
* Implement analytics (e.g., application success rate)
* Improve UI/UX with a modern frontend framework (React)
* Add email notifications or reminders

---

## About Me

I’m a first-year Computer Science student focused on building real-world, production-ready applications.

Currently developing my second full-stack project while preparing for internships by strengthening both:

* Software engineering skills (projects)
* Problem-solving skills (data structures & algorithms)

---

## Resume Bullet

Developed and deployed a full-stack job tracking application using Flask and PostgreSQL, implementing secure authentication, full CRUD operations, and real-time UI updates, while resolving deployment and version control challenges in a production environment.

---

## Why This Project Matters

This project marks a shift from simple projects to building scalable applications that reflect industry practices, including backend architecture, database design, and deployment workflows.

---

## Installation

```bash
git clone https://github.com/your-username/jobtracker-pro.git
cd jobtracker-pro
pip install -r requirements.txt
python app.py
```

---

## Final Note

This is part of a growing portfolio aimed at landing software engineering internships by demonstrating practical, real-world development skills.
