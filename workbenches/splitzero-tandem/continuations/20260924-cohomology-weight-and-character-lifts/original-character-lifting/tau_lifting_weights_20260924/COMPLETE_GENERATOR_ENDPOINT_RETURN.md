# Complete-domain endpoint inverses and their original Schwartz return

24 September 2026. GER0–GER7. The continuous endpoint resolvents already occur in the retained ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md, RZ3.1–RZ3.9. This note does not claim their discovery. It propagates them through the actual original summation image, constructs integral formulas on both original source spaces, computes the full \(L(L-1)\) representative and its exact covariance correction, and retains every zero jet and support label.

## GER0. Source and operation prerequisites

CORPUS_AND_OPERATION_RULES.md and the complete user global arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were read for the accompanying OMS proof. They continue to govern this calculation. The arithmetic and coefficient field here are the already reconstructed receivers. No addition, numerical weight, coordinate, or parity is assigned to primitive \(Z_1/\tau\).

The exact source spaces, synthesis proof, and comparison to Ralf Meyer's original author TeX are in ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md OMS0–OMS8, read and proved for this continuation. Human source: Ralf Meyer, [A spectral interpretation for the zeros of the Riemann zeta function, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), original Meyer.tex, lines 225–738, especially the:Zeta_estimate and the:Lap_range. The original author file has SHA256 ab9bc31f3c105a64fdc6f3b65ad16701dd8bf218fc90df98fe8d7f3c7c58c00e. Connes and Consani retain attribution for the source geometry and summation construction; RZ and OMS are programme derivations, not replacements of their sources.

The exact prior endpoint formula is RZ3.9 with resolvent convention \((\lambda-L)^{-1}\). Here the two inverse operators have convention \((L-c)^{-1}\), so the overall minus sign is retained in GER2. All divisions below occur in named complex receiving spaces.

## GER1. Original functions, operator, and full multiplier

Keep
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f\text{ even},\
f(0)=0,\ \int_{\mathbb R}f=0\},
\]
\[
\mathcal A=\{k:\ p_{N,j}(k)=
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jk(u)|<\infty
\quad(N,j\ge0)\},
\]
\[
\mathcal Ef(u)=u^{1/2}\sum_{n\ge1}f(nu),\quad
F_k(s)=\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},
\]
\[
I_A=\mathcal ES=\overline{\mathcal ES}^{\,\mathcal A},\qquad Q=\mathcal A/I_A.
\tag{GER1.1}
\]
The image equality is the existing proved global synthesis, with continuous source inverse, OMS3.14. Its Mellin target is the Fréchet space
\[
\mathcal B=\{F\text{ entire}: b_{A,M}(F)=
\sup_{|\sigma|\le A,t\in\mathbb R}(1+|t|)^M|F(\sigma+it)|<\infty\}.
\]
Under the topological isomorphism \(\mathcal M:\mathcal A\to\mathcal B\),
\[
I_\zeta=\mathcal M I_A
=\{F:F^{(r)}(\rho)=0\ (\rho\in\mathcal Z,\ 0\le r<m_\rho)\},
\quad Q\cong\mathcal B/I_\zeta.
\tag{GER1.2}
\]
Here \(\mathcal Z\) and \(m_\rho\) are the actual original nontrivial zeros and their full multiplicities.

The full generator on \(\mathcal A\) is
\[
D=\frac12-u\partial_u,\qquad
\mathcal M Dk(s)=sF_k(s);
\tag{GER1.3}
\]
integration by parts proves the identity, with both boundary terms zero by the defining seminorms. Multiplication by \(s\) preserves \(I_\zeta\), so \(D\) induces the continuous operator \(L\) on all of \(Q\).
Retain the actual source element
\[
f_*(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},
\quad k_*=\mathcal Ef_*,
\]
\[
F_*(s)=\mathcal Mk_*(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{GER1.4}
\]
The full Gaussian Mellin calculation and its endpoint conditions are OMS2.3–OMS2.5. In particular
\[
F_*(0)=F_*(1)=\frac18,\qquad
b:=\frac{F_*'(0)}{F_*(0)}
=\frac12\log(4\pi)-1-\frac\gamma2,
\quad F_*'(1)=-\frac b8.
\tag{GER1.5}
\]
The last identity follows from the exact reflection \(F_*(s)=F_*(1-s)\).
At each original trivial zero,
\[
F_*(-2r)=
\frac{(1+2r)2r}{8}\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{GER1.6}
\]
These values retain the zero/pole cancellations of the displayed multiplier. The original \(\zeta\) is not replaced by \(F_*\).

## GER2. Exact endpoint representatives and continuous inverse on \(Q\)

For \(c=0\) or \(c=1\), define on every \(F\in\mathcal B\)
\[
\mathscr S_cF(s)=\frac{F(s)-8F_*(s)F(c)}{s-c}.
\tag{GER2.1}
\]
Its numerator vanishes at \(c\) by (GER1.5). The exact removable value is
\[
\mathscr S_0F(0)=F'(0)-bF(0),\qquad
\mathscr S_1F(1)=F'(1)+bF(1).
\tag{GER2.2}
\]
These are the negatives of the RZ endpoint resolvents with parameter \(\lambda=c\).

For completeness, this entire division is continuous in the full topology. If \(N(c)=0\), then outside \(|s-c|<1\),
\((1+|\Im s|)^M|N(s)/(s-c)|\le(1+|\Im s|)^M|N(s)|\).
Inside \(|s-c|\le1\), the maximum principle applied to the removable quotient on the radius-two disk gives
\[
|N(s)/(s-c)|\le\frac12\sup_{|z-c|=2}|N(z)|.
\]
For \(A'\ge\max(A,c+2)\), the weight on the smaller disk is at most \(2^M\), whence
\[
b_{A,M}(N/(s-c))\le b_{A,M}(N)+2^{M-1}b_{A',0}(N).
\tag{GER2.3}
\]
The numerator in (GER2.1) satisfies
\[
b_{A,M}(F-8F_*F(c))
\le b_{A,M}(F)+8b_{A,M}(F_*)b_{A',0}(F)
\]
when \(A'\ge c\). This proves continuity of \(\mathscr S_c:\mathcal B\to\mathcal B\).

If \(F\in I_\zeta\), its numerator is in \(I_\zeta\); division by \(s-c\), which is nonzero at every actual nontrivial zero, preserves every required order. Thus it descends independently of the representative to a continuous \(S_c:Q\to Q\). On \(\mathcal B\) the exact identities are
\[
(s-c)\mathscr S_cF=F-8F_*F(c),\qquad
\mathscr S_c((s-c)F)=F.
\tag{GER2.4}
\]
The correction in the first identity belongs to the actual summation image. Therefore
\[
\boxed{S_0=L^{-1},\qquad S_1=(L-1)^{-1}}
\tag{GER2.5}
\]
are continuous two-sided inverses on the complete original \(Q\).

## GER3. Explicit return on the original strong test space

For \(k\in\mathcal A\), let
\[
g_c(u)=k(u)-8F_k(c)k_*(u),\qquad F_{g_c}(c)=0.
\tag{GER3.1}
\]
Define
\[
(\mathscr s_ck)(u)
=u^{1/2-c}\int_u^\infty g_c(v)v^{c-1/2}\frac{dv}{v}
=-u^{1/2-c}\int_0^u g_c(v)v^{c-1/2}\frac{dv}{v}.
\tag{GER3.2}
\]
The two expressions agree by \(F_{g_c}(c)=0\). Both integrals converge absolutely by the endpoint estimates for \(\mathcal A\). Differentiation gives
\[
(D-c)\mathscr s_ck=g_c.
\tag{GER3.3}
\]

Here are complete topology estimates. For an integer \(K\ge1\), on \(u\ge1\) use the first integral and \(|g_c(v)|\le p_{K,0}(g_c)v^{-K}\) to get
\[
|\mathscr s_ck(u)|
\le\frac{p_{K,0}(g_c)}{K-c+1/2}u^{-K}.
\]
On \(u\le1\), the second gives
\[
|\mathscr s_ck(u)|
\le\frac{p_{K,0}(g_c)}{K+c-1/2}u^K.
\tag{GER3.4}
\]
All denominators are positive for \(K\ge1\), \(c=0,1\). Taking \(K\ge N+1\) controls \(p_{N,0}\). Let \(\partial_{\log}=u\partial_u\), \(\alpha=1/2-c\), and \(h=\mathscr s_ck\). The differential identity gives for \(j\ge1\)
\[
\partial_{\log}^jh
=\alpha^j h-\sum_{\ell=0}^{j-1}\alpha^{j-1-\ell}
\partial_{\log}^{\ell}g_c.
\tag{GER3.5}
\]
Together with (GER3.4) this bounds every seminorm of \(h\) by finitely many of \(g_c\). Finally
\[
|F_k(c)|\le p_{K,0}(k)
\left(\frac1{K+c-1/2}+\frac1{K-c+1/2}\right)
\tag{GER3.6}
\]
follows by splitting its integral at one. Hence \(\mathscr s_c:\mathcal A\to\mathcal A\) is continuous. Taking Mellin transforms in (GER3.3), with the proved endpoint decay, gives exactly \(\mathcal M\mathscr s_ck=\mathscr S_cF_k\). Thus the integral and the RZ representative agree, with no auxiliary function space.

## GER4. Explicit return on the actual Schwartz summation image

This strengthens a mere closure-preservation statement by giving the actual preimage. Let \(f\in S\), put \(F=F_{\mathcal Ef}\), and define
\[
r_c(v)=f(v)-8F(c)f_*(v).
\tag{GER4.1}
\]
For \(v>0\), put
\[
(\mathscr t_cf)(v)=v^{-c}\int_v^\infty r_c(w)w^c\frac{dw}{w}
=-\int_0^1 r_c(vt)t^{c-1}\,dt,
\tag{GER4.2}
\]
and extend evenly. The equality of the two forms uses \(\int_0^\infty r_c(w)w^c dw/w=0\), verified next.

For \(c=0\), the original Mellin identity \(F(s)=\zeta(s)M_f(s)\), with \(\zeta(0)=-1/2\), gives \(M_{r_0}(0)=0\) because \(F_{\mathcal Er_0}(0)=0\). For \(c=1\), \(M_{r_1}(1)=0\) since \(r_1\in S\). Its additional logarithmic moment also vanishes:
\[
M_{r_1}'(1)=F_{\mathcal Er_1}(1)=0.
\tag{GER4.3}
\]
Indeed \(M_r(1)=0\) and the original residue \(\operatorname{Res}_{s=1}\zeta(s)=1\) imply \(F_{\mathcal Er}(1)=M_r'(1)\); this uses the full pole rather than treating \(\zeta(1)\) as a value.

At infinity the first expression in (GER4.2), and its differentiated versions, gives arbitrary Schwartz decay. At zero use the second. For \(j\ge1\) its derivative is the integral of \(-r_c^{(j)}(vt)t^{c+j-1}\), which is integrable. For \(j=0,c=0\), use \(r_c(vt)=O(v^2t^2)\), because \(r_c\) is even and vanishes at zero. These estimates also prove continuity in all local smooth seminorms. At zero its value is zero and every odd derivative is zero, so the even extension is smooth.

For sufficiently large \(\Re s\), absolute Fubini in the tail formula gives
\[
M_{\mathscr t_cf}(s)=\frac{M_{r_c}(s)}{s-c}.
\tag{GER4.4}
\]
Both sides continue to the region containing \(s=1\). For \(c=0\) its value there is \(M_{r_0}(1)=0\). For \(c=1\) it is \(M_{r_1}'(1)=0\) by (GER4.3). Thus \(\int_{\mathbb R}\mathscr t_cf=0\), proving \(\mathscr t_cf\in S\).
For an explicit tail estimate after differentiation, the equation
\(-v(\mathscr t_cf)'-c\mathscr t_cf=r_c\) expresses each derivative in terms of the tail integral and finitely many derivatives of \(r_c\), multiplied by powers of \(v^{-1}\); on \(v\ge1\) these preserve arbitrary decay. On \(v\le1\) the integral derivative bounds above are controlled by finitely many Schwartz seminorms. The scalar \(F(c)\) depends continuously on \(f\) through \(\mathcal E\), so \(\mathscr t_c:S\to S\) is continuous.

Multiplying (GER4.4) by the original \(\zeta(s)\) proves
\[
\boxed{\mathscr s_c\mathcal E=\mathcal E\mathscr t_c,\qquad
\mathscr S_cF_{\mathcal Ef}=F_{\mathcal E\mathscr t_cf}.}
\tag{GER4.5}
\]
The preservation of the actual image is therefore constructive, without replacing it by its closure.

## GER5. The exact inverse of \(P(L)=L(L-1)\)

Direct substitution into (GER2.1), retaining both endpoint values, gives the identities on the full \(\mathcal B\):
\[
\boxed{\mathscr S_0\mathscr S_1
=\mathscr S_1\mathscr S_0
=\mathscr S_1-\mathscr S_0
=\mathscr T,}
\]
\[
\mathscr TF(s)=
\frac{F(s)-8F_*(s)((1-s)F(0)+sF(1))}{s(s-1)}.
\tag{GER5.1}
\]
For example \((\mathscr S_1F)(0)=F(1)-F(0)\); substituting it into \(\mathscr S_0\) gives the displayed numerator. The other composition uses \((\mathscr S_0F)(1)=F(1)-F(0)\) and gives exactly the same expression. Subtracting the two original fractions gives \(\mathscr S_1-\mathscr S_0\). These are representative identities, not merely quotient identities.

Both endpoint singularities are removable. Their exact values are
\[
\mathscr TF(0)=-F'(0)+(b-1)F(0)+F(1),
\]
\[
\mathscr TF(1)=F'(1)+(b-1)F(1)+F(0).
\tag{GER5.2}
\]
They follow by differentiating the numerator and dividing by \(P'(0)=-1\), \(P'(1)=1\). At an original trivial zero \(z=-2r\),
\[
\mathscr TF(z)=
\frac{F(z)-8F_*(z)((1-z)F(0)+zF(1))}{z(z-1)},
\tag{GER5.3}
\]
where \(F_*(z)\) has the full nonzero Gamma/zeta value (GER1.6). Continuity and preservation of \(I_\zeta\) follow either from (GER5.1) or the two successive proved divisions.

On representatives the full source correction is
\[
s(s-1)\mathscr TF=
F-8F_*((1-s)F(0)+sF(1)),\qquad
\mathscr T(s(s-1)F)=F.
\tag{GER5.4}
\]
Let \(\mathscr t=\mathscr s_0\mathscr s_1\). Under Mellin inversion this says
\[
D(D-1)\mathscr tk
=k-\mathcal E\left[8F_k(0)f_*
+8(F_k(1)-F_k(0))(-vf_*'(v))\right],
\]
\[
\mathscr t(D(D-1)k)=k.
\tag{GER5.5}
\]
The exact generator intertwining used here is \(D\mathcal Ef=\mathcal E(-vf')\), proved by differentiating the original series. The full derivative is
\[
-vf_*'(v)=(2\pi^3v^6-7\pi^2v^4+3\pi v^2)e^{-\pi v^2}.
\tag{GER5.6}
\]
It is even, vanishes at zero, and has integral \(\int f_*=0\) by integration by parts, so both correction terms belong to the original \(S\). Consequently
\[
\boxed{P(L)^{-1}=S_0S_1=S_1S_0=S_1-S_0}
\tag{GER5.7}
\]
on the complete actual \(Q\), with its continuous actual Schwartz return (GER4.5).

## GER6. Full arithmetic equivariance and its exact Schwartz correction

Retain \(W_ak(u)=a^{1/2}k(u/a)\) and its Mellin multiplier \(T_aF(s)=a^sF(s)\) for every \(a>0\). Their full representative commutator is
\[
\mathscr S_cT_aF-T_a\mathscr S_cF
=8F(c)F_*(s)\frac{a^s-a^c}{s-c}.
\tag{GER6.1}
\]
The quotient is entire, with value \(a^c\log a\) at \(s=c\). More precisely, with the oriented integral when \(\log a<0\),
\[
\frac{a^s-a^c}{s-c}
=\int_0^{\log a}e^{c(\log a-t)}e^{st}\,dt.
\tag{GER6.2}
\]
Thus this commutator has the explicit original Schwartz preimage
\[
r_{c,a,F}(v)=
8F(c)\int_0^{\log a}e^{c(\log a-t)}
f_*(ve^{-t})\,dt.
\tag{GER6.3}
\]
It is a finite-interval integral in \(S\): each dilation is even, has value zero at zero, and has integral \(e^t\int f_*=0\). Every Schwartz seminorm of the integrand is bounded on that interval by a fixed seminorm of \(f_*\), proving convergence in the Schwartz topology. Also
\[
W_{e^t}\mathcal Ef_*=\mathcal E(f_*(\,\cdot\,e^{-t})),
\]
by direct substitution, with the exact factor \(e^{t/2}\) in \(W_{e^t}\) cancelling the source \(u^{1/2}\) change. Taking Mellin transforms proves that (GER6.3) sums to exactly (GER6.1).

For \(\mathscr T=\mathscr S_1-\mathscr S_0\), the complete source correction is the difference
\[
r_{P,a,F}(v)=
8\int_0^{\log a}
\left(F(1)e^{\log a-t}-F(0)\right)f_*(ve^{-t})\,dt.
\tag{GER6.4}
\]
Thus every \(S_c\) and \(P(L)^{-1}\) commutes exactly with every \(W_a\) on \(Q\), with an explicit prequotient correction in the actual \(\mathcal ES\). This includes all primes and all prime powers; no restricted height or finite set has replaced the arithmetic action.

## GER7. Every primary jet, original multiplicity, and support label

For the actual local algebra \(A_\rho=\mathbb C[T_\rho]/(T_\rho^{m_\rho})\), Taylor division gives
\[
j_\rho S_c=
M_{\displaystyle\sum_{r=0}^{m_\rho-1}
\frac{(-1)^rT_\rho^r}{(\rho-c)^{r+1}}}\,j_\rho,
\tag{GER7.1}
\]
\[
j_\rho P(L)^{-1}=
M_{\displaystyle\sum_{r=0}^{m_\rho-1}(-1)^r
\left((\rho-1)^{-r-1}-\rho^{-r-1}\right)T_\rho^r}\,j_\rho.
\tag{GER7.2}
\]
The denominators are nonzero because no original nontrivial zero is 0 or 1. Multiplication by \((\rho-c)+T_\rho\) telescopes in (GER7.1) to one modulo \(T_\rho^{m_\rho}\); the difference of the two identities gives (GER7.2), which is the complete inverse of
\((\rho+T_\rho)(\rho-1+T_\rho)\). Every multiplicity and every surviving nilpotent term remains.

For the original support lattice \(L_{\rm supp}\), write it with the subscript here only to distinguish it from the already named generator \(L\), not to replace its labels. The actual receiving functor is
\[
G_{L_{\rm supp}}(V)=
\{(0,\lambda):\lambda\in L_{\rm supp}\}
\cup\{(v,1_{L_{\rm supp}}):v\in V\},
\quad G(f)(v,\lambda)=(f(v),\lambda).
\tag{GER7.3}
\]
Every linear identity just proved lifts by this formula; substitution proves preservation of the receiving joins, meets, addition, and scalar action already specified in CW7/OMS7. In particular
\[
G(S_c)G(L-c)=G(L-c)G(S_c)=\mathrm{id},\qquad
G(P(L)^{-1})G(P(L))=\mathrm{id}.
\tag{GER7.4}
\]
Every \((0,\lambda)\) remains its own labelled zero under each map. This is not a tensor operation that collapses the zero labels, and it does not add an operation on primitive tau.

The full-domain propagation is now explicit: endpoint division and \(P(L)\)-division are continuous actual inverses on the original \(Q\), their changes of representative and arithmetic covariance errors have original Schwartz preimages, and their full jet actions preserve every original zero and multiplicity. The calculation does not delete the original function's trivial zeros or pole: their contribution appears in the retained multiplier and endpoint corrections above. It supplies an inverse in this nontrivial-zero quotient, with precisely this domain and codomain.
