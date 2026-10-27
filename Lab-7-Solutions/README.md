# Lab 7 — Mutation Testing & Suite Effectiveness

The harness applies source mutations to temporary copies and runs the Lab 6 AI-only, manual-only, and combined suites. It is a small custom educational harness rather than `mutmut`; mention the tool substitution to the lecturer.

Run from the repository root:
```powershell
python .\Lab-7-Solutions\run_mutations.py
```

The script writes detailed results to `reports/mutation_results.csv` and summary data to `reports/mutation_summary.json`. Inspect all rows, check that all intended mutants are valid, then report actual scores. The working `app/tasks.py` is not changed by the harness.
