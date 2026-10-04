"""AI-generated tests for the three previously untested functions supplied by the student."""
import copy
import json
import pytest
from app import tasks as task_module


@pytest.fixture
def isolated_file(monkeypatch, tmp_path):
    path = tmp_path / "tasks.json"
    monkeypatch.setattr(task_module, "TASKS_FILE", str(path))
    return path


def test_remove_existing_id_preserves_other_tasks():
    tasks = [{"id": 1, "title": "Read"}, {"id": 2, "title": "Study"},
             {"id": 3, "title": "Submit"}]
    expected = copy.deepcopy([tasks[0], tasks[2]])
    task_module.remove_task(tasks, 2)
    assert tasks == expected


def test_remove_unknown_id_leaves_tasks_unchanged():
    tasks = [{"id": 1, "title": "Read"}, {"id": 2, "title": "Study"}]
    expected = copy.deepcopy(tasks)
    task_module.remove_task(tasks, 99)
    assert tasks == expected


def test_remove_from_empty_list():
    tasks = []
    task_module.remove_task(tasks, 1)
    assert tasks == []


def test_save_preserves_every_field(isolated_file):
    tasks = [{"id": 7, "title": "Study", "priority": 3,
              "tags": ["school", "urgent"], "done": True}]
    task_module.save_tasks(tasks)
    assert isolated_file.exists()
    assert json.loads(isolated_file.read_text()) == tasks


def test_save_empty_list(isolated_file):
    task_module.save_tasks([])
    assert json.loads(isolated_file.read_text()) == []


def test_save_replaces_old_file_contents(isolated_file):
    isolated_file.write_text('[{"id": 99, "title": "Old task"}]')
    tasks = [{"id": 1, "title": "New task", "done": False}]
    task_module.save_tasks(tasks)
    assert json.loads(isolated_file.read_text()) == tasks


def test_load_existing_json_preserves_data(isolated_file):
    expected = [{"id": 4, "title": "Report", "priority": 2,
                 "tags": ["school"], "done": False}]
    # Write independently of save_tasks, so a matching save/load bug cannot hide.
    isolated_file.write_text(json.dumps(expected))
    assert task_module.load_tasks() == expected


def test_load_missing_file_returns_empty_list(isolated_file):
    assert task_module.load_tasks() == []


def test_load_invalid_json_raises_decoder_error(isolated_file):
    isolated_file.write_text("not valid JSON")
    # Records current behaviour; this is not an invented assessed requirement.
    with pytest.raises(json.JSONDecodeError):
        task_module.load_tasks()
