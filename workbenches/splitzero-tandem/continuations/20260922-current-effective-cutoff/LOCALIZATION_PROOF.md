# Effective localization in the full original kernel and word image

Independent derivation, 22 September 2026. The contour calculation, coefficient-to-source comparison, complete polynomial fibres, and relative-spectrum loss are proved here with finite constants. In particular the exceptional-direction contribution improves the incoming LC13. The companion scalar proof supplies its proved bound with constant 83; this value is carried through every original-metric estimate below.

## 1. Original data, source constants, and the finite scalar input

Fix the stipulated original simple quartet, its admitted period, branch and arithmetic unit. Retain
\[
k\equiv1\pmod4,\quad k\ge17,\quad q=(k+1)^2,\quad q'=(k-7)^2,
\quad\Delta=q-q'=16k-48,\quad m=8k-16,
\]
\[
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\quad
0<\delta<1/2,\quad\gamma>2,\quad
Q_k(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\quad E_k=\mathbb C[y]/Q_k.
\tag{LX1}
\]
The physical coordinate is still \(s=k/2+iy\); multiplication is \(M[p]=[yp]\), so its action is \(kI/2+iM\). The onto observation is the complete original \(\Lambda_k\), and \(I_K\) is the unchanged coefficient inclusion of its kernel \(K_k\), of rank \(m\). The complete attained source metric at degree \(N\) is \(G_N\), and \(H_{K,N}=I_K^*G_NI_K\). The cutoffs are
\[
N_j=q-1+j,\quad0\le j\le q+1,\quad t_j=j/q.
\tag{LX2}
\]
Thus the four original signs are at \(j=0,1,q,q+1\). In particular the degree \(2q\) endpoint is retained.

Use the actual comparison source
\[
d\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi}\,dy,\qquad M_\sigma=\sqrt{2\pi}.
\]
The original polynomial source comparison, before either restriction or minimization, is
\[
\ell_k\|P\|_\sigma^2\le\|P\|_{\mu_k}^2\le u_k\|P\|_\sigma^2,
\qquad\deg P\le2q,\qquad\kappa_k=u_k/\ell_k.
\tag{LX3}
\]
Here these are the original finite constants, not newly selected matrix widths. Their source formula is \(u_k=A_k\), \(\ell_k=a_k/[1+4(2q+25)^2]^{25}\) on this simple-quartet domain. In the retained full source proof, writing \(\alpha=\pi/2\), \(p=7/2\), \(B_h=50\),
\[
a_k=\frac{c_h\vartheta_h^{k-3}e^{-\alpha(k-3)}(k-2)^{-50}}
 {C_\Gamma^{\rm src}2^{25}},\qquad
A_k=\frac{C_h^{\rm tilt}}{c_\Gamma^{\rm src}}k^{9/2}M_\alpha^{k-1}.
\]
All constants \(c_h,C_h^{\rm tilt},\vartheta_h,M_\alpha,c_\Gamma^{\rm src},C_\Gamma^{\rm src}\) retain their original fixed-source definitions. Thus \(\log\kappa_k=O_h(k+\log(q+2))\). To see the polynomial step explicitly, its density bounds give \(a_k(1+y^2)^{-25}d\sigma\le d\mu_k\le A_kd\sigma\). The exact Gamma recurrence gives \(\|yP\|_\sigma\le2(N+1)\|P\|_\sigma\); expanding \((1+y^2)^{25}\) and applying that bound through all successively raised degrees gives the factor \([1+4(N+25)^2]^{25}\). Cauchy--Schwarz applied to the reciprocal two weights proves the lower bound. These are the same constants as [the retained AMT4--5 full-source proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/RETAINED_COMPLETE_PROOF_SOURCES.tex#L13402), and [HAR40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L440) retains their absolute mass as well as their ratio.

Let \(d\nu_n=|y|^{2n}d\sigma\), \(d_n=\nu_n(\mathbb R)\), and let \(\mathsf K_{n,M}\) be the full degree-\(M\) reproducing kernel for this measure. Write \(J\) for the original profile (incoming \(\beta\)), with the proved exact dictionary
\[
t=4zF'(z)/F(z),\quad F(z)=\frac2\pi K(\sqrt z),\qquad
J(t)=2\log F(z)-\frac t2\log z,
\quad J(0)=0.
\tag{LX4}
\]
It is increasing and concave; \(J(1)=C_\partial/2\). These statements, including its exact original-root dictionary, are proved in [025 EP1--17](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/ELLIPTIC_PROFILE_PROOF.md).

The companion *Effective Gamma and jet proof*, EG23, proves the following explicit bound, improving the incoming constant 110:
\[
\max_{0\le M\le\lfloor11q/10\rfloor}
\left|\log[d_q\mathsf K_{q,M}(0,0)]-qJ(M/q)\right|
\le E_G(q):=83+3\log(q+2),\qquad q\ge40.
\tag{LX5}
\]
Its proof retains the full Gamma measure, both half-lines, the exact mass and all integer degrees, including zero and odd degree. The error is now explicit. In the present original domain \(q\ge324\), so this scalar lower guard always holds.

## 2. Complete coefficient-to-quotient metric comparison

Put \(\rho=k\sqrt{\delta^2+\gamma^2}/q\) and
\(\|p\|_{c,q}=\sum_jq^j|[y^j]p|\). We prove, for \(q\ge40\) and \(\rho\le1/2\),
\[
e^{-10q}\|p\|_{c,q}\le\|[p]\|_{G_N^\sigma}
\le e^{2q}\|p\|_{c,q},\qquad \deg p<q,\quad q-1\le N\le2q.
\tag{LX6}
\]

First take any polynomial \(P\) of degree \(d\le2q\), and write \(p(x)=P(qx)\). The orthonormal basis on \([1,2]\) is \(\sqrt{2j+1}P_j(2x-3)\). Its coefficient sum is \(\sqrt{2j+1}P_j(5)\le\sqrt{2j+1}10^j\): the alternating coefficients after the shift have absolute sum equal to evaluation at \(-1\), and the generating function or three-term recurrence gives \(P_j(5)\le10^j\). Cauchy--Schwarz therefore proves
\[
\|p\|_{\rm coefficients,1}\le(d+1)10^d\|p\|_{L^2[1,2]}.
\tag{LX7}
\]
The Gamma lower envelope \(w(y)\ge\tfrac12y^{-1/2}e^{-\pi y/2}\), \(y\ge1\), gives
\[
\|P\|_\sigma^2\ge\frac{\sqrt q}{2\sqrt2}e^{-\pi q}
\|p\|_{L^2[1,2]}^2.
\]
For \(q\ge40,d\le2q\), combining this with (LX7) gives
\(\|P\|_\sigma\ge e^{-8q}\|P\|_{c,q}\). Indeed the negative logarithm of the displayed constant is at most
\(\pi q/2+2q\log10+\log(2q+1)-\tfrac14\log q+\tfrac34\log2<8q\).

Every root \(\alpha_i=\omega_i/q\) of the scaled monic polynomial has modulus at most \(\rho\). The complete Newton expansion of the remainder of \(x^j\) modulo that polynomial has coefficient norm at most
\[
\sum_{h=0}^{\min(j,q-1)}\binom jh\rho^{j-h}(1+\rho)^h
\le(1+2\rho)^j\le2^{2q}\quad(j\le2q).
\tag{LX8}
\]
This follows because the divided difference is the complete homogeneous polynomial of degree \(j-h\) in the first \(h+1\) roots, with \(\binom jh\) terms; the Newton product has norm at most \((1+\rho)^h\). Apply (LX8) to every coefficient of every representative \(P\equiv p\pmod{Q_k}\). Then \(\|p\|_{c,q}\le2^{2q}\|P\|_{c,q}\), so minimizing the preceding lower bound proves the first half of (LX6).

For the upper half retain the canonical degree-below-\(q\) representative. The exact Gamma recurrence, including its last raising row, gives \(\|y^j\|_\sigma\le\sqrt{M_\sigma}2^jj!\). For \(j<q\), this is at most \(e^{2q}q^j\). Triangle inequality and the attained minimum prove the other half. Thus the finite coefficient transfer applies to complete quotient fibres, not merely to their canonical representatives.

Source nesting and (LX3),(LX6) give the particularly useful global bound
\[
0\le\log\lambda_a(H_{K,N_j}^{-1/2}H_{K,N_i}H_{K,N_j}^{-1/2})
\le B_{\rm all}(k):=24q+\log\kappa_k\quad(i\le j).
\tag{LX9}
\]
The constant \(24\) is \(2(10+2)\); the incoming \(40\) is unnecessary. The same bound holds on any fixed restriction or attained quotient: apply the form bounds before taking its complete minimum.

## 3. An explicit circle and the entire residue operator

The actual conductor is \(\mathcal T=\sum_sa_s e^{\sigma_sD}=D^{v_0}b(D)\), where
\[
\mathcal E(z)=\sum_sa_se^{\sigma_sz}=z^{v_0}b(z),\quad
b(0)=i^{-v_0}\mu_{v_0}/v_0!\ne0,
\quad B_A=\max(1,\max_s|\sigma_s|),
\quad A_b=\frac{(\sum_s|a_s|)B_A^{v_0}}{|\mu_{v_0}|}\ge1.
\]
Taylor's integral remainder proves \(|b(z)/b(0)|\le A_be^{B_A|z|}\); it is also valid when \(v_0=0\). For \(R\ge2\), put
\[
N_R=\left\lceil\frac{\log A_b+12B_AR}{\log2}\right\rceil,
\quad L_R=\log A_b+6B_AR,
\quad\mathcal M_R=|b(0)|^{-1}e^{2L_R}[32(N_R+1)]^{N_R}.
\tag{LX10}
\]
There is \(r\in[R,2R]\), with no zero on its circle, at most \(N_R\) zeros inside it counted with multiplicity, and
\[
\max_{|z|=r}|b(z)^{-1}|\le\mathcal M_R.
\tag{LX11}
\]

Here are the details behind the classical zero-count and harmonic tools in this use. The circular mean of \(\log|z-a|\) at radius \(T\) equals \(\log\max(T,|a|)\), by the mean value property outside its zero and the convergent logarithmic series otherwise. Factoring the zeros and applying the mean value property to the remaining zero-free function gives the Jensen formula. At \(T=12R\), every zero of modulus at most \(6R\) contributes at least \(\log2\); this proves the bound \(N_R\), with limits handling a zero on the outer circle. Choose a zero-free \(S\in[4R,6R]\), and factor these zeros by the full disk Blaschke product
\(B(z)=\prod e^{i\theta_a}S(z-a)/(S^2-\overline a z)\), including repetitions. Choose phases so \(B(0)>0\). The zero-free quotient \(h=b/(b(0)B)\) has \(\log|h|\le L_R\) on \(|z|=S\). The positive harmonic function \(L_R-\log|h|\) has its value at zero at most \(L_R\), because \(|h(0)|=1/|B(0)|\ge1\). The Poisson kernel ratio is at most \((S+2R)/(S-2R)\le3\), so \(\log|h(z)|\ge-2L_R\) for \(|z|\le2R\).

Remove from \([R,2R]\) the intervals of radius \(R/[4(N_R+1)]\) around all zero moduli in \(|z|<S\). Their total length is less than \(R/2\). At any remaining radius, each Blaschke factor has modulus at least \(|z-a|/(S+|z|)\ge1/[32(N_R+1)]\). Multiplying them proves (LX11). This includes every repeated zero. Finding a numerical such circle for an unspecified period is not claimed.

The operator \(D=\partial_y\) on degree-below-\(q\) polynomials has \(\|D\|_{c,q}\le1\). Direct calculation on monomials gives
\[
(z-D)^{-1}f=E_{q,z}\lambda_{q,z}(f)-R_zf,
\quad E_{q,z}=\sum_{j<q}(zy)^j/j!,
\quad\lambda_{q,z}(f)=\sum_{n<q}n![y^n]f\,z^{-n-1},
\]
\[
R_zf=\left[e^{zy}\int_0^ye^{-zt}f(t)dt\right]_{<q},\qquad
[y^{n+j}]R_zy^n=\frac{n!z^{j-1}}{(n+j)!}\quad(j\ge1).
\tag{LX12}
\]
There is no term of degree at most \(n\) in \(R_zy^n\). Let
\[
A_r=\frac1{2\pi i}\oint_{|z|=r}\frac{(z-D)^{-1}}{b(z)}dz,
\quad B_r=\frac1{2\pi i}\oint_{|z|=r}\frac{R_z}{b(z)}dz,
\]
\[
L_rf=\sum_{0<|a|<r}\operatorname{Res}_{z=a}
\frac{E_{q,z}\lambda_{q,z}(f)}{b(z)}.
\]
The residue at zero is the full nilpotent functional calculus \(b(D)^{-1}\); the nonzero residues give
\[
b(D)^{-1}=A_r+B_r-L_r,
\quad A_r=\sum_{j<q}\alpha_jD^j,
\quad|\alpha_j|\le\mathcal M_Rr^{-j},\quad
\operatorname{rank}L_r\le N_R.
\tag{LX13}
\]
At a pole of order \(a\), its entire range is spanned by \(E_{q,z},\partial_zE_{q,z},\ldots,\partial_z^{a-1}E_{q,z}\) evaluated at that pole: Leibniz's rule puts all remaining derivatives on the scalar functional. This proves the rank count even at multiple poles.

The degree-raising part admits the improved full finite bound
\[
\boxed{\|B_r\|_{c,q}\le\mathcal M_R(6R)^q.}
\tag{LX14}
\]
Indeed (LX12) and \((n+j)!/n!\ge j!\) give
\(\|R_z\|_{c,q}\le r^{-1}\sum_{j=1}^{q-1}(qr)^j/j!\).
Backward successive ratios in this sum are less than \(1/r\), so the sum is at most \(r/(r-1)\) times its last term. Using \((q-1)!\ge((q-1)/e)^{q-1}\) and \((q/(q-1))^{q-1}<e\), it is less than \((er)^q/(r-1)\le(3r)^q\). The contour length factor is exactly \(r\mathcal M_R\); the factor \(r^{-1}\) just displayed cancels it. Since \(r\le2R\), (LX14) follows. The finite truncation is essential: its logarithmic cost is \(q\log R\), not \(Rq\).

## 4. The original invariant kernel, all constraints retained

The exact conductor implication is
\[
p\in K_k\ \Longrightarrow\ f=\mathcal Tp=Q_{k-8}\eta,
\qquad\deg\eta<\Delta-v_0.
\tag{LX15}
\]
It follows from [024 CK1--7](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L6). We use only this implication; every additional invariant row stays in the domain \(K_k=\ker\Lambda_k\).

Set \(f_0=D_0^{-v_0}f\), the primitive with its first \(v_0\) coefficients zero. Then
\(p=b(D)^{-1}f_0+l(p)\), \(\deg l<v_0\). The single cutoff-independent subspace
\[
K_{k,R}=\{p\in K_k:l(p)-L_rf_0=0\},\qquad
c_{\rm loc}=\min(m,v_0+N_R)
\tag{LX16}
\]
has codimension at most \(c_{\rm loc}\), by rank-nullity after restriction to the full invariant kernel. No arithmetic observation row is discarded. On this subspace \(p=(A_r+B_r)f_0\).

Take a positive integer \(b\) divisible by eight and impose
\[
8\Delta+8\le b\le q/10,\qquad q\ge40,\qquad0<\rho<1/2.
\tag{LX17}
\]
The lower-root polynomial, including every one of its roots, gives
\[
\|P_{<q'-h}f\|_{c,q}\le(1-\rho)^{-q'}2^{q'}\rho^h\|f\|_{c,q}.
\tag{LX18}
\]
To verify this, the coefficient at depth \(j\) of its monic reversed polynomial is at most \(\binom{q'}j\rho^j\). Its full inverse leading block has column sum bounded by \(\sum_{j\ge0}\binom{q'+j-1}j\rho^j=(1-\rho)^{-q'}\). Multiply these bounds. Also \(\|f\|_{c,q}\le M_T\|p\|_{c,q}\), where \(M_T=\sum_s|a_s|e^{|\sigma_s|}\), and \(\|f_0\|_{c,q}\le q^{v_0}\|f\|_{c,q}\).

Define the complete finite errors
\[
e_p=q^{v_0}M_T\mathcal M_R
\left[(2+(6R)^q)(1-\rho)^{-q'}2^{q'}\rho^{b/8}
+2R^{-b/4}\right],
\]
\[
e_U=(1-\rho)^{-q}e_p+\frac{4^q\rho^{b/2}}{1-\rho},
\qquad \zeta=e^{12q}(1+\rho)^q e_U.
\tag{LX19}
\]
The part of \(f_0\) below degree \(q-b/4\) obeys (LX18) with \(h=b/8\), since \(b/8+v_0\ge\Delta\). The remaining part must lose at least \(b/4\) degrees through \(A_r\) to reach degree below \(q-b/2\); the geometric derivative tail is at most \(2\mathcal M_RR^{-b/4}\). The operator \(B_r\) raises degree and therefore uses only the small low input there. Equations (LX13)--(LX14) prove
\(\|P_{<q-b/2}p\|_{c,q}\le e_p\|p\|_{c,q}\).

Retain the actual polynomial-part map
\[
U_QF=[Q_k(y)y^{-q}F(y)]_+,
\quad U_Q^{-1}p=[y^qp(y)/Q_k(y)]_+.
\tag{LX20}
\]
On degree-below-\(q\) representatives its norm is at most \((1+\rho)^q\), its inverse at most \((1-\rho)^{-q}\), and its inverse tail after depth \(b/2\) at most \(4^q\rho^{b/2}/(1-\rho)\). The first two assertions are the elementary and complete homogeneous coefficient sums. For the last, use \(\binom{q+j-1}j\le4^q\) for \(0\le j<q\), and sum the remaining geometric series. Thus the fixed map
\[
\mathcal A_{k,b,R}:K_{k,R}\longrightarrow y^{q-b}\mathcal P_{<b},
\qquad \mathcal A_{k,b,R}p=P_{\ge q-b}U_Q^{-1}p
\]
satisfies, at every original cutoff,
\[
\|p-U_Q\mathcal A_{k,b,R}p\|_{G_N^\sigma}
\le\zeta\|p\|_{G_N^\sigma}.
\tag{LX21}
\]
The factor \(e^{12q}\) is exactly the upper/lower norm transfer in (LX6). For \(\zeta<1\), this is injective. It evaluates the original vectors in their full original metrics.

## 5. The whole polynomial fibre and both real integration regions

The map (LX20) is defined on polynomials through degree \(2q\). For every band vector \(f\) it maps the entire source fibre bijectively:
\[
f+y^q\mathcal P_{N-q}\ \longrightarrow\ U_Qf+Q_k\mathcal P_{N-q}.
\tag{LX22}
\]
Its restriction to the added term is exactly \(U_Q(y^qh)=Q_kh\). Nothing is inferred from a truncated list of relation columns.

Here are explicit finite constants for its source norm. Put
\(\epsilon_0=2^{-32}\), \(d_*=q+b\), and
\[
E_Q=\frac{q(\rho/\epsilon_0)^2}{1-(\rho/\epsilon_0)^2},\quad
r_Q=\sqrt{M_\sigma}e^{8q}2^q\rho^{q-b}\epsilon_0^{-b},
\]
\[
i_F=2\sqrt2M_\sigma q^{-1/2}(d_*+1)^2 10^{2d_*}e^{\pi q}
\epsilon_0^{2(q-b)},
\]
\[
i_U=8\sqrt2M_\sigma q^{-1/2}(d_*+1)^2 10^{2d_*}e^{\pi q}
(2\epsilon_0+\rho)^{2q}(2\epsilon_0)^{-2b}.
\tag{LX23}
\]
Impose the explicit guards
\[
\rho\le\epsilon_0/2,\quad i_F\le1/4,\quad i_U\le1,
\quad r_Q\le e^{-E_Q/2}/4.
\tag{LX24}
\]
Then with \(C_Q=E_Q+2\log2\),
\[
e^{-C_Q}\|F\|_\sigma^2\le\|U_QF\|_\sigma^2
\le e^{C_Q}\|F\|_\sigma^2,
\quad F\in y^{q-b}\mathcal P_{N-q+b},\quad q-1\le N\le2q.
\tag{LX25}
\]

For the proof write \(F(qx)=x^{q-b}h(x)\), \(\deg h\le d_*\). On \(|x|\ge\epsilon_0\), pairing all opposite roots of the original \(Q_k\) gives
\(|\log|Q_k(qx)/(qx)^q|^2|\le E_Q\), because
\(|\log|1-z||\le |z|/(1-|z|)\). The negative Laurent part of \(q^{-q}Q_k(qx)x^{-b}h(x)\) has coefficient sum at most \(2^q\rho^{q-b}\|h\|_1\). Every negative power there lies between \(-b\) and \(-1\), so its complete exterior norm is at most \(\sqrt{M_\sigma}2^q\rho^{q-b}\epsilon_0^{-b}\|h\|_1\). The pre-minimum \(e^{-8q}\) coefficient bound in Section 2 makes this at most \(r_Q\|F\|_\sigma\).

For the inner region, (LX7) gives \(\sup_{|x|\le1}|h(x)|\le(d_*+1)10^{d_*}\|h\|_{L^2[1,2]}\). The contribution of \([q,2q]\) to \(\|F\|_\sigma^2\) is at least \(\sqrt q e^{-\pi q}\|h\|_2^2/(2\sqrt2)\). Therefore the entire inner norm of \(F\) is at most \(i_F\|F\|_\sigma^2\). Cauchy's polynomial-part formula on \(|z|=2\epsilon_0\) gives
\[
|U_QF(qx)|\le2(2\epsilon_0+\rho)^q(2\epsilon_0)^{-b}
\sup_{|z|=2\epsilon_0}|h(z)|\quad(|x|\le\epsilon_0).
\]
This bounds the entire inner norm of \(U_QF\) by \(i_U\|F\|_\sigma^2\). The two norm ratios are consequently bounded below by \(e^{-E_Q/2}\sqrt{1-i_F}-r_Q>\tfrac12e^{-E_Q/2}\), and above by \(\sqrt{(e^{E_Q/2}+r_Q)^2+i_U}<2e^{E_Q/2}\). Squaring proves (LX25). No Laurent expression is integrated through zero. Equation (LX22) passes this bound to complete attained minima.

For every finite degree-below-\(q\) representative, the arithmetic action defect is exactly
\[
MU_Q-U_QM_0=-[1](c_{q-1},c_{q-2},\ldots,c_0),
\qquad Q_k(y)=\sum_{j=0}^qc_jy^j.
\tag{LX26}
\]
For column \(y^j\), polynomial-part multiplication leaves the constant \(-c_{q-j-1}\); all positive powers cancel. At \(j=q-1\), use \(y^q\equiv-\sum_{a<q}c_ay^a\pmod{Q_k}\) to obtain the same constant. Thus \(U_Q\) is the proved fibre map with this retained rank-one action defect. It does not replace the physical multiplication operator.

## 6. Full power-band constants and the native estimate

Here the complete jet bounds from [024 PJ6--40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/POWER_JET_PROOF.md) are made finite. Put \(n=q-b\), \(\theta=\pi/2\), \(\alpha=2n-1/2\),
\[
c=(4\pi\sqrt{128})^{-1},\quad C=40\sqrt{128}/\pi,
\quad B_0=q/(cn),\quad D_0=\max(1,Cn/q).
\]
The full two-half-line Gamma/Laguerre comparison is \(\tfrac14\|P\|_{\lambda_n}^2\le\|P\|_{\nu_n}^2\le32\|P\|_{\lambda_n}^2\) for \(n\ge36,\deg P\le2n+2\), where \(d\lambda_n=|y|^{2n-1/2}e^{-\pi|y|/2}dy\). The near-zero lower contribution is recovered by \(\|P/y\|_{\lambda_n}\le4\pi\|P\|_{\lambda_n}/n\), giving missing mass at most \(16\pi^2/n^2\le1/4\). The full Laguerre derivative matrix and last multiplication row give \(cn\|P\|_{\nu_n}\le\|yP\|_{\nu_n}\le Cn\|P\|_{\nu_n}\) through source degree \(2n+1\). These are the original PJ6--16 calculations with their literal measure mass retained.

Define
\[
g_j=\frac{j!(\alpha+1)_j}{(\theta q)^{2j}},\quad
\mathcal L=128[(b+1)3^b]^2\max\{\max_{j\le b}g_j,(\min_{j\le b}g_j)^{-1}\},
\]
\[
U=\sum_{2h<b}\binom{\lfloor(q+b)/2\rfloor}{h}^{2}B_0^{4h}
+B_0^2\sum_{2h+1<b}\binom{\lfloor(q+b-1)/2\rfloor}{h}^{2}B_0^{4h},
\]
\[
V=\sum_{h=0}^{\lfloor(b-1)/2\rfloor}
\binom{\lfloor q/2\rfloor+h-1}{h}B_0^{2h},\qquad
L=bV^2D_0^{2(b-1)},
\]
\[
\mathcal J_{q,b}=\log\mathcal L+\max(\log L,\log U)
+2b\log(C/c)+E_G(q)+qJ((b+1)/q).
\tag{LX27}
\]
The jet map is \(P\mapsto(q^a[y^a]P)_{a<b}\), with its entire degree-\(j+b-1\) affine fibre in \(\nu_n\). Every low-to-\(N_j\) logarithmic relative eigenvalue of that full jet metric is within \(\mathcal J_{q,b}\) of \(qJ(t_j)\).

For completeness the finite argument is as follows. The monic Laguerre coefficient matrix has entries \((-1)^{j-i}\binom ji(\alpha+i+1)_{j-i}/(\theta q)^{j-i}\), and its inverse has the same magnitudes. Multiplication proves the inverse formula by the binomial alternating sum. Every factor is at most 2 here, so both operator norms are at most \((b+1)3^b\); its exact squared monic norms relative to the half-line mass are \(g_j\). Applying both half-lines and their full mass comparison gives the low metric between \(d_n\mathcal L^{-1}I\) and \(d_n\mathcal LI\), including the extra lift degree at \(j=1\).

For the upper high covariance, the nonzero roots of each orthogonal polynomial have modulus at least \(cn\): their squares are Rayleigh values of multiplication by \(y^2\), and the preceding complete raising bound applies to every test polynomial. Pair the even roots. Each divided coefficient is bounded by its constant coefficient times \(\binom{\lfloor M/2\rfloor}h(cn)^{-2h}\). For odd polynomials, its derivative-at-zero norm is at most \(\mathsf K_{n,M}(0,0)/(cn)^2\), by the exact bijection \(P\mapsto yP\) on the odd subspace. Summing all squared rows gives trace bound \(U\mathsf K_{n,M}(0,0)\), and a positive covariance is no larger than its trace times identity.

For the lower high covariance let \(H(y)=\mathsf K_{n,j-1}(y,0)/\mathsf K_{n,j-1}(0,0)\). Reproduction gives \(H(0)=1\) and \(\|H\|^2=1/\mathsf K_{n,j-1}(0,0)\); the nonzero roots have the same gap. Its reciprocal coefficients through degree \(b-1\) have total bounded by \(V\). Multiplying \(H(y)\) by the first \(b\) Taylor coefficients of the requested jet divided by \(H(qx)\) yields a simultaneous right inverse of the entire jet, with degree at most \(j+b-2\). Its squared norm is bounded by \(L\|a\|_2^2/\mathsf K_{n,j-1}(0,0)\), including every coefficient combination. This proves both full covariance bounds.

Finally, repeated raising applied to a polynomial and to the constant gives
\(|\log[d_n\mathsf K_{n,h}(0,0)]-\log[d_q\mathsf K_{q,h}(0,0)]|\le2b\log(C/c)\). All raising source degrees are at most \(q+2b-1\le2n+1\). Concavity gives \(|J(x+h)-J(x)|\le J(h)\), so the full integer shifts between \(j-1,j,j+b-1\) are bounded by the last term in (LX27). At \(j=0\) the relative metric is exactly identity. This proves the claimed all-vector finite jet estimate for all \(q+2\) original cutoffs.

Set
\[
E_{\rm loc}(k,b,R)=\mathcal J_{q,b}+2C_Q
+2\log\frac{1+\zeta}{1-\zeta}+\log\kappa_k,
\qquad\zeta\le1/4.
\tag{LX28}
\]
Equations (LX21)--(LX25), followed by (LX3), show on the fixed subspace \(K_{k,R}\)
\[
\left|\log\frac{\|p\|_{G_{N_0}}^2}{\|p\|_{G_{N_j}}^2}-qJ(t_j)\right|
\le E_{\rm loc}\quad(p\ne0).
\tag{LX29}
\]
The two triangle-inequality endpoint errors cost exactly the logarithm shown, the two complete source comparisons cost \(2C_Q\), and the arithmetic source ratio costs \(\log\kappa_k\).

## 7. A sharper exceptional-direction penalty

Let \(I_G\) be any fixed frame inclusion of \(K_{k,R}\) in the full original kernel frame. For \(i\le j\) the matrix
\[
V_j=H_{K,N_j}^{1/2}I_G(I_G^*H_{K,N_j}I_G)^{-1/2}
\]
satisfies \(V_j^*V_j=I\), and direct multiplication gives
\[
V_j^*(H_{K,N_j}^{-1/2}H_{K,N_i}H_{K,N_j}^{-1/2})V_j
=(I_G^*H_{K,N_j}I_G)^{-1/2}I_G^*H_{K,N_i}I_G
(I_G^*H_{K,N_j}I_G)^{-1/2}.
\tag{LX30}
\]
This is the exact isometric compression relating the two presentations. If a full spectral subspace above the good interval had dimension greater than the codimension \(c\), it would intersect \(\operatorname{im}V_j\), contradicting its upper Rayleigh bound. The same applies below the good interval. Thus at most \(c\le c_{\rm loc}\) eigenvalues lie above, and at most \(c\) below.

Write \(d=q[J(t_j)-J(t_i)]\). By the elementary elliptic coefficient inequality \(J(t)\le[(1+t)\log(1+t)-t\log t]/2\), valid for all \(t>0\), we have \(0\le d<q\) in the present range. Equation (LX9) puts every actual logarithm in \([0,B_{\rm all}]\). Upper exceptional deviations total at most \(c(B_{\rm all}-d)\); lower ones total at most \(cd\). Their sum is at most \(cB_{\rm all}\), retaining the complete exceptional quotient. Consequently
\[
\boxed{\Omega_{0j}:=\sum_{a=1}^m|\log\lambda_a-qJ(t_j)|
\le mE_{\rm loc}+c_{\rm loc}B_{\rm all}.}
\tag{LX31}
\]
Subtracting (LX29) at the two endpoints gives the all-pair estimate
\[
\boxed{\Omega_{ij}:=\sum_{a=1}^m|\log\lambda_a-d|
\le2mE_{\rm loc}+c_{\rm loc}B_{\rm all},\quad0\le i\le j\le q+1.}
\tag{LX32}
\]
This improves the incoming \(2c[B_{\rm all}+d]\). Define the useful explicit native discrepancy
\[
\boxed{e_{\rm native}(k,b,R)=\frac{mE_{\rm loc}+c_{\rm loc}B_{\rm all}}{mq}.}
\tag{LX33}
\]
The same quantity bounds uniformly the difference between the actual logarithmic determinant profile divided by \(mq\) and \(J(t_j)\). This follows by summing the signed logarithms and then the absolute deviations, not by a rank allocation.

## 8. One growing radius and one growing band

Put
\[
L_k=\log(k+e),\qquad R_k=e^{2\sqrt{L_k}},\qquad
b_k=8\left\lceil\frac{4q}{\sqrt{L_k}}\right\rceil.
\tag{LX34}
\]
Use this choice only when (LX17), (LX24), and \(\zeta\le1/4\) hold. All are inequalities in finite displayed data. We verify that they hold eventually, with the original source fixed.

First \(b_k/q=32/\sqrt{L_k}+O(q^{-1})\), \(\Delta=O(k)\), and \(\rho=O_h(k^{-1})\). Thus the band and root guards eventually hold. Also \(\log\mathcal M_{R_k}=O_A(R_k\log(R_k+2))=o(q)\). The high derivative term in (LX19), after the full coefficient transfer, has logarithm at most
\[
12q-\frac{b_k}{4}\log R_k+o(q)\le-4q+o(q).
\]
The low-degree term has logarithm
\[
q\log(6R_k)+\frac{b_k}{8}\log\rho+O_{h,A}(q)+o(q)
=-2q\sqrt{L_k}+O_{h,A}(q).
\]
All factors \(q^{v_0},M_T,\mathcal M_R,(1-\rho)^{-q-q'},2^{q'}\) are included here. The inverse-triangular tail has the still smaller leading exponent \(-16q\sqrt{L_k}\). Hence \(\zeta\le e^{-q}\) eventually.

For (LX24), \(E_Q=O_h(1)\), \(\log r_Q=-(q-b)\log k+O_h(q+b)= -q\log k+o(q\log k)\). The logarithms of \(i_F,i_U\), divided by \(q\), have limiting upper bound at most \(\pi+2\log10+2\log(2\epsilon_0)<0\). Therefore all four guards hold. Their sufficient threshold can be extremely large: already \(b\le q/10\) asks approximately \(\sqrt{\log k}\ge320\). The conclusion is an effective eventual rate, not an assertion of useful numerical enclosures at small native \(k\).

The finite binomial sums and Laguerre factors in (LX27), using \(\binom nh\le(en/h)^h\), give
\[
\mathcal J_{q,b}=O\bigl(b\log(C_1q/b)+b+\log(q+2)\bigr)+E_G(q).
\]
Thus the verified scalar bound \(E_G(q)=O(\log(q+2))\) gives
\[
\boxed{e_{\rm native}
=O_{h,A}\left(\frac{\log L_k}{\sqrt{L_k}}
+\frac{e^{2\sqrt{L_k}}}{k}+\frac{\log\kappa_k}{q}\right).}
\tag{LX35}
\]
The first term includes the original endpoint modulus \(J((b+1)/q)\). The residue dimension contributes the second, because \(N_R=O_A(R)\) and \(m\asymp k\). No fixed-codimension limit is silently exchanged with a moving contour.

## 9. Every positive word direction

Retain \(Q_k=D_kO_k\), \(\deg D_k=q'\), \(\deg O_k=\Delta\), the original word \(T=D_k(M)\), and \(W=D_k\mathcal P_{<\Delta}\). Its kernel has rank \(q'\); the original boundary map \(\pi_\partial\) has that same kernel. The exact identity \(\operatorname{rem}_{Q_k}(Dp)=D\operatorname{rem}_{O_k}p\) retains its complete root factors.

There is a sharper direct full-image tail than the two-stage incoming WE1. For \(p=Da\in W\),
\[
U_Q^{-1}p=[y^qa/O_k]_+,\qquad
\|P_{<q-b}U_Q^{-1}p\|_{c,q}
\le\epsilon_W\|p\|_{c,q},
\]
\[
\epsilon_W=(1-\rho)^{-q'}2^{q+\Delta}\rho^{b-\Delta},
\qquad\zeta_W=e^{12q}(1+\rho)^q\epsilon_W.
\tag{LX36}
\]
Indeed the inverse leading block of \(D\) bounds the scaled coefficients of \(a\) by \((1-\rho)^{-q'}\|p\|_{c,q}\). The reciprocal coefficients of \(O_k\) have bound \(\binom{\Delta+j-1}j\rho^j\), and the depths needed to lie below \(q-b\) are at least \(b-\Delta\). Their total count through depth \(q-1\) is \(\binom{q+\Delta-1}{q-1}\le2^{q+\Delta}\). This proves (LX36) on every image vector. Its connecting maps are also proved in [025 PH3--8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/6cf5b3aa8ff395eba6b5512b28d117334da5767b/workbenches/splitzero-tandem/continuations/20260922-cutoff-profile/PHASE_HEAT_PROOFS.md#L34).

With \(\zeta_W\le1/4\), (LX25),(LX27) give on the entire fixed image
\[
e^{-qJ(t_j)-a_W}G_{W,N_0}\preceq G_{W,N_j}
\preceq e^{-qJ(t_j)+a_W}G_{W,N_0},
\quad a_W=\mathcal J_{q,b}+2C_Q+2\log\frac{1+\zeta_W}{1-\zeta_W}+\log\kappa_k.
\tag{LX37}
\]
There is no finite-rank subtraction for this statement. For example the incoming band \(b=8\lceil16q/\log(1/\rho)\rceil\), together with all the same finite guards, gives \(\zeta_W\le e^{-q}\) eventually and
\(a_W=O_h(q\log\log k/\log k+\log\kappa_k+1)\). The original full image, not only its determinant, is controlled.

For an entirely explicit low-energy band put \(R_*=k\sqrt{\delta^2+\gamma^2}\), \(\epsilon_*=2^{-32}\), \(T_*=\epsilon_*q\), and require \(R_*\le T_*/2\), \(\Delta\le q/10\), \(q'\ge36\). Let
\[
K_D=2\sqrt2M_\sigma\Delta^2q^{-1/2}10^{2\Delta}e^{\pi q}
(\epsilon_*+\rho)^{2q'},
\quad E_D=\frac{2q'(R_*/T_*)}{1-R_*/T_*}+\log(1+K_D).
\tag{LX38}
\]
For every \(\deg h<\Delta\),
\(e^{-E_D}\|y^{q'}h\|_\sigma^2\le\|Dh\|_\sigma^2\le e^{E_D}\|y^{q'}h\|_\sigma^2\).
On the exterior use all \(q'\) factors and \(|\log|1-z||\le |z|/(1-|z|)\). On the interior the degree-\(\Delta-1\) Legendre evaluation bound gives \(\Delta^210^{2\Delta}/q\) times \(\int_q^{2q}|h|^2\); the latter contributes at least \(q^{2q'}e^{-\pi q}/(2\sqrt{2q})\) times itself to the reference outer norm. Both inner integrals are therefore at most \(K_D\) times that reference outer norm. Combining these estimates proves (LX38), with both regions retained. Here \(E_D=O_h(k)\).

The scaled boundary Vandermonde \(\mathsf V_{ij}=(\omega_i/q)^j\) obeys
\[
\|\mathsf V\|\le\Delta,\qquad
\|\mathsf V^{-1}\|\le V_-:=\Delta((q+R_*)/(2\delta))^{\Delta-1}.
\tag{LX39}
\]
These are respectively its Frobenius bound and the complete Lagrange coefficient bound; every pair of distinct original roots has separation at least \(2\delta\). If a domain boundary value is \(b\), the word image is \(Dh\) with \(h(\omega_i)=b_i\), so this is the actual word coordinate map, with no omission of the factors \(D(\omega_i)\).

The full boundary quotient satisfies
\[
(A_\partial)^{-1}I\preceq G_N^{\partial,\sigma}\preceq B_\partial I,
\]
\[
A_\partial=\frac{\Delta e^2}{M_\sigma}(2q+1)^{3/2}(4q+1)^{R_*+1},
\quad B_\partial=\Delta M_\sigma((2\Delta+R_*)/(2\delta))^{2(\Delta-1)}.
\tag{LX40}
\]
For the lower bound the exact Gamma generating function is \((1+t^2)^{-1/4}e^{z\arctan t}=\sum c_n(z)t^n\), with orthonormal multiplier squared \(n!/(M_\sigma(1/2)_n)\le(2n+1)/M_\sigma\). Cauchy's estimate at \(|t|=N/(N+1)\), the complete complex bound \(|\arctan t|\le\tfrac12\log(2N+1)\), and summation give evaluation kernel at most \(e^2(N+1)^{3/2}(2N+1)^{R_*+1}/M_\sigma\). The trace of the full boundary covariance gives its operator bound. For the upper bound, each degree-\(\Delta-1\) Lagrange lift has norm bounded by multiplying all factors with \(\|(y-z)P\|_\sigma\le[2(L+1)+|z|]\|P\|_\sigma\); Cauchy--Schwarz over the \(\Delta\) lifts gives (LX40). These rederive [018 IC12--13](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md#L125).

Let \(\mathcal L_{q,\Delta}\) be the full low coefficient constant in (LX27) with \(n=q-\Delta=q'\). Put
\[
c_0=2q\log q+[2\log(4/\pi)-2]q,
\]
\[
e_0=E_D+\log\mathcal L_{q,\Delta}+\log\kappa_k+2\log\Delta
+2\log\max(1,V_-)+\log\max(1,A_\partial)+\log\max(1,B_\partial)
+|\log d_{q'}-c_0|.
\tag{LX41}
\]
The word image form just proved, divided by the actual attained boundary metric, has all its \(\Delta\) positive energies in \([e^{c_0-e_0},e^{c_0+e_0}]\). The other \(q'\) energies are exactly zero. The numerator and denominator source transfers together cost \(\log\kappa_k\). The scalar Gamma mass bound gives \(|\log d_{q'}-c_0|\le2\Delta(\log q+1)+|2\log(4/\pi)-2|\Delta+5\); hence \(e_0=O_h(k\log q)\).

The full boundary metric changes by at most
\(\omega_k=\log\kappa_k+\log\max(1,A_\partial)+\log\max(1,B_\partial)\).
Applying the fixed image form comparison (LX37) and the exact boundary minimum to every positive direction yields
\[
\boxed{|\log\lambda_a^+(T^{\dagger_{G_{N_j}}}T)-[c_0-qJ(t_j)]|
\le e_{\rm word}:=e_0+a_W+\omega_k,
\quad a\le\Delta,\quad0\le j\le q+1.}
\tag{LX42}
\]
On the displayed guards, the verified scalar remainder gives \(e_{\rm word}=O_h(q\log\log k/\log k+k\log q)=o(q)\). All positive energies, complete boundary quotients and exact zero directions remain present. This supplies the original phase/heat receivers; it does not evaluate the separate phase-bearing arithmetic-current numerator.

## 10. The same finite improvement on every fixed subquotient

Let \(I_S:\mathbb C^s\hookrightarrow\mathbb C^m\) be any fixed coefficient inclusion, and let \(R:\mathbb C^s\twoheadrightarrow\mathbb C^r\) be any fixed onto map. At every original cutoff define the complete restriction and attained quotient
\[
H_{S,N}=I_S^*H_{K,N}I_S,\qquad
Q_N=(RH_{S,N}^{-1}R^*)^{-1}.
\]
This includes every specified \(S_k/R_k\) by choosing an onto coordinate map with kernel \(R_k\). The relative restriction is the exact isometric compression in (LX30), with \(I_G\) replaced by \(I_S\). For the quotient put
\[
A_S=H_{S,N_j}^{-1/2}H_{S,N_i}H_{S,N_j}^{-1/2},\qquad
W_j=H_{S,N_j}^{-1/2}R^*Q_{N_j}^{1/2}.
\]
Then direct multiplication proves
\[
W_j^*W_j=I_r,\qquad
W_j^*A_S^{-1}W_j
=Q_{N_j}^{1/2}Q_{N_i}^{-1}Q_{N_j}^{1/2}
=(Q_{N_j}^{-1/2}Q_{N_i}Q_{N_j}^{-1/2})^{-1}.
\tag{LX43}
\]
Thus inversion, isometric compression and inversion give exactly the relative quotient. The spectral dimension argument from Section 7 applies at each step. Restriction cannot increase the number of eigenvalues above or below a fixed threshold; inversion reverses the two thresholds; the second inversion restores them. Hence the quotient still has at most \(\min(c_{\rm loc},r)\) logarithms on either side of the good band. The full nesting bound \([0,B_{\rm all}]\) is preserved because the quotient takes the full minimum of the same pair of comparable forms.

With \(d=q[J(t_j)-J(t_i)]\), the separate exceptional deviations are again at most \(c d\) and \(c(B_{\rm all}-d)\). Therefore
\[
\boxed{\sum_{a=1}^r|\log\lambda_a(Q_{N_j}^{-1/2}Q_{N_i}Q_{N_j}^{-1/2})-d|
\le r E_{ij}+\min(c_{\rm loc},r)B_{\rm all},}
\quad E_{0j}=E_{\rm loc},\quad E_{ij}=2E_{\rm loc}\ (i>0).
\tag{LX44}
\]
These are the original fixed coefficient subquotients, with their cutoff-dependent minimizing sections retained through (LX43). In particular a fixed-rank quotient keeps its finite exceptional term; it is not assigned a vanishing error merely because the full kernel rank grows.

## 11. Provenance and scope

The new finite contour and original-metric proof is LX6--26. The sharper exceptional penalty is LX31--33; the growing choice is LX34--35; the full word control is LX36--42; the complete fixed-subquotient improvement is LX43--44. The input's LC1--15, SQ1 and WE1--9 are supported with these strengthened finite discrepancies and with the proved scalar constant 83 in LX5. The positive Gamma envelopes and scalar estimate are proved in the companion EG1--24; no numerical native period or actual native Gram matrix is claimed to have been evaluated here.

Human formula provenance is retained: R. A. Askey and R. Roy for the Gamma equations; T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt for the original Legendre and Meixner--Pollaczek formulas [DLMF18.12.E11](https://dlmf.nist.gov/18.12.E11.tex), [18.22.E8](https://dlmf.nist.gov/18.22.E8.tex), [18.23.E7](https://dlmf.nist.gov/18.23.E7.tex). The retained original equation TeX was read, and the source ledger records its exact bytes, reading coverage and receiving equations. The zero-count, harmonic and contour steps are proved above from their explicit kernels, so the finite constants do not depend on an unnamed external asymptotic theorem.
