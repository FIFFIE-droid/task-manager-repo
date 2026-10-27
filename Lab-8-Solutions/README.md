# Lab 8 — Visual Regression & Accessibility Testing

The target is the existing local HTML demo at `Lab-5-Solutions/site/demo_page.html`. Playwright captures a screenshot baseline, provides a second test with a deliberate CSS change, and axe-core exports machine-readable accessibility findings.

## Setup and run (PowerShell, from this folder)
```powershell
npm install
npx playwright install chromium
npm run test:visual -- --update-snapshots   # create initial reference snapshot
npm run test:visual                        # baseline should pass; deliberate-change test should show a diff/fail until its expected snapshot is accepted
npm run test:a11y
```
For a clean demonstration of the deliberate change, preserve the failed diff under `test-results/` before updating the second snapshot. Do not update the second snapshot before capturing failure evidence.

The existing HTML includes a viewport meta tag with `initial-scale=0.41`; some controls may lack accessible names. Confirm actual axe findings before classifying or fixing them. Do not invent violation counts or claim fixes are verified without a real before/after scan.
