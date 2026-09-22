# Whole-space words through the original source and observation

22 September 2026. WG1–WG16. This proof connects the whole-space word calculation to the actual adjacent source steps, the complete original observation and the earlier cutoff estimates. The accompanying NV1–26, NW1–18, WD1–49 and WS1–61 supply complete proofs, not assumed intermediate claims.

## 1. Which original objects receive the results

Use the full native polynomial \(Q_k\), source \(w_h^{*k}(y)\,dy\), multiplication \(M[f]=[yf]\), and onto observation \(\Lambda:E\to B\) of [RC1–2 and OCP1–7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L7). Here \(k\ge17\), \(k\equiv1\pmod4\), \(q=(k+1)^2\), \(0<\delta<1/2\), \(\gamma>2\), and the stipulated quartet and admitted period remain fixed. The exact pairing of conjugate factors in WD43 proves \(Q_k(y)>0\) for every real \(y\). The full minimum metric is
\[
G_N=(J_N\mathsf H_N^{-1}J_N^*)^{-1},\qquad
q-1\le N\le2q,
\tag{WG1}
\]
where \(J_N\) is the actual polynomial remainder map and \(\mathsf H_N\) is the complete original source moment Gram. WD2–3a proves WG1, including its minimum section and all polynomial relations. The four-return operator is
\[
\mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
\tag{WG2}
\]
The index \(N+d\) used to recover a finite boundary Gram is an auxiliary exact covariance update. All currents and all four returned values are measured at their original \(G_N\).

## 2. Source-degree control of the complete boundary Gram

The source comparison needed by WS30 is available at every finite degree, with explicit degree dependence. Precisely, [FULL_WINDOW_SOURCE_PRODUCTS.tex, FW7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/RETAINED_COMPLETE_PROOF_SOURCES.tex#L120043) gives
\[
\ell(n)=\frac{a_k}{[1+4(n+M_0)^2]^{M_0}},\quad
u=A_k,\quad M_0=21+4m_0,\quad
\ell(n)\|P\|_\sigma^2\le\|P\|_\mu^2\le u\|P\|_\sigma^2,
\tag{WG3}
\]
for every polynomial of degree at most \(n\), with
\(\log(A_k/a_k)=O_h(k+\log k)\). The reference measure has mass \(\sqrt{2\pi}\); its monic norms are
\(h_j=\sqrt{2\pi}\,j!(1/2)_j\).
The source exponent \(M_0\) is fixed and is unrelated to the operator \(M\).

Set \(n_*=2q+d+1\), \(\ell_*=\ell(n_*)\), \(\kappa_*=u/\ell_*\). This is a substitution into WG3, not reuse of a constant that was only defined at degree \(2q+2\). For every \(1\le d\le q/2\),
\[
\log\kappa_*=O_h(k+\log(q+d+2)).
\tag{WG4}
\]
The Gamma multiplication recurrence bounds multiplication on degree \(n\) by \(2(n+1)\); its two off-diagonal entries have size below \(n+1\), and the sum of the two shift norms proves this bound. Applying WG3 to \(yP\) and \(P\) proves
\(\|yP\|_\mu\le2(n+1)\sqrt{\kappa_*}\|P\|_\mu\) at every used degree. Applying the same argument to \(QP\) gives the corresponding bound for the relation measure \(Q^2d\mu\). In particular every zero of a used monic orthogonal polynomial is bounded by this compressed multiplication norm: the three-term recurrence identifies that polynomial with the characteristic polynomial of the real symmetric Jacobi compression. The recurrence itself follows by expanding \(yp_j\) in the orthogonal basis; symmetry removes all entries more than one degree below the diagonal. This is the classical source convention in [Koornwinder, Wong, Koekoek, Swarttouw and Reinhardt, DLMF18.2(iv)](https://dlmf.nist.gov/18.2#iv).

For completeness, retain all three relation blocks of WS25:
\[
R_H=\begin{pmatrix}X&Y\\0&Z_0\end{pmatrix},\qquad
F=[I_d,O_dZ_0],\qquad
F^*G_NF=K_0=
\begin{pmatrix}I-XX^*&-Y\\-Y^*&I-Z_0^*Z_0\end{pmatrix}>0.
\tag{WG5}
\]
Here \(I_d,O_d\) are the consecutive incoming and outgoing orthonormal source classes; \(X\) has its actual, possibly smaller, width. This identity uses every source relation: the high-row Gram at \(N+d\) is \(I-R_HR_H^*\); its lower block and the exact update
\(G_{N+d}^{-1}=G_N^{-1}+O_dO_d^*\)
give \((I+O_d^*G_NO_d)^{-1}=Z_0Z_0^*\).
The high-row cross block then gives \(I_d^*G_NO_d=-YZ_0^{-1}\). Substituting back into the upper block gives \(I_d^*G_NI_d=I-XX^*\), and multiplying by \(\operatorname{diag}(I,Z_0)\) gives WG5. Thus the frame change and its retained metric are explicit.

The roots of \(Q\) and of all source and relation polynomials needed here lie in the bound
\[
R_*=\max\{1,k\sqrt{\delta^2+\gamma^2},2(N+d+1)\sqrt{\kappa_*}\},
\quad B_*=2(N+d)R_*.
\]
For a monic degree-\(n\) polynomial with roots of modulus at most \(R_*\), its coefficient \(h\) positions below the top has modulus at most \((nR_*)^h\), by the elementary symmetric sums. Expanding the monic relation \(QU_{n-q}\) in the monic source basis and eliminating successive leading coefficients therefore bounds its expansion coefficient \(h\) positions below the top by \((2nR_*)^h\): induction gives the coefficient sum bound
\(1+\sum_{j=1}^{h-1}2^j\le2^h\).
For the relevant indices \(i\le n\), \(n-i\le2d\), their normalized coefficient has the additional exact factor
\[
\sqrt{\omega_i/\omega_n}\sqrt{\omega_n/\nu_{n-q}}.
\]
Minimizing WG3 over all monic polynomials gives
\(\ell_*h_i\le\omega_i\le uh_i\).
The high indices satisfy \(h_i\le h_n\), since each ratio \(h_{j+1}/h_j=(j+1)(j+1/2)\) exceeds one there. Consequently
\[
\max(\|X\|,\|Y\|,\|Z_0\|)
\le\delta_*:=d\sqrt{\kappa_*}\,B_*^{2d}
\max_{\max(q,N-d+1)\le n\le N+d}\sqrt{\omega_n/\nu_{n-q}}.
\tag{WG6}
\]
No off-diagonal relation coefficient has been omitted. The factor \(d\) bounds the matrix norm by its maximum entry times the square root of its actual row/column counts.

The full-root monic theorem [RC23, using LRS11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5c69161ca70ee187f41df0bfe786e8b6eebed422/workbenches/splitzero-tandem/continuations/20260922-current-effective-cutoff/CUTOFF_CURRENT_CONNECTION.md#L207) holds for \(0\le j\le2q\). Every \(j=n-q\) in WG6 lies in this interval, since \(n\le2q+d\) and \(d\le q/2\). Its comparison with WG3 and its logarithmic endpoint derivative estimate give
\[
\log\delta_*\le-q\psi((N+1-q)/q)
+O_h\!\left(k\log(q+2)+d[k+\log(q+2)]\right).
\tag{WG7}
\]
Indeed the argument shift is at most \((d+1)/q\); integrating \(1+|\log t|\) near zero bounds its \(q\)-weighted contribution by \(O((d+1)\log(q+2))\). All remaining factors are the explicit terms of WG6 and WG4. For \(d=o(k)\), WG7 tends to a negative constant times \(q\), uniformly across the original source window. Put \(\rho_*=\delta_*+\delta_*^2\); when \(\rho_*<1\), WG5 has
\((1-\rho_*)I\preceq K_0\preceq(1+\rho_*)I\).
This is an effective finite guard with the actual scalar norms in WG6, and its eventual validity has just been proved.

## 3. Signed volume and the four original cutoffs

For a real polynomial \(p\) of degree \(d\le q/2\), let \(c_d\ne0\) be its leading coefficient and let \(B_p\) be the full triangular outgoing matrix of WD6–7. In WG5 put \(D_p=Z_0^{-1}B_p\). The complete current is
\[
W_p=F\begin{pmatrix}0&-iD_p^*\\iD_p&0\end{pmatrix}F^{\dagger_{G_N}}.
\]
The isometry \(FK_0^{-1/2}\) converts its nonzero part to the congruence of the displayed middle matrix by \(K_0^{1/2}\). Its determinant is therefore the middle determinant times \(\det K_0\). The two triangular diagonals are
\[
(B_p)_{ss}=c_d\sqrt{\omega_{N+s}/\omega_{N-d+s}},\quad
(Z_0)_{ss}=\sqrt{\omega_{N+s}/\nu_{N+s-q}}.
\]
They cancel only the indicated intermediate norms, proving the exact identity
\[
\operatorname{pdet}W_p=(-1)^d|c_d|^{2d}
\det K_0\prod_{s=1}^{d}\frac{\nu_{N+s-q}}{\omega_{N-d+s}}.
\tag{WG8}
\]
Here pdet is the product of every nonzero eigenvalue, with sign. Original coefficient conjugation sends \(W_p\) to \(-W_p\), so those eigenvalues pair as \(\pm\sigma_j\), \(\sigma_j>0\). Every factor in WG8 is independent of the lower coefficients of \(p\). Thus the full signed product is exactly unchanged under every real change of lower coefficients with fixed \(c_d\), even unbounded changes.

Use WG3 for both monic norms in WG8. The relation comparison uses all \(Q^2d\mu\); its Gamma ratio contributes \(2q\psi((N+s-q)/q)\), and the remaining factorial ratio \(h_{N+s}/h_{N-d+s}\) has logarithm \(O(d\log(q+2))\). Summing \(d\) factors, using the endpoint shift bound from WG7 and \(|\log\det K_0|\le2d\max\{-\log(1-\rho_*),\log(1+\rho_*)\}\), proves, for \(d=o(k)\),
\[
\sum_{j=1}^{d}\log\sigma_j
=d\log|c_d|+dq\psi((N+1-q)/q)
+O_h(dk\log(q+2)+d^2\log(q+2)).
\tag{WG9}
\]
Applying WG2 at the exact parameters \(0,1/q,1,1+1/q\) gives
\[
\mathcal R\sum_{j=1}^{d}\log\sigma_j
=2d[\psi(0)-\psi(1)]q
+O_h(dk\log(q+2)+d^2\log(q+2)).
\tag{WG10}
\]
Its error divided by \(dq\) tends to zero. The leading coefficient must be the same word at all four cutoffs; then its logarithm cancels exactly. The original kernel-return constant remains \(C_\partial=2J(1)\); it is a different defined functional of the same \(\psi\), connected by the proved identity
\[
C_\partial=8\int_0^1\psi(s)\,ds+4\psi(0)-8\psi(1).
\]
This is the published [DF15–16 correction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/OBSERVED_DEFORMATION_AND_CURRENT.md). The new outward integer enclosure in WS61 strengthens its certificate; it does not reopen the sealed027 source. The exact whole-space formulas WG5 and WG8 remain valid at all \(d\le q/2\), without extending the asymptotic small-\(d\) guard beyond its proof.

## 4. Native source activation and the full observed image

NW1–18 proves the following new statement using the actual source column:
\[
D(t)=G_N^{-1}+t\,b_{N+1}b_{N+1}^{\mathsf T}/\omega_{N+1},
\qquad
\operatorname{In}W_{p,t}=(d,d,q-2d)
\quad(0\le t\le1,\ 1\le d\le q/2).
\tag{WG11}
\]
For \(2d<q\) its explicit congruence eliminates the last row/column by the exact skew identity \(a^{\mathsf T}B_N^{-1}a=0\). For \(2d=q\), its Pfaffian is the affine combination of the two nonzero, same-sign endpoint Pfaffians; the positive determinant orientation of every \(q\)-column consecutive source frame is proved there by an explicit measure pushforward. These arguments retain the moving radical, including the entire original kernel dimension.

Let \(m=\dim\ker\Lambda\). For each \(t\), put
\[
Q_B(t)=(\Lambda D(t)\Lambda^*)^{-1},\quad
J_t=D(t)\Lambda^*Q_B(t)^{1/2}.
\]
Then \(J_t^*G(t)J_t=I_B\). If \(H_+(t)\) is any positive \(d\)-dimensional subspace of the full current, the dimension formula gives
\(\dim(H_+(t)\cap\operatorname{ran}J_t)\ge d-m\).
The isometry pulls this intersection to a positive subspace of the actual observed current. Conversely any positive observed subspace maps into a positive full subspace of dimension at most \(d\). The same argument for negative subspaces proves uniformly throughout the native step
\[
\boxed{(d-m)_+\le n_\pm(J_t^\dagger W_{p,t}J_t)\le d.}
\tag{WG12}
\]
At \(d=q/2\), its nullity is at most \(m\), because \(\dim B=q-m\) and the two lower bounds sum to \(q-2m\).

On the actual size-five orbit domain, the exact invariant restriction theorem [OQX3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/RETAINED_COMPLETE_PROOF_SOURCES.tex#L11702) gives \(m=8k-16\). Hence every half-degree native step retains at least
\[
\boxed{\frac q2-m=\frac{(k-3)(k-11)}2}
\tag{WG13}
\]
observed directions of each sign. The dimension theorem's size-five domain is retained; for any other observation WG12 uses its actual \(m\). This proves a quantitative obstruction to a positive semidefinite observed half-degree current throughout the original source step, and identifies the positive and negative observed spaces through \(J_t\). It does not select a sign for a prescribed terminal vector.

## 5. The collision data now determine source curvature

Use the original adjacent paths \(N=q-1\to q\) and \(N=2q-1\to2q\), separately. Write \(\Phi_i\) for the marked current at an endpoint, \(\tau_i=\operatorname{tr}W_{B,i}\), and retain each endpoint's own observed source columns \(u_i,v_i\), \(a_i=\|u_i\|^2\), \(r_i=u_i^*v_i\). The complete area estimate gives \(a_id_i-|r_i|^2>0\).

For \(F_i(\sigma)=(\epsilon_i v_i+\sigma u_i)u_i^*\), multiplication gives \(F_i^2=(a_i\sigma+\epsilon_i r_i)F_i\). At \(\sigma_{*,i}=-\epsilon_i r_i/a_i\), the generator is
\(\epsilon_i\sqrt{a_id_i-|r_i|^2}\,h_i g_i^*\) in the actual current-plane isometry. It is nonzero square-zero. The matrices \(I,F_i\) are linearly independent: a scalar multiple of \(I\) that is nilpotent must be zero, whereas this generator is nonzero. The map from the dual-number algebra sending its generator to \(F_i\) is consequently injective and onto this two-dimensional algebra. Tracing the rank-one boundary term gives \(\tau_i=-2\epsilon_i\Im r_i=2a_i\Im\sigma_{*,i}\), retaining the positive real \(\epsilon_i\).

For the native source column \(u=b_{N+1}/\sqrt{\omega_{N+1}}\), put \(z=\Lambda u\), \(\beta=z^*Q_B(0)z\), \(w=|z^*Q_B(0)\xi|^2\), and
\[
\chi_{\rm coll}=a_{N+1}\Im\sigma_{*,N+1}-a_N\Im\sigma_{*,N}.
\]
The exact minimum-map calculation NV1–9 gives
\[
\boxed{\Phi(t)=
\frac{(1-t)\Phi_N+t(1+\beta)\Phi_{N+1}}{1+\beta t}
+\frac{2t(1-t)w\,\chi_{\rm coll}}{(1+\beta t)^2}.}
\tag{WG14}
\]
Thus the new collision datum supplies the curvature coefficient of the actual marked source path. With the explicitly invertible coordinate
\(\lambda=(1+\beta)t/(1+\beta t)\),
\[
\boxed{\frac{d^2\Phi}{d\lambda^2}=-\frac{4w}{1+\beta}\chi_{\rm coll},
\quad t_{\rm peak}=\frac1{\beta+2},
\quad \Phi(t_{\rm peak})-\frac{\Phi_N+\Phi_{N+1}}2
=\frac{w}{2(1+\beta)}\chi_{\rm coll}.}
\tag{WG15}
\]
The support weights cannot be suppressed: the two endpoints generally have different \(a_i\) and different source metrics. NV16–20 carries the earlier doubled-rate terminal support estimate into the factor \(w/(1+\beta)\), with its full finite error.

The exact whole-step sign criterion follows by putting
\(\kappa=2w\chi_{\rm coll}/(1+\beta)\).
For nonnegative endpoint values \(A=\Phi_N,B=\Phi_{N+1}\), the path is nonnegative precisely when
\[
\boxed{\kappa\ge-(\sqrt A+\sqrt B)^2.}
\tag{WG16}
\]
Indeed division of \((1-\lambda)A+\lambda B+\kappa\lambda(1-\lambda)\) by \(\lambda(1-\lambda)\) reduces the question to the infimum of \(A/\lambda+B/(1-\lambda)\). Subtracting \((\sqrt A+\sqrt B)^2\) yields
\([\sqrt A(1-\lambda)-\sqrt B\,\lambda]^2/[\lambda(1-\lambda)]\).
The zero-endpoint limits give the same criterion. NV21–24 also proves the complete negative cone and its boundary source coordinate. Actual endpoint values and weighted collision displacements remain the precise scalar data to calculate; no value is supplied by the sign count alone.

## 6. Earlier results now receiving the stronger calculation

The finite WS1–24 statements are supported by the independent complete WD1–49 derivation, including all rational denominator maps, repeated factors, isotropic extensions and high-degree divisor congruences. WS25–33 receives the degree-explicit comparison WG3–10. The mixed quartic construction WS36–38 retains the full arithmetic mixed maps \(C=P_KM|_{K^\perp}\), \(D=P_BM|_K\). Its native rank bound uses both the size-five dimension above and the original nonzero four-corner conductor condition; the complete coefficient proof of \(\dim K_8\le128\) is retained at [the bounded-observation source, equations10–13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/RETAINED_COMPLETE_PROOF_SOURCES.tex#L332958). Its phase orbit keeps the observation but has the exact action defect \(MU_\theta-U_\theta M=(e^{i\theta}-1)(PM P_K-P_KMP)\); it therefore supplies whole-fibre sign witnesses and the map recording their change of arithmetic class.

The general source pencil WS39–44 is retained with all singular blocks. NW11–16 and WG11 prove the stronger constant-inertia result for the actual adjacent polynomial source; WG12–13 transports its forced signs through the moving original quotient. The latest [EE1–48](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4ba9285b66af58a6d58fc502a494c1fb45ca5b79/workbenches/splitzero-tandem/continuations/20260922-support-transport/EVOLUTION_EXTENSION_PROOF.md) already proves the intrinsic and measured inverses on the longer stated clock, as well as all fixed \(b>0\). WS46–54 supplies an additional direct full-characteristic-polynomial contour derivation; its narrower description of what remains open is superseded by EE, not promoted into a new missing task.

The unfinished signed scalar is still the actual imaginary pairing of the retained terminal class, now joined by exact endpoint/trace and collision receivers WG14–16. The next calculation should evaluate those actual coefficient-dependent endpoint traces or pairings, with the complete source minimum, rather than repeat the already established whole-space signatures or recovery maps.
