# Faithful regularized Hardy coefficients on the full original source dual

Independent mathematical derivation, 25 September 2026. Proof locators **NHJ0–NHJ9**. This extends NHD7–NHD9 by proving injectivity before taking the original quotient, and constructs the exact Hilbert domain and its surviving boundary correction. No remote publication is performed by this note.

## NHJ0. Construction stage, sources, and the question actually attempted

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every scalar, function, Hilbert space and quotient below belongs to the coefficient system after complete-history arithmetic reconstruction. No parity, coordinate, arithmetic value, midpoint, metric or addition is assigned to that support. Separate reconstructed branch counters are not pooled. The current correction chains were read, including the complete source passages for the retracted addition, the complete-history prerequisite and the separately quotiented branches. The later instruction to search for underclaims governs the extension proved here.

The complete incoming mathematical proofs NHR0–NHR9, NAD0–NAD8, NHD0–NHD10, ADM0–ADM9 and GSP0–GSP9 were read. GAP's original seminorm estimate, exact half-Mellin comparison and Gaussian source convergence were read and used below. The source-use receipt accompanying this file records exact hashes and coverage; receipt extraction is not being called source reading.

Human provenance is S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, [arXiv:1809.09577v4](https://arxiv.org/abs/1809.09577v4), [DOI 10.1016/j.aim.2019.04.064](https://doi.org/10.1016/j.aim.2019.04.064). The indexed original-author TeX, canonical unit PUBUNIT-803463A3EF787AE3E69C519B, was read through source line 387, covering the introduction and §§1–5. Its SHA256 is `bc3075483547782dce36bf55a6349899a26766fcfc8ae9f265079ec74601f2d3`. This is the source already byte-compared with the versioned archive in NHR's receipt. Noor's underlying cited books and earlier articles were not newly read here.

The incoming NHD receiver was continuous into disk-holomorphic functions but did not determine its kernel. The next calculation asks whether its complete coefficient sequence recovers the entire original continuous functional. NHJ3–NHJ4 prove that it does, even on the prequotient source dual. NHJ5–NHJ8 then construct and study the exact Hilbert domain; they do not assume that a holomorphic receiver automatically has finite Hardy norm.

## NHJ1. Full original objects and the coefficient tests

Retain
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty
\text{ for every integer }A,N\ge0\}.
\tag{NHJ1.1}
\]
It has these original Fréchet seminorms. The original arithmetic source and its exact comparison are
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j a(u)|<\infty
\text{ for every }N,j\ge0\},
\]
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+iy)u^{-iy}\,dy.
\tag{NHJ1.2}
\]
These are the proved inverse topological maps of the source; neither factor is changed here.

Let \(\mathcal I\) impose all vanishing jets at every actual nontrivial zero \(\rho\) of the original \(\zeta\), through order \(m_\rho-1\), and let \(Q=\mathcal B/\mathcal I\). The full original source element is
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)\in\mathcal I,
\quad F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)\ne0
\quad(k\ge1).
\tag{NHJ1.3}
\]
The original pole, trivial-zero contributions and Gamma factors remain part of this full expression. They are not replaced by a different zeta function. At each nontrivial zero its full germ is
\[
F_0(\rho+v)=v^{m_\rho}
\frac{(\rho+v)(\rho+v-1)}8\pi^{-(\rho+v)/2}
\Gamma((\rho+v)/2)\frac{\zeta(\rho+v)}{v^{m_\rho}}.
\tag{NHJ1.4}
\]
Every jet below uses all derivatives of this product where needed.

Fix \(t>0\), and write \(g_t(s)=e^{ts^2}\). Define, exactly as NHD7,
\[
\phi_0(s)=-\frac1s,\qquad
\phi_m(s)=\frac{m^{1-s}-(m+1)^{1-s}}s\quad(m\ge1),
\]
\[
\psi_m(s)=\phi_m(s)+\frac{8F_0(s)}s,
\qquad F_{t,m}=g_t\psi_m.
\tag{NHJ1.5}
\]
All powers of positive integers use their real logarithms. Each numerator at \(s=0\) is \(-1+8F_0(0)=0\), so each \(\psi_m\) is entire. Division at this point means the removable holomorphic value. For every fixed strip, the elementary numerator estimate outside a unit disk, and the maximum principle for the entire divided function inside that disk, give
\[
\sup_{|\Re s|\le A}|\psi_m(s)|\le C_A(m+1)^{A+3},
\quad
b_{A,N}(F_{t,m})\le C_{A,N,t}(m+1)^{A+3}.
\tag{NHJ1.6}
\]
For the inner disk, use the radius-two boundary and the bound with real width \(\max(A,2)\); the displayed exponent \(A+3\) suffices also when \(A<2\). The Gaussian supplies the rapid vertical decay. Thus every \(F_{t,m}\) is an actual member of \(\mathcal B\).

## NHJ2. A continuous receiver already on the prequotient strong dual

For \(\Lambda\in\mathcal B'_\beta\) put
\[
\mathcal H_t^{\mathcal B}\Lambda(z)
=\sum_{m=0}^\infty\overline{\Lambda(F_{t,m})}\,z^m,
\qquad |z|<1.
\tag{NHJ2.1}
\]
It is conjugate-linear in \(\Lambda\). Continuity of \(\Lambda\) bounds it by one of the directed seminorms in NHJ1.1, so NHJ1.6 bounds the coefficients by a finite power of \(m+1\). This proves compact-open convergence of the power series.

For every \(r<1\), the series
\[
K_{t,z}=\sum_{m\ge0}F_{t,m}\bar z^m\qquad(|z|\le r)
\tag{NHJ2.2}
\]
converges in every source seminorm, uniformly on that closed disk. Its values form a bounded subset of \(\mathcal B\), and
\[
\sup_{|z|\le r}|\mathcal H_t^{\mathcal B}\Lambda(z)|
=\sup_{|z|\le r}|\Lambda(K_{t,z})|.
\tag{NHJ2.3}
\]
The right side is a defining strong-dual seminorm. Consequently
\(\mathcal H_t^{\mathcal B}:\mathcal B'_\beta\to\mathcal O(\mathbb D)\)
is continuous, where the target has its compact-open topology.

The transpose of the original quotient embeds \(Q'_\beta\) in \(\mathcal B'_\beta\) as \(\mathcal I^\perp\); continuity follows directly since quotient maps take bounded sets to bounded sets. Restricting NHJ2.1 gives NHD8's \(\mathcal H_t\). No Hilbert boundary norm has yet been asserted.

## NHJ3. All integer return times force injectivity of the coefficient observation

Suppose \(\mathcal H_t^{\mathcal B}\Lambda=0\). Define the actual entire source test, depending on \(w\in\mathbb C\),
\[
X_{t,w}(s)=g_t(s)
\frac{e^{(1-s)w}-8e^wF_0(s)}s,
\qquad L(w)=\Lambda(X_{t,w}).
\tag{NHJ3.1}
\]
The numerator vanishes at \(s=0\) for every \(w\), with the exact factor eight. The family is holomorphic in \(w\) as a \(\mathcal B\)-valued function. Here are the estimates needed for that assertion and for its growth.

Write \(s=x+iy\), \(w=a+ib\). Outside \(|s|<1\), the first numerator term satisfies
\[
(1+|y|)^N|g_t(s)e^{(1-s)w}|
\le e^{tA^2+(1+A)|a|}(1+|y|)^N e^{-ty^2+|b||y|}
\tag{NHJ3.2}
\]
on \(|x|\le A\). Completing the displayed quadratic, or shifting its maximum, bounds its supremum by
\(C_{N,t}(1+|b|)^N e^{b^2/(4t)}\).
The second term is bounded by \(8e^{|a|}b_{A,N}(g_tF_0)\). Inside the unit disk, apply the maximum principle to the entire quotient on the circle \(|s|=2\), with the full numerator and its factor \(g_t\); this gives a bound of the form \(C_{t,N}e^{3|a|+2|b|}\). Combining them, for suitable finite constants depending on the indicated source seminorm,
\[
b_{A,N}(X_{t,w})\le C_{A,N,t}(1+|w|)^N
\exp\{C_{A,t}|w|+|w|^2/(4t)\}.
\tag{NHJ3.3}
\]
Uniform versions hold for every fixed number of \(w\)-derivatives on compact parameter sets: differentiating adds powers of \(1-s\), controlled by increasing \(N\) before Gaussian domination. Local Taylor remainders obey the same estimates. This proves source-valued holomorphy, not only pointwise holomorphy. Thus \(L\) is entire and has a bound \(|L(w)|\le C\exp(C(1+|w|^2))\).

The exact finite telescoping identity, including the first coefficient, is
\[
\sum_{m=0}^{n-1}\psi_m(s)
=\frac{-n^{1-s}+8nF_0(s)}s,
\qquad X_{t,\log n}=-\sum_{m=0}^{n-1}F_{t,m}
\quad(n\ge1).
\tag{NHJ3.4}
\]
Every coefficient of NHJ2.1 is zero, so \(L(\log n)=0\) for every positive integer \(n\).

These are too many zeros for a nonzero entire function with the proved growth. For completeness, if \(L\ne0\), divide off its finite zero order at zero to obtain an entire \(V\) with \(V(0)\ne0\) and the same quadratic exponential upper bound at large radius. Jensen's formula at radius \(2R\), with a harmless slightly larger radius when a zero is on its boundary, gives
\[
\#\{w:V(w)=0,\ |w|\le R\}\log2
\le \log\max_{|w|\le2R+1}|V(w)|-\log|V(0)|
\le C_1(1+R^2).
\tag{NHJ3.5}
\]
Zeros are counted with multiplicity. But the distinct points \(\log n\), \(2\le n\le e^R\), supply at least \(\lfloor e^R\rfloor-1\) zeros in that disk, contradicting NHJ3.5 for large \(R\). Hence \(L\equiv0\).

Differentiate the full source formula before any quotient. The endpoint correction cancels exactly:
\[
(\partial_w-1)X_{t,w}(s)
=-g_t(s)e^{(1-s)w}.
\tag{NHJ3.6}
\]
Both sides are entire in \(s\), including its removable point zero. Applying \(\Lambda\) gives
\[
\boxed{\Lambda(g_t e^{vs})=0\quad\text{for every }v\in\mathbb C.}
\tag{NHJ3.7}
\]
No assumption that \(\Lambda\) annihilates \(\mathcal I\) has occurred in this proof.

## NHJ4. The full source integral and removal of regularization

Take arbitrary \(F\in\mathcal B\). For \(u>t\), let
\(H=e^{(u-t)s^2}F\in\mathcal B\), and let \(a_H=\Theta^{-1}H\in A\), using the exact source comparison NHJ1.2. After the change of variable \(v=\log x\), the original half-Mellin formula says
\[
H(s)=\frac12\int_{\mathbb R}a_H(e^v)e^{sv}\,dv.
\tag{NHJ4.1}
\]
This also proves, in the complete source topology,
\[
e^{us^2}F(s)=g_t(s)H(s)
=\frac12\int_{\mathbb R}a_H(e^v)g_t(s)e^{sv}\,dv.
\tag{NHJ4.2}
\]
Indeed \(b_{A,N}(g_t e^{vs})\le C_{A,N,t}e^{A|v|}\) for real \(v\). The definition of \(A\) bounds \(|a_H(e^v)|\) by \(C_Me^{-M|v|}\) for every \(M\). Choosing \(M>A+1\) proves integrability in the specified seminorm. Differentiated integrals and finite-interval Riemann sums obey the same estimates. Therefore the complete locally convex integral exists in \(\mathcal B\), and the continuous functional \(\Lambda\) may pass through it. Equation NHJ3.7 then yields
\[
\Lambda(e^{us^2}F)=0\quad(u>t).
\tag{NHJ4.3}
\]

For this fixed \(F\), the scalar function
\(u\mapsto\Lambda(e^{us^2}F)\) is holomorphic on \(\Re u>0\). To check the source-valued assertion, write \(u=p+iq\). On a fixed strip,
\[
\Re(us^2)=p(x^2-y^2)-2qxy.
\tag{NHJ4.4}
\]
On each compact parameter set in that half-plane, \(p\) has a positive lower bound and \(|q|\) a finite upper bound. The right side is bounded by a fixed negative quadratic in \(y\) plus a constant. Every \(u\)-derivative adds \(s^{2j}\), still dominated in every source seminorm. Taylor remainders have uniform domination as well. This proves the required holomorphy. The identity theorem and NHJ4.3 give zero on the whole half-plane.

For real \(u\downarrow0\), the exact original estimate is
\[
b_{A,N}((e^{us^2}-1)F)
\le u e^{A^2}(A^2+1)b_{A,N+2}(F)
\quad(0<u\le1).
\tag{NHJ4.5}
\]
It follows by integrating \(s^2e^{vs^2}\) from zero to \(u\), retaining the displayed constants. Thus \(e^{us^2}F\to F\) in the original topology and \(\Lambda(F)=0\). Since \(F\) was arbitrary,
\[
\boxed{\ker\mathcal H_t^{\mathcal B}=0\quad(t>0).}
\tag{NHJ4.6}
\]

This proves more than injectivity on \(Q'\): it holds on the full original prequotient dual. The source tests themselves consequently satisfy
\[
\boxed{\overline{\operatorname{span}\{F_{t,m}:m\ge0\}}^{\mathcal B}
=\mathcal B.}
\tag{NHJ4.7}
\]
For otherwise Hahn–Banach separation of a proper closed subspace would give a nonzero continuous \(\Lambda\) annihilating every test, contradicting NHJ4.6. This is a proved global density statement. It assumes no interpolation bound, no spacing of zeros and no polynomial-density assertion.

The same proof works for any entire \(C\) of polynomial growth on every fixed vertical strip, with \(C(0)=1\), replacing \(8F_0\) by \(C\). Its polynomial strip degree is absorbed by the Gaussian in NHJ1.6 and NHJ3.3; the telescoping identity and differential cancellation are otherwise identical. In particular one may use \(C=F_*/F_*(0)\) for any \(F_*\in\mathcal B\) with nonzero value at zero. No zero-divisor hypothesis on that auxiliary \(C\) is required for density or injectivity. It would be required separately for a particular quotient's cover covariance.

The density and injectivity statements also hold for every complex \(t\) with \(\Re t>0\). To verify the altered estimates, write \(t=p+iq\); the Gaussian's logarithmic modulus on a fixed strip is \(p(x^2-y^2)-2qxy\). The negative quadratic term controls the added linear term exactly as in NHJ4.4, with constants depending on this fixed \(t\). Thus all source-valued families and Jensen's quadratic-growth bound remain valid. In NHJ4 use \(u=t+v\), \(v>0\), and \(H=e^{vs^2}F\), giving zeros of the holomorphic parameter function on a horizontal ray in \(\Re u>0\). Its identity theorem and the same positive-real limit at zero finish the proof. The programme receiver below remains the specific original \(C=8F_0\) and positive real \(t\); these extensions do not change its source factors or its actual adjoint conventions.

## NHJ5. The actual quotient and every retained zero jet

The exact restriction to \(Q'_\beta\) is injective by NHJ4.6. Let
\[
N_O=\{[F]\in Q:F(\rho)=0\text{ at every actual off-line zero}\},
\qquad \mathcal R=Q/N_O.
\tag{NHJ5.1}
\]
ADM1 and AST identify the actual strong transpose inclusion
\(\pi':\mathcal R'_\beta\hookrightarrow Q'_\beta\) with \(N_O^\perp\). Therefore
\[
\boxed{\mathcal H_t^{\mathcal R}:=\mathcal H_t\pi':
\mathcal R'_\beta\longrightarrow\mathcal O(\mathbb D)
\text{ is continuous, conjugate-linear and injective}.}
\tag{NHJ5.2}
\]
This conclusion uses the actual specialization quotient, not a newly selected positive quotient.

On \(Q'\), every original derivative is still retained. For
\(\varepsilon_{\rho,j}([F])=F^{(j)}(\rho)\), \(0\le j<m_\rho\), the complete coefficient is
\[
[z^m]\mathcal H_t\varepsilon_{\rho,j}
=\overline{\sum_{a=0}^j\binom ja
g_t^{(a)}(\rho)\phi_m^{(j-a)}(\rho)}.
\tag{NHJ5.3}
\]
The correction's derivatives vanish at \(\rho\) only because its complete zero order is \(m_\rho\), with \(\rho\ne0\). No derivative is removed from the input. For a right-off-line \(\rho\), this is exactly
\[
\mathcal H_t\varepsilon_{\rho,j}
=\sum_{a=0}^j\binom ja\overline{g_t^{(a)}(\rho)}g_{\rho,j-a},
\tag{NHJ5.4}
\]
with NHR's actual Hardy jet functions. The full coefficient matrix has diagonal \(\overline{e^{t\rho^2}}\) and retains all lower orders. On \(\mathcal R'\) the higher jets have already been excluded by its specified annihilator: they remain present in \(Q'\), while \(N_O\) contains positive-order off-line jets and every line jet. The receiver does not perform that quotient again.

NHJ5.2 does not assert inverse continuity for the image's compact-open topology. Its exact inverse is on the image with the topology transported from \(\mathcal R'_\beta\). A stronger inverse statement would require its own estimate.

## NHJ6. The exact maximal Hilbert domain and a complete graph

Define a subspace of the original prequotient dual by the explicit convergent-series condition
\[
\mathfrak D_t^{\mathcal B}=
\left\{\Lambda\in\mathcal B'_\beta:
\sum_{m=0}^\infty|\Lambda(F_{t,m})|^2<\infty\right\}.
\tag{NHJ6.1}
\]
This is precisely the full domain on which NHJ2.1 has target \(H^2\). No unexamined Hardy regularity is inserted. Its conjugate-linear operator
\(C_t^{\mathcal B}:\mathfrak D_t^{\mathcal B}\to H^2\)
has zero kernel and closed graph in \(\mathcal B'_\beta\times H^2\). Indeed a convergent graph net has coefficient limits on the source side by continuity of each evaluation, and on the target side by continuity of every Hardy coefficient. Equality of all coefficients gives exactly NHJ6.1 and its image identity at the limit.

Give the domain its graph topology, with seminorms
\[
\Lambda\longmapsto
\sup_{F\in K}|\Lambda(F)|+
\left(\sum_{m\ge0}|\Lambda(F_{t,m})|^2\right)^{1/2},
\qquad K\subset\mathcal B\text{ bounded}.
\tag{NHJ6.2}
\]
It is complete. To check the source completeness used here, a strong Cauchy net in \(\mathcal B'\) has a pointwise linear limit and converges uniformly on every bounded subset. On every convergent source sequence together with its limit, a compact hence bounded set, that limit is a uniform limit of continuous functions. It is sequentially continuous; metrizability of \(\mathcal B\) makes it continuous. Thus \(\mathcal B'_\beta\) is complete. Its product with \(H^2\) is complete, and the graph is closed. No assertion that this strong-dual graph is Fréchet is needed.

The exact quotient domains are
\[
\mathfrak D_t^Q=\mathfrak D_t^{\mathcal B}\cap\mathcal I^\perp,
\quad
\mathfrak D_t^{\mathcal R}=
\{\lambda\in\mathcal R'_\beta:\pi'\lambda\in\mathfrak D_t^Q\}.
\tag{NHJ6.3}
\]
They carry the corresponding graph topologies and closed injective operators. On any of these domains the exact positive form, linear in its first argument, is
\[
B_t(\lambda,\mu)=\sum_{m\ge0}
\lambda([F_{t,m}])\overline{\mu([F_{t,m}])}
=\langle C_t\mu,C_t\lambda\rangle_{H^2}.
\tag{NHJ6.4}
\]
Use prequotient arguments instead of brackets for \(\mathcal B'\), and the specified transpose for \(\mathcal R'\). Cauchy–Schwarz proves convergence; injectivity proves that its radical is zero on its stated domain. This is not an assertion that the original reciprocal-zeta pairing equals this form or that the full original dual has this Hilbert domain.

## NHJ7. The exact prequotient boundary pole and the original cover degree

Retain \(U_nF(s)=n^{1-s}F(s)\), and Noor's raw cover
\(W_nf(z)=(1+\cdots+z^{n-1})f(z^n)\), for recovered integers \(n\ge1\). No rescaling is made. Its adjoint sums coefficient blocks. On disk-holomorphic functions the same formula defines the continuous map
\[
(\mathscr W_n^*f)_m=\sum_{a=0}^{n-1}f_{nm+a}.
\tag{NHJ7.1}
\]
Continuity follows from Cauchy's estimate: given \(r<1\), choose \(R\) with \(r^{1/n}<R<1\), so the output is bounded by
\(\frac{\sum_{a=0}^{n-1}R^{-a}}{1-rR^{-n}}\sup_{|z|\le R}|f(z)|\).

The complete representative discrepancy from coefficient telescoping is
\[
\sum_{a=0}^{n-1}F_{t,nm+a}-U_nF_{t,m}
=\delta_{n,t},\qquad
\delta_{n,t}(s)=8g_t(s)F_0(s)\frac{n-n^{1-s}}s.
\tag{NHJ7.2}
\]
The quotient in the last expression is entire with removable value \(n\log n\) at zero. It has polynomial growth on every vertical strip, so \(\delta_{n,t}\in\mathcal I\subset\mathcal B\). The original endpoint and every zero order remain in its full source representative.

Applying a prequotient functional to NHJ7.2 gives the exact holomorphic identity
\[
\boxed{\mathscr W_n^*\mathcal H_t^{\mathcal B}\Lambda
-\mathcal H_t^{\mathcal B}U_n'\Lambda
=\frac{\overline{\Lambda(\delta_{n,t})}}{1-z}.}
\tag{NHJ7.3}
\]
The coefficient on the right is independent of \(m\); its sign comes from the order of the difference in NHJ7.2. This retained source discrepancy is a literal Hardy-boundary pole. Since \(1/(1-z)\notin H^2\), for every \(\Lambda\in\mathfrak D_t^{\mathcal B}\) one obtains the exact domain statement
\[
\boxed{U_n'\Lambda\in\mathfrak D_t^{\mathcal B}
\iff\Lambda(\delta_{n,t})=0.}
\tag{NHJ7.4}
\]
Both directions follow by NHJ7.3 and boundedness of \(W_n^*\) on \(H^2\). On \(Q'\) and \(\mathcal R'\), the discrepancy is annihilated by their actual source quotient, so their exact Hilbert domains are invariant and
\[
C_t U_n'=W_n^*C_t,
\quad W_n^*W_n=nI,
\quad W_nW_n^*=nP_n.
\tag{NHJ7.5}
\]
Here \(P_n\) averages consecutive coefficient blocks of size \(n\); its complement is retained. It follows, for \(\lambda,\mu\) in either quotient Hilbert domain, that
\[
nB_t(\lambda,\mu)-B_t(U_n'\lambda,U_n'\mu)
=n\langle(I-P_n)C_t\mu,(I-P_n)C_t\lambda\rangle.
\tag{NHJ7.6}
\]
Indeed substitute NHJ7.5 in NHJ6.4 and use the self-adjoint projection \(P_n\). On the diagonal this is a nonnegative squared norm with the full factor \(n\). There is no assertion that this defect vanishes, or that \(W_n^*\) has a global inverse. The inverse source action \(T_n'=n(U_n')^{-1}\) remains the actual arithmetic action; invariance under its inverse on an arbitrary Hilbert-domain vector has not been assumed.

## NHJ8. The regularized finite-jet graph is always closable, with an exact zero kernel

Let \(E_+\) be the finite span of the full right-off-line zero derivative functionals in NHR7, and let \(D_+\) be its closure in \(Q'_\beta\). NHD1 identifies it as the annihilator of all source classes with zero full jets on that branch, retaining the other source branches in \(Q'\). Consider
\[
R_t:E_+\to H^2,\qquad R_t\lambda=\mathcal H_t\lambda
=R(m_{g_t}'\lambda),
\tag{NHJ8.1}
\]
where \(R\) denotes only NHR's conjugate-linear finite-jet receiver. The equality is the full Leibniz formula NHJ5.4, not a value-only substitution.

The graph of \(R_t\) in \(D_+\times H^2\) has a closure with no nonzero vertical part. If \(\lambda_i\to0\) strongly and \(R_t\lambda_i\to y\) in \(H^2\), source-to-analytic continuity gives \(R_t\lambda_i\to0\) in \(\mathcal O(\mathbb D)\), while Hardy convergence gives analytic convergence to \(y\). Therefore \(y=0\). More generally its closure is a subgraph of NHJ6's closed operator, and that operator is injective. Thus \(R_t\) has a closed injective extension \(\overline R_t\) on the exactly specified domain
\[
\mathfrak D_{t,\mathrm{fin}}^+=
\left\{\lambda\in D_+:\exists\text{ a net }\lambda_i\in E_+,
\lambda_i\to\lambda\text{ strongly},
\mathcal H_t\lambda_i\to\mathcal H_t\lambda\text{ in }H^2\right\}.
\tag{NHJ8.2}
\]
Its image is contained in \(\mathcal N^\perp\), since each finite image is, and that Hardy subspace is closed. The domain contains \(E_+\), hence is strongly dense in \(D_+\). Equality with the larger \(D_+\cap\mathfrak D_t^Q\) is not required or asserted. This keeps the exact closure and maximal-Hilbert domains distinct.

The graph is invariant under the actual pair \((U_n',W_n^*)\): apply this continuous pair to an approximating net in NHJ8.2 and use NHR7's finite intertwining. It retains all nilpotent coefficients at every finite block and the full closed graph limit.

Noor's unconditional theorem now yields a statement about the actual source domain with no hidden receiving kernel:
\[
\boxed{\{\lambda\in\mathfrak D_{t,\mathrm{fin}}^+:
\overline R_t\lambda\in\operatorname{dom}\bigl(((I-S)^{-1})^*\bigr)\}=\{0\}.}
\tag{NHJ8.3}
\]
The notation means the adjoint of the inverse of \(I-S\), on its actual dense domain. To prove NHJ8.3, Noor gives
\(\mathcal N^\perp\cap\operatorname{dom}( (I-S)^{-1})^*=\{0\}\), so the received vector is zero; NHJ4.6 then gives \(\lambda=0\). This removes the possible source kernel left in the general unregularized relation NHD5.5, without assuming that every source vector has the required adjoint regularity.

NAD gives an explicit arithmetic test for that final regularity. For \(y=\Phi a\), \(a\in\ell^2_\omega\), with \(\omega_m=1/[m(m+1)]\), it is exactly existence of \(\ell\in\mathbb C\) such that
\[
\sum_{m=1}^\infty\left|
m\sum_{r=m}^\infty\frac{a(r)}{r(r+1)}-\ell\right|^2<\infty.
\tag{NHJ8.4}
\]
The full adjoint-output norm is \(|\ell|^2\) plus this sum. No factor, boundary scalar or weighting is discarded. For the full finite nonzero right-zero jet span, NHR6 and NAD7 prove failure of this condition, with the explicit power-log tail retained. NHJ8.3 is a statement on the constructed infinite graph domain, not an inference that finite domain failure automatically settles infinite combinations.

## NHJ9. What advanced, what was attempted next, and the remaining original target

The all-coefficient uniqueness question is answered globally: the original Gaussian-corrected integer tests are dense in the complete original test space, and their observation injects its entire strong dual, hence both \(Q'_\beta\) and the actual specialization dual \(\mathcal R'_\beta\), into holomorphic functions on the disk. The proof retains the complete original factor and obtains uniqueness from all integer return times, followed by the exact original half-Mellin integral. It does not initialize arithmetic from a finite named set of primes.

The immediate next question was whether this faithful analytic observation supplies the positive receiver needed by the actual source. NHJ6 attempted that next step by constructing the exact coefficient-square-summability domain, proving its closed graph, completeness and zero radical. NHJ7 then calculated the full source cover discrepancy and showed that its failure to preserve the prequotient Hilbert domain is exactly the displayed boundary pole. Passing through the already existing original quotient kills that specific pole, with every representative term retained in the comparison. The remaining unilateral degree defect is NHJ7.6, not an assumed adjoint equality.

NHJ8 further proves closability and injectivity for every positive Gaussian parameter on the complete right-jet graph. Noor's actual regularity theorem is now faithfully pulled back to that source domain. This makes the remaining step a concrete source-regularity or geometric-transfer calculation on a known injective map; no receiving kernel can conceal a nonzero source class there.

The original target is still the vanishing of the actual \(\tau\)-supported lifting obstruction by a derived geometric weight separation. Nothing here proves that all members of \(\mathcal R'\) have finite Hardy norm, that they lie in Noor's adjoint domain, that NHJ7.6 vanishes, or that this positive form is the original Weil/residue pairing. The corresponding next calculation is to apply the faithful receiver to the *actual* boundary map with its factor \(d_r(\rho)\), because that factor may control the near-critical-line Hardy norm. That independent actual-boundary calculation is being carried out by the parent task; it is not assumed in any proof above.
