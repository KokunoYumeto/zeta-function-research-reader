# The original kernel value and its receiving calculations

This continuation checks all six September22 arrivals together. The full kernel manuscript supplies a fixed-symbol argument. The independent PJ1–69 proof now supplies the complete growing-jet estimate and diagonal asymptotic, and EL1–14 proves the exact identification of its constant. Together they establish the kernel value below. The uniform-return, static-memory, two-response and frequency notes retain their own original maps and receive this value through the equations stated and proved here.

## CK1. Actual arithmetic objects

Fix the programme's stipulated simple quartet \(0<\delta<1/2\), \(\gamma>2\), its admitted original period and branch, and its arithmetic unit. The result is on that fixed data domain. No zero or period is supplied by the coefficient computation. Keep
\[
 k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad q'=(k-7)^2,
 \quad\Delta=q-q'=16k-48,\quad m=8k-16,
\]
\[
 Q_k(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\qquad
 \omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\qquad S=k/2+iy.
 \tag{CK1}
\]
Let \(G_N\) be the full minimum on \(E_k=\mathbb C[y]/(Q_k)\) induced by the original arithmetic source at degree \(N\). Keep its actual observation \(\Lambda_k\) and kernel frame \(I_K\), whose image is \(K_k\) of dimension \(m\). The exact original conductor has the fixed form
\[
 \mathcal Tp=\sum_{u,v=0}^8a_{uv}p(y+\sigma_{uv}),\qquad
 \sigma_{uv}=(2v-8)\gamma-i(2u-8)\delta,
\]
\[
 \mathcal E(z)=\sum a_{uv}e^{\sigma_{uv}z}=z^{v_0}b(z),\qquad
 b(0)=i^{-v_0}\mu_{v_0}/v_0!\ne0.
 \tag{CK2}
\]
The order is denoted \(v_0\) here to keep it distinct from the sum index and the equilibrium endpoint. The original conductor identity is
\(p\in K_k\Rightarrow\mathcal Tp=Q_{k-8}\eta\), \(\deg\eta<\Delta-v_0\), with \(\deg p<q\). Only this proved inclusion is used; \(\mathcal T\) does not replace the observation.

The retained complete polynomial comparison to
\(d\sigma=|\Gamma(1/4+iy/2)|^2dy/(2\pi)\), of mass \(\sqrt{2\pi}\), is
\[
 \ell_k\|P\|_\sigma^2\le\|P\|_{\mu_k}^2\le u_k\|P\|_\sigma^2,
 \qquad\log(u_k/\ell_k)=o(q),\quad\deg P\le2q.
 \tag{CK3}
\]
It is the original full-source comparison, before any restriction or minimization. It transfers the four-sign determinant of any fixed rank-\(r\) frame with error at most \(2r\log(u_k/\ell_k)\): each determinant lies between its Gamma determinant plus \(r\log\ell_k\) and plus \(r\log u_k\), and two signs are positive and two negative. Both real integration regions and the source mass remain in CK3.

The target, with its original signs, is
\[
 \mathcal K_k=\mathcal R\log\det(I_K^*G_NI_K),\qquad
 \mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}.
 \tag{CK4}
\]

## CK2. Fixed-rank symbol residues and the original quotient

Here are the full finite steps of the kernel manuscript needed to connect CK4 to PJ. In the coefficient norm \(\|p\|_{c,q}=\sum_jq^j|[y^j]p|\), the complete Gamma norms through degree \(2q\) lie between \(e^{-Cq}\|p\|_{c,q}\) and \(e^{Cq}\|p\|_{c,q}\). The upper bound follows from the Gamma moments. For the lower bound the complete Legendre basis on \([1,2]\) bounds coefficients by \(\operatorname{poly}(q)C_0^{2q}\|p(q\cdot)\|_{L^2[1,2]}\); the actual Gamma density on \([q,2q]\) is bounded below by \(cq^{-1/2}e^{-\pi q}\). This bounds the whole-line norm from below without changing it to an interval norm.

The roots of \(q^{-q}Q_k(qx)\) have modulus at most \(\rho_k=k\sqrt{\delta^2+\gamma^2}/q=O(1/k)\). The complete Newton remainder of \(x^j\) has coefficient norm at most \(\sum_{h=0}^j\binom jh2^h=3^j\) for \(j\le2q\): its divided differences are complete homogeneous functions of all actual roots, bounded by \(\binom jh\), and its Newton basis factors have norm at most \(2^h\). Applying this to every representative of a quotient class gives, with one fixed constant,
\[
 e^{-C_1q}\|p\|_{c,q}\le\|[p]\|_{G_N^\sigma}\le e^{C_1q}\|p\|_{c,q},
 \qquad\deg p<q,\quad q-1\le N\le2q.
 \tag{CK5}
\]
Nesting in \(N\) and full determinant factorization imply that a codimension-\(c\) subspace loses a four-return between zero and \(C_2cq\). Indeed factor the metric on the larger space into its restriction and its complete attained quotient; CK5 bounds every quotient direction, and the same fixed frame is used at all four cutoffs.

Let \(D=\partial_y\) on \(\mathcal P_{q-1}\), so \(\|D\|_{c,q}\le1\). On any fixed circle \(|z|=R>1\) avoiding the zeros of \(b\), let \(M_R=\max|b(z)^{-1}|\) and let \(c_R\) count the interior zeros with multiplicity. The exact resolvent decomposition is
\[
 (z-D)^{-1}f=E_{q,z}\lambda_{q,z}(f)-R_zf,
\]
\[
 E_{q,z}=\sum_{j<q}(zy)^j/j!,\quad
 \lambda_{q,z}(f)=\sum_{n<q}n![y^n]f\,z^{-n-1},\quad
 R_zf=[e^{zy}\int_0^ye^{-zt}f(t)dt]_{<q}.
 \tag{CK6}
\]
For a monomial \(y^n\), the coefficient of \(y^j\) in \(R_zy^n\) is \(n!z^{j-n-1}/j!\) for \(j>n\), and zero otherwise. This verifies CK6 coefficient by coefficient and gives \(\|R_z\|_{c,q}\le qe^{q|z|}\). Define
\[
 A_R=\frac1{2\pi i}\oint b(z)^{-1}(z-D)^{-1}dz,\quad
 B_R=\frac1{2\pi i}\oint b(z)^{-1}R_zdz,
\]
\[
 L_Rf=\sum_{0<|\zeta|<R}\operatorname{Res}_{z=\zeta}
 [b(z)^{-1}E_{q,z}\lambda_{q,z}(f)].
\]
The residue at zero of the first integrand is \(b(D)^{-1}\), since \(D^q=0\) and \(b(0)\ne0\). At each other pole CK6 cancels the \(R_z\) terms, hence
\[
 b(D)^{-1}=A_R+B_R-L_R,\quad
 A_R=\sum_{j<q}a_jD^j,\quad |a_j|\le M_RR^{-j},\quad
 \|B_R\|\le RM_Rqe^{Rq},\quad\operatorname{rank}L_R\le c_R.
 \tag{CK7}
\]
At an order-\(a\) pole, the range of its residue lies in the \(a\) columns \(\partial_\zeta^jE_{q,\zeta}\), \(0\le j<a\); this proves the rank statement with repeated poles included. The operator \(B_R\) raises degree strictly.

For \(p\in K_k\), put \(f=\mathcal Tp\), and let \(f_0=D^{-v_0}_0f\) be its primitive with all coefficients below \(v_0\) zero. The exact identity \(\mathcal T=D^{v_0}b(D)\) gives \(p=b(D)^{-1}f_0+l(p)\), with \(l(p)\in\mathcal P_{v_0-1}\). Thus the subspace
\(K_{k,R}=\{p:l(p)-L_Rf_0=0\}\) has codimension at most \(v_0+c_R\), and \(p=(A_R+B_R)f_0\) there.

The actual lower polynomial in \(f=Q_{k-8}\eta\) has coefficients at depth \(j\) bounded by \(\binom{q'}j\rho_k^j\). Triangular inversion of its leading block bounds \(\|q^{q'}\eta(q\cdot)\|_1\le(1-\rho_k)^{-q'}\|f\|_{c,q}\). Consequently
\[
 \|P_{<q'-t}f\|_{c,q}\le(1-\rho_k)^{-q'}2^{q'}\rho_k^t\|f\|_{c,q}.
\]
Also \(\|f\|_{c,q}\le(\sum|a_{uv}|e^{|\sigma_{uv}|})\|p\|_{c,q}\) and \(\|f_0\|_{c,q}\le q^{v_0}\|f\|_{c,q}\). For fixed \(\epsilon>0\), these bounds put the coefficients of \(f_0\) below \(q-\epsilon q/2\) at \(\exp[-c_\epsilon q\log k+O(q)]\|p\|_{c,q}\), with \(q-q'=O(k)\) included. In CK7 the high part needs at least \(\epsilon q/2\) derivatives to reach below \(q-\epsilon q\), costing at most \(M_RR^{-\epsilon q/2}/(1-1/R)\). The degree-raising part uses only the small low input. Choosing fixed \(R\) sufficiently large therefore proves, for every fixed \(D_0>0\),
\[
 \|P_{<q-\epsilon q}p\|_{c,q}\le e^{-D_0q}\|p\|_{c,q}
 \quad(p\in K_{k,R}),
 \tag{CK8}
\]
eventually in \(k\). The radius is fixed after \(\epsilon,D_0\); no uniformity in moving periods is asserted.

## CK3. Complete source map, every jet, and the exceptional quotient

Define the actual triangular polynomial map
\[
 U_QF=[Q_k(y)y^{-q}F(y)]_+.
 \tag{CK9}
\]
Its diagonal is one and it sends \(y^qh\) exactly to \(Q_kh\). Its coefficient norm and inverse norm are \(e^{O(k)}\), bounded by \((1+\rho_k)^q\) and \((1-\rho_k)^{-q}\); coefficients \(j\) places below the diagonal are bounded by \(\binom qj\rho_k^j\) and \(\binom{q+j-1}j\rho_k^j\). For \(s\le q/10\), the complete source comparison is
\[
 e^{-C}\|F\|_\sigma^2\le\|U_QF\|_\sigma^2\le e^C\|F\|_\sigma^2,
 \quad F\in y^{q-s}\mathcal P_{N-q+s},\quad q-1\le N\le2q.
 \tag{CK10}
\]
Here is the full mechanism. Outside \(|y|<\eta q\), pair all opposite roots in CK1. The logarithm of \(|Q_k/y^q|^2\) is bounded by a constant times \(qk^2/|y|^2=O(1)\). In the coordinate \(x=y/q\), write \(F(qx)=x^{q-s}b(x)\). The negative Laurent part of \(x^{-s}q^{-q}Q_k(qx)b(x)\) has coefficient sum at most \(2^q\rho_k^{q-s}\|b\|_1\). Its exterior norm is \(\exp[-(1-s/q)q\log k+O(q)]\|b\|_1\), negligible by CK5's pre-minimum coefficient bound.

For the two inner integrals, Cauchy's polynomial-part formula on \(|z|=2\eta\) gives
\(|U_QF(qx)|\le2(2\eta+\rho_k)^q(2\eta)^{-s}\sup_{|z|=2\eta}|b(z)|\) for \(|x|\le\eta\). The Legendre coefficient estimate gives \(\sup_{|z|\le2\eta}|b(z)|\le\operatorname{poly}(q)10^{\deg b}\|b\|_{L^2[1,2]}\). The contribution of \([q,2q]\) to \(\|F\|_\sigma^2\) is at least \(c\sqrt q e^{-\pi q}\|b\|_{L^2[1,2]}^2\). The logarithm of the inner-to-total ratio is bounded by
\(q[\pi+2(1+1/10)\log10+2(1-1/10)\log(2\eta)+o(1)]\), negative by a fixed margin for \(\eta=2^{-32}\). The same estimate directly bounds the inner integral of \(F\). Combining these two small integrals with the exterior estimates proves CK10. No Laurent expression is integrated through zero.

The complete affine fibres correspond exactly:
\[
 f+y^q\mathcal P_{N-q}\ \xrightarrow{\ U_Q\ }\ U_Qf+Q_k\mathcal P_{N-q},
 \qquad f\in y^{q-s}\mathcal P_{s-1}.
 \tag{CK11}
\]
Thus CK10 passes to complete minima. Taking CK8 first with half as wide a band, and using the inverse coefficient tails in CK9, gives the cutoff-independent injective map
\(A_kp=P_{\ge q-s}U_Q^{-1}p\) from \(K_{k,R}\) into \(y^{q-s}\mathcal P_{s-1}\), with relative \(e^{-cq}\) error in each original quotient norm. This follows because its coefficient error is \(e^{-D_0q/2}\|p\|_{c,q}\) and CK5 bounds both original norms, with \(D_0\) chosen larger than their fixed exponents. Injectivity follows from the same strict relative bound.

This map retains the exact arithmetic-action defect. If \(Q_k=\sum_{j=0}^qc_jy^j\), then, on representatives of degree below \(q\),
\[
 M U_Q-U_QM_0=-[1](c_{q-1},c_{q-2},\ldots,c_0),
 \tag{CK12}
\]
where \(M\) is multiplication modulo \(Q_k\) and \(M_0\) multiplication modulo \(y^q\). Multiplying each polynomial part proves this identity on every basis monomial. CK11 is a metric comparison, with this rank-one action defect retained.

The independent PJ1–69 and EL1–14 proofs now give, for every coefficient vector in that power band and both original low/high pairs,
\[
 \log\frac{\|f\|_{G_l^{\rm pow}}^2}{\|f\|_{G_u^{\rm pow}}^2}
 =\frac{C_\partial q}{2}
 +O\{s\log(Cq/s)+s+\log q\}+o(q).
 \tag{CK13}
\]
The proof of every direction is the full jet right inverse PJ34–38, the complete low Gram PJ19–25, and fixed-degree power transport PJ39–45. The scalar diagonal sequence is proved by the monic minimum and zero-law arguments PJ52–69, including both regions and the exact Gamma mass; EL12 identifies its coefficient. These complete proofs accompany this note. In particular no derivative is taken of an unquantified moving-degree error.

Apply CK13 to the image of \(A_k\) and then CK10–11. It holds for every vector of \(K_{k,R}\), so generalized min–max bounds every low/high eigenvalue on that restricted subspace. If its dimension is \(m-c\), its two-pair determinant return differs from \((m-c)C_\partial q\) by at most \((m-c)q[O(\epsilon\log(C/\epsilon))+o(1)]\), with \(s=\lfloor\epsilon q\rfloor\). The complete exceptional quotient in CK5 costs at most \(C_2cq\), where \(c\le v_0+c_R\) is fixed for fixed \(\epsilon\). Divide by \(mq\), let \(k\to\infty\), and then let \(\epsilon\downarrow0\). Since \(m\to\infty\), the exceptional term tends to zero. Finally CK3 returns to the actual arithmetic metric. This proves
\[
 \boxed{\mathcal K_k=(8k-16)C_\partial q+o(kq).}
 \tag{CK14}
\]
The same proof on any cutoff-independent subspace of the original conductor kernel, of rank \(r_k\to\infty\) and \(r_k\le\Delta\), gives \(r_kC_\partial q+o(r_kq)\). The codimension removed is at most the same fixed \(v_0+c_R\); division by \(r_k\), followed by the same ordered limits, justifies even slower-growing ranks.

## CK4. Relative spectra and the original measured determinant

The relative kernel eigenvalues are bounded by \(e^{O(q)}\) in both directions, by CK5 and CK3. At most twice the discarded codimension lies outside the interval in CK13, by generalized min–max on the fixed subspace. Therefore, for each original pair \((l,u)\),
\[
 \Omega_{l,u}:=\sum_{j=1}^m\left|\log\lambda_j(H_{K,u}^{-1/2}H_{K,l}H_{K,u}^{-1/2})
 -C_\partial q/2\right|=o(kq).
 \tag{CK15}
\]
This is more information than the signed determinant alone. It is the precise input required by the earlier uniform-return manuscript.

To spell out its noncommuting transport, let \(P,Q,F>0\) be metrics and an energy form on one fixed coefficient space. Put
\(R=P^{1/2}\max(I,P^{-1/2}QP^{-1/2})P^{1/2}\). Then \(R\succeq P,Q\), and generalized min–max bounds each decreasing \(\lambda_j(F,R)\) below those for \(P,Q\). Pairing ordered logarithms through this common lower list proves
\[
 \sum_j|\log\lambda_j(F,P)-\log\lambda_j(F,Q)|
 \le\log\frac{\det R}{\det P}+\log\frac{\det R}{\det Q}
 =\sum_j|\log\lambda_j(P^{-1/2}QP^{-1/2})|.
 \tag{CK16}
\]
The equality follows by splitting the eigenvalues of \(P^{-1/2}QP^{-1/2}\) above and below one. No common eigenvectors of \(P,Q,F\) are assumed.

For the original word \(T=D_k(M)\), retain the full positive-energy band
\(e^{c_N-e_k}P_{(\ker T)^{\perp_{G_N}}}\preceq_{G_N}T^{\dagger_{G_N}}T\preceq_{G_N}e^{c_N+e_k}P_{(\ker T)^{\perp_{G_N}}}\), with \(e_k=o(q)\),
\[
 c_L=2q\log q+\eta_Lq,\quad c_H=c_L-C_\partial q/2,
 \quad\eta_L=2\log(4/\pi)-2.
 \tag{CK17}
\]
These are the original measured-word and uniform-return inputs. Their complete boundary quotient in a common fixed value frame has logarithmic width \(o(q)\). Thus for \(F_N=(TI_K)^*G_N(TI_K)\), its scaled low/high comparison has width \(o(q)\) about \(e^{C_\partial q/2}\). Apply CK16 first with the same energy and kernel metrics, and then min–max to the actual energy comparison. Equation CK15 gives
\(D_i=\sum_j|\log\alpha_{j,N_i}-\log\alpha_{j,N_{i+2}}|=o(kq)\), in precisely PT10's notation.

The full observed determinant PT4 now yields, because \(a\mapsto\log(1+e^a/z)\) is 1-Lipschitz for every \(z>0\),
\[
 \boxed{\sup_{z>0}\left|\mathcal R\log\det\mathscr Y_N(z)
 +2\Delta\log\frac{z+e^{c_L}}{z+e^{c_H}}\right|
 \le D_0+D_1+4\Delta e_k=o(kq).}
 \tag{CK18}
\]
In particular the original, unextended observation has root-scale and all lower positive-scale return \(-\Delta C_\partial q+o(kq)\). The formula is uniform for positive \(z\); it does not take the logarithm of an individual singular response at zero. The earlier depth-eight bound remains valid on its extra corner-period guards and now connects to the same original leading plateau via its exact attained compression.

## CK5. Earlier receivers updated at their actual scope

The following replacements use their complete earlier equations, not their ranks in isolation.

1. **Invariant-row covariance.** Its retained exact receiving equation is \(\mathcal K_k=(\Delta-v_0)C_\partial q+\mathcal R\log\det S_N+o(kq)\). Subtract CK14 to obtain \(\mathcal R\log\det S_N=-(\Delta-v_0-m)C_\partial q+o(kq)\). A fixed-rank difference remains \(O(q)\); it is not an evaluated order-\(q\) coefficient.
2. **Selected arithmetic layers.** AP's actual interval is \(0\le\mathcal K_k-X_s\le2t_s\mathfrak E_k\), with \(\mathfrak E_k=O(q)\). Hence any fixed layer with \(t_s=O(1)\), including its proved depth-eight domain, has \(X_s=mC_\partial q+o(kq)\). For growing remaining layers the complete quotient theorem following CK14 gives their own rank coefficient. No arbitrary layer distribution is inferred from a total alone.
3. **Two measured responses.** With the original \(Q_N\) metric, the positive secant is \(Z_N=12(2I+\mathscr Y_N(2\sigma/3))^{-1}-4(I+\mathscr Y_N(\sigma/2))^{-1}-2I\). Its proof gives \(-2W_k\le\mathcal K_k+\mathcal R\log e_{m-h_k}(Z_N)\le2m\omega_k+2W_k\), where \(W_k=O(q\log q)\), \(h_k=O(1)\), \(\omega_k=o(q)\). Thus its actual positive characteristic coefficient has return \(-mC_\partial q+o(kq)\). This is a leading signed return; individual coefficients and numerical sample precision are retained separately in S10–13.
4. **Static and dynamic memory.** The static proof's exact matrices are \(S=C^*A^{-1}C\), \(E_0=B_0-S\), and \(\Sigma(z)=C^*(z+A)^{-1}C\). They are connected by \(S-\Sigma(z)=zC^*A^{-1}(z+A)^{-1}C\). Its static root returns are \(mC_\partial q\), \(\Delta C_\partial q\), and \((\Delta-m)C_\partial q\), each with its proved \(o(kq)\) remainder. Its dynamic receiver is \(\mathcal RD_N(z)=mC_\partial q-\mathcal K_k+o(kq)\), so CK14 makes this \(o(kq)\) on the stated root domain. It does not make any individual dynamic determinant zero.
5. **Frequency recovery.** PT12–22 now receive \(\mathcal B=D_0+D_1+\sum_NE_N=o(kq)\), since \(\sum_NE_N\le4\Delta e_k\). They prove the entire measured phase transition in integral norm, with finite error, and the controlled root-scale phase-area correction. The new independent SF1–36 sharp angle bounds further strengthen the frequency error. These equations supersede the newest archive's isolated statement that its leading determinant coefficient is unevaluated.
6. **Short ambient and hidden quotients.** PEN17–20's two operations remain connected by their actual terminal metric, of rank at most128. Its two-sided \(O(q)\) correction is retained. Consequently both full proved receivers have the same \(kq\) coefficient where their old intervals transfer \(\mathcal K_k\), while their finite signs and order-\(q\) terms remain distinct.

The projected complex arithmetic currents still require their original phase-bearing insertions. Equal positive energies can correspond to different polar actions. The determinant and measured-resolvent phase results above therefore do not assign those current signs or remove the retained positive canonical action. This scope is part of the theorem, not a conclusion that the programme has ended.

**Two-response proof correction.** In the explanatory sentence following the incoming S2, the filtered secant needs its outer factor two. With \(Y^{(\sigma)}(x)=(xI+Y(\sigma x/(1+x)))/(1+x)\), the exact formula is
\[
 Z=2\{2Y^{(\sigma)}(2)^{-1}-Y^{(\sigma)}(1)^{-1}-I\}
 =2C^*(I+A)^{-1}(2I+A)^{-1}C.
 \tag{CK19}
\]
The blocks in the last expression are those of the filtered energy. The complete filtered Schur identity gives \(xY^{(\sigma)}(x)^{-1}=xI+B_0-C^*(xI+A)^{-1}C\); subtract its values at two and one to prove CK19. Substitution of the displayed response map then gives exactly the coefficients12,4,2 in the original secant. Thus the source's displayed S1 and S2 are unchanged, while their connecting sentence is corrected. The independent original-metric checker includes a negative control rejecting omission of this factor.

## Provenance and proof sources

This proof uses the user-supplied *The original kernel coefficient*, full14-page manuscript, Sections1–7; the full earlier uniform-return and static-memory proofs; the two-response proof S1–13; and frequency FD10–24. All six arrivals and every supporting file are individually recorded in `INTAKE_REVIEW.json`. The complete independent PJ, EL, PT and SF proofs accompany this continuation. Original source PDFs are preserved; the mathematical transcription and additional derivations here are identified as such.

The retained human Gamma and polynomial sources are cited in PJ's source ledger. The elliptic source and its actual reading/fetch status are in EL. Existing full-programme sources include [AP1–30](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/PROBE_PROOFS.md), [KM1–45](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/MASS_PROOFS.md), and [PEN1–27](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9104d852c6bc5b79e6fc4588c403128a40b7fda3/workbenches/splitzero-tandem/continuations/20260922-arithmetic-probe-mass/PENCIL_PROOFS.md). Those frozen proofs are preserved. The new claims above strengthen their receiving values; they do not rewrite their source history.
