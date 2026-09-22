Provenance: this request was written by Claude (Anthropic; model id claude-opus-5-5, working in a Cowork session) for the repository owner, who asked me to hand you a large calculation. Please read the GitHub repository KokunoYumeto/zeta-function-research-reader directly through your GitHub connection, at the pinned commit 4ba9285b66af58a6d58fc502a494c1fb45ca5b79 (main, 22 Sep 2026, 19:02 UTC). Do not modify the repository.

The task is a complete, rigorous calculation in two parts (A and B). Give complete proofs and an exact file:line locator for every programme input you use. Do not state conditional theorems or proof obligations; do the mathematics. Keep the programme's original objects, constants, signs, domains and error terms; do not normalize them away.

## Files to read first (paths under workbenches/splitzero-tandem/continuations/)

- OPG1–OPG4: 20260914-conductor-kernel-continuation/03_FULL_OBSERVATION_PROOFS.tex, lines 55–140. The quartet ρ=1/2+δ+iγ with 0<δ<1/2, γ>2; h; v_h=g/h with g=2ξ; E_h; U; the tensor packet E=C[S]/(χ); ι; the period map Π with e^{Φ_h/u}; the cyclic average P_k; the observation L=P_k Π^{⊗k} U^{⊗k} ι.
- BT1–BT6: 20260914-conductor-kernel-continuation/02_FULL_GAMMA_PROOFS.tex, lines 9710–9762. The arithmetic density w_h and the |ζ(1/2+it)|² inputs.
- CK1–CK14: 20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md.
- RC1–RC44: 20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md, especially RC22–RC25, RC32 and RC35–RC44.
- TR1–TR24: 20260922-terminal-response/TERMINAL_COHERENCE_PROOF.md, especially TR20 (lines 240–251) and the open-problem statement (about lines 324–326).
- ST, MP, DF, SC, EE in 20260922-support-transport/: SUPPORT_SPECTRUM_AND_TERMINAL_MASS.md, MIXED_PROBE_PROOF.md, OBSERVED_DEFORMATION_AND_CURRENT.md, STABLE_HIDDEN_ACTION_AND_SIGN_STEPS.md, EVOLUTION_EXTENSION_PROOF.md. Also RESEARCH_STATE.json, field next_calculation.

## Part A. A control completion with a genuine off-line quartet

Let γ1=14.134725… and γ2=21.022039… be the ordinates of the first two zeros of ξ; both are simple and on the critical line. Fix δ0 in (0,1/2) and γ0>2 with γ0≥1000·δ0 and γ0 different from γ1, γ2, such that ρ0=1/2+δ0+iγ0 is not a zero of ξ. For example γ0<3·10^12 works, by Platt–Trudgian, Bull. LMS 53 (2021) 792–797. Define

Q0(s) = ((s−1/2)² − (δ0+iγ0)²)·((s−1/2)² − (δ0−iγ0)²),
Q1(s) = ((s−1/2)² + γ1²)·((s−1/2)² + γ2²),
g̃(s) = 2ξ(s)·Q0(s)/Q1(s).

A1. Prove the following.
- g̃ is entire of order 1.
- g̃(1−s)=g̃(s), and g̃ is real on the real axis.
- The zero set of g̃ contains {ρ0, ρ̄0, 1−ρ0, 1−ρ̄0}, each with exact order 1.
- g̃/(2ξ)→1 as |s|→∞.
- g̃ is not of the form (the completion factor of ζ)×(a Dirichlet series). Use Hamburger, Math. Z. 10 (1921) 240–254, or a direct almost-periodicity argument. Give a complete proof.

A2. Put h:=Q0 (so m=1) and v_h=g̃/h=2ξ/Q1. Compute w̃_h(t)=|v_h(1/2+it)|²/(2π) exactly, as the analogue of BT3. Then prove the analogue of every inequality the programme uses about w_h, stating each constant change explicitly:
- the BT4–BT6 upper bounds;
- the mean-square upper bound used for CK3 and RC22;
- positivity of ϑ_h;
- the CK3 comparison constants between μ_k and the Gamma measure σ;
- the quantity I_h from AG26, if it enters the chain.

A3. Audit the complete dependency chain of TR20 and of SC1–SC25, going back through RC, CK, ST, MP, DF, EE and OPG/BT. List every place where a property of g=2ξ, or of ζ, is used. For each one, either prove that the same statement holds for g̃ (with the constants from A2), or identify exactly the step that fails for g̃ and explain why. Deliver this as one numbered table with columns: result ID, file:line, property of g used, holds for g̃?, proof or counter-reason.

A4. Conclude with exactly one of the following.
- (i) Name the first step that genuinely distinguishes ζ from g̃. That step is then the programme's arithmetic core; state it and prove it in full.
- (ii) Prove the theorem that every CK/RC/TR/SC/ST/MP/DF/EE conclusion, with its constants and error terms, holds verbatim for g̃ and its actual off-line quartet. It follows that no sign, magnitude or inequality derived only from these results can contradict δ>0. In this case also:
  - define the class 𝒢 of completed functions for which the whole chain is valid, as a space of objects (in the programme's sense that "every obstruction is a definition");
  - prove g̃∈𝒢;
  - state precisely which additional structure (Dirichlet coefficients, Euler product, or the explicit formula with primes) separates 2ξ inside 𝒢.

## Part B. Conjugation and parity symmetry of the current

B1. Let C be coefficient conjugation on E=C[S]/(χ), written in the y-coordinate (y=(S−k/2)/i). Use that w_h is real and even (BT3). Prove or disprove each of the following:
- C is antiunitary for every source metric G_N;
- CM=MC;
- C maps the construction at admitted period u to the construction at ū, that is, C(K_u)=K_ū and C∘P_B(u)=P_B(ū)∘C;
- C maps the terminal class x=v_+ (ω=kγ−ikδ, RC35) to the class at ω̄=kγ+ikδ.

Do the same for parity y↦−y. Parity may need a companion map on the period (for example u↦−u); determine that map exactly from OPG4.

B2. Compute exactly how each of the following transforms under these maps: j_G(x) (SC2), Φ_N(Λx) (RC32), and 2ε√𝔡·Im(c̄_g c_h) (TR20). In particular, decide whether on the real-period locus (u real, if such u are admitted) the currents of the terminal class and of its conjugate class are exact negatives of each other.

B3. State what B2 implies for the programme's stated next calculation (RESEARCH_STATE.json, next_calculation, in 20260922-support-transport). Can any evaluated sign of that current, by itself, contradict δ>0? If a contradiction would require a positivity principle (a quadratic form proved ≥0 for ζ that an off-line quartet would make negative), say which form, and whether it is specific to ζ.

## Output

Produce a single Markdown document containing:
- sections A1–A4 and B1–B3, each with full proofs;
- the dependency table from A3;
- a list of every external theorem used, with exact citation;
- a final short list of what remains open.

If the full A3 audit is too long for one reply, first finish A1, A2 and B1–B3 completely, then continue A3 in the next reply, keeping one continuous numbered table.
