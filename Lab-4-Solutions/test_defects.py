"""AI-assisted reproduction tests for Lab 4 defects."""

import sqlite3
from app.storage import format_task_report, build_query


def test_D01_report_with_numeric_id():
    tasks = [{"id": 1, "title": "Study"}]

    assert format_task_report(tasks) == "Task #1: Study"


def test_D02_query_title_with_apostrophe():
    title = "Bob's task"

    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE tasks (title TEXT)")
        connection.execute(
            "INSERT INTO tasks (title) VALUES (?)",
            (title,),
        )

        query, parameters = build_query(title)
        results = connection.execute(query, parameters).fetchall()

        assert results == [(title,)]