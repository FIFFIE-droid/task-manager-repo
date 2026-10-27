# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: visual.spec.js >> deliberate visual change is detected by screenshot assertion
- Location: tests\visual.spec.js:10:1

# Error details

```
Error: expect(page).toHaveScreenshot(expected) failed

  602286 pixels (ratio 0.59 of all image pixels) are different.

  Snapshot: demo-page-baseline.png

Call log:
  - Expect "toHaveScreenshot(demo-page-baseline.png)" with timeout 5000ms
    - verifying given screenshot expectation
  - taking page screenshot
    - disabled all CSS animations
  - waiting for fonts to load...
  - fonts loaded
  - 605330 pixels (ratio 0.60 of all image pixels) are different.
  - waiting 100ms before taking screenshot
  - taking page screenshot
    - disabled all CSS animations
  - waiting for fonts to load...
  - fonts loaded
  - 3044 pixels (ratio 0.01 of all image pixels) are different.
  - waiting 250ms before taking screenshot
  - taking page screenshot
    - disabled all CSS animations
  - waiting for fonts to load...
  - fonts loaded
  - captured a stable screenshot
  - 602286 pixels (ratio 0.59 of all image pixels) are different.

```

# Page snapshot

```yaml
- table [ref=e3]:
  - rowgroup [ref=e4]:
    - row [ref=e5]:
      - cell [ref=e6]:
        - heading "Demo Page" [level=1] [ref=e7]
      - cell [ref=e8]:
        - heading "SeleniumBase" [level=2] [ref=e9]
      - cell "Hover Dropdown" [ref=e10]
      - cell [ref=e13]:
        - heading "Automation Practice" [level=3] [ref=e14]
    - row [ref=e15]:
      - cell "Text Input Field:" [ref=e16]
      - cell [ref=e17]:
        - textbox [ref=e18]
      - cell "Textarea:" [ref=e19]
      - cell [ref=e20]:
        - textbox [ref=e21]
    - row [ref=e22]:
      - cell "Pre-Filled Text Field:" [ref=e23]
      - cell [ref=e24]:
        - textbox [ref=e25]: Text...
      - cell "Button:" [ref=e26]
      - cell [ref=e27]:
        - button "Click Me (Green)" [ref=e28]
    - row [ref=e29]:
      - cell "Placeholder Text Field:" [ref=e30]
      - cell [ref=e31]:
        - textbox "Placeholder Text Field" [ref=e32]
      - cell "Read-Only Text Field:" [ref=e33]
      - cell [ref=e34]:
        - textbox [ref=e35]: The Color is Green
    - row [ref=e36]:
      - cell "HTML SVG with rect:" [ref=e37]
      - cell [ref=e38]
      - cell [ref=e41]:
        - paragraph [ref=e42]: "Paragraph with Text:"
      - cell [ref=e43]:
        - paragraph [ref=e44]: This Text is Green
    - row [ref=e45]:
      - cell "Input Slider Control:" [ref=e46]
      - cell [ref=e47]:
        - slider [ref=e48]: "50"
      - 'cell "Progress Bar: (50%)" [ref=e49]'
      - cell [ref=e50]:
        - 'progressbar "Progress Bar: (50%)" [ref=e51]'
    - row [ref=e52]:
      - cell "Select Dropdown:" [ref=e53]
      - cell "Set to 25%" [ref=e54]:
        - combobox [ref=e55]:
          - option "Set to 25%" [selected]
          - option "Set to 50%"
          - option "Set to 75%"
          - option "Set to 100%"
      - 'cell "HTML Meter: (25%)" [ref=e56]'
      - cell [ref=e57]:
        - 'meter "HTML Meter: (25%)" [ref=e58]'
    - row [ref=e59]:
      - cell "Image in iFrame:" [ref=e60]
      - cell [ref=e62]:
        - iframe [ref=e63]
        - iframe [ref=e64]:
          - heading "iFrame Text" [level=4] [ref=f2e2]
      - cell "RadioButton 1:" [ref=e65]:
        - text: "RadioButton 1:"
        - radio [checked] [ref=e66]
      - cell "RadioButton 2:" [ref=e67]:
        - text: "RadioButton 2:"
        - radio [ref=e68]
    - row [ref=e69]:
      - cell "CheckBox:" [ref=e70]:
        - text: "CheckBox:"
        - checkbox [ref=e71]
      - cell "CheckBoxes:" [ref=e72]:
        - text: "CheckBoxes:"
        - checkbox [ref=e73]
        - checkbox [ref=e74]
        - checkbox [ref=e75]
      - cell "Pre-Check Box:" [ref=e76]:
        - text: "Pre-Check Box:"
        - checkbox [checked] [ref=e77]
      - cell "CheckBox in iFrame:" [ref=e78]:
        - text: "CheckBox in iFrame:"
        - iframe [ref=e79]:
          - checkbox [ref=f3e2]
    - row [ref=e80]:
      - cell "URL Link:" [ref=e81]
      - cell [ref=e82]:
        - link "seleniumbase.com" [ref=e83] [cursor=pointer]:
          - /url: https://seleniumbase.com
      - cell "Link with Text:" [ref=e84]
      - cell [ref=e85]:
        - link "SeleniumBase on GitHub" [ref=e86] [cursor=pointer]:
          - /url: https://github.com/seleniumbase/SeleniumBase
    - row [ref=e87]:
      - cell "SeleniumBase Docs:" [ref=e88]
      - cell [ref=e89]:
        - link "seleniumbase.io" [ref=e90] [cursor=pointer]:
          - /url: https://seleniumbase.io
      - cell "The Demo Page:" [ref=e91]
      - cell [ref=e92]:
        - link "SeleniumBase Demo Page" [ref=e93] [cursor=pointer]:
          - /url: https://seleniumbase.io/demo_page/
```

# Test source

```ts
  1  | const { test, expect } = require('@playwright/test');
  2  | const path = require('path');
  3  | const pageUrl = 'file://' + path.resolve(__dirname, '../../Lab-5-Solutions/site/demo_page.html').replace(/\\/g, '/');
  4  | test('capture baseline screenshot for local demo page', async ({ page }) => {
  5  |   await page.goto(pageUrl);
  6  |   await expect(page.locator('body')).toBeVisible();
  7  |   await expect(page).toHaveScreenshot('demo-page-baseline.png', { fullPage: true, animations: 'disabled' });
  8  | });
  9  | 
  10 | test('deliberate visual change is detected by screenshot assertion', async ({ page }) => {
  11 |   await page.goto(pageUrl);
  12 | 
  13 |   // Make a large, clearly visible change to the page.
  14 |   await page.evaluate(() => {
  15 |     document.body.style.setProperty('background-color', 'red', 'important');
  16 |   });
  17 | 
  18 |   // Confirm the change was applied.
  19 |   console.log(
  20 |     'Body background:',
  21 |     await page.locator('body').evaluate(el => getComputedStyle(el).backgroundColor)
  22 |   );
  23 | 
  24 |   // Compare the changed page against the original baseline.
> 25 |   await expect(page).toHaveScreenshot('demo-page-baseline.png', {
     |                      ^ Error: expect(page).toHaveScreenshot(expected) failed
  26 |     fullPage: true,
  27 |     animations: 'disabled'
  28 |   });
  29 | });
  30 | 
  31 | 
```