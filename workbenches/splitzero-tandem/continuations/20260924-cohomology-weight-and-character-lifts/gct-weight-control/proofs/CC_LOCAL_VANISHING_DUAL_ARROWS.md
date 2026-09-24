# Local vanishing arrows and the actual global residue pairing

Complete derivation, 24 September 2026. Proof locators LVD0–LVD9.


Historical attribution: these nearby/vanishing-cycle constructions go back to Deligne’s SGA7, ExposésXIII–XIV, and Beilinson’s *How to glue perverse sheaves*. The inspected explanatory author source is Ryan Reich, [Notes on Beilinson’s “How to glue perverse sheaves”, arXiv:1002.1686v4](https://arxiv.org/abs/1002.1686v4), definitions and gluing maps at the source ranges recorded above. Credit to those originals is retained through Reich; this edition does not claim a fresh reading of the original SGA or Beilinson chapters.

Human-source attribution: the extension of continuous linear functionals is the Hahn–Banach theorem, not a programme result. See Terence Tao, [245B, Notes6: Duality and the Hahn–Banach theorem](https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/), Theorem1 and its complex proof (26 January2009). For the locally convex use here, continuity bounds a functional by a continuous seminorm; quotienting its kernel reduces this application to that normed-space theorem. No continuous splitting of the original quotient is thereby asserted.

Human-source attribution: the unconditional zero-counting estimate is the classical Riemann–von Mangoldt theorem. The inspected native-TeX witness is Alain Connes, [The Riemann Hypothesis: Past, Present and a Letter Through Time](https://arxiv.org/abs/2602.04022v1), the Hardy–Littlewood discussion immediately before “Zero-free regions and zero-density estimates” (author TeX line499). It states the asymptotic that implies the bound used here; this is not a new zero-counting theorem.

## LVD0. Constructed source and scope

The supporting datum is still \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). This calculation acts on CSP's receiving sheaf after the complete arithmetic reconstruction. No addition, midpoint, metric, numerical coordinate or new parity is assigned to that support. The map of receiving spaces is
\[
\pi:\mathbb P^1(\mathbb C)\longrightarrow\{x_+,\eta,x_-\},\qquad
\pi(0)=x_+,\quad\pi(\infty)=x_-,\quad\pi(\mathbb C^\times)=\eta.
\tag{LVD0.1}
\]
In particular a pole disk is not a numerical chart on \(\tau\). Both arithmetic branches retain their own reconstructed counters. Gluing the two geometric charts of this one sheaf is not pooling two arithmetic return measures.

The source is the actual restriction diagram derived from Alain Connes and Caterina Consani, *Schemes over \(\mathbb F_1\) and zeta functions*, [arXiv:0903.2024v3](https://arxiv.org/abs/0903.2024v3), §5, with the later support and real-structure comparison to [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299v1). CSP0 records the exact author-TeX reading. CSP, CSD and SSI/ESI prove the coefficient, inverse-image and continuous-dual constructions used here. DC proves the distinct Deligne invariant-cycle cross; no identity with its arithmetic weight hypotheses is presumed.

For nearby and vanishing cycles, Ryan Reich's original author source, *Notes on Beilinson's “How to glue perverse sheaves”*, [arXiv:1002.1686v4](https://arxiv.org/abs/1002.1686v4), supplies the universal-cover and cone definitions. Its author TeX lines261–303 and356–375 give the defining triangles; lines850–911 give the gluing maps; lines1161–1220 identify the shifted vanishing functor. The finite-constructibility assertions of that paper are not applied to these infinite coefficient spaces. Every local complex below is calculated directly.

Use cohomological shifts, \(C[1]^n=C^{n+1}\), \(d_{C[1]}=-d_C\), and
\[
\operatorname{Cone}(f)^n=B^n\oplus A^{n+1},\qquad
d(b,a)=(d_Bb+fa,-d_Aa)
\tag{LVD0.2}
\]
for \(f:A\to B\). Derived sheaf statements are in sheaves of complex vector spaces. Coefficient maps retain their actual locally convex topologies. A derived category of arbitrary topological vector spaces is not assumed.

## LVD1. The full original coefficient row

Retain
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\},
\]
\[
A=\left\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^j a(u)|<\infty
\text{ for every }N,j\ge0\right\},
\]
\[
\Sigma f(u)=2\sum_{k\ge1}f(ku),\quad Ra(u)=u^{-1}a(u^{-1}),\quad
V_p=S\oplus E_p,\quad E_p=\mathbb C e_{p,0}\oplus\mathbb C e_{p,1},
\]
\[
r_+(f,e)=\Sigma f,\qquad r_-(f,e)=R\Sigma f=\Sigma\widehat f,\qquad
\widehat f(t)=\int_{\mathbb R}f(v)e^{-2\pi ivt}\,dv.
\tag{LVD1.1}
\]
Before restriction to \(S\), Poisson summation contains the full terms
\[
\Sigma\widehat f(u)=u^{-1}\Sigma f(u^{-1})+u^{-1}f(0)-\int_{\mathbb R}f(v)\,dv.
\tag{LVD1.2}
\]
The two endpoint coordinates on each chart are retained separately. SSI/ESI prove that \(J=\Sigma S\) is closed in \(A\), that \(\Sigma:S\to J\) has continuous inverse, and that
\[
0\longrightarrow J\xrightarrow{\iota}A\xrightarrow{q}Q=A/J\longrightarrow0
\tag{LVD1.3}
\]
is the actual strict Fréchet quotient row.

On a disk \(D_p\) around one pole, write \(i:\{p\}\hookrightarrow D_p\) and \(j:D_p^*\hookrightarrow D_p\). CSP's sheaf is
\[
\mathscr F|_{D_p}=\underline A_{D_p}\times_{i_*A}i_*V_p.
\tag{LVD1.4}
\]
The source inverse gives continuous decompositions \(V_p=J\oplus E_p\) with restriction \((b,e)\mapsto b\). Explicitly the section of \(r_+\) is \(b\mapsto(\Sigma^{-1}b,0)\); for \(r_-\) it is \(b\mapsto(\widehat{\Sigma^{-1}b},0)\). Hence
\[
\mathscr F|_{D_p}\simeq\mathscr F_{\rm red}\oplus i_*E_p,\qquad
\mathscr F_{\rm red}=\ker(\underline A_{D_p}\xrightarrow{q\,\mathrm{ev}_p}i_*Q).
\tag{LVD1.5}
\]
This is an explicit decomposition of the existing sheaf, not deletion of endpoints. It gives the exact sheaf row
\[
0\to\mathscr F_{\rm red}\to\underline A_{D_p}\xrightarrow{q\,\mathrm{ev}_p}i_*Q\to0.
\tag{LVD1.6}
\]
Set \(\mathsf P=\mathscr F_{\rm red}[1]\). A representative is \(\operatorname{Cone}(q\,\mathrm{ev}_p)\); its terms are \(\underline A\) in degree \(-1\) and \(i_*Q\) in degree zero, with differential \(+q\,\mathrm{ev}_p\). With the literal injection and projection of this cone, the rotated triangle is
\[
i_*Q\longrightarrow\mathsf P\longrightarrow\underline A[1]
\xrightarrow{-q\,\mathrm{ev}_p[1]}i_*Q[1].
\tag{LVD1.7}
\]
The displayed minus is the rotation sign.

## LVD2. Nearby cycles from the actual universal cover

Use the positive local coordinate \(z_p=z\) at zero and \(z_p=1/z\) at infinity. The map \(t\mapsto e^t\) from the covering half-plane is the universal cover of a sufficiently small punctured disk. The pullback of \(\mathscr F_{\rm red}|_{D_p^*}=\underline A\) is constant. The coefficient-valued de Rham resolution contracts on that half-plane: the radial homotopy integrates along the line segment to a fixed interior point. Completeness of \(A\) gives the integrals; for every seminorm the bound \(p(\int f)\le\int p(f)\) proves continuity. The only cohomology is the constant coefficient \(A\) in degree zero.

Deck translation \(t\mapsto t+2\pi i\) fixes these constants. Therefore
\[
R\psi_{z_p}\mathscr F_{\rm red}=A[0],\qquad T=1,\qquad
R\psi_{z_p}\mathsf P=A[1].
\tag{LVD2.1}
\]
The stalk of \(\mathscr F_{\rm red}\) is \(J\), and its specialization to nearby constants is the actual inclusion \(\iota:J\to A\). Put \(\Psi=R\psi[-1]\) and \(\Phi=R\phi[-1]\), with \(R\phi\) the cone of specialization. Then
\[
\Psi\mathsf P=A,
\qquad\Phi\mathsf P\simeq[J\xrightarrow{\iota}A]
\simeq Q[0],
\qquad\mathrm{can}=q.
\tag{LVD2.2}
\]
The two terms of the displayed complex have degrees \(-1,0\). Starting with the literal shifted cone gives differential \(-\iota\); negating its \(J\)-coordinate gives the displayed complex and leaves the quotient map on \(A\) unchanged.

No rank hypothesis is used. In particular the quotient in (LVD2.2) includes all actual zero jets, not only the values visible to the trace form later.

## LVD3. The positive-angle convention fixes variation

Let \(\vartheta_p=d\arg z_p/(2\pi)\) be the positive angular class. For the constant nearby complex \(C=R\psi K\), the punctured-disk complex is \(C\oplus C[-1]\), with the second summand the positive angular coordinate. Write the actual restriction as
\[
(u,v):S=i^*K\longrightarrow C\oplus C[-1].
\tag{LVD3.1}
\]
The shifted vanishing complex \(\operatorname{Cone}(u)[-1]\) has differential
\[
d(c,s)=(-d_Cc-us,d_Ss).
\tag{LVD3.2}
\]
Define
\[
\mathrm{can}(c)=(c,0),\qquad\mathrm{var}(c,s)=v(s).
\tag{LVD3.3}
\]
These are chain maps. Indeed the first uses the differential \(-d_C\) on \(C[-1]\); the second uses the chain identity for \(v:S\to C[-1]\). Permuting coordinates identifies \(\operatorname{Cone}(\mathrm{var})[-1]\) with the restriction fibre cone \(\operatorname{Cone}((u,v))[-1]\), including its differentials. This constructs variation with the chosen positive angular sign. Its sign is not deduced from the equation \(\mathrm{var}\,\mathrm{can}=1-T=0\), which by itself would not determine a sign.

For \(K=\mathsf P\), the restriction is \((\iota[1],0)\). Thus
\[
\boxed{\Psi\mathsf P=A,\quad\Phi\mathsf P=Q,\quad
\mathrm{can}=q,\quad\mathrm{var}=0.}
\tag{LVD3.4}
\]
The costalk is, after negating the shifted \(J\)-coordinate,
\[
i^!\mathsf P=[J\xrightarrow{\iota}A\xrightarrow0A]
\quad\text{in degrees }-1,0,1.
\tag{LVD3.5}
\]
Its cohomology is \(Q\) in degree zero and \(A\) in degree one. Before the cochain shift, the boundary of the positive angular class is minus the positive local fundamental class, as CSP6 proves by \(-d\chi\wedge\vartheta_p\). That orientation convention is retained; (LVD3.5) is a shifted complex, not a changed angular orientation.

## LVD4. The dual arrows, with their full chain signs

Write \(d=*\) for the algebraic dual or \(d='\) for the continuous dual, retaining their distinct domains. For \(d=*\) take ordinary Verdier duality. For \(d='\) take CSD's literal continuous compact-test current complex and shift it by \([-1]\); denote that specific object by \(D_c\mathsf P\). No equivalence between these duals is asserted. Put \(U=A^d\).

CSD5–6 (and the algebraic current comparison VSD) calculate the dual stalk, restriction and costalk by explicit currents. For the endpoint-reduced shifted object they give
\[
i^*D_d\mathsf P=
[U\xrightarrow0U\xrightarrow{-\iota^d}J^d]
\quad\text{in degrees }-1,0,1,
\tag{LVD4.1}
\]
\[
R\psi D_d\mathsf P=U[1],\qquad i^!D_d\mathsf P=J^d[-1].
\tag{LVD4.2}
\]
Restriction to the puncture is identity on the first \(U\) into its degree \(-1\) constant coordinate and identity on the second \(U\) into its degree-zero angular coordinate. The final \(J^d\) restricts to zero. The minus in (LVD4.1) is the differential of the shift of CSD's dual stalk; it is not omitted.

Apply (LVD3.2). The vanishing complex has \(U\) in degree \(-1\), \(U\oplus U\) in degree zero and \(J^d\) in degree one, with
\[
b\mapsto(-b,0),\qquad(a,b)\mapsto-\iota^d b.
\tag{LVD4.3}
\]
The first pair is contractible. The remaining complex is
\[
[U\xrightarrow{-\iota^d}J^d]\quad\text{in degrees }0,1.
\tag{LVD4.4}
\]
Algebraic extension of functionals, or Hahn–Banach for the continuous dual of the closed subspace \(J\subset A\), proves that \(\iota^d\) is onto. Its kernel is exactly the image of \(q^d:Q^d\to A^d\). Hence (LVD4.4) has cohomology \(Q^d\) in degree zero, represented by \(q^d\mu\). The canonical map lands in the contracted coordinate \((a,0)\); variation maps \((a,b)\) to \(b\). Consequently
\[
\boxed{\Psi D_d\mathsf P=A^d,\quad\Phi D_d\mathsf P=Q^d,\quad
\mathrm{can}=0,\quad\mathrm{var}=+q^d.}
\tag{LVD4.5}
\]
The plus has just been proved in the positive angular coordinate. A literal dual of the primal two-term stalk has differential \(-q^d\); that minus remains in the corresponding shifted restriction cone. The assertion is not a convention-independent unsigned transpose formula.

For \(d='\), SDT proves \(q':Q'_\beta\simeq J^\perp\subset A'_\beta\) topologically by bounded lifts. CSD proves the stated stable small-disk cohomology topologies. This argument does not assert strong openness of \(A'_\beta\to J'_\beta\).

The full endpoint summands are
\[
\mathsf P_{\rm full}=\mathsf P\oplus i_*E_p[1],\qquad
D_d\mathsf P_{\rm full}=D_d\mathsf P\oplus i_*E_p^d[-1].
\tag{LVD4.6}
\]
They have zero nearby cycles and shifted vanishing summands \(E_p[1]\) and \(E_p^d[-1]\), respectively. They have not been absorbed into the degree-zero \(Q\) or \(Q^d\).

## LVD5. All degree-zero sheaf pairings factor through the constant part

The dual of the exact source triangle, or the direct current-cone construction, gives
\[
\underline{A^d}[1]\longrightarrow D_d\mathsf P\longrightarrow i_*Q^d
\longrightarrow\underline{A^d}[2].
\tag{LVD5.1}
\]
Its final Gysin sign depends on the stated quotient coordinate; the positive-angular construction of the separate residue Gysin receiver retains it explicitly. Only the existence of these actual arrows is needed for the following factorization.

Put \(C=\underline A[1]\), \(S_0=i_*Q\), and \(C^d=\underline{A^d}[1]\). From (LVD4.2) and adjunction,
\[
\operatorname{Hom}(S_0,D_d\mathsf P)=
\operatorname{Hom}(Q,J^d[-1])=0,
\quad
\operatorname{Hom}(S_0[1],D_d\mathsf P)=0.
\tag{LVD5.2}
\]
These are degree-zero derived Hom groups over a field; the negative shifts make them zero. Applying Hom to (LVD1.7) therefore shows that every \(f:\mathsf P\to D_d\mathsf P\) factors uniquely through \(\mathsf P\to C\). Also
\[
\operatorname{Hom}(C,i_*Q^d)=
\operatorname{Hom}(A[1],Q^d)=0,
\quad
\operatorname{Hom}(C,i_*Q^d[-1])=0.
\tag{LVD5.3}
\]
Applying Hom to (LVD5.1) now proves the unique factorization
\[
\boxed{f:\mathsf P\longrightarrow\underline A[1]
\xrightarrow{h[1]}\underline{A^d}[1]\longrightarrow D_d\mathsf P.}
\tag{LVD5.4}
\]
Here \(h:A\to A^d\) is an arbitrary coefficient-linear map. The continuous coefficient construction uses continuous \(h\); the factorization theorem itself is stated in the underlying vector-space sheaf category. The same proof holds with a conjugate source and \(h:\overline A\to A^d\).

Its induced vanishing map is zero. Equivalently the natural canonical-arrow square has \(\Phi(f)q=0\), since the target canonical map in (LVD4.5) is zero; surjectivity of \(q\) forces \(\Phi(f)=0\). Thus no such map is an isomorphism when \(Q\ne0\). This computes the precise local arrow; it does not exclude pairings on nearby coefficients or global cohomology.

The source triangle (LVD1.7) itself is nonsplit when \(Q\ne0\). Indeed \(\mathsf P=\mathscr F_{\rm red}[1]\) has ordinary sheaf cohomology \(\mathcal H^0(\mathsf P)=0\), whereas the direct sum required by a split triangle has \(\mathcal H^0(i_*Q\oplus\underline A[1])=i_*Q\ne0\). This is a direct derived-sheaf proof; it requires no finite-rank perverse-sheaf theorem or unconstructed topological heart.

The same factorization holds on the entire sphere with \(i_*Q\) replaced by the two-pole skyscraper \(i_*(Q\oplus Q)\). The support/stalk adjunctions are the direct sums of (LVD5.2)–(LVD5.3). Retaining endpoints introduces no further degree-zero pairing maps: the cross groups are
\[
\operatorname{Hom}(E_p[1],J^d[-1])=0,
\qquad\operatorname{Hom}(J[1],E_p^d[-1])=0,
\qquad\operatorname{Hom}(E_p[1],E_p^d[-1])=0.
\tag{LVD5.5}
\]
Maps between distinct supported poles vanish as well. All vanish by adjunction and the indicated negative shift, without discarding an endpoint.

Since \(H^1(\mathbb P^1(\mathbb C);\underline A)=0\), every degree-zero sheaf pairing of (LVD5.4) induces the zero map on \(H^0(R\Gamma\mathsf P)=Q\). The equality for constant-sheaf cohomology follows from the two-disk/circle resolution of CSP3 and does not require finite-dimensional \(A\).

## LVD6. The original-zeta residue pairing is nevertheless nonzero

Use the existing full transform
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\,\frac{du}{u},\qquad
\kappa:Q\xrightarrow{\sim}\mathcal B/\mathcal I,\quad[a]\mapsto[\Theta a],
\tag{LVD6.1}
\]
where \(\mathcal B\) is the entire rapid-decay space on every closed vertical strip, and \(\mathcal I\) is the full ideal of jets vanishing to the actual multiplicities of all nontrivial zeros of the original \(\zeta\). Let \(\rho^\#=1-\overline\rho\). The proved residue/trace receiver RTT gives the continuous linear map with conjugate source
\[
\mathcal W:\overline Q\longrightarrow Q'_\beta,\qquad
\mathcal W(\overline{[b]})([a])
=\sum_\rho m_\rho\,\Theta a(\rho)\,
\overline{\Theta b(\rho^\#)}.
\tag{LVD6.2}
\]
The sum runs over distinct actual zeros; \(m_\rho\) is retained. It is the full-zero value trace, not an identification of the full-jet quotient with its values. Its absolute convergence follows by choosing strip-decay exponent \(N\) with \(2N>2\) and using the original zero-counting bound \(N_\zeta(T)=O(T\log(2+T))\). The sum of \(m_\rho(1+|\operatorname{Im}\rho|)^{-2N}\) then converges. The same estimate, uniformly on bounded subsets of \(Q\) using the proved quotient seminorms/bounded lifts, gives strong-dual continuity, as RTT1 proves.

Retain the entire original transform of the actual Schwartz test:
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{LVD6.3}
\]
At an actual zero \(\sigma\) of multiplicity \(m_\sigma\),
\(F_\sigma(s)=F_0(s)/(s-\sigma)^{m_\sigma}\) is entire and belongs to \(\mathcal B\). The complete local unit gives \(F_\sigma(\sigma)\ne0\), while \(F_\sigma\) vanishes at every other zero with its full multiplicity. This proves \(Q\ne0\). Taking \(F_\sigma\) and \(F_{\sigma^\#}\) in (LVD6.2) proves that \(\mathcal W\ne0\), with no assumption of RH or simple zeros. Applying these isolators separately also proves
\[
\ker\mathcal W=\overline{N_0},\qquad
N_0=\{[a]\in Q:\Theta a(\rho)=0\text{ for every actual }\rho\}.
\tag{LVD6.4}
\]
Higher jets in \(N_0\) are retained as this exact kernel, not identified with zero in \(Q\).

The original unit, pole and trivial-zero contributions remain
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r),\qquad r\ge1.
\tag{LVD6.5}
\]
The source equality is \(\mathcal M_0\Sigma f=2\zeta\,\mathcal M_0 f\) on \(\Re s>1\), with the full factor2; \(\Theta=\mathcal M_0/2\). RTT's residue comparison uses the complete original logarithmic derivative, not a substituted zeta. Nothing in the sheaf calculation alters these source identities or the retained arithmetic return measure.

## LVD7. Explicit realization on the complete global complex

Let \(W_0=V_+\oplus V_-\) and \(r=r_+-r_-:W_0\to A\). CSP's complete sphere complex for \(\mathscr F\) is
\[
D_{\mathscr F}=[W_0\xrightarrow{r}A\xrightarrow0A]
\quad\text{in degrees }0,1,2.
\tag{LVD7.1}
\]
Thus \(K=D_{\mathscr F}[1]\) has degrees \(-1,0,1\) and differential \(-r\) from degree \(-1\) to zero. Its continuous Hom dual, with
\((K^\vee)^n=(K^{-n})'\) and \(d^\vee_n=(-1)^{n+1}(d_K^{-n-1})'\), is
\[
K^\vee=[A'\xrightarrow0A'\xrightarrow{+r'}W_0']
\quad\text{in degrees }-1,0,1.
\tag{LVD7.2}
\]
CSD's explicit proper global current comparison realizes this dual with its shift sign retained. Its previously displayed complex is \(D_{\mathscr F}^{\vee}[-1]\), whose last differential is \(-r'\), while (LVD7.2) has \(+r'\). The isomorphism from (LVD7.2) to that shifted complex multiplies degree \(n\) by \((-1)^n\): its signs in degrees \(-1,0,1\) are \(-1,+1,-1\). Substituting the differentials verifies the chain identity. In particular the degree-zero pairing below is unchanged. No assertion that arbitrary continuous dualization preserves quasi-isomorphisms is required.

Define the actual continuous coefficient arrow
\[
h=q'\,\mathcal W\,\overline q:\overline A\longrightarrow A'.
\tag{LVD7.3}
\]
Set a cochain map \(\mathfrak w:\overline K\to K^\vee\) to be zero in degrees \(-1,1\) and \(h\) in degree zero. Both chain identities follow from the original quotient row:
\[
h\,\overline r=q'\mathcal W\,\overline{qr}=0,
\qquad r'h=(qr)'\mathcal W\,\overline q=0.
\tag{LVD7.4}
\]
These identities retain the source differential \(-r\) and target differential \(+r'\). On cohomology,
\[
H^0(K)=A/J=Q,\qquad H^0(K^\vee)=\ker r'=q'Q',
\quad H^0(\mathfrak w)=\mathcal W
\tag{LVD7.5}
\]
under the specified quotient and transpose identifications.

Therefore the original residue pairing has an explicit continuous representative on the complete global cohomology complex, including its endpoint and degree-two terms. It is nonzero by (LVD6.2)–(LVD6.4). By (LVD5.4)–(LVD5.5), it cannot be induced by a degree-zero sheaf morphism
\(\overline{\mathsf P_{\rm full}}\to D_c\mathsf P_{\rm full}\)
on this sphere: every such sheaf morphism induces zero in this cohomological degree. This is the precise difference between the constructed global pairing and a pairing compatible with restriction to every open set. It neither denies the global pairing nor replaces its continuous coefficients by finite-dimensional ones.

The calculation constructs an entire receiver, not only one example. In the ordinary vector-space derived category put
\[
\mathcal G=\operatorname{Hom}_{D(\mathbb C)}
(\overline{R\Gamma\mathsf P_{\rm full}},R\Gamma D_*\mathsf P_{\rm full}),
\qquad
\mathcal L=\operatorname{im}\bigl(
\operatorname{Hom}_{D(Y)}(\overline{\mathsf P_{\rm full}},D_*\mathsf P_{\rm full})
\xrightarrow{R\Gamma}\mathcal G\bigr).
\tag{LVD7.6}
\]
The existing algebraic current comparison identifies the target global complex with \(K^*\); its shift signs are exactly those above. Taking degree-zero cohomology defines
\[
\Pi:\mathcal G\longrightarrow\operatorname{Hom}_{\mathbb C}(\overline Q,Q^*).
\tag{LVD7.7}
\]
For any \(W:\overline Q\to Q^*\), the formula \(H_W^0=q^*W\overline q\), \(H_W^{-1}=H_W^1=0\), defines a cochain map by the same two identities (LVD7.4). Its derived class gives a linear map \(\mathcal J:W\mapsto[H_W]\), and \(\Pi\mathcal J=1\) because of (LVD7.5). Since (LVD5.4) proves \(\Pi\mathcal L=0\), these maps induce a split exact sequence
\[
0\to\ker\overline\Pi\to\mathcal G/\mathcal L
\xrightarrow{\overline\Pi}\operatorname{Hom}_{\mathbb C}(\overline Q,Q^*)\to0,
\qquad \overline\Pi\,\overline{\mathcal J}=1.
\tag{LVD7.8}
\]
This proves the specified full pairing space is a direct summand of the difference between global derived maps and maps coming from sheaves. It does not claim the other summand is zero. No topology is assigned to this algebraic cokernel. The continuous maps \(W:\overline Q\to Q'_\beta\) enter it through the actual inclusion \(Q'\hookrightarrow Q^*\) and the continuous chain representatives just constructed. The actual \(\mathcal W\), with its retained kernel \(\overline{N_0}\), is one nonzero member. This is an exact receiver for the failed local realization, with its injection and left inverse proved.

## LVD8. What the comparison supplies for the next lift

The earlier separator calculation FOD7 proves that the actual normal connecting class vanishes after every specified source \(\mathcal Q[k]\) in the stated derived category of \(M\)-modules, where \(M\) is the constructed entire multiplier algebra. This is not a vanishing for arbitrary sheaf maps from \(i_*Q[k]\) into the local triangle, and it does not identify all local canonical maps with zero. The local canonical map calculated here is the original quotient \(q:A\to Q\). Its dual has canonical map zero and variation \(+q'\). Both statements are compatible through the explicit source and normal extension rows calculated in FOD/NEA and the nearby-cycle comparison.

The next attempted lift is now specified by actual arrows rather than by a proposed positivity assumption: lift the supported map \(i_*\mathcal W:i_*\overline Q\to i_*Q'\) through the continuous-dual triangle (LVD5.1). Its connecting map is the Gysin image of \(q'\mathcal W\), with the quotient-coordinate sign retained. The pullback of that triangle constructs a receiver even when this connecting map is nonzero. The separate full Gysin-receiver derivation calculates it directly, including its kernel \(\overline{N_0}\). This is the concrete continuation of (LVD7.5); the missing sheaf map is not installed as a hypothesis.

Deligne's exact obstruction in DC is \(\operatorname{im}\partial/\partial K\), with its own specialization, inertia and duality. The new maps determine how the actual coefficient quotient and its residue pairing enter a local specialization/duality calculation. They do not identify the present nonconstant infinite coefficient sheaf with a proper smooth-total finite-field family, or derive its arithmetic purity from its zero topological monodromy. The nonzero residue pairing, its global representative, and the precise local Gysin receiver are all retained for that comparison.

## LVD9. Verification scope

Every displayed local group and arrow was derived from the actual disk, puncture, source restriction and current cone. The full endpoint summands, both poles, cochain shifts, transpose signs, source kernels and value-trace kernel are recorded. The factorization theorem is about this degree-zero sheaf arrow. The global cochain pairing is proved on the complete original complex, not merely on a list of eigenvalues. No conclusion about RH, a common arithmetic modulus, or the completion of WU061 is claimed by these statements.
