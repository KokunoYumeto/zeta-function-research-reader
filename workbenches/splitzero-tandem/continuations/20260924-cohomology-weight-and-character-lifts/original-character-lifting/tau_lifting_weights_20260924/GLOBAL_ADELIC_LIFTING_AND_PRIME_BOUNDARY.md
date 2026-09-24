# The complete adelic boundary and its oriented source comparison

24 September 2026. GAP0–GAP9. This calculation continues the actual source-coefficient comparison, retaining every derived prime-boundary degree. The independent companion proofs are COMPLETE_GENERATOR_ENDPOINT_RETURN.md, GLOBAL_ENDPOINT_EXTENSION_RETURN.md and FULL_DERIVED_PRIME_BOUNDARY_REVIEW.md. No full τ purity theorem is asserted.

## GAP0. Source definitions, prerequisites and provenance

The complete user arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c, and the current correction rule USR-4322be19bff532cd, were reread with B1–B5 and P1–P5. They remain in the complete private corpus, with pasted assistant passages distinguished from user arguments. The full arithmetic reconstruction precedes the coefficient operations below. The notation remains \(Z_0\) for absence, \(Z_1\) for primitive presence \(\tau\) without \(Z_2\) parity, and the specified integer data with their \(Z_2\) parity. No source addition on \(\tau\) is introduced.

The group algebras, vector spaces, exterior powers, derivatives, quotients and Fourier transforms below belong to the already constructed arithmetic receiving spaces. Their relation to the source is the explicit DCP coefficient comparison. A statement about a selected receiving boundary is not automatically a statement about the entire τ geometry.

Human sources: Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068v1), and Alain Connes, Caterina Consani and Matilde Marcolli, [*The Weil proof and the geometry of the adeles class space*](https://arxiv.org/abs/math/0703392v1), for the original adelic construction. The exact received calculation is ABR1–ABR30 in CC_ADELIC_COINVARIANT_BRIDGE_INDEPENDENT.tex; its basis, moments, resolution and connecting representatives are proved there. Jean-Louis Koszul's resolution is used with its displayed differential, whose needed exactness is also recalled below. The original Connes–Consani sheaf is [*Schemes over \(\mathbb F_1\) and zeta functions*](https://arxiv.org/abs/0903.2024v3), §5: the source restrictions, Fourier graph, original dilation and mirror actions were reread in author TeX lines 1521–1667. The receiving source double and its faithful scalar extension are DCP1–DCP12.

Pierre Deligne's [*La conjecture de Weil. II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §§3.6.1–3.6.3, is the target comparison. The entire local invariant-cycle argument was reread in the retained French transcription, not represented as original author TeX. The present calculation supplies the full adelic maps and endpoint separation; it does not import his geometric weight bounds as assumptions.

## GAP1. The original receiving objects and all endpoint factors

Keep
\[
G=\mathbb Q_{>0}^{\times},\quad R=\mathbb C[G],\quad
\varepsilon(t_a)=1,\quad I_R=\ker\varepsilon,
\quad H=\mathcal S_{\rm even}(\mathbb R;\mathbb C),
\]
\[
m(h)=\left(h(0),\int_{\mathbb R}h(v)\,dv\right),\quad
M_0=\ker(\varepsilon\otimes m:R\otimes H\to\mathbb C^2),
\quad S=\ker m.
\tag{GAP1.1}
\]
Every tensor sum is algebraic. Let
\[
W_{\rm pr}=\bigoplus_{p\ {\rm prime}}\mathbb C\ell_p,
\qquad x_p=t_p-1,
\qquad B_n=\Lambda^n W_{\rm pr}\otimes\mathbb C^2\quad(n\ge1).
\tag{GAP1.2}
\]
The ordering in each wedge is the increasing order of the original primes. No prime is replaced by an unlabelled dimension.

The actual strong Mellin space is
\[
\mathcal A=\left\{k\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^jk(u)|<\infty
\text{ for every }N,j\ge0\right\}.
\]
Use all these seminorms and the original functions
\[
\mathcal E h(u)=u^{1/2}\sum_{r\ge1}h(ru),\qquad
F_k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u},
\quad Q=\mathcal A/\mathcal ES.
\tag{GAP1.3}
\]
OMS proves that \(\mathcal ES\) is closed on these original domains. Its original zeta relation is
\[
F_{\mathcal Eh}(s)=\zeta(s)\int_0^\infty h(v)v^{s-1}\,dv
\qquad(\Re s>1),
\tag{GAP1.4}
\]
continued with every endpoint and trivial-zero term as in OMS3–OMS4.

For \(c=\sum_a t_a\otimes h_a\in M_0\), set
\[
\Phi c=\sum_a h_a\in S,\qquad
Jc=2\mathcal E\Phi c.
\tag{GAP1.5}
\]
The factor 2 is the two-sign factor in the actual adelic sum. It is retained throughout. For every \(a>0\),
\[
\mathscr R_a(t_b\otimes h)=t_b\otimes h(\,\cdot/a),
\qquad W_a k(u)=a^{1/2}k(u/a).
\tag{GAP1.6}
\]
Then \(J\mathscr R_a=W_aJ\), by direct substitution. On endpoint coordinates the action is \(D_a=\operatorname{diag}(1,a)\): evaluation at zero is fixed and the integral changes by the retained factor \(a\).

## GAP2. One complex containing every derived prime degree

Define a cochain complex \(\mathscr C\) by
\[
\mathscr C^1=\mathcal A,\qquad
\mathscr C^{-k}=M_0\otimes\Lambda^kW_{\rm pr}\quad(k\ge0),
\qquad \mathscr C^j=0\quad(j\ge2).
\tag{GAP2.1}
\]
Its differential in degree zero is \(J\). For \(k\ge1\), its differential is the full Koszul differential
\[
d(c\otimes\ell_{p_1}\wedge\cdots\wedge\ell_{p_k})
=\sum_{i=1}^k(-1)^{i-1}x_{p_i}c\otimes
\ell_{p_1}\wedge\cdots\widehat{\ell_{p_i}}\cdots\wedge\ell_{p_k}.
\tag{GAP2.2}
\]
The products lie in \(M_0\). Two successive removals of distinct wedge indices have opposite signs, so \(d^2=0\) in negative degrees. In degree \(-1\), \(\Phi(x_pc)=0\), since \(\varepsilon(x_p)=0\); hence \(Jd=0\). These checks establish the whole cochain complex, including the join at degrees \(-1,0,1\).

For completeness, the underlying complex \(R\otimes\Lambda^\bullet W_{\rm pr}\) resolves the augmentation module \(\mathbb C\). For a finite set of primes, adjoining one variable \(t_p-1\) is the cone of its multiplication on the preceding Koszul complex. The preceding degree-zero quotient is a Laurent polynomial algebra in the remaining variables; multiplication by the next \(t_p-1\) is injective. Induction gives exactness in positive degrees. Every cycle and every coefficient uses a finite set of primes, so it is already a boundary in a finite such complex. Degree zero is the quotient setting every \(t_p=1\). This proves the infinite-prime statement without completing the exterior algebra.

Tensor the exact sequence
\[
0\to M_0\to R\otimes H\xrightarrow{\varepsilon\otimes m}\mathbb C^2\to0
\]
with each free resolution degree. The middle complex has only homology \(H\) in degree zero; the last has zero differential and terms \(\Lambda^kW_{\rm pr}\otimes\mathbb C^2\). The connecting sequence gives the ABR groups
\[
H^1(\mathscr C)=Q,\qquad H^{1-n}(\mathscr C)=B_n\quad(n\ge1).
\tag{GAP2.3}
\]
For \(n=1\), this uses \(\ker J/I_RM_0=B_1\), with the exact section in AC1. For \(n\ge2\), it is the connecting isomorphism just computed. OMS7A identifies the degree-one quotient with the same \(Q\), rather than a potentially different algebraic quotient.

## GAP3. The canonical whole-complex comparison

Define the original arithmetic derivations
\[
D_p\left(\sum_a c_at_a\right)=\sum_a c_av_p(a).
\]
They satisfy
\[
D_p(rs)=\varepsilon(r)D_p(s)+D_p(r)\varepsilon(s),
\quad D_p(x_q)=\begin{cases}1&p=q,\\0&p\ne q.\end{cases}
\tag{GAP3.1}
\]
Each input has only finitely many nonzero \(D_p\). At degree \(-k\), write a coefficient of a fixed wedge as \(c=\sum_i r_i\otimes h_i\in M_0\) and put
\[
\Gamma^{-k}(c\otimes\omega)
=\frac1{k+1}\sum_{p,i}D_p(r_i)
 (\ell_p\wedge\omega)\otimes m(h_i)\in B_{k+1}.
\tag{GAP3.2}
\]
This is a well-defined linear map on the indicated tensor product: its formula is bilinear in the original factors, and the finite sum of derivations defines a linear map on \(R\). In degree one put \(\Gamma^1=\pi_Q\).

Let \(\mathscr H\) have zero differential, degree-one term \(Q\), and degree \(1-n\) term \(B_n\). Then \(\Gamma:\mathscr C\to\mathscr H\) is a chain map. At the join \(\pi_QJ=0\). For a negative-degree differential, the derivation of \(x_pc\) is its \(p\)-th augmentation moment. All terms are multiples of
\(\sum_i\varepsilon(r_i)m(h_i)=0\), the defining condition of \(M_0\). Explicitly, moving the removed \(\ell_{p_i}\) back to its ordered position cancels the Koszul sign and gives \(k\) equal wedge terms times this zero moment. Thus \(\Gamma d=0\).

To compute its map on every cohomology group, choose a section of the two moments only to write a representative:
\[
h_0(v)=(1-2\pi v^2)e^{-\pi v^2},\quad
h_1(v)=2\pi v^2e^{-\pi v^2},\quad
\sigma(u_0,u_1)=u_0h_0+u_1h_1.
\]
The Gaussian integrals give \(m\sigma=\operatorname{id}\). For an ordered \(n\)-wedge \(\omega=\ell_{p_1}\wedge\cdots\wedge\ell_{p_n}\), the connecting cycle is
\[
z_{\omega,u}=\sum_{i=1}^n(-1)^{i-1}
 (x_{p_i}\otimes\sigma(u))\otimes
 \ell_{p_1}\wedge\cdots\widehat{\ell_{p_i}}\cdots\wedge\ell_{p_n}.
\tag{GAP3.3}
\]
It is a cycle because it is the differential of \((t_1\otimes\sigma(u))\otimes\omega\) in the middle resolution. Changing \(\sigma\) changes it by a boundary in the \(M_0\) complex. Each of its \(n\) terms maps under (GAP3.2) to \((1/n)\omega\otimes u\). Hence
\[
\Gamma^{1-n}[z_{\omega,u}]=\omega\otimes u.
\tag{GAP3.4}
\]
The factor \(1/n\) is the explicit inverse to those \(n\) equal receiving terms; no exterior term is discarded. Equations (GAP2.3)–(GAP3.4), and the identity on \(Q\), prove a canonical quasi-isomorphism on all degrees. With the convention \(V[r]^j=V^{j+r}\), it is
\[
\mathscr C\xrightarrow{\Gamma}
Q[-1]\oplus\bigoplus_{n\ge1}B_n[n-1].
\tag{GAP3.5}
\]
Each degree has its one displayed term. No convergence or interchange of infinite-degree sums is used.

The comparison commutes with every \(\mathscr R_a\), acting on \(B_n\) by \(\operatorname{id}_{\Lambda^nW_{\rm pr}}\otimes D_a\). The identity follows from \(m(R_ah)=D_am(h)\) in (GAP3.2). Full diagonal rational action \(t_b\) on the source has trivial action on the target: its extra derivative term is \(D_p(t_b)\sum_i\varepsilon(r_i)m(h_i)=0\). This is not a conflation of diagonal rational action with the independent spectral real dilation.

## GAP4. Full Fourier action, including the prime-wedge coefficients

Use the original adelic additive character with finite conductor \(\widehat{\mathbb Z}\), finite measure \(\operatorname{vol}(\mathbb Z_p)=1\), and real transform
\(\widehat h(\xi)=\int_{\mathbb R}h(v)e^{-2\pi iv\xi}\,dv\).
For \(c_a=1_{a\widehat{\mathbb Z}}\), its finite Fourier transform is
\(a^{-1}c_{a^{-1}}\). Indeed integrating a character on that compact subgroup is its Haar volume if the character is trivial, and zero otherwise by translating by an element where it is nontrivial. The annihilator is \(a^{-1}\widehat{\mathbb Z}\), and its original volume is \(a^{-1}\).

The real transform of \(h(v/a)\) is \(a\widehat h(a\xi)\). Consequently the complete factors in ABR's \(\Theta\) give
\[
\mathcal F\Theta(t_a\otimes h)=
a\,a^{-1}\Theta(t_{a^{-1}}\otimes\widehat h)
=\Theta(t_{a^{-1}}\otimes\widehat h).
\tag{GAP4.1}
\]
The displayed cancellation is justified by the exact original integral maps. Both Haar factors have been calculated.

Write \(\iota(t_a)=t_{a^{-1}}\). For an ordered prime set \(P\) of cardinality \(k\), put
\[
\mathcal F_k((r\otimes h)\otimes\ell_P)
=(-1)^k\left(\prod_{p\in P}t_p^{-1}\right)\iota(r)
 \otimes\widehat h\otimes\ell_P.
\tag{GAP4.2}
\]
This preserves \(M_0\): augmentation of the displayed monomial is one, and Fourier swaps the two endpoint coordinates. It commutes with (GAP2.2), because
\(\iota(x_p)=-t_p^{-1}x_p\); each removed wedge factor contributes exactly that multiplier. Applying it twice gives identity: inversion cancels the monomial, \((-1)^{2k}=1\), and the square of the real transform is identity on even functions.

In degree one put \(\mathcal F_{\mathcal A}k(u)=k(1/u)\). The original Poisson identity, with \(h(0)=\int h=0\), gives
\(J\mathcal F_0=\mathcal F_{\mathcal A}J\). Thus these operators give an involutive chain map on \(\mathscr C\).

Let \(S_2(u_0,u_1)=(u_1,u_0)\). Under (GAP3.2), the action on \(B_n\) is
\[
\Gamma^{1-n}\mathcal F_{n-1}
=(-1)^n(\operatorname{id}_{\Lambda^nW_{\rm pr}}\otimes S_2)
\Gamma^{1-n}.
\tag{GAP4.3}
\]
To prove it, \(D_p\iota(r)=-D_p(r)\) supplies one minus sign. The other \(n-1\) signs are in (GAP4.2). Differentiating the product of \(t_p^{-1}\) instead gives a multiple of the total augmentation moment, which is zero. The remaining moment is exactly \(m(\widehat h)=S_2m(h)\). This retains every finite monomial and wedge sign.

The original relation remains
\[
W_a\mathcal F_{\mathcal A}=a\mathcal F_{\mathcal A}W_{a^{-1}},
\qquad D_aS_2=aS_2D_{a^{-1}}.
\tag{GAP4.4}
\]
No half-weight twist replaces this action.

## GAP5. The exact map to the Connes–Consani coefficient complex

Use DCP's raw space \(A\), with
\[
\Sigma h(u)=2\sum_{r\ge1}h(ru),\quad
R_A b(u)=u^{-1}b(1/u),\quad
\mathcal T:\mathcal A\to A,\quad\mathcal T k(u)=2u^{-1/2}k(u).
\tag{GAP5.1}
\]
Its inverse is \(\mathcal T^{-1}b(u)=\tfrac12u^{1/2}b(u)\). Weighted Euler derivative estimates prove both are continuous on all defining seminorms, by the product rule and an increased integer weight index. They satisfy
\(\mathcal T\mathcal E=\Sigma\), \(\mathcal TW_a=T_a\mathcal T\), and \(\mathcal T\mathcal F_{\mathcal A}=R_A\mathcal T\).

The original Cech complex is
\[
D^0=V_+\oplus V_-,\quad V_\pm=S\oplus\mathbb C^2,\qquad D^1=A,
\]
\[
d_D((h,c_0,c_1),(g,d_0,d_1))=\Sigma h-R_A\Sigma g.
\tag{GAP5.2}
\]
Its mirror swaps chart coordinates in degree zero and is \(-R_A\) in degree one. The latter minus sign is the orientation of the ordered two-chart cover.

Record that orientation in the source by the one-dimensional receiving sign representation: keep the same spaces, differential and dilations of \(\mathscr C\), but let its mirror be \(-\mathcal F_k\) in degree \(-k\) and \(-\mathcal F_{\mathcal A}\) in degree one. Denote this oriented representation by \(\mathscr C^{\rm or}\). It changes neither \(\tau\) nor the source arithmetic; it explicitly supplies the sign required by the ordered Cech comparison. Its square is identity and it still commutes with the differential.

There is now the actual chain map
\[
\begin{aligned}
\mathfrak F^1(k)&=\mathcal T k,\\
\mathfrak F^0(c)&=((\Phi c,0,0),(-\widehat{\Phi c},0,0)),\\
\mathfrak F^{-k}&=0\quad(k\ge1).
\end{aligned}
\tag{GAP5.3}
\]
It preserves the differential: Poisson gives
\(R_A\Sigma\widehat h=\Sigma h\), so
\[
d_D\mathfrak F^0(c)=\Sigma\Phi c+R_A\Sigma\widehat{\Phi c}
=2\Sigma\Phi c=\mathcal T(2\mathcal E\Phi c)=\mathfrak F^1Jc.
\tag{GAP5.4}
\]
On a negative-degree boundary \(\Phi d=0\), proving the other chain identities. Fourier scaling proves equivariance in degree zero: \(\widehat{h(\,\cdot/a)}=a\widehat h(a\,\cdot)\), which is exactly DCP's minus-chart action. Equation (GAP5.1) gives degree-one equivariance.

For the mirror, \(\Phi\mathcal F_0=\widehat{\Phi}\) and \(\widehat{\widehat h}=h\) give
\[
\mathfrak F^0(-\mathcal F_0c)=((-\widehat{\Phi c},0,0),(\Phi c,0,0)),
\]
the chart swap of \(\mathfrak F^0c\). In degree one, \(\mathcal T(-\mathcal F_{\mathcal A})=-R_A\mathcal T\). Thus every sign in the comparison is proved.

The source of (GAP5.3) can also be checked by averaging. The plus-chart map has degree-zero component \(((2\Phi c,0,0),0)\) and degree-one component \(\mathcal T\). Conjugating by both mirrors gives degree-zero component \((0,(-2\widehat{\Phi c},0,0))\) and the same degree-one component. Their sum times the explicit coefficient \(1/2\) is (GAP5.3). This explains the orientation adjustment without discarding the original factor two.

On cohomology, \(H^1(\mathfrak F)\) is exactly the isomorphism induced by \(\mathcal T\) on the original quotient. In every degree at most zero its map is zero: negative target degrees vanish, and a degree-zero source cycle has \(\Phi c=0\) by injectivity of \(\mathcal E\). Its representative therefore maps to zero, not merely to an unspecified coboundary.

## GAP6. The complete comparison defect, with its connecting signs

Do not replace the preceding quasi-isomorphism in degree one by an equivalence of the entire complexes. Define the actual cochain cone
\[
\mathscr K^j=D^j\oplus(\mathscr C^{\rm or})^{j+1},\qquad
d_{\mathscr K}(d,c)=(d_Dd+\mathfrak F c,-d_{\mathscr C}c).
\tag{GAP6.1}
\]
The chain identity in GAP5 proves its differential squares to zero. Its long exact sequence, with the computed cohomology maps, gives
\[
H^0(\mathscr K)=H^0(D)
=\{(h,\widehat h):h\in S\}\oplus\mathbb C^4,
\]
\[
H^{-n}(\mathscr K)=B_n\quad(n\ge1),\qquad
H^j(\mathscr K)=0\quad(j\ge1).
\tag{GAP6.2}
\]
The degree-zero map is induced by \(d\mapsto(d,0)\). For the negative group, projection \((d,c)\mapsto c\) induces the indicated connecting isomorphism into \(H^{1-n}(\mathscr C)\). In degree \(-1\), \(c\) is a degree-zero cycle and \(\mathfrak F^0c=0\), so \((0,c)\) is its explicit cone cycle. For lower degrees the target \(D^j\) is zero, and the same representative works. This verifies the formula without choosing an unproved splitting of the entire cone.

The boundary action in \(\mathscr C^{\rm or}\), and hence in these negative cone groups, is
\[
\operatorname{id}_{\Lambda^nW_{\rm pr}}\otimes D_a,
\qquad
w|_{B_n}=(-1)^{n+1}\operatorname{id}_{\Lambda^nW_{\rm pr}}\otimes S_2.
\tag{GAP6.3}
\]
All prime labels and endpoint coordinates survive. The top Fourier graph and all four original endpoint lines also survive in \(H^0(\mathscr K)\).

## GAP6A. The entire comparison triangle has an explicit cohomology projection

The following strengthens GAP6: it constructs the full comparison, including a quasi-isomorphism for the cone, rather than only listing that cone's groups. It does not construct a section of the quotient map from the original test space to its spectral quotient.

For \(v=((h,c_0,c_1),(g,d_0,d_1))\in D^0\), define
\[
\Pi_0v=
\left(\left(\frac{h+\widehat g}{2},c_0,c_1\right),
\left(\frac{\widehat h+g}{2},d_0,d_1\right)\right).
\tag{GAP6A.1}
\]
Both source functions belong to the original \(S\). Fourier is a continuous involution on that space, so this is continuous. Its image belongs to \(H^0(D)=\ker d_D\), because the first function is the Fourier transform of the second. On that kernel it is identity. In particular, it retains all four endpoint coordinates.

The complementary component is exactly
\[
v-\Pi_0v=((a,0,0),(-\widehat a,0,0)),\qquad
a=\frac{h-\widehat g}{2}.
\tag{GAP6A.2}
\]
The displayed coefficient \(1/2\) retains both original chart contributions. This is an explicit projection in the receiving complex vector space, not an additive operation on primitive \(Z_1/\tau\).

Let \(\mathscr H_D\) have \(H^0(D)\) in degree zero, \(Q_{\rm raw}\) in degree one, and zero differential. Put
\[
\Pi_D^0=\Pi_0,\qquad \Pi_D^1=\pi_{Q_{\rm raw}}.
\tag{GAP6A.3}
\]
It is a chain map because \(\pi_{Q_{\rm raw}}d_D=0\). Its cohomology maps are identity in degree zero and the original quotient in degree one; hence it is a quasi-isomorphism. Both maps are continuous in the original topologies. They intertwine real dilation: for the minus-chart function, the original action is \(g\mapsto a g(a\,\cdot)\), and its Fourier transform is \(\widehat g(\,\cdot/a)\), precisely the plus-chart action. The same equality verifies the second coordinate. Interchanging the two charts commutes with (GAP6A.1). In degree one the quotient retains the original oriented mirror \(-R_A\). Thus all claimed actions are preserved without changing their factors.

Use \(\Gamma\) from GAP3 with its oriented actions from GAP5. Define
\[
\mathscr H_F:\mathscr H\longrightarrow\mathscr H_D
\]
to be \(\overline{\mathcal T}:Q\to Q_{\rm raw}\) in degree one and zero in all other degrees. Then there is an exact equality of cochain maps
\[
\Pi_D\mathfrak F=\mathscr H_F\Gamma.
\tag{GAP6A.4}
\]
In degree zero, (GAP5.3) is the anti-Fourier pair in (GAP6A.2), so its projection is zero. In degree one the equality is the definition of the quotient map induced by \(\mathcal T\). Every negative target term is zero. These checks prove (GAP6A.4) degree by degree, not only after taking cohomology.

Consequently the map of cones
\[
(d,c)\longmapsto(\Pi_Dd,\Gamma c)
\tag{GAP6A.5}
\]
commutes with the exact differential (GAP6.1). It is a quasi-isomorphism: the two source-and-target maps are isomorphisms on all cohomology groups, and the cone long exact sequences give the same for the cone map. More explicitly, at each degree use exactness to lift a target class to the adjacent group, transfer it by those two isomorphisms, and correct its difference in the preceding group; this proves surjectivity, while the same exactness with a zero target proves injectivity.

The target cone retains the two-term summand
\[
Q\xrightarrow{\overline{\mathcal T}}Q_{\rm raw}
\quad\text{in degrees }0,1.
\tag{GAP6A.6}
\]
Its contracting homotopy in degree one is the actual inverse \(\overline{\mathcal T}^{-1}\); it is zero on all other terms. Its differential followed by this homotopy and the reverse composition sum to identity on the displayed pair. Projection away from this explicitly contractible pair therefore gives
\[
\operatorname{Cone}(\mathfrak F)\longrightarrow
H^0(D)[0]\oplus\bigoplus_{n\ge1}B_n[n],
\tag{GAP6A.7}
\]
a canonical equivariant quasi-isomorphism. The convention on shifts is the one in GAP3.5: \(B_n[n]\) occurs in degree \(-n\). In degree zero this map is \((v,k)\mapsto\Pi_0v\); in degree \(-n\) it is \((0,c)\mapsto\Gamma^{1-n}c\), and in degree one it is zero. Its chain identities are the identities just proved. The cochain minus sign on the shifted source remains the one in (GAP6.1).

The final connecting arrow in the contracted triangle commutes up to its exact homotopy, rather than strictly. Write \(\delta\) for the identity on each surviving shifted \(B_n\), zero on \(H^0(D)\), and write \(\Pi_K\) for (GAP6A.7). With \(\operatorname{pr}_{\mathscr C}\) the original cone projection, the difference
\[
\Gamma[1]\operatorname{pr}_{\mathscr C}-\delta\Pi_K
=d\eta+\eta d,\qquad
\eta^1(b)=\overline{\mathcal T}^{-1}\pi_{Q_{\rm raw}}(b)
\tag{GAP6A.8}
\]
has all other homotopy components zero. Its degree-zero value is exactly \(\pi_Q(k)\), since \(\pi_{Q_{\rm raw}}d_Dv=0\); this equals the difference of the two connecting maps on \((v,k)\). In negative degrees the connecting maps coincide. This proves the full triangle comparison in the homotopy/derived category with its specified homotopy. The independent proof CTF6 gives every connecting map and sign.

In this entire triangle, all prime-labelled exterior terms and all four endpoint lines survive in their stated degrees. No spectral quotient is embedded into the original test space, and no convergence of a sum over zeros is used.

## GAP6B. Faithful source coefficients in the same whole comparison

DCP8 constructs the actual source coefficient sheaf
\[
\mathcal M_{\rm full}=\mathcal N\oplus(i_+)_*V_+\oplus(i_-)_*V_-.
\]
Its extra closed coefficient group is \(V=V_+\oplus V_-\), placed in degree zero. Retain these coefficients on both sides of the preceding comparison:
\[
\mathscr C_{\rm full}=\mathscr C^{\rm or}\oplus V[0],\qquad
D_{\rm full}=D\oplus V[0],\qquad
\mathfrak F_{\rm full}=\mathfrak F\oplus\operatorname{id}_V.
\tag{GAP6B.1}
\]
The target is exactly the Cech complex (DCP9.2). The source is the displayed coefficient enlargement of the derived adelic complex, not an assertion that a new undeclared primitive cohomology theory has been constructed.

The original global receiving ring is \(\mathbb Z^3\). Its element \((a,b_+,b_-)\) acts by scalar \(a\) on \(\mathscr C^{\rm or}\) or \(D\), and by \(b_+,b_-\) on the two extra closed copies. These actions commute with the differentials and the map (GAP6B.1). DCP's exact source maps give
\[
[\tau]=(1,1,1),\qquad [n]=(n,0,0).
\tag{GAP6B.2}
\]
Here brackets denote receiving actions, not source coordinates for \(\tau\). Thus source \(\tau\) acts as identity on all the displayed coefficients, while integer \(n\) acts as \(n\) on the first summand and zero on the extra closed copies. A nonzero vector in either extra copy distinguishes \(\tau\) from every integer. A nonzero vector in the first summand distinguishes unequal integers. Multiplying these actions proves preservation of every supplied source product, and integer-input addition is the original scalar addition. No sum with \(\tau\) as an input is introduced.

Real dilations act on \(V_+\) and \(V_-\) by their original DCP formulas, and the mirror interchanges those two copies. The source and target use those same actions; hence their identity comparison preserves them. The global-ring mirror interchanges \(b_+\) and \(b_-\), so source scalar compatibility is also retained.

Extend both \(\Gamma\) and \(\Pi_D\) by \(\operatorname{id}_V\). Their commuting square (GAP6A.4) remains exact. On the cone, the additional terms are exactly
\[
\operatorname{Cone}(\operatorname{id}_{V[0]})
=[V\xrightarrow{\operatorname{id}}V]
\quad\text{in degrees }-1,0.
\tag{GAP6B.3}
\]
The degree-zero-to-degree-minus-one identity is its contracting homotopy: the cone differential sends the shifted source coordinate to the target coordinate with positive sign, since the original differential on \(V[0]\) is zero. This verifies \(dh+hd=\operatorname{id}\) on both terms. It commutes with the retained source actions, mirror and dilations. The extra coefficients have therefore been retained on both objects and compared by identity; only their explicitly contractible identity-cone contributes zero cohomology. It follows that (GAP6A.7) is also the exact comparison-cone result for (GAP6B.1).

The final-arrow homotopy (GAP6A.8) gains the degree-zero component sending the extra target \(w\in V\) to the identical \(w\) in the shifted source \(V\). The differential from the shifted source has positive sign in (GAP6B.3), so this homotopy gives exactly the retained identity on that component. CTF7.7 verifies it degree by degree. This faithful whole-complex comparison supplies the source distinction that the simple coefficient pullback alone lost. It neither assigns parity to primitive \(\tau\) nor obtains weight one from the endpoint vanishing proved below.

## GAP7. Infinitesimal action and the globally invertible endpoint polynomial

The original smooth dilations have generators
\[
L_Hh=-v h'(v),\qquad L_{\mathcal A}k=\tfrac12k-u k'(u).
\tag{GAP7.1}
\]
These are derivatives at \(a=e^t,t=0\) in the original Schwartz or strong seminorms; Taylor's integral remainder and the same seminorms on a compact \(t\)-interval prove the limit. Differentiating (GAP1.6) gives \(JL_H=L_{\mathcal A}J\). Direct integration by parts gives
\[
F_{L_{\mathcal A}k}(s)=sF_k(s),\qquad
m(L_Hh)=(0,\int_{\mathbb R}h),
\tag{GAP7.2}
\]
with zero boundary terms because of the retained decay. Thus on every actual \(B_n\), the generator is \(L_{B_n}=\operatorname{id}\otimes\operatorname{diag}(0,1)\), and
\[
P(L_{B_n})=0,\qquad P(z)=z(z-1).
\tag{GAP7.3}
\]

The actual \(P(L_Q)\) is a continuous automorphism of the entire original quotient. The companion generator proof retains the complete representative
\[
F_*(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
F_*(0)=F_*(1)=\frac18,
\]
and its explicit inverse formula
\[
\mathcal V F(s)=
\frac{F(s)-8\big((1-s)F(0)+sF(1)\big)F_*(s)}{s(s-1)}.
\tag{GAP7.4}
\]
Both removable endpoint values, every pole and Gamma contribution, the continuous division estimates and the exact original Schwartz correction are proved there. This is a map on the original \(F\) and its quotient; \(F_*\) is the displayed auxiliary summation image, not a replacement for \(\zeta\). RZ's existing complete-quotient endpoint resolvents retain their credit.

Full mirror covariance is retained: differentiating (GAP4.4) gives \(Lw=w(1-L)\). Since \(P(1-L)=P(L)\), the polynomial and its quotient inverse commute with the mirror as well as every original dilation and prime action. This is why the endpoint separation is global and does not require a finite list of zeros or a uniform gap estimate for their heights.

## GAP8. What the global lifting calculation proves

The complete proof GLOBAL_ENDPOINT_EXTENSION_RETURN.md applies the preceding exact operators to the original endpoint coefficient modules. For every extension of the actual \(Q\) by a displayed \(B_n\) in the stated operator category, its canonical lift is
\[
s(q)=P(L_E)\widetilde{P(L_Q)^{-1}q}.
\tag{GAP8.1}
\]
Here the tilde is any preimage under the extension quotient. Two choices differ by \(B_n\), annihilated by \(P(L_E)\), so the formula is independent of that choice. Applying the quotient gives \(q\). The companion supplies the complete uniqueness, continuity and all-degree extension argument, with the exact category and quotient-topology prerequisites. Every additional action commuting with \(P\), including the original mirror, is preserved. No assumption of the desired purity enters this lift.

Numerically, the two actual endpoint characters at a prime \(p\) are \(1,p\), of weights \(0,2\) in the convention \(|\alpha|=p^{w/2}\). At an original zero \(\rho\), the unchanged operator is
\[
p^\rho\sum_{j=0}^{m_\rho-1}\frac{(\log p)^j}{j!}N_\rho^j.
\tag{GAP8.2}
\]
The original strip gives \(0<2\Re\rho<2\). The whole-quotient polynomial calculation proves endpoint separation without replacing the full quotient by the direct sum or product of its primary blocks. It does not strengthen this interval to weight one.

The actual DCP supported obstruction also contains \(Q\) itself, rather than only the endpoint modules. On that supported \(Q\), \(P(L)\) is the same automorphism just proved. Consequently (GAP8.1) applies to the endpoint extension and not to that distinct supported quotient. DCP gives its exact diagonal quotient boundary and Fourier lifting map. These are retained constructions, not a claim that the user has supplied contradictory definitions.

## GAP9. Deligne comparison and the next actual geometric calculation

Deligne's local invariant-cycle cross uses three substantive maps: proper-base-change identification with the special fibre, the Hochschild–Serre surjection onto inertia invariants, and a support obstruction identified by duality as \(H^{2N-i-1}(X_s)^\vee(-N)\). His §§3.6.2–3.6.3 derive weights at most \(i\) for the target and at least \(i+1\) for the obstruction. Exactness of \(W_i\) supplies the lift in the correct subspace. No weight is assigned by the name of the supported point alone.

GAP1–GAP8 have constructed the entire actual adelic complex, its source-to-CC comparison, all higher prime-boundary terms, exact mirror orientation, and a global separation operator for those endpoints. This replaces earlier finite-block reasoning on that boundary with a theorem on the entire original quotient. It does not identify the non-endpoint supported \(Q\) with Deligne's dual special-fibre term or derive its weight bound. The next calculation remains that specific geometric comparison, with the full source support retained; no arbitrary receiving acyclicity is substituted for it.

The user-originating whole-spectrum and quotient arguments remain controlling for what may be claimed about the original source. All diagrams and receiving maps above preserve their exact domains and the distinction between source \(\tau\) and receiving coefficients. The goal remains active.
