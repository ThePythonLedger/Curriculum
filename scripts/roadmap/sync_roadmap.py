#!/usr/bin/env python3
"""
Reads the GitHub event that triggered this workflow run (an issue or PR
change) and updates the matching line in ROADMAP.md to one of three
states:

<<<<<<< HEAD
    [ ] Lists — #34                       not started
    [ ] 🚧 Lists — #34 👤 alice, bob       in progress (assigned / open PR)
    [x] Lists — #34                       done (merged / issue closed)
=======
    [ ] Lists — #34          not started
    [ ] 🚧 Lists — #34        in progress (assigned / open PR)
    [x] Lists — #34          done (merged / issue closed)
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)

GitHub's task-list rendering only recognizes [ ] and [x] as real,
interactive checkboxes — anything else (like a bare [-]) is just
literal text with no checkbox widget. So the checkbox itself stays
strictly boolean (done / not done), and "in progress" is layered on
as a 🚧 badge in the visible text instead of a third bracket state.

<<<<<<< HEAD
While a lesson is in progress, the issue's assignees are listed at the
end of the line after a 👤 marker (plain usernames, no @ mentions).
The names are dropped again once the lesson is done or unassigned.

=======
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
This only touches roadmap lines that already reference an issue, e.g.:

    * [ ] Lists — #34

Lines with no "— #N" suffix are left alone — link an issue to a lesson
by adding that suffix, and the automation picks it up from then on.
"""
<<<<<<< HEAD
import json
import os
import re
from typing import NamedTuple

ROADMAP_PATH = "ROADMAP.md"
WIP_BADGE = "🚧"
ASSIGNEE_MARKER = "👤"

# Internal state codes: " " = not started, "-" = in progress, "x" = done.
# Only how they're RENDERED matters to GitHub's markdown.
=======

import json
import os
import re

ROADMAP_PATH = "ROADMAP.md"
WIP_BADGE = "🚧"

# Internal state codes (unchanged from before): " " = not started,
# "-" = in progress, "x" = done. Only how they're RENDERED changes.
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
STATE_RENDER = {
    " ": {"check": " ", "badge": ""},
    "-": {"check": " ", "badge": f"{WIP_BADGE} "},
    "x": {"check": "x", "badge": ""},
}

<<<<<<< HEAD
# Matches e.g. "    * [ ] 🚧 Lists — #34 👤 alice" and captures the checkbox,
# an optional WIP badge, and the issue number. `rest` is everything after
# the issue number (including any assignee suffix, handled separately).
=======
# Matches e.g. "    * [ ] 🚧 Lists — #34" and captures the checkbox,
# an optional WIP badge, and the issue number — everything else on
# the line is left untouched.
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
LINE_RE = re.compile(
    r"^(?P<prefix>\s*\*\s*\[)(?P<check>[ x])(?P<mid>\]\s*)"
    rf"(?P<badge>{WIP_BADGE}\s*)?"
    r"(?P<body>.*?—\s*#)(?P<issue>\d+)(?P<rest>.*)$"
)

<<<<<<< HEAD
# The assignee suffix always sits at the very end of the line.
ASSIGNEE_SUFFIX_RE = re.compile(rf"\s+{ASSIGNEE_MARKER}\s+.*$")

# Matches "Closes #12", "Fixes #34", "Resolves #7", etc. (repeatable, case-insensitive)
ISSUE_REF_RE = re.compile(r"(?:clos(?:e[sd]?)|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)", re.IGNORECASE)

HANDLED_ISSUE_ACTIONS = {"assigned", "unassigned", "closed", "reopened"}


class Update(NamedTuple):
    state: str
    # None = keep whatever names are already on the line. PR events use this,
    # since a PR payload doesn't carry the linked issue's assignee list.
    assignees: list[str] | None = None

=======
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)

def current_state(check: str, badge: str | None) -> str:
    if check == "x":
        return "x"
    return "-" if badge else " "


<<<<<<< HEAD
def state_for_issue(issue: dict) -> str:
    if issue.get("state") == "closed":
        return "x"
    return "-" if issue.get("assignees") else " "


def assignee_logins(issue: dict) -> list[str]:
    return [a["login"] for a in issue.get("assignees") or []]


def update_from_issue(issue: dict) -> Update:
    """Works for both webhook payloads and REST API issue objects."""
    return Update(state_for_issue(issue), assignee_logins(issue))


def updates_for_issue_event(event: dict) -> dict[int, Update]:
    if event["action"] not in HANDLED_ISSUE_ACTIONS:
        return {}
    issue = event["issue"]
    # The issue object reflects the state AFTER the change, so unassigning
    # one of two people correctly leaves the line in progress.
    return {issue["number"]: update_from_issue(issue)}


def updates_for_pr_event(event: dict) -> dict[int, Update]:
=======
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
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
    action = event["action"]
    pr = event["pull_request"]
    body = pr.get("body") or ""
    issue_numbers = {int(n) for n in ISSUE_REF_RE.findall(body)}
    if not issue_numbers:
        return {}

    if action in ("opened", "ready_for_review"):
<<<<<<< HEAD
        update = Update("-")
    elif action == "closed":
        update = Update("x") if pr.get("merged") else Update("-")
    else:
        return {}

    return {n: update for n in issue_numbers}
=======
        marker = "-"
    elif action == "closed":
        marker = "x" if pr.get("merged") else "-"
    else:
        return {}

    return {n: marker for n in issue_numbers}
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)


def load_event() -> dict:
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
        return json.load(f)


<<<<<<< HEAD
def compute_updates() -> dict[int, Update]:
=======
def compute_updates() -> dict[int, str]:
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
    event_name = os.environ["GITHUB_EVENT_NAME"]
    event = load_event()

    if event_name == "issues":
<<<<<<< HEAD
        return updates_for_issue_event(event)
    if event_name in ("pull_request", "pull_request_target"):
        return updates_for_pr_event(event)
    return {}


def render_suffix(update: Update, existing_suffix: str) -> str:
    if update.state != "-":
        return ""  # names are only shown while a lesson is in progress
    if update.assignees is None:
        return existing_suffix
    if not update.assignees:
        return ""
    return f" {ASSIGNEE_MARKER} {', '.join(update.assignees)}"


def apply_updates(updates: dict[int, Update]) -> bool:
=======
        return marker_for_issue_event(event)
    if event_name == "pull_request" or event_name == "pull_request_target":
        return marker_for_pr_event(event)
    return {}


def apply_updates(updates: dict[int, str]) -> bool:
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
    with open(ROADMAP_PATH, encoding="utf-8") as f:
        lines = f.readlines()

    changed = False
    for i, line in enumerate(lines):
<<<<<<< HEAD
        stripped = line.rstrip("\r\n")
        eol = line[len(stripped):]

        m = LINE_RE.match(stripped)
=======
        m = LINE_RE.match(line.rstrip("\n"))
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)
        if not m:
            continue

        issue = int(m.group("issue"))
        if issue not in updates:
            continue

<<<<<<< HEAD
        update = updates[issue]
        old_state = current_state(m.group("check"), m.group("badge"))
        render = STATE_RENDER[update.state]

        rest = m.group("rest")
        existing = ASSIGNEE_SUFFIX_RE.search(rest)
        rest_base = ASSIGNEE_SUFFIX_RE.sub("", rest)
        suffix = render_suffix(update, existing.group(0) if existing else "")
        if suffix:
            rest_base = rest_base.rstrip()  # no double space before the 👤

        new_line = (
            m.group("prefix") + render["check"] + m.group("mid") + render["badge"]
            + m.group("body") + m.group("issue") + rest_base + suffix + eol
        )
        if new_line == line:
            continue

        lines[i] = new_line
        changed = True
        print(f"#{issue}: [{old_state}] -> [{update.state}]{suffix}")
=======
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
>>>>>>> 78c3371 (Added automated scripts for pushing ROADMAP updates automaticly on Issue assigment. Changed ROADMAP.md to fit new workflow.)

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
