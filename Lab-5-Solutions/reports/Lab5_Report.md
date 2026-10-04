# Lab 5: UI Testing and Self-Healing

## What was tested

A local copy of the SeleniumBase demo website was tested using Python, Selenium, pytest and Healenium in Docker. The local copy allowed the page to be changed for this experiment.

The Page Object Model stored the locators and actions in `demo_page.py`. Five test cases read their inputs and expected results from `test_data.json`: text input, textarea, button colour, dropdown and checkbox.

## Results

| Run | Passed | Failed | Time |
|---|---:|---:|---|
| Original page, without healing | 5 | 0 | 62.87 seconds |
| Original page through Healenium (seed) | 5 | 0 | 34.55 seconds |
| Changed page, without healing | 4 | 1 | 43.12 seconds |
| Changed page, with Healenium | 5 | 0 | 71.14 seconds |

These are pytest results. Passing tests alone do not prove that the correct element was healed.

## Locator change and healing result

The first text input's ID was changed from `myTextInput` to `myTextInputChanged`. The test continued to request the original ID. Without healing, UI01 failed because the original locator could not find the element.

The Healenium report showed:

| Item | Observed result |
|---|---|
| Failed locator | `[id="myTextInput"]` |
| Healed locator | `input#myTextInput2` |
| Healing score | 0.93 |
| Correct element selected? | No: it selected the separate pre-filled text field |
| Affected test cases | 1 |
| Correctly healed affected cases | 0 |
| Wrong-element healings | 1 |
| Correct healing success rate | 0 / 1 × 100 = **0%** |

The report screenshot highlighted the pre-filled field. The intended field was `myTextInputChanged`. The score of 0.93 did not mean that the repair was correct.

## Short analysis

Healenium found another text field and the test passed. However, the test typed into that field and checked the value in the same field. This allowed a wrong repair to produce a passing result.

Self-healing can help when a locator changes, but its chosen element needs to be checked. A stronger test should independently verify that the intended field contains the entered text. This improvement has been identified; it has not been rerun in the recorded results.

Earlier seed attempts had browser startup and session timeout errors. The final seed run passed after increasing the session timeout and allowing the Chrome container to start. A report navigation error was bypassed by opening the report's full address directly.

## Evidence and assistance

Keep the actual terminal output, JUnit XML and screenshots in `reports/baseline`, `reports/seed`, `reports/drift` and `reports/healing`. Save the displayed Healenium report screenshot in `reports/healing`.

ChatGPT generated the initial automation scaffold and helped with setup, troubleshooting and this report. The student ran the tests and supplied the terminal results and report screenshot.

