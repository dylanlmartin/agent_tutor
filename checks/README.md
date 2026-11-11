# Checks

Scripts that verify answers empirically, so correctness doesn't rest on
the tutor's say-so. What fits depends on the subject:
- maths / probability / statistics: Monte Carlo simulations, numeric checks;
- programming: runnable snippets and tests;
- physics / finance / engineering: small calculators or models.

Naming: `NN_short_name.<ext>` where `NN` is the lesson number.
Keep each short, deterministic (fixed seed), and print the computed result
next to the expected answer. Subjects with nothing to execute (history,
languages, …) can leave this folder empty.
