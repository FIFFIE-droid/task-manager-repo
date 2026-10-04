# Lab 6: AI-generated tests and coverage comparison

Selected functions: app.tasks.remove_task, save_tasks, load_tasks. They do not
appear in the existing tests/test_tasks.py pasted by the student; the Lab 4
traceability table marked their planned cases Not Run. Check other test files
before claiming no earlier tests existed anywhere in the repository.

AI assistant: ChatGPT in this conversation. Record the model/account actually
used; do not describe the account as free unless it was. AI produced the AI
suite, import scaffold, report runner and this README. It did not write the
manual test suite. Source code and docstrings were supplied in the conversation.

## Fast workflow from the repository root

1. Run the AI suite:
   `python .\Lab-6-Solutions\run_coverage.py ai`
2. Run your manual suite:
   `python .\Lab-6-Solutions\run_coverage.py manual`
3. Run both:
   `python .\Lab-6-Solutions\run_coverage.py combined`

Already installed on the student's computer: pytest and pytest-cov.
If required: `python -m pip install pytest pytest-cov`

## Submission checklist

- AI test file and genuinely independent manual test file, both runnable.
- Three real coverage reports: AI, manual and combined.
- Comparison with coverage percentages, assertion counts and weak/strong
  ratings supported by examples, plus your short verdict/reflection.
- Accurate disclosure of AI assistance, and your student details.
