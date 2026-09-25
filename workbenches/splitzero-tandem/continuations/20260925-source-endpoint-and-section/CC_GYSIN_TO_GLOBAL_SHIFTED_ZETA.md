# The CC hyperplane class and the continuous global zeta lift

24 September 2026. Complete comparison proof; locators GTZ0–GTZ9.

## GTZ0. Prerequisites, notation, and the object being compared

The supporting datum remains \(\tau\langle Z_1;\text{no }Z_2\rangle\), in the user's notation. This note introduces no addition at \(\tau\), numerical coordinate on it, or identification with an integer. The complete arithmetic reconstruction precedes every integer, prime, complex scalar, function space, and cohomology group used below.

The full relevant user corrections were read in the private corpus, including the complete-history-before-unit argument, the rejection of a Gaussian-integer example as a competing foundation, and the instruction to quotient branches separately. The governing route is argument_reconstruction/CORPUS_AND_OPERATION_RULE.md. Those private source records are not part of a public mathematical edition.

The input arithmetic is the complete reconstructed arithmetic of CG0–CG8 and BQC0–BQC6. Its original Riemann zeta function is denoted \(\zeta\). We do not reconstruct it from two selected primes. The supplied Connes–Consani charts are evaluated after that input is present. Their Gaussian coefficient ring in CGT1 is this particular chart receiver, not an alternative origin for the arithmetic.

We compare two already constructed objects:

1. The continuous quotient of the full Mellin source constructed in GSL0–GSL11, retaining all actual nontrivial zeros and their multiplicities.
2. The cohomology of the actual complex CC twistor line with that quotient as constant coefficients. Its hyperplane class is geometrically constructed.

The resulting isomorphism is in continuous complex linear representations of the CC odd monoid. It is not asserted to be an isomorphism of algebras, a complex-to-\(\ell\)-adic coefficient identification, or a construction of the original coefficient space from the projective line alone. Those types will be visible in every map.

Source reading:

- Connes–Consani, [*The Absolute Twistor Line and the Geometry of the compactified Spec Z*](https://arxiv.org/html/2609.00299v1), arXiv:2609.00299v1.

  The original CC.tex was read especially for the chart restrictions, geometric involution, and Proposition “The odd arithmetic monoid acts on the twistor line,” lines1159–1195. The supplied file has SHA256 57a10dcef5cd758e6b2f1c54b1c0a11b0fb093638f74fb1be515ec3bc7080ba4.
- Deligne, *La conjecture de Weil. II*, IHÉS52 (1980), printed213–214, §3.6; printed217 and221, chapterIV's coefficient choices; printed248–249, §6.2.9. The entire original article, printed137–252, has now been read, with coverage recorded separately from checks of individual formulas. [Original article](https://www.numdam.org/item/PMIHES_1980__52__137_0/).
- GLOBAL_SHIFTED_ZETA_LIFT.md, GSL0–GSL11, including the full continuous CRT proof and the higher-weight addition GSL6.5–GSL6.11, read completely.
- CC_GEOMETRIC_TATE_INDEPENDENT.md, CGT0–CGT12, read completely; it proves the signed chart realization, all finite-field fibres, Kummer class, ramified specialization, proper pushforward and invariant Euler factors.

These source comparisons do not ascribe the new map below to Deligne or Connes–Consani.

## GTZ1. The complete coefficient spaces and their operations

Let \(\mathcal B\) be the Fréchet space of entire functions with all seminorms
\[
b_{A,M}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty,
\qquad A,M\in\mathbf Z_{\ge0}.
\tag{GTZ1.1}
\]
Let \(\mathscr Z\) be the distinct nontrivial zeros of the original \(\zeta\), with actual multiplicities \(m_\rho\). The already proved boundary nonvanishing places them in \(0<\Re\rho<1\). Define closed ideals
\[
\begin{aligned}
\mathcal I&=\{F:F^{(j)}(\rho)=0\text{ for every }\rho,\ 0\le j<m_\rho\},\\
\mathcal I_+&=\{F:F^{(j)}(\rho+1)=0\text{ for every }\rho,\ 0\le j<m_\rho\},\\
\mathcal Q&=\mathcal B/\mathcal I,\qquad
\mathcal Q_+=\mathcal B/\mathcal I_+,\qquad
\mathcal E_+=\mathcal B/(\mathcal I\cap\mathcal I_+).
\end{aligned}
\tag{GTZ1.2}
\]
All quotients have their actual quotient Fréchet topologies. No unrestricted product of zero jets replaces them.

For every already reconstructed \(a>0\), the continuous coefficient operator is
\[
T_aF(s)=a^sF(s),\qquad L F(s)=sF(s).
\tag{GTZ1.3}
\]
Multiplication by \(a^s\) preserves each ideal and is continuous, since its modulus is \(a^{\Re s}\), bounded on each fixed vertical strip. Multiplication by \(s\) is continuous with one additional polynomial seminorm. They consequently induce the indicated operators on all quotients.

Write \(U F(s)=F(s+1)\) and \(V F(s)=F(s-1)\). Their continuity follows from
\[
b_{A,M}(U F),\ b_{A,M}(V F)\le b_{A+1,M}(F).
\tag{GTZ1.4}
\]
The map \(V\) sends \(\mathcal I\) to \(\mathcal I_+\), and \(U\) reverses this map. Thus they induce mutually inverse maps \(\bar V:\mathcal Q\to\mathcal Q_+\) and \(\bar U:\mathcal Q_+\to\mathcal Q\).

GSL4–GSL6 construct an entire multiplier \(E_+\) of \(\mathcal B\) with the full jet congruences
\[
E_+\equiv1\pmod{\mathfrak m_\rho^{m_\rho}},
\qquad
E_+\equiv0\pmod{\mathfrak m_{\rho+1}^{m_\rho}}.
\tag{GTZ1.5}
\]
Here congruences are in the local holomorphic rings at the named points. The construction uses all zeros simultaneously and proves polynomial strip growth, so multiplication by \(E_+\) and \(1-E_+\) is continuous on \(\mathcal B\). In particular these are not formal infinite sums of local projectors.

The resulting continuous maps are
\[
\begin{aligned}
\pi[F]&=[F]_{\mathcal I},\\
j[h]&=[(1-E_+(s))h(s-1)]_{\mathcal I\cap\mathcal I_+},\\
\sigma[f]&=[E_+(s)f(s)]_{\mathcal I\cap\mathcal I_+}.
\end{aligned}
\tag{GTZ1.6}
\]
They give the split exact row
\[
0\longrightarrow\mathcal Q(-1)\xrightarrow{j}
\mathcal E_+\xrightarrow{\pi}\mathcal Q\longrightarrow0.
\tag{GTZ1.7}
\]
The notation \(\mathcal Q(-1)\) here specifies \(T_a^{(-1)}=aT_a\), \(L^{(-1)}=L+1\), on the same underlying Fréchet vector space. Its compatibility with an actual geometric Tate class, rather than a declaration about a class on \(\tau\), is what is proved next.

## GTZ2. The actual complex line and its degree action

The CC object has complex points
\[
X(\mathbf C)=\mathbf P^1(\mathbf C)_+\sqcup\mathbf P^1(\mathbf C)_-,
\quad
\alpha(z,J)=(-1/z,-J),\quad J\in\{i,-i\}.
\tag{GTZ2.1}
\]
The full signed coordinate formula is retained. Its quotient by \(\alpha\) is the complex line \(M=\minf(\mathbf C)\). Each orbit has exactly one point with \(J=i\), giving an isomorphism \(M\simeq\mathbf P^1(\mathbf C)\); the other representative is explicitly obtained by \(\alpha\).

For odd \(n\ge1\), the descended source morphism is
\[
f_n(z)=
\begin{cases}
z^n,&n\equiv1\pmod4,\\
-1/z^n,&n\equiv3\pmod4.
\end{cases}
\tag{GTZ2.2}
\]
In homogeneous coordinates these are respectively
\([X:Y]\mapsto[X^n:Y^n]\) and
\([X:Y]\mapsto[-Y^n:X^n]\).
Neither pair has a common projective zero. The first pulls the transition function of \(\mathcal O(1)\) to its \(n\)-th power; the second is its composition with a projective linear automorphism. Hence
\[
f_n^*\mathcal O(1)\simeq\mathcal O(n).
\tag{GTZ2.3}
\]

Give \(M\) its complex orientation and let \(h=c_1(\mathcal O(1))\in H^2(M,\mathbf C)\). This is the image of the integral first Chern class; its integral on \(M\) is \(1\), by the clutching function of degree one. Thus it retains a specified integral generator before scalar extension. The projective line has a CW decomposition with one cell in degree zero and one in degree two. Its cellular cochain complex is \(\mathbf C\) in those two degrees and zero otherwise, with zero differential. It follows that
\[
H^0(M,\mathbf C)=\mathbf C\,1,\quad
H^1(M,\mathbf C)=0,\quad
H^2(M,\mathbf C)=\mathbf C\,h.
\tag{GTZ2.4}
\]
Naturality of \(c_1\) and (GTZ2.3) prove
\[
f_n^*1=1,\qquad f_n^*h=n h.
\tag{GTZ2.5}
\]
The coordinate minus sign in (GTZ2.2) has not become a negative degree: its projective automorphism has degree \(+1\).

The quotient and unquotiented calculation agree by actual pullback. If \(q:X(\mathbf C)\to M\), then
\[
q^*1=(1,1),\qquad q^*h=(h_+,h_-).
\tag{GTZ2.6}
\]
These follow because the restriction of \(q\) to either component is a holomorphic projective automorphism. They identify \(H^\bullet(M,\mathbf C)\) with the \(\alpha\)-invariant cohomology. The anti-diagonal component remains the complementary eigenspace; it has not been identified with zero.

## GTZ3. The geometric receiver with the full original coefficients

Take constant cellular coefficients in the already constructed \(\mathcal Q\). The cellular cochain complex is \(\mathcal Q\) in degrees zero and two, with zero differential; all its maps are continuous. Its cohomology, with the finite product topology, is
\[
\mathcal H=H^0(M;\mathcal Q)\oplus H^2(M;\mathcal Q)
=\mathcal Q\,1\oplus\mathcal Q\,h.
\tag{GTZ3.1}
\]
There is no completion of an infinite tensor product here: the geometric cochain complex has two cells.

Precisely, \(x1+yh\) denotes \(x\otimes1+y\otimes h\) in
\(\mathcal Q\otimes_{\mathbf C}H^{\rm even}(M,\mathbf C)\), with its finite-product topology. Both \(1\) and \(h\) belong to the scalar geometric cohomology; neither notation presupposes a multiplicative identity in \(\mathcal Q\). All coefficient products below are the products of the actual quotient algebra.

The joint coefficient and geometric action is
\[
\mathcal T_n=T_n\otimes f_n^*:
\quad x\,1+y\,h\longmapsto (T_nx)\,1+(nT_ny)\,h,
\qquad n\text{ odd}.
\tag{GTZ3.2}
\]
It defines a continuous monoid representation. Indeed the source maps compose by \(f_m f_n=f_{mn}\), and \(T_mT_n=T_{mn}\); the displayed formula also verifies composition directly.

Define the geometric inclusion and projection
\[
\iota_h:\mathcal Q(-1)\to\mathcal H,\quad y\mapsto y h,
\qquad
\epsilon_0:\mathcal H\to\mathcal Q,\quad x1+yh\mapsto x.
\tag{GTZ3.3}
\]
Their types retain degree two and its degree character; \(\iota_h\) is equivariant by (GTZ2.5). The section \(x\mapsto x1\) is equivariant. The class \(h\) is also the Gysin image of the oriented point class in \(M\): its Poincaré dual integrates to the point's multiplicity one, and the cellular \(H^2\) has precisely that integral generator. In the arithmetic étale formulation the corresponding map is \(\mathbf Q_\ell(-1)[-2]\to Rp_*\mathbf Q_\ell\), constructed by the Kummer Chern class in CGT4 and CGT8. Thus the degree and twist have an actual geometric source.

## GTZ4. The exact map and its inverse

Define
\[
\boxed{\Theta:\mathcal E_+\longrightarrow\mathcal H,\qquad
[F]\longmapsto [F]_{\mathcal I}\,1+[F(s+1)]_{\mathcal I}\,h.}
\tag{GTZ4.1}
\]
This is well defined. Changing \(F\) by \(D\in\mathcal I\cap\mathcal I_+\) changes the first component by an element of \(\mathcal I\); since \(D\) has all required jets zero at \(\rho+1\), \(D(s+1)\) has those jets zero at \(\rho\), so the second component is unchanged as well. Quotient maps and translation are continuous, hence so is \(\Theta\).

For \(x=[f]_{\mathcal I}\), \(y=[g]_{\mathcal I}\), define
\[
\boxed{\Xi(x1+yh)=
[E_+(s)f(s)+(1-E_+(s))g(s-1)]_{\mathcal I\cap\mathcal I_+}.}
\tag{GTZ4.2}
\]
This is independent of both representatives. If \(f\) changes by an element of \(\mathcal I\), its product with \(E_+\) vanishes to the required orders on the original divisor and, by (GTZ1.5), on the shifted divisor. If \(g\) changes by an element of \(\mathcal I\), its translate by \(V\) vanishes on the shifted divisor; multiplication by \(1-E_+\) supplies vanishing on the original divisor. The induced map is continuous by the quotient property, the continuous multiplier bounds, and (GTZ1.4).

At every original zero the expression in (GTZ4.2) has exactly the full jet of \(f\). At every shifted zero \(\rho+1\) it has exactly the full jet of \(g(s-1)\). Hence \(\Theta\Xi(x1+yh)=x1+yh\). Conversely, the expression \(\Xi\Theta[F]-[F]\) has all required jets zero at both complete divisors, and therefore belongs to the defining ideal \(\mathcal I\cap\mathcal I_+\). This proves \(\Xi\Theta=1\).

Thus \(\Theta\) is a continuous linear isomorphism with the stated continuous inverse. The argument compares the actual quotient classes, not merely a finite set of their observations.

## GTZ5. Equivariance, the entire lifting row, and every jet

For every odd \(n\), its first component satisfies \([n^sF]=T_n[F]\). Its second component is
\[
[(n^sF)(s+1)]_{\mathcal I}
=[n^{s+1}F(s+1)]_{\mathcal I}
=nT_n[F(s+1)]_{\mathcal I}.
\tag{GTZ5.1}
\]
Equations (GTZ3.2) and (GTZ5.1) prove
\[
\Theta T_n=\mathcal T_n\Theta.
\tag{GTZ5.2}
\]
The factor \(n\) is exactly the degree factor already proved on \(h\).

The maps of the entire extension agree:
\[
\Theta j(y)=yh,\qquad
\epsilon_0\Theta=\pi,\qquad
\Theta\sigma(x)=x1.
\tag{GTZ5.3}
\]
The first identity uses both congruences in (GTZ1.5), with the translation \(U V=1\); the other two use the same congruences. Thus the following is a diagram of split exact continuous equivariant rows:
\[
\begin{array}{ccccccccc}
0&\to&\mathcal Q(-1)&\xrightarrow{j}&\mathcal E_+
&\xrightarrow{\pi}&\mathcal Q&\to&0\\
&&\Vert&&\downarrow\Theta&&\Vert\\
0&\to&\mathcal Q(-1)&\xrightarrow{\iota_h}&\mathcal H
&\xrightarrow{\epsilon_0}&\mathcal Q&\to&0 .
\end{array}
\tag{GTZ5.4}
\]
In particular the analytic continuous section is sent to the geometric degree-zero section, while the kernel is sent to the hyperplane summand.

Every multiplicity remains visible. At an original zero \(\rho\), write its full jet coordinate as \(t=s-\rho\), taken modulo \(t^{m_\rho}\). The coefficient action is
\[
n^{\rho+t}
=n^\rho\sum_{j=0}^{m_\rho-1}\frac{(\log n)^j}{j!}t^j.
\tag{GTZ5.5}
\]
The shifted jet has coordinate \(t=s-(\rho+1)\). Translation \(U\) identifies these coordinates with the same \(t\), without a sign or factorial change. Its action is
\[
n^{\rho+1}\sum_{j=0}^{m_\rho-1}
\frac{(\log n)^j}{j!}t^j
=n\left(n^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log n)^j}{j!}t^j\right).
\tag{GTZ5.6}
\]
This is precisely (GTZ5.1) on the entire jet. No zero simplicity or RH has been used.

The analytic row has operators for all positive real \(a\). Its geometric identification here is asserted for the actual CC odd monoid. The absence of an even signed endomorphism in that monoid does not remove the prime \(2\) from \(\mathcal Q\): the coefficient object was constructed from the full original \(\zeta\). The fibre Frobenius at \(2\) and its separate geometric Tate factor are explicitly constructed in CGT5–CGT7.

## GTZ6. The original zeta product and all exceptional contributions

The finite-prime calculation of CGT8–CGT10 gives an independent exact comparison to the same shift. The \(\alpha\)-invariant proper pushforward is
\[
(Rg_*\mathbf Q_\ell)^\alpha
\simeq\mathbf Q_\ell\oplus\mathbf Q_\ell(-1)[-2].
\tag{GTZ6.1}
\]
Its full trace at prime \(p\), repetition \(m\), is \(1+p^m\). At \(p=2\) this is obtained from the actual nonreduced fibre and its reduction map; at \(p=\ell\) the compatible local polynomial is calculated with a different coefficient prime. Therefore
\[
\begin{aligned}
\prod_p\frac1{(1-p^{-s})(1-p^{1-s})}
&=\exp\!\left(\sum_p\sum_{m\ge1}
\frac{p^{-ms}+p^{m(1-s)}}m\right)\\
&=\zeta(s)\zeta(s-1),\qquad \Re s>2.
\end{aligned}
\tag{GTZ6.2}
\]
Both original factors, all repetitions, and both unit terms remain. This geometric Euler product is not identified with a determinant of \(\mathcal Q\); such a determinant has not been constructed in this note.

The analytic full source functions used to implement the two nontrivial zero divisors are
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad
F_{-1}(s)=\frac{(s-1)(s-2)}8
\pi^{-(s-1)/2}\Gamma((s-1)/2)\zeta(s-1).
\tag{GTZ6.3}
\]
Their product is the product of both displayed multipliers times both original zeta functions. It is not a replacement definition of those original functions.
The meromorphic product \(\zeta(s)\zeta(s-1)\) has:

- nontrivial zero divisors \((\rho,m_\rho)\) and \((\rho+1,m_\rho)\);
- simple trivial zeros at every \(-2r\) and \(1-2r\), \(r\ge1\);
- simple poles at \(s=1\) and \(s=2\).

There are no cancellations within this list: at \(\rho\), the factor \(\zeta(s-1)\) is a unit, by the functional equation and Euler nonvanishing in the reflected half-plane; at \(\rho+1\), \(\zeta(s)\) is a unit by Euler nonvanishing. At the listed trivial zeros the other zeta factor is nonzero; at the poles the other factor is respectively \(\zeta(0)=-1/2\) and \(\zeta(2)\ne0\). The trivial zeros are simple by the full functional equation and the nonzero positive-half-plane value.

The full comparison retains
\[
F_0(0)=F_0(1)=\frac18,\qquad
F_{-1}(1)=F_{-1}(2)=\frac18,
\tag{GTZ6.4}
\]
and, for every \(r\ge1\),
\[
\begin{aligned}
F_0(-2r)
&=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)\\
&=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r),\\
F_{-1}(1-2r)&=F_0(-2r),\qquad
F_{-1}(2+2r)=F_0(1+2r).
\end{aligned}
\tag{GTZ6.5}
\]
These nonzero values record the cancellation by the displayed multipliers; they are not zeros of the quotient divisor. For every derivative order \(d\), if \(K(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/8\), then
\[
F_0^{(d)}(s)=\sum_{j=0}^{d}\binom dj K^{(d-j)}(s)\zeta^{(j)}(s),
\quad
F_{-1}^{(d)}(s)=F_0^{(d)}(s-1).
\tag{GTZ6.6}
\]
At exceptional points these identities are interpreted by the meromorphic product's holomorphic continuation, as (GTZ6.4)–(GTZ6.5) explicitly compute. Thus no endpoint, Gamma derivative, multiplicity or constant is suppressed by the map.

## GTZ7. The multiplication transported by the comparison

The map \(\Theta\) is not claimed to respect the usual cup product on \(H^\bullet(M;\mathcal Q)\). There is an exact relation to it.

The quotients of \(\mathcal B\) are commutative algebras under function multiplication. Translation \(U\) respects multiplication. Therefore the product transported from \(\mathcal E_+\) to the coordinates of \(\mathcal H\) is
\[
(x1+yh)\mathbin{\diamond}(x'1+y'h)
=(xx')1+(yy')h.
\tag{GTZ7.1}
\]
This follows directly by applying \(\Theta\) to representatives \(F G\), at the two divisors. With \(\diamond\), \(\Theta\) is an algebra isomorphism.

The geometric cup product is instead
\[
(x1+yh)\smile(x'1+y'h)
=(xx')1+(xy'+yx')h,
\tag{GTZ7.2}
\]
because \(h\smile h=0\) in degree four of the two-dimensional sphere and \(1\) is the degree-zero identity in its geometric cohomology. The exact difference, in this already additive coefficient space, is
\[
(u\diamond v)-(u\smile v)
=(yy'-xy'-yx')h.
\tag{GTZ7.3}
\]
Thus the continuous representation comparison is fully specified, including the extra multiplicative structure it does and does not preserve. It does not identify an idempotent divisor projector with a square-zero cohomology class as algebras.

## GTZ8. What is proved about lifting, and what remains active

GTZ4–GTZ5 construct an actual continuous isomorphism of the whole original-zeta shifted extension with the cohomology of the CC complex line carrying the already constructed \(\mathcal Q\). Its kernel's factor \(n\) is the pullback degree of the geometric hyperplane class, and its entire section corresponds to degree zero. CGT7 separately proves the actual ramified invariant-cycle lift at \(2\), by \(a\mapsto(a,a)\).

Deligne's local invariant-cycle proof in §3.6, and its pure-complex version §6.2.9, involve a localization cross and a dual support-cohomology obstruction. GTZ5.4 is a proved comparison to this particular cohomology receiver; it does not yet identify that localization cross with the user's desired \(\tau\)-supported lifting construction. In particular \(\mathcal Q\) is an input coefficient space here, and its spectral purity has not been obtained from the purity of the projective line's geometric Tate class.

No conditional theorem replaces that calculation. The concrete result is the map \(\Theta\), its inverse, all equivariance and full jet identities, and the two geometric rows just proved. The active research goal remains to construct and calculate the actual receiving localization/support maps for the programme, using the complete source and the user's prerequisite order.

## GTZ9. Proof dependencies and illustration

The complete continuous multiplier and CRT estimates are in GSL4–GSL6; this note uses that proved multiplier, not an assumed separator. The original Mellin source identification and its topological quotient are S5 and RZ1–RZ4, with source formulas retained in GSL8. The geometric integral Chern class calculation and finite-prime realizations are CGT4, CGT7–CGT10. The complete comparison between these inputs is GTZ1–GTZ7 above.

The accompanying figure is a diagram of these exact maps and the ramified specialization. Its labels retain the shift, degree, twist and coefficient spaces. It does not depict a proved purity statement for \(\mathcal Q\).

![The full continuous comparison and the geometric source of its degree factor. Panel A is GTZ5.4, with Theta and its inverse proved in GTZ4. Panel B is the actual ramified specialization of CGT7. Panel C is the all-prime Euler product of CGT10. Q is already constructed input data.](cc_geometric_global_lift.png)

The independent mathematical check is GTZ_INDEPENDENT_MATHEMATICAL_CHECK.md, GTC0–GTC5. It checked the entire map, its topology and multiplication types, all exceptional-value factors, and the full GSL multiplier mechanism. Its tensor-notation clarification is incorporated in GTZ3.
