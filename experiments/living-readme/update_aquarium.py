#!/usr/bin/env python3
"""Render a deliberately limited issue-driven aquarium state into a README SVG.

No third-party packages, network calls, templating of user text, or shell execution.
Run via GitHub Actions on trusted default-branch code only.
"""
import json
import os
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
STATE = HERE / "aquarium-state.json"
SVG = HERE / "assets" / "readme-terrarium.svg"
OPEN = '<g id="habitat-state">'
CLOSE = '</g><!-- /habitat-state -->'
OPTIONS = {
    "Feed the betta": "feed",
    "Turn on moonlight": "moonlight",
    "Turn on daylight": "daylight",
}


def decode_choice(body):
    # GitHub issue form template: ### Action\n\nFeed the betta
    chunks = (body or "").split("### Action", 1)
    if len(chunks) != 2:
        return None
    raw = chunks[1].strip().splitlines()
    selection = next((line.strip() for line in raw if line.strip()), "")
    return OPTIONS.get(selection)


def update(event, state):
    issue = event.get("issue") or {}
    title = issue.get("title") or ""
    if not title.startswith("[Aquarium]") or event.get("action") != "opened":
        return False
    number = issue.get("number")
    if not isinstance(number, int) or number <= int(state.get("last_issue", 0)):
        return False
    choice = decode_choice(issue.get("body"))
    if choice is None:
        return False
    if choice == "feed":
        state["feed_count"] = min(999999, max(0, int(state.get("feed_count", 0))) + 1)
        state["last_action"] = "The betta enjoyed a snack!"
    else:
        state["lighting"] = choice
        state["last_action"] = "The lighting changed."
    state["last_issue"] = number
    return True


def render(svg, state):
    color = "#bceeff" if state["lighting"] == "moonlight" else "#fff0b8"
    light = "MOONLIGHT" if state["lighting"] == "moonlight" else "DAYLIGHT"
    snippet = (
        OPEN +
        '<rect x="733" y="96" width="191" height="66" rx="10" fill="#081b38" fill-opacity=".72" stroke="' + color + '" stroke-opacity=".6"/>'
        '<text x="744" y="119" fill="' + color + '" font-family="monospace" font-size="13">LIGHT: ' + light + '</text>'
        '<text x="744" y="144" fill="#ffffff" font-family="monospace" font-size="13">SNACKS: ' + str(state["feed_count"]) + '</text>'
        + CLOSE
    )
    start = svg.find(OPEN)
    if start >= 0:
        end = svg.find(CLOSE, start)
        if end < 0:
            raise ValueError("Unterminated state region")
        svg = svg[:start].rstrip() + svg[end + len(CLOSE):]
    svg = svg.replace("</svg>", "\n" + snippet + "\n</svg>")
    ET.fromstring(svg)  # fail closed if rendering breaks XML
    return svg


def main():
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf8") as f:
        event = json.load(f)
    state = json.loads(STATE.read_text(encoding="utf8"))
    if not update(event, state):
        print("Ignored invalid, unrelated or previously processed issue.")
        return
    rendered = render(SVG.read_text(encoding="utf8"), state)
    STATE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf8")
    SVG.write_text(rendered, encoding="utf8")
    print("Updated aquarium state from issue", state["last_issue"])


if __name__ == "__main__":
    main()
