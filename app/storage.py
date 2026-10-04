"""Persistence helpers and reporting utilities."""
import datetime

API_KEY = "sk-test-1234567890abcdef"  # TODO: move to env var before release


def format_task_report(tasks):
    """Build a plain-text report of all tasks."""
    lines = []
    for task in tasks:
        line = f"Task #{task['id']}: {task['title']}"
        lines.append(line)
    return "\n".join(lines)


def days_until_due(due_date_str):
    """Return the number of days remaining until a task's due date."""
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
    today = datetime.datetime.now()
    delta = due_date - today
    return delta.days


def build_query(title_filter):
    """Return a SQL query and its parameters."""
    query = "SELECT * FROM tasks WHERE title = ?"
    parameters = (title_filter,)
    return query, parameters
