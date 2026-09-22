# Arbitrary-cutoff phase and measured-heat profile in the original metrics

This proof checks CP37–51 and completes the measured-heat argument appearing only in the first part of the supplied continuation. The original physical scale, complete observation, full kernel frame, zero-word factors and cutoff indexing are retained. The stronger heat estimates below follow from an exact convolution, and do not assign a sign to the separate arithmetic-current insertion.

The scalar power-jet profile CP9/27/33 and the evaluated function \(\mathfrak J\) are established in the companion independent derivations. Their actual finite errors enter here explicitly; they are not assumed to vanish without those calculations.

## 1. Original data and the image polynomial map

Retain
\[
 q=(k+1)^2,\quad q'=(k-7)^2,\quad \Delta=q-q'=16k-48,\quad
 m=8k-16,\quad k\equiv1\pmod4,
\]
\[
 Q_k(y)=\prod_{a,b=0}^{k}[y-(2b-k)\gamma+i(2a-k)\delta]
       =D_k(y)O_k(y),\quad
 E_k=\mathbb C[y]/(Q_k),\quad M[p]=[yp],\quad T=D_k(M).
 \tag{PH1}
\]
The physical coordinate is \(s=k/2+iy\), with the original fixed period, branch, arithmetic unit and \(0<\delta<1/2,\gamma>2\). The degrees are \(\deg D_k=q'\), \(\deg O_k=\Delta\). The original complete-source quotient metric at degree \(N\) is \(G_N>0\); no new source is substituted. For the original onto observation \(\Lambda\), retain its complete fixed kernel inclusion \(I_K\), \(K=\ker\Lambda\), and
\[
 H_{K,N}=I_K^*G_NI_K,\quad
 Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
 L_N=G_N^{-1}\Lambda^*Q_{B,N}.
 \tag{PH2}
\]
Use \(N_j=q-1+j\), \(0\le j\le q+1\), \(t_j=j/q\).
In particular \(j=q+1\) is the actual cutoff \(2q\).
All subsequent heat averages explicitly use only \(0\le j<q\), as in the supplied paste; this does not remove the extra original cutoff from the determinant or phase statements.

Write \(\|p\|_{c,q}=\sum_aq^a|[y^a]p|\), and
\(\rho=k\sqrt{\delta^2+\gamma^2}/q\). The finite coefficient estimates below have the stated guard \(0<\rho<1\), which holds for all sufficiently large \(k\) at the retained fixed data.
The exact polynomial-part map and its inverse are
\[
 U_Qf=[Q_k(y)y^{-q}f(y)]_+,\qquad
 U_Q^{-1}p=[y^qp(y)/Q_k(y)]_+.
\]
They are unit triangular on degree \(<q\). More generally, multiplication and polynomial-part division at infinity give
\[
 U_Q(f+y^qh)=U_Qf+Q_kh,\qquad
 U_Q^{-1}(D_ka)=\left[\frac{y^qa(y)}{O_k(y)}\right]_+ .
 \tag{PH3}
\]
The equalities retain every relation column and every affine fibre.

For completeness, put
\(\widehat D(x)=q^{-q'}D_k(qx)\),
\(\widehat O(x)=q^{-\Delta}O_k(qx)\),
\(\widehat p(x)=p(qx)\),
\(\widehat a(x)=q^{q'}a(qx)\).
Every root of the two monic polynomials has modulus at most \(\rho\), and
\(\widehat p=\widehat D\,\widehat a\).
Reversing coefficients, the inverse leading triangular block of multiplication by \(\widehat D\) consists of the complete homogeneous coefficients of its roots. Their total absolute sum is at most \((1-\rho)^{-q'}\); hence
\[
 \|\widehat a\|_1\le(1-\rho)^{-q'}\|\widehat p\|_1 .
 \tag{PH4}
\]
Indeed the coefficient of order \(h\) in the reciprocal reversed polynomial is at most
\(\binom{q'+h-1}{h}\rho^h\), and summing the full nonnegative series gives \((1-\rho)^{-q'}\).

For any integer \(s>\Delta\), the reciprocal coefficients of \(\widehat O\) are bounded by \(\binom{\Delta+h-1}{h}\rho^h\). A term of
\([x^q\widehat a(x)/\widehat O(x)]_+\)
below degree \(q-s\) has depth at least \(s-\Delta\), and every depth contributing to its polynomial part is at most \(q-1\). Summing all these terms, using
\(\sum_{h=0}^{q-1}\binom{\Delta+h-1}{h}
=\binom{\Delta+q-1}{q-1}\le2^{q+\Delta}\), proves the full inverse-tail bound
\[
 \|P_{<q-s}U_Q^{-1}p\|_{c,q}
 \le \epsilon_{\rm tail}(q,s)\|p\|_{c,q},\qquad
 \epsilon_{\rm tail}=(1-\rho)^{-q'}2^{q+\Delta}\rho^{s-\Delta},
 \quad p\in W:=D_k\mathcal P_{<\Delta}.
 \tag{PH5}
\]
This proves the more direct full-image estimate in the paste.
Similarly, the elementary symmetric coefficients of \(\widehat D\) give
\[
 \|P_{<q-s/2}p\|_{c,q}
 \le(1-\rho)^{-q'}2^{q'}\rho^{s/2-\Delta}\|p\|_{c,q}
 \tag{PH6}
\]
whenever \(s/2>\Delta\); the looser bound also holds when its displayed right-hand multiplier is at least the full multiplication estimate. Integer depths only improve the real exponent written in PH6. Thus CP38 has a valid finite root-product proof, with its degree and radius guards explicit.

Here is a complete finite norm-transfer guard. In the coefficient coordinates \(x_a=q^a[y^a]p\), let \(\widetilde G_N\) represent \(G_N\), and set
\[
 a_*=\frac1q\min_{q-1\le N\le2q}\lambda_{\min}(\widetilde G_N),
 \quad b_*=\max_{q-1\le N\le2q}\lambda_{\max}(\widetilde G_N),
 \quad M_Q=(1+\rho)^q .
\]
Then \(a_*\|p\|_{c,q}^2\le\|p\|_{G_N}^2\le b_*\|p\|_{c,q}^2\), since
\(\|x\|_2\le\|x\|_1\le\sqrt q\|x\|_2\).
Elementary symmetric coefficients of \(Q_k\) give \(\|U_Q\|_{c,q}\le M_Q\).
Define
\[
 \vartheta=\sqrt{b_*/a_*}\,M_Q\epsilon_{\rm tail}.
 \tag{PH7}
\]
On the explicit guard \(\vartheta<1\), the fixed map
\(A_Wp=P_{\ge q-s}U_Q^{-1}p\) is injective on all of \(W\), and
\[
 (1-\vartheta)\|p\|_{G_N}
 \le\|U_QA_Wp\|_{G_N}
 \le(1+\vartheta)\|p\|_{G_N}\quad\text{for every }N.
 \tag{PH8}
\]
The proof is the triangle inequality applied to
\(p-U_QA_Wp=U_QP_{<q-s}U_Q^{-1}p\), followed by PH5 and the two coefficient bounds.
If \(A_Wp=0\), PH8 forces \(p=0\).
This is a map on every original image direction; no exceptional residue subspace is used.

For the following complete source comparison impose the further finite band guard
\(\Delta<s\le q/10\). The asymptotic choice below uses \(0<\epsilon<1/10\).

The complete high-power source comparison [CK3 and CK10–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L101) supplies the same actual two constants at every cutoff and every band vector \(g\):
\[
 a_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2}
 \le\|U_Qg\|_{G_N}^{\,2}
 \le b_k^{\rm src}\|g\|_{\mathrm{pow},N}^{\,2},\quad
 a_k^{\rm src}=\ell_ke^{-C},\quad b_k^{\rm src}=u_ke^C,\quad
 \chi_k=\log(b_k^{\rm src}/a_k^{\rm src})=2C+\log(u_k/\ell_k).
\]
Its terms are the complete two-region \(U_Q\) comparison and the actual arithmetic/Gamma form comparison; no observation row is substituted for a form.
Let \(q\delta(q,s)\) be the independently established all-vector error in CP27–28:
\[
 \left|\log\frac{\|g\|_{\mathrm{pow},N_0}^{\,2}}
 {\|g\|_{\mathrm{pow},N_j}^{\,2}}
 -q\mathfrak J(t_j)\right|\le q\delta(q,s).
\]
Combining these inequalities with PH8, keeping both endpoints, gives on all \(W\)
\[
 \left|\log\frac{\|p\|_{G_{N_0}}^2}{\|p\|_{G_{N_j}}^2}
       -q\mathfrak J(t_j)\right|\le q\zeta(q,s),
 \quad
 \zeta(q,s)=\delta(q,s)+\frac{\chi_k+
 2\log((1+\vartheta)/(1-\vartheta))}{q}.
 \tag{PH9}
\]
To verify the last constant directly, at each cutoff the logarithm
\(\log(\|p\|_{G_N}^2/\|A_Wp\|_{\mathrm{pow},N}^2)\)
belongs to
\([\log a_k^{\rm src}-2\log(1+\vartheta),\,\log b_k^{\rm src}-2\log(1-\vartheta)]\).
Its possible two-cutoff difference is exactly bounded by the width used in PH9.

For fixed \(s=\lfloor\epsilon q\rfloor\), PH5 has logarithm
\(-c\epsilon q\log k+O(q)\), whereas the complete original coefficient comparison has logarithm \(O(q)\). Thus \(\vartheta\to0\).
The proved power estimate gives
\(\limsup\delta(q,s)=O(\epsilon\log(C/\epsilon))\);
the complete source comparison has \(\chi_k=o(q)\).
Taking \(k\to\infty\) first and then \(\epsilon\downarrow0\), or taking the exact infimum of PH9 over its finitely many admitted integer \(s\), proves a common \(\zeta_k\to0\). This is CP39 with the full norm error displayed. It uses the companion power and source estimates at their proved status, not a new equilibrium assumption.

## 2. Full positive-word centre and paired compressed energies

Let \(\pi_\partial:E_k\to\mathbb C^\Delta\) be the original boundary-value map, with kernel \(V=\ker T\), and
\(B_N^\partial=(\pi_\partial G_N^{-1}\pi_\partial^*)^{-1}\).
Let \(I_W:\mathbb C^\Delta\to W\) be the fixed boundary-value frame, so that
\(G_{W,N}=I_W^*G_NI_W\) and \(T=I_WD_\partial\pi_\partial\), where
\(D_\partial\) contains the unchanged values \(D_k(\omega)\).
The minimum section
\(S_N=G_N^{-1}\pi_\partial^*B_N^\partial\)
satisfies \(\pi_\partial S_N=I\) and \(S_N^*G_NS_N=B_N^\partial\); its image is \(V^{\perp_{G_N}}\).
Therefore the positive energies of \(H_N=G_N^{-1}T^*G_NT\) are exactly the generalized eigenvalues of
\[
 F_N^W=D_\partial^*G_{W,N}D_\partial
 \quad\text{against}\quad B_N^\partial.
 \tag{PH10}
\]
This proves CP37 with its actual domain, codomain and metric. The other \(q'\) full-word energies are exactly zero.

Let \(c_0=2q\log q+[2\log(4/\pi)-2]q\), and let
\(E_0=\max_{a\le\Delta}|\log\lambda_{a,N_0}^+-c_0|\) be the original initial-word error.
The complete boundary comparison gives
\(e^{-\omega_k}B_{N_0}^\partial\preceq B_{N_j}^\partial\preceq B_{N_0}^\partial\),
where \(\omega_k=\log(b_\partial/a_\partial)\), and the second inequality is source nesting.
By PH9 and generalized min–max,
\[
 -E_0-q\zeta_k
 \le\log\lambda_{a,N_j}^+-c_k(t_j)
 \le E_0+q\zeta_k+\omega_k,\qquad
 c_k(t)=c_0-q\mathfrak J(t).
 \tag{PH11}
\]
One may replace \(\omega_k\) at \(j\) by the actual
\(\log\lambda_{\max}((B_{N_j}^\partial)^{-1/2}
 B_{N_0}^\partial(B_{N_j}^\partial)^{-1/2})\).
Thus the single finite error
\(e_k=E_0/q+\zeta_k+\omega_k/q\) proves CP40 at all \(q+2\) actual cutoffs.
The initial error obeys \(E_0\le\mathcal E_k=O_{h,\varpi}(k\log(q+2))\) by
[019 FW8–9, including their explicit constants](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/WORD_PROOFS.md#L80).
For all \(q-1\le N\le2q\), put \(R_k=k\sqrt{\delta^2+\gamma^2}\) and retain
\[
 A_{2q}^{\partial}=\frac{\Delta e^2}{\sqrt{2\pi}}
 (2q+1)^{3/2}(4q+1)^{R_k+1},\qquad
 B_k^\partial=\Delta\sqrt{2\pi}
 \left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)}.
\]
The complete boundary evaluation and Lagrange-lift proofs
[018 IC12–15](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md#L125)
give the native constants
\(a_\partial=\ell_k/A_{2q}^{\partial}\),
\(b_\partial=u_kB_k^\partial\).
Consequently
\(\omega_k=\log[(u_k/\ell_k)A_{2q}^{\partial}B_k^\partial]
=O_{h,\varpi}(k\log(q+2))=o(q)\).
This uses the actual source ratio in CK3, whose logarithm is \(O(k+\log q)\), and the displayed boundary factors.
It proves both required vanishing errors on the entire cutoff window; hence \(e_k\to0\).
In particular \(\eta(t)=c_k(t)/q-2\log q
=2\log(4/\pi)-2-\mathfrak J(t)\), including the original endpoints.

For the kernel put \(F_{K,N}=(TI_K)^*G_N(TI_K)\).
On the native transverse family it is positive and its compressed energies are the eigenvalues
\(\alpha_{a,N}\) of
\(A_N=H_{K,N}^{-1/2}F_{K,N}H_{K,N}^{-1/2}\).
For arbitrary positive \(P,Q,F\), define
\(R=P^{1/2}\max(I,P^{-1/2}QP^{-1/2})P^{1/2}\).
Then \(R\succeq P,Q\).
Generalized min–max puts the ordered log spectrum of \((F,R)\) below those of \((F,P)\) and \((F,Q)\). Pair each of the latter lists through the lower list, use the triangle inequality, and sum the exact determinant differences to get
\[
 \sum_a|\log\lambda_a(F,P)-\log\lambda_a(F,Q)|
 \le\log\frac{\det R}{\det P}+\log\frac{\det R}{\det Q}
 =\sum_a|\log\lambda_a(P^{-1/2}QP^{-1/2})|.
 \tag{PH12}
\]
This proves CP42 without common eigenvectors.

Restrict PH9 to the fixed image \(TI_K\), cancel the common scalar
\(\exp[-q(\mathfrak J(t_j)-\mathfrak J(t_i))]\) between the two forms, and apply PH12. With the complete relative-kernel discrepancy \(\Omega_{i,j}\) of CP8, one obtains
\[
 D_{i,j}:=\sum_{a=1}^{m}|\log\alpha_{a,N_i}-\log\alpha_{a,N_j}|
 \le \Omega_{i,j}+2mq\zeta_k.
 \tag{PH13}
\]
This proves CP43; its \(o(mq)\) conclusion uses the independently proved CP8 and PH9.
If \(Z=K\cap V\ne0\), replace \(H_{K,N}\) by its actual attained quotient on \(K/Z\), retain \(p=\operatorname{rank}(T|_K)\) positive energies and \(m-p\) zero factors, and use the same fixed image form. In a fixed split frame \([I_Z,I_1]=I_KS\), this quotient is
\(H_{11,N}-H_{01,N}^*H_{00,N}^{-1}H_{01,N}\).
Both the full \(H_{00,N}\) and the fixed frame volume remain in the full kernel determinant. PH12 applies to this positive quotient; its relative log deviation is controlled by the original relative-spectrum compression theorem. No inverse or logarithm of a zero energy is taken.

## 3. Finite determinant, phase and arbitrary-cutoff errors

For each cutoff define the original measured resolvent
\[
 \mathscr Y_N(z)=\Lambda z(zI+H_N)^{-1}L_N .
\]
The actual isometries \(J_{B,N}=L_NQ_{B,N}^{-1/2}\) and
\(J_{K,N}=I_KH_{K,N}^{-1/2}\) are orthogonal complements.
Full block elimination therefore gives
\[
 \det\mathscr Y_N(z)
 =\frac{\det(I_m+A_N/z)}{\det(I_q+H_N/z)} .
 \tag{PH14}
\]
It is valid also when \(A_N\) has zeros. Both dimensions and all zero factors remain in the ratio. Analytic logarithms are continued from infinity on the slit plane.

For a sharper finite error than a uniform maximum, set
\[
 E_j^W=\sum_{a=1}^{\Delta}|\log\lambda_{a,N_j}^+-c_k(t_j)|,\qquad
 \mathcal B_{i,j}=D_{i,j}+E_i^W+E_j^W
 \le D_{i,j}+2\Delta q e_k .
 \tag{PH15}
\]
The derivative of \(a\mapsto\log(1+e^a/z)\) is between zero and one for \(z>0\). Apply its Lipschitz bound to every matched positive energy in PH14:
\[
 \sup_{z>0}\left|
 \log\frac{\det\mathscr Y_{N_i}(z)}{\det\mathscr Y_{N_j}(z)}
 +\Delta\log\frac{z+e^{c_k(t_i)}}{z+e^{c_k(t_j)}}\right|
 \le\mathcal B_{i,j}.
 \tag{PH16}
\]
For \(|\arg z|\le\pi-\delta\), \(0<\delta\le\pi\), the same expression in the continued analytic logarithms is bounded by
\(\csc(\delta/2)\mathcal B_{i,j}\).
Indeed \(|z+s|\ge\sin(\delta/2)(|z|+s)\) implies
\(|s/(z+s)|\le\csc(\delta/2)\). This proves CP45 and its complex extension.

At imaginary frequency, every scalar full resolvent has positive real part and nonnegative imaginary part. Compression preserves the strict positive real part, so the principal matrix logarithm of
\(Q_{B,N}^{1/2}\mathscr Y_N(i\omega)Q_{B,N}^{-1/2}\)
exists. Its trace gives the unwrapped phase anchored at zero as \(\omega\to\infty\).
The determinant identity then proves
\[
 \Theta_N(\omega)=
 \sum_{a=1}^{\Delta}\arctan(\lambda_{a,N}/\omega)
 -\sum_{a=1}^{p}\arctan(\alpha_{a,N}/\omega).
 \tag{PH17}
\]
This is CP46, with the zero-intersection extension explicit.

Let \(f(x)=\arctan(e^x)\); \(f'(x)=1/(2\cosh x)>0\) and
\(\int_{\mathbb R}f'(x)\,dx=\pi/2\).
For any real \(a,b\), Tonelli applied to
\(|f(a-x)-f(b-x)|=\int_{\min(a,b)}^{\max(a,b)}f'(t-x)\,dt\)
proves its exact integral \((\pi/2)|a-b|\).
Therefore
\[
 \int_0^\infty\left|
 \Theta_{N_i}-\Theta_{N_j}
 -\Delta[\arctan(e^{c_i}/\omega)-\arctan(e^{c_j}/\omega)]
 \right|\frac{d\omega}{\omega}
 \le\frac\pi2\mathcal B_{i,j}.
 \tag{PH18}
\]
The signed integral is exactly
\[
 \frac2\pi\int_0^\infty(\Theta_{N_i}-\Theta_{N_j})\frac{d\omega}{\omega}
 =\log\frac{\det_+H_{N_i}}{\det_+H_{N_j}}
  -\log\frac{\det_+A_{N_i}}{\det_+A_{N_j}} ,
 \tag{PH19}
\]
and hence differs from
\(\Delta q[\mathfrak J(t_j)-\mathfrak J(t_i)]\)
by at most \(\mathcal B_{i,j}\).
The equal ranks at both cutoffs make the two frequency ends integrable. The finite equality precedes any asymptotic. The original four signs add the two pairs \((0,q)\) and \((1,q+1)\), preserving both adjacent degrees.

At \(\omega=q^{2q}e^{bq}\), the exact scalar step error is
\[
 \int_{\mathbb R}|\arctan(e^{q(a-b)})-(\pi/2)\mathbf1_{b<a}|\,db
 =\frac{2G_{\rm Cat}}q,\qquad
 G_{\rm Cat}=\int_0^1\frac{\arctan x}{x}\,dx .
\]
Split the integral at \(b=a\), use
\(\arctan x+\arctan(1/x)=\pi/2\), and substitute
\(x=e^{-q|a-b|}\) to prove the constant. Thus for \(i\le j\)
\[
 \int_{\mathbb R}\left|
 \frac{\Theta_{N_i}(q^{2q}e^{bq})-\Theta_{N_j}(q^{2q}e^{bq})}{k}
 -\frac{\pi\Delta}{2k}\mathbf1_{\eta(t_j)<b<\eta(t_i)}
 \right|db
 \le\frac{\pi\mathcal B_{i,j}}{2kq}
      +\frac{4\Delta G_{\rm Cat}}{kq}.
 \tag{PH20}
\]
This proves CP50 with its exact constants. The common error is \(o(1)\), so for fixed \(s<t\) the limiting height is \(8\pi\).

For the step interpolation \(j(t)=\lfloor qt\rfloor\), \(0\le t<1\), the extra two-variable comparison to \(\eta(t)\) has integral at most
\[
 \frac{\pi\Delta}{2k}\int_0^1[\mathfrak J(t)-\mathfrak J(\lfloor qt\rfloor/q)]\,dt
 \le \frac{\pi\Delta\,\mathfrak J(1)}{2kq}.
 \tag{PH21}
\]
The bound follows by monotonicity and upper/lower Riemann sums.
Integrate PH20 in \(t\), then use PH21. Distributional differentiation against any smooth compactly supported test in \(0<t<1\) gives the limit
\(8\pi f(t)\delta_{b=\eta(t)}\), because
\(\eta'(t)=-f(t)\). This proves CP51 without differentiating a pointwise error.

## 4. Complete measured heat and its exact angle defect

For physical heat time \(\tau>0\), retain
\[
 \mathscr Z_N(\tau)=\Lambda e^{-\tau H_N}L_N,\quad
 \Gamma_N=J_{K,N}^*G_NP_{V^{\perp_{G_N}}}J_{K,N},\quad
 \vartheta_N^\Gamma=\operatorname{Tr}\Gamma_N.
 \tag{PH22}
\]
The observed operator is similar by its actual \(Q_{B,N}^{1/2}\) to
\(J_{B,N}^*G_Ne^{-\tau H_N}J_{B,N}\).
The complete orthogonal resolution therefore gives
\[
 \operatorname{Tr}_B\mathscr Z_N(\tau)
 =(q-m-\Delta)+\sum_{\lambda>0}e^{-\tau\lambda}+d_N(\tau),
 \quad
 d_N(\tau)=\operatorname{Tr}[J_{K,N}^*G_N(I-e^{-\tau H_N})J_{K,N}].
 \tag{PH23}
\]
Indeed the full trace is \(q-\Delta+\sum_{\lambda>0}e^{-\tau\lambda}\), and the kernel compression trace is \(m-d_N(\tau)\).
This proves the paste's identity including every zero factor, even at a nonzero intersection \(K\cap V\).

For actual positive spectral bounds \(l_N,u_N\), functional calculus gives
\[
 (1-e^{-\tau l_N})\Gamma_N
 \preceq J_{K,N}^*G_N(I-e^{-\tau H_N})J_{K,N}
 \preceq(1-e^{-\tau u_N})\Gamma_N.
 \tag{PH24}
\]
Taking traces retains the same constants. The bounds are attained at
\(H_N=l_NP\) or \(u_NP\).
Also \(d_N'(\tau)=\operatorname{Tr}(J_K^*G_NH_Ne^{-\tau H_N}J_K)\ge0\).
Thus its range is \([0,\vartheta_N^\Gamma]\), and the exact observed zero-energy trace is
\[
 \operatorname{Tr}_B(\Lambda P_V^{G_N}L_N)
 =q-m-\Delta+\vartheta_N^\Gamma .
 \tag{PH25}
\]
The subtracted integer in the supplied observable is not declared equal to this generally noninteger mass.

Use precisely the declared physical scale and exponent:
\[
 \tau_k(\xi)=q^{-2q}e^{-q\xi},\quad
 u_{a,j}=q^{-1}\log\lambda_{a,N_j}-2\log q,\quad 0\le j<q.
 \tag{PH26}
\]
Then \(\tau_k(\xi)\lambda_{a,N_j}=e^{q(u_{a,j}-\xi)}\).
Keep the original integer-subtracted observable as the primary one:
\[
 F_k(\xi)=\frac1{q\Delta}\sum_{j=0}^{q-1}
 [\operatorname{Tr}_E e^{-\tau_k(\xi)H_{N_j}}-q'],
\]
\[
 M_k(\xi)=\frac1{q\Delta}\sum_{j=0}^{q-1}
 [\operatorname{Tr}_B\mathscr Z_{N_j}(\tau_k(\xi))-(q-m-\Delta)].
 \tag{PH27}
\]
Its complete connecting map is
\[
 M_k=F_k+D_k^{\rm ang},\quad
 D_k^{\rm ang}(\xi)=\frac1{q\Delta}\sum_jd_{N_j}(\tau_k(\xi)),
 \quad0\le D_k^{\rm ang}(\xi)\le
 \alpha_k:=\frac1{q\Delta}\sum_j\vartheta_{N_j}^\Gamma .
 \tag{PH28}
\]
The defect decreases in \(\xi\), from \(\alpha_k\) to zero. Hence
\(M_k(-\infty)=\alpha_k\) and \(M_k(+\infty)=1\).
The sharper frequency-dependent bounds are those of PH24, summed at the actual cutoffs.

The inherited full-angle bound, retained as a finite sum, is
\[
 \gamma_{v+r,N}\le\min(1,\mathfrak B_kr^{-2q'})
 \ \Longrightarrow\
 \vartheta_N^\Gamma\le
 \min\!\left(m,v+\sum_{r=1}^{(m-v)_+}\min(1,\mathfrak B_kr^{-2q'})\right)
 =:T_k^{\Gamma,\mathrm{fin}}.
 \tag{PH29}
\]
For \(v\ge m\), use \(T_k^{\Gamma,\mathrm{fin}}=m\).
For \(q'>1/2\), putting \(J=\lceil\mathfrak B_k^{1/(2q')}\rceil\) and integrating the decreasing tail gives the further bound
\(\min(m,v+J[1+(2q'-1)^{-1}])\).
Thus \(\alpha_k\le T_k^{\Gamma,\mathrm{fin}}/\Delta\).
Here is the exact provider and its map to this primary angle operator.
The complete source is the published
[024 original measured-word proof, equations (10)–(24)](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/RETAINED_COMPLETE_PROOF_SOURCES.tex#L348274);
its full conductor-to-invariant compression and trace sum are at
[equations (21)–(24)](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/RETAINED_COMPLETE_PROOF_SOURCES.tex#L348677).
The following reconstruction retains its constants and proves why it applies at every cutoff here.

In full root-value coordinates let
\(\mathcal J_\partial b=(F b,b)\), where
\(F=-A_{\mathcal I}^{-1}A_\partial\) is the actual conductor graph.
Its image is \(V_A\), the complete conductor kernel, which contains \(K\).
Put
\[
 H_{A,N}=\mathcal J_\partial^*G_N^{\rm val}\mathcal J_\partial,\quad
 B_K=\pi_\partial I_K^{\rm val},\quad
 I_K^{\rm val}=\mathcal J_\partial B_K .
 \tag{PH29a}
\]
The full Vandermonde \(\mathsf V\) gives
\(G_N^{\rm val}=\mathsf V^{-*}G_N\mathsf V^{-1}\) and
\(I_K^{\rm val}=\mathsf V I_K\), so these equalities preserve the actual metric.
Let \(v=\operatorname{ord}_0E_A\), where the unchanged conductor symbol is
\(E_A(w)=\sum_\beta a_\beta e^{b_\beta w}\).
The polynomials of degree below \(v\) give a \(v\)-dimensional subspace
\(\mathcal L\subset V_A\).
Choose a coisometry
\(\Pi:\mathbb C^\Delta\to\mathbb C^{\Delta-v}\)
with \(\ker\Pi=\pi_\partial\mathcal L\).
The covariance of its full attained quotient is exactly
\(\Pi H_{A,N}^{-1}\Pi^*\), by minimizing a positive quadratic form on each affine fibre.

For a row \(z\) of this full coisometry define the original functional
\[
 F_z(w)=\sum_{\beta\in\partial}z_\beta e^{\beta w},\qquad
 A_z(w)=e^{-(k/2-4)w}F_z(w)/E_A(w),\qquad
 \ell_z[f]=[f(-i\partial_w)A_z(w)]_{w=0}.
\]
The first \(v\) numerator derivatives vanish, so the displayed quotient is holomorphic at zero.
The exact conductor identity is
\(\ell_z[\mathcal T_Ap]=z\mathsf Vp\).
On every source representative with value in \(V_A\),
\(\mathcal T_Ap\) belongs to the entire lower-root ideal
\(I_N=Q_-\mathcal P_{N-v-q'}\).
The complete weighted conductor norm in the retained proof is
\[
 \mathfrak M_k=\max\{1,\,
 e^{1+2\pi\gamma}A_{\rm abs}(8q+1)^{1/4}
 (2q+1)(4q+1)^{4\delta}\},\qquad
 A_{\rm abs}=\sum_\beta|a_\beta|,
\]
and it proves
\(\|\mathcal T_Ap\|_\sigma
\le\mathfrak M_k\ell_k^{-1/2}\|p\|_{\mu_k}\).
Let \(C_N^{\rm ideal}\) be the complete covariance of the displayed functionals on \(I_N\) with its full Gamma norm.
Taking the supremum of the squared functional over every identical source fibre, then the minimum source norm, proves
\[
 \Pi H_{A,N}^{-1}\Pi^*
 \preceq(\mathfrak M_k^2/\ell_k)C_N^{\rm ideal}.
 \tag{PH29b}
\]
In detail, for a row combination \(z\), the numerator
\(|z\mathsf Vp|^2\) equals \(|\ell_z[\mathcal T_Ap]|^2\),
which is at most its ideal dual norm squared times
\(\mathfrak M_k^2\|p\|_{\mu_k}^2/\ell_k\).
Supremizing over all representatives proves the quadratic-form inequality.
This retains the full conductor quotient; it is not a replacement of \(K\).

Here are finite constants for all ideal eigenvalues, not just asymptotic notation.
Set \(R_h=\sqrt{\delta^2+\gamma^2}\),
\(B_A=\max|b_\beta|\), \(d_{\rm cond}=|E_A^{(v)}(0)|/v!>0\),
\(\bar B_A=\max(1,B_A)\), and
\[
 a_A=\frac{\log^+(A_{\rm abs}/d_{\rm cond})}{\log2},\quad
 b_A=\frac{4B_A}{\log2},\quad L_A=b_A+9,\quad
 j_A=\left\lceil\max\{2(a_A+1),a_A+1+4L_A\}\right\rceil ,
\]
\[
 \rho_A=\min\left\{1,\frac{(v+1)!\,d_{\rm cond}}
 {2A_{\rm abs}\bar B_A^{v+1}e^{\bar B_A}}\right\},\quad
 C_{\rm an}=\frac{\max(A_{\rm abs},d_{\rm cond})^2}{d_{\rm cond}^3},
 \quad c_\sigma=\Gamma(1/4)^2/(2\pi),\quad M_{\max}=2q-v-q',
\]
\[
 \mathfrak A_k=(M_{\max}+1)10^{M_{\max}}2^{q'}e^{\pi q/2}
 \sqrt{\frac{1+16q^2}{c_\sigma q}},\quad
 \mathfrak F_k=\mathfrak A_kC_{\rm an}\sqrt{\Delta}\,
 e^{2R_hq+(8+4B_A)k}(R_h+2)^{q'},
\]
\[
 M_{0,k}=2\sqrt\Delta\,\rho_A^{-v}d_{\rm cond}^{-1}
 e^{(4+kR_h)\rho_A},\quad
 \mathfrak F_{0,k}=\mathfrak A_kM_{0,k}
 (kR_h/q+2/\rho_A)^{q'}(2/\rho_A)^{M_{\max}},
\]
\[
 \mathfrak U_k=\max\{\mathfrak F_k^2(4L_A)^{2q'},
 \mathfrak F_{0,k}^2j_A^{2q'}\}.
 \tag{PH29c}
\]
Their finite domain includes \(v<\Delta\), \(N-v\ge q'\),
and \(q\ge2kR_h\); eventually all hold in the fixed-data family.
The full-strip proof in equations (14)–(20) of the cited source is as follows.
Jensen's formula bounds the number of conductor zeros in \(|w|<2R\),
with multiplicity, by \(a_A+b_AR\).
Imposing their numerator cancellations costs at most that codimension.
The radius-\(2R\) Blaschke quotient, followed by the zero-free
Harnack bound on radius \(R\), gives
\(\sup_{|w|\le R}|A_z(w)|
\le C_{\rm an}\sqrt\Delta e^{(2kR_h+8+4B_A)R}\|z\|\).
The Gamma product lower bound
\(\sigma(y)\ge c_\sigma e^{-\pi|y|/2}/(1+4y^2)\),
all \(q'\) root factors on \([q,2q]\), and the full shifted Legendre basis give
\(\|\operatorname{coef}p(q\cdot)\|_1
\le\mathfrak A_kq^{-q'}\|Q_-p\|_\sigma\).
Apply Cauchy's derivative estimate through every degree \(N-v\le2q\).
For \(2\le R\le k\), the resulting dual bound is
\(\|\ell_z|_{I_N}\|\le\mathfrak F_kR^{-q'}\|z\|\).
The Taylor remainder of \(E_A(w)/w^v\) on \(\rho_A\) is at most \(d_{\rm cond}/2\), so unrestricted rows have dual norm at most \(\mathfrak F_{0,k}\).
For \(j\ge j_A\), take \(R_j=(j-1-a_A)/(2L_A)\).
Then \(R_j\ge2\), \(R_j\ge j/(4L_A)\), and
\(a_A+b_AR_j<j\).
The full strip has dimension \(g=\Delta-v<16k\), hence
\(R_j<g/(2L_A)<k\); this checks the extended rank range explicitly.
Min–max on the cancellation subspace and the unrestricted estimate at the first indices now prove
\[
 \lambda_j^\downarrow(C_N^{\rm ideal})
 \le\mathfrak U_kj^{-2q'},\qquad1\le j\le\Delta-v,\qquad
 \log\mathfrak U_k=O_{h,\varpi}(q).
 \tag{PH29d}
\]
The full source proofs of the Gamma, Legendre, disk and derivative estimates are retained in
[019 AS12–25](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/9b7b0bad40b33dc88bba7d8cb1548da1fadbb585/workbenches/splitzero-tandem/continuations/20260921-original-angle-word/ANGLE_PROOFS.md#L186)
and the cited 024 extension. Only the strip dimension changes from the earlier invariant-row use; PH29c–d include that change in both square-root factors and the upper radius guard.

Now form the whole-conductor angle and the exact invariant-kernel isometry
\[
 \Gamma_{A,N}=H_{A,N}^{-1/2}B_N^\partial H_{A,N}^{-1/2},
 \quad U_{K,N}=H_{A,N}^{1/2}B_KH_{K,N}^{-1/2}.
\]
PH29a gives \(U_{K,N}^*U_{K,N}=I_m\), and direct multiplication gives
\[
 \Gamma_N=U_{K,N}^*\Gamma_{A,N}U_{K,N}.
 \tag{PH29e}
\]
The boundary minimum is no larger than the norm of its particular conductor lift, so \(0\preceq\Gamma_{A,N}\preceq I_\Delta\).
The full boundary interpolation above gives \(B_N^\partial\preceq u_kB_k^\partial I\).
Thus min–max, followed by the coisometry interlacing that deletes exactly \(v\) directions, and then PH29b–d, yields
\[
 \gamma_{v+j,N}^\downarrow
 \le u_kB_k^\partial\lambda_{v+j}^\downarrow(H_{A,N}^{-1})
 \le u_kB_k^\partial\lambda_j^\downarrow(\Pi H_{A,N}^{-1}\Pi^*)
 \le\mathfrak B_kj^{-2q'},\quad
 \mathfrak B_k=\max\{1,(u_k/\ell_k)B_k^\partial\mathfrak M_k^2\mathfrak U_k\}.
 \tag{PH29f}
\]
There is no conductor-graph or invariant-frame condition-number factor.
All constants are uniform for \(q-1\le N\le2q\).
Their displayed formulas give \(\log\mathfrak B_k=O(q)\);
the \(B_k^\partial,\mathfrak M_k\) and \(u_k/\ell_k\) terms contribute \(o(q)\).
Since \(q'/q\to1\) and \(v\) is fixed, PH29's \(J\) is bounded and
\(\sup_N\operatorname{Tr}\Gamma_N=O_{h,\varpi}(1)\).
This proves \(\alpha_k=O(1/\Delta)\to0\) in the original metric.
The finite identities PH22–28 themselves do not require this eventual estimate.

## 5. The exact Gumbel convolution and an improved finite error

Let \(E_{\exp}\) have scalar probability density \(e^{-x}\), \(x>0\), and set \(G_{\rm Gu}=-\log E_{\exp}\). Then
\[
 \mathbb P(G_{\rm Gu}\le x)=e^{-e^{-x}},\qquad
 e^{-e^{q(u-\xi)}}=\mathbb P(u+G_{\rm Gu}/q\le\xi).
 \tag{PH30}
\]
This auxiliary scalar probability represents the physical heat function exactly; it does not replace an arithmetic source.
Consequently \(F_k\) is the distribution function of
\((q\Delta)^{-1}\sum_{j,a}\delta_{u_{a,j}}\) convolved with the law of \(G_{\rm Gu}/q\). The \(q'\) exact zero modes were subtracted before forming this probability.

Put
\(\delta_k=\max_{j<q,a}|u_{a,j}-\eta(t_j)|\le e_k\),
\(f_*=f(1)>0\), and \(L_*=1/f_*\).
The target is the pushforward of Lebesgue probability on \([0,1]\) by the actual evaluated decreasing function \(\eta(t)=\eta(0)-\mathfrak J(t)\):
\[
 \mathcal H(\xi)=\operatorname{Leb}\{t:\eta(t)\le\xi\}
 =\begin{cases}
 0,&\xi\le\eta(1),\\
 1-\mathfrak J^{-1}(\eta(0)-\xi),&\eta(1)<\xi<\eta(0),\\
 1,&\xi\ge\eta(0).
 \end{cases}
 \tag{PH31}
\]
Since \(-\eta'(t)=f(t)\ge f_*\), its distribution function is globally \(L_*\)-Lipschitz.
The exact grid distribution
\(H_q(\xi)=q^{-1}\#\{0\le j<q:\eta(j/q)\le\xi\}\)
satisfies \(0\le\mathcal H(\xi)-H_q(\xi)\le1/q\), by counting the indices above the inverse cutoff. This includes both endpoints.

The absolute smoothing constant is
\[
 C_{\rm Gu}=\mathbb E|G_{\rm Gu}|
 =\int_0^\infty|\log x|e^{-x}\,dx
 =\gamma_{\rm E}+2E_1(1)\le1+e^{-1},
 \quad E_1(1)=\int_1^\infty e^{-x}\frac{dx}{x}.
 \tag{PH32}
\]
Here \(\gamma_{\rm E}=-\int_0^\infty\log x\,e^{-x}dx\) is Euler's constant.
Split the integral at one and integrate the positive logarithmic part by parts to obtain the equality.
For the elementary majorant, discard \(e^{-x}\le1\) on \((0,1)\), giving one, and use \(\log x\le x-1\) on \((1,\infty)\), giving \(e^{-1}\).
Every stated heat error therefore has a finite explicit majorant without native arithmetic values.

Define \(H_q^{\rm Gu}(\xi)=\mathbb E\mathcal H(\xi-G_{\rm Gu}/q)\).
Matching each actual energy to its own cutoff centre and using the one-sided grid discrepancy gives
\[
 H_q^{\rm Gu}(\xi-\delta_k)-1/q
 \le F_k(\xi)\le H_q^{\rm Gu}(\xi+\delta_k).
 \tag{PH33}
\]
Its convolution is \(L_*\)-Lipschitz and differs from \(\mathcal H\) by at most \(L_*C_{\rm Gu}/q\). Consequently
\[
 \boxed{\ \sup_\xi|F_k(\xi)-\mathcal H(\xi)|
 \le L_*\delta_k+\frac1q+\frac{L_*C_{\rm Gu}}q
 =:\varepsilon_k^{\rm heat}.\ }
 \tag{PH34}
\]
This replaces the supplied \(\log q/q\) smoothing cost by \(C_{\rm Gu}/q\).
The supplied bound itself is valid: use the Gumbel tails at \(\pm\log q\), which are \(e^{-q}\) on the left and at most \(1/q\) on the right, in the same shifted distribution argument. This gives
\(L_*(\delta_k+\log q/q)+2/q+e^{-q}\).

The primary original measured observable retains its one-sided defect:
\[
 \mathcal H(\xi)-\varepsilon_k^{\rm heat}
 \le M_k(\xi)\le
 \mathcal H(\xi)+\varepsilon_k^{\rm heat}+D_k^{\rm ang}(\xi)
 \le\mathcal H(\xi)+\varepsilon_k^{\rm heat}+\alpha_k .
 \tag{PH35}
\]
Thus the stated uniform limit follows from the proved \(\delta_k\to0\) and \(\alpha_k\to0\).
No current insertion occurs in this identity or its limiting argument.

## 6. The probability observable and its exact map to the primary heat

An additional probability observable has an exact affine map to \(M_k\); it does not replace it.
On \(\alpha_k<1\), subtract the actual observed zero trace PH25 and divide by the actual remaining mass:
\[
 P_k^{\rm obs}(\xi)=
 \frac{\sum_j[\operatorname{Tr}_B\mathscr Z_{N_j}(\tau_k(\xi))
 -(q-m-\Delta+\vartheta_{N_j}^\Gamma)]}
 {q\Delta-\sum_j\vartheta_{N_j}^\Gamma}
 =\frac{M_k(\xi)-\alpha_k}{1-\alpha_k}.
 \tag{PH36}
\]
On the native family \(\Delta>m\) and \(\vartheta_N^\Gamma\le m\), so this guard holds.
For each full energy projector,
\[
 w_{\lambda,N}
 =\operatorname{Tr}(J_{B,N}^*G_NP_{\lambda,N}J_{B,N})
 =\operatorname{rank}P_{\lambda,N}
 -\operatorname{Tr}(J_{K,N}^*G_NP_{\lambda,N}J_{K,N})\ge0.
\]
These positive observed weights sum to \(\Delta-\vartheta_N^\Gamma\).
Hence \(P_k^{\rm obs}\) is the probability distribution of the actual weighted positive exponents convolved with the same Gumbel law, with every repeated-energy projector retained.

For \(\alpha_k>0\), form \(R_k^{\rm rem}\) from the complementary nonnegative kernel projector weights, normalized by \(q\Delta\alpha_k\), and the same convolution. Then exactly
\[
 F_k=(1-\alpha_k)P_k^{\rm obs}+\alpha_kR_k^{\rm rem},
 \quad M_k=\alpha_k+(1-\alpha_k)P_k^{\rm obs},
 \quad D_k^{\rm ang}=\alpha_k(1-R_k^{\rm rem}).
 \tag{PH37}
\]
In particular \(\sup|P_k^{\rm obs}-F_k|\le\alpha_k\).
If \(\alpha_k=0\), the primary, full and observed probability functions coincide and no removed distribution is required.

A stronger global transport estimate follows from an explicit coupling.
Let \(U\) be uniform on \([0,1]\), take \(j=\lfloor qU\rfloor\), and choose a positive energy index uniformly at that cutoff.
Since \(\eta\) decreases, the mean absolute distance between its grid centre and \(\eta(U)\) is
\[
 R_q^\eta=\frac1q\sum_{j=0}^{q-1}\eta(j/q)-\int_0^1\eta(t)\,dt
 \in[0,\mathfrak J(1)/q].
\]
The actual energy adds at most \(\delta_k\) to this displacement; the independent Gumbel adds mean absolute displacement \(C_{\rm Gu}/q\).
Thus, for \(W_1\) defined as the infimum of mean absolute displacement over all couplings,
\[
 W_1(dF_k,d\mathcal H)
 \le\delta_k+R_q^\eta+C_{\rm Gu}/q
 \le\delta_k+\frac{\mathfrak J(1)+C_{\rm Gu}}q .
 \tag{PH38}
\]
For any two coupled variables, the integral of the absolute difference of their half-line indicators is their absolute distance. Tonelli therefore bounds the global integral of the difference of their distribution functions by the same right-hand side. No pointwise density convergence is needed.

All unsmoothed exponents lie in
\([\eta(1)-\delta_k,\eta(0)+\delta_k]\), of length
\(\mathfrak J(1)+2\delta_k\).
In the observed/removed decomposition, couple the common observed mass identically and the remaining mass inside this interval. Its cost is at most
\(\alpha_k[\mathfrak J(1)+2\delta_k]\).
Convolution with a common Gumbel variable preserves that bound, so
\[
 W_1(dP_k^{\rm obs},d\mathcal H)
 \le\delta_k+R_q^\eta+C_{\rm Gu}/q+
 \alpha_k[\mathfrak J(1)+2\delta_k].
 \tag{PH39}
\]
The primary \(M_k\) has left limit \(\alpha_k\); when \(\alpha_k>0\) its global \(L^1\) distance from \(\mathcal H\) is infinite.
PH36–39 specify the exact probability space and affine map that remove this defect while PH27–35 preserve the original observable.

The physical heat smoothing bias is exact:
\[
 \int_{\mathbb R}\xi\,dF_k(\xi)
 =\frac1{q\Delta}\sum_{j,a}u_{a,j}+\frac{\gamma_{\rm E}}q .
 \tag{PH40}
\]
This follows from \(\mathbb EG_{\rm Gu}=\gamma_{\rm E}\). The analogous identity uses the actual observed positive weights for \(P_k^{\rm obs}\).
The declared physical heat time has not been shifted to absorb this correction.

Inside the limiting transition interval,
\[
 \mathcal H'(\xi)=\frac1{f(t_\xi)},\qquad
 t_\xi=\mathfrak J^{-1}(\eta(0)-\xi);
 \tag{PH41}
\]
outside it the density is zero.
The endpoints have no atoms because their inverse images under the continuous strictly decreasing \(\eta\) have Lebesgue measure zero.
The finite heat densities are nonnegative mixtures of
\(q e^{-q(\xi-u)}\exp[-e^{-q(\xi-u)}]\).
PH38–39 prove convergence of their measures and bounded Lipschitz tests.
They do not assert pointwise or strong convergence of density derivatives, which is not implied by a grid spacing and a smoothing width both of order \(1/q\).

## 7. Scope and exact verification

CP37–51 and the supplied additional heat assertions are valid with their stated finite errors. PH9 supplies a finite full-image guard and retains both absolute source factors \(\ell_k,u_k\); only their ratio cancels in cutoff comparisons. PH34 sharpens the heat error, PH28 retains its exact original angle defect, and PH36–40 give the associated probability and transport maps.

The complete coefficient, quotient and image comparisons used are [CK3, CK5 and CK9–11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/1447462732b40b1474bd9a819cf79257f5326ada/workbenches/splitzero-tandem/continuations/20260922-kernel-frequency/COMBINED_KERNEL_AND_RECEIVERS.md#L30), read at lines23–145 of the published source. The companion power derivation owns CP9/27/33. Original-metric Schur identities are also proved in [021 MR1–29](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md) and rederived where used here. No positive heat expression is identified with the separate current \(i(Q_{B,N}M_{B,N}-M_{B,N}^*Q_{B,N})\) or with its marked-class sign.

The human formula sources retained in PH11 and PH29 are R. A. Askey and R. Roy,
[Gamma product, DLMF 5.8.3](https://dlmf.nist.gov/5.8.E3), and
T. H. Koornwinder, R. Wong, R. Koekoek, R. F. Swarttouw and W. P. Reinhardt,
[Legendre generating function, 18.12.11](https://dlmf.nist.gov/18.12.E11),
[Meixner–Pollaczek recurrence, 18.22.8](https://dlmf.nist.gov/18.22.E8) and
[generating function, 18.23.7](https://dlmf.nist.gov/18.23.E7).
The original formula TeX files were read in full. J. L. W. V. Jensen's zero-count formula is credited in the retained AS proof; its finite disk use is proved there, and no new reading of Jensen's historical article is claimed here.
The exponential-to-Gumbel probability change and every smoothing and transport bound used in PH30–41 are derived directly above. Naming the classical Gumbel distribution does not claim that the distribution itself is new.

The standalone checker is check_phase_heat.py. Its exact rational and complex-algebraic fixtures verify the full polynomial map, every tested relation column, full metric sections, conductor compression, zero-energy factors, scalar derivative identities, heat defects, probability map, tail constants and finite cutoff couplings. These auxiliary checks do not substitute chosen fixture values for the original period data.
