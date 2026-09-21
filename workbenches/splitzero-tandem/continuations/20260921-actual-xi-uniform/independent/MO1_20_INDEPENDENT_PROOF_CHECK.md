# Independent proof check of MO1–20

Date: 20 September 2026. Scope: complete mathematical reading and independent derivation of the new actual-observation body; no publication, layout, or source-index audit is claimed.

Checked source: `ACTUAL_MARKED_OBSERVATION_BODY.tex`, SHA-256 `3A7A23C7DB180CCA8AEC7A08F9E6E087B77011C584BE632977B4F42F25BB80F8`.

Supporting sources actually read for this check:

- `FABLE_TO_ORIGINAL_CONDUCTOR.tex`, FX1–8 for the completed factor charts and their full transition, and CA1–15 for the original quotient action and polynomial lift.
- `work/heat_zeta_literature_20260919/publication/providers/04_FULL_ORIGINAL_OBSERVABILITY.md`, complete source, especially O1–3 and O10.
- Independent exact original inverse GF7–8 and full fibre classification in `GLOBAL_FIBRE_AND_NONPROPER_LOCUS.tex`; these were derived in this task rather than inferred from verification receipts.
- `ACTUAL_CORNER_OBSERVATION.tex`, AO1–23, current source SHA-256 `0EA5A9AB1A225B239DF402A5A2EC04ED2F30CC3B1D0512F7A65EDF09623737D5`.

**Outcome:** MO1–20 are mathematically accepted on their stated original domains. No mathematical correction was required. This acceptance covers the displayed morphisms, complete residuals, fibre counts, constants, and support cases; it does not identify the introduced nonlinear map with the original linear conductor or assert a result about RH.

## Original conductor and metrics: MO1–8

1. At each lower-grid root, the original shift convolution can hit a specified upper corner only through its matching lower corner and matching degree-eight extreme shift. This independently proves all four columns of `C J_+ = J_- D_partial`, including their original coefficients and phases. The conductor-multiple invariant lift gives `ker Lambda ⊂ ker C`, so the stated factorization through the actual observation is well-defined.
2. The unreduced difference in MO2 vanishes at every distinct lower root; it is divisible by the actual lower grid polynomial. Its maximum degree after division is exactly
   \[
   ((k+1)^2-1-v)-(j+1)^2=16k-49-v.
   \]
   The polynomial residual has not been assumed zero or assigned zero physical norm.
3. The quotient actions on the actual corner idempotents have eigenvalues `k rho_l` and `j rho_l`; their difference is precisely `8 rho_l`. This proves both identities of MO4 and the retained factor `k/j`.
4. The degree gap is `16k−48≥96>v` for `k≥9`, so the original triangular conductor is onto the lower quotient. Together with positivity of the original finite source forms and the stated onto reductions, this verifies invertibility of the Gram matrices used in MO5.
5. Direct multiplication gives `bar C R_N=I` and `R_N* Q_N=T_N bar C`. Thus `Delta_N∈ker bar C` is orthogonal to the conductor minimum lift, giving MO7 with its entire positive residual. Independently, `Lambda M_N=I`, `M_N* G_N M_N=Q_N` and `Z_N∈ker Lambda` give MO8. These are two different kernels and two different complete orthogonal decompositions; neither residual is silently dropped.

## Literal marking and the complete seven-state orbit: MO9–11

6. The matrix `K` takes labelled coordinate vectors to the original four collision points, so the literal receiver is `O_+ K^{-1}`, and the generator is exactly `K diag(k rho_l) K^{-1}`. The stated nonlinear conjugacy maps are isomorphisms only on their indicated four-dimensional images; that domain restriction is correct.
7. The original common value is `h_0=2i K e_M`, so it is an eigenvector of the marked generator. Over `e^{lambda t} h_0` the finite factor roots are exactly `0,+b(t),−b(t)` with derivatives `−b²,2b²,2b²` and `b=e^{lambda t/2}`. Inserting both signs of `a²=1/h'(r)` into every coordinate of GF7 gives exactly the six finite-root formulas in MO11. GF8 gives the single positive-chart infinity point. Thus all seven trajectories and their exhaustion were derived independently.
8. Every displayed coordinate is a polynomial in `b` or `b^{-1}`, which are entire nonvanishing exponentials. Differentiating the original polynomial identity yields the unique lifted vector field because `det DP=−2`. The permutation at one target period follows from `b→−b`: it fixes the infinity state and exchanges the other pairs exactly as stated.

## The actual marked arithmetic orbit and its five escapes: MO12–19

9. Independently formed `K diag(k rho_l) K^{-1}(0,1,0,0)^T` over `Q(i,sqrt(2))[k,delta,gamma]`, not by reading the root's verification output. Its first and fourth components reduce exactly to
   \[
   \nu_A=\frac{k}{154}[-68\gamma+i(25\sqrt2\gamma-136\delta)],\qquad
   \nu_D=\frac{k}{77}[-884\delta+(1631\sqrt2+442i)\gamma].
   \]
   Both are nonzero on the admitted original domain. Independently differentiated the full quartic discriminant polynomial at `(A,B,C,D)=(0,1,0,0)`; the gradient is exactly `(0,0,0,−4)`.
10. For every finite exponential term, the integral Taylor remainder is at most `|theta|² e^{|theta|}|t|²/2` when `|t|≤1`. Summing its original coefficient moduli gives exactly `M_D,M_A`. With the displayed `r_0`, the residuals are at most half the respective nonzero linear terms, giving the MO15 lower bounds. Thus the punctured disk has eight inverse states with no hidden numerical root search.
11. Setting `t=s²,x=sv` at the double root produces `v²+nu_D` at `s=0`; its two roots are nonzero and simple. Differentiating the actual polynomial gives `h'(r)=2v s+O(s²)`. Both factor signs therefore yield four states with `t^{1/4}q→kappa e_a`, `kappa²=(2v)^{-1}`. All three other original source coordinates tend to zero by direct substitution in GF7.
12. In the negative factor chart the infinity point is `(0,1,−7i/2,11)`, with `c(0)=i`; hence `a'(0)=−i nu_A`. The positive-chart transition has leading term `−40i/a³`. Since `(-i)³=i`, its exact coefficient is `−40 nu_A^{-3}`. This independently verifies the sign and constant in MO17.
13. The other infinity state and the two signs over the simple finite root `−1` give precisely the three vectors in MO18. The original derivative remains invertible at each, so they have finite analytic lifts. The complete fibre count is eight off the center and three at it; the four quarter-power branches, one cubic-pole branch and three finite states exhaust it.
14. The observer is fixed and injective on the stated domain. Applying it to the exact vector limits gives the constants in MO19 in the full original pullback metric `K^{-*}H_+K^{-1}`. Positivity follows from the original Gram and the proved injection, not from an assigned Euclidean norm. The partial-support stacked constants follow from AO19–22 and the fact that every coordinate of `K^{-1}e_a` and `K^{-1}e_w` is nonzero.

## Completed partial-support receiver: MO20

15. AO7 recovers the active coordinates uniquely from the actual visible stack. The invisible coordinates are retained explicitly, so
   \[
   q\mapsto(Z_mK^{-1}q,(K^{-1}q)_Z)
   \]
   is a linear isomorphism onto `im Z_m ⊕ C^Z`, with exactly the inverse written in MO20. The declared empty-active-set convention gives the same statement when all columns vanish.
16. The active stack action is the actual companion restriction from AO11, while the retained invisible coordinate subspace is invariant under the actual diagonal corner action. Thus the complete receiver has precisely the direct-sum arithmetic action in MO20. Conjugating the full original polynomial through this isomorphism is valid. No descent of that nonlinear polynomial to the visible stack alone is inferred.
17. Its full original source-corner norm is the original quadratic form evaluated on the recovered active coordinates and the retained invisible coordinates. Keeping the off-diagonal blocks gives all cross terms. Completing the square in the invisible coordinates yields exactly AO13's Schur complement. Hence this last extension preserves rather than removes the missing directions.

This receipt is an independent mathematical check of the stated body. The source authorship and original human references remain those cited in the mathematical files; no source has been reassigned to the checker, and no remote publication is represented by this local acceptance.
