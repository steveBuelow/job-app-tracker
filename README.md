

# JobTracker Pro

## [[LINK FOR LIVE APPLICATION]](https://jobtrackerpro-bmff.onrender.com)

**JobTracker Pro** is a production-ready, full-stack pipeline manager designed for the modern job seeker. This application replaces local spreadsheets with a persistent cloud environment, featuring automated application aging logic, a custom Kanban interface, and a heuristic-based outreach generator.

---

## Project Overview

Built to simulate a real-world SaaS product, this tool centralizes the job hunt into a high-performance dashboard. It focuses on secure data manipulation and scalable backend architecture to handle 80+ active applications across a live database.

*   **Centralized Pipeline:** Real-time tracking of company metadata, job URLs, and application status.
*   **Persistent Cloud Architecture:** Deployed on **Render** with an environment-secured **PostgreSQL** database.
*   **Heuristic Outreach Engine:** Automatically identifies "stale" applications ($>7$ days) and generates tailored follow-up templates.
*   **Robust Security:** User data is protected via **PBKDF2 password hashing** and protected session management via **Werkzeug**.
*   **Dynamic Analytics:** Live calculation of response rates and weekly application velocity.

---

## Tech Stack

| Component | Technologies |
| :--- | :--- |
| **Frontend** | Vanilla JavaScript (ES6+), HTML5, CSS3 (Custom Variables), DM Sans Typography |
| **Backend** | Python 3, Flask, Gunicorn, Dotenv, RESTful API Design |
| **Database** | PostgreSQL, Psycopg2 (Utilizing RealDictCursor for optimized JSON serialization) |
| **Security** | Werkzeug Security (Hashing/Salting), Secure Session Cookies (SameSite=Lax) |
| **DevOps** | Render (Production Hosting), Git/GitHub (Version Control) |

---

## Key Features

### **1. Core Application Workflow**
Centralizes the job hunt into a single dashboard with global loading states for asynchronous operations. The interface ensures zero-latency UI updates during state transitions.
<video src="https://github.com/user-attachments/assets/65b97fa9-048f-4d68-8379-cc4dcbcdd96d" autoplay loop muted width="100%"></video>

### **2. Cloud Persistence & Full CRUD**
Leverages a PostgreSQL backend to ensure data remains persistent across user sessions. Includes full Create, Read, Update, and Delete capabilities with strict backend validation.
<video src="https://github.com/user-attachments/assets/02f16bf6-b9c6-4a69-9b2f-08a2640f3a6c" autoplay loop muted width="100%"></video>


### **3. Heuristic Outreach Engine**
A programmatic logic system that identifies applications where no activity has occurred in 7+ days. It generates professional follow-up templates to maintain candidate momentum.
<video src="https://github.com/user-attachments/assets/002233aa-4e13-4ad0-9890-361d195c8af9" autoplay loop muted width="100%"></video>


<img width="877" height="802" alt="Screenshot 2026-04-25 at 1 40 21 PM" src="https://github.com/user-attachments/assets/d22c70fd-05d1-488a-b044-09ef0d9de6a1" />

### **4. Interactive Kanban Management**
A visual drag-and-drop workflow for status tracking. Users can seamlessly move applications through the funnel—from **Applied** to **Interviewing** or **Offer**.
<video src="https://github.com/user-attachments/assets/a125ba2b-2bcc-4b46-992a-c225117a6cbe" autoplay loop muted width="100%"></video>

---

## Data Analytics & Logic

The dashboard implements automated metrics to provide immediate feedback on job hunt performance:

*   **Response Rate:** Calculated as: 
    $$\text{Response Rate} = \left( \frac{\text{Interviews} + \text{Offers}}{\text{Total Applications}} \right) \times 100$$
*   **Weekly Velocity:** Monitors application volume within a rolling 7-day window.
*   **Application Aging:** Server-side logic filters for entries where `date_applied` $\le 7$ days to trigger follow-up alerts.

---

## Project Structure

```
JobApplicationTracker/
│
├── assets/             # MP4 demos and high-res screenshots
│   ├── core-workflow.mp4
│   ├── crud-demo.mp4
│   ├── ai-follow-up-demo.mp4
│   └── kanban-ui-demo.mp4
│
├── static/             # Static UI assets (Logos/Icons)
├── templates/          # Frontend UI (index.html)
├── app.py              # Flask entry point & Error handling
├── routes.py           # REST API endpoints & Session logic
├── models.py           # Business logic & SQL CRUD execution
├── db.py               # PostgreSQL connection helper
└── requirements.txt    # Production dependencies

```

## Development Timeline
### April 2026: Architecture & Security
* Database Migration: Successfully migrated from SQLite to a production-ready PostgreSQL environment.
* Security Integration: Implemented Werkzeug.security for robust password salting and hashing.
* Session Management: Configured secure cookie handling and a 7-day permanent session lifetime.
### May 2026: UI/UX & AI Logic
* AI Follow-up Integration: Deployed the generate-follow-up endpoint using a heuristic template engine for automated candidate outreach.
* Asynchronous UX: Deployed global loading spinners and optimized fetch requests for non-blocking CRUD actions.
* Kanban Logic: Developed a custom drag-and-drop interface using Vanilla JS, eliminating the need for heavy external libraries.
* Production Launch: Configured Render deployment with Gunicorn and environment-secured PostgreSQL strings.

## About Me

### (LinkedIn)[www.linkedin.com/in/lawayne-steve-buelow-a8229b402]

I am a first-year Computer Science student at North Dakota State University focused on building production-ready software. This project represents a shift toward scalable architecture, secure backend design, and deployment workflows that reflect industry standards.
Resume Bullet: Developed and deployed a full-stack job tracking application used to track 80+ applications across a live PostgreSQL database built with Flask, implementing secure authentication, full CRUD operations, and real-time UI updates, while resolving deployment and version control challenges in a production environment.

## Local Installation
```
# Clone the repository
git clone https://github.com/steveBuelow/job-app-tracker.git

# Navigate to the project directory
cd job-app-tracker

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
