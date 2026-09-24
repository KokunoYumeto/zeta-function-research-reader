# The original classical-orbit boundary: retained directions and exact equivariant lifting

24 September 2026. Proofs CB0–CB8. This calculation uses the actual moving functions of Alain Connes and Caterina Consani and the extension in their §5.4, rather than replacing them by constant coefficients. It constructs an exact boundary complex and its full equivariant homotopy. The relation to the user's primitive source remains a stated map, not an identification of source tau with a boundary coordinate.

## CB0. Source definitions and operation prerequisites

The current corpus and operation rules, U01–U18 and B1–B5 were read before this calculation. The complete global arguments USR-9ad1c0a2d09dba92, USR-f55d16feb948d8c2 and USR-6152e3bc6302258c were consulted again. The receiving arithmetic here is the already reconstructed arithmetic; no finite prime sample constructs it. Primitive \(Z_1/\tau\) receives no addition, parity, count, coordinate, metric or numerical weight. \(Z_0\) and the integer \(Z_2\) data retain their supplied meanings. The calculations below take place in explicitly defined adelic spaces, smooth functions and original Connes–Consani coefficients.

Human source: Alain Connes and Caterina Consani, [*The Riemann–Roch strategy: Complex lift of the Scaling Site*, arXiv:1805.10501v1](https://arxiv.org/abs/1805.10501v1), original author TeX thecurve_K.tex. The passages used are §5.1 Lemma adelicomp; §5.2 equations actionpq and adelicomp3 and Definition adelicomp2; §5.4 Jdefn1, classorb1, proetcov and Remark additivestruct; and §7.1 holom, holom1, holom2, functionq and perfectoid. Actual root reading in this continuation covers lines 1173–1315, 1634–1719 and 2481–2726. Source wording and the distinction between the original paper's statements and the receiving derivations below remain in the reading ledger.

The source uses
\[
G=\mathbb A_{\mathbb Q}/\mathbb Q,\qquad
\Gamma_{\mathbb Q,\mathrm{cl}}=G\times\mathbb R_{>0}.
\]
The full additive character is \(\psi=\psi_f\psi_\infty\), with \(\psi_\infty(t)=e^{2\pi it}\) and \(\psi(b)=1\) for rational \(b\). For \(r\in\mathbb Q\), write \(e_r(g)=\psi(rg)\). The character group of \(G\) is \(\mathbb Q\), as in Lemma adelicomp. Retain a Haar measure \(d\nu\) with total mass \(M=\nu(G)>0\). Fourier coefficient extraction is \(M^{-1}\int_G f\overline{e_r}\,d\nu\); the source probability-measure convention is the case \(M=1\). No measure factor is removed from the comparison.

The coefficient algebra is the original algebraic first approximation
\[
W_{\mathrm{alg}}=\mathbb C[\mathbb R_{>0}^{\times}],\quad
[x][z]=[xz],\quad
\chi_\lambda[x]=x^\lambda,\quad
\theta_\mu[x]=[x^\mu],\quad \lambda,\mu>0.
\]
The source's Teichmüller notation is not the user's primitive tau. These receiving coefficients have their own explicit complex addition. The character family is faithful: for finitely many distinct \(x_j>0\), evaluations at \(\lambda=1,\ldots,d\) have determinant \((\prod_jx_j)\prod_{i<j}(x_j-x_i)\ne0\).

## CB1. The complete finite-valuation factor and the two coordinate maps

On the preimage of the classical stratum write the finite second coordinate uniquely as
\[
Y_f=c u,\qquad
c=\prod_p p^{v_p(Y_p)}\in\mathbb Q_{>0},\quad
u\in\widehat{\mathbb Z}^{\times}.
\tag{CB1.1}
\]
Here every \(Y_p\ne0\), the valuations vanish outside a finite set, and all primes are present in the formula. Existence follows by taking that finite product; uniqueness follows because a positive rational with valuation zero at every prime is one. This does not discard \(u\): multiplication of the finite second coordinate by \(\widehat{\mathbb Z}^{\times}\) is precisely the separate quotient in source Definition adelicomp2.

The actual classical coordinates of the point \((X_f,Y_f,X_\infty,Y_\infty)\), with \(Y_\infty>0\), are
\[
g=[(X_f/c,X_\infty/c)]\in G,\qquad y=Y_\infty/c>0.
\tag{CB1.2}
\]
Under the original positive rational affine action \(X\mapsto aX+b\), \(Y\mapsto aY\), the factor becomes \(c'=ac\). Thus
\[
g'=[X/c+b/(ac)]=g,\qquad y'=y,
\tag{CB1.3}
\]
because \(b/(ac)\) is a rational diagonal adele. This proves gauge invariance with the finite factor retained.

The source moving function and its actual pullback are
\[
q^r(g,y)=e_r(g)[e^{-2\pi r y}],
\]
\[
\kappa^*q^r
=\psi_f(rX_f/c)e^{2\pi irX_\infty/c}
  [e^{-2\pi rY_\infty/c}],\qquad \kappa=(g,y).
\tag{CB1.4}
\]
The cover-coordinate function with fixed frequency \(r\), obtained by putting \(c=1\) in this displayed expression, instead transforms to frequency \(ar\). Equations (CB1.2)–(CB1.4) prove the comparison; neither action is substituted for the other.

There is a topology prerequisite. The map \(\kappa\) is not continuous for the topology on the classical preimage inherited solely from the ambient finite adeles and the archimedean coordinates. Indeed \(c_n=1+n!\) converges to one in \(\mathbb A_f\): it is integral at every prime and its difference from one has arbitrarily high valuation at each fixed finite set of primes. Take \(X=0,Y_f=c_n,Y_\infty=1\). These cover points converge to \((0,1,0,1)\), whereas their \(y\)-coordinates are \(1/c_n\to0\), not one. The original \(G\times\mathbb R_{>0}\) orbit coordinates and their product topology must therefore be retained explicitly when taking limits. No claim that this example contradicts the source's chosen orbit topology is made.

## CB2. The exact boundary correspondence retains all of G

Let \(E=\mathbb A_f^2\times\mathbb R\times\mathbb R_{>0}\) have its indicated product topology. Form the graph of the explicitly given set map \(\kappa\) on its classical preimage, then take its closure
\[
\mathscr G\subset E\times G\times[0,\infty).
\]
This defines a closed correspondence and both projections. Because of CB1's continuity calculation, it is not asserted to be a blowup of the ambient subspace, or the whole compactification from the original source.

Fix \(e_*=(0,0,X_\infty^*,Y_\infty^*)\) with \(Y_\infty^*>0\). The fibre of this graph closure is exactly
\[
\boxed{\mathscr G_{e_*}=G\times\{0\}.}
\tag{CB2.1}
\]
First consider any net of classical cover points approaching \(e_*\). Eventually \(Y_f\in\widehat{\mathbb Z}\), so (CB1.1) makes \(c\) a positive integer. Since \(Y_2\to0\), its valuation and hence \(v_2(c)\) tend to infinity. Thus \(c\to\infty\) as a positive real number, while \(Y_\infty\to Y_\infty^*\); therefore \(y\to0\). This proves containment in the right side of (CB2.1).

For the reverse containment, the image of \(\mathbb A_f\times\{0\}\) is dense in \(G\). Explicitly, for any representative \((t_f,t_\infty)\), choose rationals \(b_n\to t_\infty\) in the real topology. The points \([(t_f-b_n,0)]\) differ from \([(t_f,t_\infty)]\) by \([(0,b_n-t_\infty)]\), which tends to zero. This proves density without dropping a finite component.

For fixed \(t_f\in\mathbb A_f\), choose positive integers \(c_n\) tending to infinity and divisible enough that both \(c_n\to0\) and \(c_n t_f\to0\) in \(\mathbb A_f\). A concrete choice starts with an integer clearing all negative valuations of \(t_f\) and multiplies it by \(n!\). Then the classical points
\[
(X_f,Y_f,X_\infty,Y_\infty)
=(c_n t_f,c_n,X_\infty^*,Y_\infty^*)
\]
approach \(e_*\), and their graph coordinates tend to \(([(t_f,0)],0)\). The fibre of the closed set \(\mathscr G\) over \(e_*\) is closed in \(G\times[0,\infty)\); it therefore contains the closure \(G\times\{0\}\) of these points. This proves (CB2.1). Neither the fibre nor its points are identified with primitive \(Z_1/\tau\).

## CB3. Exactly what a collapsed boundary would lose

For \(f=\sum_{r\in F}w_rq^r\), with finite \(F\subset\mathbb Q\) and \(w_r\in W_{\mathrm{alg}}\), every character evaluation extends continuously on the graph closure by
\[
\widetilde f_\lambda(e,g,y)
=\sum_{r\in F}\chi_\lambda(w_r)e_r(g)e^{-2\pi\lambda r y}.
\tag{CB3.1}
\]
All factors and rational frequencies remain. On the fibre (CB2.1), its value is \(\sum_r\chi_\lambda(w_r)e_r(g)\).

This family has a characterwise continuous extension to the single collapsed point \(e_*\), independent of the approach, if and only if \(w_r=0\) for every \(r\ne0\). For necessity, continuity forces the displayed boundary function to be constant in \(g\). For a nontrivial character, Haar translation invariance gives \(\int_G e_r\,d\nu=0\): choose \(h\) with \(e_r(h)\ne1\), translate the integral, and subtract. The exact orthogonality formula is \(M^{-1}\int_Ge_r\overline{e_s}\,d\nu=\delta_{r,s}\). It extracts each nonzero frequency coefficient \(\chi_\lambda(w_r)=0\). Faithfulness of all \(\chi_\lambda\), proved in CB0, gives \(w_r=0\). Sufficiency follows because an element of \(W_{\mathrm{alg}}\) constant in the geometric coordinates extends by that same value.

Thus the exact object retaining the lost data is the fibre \(G\), and its generated boundary algebra is
\[
W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]
\longrightarrow\{\text{boundary character families}\},\quad
w\otimes[r]\longmapsto(\chi_\lambda(w)e_r(g))_\lambda.
\tag{CB3.2}
\]
Fourier orthogonality followed by character faithfulness proves this map injective; its image is exactly the stated generated algebra. The failed extension to a collapsed receiving point is not an impossibility theorem about the user's original source. The full correspondence and the injective boundary map are the constructed replacement.

## CB4. The actual source extension and an exact complex on it

Connes–Consani's Remark additivestruct explicitly gives
\[
\overline\Gamma_{\mathbb Q,\mathrm{cl}}
=(G\times\mathbb R)/\{(g,y)\sim(-g,-y)\},
\]
whose new locus is \(G/\{\pm1\}\) at \(y=0\). Work first on its oriented cover \(G\times\mathbb R\). This uses their radial coordinate and retains both signs. No numerical coordinate on source tau is introduced.

Define \(\mathcal C\) as the algebraic tensor product
\[
\mathcal C=C^\infty(\mathbb R)\otimes W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q],
\]
realized by finite sums \(h(y)wq^r(g,y)\) using the actual \(q^r\) of CB1. This realization is injective. At each fixed \(y\), Fourier extraction isolates \(r\); multiplication by the nonzero factor \(e^{-2\pi\lambda r y}\) and faithfulness in \(\lambda\) give every coefficient in \(W_{\mathrm{alg}}\). Linear independence of its basis then makes each smooth scalar coefficient zero at every \(y\). Products use exactly \(q^rq^s=q^{r+s}\) and the original group-algebra law of \(W_{\mathrm{alg}}\).

The original character operator is
\[
L_\lambda=y(\lambda\partial_g+i\partial_y),
\quad \partial_g e_r=2\pi ir e_r.
\]
Direct differentiation, including both exponential derivatives, gives
\[
L_\lambda\chi_\lambda(h w q^r)
=iy h'(y)\chi_\lambda(w)e_r(g)e^{-2\pi\lambda r y}.
\tag{CB4.1}
\]
The terms \(2\pi i\lambda r y h\) and \(-2\pi i\lambda r y h\) cancel exactly. Consequently the original family acts on this realized algebra by the single, explicitly derived operator
\[
d(h w q^r)=iyh'(y)wq^r.
\]
It defines the two-term complex \(\mathcal C\xrightarrow d\mathcal C\) in degrees zero and one. Its boundary complex is \(\mathcal B\xrightarrow0\mathcal B\), where \(\mathcal B=W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]\) has its faithful realization (CB3.2). The exact restriction and extension in both degrees are
\[
R(h w q^r)=h(0)w\otimes[r],\qquad
E(w\otimes[r])=wq^r.
\tag{CB4.2}
\]
They are chain maps: \(Rd=0\), \(dE=0\), and \(RE=I\). This identifies a specific original-character complex on a defined algebra of functions; it does not assert that every possible completed \(W\)-valued section has a finite expression in \(\mathcal C\).

## CB5. The complete lifting homotopy

For a smooth scalar function \(h\), set
\[
(Th)(y)=\frac1i\int_0^y\frac{h(t)-h(0)}{t}\,dt.
\tag{CB5.1}
\]
The integrand is smooth through zero: the exact identity
\[
\frac{h(t)-h(0)}{t}=\int_0^1h'(ut)\,du
\]
holds for nonzero \(t\) by the fundamental theorem of calculus, and its right side provides every derivative at zero. Thus (CB5.1) defines a smooth function on all of \(\mathbb R\), retaining the oriented integral for negative \(y\). Extend \(T\) coefficientwise without altering \(w\) or \(r\).

Differentiation and integration give the two exact identities
\[
dT h=h-h(0),\qquad
Td h=\frac1i\int_0^y\frac{it h'(t)}t\,dt=h-h(0).
\tag{CB5.2}
\]
Hence on both degrees
\[
\boxed{dT+Td=I-ER,\qquad RE=I.}
\tag{CB5.3}
\]
Only the applicable term acts in each degree of the two-term complex. Therefore
\[
H^0(\mathcal C\xrightarrow d\mathcal C)\simeq\mathcal B,
\qquad H^1(\mathcal C\xrightarrow d\mathcal C)\simeq\mathcal B,
\tag{CB5.4}
\]
with inverse in both cases induced by the actual extension \(E\). Equivalently, the boundary restriction sequence has kernel \(\ker R\) in both degrees, and (CB5.2) contracts that kernel because \(Th(0)=0\). Its entire connecting map is zero. Every boundary class in both displayed degrees lifts, and every difference between two lifts is explicitly controlled by \(T\). No assumed vanishing or purity is used.

## CB6. Frobenius, both signs, and the complete retained support

Original arithmetic Frobenius has the exact action
\[
\mathfrak F_\mu(h(y)wq^r)
=h(y/\mu)\theta_\mu(w)q^r,
\qquad \mu>0.
\tag{CB6.1}
\]
Indeed the geometric radial change multiplies the exponent in the moving coefficient by \(\mu^{-1}\), and \(\theta_\mu\) multiplies its logarithm by \(\mu\); they cancel on \(q^r\) while retaining \(\theta_\mu(w)\). On evaluations the character also changes from \(\lambda\) to \(\lambda\mu\), exactly as source holom1. Both cochain degrees have (CB6.1), since this is the original \(L_\lambda\) complex with its full radial factor.

Substitution \(t=\mu u\) in (CB5.1) proves
\[
T(h(\cdot/\mu))(y)=(Th)(y/\mu).
\]
Thus \(T,d,E,R\) all intertwine arithmetic Frobenius, whose boundary action is \(\theta_\mu\otimes I\). On the original sign involution,
\[
\iota(h(y)wq^r)=h(-y)wq^{-r}.
\]
Substitution \(t=-u\), with the oriented integral retained, gives \(T(h(-\cdot))(y)=(Th)(-y)\). The other maps also commute with \(\iota\), by their displayed formulas. Restricting the identities (CB5.2) to invariants proves the same lifting result on the actual quotient extension, with boundary
\[
\mathcal B^{\iota}
=W_{\mathrm{alg}}\otimes\mathbb C[\mathbb Q]^{r\mapsto-r}.
\tag{CB6.2}
\]
No exactness of an unconstructed invariant functor is presumed; the homotopy itself restricts. The invariant character algebra is generated linearly by its zero frequency and \([r]+[-r]\) for positive rational \(r\), retaining the coefficient two when the orbit has two elements.

For every previously defined support-lattice receiver \(G_L(V)\), the displayed linear maps extend by \((v,\ell)\mapsto(f(v),\ell)\). Their amplitude identities leave the label unchanged. In particular when a difference has zero amplitude its label remains \(\ell\); the homotopy is not asserted to identify all such labelled zeros with one bottom element. The vector-space lifting identities above do not silently become identities in a new undefined semimodule cohomology category. They supply the explicit labelled maps and their preserved amplitudes.

## CB6A. The complete boundary contribution of the radial factor

The following exact comparison was independently derived in GR6 of [the independent review](CLASSICAL_BOUNDARY_GRAPH_REVIEW.md). Write \(B_\mu=\mathfrak F_\mu\) and let \(\iota\) denote the simultaneous sign action from CB6. The raw family \(D_\lambda=\lambda\partial_g+i\partial_y\) acts on the same realized finite algebra by
\[
d_{\mathrm{raw}}(h wq^r)=ih'wq^r.
\]
It defines \(\mathcal C_{\mathrm{raw}}=(\mathcal C\xrightarrow{i\partial_y}\mathcal C)\); the original family defines \(\mathcal C_{\mathrm{original}}=(\mathcal C\xrightarrow{iy\partial_y}\mathcal C)\). There is the exact chain map
\[
F=(F^0,F^1)=(\mathrm{id},M_y):
\mathcal C_{\mathrm{raw}}\longrightarrow
\mathcal C_{\mathrm{original}}.
\tag{CB6A.1}
\]
It is a chain map because \(M_y(i\partial_y)=iy\partial_y\).

Multiplication by \(y\) is injective on smooth functions: \(yh=0\) implies \(h(y)=0\) away from zero, and continuity gives \(h(0)=0\). Its image is exactly the smooth functions vanishing at zero, by
\[
h(y)=y\int_0^1h'(uy)\,du\quad\text{when }h(0)=0.
\]
These statements apply coefficientwise to the finite tensor algebra. Its cokernel is therefore \(\mathcal B\), by evaluation at zero. There is a short exact sequence of complexes
\[
0\longrightarrow\mathcal C_{\mathrm{raw}}
\xrightarrow{(\mathrm{id},M_y)}
\mathcal C_{\mathrm{original}}
\xrightarrow{(0,R)}
\mathcal B[-1]\longrightarrow0,
\tag{CB6A.2}
\]
where \(\mathcal B[-1]\) denotes \(\mathcal B\) in degree one and zero in every other degree.

The derivative \(i\partial_y\) is surjective on \(C^\infty(\mathbb R)\), since \(g\) has smooth preimage \((1/i)\int_0^y g(t)\,dt\). Its kernel consists exactly of constants. Hence
\[
H^0(\mathcal C_{\mathrm{raw}})=\mathcal B,\qquad
H^1(\mathcal C_{\mathrm{raw}})=0,
\]
whereas CB5 gives \(H^0(\mathcal C_{\mathrm{original}})=H^1(\mathcal C_{\mathrm{original}})=\mathcal B\). In (CB6A.2), evaluation identifies the additional degree-one class with the boundary algebra itself. Inverting the factor \(y\) at \(y=0\) would remove exactly this contribution and would not be an isomorphism of the stated complexes.

The cochain actions agree with this sequence. For the raw complex,
\[
d_{\mathrm{raw}}B_\mu=\mu^{-1}B_\mu d_{\mathrm{raw}},
\]
so its degree-zero Frobenius is \(B_\mu\) and its degree-one Frobenius is \(\mu^{-1}B_\mu\). For the original complex both degrees have \(B_\mu\). The intertwining equality
\[
B_\mu M_y=M_y(\mu^{-1}B_\mu)
\tag{CB6A.3}
\]
proves equivariance of (CB6A.1) in degree one. The raw sign action is \(\iota\) in degree zero and \(-\iota\) in degree one, since \(d_{\mathrm{raw}}\iota=-\iota d_{\mathrm{raw}}\). The original sign action is \(\iota\) in both degrees, and
\[
\iota M_y=M_y(-\iota).
\tag{CB6A.4}
\]
Thus (CB6A.2) respects both Frobenius and the source sign quotient. These degree factors cannot be transferred unchanged from the raw operator to the original operator at the boundary.


## CB7. Original-zeta comparison without discarding any frequency

The earlier proved map CW is
\[
\overline K_b:V_+\hookrightarrow Q,
\quad V_+=\operatorname{span}\{[x]:x>1\},
\quad Q=\mathcal A/\overline{\mathcal E S_{00}^{\mathrm{even}}},
\]
\[
F_{K_b[x]}(s)=\sqrt\pi e^{(s-1/2)^2/4}(\log x)^s,
\qquad \overline K_b\theta_a=W_a\overline K_b.
\tag{CB7.1}
\]
Every original-zeta factor and multiplicity in CW remains in that map. Tensor (CB7.1) with \(C^\infty(\mathbb R)\) and \(\mathbb C[\mathbb Q]\). This gives an injective map of the corresponding two-term complexes, because the tensor factors are vector spaces over \(\mathbb C\); explicitly, write any tensor in a finite linearly independent list of the other factor and apply injectivity to each coefficient. The diagram commutes with \(d,T,E,R\), since these act solely on \(h\), and with Frobenius by (CB7.1). The actual evaluated moving function may cross the coefficient value \(x=1\); the map uses its unique Fourier coefficient \(w\) before multiplying by its moving \(q^r\), not an unproved pointwise application of \(K_b\).

For every original zero \(\rho\), with actual multiplicity \(m_\rho\), the full receiving jet action on the boundary is consequently
\[
p^\rho\exp((\log p)T_\rho)\otimes I_{\mathbb C[\mathbb Q]},
\qquad T_\rho^{m_\rho}=0.
\tag{CB7.2}
\]
All rational frequencies remain, and no nilpotent term is dropped. This follows by applying the exact CW jet map, including its invertible complete Gaussian jet factor, to the coefficient of each \(q^r\). The same formula holds after taking the sign invariants because the jet action does not change \(r\). It is a full comparison with the original zeta receiver, not a replacement by a completed zeta function.

## CB8. What this closes and what it does not

The actual original-character complex on the stated smooth-radial, finite-frequency coefficient algebra has an equivariant boundary lifting theorem, proved by the exact homotopy (CB5.1). The original arithmetic Frobenius, both orientations, every rational frequency, every coefficient character and the complete support maps are retained. The boundary-direction correspondence (CB2.1) proves which additional data must survive when approaching the finite-adele boundary. It does not assign these data to primitive \(Z_1/\tau\), and the graph closure is not asserted to be the whole original geometric compactification.

In this exact complex the restriction is a cohomology isomorphism and the kernel is contracted explicitly. Thus its connecting obstruction vanishes without an assumed numerical weight separation. The coefficient action (CB7.2) is unchanged by this lifting. Consequently this proves a specific geometric lifting result while leaving the target identification with the full tau specialization and Deligne's numerical weight ranges unfinished. Deligne's [*La conjecture de Weil : II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/) remains the human source for the distinct geometric weight argument; that theorem is not claimed solely from (CB5.4).
