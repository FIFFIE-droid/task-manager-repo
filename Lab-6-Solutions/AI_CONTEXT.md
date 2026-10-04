# AI generation record

The student pasted app/tasks.py and tests/test_tasks.py into ChatGPT and asked
to continue Labs 5 and 6 before the deadline. The assistant selected these
three functions based on that code and the previous Lab 4 traceability table.

The following are reproducible per-function prompts, not a claim that the
student separately typed these exact sentences in the original conversation:

1. Given the pasted remove_task implementation and its "Remove a task by id"
   docstring, generate pytest unit tests for existing and unknown IDs and an
   empty task list. Check actual list contents and preserve unaffected tasks.
2. Given the pasted save_tasks implementation and its "Persist tasks to disk"
   docstring, generate pytest tests that isolate TASKS_FILE with monkeypatch
   and tmp_path. Inspect saved JSON rather than relying on load_tasks.
3. Given the pasted load_tasks implementation and its docstring about missing
   files, generate pytest tests using independently written JSON fixtures.
   Check existing and missing files, plus current malformed-JSON behaviour.

Initial AI output: test_ai_generated.py. Syntax/import corrections and later
changes made by the student should be recorded here: __________
