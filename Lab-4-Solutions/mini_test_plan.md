# Mini test plan:R08 Premium Customer Discount

Status: Draft based on the function’s code. Uses an IEEE 829-style structure.

**Scope:** The premium discount in calculate_discount

**Test items:** app/tasks.py:calculate_discount

**Approach:** Run the existing unit test using price=100 and is_premium=True. Compare the returned value with the expected result of 80.

**Entry criteria:** Python and pytest work, and the function and test file are available

**Pass criteria:** The function returns 80 for the specified inputs.

**Exit criteria:** TC01 returns the expected 80 for price 100, and its result is recorded

**Evidence:** The terminal run showed test_calculate_discount_for_premium_user PASSED. Save a screenshot of that output in the Lab 4 screenshots folder.

**Roles:** The student runs the test and reviews the result. AI assistance with drafting the plan is disclosed.
