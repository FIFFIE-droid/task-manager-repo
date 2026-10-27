# Lab 8 Results Report — Visual Regression and Accessibility Testing

## 1. Visual Regression Testing

- **Target page:** `Lab-8-Solutions/site/demo_page.html`
- **Tool:** Playwright
- **Baseline snapshot:** `tests/visual.spec.js-snapshots/demo-page-baseline-win32.png`
- **Deliberate CSS change:** The page's body background colour was changed to red using JavaScript.
- **Observed pixel difference:** 602,286 pixels, approximately 59% of the screenshot.
- **Baseline test:** Passed.
- **Deliberate-change test:** Failed as expected because the screenshot differed from the baseline.
- **Diff evidence:** `test-results/visual-deliberate-visual-c-4226c-ted-by-screenshot-assertion/demo-page-baseline-diff.png`
- **Actual screenshot:** `test-results/visual-deliberate-visual-c-4226c-ted-by-screenshot-assertion/demo-page-baseline-actual.png`

The results demonstrate that Playwright detected a deliberate visual change by comparing the current screenshot with the saved baseline.

## 2. Accessibility Testing

- **Scanner:** axe-core using `@axe-core/playwright`
- **WCAG tags:** WCAG 2.0 A/AA and WCAG 2.1 A/AA
- **Initial violations:** 5 violation categories
- **Violations after fixes:** 3 violation categories

### Accessibility Triage Table

| Rule | Impact | Evidence | Remediation | After-scan status |
|---|---|---|---|---|
| `select-name` | Critical | The dropdown did not have an accessible name. | Added `aria-label="Select progress percentage"` to the dropdown. | Resolved: absent from the latest violations list. |
| `frame-title` | Serious | Three iframe elements lacked accessible titles. | Added descriptive `title` attributes to the three iframes. | Resolved: absent from the latest violations list. |
| `color-contrast` | Serious | One element failed the colour-contrast requirement. | Further remediation is needed. | Unresolved |
| `image-alt` | Critical | One image lacked appropriate alternative text. | Further remediation is needed. | Unresolved |
| `label` | Critical | Thirteen elements lacked accessible labels. | Further remediation is needed. | Unresolved |

The accessibility rescan reported three remaining violation categories: `color-contrast`, `image-alt`, and `label`. The dropdown accessible-name and iframe-title violations were no longer present in the latest violations list.

## 3. Reflection

A pixel-diff test compares the visual appearance of a page against a baseline screenshot. It may detect visible changes but cannot reliably identify accessibility problems that do not change the rendered pixels, such as missing accessible names, missing programmatic labels, or incorrect semantic relationships.

Therefore, visual regression testing and accessibility scanning should be used together. Visual regression testing identifies unintended appearance changes, while axe-core checks accessibility rules and reports violations that may affect users of assistive technologies.

## 4. Conclusion

The Lab 8 tests demonstrated that Playwright can detect deliberate visual changes and that axe-core can identify accessibility violations. Two accessibility issues were addressed and confirmed resolved by rescanning. Three violation categories remain and are documented for further remediation.