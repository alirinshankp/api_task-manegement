
def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Python",
            "description": "Complete Python basics",
            "priority": "High",
            "status": "Pending"
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn Python"
    assert response.json()["priority"] == "High"


def test_get_all_tasks(client):
    client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Study API development",
            "priority": "Medium"
        }
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_task_by_id(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Learn SQL",
            "description": "Practice SQL queries",
            "priority": "Low"
        }
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Learn SQL"


def test_update_task(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Learn Python",
            "description": "Basics",
            "priority": "Low"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Learn Advanced Python",
            "description": "Complete advanced topics",
            "priority": "High",
            "status": "In Progress"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Learn Advanced Python"
    assert response.json()["status"] == "In Progress"


def test_update_task_status(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Complete project",
            "description": "Finish API project",
            "priority": "High"
        }
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}/status",
        json={"status": "Completed"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Completed"


def test_delete_task(client):
    create_response = client.post(
        "/tasks",
        json={
            "title": "Learn Git",
            "description": "Practice Git commands",
            "priority": "Medium"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404


def test_filter_by_priority(client):
    client.post(
        "/tasks",
        json={
            "title": "High priority task",
            "priority": "High"
        }
    )

    client.post(
        "/tasks",
        json={
            "title": "Low priority task",
            "priority": "Low"
        }
    )

    response = client.get("/tasks?priority=High")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["priority"] == "High"


def test_filter_by_status(client):
    client.post(
        "/tasks",
        json={
            "title": "Pending task",
            "priority": "Medium",
            "status": "Pending"
        }
    )

    client.post(
        "/tasks",
        json={
            "title": "Completed task",
            "priority": "Medium",
            "status": "Completed"
        }
    )

    response = client.get("/tasks?status=Completed")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["status"] == "Completed"


def test_invalid_priority(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test task",
            "priority": "Urgent"
        }
    )

    assert response.status_code == 422


def test_task_not_found(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
