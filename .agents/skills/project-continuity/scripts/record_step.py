#!/usr/bin/env python3
"""Update the latest project state and append an execution-history entry."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


REPO_ROOT = Path(__file__).resolve().parents[4]
STATE_PATH = REPO_ROOT / "PROJECT_STATE.md"
HISTORY_PATH = REPO_ROOT / "PROJECT_HISTORY.md"


def git_value(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"


def bullet_lines(values: list[str], empty: str) -> str:
    if not values:
        return f"- {empty}"
    return "\n".join(f"- {value}" for value in values)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--status",
        required=True,
        choices=("in_progress", "completed", "blocked"),
    )
    parser.add_argument("--task", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--verification", action="append", default=[])
    parser.add_argument("--changed", action="append", default=[])
    parser.add_argument("--next", required=True)
    parser.add_argument("--note", action="append", default=[])
    args = parser.parse_args()

    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    timestamp = now.isoformat(timespec="seconds")
    branch = git_value("branch", "--show-current")
    commit = git_value("rev-parse", "--short", "HEAD")

    state = f"""# Project State

Last updated: {timestamp}

## Current Execution

- Status: `{args.status}`
- Task: {args.task}
- Branch: `{branch}`
- Commit: `{commit}`

## Latest Result

{args.result}

## Verification

{bullet_lines(args.verification, "Not recorded.")}

## Changed Files

{bullet_lines([f"`{path}`" for path in args.changed], "No tracked file changes.")}

## Next Action

{args.next}

## Notes

{bullet_lines(args.note, "None.")}

## Resume

```bash
git fetch origin
git checkout {branch}
git pull --ff-only
cat PROJECT_STATE.md
```
"""
    STATE_PATH.write_text(state, encoding="utf-8")

    if not HISTORY_PATH.exists():
        HISTORY_PATH.write_text(
            "# Project History\n\n"
            "Append-only execution history. Do not store credentials or rewrite "
            "previous entries.\n",
            encoding="utf-8",
        )

    entry = f"""

## {timestamp} | {args.status}

- Task: {args.task}
- Result: {args.result}
- Branch: `{branch}`
- Commit at record time: `{commit}`
- Verification: {"; ".join(args.verification) if args.verification else "Not recorded."}
- Changed: {", ".join(f"`{path}`" for path in args.changed) if args.changed else "None."}
- Next: {args.next}
- Notes: {"; ".join(args.note) if args.note else "None."}
"""
    with HISTORY_PATH.open("a", encoding="utf-8") as history:
        history.write(entry)

    print(f"Updated {STATE_PATH.relative_to(REPO_ROOT)}")
    print(f"Appended {HISTORY_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
