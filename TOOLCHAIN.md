# Project Toolchain

Last verified: 2026-06-14 Asia/Shanghai

## Required

| Tool | Required version | Project standard | Verified executable |
| --- | --- | --- | --- |
| Python | `>=3.10` | `3.13.11` | `/opt/homebrew/bin/python3.13` |
| pip | Compatible with project Python | `25.3` | `/opt/homebrew/bin/python3.13 -m pip` |
| Git | `>=2.30` | `2.52.0` | `git` |

The macOS system `python3` currently reports `3.9.6` and is not compatible with
`sync/deploy.py`, which uses Python 3.10+ type-union syntax. Do not use the
system `python3` for deployment or preview generation.

## Python Dependencies

Install the dependency ranges declared in `sync/requirements.txt`:

| Package | Minimum version |
| --- | --- |
| `requests` | `2.31.0` |
| `markdownify` | `0.14.1` |
| `python-dotenv` | `1.0.0` |
| `beautifulsoup4` | `4.12.0` |
| `deep-translator` | `1.11.4` |

The preview generation verified on 2026-06-14 resolved:

| Package | Verified version |
| --- | --- |
| `requests` | `2.34.2` |
| `markdownify` | `1.2.2` |
| `python-dotenv` | `1.2.2` |
| `beautifulsoup4` | `4.15.0` |
| `deep-translator` | `1.11.4` |

Recommended setup:

```bash
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install -r sync/requirements.txt
.venv/bin/python sync/deploy.py preview
```

`.venv/` is ignored by Git.

## Local Preview Server

Serve generated previews on `http://127.0.0.1:8765/`:

```bash
launchctl remove com.dynamicycle.preview >/dev/null 2>&1 || true
launchctl submit -l com.dynamicycle.preview -- \
  /opt/homebrew/bin/python3.13 -m http.server 8765 \
  --bind 127.0.0.1 \
  --directory /Users/lqhy/Documents/Projects/Dynamicycle/build/deploy-previews
```

Check the server:

```bash
curl -I http://127.0.0.1:8765/category-campaigns.html
launchctl print gui/$(id -u)/com.dynamicycle.preview
```

Stop the server:

```bash
launchctl remove com.dynamicycle.preview
```

Do not stop the preview server after browser verification when the user is
actively reviewing pages.

## Optional

| Tool | Current version | Use |
| --- | --- | --- |
| Node.js | `25.8.1` | Local automation and browser tooling; not required by `sync/deploy.py` |

## Upgrade Protocol

Codex must not upgrade system-level software without user action. When a tool
upgrade is needed, Codex must report:

1. Tool and current version.
2. Required or recommended target version.
3. Technical reason for the upgrade.
4. Verification command.

The user performs the upgrade. Codex then verifies the installed version and
updates this document if the project standard changed.
