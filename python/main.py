"""
Main entry point for starting the didactic lamp.
"""

import datetime
from typing import Dict, Optional

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

tasks: Dict[str, list] = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in ["http://localhost","http://localhost:4200","http://localhost:3000","http://localhost:8080","https://localhost","https://localhost:4200","https://localhost:3000","https://localhost:8080"]],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    """
    Class that represents our FastAPI response model.
    """

    name: Optional[str] = None
    items: Optional[list] = None


@app.get("/")
async def root():
    """
    This is just a dummy endpoint to show that the server is running.
    """
    return {"message": f"Hello, World! It's currently {await health()} (UTC)."}


@app.get("/healthz")
async def health():
    """
    This is an health endpoint that returns the current time,
    called by the Kubernetes health check system.
    """
    return datetime.datetime.utcnow().isoformat()


@app.get("/tasks", response_model=Task, response_model_exclude_none=True)
async def get_task():
    """
    This is the endpoint that returns the latest task, removing it from the list.
    Returns an empty list if there are no tasks.
    """
    if len(tasks.keys()) > 0:
        first_task_id = list(tasks.keys())[0]
        task = tasks.pop(first_task_id)
        return Task(name=first_task_id, items=task)
    return Task()


@app.post("/tasks")
async def create_task(task: Dict[str, list]):
    """
    This is the endpoint that creates a new task, adding it to the list.
    """
    _tasks = task.get("task")
    if _tasks:
        _task = _tasks[0]
        tasks_id, tasks_val = list(_task.items())[0]
        tasks[tasks_id] = tasks_val
        return task


def main():  # pragma: no cover
    """
    Main entry point for starting the didactic lamp.
    """
    uvicorn.run(
        "didactic_lamp.main:app", host="0.0.0.0", port=8080, log_level="info", log_config=None
    )


if __name__ == "__main__":  # pragma: no cover
    main()
