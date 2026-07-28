from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select

from database import engine, create_db_and_tables
from models import Task

app = FastAPI(
    title="Task API",
    version="1.0"
)


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


@app.on_event("startup")
def startup():

    create_db_and_tables()

    with Session(engine) as session:

        tasks = session.exec(select(Task)).all()

        if len(tasks) == 0:
            session.add(Task(title="Learn FastAPI"))
            session.add(Task(title="Build CRUD API"))
            session.add(Task(title="Upload project"))
            session.commit()


@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():

    with Session(engine) as session:
        return session.exec(select(Task)).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    with Session(engine) as session:

        task = session.get(Task, task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )

        return task


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    with Session(engine) as session:

        new_task = Task(
            title=task.title,
            done=False
        )

        session.add(new_task)
        session.commit()
        session.refresh(new_task)

        return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskUpdate):

    with Session(engine) as session:

        task = session.get(Task, task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )

        if updated.title is not None:
            task.title = updated.title

        if updated.done is not None:
            task.done = updated.done

        session.add(task)
        session.commit()
        session.refresh(task)

        return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    with Session(engine) as session:

        task = session.get(Task, task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )

        session.delete(task)
        session.commit()

        return