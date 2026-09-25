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
| `12_CONTINUATIONS_25SEP_PART2_DIVISOR_POTENTIAL_SYNTHESIS_HILBERT_RETURNS.md` | Content map of eight further 25 September proof blocks: OZD (a positive off-line detector as a potential of log\|ζ\|), SPF1–SPF8, GSP and CTS (spectral synthesis), FGR (Connes' harmonic trace with the full Gram matrix), WHR (Connes' weighted-L² realization compared with Meyer's quotient), HCS and GMC. Includes checks and items for the four goals |
| `13_LEDGER_OF_THE_ZEROS_AND_ONES_IN_THE_COMPLETED_ZETA.md` | Separates every object called 0 or 1 in the classical derivation of the poles of ζ: lattice origin, dual origin, additive origin with its local germ, pole position, fixed point of the sign, and the unit of the clock. For each it derives which pole or term it produces, and it lists as a proposal the slots where the programme's τ could go |
| `14_CONTINUATIONS_25SEP_PART3_WEIGHT_RECEIVERS_AND_TENSOR_GROWTH.md` | Content map of VWR (Connes' weighted-L² construction on every vertical line: jointly faithful receivers, each pure of weight 2σ) and ATG (tensor powers: growth exponent k, error k(B − ½) linear in k, infinite multiplicities). Includes items for the goals |
| `15_CLOCK_STACK_TAU_AT_WINDING_ZERO_AND_PSI.md` | The programme's clock stack (PMS): τ is present at winding zero, which is not absence; the completed prime clock is Ẑ; the joint clock of periods 1..N has lcm(1..N) = e^{ψ(N)} states. With checks and Figure 15.1 |
| `16_SOURCE_ENDPOINT_NCI_RSS_NHJ_NYMAN_BEURLING_IN_FRECHET.md` | The source-endpoint proofs NCI, RSS and NHJ: the zero-jet ideal is the closure of ξℬ and is spanned by the cover discrepancies (unconditionally, in the Fréchet topology). The residue section decides which divisor the Hardy receiver's covariance selects |
| `17_THE_MIRROR_LINE_AT_MINUS_ONE_HALF_AND_THE_HURWITZ_JET.md` | The owner's mirror line at Re s = −½, made exact. The first Hurwitz jet vanishes exactly on Z − 1 = A(Z), the mirror of the zeros through the pole 0 (unconditional). Mirror = shift on every zero is equivalent to RH. The critical line and the line at −½ are the two halves of one (1,−1) circle on the Clifford torus. Only the ½-centred explicit-formula pairing is real. With checks and Figure 17.1 |
| `18_THE_TWO_LINES_IN_THE_PROGRAMME_SEPARATOR_RECEIVERS_AND_GAUSSIAN_APPROXIMATION.md` | Content map of SMC, GAP and ADM, with checks. Every positive measure receiver sees only the critical-line values, and the off-line Weil complement W_O stays explicit. Gaussian approximation of the whole source. The programme's separator is built from G(s) = F₀(s)F₀(s+1), whose zeros are the critical zeros and their copy one line to the left. The unconditional pair of modules is Q and its twist Q₊ (jets at Z + 1); they are derived-separated for a general algebraic reason (coprime annihilators). The global model's pair ℛ[1] ⊕ ℛ(−1)[−1] holds only off-line data and vanishes iff RH. This locates the owner's "two lines" inside the programme (revised after a referee pass) |
| `19_THE_PRODUCT_TRACE_ITS_DIAGONAL_RETURN_AND_THE_HARDY_RECEIVER.md` | Content map of FTD, PRS, DER, FSC, FEM and NHJ4–NHJ9, with checks. This completes board task 5. The three-point base has dualizing complex j_!k[1], so the residue pairing lives on the product. The diagonal return needs the right adjoint Rq_*, which keeps the trace with coefficient +1. Returned to Spec ℤ ∪ {m₊, m₋} it is a correspondence, since no continuous single-valued lift fixes the arithmetic diagonal. Paired weights always sum to 2, and nothing in the chain forces weight 1. Noor's tests are dense, and the covers' only obstruction is a boundary pole 1/(1−z) |
| `20_THEOREM_C_REPROVED_SUMMED_HURWITZ_VELOCITIES_FLUCTUATE_AT_ORDER_T.md` | Board task 4: the copy's Theorem C, parts 1–3, proved in full along the copy's route, relative to Theorem A (revised after a referee pass: the conjugate zeros, the integration by parts at good heights, the range of Lemma 20.2(b)). Under (H), the summed Hurwitz zero velocities ρζ(ρ+1)/ζ′(ρ) deviate from their drift by unbounded multiples of T. The mean-square constant is ≈ 0.0373. The Liouville twist makes the squarefree terms positive, and its partial sums have mean 2/5 (Σ b(n)λ(n)n^{−s} = ζ(s)ζ(2s+2)/(ζ(2s)ζ(s+1))) |
| `figures/` | Illustrations, each with the script that draws it from the checked data (see `figures/README.md`): the zeros of the even sheet Z_{1/5}, the factorial and half-factorial sheets, the shifted-flow crossings, the clock stack, and the mirror line with the chiral pair of circles |
| `copy_round2/code/` | The copy's scripts. The zero data they read from `data/` are not published; `zerodata.py` regenerates them |
| `09_HARMONIC_SWEEP_SOURCE_PAIRING_AND_NYMAN_BEURLING.md` | Content map of the 25 September harmonic-sweep (HSW), source-pairing (OPD) and positive-measure (SPF) notes. It also gives the bridges to Hilbert–Pólya, Wiener, Nyman–Beurling and Burnol's co-Poisson theory |
| `10_RESULTS_DIGEST_DRAFT.md` | Concise results digest (Claude's edition, draft 1), written for later use as the Zenodo front document |
| `11_FREE_MONOIDS_EULERIAN_SHEETS_AND_F12_UNITS.md` | Congruence monoids joining Theorem E and the even-sheet Euler test. A general lemma: the formal logarithm of a monoid of integers is nonnegative iff the monoid is free. Half-factoriality, and the sign ±1 as the passage 𝔽₁ → 𝔽_{1²} (revision 2) |
| `ERRATUM_FLIP_FABLE_ADDENDUM_4.md` | Erratum to an earlier claude-ab claim about the shifted flow |
| `PLAN.md` | The working plan and log |
| `BRIEFING_FOR_LOCAL_SESSION.md` | Briefing for a cooperating local Claude session |

None of these files claims a proof or disproof of the Riemann hypothesis.
