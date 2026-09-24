# The actual Mellin quotient: synthesis, image topology, and source return

24 September 2026. OMS0–OMS8. This receives the existing global synthesis, exact Schwartz image, and original-zeta projectors into CW's actual quotient. It does not claim those earlier theorems as new discoveries. The division argument, continuous inverse, and comparisons required here are proved with all original factors.

## OMS0. Sources and operation prerequisites

The complete user arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2, and USR-6152e3bc6302258c were reread in the preserved corpus together with CORPUS_AND_OPERATION_RULES.md. Arithmetic, all primes, the original zeta function, and the complex receiving field below are the already reconstructed global objects. No operation counts primitive tau, assigns it parity, or introduces addition on tau. The notation remains \(Z_0,Z_1,Z_2,\tau\); a receiving supported zero \(z_\lambda\) is not identified with primitive tau.

Human source: Ralf Meyer, [A spectral interpretation for the zeros of the Riemann zeta function, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3). Original author source sources/Meyer_0412277v3/Meyer.tex, SHA256 ab9bc31f3c105a64fdc6f3b65ad16701dd8bf218fc90df98fe8d7f3c7c58c00e. Lines 225–738 were read, including the function spaces, the Zeta operator, Poisson summation, the closed-image theorem the:Zeta_estimate, and the exact Fourier–Laplace range theorem the:Lap_range. His theorem requires two rapid-division conditions; this note proves them from full zero-jet vanishing instead of attributing that unproved inference to his statement.

Programme sources read: GLOBAL_MELLIN_SYNTHESIS.md S1–S7; GLOBAL_MELLIN_SYNTHESIS_REVIEW.md R1–R5; EXACT_SCHWARTZ_SUMMATION_IMAGE.md SSI0–SSI10; CC_W_MELLIN_INDEPENDENT.md CW0–CW7; and the actual representative/projector construction RZ1–RZ8 in sources/programme/cc_sheaf/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md under quantum_tau_programme_bridge_20260924. The longer independent image check was consulted through its strip calculation; no complete new reading of that check is claimed. The S/SSI synthesis and RZ projectors are retained prior programme results, not newly discovered here. Their complete proofs are supplied locally; this statement is not an external-publication receipt.

S2 credits Jacques Hadamard's factorization theorem and records its original-TeX presentation in Alain Connes, [The Riemann Hypothesis: Past, Present and a Letter Through Time, arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), rhready.tex lines 526–535. That source reading is inherited from S2, not claimed as a new reading of either complete paper. The particular product estimate needed here is proved below.

## OMS1. Original spaces and exact comparison to Meyer

Let
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C): f(-v)=f(v),\
f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\},
\]
\[
\mathcal A=\{k\in C^\infty(\mathbb R_{>0}):
p_{N,j}(k)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jk(u)|<\infty
\quad(N,j\ge0)\},
\]
\[
\mathcal E f(u)=u^{1/2}\sum_{n\ge1}f(nu),\quad
I_A=\overline{\mathcal ES}^{\,\mathcal A},\quad Q=\mathcal A/I_A,
\quad F_k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{OMS1.1}
\]
The original action is \(W_a k(u)=a^{1/2}k(u/a)\), \(a>0\).
Write \(\mathcal B\) for the entire functions with all seminorms
\[
b_{A,M}(F)=\sup_{|\sigma|\le A,t\in\mathbb R}
(1+|t|)^M|F(\sigma+it)|<\infty.
\tag{OMS1.2}
\]
Integer indices suffice.

The Mellin map \(\mathcal M:\mathcal A\to\mathcal B\), \(\mathcal Mk=F_k\), is a topological isomorphism. For \(K(x)=k(e^x)\), its source seminorms are equivalent to \(\sup_x e^{N|x|}|K^{(j)}(x)|\). The integral is \(\int K(x)e^{(s-1/2)x}dx\). Stronger exponential seminorms justify every derivative in \(s\); repeated integration by parts proves uniform rapid decrease on every vertical strip. The exact inverse is
\[
K(x)=\frac1{2\pi}\int_{\mathbb R}F(1/2+it)e^{-itx}dt
=\frac{e^{-(c-1/2)x}}{2\pi}
\int_{\mathbb R}F(c+it)e^{-itx}dt .
\tag{OMS1.3}
\]
Contour shifting proves the second expression for every real \(c\), since horizontal sides tend uniformly to zero. For \(x\ge0\) choose \(c=1/2+N+1\); for \(x\le0\) choose \(c=1/2-N-1\). Differentiation inserts \((-(c-1/2+it))^j\), and an integrable bound with \(M>j+1\) proves each inverse seminorm estimate. Fourier inversion and the identity theorem prove the inverse identities. Completeness of the smooth weighted uniform topology shows that both spaces are Fréchet.

Meyer's source is \(\mathcal H_-=\bigcap_{\sigma\in\mathbb R}\mathcal S(\mathbb R_{>0}^{\times})_\sigma\), his operator is \(Zf(u)=\sum_{n\ge1}f(nu)\), and his action is \(\lambda_a b(u)=b(u/a)\). The exact topological comparison and every factor are
\[
T_0k(u)=u^{-1/2}k(u),\quad T_0^{-1}b(u)=u^{1/2}b(u),
\quad T_0\mathcal E=Z,\quad T_0W_a=\lambda_aT_0,
\]
\[
\widehat{T_0k}(s)=\int_0^\infty T_0k(u)u^s\frac{du}{u}=F_k(s).
\tag{OMS1.4}
\]
To check the spaces and topology, derivatives in \(x=\log u\) of the displayed exponential multiple are finite sums of weighted derivatives of \(K\). Every polynomial in \(x\) is bounded by a larger exponential, and weights \(e^{\pm(N+1)x}\) bound \(e^{N|x|}\). These inequalities prove continuity in both directions. Substitution proves all intertwining identities.

For the raw two-sign convention in SSI,
\[
\Sigma f(u)=2\sum_{n\ge1}f(nu)=2T_0\mathcal Ef(u),\qquad
\mathcal M_0\Sigma f=2F_{\mathcal Ef}.
\tag{OMS1.5}
\]
Meyer's Fourier phase \(e^{2\pi ivt}\) equals the phase \(e^{-2\pi ivt}\) on these even functions by \(v\mapsto-v\). These comparisons retain the half-power, the sign convention, and the factor two.

## OMS2. The exact ideal and its global division estimate

Let \(\mathcal Z\) be the distinct actual nontrivial zeros of the original \(\zeta\), with actual multiplicity \(m_\rho\), and set
\[
I_\zeta=\{F\in\mathcal B:F^{(r)}(\rho)=0
\quad(\rho\in\mathcal Z,\ 0\le r<m_\rho)\}.
\tag{OMS2.1}
\]
This is closed by Cauchy's evaluation estimate on fixed small circles.
Absolute summation on \(\Re s>1\) gives the original identity
\[
F_{\mathcal Ef}(s)=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}.
\tag{OMS2.2}
\]
The second factor is holomorphic for \(\Re s>-2\), because \(f(v)=O(v^2)\) at zero, and vanishes at \(s=1\). Continuation proves \(\mathcal M\mathcal ES\subset I_\zeta\), with every multiplicity retained.

Keep the actual source vector and all its factors:
\[
f_*(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\quad
k_*=\mathcal Ef_*,\quad
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{OMS2.3}
\]
Here \(f_*(0)=0\), and Gaussian moments give
\[
\int f_*=\frac\pi2\left(2\pi\frac3{4\pi^2}-3\frac1{2\pi}\right)=0.
\]
The direct Mellin integral before Gamma recurrence is
\[
\frac\pi2\left[
2\pi\frac12\pi^{-(s+4)/2}\Gamma((s+4)/2)
-3\frac12\pi^{-(s+2)/2}\Gamma((s+2)/2)\right].
\tag{OMS2.4}
\]
It yields exactly the multiplier in (OMS2.3).
Fourier differentiation of the Gaussian gives
\(\widehat{v^2e^{-\pi v^2}}=(1/(2\pi)-t^2)e^{-\pi t^2}\) and
\(\widehat{v^4e^{-\pi v^2}}=(t^4-3t^2/\pi+3/(4\pi^2))e^{-\pi t^2}\).
Thus \(\widehat f_*=f_*\). Poisson summation proves \(k_*(u)=k_*(1/u)\).
Gaussian decay at infinity and that reflection prove \(k_*\in\mathcal A\), and hence \(F_*\in\mathcal B\).
The exceptional values are
\[
F_*(0)=F_*(1)=\frac18,\quad
F_*(-2r)=F_*(1+2r)=
\frac{(1+2r)2r}{8}\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{OMS2.5}
\]
The pole at 1 and reflection give these values. Gamma has no zeros, so the zeros of \(F_*\) are exactly \(\mathcal Z\) with multiplicities. This auxiliary transform is used with its entire multiplier, not as a working replacement for \(\zeta\).

Gaussian summation gives \(|k_*(u)|\le Cu^B e^{-cu^2}\) for \(u\ge1\). Consequently
\[
\max_{|s|\le R}|F_*(s)|
\le2C\int_1^\infty u^{B+R+1/2}e^{-cu^2}\frac{du}{u}
\le e^{C_1(R+2)\log(R+2)}.
\tag{OMS2.6}
\]
The Gamma integral after \(y=cu^2\), or splitting its exponential tail beyond a constant multiple of \(R+2\), proves the final estimate. Jensen at radius \(2R\), using \(F_*(0)=1/8\), gives \(n(R)\le C_2(R+2)^{3/2}\), with multiplicities. Hadamard's theorem then gives
\[
F_*(s)=e^{a+bs}\prod_\rho(1-s/\rho)e^{s/\rho},
\quad e^a=\frac18,\quad
b=F_*'(0)/F_*(0)=\frac12\log(4\pi)-1-\frac{\gamma}{2}.
\tag{OMS2.7}
\]
Every repeated zero and every genus-one exponential remains in the product.

For \(F\in I_\zeta\), \(G=F/F_*\) is entire by local Taylor division. We prove
\[
\sup_{|\sigma|\le A}|G(\sigma+it)|
\le C_{A,F}\exp\{C(|t|+2)^{3/2}\log(|t|+2)\}.
\tag{OMS2.8}
\]
At large radius \(R\), surround each zero \(|\rho|\le8R\) by an open disk of radius \(R^{-2}\). The total radii are \(O(R^{-1/2})\). Every connected component has diameter below one for large \(R\), since a simple chain of intersecting disks joining two points has diameter at most twice their total radii. Outside these disks and for \(R/2\le|s|\le3R\), each finite factor satisfies \(|1-s/\rho|\ge(8R^3)^{-1}\). Their logarithms sum to at least \(-CR^{3/2}\log R\).
Dyadic summation of \(n(R)\) gives
\[
\sum_{|\rho|\le8R}|\rho|^{-1}=O(R^{1/2}),\qquad
\sum_{|\rho|>8R}|\rho|^{-2}=O(R^{-1/2}).
\]
The finite exponential factors therefore contribute at least \(-CR^{3/2}\). In the tail \(|w|=|s/\rho|\le3/8\), and
\[
\log|(1-w)e^w|
=\Re(-\sum_{j\ge2}w^j/j)\ge-\tfrac85|w|^2.
\]
The tail contributes at least \(-CR^{3/2}\); the leading exponential contributes at least \(-|a|-3|b|R\). Hence \(|F_*(s)|\ge e^{-CR^{3/2}\log R}\) outside the disks in that annulus.
For \(R\le|s|\le2R\) inside a component with \(|\Re s|\le A\), the entire component boundary lies within \(|\Re z|\le A+1\), inside the larger annulus, and outside the open disk union. The boundary quotient is bounded by the last estimate and \(b_{A+1,0}(F)\). The maximum principle for the entire quotient gives the same bound inside. Applying this at dyadic radii and bounding the remaining compact set proves (OMS2.8), including all zero clusters and multiplicities.

## OMS3. Rapid division, exact source inverse, and endpoints

Set \(H(s)=F(s)/\zeta(s)\). The only possible poles are simple poles at \(-2r\), with
\[
\operatorname{Res}_{s=-2r}H(s)=c_r(F)=\frac{F(-2r)}{\zeta'(-2r)},\quad
\zeta'(-2r)=(-1)^r2^{-2r-1}\pi^{-2r}(2r)!\zeta(1+2r).
\tag{OMS3.1}
\]
The complete functional multiplier is
\[
\zeta(s)=\chi(s)\zeta(1-s),\quad
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{OMS3.2}
\]
Its simple sine zero proves (OMS3.1). At the endpoints,
\[
H(0)=-2F(0),\quad H(1)=0,\quad H'(1)=F(1).
\tag{OMS3.3}
\]
Also
\[
H(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\,G(s).
\tag{OMS3.4}
\]
For any bounded real strip and \(|t|\ge1\), choose an integer \(L\) making \(\sigma/2+L\ge1\). Gamma recurrence and its Euler integral give
\[
|\Gamma(s/2)|\le
\frac{\Gamma(\sigma/2+L)}{\prod_{j=0}^{L-1}|s/2+j|}
\le C_{A,L}(2/|t|)^L.
\]
Together with (OMS2.8) this proves subquadratic logarithmic growth of \(H\) and of each polynomial times \(H\) on those strip parts.

Choose \(N\ge0\), \(a=-2N-1\), \(b\ge2\). The reciprocal Euler series gives
\[
|\zeta(b+it)^{-1}|\le\sum_{n\ge1}|\mu(n)|n^{-b}\le\zeta(b).
\tag{OMS3.5}
\]
On the left edge, writing \(y=t/2\), Gamma recurrence and reflection give
\[
|\chi(a+it)|^2=
\pi^{-4N-3}y\coth(\pi y)
\prod_{k=1}^{N}(k^2+y^2)
\prod_{j=0}^{N}((j+\tfrac12)^2+y^2).
\tag{OMS3.6}
\]
The first product is one at \(N=0\); the continuous value of \(y\coth(\pi y)\) at zero is \(1/\pi\). Indeed recurrence reduces the Gamma ratio to
\[
\frac{|\Gamma(1-iy)|^2}{|\Gamma(1/2+iy)|^2}
=\frac{\pi y/\sinh(\pi y)}{\pi/\cosh(\pi y)}.
\]
Each quadratic factor is at least \((1+|t|)^2/8\), and \(y\coth(\pi y)\ge(1+|t|)/(2\pi)\). Applying (OMS3.5) at real part \(1-a=2N+2\) yields
\[
|\zeta(a+it)^{-1}|\le
\zeta(2N+2)\sqrt{2\,8^{2N+1}}\pi^{2N+2}
(1+|t|)^{-2N-3/2}.
\tag{OMS3.7}
\]
Thus \(H\) decreases rapidly on both vertical edges, with continuous bounds in finitely many seminorms of \(F\).

Put \(P_N(s)=\prod_{r=1}^N(s+2r)\), \(P_0=1\), and \(\kappa=2N+2\). The function
\(V(s)=(s+\kappa)^M P_N(s)H(s)\) is holomorphic on the closed strip; every possible pole there has been cancelled explicitly. Its vertical-edge bound is \(C b_{A_0,M+N}(F)\), for \(A_0\ge\max(2N+1,b)\). Apply the maximum principle to \(e^{\varepsilon s^2}V(s)\) on rectangles of height \(\pm T\). Their horizontal bound is a polynomial times
\(\exp[-\varepsilon T^2+C(T+2)^{3/2}\log(T+2)]\), which tends to zero. Their vertical bound is multiplied by at most \(e^{\varepsilon\max(a^2,b^2)}\). First let \(T\to\infty\), then \(\varepsilon\downarrow0\), with the evaluation point fixed. Since \(|s+\kappa|\ge(1+|t|)/\sqrt2\), this proves
\[
\sup_{a\le\sigma\le b,t\in\mathbb R}
(1+|t|)^M|P_N(\sigma+it)H(\sigma+it)|
\le C_{N,b,M}b_{A_0,M+N}(F).
\tag{OMS3.8}
\]
The \(F\)-dependent growth constant was used only to eliminate horizontal edges and does not enter this final linear seminorm bound. Away from the finitely many trivial poles this proves rapid bounds for \(H\); Cauchy's formula on slightly larger strips supplies every derivative bound.

Now define, for \(v>0\),
\[
f_F(v)=\frac1{2\pi}\int_{\mathbb R}H(2+it)v^{-2-it}dt.
\tag{OMS3.9}
\]
Moving to any line \(c\ge2\) and differentiating gives
\[
f_F^{(j)}(v)=\frac{(-1)^j}{2\pi}
\int_{\mathbb R}(c+it)_jH(c+it)v^{-c-it-j}dt,
\quad(s)_j=s(s+1)\cdots(s+j-1).
\tag{OMS3.10}
\]
Arbitrary \(c\) proves rapid decrease of every derivative at infinity. Moving instead to \(a=-2N-1\) crosses exactly the original trivial-zero poles:
\[
f_F(v)=\sum_{r=1}^{N}c_r(F)v^{2r}
+\frac1{2\pi}\int_{\mathbb R}H(a+it)v^{-a-it}dt.
\tag{OMS3.11}
\]
The \(j\)-th derivative of the remainder is bounded for \(0<v\le1\) by
\[
\frac{v^{2N+1-j}}{2\pi}\int_{\mathbb R}|(a+it)_jH(a+it)|dt.
\]
Choose \(N\) with \(2N+1>j\). All derivatives extend continuously with the indicated polynomial limits. The fundamental theorem of calculus for consecutive derivatives verifies smoothness of the extension. Its even extension to \(\mathbb R\) is Schwartz and obeys
\[
f_F(0)=0,\quad f_F^{(2r-1)}(0)=0,\quad
\frac{f_F^{(2r)}(0)}{(2r)!}=\frac{F(-2r)}{\zeta'(-2r)}.
\tag{OMS3.12}
\]
Fourier inversion at \(\Re s=2\), and then the identity theorem, prove
\[
\int_0^\infty f_F(v)v^s\frac{dv}{v}=H(s)\quad(\Re s>-2).
\tag{OMS3.13}
\]
At \(s=1\), this gives \(\int_{\mathbb R}f_F=2H(1)=0\). Thus \(f_F\in S\), and (OMS2.2) gives \(\mathcal M\mathcal Ef_F=F\).

Each Schwartz seminorm is bounded continuously by finitely many seminorms of \(F\): use (OMS3.10) on \(|v|\ge1\), and (OMS3.11) with \(N\) large on \(|v|\le1\). Its finitely many residues are bounded by the corresponding evaluations of \(F\). Injectivity follows from (OMS2.2) on \(\Re s>1\), where \(\zeta\ne0\), and Fourier uniqueness. Therefore
\[
\boxed{\mathcal M\mathcal E:S\xrightarrow{\sim}I_\zeta
\text{ topologically},\qquad
I_A=\mathcal ES=\mathcal M^{-1}I_\zeta.}
\tag{OMS3.14}
\]
The retained endpoint moments are
\[
\int_0^\infty f_F(v)\frac{dv}{v}=-2F(0),\qquad
\int_0^\infty f_F(v)\log v\,dv=F(1).
\tag{OMS3.15}
\]
They follow from (OMS3.3) and (OMS3.13). The complete higher local coefficients are the Laurent division coefficients of the original \(F/\zeta\); no Gamma cancellation has erased them.

## OMS4. Meyer's full criterion and the counting inverse

The estimate proves that \(F/\zeta\), after removable extension, is Schwartz on every line \(\sigma\ge1/2\). Apply the same proof to \(F^\sharp(s)=F(1-s)\). The full functional equation preserves every nontrivial-zero multiplicity, so \(F^\sharp\in I_\zeta\). For \(\sigma\le1/2\) put \(w=1-\sigma-it\). Then
\[
\frac{F(\sigma+it)}{\zeta(1-\sigma-it)}
=\frac{F^\sharp(w)}{\zeta(w)}
\tag{OMS4.1}
\]
is Schwartz too. These are exactly both conditions in Meyer's original range theorem. Conversely their pole removability forces all corresponding zero multiplicities to divide \(F\). The overlap \(\sigma=1/2\) retains both conditions.

If \(b=T_0k\) and \(F=\widehat b\in I_\zeta\), the exact inverse is also
\[
f_F(v)=\sum_{n\ge1}\mu(n)b(nv)\quad(v>0).
\tag{OMS4.2}
\]
Indeed \(b=Zf_F\). For fixed \(v>0\), the double sum after this substitution is bounded by \(C_{v,L}\sum_{n,m\ge1}(mn)^{-L}<\infty\), \(L>1\). Rearrangement gives \(\sum_k f_F(kv)\sum_{n\mid k}\mu(n)=f_F(v)\); the finite divisor sum is one at \(k=1\) and zero otherwise by \(\prod_{p\mid k}(1-1)\). This uses the entire already reconstructed prime system. Derivatives converge locally for \(v>0\); the endpoint extension is (OMS3.11), not an unjustified termwise endpoint limit.

For any even Schwartz source the complete Poisson identity remains
\[
\frac{f(0)}2+Zf(u)=u^{-1}Z\widehat f(u^{-1})
+\frac{\widehat f(0)}{2u}.
\tag{OMS4.3}
\]
Only the two stated defining conditions of \(S\) remove these two terms in this sector. Their endpoint characters \(1,a\) remain in Meyer's larger source extension. In particular neither \(F(0)\), \(F(1)\), nor \(F(-2r)\) has been set to zero by the synthesis theorem.

## OMS5. Exact global jet image and its topology

Put \(A_\rho=\mathbb C[T_\rho]/(T_\rho^{m_\rho})\) and
\[
j_\rho([k])=\sum_{r=0}^{m_\rho-1}
\frac{F_k^{(r)}(\rho)}{r!}T_\rho^r,\quad
J:Q\longrightarrow\prod_{\rho\in\mathcal Z}A_\rho.
\tag{OMS5.1}
\]
By (OMS3.14),
\[
\boxed{\ker J=0.}
\tag{OMS5.2}
\]
Every representative invisible to all full original zero jets belongs to the actual Schwartz summation image. Thus the common jet kernel previously left unspecified in QS/CW is calculated, not merely renamed.

The exact image is
\[
\mathscr J=\{(F(\rho+T_\rho)\bmod T_\rho^{m_\rho})_\rho:F\in\mathcal B\}.
\tag{OMS5.3}
\]
The exact quotient relations are
\[
Q\xrightarrow{[k]\mapsto[F_k]}\mathcal B/I_\zeta
\xrightarrow{[F]\mapsto(F(\rho+T_\rho))_\rho}\mathscr J.
\tag{OMS5.4}
\]
Both arrows are isomorphisms when \(\mathscr J\) has the transported quotient topology
\[
\bar b_{A,M}(JF)=\inf_{G\in I_\zeta}b_{A,M}(F+G).
\tag{OMS5.5}
\]
These seminorms define the quotient topology because the strip seminorms form a directed family. Completeness follows, for example, by lifting the successive differences of a quotient-Cauchy subsequence with its \(j\)-th difference bounded by \(2^{-j}\) in \(b_{j,j}\), summing in the complete \(\mathcal B\), and using closedness of \(I_\zeta\).

For every fixed \(r,M\), Cauchy's formula on radius-\(1/2\) circles proves
\[
\sup_{\rho:m_\rho>r}(1+|\Im\rho|)^M
\left|\frac{F^{(r)}(\rho)}{r!}\right|
\le C_{r,M}b_{2,M}(F).
\tag{OMS5.6}
\]
All circles lie in \(|\Re s|\le2\), since \(0<\Re\rho<1\); their imaginary weights differ by a bounded factor. No zero-spacing condition occurs.
The product tuple having constant coordinate one at every zero therefore is not in \(\mathscr J\), since zero heights are unbounded. This classical fact is quantitatively supplied by the original-source zero-count theorem cited in CW3. Every finite tuple is realized by OMS6 below. Hence \(\mathscr J\) is a proper dense subspace of the product in its product topology.

The topology (OMS5.5) is strictly stronger than that inherited from the product. Were they equal, completeness would make \(\mathscr J\) closed in the product: a net in its closure has a Cauchy net of approximants, which completeness makes converge in the subspace. This contradicts the proved proper dense image. Thus the actual \(Q\) has not been replaced by arbitrary zero sequences or by coordinatewise convergence.

If \(\pi:Q\to V\) is a linear quotient through which every original full \(j_\rho\) factors, then \(\ker\pi\subset\ker J=0\), so it is an isomorphism of vector spaces. This is an exact receiving statement about observation-preserving quotients. It is not an assertion that every quotient of the full tau geometry has already been mapped to this receiver, and it is not a bound on \(\Re\rho\).

## OMS6. Existing RZ primary sections, with their exact receiving action

This is the previously established RZ5–RZ8 construction, now entered into (OMS5.4), not a new discovery. Fix \(\rho\), let \(m=m_\rho\), and set
\[
U_\rho(s)=F_*(s)/(s-\rho)^m,\qquad
u_r=U_\rho^{(r)}(\rho)/r!,\quad u_0\ne0,
\]
\[
c_0=u_0^{-1},\qquad
c_n=-u_0^{-1}\sum_{r=1}^n u_r c_{n-r}\quad(1\le n<m).
\tag{OMS6.1}
\]
The entire \(U_\rho\) belongs to \(\mathcal B\): outside a compact neighborhood of \(\rho\) division by the fixed polynomial preserves rapid decay; inside, the Taylor-removable quotient is bounded. Let \(c_\rho(T)=\sum_{r<m}c_rT^r\). For \(P\in A_\rho\), define
\[
\mathcal R_\rho(P)(s)=U_\rho(s)
[P(T)c_\rho(T)]_{<m}\big|_{T=s-\rho},\quad
s_\rho(P)=[\mathcal M^{-1}\mathcal R_\rho(P)]\in Q.
\tag{OMS6.2}
\]
The bracket means the unique polynomial representative of degree below \(m\); its finite multiplication occurs only in the specified complex algebra. The inverse Mellin is (OMS1.3), so these are actual test representatives with every seminorm finite.
The reciprocal recursion gives full jet \(P\) at \(\rho\); at every other zero, \(U_\rho\) retains its original full vanishing order. Thus
\[
j_\eta s_\rho=\delta_{\eta\rho}\mathrm{id},\qquad
\Pi_\rho=s_\rho j_\rho,\quad
\Pi_\rho^2=\Pi_\rho,\quad\Pi_\rho\Pi_\eta=0\ (\rho\ne\eta).
\tag{OMS6.3}
\]
Continuity follows from finite jet evaluation and the finite-dimensional section domain. Summing finitely many sections proves the finite surjectivity used in OMS5. No convergence of the infinite sum of projectors is asserted.

All multiplier derivatives are still available exactly. With \(C(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/8\),
\[
u_r=\sum_{h=0}^r
\frac{C^{(h)}(\rho)}{h!}
\frac{\zeta^{(m+r-h)}(\rho)}{(m+r-h)!},
\]
\[
C^{(h)}(s)=\frac{\pi^{-s/2}}8
\sum_{\substack{a+b+c=h\\0\le a\le2}}
\frac{h!}{a!b!c!}(s(s-1))^{(a)}
\left(-\frac{\log\pi}{2}\right)^b2^{-c}\Gamma^{(c)}(s/2).
\tag{OMS6.4}
\]
Every Gamma, pi, endpoint, and original-zeta derivative is retained.

Substitution in (OMS1.1) gives \(F_{W_ak}(s)=a^sF_k(s)\), and hence
\[
j_\rho W_a=
M_{a^\rho\exp((\log a)T_\rho)}j_\rho.
\]
The two sides of the following equality have equal full jets at every zero; (OMS5.2) therefore proves
\[
\boxed{W_as_\rho(P)=
s_\rho\left(a^\rho\sum_{r=0}^{m_\rho-1}
\frac{(\log a)^rT_\rho^r}{r!}\,P\right)\quad(a>0).}
\tag{OMS6.5}
\]
These are actual invariant primary subspaces of \(Q\), of dimension \(m_\rho\). The original nilpotent order and all prime/prime-power actions remain. The section is into \(Q\); its test representative in \(\mathcal A\) need not be equivariant before quotienting. Its covariance error lies in the actual image \(\mathcal ES\) by synthesis. This gives the exact return to earlier test-space section obstructions.

## OMS7. CW propagation and every support label

CW's original Gaussian and coefficient map still give
\[
B(s)=\sqrt\pi\,e^{(s-1/2)^2/4},\quad
F_{K_b[x]}(s)=B(s)(\log x)^s,\quad x>1,
\]
\[
j_\rho\overline K_b[x]=B(\rho+T_\rho)(\log x)^\rho
\sum_{r<m_\rho}\frac{(\log\log x)^rT_\rho^r}{r!},
\]
\[
B(\rho+T_\rho)=\sqrt\pi e^{(\rho-1/2)^2/4}
e^{(\rho-1/2)T_\rho/2+T_\rho^2/4}.
\tag{OMS7.1}
\]
All finite nilpotent terms are retained. Equality of these full joint observations is now proved to be equality in the actual \(Q\), with no residual invisible class. This does not enlarge CW's finite coefficient domain to arbitrary infinite tuples. MQ's moving-frequency and finite-valuation-frame domains remain their own proved domains; synthesis alone does not extend them across an unproved geometric boundary.

For the original bounded distributive support lattice \(L\), use the actual CW7 receiver
\[
G_L(V)=\{(0,\lambda):\lambda\in L\}\cup\{(v,1_L):v\in V\}.
\]
For a linear map \(f\), the lift is
\[
G_L(f)(v,\lambda)=(f(v),\lambda).
\tag{OMS7.2}
\]
A non-top input forces \(v=0\), so it is well-defined. Linearity proves that it preserves the already specified receiving addition
\((v,\lambda)+(w,\mu)=(v+w,\lambda\vee\mu)\) and scalar action
\((c,\nu)(v,\lambda)=(cv,\nu\wedge\lambda)\). These are not operations on primitive tau. Applying (OMS7.2) to the two inverse maps in (OMS5.4) proves
\[
G_L(Q)\xrightarrow{\sim}G_L(\mathscr J),
\tag{OMS7.3}
\]
with every \((0,\lambda)\) retained separately. The primary maps, prime actions, and finite diagrams likewise keep that same label. Products here carry a common label; independent block labels would define a different object.
Ordinary tensoring does not prove this zero-label statement: \(0\otimes e_\lambda=0\) for every \(\lambda\). Equations (OMS7.2)–(OMS7.3) provide the exact supported-zero repair rather than a tensor assertion that erases those fibres.

## OMS7A. Return to the complete adelic periodization complex

The earlier AC1–AC4 use the same even Schwartz space with both endpoint conditions:
\[
H_{00}=S=\{h\in\mathcal S_{\rm even}(\mathbb R):h(0)=0,\ \int_{\mathbb R}h=0\}.
\]
The map \(\Phi:Q_0\to H_{00}\) there is onto: the class
\([t_1\otimes h]\) has image \(h\). Its periodization is the original
\(J=2\mathcal E\Phi\). Consequently, as subspaces of the same strong
space \(\mathcal A\),
\[
I_0=J(Q_0)=2\mathcal ES=\mathcal ES=\overline{\mathcal ES}.
\tag{OMS7A.1}
\]
The equality of subspaces uses the invertible receiving scalar 2;
it does not replace the map \(J\) by \(\mathcal E\). Its inverse still has
the exact factor
\[
h_k(x)=\frac1{4\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
\frac{F_k(s)}{\zeta(s)}x^{-s}\,ds,\qquad \sigma>1.
\]
The endpoint conditions, trivial-zero residues and continuity of this
inverse follow from OMS3–OMS4 with this factor retained.

Thus AC4's defined closure-difference space and comparison are now determined:
\[
D_{\rm cl}=\overline{I_0}/I_0=0,\qquad
C_{\rm alg}=\mathcal A/I_0\longrightarrow Q=\mathcal A/\overline{I_0},
\quad[k]_{I_0}\longmapsto[k]_{\overline{I_0}}.
\tag{OMS7A.2}
\]
The inverse sends the same representative back. The two quotient topologies
are identical, since their quotient maps have the same domain and kernel.
All dilations commute with both maps.

For the full two-term complex after degree-zero adelic coinvariants,
\(C=[Q_0\xrightarrow{J}\mathcal A]\) in degrees \(-1,0\), AC2's explicit
split coordinates give the cochain isomorphism
\[
C\cong\mathcal B_{\rm pr}[1]\oplus[I_0\hookrightarrow\mathcal A],
\qquad c\longmapsto(\beta(c),Jc).
\]
Its inverse in degree \(-1\) is
\((b,k)\mapsto j(b)+[t_1\otimes h_k]\). Hence
\[
H^{-1}(C)=\mathcal B_{\rm pr},\qquad H^0(C)=Q.
\tag{OMS7A.3}
\]
The cochain map to \(\mathcal B_{\rm pr}[1]\oplus Q[0]\), given by
\(\beta\) and the original quotient, induces these identities and is
an equivariant quasi-isomorphism in the stated algebraic representation
category. No unspecified topology on \(Q_0\) is used for a derived equivalence.
The specific two-extension
\[
0\to\mathcal B_{\rm pr}\to Q_0\xrightarrow{J}\mathcal A\to Q\to0
\tag{OMS7A.4}
\]
has zero class: it is the Yoneda splice of the split sequence
\(0\to\mathcal B_{\rm pr}\to Q_0\to I_0\to0\) with
\(0\to I_0\to\mathcal A\to Q\to0\). The explicit section above
makes the first class zero, so its Yoneda product is zero. This does not
assert vanishing of the entire group \(\operatorname{Ext}^2(Q,\mathcal B_{\rm pr})\),
or a section of \(\mathcal A\to Q\).

Every endpoint and prime label remains:
\[
\mathcal B_{\rm pr}=\left(\bigoplus_p\mathbb C\ell_p\right)\otimes\mathbb C^2,
\qquad W_a|_{\mathcal B_{\rm pr}}=
\operatorname{id}\otimes\begin{pmatrix}1&0\\0&a\end{pmatrix}.
\]
AC4's higher derived-coinvariant groups are not terms of this two-term
complex and are unchanged by (OMS7A.1). The result removes the earlier
closure uncertainty on the actual adelic coefficient complex; it does
not identify that complex with the entire geometric specialization.
The original adelic construction retains the Connes and
Connes–Consani–Marcolli attribution and exact ABR proof dependencies
listed in AC0. This propagation was independently checked against
the full definitions in AC0–AC4 and OMS1–OMS5.

## OMS8. The calculated global conclusion

The result on the original domain is
\[
\boxed{\mathcal ES=\overline{\mathcal ES}
=\{k\in\mathcal A:F_k^{(r)}(\rho)=0
\quad\text{for all actual }\rho,\ 0\le r<m_\rho\}.}
\tag{OMS8.1}
\]
The proof constructs the actual continuous source inverse, proves both Meyer half-plane conditions, and recovers every endpoint moment and trivial-zero Taylor coefficient. The quotient has zero common full-jet kernel, the exact image topology (OMS5.5), and the retained original RZ primary sections with all nilpotents and prime actions. These are consequences for the actual original arithmetic receiver after the full-spectrum reconstruction.

No conclusion about \(|p^\rho|=p^{1/2}\) was inserted. The calculation retains each actual \(\rho\), rather than moving it or deleting it. Its contribution to the geometric programme is that a constructed map into this \(Q\) can now be checked on its complete original spectral data without an unknown common jet kernel; its construction and any Deligne weight estimate remain distinct mathematical calculations.
