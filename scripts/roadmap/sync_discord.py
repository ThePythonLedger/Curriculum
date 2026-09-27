#!/usr/bin/env python3
"""
Renders ROADMAP.md into Discord embeds and PATCHes a set of existing
webhook messages, so a Discord channel mirrors the roadmap's current
state. Uses only the standard library — no extra dependency to install
in the workflow.

Requires:
  DISCORD_WEBHOOK_URL   The webhook's execute URL
                        (https://discord.com/api/webhooks/<id>/<token>)
  DISCORD_MESSAGE_IDS   JSON array of message IDs to update, one per
                        "page" of phases (see PHASES_PER_MESSAGE below)

One-time setup: send an initial message through the webhook manually
(any content) for each page you'll need, note the returned message
IDs, and store them as DISCORD_MESSAGE_IDS. This script only edits
those messages — it never creates new ones — so the roadmap always
lives at the same spot in the channel.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

ROADMAP_PATH = "ROADMAP.md"
PHASES_PER_MESSAGE = (
    9  # 18 phases / 9 = 2 messages; keeps each embed well under Discord's limits
)

STATE_EMOJI = {" ": "⬜", "-": "🚧", "x": "✅"}
WIP_BADGE = "🚧"

PHASE_RE = re.compile(r"^\d+\.\s+(.+)$")
ITEM_RE = re.compile(
    rf"^\s*\*\s*\[(?P<check>[ x])\]\s*(?P<badge>{WIP_BADGE}\s*)?(?P<text>.+?)\s*$"
)


def item_state(check: str, badge: str | None) -> str:
    if check == "x":
        return "x"
    return "-" if badge else " "


Phase = tuple[str, list[tuple[str, str]]]


def parse_roadmap(text: str) -> list[Phase]:
    phases: list[Phase] = []
    current_items: list[tuple[str, str]] = []
    current_title: str | None = None

    for raw_line in text.splitlines():
        phase_match = PHASE_RE.match(raw_line)
        if phase_match:
            if current_title is not None:
                phases.append((current_title, current_items))
            current_title = phase_match.group(1)
            current_items = []
            continue

        item_match = ITEM_RE.match(raw_line)
        if item_match and current_title is not None:
            state = item_state(item_match.group("check"), item_match.group("badge"))
            current_items.append((state, item_match.group("text")))

    if current_title is not None:
        phases.append((current_title, current_items))

    return phases


def build_embed(phases: list[Phase]) -> dict:
    fields = []
    for title, items in phases:
        lines = [f"{STATE_EMOJI[state]} {text}" for state, text in items]
        value = "\n".join(lines) or "—"
        fields.append({"name": title[:256], "value": value[:1024], "inline": False})

    return {
        "title": "📍 Curriculum Roadmap",
        "color": 0x3776AB,
        "fields": fields[:25],
    }


def patch_message(webhook_url: str, message_id: str, embed: dict) -> None:
    url = f"{webhook_url}/messages/{message_id}"
    payload = json.dumps({"content": "", "embeds": [embed]}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        method="PATCH",
        headers={
            "Content-Type": "application/json",
            "User-Agent": "ThePythonLedger-RoadmapSync (https://github.com/ThePythonLedger/Curriculum, 1.0)",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            if resp.status not in (200, 204):
                print(
                    f"Unexpected status {resp.status} updating message {message_id}",
                    file=sys.stderr,
                )
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} updating message {message_id}: {body}", file=sys.stderr)
        raise


def main() -> None:
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    message_ids = json.loads(os.environ["DISCORD_MESSAGE_IDS"])

    with open(ROADMAP_PATH, encoding="utf-8") as f:
        phases = parse_roadmap(f.read())

    chunks = [
        phases[i : i + PHASES_PER_MESSAGE]
        for i in range(0, len(phases), PHASES_PER_MESSAGE)
    ]

    if len(chunks) != len(message_ids):
        print(
            f"Expected {len(chunks)} message(s) for {len(phases)} phases, "
            f"but DISCORD_MESSAGE_IDS has {len(message_ids)}. Update the "
            f"variable or PHASES_PER_MESSAGE so they match.",
            file=sys.stderr,
        )
        sys.exit(1)

    for message_id, chunk in zip(message_ids, chunks):
        patch_message(webhook_url, message_id, build_embed(chunk))
        print(f"Updated message {message_id} ({len(chunk)} phases)")


if __name__ == "__main__":
    main()
