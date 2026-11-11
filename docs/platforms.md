# Platforms

All tutor rules live in `AGENTS.md`, the cross-tool instruction file
standard. Platforms that use their own filename get a one-line pointer
(`CLAUDE.md`, `GEMINI.md`) that imports it, so there is only one set of
rules to maintain.

## What the agent needs
| Capability | Used for | Without it |
|---|---|---|
| Read/write files in the repo | Progress, lessons, misconceptions | Use manual mode (below) |
| Shell + git | Silent commit/push to `main` | Learner commits; agent lists changed files |
| Web search / fetch | Sourcing materials, transcripts | Learner provides materials or fetches suggested links |
| Code execution | `checks/` scripts | Learner runs the scripts |

## Coding agents (repo access)
| Platform | Reads | Notes |
|---|---|---|
| OpenAI Codex (CLI / IDE) | `AGENTS.md` | Works as is. Codex cloud tasks typically hand back a diff or PR; for lessons, prefer the CLI or IDE in a local clone so commits go straight to `main`. |
| Claude Code | `CLAUDE.md` → `@AGENTS.md` | Prompt suggestions are disabled in `.claude/settings.json`. Cloud sessions may start on an assigned branch; the Git workflow tells the agent to use `main` for learning work. |
| Grok Build (xAI CLI) | `AGENTS.md` | Works as is. |
| Cursor | `AGENTS.md` | Use agent mode. Turn off inline suggestions in any chat where you type answers. |
| GitHub Copilot | `AGENTS.md` | Use agent mode in the IDE. The cloud coding agent works through PRs, which doesn't fit lesson work. |
| Gemini CLI | `GEMINI.md` → `@AGENTS.md` | Works as is. |
| Anything else | — | Start with: "Read AGENTS.md and follow it exactly." |

Support for these files changes often; if a platform ignores them, use the
"anything else" opener.

## Chat assistants without repo access (manual mode)
ChatGPT, Grok, Claude, Gemini and similar chat apps can still run the
course; the learner carries the files between sessions. Project or
workspace features that keep uploaded files help.

1. **Start of session:** upload or paste `AGENTS.md`, `learner.md`,
   `syllabus.md`, `progress.md`, `misconceptions.md`, and the current
   lesson file (plus `docs/setup.md` and `docs/materials.md` for the first
   session). Say "resume" (or "set up").
2. **During the session:** the tutor teaches as normal, and doesn't mention
   files.
3. **End of session:** say "end session". The agent outputs the full,
   updated contents of every changed file. Save them to the repo and commit.

## Answer leakage
Some platforms suggest replies or autocomplete what you type, which can give
away the answer to a pending question. Turn those off where possible
(Claude Code: done in `.claude/settings.json`; elsewhere check the
platform's settings).
