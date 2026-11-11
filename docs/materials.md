# Materials: providing, sourcing, and indexing

Materials are flexible. A course can run on anything from a single
textbook PDF to a mix of videos, articles, docs, and problem sets that the
learner supplied or the agent found, or on nothing at all (the tutor
teaches from first principles). Whatever is used, it is catalogued in
`resources/README.md` and mapped to lessons so the tutor can point to the
right section, page, or clip at the moment a concept is taught.

## 1. What counts as material
| Kind | Examples | What the tutor uses it for |
|---|---|---|
| Primary text | textbook, course notes, official docs, a book | Spine of the syllabus; readings per lesson |
| Video | lecture series, talks, explainer videos | Short clips while teaching a concept |
| Problems | problem sets, exercises, past exams, katas | Practice and review questions |
| Solutions | answer keys, solution manuals | Checking finished answers only |
| References | cheatsheets, formula sheets, API references | Lookup *after* a concept is taught |
| Interactive | simulators, visualizations, sandboxes, REPLs | Exploration and checks |
| Learner notes | your own notes, slides, flashcards | Context on what you've seen before |

## 2. Learner-provided materials
Accept anything, in any form:
- **Files** dropped into `resources/` (PDF, EPUB, slides, notes, transcripts,
  code). Keep large binaries out of git only if the learner asks; otherwise
  commit them so future sessions can open them.
- **Links** (sites, playlists, repos, courses): record them in the catalogue;
  download a local copy only when the license allows and it helps.
- **Partial material** is fine: e.g. "I have the textbook but no problems"
  means the agent sources problems (§3) to fill the gap.

For each item, work out and record: what it is (title, author, edition),
how to locate things in it (e.g. "PDF page = printed page + 18"), whether it
contains solutions, and its license/origin.

## 3. Agent-sourced materials
When the learner has no materials, or there are gaps, the agent searches
for them. Guidelines:
- **Search for each role in §1 separately**: one primary text, a lecture
  series, problem sets with solutions, a reference sheet, interactive tools.
- **Prefer** free, reputable, stable sources: open textbooks (OpenStax,
  LibreTexts, authors' free PDFs), university OpenCourseWare (MIT OCW,
  Harvard, Stanford), official documentation, well-known lecture series and
  educators on YouTube, and established problem collections.
- **Vet before proposing**: check the author/institution, that the content
  matches the learner's level and goal, and that it covers the syllabus. For
  videos, check length, audio and whether a transcript or chapters exist.
- **Respect licenses**: link to anything you can't redistribute. Never
  download pirated copies.
- **Propose, then confirm.** Show the learner a short shortlist (source,
  role, why, cost/licence) and get approval before downloading or
  committing anything. Fewer, better sources beat many overlapping ones.
- If the network or tools block a fetch, record the link and tell the
  learner what to download manually.

## 4. Indexing → `resources/README.md`
- **Texts**: map each lesson to sections and page ranges. Note any page
  offset between printed and PDF numbering.
- **Problems**: map problem numbers to lessons; mark which have solutions
  and where those solutions are.
- **Videos**: index by concept with start/end times taken from a
  transcript or the video's own chapter markers, never guessed. Where you
  can fetch a transcript (e.g. `yt-dlp --write-auto-subs --skip-download`),
  save it under `resources/videos/NN.md` with a concept index table
  (start, end, lesson, concept) above the timestamped transcript. Clip
  links: `https://www.youtube.com/embed/<id>?start=<sec>&end=<sec>` plays
  just the segment; `https://youtu.be/<id>?t=<sec>` opens at a moment. If
  no transcript or chapters are available, link the whole video and name
  the topic without times.
- **Coverage gaps**: list lessons with no coverage so the tutor knows to
  teach from first principles or source more material.

## 5. Adding material mid-course
The learner can add or ask for material at any time ("here's a new
playlist", "find me more problems on X"). Then: catalogue it (§2/§3),
index it (§4) for current and future lessons, and commit. If a lesson is
being taught with thin coverage, the tutor may propose sourcing more. This
is a short detour: the current question still stays pending.

## 6. Using materials during lessons
- Teach first, then point to the source section or clip for that concept
  (or show the clip first and then discuss it). One clip per concept;
  keep clips short.
- Draw practice problems from problem sources, but never show a solution
  while its question is open (see "No answer leakage" in `CLAUDE.md`).
- References and cheatsheets come out only after the concept is taught.
