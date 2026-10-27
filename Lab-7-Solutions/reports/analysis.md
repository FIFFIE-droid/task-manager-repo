# Lab 7 Mutation Analysis

The mutation runner and result files are included. Before submission, rerun `python Lab-7-Solutions/run_mutations.py` and inspect the current CSV/JSON; do not use the old numbers unless the run completes successfully. A mutant is killed when a test fails against the mutated implementation; a surviving mutant means the tests did not detect the change. Mutation score = killed valid mutants / valid mutants × 100.

Mutation testing complements Lab 6 coverage: coverage says which lines executed, while mutation testing checks whether assertions detect changes to behavior. A test can execute a line and still survive a mutation if its assertions are weak or fail to distinguish the correct result from the incorrect result.

The report must name at least three surviving mutants from the completed CSV, explain the missing assertion for each, add targeted tests, and rerun. Do not claim improvement until the final run provides evidence.
