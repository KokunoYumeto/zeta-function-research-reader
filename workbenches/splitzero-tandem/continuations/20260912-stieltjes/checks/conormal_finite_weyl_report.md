# Exact conormal derivative and finite Weyl calibration

The final checker passes **1,076 records: 991 exact equalities or structural checks and 85 negative controls**. Normal Python and `python -O` produce identical record arrays. Each intentional-failure run produces those same 1,076 passing records followed by one false record, and exits with code 1. The ordinary runs exit with code 0. The checker uses explicit exceptions, never Python `assert`.

This is an exact finite calibration of the polynomial quotient, its first conormal thickening, its specified sections, unit transport, and the dual-number algebra map. The proofs for arbitrary degree and tensor order are in `tex/conormal_finite_weyl.tex`. The polynomial units and the one positive metric below are explicitly declared fixtures. The checker does not identify these fixtures with arithmetic theta-unit values and does not test the analytic estimates, global dilation equivariance, or split-semiring construction in CW.26–40. It performs no Lean run.

## Source correlation and reproducibility

All four final JSON receipts have the following identical source and checker SHA256 values:

- Checker `scripts/check_conormal_finite_weyl.py`: `307b9b879a46f56a8701e9f920a085e1a75257de8d931ae22efdff7ce8fac7a9`.
- Proof `tex/conormal_finite_weyl.tex`: `6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a`.
- Original PR20 `sources/web_sum_connection_delivery/Tau_Sum_Connection_Control/NOTE.tex`: `11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687`.

Receipts are `checks/conormal_finite_weyl.json`, `checks/conormal_finite_weyl_optimized.json`, `checks/conormal_finite_weyl_negative.json`, and `checks/conormal_finite_weyl_negative_optimized.json`. They record the Python and SymPy versions, optimization flag, exact fixture polynomials and bases, each named check, and the error field. The final source correction after CW.20 gives the separate exact Hermiticity conditions for each projector and their sum. The independent code and proof audit is `workspace:/work/conormal_weyl_formula_audit_20260912.md`.

From the repository root, the successful normal invocation is:

```powershell
& 'runtime:research-python\python.exe' 'output/split_zero_rh_tandem_2026-09-12/scripts/check_conormal_finite_weyl.py' --output 'output/split_zero_rh_tandem_2026-09-12/checks/conormal_finite_weyl.json'
```

Use `-O` before the script for the optimized invocation, and `--self-test-failure` for the deliberate failure. Choose the corresponding receipt filename in each case.

## Independent construction in the original coordinates

For each original monic polynomial \(h\in\mathbb Q[s]\), with degree \(d\ge1\), the checker constructs

\[
 P=\mathbb Q[s_1,\ldots,s_k],\quad
 I=(h(s_1),\ldots,h(s_k)),\quad E=P/I,\quad E_2=P/I^2.
\]

The basis of \(E\) is the unscaled ordered tensor power basis \(s_1^{a_1}\cdots s_k^{a_k}\), with every \(0\le a_i<d\). The basis of \(E_2\) is that entire basis, followed by each \(h(s_i)\) times that entire basis. For each actual polynomial, repeated monic division in each original variable computes its full \(h\)-adic expansion. Exactly the terms of total \(h\)-degree zero and one survive. Thus 

\[
 E_2\cong E\oplus\bigoplus_{i=1}^k h(s_i)E
\]

is implemented without deleting repeated roots or replacing their local algebras by point values. Every displayed basis vector is independently reduced and checked against its coordinate column. Products \(h(s_i)h(s_j)b\), for every basis monomial \(b\), reduce to zero in \(E_2\); their original polynomial derivatives reduce to zero in \(E\).

The maps \(\pi:E_2\to E\), \(j:E\to E_2\), and \(\iota_N:E^k\to E_2\) are the corresponding projection, canonical remainder section, and conormal inclusion. The operator

\[
 \delta:E_2\longrightarrow E,\qquad
 [p]_{I^2}\longmapsto
 \left[\frac1k\sum_i\frac{\partial p}{\partial s_i}\right]_I
\]

is formed by differentiating each actual polynomial basis vector. The checker independently constructs multiplication by the original sum \(S=\sum_i s_i\) and by the centered sum \(S-k/2\), on both quotients, and verifies the exact scalar-shift maps. With \(Z=M_{S-k/2}\), \(\widehat Z=M_{S-k/2}\) on the respective spaces, it checks

\[
 Z\delta-\delta\widehat Z=-\pi,\qquad
 D_0=\delta j,\qquad
 \widehat Zj-jZ=\iota_N(c_i\ell_i)_i,
\]

\[
 [Z,D_0]=-I+J,\qquad
 J=\frac1k\sum_i M_{h_i'}c_i\ell_i.
\]

Here \(\ell_i:E\to E_{\widehat i}\) extracts the coefficient of \(s_i^{d-1}\), and \(c_i:E_{\widehat i}\to E\) includes polynomials independent of \(s_i\). In the implementation, the square matrix \(L_i\) is the composite \(c_i\ell_i\); it is checked against literal coefficient extraction on every basis vector. These identities are obtained from direct polynomial derivative and multiplication matrices; their right-hand sides do not define the matrices being tested.

For \(P_i=d^{-1}M_{h_i'}L_i\), all idempotence, commutation, and rank identities are checked in the actual power coordinates. Every joint idempotent

\[
 P_T=\prod_{i\in T}P_i\prod_{i\notin T}(I-P_i)
\]

has checked rank \((d-1)^{k-|T|}\), satisfies \(JP_T=(d|T|/k)P_T\), and the joint idempotents sum to the identity. Direct computation of the characteristic polynomial verifies

\[
 \det(tI-J)=\prod_{j=0}^{k}
 \left(t-\frac{dj}{k}\right)^{\binom{k}{j}(d-1)^{k-j}},\quad
 \operatorname{tr}J=d^k,\quad
 \operatorname{rank}J=d^k-(d-1)^k.
\]

The \(d=1\) fixtures retain the endpoint: only the full subset contributes a nonzero joint projector, and \(J=I\).

## Exact bridge to the full conormal derivative

Let \(C:E^k\to E\) be the directly checked row

\[
 C=\frac1k(M_{h_1'},\ldots,M_{h_k'}),\qquad
 L=(L_1,\ldots,L_k)^T:E\to E^k.
\]

The checker verifies \(\delta\iota_N=C\), \(J=CL\), the inclusion \(\operatorname{im}J\subseteq\operatorname{im}C\), and that \(C\) is injective on \(\operatorname{im}L\). If \(r\) is the number of distinct roots of the retained \(h\), then

\[
 \operatorname{rank}C=d^k-(d-r)^k,\qquad
 \operatorname{rank}C-\operatorname{rank}J
 =(d-1)^k-(d-r)^k.
\]

The rank comparison is thus tested through the exact typed factorization \(E\xrightarrow{L}E^k\xrightarrow C E\). The mixed repeated and squarefree fixtures have strict rank gaps, including \(d=3,k=2\), where the correction rank is 5 and the full row rank is 8.

For the local polynomial \(h(w)=w^m(2+3w+w^2)\), with \(m=1,2,3,4\), all input monomials are checked modulo \(w^m\):

\[
 h'(w)w^a\equiv
 \begin{cases}2m w^{m-1},&a=0,\\0,&1\le a<m.\end{cases}
\]

This verifies exactly which coefficient multiplication by \(h'\) sends to the socle. The coefficient map \(\ell\), by contrast, has the explicitly checked type and top-coefficient formula above; the map relating it to the derivative is \(M_{h'}c\ell\). The sealed PR20 source is preserved, and the new proof CW.10 states the local multiplication formula explicitly.

## Full first-order unit and dual-number map

The declared polynomial unit is

\[
 v_{\rm fixture}=\prod_{i=1}^{k}(s_i+5)+\sum_{i=1}^{k}i\,h(s_i),
\]

where the displayed indices run from 1 to \(k\). Both multiplication matrices \(U=M_{[v]_I}\) and \(\widehat U=M_{[v]_{I^2}}\) are tested invertible. The conormal sum vanishes in \(E\), while its full multiplication matrix survives in \(E_2\). The checks retain this sum and its effect on the connection:

\[
 j_U=\widehat UjU^{-1},\quad
 \beta=M_{U^{-1}\delta[ v]_{I^2}},\quad
 D_U=\delta j_U=\beta+UD_0U^{-1},
\]

\[
 [Z,D_U]=-I+UJU^{-1},\qquad
 \widehat Zj_U-j_UZ
 =\widehat U(\widehat Zj-jZ)U^{-1}.
\]

Removing the conormal sum leaves \(U\) unchanged but changes \(D_U\) by precisely

\[
 M_{\partial_\Sigma(\sum_i i h(s_i))}U^{-1}.
\]

The checker verifies that difference directly and rejects deletion of the first-order term. It also verifies the conormal multiplication identity \(\widehat U\iota_N=\iota_N\operatorname{diag}(U,\ldots,U)\). For \(k=1\), the original fixture is \(g=h(s)(s+5+h(s))\), and it checks

\[
 UJU^{-1}=M_{[g']_I}c_1\ell_1U^{-1},\qquad
 M_{[g']_I}=U M_{[h']_I}.
\]

The algebra map

\[
 \Phi:E_2\longrightarrow E[\varepsilon]/(\varepsilon^2),
 \quad a\longmapsto\pi a+\varepsilon\delta a
\]

is checked unital. Multiplicativity is verified by its intertwining with each original generator \(s_i\) on the entire basis of \(E_2\). The target multiplication matrix for \(\Phi(s_i)=s_i+\varepsilon/k\) is

\[
 \begin{pmatrix}M_{s_i}&0\\I/k&M_{s_i}\end{pmatrix}.
\]

Since those original generators generate the source algebra and every source basis column is included, these are full finite algebra-map checks. Direct matrix ranks and kernels verify

\[
 \operatorname{rank}\Phi=2d^k-(d-r)^k,\qquad
 \dim\ker\Phi=(k-1)d^k+(d-r)^k,\qquad
 \ker\Phi\subseteq N.
\]

The image description is checked by the exact codomain transformation \((q,t)\mapsto(q,t-D_0q)\), which carries the matrix of \(\Phi\) to the block map \(\operatorname{diag}(I,C)\). Surjectivity holds exactly in the squarefree fixtures. Isomorphism holds exactly when \(k=1\) and the fixture is squarefree.

## Fixtures and controls

| Original \(h(s)\) | \(k\) | \(\dim E\) | \(\dim E_2\) | \(\operatorname{rank}J\) | \(\operatorname{rank}C\) | \(\operatorname{rank}\Phi\) |
|---|---:|---:|---:|---:|---:|---:|
| \(s-2\) | 1 | 1 | 2 | 1 | 1 | 2 |
| \(s-2\) | 2 | 1 | 3 | 1 | 1 | 2 |
| \(s-2\) | 3 | 1 | 4 | 1 | 1 | 2 |
| \((s-1/3)^2\) | 1 | 2 | 4 | 1 | 1 | 3 |
| \((s-1/3)^2\) | 2 | 4 | 12 | 3 | 3 | 7 |
| \((s-1/3)^2\) | 3 | 8 | 32 | 7 | 7 | 15 |
| \((s-1)^2(s+2)\) | 1 | 3 | 6 | 1 | 2 | 5 |
| \((s-1)^2(s+2)\) | 2 | 9 | 27 | 5 | 8 | 17 |
| \((s-1)(s+2)\) | 2 | 4 | 12 | 3 | 4 | 8 |

Negative controls reject a reversed derivative sign, omission of \(k/2\), omission of the finite correction, omission of \(1/k\), false equality of the two ranks, deletion of the full unit's conormal term, omission of the connection term, untransported corrections, replacement of nonorthogonal projectors by their transposes, and the erroneous local top-coefficient interpretation.

One exact additional fixture checks the CW.20 distinction. For \(h=s^2,k=2\), in basis \((1,s_2,s_1,s_1s_2)\), take

\[
 P_1=\operatorname{diag}(0,0,1,1),\quad
 P_2=\operatorname{diag}(0,1,0,1),\quad
 J=P_1+P_2,
\]

\[
 G=\begin{pmatrix}1&0&0&0\\0&2&1&0\\0&1&2&0\\0&0&0&1\end{pmatrix}.
\]

All leading principal minors of \(G\) are checked positive. Direct multiplication verifies \(J^*G=GJ\), while both equalities \(P_i^*G=GP_i\) fail. For any actual positive metric the exact common coordinate map remains \(A\mapsto G^{1/2}AG^{-1/2}\); its transported \(A\) is Hermitian precisely when \(A^*G=GA\). The source now states that criterion separately for \(P_i\) and \(J\).

The record count enumerates exact finite checks and deliberately false alternatives; it is not a count of theorems. The finite calculations retain their stated fixture scope. The standalone arbitrary-parameter proof and its independent audit remain the mathematical source for the general claims.
