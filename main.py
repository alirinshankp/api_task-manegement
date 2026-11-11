
from fastapi import FastAPI
from database import create_table
from routes.task import router as task_router

app = FastAPI(
    title="Task Management API",
    description="API for managing tasks using FastAPI and SQLite",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    create_table()


app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "Welcome to Task Management API"}
