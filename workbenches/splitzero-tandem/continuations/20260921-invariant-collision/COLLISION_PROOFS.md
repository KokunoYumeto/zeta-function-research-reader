# The actual pivot-interior collision and its complete metric cost

Independent derivation, 21 September 2026. The complete received collision continuation is the original attachment fe30e0e3-c194-4524-8337-d207aee17fc4. This proof treats its equations (1)–(27); the full-row covariance execution (28)–(36) is treated by the accompanying derivation. Its claim about the long polynomial word is proved below from full quadratic-form estimates, with a direct repair of its source-comparison step. A complex translation of the inner grid is not treated as a real translation of its integration variable.

The original data are fixed throughout: the simple quartet, the original divisor \(h\), and the entire original period and amplitude matrix \(\mathsf H=F^{-1}\Pi U\mathcal E_{\rm prim}\) on the five-orbit period locus of OCF1. This includes the admitted original logarithm branches; no coefficient is made generic. Fix an actual pivot chart. Bounds depending on its nonzero pivot retain that dependence. All activation statements use the actual fixed added section and full tensor-value constraint of J1–J7, with every original cross Gram; no arbitrary positive added source is substituted.

## 1. Exact collision, full kernel, and physical coordinate

Let
\[
k\ge9,\quad k\equiv1\pmod4,\quad q=(k+1)^2,\quad
q'=(k-7)^2,\quad \Delta=16k-48,\quad m=8k-16,
\]
\[
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\quad
0<\delta<\tfrac12,\quad\gamma>2,\quad
Q_k(y)=\prod_{a,b=0}^k(y-\omega_{ab}),\quad
E_k=\mathbb C[y]/(Q_k),\quad M[f]=[yf].
\tag{IC1}
\]
The physical variable is \(S=k/2+iy\). Write the complete conductor biform as
\(A=\sum_{r,s=0}^{8}a_{rs}e_{rs}^{(8)}\), and let
\((r_*,s_*)\) be its largest nonzero lexicographic coefficient,
\(a_*=a_{r_*s_*}\ne0\). The actual pivot sets and factors are
\[
\mathcal I=\{(r_*+a,s_*+b):0\le a,b\le k-8\},\quad
\partial=\{0,\ldots,k\}^2\setminus\mathcal I,
\]
\[
D(y)=\prod_{\mathcal I}(y-\omega_{ab}),\quad
O(y)=\prod_{\partial}(y-\omega_{ab}),\quad Q_k=DO.
\tag{IC2}
\]
Every root is distinct, because its real and imaginary parts determine its two indices. The factors have degrees \(q'\) and \(\Delta\). The translated-grid identity is exactly
\[
D(y)=Q_{k-8}(y-z_*),\qquad
z_*=(2s_*-8)\gamma-i(2r_*-8)\delta.
\]
It need not preserve the real integration axis. The physical monic word is
\(D^S(S)=i^{q'}D((S-k/2)/i)\), and with the original physical multiplication operator \(\mathscr A_k=kI/2+iM\),
\[
D(M)=i^{-q'}D^S(\mathscr A_k).
\tag{IC3}
\]

Let \(\mathsf V:E_k\to\mathbb C^{q}\) be the original value isomorphism in the stated root order. Let \(M_A\) be the complete biform multiplication matrix. Its transpose is the conductor observation on values. Split its columns into interior and boundary positions:
\[
C_A=M_A^{\mathsf T}=[T\ U],\qquad F=-T^{-1}U.
\]
The pivot proof is literal: the largest coefficient of
\(Ae_{ij}^{(k-8)}\) is \(a_*e_{r_*+i,s_*+j}^{(k)}\), and every other position is earlier in the same additive lexicographic order. Thus \(T\) is triangular with diagonal \(a_*\), and
\[
\det T=a_*^{q'},\qquad
\ker C_A=\left\{\binom{Fb}{b}:b\in\mathbb C^\Delta\right\}.
\tag{IC4}
\]
This is complex-linear transpose, without conjugation. The exact dual-coordinate identification is [OCF23–24](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/ORIGINAL_CONDUCTOR_STRIP_FRAME.tex).

The conductor inclusion in the full invariant image gives \(K=\ker\Lambda\subset\ker C_A\). For any fixed original frame \(I_K:\mathbb C^m\to E_k\), set \(J_\partial=\operatorname{pr}_\partial\mathsf V I_K\). Then
\[
\mathsf V I_K=\binom F{I_\Delta}J_\partial,\qquad
\operatorname{rank}J_\partial=m.
\tag{IC5}
\]
Indeed \(J_\partial c=0\) forces both blocks of \(\mathsf V I_Kc\) to vanish.

For completeness the elimination costs at a fixed period have linear path length. Every nonpivot coefficient step decreases the integer \(9a+b\) by at least one: either its first-index decrement is at least one and its second-index increment is at most eight, or its first index is unchanged and its second decreases. On the entire square that integer has range \(10k\). If \(A_1=\sum|a_{rs}|\), induction on this height bounds the total absolute mass of every elimination tree by \((A_1/|a_*|)^{10k}\). Hence the strip elimination has norm at most
\[
\sqrt q(A_1/|a_*|)^{10k},\qquad
\log^+\|F\|=O_\varpi(k+\log q).
\tag{IC6}
\]
No estimate of a growing list of pivot minors is needed.

At the collision,
\[
V_D=\ker D(M)=O\mathcal P_{<q'},\qquad K\cap V_D=0.
\tag{IC7}
\]
The first statement follows either from root values or from the coprime factors \(D,O\); the second follows from IC5, since \(V_D\) has zero boundary values.

For every polynomial \(p\),
\[
\operatorname{rem}_{Q_k}(Dp)=D\operatorname{rem}_O p,\qquad
\pi_D:=\operatorname{quo}_D\operatorname{rem}_{Q_k}(D\,\cdot)
=\operatorname{rem}_O.
\tag{IC8}
\]
Both sides of the first identity have degree below \(q\) and differ from \(Dp\) by a multiple of \(DO\). Its kernel is precisely \(V_D\). The polynomial frame
\(y^{\Delta+j}-\operatorname{rem}_O y^{\Delta+j}\), \(0\le j<q'\),
equals \(O\) times monic polynomials of respective degrees \(j\). It is a triangular change with diagonal one from \(O,yO,\ldots,y^{q'-1}O\). Thus the continued subspace has rank \(q'\) even though the rational inverse of \(D(M)\) is unavailable.

Use the complete original strip invariant columns \(Z\), of rank
\(j=8k-32=\Delta-m\), as constructed in OCF12–22. The columns
\([M_A,S_\partial Z]\) are an actual basis of the full invariant image. Their transpose gives an output-coordinate isomorphism of the original observation:
\[
\widetilde\Lambda\binom{x_\mathcal I}{x_\partial}
=\binom{Tx_\mathcal I+Ux_\partial}{Z^{\mathsf T}x_\partial}.
\tag{IC9}
\]
The output metric is transported by that same fixed isomorphism. This changes no kernel or attained minimum. The quotient observation is \(b\mapsto Z^{\mathsf T}b\), and \(\ker Z^{\mathsf T}=\operatorname{im}J_\partial\).

The maps
\[
q_E(x_\mathcal I,x_\partial)=x_\partial,\quad q_B(c,\eta)=\eta,\quad
j_Eb=(Fb,b),\quad j_B\eta=(0,\eta),\quad h(c,\eta)=(T^{-1}c,0)
\]
satisfy \(q_Ej_E=I\), \(q_Bj_B=I\), and
\[
I-j_Eq_E=h\widetilde\Lambda,\quad
I-j_Bq_B=\widetilde\Lambda h,\quad
\widetilde\Lambda j_E=j_BZ^{\mathsf T}.
\tag{IC10}
\]
These are direct block multiplications; in particular they do not assert that \(j_E\) minimizes a metric. Writing
\(M_\partial=\operatorname{diag}(\omega_\partial)\) gives
\[
q_EM=M_\partial q_E,\qquad
Mj_E-j_EM_\partial
=\binom{\operatorname{diag}(\omega_\mathcal I)F-F\operatorname{diag}(\omega_\partial)}0 .
\tag{IC11}
\]
The defect lies in the removed interior space. Invariance of the reduced kernel is not needed or asserted.

## 2. The entire boundary metric has logarithmic width \(o(q)\)

Put \(R_k=k\sqrt{\delta^2+\gamma^2}\), \(M_\sigma=\sqrt{2\pi}\), and retain the source
\[
d\sigma(y)=|\Gamma(1/4+iy/2)|^2\,dy/(2\pi).
\]
The actual native source comparison on all degrees through \(2q\) is
\(\ell_k\|p\|_\sigma^2\le\|p\|_{\mu_k}^2\le u_k\|p\|_\sigma^2\),
with \(\ell_k=\ell_{k,2q}\). The unchanged constants have
\(|\log \ell_k|+|\log u_k|=O_h(k+\log q)\), by [HAR40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L440). This uses the constant-polynomial test together with their exact ratio, retaining the original source mass.

The generating function and recurrence below retain their classical source: T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, with W. P. Reinhardt, [DLMF18.23.E7 original TeX](https://dlmf.nist.gov/18.23.E7.tex) and [DLMF18.22.E8 original TeX](https://dlmf.nist.gov/18.22.E8.tex). The Gamma identities and envelopes retain R. A. Askey and R. Roy's [DLMF5.8.E3 original TeX](https://dlmf.nist.gov/5.8.E3.tex), together with the full Euler/reflection proof in OSP9–13. These original equation files were read directly; all source masses and coordinate factors in their present application remain displayed.

Here is a full proof of the received boundary evaluation constant. The original Meixner–Pollaczek generating function is
\[
(1+t^2)^{-1/4}e^{z\arctan t}=\sum_{n\ge0}c_n(z)t^n,
\]
where \(c_n(z)=p_n^{\rm monic}(z)/n!\), and the orthonormal polynomial is \(\rho_nc_n/\sqrt{M_\sigma}\), with squared coefficient multiplier
\(\rho_n^2=n!/(1/2)_n\le2n+1\). On \(|t|=N/(N+1)\), \(N\ge1\),
\[
|\arctan t|\le\operatorname{arctanh}|t|=\tfrac12\log(2N+1),\quad
|1+t^2|^{-1/4}\le(N+1)^{1/2}(2N+1)^{-1/4}.
\]
Cauchy's coefficient estimate and \((1+1/N)^N\le e\), followed by summation of the \(N+1\) squared orthonormal polynomials, give
\[
K_{\sigma,N}(z,z)
\le\frac{e^2}{M_\sigma}(N+1)^2(2N+1)^{R_k+1/2}
\le\frac{e^2}{M_\sigma}(N+1)^{3/2}(2N+1)^{R_k+1}.
\]
The last inequality is \(N+1\le2N+1\); \(N=0\) is immediate. The operator norm of the whole boundary evaluation covariance is at most its trace, so
\[
A_N^\partial=\frac{\Delta e^2}{M_\sigma}
(N+1)^{3/2}(2N+1)^{R_k+1}
\tag{IC12}
\]
is valid as received. No factor exponential in the real part of a root is missing: the absolute \(\operatorname{arctanh}\) estimate controls the complete complex exponent.

For the upper metric bound use every boundary Lagrange polynomial. Distinct roots have separation at least \(2\delta\). The original Gamma recurrence proves
\(\|(y-z)p\|_\sigma\le[2(L+1)+|z|]\|p\|_\sigma\) for \(\deg p\le L\).
Starting from the unchanged constant mass and multiplying all \(\Delta-1\) factors gives
\[
B_k^\partial=\Delta M_\sigma
\left(\frac{2\Delta+R_k}{2\delta}\right)^{2(\Delta-1)}.
\tag{IC13}
\]
Indeed each Lagrange polynomial has squared norm at most the displayed expression divided by \(\Delta\), and Cauchy–Schwarz bounds the norm of their linear combination. The degree is \(\Delta-1\le q-1\), so this is a permitted lift at every cutoff. Consequently
\[
(A_{2q}^\partial)^{-1}I\preceq G_N^{\partial,\sigma}\preceq B_k^\partial I.
\]

Retain the actual J1–J7 joint-source constants
\[
\mathbf L_k^{-1}T_k\preceq G_N^J\preceq\mathbf B_k T_k,\qquad
T_k=\operatorname{diag}(W_\omega),\qquad
a_{\min}^k\le W_\omega\le A_w^k.
\]
Their fixed section, full tensor constraint and degree \(n_*=\max(2q,2\deg h-1)\) remain as in [MF1–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/cb9705da84d6f8689611914ed9659298e620ba0a/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/ACTIVATED_RATIONAL_PROOFS.md). The attained quotient of the diagonal form onto boundary values is exactly its boundary diagonal block. Set
\[
b_-=\min\{\ell_k/A_{2q}^\partial,\ a_{\min}^k/\mathbf L_k\},\quad
b_+=\max\{u_kB_k^\partial,\ \mathbf B_kA_w^k\},\quad
\kappa_\partial=b_+/b_-.
\]
For the actual covariance interpolation
\(G_N(\alpha)^{-1}=(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1}\), the boundary covariance is the same convex combination of boundary covariances. Inversion therefore proves
\[
b_-I\preceq G_N^\partial(\alpha)\preceq b_+I,\quad
0\le\alpha\le1,\quad q-1\le N\le2q,
\tag{IC14}
\]
\[
E_\partial:=\max(0,-\log b_-,\log b_+)
=O_{h,\varpi}(k\log^2(q+2)),\quad
\log\kappa_\partial\le2E_\partial.
\tag{IC15}
\]
The estimates on \(A^\partial,B^\partial\) contribute \(O_h(k\log q)\). Individual source constants are retained, not only their ratio.

For any fixed injective \(J:\mathbb C^t\to\mathbb C^\Delta\), congruence gives
\(b_-J^*J\preceq J^*G_N^\partial(\alpha)J\preceq b_+J^*J\).
The source spaces increase with \(N\), including the same actual added section, so these metrics decrease at fixed \(\alpha\). With the original signs
\(\mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q}\),
\[
0\le\mathcal R\log\det(J^*G_N^\partial(\alpha)J)
\le2t\log\kappa_\partial.
\tag{IC16}
\]
The complete determinant of \(J^*J\) cancels. In particular \(J=J_\partial\) gives the received \(O(k^2\log^2q)=o(kq)\) boundary-kernel return. For any arithmetic polynomial word \(P_k(M_\partial)\) injective on the frame, the same proof applies to its complete fixed image frame without a degree-dependent multiplication estimate.

## 3. The actual long word and its scalar-source quotient

Let \(\mathsf V_O\) be the boundary Vandermonde on degree-below-\(\Delta\) polynomials, and put \(P_K=\mathsf V_O^{-1}J_\partial\). Then exactly
\[
D(M)I_K=[DP_K].
\tag{IC17}
\]
Both sides vanish on the interior and have the same values \(D(\omega)J_\partial\) on the boundary. The actual representative of this class at cutoff \(N\) has the form
\(D(p+Oh)\), with \(\deg(p+Oh)\le N-q'\). Indeed every representative vanishes at the \(q'\) roots of \(D\), hence is divisible by \(D\), and its remaining quotient differs from \(p\) by a multiple of \(O\). Thus the exact word-image metric is
\[
H_{\rm word,N}=P_K^*\mathfrak G_N^{D,O}P_K,\quad
\mathfrak G_N^{D,O}[p]=
\min_{\deg(p+Oh)\le N-q'}\int|D(y)|^2|p(y)+O(y)h(y)|^2\,d\mu_k(y).
\tag{IC18}
\]
The four source degrees are \(\Delta-1,\Delta,q+\Delta-1,q+\Delta\). Multiplication by \(D\) returns them to exactly \(N\); it never enlarges the permitted original source.

The all-direction estimate used below is derived from the actual argument of [DCR9–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/CONDUCTOR_DIVISOR_COVARIANCE_RETURN.tex#L139) and [OOQ1–40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/09_INPUT_CUMULATIVE_PROOFS.tex#L23179). DCR's final full-volume conclusion alone would not suffice. Two changes are made explicitly: the weight uses every actual root of \(D\), without a false pairing premise; and the contour uses the actual \(O(k)\) root radius, improving the error.

### 3.1 Full-form comparison for an unpaired original factor

Write \(Q=q'\), \(d=\Delta\), \(R=R_k\), \(\epsilon_0=2^{-32}\), \(T_0=\epsilon_0q\). Impose the finite guards
\[
k\ge29,\qquad R\le T_0/2.
\tag{IC19}
\]
They imply \(Q\ge q/2\), \(T_0\le q/2\), and hold eventually for each fixed original quartet.

For \(|y|\ge T_0\), retain each root separately:
\[
\left|\log\frac{|D(y)|^2}{|y|^{2Q}}\right|
\le 2Q[-\log(1-R/T_0)]
\le \eta_D:=\frac{2QR}{T_0-R}.
\tag{IC20}
\]
For all real \(y\), \(|D(y)|\le(|y|+R)^Q\). Let
\(A_B=\int_q^{2q}|y|^{2Q}|p(y)|^2d\sigma(y)\).
The original Gamma lower envelope is \(d\sigma/dy\ge C_Le^{-\pi|y|}\),
\(C_L=\pi/\Gamma(3/4)^2\). OSP15's complete Legendre argument gives, for \(\deg p\le L\),
\[
\sup_{|y|\le T_0}|p(y)|^2
\le (L+1)^2\,10^{2L}q^{-1}\int_q^{2q}|p|^2.
\]
Combining these facts with the full mass \(M_\sigma\) bounds each inner integral, with \(|D|^2\) or \(|y|^{2Q}\), by \(\kappa_D A_B\), where
\[
\kappa_D=
\frac{M_\sigma}{C_L}\frac{(L+1)^2}{q}
e^{2\pi q}10^{2L}\left(\frac{T_0+R}{q}\right)^{2Q}.
\tag{IC21}
\]
For \(L\le2q\), IC19 implies
\[
\kappa_D\le K_q:=
\frac{M_\sigma}{C_L}\frac{(2q+1)^2}{q}e^{-2q}.
\]
To verify the exponent, its coefficient is at most
\(2\pi+4\log10+\log(3\epsilon_0/2)<-2\).
The elementary bounds \(\pi<4,\log10<4\log2,\log(3/2)<1/2,\log2>2/3\) already give this strict inequality.

Outside the inner interval the two integrals compare by \(e^{\pm\eta_D}\), and \(A_B\) belongs to that outside interval. Adding the complete inner integrals proves
\[
e^{-E_D}\int |y|^{2Q}|p|^2d\sigma
\le\int |D|^2|p|^2d\sigma
\le e^{E_D}\int |y|^{2Q}|p|^2d\sigma,\quad
E_D=\eta_D+\log(1+K_q)=O_h(k).
\tag{IC22}
\]
This proof never assumes that \(D\) has paired roots. It repairs the source step for every actual pivot, including a nonreal \(z_*\). The product \(Dp\) still has its exact original coefficients.

The native comparison is applied to \(Dp\), whose degree is \(N\le2q\). The full Gamma-to-exponential comparison, with \(\vartheta=\pi/2\), \(h_q=1/q\), is
\[
L_{h_q}e^{-(\vartheta+h_q)|y|}
\le d\sigma/dy\le U_{h_q}e^{-(\vartheta-h_q)|y|},
\]
\[
L_{h_q}=C_L(\sin h_q)^{3/2},\qquad
U_{h_q}=\frac{\Gamma(1/4)^2}{2\pi}(\sin h_q)^{-1/2}.
\tag{IC23}
\]
These are the unchanged OOQ30 constants. Thus every complete fibre in IC18 is bounded between the corresponding two exponential-source fibres with multipliers \(\ell_k L_{h_q}e^{-E_D}\) and \(u_kU_{h_q}e^{E_D}\).

### 3.2 Full all-direction exponential quotient bounds

Use exactly OOQ3–6's equilibrium for
\(V_{\alpha,\beta}(x)=\beta\sqrt x-\alpha\log x\) on the rectangle
\(\mathcal K=[3/2,5/2]\times[\pi/4,\pi]\).
Its potential is \(P\), Euler constant \(\ell_{\rm eq}\), excess
\(D_{\rm eq}=V-2P-\ell_{\rm eq}\ge0\), and
\(W=P(0)+\ell_{\rm eq}/2\). To specify the constants:
\(a_{\rm eq}\) is the minimum left endpoint, \(B_{\rm eq}\) the maximum right endpoint,
\(b_{\rm eq}\) the minimum support length, \(M_{\rm eq}\) the maximum density, and
\(L_{\rm eq}\) the maximum \(|V'|\) on these supports. Put
\[
C_{\rm BM}=\sqrt{32}e^{3L_{\rm eq}/4},\quad
C_{\rm quant}=B_{\rm eq}+2M_{\rm eq},\quad C_0=B_{\rm eq}/a_{\rm eq},
\]
\[
C_{\rm tail}=\max(0,\sup_{\mathcal K,x>0}[\log(1+\sqrt x)-D_{\rm eq}(x)]),\quad
T_{\rm eq}=\max(1,\sup_\mathcal K\int_0^\infty e^{-D_{\rm eq}}dx),
\]
\[
C_W=1+\max_\mathcal K|W|+
(4+\pi)\max_\mathcal K(|W_\alpha|+|W_\beta|).
\]
Their finiteness and original equilibrium identities are proved in the cited complete OOQ section; the accepted EIQ source status is retained.

Take \(n=q/2\), and now choose the sharper actual-root contour
\[
r=R/n,\qquad \rho=2R/n,\qquad
C_{\rm rem}=\rho d(1+r)^d(2/\rho)^d.
\]
Retain these finite guards in addition to IC19:
\[
n\ge2d+1,\quad n\ge2/b_{\rm eq},\quad
\rho\le\min(1/2,\sqrt{a_{\rm eq}/2}),
\tag{IC24}
\]
and, for \(\beta_\pm=\vartheta\pm1/q\) and both \(L=q+d-1,q+d\), require
\[
((Q-\tfrac12)/n,\beta_\pm),\quad
((Q-\tfrac12)/m_e,n\beta_\pm/m_e),\quad
((Q+\tfrac12)/m_o,n\beta_\pm/m_o)\in\mathcal K,
\]
where \(m_e=\lfloor L/2\rfloor\), \(m_o=\lfloor(L-1)/2\rfloor\).
These are computable inequalities on the original data and hold eventually; \(m_e,m_o\ge n\) and \(d=O(k)\).

For \(\widehat O(z)=n^{-d}O(nz)\) the exact Cauchy remainder is
\[
\mathcal R_OF(z)=\frac1{2\pi i}\int_{|\zeta|=\rho}
F(\zeta)\frac{\widehat O(\zeta)-\widehat O(z)}
{(\zeta-z)\widehat O(\zeta)}\,d\zeta,\qquad
\|\mathcal R_OF\|_1\le C_{\rm rem}\sup_{|\zeta|=\rho}|F|.
\tag{IC25}
\]
The denominator is at least \((\rho/2)^d\); the divided difference has coefficient sum at most \(d(1+r)^d\); and the contour contributes \(\rho\). Cauchy's formula proves matching values at every root, hence the exact remainder. All integrands used below are holomorphic on a neighbourhood of the closed disk.

Put
\[
c_H(Q,\beta)=(2Q+1)\log n-2nW((Q-\tfrac12)/n,\beta).
\]
The original parity decomposition \(f(nz)=f_e(z^2)+zf_o(z^2)\) gives exactly
\[
\|f\|_{\exp}^2=n^{2Q+1}\left[
\int_0^\infty|f_e|^2x^{Q-1/2}e^{-n\beta\sqrt x}dx+
\int_0^\infty|f_o|^2x^{Q+1/2}e^{-n\beta\sqrt x}dx\right].
\]
OOQ7–8 bounds each polynomial at \(\zeta^2\) by its full norm times
\(C_{\rm BM}m^2e^{mW+2m\rho^2/a_{\rm eq}}\).
The same-rectangle mean-value estimate is
\(|mW-nW((Q-\tfrac12)/n,\beta)|\le C_W(d+2)\).
Applying IC25 therefore bounds every lift of the scaled remainder \(t\) by
\[
\|t\|_2\le C_{\rm rem}\sqrt2 C_{\rm BM}(n+d)^2
e^{nW+C_W(d+2)+2(n+d)\rho^2/a_{\rm eq}}
n^{-(2Q+1)/2}\|f\|_{\exp}.
\tag{IC26}
\]

For the reverse inequality use the actual equilibrium quantile polynomial
\(r_n(x)=\prod_{i=1}^n(1-x/\xi_i)\), \(\xi_i\in[a_{\rm eq},B_{\rm eq}]\).
OOQ9–11 gives
\(\log|r_n(x)|\le n(P(x)-P(0))+C_{\rm quant}\sqrt n+C_0\)
and \(|r_n(z)|^{-1}\le e^{2n|z|/a_{\rm eq}}\).
The exact lift is
\[
a_t=\mathcal R_O(t/r_n(z^2)),\qquad
f_t(nz)=r_n(z^2)a_t(z).
\tag{IC27}
\]
Its degree is at most \(q+d-1\), and it has all prescribed values at the actual outer roots. IC25 gives
\(\|a_t\|_1\le C_{\rm rem}\sqrt d\,e^{2n\rho^2/a_{\rm eq}}\|t\|_2\).
On both real branches,
\(|a_t(\pm\sqrt x)|\le\|a_t\|_1(1+\sqrt x)^{d-1}\).
The Euler identity and
\(\log(1+\sqrt x)\le C_{\rm tail}+D_{\rm eq}(x)\)
leave the integrable factor \(e^{-[n-2(d-1)]D_{\rm eq}}\), bounded in integral by \(T_{\rm eq}\).
It follows that the high quotient metric in the original coefficient frame is within \(e^{\pm E_H}\) of \(e^{c_H}I\), where
\[
\begin{split}
E_H^-={}&2\log(C_{\rm rem}\sqrt2 C_{\rm BM}(n+d)^2)
+2C_W(d+2)+4(n+d)\rho^2/a_{\rm eq},\\
E_H^+={}&2\log C_{\rm rem}+\log d+4n\rho^2/a_{\rm eq}
+2C_{\rm quant}\sqrt n+2C_0+2C_{\rm tail}(d-1)+\log T_{\rm eq},\\
E_H={}&\max(0,E_H^-,E_H^+)+2(d-1)\log n.
\end{split}
\tag{IC28}
\]
The last term retains the exact coefficient scaling
\(\operatorname{diag}(1,n,\ldots,n^{d-1})\).

At low source degrees \(d-1,d\), put
\(c_L(Q,\beta)=2Q\log(2Q/\beta)-2Q\), \(y_0=2Q/\beta\).
The original shifted-Legendre argument on \([y_0,y_0+1]\) bounds the full degree-\(d\) Gram below by
\(e^{c_L-\beta}/[(d+1)^2(2d+1)64^d(1+y_0)^{2d}]\).
Its upper bound is its exact trace \(\sum_{j=0}^d2(2Q+2j)!/\beta^{2Q+2j+1}\).
At degree \(d\) the remainder map is \([I,-o]\) with squared norm at most \((d+1)(1+R)^{2d}\), retaining the entire extra ideal column. Hence both low quotient metrics are within \(e^{\pm E_L}\) of \(e^{c_L}I\), where
\[
\begin{split}
E_L(Q,\beta)=\max\{0,\;&
\log\sum_{j=0}^d2(2Q+2j)!/\beta^{2Q+2j+1}-c_L,\\
&\beta+3\log(d+1)+\log(2d+1)+d\log64\\
&\qquad+2d\log(1+y_0)+2d\log(1+R)\}.
\end{split}
\tag{IC29}
\]
Each minimum in these arguments is on the unchanged full remainder fibre.

### 3.3 The long-word coefficient and its error

The original scalar centres are
\[
c_{\rm lo}=2q\log(2q/\vartheta)-2q,\quad
c_{\rm hi}=2q\log(q/2)-qW(2,\vartheta),\quad
c_{\rm lo}-c_{\rm hi}=qC_\partial/2.
\tag{IC30}
\]
The last equality is the exact OOQ36 energy identity, not a new approximation.

An explicit sufficient common error is
\[
\begin{split}
\varepsilon_k={}&E_D+\max(|\log\ell_k|,|\log u_k|)
+\max(|\log L_{h_q}|,|\log U_{h_q}|)\\
&+\max_{\beta=\beta_\pm}\{E_L(Q,\beta)+E_H(Q,\beta)
+|c_L(Q,\beta)-c_{\rm lo}|+|c_H(Q,\beta)-c_{\rm hi}|\}.
\end{split}
\tag{IC31}
\]
The \(E_H\) maximum includes both high degrees. Taking identical minima in IC23 and IC26–29 proves
\[
e^{c_{\rm lo}-\varepsilon_k}I_\Delta\preceq
\mathfrak G_N^{D,O}\preceq e^{c_{\rm lo}+\varepsilon_k}I_\Delta
\quad(N=q-1,q),
\]
\[
e^{c_{\rm hi}-\varepsilon_k}I_\Delta\preceq
\mathfrak G_N^{D,O}\preceq e^{c_{\rm hi}+\varepsilon_k}I_\Delta
\quad(N=2q-1,2q).
\tag{IC32}
\]
These are full operator estimates. Since \(\rho=2R/n\),
\(n\rho^2=4R^2/n=O_h(1)\),
\(\log C_{\rm rem}=O_h(k\log q)\), and \(\sqrt n=O(k)\).
The factorial integral bounds and the fixed-rectangle derivative bounds give
\[
\varepsilon_k=O_h(k\log(q+2))=o(q).
\tag{IC33}
\]
This improves the \(q^{7/8}\) contour error used for the more distant DCR roots. It is specific to the literal pivot-interior and boundary factors here.

Congruence by the actual full-rank \(P_K\) gives scalar bounds relative to \(P_K^*P_K\). Its determinant cancels at the four cutoffs, regardless of its conditioning. Therefore
\[
\boxed{\left|\mathcal R\log\det H_{\rm word,N}
-mC_\partial q\right|\le4m\varepsilon_k
=O_h(k^2\log(q+2))=o(kq).}
\tag{IC34}
\]
Every relative eigenvalue between a corresponding low and high word-image metric has logarithm within \(2\varepsilon_k\) of \(qC_\partial/2\). Thus the long-word claim is valid, with an explicit repaired all-direction proof. It does not assign the same value to the original unmultiplied kernel.

For weak critical activation with fixed margin \(\zeta\ge\beta_L+\epsilon\), the full source inequality
\[
G_N(0)/(1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N)
\preceq G_N(\alpha)\preceq G_N(0)
\]
from HAR/MF applies to every actual word-image vector. Here
\(\log(\mathbf L_k\Gamma_N)=o(q)\),
\(\log\mathsf S_N\le2q\log(q/k)+\beta_Lq+o(q)\).
For \(\alpha=e^{-2q\log(q/k)-\zeta q}\), each logarithmic determinant changes by at most
\(m\log(1-\alpha+\alpha\mathbf L_k\Gamma_N\mathsf S_N)=me^{-\epsilon q+o(q)}\).
Thus IC34 survives this entire weak-activation range. General activation is not identified with the scalar divisibility source IC18.

## 4. Exact graph remainder and its complete variation

In the original ordered root coordinates write the full actual metric, at any activation,
\[
\mathsf G_N(\alpha)=
\begin{pmatrix}G_{\mathcal I\mathcal I}&G_{\mathcal I\partial}\\
G_{\partial\mathcal I}&G_{\partial\partial}\end{pmatrix}.
\]
Its attained boundary metric is the full Schur complement
\(G_N^\partial=G_{\partial\partial}
-G_{\partial\mathcal I}G_{\mathcal I\mathcal I}^{-1}G_{\mathcal I\partial}\).
Define
\[
\widehat H_N=J_\partial^*G_N^\partial J_\partial,\quad
X_N=(F+G_{\mathcal I\mathcal I}^{-1}G_{\mathcal I\partial})J_\partial,\quad
\Xi_N=G_{\mathcal I\mathcal I}^{1/2}X_N\widehat H_N^{-1/2}.
\]
Completing the exact quadratic square gives
\[
H_{K,N}=\widehat H_N+X_N^*G_{\mathcal I\mathcal I}X_N,\quad
\delta_N^\partial:=\log\det H_{K,N}-\log\det\widehat H_N
=\log\det(I_m+\Xi_N^*\Xi_N)\ge0.
\tag{IC35}
\]
All cross terms and all \(m\) eigenvalues remain. At fixed activation IC16 proves
\[
0\le\mathcal R\log\det H_{K,N}-\mathcal R\delta_N^\partial
\le2m\log\kappa_\partial.
\tag{IC36}
\]
Let \(b_N=\log\det\widehat H_{q-1}-\log\det\widehat H_N\).
Both original and boundary metrics decrease with \(N\), so
\(0\le b_N\le m\log\kappa_\partial\), \(b_N\) increases, and
\(\delta_N^\partial-b_N=\log\det H_{K,N}-\log\det\widehat H_{q-1}\) decreases.
Consequently each positive increment of \(\delta^\partial\) is at most the corresponding increment of \(b\), and summing yields
\[
\sum_{N=q-1}^{2q-1}(\delta_{N+1}^\partial-\delta_N^\partial)_+
\le m\log\kappa_\partial=o(kq).
\tag{IC37}
\]
This is a whole-window bound, uniform in physical activation.

At the canonical source, combine IC34 and IC36 without deleting the graph metric:
\[
\left|\mathcal R\log\frac{\det H_{\rm word,N}}{\det H_{K,N}}
-\left(mC_\partial q-\mathcal R\delta_N^\partial\right)\right|
\le4m\varepsilon_k+2m\log\kappa_\partial=o(kq).
\tag{IC38}
\]
The same statement with an exponentially small additional error holds in the weak-activation range just proved. The graph term is the exact remaining original-kernel coefficient, up to the fully bounded boundary return. Its value is not inferred from the long word.

## 5. The evaluated inverse-power loss and reduced heat

For \(1\le r\le\Delta\), retain the original inverse-power map
\(U_rc=\sum_{j=1}^r c_j[y^{-j}]\), available because all \(q\) roots are nonzero.
Its boundary evaluation matrix is
\[
V_{\partial,r}=(\omega^{-j})_{\omega\in\partial,\ 1\le j\le r}.
\]
Any \(r\) selected distinct reciprocal nodes give a Vandermonde matrix times a nonzero diagonal matrix. Hence its rank is \(r\), and
\(\operatorname{ran}U_r\cap V_D=0\).

Put \(\varrho=\min_{\partial}|\omega|\). Every original root has modulus at least \(\sqrt{\delta^2+\gamma^2}>2\). Every boundary pair has one index at most seven or at least \(k-7\), so for \(k>14\), \(\varrho\ge\delta(k-14)\).
Reciprocal-node separations are at least \(2\delta/R_k^2\).
For any selected \(r\) nodes, each complete Lagrange polynomial on these reciprocal nodes has coefficient sum at most
\[
\mathcal T_k^{r-1},\qquad
\mathcal T_k=\max\left(1,\frac{R_k^2(1+\varrho^{-1})}{2\delta}\right).
\]
The inverse Vandermonde Frobenius norm is at most \(\sqrt r\,\mathcal T_k^{r-1}\), and the remaining diagonal inverse has norm at most \(R_k\). The whole matrix therefore satisfies
\[
v_-I_r\preceq V_{\partial,r}^*V_{\partial,r}\preceq v_+I_r,\quad
v_-=\frac1{rR_k^2\mathcal T_k^{2(r-1)}},\quad
v_+=\frac{\Delta}{\varrho^2-1}.
\tag{IC39}
\]
The upper bound is the exact convergent geometric bound on its squared Frobenius norm. All roots and inverse-power signs are retained.

For the full source inverse-power metric use the proved HAR harmonic comparison, with its original finite degree/radius/absorption domain, equivalently [MF4–10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/cb9705da84d6f8689611914ed9659298e620ba0a/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/ACTIVATED_RATIONAL_PROOFS.md):
\[
e^{-E_{r,N}}h_N(\alpha)I_r\preceq
H^E_{r,N}(\alpha)\preceq e^{E_{r,N}}h_N(\alpha)I_r,\qquad
h_N(\alpha)=\frac{\mathsf S_N}{1-\alpha+\alpha\mathsf S_N}.
\]
Explicitly this use retains \(q_-=(k-7)^2\ge16\),
\(R_k\le2^{-14}q_-\), the reciprocal-kernel radius guard,
\(Jr-v\le q_-\), \(n_-+2\le2q_-\), \(n_-=N-v+Jr-q_-\), and the original positive absorption inequality in RF37/MF5. The denominator is \(y^r\), so the compact pole set is \(\{0\}\), off the odd lattice. All hold eventually for \(r\le\Delta=O(k)\) at fixed original conductor and period. No claim at an excluded finite index is made by invoking an eventual statement.

IC14 and IC39 give
\(b_-v_-I_r\preceq V_{\partial,r}^*G_N^\partial(\alpha)V_{\partial,r}\preceq b_+v_+I_r\).
Define the complete finite error
\[
E_{r,N}^{\rm loss}
=rE_{r,N}+r\max\{|\log(b_-v_-)|,\ |\log(b_+v_+)|\}.
\]
The angle loss to the actual collision quotient is thus
\[
\boxed{\delta_{r,D,N}=
\log\det H^E_{r,N}(\alpha)
-\log\det[V_{\partial,r}^*G_N^\partial(\alpha)V_{\partial,r}]
=r\log h_N(\alpha)+e_{r,N},\quad |e_{r,N}|\le E_{r,N}^{\rm loss}.}
\tag{IC40}
\]
It is nonnegative, because quotient minima are at most original norms. Its error is
\(O_{h,\varpi}(rk\log^2(q+2)+r^2\log(q+2))=o(rq)\)
for the entire \(1\le r\le\Delta\).

The unchanged endpoint scalar is
\(\log\mathsf S_{L/H}=2q\log(q/k)+\beta_{L/H}q+e_{L/H}\),
\(\max|e_{L/H}|=o(q)\).
For every physical \(\zeta\ge-2\log(q/k)\), including moving \(\zeta\), put
\(\alpha_k(\zeta)=e^{-2q\log(q/k)-\zeta q}\), with \(\alpha=0\) represented by \(\zeta=+\infty\).
For \(\mathsf S\ge1\),
\[
\max(1,\alpha\mathsf S)\le1-\alpha+\alpha\mathsf S
\le2\max(1,\alpha\mathsf S).
\]
Consequently IC40 gives
\[
\boxed{\mathcal R\delta_{r,D,N}
=rqC_{\rm inv}(\zeta)+o(rq),\quad
C_{\rm inv}(\zeta)=
2[\min(\beta_L,\zeta)-\min(\beta_H,\zeta)].}
\tag{IC41}
\]
A finite error is
\(\sum_NE_{r,N}^{\rm loss}+4r\max|e_{L/H}|+4r\log2\),
uniform on the whole physical activation domain. The inherited high-endpoint profile/zero-law status remains exactly that of HAR41–49; the finite collision proof does not independently replace it.

Finally, for the actual reduced arithmetic operator in its actual attained boundary metric,
\[
\frac{\varrho^2}{\kappa_\partial}I
\preceq M_\partial^\dagger M_\partial
\preceq R_k^2\kappa_\partial I.
\tag{IC42}
\]
Indeed compare each Rayleigh quotient to its original Euclidean diagonal action using IC14. Its complete heat therefore obeys
\[
0\le\operatorname{Tr}e^{-\tau M_\partial^\dagger M_\partial}
\le\Delta\exp[-\tau\varrho^2/\kappa_\partial].
\]
At \(\tau=\exp(2q\log(q/k)+bq)\), with fixed \(b\), this tends to zero, uniformly over physical activation. The nonisometric collision retraction loses the ultrasmall original mode; IC40–41 quantifies that loss on the entire original inverse-power family.

## 6. Mechanism, verification and scope

The exact maps fit the following diagram. Vertical arrows use the original root-value coordinates; the lower metric is the attained minimum, and the graph term in IC35 measures the difference from the conductor-zero section.
\[
\begin{array}{ccccc}
\mathbb C^m&\xrightarrow{\ I_K\ }&E_k&\xrightarrow{\ D(M)\ }&D\mathcal P_{<\Delta}\\
\downarrow J_\partial&&\downarrow\pi_\partial&&\downarrow[D p]\mapsto[p]_O\\
\ker Z^{\mathsf T}&\longrightarrow&\mathbb C^\Delta&\xrightarrow{\ \mathsf V_O^{-1}\ }&\mathbb C[y]/(O).
\end{array}
\]
The right arrow has the weighted source \(|D|^2d\mu_k\) of IC18, while the middle lower space has the boundary minimum of the original source. IC32 controls every direction of the first metric; IC14 controls every direction of the second. Their different leading returns are compatible and are joined to the actual kernel by IC35–38.

The reproducible checker and source-use ledger accompany this proof. The executed receipt COLLISION_CHECKS.json records 767 exact checks and 52 numerical checks. Exact finite algebra tests retain the entire pivot-interior block, actual original-root coordinates, complete observation and graph cross terms. Separate finite numerical tests check the metric and scalar inequalities. They are not calculations of native xi moments or a replacement for the retained analytic source hypotheses.

The main received coefficient survives: the actual degree-\(q'\) word image has return \(mC_\partial q+o(kq)\). Its proof is IC19–34, with every source degree and the unpaired-root repair included. The reduced boundary kernel has return \(o(kq)\); the exact positive graph determinant carries the remaining original-kernel value. The full-row invariant covariance calculation is retained with the accompanying derivation.
