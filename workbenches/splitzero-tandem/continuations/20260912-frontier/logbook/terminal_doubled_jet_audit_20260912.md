# Audit of terminal doubled jets and tail extraction

Date: 2026-09-12. Scope: KT.19–KT.25 and the subsequently added exact projection formulas KT.26–KT.27 in `output/split_zero_rh_tandem_2026-09-12/tex/kernel_terminal_continuation.tex`, with the source resolvent identities in `kernel_resolvent.tex` and the stated derivative bounds and CRT maps in `kernel_convergence.tex`. KT.1–KT.18 are assigned to a separate auditor. No cumulative fragment was edited by this auditor.

## Full confluent divided kernel

The positive line-supported partial fractions give `conjugate(F_n(1-conjugate(z)))=-F_n(z)`. Thus KT.19 preserves the original vertical-line reflection exactly.

At a reflected pair `rho=1-conjugate(sigma)`, write `z=rho+x` and `1-conjugate(w)=rho-y`. In the Taylor series for the divided difference, the coefficient of `x^k y^l` comes only from degree `k+l+1` and equals `(-1)^l F_n^[k+l+1](rho)`. This verifies KT.20, including its sign and the absence of an extra factorial or binomial factor. Reflection and conjugation of the actual entire function `g` preserve zero multiplicity; therefore the maximum derivative order at two selected full reflected factors is `2m_rho-1`.

For nonzero `D=rho+conjugate(sigma)-1`, the coefficient of `x^a y^b` in `(D+x+y)^(-1)` is `(-1)^(a+b) binomial(a+b,a) D^(-a-b-1)`. Multiplication by the separate Taylor series of `F_n(rho+x)` and `conjugate(F_n(sigma+conjugate(y)))` gives exactly both sums in KT.21. Both numerator constants remain present. Applying the complete CRT Taylor map to each rational resolvent column gives the congruence KT.22 with the stated adjoints and inverse maps.

The rational domain must be explicit: the centres used by KT.19–KT.22 must satisfy `q_n(rho) != 0`. Every off-line centre does; a critical quadrature collision does not. The source author has added this domain sentence and retained the polynomial formulas KT.2–KT.14 for collisions.

## Exact doubled sequence and its multiplication

KT.23 is exact as a sequence of `C[s]`-modules. Cancellation in the polynomial domain proves that multiplication by the unchanged `h_off` induces an injection `C[s]/(h_off) -> C[s]/(h_off^2)`. Its image is exactly the reduction kernel, and both maps intertwine multiplication by `s`.

The injection identifies the source module with the square-zero ideal `(h_off)/(h_off^2)`, whose inherited product is `[h_off p][h_off q]=[h_off^2 pq]=0`; the reduction itself is a unital algebra homomorphism. The author added these precise types after audit feedback. The doubled local factors have lengths exactly `2m_rho`, and reduction retains the first `m_rho` coefficients. The injection retains the other local factors of `h_off`; it is the displayed global multiplication map, not an unrecorded pure local shift.

The full algebra projection onto `E_off` has precisely the critical CRT summand as kernel. Its idempotents and inverse Taylor transport are the explicit maps proved in GC.17–GC.19. No critical multiplicity or action is erased from the full polynomial packet.

## Nonzero denominators and every reciprocal coefficient

For an off-line point, the real part of the genuine tail resolvent observation has the strict sign of `Re z-1/2`: the scalar identity is that signed displacement times the squared norm of the tail resolvent applied to its nonzero endpoint vector. Hence `zeta_n(z)` never vanishes there.

The positive measure `|q_n|^2 nu_Z/kappa_n` has total mass one. Its Cauchy transform `H_n^obs` has the same strict real-part sign. Since `q_n` has only critical-line roots, KR.16 implies that the initial error `E_n` is nonzero at every off-line point. The coefficient `a_n` is strictly positive. Thus every reciprocal in KT.24 is defined on a neighborhood of each off-line centre, and is a unit in its doubled local algebra.

From `H=zeta/(1+a_n F_n zeta)` one gets `1/H=1/zeta+a_n F_n`; inserting `E_n=(-1)^n kappa_n H/q_n^2` gives exactly KT.24, including the sign `(-1)^n`, the factor `q_n^2`, and both retained inverses. KT.25 is the coefficient equation for the product of two truncated Taylor series to equal one; it supplies all coefficients through order `2m_rho-1` without binomial factors. GC.13–GC.16 explicitly allow every nonnegative derivative order and apply to these finite lists of error coefficients.

## Required scope of the extraction

The extraction from the off-line tail data yields the terminal Gram on the off-line quotient, using the **same** arithmetic measure `nu_Z`, norms, polynomials, and terminal observation as the full packet. Set `pi:E -> E_off`, `A_off pi=pi A`, and `c_off=pi c`. Its directly defined Gram is

```
S_off = sum_j sigma_j X_off,j X_off,j*,
X_off,j = (A_off-lambda_j I)^(-1)c_off.
```

Every factor exists independently of critical collisions elsewhere. On the full rational chart, `X_off,j=pi X_j` proves `S_off=pi S_n pi*`. Always, the full polynomial kernel projects by `K_off=pi K_{n-1} pi*` and obeys `K_off=kappa_{n-1}^(-1) q_n(A_off) S_off q_n(A_off)*`. This retains the original measure; replacing it by `|g/h_off|^2` would be a different construction.

The critical diagonal and mixed blocks of the original packet remain in the universal polynomial kernel. Off-line Taylor data alone are not asserted to reconstruct those blocks. The author added KT.26–KT.27 and explicitly restricted the tail extraction to the off-line metric, preserving the same measure throughout. These added formulas were read and verified against the displayed definitions above. The source now explicitly defines `A_off=M_s`, `c_off=[1]=pi c` and `pi([p]_h)=[p]_(h_off)` in the retained quotient monomial coordinates; this distinguishes that presentation from the isomorphic idempotent-summand presentation of GC.20. The final coordinate sentence was re-read and verified.

## Final scope pin

At completion of this bounded audit, the whole source file had SHA256 `4E107C0457DC9CC4E5FB46E92042007F2A8F068A019C1BF98B9D08479C53A2D3`. The author is appending independently reviewed material outside the audited subsection, so the stable audit pin is also recorded for the exact UTF-8 bytes starting at `\subsection{The extra jets required to recover the metric from the tail}` and ending immediately before `\subsection{Actual quartet packets close the energy in two volume ratios}`. That subsection contains 7,161 bytes and has SHA256 `92B7A3665FE93B38B49A06491FCA2F711F9A5194713867B1B5357A8234A201EF`.

All requested clarifications are incorporated. No sign, coefficient, type, or domain correction remains within KT.19–KT.27. The appended quartet theorem and later generic example are outside this audit's scope.
