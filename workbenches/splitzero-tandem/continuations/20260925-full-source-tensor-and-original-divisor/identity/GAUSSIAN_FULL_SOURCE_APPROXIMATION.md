# Gaussian approximation on the complete original source and its actual defect

25 September 2026. Complete derivation, **GAP0–GAP9**.

## GAP0. The construction and the question being attempted

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Arithmetic, analytic coordinates, vector spaces and parameters below belong to the complete recovered coefficient system, after the global arithmetic comparison. They are not operations on this support. The separate branch counters remain separate. Addition at \(\tau\), an assigned metric there, and a midpoint expression for it are not used.

ECR1 constructs proper injective maps in both directions between the full original quotient and the cyclic original extension-class module. Their composites are Gaussian multiplication, not identity. AST2–AST6 construct the actual specialization quotient and its continuous transpose. The next question is whether those Gaussian composites recover identity in the original source topology and how the whole extension-class trace behaves in the same limit. This note proves those statements. No topology on an unspecified Ext group and no inverse Gaussian multiplier is presumed.

Inputs are the complete ECR0–ECR7 and ECI0–ECI13 proofs, GMS1–GMS3 and GMS9, AST1–AST6, and SDT's source topology. These are programme derivations. The human coefficient construction remains Connes–Consani, *Schemes over* \(\mathbb F_1\) *and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), as reconstructed with the retained author source in the earlier chapters. Deligne's invariant-cycle weight argument is the distinct cross reconstructed in DC0–DC12; none of its arithmetic purity hypotheses is inserted here. The local reading ledger specifies source versions and coverage.

Use the entire-function space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{A,N}(F):=\sup_{|x|\le A,\,y\in\mathbb R}
(1+|y|)^N|F(x+iy)|<\infty\quad(A,N\ge0)\}.
\tag{GAP0.1}
\]
Integer \(A,N\) give its Fréchet topology. Let \(M\) be the ring of entire functions of at most polynomial growth on each closed vertical strip; its exponent may depend on the strip. The ideal \(\mathfrak a\subset M\) imposes vanishing to the full multiplicity \(m_\rho\) at every actual nontrivial zero \(\rho\) of the original \(\zeta\). Set
\[
\mathcal I=\mathcal B\cap\mathfrak a,\qquad
Q=\mathcal B/\mathcal I,\qquad
\mathscr C=M/\mathfrak a=M e_0.
\tag{GAP0.2}
\]
The closed subspaces in AST are
\[
N_O=\ker(P_OE:Q\to H_O),\quad N_0=\ker E,
\quad\mathcal R=Q/N_O.
\tag{GAP0.3}
\]
All quotient topologies here are the original Fréchet quotient topologies. In particular no value norm replaces the topology of \(Q\) or \(\mathcal R\).

## GAP1. A full strip estimate and its quotient consequence

For \(0<t\le1\) put \(g_t(s)=e^{ts^2}\). Write \(s=x+iy\). For \(|x|\le A\),
\[
|g_t(s)|=e^{t(x^2-y^2)}\le e^{A^2},\qquad
g_t(s)-1=\int_0^t s^2e^{us^2}\,du.
\tag{GAP1.1}
\]
Consequently
\[
|g_t(s)-1|\le t e^{A^2}(A^2+y^2)
\le t e^{A^2}(A^2+1)(1+|y|)^2,
\]
\[
\boxed{b_{A,N}((g_t-1)F)
\le t e^{A^2}(A^2+1)b_{A,N+2}(F).}
\tag{GAP1.2}
\]
These estimates prove continuity of multiplication and convergence \(m_{g_t}\to1\) uniformly on every bounded subset of \(\mathcal B\), in every defining seminorm. They also prove that the set
\[
\{t^{-1}(g_t-1)F:0<t\le1,\ F\in K\}
\tag{GAP1.3}
\]
is bounded whenever \(K\subset\mathcal B\) is bounded.

Every ideal defined by full vanishing jets is invariant under these multipliers, and every value kernel in (GAP0.3) is invariant as well. For an invariant closed subspace \(L\subset\mathcal B\), let
\(\bar b_{A,N}([F])=\inf_{H\in L}b_{A,N}(F+H)\).
For each representative \(F+H\), the left side of (GAP1.2), with its quotient seminorm, bounds the same quotient element. Taking the infimum over \(H\) proves
\[
\bar b_{A,N}((m_{g_t}-1)[F])
\le t e^{A^2}(A^2+1)\bar b_{A,N+2}([F]).
\tag{GAP1.4}
\]
These seminorms generate the quotient topology: the original family is directed, so an image of a finite intersection of seminorm balls contains an image of one such ball. Applying this to \(L=\mathcal I\), to the inverse images of \(N_O,N_0\), and restricting to invariant closed subspaces proves the same bounded convergence on \(Q,\mathcal R,N_O,N_0\) and their specified subquotients. For a subspace followed by a quotient, use the restricted seminorms and then the same infimum argument. No continuous linear section is required.

## GAP2. The generator, every multiplicity, and the cyclic comparison

The exact semigroup identity is \(m_{g_t}m_{g_u}=m_{g_{t+u}}\). The second integral remainder gives
\[
g_t-1-ts^2=\int_0^t(t-u)s^4e^{us^2}\,du,
\]
\[
b_{A,N}((g_t-1-ts^2)F)
\le\frac{t^2}{2}e^{A^2}(A^2+1)^2b_{A,N+4}(F).
\tag{GAP2.1}
\]
Thus \(t^{-1}(m_{g_t}-1)\to m_{s^2}\) uniformly on bounded subsets of every space just listed, with its stated topology. Multiplication by \(s^2\) is itself continuous there by the same strip estimate.

At a zero of multiplicity \(m\), the entire local multiplier and all its Taylor coefficients are
\[
g_t(\rho+z)=e^{t\rho^2}e^{2t\rho z}e^{tz^2},\qquad
[z^k]g_t(\rho+z)=e^{t\rho^2}
\sum_{v=0}^{\lfloor k/2\rfloor}
\frac{(2t\rho)^{k-2v}t^v}{(k-2v)!v!}.
\tag{GAP2.2}
\]
The length-\(m\) jet matrix has these entries at position \((i,j)\) with \(k=i-j\ge0\), and zero for \(i<j\). Its determinant is \(e^{mt\rho^2}\). These are the full matrices of ECR2; only the passage to the actual length \(m\) truncates them. The convergence proved above is on the complete source, not an inference from separate convergence on finitely many jet matrices.

Retain the exact maps
\[
j:Q\hookrightarrow\mathscr C,\quad [F]\mapsto F e_0,
\qquad b_t:\mathscr C\hookrightarrow Q,\quad h e_0\mapsto[g_th].
\]
Their well-definedness and injectivity follow from full vanishing orders and the fact that \(g_t\) is a unit in each local holomorphic ring. Their exact composites are
\[
b_tj=m_{g_t}\text{ on }Q,\qquad jb_t=m_{g_t}\text{ on }\mathscr C.
\tag{GAP2.3}
\]
Equation (GAP1.4) now proves \(b_tj\to1_Q\) uniformly on bounded subsets of the actual source. There is no topology or convergence claim for \(jb_t\) on \(\mathscr C\), and no statement that either embedding is onto. The properness proofs in ECR1 remain valid.

## GAP3. The original half-Mellin source, with every factor

Retain
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for all }N,j\ge0\},
\]
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\quad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+iy)u^{-iy}\,dy.
\tag{GAP3.1}
\]
The complete source theorem proves these are continuous inverse maps \(A\leftrightarrow\mathcal B\). In ECR3 the inverse of \(g_t\) is
\[
a_{t,1}(u)=\frac{e^{t/4}}{\sqrt{\pi t}}u^{-1/2}
\exp\!\left(-\frac{(\log u-t)^2}{4t}\right).
\tag{GAP3.2}
\]
Define the following actual operator on \(A\):
\[
\boxed{
S_ta(u)=\frac{e^{t/4}}{2\sqrt{\pi t}}
\int_0^\infty (u/v)^{-1/2}
\exp\!\left(-\frac{(\log(u/v)-t)^2}{4t}\right)
a(v)\frac{dv}{v}.}
\tag{GAP3.3}
\]
Here the coefficient \(1/2\) is necessary. For multiplicative convolution
\((a*_Mb)(u)=\int a(u/v)b(v)dv/v\), absolute Fubini and \(u=wv\) give
\[
\Theta(a*_Mb)=2\Theta a\,\Theta b.
\tag{GAP3.4}
\]
Absolute Fubini is valid on every vertical line: \(a,b\in A\) have finite absolute moments of every real order, so the absolute double integral is the product of two such moments. The convolution is in \(A\). To verify this directly, move each logarithmic derivative onto the first factor and use
\((wv)^N+(wv)^{-N}\le(w^N+w^{-N})(v^N+v^{-N})\);
the remaining weighted integral of the second factor is finite, by its estimates with exponent \(N+1\) at both ends. Differentiation under the integral follows from the same bounds. Thus (GAP3.3), which is \(\tfrac12a_{t,1}*_Ma\), satisfies exactly
\[
\Theta S_t=m_{g_t}\Theta.
\tag{GAP3.5}
\]
It follows from (GAP1.2), (GAP2.1) and the continuous inverse that \(S_t\to1_A\) uniformly on bounded sets, \(S_tS_u=S_{t+u}\), and
\[
t^{-1}(S_t-1)\longrightarrow (u\partial_u)^2
\tag{GAP3.6}
\]
in that same operator topology. For the last identity, integration by parts gives \(\Theta(u\partial_u)a=-s\Theta a\), with both endpoint terms zero by the defining source estimates; applying it twice gives \(s^2\). All factors in the original formula (GAP3.3) remain. This is an approximation of test sources. It does not deform \(\zeta\), and it makes no claim about a different real-axis heat integral with an endpoint term.

The source subspace \(J\), defined in AST1 by Schwartz summation, has \(\Theta J=\mathcal I\). Thus \(S_t\) preserves \(J\) and \(A_O=q^{-1}N_O\), and induces the proved operators on \(Q=A/J\) and \(A/A_O=\mathcal R\).

## GAP4. The actual specialization map and its Hilbert receiver

Use precisely AST1's \(H=\ell^2(\mathscr Z,m)\), \(\rho^\#=1-\overline\rho\), and
\[
d_r(\rho)=e^{-i\Im\rho\log r}(r^{\Re\rho}-r^{1-\Re\rho}),
\quad(\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#),\quad r>1.
\tag{GAP4.1}
\]
Let \(G_t^\#\) be the diagonal operator with entry \(g_t(\rho^\#)\). Then
\[
\beta_rm_{g_t}=G_t^\#\beta_r,\qquad
b_rS_t=G_t^\# b_r,\qquad b_r=\beta_rq.
\tag{GAP4.2}
\]
The entry is reflected; it is not replaced by \(g_t(\rho)\) or its absolute value. Since \(0<\Re\rho^\#<1\), \(\|G_t^\#\|\le e^t\). For a fixed \(y\in H\), each coordinate of \((G_t^\#-1)y\) tends to zero and is bounded in modulus by \((e+1)|y_\rho|\). Summability with the original weights \(m_\rho\) proves strong convergence to identity on \(H\). It is uniform on compact subsets: a finite epsilon-net and the uniform operator bound reduce the assertion to the finitely many net points.

On the full \(H\) this is not convergence in operator norm. For each \(t>0\), the unbounded actual zero heights imply \(g_t(\rho^\#)\to0\) along a sequence, so \(\|G_t^\#-1\|\ge1\). This statement uses the full zero set and makes no assertion that off-line zeros exist or have unbounded heights.

For the common smooth domain
\[
H_\infty=\{y:p_N(y)^2=\sum_\rho m_\rho(1+|\Im\rho|)^{2N}|y_\rho|^2<\infty
\text{ for all }N\ge0\},
\tag{GAP4.3}
\]
the stronger estimate is
\[
p_N((G_t^\#-1)y)\le te\,p_{N+2}(y).
\tag{GAP4.4}
\]
Indeed \(|\rho^\#|^2\le1+|\Im\rho|^2\le(1+|\Im\rho|)^2\), and (GAP1.1) with \(A=1\) applies coordinatewise. The space \(H_\infty\) is complete: a sequence Cauchy in all \(p_N\) has compatible limits in the nested complete weighted Hilbert spaces, giving one coordinate vector in their intersection. Every weighted evaluation \(E_N:Q\to H\), \((E_NF)_\rho=(1+|\Im\rho|)^NF(\rho)\), is continuous by ECI5.2. Thus \(E\) and \(\beta_r\) have continuous range in \(H_\infty\). This supplies the domain needed in (GAP4.4) before it is used.

Consequently (GAP4.2) induces bounded-set convergence on the actual \(\mathcal R\) and its continuously injected specialization image with its transported source topology. It preserves the literal short exact sequence of complexes
\[
0\to[\underline{A_O}\xrightarrow0 iH]
\to[\underline A\xrightarrow{b_r}iH]
\to\underline{\mathcal R}[1]\to0.
\tag{GAP4.5}
\]
The two bracketed complexes occupy degrees \((-1,0)\). The maps are \(S_t\) on the displayed source spaces and \(G_t^\#\) on \(H\). All differentials commute by (GAP4.2). AST5's positive quotient and positive final cone projection still give connecting stalk map \(-\bar\beta_r\); its differentiate-a-lift SES convention gives \(+\bar\beta_r\). Neither sign changes in this approximation. This note does not identify the whole derived connecting morphism with just its stalk map.

## GAP5. Strong-dual convergence, with the actual bounded sets

Let \(X\) be any source, invariant subspace or quotient in GAP1 or GAP3, and let \(T_t\) denote its constructed Gaussian operator. Give \(X'\) the strong topology \(\beta(X',X)\), with seminorms \(p_K(\lambda)=\sup_{x\in K}|\lambda(x)|\) for bounded \(K\subset X\). For such \(K\), GAP1 proves that
\(D_K=\{t^{-1}(T_t-1)x:0<t\le1,x\in K\}\)
is bounded in \(X\). Hence
\[
p_K((T_t'-1)\lambda)\le t p_{D_K}(\lambda).
\tag{GAP5.1}
\]
If \(\Lambda\) is bounded in \(X'_\beta\), the right side is bounded by
\(t\sup_{\lambda\in\Lambda}p_{D_K}(\lambda)<\infty\).
This proves convergence uniformly on bounded subsets of the strong dual, not only weak convergence on individual tests. The same argument with the second remainder proves convergence of the dual difference quotient to the transpose of the full generator.

For example the exact transposed relation is
\[
m_{g_t}'\beta_r'=\beta_r'(G_t^\#)',
\qquad S_t'b_r'=b_r'(G_t^\#)'.
\tag{GAP5.2}
\]
No Hermitian conjugation is hidden in this continuous linear transpose. Under AST1's Riesz identification
\(R(\overline y)(h)=\sum m_\rho h_\rho\overline{y_\rho}\),
\((G_t^\#)'R(\overline y)=R(\overline{(G_t^\#)^*y})\),
where \(((G_t^\#)^*y)_\rho=\overline{g_t(\rho^\#)}y_\rho\).
These equations give the literal dual maps and their original multiplicity factors.

## GAP6. Every polynomial-growth class has a strong residue limit

Use ECI5's actual continuous functional
\[
\mathcal W_M(h)(F)=\sum_\rho m_\rho F(\rho)\overline{h(\rho^\#)},
\qquad h\in M,
\tag{GAP6.1}
\]
on \(Q\). It depends only on \(h\bmod\mathfrak a\); its additional kernel is the value-zero ideal modulo \(\mathfrak a\), not an assumed uniform nilradical. The complete full-jet residue receiver for this functional is the one constructed in ECI5–ECI6.

Fix \(h\), and choose \(C_h,d\) with \(|h(\rho^\#)|\le C_h w_\rho^d\), \(w_\rho=1+|\Im\rho|\). The established zero-count estimate gives \(C_0^2=\sum m_\rho w_\rho^{-4}<\infty\). For \(k\ge d+4\), (GAP1.1) and weighted Cauchy–Schwarz yield
\[
\begin{aligned}
|\mathcal W_M(g_th)(F)-\mathcal W_M(h)(F)|
&\le teC_h\sum_\rho m_\rho|F(\rho)|w_\rho^{d+2}\\
&\le teC_h C_0\|E_kF\|_H.
\end{aligned}
\tag{GAP6.2}
\]
The sum is absolutely convergent. The estimate is independent of a representative of \(F\) because it uses the continuous quotient map \(E_k\). Taking the supremum over an arbitrary bounded \(K\subset Q\) proves
\[
\boxed{\mathcal W_M(g_th)\longrightarrow\mathcal W_M(h)
\quad\text{in }Q'_\beta.}
\tag{GAP6.3}
\]
It also gives a uniform rate for any specified set of multipliers sharing the displayed \(C_h,d\). It assigns no topology to \(\mathscr C\).

In contrast, the source classes \(b_t(e_0)=[g_t]\) do not converge in \(Q\) as \(t\downarrow0\). If their limit were \([F]\), continuity of each value functional would give \(F(\rho)=1\) at every actual nontrivial zero. The strip estimate \(b_{1,1}(F)<\infty\) contradicts those values along the unbounded zero heights. Every class has a representative \(F\in\mathcal B\), so this proves nonconvergence. This does not contradict (GAP2.3): there the input lies in \(j(Q)\), whereas \(e_0\notin j(Q)\). It also does not contradict (GAP6.3), which is convergence in the explicitly different strong-dual receiver. No assertion about this sequence in the possibly zero off-line quotient \(\mathcal R\) is made.

## GAP7. Reflection, the normal coordinate and all four endpoints

Retain \(\mathsf K_1F(s)=\overline{F(1-\overline s)}\). Direct substitution gives
\[
g_t^{\#_1}(s)=e^{t(1-s)^2}=d_t(s)g_t(s),\qquad
d_t(s)=e^{t(1-2s)},\qquad d_t^{\#_1}=d_t^{-1}.
\tag{GAP7.1}
\]
Thus \(\mathsf K_1m_{g_t}=m_{d_t}m_{g_t}\mathsf K_1\) exactly at every positive \(t\). The full normal translation and transported reflection factors are
\[
(Vg_t)(\lambda)=e^{t(\lambda-1)^2},\qquad
(Vd_t)(\lambda)=e^{t(3-2\lambda)},\qquad
\mathsf K_3V=V\mathsf K_1.
\tag{GAP7.2}
\]
For a fixed strip,
\[
|d_t(s)-1|\le t e^{1+2A}(1+2A+2|y|)
\le t e^{1+2A}(3+2A)(1+|y|).
\tag{GAP7.3}
\]
This follows by integrating \((1-2s)e^{u(1-2s)}\) from zero to \(t\); its real exponential is bounded by \(e^{1+2A}\). The identical bound applies to \(d_t^{-1}-1\) using \(-(1-2s)\). Both factors therefore tend to identity uniformly on bounded sets of the spaces and strong duals already constructed. Their finite-\(t\) factors remain in the reflection identities; in particular ECI12's dual covariance uses \(m_{d_t^{-1}}'\), not \(m_{d_t}'\).

For the full simultaneous source of GMS9, the exact Gaussian action is
\[
\begin{aligned}
g_t(f,c_0,c_1)&=s_+(S_t\Sigma f)+(0,c_0,e^tc_1),\\
g_t(g,d_0,d_1)&=s_-(S_tR\Sigma g)+(0,e^td_0,d_1).
\end{aligned}
\tag{GAP7.4}
\]
Here \(s_\pm\), \(\Sigma\) and the source reflection \(R\) are the proved maps of that full source decomposition. Thus the four endpoint multipliers are exactly \((1,e^t,e^t,1)\). Continuity of the sections and restrictions, (GAP3.5), and convergence of these four scalars prove bounded-set convergence on that full source. In the separate degree-two normal term the same ring element acts by
\[
g_t(s+1)=e^{t(s+1)^2}.
\tag{GAP7.5}
\]
Apply GAP1 on the enlarged strip \(|\Re(s+1)|\le A+1\) to prove its convergence. This is not the transported original Gaussian \(Vg_t\) in (GAP7.2). Keeping those operations distinct retains GMS9's actual arithmetic degree factor.

## GAP8. The original zeta comparison is unchanged

The source factor remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\frac18,\quad
F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
\quad(k\ge1).
\tag{GAP8.1}
\]
At \(\rho\), the exact local unit multiplying \((s-\rho)^{m_\rho}\) is
\[
\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)
\frac{\zeta(s)}{(s-\rho)^{m_\rho}}.
\tag{GAP8.2}
\]
Every derivative of the regularized source is the full product derivative
\[
(g_tF_0)^{(j)}(s)=\sum_{v+k_0+k_1+k_2+k_3=j}
\frac{j!}{v!k_0!k_1!k_2!k_3!}g_t^{(v)}(s)
\left(\frac{s(s-1)}8\right)^{(k_0)}
\left(-\frac{\log\pi}2\right)^{k_1}\pi^{-s/2}
2^{-k_2}\Gamma^{(k_2)}(s/2)\zeta^{(k_3)}(s).
\tag{GAP8.3}
\]
At exceptional points evaluate the holomorphic full product, rather than the separately singular factors. Thus its endpoint values are \(1/8,e^t/8\), and its values at \(-2k\) are \(e^{4tk^2}\) times (GAP8.1). These are exact finite-point values, not a convergence assertion for an unrestricted infinite sum of trivial-zero contributions.

The original unit, prime repetitions, functional-equation factor and reflected Gaussian weight remain
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\quad
-\zeta'(s)/\zeta(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
\quad(\Re s>1),
\]
\[
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
\quad\zeta(s)=\chi(s)\zeta(1-s),
\]
\[
g_t(\rho)\overline{g_t(\rho^\#)}
=e^{t\{\rho^2+(1-\rho)^2\}}.
\tag{GAP8.4}
\]
The last expression is not substituted by the different positive value \(|g_t(\rho)|^2\). ECR4's original explicit formula, including its prime window, Gamma integral, endpoints and stated finite trivial-divisor cutoff, remains the arithmetic receiver. No new interchange with an infinite trivial-zero sum is used in GAP6.

## GAP9. The separator on the retained specialization source

Let \(c\in M\) be the complete GMS separator, so \(c-1\in\mathfrak a\), and \(c\) vanishes to all normal shifted-zero orders. Since multiplication commutes before every quotient,
\[
cm_{g_t}=m_{g_t}c,\quad c|_Q=1_Q,\quad c|_{\mathcal R}=1_{\mathcal R},
\quad\beta_rcm_{g_t}=\beta_rm_{g_t}.
\tag{GAP9.1}
\]
Taking the proved limit gives the same identity on the entire specialization source, not just on finitely many jets. On the actual target coordinates, \(c(\rho^\#)=1\), so it is identity there too. The different transported normal operator \(c(s+1)=1-E(s)\) instead belongs to \(\mathfrak a\), and its induced map on \(Q\) and \(\mathcal R\) is zero. Both statements preserve their exact domains and shifts.

This answers the attempted approximation question: the complete original source and its strong duals admit the stated Gaussian approximation; every polynomial-growth class has its canonical strong trace limit, even though its generator has no limit in the rapid source. The earlier separator retains the specialization image in this construction. The additional calculation needed to apply the full multiplier algebra to that same boundary is its common target domain and the actual normal-ideal-to-\(\mathcal R\) map; ADM constructs these directly. No vanishing or purity is inferred from a proper embedding, a change of topology, or the existence of the approximation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
