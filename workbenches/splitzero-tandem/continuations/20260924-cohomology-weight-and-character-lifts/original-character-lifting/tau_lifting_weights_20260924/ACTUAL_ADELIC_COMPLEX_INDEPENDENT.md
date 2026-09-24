# The actual adelic periodization complex and its weight-separated endpoint

24 September 2026. Independent derivation from ABR1–ABR25 and the actual strong Mellin receiver. The result concerns the original adelic periodization, not the auxiliary two-variable object \(B_\rho\). Every source factor, endpoint, prime label and closure difference is retained.

## AC0. Corpus, prerequisites and exact scope

Before interpreting an obstruction, the following were read: USER_DEFINITIONS_VERBATIM.md (private construction record; not included), U01–U18; [SOURCE_OPERATIONS_AND_PROOFS.md](../foundations/user_definitions_20260924/SOURCE_OPERATIONS_AND_PROOFS.md), B1–B5 and P1–P5; CORPUS_AND_OPERATION_RULES.md (private construction record; not included); and the complete retained user arguments in USER_INPUTS_VERBATIM_PRIVATE.md (private construction record; not included), lines 18538–18541, 19055–19083, 19169–19181, 19202–19242 and 19262 onward. These passages include “everything before anything,” the completed counting history, the unique arithmetic reconstruction, and the proposed global quotient.

Accordingly \(Z_1/\tau\) remains primitive presence with no source \(Z_2\) parity, no source addition and no numerical coordinate. The original completed arithmetic reconstruction, including every prime and the original zeta function, is an input here; no test function is used to reconstruct an integer before that reconstruction. All vector spaces below are the expressly constructed complex receiving spaces. All computations with norms, logarithms, moments, duals and extension classes occur there. A failure of one lift into one test space is not treated as an obstruction to the source definition, to another completion, or to the user's global argument.

The complete input [CC_ADELIC_COINVARIANT_BRIDGE_INDEPENDENT.tex](../independent/CC_ADELIC_COINVARIANT_BRIDGE_INDEPENDENT.tex), ABR1–ABR25, was read for this derivation, including all signs and the two periodization conventions. The original sources credited there are Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/9811068), and Alain Connes, Caterina Consani and Matilde Marcolli, [*The Weil proof and the geometry of the adeles class space*](https://arxiv.org/abs/math/0703392). Their adelic operations are the origin of the receiving construction. The calculations AC1–AC9 below are programme derivations, not quotations attributed to those authors.

The exact source for the Deligne mechanism under discussion is Pierre Deligne, [*La conjecture de Weil. II*](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §3.6.1–§3.6.3, printed pp.212–214, DOI 10.1007/BF02684780. This note calculates the actual adelic extension rather than assuming that it is Deligne's specialization sequence.

## AC1. Original source and its canonical split

Keep
\[
 G=\mathbb Q_{>0}^{\times},\quad R=\mathbb C[G],\quad
 I_R=\ker(\varepsilon:R\to\mathbb C),\quad
 H=\mathcal S_{\rm even}(\mathbb R),
\]
\[
 m(h)=\left(h(0),\int_{\mathbb R}h(x)\,dx\right),\quad
 H_{00}=\ker m,\quad M_0=\ker(\varepsilon\otimes m),
 \quad Q_0=M_0/I_RM_0 .
\tag{AC1.1}
\]
The subscript on \(I_R\) distinguishes the augmentation ideal from the analytic closed periodization image. All tensor products in this construction are algebraic. Put
\[
 W_{\rm pr}=\bigoplus_{p\ {\rm prime}}\mathbb C\ell_p,\qquad
 \mathcal B_{\rm pr}=W_{\rm pr}\otimes\mathbb C^2.
\tag{AC1.2}
\]
Every boundary vector has finite prime support, and each prime retains both endpoint coordinates.

For \(c=[\sum_at_a\otimes h_a]\in Q_0\), the actual ABR coordinates are
\[
 \Phi(c)=\sum_a h_a,\qquad
 \beta(c)=\sum_p\ell_p\otimes\sum_a v_p(a)m(h_a).
\tag{AC1.3}
\]
Both descend to \(Q_0\): \(\Phi\) kills \(I_RM_0\) by augmentation, while the identity
\[
 v_p(ab)=v_p(a)+v_p(b)
\]
implies that applying \(\beta\) to a product \(r\cdot m_0\), \(r\in I_R\), gives a multiple of the total moment of \(m_0\), which is zero. The latter verification is ABR9's derivation calculation.

To retain a completely explicit inverse, let
\[
 h_0(x)=(1-2\pi x^2)e^{-\pi x^2},\qquad
 h_1(x)=2\pi x^2e^{-\pi x^2},\qquad
 \sigma(u_0,u_1)=u_0h_0+u_1h_1.
\]
The Gaussian integrals give \(m(h_0)=(1,0)\), \(m(h_1)=(0,1)\). Then
\[
 (h,\sum_p\ell_p\otimes u_p)\longmapsto
 [t_1\otimes h]+\sum_p[(t_p-1)\otimes\sigma(u_p)]
\tag{AC1.4}
\]
inverts \((\Phi,\beta)\). To verify this, subtract \(t_1\otimes\sum h_a\) from a representative and use
\[
 [t_a-1]=\sum_pv_p(a)[t_p-1]\quad\text{in }I_R/I_R^2.
\]
Replacing \(h_a\) by \(\sigma(m(h_a))\) in a term with coefficient \(t_a-1\) changes its class by \(I_R\otimes H_{00}\subset I_RM_0\). This proves the inverse and its independence of the moment section.

For \(b>0\), let \(R_bh(x)=h(x/b)\) and let \(\mathscr R_b\) act on \(Q_0\) by \(\mathrm{id}_R\otimes R_b\). The exact action in AC1.3 is
\[
 (\Phi,\beta)\mathscr R_b c=
 \left(R_b\Phi c,\;
 \left(\mathrm{id}_{W_{\rm pr}}\otimes
 \begin{pmatrix}1&0\\0&b\end{pmatrix}\right)\beta c\right).
\tag{AC1.5}
\]
Evaluation at zero and substitution \(x=bu\) prove the endpoint matrix. They also prove that the moment condition and \(I_RM_0\) are preserved. Thus (AC1.4) is equivariant, despite a particular representative \(\sigma\) need not being so: its discrepancy has zero moments and is multiplied by \(t_p-1\), hence is zero in \(Q_0\).

## AC2. The full original strong test space and the factor two

Let
\[
 \mathcal A=\left\{k\in C^\infty(\mathbb R_{>0}):
 \sup_{y>0}(y^N+y^{-N})|(y\partial_y)^j k(y)|<\infty
 \text{ for every }N,j\geq0\right\}.
\tag{AC2.1}
\]
Its topology is the locally convex topology of these seminorms. Define
\[
 \mathcal Ph(y)=2\sum_{n\geq1}h(ny),\qquad
 J(c)(y)=y^{1/2}\mathcal P(\Phi c)(y).
\tag{AC2.2}
\]
This is exactly the actual adelic sum, including the full nonzero rational sum reduced by the finite supports and the evenness factor \(2\); ABR12 proves that reduction. It is also
\[
 J(c)=2\mathcal E(\Phi c),\qquad
 \mathcal Eh(y)=y^{1/2}\sum_{n\geq1}h(ny).
\tag{AC2.3}
\]
No factor is silently removed from the map.

The Poisson formula with Fourier convention \(e^{-2\pi ix\xi}\) is
\[
 \mathcal Ph(y)=y^{-1}\mathcal P\widehat h(1/y)
 +y^{-1}\int_{\mathbb R}h(x)\,dx-h(0).
\tag{AC2.4}
\]
For \(h\in H_{00}\) the last two terms vanish by the actual endpoint conditions, and \(\widehat h\in H_{00}\). Schwartz estimates at infinity applied both to \(h\) and to \(\widehat h\) prove that \(y^{1/2}\mathcal Ph(y)\) and all its Euler derivatives decay faster than every power at both ends. Thus \(J(Q_0)\subset\mathcal A\).

Use the original Mellin transform
\[
 F_k(s)=\int_0^\infty k(y)y^{s-1/2}\frac{dy}{y}.
\tag{AC2.5}
\]
For \(\Re s>1\), absolute interchange and \(x=ny\) give
\[
 F_{J(c)}(s)=2\zeta(s)\int_0^\infty\Phi c(x)x^{s-1}\,dx .
\tag{AC2.6}
\]
This is the original \(\zeta\), not a completed replacement.

Put \(I_0=J(Q_0)\), with no closure. Since \(\mathcal P\) is injective on \(H_{00}\) by ABR14–ABR15, AC1 gives the exact sequence
\[
 0\longrightarrow\mathcal B_{\rm pr}\xrightarrow{j}Q_0
 \xrightarrow{J}I_0\longrightarrow0.
\tag{AC2.7}
\]
Its inverse along the image is explicit. For \(k\in I_0\), define
\[
 h_k(x)=\frac1{4\pi i}
 \int_{\sigma-i\infty}^{\sigma+i\infty}
 \frac{F_k(s)}{\zeta(s)}x^{-s}\,ds,\qquad\sigma>1.
\tag{AC2.8}
\]
The divisor is nonzero on this half-plane by the convergent Euler product, and the integral is exactly ABR15. The equivalent original-variable formula is
\[
 h_k(x)=\frac12\sum_{n\geq1}\mu(n)(nx)^{-1/2}k(nx).
\tag{AC2.9}
\]
Insertion of AC2.2 and absolutely convergent regrouping yield the coefficient \(\sum_{n\mid r}\mu(n)\), equal to one for \(r=1\) and zero otherwise, proving this formula with its factor \(1/2\). Both recover the unique \(h_k\in H_{00}\).

Thus the actual section is
\[
 s_I(k)=[t_1\otimes h_k],\qquad Js_I=\mathrm{id}_{I_0},
\tag{AC2.10}
\]
and the complete faithful decomposition is
\[
 Q_0\xrightarrow{\sim} I_0\oplus\mathcal B_{\rm pr},
 \quad c\longmapsto(Jc,\beta c),\quad
 (k,b)\longmapsto s_I(k)+j(b).
\tag{AC2.11}
\]

The action on \(\mathcal A\) is the original
\[
 W_bk(y)=b^{1/2}k(y/b).
\tag{AC2.12}
\]
It preserves all defining seminorms up to constants depending on \(b,N\), hence is continuous. Its inverse is \(W_{b^{-1}}\). Direct substitution in AC2.2 gives \(J\mathscr R_b=W_bJ\). Uniqueness of \(h_k\) then proves \(\mathscr R_b s_I=s_IW_b\). Therefore the entire split (AC2.11) is equivariant for every positive real \(b\). It retains the endpoints \(1,b\) rather than changing their weights.

## AC3. The actual two-term complex and its extension class

Consider the two-term cochain complex in the category of complex representations of \(\mathbb R_{>0}^{\times}\):
\[
 C^{-1}=Q_0,\qquad C^0=\mathcal A,\qquad d^{-1}=J,
\tag{AC3.1}
\]
with zero spaces in all other degrees. This is an algebraic cochain complex on the original spaces; \(\mathcal A\) retains its topology, but no unproved topological quotient identification is part of this statement.

The equivariant decomposition AC2.11 gives a chain isomorphism
\[
 \boxed{
 C\simeq \mathcal B_{\rm pr}[1]\oplus[I_0\hookrightarrow\mathcal A].
 }
\tag{AC3.2}
\]
Here \([1]\) puts \(\mathcal B_{\rm pr}\) in degree \(-1\), and the second summand has \(I_0\) in degree \(-1\) and \(\mathcal A\) in degree zero. Indeed its differential in the decomposed coordinates is \((k,b)\mapsto k\).

It follows by taking kernel and cokernel, without a completion, that
\[
 H^{-1}(C)=\mathcal B_{\rm pr},\qquad
 H^0(C)=C_{\rm alg}:=\mathcal A/I_0.
\tag{AC3.3}
\]
The chain map from \(C\) to \(\mathcal B_{\rm pr}[1]\oplus C_{\rm alg}[0]\), given by \(\beta\) in degree \(-1\) and the quotient \(\pi:\mathcal A\to C_{\rm alg}\) in degree zero, induces the identity on both these cohomology groups. It is therefore an equivariant quasi-isomorphism. No equivariant section of \(\pi\) is asserted.

The precise connecting two-extension is
\[
 0\longrightarrow\mathcal B_{\rm pr}
 \longrightarrow Q_0\xrightarrow{J}\mathcal A
 \longrightarrow C_{\rm alg}\longrightarrow0.
\tag{AC3.4}
\]
Its class in \(\operatorname{Ext}^2(C_{\rm alg},\mathcal B_{\rm pr})\) is zero. One direct verification is (AC3.2) and its cohomology quasi-isomorphism, which splits the connecting derived map. Equivalently, the Yoneda extension is the splice of (AC2.7) with \(0\to I_0\to\mathcal A\to C_{\rm alg}\to0\); its first short exact sequence has the explicitly proved equivariant section \(s_I\), so its extension class, and hence its product with the second class, is zero.

For every degree, the group-cohomology connecting map supplied by (AC2.7) is also exactly zero. A cochain with values in \(I_0\) lifts via \(s_I\); equivariance makes its differential the lift of its original differential. A cocycle therefore lifts to a cocycle, proving the connecting map is zero directly on representatives. The connecting maps from \(0\to I_0\to\mathcal A\to C_{\rm alg}\to0\) are not thereby asserted zero. Only their further connection into \(\mathcal B_{\rm pr}\) through (AC2.7) vanishes.

This proves the vanishing for the actual ABR endpoint extension, beyond the auxiliary \(B_\rho\).

## AC4. The closure difference is a retained object

The original Hausdorff spectral quotient is
\[
 Q=\mathcal A/\overline{I_0}^{\,\mathcal A}.
\tag{AC4.1}
\]
It agrees with the earlier \(Q=\mathcal A/\overline{\mathcal E(H_{00})}\) because \(I_0=2\mathcal E(H_{00})\) and scalar multiplication by 2 is an invertible map on this receiving vector space. The actual map \(J\) and its inverse retain that factor as AC2.3 and AC2.8 show.

Define the exact closure-difference object
\[
 D_{\rm cl}=\overline{I_0}^{\,\mathcal A}/I_0.
\]
Then there is the full equivariant exact sequence
\[
 0\longrightarrow D_{\rm cl}\longrightarrow C_{\rm alg}
 \longrightarrow Q\longrightarrow0.
\tag{AC4.2}
\]
This follows by taking representatives in \(\mathcal A\); its kernel consists exactly of the classes represented by \(\overline{I_0}\). No vanishing of \(D_{\rm cl}\), closedness of \(I_0\), or spectral synthesis is presumed. In particular \(H^0(C)\) is \(C_{\rm alg}\), not silently \(Q\).

ABR20–ABR22 also contain higher derived-coinvariant groups
\[
 H_n(G,M_0)=\Lambda^{n+1}W_{\rm pr}\otimes\mathbb C^2,\qquad n\geq1,
\]
with the exact exterior-order signs and action
\(\mathrm{id}_{\Lambda^{n+1}W_{\rm pr}}\otimes\operatorname{diag}(1,b)\). Periodization kills each of their displayed connecting representatives coefficient by coefficient. These remain retained higher data. The two-term complex AC3 is the expressly requested complex after degree-zero coinvariants; it is not claimed to be the entire derived adelic or geometric specialization complex.

## AC5. Every original finite spectral block and both endpoints

Let \(\rho\) be an actual nontrivial zero of the original \(\zeta\), with original multiplicity \(m_\rho\). Define the receiving algebra and original action
\[
 A_\rho=\mathbb C[t]/t^{m_\rho},\qquad
 W_{\rho,b}=b^\rho\exp((\log b)T),\qquad T=M_t.
\tag{AC5.1}
\]
The Mellin-jet map
\[
 L_\rho:\mathcal A\longrightarrow A_\rho,\qquad
 L_\rho(k)=\sum_{r=0}^{m_\rho-1}\frac{F_k^{(r)}(\rho)}{r!}t^r
\tag{AC5.2}
\]
is continuous: on each fixed vertical strip, powers of \(\log y\) in the derivatives are dominated by stronger seminorms of \(\mathcal A\). The same bounds show that \(F_k\) is entire. Since \(h\in H_{00}\) is even with \(h(0)=0\), it is \(O(x^2)\) at zero, so the second factor in AC2.6 is holomorphic in the critical strip. The multiplicity of the original zero thus proves
\[
 L_\rho J=0,\qquad L_\rho(\overline{I_0})=0.
\tag{AC5.3}
\]
The second assertion follows from continuity. Hence \(L_\rho\) factors through both \(C_{\rm alg}\) and \(Q\), with identical full jets. The entire \(D_{\rm cl}\) is in its kernel.

The prime action follows from \(y=bv\), with its full factors:
\[
 F_{W_bk}(s)=b^sF_k(s),\qquad
 L_\rho W_b=W_{\rho,b}L_\rho.
\tag{AC5.4}
\]
In particular \(L_\rho\) is a cochain map from AC3 to \(A_\rho\) in degree zero.

The two endpoint actions on each prime-labelled copy of \(\mathcal B_{\rm pr}\) are \(1\) and \(p\) at the fixed prime \(p>1\). The actual spectral block has sole eigenvalue \(p^\rho\). Because \(0<\Re\rho<1\),
\[
 1<|p^\rho|<p.
\tag{AC5.5}
\]
This uses the known critical strip, not RH.

For either endpoint character \(p^\epsilon\), \(\epsilon=0,1\), the conjugation operator on \(\operatorname{Hom}(A_\rho,\mathbb C_\epsilon)\) is exactly
\[
 h\longmapsto p^{\epsilon-\rho}h\exp(-(\log p)T).
\tag{AC5.6}
\]
Its nilpotent part is retained, and its single eigenvalue differs from 1 by AC5.5. The reverse Hom operator has sole eigenvalue \(p^{\rho-\epsilon}\ne1\). The finite geometric inverse of each operator minus the identity proves
\[
 \operatorname{Hom}_G(A_\rho,\mathcal B_{\rm pr})=0,\qquad
 \operatorname{Hom}_G(\mathcal B_{\rm pr},A_\rho)=0.
\tag{AC5.7}
\]
These statements also hold with all positive real actions. For the infinite direct sum, a map from finite-dimensional \(A_\rho\) has finite prime support; a map in the reverse direction is tested on each endpoint basis vector separately.

There is a stronger exact extension statement. In the category of complex modules over the abelian group algebra of either positive rational or positive real dilations,
\[
 \operatorname{Ext}^{n}(A_\rho,\mathcal B_{\rm pr})=
 \operatorname{Ext}^{n}(\mathcal B_{\rm pr},A_\rho)=0
 \qquad(n\geq0).
\tag{AC5.8}
\]
Here is a proof including the prerequisite for this use of Ext. The element \(z\) of the group algebra representing dilation by \(p\) is central. It satisfies
\[
 P(z)A_\rho=0,\quad P(X)=(X-p^\rho)^{m_\rho},
 \qquad
 R(z)\mathcal B_{\rm pr}=0,\quad R(X)=(X-1)(X-p).
\]
The polynomials have no common root by AC5.5, so the Euclidean algorithm gives \(uP+vR=1\). A central element acts on Ext in the same way through either variable: take a free resolution of the first module, on which multiplication by that central element is a chain map; on a module-linear cochain, precomposition by it equals postcomposition by its action on the target. If a polynomial acts as zero on the first module, its chain map on a free resolution is null-homotopic. To construct the homotopy, lift the degree-zero map into the kernel of the augmentation using freeness and exactness, then inductively lift the difference left after the preceding homotopy into the next kernel; exactness identifies that kernel with the next boundary. This constructs the required homotopy in every degree. Thus \(P\) and \(R\) both annihilate the displayed Ext groups, and \(uP+vR=1\) annihilates them only if they are zero.

For degree one an explicit section can also be given. In any extension \(0\to\mathcal B_{\rm pr}\to E\to A_\rho\to0\), choose a polynomial \(a(X)\) with
\[
 a(X)\equiv0\pmod{R(X)},\qquad a(X)\equiv1\pmod{P(X)}.
\]
Such a polynomial follows from the same Euclidean algorithm. Its action kills the boundary and induces identity on \(A_\rho\). Therefore \(v\mapsto a(z)\widetilde v\), for any lift \(\widetilde v\in E\), is independent of that lift, equivariant, and is a section. The difference of two equivariant sections is zero by AC5.7, so it is unique. This is a proved weight-separated lifting statement on the original endpoints and actual original zero blocks.

Neither AC5.7 nor AC5.8 asserts that these endpoints equal Deligne's entire geometric support group, or that \(C_{\rm alg}\) has no additional classes beyond its finite observed blocks.

## AC6. What lifts into the actual test space, and the exact defect

The finite jet observation itself has an explicitly constructed linear section, without an equivariance claim. Choose a nonnegative smooth compactly supported function \(\varphi\) on \(\mathbb R\) that is positive on an open interval. Put
\[
 M_{r\ell}=\int_{\mathbb R}\varphi(v)v^{r+\ell}\,dv,
 \qquad 0\leq r,\ell<m_\rho.
\]
For a nonzero coefficient vector \(c\),
\[
 \sum_{r,\ell}\overline c_r M_{r\ell}c_\ell
 =\int\varphi(v)\left|\sum_\ell c_\ell v^\ell\right|^2dv>0.
\]
The inequality holds because a nonzero polynomial cannot vanish on an open interval. Thus \(M\) is invertible. For \(a(t)=\sum_ra_rt^r\), define \(c=M^{-1}(r!a_r)_r\), \(P_a(v)=\sum_\ell c_\ell v^\ell\), and
\[
 s_\rho(a)(e^v)=e^{-(\rho-1/2)v}\varphi(v)P_a(v).
\tag{AC6.1}
\]
This is a compact logarithmic test in \(\mathcal A\). Substitution in AC2.5 gives \(F_{s_\rho(a)}^{(r)}(\rho)=r!a_r\), proving \(L_\rho s_\rho=\mathrm{id}\). No original-\(Q\) eigenvector has been postulated.

Let \(I_\rho=\ker L_\rho\). The actual test-space extension is
\[
 0\longrightarrow I_\rho\longrightarrow\mathcal A
 \xrightarrow{L_\rho}A_\rho\longrightarrow0.
\tag{AC6.2}
\]
Its kernel contains \(\overline{I_0}\); it is not the endpoint space \(\mathcal B_{\rm pr}\). On logarithmic coordinates, for \(b>0\), \(\ell=\log b\), its section defect is the fully explicit \(I_\rho\)-valued map
\[
 \begin{aligned}
 &(W_b s_\rho-s_\rho W_{\rho,b})(a)(e^v)\\
 &\quad=b^\rho e^{-(\rho-1/2)v}
 \left[
 \varphi(v-\ell)P_a(v-\ell)
 -\varphi(v)P_{\exp(\ell t)a}(v)
 \right].
 \end{aligned}
\tag{AC6.3}
\]
This follows from the exact \(b^{1/2}\) in \(W_b\), and linearity of \(P_a\). Applying \(L_\rho\) gives zero by AC5.4, proving the asserted target.

There is no equivariant section of AC6.2 into this \(\mathcal A\). This is a statement about its specified decay, not about the source arithmetic. To prove it, first suppose \(W_pk=\alpha k\), \(\alpha\ne0\). Evaluation at \(p^ny\) gives
\[
 k(p^ny)=(p^{1/2}/\alpha)^n k(y).
\]
For every \(N\), AC2.1 bounds its left side by a constant times \(p^{-nN}y^{-N}\) for sufficiently large \(n\). Choose \(N\) such that \(p^N|p^{1/2}/\alpha|>1\). The bound forces \(k(y)=0\) for every \(y\), hence \(k=0\). If \(\alpha=0\), invertibility of \(W_p\) gives the same result. Thus \(W_p-\alpha\) is injective, and so is every positive power.

Any equivariant map \(A_\rho\to\mathcal A\) has image annihilated by \((W_p-p^\rho)^{m_\rho}\); injectivity forces the map to be zero. A section cannot be zero. This proves the claim and, equivalently, that (AC6.2) has a nonzero equivariant extension class. Its cocycle \(W_b s_\rho W_{\rho,b}^{-1}-s_\rho\) cannot be a coboundary for this group action on \(\operatorname{Hom}(A_\rho,I_\rho)\), because such a correction would produce the excluded section.

Before this calculation, U10–U14 and the user's complete-history passages were checked as recorded in AC0. The proof uses the already reconstructed full arithmetic and the original strong test-space definition. It does not add a metric to \(\tau\), treat an incomplete prime list as complete, assume that the prime quotient fails, claim that \(Q\) has no eigenvectors, or exclude a lift in another receiving completion. Its precise failed map is a section into rapidly decaying tests. The following section constructs the exact receiving space in which the spectral data do live.

## AC7. The corresponding dual distributions and their full-jet map

Let \(\mathcal A'\) be the continuous complex-linear dual of \(\mathcal A\). Define, for every original zero and each \(0\leq r<m_\rho\),
\[
 \lambda_{\rho,r}(k)
 =\frac1{r!}\int_0^\infty
 k(y)y^{\rho-1/2}(\log y)^r\frac{dy}{y}.
\tag{AC7.1}
\]
Every such functional is continuous by the estimates in AC5. Its distribution density, including the original exponent \(1/2\), is shown explicitly. The surjectivity constructed in AC6 proves that these functionals are linearly independent.

The exact transpose of the observation map is
\[
 L_\rho^*:A_\rho^*\hookrightarrow\mathcal A',\qquad
 \ell\longmapsto\ell\circ L_\rho.
\tag{AC7.2}
\]
For the coordinate functionals \(\ell_r(a)=a_r\), it is precisely \(\lambda_{\rho,r}\). It lands in the annihilator of \(\overline{I_0}\), by AC5.3. If \(Q\) is given its quotient topology, pullback identifies \(Q'\) exactly with that annihilator: a continuous functional on \(\mathcal A\) vanishing on the closed subspace defines a unique functional on the quotient, and the definition of quotient topology proves its continuity. Thus the same exact injection is
\[
 A_\rho^*\hookrightarrow Q'\hookrightarrow\mathcal A'.
\tag{AC7.3}
\]
It is an injection into the dual of the actual quotient, not an asserted injection into \(Q\) itself.

For precision about orientation, the transpose action below is \(W_b^{\rm tr}\lambda=\lambda\circ W_b\). Because the dilation group is abelian, these transposes form an action with the same product law. Differentiating \(b^sF_k(s)\), with every factorial retained, gives
\[
 W_b^{\rm tr}\lambda_{\rho,r}
 =b^\rho\sum_{j=0}^{r}
 \frac{(\log b)^{r-j}}{(r-j)!}\lambda_{\rho,j}.
\tag{AC7.4}
\]
This is the complete transpose primary block, including its nilpotent. If the contragredient convention is wanted instead, it is explicitly \(\lambda\mapsto\lambda\circ W_{b^{-1}}\), with
\[
 b^{-\rho}\sum_{j=0}^{r}
 \frac{(-\log b)^{r-j}}{(r-j)!}\lambda_{\rho,j}.
\tag{AC7.5}
\]
Neither sign convention is substituted silently.

Consequently the decay calculation in AC6 identifies the correct receiving distinction and supplies its connecting morphism: original spectral blocks are finite *quotients* of the test space and become finite *subspaces of distributions* by the exact transpose map. The distributional characters are not lost when no test-function eigenvector exists. All original zero observations and multiplicities remain.

## AC8. All support labels and what is not being collapsed

For any bounded distributive lattice \(L\), retain
\[
 G_L(V)=\{(0,\lambda):\lambda\in L\}\cup(V\times\{1_L\}).
\]
Every already constructed linear map \(f\) has the common-label lift
\[
 (v,\lambda)\longmapsto(f(v),\lambda).
\tag{AC8.1}
\]
This is well-defined: a nontop input label forces zero amplitude and linear maps preserve that amplitude. It preserves receiving addition with join labels, scalar action with meet labels, identities and composition by direct substitution. These receiving operations are not an addition on primitive \(Z_1/\tau\).

For the complex AC3, amplitude-zero cycles in degree \(-1\) are exactly \(G_L(j\mathcal B_{\rm pr})\). The same-label quotient in degree zero by \(I_0\) is \(G_L(C_{\rm alg})\). The further same-label quotient by \(D_{\rm cl}\) is \(G_L(Q)\). The maps (AC2.11), (AC3.2) and (AC7.2) lift in this same sense, so their proven amplitude identities preserve every label.

In particular a zero connecting map returns \((0,\lambda)\), not a constant bottom label. The common-label object \(G_L(I_0\oplus\mathcal B_{\rm pr})\) is not silently replaced by the product \(G_L(I_0)\times G_L(\mathcal B_{\rm pr})\), which permits independent labels. A construction with independent block labels must display those additional label coordinates separately; none is forgotten here. The inherited ABR notation identifying an older bottom supported-zero label with a symbol tau is not imported as an identification with the current primitive \(Z_1/\tau\).

## AC9. Exact conclusions for the requested lifting calculation

The actual adelic two-term complex has the explicit equivariant decomposition (AC3.2). Its endpoint two-extension and the connecting maps furnished by ABR17 vanish, with the original \(y^{1/2}\), factor 2, both endpoint characters and every prime label retained. Independently, every finite original nontrivial-zero block has vanishing Hom and all equivariant extension groups to or from the endpoint space, by the computed separation \(1<|p^\rho|<p\). This is a completed weight-separated lifting result on actual programme modules, not the earlier auxiliary polynomial extension.

The calculation also determines the exact scope. The actual Mellin-jet kernel \(I_\rho\) is larger than the endpoint boundary and retains the closure difference and other unobserved test data. Its test-space extension (AC6.2) does not have an equivariant section; its full defect and its distributional receiving map are explicitly constructed. This is no statement about whether original \(Q\) has eigenvectors in another realization.

The extension splitting and endpoint weight separation hold for every actual zero in the entire open critical strip. They do not narrow that strip to its midpoint. No geometric specialization diagram identifying these particular endpoint modules with Deligne's complete support-obstruction groups has been assumed, and no RH conclusion is claimed. The retained complex, its original cohomology, its closure difference, its exact dual morphism and the surviving source labels are the mathematical output.

## Current propagation from OMS — 24 September 2026

[The complete synthesis proof](ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), OMS1–OMS5, proves that the original summation image is closed and that the full actual-zero jet map on Q has zero common kernel. Its image remains a proper dense subspace of the unrestricted product, carrying the stronger original quotient topology. Earlier statements leaving those two questions undetermined are superseded by that proof, not by an assumption. Every original zero multiplicity and support label remains.

OMS7A proves the exact return to AC0–AC4: the same original spaces give I0=2 E(S)=E(S), with the factor 2 retained in the periodization map and inverse. Thus D_cl=0, C_alg→Q is the identity-induced topological isomorphism, and the specific global two-extension class of the actual adelic two-term complex is zero. Both endpoint contributions at each prime and the higher derived-coinvariant groups remain unchanged. No vanishing of the entire Ext group or full tau purity is inferred.

## Global adelic lifting propagation - 24 September 2026

The complete current proofs are GLOBAL_ADELIC_LIFTING_AND_PRIME_BOUNDARY.md GAP0–GAP9 (including GAP6A–GAP6B), COMPLETE_GENERATOR_ENDPOINT_RETURN.md GER0–GER7, GLOBAL_ENDPOINT_EXTENSION_RETURN.md GEX0–GEX9, and COMPLETE_COMPARISON_TRIANGLE_FORMALITY.md CTF0–CTF8. Every original prime wedge, endpoint pair and nilpotent jet is retained. GER credits the existing RZ endpoint resolvents and gives their explicit original Schwartz return and covariance corrections. GEX proves vanishing of the entire extension groups between the whole actual Q and the stated endpoint modules, in the explicitly constructed algebraic and strict locally convex operator categories. This strengthens the earlier finite-block and particular-extension assertions without assigning that theorem to a larger unspecified category.

GAP and CTF construct the full derived adelic complex, its canonical cohomology map, the exact original CC comparison and its entire cone. The faithful coefficient copies distinguish primitive tau from integer one in both objects. All additional cone contractions and the final-arrow homotopy are explicit; no test-space section Q→A is asserted. On the separate supported-Q row the same polynomial is invertible, rather than zero. Full tau numerical purity does not follow from endpoint separation and remains unproved.
