# Briefing for the cooperating local Claude session

From: claude-ab. This is a Claude session running in the cloud through the Cowork web interface, on model `claude-opus-5-5` (Opus 5.5) at maximum reasoning effort.
To: the owner's new local session (Claude Code on the owner's PC).
Date: 25 September 2026, about 05:00 UTC.

I cannot message your session directly: it is not reachable from my cloud container. Coordination therefore goes through two channels:

- files on GitHub;
- the owner, who relays.

Please read this whole briefing before starting.

## 1. What the project is

The owner (GitHub: KokunoYumeto) runs a research programme around the Riemann zeta function.

- **Split-zero, non-Eulerian programme.** The object is the Hurwitz flow ζ(s, 1+t) (the "τ-weight flow").
- **Second attempt.** It builds arithmetic from a parityless support τ〈Z₁; no Z₂〉, realized at the generic point of Connes–Consani's 𝔽_{1²} line (arXiv:2609.00299). It includes prime clocks, timed primes, a positive-quotient lane, a character-lifting lane, and a reconstruction of Deligne's Weil II weight argument.
- **Who writes it.** Most of the programme text is written by ChatGPT/Codex lanes. It lives on `main` of `KokunoYumeto/zeta-function-research-reader`, together with Zenodo editions.

My lane is salvage, verification and new results, organized by the owner's four goals:

1. negative results, stated readably, not as "machine junk";
2. bridges and implied unifications across fields and programmes;
3. lemmas that can be stated independently of the project;
4. the F1 context: framing the question the programme partly asked without meaning to.

The owner also asked for the corpus to be read holistically, not in its own terms. Two working styles are both wanted: exhaustive calculation, and fleshing out one precise idea.

## 2. Where my work is

- **GitHub.** Branch `claude/claude-ab-grind-20260925`, folder `contrib/claude-ab/grind_20260925/`. This is the durable mirror. `00_RESULTS_REGISTER.md` is the index.
- **Your disk.** The owner's local folder `work/claude_grind_20260925`, inside the owner's math folder, holds a copy that I commit to while the PC is connected. It may lag the branch.

Files:

- `00_` is the register.
- `01_`, `04_`, `05_` and `07_` are content maps of the second attempt's proofs, read in full.
- `02_` and `03_` are the reports of an earlier Claude copy.
- `06_` is the Theorem E referee report.
- `08_` holds the Euler test, the inputs of Deligne's argument compared with the programme, and the F1 framing (revision 2).
- `checks/` holds scripts and their outputs.
- `PLAN.md` holds the plan, the log and the standing rules.

## 3. Rules the owner has set (all binding)

**Repository and publication**

- Never commit to, push to, or rewrite `main`. Work on branches named `claude/<topic>-<date>` or open pull requests.
- Note your model and reasoning effort in commits and pull requests.
- GitHub is the durable mirror of the work. Zenodo gets it only when something is mature: as a new version of record **22911829**, adding files and never replacing them, with metadata changed only by an added "Claude's edition" note. Do not use record 22949437. Stay out of Codex's files and metadata.
- No private filesystem paths in public outputs.

**Conduct**

- No notifications or pings. Do not spawn many agents; at most one or two, and only when clearly needed.
- No heavy computations or scans on the owner's PC.

**Writing**

The owner's preferences, verbatim: "Never make personal comments. At all. Do not be 'concise' or informal - do not tone-match user. Do not present your opinions as facts. Prove every single claim you make with either an explicit calculation, derivation or citation to the research literature."

**Method**

The owner's heuristics:

- "don't normalize, don't simplify";
- "When X does not equal Y, your immediate next step must always be Prove the exact typed morphism between X and Y";
- "every obstruction is a definition";
- "You are not here to correct me. You are here to take my ideas and push them to their logical conclusions."

Further rules:

- Accuracy over speed.
- Judge work by what it establishes, not by whether it proves RH.
- Never identify τ with the supported zero e.

## 4. What is open, and a proposed split

I will continue in the cloud with the remaining content maps, the register, and referee passes on new programme files. Because you have the disk, local git and the owner's other repositories, the following fit your side better. They are proposals; the owner decides.

1. **Codex's even-tensor-power calculation.** Codex reports that "the even tensor powers retain the spectral data and have nonnegative Euler coefficients". Locate this calculation in the repository and check it against Deligne's two-part step in Weil II §1.5:
   - DP4, the positivity of coefficients (the reported calculation);
   - DP5.1, a pole-free disc for the L-function of F^{⊗2k} that is fixed uniformly in k by the curve's H_c² denominator.

   The question is whether the programme has the second half. See `08_` §3, item (e), and the Deligne reader `DELIGNE_WEIGHT_CONTROL_FULL.md`, DP4–DP6.
2. **Cross-programme bridges (goal 2).** The owner reports that the ChatGPT lanes reused results across Navier–Stokes, Yang–Mills, "Elpo G's S¹ work" (higher-dimensional topology), zeta and Erdős–Straus. The repositories `erdos-straus-foundation` and `erdos-problem-817-workbench` are on GitHub. Find the concrete places where one programme's lemma is used in another, and state each reuse as a typed morphism with its exact hypotheses.
3. **An erratum.** My earlier "FLIP_FABLE Addendum 4" claimed that zeros sit on vertical lines only at Eulerian times. Certified crossings in another lane refuted it. The file is in `claude_orientation_20260922` on the owner's disk or branch `claude/orientation-20260922`, and needs a dated erratum paragraph.
4. **An independent re-proof of Theorem C, parts 1–2.** Theorem C comes from the earlier copy (`02_`, `03_`). It says the sharp velocity laws fail at order T, with Bohr coefficients −b(n)/(2π√n log n).

## 5. How to cooperate

- **Branches.**
  - Push your work to your own branch, for example `claude/local-<topic>-20260925`, with a short `HANDOFF.md` saying what is done and what is open.
  - Do not edit files on my branch.
  - For a correction to my files, write it in your `HANDOFF.md` or tell the owner. I will apply it and credit you.
- **Rivalry is welcome** ("#rivalry #betterresultsbecauserivalry"). If you think one of my claims is wrong, write the counterexample or the missing step. The referee pass on `08_` already caught real errors (a zero count and a section citation), and they are corrected in revision 2.
- **The register.** Results for the register should come with a statement, a status, a source and a check.
