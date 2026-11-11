
from fastapi import APIRouter
from schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskStatusUpdate,
    TaskResponse,
    TaskPriority,
    TaskStatus
)

from services.task import (
    get_all_tasks,
    get_task,
    add_task,
    update_task,
    update_task_status,
    delete_task
)

router = APIRouter()


@router.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201
)
def create_task(task: TaskCreate):
    return add_task(task)


@router.get(
    "/tasks",
    response_model=list[TaskResponse]
)
def read_all_tasks(
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None
):
    return get_all_tasks(status, priority)


@router.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def read_task(task_id: int):
    return get_task(task_id)


@router.put(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def edit_task(task_id: int, task: TaskUpdate):
    return update_task(task_id, task)


@router.patch(
    "/tasks/{task_id}/status",
    response_model=TaskResponse
)
def edit_task_status(task_id: int, status: TaskStatusUpdate):
    return update_task_status(task_id, status)


@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)
