# Setup protocol (run once, by the agent)

Goal: turn an empty template into a working course: a learner profile, a
syllabus of one-concept lessons, an indexed resource library, and seeded
levels. Ask the learner questions one at a time; don't front-load a form.

## 1. Intake interview → `learner.md`
Ask, one at a time:
1. What do you want to learn, and what does "done" look like? (an exam, a
   course, a job skill, a book finished, a project built)
2. What's your relevant background? What adjacent things do you already know?
3. Do you have materials (textbook, course, videos, notes, problem sets)?
   Add them to `resources/` or give links. Want me to find materials,
   fill gaps in yours, or teach without any?
4. How much time per session / per week? Any deadline?
5. How strict should I be, and anything about how you like to be taught?

Fill in `learner.md`. Don't assume prior exposure to the subject itself
unless they say so.

## 2. Gather materials → `resources/`
Follow `docs/materials.md`. In short:
- **Learner-provided.** Catalogue everything in `resources/` and any links
  given, in whatever form (files, links, playlists, notes).
- **Agent-sourced.** Fill each missing role (primary text, videos, problems
  with solutions, reference sheet, interactive tools) by searching for
  free, reputable sources. Present a short shortlist and get approval of
  the sources before downloading or adding them.
- **No materials wanted** is also valid: the tutor teaches from first
  principles and sources problems as needed.

Mark every item that contains solutions.

## 3. Design the syllabus → `syllabus.md`
- Follow the primary source's structure where it is sound.
- **One core concept per lesson.** If a lesson needs "and", consider
  splitting it. Typical size: teachable in 20–40 minutes with practice.
- Group lessons into units of ~4–8. Number lessons globally (`01`, `02`, …)
  so they match `lessons/NN-topic.md`.
- Order by prerequisite; note non-obvious prerequisites inline.
- Show the draft to the learner and revise before continuing.
- When approved, replace `STATUS: NOT SET UP` with `STATUS: ACTIVE`.

## 4. Map materials to lessons → `resources/README.md`
Index per `docs/materials.md` §4: for each lesson, readings
(section/pages), video clips (start/end from transcripts or chapters,
never guessed), and problems. Lessons with no coverage: say so, and offer
to source more for those.

## 5. Placement → `progress.md`
- Build `progress.md` with every lesson at `0`.
- If the learner has prior exposure, run a brief placement diagnostic per
  unit (1–2 questions each, one at a time). Seed levels from it with a
  trailing `?` (provisional, capped at 2).
- Record anything they got wrong in `misconceptions.md`.

## 6. Save and start
Commit ("Set up course: <subject>") and push to `main`, silently, per the
Git workflow in `AGENTS.md`. Then begin Lesson 01 (or the first lesson
below 3) in tutoring mode.
