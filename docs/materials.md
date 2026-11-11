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
  role, why, cost/licence) and get approval of the sources before
  downloading or adding them. (Approval is about *which* sources, not git:
  once approved, commit them like any other learning work.) Fewer, better sources beat many overlapping ones.
- If the network or tools block a fetch, record the link and tell the
  learner what to download manually. If your platform has no web access
  at all, say so and suggest well-known sources from memory, marked
  unverified, for the learner to fetch and confirm.

## 4. Indexing → `resources/README.md`
- **Texts**: map each lesson to sections and page ranges. Note any page
  offset between printed and PDF numbering.
- **Problems**: map problem numbers to lessons; mark which have solutions
  and where those solutions are.
- **Videos** (fully automated pipeline, no API key needed):
  1. **Fetch.** `pip install yt-dlp`, then
     `python3 tools/fetch_videos.py <video-or-playlist URL> ...`. This writes
     `resources/videos/NN.md` per video: title, link, length, the uploader's
     chapters (if any), an empty concept-index table, and the timestamped
     transcript (uploaded captions preferred, auto-captions otherwise). It
     skips files that already exist, so it is safe to re-run; use `--first N`
     to number additional videos after existing ones.
  2. **Index.** Read each transcript and fill its concept-index table: one
     row per concept segment (`| Start | End | Lesson | Concept |`, times as
     `m:ss`), lesson = syllabus number(s) or `—` for off-topic parts. Take
     times from the transcript lines, never guess. Segments of roughly 1–8
     minutes, one idea each, work best. Work one video at a time (in a
     subagent per video if your platform has them, since transcripts are
     long), and commit after each so progress survives interruptions.
  3. **Build.** `python3 tools/build_clips.py` regenerates
     `resources/clips.md`: for every lesson, the clips that cover it as
     player links, plus a list of lessons with no video coverage. Re-run it
     after any index edit; never edit `clips.md` by hand.

  If YouTube blocks the fetch (e.g. "sign in to confirm you're not a
  bot", common from cloud machines), ask the learner to run step 1 on
  their own computer and commit the output; steps 2–3 then run as normal.
  Videos with no transcript: index from the uploader's chapters if present,
  otherwise link the whole video and name the topic without times.
  Non-YouTube videos: index by hand in the same `NN.md` format if a
  transcript is available.
- **Clip links** (generated by `build_clips.py`) use the shared clip
  player, which plays only the segment and stops by itself:
  `https://dylanlmartin.github.io/video_embedding/?v=<id>&start=<sec>&end=<sec>&title=<url-encoded text>`
  (times in seconds or `m:ss`). Raw `youtube.com/embed` links often fail
  with "Error 153" when opened directly, because YouTube's player must run
  inside a web page; the player page handles that and has an "Open on
  YouTube" fallback. To host your own, fork
  [dylanlmartin/video_embedding](https://github.com/dylanlmartin/video_embedding),
  enable GitHub Pages, and replace the base URL. Use
  `https://youtu.be/<id>?t=<sec>` for a single moment rather than a
  segment. Videos whose owners disable embedding only play on YouTube.
  If no transcript or chapters are available, link the whole video and
  name the topic without times.
- **Coverage gaps**: list lessons with no coverage so the tutor knows to
  teach from first principles or source more material.

## 5. Adding material mid-course
The learner can add or ask for material at any time ("here's a new
playlist", "find me more problems on X"). Then: catalogue it (§2/§3),
index it (§4) for current and future lessons, and commit silently to
`main`. If a lesson is
being taught with thin coverage, the tutor may propose sourcing more. This
is a short detour: the current question still stays pending.

## 6. Using materials during lessons
- Teach first, then point to the source section or clip for that concept
  (or show the clip first and then discuss it). One clip per concept;
  keep clips short.
- Draw practice problems from problem sources, but never show a solution
  while its question is open (see "No answer leakage" in `AGENTS.md`).
- References and cheatsheets come out only after the concept is taught.
