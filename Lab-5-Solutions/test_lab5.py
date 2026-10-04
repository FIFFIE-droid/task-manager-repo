"""Five UI cases; their inputs and expected results come from JSON."""
import json
from pathlib import Path
import pytest
from demo_page import DemoPage

CASES = json.loads(Path(__file__).with_name("test_data.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", CASES, ids=[case["id"] for case in CASES])
def test_demo_page(browser, case):
    page = DemoPage(browser)
    if case["action"] == "text":
        actual = page.enter_text(case["input"])
    elif case["action"] == "notes":
        actual = page.enter_notes(case["input"])
    elif case["action"] == "button":
        actual = page.change_button_colour()
    elif case["action"] == "select":
        actual = page.select_percentage(case["input"])
    elif case["action"] == "checkbox":
        actual = page.set_checkbox(case["input"])
    else:
        raise ValueError(f"Unknown test action: {case['action']}")
    assert actual == case["expected"]
