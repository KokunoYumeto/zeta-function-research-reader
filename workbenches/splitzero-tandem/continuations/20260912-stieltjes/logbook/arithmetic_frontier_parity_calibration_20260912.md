# Exact calibration of the arithmetic frontier parity identities

Date: 2026-09-12. Status: completed exact rational calibration. The proof source is `tex/arithmetic_frontier_parity.tex` in `output/split_zero_rh_tandem_2026-09-12`; no TeX or cumulative-reader file was changed by this lane.

The delivered checker `scripts/check_arithmetic_frontier_parity.py` passes **739/739** explicit Boolean validations in ordinary Python and under `python -O`. Both negative controls exit with status 1 and exactly the same three failed identities. This is an independent finite Gaussian model, with comparison packets whose specified roots are not asserted to be zeros of zeta. It does not compute actual theta moments, certify arithmetic asymptotics, or establish an RH estimate. It is written mathematics with exact symbolic execution; no Lean formalization or Lean process is involved.

## Retained Gaussian measure and monic polynomials

The original measure chosen for this comparison is

\[
s=\tfrac12+it,\qquad d\nu(t)=\sqrt{8/\pi}\,e^{-8t^2}\,dt,
\qquad \kappa_0=1,\qquad \operatorname{Var}(t)=\tfrac1{16}.
\]

The mass is part of this chosen measure. No subsequent rescaling of the measure, polynomial, quotient generator, unit, or interpolation matrix is performed. The original monic recurrence is

\[
q_0(s)=1,\quad q_1(s)=s-\tfrac12,\quad
q_{n+1}(s)=(s-\tfrac12)q_n(s)+\frac n{16}q_{n-1}(s),
\quad \kappa_n=\frac{n!}{16^n}.
\]

It follows directly that

\[
sq_n=q_{n+1}+\tfrac12q_n-\frac n{16}q_{n-1}.
\]

The checker retains this negative lowering sign. It constructs `q_0,...,q_7` as polynomials in the original variable `s`, checks their leading coefficients, checks every reflection identity `q_n(1-s)=(-1)^n q_n(s)`, and checks every recurrence needed for those polynomials.

Their Gram entries are evaluated independently from the recurrence. For every polynomial `P(t)`, expand its original coefficients and use

\[
\int t^{2j+1}\,d\nu=0,\qquad
\int t^{2j}\,d\nu=(2j-1)!!\,16^{-j}.
\]

The odd moments vanish by `t↦-t`. For the even moments, the density derivative is `-16t` times the density. Integration by parts, whose boundary term is zero because a polynomial times `e^{-8t^2}` tends to zero at both ends, gives the recursion `m_{2j}=(2j-1)m_{2j-2}/16`. The initial Gaussian integral is the displayed mass one, and this proves the formula. Substitution of `s=1/2+it` into `conjugate(q_n(s))*q_m(s)` then computes all 64 entries for `0≤n,m≤7`. They agree exactly with `δ_nm n!/16^n`. No numerical quadrature or floating-point arithmetic occurs.

## Original quotient, complete repeated jets, and unit

For a monic degree-`d` polynomial `h`, the target basis is always

\[
(1,s,\ldots,s^{d-1})\quad\text{in }\mathbb C[s]/(h).
\]

If `r_h(P)` is the column of the complete polynomial remainder of `P` in this basis, the matrices are constructed column by column as

\[
A=[r_h(s),r_h(s^2),\ldots,r_h(s^d)],\qquad
C=[r_h(1),r_h(1-s),\ldots,r_h((1-s)^{d-1})],
\]
\[
\upsilon(s)=1+(s-\tfrac12)^2,\qquad
U_\upsilon=I+(A-\tfrac12I)^2.
\]

Thus `A` is the original multiplication by `s`, and `C` is the original linear reflection. They are never replaced by diagonal matrices in the calculations.

The first packet is

\[
h_{\rm rep}=(s-\tfrac14)^2(s-\tfrac34)^2,\qquad d=4,\quad k=1,
\quad M\in\{4,5,6\}.
\]

The checker verifies that the full characteristic polynomial of `A` is exactly `h_rep`, that `h_rep(A)=0`, and that `(A-1/4 I)(A-3/4 I)≠0`. The latter identity explicitly prevents a semisimple replacement. The complete jet map is

\[
J:P\longmapsto(P(\tfrac14),P'(\tfrac14),P(\tfrac34),P'(\tfrac34))^T.
\]

In the original monomial basis it is the invertible matrix whose rows are respectively `(ρ^j)_{j=0}^3` and `(jρ^{j-1})_{j=0}^3`, for `ρ=1/4,3/4`, with the `j=0` derivative entry zero. Exact multiplication verifies

\[
JA=
\operatorname{diag}\left(
\begin{pmatrix}\tfrac14&0\\1&\tfrac14\end{pmatrix},
\begin{pmatrix}\tfrac34&0\\1&\tfrac34\end{pmatrix}
\right)J.
\]

The unit is retained under that same typed map:

\[
JU_\upsilon J^{-1}=
\operatorname{diag}\left(
\begin{pmatrix}\tfrac{17}{16}&0\\-\tfrac12&\tfrac{17}{16}\end{pmatrix},
\begin{pmatrix}\tfrac{17}{16}&0\\\tfrac12&\tfrac{17}{16}\end{pmatrix}
\right).
\]

Both nonzero derivative coefficients are checked. The subsequent metric and frontier calculations remain in the original monomial basis; this jet map is an additional exact verification of the retained nilpotents.

The second packet is

\[
h_{\rm pair}=(s-\tfrac14)(s-\tfrac34),\qquad d=2,\quad k=2,
\quad M\in\{2,3,4\}.
\]

Here the same original polynomial unit has the exact remainder `17/16`, since `(s-1/2)^2=1/16` in this quotient. Thus the retained tensor unit acts by `(17/16)^2 I`. This case does not have a nonconstant quotient unit; the first packet above supplies the nonconstant local-unit calibration. This distinction is recorded in each receipt together with the original polynomial and its exact remainder.

For `k` factors, the coordinate basis is the lexicographic product of the original monomial bases, with the last coordinate varying fastest. For example the two-factor basis is `(1⊗1,1⊗s,s⊗1,s⊗s)`. The generator and reflection are

\[
A_k=\sum_{j=1}^k I^{\otimes(j-1)}\otimes A\otimes I^{\otimes(k-j)},
\qquad C_k=C^{\otimes k}.
\]

Every tensor column is computed as

\[
z_\alpha=\bigotimes_{j=1}^k U_\upsilon r_h(q_{\alpha_j}),\qquad
\kappa_\alpha=\prod_{j=1}^k\frac{\alpha_j!}{16^{\alpha_j}}.
\]

## Exact interpolation and the two frontier maps

For each specified `(k,M)`, the checker constructs the complete inverse interpolation matrix and its inverse:

\[
\mathcal C_M=\sum_{|\alpha|\le M}\frac{z_\alpha z_\alpha^*}{\kappa_\alpha},
\qquad G_M=\mathcal C_M^{-1}.
\]

It verifies Hermitian symmetry and every leading principal minor of both matrices is strictly positive. This is an exact Sylvester-criterion certificate of positive definiteness; the matrix inverses therefore exist. Every entry of `C_M`, `G_M`, `A_k`, `C_k`, `F`, `E_+`, `Omega` and the resulting `W_M` is written as an exact rational string in the normal receipt's `cases[].matrices` object.

The multi-indices are ordered with their first component increasing, then recursively in the remaining components. For each frontier index `|β|=M+1`, set

\[
F_\beta=z_\beta,\qquad
(E_+)_\beta=\sum_{j:\beta_j>0}\frac{\beta_j}{16}z_{\beta-e_j},
\qquad \Omega_{\beta\beta}=\kappa_\beta.
\]

The incidence matrix has exactly `L_{αβ}=β_j/16` if `α=β-e_j`, with summation over incidences. The checker independently reconstructs `E_+=ZL`, with `Z=[z_α]_{|α|=M}`. It verifies all of the following full matrix identities:

\[
C_k^2=I,\quad C_kA_k=(kI-A_k)C_k,\quad
C_k^*G_MC_k=G_M,\quad C_k^*W_MC_k=-W_M,
\]
\[
C_kF=\eta F,\qquad C_kE_+=-\eta E_+,\qquad
F^*G_ME_+=0,\qquad \eta=(-1)^{kd+M+1},
\]
\[
A_k\mathcal C_M+\mathcal C_MA_k^*-k\mathcal C_M
=F\Omega^{-1}E_+^*+E_+\Omega^{-1}F^*,
\]
\[
W_M=A_k^*G_M+G_MA_k-kG_M
=G_M(F\Omega^{-1}E_+^*+E_+\Omega^{-1}F^*)G_M,
\]
\[
\mathcal C_{M+1}=\mathcal C_M+F\Omega^{-1}F^*.
\]

The packet reflection and original unit parity are also explicitly validated before these identities are tested.

## Full spectra, ranks, volume, and departure

To avoid introducing square roots in the exact arithmetic, let

\[
L_M=G_M^{-1}W_M,\quad
B_F=\Omega^{-1}F^*G_MF,\quad
B_E=\Omega^{-1}E_+^*G_ME_+,\quad Q=B_FB_E.
\]

These are the original matrices with the indicated source and target sizes. The positive operator in AP.15 is related by explicit maps: if `mathsf A=Omega^{-1/2} F^*G_M F Omega^{-1/2}` and `mathsf B=Omega^{-1/2} E_+^*G_M E_+ Omega^{-1/2}`, then

\[
Q=\Omega^{-1/2}(\mathsf A\mathsf B)\Omega^{1/2}.
\]

The characteristic polynomials of `mathsf A mathsf B` and `mathsf A^{1/2} mathsf B mathsf A^{1/2}` agree, including their zero factors, by `det(lambda I-XY)=det(lambda I-YX)` applied to `X=mathsf A^{1/2}` and `Y=mathsf A^{1/2} mathsf B`. Thus the computed source characteristic polynomial is that of the AP positive operator, including all zero multiplicities. Also `L_M` is conjugate to the original relative self-adjoint operator `S_M` by the displayed positive-metric isometry. No original matrix is discarded.

With `D=d^k` and `r=binom(M+k,k-1)`, the checker verifies

\[
\operatorname{Tr}(L_M^2)=2\operatorname{Tr}(Q),
\]
\[
\boxed{\lambda^{2r}\det(\lambda I_D-L_M)
=\lambda^D\det(\lambda^2I_r-Q).}
\]

This is a polynomial identity evaluated exactly, rather than a comparison of approximate eigenvalues. Define `p=rank(F Omega^{-1} E_+^*)`; the checker verifies `rank(W_M)=2p`, `rank(Q)=p`, and that the full zero multiplicity of `det(lambda I_D-L_M)` is `D-2p`. The reflection weight identity and positive metric above imply equal positive and negative inertias: reflection is an invertible isometry carrying an eigenspace of the relative operator at `lambda` to the eigenspace at `-lambda`. These exact rank tests therefore give both inertias equal to `p`.

The original determinant quotient is independently computed from the two inverse matrices and checked against its complete source determinant:

\[
\pi_M=\frac{\det G_{M+1}}{\det G_M},\qquad
\pi_M\det(I_r+B_F)=1,\qquad0<\pi_M\le1.
\]

For `k=1`, `r=1`; the computed spectrum verifies the exact scalar identity

\[
\epsilon_{1,M}^2
=\frac{(F^*G_MF)(E_+^*G_ME_+)}{\Omega^2}.
\]

The quotient generator retains each eigenvalue with its full algebraic multiplicity. The departure is computed from its original matrix as

\[
\mathfrak d_M^{(k)}=
\operatorname{Tr}(G_M^{-1}A_k^*G_MA_k)
-\sum_{i_1,\ldots,i_k}|\rho_{i_1}+\cdots+\rho_{i_k}|^2.
\]

It is nonnegative in every case, and the checker verifies the complete AP.22 identity

\[
\mathfrak d_M^{(k)}=\operatorname{Tr}(Q)
-2\sum_{i_1,\ldots,i_k}
\left(\operatorname{Re}(\rho_{i_1}+\cdots+\rho_{i_k})-\tfrac k2\right)^2.
\]

The six requested cases all have `D=4`, `p=1` and

\[
\det(\lambda I_D-L_M)=\lambda^2(\lambda^2-R),\qquad
\det(\lambda I_r-Q)=\lambda^{r-1}(\lambda-R).
\]

Every value below is exact. Thus `R=epsilon^2` in the two-factor cases as well, with its rank and zero factors certified by the full characteristic identities.

| Packet | k | M | r | Gamma | pi | R | departure |
|---|---:|---:|---:|---:|---:|---:|---:|
| repeated | 1 | 4 | 1 | 5/16 | 30/367 | 13817/4512 | 11561/4512 |
| repeated | 1 | 5 | 1 | 3/8 | 846/4001 | 1063235/827952 | 649259/827952 |
| repeated | 1 | 6 | 1 | 7/16 | 77070/492941 | 262414601/140963232 | 191932985/140963232 |
| pair | 2 | 2 | 4 | 3/8 | 9/289 | 7/5 | 2/5 |
| pair | 2 | 3 | 5 | 1/2 | 45/988 | 126/85 | 41/85 |
| pair | 2 | 4 | 6 | 5/8 | 7225/97344 | 157851/134368 | 23483/134368 |

## Exact incidence positivity

The checker computes

\[
\Gamma=\max_{|\alpha|=M}\sum_j
\left(\frac{\alpha_j+1}{16}+(k-1)\frac{\alpha_j}{16}\right)
\]

and verifies every original row sum of `Omega_M L Omega^{-1} L^*`. It proves each of the following Hermitian matrices positive semidefinite by checking all their nonempty principal minors exactly:

\[
\Gamma Z\Omega_M^{-1}Z^*-E_+\Omega^{-1}E_+^*,\quad
\Gamma\mathcal C_M-E_+\Omega^{-1}E_+^*,\quad
\mathcal C_M-Z\Omega_M^{-1}Z^*.
\]

Their order is four in the requested cases, so there are exactly 15 nonempty principal minors per matrix. The supplementary zero cases have order two. The source matrix `F^*G_MF` is also tested by all principal minors when its order is at most four; at every source size its Gram representation proves positivity directly, since `x^*F^*G_MFx=(Fx)^*G_M(Fx)≥0` and `G_M` has the exact positive-definiteness certificate above.

An independent sub-lane derived the complete incidence bound without using the main checker. Its report is `work/frontier_incidence_independent_review_20260912.md`. For `k=1`,

\[
\Gamma\Omega_M^{-1}-L\Omega^{-1}L^*=0.
\]

For `k=2`, order the lower indices as `(i,M-i)`, `0≤i≤M`, and retain an arbitrary positive original measure mass `m`. The exact factorization is

\[
\Gamma\Omega_M^{-1}-L\Omega^{-1}L^*
=\sum_{i=0}^{M-1}
\frac{16^{M-1}}{m^2i!(M-i-1)!}
(e_i-e_{i+1})(e_i-e_{i+1})^*.
\]

The report proves every entry and every coefficient, provides all six explicit incidence matrices and row-sum matrices, and checks the factorization with rational arithmetic at masses `m=1` and `m=7/3`. The independent report's 12 rational runs do not rely on numerical PSD decisions. Congruence by the original `Z` yields the exact first matrix bound above; adding the full lower-degree sum yields the second. The scalar `k=1` bounds `epsilon^2≤Gamma B_F≤Gamma(pi^{-1}-1)` are additionally checked as exact rational inequalities.

## Zero-rank controls and construction audit

Two supplementary cases test the zero-rank alternatives in AP.15, rather than inferring them from the six positive-rank cases. Their packet is

\[
h_0=q_2(s)=(s-\tfrac12)^2+\tfrac1{16},\qquad
\rho=\tfrac12\pm\tfrac i4,\qquad k=1,
\]

and the exact original unit remainder is `15/16`. The two roots, complete degree two, unit, and reflection are retained. At `M=1`, `F=r_h(q_2)=0`, `E_+` is nonzero, `p=0`, `W=0`, and `pi=1`. At `M=2`, `F` is nonzero, `E_+=a_3r_h(q_2)=0`, `p=0`, `W=0`, and `pi=3/5`. Both have full characteristic polynomial `lambda^2` and departure zero. These test that zero relative weight does not require zero metric change.

During construction, an attempted supplemental degree-one central packet with an even unit failed the parity checks. That proposed fixture violated the original unit parity `C U=(-1)^d U C`; it was not an admissible AP fixture and was replaced by the explicit even-degree Gaussian-node packet above. The final checker now validates the packet and unit parity themselves in every case, so that mismatch cannot silently re-enter. No AP identity was altered to accommodate a fixture.

## Failure controls, receipts, and reproducibility

The negative control reverses exactly the first predecessor frontier column in the repeated packet at `M=4`, while retaining the original metric, generator, arithmetic unit, and all degree data. That changes a mathematical sign; it does not insert an unconditional false test. Both normal and optimized execution detect exactly:

1. `repeated_k1_M4:incidence_predecessors`;
2. `repeated_k1_M4:exact_displacement`;
3. `repeated_k1_M4:exact_weight`.

The negative receipts contain **736 passes and three failures out of 739**, and both runs exit 1. The positive receipts contain **739 passes out of 739** and both runs exit 0. Checks use explicit Boolean records and a nonzero failure exit, with no Python `assert` statements, so `-O` cannot disable them. Any unexpected exact-calculation or matrix-inversion exception also terminates execution without writing a success receipt.

From the output root, reproduce with the research Python environment containing SymPy 1.13.1:

```text
python scripts/check_arithmetic_frontier_parity.py
python -O scripts/check_arithmetic_frontier_parity.py --output checks/arithmetic_frontier_parity_optimized.json
python scripts/check_arithmetic_frontier_parity.py --negative-control --output checks/arithmetic_frontier_parity_negative.json
python -O scripts/check_arithmetic_frontier_parity.py --negative-control --output checks/arithmetic_frontier_parity_negative_optimized.json
```

The four receipts are under `checks/` with exactly those names. They contain all check records, complete case parameters, exact matrix entries, characteristic polynomials, mathematical scope, source hash, script hash, Python optimization status, and SymPy version.

Pinned hashes at completion:

- Checker SHA-256: `0aeffe803bb23679effa5afc8b8932d7416f68886019f393b6853ebabae75734`.
- AP proof SHA-256: `b93922a11dd9658183a59eabc9cc2d0a7fa214895af23f4ad3d38a686b0a9987`.
- Independent incidence report SHA-256: `1c3c107178a08025b3b67a2ed9aad7fbeacea9a5fb0f9dc38c303baadb0c48c1`.

This lane edited only its new checker, four new receipts, this report, and its child's new independent incidence report. The cumulative TeX, PDF build, source ZIPs and GitHub publication remain with the parent lane.
