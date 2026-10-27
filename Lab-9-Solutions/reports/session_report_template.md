# Lab 9 — Exploratory Testing Session Report

> **Session note:** The tests below were performed individually. Exact test times were not recorded, and completion of the full 45-minute time-box has not been established.

## Session summary

- **Charter:** Task persistence and deletion reliability.
- **Time-box:** 45 minutes (required; full duration not confirmed).
- **Build/commit tested:** Local working copy; commit hash not recorded.
- **Areas explored:** Task creation, deletion, completion, pending-task filtering, title search, average priority, discounts, saving and loading task data, malformed JSON, unexpected JSON structures, and invalid save paths.
- **Confirmed reproducible issues:** 3 potential defects requiring requirements-based confirmation.

## Findings

| ID | Reproduction steps | Expected | Actual | Severity | Source (AI/self) | Evidence |
|---|---|---|---|---|---|---|
| L9-01 | Add tasks with IDs 1 and 2; remove ID 1; add another task. | New task IDs should be unique. | The new task received ID 2, duplicating the remaining task's ID. | Medium | Self | Reproduced in terminal; output showed two tasks with ID 2. |
| L9-02 | Put malformed JSON in `tasks.json`; call `load_tasks()`. | Invalid data should be handled safely if recovery is required by the specification. | `load_tasks()` raised `JSONDecodeError`. | Medium | AI-suggested | Reproduced in terminal; exception traceback observed. |
| L9-03 | Put valid JSON `{"tasks": []}` in `tasks.json`; call `load_tasks()`. | Loaded data should be validated as a task list if that is the required format. | The function returned a dictionary instead of a list. | Medium | AI-suggested | Reproduced in terminal; returned `{'tasks': []}`. |
| L9-04 | Set the save destination to `missing_folder/tasks.json` and call `save_tasks([])`. | Invalid paths should be handled appropriately if graceful error handling is required. | `FileNotFoundError` was raised. | Low–Medium | AI-suggested | Reproduced in terminal; exception traceback observed. |
| L9-05 | Call `add_task()` with an empty title. | Depends on whether empty titles are prohibited by the requirements. | A task with an empty title was created. | Low; unconfirmed | Self | Reproduced in terminal; returned task had an empty title. |

**Note:** Findings L9-02 to L9-05 require checking the project requirements before classifying them as confirmed defects. An exception or unusual input is not automatically a bug if the behaviour is permitted by the specification.

## Other test results

The following behaviours were observed to work as expected in the tests performed:

- Removing a task by a known ID.
- Leaving the task list unchanged when removing an unknown ID.
- Returning an empty list when the task file is missing.
- Saving and loading an empty list.
- Preserving task fields in a save/load round-trip.
- Completing an existing task and returning `False` for a missing task ID.
- Calculating average priority for an empty list and a list containing priorities 2 and 4.
- Returning only pending tasks.
- Finding a task by title and returning `None` when no title matches.
- Applying a 20% premium discount and no discount for non-premium customers.

## AI vs. self-discovered avenues

The malformed JSON, unexpected JSON structure, and invalid save-path tests were explored using AI-suggested avenues. The duplicate-ID issue and empty-title behaviour were explored through self-generated tests.

- **Potential defects from AI-suggested avenues:** 3
- **Potential defects from self-generated avenues:** 2
- **Total potential findings:** 5

These counts represent potential findings, not five fully confirmed defects. The unique-ID issue is the clearest confirmed functional problem because two tasks ended up with the same ID after a deletion and subsequent addition.

Using the five potential findings as a provisional count:

- AI-suggested share: 3 / 5 × 100% = **60%**
- Self-found share: 2 / 5 × 100% = **40%**

These percentages describe the source of the potential findings, not the proportion of all possible bugs discovered.

## Reflection

AI suggestions helped broaden testing beyond normal task creation and deletion. They prompted checks for malformed JSON, unexpected JSON structures, and invalid file paths, which exposed behaviours that ordinary successful-use tests would not reveal.

The self-generated deletion-and-addition test exposed a particularly important issue: task IDs are generated using the current list length plus one. After a task is deleted, this can assign an ID that already belongs to another task. The terminal output showing two tasks with ID 2 provides direct evidence of the problem.

Some observations need further interpretation. For example, accepting an empty task title is only a defect if empty titles are prohibited. Similarly, raising an exception for malformed JSON or an invalid save path may be acceptable if the requirements permit errors to propagate. Comparing these behaviours with the project requirements would help determine which findings should be classified as confirmed bugs.

The tests demonstrate the value of combining AI-generated test ideas with independently designed tests. However, the full 45-minute session was not confirmed, and exact timestamps were not recorded. The session duration and any additional evidence should be updated if the required timed session is completed.