# Meeting Intelligence Service

Live Deployment

The application is deployed and publicly accessible at:

Base URL:
https://meeting-intelligence-service-pslx.onrender.com

Useful Endpoints
Health Check: GET /health
API Documentation (Swagger): /apidocs
Evaluation Endpoint: /api/evaluation

Testing the APIs

Most endpoints require authentication.

Register a user using POST /auth/register
Login using POST /auth/login
Copy the returned JWT access token
Add the token to the Authorization header:
Authorization: Bearer <your_token>
Access protected endpoints such as:
POST /meetings
GET /meetings
POST /meetings/{id}/analyze
POST /api/action-items
GET /api/action-items/overdue

## Features

- JWT Authentication
- Meeting Management
- AI Meeting Analysis (Gemini)
- Grounded Citations
- Action Item Management
- Overdue Detection
- Reminder Scheduler
- Discord Integration
- Trace IDs
- Structured Logging
- Swagger Documentation

## Tech Stack

- Flask
- PostgreSQL
- SQLAlchemy
- Gemini API
- APScheduler
- Marshmallow
- Flasgger

## Setup

1. Clone repo
2. Create .env
3. Install dependencies

pip install -r requirements.txt

4. Run

python main.py
