
import sqlite3


def get_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT NOT NULL
                    CHECK(priority IN ('Low', 'Medium', 'High')),
                status TEXT NOT NULL
                    CHECK(status IN ('Pending', 'In Progress', 'Completed'))
            )
        """)

        conn.commit()

    finally:
        conn.close()
