"""Run each requested suite separately and derive a comparison from actual reports."""
import argparse
import ast
import csv
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SELECTED = {"remove_task", "save_tasks", "load_tasks"}


def test_count_and_checks(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    functions = [node for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                 and node.name.startswith("test_")]
    asserts = sum(isinstance(node, ast.Assert) for fn in functions for node in ast.walk(fn))
    raises = sum(isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                 and isinstance(node.func.value, ast.Name) and node.func.value.id == "pytest"
                 and node.func.attr == "raises" for fn in functions for node in ast.walk(fn))
    return len(functions), asserts, raises


def summarise(mode, report_dir, paths, exit_code):
    data = json.loads((report_dir / "coverage.json").read_text(encoding="utf-8"))
    matching = [details for name, details in data["files"].items()
                if name.replace("\\", "/").endswith("app/tasks.py")]
    if len(matching) != 1:
        raise RuntimeError("Could not uniquely identify app/tasks.py in coverage JSON")
    details = matching[0]
    covered = set(details["executed_lines"])
    missing = set(details["missing_lines"])
    tree = ast.parse((REPO / "app" / "tasks.py").read_text(encoding="utf-8"))
    body_lines = set()
    for fn in tree.body:
        if isinstance(fn, ast.FunctionDef) and fn.name in SELECTED:
            # Exclude the function definition line, which executes on import.
            body_lines.update(range(fn.lineno + 1, fn.end_lineno + 1))
    target_executable = (covered | missing) & body_lines
    target_covered = covered & target_executable
    module_percent = 100 * len(covered) / len(covered | missing) if covered | missing else 0
    target_percent = 100 * len(target_covered) / len(target_executable) if target_executable else 0
    counts = [test_count_and_checks(path) for path in paths]
    summary = {
        "run": mode, "module_statement_coverage_percent": round(module_percent, 2),
        "selected_function_body_coverage_percent": round(target_percent, 2),
        "test_functions": sum(c[0] for c in counts),
        "assert_statements": sum(c[1] for c in counts),
        "pytest_raises_checks": sum(c[2] for c in counts),
        "pytest_exit_code": exit_code,
    }
    (report_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    rows = []
    for name in ["ai", "manual", "combined"]:
        path = ROOT / "reports" / name / "summary.json"
        if path.exists():
            rows.append(json.loads(path.read_text(encoding="utf-8")))
    csv_path = ROOT / "reports" / "comparison.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(summary))
        writer.writeheader()
        writer.writerows(rows)
    print("Actual run summary:", json.dumps(summary, indent=2))
    print("Comparison CSV:", csv_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["ai", "manual", "combined"])
    args = parser.parse_args()
    ai = ROOT / "test_ai_generated.py"
    manual = ROOT / "test_manual.py"
    if args.mode in {"manual", "combined"} and test_count_and_checks(manual)[0] == 0:
        print("Write your independent tests in test_manual.py first. It currently contains no tests.")
        return 2
    paths = [ai] if args.mode == "ai" else [manual] if args.mode == "manual" else [ai, manual]
    report_dir = ROOT / "reports" / args.mode
    report_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["COVERAGE_FILE"] = str(report_dir / ".coverage")
    command = [sys.executable, "-m", "pytest", *map(str, paths), "-v", "--color=no",
               "--cov=app.tasks", "--cov-report=term-missing",
               f"--cov-report=html:{report_dir / 'html'}",
               f"--cov-report=json:{report_dir / 'coverage.json'}",
               f"--junitxml={report_dir / 'results.xml'}"]
    with (report_dir / "terminal.txt").open("w", encoding="utf-8") as log:
        process = subprocess.Popen(command, cwd=REPO, env=env, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")
        for line in process.stdout:
            print(line, end="", flush=True)
            log.write(line)
        exit_code = process.wait()
    if (report_dir / "coverage.json").exists() and exit_code in {0, 1}:
        summarise(args.mode, report_dir, paths, exit_code)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
