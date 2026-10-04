"""AI-assisted tests for Lab 4."""

from app.tasks import (
    add_task, 
    complete_task, 
    get_pending_tasks,
    average_priority,
    find_task_by_title,
    )


def test_TC03_add_task():
    tasks = []

    add_task(tasks, "Study", priority=2, tags=["school"])

    assert tasks == [
        {
            "id": 1,
            "title": "Study",
            "priority": 2,
            "tags": ["school"],
            "done": False,
        }
    ]


def test_TC04_complete_existing_task():
    tasks = []
    add_task(tasks, "Study")

    result = complete_task(tasks, 1)

    assert result is True
    assert tasks[0]["done"] is True


def test_TC05_complete_unknown_task():
    tasks = []
    add_task(tasks, "Study")

    result = complete_task(tasks, 99)

    assert result is False
    assert tasks[0]["done"] is False

def test_TC06_pending_tasks():
    tasks = []
    add_task(tasks, "Study")
    add_task(tasks, "Exercise")
    add_task(tasks, "Write report")
    complete_task(tasks, 2)

    pending = get_pending_tasks(tasks)

    assert [task["title"] for task in pending] == [
        "Study",
        "Write report",
    ]


def test_TC07_all_tasks_completed():
    tasks = []
    add_task(tasks, "Study")
    add_task(tasks, "Exercise")
    complete_task(tasks, 1)
    complete_task(tasks, 2)

    assert get_pending_tasks(tasks) == []

def test_TC08_average_priority():
    tasks = []
    add_task(tasks, "Study", priority=1)
    add_task(tasks, "Write report", priority=3)

    assert average_priority(tasks) == 2


def test_TC09_average_priority_empty_list():
    assert average_priority([]) == 0

def test_TC10_find_first_matching_title():
    tasks = []
    add_task(tasks, "Study")
    add_task(tasks, "Exercise")
    add_task(tasks, "Study")

    result = find_task_by_title(tasks, "Study")

    assert result is tasks[0]


def test_TC11_find_unknown_title():
    tasks = []
    add_task(tasks, "Study")

    result = find_task_by_title(tasks, "Missing")

    assert result is None