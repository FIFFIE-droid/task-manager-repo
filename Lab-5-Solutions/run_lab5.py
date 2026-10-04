"""Run a real pytest phase and save its output; no simulated test results."""
import argparse
import functools
import json
import os
from pathlib import Path
import subprocess
import sys
import threading
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["baseline", "seed", "drift", "healing"])
    args = parser.parse_args()
    original = (ROOT / "site" / "demo_page_original.html").read_text(encoding="utf-8")
    assert original.count('id="myTextInput"') == 1
    changed = args.phase in {"drift", "healing"}
    html = original.replace('id="myTextInput"', 'id="myTextInputChanged"', 1) if changed else original
    (ROOT / "site" / "demo_page.html").write_text(html, encoding="utf-8")
    report_dir = ROOT / "reports" / args.phase
    report_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["LAB5_PHASE"] = args.phase
    env.pop("LAB5_BASE_URL", None)
    env.pop("LAB5_REMOTE_URL", None)
    if args.phase in {"seed", "healing"}:
        env["LAB5_REMOTE_URL"] = "http://localhost:8085"
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(ROOT / "site"))
    try:
        server = ThreadingHTTPServer(("0.0.0.0", 8010), handler)
    except OSError as exc:
        print(f"Cannot start the demo server on port 8010: {exc}")
        return 2
    threading.Thread(target=server.serve_forever, daemon=True).start()
    print(f"Phase: {args.phase}; locator changed: {changed}", flush=True)
    command = [sys.executable, "-m", "pytest", str(ROOT / "test_lab5.py"), "-v", "--color=no",
               f"--junitxml={report_dir / 'results.xml'}"]
    started = datetime.now(timezone.utc).isoformat()
    try:
        with (report_dir / "terminal.txt").open("w", encoding="utf-8") as log:
            process = subprocess.Popen(command, env=env, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
            for line in process.stdout:
                print(line, end="", flush=True)
                log.write(line)
            code = process.wait()
        (report_dir / "run.json").write_text(json.dumps({
            "phase": args.phase, "started_utc": started, "locator_changed": changed,
            "remote_url": env.get("LAB5_REMOTE_URL"), "pytest_exit_code": code,
        }, indent=2), encoding="utf-8")
        return code
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    raise SystemExit(main())
