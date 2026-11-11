
import sqlite3
import pytest
from fastapi.testclient import TestClient

import database
import services.task as task_service


@pytest.fixture
def client(tmp_path, monkeypatch):

    db_path = tmp_path / "test_tasks.db"

    def get_test_connection():
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    # Redirect database connections to the temporary database
    monkeypatch.setattr(
        database,
        "get_connection",
        get_test_connection
    )

    monkeypatch.setattr(
        task_service,
        "get_connection",
        get_test_connection
    )

    from main import app

    with TestClient(app) as test_client:
        yield test_client
