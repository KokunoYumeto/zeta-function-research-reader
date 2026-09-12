# Tau-base formalization recovery and global comparison

This owner-directed continuation recovers the interrupted tau-base sources and extends the existing SplitZero Lean workspace. It does not create a second scalar implementation. No Sneed-side work is included.

The exact source files are in `formal/splitzero/`; see `TAU_RECOVERY_MODULES.txt`, `TAU_RECOVERY_TARGETS.json`, and `TAU_RECOVERY_MATHEMATICS.md`. Run the `SplitZero tau recovery` workflow, or the reproduction commands in that mathematical note. A completed successful run at an exact source revision, not this README, supplies the execution record.

Sources: the interrupted tau branch at `621eb8863d6e0421b1ce3a604e5712c14d7b5cc2`; the accepted derived package at `14c69d604044b848d64318751a7bee19edfd9aba`; chain-descent PR #9 at `8f99b94d306c3b1aaa817d52c57fa6fd298d511c`; and global-retraction PR #10 at `d26c283c2a58da57bb5a5a4d4bc8669019f6ebb7`.

The analytic construction of the global theta inverse and the arithmetic weight estimates are not Lean theorems in this package. Its retraction, continuity, and operator results have explicit hypotheses that those analytic constructions must supply. No private transcripts or external source corpus are republished.
