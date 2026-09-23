# Supported-zero inversion and the time-zero heat fibre

23 September 2026. This calculation proves the supported-zero inversion and specialization maps and their exact relation to the de Bruijn–Newman flow. It uses the original Split-Zero operations, retains the supported-zero prime and the supported Weil receiver, and proves the localization and specialization maps. It establishes no zero of the Riemann zeta function away from its critical line.

The heat-flow statements are checked against original author TeX: Brad Rodgers and Terence Tao, [*The De Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), introduction, equations `hoz`, `sas`, `phidef`, `htdef`, and Theorem `main`; Dave Platt and Tim Trudgian, [*The Riemann hypothesis is true up to 3·10¹²*, arXiv:2004.09765v1](https://arxiv.org/abs/2004.09765v1), subsection *The de Bruijn–Newman constant* and its corollary. Only the stated source ranges, not the full proofs of those literature theorems, were read for this calculation.

The original programme definition is repeated below. Its integer localization is already proved in [the original globalization note, theorem thm:frac-collapse](../supporting_sources/globalization_note.tex). The supported Weil formula used here is [SZW1–SZW4, SZW33–SZW35 and SZW44–SZW47](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/4a4238afc992e77aee83b97d38a1a63d283f540c/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md#L15). This note does not replace that formula by an unlabelled one.

## 1. Original multiplication and the two meanings of inverse

For a nonzero commutative unital ring A, define
\[
G(A)=\{\tau\}\sqcup A^\bullet,\qquad e=0_A^\bullet,\qquad 1_G=1_A^\bullet.
\tag{HZ1}
\]
The operations are
\[
a^\bullet+b^\bullet=(a+b)^\bullet,\quad
a^\bullet b^\bullet=(ab)^\bullet,\quad
\tau+x=x,\quad\tau x=\tau.
\tag{HZ2}
\]
In particular
\[
e^2=e,\quad ea^\bullet=e\ (a\in A),\quad e\tau=\tau,
\qquad e\ne\tau,\quad e\ne1_G.
\tag{HZ3}
\]
A unit of G(A) is exactly a supported unit of A. Indeed an inverse to a supported element cannot be tau, and the equation a^bullet b^bullet=1_G is exactly ab=1 in A. The product of tau with anything is tau. Consequently e has no inverse with product 1_G in G(A).

There is nevertheless a precise local inverse. The multiplicative submonoid
\[
eG(A)=\{\tau,e\}
\tag{HZ4}
\]
has identity e, and e is its own inverse with respect to that identity. It is also an inner inverse in the ambient monoid: eee=e. Its inclusion in G(A) preserves multiplication and addition, but does not send its identity e to 1_G. The corner identity and the ambient identity are different specified elements. This identifies the local inverse without erasing it or turning it into an ambient unit.

## 2. Inverting e globally retains precisely Boolean support

Let U={1_G,e}. In semiring localization, fractions satisfy
\[
(x,u)\sim(y,v)\quad\Longleftrightarrow\quad
\text{there exists }w\in U\text{ with }wvx=wuy.
\tag{HZ5}
\]
Every two fractions with supported numerators are equal: use w=e, after which both sides equal e. A fraction with numerator tau cannot equal one with supported numerator, because the two sides of the displayed relation then have different support. There are exactly two classes, and their operations are OR and AND. Thus
\[
G(A)[e^{-1}]\simeq\mathbb B=\{0,1\},\qquad
\chi(\tau)=0,\quad\chi(a^\bullet)=1\quad(a\in A).
\tag{HZ6}
\]
This is also the universal property directly. For a unital semiring map f with f(e) invertible, f(e)^2=f(e) implies f(e)=1. Then f(e)f(a^bullet)=f(e) implies f(a^bullet)=1 for every a. Since e+e=e, the target satisfies 1+1=1, so the unique unital map B→target sending its two elements to 0 and1 factors f. Conversely every such factorization inverts e. No arithmetic distinction survives this factorization; tau remains different from the supported class in B.

Arithmetic observation is instead
\[
\pi_A:G(A)\longrightarrow A,\qquad
\pi_A(\tau)=0,\quad\pi_A(a^\bullet)=a.
\tag{HZ7}
\]
It cannot factor through HZ6: e would have to map both to0, by HZ7, and to1, by HZ6 and unitality. A unital semiring map B→a nonzero ring also cannot exist, because 1+1=1 would give1=0 by cancellation. The joint map
\[
(\pi_A,\chi):G(A)\hookrightarrow A\times\mathbb B,\qquad
a^\bullet\mapsto(a,1),\quad\tau\mapsto(0,0)
\tag{HZ8}
\]
is injective and preserves both operations, as substitution verifies. This is the exact correspondence retaining the arithmetic amplitude together with support.

For A=Z the full spectrum is
\[
P_\tau\subsetneq P_e\subsetneq P_p,\qquad
P_\tau=\{\tau\},\quad P_e=\{\tau,e\},\quad
P_p=\{\tau\}\cup(p\mathbb Z)^\bullet.
\tag{HZ9}
\]
To prove exhaustion, any ideal containing a supported element contains e by multiplying by e; its supported amplitudes form an integer ideal, since multiplication by minus1 supplies inverses within that group. Such an ideal is {tau} union (nZ)^bullet. Primeness is exactly primeness of nZ. The remaining ideal {tau} is prime because a product is unsupported exactly when a factor is unsupported. The strict inclusions follow by their elements. Thus
\[
D(e)=\{P_\tau\},\qquad V(e)=\{P_e,P_p:p\text{ prime}\}.
\tag{HZ10}
\]
Inverting e restricts to D(e). It does not create a new arithmetic value at the point P_e: that point, and the entire closed arithmetic subspace V(e), are outside this open. HZ6 proves the ring-of-sections statement as well as the point calculation.

## 3. The heat parameter specializes to supported zero

Let R=C[t]. Evaluation at t=0 and inversion of t give the commutative square
\[
\begin{array}{ccc}
G(\mathbb C[t])&\longrightarrow&G(\mathbb C[t,t^{-1}])\\
\downarrow G(\operatorname{ev}_0)&&\downarrow\chi\\
G(\mathbb C)&\xrightarrow{\chi}&\mathbb B.
\end{array}
\tag{HZ11}
\]
The upper arrow is the localization at t^bullet: fractions with supported numerators have the ordinary Laurent fraction relation, while absent fractions stay absent. The left map is
\[
f(t)^\bullet\longmapsto f(0)^\bullet,\qquad
t^\bullet\longmapsto e,\qquad\tau\longmapsto\tau.
\tag{HZ12}
\]
The square is a pushout in commutative unital semirings. For compatible maps from the upper right and lower left into a target, the lower-left image of e must be a unit, since it equals the image of the unit t^bullet from the upper right. HZ6 gives a unique factorization from B. Every supported polynomial maps to1 in that factorization; its Laurent fractions do too. This verifies compatibility with the entire upper-right map and proves the pushout property.

The corresponding ring square has lower-right ring zero:
\[
\mathbb C[t,t^{-1}]\otimes_{\mathbb C[t]}\mathbb C=0,
\tag{HZ13}
\]
because t becomes both invertible and zero, so1=t t^{-1}=0. In HZ11 the supported Boolean fibre survives. Its arithmetic group completion is zero: the equality1+1=1 forces1=0 in every additive group receiver. These are exact maps of two different fibres, not an identification of the surviving supported point with an arithmetic nonreal root.

## 4. The actual heat family and its retained zero set

Use Rodgers–Tao's exact normalization
\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},
\tag{HZ14}
\]
\[
H_0(z)=\tfrac18\xi(\tfrac12+\tfrac{iz}{2}),\qquad
\xi(s)=\tfrac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{HZ15}
\]
HZ15 is the original author's formula `hoz` with `sas`. The following convergence and specialization argument is given explicitly here. For u≥0,
\[
|\Phi(u)|\le C e^{9u}e^{-(\pi/2)e^{4u}},
\tag{HZ16}
\]
where C is finite: factor e^{-(pi/2)e^{4u}} out of every exponential and bound the remaining n-series by the convergent sum of (2pi²n⁴+3pi n²)e^{-(pi/2)n²}. For |t|≤T and |z|≤Z the integrand, including any fixed number of its t and z derivatives, is bounded by a constant times
\[
(1+u)^m\exp(Tu^2+(9+Z)u-(\pi/2)e^{4u}).
\tag{HZ17}
\]
This is integrable: the negative exponential-in-u term eventually exceeds twice every displayed polynomial and linear positive term. Differentiation under the integral is justified on each compact set. It follows that H is entire jointly in (t,z),
\[
\partial_tH=-\partial_z^2H,\qquad
H_t\longrightarrow H_0\text{ locally uniformly as }t\to0.
\tag{HZ18}
\]
Let E_2 be the ring of entire functions on C² and E_1 the ring of entire functions on C. Restriction r:E_2→E_1 to t=0 is onto, with kernel tE_2. For the kernel assertion, an entire f satisfies
\[
f(t,z)-f(0,z)=t\int_0^1\partial_tf(st,z)\,ds;
\tag{HZ19}
\]
the integral is entire by uniform convergence on compact sets. Thus the exact HZ11 specialization extends to this analytic family. In particular
\[
G(r)(H^\bullet)=H_0^\bullet,\qquad
\widetilde H_t(z):=H_t(z)^\bullet\in G(\mathbb C),
\tag{HZ20}
\]
\[
\widetilde H_t(z)=e\iff H_t(z)=0,
\qquad\widetilde H_t(z)\ne\tau\text{ for every }(t,z).
\tag{HZ21}
\]
This retains every arithmetic zero as supported zero. On the other hand,
\[
\chi(\widetilde H_t(z))=1\quad\text{for every }(t,z).
\tag{HZ22}
\]
The last equality includes actual zeros and nonzeros alike. It cannot test whether a zero has a nonzero imaginary part. HZ21, with the amplitude coordinate in HZ8 retained, tests precisely that property; no zero is lost in the full supported object.

## 5. A nonreal zero at time zero persists at positive times

The set of real times for which H_t has at least one nonreal zero is open. Here is the full local proof. Fix such a zero z_0 at a time t_0. H_{t_0} is not identically zero: at z=0 its defining integral is strictly positive for real t_0, since every summand of Phi is positive for u≥0, as 2pi n²e^{4u}>3. Choose a closed disk D about z_0 of radius smaller than |Im z_0|, and small enough that H_{t_0} has no boundary zeros. Its isolated-zero property allows this choice. The positive boundary minimum m=min_{∂D}|H_{t_0}| exists. By HZ17–HZ18, for real t sufficiently close to t_0 one has sup_{∂D}|H_t-H_{t_0}|<m. The contour homotopy H_{t_0}+s(H_t-H_{t_0}), 0≤s≤1, has no boundary zeros, so its winding number around0 is constant. The argument principle gives the same positive number of zeros in D for H_t as for H_{t_0}. All these zeros are nonreal because D avoids the real axis.

Consequently real-rootedness cannot fail only at time0 while holding for all sufficiently small positive times. This statement uses the actual analytic family, not an algebraic convention for its zero value. The known bound t≥0.2 by itself says nothing about all sufficiently small positive times; that interval has not been filled in by this argument.

The literature gives a finite Lambda with real-rooted times exactly [Lambda,infinity), and Rodgers–Tao proves Lambda≥0. Thus
\[
\mathrm{RH}\iff\Lambda=0,
\qquad
\neg\mathrm{RH}\iff\Lambda>0.
\tag{HZ23}
\]
An arithmetic disproof through this route would therefore establish a nonreal zero of the actual H_t at some t≥0, equivalently a strictly positive lower bound for Lambda. HZ6 or HZ11 supplies no such root or bound: their right-hand support maps identify all supported amplitudes.

## 6. Two exact heat families showing what support forgets

For sigma in {−1,+1}, set
\[
P_t^\sigma(z)=z^2+\sigma-2t.
\tag{HZ24}
\]
Both satisfy the same equation ∂_tP=−∂_z²P, since the two sides equal−2. At t=0, P^− has roots±1 and P^+ has roots±i. Their real-rooted times are respectively [−1/2,infinity) and [1/2,infinity), directly from z²=2t−sigma. At collision time t=sigma/2 their coordinate rings are both C[z]/(z²), with the generator retained as a nonzero nilpotent. Every value of either family becomes1 under HZ6. Thus the same supported-zero inversion and the same dual-number collision occur with opposite time-zero root behavior. These two families compute the relation between support and root location explicitly. Their parameters and zero sets remain separate from those of the Riemann heat family.

## 7. The supported Weil receiver remains present

The assertion that every additive map G(A)→an abelian group identifies e and tau is correct with that domain: tau maps to0; e+1^bullet=1^bullet gives the image of e equal to0 by cancellation. Its extension to all real-valued observations on supported objects is false. On the real vector space freely generated by the distinct points e and tau, the coordinate maps
\[
\delta_e([e])=1,\quad\delta_e([\tau])=0,
\qquad
\delta_\tau([e])=0,\quad\delta_\tau([\tau])=1
\tag{HZ25}
\]
are real-linear and distinguish them. They are functions on labelled points, not additive characters of the original semiring. The map x↦[x] into this free vector space is not semiring-additive. HZ25 specifies the exact changed domain, rather than claiming an exception to cancellation in an abelian group.

The programme's actual SZW receiver uses such retained labels. For its test h and Mellin transform M_h(s)=integral h(v)e^{−(s−1/2)v}dv, write m_j=M_h(j), j=0,1, and let L be the finite support lattice. SZW33–SZW34 says
\[
\begin{aligned}
\boldsymbol B_L&=(m_0+m_1)\mathbf e_{1_L}
+m_0\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol Z_L&=Z(h)\mathbf e_{1_L},\\
\boldsymbol D_L&=(P_{\rm fin}(h)-A_\infty(h))\mathbf e_{1_L}
+m_0\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol B_L-\boldsymbol Z_L&=\boldsymbol D_L.
\end{aligned}
\tag{HZ26}
\]
Here Z(h) is the complete zero-divisor trace, not the heat time or a replacement polynomial. The scalar map epsilon_top extracts the top coordinate. The map epsilon_all sums every coordinate. Their difference on D_L is exactly (|L|−1)m_0; it is not declared zero. On B_L their values are m_0+m_1 and |L|m_0+m_1. On Z_L they agree. These identities follow by applying the stated linear maps to every term of HZ26. The linked SZW source gives the full theta, test, trace and analytic proofs of HZ26. This calculation preserves that established identity and does not infer it from the spectrum alone.

There is also an exact multiplicative-algebra corner. Let
\[
\Gamma_A=\mathbb Z[(G(A),\cdot)]/([\tau]),\qquad E=[e].
\tag{HZ27}
\]
Its abelian-group basis is [a^bullet], a∈A; no additive relations from A are imposed. E²=E and E[a^bullet]=E give EΓ_A=ZE. The mutually inverse ring maps
\[
\Gamma_A\longleftrightarrow E\Gamma_A\times(1-E)\Gamma_A,
\qquad x\mapsto(Ex,(1-E)x),\quad(u,v)\mapsto u+v
\tag{HZ28}
\]
follow from E(1−E)=0 and E+(1−E)=1. The unit of the first factor is E; it is not the unit of Γ_A. Inverting E gives
\[
\Gamma_A[E^{-1}]\simeq E\Gamma_A\simeq\mathbb Z,
\quad \sum_a c_a[a^\bullet]\mapsto\sum_a c_a,
\quad\ker=(1-E)\Gamma_A.
\tag{HZ29}
\]
By contrast the arithmetic ring map alpha:Γ_A→A sends [a^bullet]→a and E→0. Its factorization through the second factor follows from alpha(Ex)=0. Thus E is invertible in the support corner, whose integer coefficients retain multiplicities, while the arithmetic factor lies in the exact kernel of E-localization. Boolean semiring localization and this integer linearization are connected by the contracted monoid-algebra construction; they are not the same additive object. None of these maps removes the independent label functions in HZ25–HZ26 from the unlocalized programme.

## 8. Scope of the conclusion

The supported-zero prime is present, its local and localized inverses have been specified, and the full heat specialization preserves arithmetic zero exactly as e. These calculations do not establish failure of RH at time0. They identify the exact loss of arithmetic amplitude when supported zero is inverted globally, and prove analytically that failure at time0 would persist at nearby positive times. The unlocalized programme still retains the amplitudes, support labels, zero-divisor trace and nilpotent data needed for further work. 
