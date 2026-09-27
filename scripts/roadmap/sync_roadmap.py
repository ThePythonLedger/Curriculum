#!/usr/bin/env python3
"""
Reads the GitHub event that triggered this workflow run (an issue or PR
change) and updates the matching line in ROADMAP.md to one of three
states:

    [ ] Lists — #34          not started
    [ ] 🚧 Lists — #34        in progress (assigned / open PR)
    [x] Lists — #34          done (merged / issue closed)

GitHub's task-list rendering only recognizes [ ] and [x] as real,
interactive checkboxes — anything else (like a bare [-]) is just
literal text with no checkbox widget. So the checkbox itself stays
strictly boolean (done / not done), and "in progress" is layered on
as a 🚧 badge in the visible text instead of a third bracket state.

This only touches roadmap lines that already reference an issue, e.g.:

    * [ ] Lists — #34

Lines with no "— #N" suffix are left alone — link an issue to a lesson
by adding that suffix, and the automation picks it up from then on.
"""

import json
import os
import re

ROADMAP_PATH = "ROADMAP.md"
WIP_BADGE = "🚧"

# Internal state codes (unchanged from before): " " = not started,
# "-" = in progress, "x" = done. Only how they're RENDERED changes.
STATE_RENDER = {
    " ": {"check": " ", "badge": ""},
    "-": {"check": " ", "badge": f"{WIP_BADGE} "},
    "x": {"check": "x", "badge": ""},
}

# Matches e.g. "    * [ ] 🚧 Lists — #34" and captures the checkbox,
# an optional WIP badge, and the issue number — everything else on
# the line is left untouched.
LINE_RE = re.compile(
    r"^(?P<prefix>\s*\*\s*\[)(?P<check>[ x])(?P<mid>\]\s*)"
    rf"(?P<badge>{WIP_BADGE}\s*)?"
    r"(?P<body>.*?—\s*#)(?P<issue>\d+)(?P<rest>.*)$"
)


def current_state(check: str, badge: str | None) -> str:
    if check == "x":
        return "x"
    return "-" if badge else " "


# Matches "Closes #12", "Fixes #34", "Resolves #7", etc. (repeatable, case-insensitive)
ISSUE_REF_RE = re.compile(
    r"(?:clos(?:e[sd]?)|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)", re.IGNORECASE
)


def marker_for_issue_event(event: dict) -> dict[int, str]:
    action = event["action"]
    issue_number = event["issue"]["number"]

    if action == "assigned":
        return {issue_number: "-"}
    if action == "unassigned":
        return {issue_number: " "}
    if action == "closed":
        return {issue_number: "x"}
    if action == "reopened":
        has_assignee = bool(event["issue"].get("assignees"))
        return {issue_number: "-" if has_assignee else " "}
    return {}


def marker_for_pr_event(event: dict) -> dict[int, str]:
    action = event["action"]
    pr = event["pull_request"]
    body = pr.get("body") or ""
    issue_numbers = {int(n) for n in ISSUE_REF_RE.findall(body)}
    if not issue_numbers:
        return {}

    if action in ("opened", "ready_for_review"):
        marker = "-"
    elif action == "closed":
        marker = "x" if pr.get("merged") else "-"
    else:
        return {}

    return {n: marker for n in issue_numbers}


def load_event() -> dict:
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
        return json.load(f)


def compute_updates() -> dict[int, str]:
    event_name = os.environ["GITHUB_EVENT_NAME"]
    event = load_event()

    if event_name == "issues":
        return marker_for_issue_event(event)
    if event_name == "pull_request" or event_name == "pull_request_target":
        return marker_for_pr_event(event)
    return {}


def apply_updates(updates: dict[int, str]) -> bool:
    with open(ROADMAP_PATH, encoding="utf-8") as f:
        lines = f.readlines()

    changed = False
    for i, line in enumerate(lines):
        m = LINE_RE.match(line.rstrip("\n"))
        if not m:
            continue

        issue = int(m.group("issue"))
        if issue not in updates:
            continue

        new_state = updates[issue]
        old_state = current_state(m.group("check"), m.group("badge"))
        if old_state == new_state:
            continue

        render = STATE_RENDER[new_state]
        lines[i] = (
            m.group("prefix")
            + render["check"]
            + m.group("mid")
            + render["badge"]
            + m.group("body")
            + m.group("issue")
            + m.group("rest")
            + "\n"
        )
        changed = True
        print(f"#{issue}: [{old_state}] -> [{new_state}]")

    if changed:
        with open(ROADMAP_PATH, "w", encoding="utf-8") as f:
            f.writelines(lines)

    return changed


def main() -> None:
    updates = compute_updates()
    if not updates:
        print("No linked roadmap issue affected by this event — nothing to do.")
        changed = False
    else:
        changed = apply_updates(updates)
        if not changed:
            print("Matching roadmap line(s) already up to date.")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
