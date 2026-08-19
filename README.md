# Backend Task Queue

This is my FastAPI project for Devnexes Internship.
It creates jobs and processes them with a background worker using SQLite.

## How to Install

1. Install dependencies:
pip install fastapi uvicorn sqlalchemy

## How to Run

1. Start the API:
uvicorn app:app --reload

2. Start the Worker in a new terminal:
python worker.py

3. Open this in browser:
http://localhost:8000/docs

## API Endpoints

POST /jobs - Create a new job
GET /jobs/{id} - Check job status

## Features
- Create jobs using API
- Jobs saved in SQLite database
- Background worker processes jobs
- Check job status anytime
