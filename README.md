# JobTracker Pro

**JobTracker Pro** is a full-stack job application tracking system that replaces spreadsheet-based workflows with a persistent, structured pipeline built with Flask and PostgreSQL. It includes real-time application tracking, automated follow-up detection, and a Kanban-style interface for managing a high-volume job search.

## [Link for Live Application](https://jobtrackerpro-bmff.onrender.com)

## Overview

JobTracker Pro is a full-stack web application designed to centralize and organize the job search process. It was built to handle 80+ active applications with persistent storage, secure authentication, and a workflow-based interface.

<video src="https://github.com/user-attachments/assets/a125ba2b-2bcc-4b46-992a-c225117a6cbe" autoplay loop muted width="100%"></video>

The project focuses on:
- Persistent cloud database storage
- RESTful backend design
- Stateful session handling
- Workflow automation logic
- Responsive asynchronous frontend updates

## Key Features

### Application Pipeline Management
A centralized system for tracking job applications, including:
- Company information
- Job URLs and role details
- Status tracking: Applied, Interviewing, Offer, Rejected
- Full CRUD lifecycle for each application

<video src="https://github.com/user-attachments/assets/65b97fa9-048f-4d68-8379-cc4dcbcdd96d" autoplay loop muted width="100%"></video>

<video src="https://github.com/user-attachments/assets/02f16bf6-b9c6-4a69-9b2f-08a2640f3a6c" autoplay loop muted width="100%"></video>

### Kanban Workflow Interface
A custom drag-and-drop Kanban board built in Vanilla JavaScript:
- Real-time status updates without page refresh
- Client-side state synchronization with the backend API
- Minimal dependency design

### Application Aging & Follow-Up Logic
A server-side system that identifies inactive applications:
- Flags applications with no updates for 7+ days
- Generates structured follow-up message templates
- Supports consistent outreach during the job search process

<video src="https://github.com/user-attachments/assets/002233aa-4e13-4ad0-9890-361d195c8af9" autoplay loop muted width="100%"></video>

<img width="877" height="802" alt="Screenshot 2026-04-25 at 1 40 21 PM" src="https://github.com/user-attachments/assets/d22c70fd-05d1-488a-b044-09ef0d9de6a1" />

### Analytics Dashboard
Lightweight analytics for tracking job search progress:
- Response rate calculation
- Weekly application velocity
- Application status distribution

### Authentication & Security
Built with secure session handling:
- Password hashing and salting using Werkzeug (PBKDF2)
- Secure session cookies with SameSite=Lax
- Environment-based configuration for deployment

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Frontend | HTML5, Vanilla JavaScript (ES6+), CSS3 |
| Backend | Python, Flask, Gunicorn |
| Database | PostgreSQL, Psycopg2 |
| Security | Werkzeug Security (PBKDF2), Secure Sessions |
| Deployment | Render, Git/GitHub |

## Architecture

```
Frontend (Vanilla JS)
        ↓ REST API
Flask Backend (app.py / routes.py)
        ↓
Business Logic Layer (models.py)
        ↓
PostgreSQL Database
```

## Project structure:
- `routes.py` handles API endpoints and request logic
- `models.py` manages database operations and business rules
- `db.py` manages database connections
- `app.py` serves as the application entry point and configuration layer

## Data Model & Logic
### Application Aging Rule
Applications are evaluated based on their date_applied value:

```
if current_date - date_applied >= 7 days:
    mark as eligible for follow-up
```

### Response Rate Calculation

```Response Rate = (Interviews + Offers) / Total Applications × 100```

### Weekly Application Velocity
Tracks the number of applications submitted within a rolling 7-day window to measure consistency.
## Development Highlights
### Database Migration
Migrated from SQLite to PostgreSQL for persistent cloud deployment and improved scalability.
### Backend Refactor
Refactored the project from a monolithic structure into modular components:
* API routes separated from business logic
* Database abstraction layer introduced
### Frontend Optimization
Rebuilt UI interactions using asynchronous fetch-based updates to avoid full-page reloads.
### Production Deployment
Configured for Render deployment using Gunicorn and environment-based configuration.

## Project Structure
```
JobApplicationTracker/
│
├── assets/              # UI demos and screenshots
├── static/              # CSS and UI assets
├── templates/           # HTML frontend
├── app.py               # Application entry point
├── routes.py            # REST API endpoints
├── models.py            # Business logic + DB operations
├── db.py                # Database connection layer
└── requirements.txt     # Dependencies
```

## Installation
```
git clone https://github.com/steveBuelow/job-app-tracker.git
cd job-app-tracker
pip install -r requirements.txt
python app.py
```

## About Me
I am a first-year Computer Science student at North Dakota State University focused on building production-oriented software systems.
This project reflects a shift from academic exercises to real-world engineering practices, including:
* Backend architecture design
* Secure authentication systems
* Cloud deployment workflows
* State-driven frontend design

## Resume Summary
Developed and deployed a full-stack job application tracking system using Flask and PostgreSQL, implementing secure authentication, RESTful API design, and a custom Kanban workflow interface. Built automated application aging logic and real-time analytics to support structured job search tracking across 80+ entries in a production cloud environment.
