# Lab 9 Test Charter — Task Manager Core

**Mission:** Explore task persistence and deletion to discover failures that could cause a user to lose, duplicate, or incorrectly retain tasks.

**Scope:** `app/tasks.py`: `remove_task`, `save_tasks`, and `load_tasks`; exercise empty lists, known and unknown IDs, existing/missing files, valid and malformed JSON, and persistence round trips. Excludes performance, multi-user concurrency, and UI behavior.

**Time-box:** 45 minutes. Stop when the timer ends even if an avenue remains unfinished.

**AI co-pilot prompts / five avenues:**
1. Delete first, middle, last, missing, and duplicate IDs; inspect whether exactly one or all matching tasks are removed.
2. Load when the file is absent, empty, valid JSON, malformed JSON, and valid JSON of an unexpected type.
3. Save an empty list and a task containing all fields; inspect exact persisted JSON.
4. Save then load the same data and compare all fields and types.
5. Explore file permissions/path errors and determine whether failures are clear and safely handled.

**Evidence rules:** Timestamp observations as they occur. Record reproducible steps, expected/actual result, severity, and whether the avenue came from AI or personal exploration. AI suggestions are prompts, not proof of a defect. Do not label an unexecuted hypothesis as a confirmed bug.
