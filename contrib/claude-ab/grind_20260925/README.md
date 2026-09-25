# claude-ab lane: salvage, verification and new results (25 September 2026)

Author: Claude (Anthropic), model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort, working as the "claude-ab" lane beside the ChatGPT/Codex lanes and the other Claude sessions. Everything here lives on the branch `claude/claude-ab-grind-20260925`. Nothing on `main` is modified.

The folder is organized by the owner's four goals:

1. negative results, stated readably;
2. bridges between programmes;
3. lemmas that can be stated independently of the project;
4. the F1 context.

`00_RESULTS_REGISTER.md` is the index. Each other file states its own scope and verification status.

| File | Content |
|---|---|
| `00_RESULTS_REGISTER.md` | Register of lemmas, negative results, bridges and F1 context, with status and source |
| `01_…`, `04_…`, `05_…`, `07_…` | Content maps of the second attempt's proofs, read in full, with independent checks |
| `08_DELIGNE_MECHANISM_AUDIT_EULER_TEST_AND_THE_SQUARE.md` | The Euler test (which proved statements survive a non-factorial sheet with off-line zeros), Deligne's inputs compared with the programme's constructions, and the F1 framing (revision 2, after a referee pass) |
| `02_…`, `03_…` | Reports of the second Claude instance ("copy-newresults"), with claude-ab's verification headers |
| `06_THEOREM_E_REFEREE_REPORT.md` | Referee report on Theorem E (the Eulerian characterization by velocity spectra) |
| `checks/` | Independent check scripts with their outputs |
| `copy_round2/code/` | The copy's scripts. The zero data they read from `data/` are not published; `zerodata.py` regenerates them |
| `09_HARMONIC_SWEEP_SOURCE_PAIRING_AND_NYMAN_BEURLING.md` | Content map of the 25 September harmonic-sweep (HSW), source-pairing (OPD) and positive-measure (SPF) notes. It also gives the bridges to Hilbert–Pólya, Wiener, Nyman–Beurling and Burnol's co-Poisson theory |
| `PLAN.md` | The working plan and log |
| `BRIEFING_FOR_LOCAL_SESSION.md` | Briefing for a cooperating local Claude session |

None of these files claims a proof or disproof of the Riemann hypothesis.
