const { test, expect } = require('@playwright/test');
const path = require('path');
const pageUrl = 'file://' + path.resolve(__dirname, '../../Lab-5-Solutions/site/demo_page.html').replace(/\\/g, '/');
test('capture baseline screenshot for local demo page', async ({ page }) => {
  await page.goto(pageUrl);
  await expect(page.locator('body')).toBeVisible();
  await expect(page).toHaveScreenshot('demo-page-baseline.png', { fullPage: true, animations: 'disabled' });
});

test('deliberate visual change is detected by screenshot assertion', async ({ page }) => {
  await page.goto(pageUrl);

  // Make a large, clearly visible change to the page.
  await page.evaluate(() => {
    document.body.style.setProperty('background-color', 'red', 'important');
  });

  // Confirm the change was applied.
  console.log(
    'Body background:',
    await page.locator('body').evaluate(el => getComputedStyle(el).backgroundColor)
  );

  // Compare the changed page against the original baseline.
  await expect(page).toHaveScreenshot('demo-page-baseline.png', {
    fullPage: true,
    animations: 'disabled'
  });
});

