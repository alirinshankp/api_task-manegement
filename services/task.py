
from fastapi import HTTPException
from database import get_connection


def get_all_tasks(status=None, priority=None):
    conn = get_connection()

    try:
        query = "SELECT * FROM tasks WHERE 1=1"
        values = []

        if status is not None:
            query += " AND status = ?"
            values.append(status.value)

        if priority is not None:
            query += " AND priority = ?"
            values.append(priority.value)

        query += " ORDER BY id"

        cursor = conn.execute(query, values)

        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()


def get_task(task_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        )

        task = cursor.fetchone()

        if task is None:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return dict(task)

    finally:
        conn.close()


def add_task(task):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO tasks (title, description, priority, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                task.title,
                task.description,
                task.priority.value,
                task.status.value
            )
        )

        conn.commit()

        return get_task_from_connection(conn, cursor.lastrowid)

    finally:
        conn.close()


def get_task_from_connection(conn, task_id):
    cursor = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return dict(task)


def update_task(task_id: int, task):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, priority = ?, status = ?
            WHERE id = ?
            """,
            (
                task.title,
                task.description,
                task.priority.value,
                task.status.value,
                task_id
            )
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return get_task_from_connection(conn, task_id)

    finally:
        conn.close()


def update_task_status(task_id: int, status):
    conn = get_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """,
            (status.status.value, task_id)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return get_task_from_connection(conn, task_id)

    finally:
        conn.close()


def delete_task(task_id: int):
    conn = get_connection()

    try:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return {"message": "Task deleted successfully"}

    finally:
        conn.close()
