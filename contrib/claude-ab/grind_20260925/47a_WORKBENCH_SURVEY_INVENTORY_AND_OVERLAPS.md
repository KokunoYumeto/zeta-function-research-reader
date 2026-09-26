# Workbench survey: inventory for the workbench readers

Prepared by Claude (model `claude-opus-5-5`, Opus 5.5, maximum reasoning effort), 26 September 2026, 01:56 UTC. This is an inventory for the author to audit and write from; it is not a reader. It is read-only work: nothing in any repository was committed, pushed or edited. The only writes were `git fetch` of `origin` and lazy blob fetches into the local object stores.

Organisation: §0 sources and conventions; §§1–7 one block per workbench (ES; YM; NS; S⁶/Alpöge; Jacobian-counterexample material; Erdős 817; Collatz); §8 overlaps; §9 gaps; §10 discrepancies found while surveying. The task asks for four readers "one per workbench". The provided repositories are ES, YM (which also holds NS, S⁶ and the Jacobian attribution), 817 and zeta. There is no Collatz repository among them (see §7). How the seven blocks map onto four readers is the author's decision.

---

## 0. Sources, method, conventions

### 0.1 Commits read

| Repository (local path) | `origin/main` read | Commit date | Clone state and notes |
|---|---|---|---|
| ES `erdos-straus-foundation` | `d20b32e1547aee2f08b440d56cceb47ab16dc4b7` | 2026-09-23 22:38 +0200 ("Pin ES proof locators and publication receipts") | Shallow (depth 1), sparse, partial clone; unchanged by today's fetch. Same commit that `21_` read. |
| YM `yang-mills-interacting-workbench` (also `navier-stokes/`, `s6/`) | `fa79faff2cd697e16cfa3a7953f36810c22c8922` | 2026-09-21 23:51 +0200 ("Publish fifth-reference source, physical spectrum and heat reader") | No working tree checked out; read through git objects; 38 commits. Other remote branches (`poly-clank/*`, `research/2026091*`) were **not** read. Same commit that `21_`, `28_`, `34_` read. |
| 817 `erdos-problem-817-workbench` | `dbd0a93f2cf935103e88e5c2b2b71fe85ae7537b` | 2026-09-16 23:45 +0200 ("Publish finite-period approximation and corrected cumulative research reader") | Shallow, sparse. |
| zeta `zeta-function-research-reader` | `baa6f7a58c00390b0fae25b56b8350f2c1a685a5` | 2026-09-25 06:41 +0200 | Fetched today (local checkout is still at `32acd0d`; not used). Overlap look-ups only. |

Audit notes read first: `21_CROSS_PROGRAMME_BRIDGES_PART1…`, `28_CROSS_PROGRAMME_BRIDGES_PART2…`, `34_AUDIT_YM_THEOREM_14_2…` (all in full); `00_RESULTS_REGISTER.md` (Goal 2 bridges 1–44; rows S40, S41, S52–S54; negative results 42, 49, 57); `BRIEFING_FOR_LOCAL_SESSION.md`; the tail of `PLAN.md` (the readers request, 25 Sep 23:38–23:42 UTC; board task 10).

Drift check: `21_`/`28_`/`34_` read ES and YM at the same commits as above. The zeta files used by the ES↔zeta edges (`satellites/10_literature_foundations.tex`, `satellites/14_globalization_cue_split_zero_and_shifted_sheets.tex`) have the same blob ids at `42d00e3` (read by `21_`) and at `baa6f7a` (`04c807f0`, `49318a57`).

### 0.2 Method and limits

- Material was located by listing tree paths on all fetched branches (for file names) and by `git grep` over text blobs (md, tex, json, py, txt, lean) at `origin/main`. PDF, ZIP, GZ and PNG members were not opened. Content inside release ZIPs is therefore not surveyed.
- Each item below says whether I read it in full, read its statement only, or only located it.
- Line numbers refer to the file at the commit in §0.1.
- Quotations are under 15 words; everything else is paraphrase.
- I re-proved nothing, except two small arithmetic facts marked "my arithmetic".

### 0.3 Status vocabulary

- **WB label**: the workbench's own words, e.g. "proved", "ordinary mathematical proof", "candidate", "not certified", "reconstruction".
- **Proof in repo**:
  - Y: a complete written proof is in the git tree (path given);
  - P: partial;
  - N: the proof is external or absent.
- **Checks**:
  - F: finite exact-arithmetic or symbolic replays recorded by the workbench;
  - L: Lean-checked;
  - —: none.
- **Audit** (by `21_`/`28_`/`34_`):
  - C: checked and correct (corrections noted);
  - Cc: correct conditional on stated inputs;
  - Lo: located only;
  - —: not audited.

### 0.4 Web checks (26 September 2026)

| External source | Outcome |
|---|---|
| T. Tao, "A digestion of the Jacobian conjecture counterexample", 21 Jul 2026 | Fetched. It gives the same F as YM `ATTRIBUTION.md` L11–17, det DF = −2, and (0,0,−1/4), (1,−3/2,13/2), (−1,3/2,13/2) ↦ (−1/4,0,0). Per the fetch summary it credits the result to work "using the Fable AI" and does not name Alpöge. |
| D. Speyer, "The new counterexample to the Jacobian conjecture", 20 Jul 2026 | Fetched. It reports that "Levent Alpöge tweeted that Fable had found a counterexample". |
| Alpöge's X post `x.com/__alpoge__/status/2079028340955197566` | **robots.txt disallowed.** Not retrieved by other means. The credit "Akhil for the question and Fable for the work" rests on the repositories' reports (YM `ATTRIBUTION.md` L9; zeta `README.md` L295). |
| `alpo.ge/s6.pdf` | Fetched. Title: "A compact complex threefold fibred by tori over the projective line, and the six-sphere". Abstract: X is "diffeomorphic to S6". The p. 2 "Setup" has Π(z) = [[6μ, τ, 1, 0], [β, μ, 0, 1]], and the text uses the (3,4,∞) modular family of 2-tori. Two targeted fetches found **no author line and no AI or Claude credit** in the returned text. |
| P. Engel, "Complex Structures on S^6", 13 Sep 2026 (`philip-engel.github.io/S6.pdf`) | Fetched. The abstract says the manuscript was "produced by Claude under the direction of Levent Alpöge". §1.1 mentions a 108-page manuscript. The exposition states a self-contained proof (its Theorem 4.1), and §1.3 displays Π(z). |
| OpenAI, *Finite Time Blowup for Navier–Stokes* (`cdn.openai.com/pdf/32d9f210-…/navier-stokes.pdf`) | Fetched. Title and author "OpenAI" confirmed, and Theorem 1.1 matches ES `ns_operator_bridge/ATTRIBUTION.md` L18–44. The page count was not reliably determined; the repositories record 165- and 166-page captures under this same URL. |
| `github.com/KokunoYumeto/collatz-workbench` | Fetched. It exists and is public; README title "Collatz research workbench". Per the fetch summary it holds a 16 Sep cumulative collection of 237 pages in 20 chapters, and says it is "not a claim that the Collatz conjecture has been solved". **Not among the provided repositories; not cloned.** |
| arXiv:2609.06303 (S. Costa), cited by 817 | The abs page returned no machine-readable text, and `export.arxiv.org` is **robots.txt disallowed**. Not retrieved otherwise; 817's own `sources/costa-2026.md` is used instead. |

---

## 1. Erdős–Straus workbench (ES)

### 1a. Location, own status, dates

**Repository.** KokunoYumeto/erdos-straus-foundation @ `d20b32e` (23 Sep 2026). Collective author "The Clankers" (README L469). Human credits:
- u/UmbrellaCorp_HR and u/CommonCareful3149;
- JT (12 Sep continuation);
- the owner (KokunoYumeto = u/lepthymo; RESULTS.md L41).

**Entry files.**
- `README.md`, with the 28-item "Start reading" list at L44–401 and the edition table at L439–447.
- `RESEARCH_STATE.md`, with the approach/scope table at L83–112.
- `RESULTS.md`, `results/PROOF_NOTES.md`, `results/records.json`, `results/check_selected.py`.
- `SOURCE_LED_RESULTS.md` and `results/integration-2026-09-10/{ARGUMENTS,CROSS_WORKBENCH_COMPARISON,SOURCES}.md`.
- `WORKBENCH.md`, `ATTEMPTS.md`, `DAILY_RESULTS_20260919.md` … `DAILY_RESULTS_20260923.md`.
- `INTEGRATION_OPPORTUNITIES.md`, `RESEARCH_DIRECTIONS.md`, `LITERATURE.md`.
- `polyclank/claims.json` (the index of 72 statements).

**Proof sources.**
- `research/expanded-2026-09-08/exact_bounded_transport_72/`: 15 canonical modules and 85 files; Zenodo 10.5281/zenodo.22678971, 9 Sep.
- `research/continuation-2026-09-12/`: the JT Boolean/cyclotomic work and `received/es_s6_counterfactual/`.
- `research/incoming/*`: 41 folders dated 10–23 Sep, typically with `core.tex` or proof files, a README, checks and `source_reading.json`. Of these, 27 back the README list (table E below) and 14 earlier packages are listed in table F.

**Editions** (README L439–447):
- the 124-page GitHub cumulative ES/Fable reader (`research/incoming/es-fable-zeta-bridge-20260920/output/pdf/ES_FABLE_ZETA_CROSSWALK.pdf`);
- the 86-page supplement (Zenodo 22678971) and the 67-page supplement (22666493);
- the 619-page archive (31 Aug);
- the 488-page reader (repository root PDF; source only inside `01_…zip`).

**Own status.**
- README L3: "The project does not claim a proof or counterexample to the conjecture."
- RESEARCH_STATE L5–6: "an ongoing research programme, not a completed proof".
- Scheduled mirroring has been paused since 9 Sep (README L479–488).
- Scope of the target (RESEARCH_STATE L11–36): primes p ≡ 1 (mod 24) remain. These identities are "not advertised as new results" (L33).

### 1b. Main results

**A. Published 72-statement supplement** (9 Sep; `exact_bounded_transport_72/`). Common WB status:
- RESEARCH_STATE L152–154: written proofs and recorded finite checks; "not represented as a whole-supplement Lean formalization".
- The index `polyclank/claims.json` has verification scope "File identity, deterministic extraction and reference consistency only".

| ID | Statement (paraphrase) | Locator | Proof in repo | Audit |
|---|---|---|---|---|
| ES-01 | Shell bijection: 𝒲_a (coprime divisor pairs of S_a with R_a ∣ m+n) ↔ ordered solutions with first denominator a | `bounded_transport.tex` `lem:units` L49–67 | Y | — |
| ES-02 | ES(p) ⇔ Q_p = Σ_a(\|E_a\| + ½\|M_a\|) > 0; shellwise and global no-hit criteria | RESEARCH_STATE L56–70; `bounded_transport.tex` L146; `counterexample_sieve/all_shell_no_hit.tex` `thm:shellwise-no-hit` L79, `thm:global-no-hit` L295 | Y | — |
| ES-03 | Complete residual-3 and residual-7 factor sieves | `first_two_shell_sieve.tex` `thm:r3-factor-sieve` L18, `thm:r7-factor-sieve` L95; `all_shell_no_hit.tex` `cor:global-r3-r7` L330 | Y | — |
| ES-04 | Bounded exponent gluing/CRT, ratio and shear transports; "no two consecutive positive shears" | `bounded_transport.tex` (17 statements: `thm:glue` L243, `thm:divisor-crt` L515, `thm:ratio` L694, `thm:shear` L806, `thm:no-two-shears` L893, …) | Y | — |
| ES-05 | Connes–Consani ordered-group and cyclic interfaces | `connes_reading/connes_primitive_intersections.tex` (7 statements); `integral_cyclic_bridge.tex` (3) | Y | — |
| ES-06 | Unary/Boolean transport, shared-variable CRT, input–output and raw-scale incidence, fixed-y successor, boundary swap (exact first code on the residual-3 domain) | `unary_boolean_transport.tex` (3), `shared_variable_crt.tex` (5), `input_output_incidence.tex` (1), `raw_scale_hit_incidence.tex` (4), `exact_audit/fixed_y_successor.tex` (1), `boundary_swap/boundary_swap_completion.tex` (4; `thm:boundary-r3-global-minimum` L383) | Y | — |
| ES-07 | **NS auxiliary-torus operator bridge** (21 of the 72 statements) | `ns_operator_bridge/torus_cover_lemma.tex` (7: `thm:ns-directional-intertwining` L33, `thm:ns-torus-fibres` L92, `thm:ns-torus-average` L150, `prop:ns-torus-powers` L236, `lem:ns-finite-dual` L278, `thm:ns-es-packet` L341, `cor:ns-es-cover-repair` L454); `sieve_character_cover.tex` (4); `reverse_proof_transport.tex` (5); `reverse_smooth_inverse.tex` (5; `thm:ns-sharp-denominator` L20) | Y | **C** for `thm:ns-es-packet`, `cor:ns-es-cover-repair` and `thm:ns-sharp-denominator` (`21_` §1, Prop. 21.1, Neg. 21.2, Lemma 21.3; checks A1–A7; register S40). **Lo** for `sieve_character_cover.tex` and `reverse_proof_transport.tex` (`21_` §10). |

**B. Results bench R01–R10** (10 Sep; `RESULTS.md`, `results/PROOF_NOTES.md`). Common WB status (RESULTS.md L31–33):
- "No formal prover was run, no independent reviewer was obtained";
- "no comprehensive novelty search was performed";
- "Do not describe this as ten newly discovered theorems."

Checks F (`results/check_selected.py`). Proof in repo: Y for each, in PROOF_NOTES. Most items trace to CN-* sources in the owner's private Chatnotes archive, which is not public.

| ID | Statement (paraphrase) | PROOF_NOTES locator | Audit |
|---|---|---|---|
| R01 | Adjoin an absent zero τ to a ring: S = R ⊔ {τ} is a commutative semiring; {τ} is prime, and {τ, 0_R} is prime iff R is a domain | L5–13 | Zeta counterpart G(R) checked by hand in `21_` §6 |
| R02 | In ℂ[C₆], δ_k = e₃ + 2e_{3−k} has all Fourier components nonzero | L15–21 | — |
| R03 | 15 → 16 finite coordinate algebra on Ogg's primes (partition 1+7+7 → 1+1+7+7) | L23–31 | — |
| R04 | Busy-Beaver/107 congruences (6, 21, 107, 47,176,870; p = 8,803,369) | L33–41 | — |
| R05 | **Collatz**: T(n) = 4n+1 and θ(n) = 3n+1 satisfy θT = 4θ; the odd step U(n) = (3n+1)/2^{v₂(3n+1)} satisfies U(T^j n) = U(n) | L43–53 | — |
| R06 | mod-53 deficit progression and two covering translates | L55–63 | — |
| R07 | inf over k ≠ 0 of \|v·k\|‖k‖ equals 1/√(4+2√2) for the √2 directions (the same statement as ES-07's `thm:ns-sharp-denominator`) | L65–73 | **C** (`21_` Lemma 21.3; A7) |
| R08 | Three-colour lattice test: Λ³, its diagonal and zero-sum parts, Eisenstein action; a Leech input gives rank 72 | L75–85 | — |
| R09 | Finite Star–Kneser obstruction (imports Kneser via DeVos, arXiv:1303.3539) | L87–93 | — |
| R10 | Order-72 glue H ⊂ (ℤ/6)⁴ × F₂² (duad code plus tetracode), with q(H) = 0 and coset costs 4 (×46) and 6 (×25) | L95–103 | — |

**C. Source-led X1–X7** (10 Sep; `results/integration-2026-09-10/ARGUMENTS.md`). WB (SOURCE_LED_RESULTS L7): "reusable expositions or checks, not seven new discoveries". Checks F (`verify_results.py`).
- X1: the M₅(F₁₀₇) algebra (already present in a local integrated ES reader; CROSS_WORKBENCH L13–17).
- X2: Descartes/Kocik pencil.
- **X3**: support-sensitive semiring G(R) (ARGUMENTS L61–71).
- **X4**: support-aware affine homogenization, a **Collatz**-related item (L73–87).
- X5: abstract C₆ Fourier law, together with a false identification mod 840 in source S5 (L89–99).
- **X6**: finite Weyl basis.
- X7: neutral-state gap 1/(9ρ²) in a diagonal model (L127: "not an interacting Yang–Mills theorem").

Audit: X3 **C** via its zeta counterpart (`21_` §6); X6 not read by `21_`; the others —.

**D. 12 Sep continuation** (`research/continuation-2026-09-12/`)

*ES-08 (JT Boolean/cyclotomic).*
- At p = 1201, a = 310, character-cell energy 30 < 32 forces the middle target (RESEARCH_STATE L122–131; `reconstructed/boolean_cyclotomic.tex`).
- It also contains a common-modulus affine return map with hexagonal coordinates and an explicit compactification correction (`CORRECTIONS.md`).
- Proof in repo: Y (reconstructed modules). Audit —.

*ES-09 (**ES → S⁶**, `received/es_s6_counterfactual/`).*
- Setting: affine torsion covers of the (3,4,∞) period monodromy (matrices A₁, A₂, A_∞ from `alpo.ge/s6.pdf` §2, Lemmas 2.4–2.7; `src/core.tex` L1–20).
- Results:
  - `thm:class`: a primitive obstruction class of exact order D (`src/core.tex` L38);
  - `lem:shears` (L75);
  - `thm:orbits`: complete odd-level orbit classification and genus formulas, with g(D) = (5D³ − 12D² − 17D + 24)/24 for 3 ∤ D (L106) and g₁(D) for 3 ∣ D (L108);
  - `prop:crt` (L173).
- Application (`preprint.tex` L55–64): ES holds at p exactly when some fully marked candidate has return level D = 1.
- WB: "written proofs"; "No Lean build or independent mathematical review" (README L38–40). It uses the S⁶ matrices, "not the source's global six-sphere claim" (preprint L24–25).
- Proof in repo: Y. Checks F (`verify.py`). Audit —.

**E. Structural continuations, 17–23 Sep** (README items 1–28; proof bulletins with 98 stable IDs).

Common WB status:
- DAILY_RESULTS_20260922 L679–686: the Python replays "are not Lean builds or independent human review", and "No module claims a proof or counterexample to the Erdős–Straus conjecture."
- The 19 Sep frontier (DAILY_RESULTS_20260919 L297–311): the remaining statement is ∀p in the unresolved class, #E_p + #M_p > 0; "No result in this bulletin assumes that statement".
- Each item below is proved in its `core.tex` or proof files, with checks F.

The bulletin-ID mapping comes from each item's own "Proof:" line.

| README item | Result (paraphrase) | Bulletin IDs | Proof folder (`research/incoming/…`) | Kind (WB) |
|---|---|---|---|---|
| 1 | Simultaneous exterior/middle failure; index-six normal form | — | `es-turn01-joint-failure-20260917` | proved |
| 2 | Complete shifted-factor graph; genuine seven-vertex sink at p = 2521 | — | `es-turn02-shifted-graph-20260918` | "disproves the proposed local/cycle implication, not Erdős–Straus" (README L57–58) |
| 3 | Certified constant-C₆ three-cycle refutes strict canonical descent | — | `es-turn03-primitive-sextic-20260918` | method counterexample plus proofs |
| 4 | At most five external nonresidue vertices always have an outside factor t ∈ {1,3,5,7,9} | — | `es-turn04-square-expansion-20260918` | proved |
| 5 | Exterior/middle involution; 2τ(h) pair fibres; Möbius return | — | `es-turn05-channel-coupling-20260919` | proved |
| 6 | Complete-shell spectral bounds; five-mode proof of 60 target pairs at p = 944329, R = 47 | — | `es-turn06-full-shell-20260919` | proved |
| 7 | Pointwise localization via the least quadratic nonresidue | — | `es-turn06b-pointwise-localization-20260919` | proved; "does not prove that it is occupied" (README L79) |
| 8–10 | Sharp middle atlas; strict cubic exterior cutoff; small-shape rigidity through radius 8 | SZ-20260919-001…009 | `es-turn07-middle-cutoff`, `es-turn07b-exterior-atlas`, `es-turn07-shape-rigidity` | proved; "branch reductions, not universal occupancy" (README L98) |
| 11, 13 | **Normalized ES quartic**: p = −5u₄/u₃; coefficient hypersurface 625u₀u₄³ − 125u₃u₄² + 25u₂u₃²u₄ − 4u₃⁴ = 0; 8-point signed fibre; conductor transport; fixed-input cover of ranks 2+6 with monodromy of order 48 and deck group C₂×C₂; rank-8 completion | SZ-20260920-019…039 | `es-fable-zeta-bridge-20260920` (`ES_FABLE_ZETA_CROSSWALK.tex` EZ1–EZ36, `ODD_RECEIVER_ES_PULLBACK.tex`, `FIXED_INPUT_BOUNDARY_MONODROMY.tex`; upstream `FABLE_TO_ORIGINAL_CONDUCTOR.tex`) | proved; "a structural bridge, not an occupancy or zeta-zero theorem" (README L109–110). Audit: quartic identities (019) **C** (`21_` Prop. 21.6, C1–C3); det DP = −2 **C** (`21_` C4); 8-sheet cover, order-48 monodromy and conductor bridge not checked (`21_` §4 Scope) |
| 12 | Prime-local Fable fibres: E has ℚ_p³ × K_ram², M has ℚ_p³ × K_unr²; fixed-cofactor bijection | SZ-20260920-028…031 | `es-turn07-fabel-arithmetic-bridge-20260920` (`INTEGRATION_AUDIT.md`, `corrected/`) | proved after repairs: the audit repairs a missing exterior divisibility gate (README L121–122) |
| 14 | Cofactor capacity trichotomy; sharp h ≤ t² − 3t + 1 | SZ-20260920-040…044 | `es-turn07-capacity-completion-20260920` | proved; "not an ES counterexample" (README L141–142) |
| 15 | Rank-three crossing on a positive-real ray; residue pairing composed with ×2η³; native Gram multiplier | SZ-20260920-045…049 | `es-rh-multi-20260920` | proved; RH-facing parts are "interfaces, not ES occupancy claims" (README L150–151); uses zeta sources (§8 OV-12) |
| 16–17 | Integral signed completion (indices p² and p⁹); defining-prime twist; conductor-index identity | SZ-20260920-050…052, 057…059 | `es-defining-prime-continuation-20260920`, `es-turn07-integral-completion-20260920` | proved |
| 18 | Odd-frame nonsingularity on 3,456 classes mod 521,220; (13;4,18,468) over F₆₁ | SZ-20260920-053…056 | `es-rh-continuation-b-20260920` | proved; conditions "sufficient, not necessary" (RESEARCH_STATE L102) |
| 19 | Global trace integrality; raw-source fibres | SZ-20260920-060…062 | `es-turn07-trace-rigidity-20260920` | proved |
| 20 | General-family source geometry; ES-labelled tensor action; collision exponents | SZ-20260920-063…066 | `es-rh-family-integration-c-20260920` | finite results proved; **metric asymptotics conditional on zeta NG20–NG21** (README L189–192; `SOURCE_LEDGER.md` L20–29) |
| 21 | Original-divisor descent; nine-word boundary u ∣ 36 | SZ-20260921-001…004 | `es-turn07-divisor-descent-20260921` | proved; "method obstructions, not Erdős–Straus counterexamples" (README L202–203) |
| 22 | Global sign of the odd receiver: 𝔑 < −(125873811/262144)p⁸ for every integral witness at p ≡ 1 (mod 12) | SZ-20260921-005…007 | `es-turn07-global-receiver-determinant-20260921/core.tex` L1–488 (pinned `6bdfce2`; identical at tip) | proved; conditional "only in the literal sense" that a witness is given (README L357–359) |
| 23 | Sharp receiver growth; at most one inverse singular direction diverges | SZ-20260922-001…003 | `es-turn07-sharp-receiver-growth-20260921/core.tex` L75–636 (pinned `e713c34`; identical) | proved |
| 24 | Mod-24 mixed trace return; nine automatic rays | SZ-20260922-004…007 | `es-turn07-mod24-ray-trace-20260922/core.tex` L9–322 (pinned `e713c34`; **tip differs in 2 lines at L512–513**); `receiver_bridge.tex` L7–280 (identical) | proved |
| 25 | Complete mixed-return fibres; hard-middle spectra | SZ-20260922-008…010 | `es-turn07-fibres-middle-spectrum-20260922/core.tex` L74–641 (identical) | proved |
| 26 | Square-zero trace defects; Pell specialization; p = 67369 refutes nonincreasing repair | SZ-20260923-008…016 | `es-turn07-square-zero-pell-20260922/core.tex` L340–1046 (pinned `6c064a0`; **tip has 7 extra lines after L85 and L433**, so the pinned ranges shift) | proved; counterexample to a method, "not Erdős–Straus" (README L266) |
| 27 | Affine E/M channel operator; quotient-support criterion; upward return | SZ-20260923-001…007 | `es-turn07-mixed-order-upward-20260923/core.tex` L101–365, L611–786 (pinned `6125e74`; **tip has 2 extra lines after L531 and L566**) | proved |
| 28 | Signed opposition form; unique three-colour closure; residual-27 empty locus | SZ-20260923-017…024 | `es-third-defect-signed-pairing-20260923/core.tex` L45–729 (identical) | proved |

**F. Further incoming packages (10–16 Sep) not in the README "Start reading" list** (`research/incoming/…`). These were located, and their titles and zeta read-scopes read; the mathematics was not surveyed.

| Folder | Title (README line 1) | Zeta sources in `source_reading.json` / references |
|---|---|---|
| `2026-09-10-cyclic-support-jordan-koide` | One support, all cyclic degrees, and a reversible Koide–Jordan map | none |
| `split-box-energy-20260912` | Split-box collision forcing and exact integral return | none |
| `es-zero-cohomology-20260913` | Supported ES cohomology and original arithmetic weights | `formal/splitzero/DERIVED_MATHEMATICS.md` (@`7ea0a49`) |
| `es-splitzero-support-cohomology-20260914` | Actual SplitZero mixed-support cohomology (a three-support class at (p,a,R) = (241,118,231)) | `formal/splitzero/DERIVED_MATHEMATICS.md` §§1–4, 6; `…/20260914-original-kernel-web/08_ORIGINAL_MIXED_CONTROL.tex` (full); `…/13_ARITHMETIC_MIXED_TRANSFER.tex` L1–250, "particularly AMT1-10" |
| `es-mixed-support-20260914` | Ternary mixed-support ES certificate | `…/20260914-joint-gamma-schur/sources/` (`JOINT_SCHUR_EXACT_INTEGRATION.tex`) |
| `es-split-boundary-20260914` | Prime-power SplitZero comparison and canonical ES moment bounds (YM's "ES PR6" candidate, OV-21) | `workbenches/tau-split-integration/RESEARCH_NOTE.md`; `…/deligne-mixed-control/sources/SP.tex` |
| `es-discrete-positivity-20260914` | Discrete-spectrum positivity after uniform ES-array control | none |
| `es-split-scalar-arithmetic-20260915`, `es-padic-capacity-20260916`, `es-relative-boundary-20260916` | Split-zero inversion and exact arithmetic capacity control; explicit 2-adic capacity; relative boundary packets | one zeta repository record each (paths not extracted) |
| `es-cofactor-transport-20260915`, `es-factor-socle-20260915`, `es-actual-factor-socle`, `es-unit-boundary-20260916` | Cofactor transport and prime-power forcing; actual-factor socle certificates (two packages); unit-corrected relative boundary packets | none |

**Count.** 72 indexed supplement statements, R01–R10, X1–X7, the two 12 Sep packages, 28 headline continuations with 98 bulletin items, and 14 earlier incoming packages (table F, not surveyed). The status mix is uniform:
- every item is "proved" as a written argument, with finite replays;
- no Lean (for the current supplement), no independent review, novelty not assessed;
- several items are proved counterexamples to proposed *methods* (README items 2, 3, 21, 24, 26);
- one item is explicitly conditional on a zeta-programme theorem (item 20: NG20–NG21);
- one source-passage error is recorded (X5: 289³ ≡ 169, not −1, mod 840).

### 1c. What ES says it does not prove

- README L3: the project does not claim "a proof or counterexample to the conjecture".
- README L400–401: "None asserts the still-missing universal positivity theorem."
- RESEARCH_STATE L66–68: an empty shell or failed restricted search "is not an ES counterexample".
- RESEARCH_STATE L89: "No full fluid theorem or ES resolution follows merely from the cover."
- Supplement `README.md` L42–47: the results do not prove or disprove ES, RH or the Yang–Mills mass gap, and "do not independently validate" the NS construction.
- `ns_operator_bridge/ATTRIBUTION.md` L3: "It does not certify either complete fluid proof."
- RESULTS.md L31–35: no prover, no independent reviewer, no novelty search; "A proof of A ⇒ B is not a proof of B".
- Crosswalk bridge: "neither prove universal Erdős–Straus existence nor identify arithmetic roots" with zeta zeros (quoted in `21_` §4 Scope).
- `es_s6_counterfactual/README.md` L55–57: the six-sphere conclusion was "not independently audited".

### 1d. Audit coverage of ES (`21_`/`28_`/`34_`)

**Checked** (`21_`):
- the NS operator bridge (ES-07: `thm:ns-es-packet`, `cor:ns-es-cover-repair`, `thm:ns-sharp-denominator` = R07), found correct. The repair (T17) was confirmed. 21.2 is a negative result on unchanged finite torsion (13 against 4 at p = 13, a = 4; register negative result 42).
- the quartic identities and intrinsic prime (SZ-20260920-019) and det DP = −2 for the 4-D map P (Prop. 21.6; C1–C4).
- G(R) = R01/X3, on the zeta side, checked by hand (`21_` §6).

**Located only**: `sieve_character_cover.tex`, `reverse_proof_transport.tex`, the C123 preprint (read in three ranges on 23 Sep for FLIP_FABLE), and X6.

**Not audited**: all 28 structural continuations beyond SZ-019, R02–R06, R08–R10, X1–X2, X4–X7, ES-08, ES-09 and the 14 packages of table F.

`28_` and `34_` do not treat ES.

---

## 2. Yang–Mills workbench (YM)

### 2a. Location, own status, dates

**Repository.** KokunoYumeto/yang-mills-interacting-workbench @ `fa79faf` (21 Sep 2026).

**Top-level files.**
- `README.md`, `WORKBENCH.md`, `ATTEMPTS.md` (+ `research-attempts.json`), `ATTRIBUTION.md` (21 Sep), `RESEARCH_LOG.md`, `REVIEW_GUIDE.md`, `workbench.json`.
- The YM tree is `yang-mills/`:
  - `README.md`, `AI_READING_INDEX.md`;
  - `sources/` (the 9 Sep foundation sources);
  - `consolidation/20260916`, `…/20260917`, `…/20260919`, `…/20260921`, `…/20260921-fifth-reference`;
  - `continuations/`;
  - `research-control/` (14 Sep).
- The same repository holds `navier-stokes/` (§3) and `s6/` (§4).

**Zenodo editions.**
- 9 Sep foundation: 10.5281/zenodo.22678364.
- 21 Sep heat/volume: 22803564.
- 21 Sep fifth-reference: 22883643.
- Historical: 22667605.

**Own status.**
- README L35: "They do not constitute a claimed solution" of the interacting 4-D mass gap. The same sentence disclaims "independent certification of every global step" in the S⁶ or NS constructions.
- WORKBENCH L21: "The full interacting four-dimensional continuum/mass-gap question remains unresolved".
- `research-control/state.json` has `"continuum_gap_proved": false` (14 Sep).

### 2b. Main results

Common WB status:
- written analytic arguments plus finite exact checks;
- "No Lean or independent external analytical certification is claimed" (fifth-reference README L117);
- 17 Sep: the analytic passage "reviewed separately", with "No missing implication was found" within finite-regulator scope; "not Lean-formalized" (`consolidation/20260917/VALIDATION.md` L19).

| ID | Statement (paraphrase) | Locator | WB label / proof in repo | Audit |
|---|---|---|---|---|
| YM-01 | Kogut–Susskind SU(2) Hamiltonian on the open box {−L,…,L}³, L ≥ 2, κ = 2g²/a, ξ = 1/(4g⁴). Complete fifth-order vacuum source, with a convergent correction including the endpoint (α₅ ≈ 0.0184249535761176167). **Gap bound Δ_L ≥ κ d₅(ξ) for all L ≥ 2, a > 0, 0 < ξ ≤ α₅**, i.e. g² ≥ 1/(2√α₅) ≈ 3.6835519839857273; e.g. g² ≥ 4 gives Δ_L > 1.9068κ | `consolidation/20260921-fifth-reference/README.md` L9–68; proof `…/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md` F35–F42 (boxed F37 near L380) | proved (written) + F (51 named checks, 11 false-formula controls); producer/dual auditor not rerun (README L117) | — |
| YM-02 | Heat remainder bound on the circle \|ξ\| < 1/55; full-complement relaxation 1999/2000 ≤ … for g² ≥ 13, and 24999/25000 for g² ≥ 16 | same README L70–111; `HEAT_AND_COMPLEMENT.md` H1–H34 | proved (written) + F | — |
| YM-03 | 21 Sep heat/volume: fourth-order heat correlations; box-independent all-time row estimate (source radius 3/256); fixed-spacing spatial-volume limit; full-complement energy retained above 999/1000 at g² ≥ 16 | `consolidation/20260921/README.md` (L51: "not a limit as the lattice spacing tends to zero"); `yang-mills/README.md` L22; five proof manuscripts in `consolidation/20260921/package/…` | proved (written) + F | — |
| YM-04 | 19 Sep: sixth source, eighth energy, finite 240-face plaquette response, minimum-energy support maps | `consolidation/20260919/` | written notes; "the new spatial tables and final cumulative execution package were not supplied" (WORKBENCH L13) | — |
| YM-05 | 17 Sep: fourth-order vacuum source in two presentations, equal as polynomials (78 representatives; 8,621 anchored multisets); sixth-order energy with cube contribution −83/1944; **Δ_L > 1.6584κ for g² ≥ 15/4** | `consolidation/20260917/reader/yang_mills_quartic_cube_reader.tex` L533–534; `VALIDATION.md` L9–19 | proved (written) + F; "retains its existing analytical-review qualification", and the 21 Sep proof "does not recertify the earlier stronger interval" (`yang-mills/README.md` L29) | — |
| YM-06 | 14–16 Sep: actual-loop, uniform-gap, gauge-native, local-fibre, cubic-source and linearized-return arguments | `consolidation/20260916/` (`CURRENT_RESEARCH.md`, 297-page reader TeX) | written; "bounded proof reviews" (yang-mills/README L37) | — (located) |
| YM-07 | 9 Sep foundations (five readers). Quantum blocking gives volume-independent bounds for selected Wilson-loop channels. The non-Abelian cubic vertex is nonzero on L = 2. The tensor-band map is onto at a fixed box and small coupling. For volume-uniform estimates, the "certified endpoint diverges along the logarithmic path". The spatial limit contains §26.13 (oscillator path rates) and **§27, exact collapse of the finite-box weak-coupling disk at fixed coupling** (a negative result) | `yang-mills/sources/ym_*_astra_20260908/…`; `spatial_continuum.md` §27 at L8275; `check_fixed_coupling_analytic_disk_obstruction.py`; ATTEMPTS L119–155 | written; the checkers are "finite … diagnostics within their stated scope" (yang-mills/README L65) | — |
| YM-08 | **Jacobian → YM (material tensor).** Theorem 13.1 decomposes the spectral measure of S ↦ Ξ_{f_S} into three cubic-symmetry sectors, with weights (tr S)²/9, ½Σ(S_ii − tr S/3)², Σ_{i<j}S_ij² | `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md` Thm 13.1 L216–231 | proved (written) | endpoint coefficients 113569/36864, 100825/12288, 531/512 recomputed **C** (`28_` J6); lattice parts not re-derived |
| YM-09 | **Theorem 14.2.** Physical vectors w_j orthogonal to the vacuum, with j·Q_j → 100√2π, along L_j = j², a_j = 1/(100j), g_j < 1/j | `FABEL_LOW_MODE_TRANSFER.md` Thm 14.2 L335–363 | proved (written); "The common interacting continuum state/observable identification remains unresolved" (FABEL_CORRECTIONS L87) | **Cc** (`34_`): the algebra is correct; the proof is a valid diagonal argument conditional on fixed-box weak-coupling limits that are only sketched; Q_j is the free two-gluon threshold (Q_j·ℓ_j → 2√2π); it "does not bear on the mass gap"; register negative result 57, bridge 38 |
| YM-10 | **NS → YM.** The NS velocity becomes the reducible SU(2) connection A_i = λu_iT; curvature masses; a zero-quotient diagonal (263)–(265), with couplings g_{j_n} → 0 | `…/released_profile_measures_addendum.tex` L8 (imports (250)), L168–213 | "a rigorous weak-coupling counterexample candidate, not a completed Millennium disproof" (L195) | **Cc** (`21_` §2: identity and constants checked, B1–B4; conditional on the NS rate bounds (250) and a dissipation bound, which were not checked; scope limit 21.4) |
| YM-11 | **S⁶ → YM.** The magnetic background is built from the imaginary period block of Π(z); magnetic translation; Gauss projection | `yang-mills/sources/ym_gap_primary_20260908/magnetic_translation_true_vacuum.md` §1 (L1–10: "not an input" is the S⁶ identification), §§2–9; `retained_cusp_nonlinear_bridge.md` §1; `ym_volume_uniform…/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md` §19 | written finite-regulator calculation | **C**: `28_` Lemma 28.2, only D = Lq + 6m² enters on the non-wrapping patch (S1; register S53) |
| YM-12 | **zeta → YM (heat).** The HM6–HM14 and HM19–HM24 Gram sandwich from zeta, instantiated with the YM heat semigroup: (1−ε)²Φ*Φ ⪯ Φ_T*Φ_T ⪯ Φ*Φ with a₀ = 27κ/10 (T1–T3); finite heat horizon (T4); mixed terms (T5); **T7 receiving instance of zeta `INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex`**; T8 | `consolidation/20260921/package/workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md` (also a copy under `…-fifth-reference/package/…`) | proved (written) + F | T1–T3 **C** (`21_` §3, Lemma 21.5; E0–E2; register S41; `21_` found δ ≤ 1 necessary, and the source assumes δ < 1); T4–T8 — |
| YM-13 | **research-control (14 Sep).** Local score estimate L8, Hamiltonian coupling L14, minimum-energy sections L17–23, tower composition L25. Zeta AMT7–10 is "instantiated" as L25 and zeta OK1–2 (PR32) as L22 | `yang-mills/research-control/RESEARCH_NOTE.md` L191, L219, L245–247; `STATUS.md` L15; `state.json` `sources`, `transfers` | written + F (56 checks, 17 negative controls); fixtures "are not interacting Yang–Mills vacuum integrals" (STATUS L15) | — |

Status mix:
- all items are written proofs with finite checks, no Lean and no independent external certification;
- YM-04 has unreplayed components;
- YM-05 carries a stated review qualification;
- YM-09 and YM-10 are explicitly weak-coupling or finite-regulator results; YM-10 is labelled "candidate";
- YM-07 §27 is a negative result.

### 2c. What YM says it does not prove

- README L21: "not a claimed solution of the four-dimensional continuum mass-gap problem".
- `yang-mills/README.md` L29: neither edition "establishes a four-dimensional continuum field or a finite positive continuum mass"; L59: "do not establish or refute" the continuum mass gap.
- Fifth-reference README L125: on the standing path a_n = a₀2⁻ⁿ the path "eventually leaves both" domains.
- `FABEL_TENSOR_TRANSFER.md` L7: "No equality between fluid evolution and quantum Hamiltonian evolution" (as quoted in `28_`).
- FABEL_CORRECTIONS L66: "No counterexample or all-theory exclusion follows."
- Addendum L195: "does not yet prove failure" of the mass-gap assertion.
- `RH_HEAT_TRANSFER.md` L31–32: an arithmetic-to-gauge map "is not asserted"; T6 L241–245: tests do not "establish the four-dimensional continuum gap".
- ATTRIBUTION L19: the Jacobian map and its mechanism "are source results, not discoveries of the present workbench".

### 2d. Audit coverage of YM

**Checked:**
- YM-08: endpoint coefficients (`28_` §2);
- YM-09: proof of Thm 14.2 (`34_`);
- YM-10 (`21_` §2);
- YM-11 (`28_` §3);
- YM-12 T1–T3 (`21_` §3).

**Not audited**: the programme's main strong-coupling results YM-01–YM-07, research-control YM-13, and `RH_HEAT_TRANSFER` T4–T8.

Note also that `34_` §5 could not find the three source files credited for the fixed-box limits.

---

## 3. Navier–Stokes material (NS)

### 3a. Location, own status, dates

**YM repository.**
- `navier-stokes/`: `README.md`, `RESEARCH_STATE.md` (9 Sep, with addenda of 19 and 20 Sep), `research-state.json`, `SOURCE_READING_20260920.json`, `navier_stokes_checks.json`, `navier_stokes_primary_manifest.json`, `navier_stokes_source_bundle.zip` (120 members), `navier_stokes_workbench.tex` and `…_208p.pdf`.
- `navier-stokes/sources/openai-source-faithful-20260920/`: a complete **independent LaTeX transcription** of the OpenAI manuscript, preserved from KokunoYumeto/openai-navier-stokes-latex@`5e162f34`; Zenodo 22852310.
- `navier-stokes/continuations/20260919-vacuum-hydrodynamics/`.
- Root duplicates `navier_stokes_*`: the two `.tex` blobs differ only in CRLF line endings (checked); the PDFs are identical.

**Elsewhere.**
- ES `…/ns_operator_bridge/ATTRIBUTION.md` (8 Sep): source attribution for the manuscript and the companion Alpöge–Buckmaster papers.
- Zeta:
  - `sidebar/fluid/` (137 files): the fluid research notebook, including "concrete maps from the earlier polynomial, S6 and arithmetic work" (README L3). Its `reader.pdf` is **not** the same file as YM's 208-page PDF (blob ids differ).
  - `satellites/29g…29s_ns_*.tex`: 12 NS→arithmetic chapters.
  - `ATTEMPTS.md` L11, L25–35.

**Zenodo.** Corrected 208-page edition 10.5281/zenodo.22678406 (the earlier 162-page edition is 22667379); transcription 22852310.

**Own status.**
- `navier-stokes/README.md` L31: "complete independent analytic and Lean validation remains unfinished"; "not a claim of discovery".
- `research-state.json`: `complete_independent_analytical_validation: false`; `lean_kernel_certificate: false`; `current_formal_run_status: stopped_without_endpoint_or_Comparator_certificate`.

### 3b. Main results

| ID | Statement (paraphrase) | Locator | WB label | Audit |
|---|---|---|---|---|
| NS-00 (imported source claim) | OpenAI Thm 1.1: for every ν > 0 there are a compactly supported smooth force and zero initial velocity giving a smooth solution on [0,1) with bounded energy and lim sup_{t↑1}‖u(t)‖_∞ = ∞; Cor. 10.6 gives the same on 𝕋³ | ES `ns_operator_bridge/ATTRIBUTION.md` L18–46; transcription `…/upstream/reconstruction/sections/pp001-006.tex` | "recorded manuscript claims; this attribution audit has not supplied their complete independent proofs" (ES ATTRIBUTION L46) | not audited anywhere |
| NS-01 | Reconstruction of the source's stage sequence: profiles (§4, App. B), base/heat (§5, App. A), oscillations (§§6–7), mean corrections (§8), correction cycle (§9), endpoint (§10); 13 complete component bodies | `navier_stokes_workbench.tex` / 208p PDF; ZIP bodies listed in `RESEARCH_STATE.md` L21–35 | "reconstruction"; "does not independently verify the assembled infinite construction" (YM ATTEMPTS L25) | — |
| NS-02 | Corrections: restores the actual-shear remainder and positive-production bounds, the radial transport factors and the plane-coordinate inverse | `RESEARCH_STATE.md` L37–43 | correction in published reader; "do not certify the manuscript's full cycle or endpoint" (ATTEMPTS L33) | — |
| NS-03 | 166-page source-faithful LaTeX transcription (166 page checks, 6,175 formula occurrences) | `sources/openai-source-faithful-20260920/` README L24–26; `SOURCE_READING_20260920.json` L38–55 | transcription checks only; `independent_mathematical_proof_verification: false` | — |
| NS-04 | Vacuum hydrodynamics (19 Sep), four sub-results. (a) Exact nonlinear Einstein constraint data from any compact divergence-free velocity, with a left inverse 𝒟∘ℰ = id (marked data). (b) Homogeneous Kasner realization, a bijection onto P_w < 1/4. (c) Linear Rindler shear response and hydrodynamic series, symbolic through q¹⁰; a pole-cluster collision near q_c ≈ 0.7785 that is **numerical, not interval certified**. (d) A positive slab-stress regularity theorem for a *modified* equation | `continuations/20260919-vacuum-hydrodynamics/README.md` L23–84, L86–124, L126–156; `SLAB_COMPARATORS.md`; `manuscripts/IDENTITY_AND_COMPLETION.md`, `RESEARCH.md` | proved (a, b, d) with finite checks; (c) partly numerical; historical suites "were not replayed" (L176–178) | — |
| NS-05 | Audits of the 40-page `fluid_blowup_reconstruction.zip` report: local proof fragments; the arithmetic heat map has no nonzero solenoidal field, so a solenoidal isometry was built ("six-channel image has zero averaged swirl") | YM `ATTEMPTS.md` L47–75; bodies inside `navier_stokes_source_bundle.zip` | "neither certifies the report nor proves a classical Navier–Stokes singularity" (L57) | — |
| NS-06 | Coupled viscous Boussinesq stages: first two targets, second return, and third growth/transition/steering completed; finite pulse bridge to the source's profile stages | ATTEMPTS L79–107 | "The third return … remain unproved" (L89); "no uniform endpoint estimate transfers" (L97) | — |

### 3c. What NS says it does not prove

- `RESEARCH_STATE.md` L13: the S⁶-, algebraic- and heat-transfers' "proposed implications are not certified by this reader".
- L47: unfinished items include "imported profile and admissible-stress existence", all-stage realization and convergence, and the formal endpoint.
- Vacuum-hydro README L84: injectivity only for marked data.
- L122–124: an NS-time Einstein conjugacy "would need a further evolution map"; the blowup estimates "remain imported hypotheses".
- L156: "not the nonlinear NS velocity norm".
- L170: no ER = EPR, NS–Einstein conjugacy, blowup cancellation "or an S6 implication".
- Transcription README L7: "not an official OpenAI LaTeX release".

### 3d. Audit coverage of NS

- `21_` §1: the NS→ES operator edge; no NS theorem is used by ES.
- `21_` §2: the NS→YM edge (conditional on the NS rate bound (250), unverified).
- `21_` §7 Prop. 21.7: a claude-ab Mellin reading of the terminal singularity; labelled a reading.
- `28_` §4: the NS research state read in full; "no certified NS-side transfer to state as a morphism"; a search of the NS TeX finds no "Fabel".
- **Not audited**: NS-00 to NS-06, zeta's NS satellites 29g–29s, and zeta `sidebar/fluid`.

---

## 4. S⁶ and Alpöge's construction

### 4a. Location, own status, dates

**YM `s6/`** (6 Sep checkpoint, packaged 9 Sep, attribution 21 Sep):
- `26_s6_key_advances_frozen_2026-09-06.pdf` and `27_…tex` (a 5-page reader, 325 lines of TeX);
- `README.md`, `S6_FROZEN_PROJECT_GUIDE_2026-09-09.md`, `ATTEMPTS.md`, the package manifest.

**The complete project is not in git.**
- The 1,079-file, 174 MB archive is on Zenodo 10.5281/zenodo.22678442 (family 22235523, v1.2 22346462).
- Its 782-page workbench and 138-page higher-rung paper are cited by page (s6/README L9; guide L7–9).

**Uses elsewhere.**
- YM: `magnetic_translation_true_vacuum.md`, `retained_cusp_nonlinear_bridge.md`, `VOLUME_UNIFORM…` §19 (ATTRIBUTION L39).
- ES: `research/continuation-2026-09-12/received/es_s6_counterfactual/` (ES-09).
- Zeta:
  - `sidebar/fluid/tex/s6_bridge.tex` (8 Sep; "Exact bridges from the retained Fable polynomial and the S6 cusp");
  - `sidebar/fluid/tex/s6_dynamics_bridge.tex` (a map to classical positive-viscosity NS on 𝕋³ whose image consists of global smooth solutions; L1–14);
  - `sidebar/heat/tex/s6_three_point_quotient.tex` (Prop. "Typed quotient, kernel and full monodromy intertwining", L133).

**Attribution in the repositories.**
- YM `ATTRIBUTION.md` L31: "circulated by Levent Alpöge and produced with Claude" (`alpo.ge/s6.pdf`); Engel's exposition credited separately (L37).
- The frozen reader L27, YM `ATTEMPTS.md` L209 and `research-attempts.json` L736 say "circulated by Levent Alpöge with Fable" (§10 D2).
- ATTRIBUTION L41: the S⁶ construction "is not the July Jacobian counterexample".

**Own status.**
- s6/README L11: "does not independently certify a global complex structure on S6", nor a CDP20 counterexample, nor a YM mass-gap theorem.
- The key-advances TeX L315–320 says the same, and "not independent expert adjudication or Lean formalization".

### 4b. Main results

The frozen 6 Sep reader's five advances. WB (s6/ATTEMPTS L31–33): results are those "recorded in the frozen source", and the documentation pass "did not newly reprove these theorems".

| ID | Statement (paraphrase) | Locator (reader TeX / full proof) | Proof in git | Audit |
|---|---|---|---|---|
| S6-1 | ω_X ≅ 𝒪_X(−2S₂); the anticanonical ring is ℂ[U,V] with deg U = 1, deg V = 2; its degree-2 sections recover the fibration to ℙ¹ | `27_…tex` §1 L33–74; workbench Thm 53.17, pp. 699–700; `analytic_canonical_ring.tex` CR1–CR5 | N (in the Zenodo archive) | — |
| S6-2 | The period constant gives a nonzero deformation: KS_{X_{c*}}(∂_c) ≠ 0 | §2 L77–135; Thm 53.18, pp. 701–705; PD1–PD18 | N | — |
| S6-3 | Finite fillings: product covers of degrees 9 and 8; the full central attachment kernel is ≅ ℤ; smooth normal-line trivialization | §3 L138–195; Thms 53.4, 53.6, 53.7, 53.9, pp. 684–690; FF1–FF46 | N | — |
| S6-4 | Niemeier–Leech transport for R = A₅^{⊥4} ⊥ D₄ with [N:R] = 72: value-group inclusions diag(1,4,1) and diag(1,1,3), total quotient ℤ/12; Albert determinant λ³ − λ(y,y) + 2F(y) | §4 L198–262; higher-rung paper §§9–11, pp. 106–125 (`es_niemeier_cubic_arithmetic.tex`, …) | N | — |
| S6-5 | Literal common lattice with Wilson's Leech: {√2(a,a,a) : a ∈ D₄}, Gram 6G_{D₄}, det 5184, min 12; the cubic generates 4√2ℤ but does not attain 12√2 | §5 L265–300; higher-rung §12, pp. 125–135 (`es_niemeier_wilson_cyclic.tex`) | P (the TeX gives the short mod-3 argument, L289–292) | — |

Uses of S⁶ data elsewhere:
- **YM-11**: only D enters (`28_` Lemma 28.2).
- **ES-09**: affine torsion covers from the S⁶ monodromy matrices.
- **Zeta sidebar** bridges into NS (§3a). `s6_bridge.tex` L7–21 notes that the source's own status file calls all six topology bridges "closed". It checks only "the concrete polynomial, metric, differential-operator and Fourier calculations".

### 4c. What the S⁶ material says it does not prove

- s6/README L11 and guide L15: no certification of the global complex structure, no CDP20 counterexample, no mass-gap conclusion.
- ATTEMPTS limits:
  - L51–52: "do not, by themselves, establish the complete global identification";
  - L92–93: no pairwise non-isomorphism is claimed;
  - L112–115: value groups are "not an assertion that the original lattices are equal";
  - L142–144: "a rank-four intersection".
- YM `magnetic_translation_true_vacuum.md` L8–10: the S⁶ identification "is not an input".
- ES `es_s6_counterfactual/README.md` L44: "The rank-four period lattice is 𝕃, not the rank-24 Leech lattice".

### 4d. Audit coverage of S⁶

- `21_` §5: the S⁶→YM and S⁶/heat→NS edges located only.
- `28_` §3: Lemma 28.2 verified (S1).
- **Not audited**: S6-1 to S6-5, ES-09, and the zeta sidebar S⁶ bridges.
- External (web, §0.4): Engel's 13 Sep exposition states a self-contained proof that Y is a compact complex manifold diffeomorphic to S⁶. That is outside the repositories and was not checked here.

---

## 5. Jacobian-conjecture counterexample material

### 5a. Location, own status, dates

**The object.** F(x,y,w) = ((1+xy)³w + y²(1+xy)(4+3xy), y + 3x(1+xy)²w + 3xy²(4+3xy), 2x − 3x²y − x³w). det DF = −2, and three points collide over (−1/4,0,0) (YM `ATTRIBUTION.md` L9–19).

**Provenance.**
- Announcement: Levent Alpöge, 20 Jul 2026, crediting Akhil (question) and Fable (work) (ATTRIBUTION L9). Web-verifiable only through Speyer's and Tao's posts, since X is robots-disallowed.
- The zeta README L295 adds: "The ES source identifies Akhil Mathew and Claude Fable 5."
- Tao (21 Jul) and Speyer (20 Jul) are expositions.
- Poplett's "Local Fidelity, Global Alias" (24 Jul) is cited by zeta as a "Locally retained TeX edition" (`satellites/90_references.tex` L657–661).

**Where it is used.**
- **YM**: `ATTRIBUTION.md` (21 Sep), plus the Fabel files in `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/`:
  - `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md` (§§1–5);
  - `FABEL_TENSOR_TRANSFER.md` (Thm 13.1);
  - `FABEL_LOW_MODE_TRANSFER.md` (Thms 14.1, 14.2);
  - `FABEL_CORRECTIONS_20260908.md`;
  - `extensive_quantum_blocking.md` and `fabel_propagation_addendum.tex`.
- **Zeta** (frozen 411-page reader, Zenodo 22678086):
  - `satellites/23_source_mechanism_transfer.tex` (`prop:retained-fibre` L43–44);
  - `26_incompressible_fibre_heat.tex`, `27_material_arithmetic_generator.tex`, `29_material_endpoint_jets.tex`;
  - `ATTEMPTS.md` L9, L17–19;
  - continuations `…/20260921-actual-xi-uniform/ALPOGE_FABLE_ROLE.tex` (ALF1–ALF3) and `FABLE_TO_ORIGINAL_CONDUCTOR.tex` (many copies);
  - `sidebar/fluid/tex/s6_bridge.tex` L31–46, which takes F from the S⁶ archive's `comparative_context/prior_fable_context.tex`, citing "a pinned JGPTech certificate".
- **ES (a different, 4-D map P)**:
  - ES 488-page reader v69, `thm:explicit-four-time-Jacobian-collision`: P : ℂ⁴ → ℂ⁴, det DP = −2, four colliding points q_M, q_N, q_T, q_E. It is vendored in zeta at `…/20260921-actual-xi-uniform/source_dependencies/ES_READER_V69.tex` L19484ff; in the ES git tree the source is only inside `01_…zip`.
  - Crosswalk EZ4 (`ES_FABLE_ZETA_CROSSWALK.tex` L121–133).
  - `upstream/FABLE_TO_ORIGINAL_CONDUCTOR.tex`: FC/GF/SE/SM equations; generic 8-point fibres; monodromy of order 48.
- **Audit side (claude-ab)**: the FLIP_FABLE note (zeta branch `claude/orientation-20260922`, not re-read here), `ERRATUM_FLIP_FABLE_ADDENDUM_4.md`, and `28_` Lemma 28.1 (register S52).

**Own status.**
- YM ATTRIBUTION L19: "source results, not discoveries of the present workbench"; L27: later constructions are not attributed to Alpöge.
- Zeta `ALPOGE_FABLE_ROLE.tex` L10–11: "not results of this Split-Zero calculation".

### 5b. Main results that use F or P

| ID | Statement (paraphrase) | Locator | WB label | Audit |
|---|---|---|---|---|
| JC-0 (source) | F is Keller (det DF = −2) and not injective | YM ATTRIBUTION L19; Tao; Speyer | source result | det and collision **C** (`21_` check F; `28_` J1) |
| JC-1 | YM coordinate audit: the "retained Navier–Stokes orbit" γ(τ) = (z⁻¹, −3z/2, 13z²/2) with z = √(1−8τ); Lagrangian deformation; loss of uniform ellipticity at the endpoint | `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md` §§2–3 | written; the endpoint is "not a finite-time singularity" (quoted in `28_` §1) | **C** (`28_` J4–J5, J5b) |
| JC-2 | YM Thm 13.1 and Thm 14.2 (= YM-08, YM-09) | §2 above | §2 above | **C** / **Cc** (`28_`, `34_`) |
| JC-3 | Zeta: exact inverse-fibre chart of F; incompressible trajectories; an "escaping trajectory in the retained pullback metric"; heat on the two-sheet module | zeta `satellites/23…` (`prop:retained-fibre` L43; heat proposition L561); `26…`; zeta ATTEMPTS L17–19 | written proofs; "That metric is incomplete"; "did not itself produce" an NS singularity or off-critical zero (ATTEMPTS L19) | — |
| JC-4 | ES/zeta 4-D map P. Complete inverse, image complement and nonproper locus (GF1–GF18); 8 signed states; conductor intertwining T_A Φ = Ψ and T_A P_𝒰 = P_𝒲 T_A (ALF1–ALF3) | ES crosswalk EZ4–EZ36; `upstream/FABLE_TO_ORIGINAL_CONDUCTOR.tex` (= zeta `20260920-fable-signed-states/…`, byte-identical); zeta `ALPOGE_FABLE_ROLE.tex` L19–60 | proved (written) + F | det DP = −2 **C** (`21_` C4); the rest — |
| JC-5 (audit-side, not a workbench result) | Keller maps give incompressible polynomial flows; the γ-curve escapes at τ = 1/8; this is impossible for automorphisms | `28_` Lemma 28.1; register S52 | claude-ab, proved and refereed | n/a |

### 5c. What the material says it does not prove

- `FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md` §4: a complex Fabel tangent vector has "no map into this real gauge-invariant Hilbert space" without further specification (quoted in `28_` §2).
- FABEL_CORRECTIONS item 6: the NS manuscript must not be "confused with the stationary Fabel polynomial" (as quoted in `28_` §1).
- Zeta `FABLE_TO_ORIGINAL_CONDUCTOR.tex` (fable-conductor copy) L22–26: conclusions "neither assert RH nor classify all nonlinear maps".
- ES crosswalk: it identifies no ES root with a zeta zero (`README.md` of the bridge, L46).

### 5d. Audit coverage

- `21_` §4: F's determinant, collision and real symmetry; P's determinant.
- `28_` §§1–2: the flow lemma and the tensor chain.
- `34_`: Theorem 14.2.
- **Not audited**: zeta satellites 23/26/27/29, `ALPOGE_FABLE_ROLE.tex` and the FC/GF equations beyond det DP.

---

## 6. Erdős Problem 817 workbench

### 6a. Location, own status, dates

**Repository.** KokunoYumeto/erdos-problem-817-workbench @ `dbd0a93` (16 Sep 2026).

**Files.**
- `README.md`, `STATUS.md` (13 Sep), `problem/statement.md`, `paper/ep817_k4_rate.tex` (+ `output/pdf/ep817_k4_rate.pdf`);
- `formal/lean/ErdosProblem817/{Core,Extended}.lean`, `certificates/`, `corpus/claims.ndjson` (11 claims);
- `notes/`, `research/*` (13 folders);
- `editions/cumulative_20260916/` (29-note corrected collection; `NOTE_INDEX.md`, `PUBLICATION_NOTES.md`);
- `integration/20260916/`;
- `interfaces/zeta/workbenches/ep817-*` (11 folders). They hold 10 SplitZero interface notes: nine `splitzero-receiving-map.md` and one `splitzero-return.md`. Nine are chapters of the collection (Nos. 10, 13, 15, 17, 19, 21, 25, 27, 29); the all-block-image receiving map is not. The folders also carry mirrored copies of the arithmetic notes.
- The original delivery is a GitHub release asset (`cumulative-2026-09-16`), not in the tree.

**Attribution.**
- The k = 4 proof is from an anonymous or deleted Reddit contributor (README L38–54).
- The Lean upper-bound extension is by sneed-and-feed (PR #1, commit `155523c`; STATUS L36–54).
- The continuation is by "The Clankers".

**Own status.**
- README L53–54: the work concerns the k = 4 exponential-rate subproblem, "not a solution of every part of Erdős Problem 817".
- STATUS L27: novelty and priority "not claimed".

### 6b. Main results

| ID | Statement (paraphrase) | Locator | WB label | Proof / checks | Audit |
|---|---|---|---|---|---|
| EP-01 | For all n ≥ 1, (19^{n/3} − 1)/(2n) ≤ g₄(n) ≤ 8·19^{⌈n/3⌉−1}; hence lim g₄(n)^{1/n} = 19^{1/3} | `paper/ep817_k4_rate.tex` `thm:main`; `corpus/claims.ndjson` MC-ERDOS-817-THM-001 | "proved-in-written-note" | written proof "complete, independently reconstructed" (STATUS L21) + F | — |
| EP-02 | Lemmas in the written proof and the Lean coverage | see the list below this table | proved-written-and-lean for four items; written only for the remaining lemmas and the ternary count | L: Core + Extended, 44 theorem axiom checks with `propext`, `Classical.choice`, `Quot.sound` (STATUS L56–63); Lean does **not** cover the lower bound, the block decomposition, the ternary product or the real squeeze (STATUS L24; README L116–117) | — |
| EP-03 | Ternary-variance refinement: g₄(n) ≥ ⌈√(19(M_n² − 1)/(192n))⌉, an order-√n gain in the lower bound | `notes/ternary-variance-lower-bound.md` L30–56 | "ordinary mathematical derivation"; "**Not Lean-checked**" (L5–6) | written + F | — |
| EP-04 | General k. Thm 1: Λ_k = lim g_k(n)^{1/n} exists and equals an infimum over finite modular certificates. Thm 2: all-length decidability by a finite carry graph. Thm 3: Λ₅ ≤ 97^{1/6} and Λ₆ ≤ 93^{1/6}, improving Korsky's v1 | `notes/general-k-capacity.md` L26–71 (also `research/general_k/notes/general-k-carry-capacity.md`) | "ordinary mathematical proofs"; "no new Lean" (L6) | written + F | — |
| EP-05 | Graphical obstructions: g₆(n) ≤ 257·1651^{⌈n/10⌉−1}, improving 93^{1/6} since 1651³ < 93⁵ | `research/graphical_obstructions/notes/graphical-obstructions.md` L1–45 (Thms 3.1, 5.2, 5.3) | "independent mathematical review pending" (L3) | written + F | — |
| EP-06 | Outer control (k = 5, 6): exact fixed-block optima for n ≤ 5 (e.g. 65^{1/5} for k = 5 and 47^{1/5} for k = 6 at n = 5) | `research/splitzero_outer/README.md` L9–19; `notes/outer-support-control.md` | ordinary proofs + certificates (47,259 rank-five blocks audited); "No new Lean" (L49) | written + F | — |
| EP-07 | Cone dual C1–C5 (9 facets, 10 extremal rays; the observation does not decide admissibility, C5) | `research/cone_dual/notes/cone-and-dual.md` L15–60 | ordinary proofs + certificates | written + F | — |
| EP-08 | Finite-period approximation: 0 ≤ log U_m − log δ_q(D) ≤ log(q−1)/(m·n_min) (FP1, with FP2 and FP3). The radix-ten minima are a_{3r} = 893^r, etc.; the infinite rate is 893^{1/6} (local flow, attained by AAB) | `research/finite_period/notes/finite-period-control.md` L106–311; README L9–25; `integration/20260916/README.md` L9–19 | ordinary proofs; "no new Lean certification" (README L27) | written + F (producer + independent auditor) | — |
| EP-09 | Recurrence control (R1–R5, including a seven-term obstruction); canonical isolation (CI1–CI4); arity boundary; all-block image (Thms A–C); seven-observable capacity (Thms 1–4; the correction L > 3Q); supported defects; defect closure; variable blocks | `research/*/notes/*.md`; `NOTE_INDEX.md` L9–37 | ordinary proofs + finite checks; one published correction (seven-observable L > 3Q replaces an older L > 2Q; `PUBLICATION_NOTES.md` L7) | written + F | — |
| EP-10 | **SplitZero receiving maps** (10 interface notes; 9 are chapters): 817 finite constructions restated in the zeta programme's supported-quotient and receiving-kernel framework, e.g. exact kernels and the cocycle κ(u,v)κ(uv,w) = κ(v,w)κ(u,vw) | `interfaces/zeta/workbenches/ep817-*/notes/splitzero-receiving-map.md` (finite period: L1–120) | written; "does not claim a new result about the Riemann zeta function" (`PUBLICATION_NOTES.md` L27) | written | — |

The EP-02 lemmas and their Lean coverage (corpus IDs):
- LEM-RELATION-SPLIT, MOD19-KERNEL and DIGIT-RIGIDITY: Lean-checked (`Core.lean`).
- THM-LIFT and THM-FINITE-UPPER: Lean-checked (`Extended.lean` `erdos_problem_817_upper_bound`, independently).
- LEM-BLOCKS and SHORT-KERNEL: written proof only.
- EQ-TERNARY-COUNT: written proof with bounded checks.
- COR-FINITE-LOWER: sharpened lower bound by The Clankers; written.

Count and status mix:
- one main theorem, proved in writing, with its upper-bound half Lean-checked;
- 11 corpus claims: 5 written-and-Lean, 4 written, 1 written plus bounded checks, 1 nonclaim;
- 29 notes of continuation results, all "ordinary proofs + exact finite certificates, submitted for independent review", with no new Lean.

The unrestricted Λ_k for general k is open (general-k L71).

### 6c. What 817 says it does not prove

- README L53–54: it does not settle "every part of Erdős Problem 817" and is "not an Erdős–Straus artifact".
- STATUS L29–32: it does not address all of Problem 817 or determine every finite value.
- `corpus/claims.ndjson` MC-ERDOS-817-NONCLAIM-001.
- README L139–141: "makes no novelty or priority claim".
- The finite-period theorem "is not a claim that the original source quotients become constant" (receiving note L95–96).
- The zeta-side intake (below): "no analytic allocation coefficient or statement about zeta zeros".

### 6d. Audit coverage

None. 817 is not treated in `21_`, `28_`, `34_` or the register (only `BRIEFING_FOR_LOCAL_SESSION.md` L88 names the repository).

---

## 7. Collatz material

### 7a. Where it is (searched: file names on all fetched branches of the four repositories; contents at `origin/main` for "collatz", "3x+1", "3n+1", "syracuse", "hailstone", "kakutani")

No file name in any of the four repositories contains a Collatz term. Content hits:

| Repository | Material | Locator |
|---|---|---|
| ES | R05, the odd-step Collatz identity | `RESULTS.md` L17; `results/PROOF_NOTES.md` L43–53; `results/records.json` (R05) |
| ES | X4, support-aware affine homogenization (a "Collatz F-series" construction) | `results/integration-2026-09-10/ARGUMENTS.md` L73–87; `CROSS_WORKBENCH_COMPARISON.md` L27–29; `crossworkbench.json` X4 (`exact_public_counterpart_unresolved`) |
| ES | Handoff and index | `RESEARCH_DIRECTIONS.md` §7 L55–61; `INTEGRATION_OPPORTUNITIES.md` I13 L93–97; `results/SOURCES.md` L33–35 (drafts CN-6d25f4720ad4a3 `collatz_unconditional_note.tex` and CN-1cfd281002ed14 `odd_step_collatz_orbit_packets_note.tex`: "Indexed only" / "not fully reviewed"; private corpus) |
| YM | Regression fixture from the external Collatz workbench: X_v(q) − X_u(q) = (q−3)(q+4)/32, X_u(3) = X_v(3) = 19/32 | `yang-mills/research-control/check.py` L238–243; `state.json` (source COLLATZ = KokunoYumeto/collatz-workbench@`63407034387466870f9e092dcdf39fb5a1ec0399`, `collatz_reconstruction/research_program/split_zero_history_20260913/note.tex`, read L70–210; transfer status "regression-only"); `consolidation/20260916/transcript-mathematics/05_local_score_workflow_20260914.md` L57–64; `WORKFLOW.md` L35–37; `STATUS.md` L19. In all, 164 YM files contain a hit. About 140 of them are copies in `consolidation/**/package/` and `…/history/` folders, and the peer-intake mentions (e.g. `continuations/20260914-coupled-response/RESEARCH_NOTE.md` L216) only record watched revisions |
| YM (false positive) | "rational Collatz bounds" are Collatz–Wielandt eigenvalue bounds in a lattice certificate, not the 3x+1 problem | `consolidation/20260916/audits/checker_scope.md` L28 |
| zeta | Citation of The Clankers, *Support-Idempotent Homogenization for a Split-Zero Collatz F-Series Frame*, Zenodo 10.5281/zenodo.19900461, used for (x,1) ↦ (x,h) and (x,h) ↦ (ax+bh, h) | `workbenches/splitzero-tandem/foundations/split-support-geometry-v11/split_support_geometry_arithmetic_curve_v11.tex` L3043–3052 (remark after `cor:no-global-translation`), bibitem L8956–8961; the same bibitem in v5/v11 copies in continuations |
| zeta (false positives) | b(3x+1−b) ≥ 0; a = 3n+1 in the vendored ES reader; X^{3n+1} | `…/tau-zero-prime-positivity/*`; `…/source_dependencies/ES_READER_V69.tex` L42501; `PUBLIC_MATHEMATICAL_CONTENT.*` |
| external | KokunoYumeto/collatz-workbench: public, 16 Sep cumulative collection; disclaims a Collatz proof | web check §0.4; **not in the provided set** |

### 7b. Main results

| ID | Statement | Locator | WB label | Proof | Audit |
|---|---|---|---|---|---|
| CZ-1 (ES R05) | θT = 4θ with T(n) = 4n+1 and θ(n) = 3n+1; T^j(n) = 4^j n + (4^j − 1)/3; mod M a conjugacy to multiplication by 4 when gcd(3,M) = 1, otherwise a semiconjugacy onto the image of θ; for odd n, U(T^j n) = U(n) | `results/PROOF_NOTES.md` L45–51 | "This is not a convergence proof or a novelty claim" (RESULTS L17) | Y; F | — |
| CZ-2 (ES X4) | No support-independent affine family has constant terms e/2 and f/2 on eA and fA. The homogenized maps L_{(a,b)}(x,h) = (ax+bh, h) commute with support inclusions. Finite-word identity M_{d₀}…M_{d_{N−1}}(0,s) = (s Σ d_n Q^{s_n}/2^{n+1}, s) | `ARGUMENTS.md` L75–87 | "written proof of the precise diagram"; "Neither Collatz convergence nor any real/adic interchange" is asserted (L75) | Y | — |
| CZ-3 (YM) | A specialization fiber used as a negative control against reconstructing a source from a collapsed observation | `check.py` L238–243 | "regression-only"; "not a Yang-Mills energy theorem" (state.json read scope) | the fixture is checked (F); its proof lives in the external repository | — |
| CZ-4 (zeta) | The affine-map homogenization reused in the v11 split-support foundation | v11 L3043–3052 | remark, citing Zenodo 19900461 | cited, not proved there | — |

### 7c. Disclaimers

- ES RESULTS L17 (above).
- `PROOF_NOTES.md` L53: "It gives common next-odd-value fibres, not convergence of Collatz."
- `CROSS_WORKBENCH_COMPARISON.md` L29: "Nothing here establishes a Collatz convergence result."
- I13 L97: the construction should be usable "without an implied Collatz proof".
- YM `state.json`: "regression-only".

### 7d. Audit coverage

None of `21_`, `28_`, `34_` or the register mentions Collatz (checked by search of the audit folder).

---

## 8. Overlaps

Type codes:
- **P**: a proved typed map or lemma, stated with domain and codomain and instantiated on both sides.
- **I**: the same object or identity appears on both sides (same formula, label or file); I state how the identity was established.
- **D**: one side imports the other's theorem as an unproved hypothesis or dependency.
- **R**: regression or test-fixture use only.
- **A**: analogy, proposal or located-only.
- **M**: methodological or provenance link, no mathematics.

| # | Edge | Shared object / lemma | Side A (source) | Side B (use) | Type | Audit / register |
|---|---|---|---|---|---|---|
| OV-01 | NS → ES | Torus endomorphism J = [[3,1],[1,5]], eigen-directions 4 ± √2, directional derivatives | NS manuscript §6.1 eq. (6.2) and Lemma 6.2 eq. (6.19); transcription in YM `navier-stokes/sources/…/sections/pp061-066.tex` L66–72 and `pp067-072.tex` L41–77 | ES `ns_operator_bridge/*.tex` (21 statements, ES-07); R07 | **P** (operator only; the ES proofs use no fluid theorem, supplement README L46–47) | **C** (`21_` §1; S40; neg. 42); bridge 17 |
| OV-02 | NS → YM | Velocity → reducible SU(2) connection; −2Σ tr F_ij² = λ²\|curl u\|² | NS rate bounds (250) imported from "the source reader and its endpoint continuation" | YM `released_profile_measures_addendum.tex` (250)–(266) | **P** for the map and identity; **D** on (250) and the dissipation bound (unverified) | **Cc** (`21_` §2; neg. 42; scope limit 21.4) |
| OV-03 | zeta → YM | Gram sandwich from a relative column error (δ ≤ 1) | zeta `…/20260919-circle-heat-original-metrics/HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex` HM10–HM14 (L178–235 at `baa6f7a`), HM19–HM24; `ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex` HG6–HG10 | YM `RH_HEAT_TRANSFER.md` T1–T5 | **P** (one lemma, two instances; "not asserted": an arithmetic-to-gauge map) | **C** (`21_` §3; S41); typos in zeta HM10 and HM19 noted in `21_` |
| OV-04 | zeta → YM | Inverse-power conductor observability, receiving instance | zeta `INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex` (21 Sep) | YM `RH_HEAT_TRANSFER.md` T7 (L247–300) | **P** per YM ("no identification of arithmetic zeta zeros") | — |
| OV-05 | zeta → YM | Composed minimum-lift identity AMT7–10; corrected residual and observed-iterate maps OK1–2 | zeta `…/20260914-original-kernel-web/13_ARITHMETIC_MIXED_TRANSFER.tex` (blob `b6cfec2a`, present at `baa6f7a`); `workbenches/tau-observation-kernel-formal/RESEARCH_NOTE.md` (blob `866ed2f6`; PR32) | YM `research-control/RESEARCH_NOTE.md` L25 (L219) and L22 (L191) | **P** ("instantiated"; "No arithmetic asymptotic constant transferred") | — |
| OV-06 | Jacobian F → NS kinematics → YM | U = DF⁻¹(V∘F), the curve γ, material tensor K_τ; Theorems 13.1, 14.2 | F (Alpöge announcement; YM ATTRIBUTION) | YM Fabel files (§5) | **P** at every algebraic step; the YM end is finite-regulator, g → 0 | **C** (`28_` §§1–2; S52 = claude-ab Lemma 28.1), **Cc** (`34_`; neg. 49, 57; bridges 32, 38) |
| OV-07 | S⁶ → YM | Imaginary period block B of Π(z); only D = det B enters | `alpo.ge/s6.pdf` p. 2 Setup (ATTRIBUTION L31–35) | YM `magnetic_translation_true_vacuum.md` (1.2)–(1.4); `retained_cusp_nonlinear_bridge.md` §1; `VOLUME_UNIFORM…` §19 | **P** (S⁶ identification "not an input") | **C** (`28_` Lemma 28.2; S53); `21_` §5 Lo |
| OV-08 | S⁶ → ES | Integral monodromies A₁, A₂, A_∞ of the (3,4,∞) period system → decorated affine-torsion covers of the ES divisor atlas | `alpo.ge/s6.pdf` §2 Lemmas 2.4–2.7 (as cited in ES `src/core.tex` L1–15) | ES `…/received/es_s6_counterfactual/` (`thm:class`, `thm:orbits`, `prop:crt`; preprint L55–64) | **P** (the proofs use "the displayed matrices", not the global S⁶ claim) | — (**new**; not in `21_`/`28_`) |
| OV-09 | ES ↔ S⁶ (lattices) | Niemeier lattice with root system A₅⁴D₄ and glue index 72 | ES R10 (order-72 glue H ⊂ (ℤ/6)⁴ × F₂²; PROOF_NOTES L95–103); `RESEARCH_DIRECTIONS.md` §2; I05 | S⁶ key advances §4 (R = A₅^{⊥4} ⊥ D₄, [N:R] = 72; TeX L199–201); S⁶ archive files named `es_niemeier_*` (Zenodo only) | **I** at the level of the named object. My arithmetic: \|disc R\| = 6⁴·4 = 5184, so [N:R] = √5184 = 72. The two glue codes were **not** compared line by line, and the S⁶ files are not in git | — (**new**) |
| OV-10 | ES ↔ zeta | Split-zero semiring G(R) = R ⊔ {τ}; unique Boolean character | ES R01 (PROOF_NOTES L5–13), X3 (ARGUMENTS L61–71) | zeta `satellites/14_…tex` `prop:gcue-coordinate-support` (L40) | **I** (same model; the zeta proof was checked by hand) | **C** (`21_` §6); bridge 17 |
| OV-11 | ES ↔ zeta | Finite Weyl phase-space basis | ES X6 | zeta `satellites/10_literature_foundations.tex` `prop:finite-weyl-coordinate-isomorphism` (L3322) | **I** per ES ("Already fully covered", CROSS_WORKBENCH L37–41) | not read by `21_` |
| OV-12 | zeta → ES (RH-facing) | NG20 (native compression law), NG21 (rank-one identity); native moment precision; projection phase return; native secular receiver; forward weighted conductor | zeta `…/20260920-gaussian-arithmetic-return/NATIVE_GAUSSIAN_TRANSFER.tex` (blob `6122e3b4`); `…/20260920-theta-transfer-current-precision/NATIVE_MOMENT_PRECISION.tex`, `PROJECTION_PHASE_RETURN.tex`; `…/20260920-native-secular-frame/NATIVE_SECULAR_RECEIVER.tex`; `…/20260920-marked-observation-illustrated/FABLE_TO_ORIGINAL_CONDUCTOR.tex` | ES `es-rh-family-integration-c` MR7–MR10, MR14, JS15 (`SOURCE_LEDGER.md` L20–29); `es-rh-multi`, `es-rh-continuation-b` ledgers | **D** (Family C "uses the provider as a theorem dependency; it does not reprove" it) | — (**new**) |
| OV-13 | ES ↔ zeta (Fable conductor) | 4-D Keller map P (det −2) and its fibres, transported into the Split-Zero weighted conductor T_A (WCF6) | ES reader v69 `thm:explicit-four-time-Jacobian-collision`; ES `upstream/FABLE_TO_ORIGINAL_CONDUCTOR.tex` | zeta `…/20260920-fable-signed-states/FABLE_TO_ORIGINAL_CONDUCTOR.tex` (**byte-identical, blob `50b39a8`**) and later copies; zeta `ALPOGE_FABLE_ROLE.tex` ALF1–ALF3 | **P** (written maps on both sides; the shared file is identical) | det DP **C** (`21_` C4); rest — |
| OV-14 | ES → zeta (vendored source) | The ES 488-page reader v69 (Zenodo 21845035) as a source dependency ("ES488") | ES reader (root PDF; source in `01_…zip`) | zeta `…/20260921-actual-xi-uniform/source_dependencies/ES_READER_V69.tex` (1.7 MB; also in three other 21 Sep continuations); cited in `ACTUAL_XI_UNIFORM_CONDUCTOR.tex` L37–69 | **D** (citation of specific ES theorems) | — |
| OV-15 | Jacobian F → zeta | Inverse-fibre chart; incompressible fibre heat; material generator; endpoint jets | F (cited to Tao, Speyer, Poplett) | zeta `satellites/23`, `26`, `27`, `29_*.tex`; zeta ATTEMPTS L17–19 | **P** within zeta (written); the relation to YM's use of F is **A** (same map, different constructions) | Lo (`21_` §4 lists only the FLIP_FABLE note on the zeta side) |
| OV-16 | NS → zeta | The released NS field as arithmetic input: angular momentum → dilation/Mellin; residue at s = −1; radial recursion | NS manuscript (imported) | zeta `satellites/29g…29s_ns_*.tex` (e.g. `29i` L5–23, `29k` L7–15); zeta ATTEMPTS L25–35 | **D** on the imported NS existence theorem ("Independent verification … is unfinished", ATTEMPTS L27) + **P** for the transports | — |
| OV-17 | S⁶ and F → NS (inside zeta) | F and the S⁶ cusp → fluid coordinates; S⁶ gauge-scalar equations → NS on 𝕋³ with a globally smooth image; three-point quotient | S⁶ archive (`quaternionic_4441_reconciliation.tex`, `prior_fable_context.tex`) | zeta `sidebar/fluid/tex/s6_bridge.tex`, `s6_dynamics_bridge.tex`; `sidebar/heat/tex/s6_three_point_quotient.tex` | **P** for the displayed calculations (bounded audit, L17–21); the NS workbench does **not** certify these transfers (RESEARCH_STATE L13) | — (`21_` §5 and `28_` §4 quote the NS disclaimer but did not locate these files) |
| OV-18 | 817 → zeta | 817 finite word sources and quotients in the Split-Zero supported quotient and receiving kernels (D6)–(D8) | 817 `interfaces/zeta/workbenches/ep817-*` (10 interface notes) | zeta `…/20260919-*/…/modular_ep817/EXACT_SUPPORTED_METRIC_RETURN.tex` (L18–26; nonclaim L408–415) and its RESULTS.json | **P** (typed cochain maps, written); no zeta statement is entered | — (**new**) |
| OV-19 | Collatz ↔ ES ↔ zeta | Support-idempotent homogenization (x,h) ↦ (ax+bh, h) | Clankers Zenodo 19900461 (external); ES X4 (ARGUMENTS L73–87) | zeta v11 foundation L3043–3052 | **I** (same formula; zeta cites it, ES proves the diagram) | — (**new**) |
| OV-20 | Collatz → YM | Specialization fiber (q−3)(q+4)/32 | collatz-workbench@`6340703` `…/split_zero_history_20260913/note.tex` L70–210 (external) | YM `research-control/check.py` L238–243 | **R** | — |
| OV-21 | ES → YM | Original labelled top-socle line → augmentation = success projector (ES PR6) | ES `research/incoming/es-split-boundary-20260914/core.tex` L1–145 (at `f234ed0`) | YM `research-control/state.json` transfer | **A** ("candidate-not-imported") | — |
| OV-22 | 817 → YM | Content-addressed validator | 817 `scripts/validate_workbench_state.py` L1–190 | YM `research-control/check.py` design | **M** ("No mathematical norm transported") | — |
| OV-23 | ES/817/YM | PolyClank design documents | YM `docs/polyclank/*` | ES `POLYCLANK.md` L15; 817 `research/general_k/notes/general-k-carry-capacity.md` L947–948; `notes/general-k-capacity.md` L576 | **M** | — |
| OV-24 | ES ↔ YM | "Gap" in ES X7 (a diagonal model, sharp gap 1/(9ρ²)) versus the YM gap | ES ARGUMENTS L127; CROSS_WORKBENCH L43–45 | YM programme | **A** (ES: the word "gap" does not identify the systems) | — |
| OV-25 | zeta ↔ ES (CUE) | CUE / Hurwitz / finite phase-space programme routed to zeta | ES I12, CROSS_WORKBENCH L7 (zeta PR #1) | zeta `CUE_RESEARCH_MAP.md` | **A** (routing proposal) | — |
| OV-26 | YM ↔ zeta (reporting) | YM's own summary of the zeta routes | zeta frozen reader (22678086) | YM `ATTEMPTS.md` L254–300; `research-attempts.json` L905–920 | **A** (summary; contains the 10⁻¹⁹ transcription error, §10 D1) | — |
| OV-27 | NS terminal time ↔ zeta Mellin | Mellin abscissa of a terminal singularity, from (250) and (255) | YM addendum | claude-ab `21_` Prop. 21.7 | **A** (labelled a reading in `21_` §7) | claude-ab |
| OV-28 | zeta → ES (13–16 Sep SplitZero packages) | Split-Zero support diagram and derived mathematics; original mixed-kernel control; AMT1–10 (the file YM also instantiates, OV-05) | zeta `formal/splitzero/DERIVED_MATHEMATICS.md` (blob `fe05d32c`); `…/20260914-original-kernel-web/08_ORIGINAL_MIXED_CONTROL.tex` (`bfcaccb3`), `…/13_ARITHMETIC_MIXED_TRANSFER.tex` (`b6cfec2a`); `…/20260914-joint-gamma-schur/`; `workbenches/tau-split-integration/RESEARCH_NOTE.md` | ES `es-zero-cohomology-20260913`, `es-splitzero-support-cohomology-20260914`, `es-mixed-support-20260914`, `es-split-boundary-20260914` (§1b F) | **P/D**, as recorded read scopes: the framework is reused; the analytic estimates are "not finite arithmetic assumptions" (`08_…` read scope). Not read in detail here | — (**new**) |

Not found:
- no 817↔ES or 817↔NS/S⁶ mathematical edge (817's mentions of ES and YM are methodological, OV-23);
- no NS-workbench-certified transfer (`28_` §4 confirmed);
- the NS vacuum-hydrodynamics continuation found "No S6 edge" (README L170).

---

## 9. Gaps: what a reader of each workbench would need that is missing or unproved in the repositories

**ES**
- G-ES-1: The current supplement has no Lean ("not represented as a whole-supplement Lean formalization", RESEARCH_STATE L152–154). The 72-statement index verifies only file identity (claims.json `verification_scope`).
- G-ES-2: The results-bench and X sources (CN-* from the Chatnotes archive, S1–S8) are private ("The raw chat archive remains private", README L499). R01–R10 and X1–X7 therefore cannot be traced to their original texts by a reader.
- G-ES-3: The ES/Fable C123 preprint (canonical local corpus unit PUBUNIT-1C9A160031EECC8F3F032D4D, source lines 22314–22543; crosswalk bibitem `ESC123` at L1992–2001) is not in the repository. The crosswalk uses it for the constant-Jacobian chart.
- G-ES-4: The 488-page reader source and Lean packages are only in `01_…zip` and `02_…zip`, not browsable. A copy of v69 TeX is vendored in the zeta repository instead (OV-14).
- G-ES-5: Item 20's metric asymptotics depend on zeta NG20–NG21, which ES does not reprove (OV-12).
- G-ES-6: ES-09 relies on S⁶ matrices read "through the web"; the 174 MB S⁶ archive was "located but not downloaded" (`es_s6_counterfactual/README.md` L56–58).
- G-ES-7: Three README-pinned proof files have changed since pinning (items 24, 26, 27; §1b E), so the pinned line ranges drift by up to 7 lines at tip.
- G-ES-8: The Collatz drafts CN-6d25…, CN-1cfd… are "Indexed only".
- G-ES-9: The historical correction (an earlier endpoint overclaim withdrawn) is not located: "did not identify the exact withdrawn DOI/version" (RESEARCH_DIRECTIONS L75).

**YM**
- G-YM-1: No Lean; no independent external analytical review.
- G-YM-2: The fifth-reference dual-certificate auditor and coefficient producer were not rerun (README L117).
- G-YM-3: The 19 Sep spatial tables and final execution package are not supplied (WORKBENCH L13).
- G-YM-4: The fixed-box weak-coupling limits used by Theorem 14.2 are credited to three source files that `34_` could not find (§5 of `34_`). They are only sketched in `FABEL_LOW_MODE_TRANSFER.md`.
- G-YM-5: The NS-profile edge imports the NS rate bounds (250) and a dissipation bound from the NS reconstruction; these are unverified (NS G-NS-2).
- G-YM-6: The "uncertified full-L2 tensor contraction calculation" is excluded (`yang-mills/README.md` L67; `OMISSIONS.json`).
- G-YM-7: The continuum problem: "the original shrinking-coupling continuum path still leaves the established domain" (WORKBENCH L9).
- G-YM-8: The external Collatz source used as a regression (OV-20) is not in the provided set.

**NS**
- G-NS-1: The official OpenAI PDF is not in the repository. Only its hashes (165-page `8c8a94ad…`, 166-page `0e779481…`) are recorded, together with an independent transcription (NS-03). The primary 208-page reader was derived from the 165-page capture (RESEARCH_STATE L15).
- G-NS-2: The imported source theorem is not independently validated: "imported profile and admissible-stress existence", all-stage realization and convergence, and the final forcing (RESEARCH_STATE L47).
- G-NS-3: The formal companion `openai/NavierStokesAndEuler@8937a8f` is external. The local formal run "stopped without an endpoint or Comparator certificate" (`research-state.json`).
- G-NS-4: The companion Alpöge–Buckmaster papers (IPM, Boussinesq, Euler) and `fluid_lean` are external (ES ATTRIBUTION L50–85).
- G-NS-5: For the vacuum-hydrodynamics continuation, the historical code for 60 symbolic assertions, 21 numerical checks and 19 test methods was not supplied (README L178). The Rindler collision location is not interval certified (L145–152).
- G-NS-6: The exploratory S⁶/Jacobian/heat → fluid transfers live in the zeta repository (`sidebar/fluid`, `sidebar/heat`; OV-17) and are uncertified by the NS workbench. An NS reader would need to say where they are and that they are outside its scope.
- G-NS-7: The 40-page `fluid_blowup_reconstruction.zip` report is accessible only inside `navier_stokes_source_bundle.zip`.

**S⁶**
- G-S6-1: The S⁶ manuscript (`alpo.ge/s6.pdf`) is external; it is not in any repository.
- G-S6-2: The full frozen project is only on Zenodo 22678442 (1,079 files, 174 MB). This includes the 782-page workbench (Theorems 53.4–53.18), the 138-page higher-rung paper (§§9–12), `analytic_canonical_ring.tex`, `period_parameter_deformation.tex`, `finite_filling_certificates.tex` and the `es_niemeier_*` files. The git repository has only the 5-page reader.
- G-S6-3: The global S⁶ claim is not certified by the workbench (s6/README L11). Engel's exposition, which states a self-contained proof, is external and was not checked here.
- G-S6-4: The attribution wording is inconsistent across files (§10 D2). The fetched S⁶ PDF text carries no author line or AI credit, so "produced with Claude" is supported by Engel's abstract and the YM attribution file, not by the PDF text as fetched.

**Jacobian material**
- G-JC-1: The originating announcement (X, 20 Jul 2026) is robots-disallowed and not verifiable here.
- G-JC-2: Poplett's research note is cited by zeta as "Locally retained" (90_references L657–661), so it is not public in the repository.
- G-JC-3: The zeta public reader's satellites 23/26/27/29 and its bibliography credit Tao, Speyer and Poplett for F but not Alpöge's announcement. The credit is supplied only by zeta `README.md` L295 and `ALPOGE_FABLE_ROLE.tex` (§10 D4).
- G-JC-4: The ES 4-D extension P rests on the ES reader v69 (zip in ES; vendored TeX in zeta) and the C123 preprint (not in the repository).
- G-JC-5: Fixed-box weak-coupling limits (G-YM-4).

**817**
- G-EP-1: Lean does not cover the lower bound, the minimal signed-block decomposition, the ternary product or the real asymptotic squeeze (STATUS L24; README L116–117).
- G-EP-2: All 29 continuation notes are "submitted for independent review"; no new Lean.
- G-EP-3: The 17 Sep continuation "Residue prices, constrained composition, and nonperiodic optimal schedules" exists only as a vendored copy in the zeta repository. It sits under `…/modular_ep817/source/research/residue_composition/`; there is no `residue_composition` folder in the 817 tree.
- G-EP-4: The original delivery is a GitHub release asset (`cumulative-2026-09-16`), not in the tree.
- G-EP-5: The unrestricted Λ_k (all block ranks) is open (`notes/general-k-capacity.md` L71; `editions/cumulative_20260916/README.md` L13).
- G-EP-6: Costa (arXiv:2609.06303, used for scope only) is external. The web check was blocked (§0.4).
- G-EP-7: The anonymous contributor's identity is private, by design (README L78–84).

**Collatz**
- G-CZ-1: No Collatz repository is among the provided sources. The Collatz workbench exists publicly but was not surveyed.
- G-CZ-2: The ES R05 source (CN-6fe2d9040d950e L1632–1757, crediting u/CivQ17) is private.
- G-CZ-3: The Clankers' Zenodo record 19900461, cited by zeta for the homogenization, is external.
- G-CZ-4: ES's handoff is outdated (§10 D3).

---

## 10. Discrepancies and cautions found while surveying (for the author to decide)

- **D1 (numerical transcription error in YM).**
  - The zeta source records W(wg₀, wg₀) = [2.0984855607004·10⁻¹¹ ± 6.08·10⁻²⁵] > 0 (`satellites/29f_actual_theta_weil.tex` L294). Zeta `ATTEMPTS.md` L23 and YM `research-attempts.json` L915 ("outcome") agree.
  - YM `ATTEMPTS.md` L274 and `research-attempts.json` L918 ("brief") say "2.0984855607004 × 10^-19".
- **D2 (S⁶ attribution wording).**
  - "produced with Claude": YM `ATTRIBUTION.md` L31, `README.md` L31, `WORKBENCH.md` L27, `s6/README.md` L9, guide L3.
  - "with Fable": frozen `27_…tex` L27, YM `ATTEMPTS.md` L209, `research-attempts.json` L736.
  - ATTRIBUTION L49 says historical files retain their bytes and that the clarification supplements them.
  - External: Engel says "produced by Claude under the direction of Levent Alpöge". The fetched S⁶ PDF shows no credit line.
- **D3 (Collatz repository).**
  - ES (10 Sep): "Repository searches did not positively identify a current Collatz repository" (`RESEARCH_DIRECTIONS.md` L61), and "No Collatz repository … was identified" (I13 L97).
  - YM research-control (14–15 Sep) tracks KokunoYumeto/collatz-workbench@`6340703`, and the repository is public (web check). The ES handoff is outdated.
- **D4 (Jacobian credit in the zeta reader).** Satellites 23/26/27 cite only Tao, Speyer and Poplett for F (e.g. `23_…tex` L6–8; `90_references.tex` L647–661 has no bibitem for Alpöge's announcement). This contrasts with YM `ATTRIBUTION.md` L19 ("not a substitute for crediting its origin") and with zeta's own README correction (L295).
- **D5 ("Fable" names three different objects).**
  - The Jacobian map F: YM "Fabel/Jacobi"; zeta `s6_bridge.tex` "retained Fable polynomial".
  - The S⁶ construction: the frozen S⁶ reader "with Fable"; the ES `es_s6_counterfactual` core "the Fable comparison" (the (3,4,∞) base marking).
  - The ES 4-D map P and its signed cover: "ES–Fable" cover and conductor.
  - A reader should disambiguate these every time; YM ATTRIBUTION L41 warns about exactly this.
- **D6 (audit-note coverage).**
  - The S⁶ edges are more extensive than `21_` §5 ("located only") records: ES-09 (OV-08) and the zeta sidebar S⁶ → NS bridges (OV-17).
  - The NS workbench's early transfers do exist, uncertified, in the zeta `sidebar/`.
  - OV-04, OV-05, OV-12, OV-13 (beyond det DP), OV-14, OV-18, OV-19 and OV-28 are not in the register's Goal 2 list.
  - Two zeta files are each used by two workbenches: AMT1–10 (`13_ARITHMETIC_MIXED_TRANSFER.tex`) by YM (OV-05) and by ES (OV-28), and `FABLE_TO_ORIGINAL_CONDUCTOR.tex` by ES as its upstream (OV-13) and as a source of `es-rh-multi` (OV-12).
- **D7 (sources quoted by `21_` are confirmed).**
  - The phrase "rigorous weak-coupling counterexample candidate, not a completed Millennium disproof" is at the end of `released_profile_measures_addendum.tex` L195. It is also duplicated in `extensive_quantum_blocking.md` L4329 and `markdown_source.tex` L5896.
  - The NS "not certified by this reader" sentence is at `navier-stokes/RESEARCH_STATE.md` L13.
- **D8 (duplicate files).** YM's two `navier_stokes_workbench.tex` copies differ only in CRLF line endings (verified by stripping CR). The zeta `sidebar/fluid/reader.pdf` is a different file from YM's 208-page PDF.
- **D9 (hygiene).** 817 review manifests contain Windows paths under a placeholder user (a placeholder user folder followed by a private-review folder name, e.g. `integration/20260916/reviews/ep817/recurrence_auditor/manifest.json` L11–15). They are sanitized, but they name a private folder structure. I note this only because the owner's rules exclude private paths from public outputs.
