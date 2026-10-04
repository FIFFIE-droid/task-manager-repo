# Lab 5: Data-driven UI automation and self-healing

AI-assisted implementation.
Target: a local copy of https://seleniumbase.io/demo_page/ (SeleniumBase, MIT).
The local copy makes an intentional locator change possible. Analytics scripts
were removed from both baseline copies; the five tested controls are unchanged.
Original source: https://github.com/seleniumbase/seleniumbase.github.io
License: source/LICENSE. Five cases are read from test_data.json; locators and
actions are encapsulated in DemoPage. Each test gets a fresh Chrome session.

## Run from your task-manager-repo folder in PowerShell

1. Baseline:
   `python .\Lab-5-Solutions\run_lab5.py baseline`
2. Start real Healenium (requires Docker Desktop running):
   `docker compose -f .\Lab-5-Solutions\healenium\docker-compose.yaml up -d`
   Wait for containers to start; check with the same compose command followed by `ps`.
3. Seed the original locators through the proxy:
   `python .\Lab-5-Solutions\run_lab5.py seed`
   Confirm five passes before continuing. This stores the baseline DOM in Healenium.
4. Change the text-input ID and run without healing:
   `python .\Lab-5-Solutions\run_lab5.py drift`
5. Run the identical test suite on the changed page through Healenium:
   `python .\Lab-5-Solutions\run_lab5.py healing`
6. Open http://localhost:7878/healenium/report and capture the actual healing report.
   Save a screenshot under reports/healing/ and inspect the chosen element.
7. Export actual proxy logs:
   `docker compose -f .\Lab-5-Solutions\healenium\docker-compose.yaml logs --no-color hlm-proxy > .\Lab-5-Solutions\reports\healing\proxy-log.txt`

The runner starts/stops its own HTTP server on port 8010. Local Chrome uses
localhost; Docker Chrome uses host.docker.internal. Keep Docker running across
seed and healing. No fallback locator is implemented in the Page Object.
If Docker is unavailable, run baseline and drift, record the limitation honestly,
and leave healing marked Not Run. This leaves the Healenium requirement incomplete.

## Evidence and submission

Actual console output, JUnit XML and page screenshots are saved under reports/
for each phase. Take a terminal screenshot too if requested by your lecturer.
Fill in REPORT.md using actual results. Expected (unverified) outcomes: baseline
5 passes; seed 5 passes; drift UI01 fails and four others pass. A successful healing
run should pass all five and show the UI01 healing decision in the real report.
The report/dashboard must confirm the correct input was chosen; passing alone
does not prove a healing decision occurred.

Self-healing success rate = correctly healed affected cases / affected cases * 100.
If UI01 is the only affected case and correctly heals, the rate is 1/1 = 100%.
five-case pass rate from the healing success rate. 

Docker setup is adapted from the official Healenium compose example, retaining
Chrome only: https://github.com/healenium/healenium/blob/master/docker-compose.yaml
Selenium latest image tags reflect that upstream example; actual pulled versions

