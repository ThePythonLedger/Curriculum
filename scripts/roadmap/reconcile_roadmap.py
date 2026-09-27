#!/usr/bin/env python3
"""
Scans every issue already linked in ROADMAP.md ("— #N") and sets its
checkbox to match that issue's CURRENT state on GitHub — closed,
assigned, or neither.

Use this:
  - once, right after linking a batch of issues, to catch anything that
    changed *before* the link existed — sync_roadmap.py only reacts to
    events on lines that already have "— #N" on them, so a PR merged
    before you added the link is invisible to it
  - on a schedule, as a safety net in case a future event is ever missed
    (a failed workflow run, a webhook delivery hiccup, etc.)

Unlike sync_roadmap.py, this doesn't look at PR state directly — an
issue's own state (closed / has an assignee) is used as the signal.
That covers the common paths (assigned, merged-and-closed) even for
history that predates the automation.
"""

import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(__file__))
from sync_roadmap import LINE_RE, ROADMAP_PATH, apply_updates  # noqa: E402


def find_linked_issues() -> set[int]:
    with open(ROADMAP_PATH, encoding="utf-8") as f:
        lines = f.readlines()

    issues = set()
    for line in lines:
        m = LINE_RE.match(line.rstrip("\n"))
        if m:
            issues.add(int(m.group("issue")))
    return issues


def fetch_issue(repo: str, token: str, number: int) -> dict:
    url = f"https://api.github.com/repos/{repo}/issues/{number}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def target_state(issue: dict) -> str:
    if issue.get("state") == "closed":
        return "x"
    if issue.get("assignees"):
        return "-"
    return " "


def main() -> None:
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]

    issue_numbers = find_linked_issues()
    if not issue_numbers:
        print("No linked issues found in ROADMAP.md.")
        return

    updates: dict[int, str] = {}
    for number in sorted(issue_numbers):
        try:
            issue = fetch_issue(repo, token, number)
        except urllib.error.HTTPError as e:
            print(
                f"#{number}: could not fetch issue ({e.code}) — skipping",
                file=sys.stderr,
            )
            continue
        updates[number] = target_state(issue)

    changed = apply_updates(updates)
    if not changed:
        print("Roadmap already matched issue states.")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
