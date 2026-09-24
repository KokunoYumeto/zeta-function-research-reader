# The Z_1 base, the twistor involution, and the original-zeta receiver

24 September 2026. This is a source-directed calculation on the supplied author TeX. It retains the user's notation: tau carries Z_1 presentness without Z_2 parity; integer 1 is the identity on the integer part; tau is the global multiplicative identity. Addition involving tau is not used. An operation on an auxiliary coefficient ring or on a space of functions is not an additional operation on tau. Every comparison below states its domain and what it retains.

The human sources are Alain Connes and Caterina Consani, *The Absolute Twistor Line and the Geometry of Spec Z* ([2609.00299v1](https://arxiv.org/abs/2609.00299v1), CC.tex); the same authors, *On the Absolute Geometry of Spec Z* ([2606.06604v1](https://arxiv.org/abs/2606.06604v1), FF.tex); their *On the Jacobian of Spec Z* ([2602.15941v1](https://arxiv.org/abs/2602.15941v1), Jacobian.tex); and Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time* ([2602.04022v1](https://arxiv.org/abs/2602.04022v1), rhready.tex). All four supplied TeX files are byte-identical to the respective original arXiv sources. Source archives and the exact reading ledger are retained. The calculations marked C1–C10 below are this note's derivations, not claims of literature novelty.

## C1. The multiplicative base comparison retains tau and integer 1

Let M be the multiplicative integer-plus-tau stage. Its products are the ordinary integer products and tau*x=x*tau=x for every x in M. Tau differs from each nonzero integer by the retained Z_2 availability; tau=0 would imply 1=tau*1=0*1=0. Thus the disjoint presentation M=Z disjoint-union {tau} records a consequence. Higher stages of the user's hierarchy are not declared absent.

Put B_tau={0,tau} with these products. The map

\[
b:B_\tau\longrightarrow\{0,1_{\mathrm{CC}}\},\qquad
b(0)=0,\quad b(\tau)=1_{\mathrm{CC}}
\tag{C1.1}
\]

is an isomorphism of pointed multiplicative monoids: 0 is absorbing and tau is the unit, exactly matching the two source products. Its inverse sends the source unit to tau. This is the pointed-monoid part of the source's F_1 base, not a claim that an unspecified additive structure or every framework called F_1 has been identified.

The integer receiver r:M->(Z,multiplication), r(n)=n, r(tau)=1 is multiplicative. It identifies the images of tau and integer 1. Retain also

\[
\chi:M\longrightarrow B_\tau,\qquad
\chi(\tau)=\tau,\quad \chi(n)=0\quad(n\in\mathbb Z).
\tag{C1.2}
\]

For an integer product both sides of multiplicativity are 0; for a product with tau both sides equal the value of the other factor. Hence chi is multiplicative. The pair (chi,r) is injective and has image

\[
(\{0\}\times\mathbb Z)\ \cup\ \{(\tau,1)\}.
\tag{C1.3}
\]

Indeed an integer n has the unique pair (0,n), whereas tau has (tau,1). In particular using the complex-valued points of the authors' geometry does not make the scalar value 1 a faithful record of the original source element. Equations C1.2–C1.3 give an explicit faithful receiver. No integer amount or parity is assigned to tau.

## C2. Signed extension and the exact generic involution

CC.tex, Definition `def:alpha_symmetry`, uses epsilon^2=1 and J^2=epsilon. Retain its sign as a new multiplicative datum. It is not automatically the user's Z_2 parity.

Here is an extension preserving the full M before taking geometric points. Take the disjoint union of the Gaussian integers Z[i] and four new units u_0,u_1,u_2,u_3. Set u_0=tau, u_2=epsilon, u_1=J; define

\[
u_r u_t=u_{r+t\bmod4},\qquad
u_r a=a u_r=i^r a\ (a\in\mathbb Z[i]),
\tag{C2.1}
\]

and use ordinary products on Z[i]. Associativity follows separately for three units from addition modulo 4, for two units and a Gaussian integer from i^(r+t)=i^r i^t, and for one unit and two Gaussian integers from i^r(ab)=(i^r a)b. Three Gaussian integers use their usual associativity. Commutativity reduces all orders to these cases. Zero is absorbing and tau is the global unit. Inclusion embeds M multiplicatively. Local Gaussian i and global J remain different, as do local -1 and epsilon. J^2=epsilon and epsilon^2=tau hold without identifying local integer 1 with tau.

For the generic source chart itself let

\[
A_\eta=\{0\}\ \cup\ \{J^rT^k:r\in\mathbb Z/4\mathbb Z,\ k\in\mathbb Z\}.
\tag{C2.2}
\]

Its product adds the exponent k and adds r modulo 4; 0 is absorbing, J^0T^0=tau, and epsilon=J^2T^0. This is the explicitly presented multiplicative monoid of the source chart. Its isomorphism to the authors' monomial presentation sends tau to their unit and retains J,T,epsilon. The inverse recovers the two exponents. The infinite exponent k is never reduced modulo 2 or 4.

The source's signed inversion has the exact coordinate form

\[
\alpha^*(J^rT^k)=J^{-r+2k}T^{-k},\qquad
\alpha^*(0)=0.
\tag{C2.3}
\]

This follows by multiplying (J^(-1))^r and (epsilon*T^(-1))^k. The map on the exponent pair is additive, so it preserves products. Applying it twice sends (r,k) to
(-(-r+2k)+2(-k),-(-k))=(r,k); hence it is an involution. Fixedness requires k=-k in Z and r=-r modulo 4. Consequently its entire fixed submonoid is

\[
\operatorname{Fix}(\alpha^*)=\{0,\tau,\epsilon\}.
\tag{C2.4}
\]

Tau's fixedness is thus proved in the actual generic algebra. Epsilon is also fixed; it must not be discarded. For every positive odd n, the power map F_n:(r,k)->(nr,nk) commutes with alpha. The joint fixed submonoid of all these maps is again {0,tau,epsilon}: n=3 forces k=0 and 2r=0, and those three elements are fixed for every odd n.

CC's underlying three-point space has alpha(+)=-, alpha(-)=+, alpha(eta)=eta. The earlier integer-step orbit receiver Q={tau-marker,E,O} is isomorphic as an involutive set to it by tau-marker->eta, E->+, O->-. Checking the three values proves equivariance and the inverse. This is a map of involutive sets. It does not identify a base element tau with a point carrying the entire generic stalk A_eta, and it does not discard the full integers in M.

## C3. The sign distinguishing two real structures

Over C, source points have J-coordinate i or -i. Alpha sends (z,i) to (-1/z,-i), while complex conjugation sends it to (bar(z),-i). Returning to the i branch after conjugation gives exactly

\[
\sigma(z)=-\frac1{\bar z},\qquad \sigma(0)=\infty,
\quad\sigma(\infty)=0.
\tag{C3.1}
\]

This reconstructs CC.tex, Theorem `thm:twistor_space_scheme`, without dropping the sign. For finite nonzero z, fixedness would give |z|^2=-1, which is impossible; the endpoints are exchanged. Thus sigma has no fixed points on P^1(C).

There is also an explicitly related involution. The source automorphism R has R(T)=epsilon*T and R(J)=J; it extends to both charts, preserves their restrictions, and commutes with alpha. For example alpha R(T)=T^(-1)=R alpha(T), and both composites take J to J^(-1). Its induced complex map is R(z)=-z. Therefore

\[
\kappa=R\circ\sigma,\qquad
\kappa(z)=\frac1{\bar z},\qquad
\operatorname{Fix}(\kappa)=\{|z|=1\}\subset\mathbb C^\times.
\tag{C3.2}
\]

The endpoints are again exchanged; the displayed fixed locus follows by multiplying z=1/bar(z) by bar(z). R^2=id and R commutes with sigma, so kappa^2=id. This is a proved sign twist of the source involution, not the same real structure silently renamed. No bijective conjugacy can turn sigma into kappa, since a conjugacy maps fixed sets bijectively and their fixed sets are empty and nonempty respectively.

The sign remains visible in homogeneous coordinates. With z=x/y, put

\[
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
B=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
D=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\tag{C3.3}
\]

Then A*bar(x,y) induces sigma, B*bar(x,y) induces kappa, B=DA, A*bar(A)=-I and B*bar(B)=I. Projectivization makes both induced squares the identity but retains different real structures. The unit comparison tau->I and epsilon->-I uses the source multiplicative sign; it does not define tau as an additive zero vector.

For comparison with the user's radius proposal, the complete sphere map is

\[
\Phi(z)=\frac{(2\Re z,2\Im z,|z|^2-1)}{1+|z|^2},\quad
\Phi(\infty)=(0,0,1).
\tag{C3.4}
\]

Its numerator has squared norm 4|z|^2+(|z|^2-1)^2=(1+|z|^2)^2. Thus its radius is 1 for every z. Direct substitution gives Phi(sigma(z))=-Phi(z). Away from the north pole its inverse is z=(X+iY)/(1-Z); the north pole returns infinity. Equal sphere radius therefore coexists with a retained, recoverable coordinate |z|. It is a property of this target geometry, not an assigned metric at the user's tau.

The actual odd Frobenius in CC.tex, Proposition `prop:twistor_frobenius`, is z^n for n=1 mod 4 and -1/z^n for n=3 mod 4. Consequently |z| becomes |z|^n or |z|^(-n), respectively, while Phi of either result still has radius 1. This is an exact calculation within the supplied geometry; it retains the spectral size that a sphere-radius observation alone does not record.

## C4. Descent to the supplied Tate curve and its two fixed circles

![The Tate fixed circles and the retained signed action](https://raw.githubusercontent.com/KokunoYumeto/zeta-function-research-reader/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/tate_fixed_locus.png)

Figure 1. The left drawing uses p=3 solely to display the annulus. C4 proves the circles for every prime p. The right drawing displays the actual quotient maps; the marked point is an arbitrary geometric point, not an asserted zeta zero. Reproducible source: draw_tate_fixed_locus.py. Proofs: C4–C5. The two radial boundary circles are identified by the deck factor p.

FF.tex, `The Tate curve E_p` and `thm:tate_decomposition`, supplies

\[
E_p=\mathbb C^\times/p^{\mathbb Z},\qquad p\text{ a positive rational prime}.
\tag{C4.1}
\]

Both sigma and kappa descend to E_p, since sigma(p^k z)=p^(-k)sigma(z) and kappa(p^k z)=p^(-k)kappa(z). A sigma-fixed class would satisfy -1/bar(z)=p^k z, hence -1=p^k |z|^2. No such class exists.

A kappa-fixed class instead satisfies

\[
\frac1{\bar z}=p^kz
\quad\Longleftrightarrow\quad
|z|^2=p^{-k}.
\tag{C4.2}
\]

Retain n=-k. Before quotienting, the full solution set with its integer degree is

\[
\widetilde{F}_p=\{(z,n)\in\mathbb C^\times\times\mathbb Z:
|z|^2=p^n\}.
\tag{C4.3}
\]

Changing representative z to p^j z changes n to n+2j. Thus n modulo 2 is independent of representative, while n itself is retained on the lifted set. Multiplication is (z,n)(w,m)=(zw,n+m), which preserves the equation because |zw|^2=p^(n+m). Its identity is (1,0), and its inverse is (1/z,-n).

Every even n has a unique representative with radius 1 after division by p^(n/2); every odd n has a unique representative with radius sqrt(p) after division by p^((n-1)/2). Their phases do not change. Explicitly,

\[
S^1\times\{0,1\}\longrightarrow\operatorname{Fix}(\kappa:E_p\to E_p),
\qquad (v,a)\longmapsto[p^{a/2}v]
\tag{C4.4}
\]

is bijective. Equality of two images implies p^((a-b)/2)*v/w=p^j. Taking moduli forces a=b and j=0, then v=w. Surjectivity was proved by the representative reduction. On the source of C4.4 the group law is (v,a)(w,b)=(vw,a+b mod 2): the factor p arising when a=b=1 is precisely the retained deck multiplication. Hence the fixed locus is a group isomorphic to S^1 times the two-element degree group.

This proves the two-circle classification, including its lifted integer data. Its two-state label is the parity of n. It is not silently identified with the intrinsic Z_2 state of an arbitrary integer element in the user's base. The exact comparison is n->n mod 2 on the displayed lifted integer coordinate.

## C5. Original zeta coordinates and the weight-one circle

For every complex s retain the unquotiented value Lambda_p(s)=p^s=exp(s log p), with the real positive log p. Define j_p(s)=[p^s] in E_p. No zeta completion or rescaling of the zeta function is involved.

In the open critical strip S={s:0<Re(s)<1}, C4.2 gives

\[
\begin{aligned}
j_p(s)\in\operatorname{Fix}(\kappa)
&\Longleftrightarrow |p^s|^2=p^n\text{ for some }n\in\mathbb Z\\
&\Longleftrightarrow 2\Re s=n\in\mathbb Z\\
&\Longleftrightarrow \Re s=\tfrac12.
\end{aligned}
\tag{C5.1}
\]

The last implication uses 0<2Re(s)<2, so n=1, not a choice of a radius. The full unquotiented radius on this locus is |p^s|=sqrt(p). Thus the strip selects exactly the odd-degree circle. Endpoints of the strip were not included; their real parts 0 and 1 land on the even-degree circle and are not removed from the global map.

Let R_zeta(s)=1-bar(s). The exact equivariance is

\[
\Lambda_p(R_\zeta s)=\frac p{\overline{\Lambda_p(s)}},\qquad
j_p(R_\zeta s)=\kappa(j_p(s)).
\tag{C5.2}
\]

The factor p in the first equality becomes a deck transformation in the second, and is retained explicitly. The involution on the unquotiented value is iota_p(z)=p/bar(z)=-p*sigma(z), whose fixed circle is |z|^2=p. This is the precise weight-one comparison with the supplied twistor map, including the sign and prime factor.

The arithmetic fixedness defect has a full scalar representative

\[
\Delta_p(s)=|p^s|^2-p=p^{s+\bar s}-p.
\tag{C5.3}
\]

It is zero, positive or negative according as Re(s) is 1/2, greater than 1/2 or less than 1/2, since exponentiation by p>1 is strictly increasing. Its reflected value is

\[
\Delta_p(R_\zeta s)=-\frac p{|p^s|^2}\Delta_p(s),
\tag{C5.4}
\]

by substituting |Lambda_p(R s)|^2=p^2/|p^s|^2. A paired sign change thus preserves the precise nonzero defect when the point is not fixed.

The quotient has an exact faithful two-prime receiver on S. For distinct primes p,q the map (j_p,j_q):S->E_p times E_q is injective. To prove this, j_p(s)=j_p(t) implies
s-t=m+2*pi*i*k/log(p), m,k integers. Since Re(s-t) lies strictly between -1 and 1, m=0. Equality for q similarly gives Im(s-t)=2*pi*l/log(q). If this common number is nonzero, k,l are nonzero and k log(q)=l log(p), contradicting unique prime factorization after exponentiation, also for negative integer exponents. Therefore k=l=0 and s=t. This provides an exact way to retain the original strip coordinate rather than treating its one-prime quotient as injective.

In particular RH is exactly the assertion that every nontrivial zero rho of the ORIGINAL zeta has j_p(rho) in the odd fixed circle, for one (hence every) prime p. This is a proved equivalence, not an assumption inserted to prove RH. Multiplicity is retained by attaching the original integer m_rho to each original zero and using the injective two-prime receiver. No infinite pushforward is asserted to be a locally finite divisor on a compact torus.

The functional equation supplies the paired zero 1-bar(rho); C5.2 proves the corresponding symmetry of their images. It does not by itself identify the two original zeros. The injective two-prime receiver makes the distinction testable on the actual source zeros, without changing their equation to the zeros of an auxiliary function.

## C6. The original-zeta multiplier and an exact factor-four correction

The supplied rhready.tex, lines 1062–1080, defines

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\mathcal E(f)(u)=u^{1/2}\sum_{n=1}^{\infty}f(nu),
\]
\[
h(u)=\frac\pi2 u^2(2\pi u^2-3)e^{-\pi u^2},\qquad k=\mathcal E(h).
\tag{C6.1}
\]

Compute from these actual definitions. For Re(s)>1, absolute convergence permits the change v=nu and interchange of integral and sum:

\[
\int_0^\infty\mathcal E(h)(u)u^{s-1/2}\frac{du}{u}
=\zeta(s)\int_0^\infty h(v)v^s\frac{dv}{v}.
\tag{C6.2}
\]

Indeed the sum of absolute integrals is bounded by zeta(Re(s)) times the finite integral of |h(v)|v^(Re(s))dv/v. The Gaussian controls infinity and h(v)=O(v^2) controls zero. Substitution t=pi*v^2 yields the complete two-term integral

\[
\begin{aligned}
\int_0^\infty h(v)v^s\frac{dv}{v}
={}&\frac\pi2\left[
2\pi\frac12\pi^{-(s+4)/2}\Gamma\left(\frac{s+4}{2}\right)
-3\frac12\pi^{-(s+2)/2}\Gamma\left(\frac{s+2}{2}\right)\right]\\
={}&\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\end{aligned}
\tag{C6.3}
\]

The second displayed expression is an evaluated identity, not a replacement of the two original contributions; both remain in C6.3. The Gamma recurrence proves the identity by extracting Gamma(s/2) and evaluating (1/2)(s/2)((s/2+1)-3/2).

Consequently the correct exact comparison is

\[
\boxed{\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}
=\frac18s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac14\xi(s).}
\tag{C6.4}
\]

The equality to xi asserted for this displayed k in the source is therefore missing a factor 4. At s=2 the left side is pi/24 and xi(2)=pi/6. This also supplies a direct exact check independent of numerical plotting.

For completeness the equality continues to the critical line without discarding boundary terms. Under the source Fourier convention exp(2*pi*i*x*y), the Gaussian g=exp(-pi*x^2) transforms to itself; differentiating the Gaussian transform gives
F(x^2g)=(1/(2*pi)-y^2)g and
F(x^4g)=(y^4-3*y^2/pi+3/(4*pi^2))g.
Since h=pi^2*x^4*g-(3*pi/2)*x^2*g, these identities give Fh=h, h(0)=0 and integral h=0. Poisson summation then gives k(u)=k(1/u). Gaussian decay of k at infinity and this symmetry give rapid decay at both ends in logarithmic coordinates. Thus its Mellin integral is entire in s, and analytic continuation extends C6.4. For Xi(t)=xi(1/2+it) the corrected equality is Xi(t)=4*integral k(u)u^(it)du/u, keeping exactly the source kernel.

The original zeta remains recovered on every domain where the displayed inverse is defined:

\[
\zeta(s)=\frac{8\pi^{s/2}}{s(s-1)\Gamma(s/2)}
\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{C6.5}
\]

In the open critical strip the multiplier C(s)=s(s-1)pi^(-s/2)Gamma(s/2)/2 is holomorphic and nonzero, so C6.4–C6.5 preserve all zero multiplicities there. Globally keep

\[
\frac{\xi'}{\xi}=
\frac{\zeta'}{\zeta}+\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)}.
\tag{C6.6}
\]

At 1 the factor C has a simple zero and zeta a simple pole. At 0, s*Gamma(s/2) has limit 2, so C(0)=-1 and zeta(0)=-1/2 yields xi(0)=1/2. At -2m, m>=1, C has leading coefficient
2m(2m+1)(-1)^m*pi^m/m! times (s+2m)^(-1); the original zeta has a simple trivial zero there. Retain the local pair zeta(s)=(s+2m)a_m(s), C(s)=(s+2m)^(-1)b_m(s), so xi=a_m*b_m and zeta=(s+2m)xi/b_m. The nonzero b_m(-2m) is the displayed coefficient. These are local meromorphic identities; no canceled divisor is declared absent from the original zeta.

## C7. The plotted projection defect and its actual involution

Use exactly H=L^2(R)_even, the Fourier transform F with kernel exp(2*pi*i*x*y), P=P_lambda the projection to [-lambda,lambda], and Q=F P F^(-1). On H, F^2=I, so Q=F P F. For the source prolate eigenfunction h=h_(2m,lambda), P h=h and P F P h=chi_m h. Therefore

\[
PQP h=\chi_m^2 h,\qquad
\|(I-Q)h\|^2=(1-\chi_m^2)\|h\|^2.
\tag{C7.1}
\]

Proof: PQP=(PFP)^2 on PH. Since Q is an orthogonal projection, <Qh,h>=||Qh||^2=chi_m^2||h||^2, and orthogonal Pythagoras gives the second identity. For m=2, the source chi_2 is positive and strictly below 1. Hence the precise orange quantity in the supplied plot is

\[
1-\chi_2=
\frac{\|(I-Q)h_{4,\lambda}\|^2}
{(1+\chi_2)\|h_{4,\lambda}\|^2}.
\tag{C7.2}
\]

Every norm and factor remains displayed.

The exact reflection product behind this defect is U=(2P-I)(2Q-I). Put a=|chi_m|, b=sqrt(1-a^2), with 0<a<1, and choose e=h/||h||, f=(Qe-a^2e)/(ab). Then P f=0, <f,e>=0, ||f||=1. Applying Q^2=Q gives Q f=ab e+b^2 f. Thus the span of e,f is invariant under both projections and their matrices are

\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
Q=\begin{pmatrix}a^2&ab\\ab&b^2\end{pmatrix},\quad
U=\begin{pmatrix}2a^2-1&2ab\\-2ab&2a^2-1\end{pmatrix}.
\tag{C7.3}
\]

The relation a^2+b^2=1 gives U*U=I. Writing a=cos(alpha), b=sin(alpha), 0<alpha<pi/2, its eigenvalues are exp(2i alpha) and exp(-2i alpha). This establishes the nontrivial phase of the product of the two involutions from the source projections; no physical holonomy is assumed. The leakage 1-a^2=sin^2(alpha) remains recoverable from it.

## C8. The same projection block retains both trace signs

The source's archimedean and semilocal trace expressions use D=I-P-Q, not just I-PQP. In the exact block C7.3,

\[
D=\begin{pmatrix}-a^2&-ab\\-ab&a^2\end{pmatrix},
\qquad D^2=a^2I,\quad\operatorname{Tr}D=0.
\tag{C8.1}
\]

Multiplication of this displayed matrix proves the square identity; its characteristic polynomial is t^2-a^2. Thus its two eigenvalues are +a and -a. A unitary product of reflections and a positive leakage quantity coexist with these two trace signs on the same source block. For any positive operator B on this block, in an orthonormal D-eigenbasis,
Tr(BD)=a(<Be_+,e_+>-<Be_-,e_->). Both terms must be retained. This does not assert that an arbitrary B is the image of a global admissible Weil test.

The full source formula, rhready.tex `weilqb`, is

\[
-\sum_{v\in S}W_v(f)=\log(TW)f(1)
+\operatorname{Trace}\!\left(\vartheta(f)
(I-P_T^S-\widehat P_W^S)\right).
\tag{C8.2}
\]

The cutoff term, the admissible test representation, the prime contributions and the trace's meaning in the source are not removed. C8.1 computes its projection factor only; it is not a claim that the individual unsmoothed factors are globally trace class. The blue plot quantity epsilon(lambda) is the least eigenvalue of the full Weil operator A_lambda in the different space L^2([lambda^(-1),lambda],du/u). No equality between that operator and the positive leakage operator is supplied by C7.2. The source itself describes the comparison in `poisson` and `miss` as numerical and leaves the eigenfunction comparison unfinished.

## C9. The two prolate modes have an exact nonzero endpoint defect

Fix lambda>1. Let h_0=h_(0,lambda), h_4=h_(4,lambda), c_0=h_0(0), c_4=h_4(0), with the source support extension by zero. Both c_0 and c_4 are nonzero: the functions are even, so their first derivatives at 0 vanish; their second-order prolate differential equation is regular at 0. If their values vanished too, uniqueness for the initial-value problem would make the eigenfunction identically zero, a contradiction.

The compressed Fourier identities give integral h_0=chi_0*c_0 and integral h_4=chi_2*c_4 by evaluation at Fourier coordinate 0. The source's strictly ordered squared eigenvalues and positive signs at indices 0,2 give 1>chi_0>chi_2>0. Thus the exact endpoint map on their two-dimensional span is

\[
L(a_0h_0+a_4h_4)=
\begin{pmatrix}f(0)\\\widehat f(0)\end{pmatrix}
=\begin{pmatrix}c_0&c_4\\\chi_0c_0&\chi_2c_4\end{pmatrix}
\begin{pmatrix}a_0\\a_4\end{pmatrix},
\quad\det L=c_0c_4(\chi_2-\chi_0)\ne0.
\tag{C9.1}
\]

No nonzero combination of these two modes kills both endpoints. This is an invertible map onto the two endpoint values, so the obstruction also constructs their complete two-mode parameterization: for prescribed values (u,v),

\[
a_0=\frac{\chi_2u-v}{c_0(\chi_2-\chi_0)},\qquad
a_4=\frac{v-\chi_0u}{c_4(\chi_2-\chi_0)}.
\tag{C9.2}
\]

For the source's integral-zero choice retain any scalar A and write

\[
h_\lambda=A(\chi_2 c_4h_0-\chi_0 c_0h_4),\quad
\widehat h_\lambda(0)=0,\quad
h_\lambda(0)=A c_0c_4(\chi_2-\chi_0).
\tag{C9.3}
\]

The last value is nonzero for A!=0; it tends toward a small value only under additional estimates, not by an exact cancellation. Conversely choosing f(0)=0 leaves the Fourier endpoint c_0c_4(chi_0-chi_2) times the chosen scalar. These formulas retain the distinction between near cancellation and actual vanishing.

The next source mode constructs an exact repair of both endpoint equations. Put h_8=h_(8,lambda), c_8=h_8(0), and let chi_4 be its compressed Fourier eigenvalue. As above c_8!=0, and the source ordering gives 1>chi_0>chi_2>chi_4>0. Define the actual function

\[
\begin{aligned}
g_\lambda={}&\frac{\chi_2-\chi_4}{c_0}h_0
+\frac{\chi_4-\chi_0}{c_4}h_4
+\frac{\chi_0-\chi_2}{c_8}h_8.\end{aligned}
\tag{C9.4}
\]

Its value at zero is the sum of the three displayed numerators, which is 0. Its integral is
chi_0(chi_2-chi_4)+chi_2(chi_4-chi_0)+chi_4(chi_0-chi_2)=0 by direct expansion. The coefficient of h_0 is nonzero; the distinct prolate eigenfunctions are linearly independent, so g_lambda is nonzero. The endpoint map on the three-mode span has rank 2 by its already invertible first two columns. Its kernel is therefore exactly the one-dimensional space spanned by g_lambda. This proves existence, uniqueness up to its retained scalar, and the exact map to both endpoint values.

The remaining Fourier defect is also explicit. Set
d_0=(chi_2-chi_4)/c_0, d_2=(chi_4-chi_0)/c_4,
d_4=(chi_0-chi_2)/c_8, so g_lambda=sum_(j=0,2,4) d_j h_(2j,lambda). Orthogonality of the distinct selfadjoint prolate eigenfunctions and the compressed Fourier equation give

\[
\|(F-I)g_\lambda\|^2
=2\sum_{j\in\{0,2,4\}}|d_j|^2(1-\chi_j)
\|h_{2j,\lambda}\|^2>0.
\tag{C9.5}
\]

Indeed F is a unitary involution on the even Hilbert space, so the left side equals 2||g_lambda||^2-2 Re< Fg_lambda,g_lambda>. Since every h_(2j,lambda) is supported in P, its pairing with Fh_(2k,lambda) equals its pairing with chi_k h_(2k,lambda). Expanding gives exactly C9.5, including every coefficient and norm. Strict positivity follows from chi_j<1 and the nonzero coefficients. The endpoint repair thus retains a nonzero Fourier defect; no finite-cutoff function has been declared exactly Fourier invariant.

For an even Schwartz function f, Poisson summation gives the full endpoint formula

\[
\mathcal E(\widehat f)(x)=\mathcal E(f)(x^{-1})
+\frac{f(0)}{2\sqrt x}-\frac{\sqrt x}{2}\widehat f(0).
\tag{C9.6}
\]

To prove it, separate n=0 in sum_(n in Z) f(n/x)=x*sum_(n in Z)hat(f)(nx), pair n with -n, and multiply by x^(-1/2)/2. This retains both half-factors and both endpoints. The source's equation `poissonintro` is its restriction to both endpoint values zero.

The compactly truncated prolate functions are not automatically Schwartz; C9.1–C9.5 require only their integrability and the source compressed Fourier equations, and are already exact. C9.6 is stated on its proved Schwartz domain and is not silently applied to nonsmooth extensions. Its endpoint receiver L identifies precisely the values that an extension of that identity or a smoothing construction must retain. The nonzero two-mode endpoint and the three-mode repair are therefore explicit data, not a discarded obstacle and not a claimed negative Weil value.

## C10. Return to the existing supported original-zeta form

The existing coefficient receiver is used rather than replacing the programme by the authors' scalar form. Write U=[tau], f=[1], Q_0=U-f in the auxiliary coefficient algebra of WEIL_UNIT_DIFFERENCE_LIFT.md, WU1–WU8. These are formal linear coefficients; no source subtraction tau-1 is asserted. Products give f^2=f, Q_0^2=Q_0, fQ_0=0, U=f+Q_0. Arithmetic evaluation sends both U and f to scalar 1 and Q_0 to scalar 0.

For an original compact smooth test h(v), retain H(s)=integral h(v)exp(-(s-1/2)v)dv, the full prime-power term P(h), and the Gamma term A_infinity(h). The programme's exact original-zeta receiver is

\[
W_\zeta(h)=H(0)+H(1)+A_\infty(h)-P(h)
=\sum_\rho m_\rho H(\rho),
\]
\[
P(h)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
(h(\log n)+h(-\log n)),
\]
\[
A_\infty(h)=\frac1{2\pi}\int_{\mathbb R}\widehat h(t)
\left(\Re\frac{\Gamma'(1/4+it/2)}{\Gamma(1/4+it/2)}-\log\pi\right)dt.
\tag{C10.1}
\]

Every finite trivial-zero cutoff is retained in the original identity
V_(zeta,N)=Z(H)+sum_(m=1)^N H(-2m)-H(1)=G_N-P(h),
G_N=A_infinity+H(0)+sum_(m=1)^N H(-2m).
The cancellation in the displayed W_zeta is an explicitly recorded map from this triple, not removal of its components. Its full contour derivation is OZC1–OZC15 in the retained programme source; WU2 states the boundary domains and convergence.

The source test identification is a(x)=h(log x). It preserves convolution and the involution a*(x)=bar(a(x^(-1))) because dx/x=dv. The source Fourier integral of a at t is H(1/2+it). Its endpoint values at +/-i/2 are respectively H(0),H(1), and the prime terms are exactly P(h). Thus the compared source form is reached by an explicit change of variable with all half-powers retained.

The archimedean comparison also retains its constant. The digamma integral, for Re(z)>0, is psi(z)=-gamma+integral_0^infinity (exp(-t)-exp(-zt))/(1-exp(-t)) dt. Apply it to z=1/4+iy/2 and Fourier inversion of h. First perform the t integral on [delta,R]; then send delta to 0 and R to infinity. The paired numerator at 0 vanishes to first order, and the Schwartz decay of hat(h) controls the polynomial y factors in its Taylor estimate. At infinity the exponential factors dominate. These bounds justify the passage to the limit and yield, after t=2v,

\[
\begin{aligned}
A_\infty(h)={}&-(\gamma+\log\pi)h(0)\\
&+\int_0^\infty\frac{2h(0)e^{-2v}-(h(v)+h(-v))e^{-v/2}}
{1-e^{-2v}}\,dv.
\end{aligned}
\tag{C10.3}
\]

The supplied source's archimedean expression, after x=exp(v), is exactly

\[
\begin{aligned}
W_{\mathbb R}(a)={}&(\log(4\pi)+\gamma)h(0)\\
&+\int_0^\infty\frac{(h(v)+h(-v))e^{-v/2}-2h(0)e^{-v}}
{1-e^{-2v}}\,dv.
\end{aligned}
\tag{C10.4}
\]

Adding C10.3 and C10.4 gives log(4)*h(0) minus
2h(0)*integral_0^infinity exp(-v)/(1+exp(-v))dv.
The last integral equals log(2), by the substitution w=exp(-v). Hence A_infinity(h)=-W_R(a), with the exact log(4*pi), gamma and log(pi) constants accounted for. Together with the already proved prime and endpoint maps this gives W_zeta(h)=H(0)+H(1)-sum_v W_v(a) without dropping an archimedean summand.

For the programme's support lattice L retain the vectors

\[
\boldsymbol B=\mathbf e_{1_L}(H(0)+H(1))
+\sum_{\ell\ne1_L}\mathbf e_\ell H(0),\quad
\boldsymbol Z=\mathbf e_{1_L}Z(H),
\]
\[
\boldsymbol D=\mathbf e_{1_L}(P(h)-A_\infty(h))
+\sum_{\ell\ne1_L}\mathbf e_\ell H(0).
\tag{C10.2}
\]

C10.1 proves bold(B)-bold(Z)=bold(D) on each coordinate. Tensoring each displayed term with U or f retains the two source records; their difference is the same complete vector tensored with Q_0. Arithmetic evaluation returns C10.2 without deleting a support coordinate. This is the exact comparison from WU3–WU5, and does not turn Q_0 into an extra classical Euler factor at 0.

The support trace proof is [SZW33–SZW38 at the pinned programme edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). The complete local return and full original-zeta reconstruction are retained with their proof locators in WEIL_UNIT_DIFFERENCE_LIFT.md, WU2–WU5, and the companion original source copies identified in the source ledger.

What has been established here is the actual base comparison, the sign-adjusted Tate fixed locus with all winding data, its faithful two-prime map from the original critical strip, the factor-four repair, the two-mode endpoint isomorphism, its three-mode repair with the complete Fourier defect, and the two-sign trace block. None of these statements assumes every zeta zero is fixed. The supplied geometry's involution and equal sphere radius have been carried through to these exact arithmetic and trace expressions; their values have not been assigned a positive sign by definition.
