# The finite-corner multiplier map and its Hilbert-module realization

## 1. The source statement and the question it answers

Bruce Blackadar, *K-Theory for Operator Algebras*, first edition (1986), §15.9, printed p.156, constructs covariance in the ideal variable for stable extension classes. Given a homomorphism \(g:B_1\to B_2\) with \(B_1\) sigma-unital, he forms \(H_{B_1}\otimes_g B_2\), embeds it as a complemented submodule of \(H_{B_2}\), and uses the induced stabilized multiplier and corona maps. Here \(H_B=\ell^2(\mathbb N_0,B)\). The construction does not require \(g\) itself to be nondegenerate. It also does not assert an extension \(M(B_1)\to M(B_2)\) restricting to an arbitrary \(g\) in unchanged coordinates. The exact historical page was read, rather than inferred from a secondary description.

The stabilization theorem used there is Blackadar's Theorem 13.6.2, printed p.131. That page credits G. G. Kasparov for the theorem and J. A. Mingo and W. J. Phillips for the proof presented in the book. Kasparov's original Theorem 2, printed pp.138–139 of his 1980 paper, was also read. The [source trail](HUMAN_SOURCE_TRAIL.md) gives precise verification levels and antecedents.

The programme's actual map has an explicit multiplier extension. We prove it and construct its precise relation to the tensor-module operation. This calculation concerns the formulas in `19b_global_place_balancing_conjecture.tex` and the constant-fibre multiplier formulas in `19d_stable_to_natural_extension_morphism.tex`; their inspected versions are pinned in the [correction record](CORRECTION_RECORD.json).

## 2. Original objects and fixed corners

Retain the original algebra

\[
 J=C_0(\mathbb R)\otimes\mathcal K(\ell^2(\mathbb N_0)),
 \qquad \mathcal V=\{\infty\}\cup\{\text{rational primes}\}.
\]

Fix the original bijection \(\nu:\mathcal V\to\mathbb N_0\). With

\[
 \kappa(j,k)=\frac{(j+k)(j+k+1)}2+k,
 \quad S_je_k=e_{\kappa(j,k)},\quad s_v=1\otimes S_{\nu(v)}\in M(J),
\]

we have \(s_v^*s_w=\delta_{vw}1\). Indeed, writing \(N=j+k\), the values of \(\kappa\) on that diagonal are the consecutive integers from \(N(N+1)/2\) to \((N+1)(N+2)/2-1\). Thus \(\kappa\) is bijective, each \(S_j\) is an isometry, and distinct ranges are orthogonal.

For the original finite prime set \(P\), put

\[
 V_P=P\cup\{\infty\},\qquad B_P=\bigoplus_{v\in V_P}J,
 \qquad p_P=\sum_{v\in V_P}s_vs_v^*.
\]

The projection \(p_P\) is proper: choose \(w\notin V_P\). Then \(p_Ps_w=0\) and \(s_w^*s_w=1\). All sums over \(V_P\) below are finite.

The source hypothesis is met explicitly. Set \(h_n(t)=\min(1,\max(0,n+1-|t|))\), let \(q_n\) project onto \(e_0,\ldots,e_n\), and put \(e_n=h_n\otimes q_n\). These positive contractions form a countable approximate identity of \(J\): multiplication converges on elementary tensors by uniform convergence on compact subsets in the first factor and finite-rank approximation in the second; density and contractivity extend the conclusion to \(J\). Their finite diagonal copies form a countable approximate identity of \(B_P\), proving sigma-unitality without identifying that property with separability in general.

## 3. Multipliers, support and coronas

Define

\[
 \mu_P(b)=\sum_v s_vb_vs_v^*,\qquad
 \overline\mu_P(m)=\sum_v s_vm_vs_v^*,
 \quad m\in M(B_P)=\bigoplus_vM(J).
\]

Products of multipliers with elements of \(J\) lie in \(J\), so the first formula lands in \(J\); the second lands in \(M(J)\). Orthogonality gives

\[
 \overline\mu_P(m)\overline\mu_P(n)
 =\sum_{v,w}s_vm_vs_v^*s_wn_ws_w^*
 =\sum_v s_vm_vn_vs_v^*=\overline\mu_P(mn),
\]

and preservation of adjoints follows by taking adjoints term by term. Moreover

\[
 s_v^*\overline\mu_P(m)s_v=m_v.
\]

Consequently both maps are injective homomorphisms, and \(\overline\mu_P\) extends \(\mu_P\). Its unit is sent to \(p_P\), not to \(1\).

This extension is strictly continuous. For a strictly convergent net \(m_{v,\lambda}\to m_v\) and \(b\in J\),

\[
 (\overline\mu_P(m_\lambda)-\overline\mu_P(m))b
 =\sum_v s_v(m_{v,\lambda}-m_v)(s_v^*b)\longrightarrow0
\]

in norm, since \(s_v^*b\in J\). Likewise

\[
 b(\overline\mu_P(m_\lambda)-\overline\mu_P(m))
 =\sum_v (bs_v)(m_{v,\lambda}-m_v)s_v^*\longrightarrow0.
\]

Strict density of \(B_P\) in \(M(B_P)\) proves uniqueness among strictly continuous extensions: for any contractive approximate identity \(e_\lambda^P\) of \(B_P\), \(me_\lambda^P\to m\) strictly, and two such extensions agree on every \(me_\lambda^P\).

For a contractive approximate identity \(e_\lambda\) of \(J\), the diagonal approximate identity of \(B_P\) satisfies

\[
 \mu_P((e_\lambda)_v)\longrightarrow p_P
 \quad\text{strictly in }M(J).
\]

In particular, \(\mu_P\) is degenerate as a map into \(J\). Explicitly, if \(0\ne c\in J\) and \(w\notin V_P\), then \(b=s_wc\ne0\), while \(\mu_P((e_\lambda)_v)b=0\) for every \(\lambda\). The existence of the multiplier map was established by its formula, not by an inapplicable nondegeneracy assertion.

Write \(Q(B)=M(B)/B\). Since \(\overline\mu_P(B_P)\subset J\), there is an induced map

\[
 \dot\mu_P:Q(B_P)\longrightarrow Q(J),\qquad
 \dot\mu_P([m])=[\overline\mu_P(m)].
\]

It is injective: if \(\overline\mu_P(m)\in J\), then compression by \(s_v^*\) and \(s_v\) gives \(m_v\in J\) for every \(v\), hence \(m\in B_P\). Multiplication and adjoints descend from the already proved identities.

## 4. The exact tensor-module unitary

Let \(E=B_P\otimes_{\mu_P}J\), the completion after quotienting the null space of the balanced algebraic tensor product with inner product

\[
 \langle b\otimes c,d\otimes e\rangle=c^*\mu_P(b^*d)e.
\]

The formula

\[
 U(b\otimes c)=\mu_P(b)c
\]

respects balancing, since \(\mu_P(bd)c=\mu_P(b)\mu_P(d)c\). Its inner-product identity is exactly

\[
 U(b\otimes c)^*U(d\otimes e)=c^*\mu_P(b^*d)e.
\]

Thus it extends to an isometry into \(J\). Its range lies in \(p_PJ\). Conversely, for \(x=p_Px\), the vectors \(\mu_P((e_\lambda)_v)x\) belong to its algebraic range and converge to \(x\). Since the range of a complete isometry is closed, \(U:E\to p_PJ\) is onto. A surjective inner-product-preserving module map is adjointable with adjoint its inverse, so \(U\) is a Hilbert-module unitary.

On elementary tensors, for \(m\in M(B_P)\),

\[
 U((mb)\otimes c)=\mu_P(mb)c
 =\overline\mu_P(m)\mu_P(b)c.
\]

Hence the multiplier action under \(U\) is multiplication by \(\overline\mu_P(m)\). The submodule \(p_PJ\) is complemented by the adjointable projection \(x\mapsto p_Px\). Extending the action by zero on \((1-p_P)J\) gives that same multiplier, because \(\overline\mu_P(m)=p_P\overline\mu_P(m)p_P\). This realizes the source's complemented-submodule construction in the original corner coordinates.

## 5. Stabilization, including boundedness and the compact ideal

The componentwise version of \(U\) is a unitary

\[
 U_\infty:H_{B_P}\otimes_{\mu_P}J
 \longrightarrow\ell^2(\mathbb N_0,p_PJ).
\]

For finite sequences, the inner-product calculation is the sum of those in §4. Finite sequences are dense in both modules, and finite vectors in the target are approximated componentwise by the range of \(U\). This proves the assertion for the completions. Let \(i\) be inclusion of this target in \(H_J\); its adjoint is coordinatewise multiplication by \(p_P\).

If \(T\in\mathcal L(H_{B_P})\), its tensor action \(T\otimes1\) is well defined and bounded with norm at most \(\|T\|\). To verify the bound rather than assume it, put \(D=(\|T\|^2-T^*T)^{1/2}\). For finite \(\xi=\sum_r x_r\otimes c_r\), the difference between \(\|T\|^2\langle\xi,\xi\rangle\) and the inner product of its image is

\[
 \sum_{r,s}c_r^*\mu_P(\langle Dx_r,Dx_s\rangle)c_s\ \geq\ 0.
\]

The Gram matrix is positive; its entrywise image under a homomorphism is positive, so the displayed inequality follows. It shows that the action respects null vectors and extends boundedly. Its adjoint is \(T^*\otimes1\), as is checked on elementary tensors.

Therefore

\[
 \Psi(T)=iU_\infty(T\otimes1)U_\infty^*i^*
 \in\mathcal L(H_J)
\]

is a homomorphism: in products, the middle factor \(i^*i\) is the identity, and adjoints follow from the formula. If \(T_{ij}\in M(B_P)\) are the matrix entries of \(T\), then

\[
 \Psi(T)_{ij}=\overline\mu_P(T_{ij}).
\]

Indeed, for input coordinate \(j\) in the dense set \(\mu_P(B_P)J\), this is the intertwining formula of §4; on its orthogonal complement both sides vanish. Density gives equality everywhere. In particular,

\[
 \Psi(m\otimes e_{ij})=\overline\mu_P(m)\otimes e_{ij}.
\]

The map sends compact module operators into compact module operators. For finitely supported \(x,y\in H_{B_P}\), the rank-one operator \(\theta_{x,y}\) is a finite matrix with entries \(x_i y_j^*\in B_P\). Its image is a finite matrix with entries in \(J\), hence compact. General \(x,y\) follow by truncation, using \(\|\theta_{x,y}\|\leq\|x\|\|y\|\), and all compact operators follow by norm closure.

Kasparov's Theorem 1 and its consequence, printed p.137, identify these adjointable algebras with the multipliers of the respective compact-operator algebras. Thus \(\Psi\) is precisely a stabilized multiplier map of the type used in Blackadar §15.9, and it descends to the stabilized coronas. Its rank-one matrix corner recovers \(\overline\mu_P\). No universal unstabilized extension principle is used.

## 6. The original constant-unit-fibre map

Retain the original nonempty compact unit fibre \(K_P\) and declared coordinate isomorphism

\[
 \chi_P:\mathfrak I_P^{\mathrm s}\xrightarrow{\cong} C(K_P)\otimes J.
\]

The actual map in chapter 19d is \(\jmath_P(b)=\chi_P^{-1}(1\otimes b)\). It is nondegenerate: multiplication by \(1\otimes e_\lambda\) converges to the identity on elementary tensors on both sides; density and contractivity give convergence on every element of \(C(K_P)\otimes J\).

For \(m\in M(J)\), define \(1\otimes m\) by its two actions on continuous \(J\)-valued functions:

\[
 ((1\otimes m)a)(k)=m a(k),\qquad (a(1\otimes m))(k)=a(k)m.
\]

They are bounded by \(\|m\|\), preserve continuous functions, and satisfy the double-centralizer identity \(a(k)(m b(k))=(a(k)m)b(k)\). They therefore define a multiplier. These formulas prove multiplicativity, preservation of adjoints and the unit, and extension of \(b\mapsto1\otimes b\). Conjugating by \(\chi_P\) defines \(\overline\jmath_P\).

For clarity, the continuity estimate needed here is valid on every norm-bounded strictly convergent net. If \(m_\lambda\to m\) strictly and \(\sup_\lambda\|m_\lambda\|<\infty\), the range of a continuous function \(a:K_P\to J\) is norm compact. A finite norm net for this range reduces the two uniform products to finitely many strict seminorms, with approximation error bounded by \((\sup\|m_\lambda\|+\|m\|)\) times the net radius. Thus \((1\otimes m_\lambda)a\to(1\otimes m)a\) and their right-hand analogues uniformly. This argument does not make an unproved uniform-boundedness assertion about arbitrary nets.

Evaluation has an explicit multiplier extension. For \(N\in M(C(K_P)\otimes J)\), fix \(k\in K_P\) and define its left and right actions on \(b\in J\) by

\[
 L_k(N)b=(N(1\otimes b))(k),\qquad bR_k(N)=((1\otimes b)N)(k).
\]

These are bounded double centralizers: insert constant functions for the two factors in the multiplier identity and evaluate. Thus they determine a multiplier \(\overline\epsilon_k(N)\in M(J)\). To check multiplication on general products, observe that for every \(a\in C(K_P,J)\),

\[
 (Na)(k)=\overline\epsilon_k(N)a(k),\qquad
 (aN)(k)=a(k)\overline\epsilon_k(N).
\]

For an elementary \(a=f\otimes b\), this follows because the central multiplier \(f\otimes1\) commutes with \(N\): their commutator annihilates the essential ideal, hence is zero. Finite sums and norm density prove the formula for all \(a\). Applying it twice proves multiplicativity of \(\overline\epsilon_k\); taking adjoints proves preservation of adjoints. It sends ideal elements to their values in \(J\), so it descends to coronas.

Finally \(\overline\epsilon_k(1\otimes m)=m\). After transport by \(\chi_P\), this gives left inverses for \(\jmath_P\), \(\overline\jmath_P\) and \(\dot\jmath_P\); all three are split injective.

## 7. Composition in the Busby formula

The composite multiplier map exists explicitly and has support projection \(\overline\jmath_P(p_P)\):

\[
 (\overline\jmath_P\,\overline\mu_P)(m)
 =\chi_P^{-1}\!\left(1\otimes\sum_v s_vm_vs_v^*\right).
\]

Here \(\chi_P^{-1}\) denotes its multiplier transport. For the quotient maps \(\pi\), the equality

\[
 \pi_{\mathfrak I}\overline\jmath_P\overline\mu_P
 =\dot\jmath_P\dot\mu_P\pi_{B_P}
\]

holds on every representative. Hence the corona map of the composite is exactly \(\dot\jmath_P\dot\mu_P\), as used in chapter 19d. This verifies that multiplier/corona step; it does not purport to reprove the chapter's separate Green-module and linking-algebra compatibility arguments.

The historical source statement should therefore retain its sigma-unital-source hypothesis and explain the tensor-module realization. The explicit \(\mu_P\) formula, its corona map and this composition remain valid. The source theorem and the original record are preserved, with the omitted construction now supplied.
