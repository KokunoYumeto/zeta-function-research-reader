# Exact failure of consecutive terminal-energy monotonicity

Date: 2026-09-12. Scope: a positive vertical-line moment measure, with a complete reflection-stable two-dimensional packet. This establishes a counterexample to a universal monotonicity assertion for such moment measures. It makes no claim that the displayed measure is the arithmetic measure `nu_Z=|g/h|^2 dt/(2 pi)`.

## The retained measure and packet

On the original line `s=1/2+i t`, take the probability measure with the following atoms. A listed weight in a plus/minus row is the weight at **each** atom.

| `t` | Weight |
|---|---:|
| `0` | `115/288` |
| `+1/4`, `-1/4` | `29/120` |
| `+1/2`, `-1/2` | `13/240` |
| `+3/4`, `-3/4` | `11/2520` |
| `+1`, `-1` | `1/6720` |

All weights are positive. Their sum is one. Symmetry gives every odd moment zero. Direct substitution gives

\[
 \int t^2\,d\nu=\frac1{16},\quad
 \int t^4\,d\nu=\frac3{256},\quad
 \int t^6\,d\nu=\frac{15}{4096},\quad
 \int t^8\,d\nu=\frac{105}{65536}.
\]

For example, after the explicitly declared auxiliary substitution `u=4t`, the total paired masses at `u=1,2,3,4` are
`29/60,13/120,11/1260,1/3360`; their moments of orders `2,4,6,8` are respectively `1,3,15,105`. The measure in the displayed table and all original `s,t` coordinates remain unchanged.

Use
\[
 h(s)=(s-\tfrac34)(s-\tfrac14)=s^2-s+\tfrac3{16},
 \qquad E=\mathbb C[s]/(h),\qquad c=j_h1.
\]
The reflection `rho -> 1-conjugate(rho)` exchanges the two centres. They are distinct, belong to the open critical strip, and each has its full multiplicity one. In the retained monomial basis `1,s`,
\[
 c=\binom10,\qquad
 A=M_s=\begin{pmatrix}0&-3/16\\1&1\end{pmatrix}.
\]

The complete evaluation map is the explicitly typed algebra isomorphism
\[
 T:E\longrightarrow\mathbb C\oplus\mathbb C,
 \qquad [p]\longmapsto(p(3/4),p(1/4)),\qquad
 T=\begin{pmatrix}1&3/4\\1&1/4\end{pmatrix}.
\]
It is well defined because both evaluations annihilate `(h)`. Its determinant is `-1/2`, so it is bijective, and evaluations preserve addition, multiplication and the unit. Moreover
\[
 T A=\operatorname{diag}(3/4,1/4)T,\qquad Tc=(1,1)^{\mathsf T}.
\]
Thus all calculations below have an exact transport back to the original packet coordinates.

## Orthogonal polynomials with exact norms

Put `x=s-1/2` and `v=1/16`, as explicitly named polynomials and a retained constant. The first five monic orthogonal polynomials and their norms are
\[
\begin{array}{c|c|c}
k&q_k(s)&\kappa_k\\\hline
0&1&1\\
1&x&v\\
2&x^2+v&2v^2\\
3&x^3+3vx&6v^3\\
4&x^4+6vx^2+3v^2&24v^4.
\end{array}
\]
Here the inner product is `integral conjugate(P(s)) Q(s) dnu`. On the measure line `conjugate(x)=-x`. Inserting the moment values above into this inner product gives zero for each distinct pair in this table and the displayed positive diagonal norms. This is also directly checked in the accompanying exact script. Positivity on the nine distinct atoms ensures uniqueness of each monic orthogonal polynomial through degree four: a nonzero polynomial of degree at most four cannot vanish at all nine atoms. These are therefore the actual orthogonal polynomials of the stated finite measure.

The same table is obtained for the continuous centered Gaussian `dnu(t)=4/sqrt(2 pi) exp(-8t^2)dt`; its first eight moments equal the displayed ones. The finite positive measure is used here to give rational exact data throughout.

The recurrence through the displayed degrees is
\[
 s q_k=q_{k+1}+\tfrac12q_k-\frac{k}{16}q_{k-1}
 \qquad(0\leq k\leq3),
\]
with the last term omitted at `k=0`, and `a_k=k/16=kappa_k/kappa_{k-1}>0` for `1<=k<=4`. In particular `b_k+conjugate(b_k)=1`, with the required negative sign before `a_k q_{k-1}`.

## The kernels and energy increase

For `N>=1`, define, in the original basis,
\[
 K_N=\sum_{k=0}^N\frac{j_hq_k(j_hq_k)^*}{\kappa_k},
 \qquad L_N=A K_N+K_N A^*-K_N,
 \qquad \epsilon_N=\|K_N^{-1/2}L_NK_N^{-1/2}\|.
\]
The first two residue columns are independent, so these kernels are positive definite. Since `x^2=v` in `E`, the five residue columns are
\[
 j_hq_0=\binom10,\quad
 j_hq_1=\binom{-1/2}1,\quad
 j_hq_2=\binom{1/8}0,\quad
 j_hq_3=\binom{-1/8}{1/4},\quad
 j_hq_4=\binom{5/128}0.
\]
Consequently
\[
 K_3=\begin{pmatrix}53/3&-88/3\\-88/3&176/3\end{pmatrix},
 \qquad
 K_4=\begin{pmatrix}131/6&-88/3\\-88/3&176/3\end{pmatrix},
\]
\[
 L_3=\begin{pmatrix}-20/3&20/3\\20/3&0\end{pmatrix},
 \qquad
 L_4=\begin{pmatrix}-65/6&65/6\\65/6&0\end{pmatrix}.
\]
The difference is the exact positive update `K_4-K_3=(25/6)c c^*`.

The original terminal defect identity is retained as well. The next monic polynomial is
\[
q_5=x^5+10vx^3+15v^2x,
\qquad j_hq_5=\binom{-13/256}{13/128}.
\]
Orthogonality of this polynomial against `q_0,...,q_4` follows by substitution of moments through order nine, with all odd moments zero; its recurrence is `s q_4=q_5+(1/2)q_4-4v q_3`. Direct multiplication of the displayed residue columns proves, for both `N=3` and `N=4`,
\[
 L_N=\frac{j_hq_{N+1}(j_hq_N)^*+j_hq_N(j_hq_{N+1})^*}{\kappa_N}.
\]
Thus the counterexample satisfies both the positive kernel update and the terminal recurrence responsible for the rank-two weight form.

To calculate the energy, transport both forms by the already proved map `T`:
\[
 \widetilde K_3=T K_3T^*
 =\begin{pmatrix}20/3&-2/3\\-2/3&20/3\end{pmatrix},
 \qquad
 \widetilde K_4=T K_4T^*
 =\begin{pmatrix}65/6&7/2\\7/2&65/6\end{pmatrix}.
\]
Writing either transported kernel as `[[a,b],[b,a]]` gives
\[
 \widetilde L=\operatorname{diag}(a/2,-a/2),\qquad
 \det(\widetilde L-\lambda\widetilde K)
 =\lambda^2(a^2-b^2)-a^2/4.
\]
The eigenvalues of `K^{-1/2} L K^{-1/2}` are precisely the generalized eigenvalues of `(L,K)`, since multiplying `L-lambda K` on both sides by `K^{-1/2}` changes its determinant by the nonzero factor `det(K)^{-1}`. The congruence by `T` changes the determinant by the further nonzero factor `|det(T)|^2`; it therefore preserves these eigenvalues. As the Hermitian eigenvalues here are opposite, the energy is their common absolute value. It follows exactly that
\[
 \epsilon_3^2=\frac{25}{99},\qquad
 \epsilon_4^2=\frac{4225}{15136},\qquad
 \epsilon_4^2-\epsilon_3^2=\frac{39875}{1498464}>0.
\]
Thus **the consecutive energy increases from `N=3` to `N=4`**. Both degrees belong to the `N=d+m`, `d=2`, `m>=0` range: they are levels `m=1` and `m=2`.

For comparison, the earlier exact values are `epsilon_1^2=1/4` and `epsilon_2^2=1/3`, which give a second increase; the `N=3,4` example avoids depending on the degree below the `N=d+m` range.

## Scope of the conclusion

This positive, reflection-stable, rational finite moment example disproves universal consecutive monotonicity under the vertical recurrence and positive-kernel hypotheses alone. Its precise connection to the arithmetic construction is the same moment-to-packet map `P -> j_h P`, with the same multiplication operator `A`, complete residue algebra, Christoffel sum, Hermitian defect and energy. Replacing its stated measure by `nu_Z` changes every moment and hence the recurrence and kernel; the example does not establish an increase for that particular arithmetic measure. An arithmetic monotonicity argument would therefore have to use additional proved identities of that measure beyond the vertical recurrence and positivity.

Verification files: `work/check_terminal_energy_monotonicity_20260912.py` and its generated JSON receipt. The checks are exact rational and complex-rational identities; they supplement the explicit derivation above.

Execution result: **88 exact checks passed** in ordinary Python and **88 exact checks passed** with `python -O`. They use explicit exceptions on nonzero differences, including the two generalized characteristic polynomials, and do not depend on Python assertions. Separate receipts are `work/check_terminal_energy_monotonicity_20260912.json` and `work/check_terminal_energy_monotonicity_20260912.optimized.json`.
