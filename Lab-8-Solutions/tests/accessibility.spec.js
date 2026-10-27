const { test, expect } = require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');
const path = require('path');
const fs = require('fs');
const pageUrl = 'file://' + path.resolve(__dirname, '../site/demo_page.html').replace(/\\/g, '/');
test('run axe accessibility scan and save violations', async ({ page }) => {
  await page.goto(pageUrl);
  const results = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
  fs.mkdirSync(path.resolve(__dirname, '../reports'), { recursive: true });
  fs.writeFileSync(path.resolve(__dirname, '../reports/axe-results.json'), JSON.stringify(results, null, 2));
  console.log(`Axe violations: ${results.violations.length}`);
  expect(results.passes.length).toBeGreaterThan(0);
});
