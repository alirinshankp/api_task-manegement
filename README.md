# Task Management API

A simple task management backend built with FastAPI and SQLite. This project allows users to create, view, update, filter, and delete tasks with priority and status tracking.

## Features

- Create new tasks
- View all tasks
- Fetch a single task by ID
- Update task details
- Change task status
- Filter tasks by status and priority
- Delete tasks
- Persistent storage using SQLite

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
task_manegement/
├── database.py          # SQLite connection and table creation
├── main.py              # FastAPI app entry point
├── tasks.db             # SQLite database file
├── routes/
│   └── task.py          # Task-related API routes
├── schemas/
│   └── task.py          # Pydantic request/response models
├── services/
│   └── task.py          # Business logic for task operations
├── testes               # Test files or experimental scripts
├── myvenv               # Virtual environment
├── .gitignore
└── README.md            # Project documentation
```

## Requirements

- Python 3.10+
- pip

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### Create a task

```http
POST /tasks
```

Request body example:

```json
{
  "title": "Write project README",
  "description": "Add setup and API documentation",
  "priority": "High",
  "status": "Pending"
}
```

### Get all tasks

```http
GET /tasks
```

Optional filters:

- `status` = `Pending`, `In Progress`, `Completed`
- `priority` = `Low`, `Medium`, `High`

Example:

```http
GET /tasks?status=Pending&priority=High
```

### Get a single task

```http
GET /tasks/{task_id}
```

### Update a task

```http
PUT /tasks/{task_id}
```

### Update task status

```http
PATCH /tasks/{task_id}/status
```

Example:

```json
{
  "status": "Completed"
}
```

### Delete a task

```http
DELETE /tasks/{task_id}
```

## Task Model

```json
{
  "id": 1,
  "title": "Task title",
  "description": "Task details",
  "priority": "Medium",
  "status": "Pending"
}
```

## Notes

- The project uses SQLite, so no external database service is required.
- The database schema is created automatically on startup.
- The app exposes a simple REST API suitable for small task-management workflows.

## License

This project is provided as a learning/demo project and can be freely modified for personal or educational use.
