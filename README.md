# Task API - BE-01

## Description

A simple CRUD API built with FastAPI that manages an in-memory to-do list. This project was created as part of the FlyRank Backend AI Engineering Week 2 assignment.

## Features

- Create a task
- Read all tasks
- Read a single task
- Update a task
- Delete a task
- Automatic Swagger UI documentation

## Tech Stack

- Python 3
- FastAPI
- Uvicorn

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/BE-01-crud-api.git
cd BE-01-crud-api
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API information |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{task_id} | Get a single task |
| POST | /tasks | Create a task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

---

# Example curl

```bash
curl -i -X POST http://127.0.0.1:8000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Buy milk\"}"
```

Expected response:

```json
{
    "id": 4,
    "title": "Buy milk",
    "done": false
}
```

---

# Swagger UI

Add your screenshot here:

```
screenshots/swagger.png
```

---

# Note

This project uses **in-memory storage**. All tasks are lost when the server is restarted because no database is used.