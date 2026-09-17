# LRC11–LRC12 independent proof audit

**Verdict: proved as written.** The original constant `24 K_h² + 30 Q_h` is valid for every integer `n ≥ 1` and every real evaluation point. The complete argument proves the stronger constant `16 K_h² + 24 Q_h`; the stated downstream constant is retained.

The full mathematical proof is [LRC11_LRC12_FULL_PROOF.tex](LRC11_LRC12_FULL_PROOF.tex). It is an integration-ready TeX fragment containing the hypotheses, all maps, every estimate, the small-n cases, the exact EIQ density factors, and proofs of the endpoint and exterior cases. No compilation was performed, as instructed.

## Exact claim

Let μ be a probability measure on `[A,B]`, `A < B`, with density `H(y)√((B−y)(y−A))`, where `H > 0` and `H ∈ C¹([A,B])`. Put `c=(B−A)/2`, `m=(A+B)/2`, and `h(t)=c² H(m+ct)` on `[-1,1]`. Define `Q_h=max h/min h`, `M_h=max|h′/h|`, and `K_h=Q_h(1+M_h)`. If `y_j` is the original midpoint probability quantile at `(j−1/2)/n`, then

$$
\sum_{j=1}^n\log|x-y_j|
\le n\int_A^B\log|x-y|\,d\mu(y)+24K_h^2+30Q_h
\qquad(n\in\mathbb Z_{\ge1},\ x\in\mathbb R).
$$

The integral is finite for every real x. If x is one of the selected quantiles, the left side is `−∞` and the conclusion holds in the extended-real sense.

For the original EIQ density, with `0 < A < B`, `β > 0`, and the exact factor

$$
H(y)=\frac{\beta}{4\pi^2 y}
\int_0^\infty\frac{\sqrt s}{(y+s)\sqrt{(A+s)(B+s)}}\,ds,
$$

the proof gives `Q_h ≤ (B/A)²` and `K_h ≤ (B/A)³`. Thus the original value `C_disc=24(B/A)⁶+30(B/A)²` follows without a change in measure or normalization.

## Dependency graph and evidence

| Implication | Evidence in full proof | Status |
|---|---|---|
| Original measure → transported density and original quantiles | Increasing affine bijection, inverse, density Jacobian, exact cancellation of `n log c` | Passed |
| Positive C¹ square-root-edge density → inverse quantile is C² inside | Differentiation of `F(q(u))=u` | Passed |
| Density → logarithmic derivative bound for `q′` | Explicit left and right tail integrals; no claim that `F(0)=1/2` | Passed |
| Logarithmic derivative bound → `|f″| ≤ 48 K_h²/d²` | Segment integration with explicit length, original exterior distance inequality, full differentiation | Passed |
| Marked cells → at most six | Exact inclusive condition `dist(v,I_j) ≤ 1/n`, equivalently `j ∈ [nv−1,nv+2]` | Passed |
| Unmarked cells → inverse-square sum ≤ 8 | Four explicit telescopically bounded series | Passed |
| Unmarked cells → discrepancy ≤ `16 K_h²` | Proved midpoint remainder constant `1/24` | Passed |
| Physical probability cell → density ≤ `2 Q_h/L` | Concavity and the two exact inscribed triangles | Passed |
| Every real evaluation point → interval logarithm integral ≤ `2L` | Explicit primitive, separate interior, endpoint, and exterior calculations | Passed |
| Marked cells → total discrepancy ≤ `24 Q_h` | Conditional density bound and at most six cells | Passed |
| Exact EIQ factor → `−2/y ≤ H′/H ≤ −1/y` | Integrable domination, differentiated positive integral, exact probability ratio | Passed |
| EIQ derivative bound → original LRC12 constant | Integrated ratio and explicit affine derivative chain rule | Passed |

Every analytic estimate in this dependency graph is proved in the fragment. The EIQ density itself is the original source formula, read directly in `14_CURRENT_KERNEL_AND_MULTIPLICITY_PROOFS.tex`, EIQ10–EIQ11, lines 11449 and 11460; the source's function named `h` equals `2π H` here. This audit does not need to change or re-establish the already defined equilibrium measure to prove its discrepancy bound.

## Details repaired in the abbreviated source proof

The source states the needed estimates but does not explicitly specify how to count cells whose boundaries are exactly one mesh width from the singularity. The full proof includes those boundary cases and still marks at most six cells. It also supplies the inverse-square sum, the midpoint remainder constant, and the logarithmic primitive for exterior points. These are omissions of detail, not counterexamples to the statement or reasons to enlarge the stated constant.

The point `t=0` in physical coordinates need not have probability coordinate `1/2`. The tail calculation uses `min(F(t),1−F(t)) ≤ F(t)` for `t ≤ 0` and `≤ 1−F(t)` for `t ≥ 0`; it makes no symmetry assumption on h.

For exterior evaluation points, the segment proof uses the explicit inequality `|x−q(u)| ≥ |q(v)−q(u)|`, with the correct nearest endpoint v. It does not assign an exterior physical point a nonexistent inverse probability value.

## Independent check and remaining scope

The separately delegated cell audit reproduced the interval-logarithm inequality and exact cell enumeration, including `n=1` and singular probabilities on grid boundaries. The full proof was then checked directly for consistency. No numerical sampling, external theorem citation, symbolic package, Lean run, or compilation is part of its evidence.

There is no remaining mathematical gap in LRC11–LRC12 under their stated hypotheses. LRC13 onward, including the full original-root norm comparison and the norm minima, belong to the parent's separate audit.

The source assignment and provenance are recorded in [USER_INPUTS.md](USER_INPUTS.md); work and decisions are recorded in [LOGBOOK.md](LOGBOOK.md). Root owns the shared original user transcript, and the parent retains the complete attachment at `../input_pasted_text.txt`.
