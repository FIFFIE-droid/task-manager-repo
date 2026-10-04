**Functions tested:** `remove_task`, `save_tasks` and `load_tasks`.

| Suite | Tests passed | Whole-module coverage | Assert statements | Assertion strength |
|---|---:|---:|---:|---|
| AI only | 9 | 47.92% | 9 | Strong |
| Student suite, with AI help | 3 | 45.83% | 3 | Strong for the cases tested |
| Combined | 12 | 47.92% | 12 | Strong |

AI and combined suites also contain one exception check each. All three runs passed.

The percentages above cover the whole `app/tasks.py` module. For the three selected function bodies only, coverage was **100% for AI, 90.91% for the student suite, and 100% combined**. Other functions explain the lower whole-module percentages.

#Comparison

The AI suite checked more situations, including empty lists, unknown IDs, missing files and invalid JSON. Its assertions checked actual results. For example, its save test compared all task fields with the saved JSON.

The student suite checked normal removal, saving and loading. Its assertions compared the results with expected task lists. It also tested removing the first task, while the AI existing-ID test removed the middle task.

Combining the suites added **0 percentage points** of coverage because the AI tests already covered the measured lines. The extra first-task removal case still added a useful behaviour check. The AI suite did not explicitly test removing the first or last task; the student suite addressed the first-task case.

High coverage does not prove every input works. Both suites used meaningful assertions, so this experiment did not show high coverage caused only by checking that functions do not crash.

# AI assistance

ChatGPT generated the AI tests and this comparison. The student drafted the second suite after an AI example, and AI helped correct its function calls, file setup and indentation.

# Student reflection

I learned that a test must call the application’s function and check its actual result. I also learned that high coverage does not mean every situation has been tested.
