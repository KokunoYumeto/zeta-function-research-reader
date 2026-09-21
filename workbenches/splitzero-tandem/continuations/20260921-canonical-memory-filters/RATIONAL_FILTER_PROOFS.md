# Colliding rational filters in the complete original metric

21 September 2026. Independent derivation of received equations (10)–(32) and (50)–(58). The exact received source and its hash are retained in the source ledger. Every norm below uses the original source or its stated attained minimum. The full observed fibre, all conductor coefficients, and every filter multiplicity are retained.

The collision-uniform theorem is valid. This proof supplies explicit finite constants and guards for its contour, lower relation degree, numerator absorption, surjective remainder map, and separated singular cluster. The evaluated coefficient uses the established original monic profile and zero law at their stated scope; the finite inequalities do not require those asymptotic inputs. The exact checks accompanying this proof test algebra and matrix identities, not unknown native moments.

## 1. Objects, coordinates and source inputs

Fix the original simple-quartet and period domain, with
\[
0<\delta<\tfrac12,\quad \gamma>2,\quad k\ge9,\quad k\equiv1\pmod4,\quad
q=(k+1)^2,\quad S=k/2+iy,
\]
\[
Q=Q_k(y)=\prod_{a,b=0}^{k}[y-(2b-k)\gamma+i(2a-k)\delta],
\quad E=\mathbb C[y]/(Q),\quad M[f]=[yf].
\tag{RF1}
\]
Write \(D_0=\sqrt{\delta^2+\gamma^2}\), \(R_k=kD_0\). Keep
\(d\mu_k=w_h^{*k}(y)\,dy\) and
\[
d\sigma(y)=|\Gamma(1/4+iy/2)|^2\,dy/(2\pi),\qquad
M_\sigma=\sqrt{2\pi}.
\]
The source degree is \(q-1\le N\le2q\). Its quotient map and full minimum section are \(J_N:\mathcal P_N\to E\) and \(L_N:E\to\mathcal P_N\). The attained metric is \(G_N\), so \(J_N\) is contractive and \(L_N\) is an isometry. Original NG2 gives
\[
\ell_{k,N}\|f\|_\sigma^2\le\|f\|_{\mu_k}^2\le u_k\|f\|_\sigma^2,
\qquad \log(u_k/\ell_{k,N})=O_h(k+\log(N+1)).
\tag{RF2}
\]
The unchanged onto observation is \(\Lambda:E\to B\), with
\[
Q_{B,N}=(\Lambda G_N^{-1}\Lambda^*)^{-1},\quad
L_{B,N}=G_N^{-1}\Lambda^*Q_{B,N},\quad P_B=L_{B,N}\Lambda.
\tag{RF3}
\]
Thus \(P_B\) is the original orthogonal projection, with kernel \(K\), and
\[
\|P_Bx\|_{G_N}
=\inf_{\deg f\le N,\;\Lambda[f]=\Lambda x}\|f\|_{\mu_k}.
\tag{RF4}
\]

The finite inputs used below are the proved IVO3–12 and IVO21–23, from the
[pinned complete IVO proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INDEPENDENT_FINITE_OBSERVATION.tex).
They retain the original-author Meixner–Pollaczek generating function and recurrence of T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, with W. P. Reinhardt, [DLMF 18.23.7](https://dlmf.nist.gov/18.23.E7) and [18.22.8](https://dlmf.nist.gov/18.22.E8). R. A. Askey and R. Roy's [Gamma product 5.8.3](https://dlmf.nist.gov/5.8.E3) supplies the retained Gamma envelope. Their original TeX versions were retained and read in the IVO source work; the source-use ledger identifies the exact local providers reread here.

Let
\[
\mathscr L=\{(2a+1)\gamma-i(2b+1)\delta:a,b\in\mathbb Z\},\qquad
\mathscr P\Subset\mathbb C\setminus\mathscr L,\quad
R=\max_{\zeta\in\mathscr P}|\zeta|.
\]
Assume \(\mathscr P\ne\varnothing\). Every filter is monic,
\[
p(y)=\prod_{\nu=1}^{d}(y-\lambda_\nu),\qquad
\lambda_\nu\in\mathscr P,\quad1\le d\le q,
\]
with repetitions retained. Since the original roots belong to \(\mathscr L\), \(p\) is a unit modulo \(Q\). Define in the original numerator coefficient frame
\[
U_pa=[a/p],\quad \deg a<d,\qquad
H_{p,N}=U_p^*G_NU_p,\quad
H^B_{p,N}=U_p^*\Lambda^*Q_{B,N}\Lambda U_p.
\tag{RF5}
\]
Multiplying \(U_pa=0\) by the unit \(p\) gives \([a]=0\); its degree \(<d\le q\) proves \(a=0\). Thus \(H_{p,N}>0\) before any observed estimate.

## 2. A fixed contour and a complete collision-uniform remainder

The positive number \(\eta=\operatorname{dist}(\mathscr P,\mathscr L)\) exists because the first set is compact and the second closed. Choose
\(a_\Gamma\in(R+1,R+2)\) different from every lattice modulus in that bounded interval. Then
\(b_\Gamma=\operatorname{dist}(\{|z|=a_\Gamma\},\mathscr L)>0\).
Choose
\[
0<\varepsilon_\Gamma<\min(\eta/4,\delta/4,b_\Gamma/3,1/4).
\]
Let \(\Omega\) be the disk \(|z|<a_\Gamma\) with the closed radius-\(\varepsilon_\Gamma\) disks about every lattice point inside it removed. These disks are disjoint, lie strictly inside the outer circle, and miss \(\mathscr P\). Put \(\Gamma=\partial\Omega\), with the outer circle positive and all hole circles negative. Then
\[
\rho_\Gamma=\operatorname{dist}(\Gamma,\mathscr P)>0,\quad
b=\operatorname{dist}(\Gamma,\mathscr L)>0,\quad
|\Gamma|=2\pi a_\Gamma+2\pi\varepsilon_\Gamma\,\#(\mathscr L\cap\{|z|<a_\Gamma\}).
\tag{RF6}
\]
This construction is independent of \(k,d,p\). Every pole is enclosed with winding number one and every lattice point with winding number zero.

For \(f\) holomorphic on a neighbourhood of \(\overline\Omega\), set
\[
\mathcal R_pf(z)=\frac1{2\pi i}\int_\Gamma
\frac{f(w)}{p(w)}\,\frac{p(w)-p(z)}{w-z}\,dw .
\tag{RF7}
\]
The divided polynomial in \(z\) has degree \(<d\). Cauchy's formula writes the expression near each pole as \(f(z)-p(z)g(z)\) with \(g\) holomorphic there. Hence all derivatives through the pole's full multiplicity agree. This proves the complete Hermite remainder, including coincident poles. It also proves uniqueness: the difference of two such degree-\(<d\) polynomials is divisible by \(p\).

For every coefficient of \((p(w)-p(z))/(w-z)\), the elementary symmetric coefficient bounds give
\[
\left|[z^j]\frac{p(w)-p(z)}{w-z}\right|
\le (R+\max(1,a_\Gamma))^d.
\]
Indeed \(|[y^t]p|\le\binom dtR^{d-t}\), and the relevant finite geometric sum is bounded by the binomial expansion with \(\max(1,|w|)\). Since \(|p(w)|\ge\rho_\Gamma^d\),
\[
\|\operatorname{coeff}\mathcal R_pf\|_2
\le C_d\sup_\Gamma|f|,\qquad
C_d=\frac{|\Gamma|}{2\pi}\sqrt d
\left(\frac{R+\max(1,a_\Gamma)}{\rho_\Gamma}\right)^d.
\tag{RF8}
\]
There is no inverse distance between poles.

For later use write
\(H_{\rm odd}(t)=\sum_{1\le j\le t,\;j\ {\rm odd}}j^{-1}\).
The exact negation-pair shell count gives
\[
\sum_{\omega/\pm,\;\omega\in Q_k}\frac1{|\omega|^2}
\le \frac2{\delta^2}H_{\rm odd}(k).
\tag{RF9}
\]
Consequently, for \(|z|\le r\),
\[
|Q_k(z)/Q_k(0)|\le M_k^+(r)
:=\exp[2r^2H_{\rm odd}(k)/\delta^2].
\tag{RF10}
\]
For the reciprocal on \(\Gamma\), take one representative from every infinite-lattice negation pair of modulus at most \(2a_\Gamma\), and put
\[
C_\Gamma^-=\prod_{\substack{\omega/\pm\in\mathscr L\\|\omega|\le2a_\Gamma}}
\max(1,|\omega|^2/b^2),\qquad
M_k^-=C_\Gamma^-\exp[8a_\Gamma^2H_{\rm odd}(k)/(3\delta^2)].
\tag{RF11}
\]
Each retained small factor is bounded using
\(|(z-\omega)(z+\omega)|\ge b^2\). For all remaining factors,
\(|z^2/\omega^2|\le1/4\) and
\(-\log|1-z^2/\omega^2|\le(4/3)|z^2/\omega^2|\).
Thus \(\sup_\Gamma|Q_k(0)/Q_k|\le M_k^-\).
Both logarithmic costs are \(O_{\mathscr P,h}(\log(k+2))\), with every small lattice factor present.

## 3. Evaluation and division in the full Gamma source

Retain \(b_L=\sqrt{2L+1}\sum_{j=1}^L1/j\), \(b_0=0\). IVO5 proves, for every complex \(z\) and polynomial of degree at most \(L\),
\[
(2b_{L+1})^{-1}\|f\|_\sigma\le\|(y-z)f\|_\sigma
\le[2(L+1)+|z|]\|f\|_\sigma.
\tag{RF12}
\]
This estimate acts on polynomials, including when \(z\) is real.

A convenient explicit evaluation bound, slightly stronger than the received one, is
\[
\sqrt{K_{\sigma,L}(z,z)}
\le E_\sigma(L,r):=
\frac{e^{1+\pi r/4}}{\sqrt{M_\sigma}}
(L+1)(2L+1)^{r/2+1/4},\qquad |z|\le r.
\tag{RF13}
\]
For \(L\ge1\), apply Cauchy's coefficient estimate to the original generating function
\((1+t^2)^{-1/4}e^{z\arctan t}\) on \(|t|=L/(L+1)\).
The factors are bounded by
\((L+1)^{1/2}(2L+1)^{-1/4}\),
\(e^{\pi r/4}(2L+1)^{r/2}\), and \(e\).
The orthonormal coefficient ratio is
\(\rho_n=\sqrt{n!/(1/2)_n}\le\sqrt{2n+1}\).
Summing \(L+1\) squared bounds gives RF13. The case \(L=0\) follows from \(K_{\sigma,0}=1/M_\sigma\). Since
\((L+1)(2L+1)^{1/4}\le(L+1)^{3/4}(2L+1)^{1/2}\),
the received constant (18) follows as well.

Let \(D_zf=(f-f(z))/(y-z)\). Evaluation and RF12 give, for \(L\ge1\),
\[
\|D_zf\|_\sigma\le
\mathcal D(L,r)\|f\|_\sigma,\quad
\mathcal D(L,r)=2b_L[1+\sqrt{M_\sigma}E_\sigma(L,r)]
\quad(|z|\le r,\ \deg f\le L).
\tag{RF14}
\]
Successive divisions by \(\lambda_1,\ldots,\lambda_d\), retaining their order and multiplicity, have final quotient exactly \(\mathfrak Q_pf\). Expanding each identity \(f=(y-\lambda_1)D_{\lambda_1}f+f(\lambda_1)\) proves this by induction. Thus
\[
\|\mathfrak Q_pf\|_\sigma\le\mathcal D(L,R)^d\|f\|_\sigma
\quad(\deg f\le L,\ L\ge d).
\tag{RF15}
\]
If \(L<d\), the quotient is zero. No rational source integral occurs.

## 4. An explicit polynomial lift and its native upper norm

Set
\[
n_0=2\left\lfloor\frac{N+1-q}{2}\right\rfloor,\quad
K_0=K_{Q,n_0}(0,0),\quad T=T_{k,N}=\frac1{|Q(0)|\sqrt{K_0}},
\quad H(y)=K_{Q,n_0}(y,0)/K_0.
\tag{RF16}
\]
The finite guards used in this section are
\[
q\ge16,\quad R_k\le2^{-13}q,\quad n_0\le2q-2,\quad
a_\Gamma^2\le\beta_q/2,\qquad \beta_t=2^{-27}t^2.
\tag{RF17}
\]
IVO9–11 gives \(\|QH\|_\sigma=K_0^{-1/2}\), \(H(0)=1\), and
\(|H(z)|\ge e^{-n_0a_\Gamma^2/\beta_q}\) throughout \(|z|\le a_\Gamma\). In particular its reciprocal is holomorphic on the required contour region.

For \(\deg a<d\), put
\[
h=-H\mathcal R_p\!\left(\frac a{QH}\right),\qquad
f=\frac{a+Qh}{p}.
\tag{RF18}
\]
The numerator has the full required zero multiplicities at every root of \(p\). Thus \(f\) is a polynomial and
\(\deg f\le q+n_0-1\le N\). Its original class is \(U_pa\).
Since \(\deg a<d\), it also equals \(\mathfrak Q_p(Qh)\).

Define
\[
A_{\Gamma,d}=\left(\sum_{j=0}^{d-1}a_\Gamma^{2j}\right)^{1/2},\quad
V_{d,N}=\left(\sum_{j=0}^{d-1}[2(N+d+1)]^{2j}\right)^{1/2},
\]
\[
\mathcal U_{p,N}^{\,\rm unif}
=C_dA_{\Gamma,d}M_k^-e^{n_0a_\Gamma^2/\beta_q}
 V_{d,N}\mathcal D(N+d,R)^d.
\tag{RF19}
\]
RF8 bounds the coefficient norm of the remainder in RF18. Multiplying \(QH\) by its degree-\(<d\) remainder, RF12 bounds each power by the corresponding term in \(V_{d,N}\); all intermediate degrees are at most \(N+d\). Finally use RF15 on \(Qh\). Therefore
\[
\|U_pa\|_{G_N}\le
\sqrt{u_k}\mathcal U_{p,N}^{\,\rm unif}T\|\operatorname{coeff}a\|_2 .
\tag{RF20}
\]
The notation records a uniform constant: its displayed value depends on \(d\) and the fixed compact set, not on individual pole separations.

## 5. The full rational conductor and its explicit inverse

Retain every nonzero original conductor coefficient \(a_j\), physical shift \(b_j\), number \(J\), and first symbol moment \(\mu_v\ne0\). Set
\[
\tau_j=(b_j-4)/i,\quad
\widetilde{\mathcal T}_Af(y)=\sum_{j=1}^Ja_jf(y+\tau_j),
\quad \widetilde E_A(z)=\sum_ja_je^{\tau_jz}.
\tag{RF21}
\]
This is exactly IVO1: \(\tau_j=-\zeta_j\).
Its first nonzero derivative is \(i^{-v}\mu_v\), and \(0\le v\le J-1\).
Every \(\tau_j\) is an even lattice translation, so
\(\mathscr L+\tau_j=\mathscr L\).
Consequently all roots of every \(p(y+\tau_j)\) remain outside the full lower lattice, even when translated poles collide.

Write \(Q_-=Q_{k-8}\), \(q_-=(k-7)^2\),
\(\Delta=q-q_-=16k-48\), \(Z=\max_j|\tau_j|\), \(A_1=\sum_j|a_j|\), and
\[
B_p(y)=\prod_{j=1}^Jp(y+\tau_j),\quad L=Jd,\quad R_B=R+Z,
\quad N_a(y)=B_p(y)\widetilde{\mathcal T}_A(a/p)(y).
\tag{RF22}
\]
Here \(B_p\) denotes only the scalar denominator polynomial; the bounded inverse operator will be denoted \(\mathbf B_p\).

If \(a/p=c\,y^{-n}+O(y^{-n-1})\), \(n=d-\deg a\ge1\), then
\[
\widetilde{\mathcal T}_A(a/p)
=(-1)^v\binom{n+v-1}{v}i^{-v}\mu_v c\,y^{-n-v}
+O(y^{-n-v-1}).
\tag{RF23}
\]
Expanding \((y+\tau)^{-n}\) proves this coefficient; lower moments vanish, including every possible contribution from later Laurent coefficients. Therefore
\(\deg N_a=L-n-v\le L-v-1\), and the conductor on proper rational functions is injective.

Here is a complete finite inverse bound, without selecting a residue. Put
\[
e(z)=z^{-v}\widetilde E_A(-z),\quad e(0)=(-1)^vi^{-v}\mu_v/v!,
\quad H_*=\frac{2v!}{|\mu_v|}.
\]
A concrete admissible positive radius is
\[
\varrho=\min\left(1,\frac{|e(0)|(v+1)!}
 {2A_1\max(1,Z)^{v+1}e^Z}\right).
\tag{RF24}
\]
The exponential-series tail satisfies
\(|e(z)-e(0)|\le A_1Z^{v+1}|z|e^{Z|z|}/(v+1)!\le|e(0)|/2\)
on this disk. Hence Cauchy's formula gives
\(|[z^j]e^{-1}|\le H_*\varrho^{-j}\).

Define
\[
B_{d,L}=\sqrt L\sum_{j=0}^{v+d-1}
 \binom{L+j-1}{j}R_B^j,\quad
A_d=\max_{1\le n\le d}(n-1)!
 \sum_{\ell=1}^n\frac{H_*\varrho^{-(n-\ell)}}{(v+\ell-1)!},
\]
\[
\mathcal W_d=\sqrt d(1+R)^dA_dB_{d,L}.
\tag{RF25}
\]
To prove the bound, write
\(a/p=\sum_{n\ge1}c_ny^{-n}\),
\(\widetilde{\mathcal T}_A(a/p)=\sum_{n\ge1}b_ny^{-n}\).
Their exponential coefficient series obey exactly
\[
\sum_{n\ge1}\frac{b_nz^{n-1}}{(n-1)!}
=\widetilde E_A(-z)\sum_{n\ge1}\frac{c_nz^{n-1}}{(n-1)!}.
\tag{RF26}
\]
The first \(v+d\) Laurent coefficients of \(N_a/B_p\) are bounded by
\(B_{d,L}\|\operatorname{coeff}N_a\|_2\): expand
\(\prod_{\nu=1}^{L}(1-\xi_\nu/y)^{-1}\), whose degree-\(j\) coefficient is at most
\(\binom{L+j-1}{j}R_B^j\).
Inverting RF26 bounds each \(c_n\), \(n\le d\), by \(A_d\) times that number.
Finally multiply the first \(d\) Laurent coefficients by \(p\) and take the polynomial part. Its coefficient operator norm is at most
\((1+R)^d\), by the coefficient one-norm of \(p\).
Thus
\[
\|\operatorname{coeff}a\|_2
\le\mathcal W_d\|\operatorname{coeff}N_a\|_2.
\tag{RF27}
\]
In particular \(\log^+\mathcal W_d=O_{A,\mathscr P}(d\log(d+2))\), directly from the factorial and binomial bounds in RF25.

The exact lower quotient map is
\[
M_{B_p}^{(-)}C_AU_pa=[N_a]_{Q_-}.
\tag{RF28}
\]
Each shifted \(p\) is a unit there, by shifting a Bézout identity for \(p,Q\) and using \(Q_-\mid Q(y+\tau_j)\). This proves the identity on the complete lower quotient. On the finite algebraic guard
\[
L-v\le q_-,
\tag{RF29}
\]
every \(N_a\) is already its unreduced lower remainder. RF27 proves \(C_AU_p\) injective, including all translated collisions. The degree bound is attained by \(a=y^{d-1}\), so RF29 is the sharp guard for this unreduced-numerator recovery.

## 6. Lower norm with the full numerator and boundary product

Every polynomial \(f_-\), of degree at most \(N-v\), representing \(C_AU_pa\) satisfies
\[
B_pf_--N_a=Q_-h_-,\qquad
\deg h_-\le n_-:=N-v+L-q_- .
\tag{RF30}
\]
Since \(\deg N_a<L\), taking the entire remainder modulo \(B_p\) gives
\(N_a=-\mathcal R_{B_p}(Q_-h_-)\).
Use the circle of radius \(r_B=R_B+1\), on which every denominator factor has modulus at least one. RF8, now with \(L\) roots, gives the constant
\[
C_B=r_B\sqrt L(R_B+r_B)^L.
\]
IVO10 and RF10 give
\[
\|\operatorname{coeff}N_a\|_2
\le C_B |Q_-(0)|M_{k-8}^+(r_B)\,
 E_-(r_B)\sqrt{K_{Q_-,n_-}(0,0)}\,\|Q_-h_-\|_\sigma,
\]
\[
E_-(r_B)=
e^{n_-r_B^2/(2\beta_{q_-})}
\sqrt{1+r_B^2/\beta_{q_-}}.
\tag{RF31}
\]
The circle may enclose lattice roots: \(Q_-h_-\) is a polynomial, so no reciprocal of \(Q_-\) is used here.

The exact central-grid factorization is \(Q=Q_-D_\partial\).
Set
\[
W_N=2(q+n_0+1)+R_k,\quad
U_-=2(q_-+n_-+2),\quad V_-=b_{q_-+n_-+1}+q_-/\delta,
\]
\[
D_-=\prod_{t=1}^{\lfloor n_-/2\rfloor-n_0/2}
 \left[1+\left(\frac{U_-V_-}{n_0+2t}\right)^2\right],\qquad
\mathcal R_N=\frac{|D_\partial(0)|}{W_N^\Delta\sqrt{D_-}}.
\tag{RF32}
\]
The product is empty and equals one if its upper limit is zero.
Multiplication by every boundary factor and IVO12 prove
\[
\frac1{|Q_-(0)|\sqrt{K_{Q_-,n_-}(0,0)}}\ge\mathcal R_N T.
\tag{RF33}
\]
Indeed \(K_{Q_-,n_0}\le W_N^{2\Delta}K_{Q,n_0}\), then \(K_{Q_-,n_-}\le D_-K_{Q_-,n_0}\). All factors are retained. Moreover
\(|D_\partial(0)|\ge[\delta(k-6)]^\Delta\), since every boundary root has an odd coordinate of modulus at least \(k-6\).

Define
\[
\mathcal L_N=\frac{\mathcal R_N}
 {\mathcal W_dC_BM_{k-8}^+(r_B)E_-(r_B)},\quad
\mathcal B_N=2(N-v+L+1)+R_B,
\]
\[
\mathcal A_d=\sqrt{M_\sigma}A_1\sqrt d
 [2(L+1)+R_B]^{L-1}.
\tag{RF34}
\]
RF27 and RF31–33 give
\(\|Q_-h_-\|_\sigma\ge\mathcal L_NT\|\operatorname{coeff}a\|_2\).
The entire numerator in RF22 satisfies
\[
\|N_a\|_\sigma\le\mathcal A_d\|\operatorname{coeff}a\|_2,\qquad
\|B_pf_-\|_\sigma\le\mathcal B_N^L\|f_-\|_\sigma.
\tag{RF35}
\]
For the first bound, expand each \(a(y+\tau_j)\) in its original monomials. Every term is a product of at most \(L-1\) factors with root modulus at most \(R_B\); apply RF12 to each and then
\(\sum_{\nu<d}|a_\nu|\le\sqrt d\|a\|_2\). The second bound applies the same estimate to all \(L\) denominator factors.

For a numerical finite lower bound on \(T\), retain IVO23:
\[
T^{\rm lb}=
\frac{\sqrt{c_\sigma q/(1+16q^2)}
 (q-R_k)^q e^{-\pi q/2}}
 {|Q(0)|(n_0+1)10^{n_0}},
\qquad c_\sigma=\Gamma(1/4)^2/(2\pi).
\tag{RF36}
\]
Its proof is the full Legendre evaluation bound on \([q,2q]\), the Gamma lower envelope, and every factor of \(Q\). Thus \(T\ge T^{\rm lb}\).

The complete finite domain for the rational norm theorem is
\[
\boxed{
q_-\ge16,\quad R_k\le2^{-14}q_-,\quad
a_\Gamma^2\le\beta_q/2,\quad
L-v\le q_-,\quad n_-+2\le2q_-,\quad
\mathcal L_NT^{\rm lb}\ge2\mathcal A_d.}
\tag{RF37}
\]
These imply RF17 and every required relation-kernel degree: \(N-q-n_0\) is either \(-1\) or \(0\), and \(L-v=Jd-v\ge1\), so
\[
n_--n_0=\Delta+L-v+(N-q-n_0)\ge\Delta>0.
\]
Thus \(0\le n_0\le n_-\le2q_--2\le2q-2\). The radii of both \(Q\) and \(Q_-\) are at most \(R_k\le2^{-14}q_-\), within the respective \(2^{-13}\) root-radius allowances in IVO9. IVO10 permits every complex evaluation radius and retains its displayed exponential; no extra inequality involving \(r_B\) is needed in RF31. The separate bound \(a_\Gamma^2\le\beta_q/2\) is required and imposed for the nonvanishing reciprocal \(H^{-1}\) in IVO11. The last inequality in RF37 absorbs the complete numerator in RF30, giving for every representative
\[
\|f_-\|_\sigma\ge
\frac{\mathcal L_N}{2\mathcal B_N^L}\,T\|a\|_2.
\tag{RF38}
\]

To pass through the entire observation, use the exact original inclusion
\(K\subseteq\ker C_A\). Therefore there is a well-defined map
\(\widehat C_A:B\to E_-\) with \(\widehat C_A\Lambda=C_A\).
Every lift in RF4 has the same conductor image. IVO4, proved by applying the complete conductor to each such lift, gives
\[
\|P_BU_pa\|_{G_N}\ge
\frac{\sqrt{\ell_{k,N}}}{\mathcal F_N}
\|C_AU_pa\|_{\sigma,Q_-,N-v},\quad
\mathcal F_N=A_1e^{1+2\pi\gamma}(N+1)(2N+1)^{4\delta+1/2}.
\tag{RF39}
\]
Taking the minimum in RF38 now proves
\[
\boxed{
\ell_{k,N}\left(\frac{\mathcal L_N}
 {2\mathcal F_N\mathcal B_N^L}\right)^2T^2I_d
\preceq H^B_{p,N}\preceq H_{p,N}
\preceq u_k(\mathcal U_{p,N}^{\,\rm unif})^2T^2I_d.}
\tag{RF40}
\]
This proof does not identify the conductor kernel with \(K\).

Let \(E_{k,d,N}\) be the maximum of zero, the negative logarithm of the left scalar in RF40 after division by \(u_kT^2\), and the logarithm of the right scalar after that division. All its constants are displayed. For fixed original data,
\[
E_{k,d,N}=O_{h,A,\mathscr P}((k+Jd)\log(q+Jd+2)).
\tag{RF41}
\]
The bounds follow from RF8–15, RF25 and the \(O(k+Jd)\) factors in RF32. No contour constant depends on pole collisions. If \(d\log(q+2)=o(q)\), then \(d=o(q)\), \(n_-=N-q+O(k+Jd)\), and all degree/radius guards in RF37 hold eventually, uniformly over the pole family and \(q-1\le N\le2q\). Also
\(\log T^{\rm lb}\ge q\log(q/k)-O_h(q)\), whereas
\(\log^+(\mathcal A_d/\mathcal L_N)=o(q)\), so the absorption guard holds eventually. Consequently RF40 proves received (12)–(13) with \(E_{k,d}=\max_NE_{k,d,N}=o(q)\).

## 7. The remainder projection is onto and the inverse has rank \(d\) at the late scale

Define
\[
T_p=\mathcal R_pL_N,\quad
\mathbf B_p=J_N\mathfrak Q_pL_N,\quad F_p=U_pT_p.
\]
Complete polynomial division of the actual minimum representative gives
\[
X=p(M)^{-1}=\mathbf B_p+F_p,\qquad
\|\mathbf B_p\|_{G_N}\le
\beta_N:=\sqrt{u_k/\ell_{k,N}}\,\mathcal D(N,R)^d.
\tag{RF42}
\]
When \(N<d\), the quotient vanishes and \(\beta_N\) may be set to zero. In the eventual growing family \(d<N\). In all cases
\(\log^+\beta_N=O_{h,\mathscr P}(k+d\log(q+2))\).

For the low-polynomial inclusion \(\iota:a\mapsto[a]\), write its original minimum lift as
\(L_N[a]=a-Qh_a\).
The second term is the \(\mu_k\)-orthogonal projection of \(a\) onto the entire relation space \(Q\mathcal P_{N-q}\). Hence
\[
\|Qh_a\|_\sigma\le\sqrt{u_k/\ell_{k,N}}\|a\|_\sigma.
\tag{RF43}
\]
If \(N=q-1\), this term is zero. Otherwise \(\deg h_a\le N-q\le n_0\).
Define
\[
P_d=\sqrt{M_\sigma}
 \left(\sum_{j=0}^{d-1}[2(d+1)]^{2j}\right)^{1/2},\quad
E_0(r)=e^{n_0r^2/(2\beta_q)}\sqrt{1+r^2/\beta_q},
\]
\[
\eta_N=
\frac{C_dM_k^+(a_\Gamma)E_0(a_\Gamma)
 \sqrt{u_k/\ell_{k,N}}P_d}{T^{\rm lb}}.
\tag{RF44}
\]
At \(N=q-1\) set \(\eta_N=0\).
The coefficient bound \(\|a\|_\sigma\le P_d\|a\|_2\), RF8, RF10, and IVO10 show
\[
T_p\iota=I-\mathcal E_{p,N},\qquad
\|\mathcal E_{p,N}\|\le\eta_N.
\tag{RF45}
\]
Here the factor \(|Q(0)|\sqrt{K_0}=T^{-1}\) arises exactly; no small relation projection is presumed. Thus the finite guard \(\eta_N<1\) proves that
\(\iota(I-\mathcal E_{p,N})^{-1}\) is a right inverse of \(T_p\), of norm at most
\[
\sqrt{u_k}P_d/(1-\eta_N).
\tag{RF46}
\]
Also RF8 and RF13 on the actual minimum section give
\[
\|T_p\|\le C_dE_\sigma(N,a_\Gamma)/\sqrt{\ell_{k,N}}.
\tag{RF47}
\]
For an onto Hilbert-space map, the norm of any right inverse bounds the reciprocal of its least positive singular value: apply its adjoint to a target unit vector, or use the attained inverse. Combining RF40 and RF46–47 gives
\[
f_-T\le s_d(F_p)\le s_1(F_p)\le f_+T,
\tag{RF48}
\]
\[
f_-=
\sqrt{\ell_{k,N}/u_k}\,
\frac{\mathcal L_N(1-\eta_N)}
 {2\mathcal F_N\mathcal B_N^LP_d},\qquad
f_+=
\sqrt{u_k/\ell_{k,N}}\,
\mathcal U_{p,N}^{\,\rm unif}C_dE_\sigma(N,a_\Gamma).
\]
This proves rank \(d\); rank is not inferred from the division identity alone.

A complete useful cluster guard is
\[
\boxed{\eta_N\le\tfrac12,\qquad f_-T^{\rm lb}>2\beta_N.}
\tag{RF49}
\]
Both follow eventually from the explicit growth in RF36, uniformly over the admissible pole family. Weyl's singular-value inequality and the rank-\(d\) perturbation bound give
\[
f_-T-\beta_N\le s_d(X)\le s_1(X)\le f_+T+\beta_N,\qquad
s_{d+1}(X)\le\beta_N\quad(d<q).
\tag{RF50}
\]
For completeness the last inequality follows by restricting \(X\) to
\(\ker F_p\), of dimension at least \(q-d\), where \(X=\mathbf B_p\).
Taking reciprocal singular values in the original metric therefore proves
\[
\log s_{q-d+j,N}(p(M))=-\log T+O_{h,A,\mathscr P}((k+Jd)\log(q+Jd+2)),
\quad1\le j\le d,
\]
\[
s_{q-d,N}(p(M))\ge\beta_N^{-1}\quad(d<q).
\tag{RF51}
\]
The least \(d\) singular directions are exactly the late cluster because their logarithms are
\(-q\log(q/k)+O_h(q)\), while the remaining ones are bounded below by \(e^{-o(q)}\).

## 8. Evaluated exponent and the complete observed late heat

The actual retained analytic providers are H4–9 of
[the original profile proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/RETAINED_PROFILE_PROOF.tex),
S2–4 and S22–30 of
[the smallest-singular proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/0fd693c844aad9117e30ec447c59864a28af10f3/workbenches/splitzero-tandem/continuations/20260921-native-spectral-real-pair/003/NATIVE_SMALLEST_SINGULAR_PROOF.tex),
and IFH8–10 of
[the original flag proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/edd4008690952fb8568a01744e49ad7e180401e9/workbenches/splitzero-tandem/continuations/20260921-original-observation/INVERSE_FLAG_AND_RELATIVE_HEAT.tex#L132).
Their profile and zero-law status is retained, rather than reclassified as a finite matrix computation.

Here is the exact connection to \(T\). For even \(n=n_0\), let \(V_n,\nu_n^\Gamma\) be the monic polynomial and its squared norm for the full \(Q^2d\sigma\).
Parity and Christoffel–Darboux give
\[
K_{Q,n}(0,0)=\frac{V_n(0)^2\Xi_n}{\nu_n^\Gamma},
\qquad \Xi_n=\frac{V_{n+1}'(0)}{V_n(0)}.
\tag{RF52}
\]
Positive-zero interlacing as in IFH9 gives
\(1\le\Xi_n\le4(q+n+2)^2/\beta_q\); \(\Xi_0=1\).
Thus \(\log\Xi_n=O(1)\) on the retained degree window.
Applying NG2 on the full degree-\(q+n\) monic source and relation fibres transfers H4 to the Gamma ratio: each of the two minima changes by a factor between the same positive source-comparison constants, so the logarithm of their ratio changes by at most \(\log(u_k/\ell_{k,2q+2})=O_h(k+\log q)\). Therefore the full reference monic profile gives
\(\log(\nu_n^\Gamma/\gamma_{q+n})=2q\psi(n/q)+o(q)\),
where \(\gamma_j=M_\sigma j!(1/2)_j\).
The zero law, with the finite IVO9 gap permitting the logarithmic test, gives
\[
\log|V_n(0)|=n\log q+\frac{sq}{2}\int\log x\,\rho_s(x)\,dx+o(q),
\quad n/q\to s>0.
\]
At \(s=0\), the fixed scaled lower and upper zero bounds make the residual \(O(n)=o(q)\). The actual root product, proved with its \(O(k)\) error in [HAR35 of the pinned harmonic proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/360d3c1d798da434966d35f7e407fc59c14f234b/workbenches/splitzero-tandem/continuations/20260921-critical-inverse-activation/HARMONIC_PROOFS.md#L389), is
\[
\log|Q(0)|=q\log k+\tfrac q2 I+O_{\delta,\gamma}(k),
\quad
I=\log(\delta^2+\gamma^2)-3+
\frac\delta\gamma\arctan\frac\gamma\delta+
\frac\gamma\delta\arctan\frac\delta\gamma .
\]
Substituting into RF52 proves on the established window \(0\le s\le1\), including each adjacent-cutoff pair,
\[
\log T=q\log(q/k)+q[\psi(s)+J(s)-I/2]+o_h(q),
\]
\[
J(s)=(1+s)(\log(1+s)-1)-\frac s2\int\log x\,\rho_s(x)\,dx,\qquad
J(0)=-1.
\tag{RF53}
\]
No profile outside this source window is needed or claimed. RF51 and RF53 prove received (26)–(27), uniformly in the admissible pole family and singular index.

At the four actual cutoffs \(q-1,q,2q-1,2q\), use the same polynomial and signs \(+,+,-,-\). Put
\[
\mathfrak C=4[\psi(0)-\psi(1)-J(1)-1],
\quad 1.353893<\mathfrak C<1.354751.
\]
The interval is the inherited directed certificate, not a new numerical test. Taking determinants of RF40, and observing that \(u_k\) and the numerator coefficient frame are identical at all endpoints, gives
\[
\mathcal R\log\det H^X_{p,N}=\mathfrak C\,dq+o(dq),\quad X=E,B,
\]
\[
\mathcal R\sum_{j=q-d+1}^{q}\log s_{j,N}(p(M))^2
=-\mathfrak C\,dq+o(dq).
\tag{RF54}
\]
The finite determinant error is bounded by \(d\sum_NE_{k,d,N}\).

For the common time
\[
\tau_k^*=\exp\{2q[\log(q/k)-1-I/2]\},
\tag{RF55}
\]
every slow heat exponent tends to zero exponentially at the low pair, because
\(-1-\psi(0)-J(0)=-\psi(0)<0\).
At the high pair it tends to infinity exponentially, because
\(\psi(1)<1/8\) and the retained \(J(1)<-1.163427\) imply
\(-1-\psi(1)-J(1)>0\).
The remaining heat contribution is at most
\((q-d)e^{-\tau_k^*/\beta_N^2}\), by RF50.
Hence
\[
\frac1d\mathcal R\operatorname{Tr}e^{-\tau_k^*p(M)^\dagger p(M)}\longrightarrow2.
\tag{RF56}
\]

The observed assertion needs the actual original projection, rather than unweighted slow counts. Let \(V_d\) be the top left singular space of \(X\). If \(x\in V_d\), then \(\|X^{-1}x\|\le\|x\|/s_d(X)\), and
\[
\|(I-P_{\operatorname{ran}U_p})x\|
=\|(I-P_{\operatorname{ran}U_p})\mathbf B_pX^{-1}x\|
\le\epsilon_N\|x\|,\quad
\epsilon_N=\frac{\beta_N}{f_-T-\beta_N}.
\tag{RF57}
\]
RF40 gives \(\ell_N=e^{-2E_{k,d,N}}\) on \(\operatorname{ran}U_p\). For any orthogonal projections onto \(K\), \(U\), and any unit \(x\) at distance at most \(\epsilon\) from \(U\), Cauchy–Schwarz in the two orthogonal components gives
\[
|\langle z,x\rangle|\le
a\sqrt{1-t^2}+\sqrt{1-a^2}\,t,\quad
a=\|P_Uz\|\le\sqrt{1-\ell},\quad
t=\|(I-P_U)x\|\le\epsilon,\quad z\in K,\ \|z\|=1.
\]
If \(\epsilon<\sqrt\ell\), this expression increases in both \(a,t\) on these intervals. Substituting their endpoints and subtracting the square from one proves the sharp lower fraction
\[
\ell_{\rm sharp,N}
=\left(\sqrt{\ell_N}\sqrt{1-\epsilon_N^2}
-\sqrt{1-\ell_N}\epsilon_N\right)_+^2.
\tag{RF58}
\]
For \(\epsilon_N\ge\sqrt{\ell_N}\) this bound is zero. If needed use
\(\min(1,\epsilon_N)\) in the displayed expression.
The finite additional guard
\(\epsilon_N\le\sqrt{\ell_N}/4\)
implies \(\ell_{\rm sharp,N}\ge\ell_N/4\).
It holds eventually because \(\log\epsilon_N=-q\log(q/k)+O_h(q)\), whereas \(E_{k,d,N}=o(q)\).

If \(Xu_j'=s_j(X)u_j\), then \(p(M)^\dagger p(M)u_j=s_j(X)^{-2}u_j\). Thus the same left singular vectors are exactly the slow heat eigenvectors. Their observed weights are \(\|P_Bu_j\|^2\), bounded below by RF58. The measured trace is
\[
\operatorname{Tr}(\Lambda e^{-\tau p(M)^\dagger p(M)}L_{B,N})
=\sum_j e^{-\tau/s_j(X)^2}\|P_Bu_j\|^2.
\tag{RF59}
\]
At \(\tau=\tau_k^*\), the positive low pair contributes at least
\(d(\ell_{\rm sharp,q-1}+\ell_{\rm sharp,q})(1-o(1))\).
The total negative high pair is at most \(2q\exp[-\exp(cq)]\) for some fixed \(c>0\), eventually; all noncluster tails satisfy the same type of stronger bound. The first term is \(d e^{-o(q)}\), so it dominates. The upper bound on the return divided by \(d\) is \(2+o(1)\). Consequently the return is eventually positive and
\[
\frac1q\log\left[
\frac1d\mathcal R\operatorname{Tr}
(\Lambda e^{-\tau_k^*p(M)^\dagger p(M)}L_{B,N})\right]\longrightarrow0.
\tag{RF60}
\]
For a nonmonic filter \(c_kp_k\), singular values are multiplied by \(|c_k|\) and heat time by \(|c_k|^2\), exactly.

## 9. The explicit ES datum, its action, and the original kernel quotient

The selected witness and filter datum are attributed to the received continuation; no unread ES foundation file is claimed as a source. Direct rational arithmetic proves
\[
\frac4{13}=\frac14+\frac1{18}+\frac1{468},
\]
\[
\begin{gathered}
P_{\rm ES}(t)=(t-13)(t-4)(t-18)(t-468)\\
=t^4-503t^3+16738t^2-168480t+438048,\\
\sum_{\lambda=13,4,18,468}\lambda^{-1}=\frac5{13}.
\end{gathered}
\tag{RF61}
\]
Take the literal polynomial \(p_k=P_{\rm ES}^k\), degree \(d=4k\). Its real poles have distance at least \(\delta\) from every original odd-lattice root. Since \(4k\log(q+2)=o(q)\), all preceding eventual conclusions apply with every repetition retained:
\[
\mathcal R\log\det H^B_{p_k,N}=4\mathfrak C\,kq+o(kq),
\quad 5.415572<4\mathfrak C<5.419004,
\]
\[
\frac1{4k}\mathcal R\operatorname{Tr}
e^{-\tau_k^*p_k(M)^\dagger p_k(M)}\longrightarrow2,
\tag{RF62}
\]
and the original measured heat obeys RF60.
For \(J\le81\), the unreduced-conductor guard follows from
\(324k\le(k-7)^2\) when \(k\ge341\), \(k\equiv1\pmod4\):
the difference \(k^2-338k+49\) is 1072 at 341 and increasing thereafter.
This is an algebraic threshold only. RF37 and RF49, not this single integer, specify the additional finite analytic guards.

For any admissible monic \(p\), let \(C_p\) be multiplication by \(y\) on
\(\mathbb C[y]/(p)\) in its unchanged coefficient frame. Polynomial division of \(ya\) gives the exact maps
\[
MU_p=U_pC_p+[1]e_{d-1}^*,\qquad
M_SU_p=U_p(kI/2+iC_p)+i[1]e_{d-1}^*.
\tag{RF63}
\]
The quotient \(ya/p\) has constant part equal to the leading coefficient of \(a\), proving both identities. The attained compression is
\[
H_{p,N}^{-1}U_p^*G_NMU_p
=C_p+H_{p,N}^{-1}U_p^*G_N[1]e_{d-1}^*.
\tag{RF64}
\]
The domain of \(U_p\) has its pulled-back metric \(H_{p,N}\). If its domain instead uses the Euclidean metric, its adjoint is \(U_p^*G_N\), not \(H_{p,N}^{-1}U_p^*G_N\). This explicit metric convention repairs the ambiguity in the received adjoint notation (57).

The exact monic physical denominator is
\(D(S)=i^dp((S-k/2)/i)\), with numerator map
\(a\mapsto i^da((S-k/2)/i)\).
The quotient-coordinate isomorphism \([f(y)]\mapsto[f((S-k/2)/i)]\)
intertwines these two rational maps, since both \(i^d\) factors cancel in their ratio. The source and observed Grams transform by the same numerator congruence. If an existing physical unit is subsequently multiplied, it acts on every term of RF63, including the defect vector. The ES integers are filter poles; these exact maps do not identify them with zeta zeros.

Finally define, in the original coefficient coordinates,
\[
\pi_p[x]=\mathfrak Q_p(\operatorname{rem}_Q(px))
\in\mathcal P_{<q-d}.
\tag{RF65}
\]
For \(x\) of degree below \(q-d\), \(px\) has degree below \(q\), so \(\pi_p[x]=x\). Thus the low-polynomial inclusion is a right inverse. Also \(\pi_p[x]=0\) exactly when \(\operatorname{rem}_Q(px)=a\) has degree below \(d\), equivalently \([x]=U_pa\). Hence \(\ker\pi_p=\operatorname{ran}U_p\).
RF40 implies this subspace meets \(K\) only at zero, so \(\pi_p|_K\) is injective.

Let \(I_K\) be any fixed full frame. Completing the quadratic form over the entire \(U_p\)-fibre proves that the attained quotient metric is
\((\pi_pG_N^{-1}\pi_p^*)^{-1}\).
The two Schur complements of the full Gram of \([I_K,U_p]\) then give the exact equality
\[
\begin{aligned}
\delta_{p,N}
&=\log\det H_{p,N}-\log\det H^B_{p,N}\\
&=\log\det(I_K^*G_NI_K)
-\log\det\!\left[
(\pi_pI_K)^*(\pi_pG_N^{-1}\pi_p^*)^{-1}(\pi_pI_K)\right].
\end{aligned}
\tag{RF66}
\]
Indeed, after using orthonormal frames of \(K,U_p\), both ratios are determinants of \(I-C^*C\) or \(I-CC^*\), where \(C\) is their full cross Gram. Their nonzero singular values coincide and their number is at most \(\min(\dim K,d)\). RF40 bounds each observed relative eigenvalue below by \(e^{-2E_{k,d,N}}\). Therefore
\[
0\le\delta_{p,N}\le2\min(\dim K,d)E_{k,d,N}.
\tag{RF67}
\]
On the actual original kernel, \(\dim K=8k-16\), so RF41 gives
\(\sum_N\delta_{p,N}=o(kq)\). Subtracting RF66 at the same four cutoffs proves received (58) with the complete original kernel and attained quotient intact. The result preserves its leading coefficient; it does not assign a value to that coefficient.

## 10. What the finite theorem establishes

RF37 is the complete finite norm domain. RF44 and RF49 make the remainder map onto and separate exactly \(d\) singular directions. RF58 states the further explicit observation guard for transferring the cluster. All of these follow from \(d\log(q+2)=o(q)\) with fixed original data, but their finite inequalities remain available before passage to a limit.

The original-source scalar factors, the full conductor numerator, every boundary root, the physical \(i\) in the coordinate map, the pulled-back adjoint metric, and the whole observation minimum have appeared explicitly. The retained high-endpoint coefficient uses the established H/IFH analytic inputs. The separate finite reduced model and complete memory/energy calculations are handled by their own derivations, not replaced by this rational norm theorem.

The independent checker check_rational_filters.py records 113 passing exact checks in RATIONAL_FILTER_CHECKS.json. It computes Hermite contour residues at repeated poles, the complete Laurent inverse with translated-pole collisions, both actual lattice shifts, a full polynomial moment source with its entire relation minimum, a complex observation and all its cross terms, the action defect, both quotient angle determinant ratios, and the ES arithmetic. Its small lattices test exact algebra; they are explicitly outside the asserted eventual analytic domain. No new native moment computation or limiting-profile certificate is claimed.
