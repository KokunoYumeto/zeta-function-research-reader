# Working plan: extracting results from the split-zero / RH programme

Claude (Opus 5.5 configuration), session claude-ab. Started 25 September 2026, 00:52 UTC.

## The four goals, as the owner set them (25 September 2026)

1. **Negative results.** Collect what did not work, and state each one readably and accurately: the precise statement, its scope, and the reason. Machine labels do not replace the statement.
2. **Bridges.** Record connections the programme found or implied between fields (F1 geometry, heat flow, noncommutative geometry, analytic bounds, algebraic geometry) and between programmes (zeta, Erdős–Straus, Navier–Stokes, Yang–Mills, topology), where results were used interchangeably.
3. **Standalone lemmas.** Extract statements that hold, and can be stated, without the programme's vocabulary.
4. **F1 context.** Place the ansätze in the F1 literature, and frame the question the programme asked, partly inadvertently.

The material is judged holistically and by what it establishes, not by its own framing and not by whether it proves RH. Both working styles in the corpus are legitimate: exhaustive calculation, which constrains the space, and following one precise idea to its consequences.

## Reading rule

Read the mathematics itself: proofs, derivations and calculations. A README, summary or disclaimer is not a reading of the work. A statement enters a deliverable only after it has been checked by derivation, computation or citation, and the deliverable says which.

## Standing constraints

- Formal register. Every claim is proved, computed or cited. Opinions are labelled as opinions.
- Never identify τ with the supported zero e.
- The main branch is not touched. Pull requests, if any, go on separate branches and state the model.
- No private paths in public outputs. No heavy scans of the owner's computer. No spawning of agents at scale; at most one or two, and only for reading that would otherwise overflow context.
- No notifications beyond the self-timer below.

## Order of work, and why

| Block | Content | Reason for its position |
|---|---|---|
| 1 | Read the second attempt's new work in full: `temporary-arguments/20260924-fixed-generic-point-purity` (prime clocks P1–P14, winding parity, orchard and spectrum, Deligne common modulus, clock arithmetic, timed-prime reconstruction, clock-history radius). Then the three-lane edition's proofs, in order of dependence. Deliverable: a content map of what it establishes, with checks. | The owner pointed out that the previous reply read only the conclusions. This is the active direction, and its overlap with Connes–Consani arXiv:2609.00299 is exact in places. |
| 2 | F1 note: the split-zero semiring G(R) and the τ〈Z1; no Z2〉 construction in F1 geometry (Deitmar, Lorscheid, Connes–Consani spherical algebras, arithmetic site, twistor line, Borger's λ-rings), with exact comparison maps. | Goal 4. Parts were derived in the replies of 24–25 September; they need a standalone statement with literature. |
| 3 | Standalone lemmas register: statement in standard terms, proof status, literature search for prior occurrence. | Goal 3. Candidates come from Blocks 1–2 and from earlier work: the Eulerian-weight theorem N1, the Stokes datum, the circle heat-kernel Mellin identity, the fixed-point and mirror-parity statements, TD1 and TD8. |
| 4 | Negative results register. | Goal 1. There are many across the lanes; each needs a plain statement and its exact scope. |
| 5 | Bridges: locate results reused across fields or programmes, and check that the shared lemma's hypotheses hold in every use. | Goal 2. This is the most expensive block, and it needs the vocabulary built in Blocks 1–4. |
| 6 | Verification pass over every deliverable. | Required before anything is presented as a result. |

## Access

The owner's computer is not connected at the start of this plan. Block 1 therefore works from the published GitHub copy (zeta-function-research-reader, commit 064f33b). Material that exists only on the local disk waits for reconnection. Deliverables are written here, and are copied to `work/claude_grind_20260925/` in the math folder once the computer is reachable.

## Timer

A reminder is scheduled into this session. When it fires: read this file and the log below, continue the first unfinished block, append to the log, and schedule the next reminder before stopping.

## Earlier backlog (from this session's task list)

- #10: collect and verify the ChatGPT Pro audit (A/B).
- #15–#17: SGA 6 Riemann–Roch for G(Z) and the height change.
- #16: the earlier reading items (P2 later sections, secondary note, identity–absorber folder, Pro answers). Its identity–absorber part falls under Block 1.
- #21: the correction to the zero-prime note (N(P0) ∈ {0, ∞}) and Theorem F (τ-square collapse). This belongs under Block 4 as an erratum.

## Log

- 2026-09-25 00:52 UTC: plan written; timer set (send_later, fires 03:23 UTC); Block 1 started from the GitHub copy.
- 01:00 UTC: Block 1, part 1 finished.
  - I read the fixed-generic-point folder in full: CC1–CC5, W1–W10, D1–D5, P1–P14, TP0–TP14 and the clock-history note.
  - Deliverable: `01_SECOND_ATTEMPT_FIXED_POINT_AND_CLOCKS_CONTENT_MAP.md`, with checks in `fgp_checks.py` (all pass).
- 01:00–02:45 UTC: second instance "copy-newresults", launched at the owner's request (Agent, remote isolation).
  - **Round 1:** Theorems A and B, and C (C conditional on RH and simplicity); primes read off the velocity spectrum; the sign sector y² = x³ − x as the receiver asked for in TD12.
  - **Round 2:**
    - Theorem A_a on every sheet;
    - Theorem F (the exact smoothed velocity spectrum);
    - Theorem E (the spectrum is multiplicative iff a ∈ {1, 1/2});
    - Theorem D (the velocity angle equals the Gram offset, which explains the one-sided tail);
    - Proposition H (typed morphisms from the sign sector to TD3 and TD12).
  - **Independent checks by claude-ab, all pass:**
    - Theorem A at [100, 1000], Δ = 1 with mpmath zeros: relative difference 1.8e-18;
    - Theorem D for n ≤ 40: deviation 2e-30;
    - the exact β_r(2) values;
    - the elliptic-curve lifts, checked by hand.
  - Reports saved as `02_…` and `03_…`.
- 02:40 UTC: erratum to the N3 table in `SHIFTED_SHEETS_N1_N3.md`.
  - The T = 2515 column contains 1,999 zeros.
  - The explanation of the failure of the horizontal law was corrected by the copy's Theorems C and D.
- GitHub cooperation branch: the git proxy refused a dry-run push. KokunoYumeto/zeta-function-research-reader is not in this session's authorized repository set, and the owner would have to add it to the session's sources.
- 03:05 UTC: the computer reconnected. Deliverables 00–03 and the check scripts were copied to `work/claude_grind_20260925/`. The N3 erratum was written to the disk copy, guarded by its expected timestamp.
- 03:30 UTC: Block 1, part 2.
  - Read in full: S1–S7, PSC, CFP and CPS.
  - Deliverable: `04_SECOND_ATTEMPT_POSITIVE_QUOTIENT_CONTENT_MAP.md`, with checks in `checks/lane_pq_checks.py` (all pass).
  - First consolidated register: `00_RESULTS_REGISTER.md`, organized by the four goals.
- 03:30–03:40 UTC: Block 1, part 3 (first half), and a referee pass.
  - Read in full: IH1–IH8, PL1–PL8 and TL0–TL8 (the integrality, loop and weight-separation notes of the character-lifting lane).
  - Deliverable: `05_SECOND_ATTEMPT_INTEGRALITY_LOOPS_AND_WEIGHT_SEPARATION.md`.
  - Referee pass on the copy's Theorem E, done by me instead of a copy round: `06_THEOREM_E_REFEREE_REPORT.md` (verdict: correct), with `checks/thmE_referee_checks.py` (all pass).
  - Register updated: lemmas S14–S16, negative results 14–17, bridge 9.
  - Next timer: 06:31 UTC.
- Next block:
  1. Block 1, part 3 (second half): the character-lifting core (MCL, then SCT, RPC, ORE), then the Deligne reconstruction's core (DC/DR/DP) in order of dependence.
  2. Write the FLIP_FABLE Addendum 4 erratum into the negative-results record.
  3. Optionally, copy-newresults round 3 (a literature comparison with Meyer for S12–S13; a re-proof of Theorem C).
