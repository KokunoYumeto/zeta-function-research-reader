# PR14: exact tensor trace, layer rank, metric loss, and packet transport

Independent mathematical review, 12 September 2026. Sources read in full: `output/split_zero_rh_tandem_2026-09-12/sources/web_pr14_delivery/Tau_Coherent_Interpolation_Control/NOTE.tex`; current `tex/metric_departure.tex`; relevant aggregate-control proof in `tex/tau_chain.tex`. This note contains written proofs. The finite comparison check at the end supplements those proofs and makes no claim about actual zeta zeros.

## 1. All original spaces and operators

For a complete finite packet put

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\quad
E_h=\mathbb C[s]/h,\quad d=\sum_\rho m_\rho,
\quad A=M_s.
\]

For tensor degree \(k\ge1\), retain the original ordered tensor space

\[
E=E_h^{\otimes k},\quad D_0=\dim E=d^k,\quad
A_k=\sum_{j=1}^k I^{\otimes(j-1)}\otimes A\otimes I^{\otimes(k-j)}.
\]

At the total-degree level \(M\ge k(d-1)\), let \(R=R_{k,M}:E\to\mathcal H_k\) be the actual least-norm representative of PR14, let \(G=R^*R>0\), and let \(G'=G_{k,M+1}>0\). The new source relation layer is the specified Hilbert space

\[
\mathcal E=(I-P_{\mathcal B_{k,M}})\mathcal B_{k,M+1},\qquad
L=\dim\mathcal E=\binom{M+k}{k-1}.
\]

Keep the two original maps \(Y,C:E\to\mathcal E\) from PR14 §8. They satisfy

\[
\Delta=G-G'=Y^*Y,\qquad
W=A_k^*G+GA_k-kG=-(Y^*C+C^*Y).                 \tag{1}
\]

The positive square root provides only the explicitly stated isometry \(G^{1/2}:(E,G)\to\mathbb C^{D_0}\). Define the transported maps, without altering the source maps or their coordinates,

\[
\widetilde Y=YG^{-1/2},\quad \widetilde C=CG^{-1/2},\quad
S=G^{-1/2}WG^{-1/2},\quad \epsilon=\|S\|_{\rm op}.
\]

All Hilbert adjoints use conjugate-linearity in the first input. Thus

\[
S=-(\widetilde Y^*\widetilde C+\widetilde C^*\widetilde Y),\qquad
T=\widetilde Y^*\widetilde Y=G^{-1/2}\Delta G^{-1/2},\quad 0\preceq T\prec I.
\tag{2}
\]

Let

\[
r=\operatorname{rank}Y=\operatorname{rank}\Delta=\operatorname{rank}T
\le\min(D_0,L).
\]

The equality of ranks follows because \(\ker(Y^*Y)=\ker Y\), and both occurrences of \(G^{-1/2}\) are invertible.

## 2. Complete tensor eigenvalue list and nilpotents

On the full CRT factor
\(\bigotimes_j\mathbb C[z_j]/z_j^{m_{\rho_j}}\), the action is

\[
A_k=(\rho_1+\cdots+\rho_k)I+\sum_jN_j,
\quad N_j=z_j\cdot,
\quad \left(\sum_jN_j\right)^{1+\sum_j(m_{\rho_j}-1)}=0.
\tag{3}
\]

The final equality holds term by term in the multinomial expansion: every monomial of the displayed total degree exceeds at least one permitted exponent. The factor has dimension \(\prod_jm_{\rho_j}\). Consequently its only eigenvalue is \(\rho_1+\cdots+\rho_k\), with that algebraic multiplicity. This proves the complete eigenvalue list, including collisions between different ordered tuples, without deleting any nilpotent action.

Write

\[
a_{\boldsymbol\rho}=\sum_{j=1}^k(\operatorname{Re}\rho_j-\tfrac12),\qquad
\mathcal D_k=\sum_{\boldsymbol\rho\in Z^k}
 \left(\prod_jm_{\rho_j}\right)|a_{\boldsymbol\rho}|.
\tag{4}
\]

Every sum below uses this full repeated list of length \(D_0\).

## 3. Sharp trace and boundary-flux inequalities

The following exact generic consequence of (1) is valid for every packet, including packets without a reflection involution:

\[
\boxed{\mathcal D_k\le\tfrac12\|S\|_1
 \le\|\widetilde Y\|_{\rm HS}\|\widetilde C\|_{\rm HS}.}
\tag{5}
\]

Here \(\|S\|_1\) is the sum of the absolute values of its real eigenvalues. There is no missing dimension factor.

**Proof of the first inequality and its complete partial-sum version.** Put \(B=G^{1/2}A_kG^{-1/2}\). An orthonormal invariant flag triangularizes \(B\): one chooses a unit eigenvector, extends it to an orthonormal basis, and iterates on the lower-right compression. Thus \(U^*BU\) is upper triangular with the complete eigenvalue list on the diagonal. In the same basis, \(U^*SU\) has diagonal entries \(2a_j\). For any selected set of \(q\) indices, let \(P\) be its diagonal orthogonal projection and let \(J\) have diagonal \(\operatorname{sign}(a_j)\) on the set and zero elsewhere. Then \(-P\preceq J\preceq P\), and

\[
2\sum_{j\in I}|a_j|=\operatorname{Tr}(J U^*SU).
\]

Diagonalize \(U^*SU\) with unit eigenvectors \(v_l\) and eigenvalues \(\lambda_l\). Since \(|v_l^*Jv_l|\le v_l^*Pv_l\), its right side is at most \(\sum_l|\lambda_l|v_l^*Pv_l\). The weights lie in \([0,1]\) and sum to \(q\). Rearranging them therefore bounds this by the sum of the \(q\) largest numbers \(|\lambda_l|\). Selecting the \(q\) largest \(|a_j|\) proves the stronger family

\[
2\sum_{j=1}^q |a|_{(j)}\le\sum_{j=1}^q\sigma_j(S)
\quad(1\le q\le D_0),                         \tag{6}
\]

where each list is decreasing. The case \(q=D_0\) is the first inequality in (5); \(q=1\) retains the individual spectral constraint \(\epsilon\ge2\max|a_j|\).

**Proof of the second inequality.** Let \(H=\operatorname{sign}(S)\), defined as zero on \(\ker S\). Then \(\|H\|\le1\), and cyclicity of the finite traces and (2) give

\[
\|S\|_1=\operatorname{Tr}(HS)
=-2\operatorname{Re}\operatorname{Tr}(\widetilde C H\widetilde Y^*).
\]

Cauchy–Schwarz for the Hilbert–Schmidt inner product bounds the absolute value of the last trace by \(\|\widetilde C\|_{\rm HS}\|\widetilde YH\|_{\rm HS}\le\|\widetilde C\|_{\rm HS}\|\widetilde Y\|_{\rm HS}\). This proves (5) directly, without invoking a trace-class estimate whose scope has not been proved.

The signed versions, obtained with the projection onto positive or negative diagonal entries in the same Schur basis, are

\[
2\sum_{a_j>0}a_j\le\operatorname{Tr}S_+,
\qquad 2\sum_{a_j<0}(-a_j)\le\operatorname{Tr}S_-.
\tag{7}
\]

For example, \(\operatorname{Tr}(PS)\le\operatorname{Tr}(PS_+)\le\operatorname{Tr}S_+\); each inequality follows from a positive square root inside the trace. Thus no order of noncommuting products is silently assumed.

## 4. Signed rank and exact determinant cost

For any factorization (1),

\[
\boxed{n_+(S),n_-(S)\le\min(\operatorname{rank}Y,\operatorname{rank}C).}
\tag{8}
\]

Indeed, the restriction of the quadratic form of \(W\) to \(\ker Y\) is identically zero. If a strictly positive subspace had dimension greater than \(\operatorname{rank}Y\), it would intersect \(\ker Y\) in a nonzero vector, a contradiction. The same argument applies to negative subspaces and to \(\ker C\). The congruence \(G^{-1/2}\) preserves positive and negative dimensions because it is invertible. This proves (8), including possible kernels.

It follows that

\[
\mathcal D_k\le\tfrac12\|S\|_1\le r\epsilon.
\tag{9}
\]

The sharper signed requirements are \(2\sum_{a_j>0}a_j\le n_+(S)\epsilon\) and \(2\sum_{a_j<0}(-a_j)\le n_-(S)\epsilon\). If \(r=0\), then \(W=0\) and \(\mathcal D_k=0\); one must retain this case instead of dividing by zero. For \(r>0\), (9) is a lower bound \(\epsilon\ge\mathcal D_k/r\). It combines with (6), rather than replacing its \(q=1\) constraint.

The relative Gram loss has exact trace and determinant

\[
\tau=\operatorname{Tr}(G^{-1}\Delta)=\|\widetilde Y\|_{\rm HS}^2,
\qquad p=\frac{\det G'}{\det G}=\det(I-T).
\tag{10}
\]

For \(r>0\), let \(t_1,\ldots,t_r\in(0,1)\) be the positive eigenvalues of \(T\). Then \(\tau=\sum_it_i\), \(p=\prod_i(1-t_i)\), and

\[
1-p\le\tau\le r(1-p^{1/r})<r.                \tag{11}
\]

The left inequality follows by induction from \(\prod_i(1-t_i)\ge1-\sum_it_i\). The right follows from the arithmetic–geometric mean inequality for the positive numbers \(1-t_i\). Hence the original source boundary flux obeys

\[
\boxed{\mathcal D_k^2\le
\operatorname{Tr}(G^{-1}\Delta)\operatorname{Tr}(G^{-1}C^*C)
\le r(1-p^{1/r})\operatorname{Tr}(G^{-1}C^*C).}
\tag{12}
\]

Every matrix in (12) is the actual PR14 moment/next-layer matrix. For a rank-one loss, \(\tau=1-p\) exactly. This is the full-rank tensor extension of the one-dimensional determinant-loss factor, with no assumption that inverse and compression commute.

## 5. Exact tensor departure identity

Let \(\lambda_j\) be the complete eigenvalue list of \(A_k\). Define, in the original metric,

\[
\mathfrak d_G(A_k)=\operatorname{Tr}(G^{-1}A_k^*GA_k)-\sum_j|\lambda_j|^2.
\]

The same triangularization above proves that this is the sum of squared absolute values of all strict upper-triangular entries of \(U^*BU\). It is nonnegative and vanishes precisely when \(B\) is normal. Expanding \((B+B^*-kI)^2\) under the trace gives the exact tensor version of MD2:

\[
\operatorname{Tr}S=2\sum_ja_j,\qquad
\operatorname{Tr}S^2=4\sum_ja_j^2+2\mathfrak d_G(A_k).
\tag{13}
\]

To check the constants, each diagonal contribution is
\(2|\lambda|^2+2\operatorname{Re}\lambda^2-4k\operatorname{Re}\lambda+k^2=4(\operatorname{Re}\lambda-k/2)^2\). Nilpotent entries enter the departure term and remain present.

If the packet is reflection-stable with full orders, PR14 §9 proves symmetry of the generalized spectrum for this same \(G\). Write \(r_W=n_+(S)=n_-(S)\le\min(r,\lfloor D_0/2\rfloor)\). If \(r_W>0\), (13) gives

\[
\epsilon^2\ge\frac{2\sum_ja_j^2+\mathfrak d_G(A_k)}{r_W}
\ge\frac{2\sum_ja_j^2+\mathfrak d_G(A_k)}r.
\tag{14}
\]

Indeed, \(S\) has \(2r_W\) nonzero eigenvalues, each bounded in absolute value by \(\epsilon\). If \(r_W=0\), (13) forces both nonnegative quantities in its right side to vanish. In particular all tensor eigenvalues have the central real part and the retained tensor action is normal for this metric.

The sum in (13) and (14) has the following exact expansion, writing \(\delta_\rho=\operatorname{Re}\rho-1/2\):

\[
\sum_ja_j^2=
k d^{k-1}\sum_\rho m_\rho\delta_\rho^2
+k(k-1)d^{k-2}\left(\sum_\rho m_\rho\delta_\rho\right)^2.
\tag{15}
\]

For \(k=1\), the second term means zero and can be omitted. Formula (15) is obtained by expanding every ordered squared sum: there are \(k\) diagonal positions, and \(k(k-1)\) ordered cross positions. Reflection makes the second term zero. Equation (14) therefore provides an explicit lower bound from the actual metric departure and every multiplicity.

There is also an exact source-layer evaluation of the left side of (13):

\[
\operatorname{Tr}S^2=
2\operatorname{Re}\operatorname{Tr}_{\mathcal E}
 ((\widetilde C\widetilde Y^*)^2)
+2\operatorname{Tr}_{\mathcal E}
 ((\widetilde Y\widetilde Y^*)(\widetilde C\widetilde C^*)).
\tag{16}
\]

Expand \((X+X^*)^2\), with \(X=\widetilde Y^*\widetilde C\), and move the rectangular factors around the trace to obtain (16). The whole expression is nonnegative; its individual real cross term need not be.

## 6. Why signed rank gives no half-plane eigenvalue-count bound

Here is an exact comparison family which simultaneously makes (5), (8), and (9) sharp, preserves a same-metric reflection, retains nontrivial nilpotent chains, and has arbitrarily many eigenvalues in either open half-plane.

Choose an integer \(n\ge1\), \(\delta>0\), and \(a>0\) with \(2na^2<1\). Let \(J_n\) have every entry one, let \(U_n\) have entries one strictly above the diagonal and zero elsewhere, and set

\[
A_+=(\tfrac12+\delta)I_n+2\delta U_n,
\quad A_-=I_n-A_+,\quad A=\operatorname{diag}(A_+,A_-),\quad G=I_{2n},
\]

\[
Y=a(\mathbf1_n^T,\mathbf1_n^T),\qquad
C=(\delta/a)(-\mathbf1_n^T,\mathbf1_n^T).
\]

These are maps to the one-dimensional layer \(\mathbb C\). Direct multiplication gives

\[
W=A^*+A-I=2\delta\operatorname{diag}(J_n,-J_n)=-(Y^*C+C^*Y),
\quad G'=I-Y^*Y>0.
\tag{17}
\]

The strict positivity of \(G'\) follows because the only nonzero eigenvalue of \(Y^*Y\) is \(2na^2<1\). The spectrum of \(W\) is \(2n\delta,-2n\delta\) and \(2n-2\) zeros. Thus \(\operatorname{rank}Y=n_+(W)=n_-(W)=1\). But \(A\) has \(n\) eigenvalues \(1/2+\delta\) and \(n\) eigenvalues \(1/2-\delta\), counting algebraic multiplicity. For \(n>1\), both nilpotent parts have full nilpotence index \(n\): the entry \((U_n^{n-1})_{1n}=1\), and \(U_n^n=0\).

Let \(K\) exchange the two coordinate blocks. The antilinear map \(v\mapsto K\overline v\) satisfies \(AK=K(I-\overline A)\), \(K^*GK=\overline G\), and \(K^*WK=-\overline W\). This verifies same-metric reflection exactly. Finally,

\[
\mathcal D_1=2n\delta=\tfrac12\|W\|_1
=\|Y\|_{\rm HS}\|C\|_{\rm HS}=\epsilon,
\]

so all the displayed sharpness claims are identities. This family proves that the generic factorization and reflection hypotheses alone cannot bound the number of positive-real-part eigenvalues by \(\operatorname{rank}Y\), nor the negative count. It does not assert that any of its chosen eigenvalues are zeta zeros or that these comparison matrices are the canonical arithmetic source matrices. The exact surviving relation is the trace/majorization family (6)–(9), which counts the magnitude and multiplicity of the real parts.

## 7. Nested packets: the exact multivariate transport

Let \(h\mid H\) be full-order packets, let \(m=H/h\), and put \(q=\deg m\), \(D=\deg H=d+q\), \(N=M+kq\). Full orders and the addition of disjoint centres give \(\gcd(h,m)=1\). Let \(\iota:E_h\hookrightarrow E_H\) be the CRT injection retaining the old jets and inserting zero jets at the new centres; it is an injective \(\mathbb C[s]\)-module map. Its tensor power \(I=\iota^{\otimes k}\) satisfies \(A_H^{(k)}I=IA_h^{(k)}\).

Define the explicit polynomial map

\[
S_{hH}^{(k)}:\mathcal P_M^{(k)}\longrightarrow\mathcal P_N^{(k)},
\quad P\longmapsto P\prod_{j=1}^k m(t_j).
\tag{18}
\]

It is injective because the polynomial ring has no zero divisors; the total degree increases by \(kq\). Since \(v_Hm=v_h\), its actual source and jet maps satisfy

\[
\mathcal T_H^{(k)}S_{hH}^{(k)}=\mathcal T_h^{(k)},\qquad
J_{H,k,N}S_{hH}^{(k)}=I J_{h,k,M}.           \tag{19}
\]

The first is equality of the original test functions after taking their Mellin transforms; injectivity of the transform on these spaces proves it. For the second, \(v_h\) has the prescribed complete vanishing at every newly added centre, while the old full jets are unchanged. This also proves that (18) is isometric for the two specified product moment metrics.

For every relation term one has the exact polynomial identity

\[
S_{hH}^{(k)}(h(t_j)P_j)
=H(t_j)P_j\prod_{l\ne j}m(t_l).
\tag{20}
\]

Thus \(\mathcal B_{h,k,M}\subseteq\mathcal B_{H,k,N}\) as actual subspaces of the same \(\mathcal H_k\); the primitive still lies in its same tensor factor with the same \((-1)^{j-1}\) cochain factor. The right numerator has total degree at most \(N-D\), as follows either directly from \(\deg P_j\le M-d\) or by subtracting \(D\) from its relation term. No support label or newly represented zero is deleted.

The low-degree sections obey \(s_H\iota=s_h\). To verify this directly, \(m\operatorname{rem}_h(\varepsilon_hu)\) has degree below \(D\), has the required old jets after multiplication by \(v_H\), and has zero new jets. The uniqueness of the degree-below-\(D\) full-jet interpolant proves equality with the original numerator for \(s_H\iota u\). Tensoring gives \(s_H^{\otimes k}I=s_h^{\otimes k}\).

Write \(B_h=\mathcal B_{h,k,M}\), \(B_H=\mathcal B_{H,k,N}\), and \(F=B_H\cap B_h^\perp\), so \(B_H=B_h\mathbin\oplus^\perp F\). Then

\[
Z=P_F R_{h,k,M}:E_h^{\otimes k}\to F,
\qquad R_{H,k,N}I=R_{h,k,M}-Z,                \tag{21}
\]

\[
\boxed{I^*G_{H,k,N}I=G_{h,k,M}-Z^*Z.}       \tag{22}
\]

Indeed \((I-P_{B_H})(I-P_{B_h})=I-P_{B_H}\); the section identity gives (21). The two summands \(R_{H,k,N}I\) and \(Z\) are orthogonal, proving (22). The exact dimension is

\[
\dim F=\binom{N+k}{k}-D^k-\binom{M+k}{k}+d^k,
\tag{23}
\]

because each full-jet map is onto and each polynomial-to-source map is injective. For \(k=1\) and \(M=n+d\), one has \(N=n+D\) and (23) equals zero, recovering the exact same-level naturality of PR14 §4. For \(k>1\), the additional orthogonal projection in (21) is the proved relation.

Finally, preserving the intertwined action gives the exact control-form transport

\[
\boxed{I^*W_{H,k,N}I=W_{h,k,M}
-\big((A_h^{(k)})^*Z^*Z+Z^*ZA_h^{(k)}-kZ^*Z\big).}
\tag{24}
\]

This follows by substituting (22) in the defining control form. Its extra term is completely specified; the positivity of \(Z^*Z\) alone does not order that term.

## 8. Finite-check scope and review conclusion

The reproducible standalone checker is `output/split_zero_rh_tandem_2026-09-12/scripts/check_coherent_tensor_comparison.py`. It checks 40 exact Boolean validations for the comparison family (17) with \(n=1,2,3,4\), \(\delta=1/5\), \(a=1/(2n)\). For each size it checks factorization, the exact block form, ranks of \(Y,W\), the action/reflection equation, sign reversal of \(W\), strict positivity via the determinant of the rank-one Gram subtraction, zero trace, the exact squared trace, and the full characteristic polynomial. All 40 passed both normally and with Python `-O`. The checker uses explicit Boolean records and process exit status; optimization cannot remove its validations. These 40 records are finite algebra checks, not theorem counts or numerical evidence about arithmetic zeros.

From the package root, reproduce the successful runs with:

```text
python scripts/check_coherent_tensor_comparison.py --output checks/coherent_tensor_comparison.json
python -O scripts/check_coherent_tensor_comparison.py --output checks/coherent_tensor_comparison_optimized.json
```

Adding `--negative-control` deliberately changes the first comparison's map \(C\) while retaining \(W\). Both normal and optimized runs then recorded exactly the intended `n=1:factorization` failure and exited with status 1, with 39 of 40 validations passing. Their receipts are `checks/coherent_tensor_comparison_negative.json` and `checks/coherent_tensor_comparison_negative_optimized.json`. All four receipts record SymPy 1.13.1, the optimization flag, and checker SHA256 `e693d6478d10209e924bbc2d4dde342d5732b25fde3ca94b6985b545419f4776`.

The PR14 total-degree source construction and layer identities support (5)–(16) with their stated types and full multiplicities. The nested-packet extension supports (18)–(24). There is no generic half-plane eigenvalue-count implication of the layer rank, even with the same-metric reflection; (17) is an explicit sharp obstruction and (6)–(9) are the exact surviving spectral relations.

## 9. Review of the actual cumulative TeX fragment

Read the entire final `output/split_zero_rh_tandem_2026-09-12/tex/coherent_tensor_integration.tex` at SHA256 `929ec374aa0f678585bdc8514e9ce92a4982f056b33749efafae6d4ea7d093be`. The first review's missing backslash before `qquad` in CT.17 and map-versus-image wording after CT.15 are corrected in these bytes. The final proof includes the exact same-metric product reflection CT.16a, the original layer parity CT.16b, the equal signed-inertia refinement CT.24a–25, and determinant-loss CT.26.

The complete written derivations CT.1–26 check with the inherited nonempty, full-order actual-packet convention and the previously proved analytic inputs. In particular, the unit congruence CT.3–4 retains multiplication by the arithmetic local unit; the joint relation degree and cochain signs are correct; CT.18 is the actual additional projection for nested multivariate packets; the tensor trace constants and complete multiplicity sums are correct; CT.16b follows from the anti-intertwining of both original generators, not from spectrum alone; and CT.26 uses the positive relative-loss eigenvalues with their actual rank. The cases of zero signed inertia and zero Gram loss are explicitly retained. No mathematical blocker remains in these reviewed fragment bytes. This is a written-proof review, not a Lean or arithmetic-numerical certificate.
