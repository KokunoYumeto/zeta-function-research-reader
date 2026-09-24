# Canonical Mellin scale, the actual zero characters, and the sphere involutions

24 September 2026. This is a global derivation, with no finite-range zero experiment. It continues M1–M9 in PRIME_MONODROMY_STACKED_HISTORY.md. The source element tau retains the user's Z_1 presence and no integer parity; no addition at tau is used. Auxiliary convolution algebras of functions and their complex coefficients are named as such. They are not new operations on source tau.

The user specifically requests the involution pictures in Thomas Ponweiser, *Computer Algebra and Analysis: Complex Variables Visualized*, revised 17 June 2014. Printed pages 15–19, PDF pages 29–33, including Figures 1.2–1.3, were read and visually inspected. This explicit PDF request governs this reading; it does not change the original-TeX practice for the Connes papers. The disk corpus index returned no matching title entry. The source CC.tex is the byte-verified author source of Connes–Consani, [The Absolute Twistor Line and the Geometry of the compactified Spec Z, 2609.00299v1](https://arxiv.org/abs/2609.00299v1). The E-map and Fourier convention are retained from Alain Connes, [2602.04022v1](https://arxiv.org/abs/2602.04022v1), with the factor correction proved in C6. No priority claim is made for the convolution-character method.

## G1. The family of scales and its exact Fourier defect

Let S_0^even be the even Schwartz functions on R satisfying f(0)=0 and integral_R f=0. Use the Fourier transform Ff(y)=integral_R f(x) exp(2*pi*i*x*y) dx. On even functions F squared is the identity. For real c define

\[
E_c f(u)=u^c\sum_{n\ge1}f(nu),\qquad
U_{a,c}f(x)=a^{-c}f(x/a),\qquad V_a k(u)=k(u/a),\quad a,u>0.
\tag{G1.1}
\]

The original sum, its measure and all powers are retained. Substitution gives E_c U_(a,c)=V_a E_c. Poisson summation on the full integer lattice gives

\[
f(0)+2\sum_{n\ge1}f(nu)
=u^{-1}\left(Ff(0)+2\sum_{n\ge1}Ff(n/u)\right).
\tag{G1.2}
\]

Both displayed endpoint terms are zero on this stated domain. Consequently

\[
E_c f(u)=u^{2c-1}E_c(Ff)(1/u).
\tag{G1.3}
\]

Thus the untwisted inversion I k(u)=k(1/u) intertwines F and E_c exactly for c=1/2. To prove necessity rather than merely sufficiency, use the retained nonzero self-Fourier Gaussian polynomial f_0 from C6. E_c f_0 is continuous and nonzero on an open interval, since its Mellin transform is not identically zero. If both the untwisted equation and G1.3 hold, u^(2c-1)=1 on that interval, forcing 2c-1=0. The inversion defect at any other real scale is precisely the multiplier u^(2c-1), not an omitted term.

Independently, direct change of variables gives

\[
\|U_{a,c}f\|_{L^2(dx)}^2=a^{1-2c}\|f\|_{L^2(dx)}^2.
\tag{G1.4}
\]

Unitary dilation for every a>0 therefore forces the same real c=1/2. If a complex exponent is allowed, unitarity fixes Re(c)=1/2 only; its imaginary part is a phase character. Requiring the untwisted Fourier inversion in G1.3 removes that phase as well. These calculations identify the scale from the original measure and Fourier operation. They do not infer purity of a quotient spectrum from unitarity of the source space.

Write E=E_(1/2). The exact Mellin convention throughout this note is

\[
Mk(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{G1.5}
\]

For other c the same arithmetic parameter s is retained by using the exponent s-c with E_c. Changing the display of this exponent never changes the original zeta argument.

## G2. The convolution algebra and the source ideal

Let A be the space in M9: k is smooth on R_>0 and all seminorms

\[
p_{N,j}(k)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j k(u)|
\tag{G2.1}
\]

are finite, for nonnegative integers N,j. In the coordinate v=log(u), K(v)=k(e^v) and every derivative decays faster than every exponential in both directions. Define

\[
(k*l)(u)=\int_0^\infty k(a)l(u/a)\frac{da}{a},\qquad
k^\#(u)=\overline{k(1/u)}.
\tag{G2.2}
\]

The logarithmic convolution is ordinary additive convolution. The inequalities exp(N|v|)<=exp(N|w|)exp(N|v-w|) and integral exp(-|w|)dw=2 give a bound of each weighted derivative supremum of K*L by twice the corresponding weighted supremum of L times a weighted supremum of K with index N+1. Reversing the factors bounds either derivative placement. This proves convergence, differentiation under the integral and joint continuity. Fubini with the same bounds proves associativity and commutativity. Substitution v->-v proves that # is a continuous conjugate-linear involution preserving the convolution product.

The image E(S_0^even) is an ideal of A. The exact lift of k*E(f) is

\[
f_k(x)=\int_0^\infty k(a)a^{-1/2}f(x/a)\frac{da}{a},
\qquad E(f_k)=k*E(f).
\tag{G2.3}
\]

For the Schwartz seminorm q_(M,j)(f)=sup_x (1+|x|)^M |f^(j)(x)| one has

\[
q_{M,j}(a^{-1/2}f(\cdot/a))
\le a^{-j-1/2}\max(1,a)^M q_{M,j}(f).
\tag{G2.4}
\]

The weighted rapid decay of k at both endpoints makes the integral of every right side finite. Hence f_k is Schwartz, even, and f_k(0)=0. Absolute integration and x=ay give integral f_k=(integral k(a)a^(1/2) da/a)(integral f)=0. For fixed u>0, absolute interchange in E follows by a Schwartz bound on the sum of |f(nu/a)|: for a>=u it is at most a constant times a/u, while for a<=u it is at most a constant times (a/u)^M, M>1. Multiplication by |k(a)|a^(-1/2) is integrable in both ranges. This proves G2.3 on its entire stated domain.

Conjugation commutes with E, and G1.3 at c=1/2 gives

\[
(E f)^\#=E(\overline{Ff}).
\tag{G2.5}
\]

The Fourier transform preserves the even Schwartz domain and exchanges its two vanishing endpoints. Thus the image is #-stable. Its closure J in A is a closed convolution ideal, stable under #, and the quotient

\[
Q=A/J
\tag{G2.6}
\]

is a commutative locally convex involutive algebra. The dilations V_a preserve J and descend to Q by G1.1. No identity element of A or Q has been asserted. V_a is the convolution multiplier induced by a translated Dirac measure; it is not generally an algebra homomorphism, since (V_a k)*(V_a l)=V_(a^2)(k*l).

## G3. Every continuous character is a full Mellin observation

A character means a nonzero continuous complex-linear multiplicative functional. We classify all such characters on A without presupposing a zeta spectrum. Work in logarithmic coordinates and let T_b K(v)=K(v-b). Choose G with chi(G)!=0. The identity

\[
(T_bK)*G=K*(T_bG)
\tag{G3.1}
\]

implies chi(T_bK)=psi(b)chi(K), where psi(b)=chi(T_bG)/chi(G). It follows by applying this twice and taking K=G that psi(b+c)=psi(b)psi(c), psi(0)=1, and psi has no zeros. Translation is smooth in the topology of A: difference quotients converge in each weighted derivative seminorm by the integral mean-value formula and a bound on the next two derivatives. Thus psi is differentiable. Differentiating its group law gives psi'(b)=lambda psi(b), with lambda=psi'(0), hence psi(b)=exp(lambda b).

In A itself,

\[
K*G=\int_{\mathbb R}K(b)T_bG\,db.
\tag{G3.2}
\]

This integral converges in every seminorm: the seminorm of T_bG is at most exp(N|b|) times that of G, and K decays faster than exp(-(N+1)|b|). Completeness follows directly by taking weighted uniform limits of all derivatives and compatibility under differentiation; hence the integral belongs to A. Applying the continuous character to G3.2 and dividing by chi(G) proves

\[
\chi(K)=\int_{\mathbb R}K(b)e^{\lambda b}db=Mk(1/2+\lambda).
\tag{G3.3}
\]

Conversely every complex lambda gives a continuous functional by the same weighted bounds, and Fubini proves multiplicativity. It is nonzero by a compactly supported bump with a compensating phase. Distinct lambda give distinct functionals because their exponential densities differ on some open interval. Thus s->(k->Mk(s)) is a bijection from C to the continuous character set of A.

## G4. The quotient characters are exactly the original nontrivial zeros

M9 proves that every actual nontrivial zero rho of the original zeta annihilates E(S_0^even), and hence J. Conversely, a character of Q pulls back to an A-character, so G3 identifies it with evaluation at a unique s. It annihilates the particular element k_0=E(f_0), whose full transform is

\[
Mk_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{G4.1}
\]

This is an evaluated transform with every factor retained, not a replacement for the original zeta. We check its exceptional points explicitly. At s=1 the factor s-1 cancels the simple original pole of residue 1 and gives Mk_0(1)=1/8. At s=0, Gamma(s/2) has leading term 2/s, zeta(0)=-1/2, and Mk_0(0)=1/8. At s=-2m, m>=1, the Gamma factor has residue 2(-1)^m/m!, while the original zeta has a simple zero. The retained product value is

\[
Mk_0(-2m)=\frac{m(2m+1)(-1)^m\pi^m}{2m!}\zeta'(-2m)
\ne0.
\tag{G4.2}
\]

The simplicity and nonzero derivative here follow directly from the original functional equation: sin(pi*s/2) has a simple zero, while 2^s pi^(s-1) Gamma(1-s) zeta(1-s) is finite and nonzero at -2m. At all other points outside the nontrivial-zero set the retained factors are finite and nonzero, using the classical zero-free regions Re(s)>=1 and the reflected region, as in the programme's original-zeta source. Therefore the zeros of G4.1 are exactly the original nontrivial zeros with their full multiplicities.

It follows that

\[
\boxed{\operatorname{Char}_{\rm cont}(Q)
=\{[k]\mapsto Mk(\rho):\zeta(\rho)=0,\ 0<\Re\rho<1\}.}
\tag{G4.3}
\]

There are no extra continuous characters in this constructed quotient. This assertion does not by itself identify the entire quotient with an unrestricted product of local jets, nor assume simplicity. Every original trivial zero and pole remains in the comparison G4.1–G4.2 and the full Weil receiver.

## G5. The exact involution, scaling, and Weil trace on this quotient

Changing u to 1/u in G1.5 gives, with every conjugation retained,

\[
M(k^\#)(s)=\overline{Mk(1-\bar s)},\qquad
M(V_a k)(s)=a^{s-1/2}Mk(s).
\tag{G5.1}
\]

Thus the actual character involution is rho->rho#=1-bar(rho), and dilation has character value a^(rho-1/2). M9 already retains all differentiated jet terms. These are relations on the actual original-zeta quotient Q, established through E, rather than relations on an unrelated unit circle representation.

For k,l in A define the trace pairing

\[
B_Q([k],[l])=\sum_\rho m_\rho
\overline{Mk(\rho^\#)}Ml(\rho).
\tag{G5.2}
\]

It is well defined on Q since J annihilates every displayed value. For uniform convergence in the whole strip, write v=log u and integrate by parts j times in Mk(s). The L1 norms of derivatives of exp((Re(s)-1/2)v)K(v) are bounded uniformly for 0<=Re(s)<=1 by finitely many p_(N,j), taking N>=2. Thus |Mk(s)|<=C_j(1+|Im(s)|)^(-j), uniformly in that strip. The known unconditional zero count O(R log(R+2)), retained from the original-zeta reconstruction, proves absolute convergence and continuity of G5.2. Reflection preserves multiplicity, so the form is Hermitian. G5.1 gives exact dilation invariance because

\[
\overline{a^{\rho^\#-1/2}}a^{\rho-1/2}=1.
\tag{G5.3}
\]

No positivity is used in this calculation. The map [k]->(Mk(rho)) has values in the existing ell²(Z,m) space of NI5 and intertwines B_Q with its original reflection form. This proves the connecting map to the previously constructed signed trace; the NI local radical calculation is not rediscovered as a new result here.

The original compact Weil tests sit here by the precise orientation

\[
k_f(u)=f(-\log u),\qquad Mk_f(s)=H_f(s),\qquad
k_{f^\#*g}=k_f^\#*k_g,
\tag{G5.4}
\]

where f#(v)=bar(f(-v)) and H_f(s)=integral f(v)exp(-(s-1/2)v)dv. Substitution v=-log u proves the first two identities. The change a=e^(-w) in convolution proves the third, including the reversed integration endpoints. Therefore B_Q([k_f],[k_g]) is exactly W_zeta(f#*g), with all endpoint, Gamma and history-weight terms M7.1–M7.3 retained by that equality. Tensoring this map with the two distinct coefficient records [tau], [1] and every support basis vector gives M9.7 and WU1–WU8. It does not identify the two records or remove the supported-zero contribution.

## G6. The book's disk/sphere maps and the precise CC comparison

Ponweiser's equations (1.20)–(1.21) give the inverse stereographic map

\[
P^{-1}(z)=\frac{(2\Re z,2\Im z,|z|^2-1)}{1+|z|^2},\quad
P^{-1}(\infty)=(0,0,1),\qquad P(X,Y,Z)=\frac{X+iY}{1-Z}.
\tag{G6.1}
\]

Its numerator norm squared is (1+|z|²)², and substitution proves that the maps are inverse, including the two poles. The disk |z|<1 maps to the southern hemisphere Z<0; its boundary maps to the equator. Example 1.41 gives the involution f(z)=1/z. Direct substitution in G6.1 yields

\[
P^{-1}(1/z)=\operatorname{diag}(1,-1,-1)P^{-1}(z).
\tag{G6.2}
\]

This is the half-turn in Figure 1.2. The zero and infinity are exchanged. The fixed points are z=+1,-1. Example 1.43's modified Cayley map Phi(z)=(iz+1)/(z+i) satisfies Phi(Phi(z))=1/z by direct rational substitution; it carries the upper half-plane to the disk. It is the quarter-turn shown in Figure 1.3. It is not being silently identified with an order-two transformation.

Complex conjugation C(z)=bar(z) acts on the sphere by diag(1,-1,1), while S(z)=-z acts by diag(-1,-1,1). The new CC paper's real structure is sigma=S f C. Consequently

\[
\sigma(z)=-1/\bar z,\quad P^{-1}\sigma=-P^{-1};\qquad
\kappa(z)=1/\bar z,\quad
P^{-1}\kappa=\operatorname{diag}(1,1,-1)P^{-1}.
\tag{G6.3}
\]

These are exact compositions, not claimed holomorphic conjugacies. Sigma is antipodal and has no fixed sphere point. Kappa is equatorial reflection and fixes the complete unit circle. The source minus sign is the explicitly retained S operation between them. This proves the relation of the book's involution to the CC real structure instead of treating their differing fixed sets as an absence of a relation.

## G7. Keeping the prime weight on the sphere

For every prime p define the bijection from the extended z-plane to the unit sphere

\[
P_p^{-1}(z)=
\frac{(2\sqrt p\Re z,\ 2\sqrt p\Im z,\ |z|^2-p)}{|z|^2+p},
\qquad
P_p(X,Y,Z)=\sqrt p\,\frac{X+iY}{1-Z}.
\tag{G7.1}
\]

This is the explicitly invertible comparison P^(-1)(z/sqrt p); the original unscaled z is returned by P_p. Squaring the numerator gives 4p|z|²+(|z|²-p)²=(|z|²+p)². The weight-one involution iota_p(z)=p/bar(z) acts by Z->-Z with X,Y unchanged. For the original coordinate z=p^s, s=sigma_0+it, put v=(sigma_0-1/2)log p and theta=t log p. Direct substitution yields the full exact point

\[
P_p^{-1}(p^s)=
\left(\frac{\cos\theta}{\cosh v},\frac{\sin\theta}{\cosh v},\tanh v\right).
\tag{G7.2}
\]

The phase theta, prime factor log p and all signs are retained. The sphere norm is 1 for every s, while its third coordinate has the exact inverse

\[
\Re s-\frac12=\frac{\operatorname{artanh}(Z)}{\log p}.
\tag{G7.3}
\]

For finite s its value satisfies -1<Z<1. Thus the precise purity datum retained by the sphere is its latitude: |p^s|²=p exactly when Z=0. This is a global identity for every s and every prime, not a plot of selected zeros. The two-prime injective strip receiver C5 retains the full original s when its phase periods are also retained. No point of this sphere is declared to be the user's primitive tau; G6–G7 compare the geometric realizations supplied by the papers.

## G8. What has now been established

The scale 1/2 is derived from the original Fourier/measure comparison, not chosen to move zero locations. The quotient Q has exactly the original nontrivial-zero continuous characters, and its source-derived involution is exactly critical-line reflection. The actual global Weil form descends to Q with its full support records and is dilation invariant. The book's sphere carries the same purity defect as a recoverable latitude. Neither the common radius of the sphere nor the proved dilation invariance establishes that this form is positive. Its sign remains the actual programme problem, with the exact receiving maps G5.2–G5.4 now supplied.
