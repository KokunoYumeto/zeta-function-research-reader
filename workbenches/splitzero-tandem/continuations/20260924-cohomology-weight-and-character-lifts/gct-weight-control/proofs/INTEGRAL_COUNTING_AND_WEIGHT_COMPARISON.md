# Integral counting, arithmetic operators, and the weight comparison

24 September 2026. Proof labels IC1–IC9. This note receives the proposed implication from the complete global counting unit to integrality and then purity. It calculates the intervening maps. It does not assume an off-critical zero exists, and the projective-line calculation below is not asserted to satisfy the entire tau/Connes–Consani programme.

The supporting point remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). No addition, subtraction, distance, coordinate, vector or numerical value is assigned to that point. Every operation below has as its domain a stalk quotient, an endomorphism ring, a group algebra, a cohomology group or the original-zeta quotient explicitly specified below.

## Sources actually used

- `CANONICAL_GENERIC_RECONSTRUCTION.md`, CG0–CG8, read in full: the complete winding quotient, its endomorphism ring, the canonical unit, prime norms, and original-zeta return measure. Its original Connes–Consani source and exact author-source locators are retained there.
- `TWISTOR_DEGREE_DERIVATION.md`, TD3–TD4 and TD8, read in full for the integral sphere cohomology, its degree action, both signed source components, and the finite-characteristic fixed-point calculation. The calculation below restates the relevant proof rather than importing a conclusion called purity.
- `ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md`, RZ8 and RZ10–RZ11, read in full: the actual multiplier \(a^s\), its full source factor \(a^{1/2}\), all multiplicity jets, and the reflected Weil form. RZ5 supplies its proved zero-isolating representatives. This note uses that proved receiving space, not an assumed spectral object.
- No claim is made here to have read Deligne's original author TeX or to reconstruct Deligne's proof. The elementary finite-field comparison has the weight convention \(|\lambda|=p^{w/2}\), with its actual weights calculated below.

## IC1. The integral ring recovered from the complete winding object

Retain the complete CC generic group and its finite subgroup:
\[
G=\langle T,J,\epsilon:
TJ=JT,\ T\epsilon=\epsilon T,\ J\epsilon=\epsilon J,
\ J^2=\epsilon,\ \epsilon^2=1\rangle,
\qquad H=\langle J\rangle,\qquad L_{\mathrm w}=G/H.
\tag{IC1.1}
\]
All source commutation relations remain displayed, including those also implied by \(\epsilon=J^2\). CG2–CG3 prove that \(G\cong\mathbb Z\times C_4\) and \(L_{\mathrm w}\) is infinite cyclic, retaining \(1\to H\to G\to L_{\mathrm w}\to1\). The subscript here distinguishes the winding group from the spectral operator below.

Let
\[
R=\operatorname{End}_{\mathrm{Ab}}(L_{\mathrm w}),\qquad
(f\oplus g)(x)=f(x)g(x),\quad (f\odot g)(x)=f(g(x)).
\tag{IC1.2}
\]
An endomorphism is exactly a power map \([n]:x\mapsto x^n\), with \(n\in\mathbb Z\). Indeed its value on a generator determines every value, and is a unique power of that generator. Choosing the inverse generator leaves the exponent unchanged. Thus
\[
R\cong\mathbb Z,\qquad [a]\oplus[b]=[a+b],\quad
[a]\odot[b]=[ab],\quad \mathbf1_R=[1]=\operatorname{id}_{L_{\mathrm w}}.
\tag{IC1.3}
\]
The nonnegative submonoid \(R_+\) consists of the successive sums of this identity, including the zero endomorphism. For nonzero \(f=[n]\in R_+\), define
\[
d(f)=|L_{\mathrm w}/f(L_{\mathrm w})|=n.
\tag{IC1.4}
\]
Representatives are the first \(n\) powers of any generator. Division of exponents proves that they exhaust the quotient without repetition. In particular
\[
d(f\odot g)=d(f)d(g),\qquad d(\mathbf1_R)=1.
\tag{IC1.5}
\]
This is a proved integrality statement: every counting endomorphism has an integer degree and every positive prime degree is a finite quotient cardinality. It makes no assertion that eigenvalues of a different representation of these degrees are algebraic integers.

## IC2. The exact map from the counting operators to the original-zeta action

Use the original-zeta receiving object from RZ. Let \(\mathcal B\) be the entire functions rapidly decreasing vertically in each bounded real strip, with seminorms
\[
b_{A,M}(F)=\sup_{|\operatorname{Re}s|\le A}
(1+|\operatorname{Im}s|)^M|F(s)|.
\tag{IC2.1}
\]
Let \(\mathscr Z\) be the set of distinct actual nontrivial zeros of the original \(\zeta\), and \(m_\rho\) their full multiplicities. The closed ideal is
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every }\rho\in\mathscr Z,\ 0\le j<m_\rho\},
\qquad\mathcal Q=\mathcal B/\mathcal I.
\tag{IC2.2}
\]
The prior global synthesis proves that this is the quotient of the original arithmetic source by its closed image, with the full multiplier
\[
F_0(s)=\frac{s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)}8
\tag{IC2.3}
\]
retained in the source comparison. Formula (IC2.3) is not a replacement for \(\zeta\): the full endpoint, Gamma and trivial-zero comparison belongs to that proof. Only the actual nontrivial-zero ideal (IC2.2) is used for the receiving calculation here.

Write \(L_\zeta[F]=[sF(s)]\). For every real \(a>0\), RZ8 defines the continuous invertible operator
\[
T_a[F]=[a^sF(s)],\qquad a^s=\exp(s\log a).
\tag{IC2.4}
\]
Here \(\log a\) is real. Direct multiplication proves
\[
T_aT_b=T_{ab},\qquad T_1=I,\qquad T_a^{-1}=T_{1/a}.
\tag{IC2.5}
\]
The exact continuity estimate before passage to the quotient is
\[
b_{A,M}(T_aF)\le\max(a^A,a^{-A})b_{A,M}(F).
\tag{IC2.6}
\]
The multiplier is entire and nowhere zero, so it preserves every vanishing order in (IC2.2). Taking infima over representatives gives the same bound for quotient seminorms. The source Mellin transform and its inverse comparison are
\[
\mathcal Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},
\qquad
\mathcal M^{-1}T_a\mathcal Mk(u)=a^{1/2}k(u/a).
\tag{IC2.7}
\]
Substituting \(u=av\) into the integral proves this identity with both powers retained. In the multiplier sense, RZ writes \(a^{L_\zeta}=T_a\); it does not require convergence of an operator power series.

The requested canonical map out of the positive counting degrees is therefore
\[
(R_+\setminus\{0\},\odot)\longrightarrow
\operatorname{Aut}_{\mathrm{cont}}(\mathcal Q),\qquad
f\longmapsto T_{d(f)}.
\tag{IC2.8}
\]
Equations (IC1.5) and (IC2.5) prove the homomorphism property, including the unit. No arbitrary orientation or preassigned prime label is needed. The full source ring is retained; (IC2.8) states which of its operations this particular receiving map preserves.

## IC3. The integral group algebra carrying the arithmetic action

Let \(\mathbb Q_{>0}^{\times}\) be the multiplicative group of positive rational numbers. Define
\[
\Lambda=\mathbb Z[\mathbb Q_{>0}^{\times}]
=\left\{\sum_{r\in S}a_r b_r:
 S\subset\mathbb Q_{>0}^{\times}\text{ finite},\ a_r\in\mathbb Z\right\},
\quad b_rb_t=b_{rt},\quad 1_\Lambda=b_1.
\tag{IC3.1}
\]
Different symbols \(b_r\) are a free additive basis; coefficients of equal symbols are added. Multiplication is the displayed finite convolution, hence associative, commutative and distributive, with identity \(b_1\). Negative coefficients are additive inverses. This constructs the ring directly.

Unique prime factorization gives the exact identification
\[
\Lambda\cong\mathbb Z[b_p,b_p^{-1}:p\text{ prime}],
\qquad b_r=\prod_p b_p^{v_p(r)},
\tag{IC3.2}
\]
where only finitely many integer valuations \(v_p(r)\) are nonzero. All primes, including two, occur.

The original arithmetic action extends to the unital ring homomorphism
\[
\Phi:\Lambda\longrightarrow\operatorname{End}_{\mathrm{cont}}(\mathcal Q),
\qquad
\Phi\left(\sum_{r\in S}a_r b_r\right)
=\sum_{r\in S}a_r T_r.
\tag{IC3.3}
\]
Additivity holds term by term. Multiplying two finite sums and using \(T_rT_t=T_{rt}\) proves multiplicativity, and \(\Phi(b_1)=I\). Each image is continuous because
\[
b_{A,M}\left(\sum_{r\in S}a_r r^sF(s)\right)
\le\left(\sum_{r\in S}|a_r|\max(r^A,r^{-A})\right)b_{A,M}(F).
\tag{IC3.4}
\]
The same estimate passes to the quotient. We assert continuity of every represented operator; no topology on the abstract finite-support ring \(\Lambda\) is implicit in this statement. No injectivity of \(\Phi\) is needed or asserted.

There are now two exact maps, with different domains of preserved operations:
\[
\begin{array}{rcll}
R\cong\mathbb Z&\longrightarrow&\Lambda,&[n]\longmapsto n b_1,
\quad\text{a unital ring homomorphism};\\
R_+\setminus\{0\}&\longrightarrow&\Lambda^\times,&[n]\longmapsto b_n,
\quad\text{a multiplicative-monoid homomorphism}.
\end{array}
\tag{IC3.5}
\]
The first is injective because the \(b_1\)-coefficient of \(n b_1\) is \(n\). Their represented images are respectively
\[
\Phi(n b_1)=nI,
\qquad \Phi(b_n)=T_n=n^{L_\zeta}.
\tag{IC3.6}
\]
For example \(b_2\ne2b_1\) already in the free additive basis. The difference is not erased in the actual receiving quotient. On any actual zero block \(\mathcal Q_\rho\), RZ8 proves the eigenvalue of \(T_2\) is \(2^\rho\). Since \(0<\operatorname{Re}\rho<1\),
\[
|2^\rho|=2^{\operatorname{Re}\rho}<2.
\tag{IC3.7}
\]
Thus \(T_2\ne2I\). The nontrivial-zero set is nonempty, independently of RH; the source quotient used here includes its proved nonzero isolating blocks. Consequently (IC2.8) cannot be an additive extension of the identity map on \(R\): such an extension would give \(T_2=T_1+T_1=2I\), contradicting (IC3.7).

This pinpoints the integrality transfer rather than discarding the relation between the two objects. The full map is (IC3.5) followed by (IC3.3), and its scalar and multiplicative inputs are explicitly distinct.

## IC4. What integrality of the group algebra does, and does not, assert

An endomorphism of a finite-rank free abelian group has an integer matrix in an integral basis. Expanding \(\det(XI-A)\) by permutations yields a monic polynomial with integer coefficients; every complex eigenvalue annihilates this polynomial. This proves that such an eigenvalue is an algebraic integer.

In contrast, the word integral in the coefficient ring \(\Lambda=\mathbb Z[\mathbb Q_{>0}^{\times}]\) does not assert that each \(b_p\) is integral over its scalar subring \(\mathbb Zb_1\). In fact it is not. If a monic relation of positive degree existed, it would have the form
\[
b_p^d+a_{d-1}b_p^{d-1}+\cdots+a_0b_1=0,
\qquad a_j\in\mathbb Z.
\tag{IC4.1}
\]
But \(b_p^j=b_{p^j}\), and the positive rationals \(1,p,\ldots,p^d\) are distinct. The free additive basis in (IC3.1) makes the coefficient of \(b_{p^d}\) on the left equal to one, a contradiction. This proves the precise algebraic distinction without a spectral assumption.

On an actual zero block, with full multiplicity \(m=m_\rho\), the represented action is
\[
T_p|_{\mathcal Q_\rho}
=p^\rho\sum_{j=0}^{m-1}\frac{(\log p)^j}{j!}N_\rho^j,
\qquad N_\rho^m=0,
\tag{IC4.2}
\]
and its characteristic polynomial is exactly
\[
\det(XI-T_p|_{\mathcal Q_\rho})=(X-p^\rho)^m.
\tag{IC4.3}
\]
The nilpotent terms have not been removed; their diagonal is zero and their full coefficients remain (IC4.2). Neither CG's integral counting ring nor the representation (IC3.3) proves that the coefficients of (IC4.3) are integers, or that \(p^\rho\) is an algebraic integer. No finite-rank invariant integral lattice for these blocks has been constructed in these calculations. This is a record of the exact established property, not an assertion that such a lattice or a different weight construction is impossible.

## IC5. An actual finite-field comparison, with every point count retained

Fix a rational prime \(p\), including \(p=2\), and consider the projective line over \(\mathbb F_p\). For every \(r\ge1\), its \(\mathbb F_{p^r}\)-points consist of the \(p^r\) affine elements and the point at infinity. Hence
\[
\#\mathbb P^1(\mathbb F_{p^r})=1+p^r.
\tag{IC5.1}
\]
Equivalently, the morphism \(f_p:[x:y]\mapsto[x^p:y^p]\) over \(\overline{\mathbb F}_p\) has these fixed-point counts for all powers: in its affine chart, \(f_p^r\) fixes the roots of \(z^{p^r}-z\). The derivative is \(-1\), giving \(p^r\) distinct roots, and infinity is fixed.

Here is an integral constants-and-divisors realization of its degree-zero and degree-two cohomological action. Let
\[
M=\mathbb Ze_0\oplus\mathbb Ze_2,
\qquad e_0\cdot e_0=e_0,
\quad e_0\cdot e_2=e_2\cdot e_0=e_2,
\quad e_2\cdot e_2=0.
\tag{IC5.2}
\]
The first class is the constant class. The second is the degree-one divisor class \([\infty]\). Over an algebraically closed field every divisor is a finite integer sum of points. The rational function \(z-a\) has divisor \([a]-[\infty]\); multiplying its integer powers shows every divisor of degree \(d\) is equivalent to \(d[\infty]\). Principal divisors have degree zero, by counting numerator and denominator zeros including infinity. Thus the divisor class group is exactly \(\mathbb Z[\infty]\), proving the integral second summand directly.

The same ring is the full integral singular cohomology of \(\mathbb P^1(\mathbb C)\): its sphere cell decomposition has a cell in degrees zero and two and none in degree one, and the square of a degree-two class vanishes because degree four is absent. This gives the integral comparison package conventionally denoted \(H^0\oplus H^2\). In the finite-field cohomological notation the second summand is the Tate class \(\mathbb Z_\ell(-1)\), for \(\ell\ne p\); the Frobenius convention here is the one entering point-count traces and acting by \(p\) on that untwisted degree-two class. The elementary calculation uses the displayed constants and divisor pullback; it does not require reconstructing the general étale comparison theorem.

The pullback of a constant is that constant. In the local parameter \(w=1/z\) at infinity, \(f_p\) sends \(w\) to \(w^p\), so \(f_p^*[\infty]=p[\infty]\). Therefore the full action is
\[
F_pe_0=e_0,\qquad F_pe_2=pe_2,
\qquad F_p=\begin{pmatrix}1&0\\0&p\end{pmatrix}.
\tag{IC5.3}
\]
Its trace on every iterate is exactly \(1+p^r\), matching (IC5.1), and its characteristic polynomial and determinant factor are
\[
\det(XI-F_p)=X^2-(1+p)X+p,
\quad
\det(I-tF_p)=(1-t)(1-pt).
\tag{IC5.4}
\]
Both eigenvalues are integers. All extension-field point counts are present. Their full generating function is
\[
Z(\mathbb P^1/\mathbb F_p,t)
=\exp\left(\sum_{r\ge1}\frac{1+p^r}{r}t^r\right)
=\frac1{(1-t)(1-pt)}.
\tag{IC5.5}
\]
This is an identity of formal power series and of analytic functions for \(|t|<1/p\): expand separately \(-\log(1-t)\) and \(-\log(1-pt)\), retaining both terms. It is not an identification of (IC5.5) with the original Riemann zeta function.

For connection with the already calculated actual CC signed sphere maps, TD8 has \(z\mapsto z^p\) for \(p\equiv1\pmod4\), and \(z\mapsto-1/z^p\) for \(p\equiv3\pmod4\). The latter fixed-point equation in the odd reciprocal iterates is \(z^{p^r+1}=-1\), with exactly \(p^r+1\) distinct roots. Its degree action and all counts are therefore precisely the same (IC5.3)–(IC5.5). TD8 requires odd \(p\) for that signed source lift. The present projective-line Frobenius example itself includes two; it is not an unproved extension of that odd source lift.

## IC6. Its degree-p pairing and its exact weights

Let \(\operatorname{tr}(e_0)=0\) and \(\operatorname{tr}(e_2)=1\), and define the integral bilinear form by extracting the top-degree coefficient:
\[
B(x,y)=\operatorname{tr}(xy),\qquad
B(ae_0+be_2,ce_0+de_2)=ad+bc.
\tag{IC6.1}
\]
Its matrix and exact degree relation are
\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
F_p^{\mathsf T}JF_p=pJ.
\tag{IC6.2}
\]
The determinant of \(J\) is \(-1\), so the integral pairing is perfect. Direct evaluation gives
\[
B(e_0+e_2,e_0+e_2)=2,\qquad
B(e_0-e_2,e_0-e_2)=-2.
\tag{IC6.3}
\]
Thus its real signature is \((1,1)\). The multiplier \(p\) pairs the eigenvalues \(1\) and \(p\); it does not make both eigenvalues have modulus \(\sqrt p\).

The complete degree filtration is
\[
W_{-1}M=0,\quad W_0M=W_1M=\mathbb Ze_0,
\quad W_2M=M.
\tag{IC6.4}
\]
This records the proved cohomological degrees in (IC5.2), rather than assigning an unknown sector a desired degree. The associated graded degree-zero action is \(1\), and the degree-two action is \(p\). Their absolute values are exactly
\[
|1|=p^{0/2},\qquad |p|=p^{2/2}.
\tag{IC6.5}
\]
They are pure of weights zero and two, respectively, in the finite-field weight convention. The direct sum is not pure of weight one. Its degree-one cohomology vanishes in this calculation. This is consistent with, and is not a violation of, the purity assertion for each specified cohomological degree.

There is also no positive-definite Hermitian form \(K\) on \(M\otimes\mathbb C\) having this same degree-p similitude. Evaluating \(K(F_pe_0,F_pe_0)=pK(e_0,e_0)\) would give \((p-1)K(e_0,e_0)=0\). Since \(p>1\), this forces \(K(e_0,e_0)=0\), incompatible with positive definiteness on the nonzero vector \(e_0\). This explicit calculation identifies the role of the cohomological sector and its form. It does not assert that positivity cannot be obtained on a different, correctly constructed weight-one object.

## IC7. The exact map from the counting ring to the comparison package

The preceding integral package can be built canonically over the already reconstructed ring \(R\): take \(R e_0\oplus R e_2\) and, for each nonzero \(f\in R_+\), put
\[
\mathcal F_f(ae_0+be_2)=ae_0+(f\odot b)e_2.
\tag{IC7.1}
\]
In the canonical coordinates (IC1.3), \(f=[n]\) gives \(\operatorname{diag}(1,n)\), not a chosen numerical coordinate at \(\tau\). Associativity of composition gives
\[
\mathcal F_f\mathcal F_g=\mathcal F_{f\odot g},\qquad
\mathcal F_{\mathbf1_R}=I.
\tag{IC7.2}
\]
The pairing \(B_R(ae_0+be_2,ce_0+de_2)=a\odot d\oplus b\odot c\) obeys
\[
B_R(\mathcal F_fx,\mathcal F_fy)=f\odot B_R(x,y).
\tag{IC7.3}
\]
For \(f=[p]\), applying \(R\cong\mathbb Z\) gives exactly the degree-p relation (IC6.2), with no altered multiplier. Thus the same canonical unit and recovered prime norms have an explicit integral cohomological representation whose actual weight pieces are zero and two. The representation supplies a precise comparison of integrality and weight. It is not a model of the full original-zeta receiving quotient, nor is it a claim that the CC programme has only these pieces.

## IC8. The actual original-zeta pairing has its own precise integral-indexed degree relation

Let \(\rho^\#=1-\overline\rho\). On \(\mathcal Q\), the full source-derived Weil form is
\[
W([F],[G])=\sum_{\rho\in\mathscr Z}m_\rho
\overline{F(\rho^\#)}G(\rho).
\tag{IC8.1}
\]
The previous source calculation proves absolute convergence and Hermitian symmetry. Since \(\overline{\rho^\#}+\rho=1\), the actual unshifted arithmetic action satisfies, for every real \(a>0\),
\[
W(T_ax,T_ay)=aW(x,y),\qquad
W(T_px,T_py)=pW(x,y)\quad\text{when }a=p.
\tag{IC8.2}
\]
Every zero and every multiplicity is retained in this equality. The numerical norm \(p=|L_{\mathrm w}/[p]L_{\mathrm w}|\) is exactly its multiplier. This is the concrete meeting point between the global counting ring and the spectral pairing.

On a reflected pair of distinct actual zeros, put \(\lambda=p^\rho\), \(\mu=p^{\rho^\#}\). Then
\[
\overline\lambda\mu=p,
\qquad |\lambda|=p^{\operatorname{Re}\rho},
\qquad |\mu|=p^{1-\operatorname{Re}\rho}.
\tag{IC8.3}
\]
The exact isolating representatives give matrix \(\left(\begin{smallmatrix}0&m_\rho\\m_\rho&0\end{smallmatrix}\right)\) on the two constant-jet coordinates. These statements describe what the actual formula would record at such a zero; they do not invent a zero or discard any prime. Higher jets remain the full nilpotent structure (IC4.2), even where the ordinary trace pairing has a radical.

The weighted adjoint relation also determines an exact coefficient-domain enlargement. Set
\[
\Lambda_{\mathbb Q}=\mathbb Q[\mathbb Q_{>0}^{\times}],\qquad
\Phi_{\mathbb Q}\left(\sum_{r\in S}c_r b_r\right)
=\sum_{r\in S}c_r T_r,
\quad c_r\in\mathbb Q,
\tag{IC8.4a}
\]
where \(S\) is finite. This explicitly extends \(\Phi\) from (IC3.3). The same finite-convolution proof establishes its unital ring homomorphism property, and (IC3.4) with \(|c_r|\) proves continuity of every image operator. On \(\Lambda_{\mathbb Q}\), the assignment
\[
b_r^{\star}=r\,b_{1/r},\qquad a^{\star}=a\ (a\in\mathbb Q)
\tag{IC8.4}
\]
is an involution: \((b_r^\star)^\star=r(1/r)b_r=b_r\), and multiplication is respected because \(rt\,b_{1/(rt)}=(r b_{1/r})(t b_{1/t})\). The form satisfies
\[
W(\Phi_{\mathbb Q}(A)x,y)
=W(x,\Phi_{\mathbb Q}(A^\star)y),
\qquad A\in\Lambda_{\mathbb Q}.
\tag{IC8.5}
\]
For a monomial this is \(W(T_rx,y)=W(x,rT_{1/r}y)\), obtained from (IC8.2) and invertibility. Rational coefficients are real, so conjugate-linearity in the first argument and linearity in the second give exactly the displayed equality for finite rational sums.

This rational enlargement is the smallest unital subring of \(\Lambda_{\mathbb Q}\) containing \(\Lambda\) and preserved by this specified weighted involution. To prove minimality, let \(A\) be any such subring. For every prime \(p\), the monomial \(b_{1/p}\) belongs to \(\Lambda\subseteq A\). Stability under \(\star\) and closure under multiplication give
\[
(b_{1/p})^\star b_{1/p}
=\left(\frac1p b_p\right)b_{1/p}
=\frac1p b_1\in A.
\tag{IC8.6}
\]
Every positive integer denominator is a finite product of prime powers. Multiplying the corresponding scalar elements in (IC8.6), and then multiplying by an arbitrary integer scalar, proves \(\mathbb Q b_1\subseteq A\). Since \(A\) also contains every \(b_r\), multiplication supplies \(c_r b_r\) for every rational \(c_r\), and finite addition supplies every element of \(\Lambda_{\mathbb Q}\). Hence \(A=\Lambda_{\mathbb Q}\). Conversely, (IC8.4) directly preserves \(\Lambda_{\mathbb Q}\), so this ring attains the asserted minimum.

In particular \(\Lambda\) itself is not preserved: the \(b_p\)-coefficient of \((b_{1/p})^\star\) is \(1/p\), which is not an integer. Equations (IC8.4a)–(IC8.6) construct and characterize the object required to retain the full weighted adjoint symmetry in this exact group-algebra presentation. This does not rule out integral arithmetic geometry, a different integral realization, or a pairing valued in an integral Tate object; those are not the scalar-valued coefficient presentation classified here.

## IC9. What the complete spectrum detects

CG7 proves that the complete normed prime spectrum, including its unit atom and every prime-power repetition, determines
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}
=\prod_p(1-p^{-s})^{-1},\qquad\operatorname{Re}s>1,
\tag{IC9.1}
\]
with absolute convergence. Its proved meromorphic continuation is unique. Consequently an actual nontrivial zero, wherever located, belongs to the analytic function determined by that same complete prime data. It would not be an additional prime omitted by the counting process. The whole prime spectrum determines the whole analytic function, including a possible off-critical zero; uniqueness alone does not tell us the location of that zero.

This last statement has a direct logical proof. If two meromorphic functions had the same complete series in (IC9.1), they would coincide on the open half-plane and hence throughout the connected continuation domain by the meromorphic identity theorem. Their zero divisors, with multiplicities, would therefore coincide. The argument contains no inequality or equality restricting the real parts of those zeros. The constructed original-zeta receiver strengthens the detection statement: its full joint arithmetic action has a block of dimension \(m_\rho\) for each actual zero, with coefficients (IC4.2). Such a zero is detected there, not missing from the reconstructed function.

The proved chain is therefore complete at the following levels: the source supplies the unique counting identity; its full endomorphism ring has integral degrees and prime norms; those degrees act through the explicit integral group algebra; the actual original-zeta quotient receives that action with every zero and multiplicity; and the Weil pairing has exactly the same prime norm as its similitude multiplier. The projective-line calculation identifies why integrality, complete counts and a degree-p pairing do not by themselves specify a weight-one sector. None of these calculations asserts a counterexample to the user's full geometric programme, or an RH resolution.
