
import json
import pytest
from app.tasks import remove_task
from app import tasks as task_module


def test_remove_a_task():
    tasks = [
        {"id": 1, "title": "Study"},
        {"id": 2, "title": "Submit"},
    ]
    remove_task(tasks, 1)

    assert tasks == [{"id": 2, "title": "Submit"}]

def test_load_tasks(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setattr(task_module, "TASKS_FILE", str(tasks_file))
    tasks = [
        {"id": 1, "title": "Study"},
        {"id": 2, "title": "Submit"},
    ]
    with open(tasks_file, "w") as f:
        json.dump(tasks, f)

    loaded_tasks = task_module.load_tasks()

    assert loaded_tasks == tasks

def test_save_tasks(tmp_path, monkeypatch):
    tasks_file = tmp_path / "tasks.json"
    monkeypatch.setattr(task_module, "TASKS_FILE", str(tasks_file))
    tasks = [
        {"id": 1, "title": "Study"},
        {"id": 2, "title": "Submit"},
    ]

    task_module.save_tasks(tasks)

    with open(tasks_file, "r") as f:
     loaded_tasks = json.load(f)

    assert loaded_tasks == tasks