# agent_tutor — mastery tutoring with an off-the-shelf AI agent

A repo template for learning any subject with an AI coding agent (Claude
Code or similar) as a tutor. The repo is the tutor's memory: a syllabus,
per-lesson notes, mastery levels, and a log of your misconceptions,
updated and committed every session.

## The method
- **Instruction + Socratic questioning.** Each lesson: a short diagnostic
  to place you → direct teaching (explanation + worked example, tied to
  your sources) → practice, one question at a time. When you're wrong the
  tutor asks a narrower question rather than giving the answer, and
  explains directly only after two failed attempts.
- **Mastery before progression.** Levels 0–5 per lesson. A level rises
  only after 2+ correct checks, at least one from unprompted recall. You
  don't move on until the lesson is at 3/5; a unit is done when every
  lesson is at 4/5.
- **Spaced review.** Every session opens with unannounced questions from
  earlier lessons; misses lower the level.
- **Misconceptions are tracked** and re-tested until fixed.

## Inspiration
Inspired by Jane Street's **socratic-tutor** skill in
[janestreet/agent_skills](https://github.com/janestreet/agent_skills)
(diagnostic placement, a 0–5 skill map, one question at a time, spaced
review). This template turns that approach into a repo that persists
across sessions: a syllabus, progress and misconceptions files, and
lesson notes committed every session. It adds direct instruction alongside the
questioning, mastery gating between lessons, and a setup process
for providing or sourcing materials.

## Getting started
1. Create a repo from this template ("Use this template" on GitHub, or copy it).
2. Optional: drop your materials (textbook PDFs, notes, slides, problem
   sets, lecture or playlist links) into `resources/`. Or bring none.
3. Open a session with your agent in the repo and say "set up" — or just
   say what you want to learn. The agent reads `CLAUDE.md`, sees the course
   isn't set up, and follows `docs/setup.md`: it interviews you, catalogues
   your materials and/or searches for good ones (open textbooks, lecture
   videos, problem sets, interactive tools) for your approval, indexes
   them to lessons down to page ranges and video timestamps, drafts a
   syllabus for your approval, and places you.

## Materials
Anything works: what you provide, what the agent finds, a mix, or nothing.
During lessons the tutor points you to the exact reading or short video
clip for each concept as it teaches it, and draws practice problems from
problem sources (keeping solutions hidden until you've answered). You can
add or ask for materials at any time. Details: `docs/materials.md`.
4. After that, each session: say "resume". The stop point is at the top of
   `progress.md`.

Using a different agent? `AGENTS.md` points it to the same instructions.

## Layout
| Path | Contents |
|---|---|
| `CLAUDE.md` | Tutor rules (loaded every session) |
| `AGENTS.md` | Pointer to `CLAUDE.md` for other agents |
| `docs/setup.md` | One-time setup protocol |
| `docs/materials.md` | Providing, sourcing, indexing, and using materials |
| `learner.md` | Your background, goals, preferences |
| `syllabus.md` | Units and one-concept lessons |
| `progress.md` | Levels per lesson, unit rollups, stop point, session log |
| `misconceptions.md` | Error log with open/probing/fixed status |
| `lessons/NN-topic.md` | Per-lesson notes, your answers, feedback (`_template.md`) |
| `checks/` | Scripts verifying answers (simulations, code) |
| `resources/` | Your materials + index mapping them to lessons |

## Notes
- During learning (setup, lessons, progress updates, materials) the agent
  works only on `main` and commits and pushes silently: no branches, no
  PRs, no permission prompts, and no git talk in lessons. When you change
  the tutor's own mechanics (`CLAUDE.md`, `docs/`, formats), it uses a
  normal development workflow instead.
- Keep the repo private if your notes are personal or your materials are
  copyrighted.
- Prompt suggestions are disabled (`.claude/settings.json`) so they can't
  leak answers to pending questions.
