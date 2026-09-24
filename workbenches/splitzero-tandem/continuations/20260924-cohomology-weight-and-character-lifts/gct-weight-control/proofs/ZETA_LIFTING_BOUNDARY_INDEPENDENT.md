# The connecting boundary of the original-zeta germ extension

Independent derivation, 24 September 2026. Proof locators ZLB0–ZLB11.

## ZLB0. The construction being tested and the source dependencies

The input is the original Riemann zeta function obtained after the complete arithmetic reconstruction, together with the actual local quotient in OZR5 and arithmetic multiplication in OZR6 of [Original zeta reflection and descent](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/ORIGINAL_ZETA_REFLECTION_AND_DESCENT.md). This note computes the boundary of that explicitly specified analytic extension. It does not identify its eigenvector-lifting problem with every lift required by the user's construction or by a possible Deligne comparison.

The supporting datum remains
\[
\tau\langle Z_1;\text{no }Z_2\rangle.
\tag{ZLB0.1}
\]
No addition, subtraction, coordinate, metric, or vector is assigned to it. The coordinate \(s\), the analytic germs, the vector spaces, and the recovered arithmetic characters below belong to the analytic receiver after the complete arithmetic has been obtained. In particular \(z=s-\rho\) is a coordinate at an actual analytic zero; it is not a displacement from \(\tau\).

The governing reconstruction and correction chain was checked through READ_FIRST_USER_CONSTRUCTION.md, USER_ARGUMENT_RECONSTRUCTION.md §§1–38, USER_ARGUMENT_CONNECTIONS.md, and the corresponding primary passages in USER_CONSTRUCTION_FULL_LOGBOOK.md, particularly U060, U123–U134, U138, and WU042–WU055. These preserve the retraction of addition at \(\tau\), the rejection of an assumed metric or formal vector at \(\tau\), whole arithmetic before named numerical inputs, separate branch counters, and the restriction to the original zeta function. The corpus is a source record with embedded speakers; an earlier quoted assistant construction is not made a user axiom here.

The mathematical prerequisites already proved and used are:

- OZR5.1–OZR5.3: actual nontrivial zero germs, their full multiplicities, and the quotient by the original \(\zeta\).
- OZR5.4–OZR5.9: the exact original-zeta reflection, including the local unit and all derivative terms.
- OZR6.1–OZR6.7: the recovered arithmetic character \(a^s\), its full nilpotent action, and interchange of \(F_a\) with \(aF_a^{-1}\).
- DC5–DC9 of [Deligne invariant cycles](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/DELIGNE_INVARIANT_CYCLE_QUOTIENT.md): the actual cohomological obstruction quotient, the separated source weights, and the proved lift in Deligne's stated proper smooth-model setting.

The existing source ledger ORIGINAL_ZETA_REFLECTION_SOURCE_READING_PRIVATE.json was consulted before deriving new formulas. Its human source is Alain Connes, [The Riemann Hypothesis: Past, Present and a Letter Through Time](https://arxiv.org/abs/2602.04022v1), original author source rhready.tex, formula smallxi and the functional-equation paragraph, local lines 526–545. Those lines and the surrounding lines 491–556 were read here. The full multiplier used is written in ZLB8. Deligne's human source is [La conjecture de Weil. II](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §3.6, with the transcription/source distinction and actual reading coverage retained in DC0. No new Deligne theorem is assumed for the analytic quotient.

The requested scope check has a concrete answer: OZR constructs the zero-jet quotient and its operator action, but it does not assert that a quotient eigenvector must lift to an exact eigenfunction in the holomorphic germ ring. The calculation below therefore decides precisely that added lifting question for this analytic extension. Its nonzero answer is not called an obstruction to the user's complete reconstruction, a failure of RH, or a classification of all possible cohomological receivers.

## ZLB1. The original germ and the exact differential

Put
\[
S=\{s\in\mathbb C:0<\Re s<1\},
\qquad
Z=\{\rho\in S:\zeta(\rho)=0\}.
\tag{ZLB1.1}
\]
Fix an actual \(\rho\in Z\), with multiplicity \(m=m_\rho\ge1\), and put \(z=s-\rho\). The original function has the convergent expansion
\[
\zeta(\rho+z)=z^m u_\rho(z),\qquad
u_\rho(z)=\sum_{j=0}^{\infty}
\frac{\zeta^{(m+j)}(\rho)}{(m+j)!}z^j,
\qquad
u_\rho(0)=\frac{\zeta^{(m)}(\rho)}{m!}\ne0.
\tag{ZLB1.2}
\]
Write
\[
O=\mathcal O_\rho,\qquad I=\zeta O,\qquad J=O/I,\qquad
\mathfrak m_\rho=zO.
\tag{ZLB1.3}
\]
The equality \(I=z^mO\) follows from invertibility of \(u_\rho\), but every calculation with the original generator retains \(u_\rho\).

After the whole arithmetic reconstruction, choose a recovered positive integer \(a>1\). Define
\[
\ell_a=\log a>0,\quad
E_a(s)=a^s,\quad
\lambda=a^\rho,\quad
F_a=M_{E_a},\quad
d_a=F_a-\lambda=M_{g_a},
\qquad g_a(s)=a^s-a^\rho.
\tag{ZLB1.4}
\]
Multiplication by \(E_a\) preserves \(I\) and acts on all three terms of
\[
0\longrightarrow I\xrightarrow{\jmath}O\xrightarrow{q}J\longrightarrow0.
\tag{ZLB1.5}
\]
Its exact local difference is
\[
g_a(\rho+z)=z\,b_a(z),\qquad
b_a(z)=\lambda\sum_{r=1}^{\infty}\frac{\ell_a^r}{r!}z^{r-1},
\qquad b_a(0)=\lambda\ell_a\ne0.
\tag{ZLB1.6}
\]
Thus \(b_a\) is a holomorphic unit germ. No Taylor term has been dropped from this identity.

## ZLB2. The complete connecting sequence

For \(M=I,O,J\), form the cochain complex
\[
\mathsf C_a(M)=[\,M\xrightarrow{d_a}M\,]
\tag{ZLB2.1}
\]
in degrees zero and one. The three complexes form a short exact sequence because (ZLB1.5) is exact in each degree and its maps commute with \(d_a\).

Here is the connecting sequence with its sign fixed:
\[
0\to\ker(d_a|I)\to\ker(d_a|O)\to\ker(d_a|J)
\xrightarrow{\delta_a}I/d_aI
\to O/d_aO\to J/d_aJ\to0.
\tag{ZLB2.2}
\]
For \(\bar f\in\ker(d_a|J)\), choose any holomorphic germ \(f\) lifting it. Since \(d_af\in I\), set
\[
\delta_a(\bar f)=[d_af]_{I/d_aI}.
\tag{ZLB2.3}
\]
Changing the lift by \(v\in I\) adds \(d_av\), so this is well-defined. This is the positive cochain-boundary convention.

For completeness, exactness can be proved at every term directly. A kernel element of \(O\) mapping to zero in \(J\) belongs to \(I\), and remains a kernel element there. A kernel element of \(J\) has zero boundary exactly when a lift \(f\) satisfies \(d_af=d_av\) for some \(v\in I\); then \(f-v\) is a kernel lift in \(O\). A class \([v]\in I/d_aI\) maps to zero in \(O/d_aO\) exactly when \(v=d_af\) for some \(f\in O\); the class of \(f\) in \(J\) then has boundary \([v]\). A class \([f]\in O/d_aO\) maps to zero in \(J/d_aJ\) exactly when \(q(f)=d_aq(h)\) for a germ \(h\), which says \(f-d_ah\in I\). The final arrow is onto because \(O\to J\) is onto. The other maps are the maps induced by inclusion and quotient. All cohomology outside degrees zero and one is zero.

The germ ring \(O\) is an integral domain: a nonzero germ has a finite order of vanishing and a nonzero unit factor, and orders add under multiplication. Therefore multiplication by the nonzero germ \(g_a\) is injective on \(O\), hence on \(I\). The complete groups are
\[
\begin{array}{c|c|c}
M&H^0\mathsf C_a(M)&H^1\mathsf C_a(M)\\ \hline
I&0&I/zI\\
O&0&O/zO\\
J&z^{m-1}O/z^mO&O/zO.
\end{array}
\tag{ZLB2.4}
\]
For the last row, \(g_af\in I\) means \(zf\in z^mO\), since \(b_a\) is a unit. Its cokernel is
\(O/(I+zO)=O/zO\). The identifications for \(I\) and \(O\) use \(g_aI=zI\) and \(g_aO=zO\); the original function \(g_a=zb_a\) remains available in the differential.

The coefficient maps
\[
I/zI\longrightarrow\mathbb C,\quad[\zeta h]\longmapsto h(\rho),
\qquad
O/zO\longrightarrow\mathbb C,\quad[f]\longmapsto f(\rho)
\tag{ZLB2.5}
\]
are isomorphisms. Uniqueness of \(h\) follows from the domain property. The first class \([\zeta]_{I/zI}\) is nonzero: \(\zeta\in zI\) would imply \(1=zh\) after cancellation in \(O\), which is impossible on evaluating at \(\rho\). It must not be confused with \([\zeta]_J=0\).

The map \(I/d_aI\to O/d_aO\) is zero, since every element of \(I\) vanishes at \(\rho\). The last map is the identity under evaluation. Consequently (ZLB2.2) is exactly
\[
0\longrightarrow \ker(d_a|J)
\xrightarrow[\sim]{\delta_a}I/zI
\xrightarrow{\,0\,}\mathbb C
\xrightarrow{\operatorname{id}}\mathbb C
\longrightarrow0.
\tag{ZLB2.6}
\]

## ZLB3. The original-generator boundary, with every factor retained

For the coordinate socle class, compute
\[
d_a(z^{m-1})=z^m b_a(z)
=\zeta(\rho+z)\frac{b_a(z)}{u_\rho(z)}.
\tag{ZLB3.1}
\]
Thus
\[
\delta_a[z^{m-1}]_J
=\frac{\lambda\log a}{u_\rho(0)}[\zeta]_{I/zI}.
\tag{ZLB3.2}
\]
The factor \(u_\rho(0)\) is the original \(m\)-th derivative divided by \(m!\), not a coefficient chosen to make \(\zeta\) monic.

There is a version using the original function itself. The holomorphic germ
\[
k_\rho(s)=\frac{\zeta(s)}{s-\rho}
=z^{m-1}u_\rho(z)
\tag{ZLB3.3}
\]
has nonzero class in \(J\), and spans \(\ker(d_a|J)\). Its boundary is
\[
d_ak_\rho=b_a(z)\zeta,\qquad
\boxed{\delta_a[k_\rho]_J
=\lambda\log a\,[\zeta]_{I/zI}\ne0.}
\tag{ZLB3.4}
\]
The higher terms in \(b_a\) have not been omitted by an approximation. Their difference from the constant representative is the exact boundary
\[
(b_a(z)-b_a(0))\zeta
=d_a\!\left(
\frac{b_a(z)-b_a(0)}{z\,b_a(z)}\,\zeta
\right).
\tag{ZLB3.5}
\]
The quotient inside parentheses is holomorphic, because its numerator vanishes at zero and its denominator is \(z\) times a unit.

There is an \(a\)-independent connecting line. Set
\[
\mathcal S_\rho=\operatorname{Ann}_{J}(\mathfrak m_\rho)
=z^{m-1}O/z^mO,\qquad
\mathcal N_\rho=I/\mathfrak m_\rho I.
\tag{ZLB3.6}
\]
Define
\[
\kappa_\rho:\mathcal S_\rho\longrightarrow\mathcal N_\rho,
\qquad [f]\longmapsto[zf].
\tag{ZLB3.7}
\]
For a socle element \(zf\in I\); a change of lift by \(I\) changes \(zf\) by \(zI\). The map sends \([k_\rho]\) to \([\zeta]\), so it is an isomorphism of one-dimensional spaces. In these fixed spaces the whole recovered arithmetic family has
\[
\delta_{a,\rho}=a^\rho\log a\,\kappa_\rho.
\tag{ZLB3.8}
\]
For any recovered \(a,b>1\), the character identity gives the exact relation
\[
\delta_{ab,\rho}=a^\rho\delta_{b,\rho}+b^\rho\delta_{a,\rho}.
\tag{ZLB3.9}
\]
Indeed both sides equal \((ab)^\rho(\log a+\log b)\kappa_\rho\). The operation here is addition of linear maps in the analytic receiver; it is not addition at the supporting point.

## ZLB4. The actual next-jet extension

The nonzero boundary is already visible in the finite-dimensional algebra
\[
\mathcal B_\rho
=O/(z\zeta O)
=O/\bigl((a^s-a^\rho)\zeta O\bigr).
\tag{ZLB4.1}
\]
Equality of the ideals follows from the unit \(b_a\). The full defining product is
\[
(a^s-a^\rho)\zeta
=z^{m+1}b_a(z)u_\rho(z).
\tag{ZLB4.2}
\]
Thus \(\dim_{\mathbb C}\mathcal B_\rho=m+1\), and the exact sequence is
\[
0\longrightarrow\mathcal N_\rho
\longrightarrow\mathcal B_\rho
\longrightarrow J_\rho
\longrightarrow0.
\tag{ZLB4.3}
\]
The first arrow is inclusion of \(I/zI\). Its kernel is zero by the definition of the quotient; its image is the kernel of the second arrow. This ideal is square-zero, because \(I^2\subset zI\) follows from \(2m\ge m+1\). Multiplication by a class \(f\in J\) on \(\mathcal N_\rho\) is its scalar value \(f(\rho)\), as \((f-f(\rho))\zeta\in zI\).

All recovered \(F_a\) preserve this same extension. The exact truncated functions acting on it and on \(J\) are
\[
F_a|_{\mathcal B_\rho}
=\lambda\sum_{r=0}^{m}\frac{(\log a)^r}{r!}M_z^r,
\qquad
F_a|_{J}
=\lambda\sum_{r=0}^{m-1}\frac{(\log a)^r}{r!}M_z^r.
\tag{ZLB4.4}
\]
Their omitted tails belong to the respective displayed defining ideals. On \(\mathcal B_\rho\), \(d_a=z b_a(z)\) has nilpotence order exactly \(m+1\), because \(z^m b_a(z)^m\notin z^{m+1}O\); on \(J\), its order is exactly \(m\). These are the actual original-zeta jet algebras, not independently selected matrices.

Applying the degree-zero lifting construction to (ZLB4.3) gives the same boundary (ZLB3.4): a lift of \([k_\rho]\) to \(\mathcal B_\rho\) has \(d_a\)-image \(\lambda\log a[\zeta]\), and \(d_a\mathcal N_\rho=0\). Thus the eigenvector has no eigenvector lift even to this finite extension.

There is also no \(F_a\)-equivariant linear section \(J\to O\). In fact every \(F_a\)-equivariant linear map \(T:J\to O\) is zero: \(d_a^m=0\) on \(J\), while multiplication by \(d_a^m\) is injective on \(O\), and
\[
d_a^mT=T d_a^m=0
\tag{ZLB4.5}
\]
forces \(T=0\). This statement is about the specified holomorphic source \(O\) and multiplication action; it is not a statement that no other cohomological source can lift the same quotient.

## ZLB5. All multiplicities through higher connecting complexes

For every positive integer \(r\), repeat the construction with differential \(d_a^r=z^r b_a(z)^r\). The same elementary proof of (ZLB2.2) gives its entire long exact sequence. Its groups are
\[
H^0\mathsf C_{a,r}(I)=H^0\mathsf C_{a,r}(O)=0,
\qquad
H^0\mathsf C_{a,r}(J)=z^{\max(m-r,0)}O/z^mO,
\tag{ZLB5.1}
\]
\[
H^1\mathsf C_{a,r}(I)=I/z^rI,\quad
H^1\mathsf C_{a,r}(O)=O/z^rO,\quad
H^1\mathsf C_{a,r}(J)=O/z^{\min(r,m)}O.
\tag{ZLB5.2}
\]
These equalities follow by comparing orders in \(z^r b_a^r f\in z^mO\). The connecting map is
\[
\delta_{a,r}[f]=[z^r b_a(z)^r f]_{I/z^rI}.
\tag{ZLB5.3}
\]
For \(1\le r\le m\), every source element can be written
\([\zeta z^{-r}h]\), with \(h\) determined modulo \(z^rO\), and
\[
\delta_{a,r}[\zeta z^{-r}h]
=[\zeta\,b_a(z)^r h]_{I/z^rI}.
\tag{ZLB5.4}
\]
Since \(b_a^r\) is a unit, this is an isomorphism onto \(I/z^rI\). All its \(r\) coefficient layers are retained. For \(r>m\), the entire \(J\) is the kernel, and
\[
\delta_{a,r}[f]
=\left[\zeta\,z^{r-m}
       \frac{b_a(z)^r}{u_\rho(z)}f\right]_{I/z^rI},
\qquad
\operatorname{im}\delta_{a,r}
=z^{r-m}I/z^rI.
\tag{ZLB5.5}
\]
The image has dimension \(m\). Inclusion \(I/z^rI\to O/z^rO\) has exactly this kernel, and the final quotient \(O/z^rO\to O/z^{\min(r,m)}O\) proves exactness at the remaining terms as well.

One can record the full equivariant extension class explicitly. Let
\(\mathscr R_a=\mathbb C[t,t^{-1}]\) act by \(t=F_a\), whose inverse is multiplication by the holomorphic unit \(a^{-s}\). On \(J\), the vectors \(1,d_a1,\ldots,d_a^{m-1}1\) are a basis: their orders are \(0,\ldots,m-1\), with nonzero leading coefficients \(b_a(0)^j\). Hence
\[
J\simeq\mathscr R_a/(t-\lambda)^m.
\tag{ZLB5.6}
\]
The free resolution with differential \((t-\lambda)^m\), after applying \(\operatorname{Hom}_{\mathscr R_a}(-,I)\), gives
\[
\operatorname{Ext}^1_{\mathscr R_a}(J,I)
\simeq I/d_a^mI.
\tag{ZLB5.7}
\]
This resolution is exact because \(\mathscr R_a\) is a domain and the quotient is (ZLB5.6). The extension (ZLB1.5) is represented, by lifting \(1\in J\) to \(1\in O\), by
\[
\left[(a^s-a^\rho)^m\right]_{I/d_a^mI}
=\left[\zeta\,\frac{b_a(z)^m}{u_\rho(z)}\right]_{I/z^mI}.
\tag{ZLB5.8}
\]
Changing the lift adds \(d_a^mI\), proving independence of that choice. This representative has order \(m\), whereas every element of \(d_a^mI\) has order at least \(2m\), so the class is nonzero. It retains the full extension, beyond the one-dimensional socle boundary.

## ZLB6. Actual finite-zero compatibility inside the original analytic quotient

Here we use a specified auxiliary global analytic space, not an identification with every growth-restricted programme source:
\[
\mathcal A=\mathcal O(S),\qquad
\mathcal Q=\mathcal A/\zeta\mathcal A.
\tag{ZLB6.1}
\]
There is a natural restriction map \(\mathcal Q\to J_\rho\) for each actual zero. Let \(D\subset Z\) be a finite set of distinct actual zeros. The following construction gives every finite collection of full zero jets an actual holomorphic representative.

For \(f_\rho\in J_\rho\), choose a germ representing it and let
\[
P_\rho(z)=
T_{m_\rho-1}\!\left(\frac{f_\rho(\rho+z)}{u_\rho(z)}\right)
=\sum_{j=0}^{m_\rho-1}c_{\rho,j}z^j.
\tag{ZLB6.2}
\]
Here \(T_{m-1}\) denotes the Taylor polynomial through degree \(m-1\); its meaning is the displayed finite coefficient extraction. Changing the germ by \(\zeta h\) changes \(f_\rho/u_\rho\) by \(z^mh\), so \(P_\rho\) is independent of the representative. Define
\[
L_\rho(f_\rho)(s)
=\frac{\zeta(s)}{(s-\rho)^{m_\rho}}P_\rho(s-\rho).
\tag{ZLB6.3}
\]
This is holomorphic on \(S\): the possible denominator singularity is removed by the actual multiplicity at \(\rho\). At \(\rho\), its class is \(f_\rho\). At every other actual zero \(\sigma\), the denominator is a unit and the expression vanishes to at least the full multiplicity \(m_\sigma\). Therefore
\[
\iota_D:\prod_{\rho\in D}J_\rho\longrightarrow\mathcal Q,\qquad
(f_\rho)_\rho\longmapsto
\left[\sum_{\rho\in D}L_\rho(f_\rho)\right]
\tag{ZLB6.4}
\]
is injective and is a section of the restriction onto the indicated factors.

To check multiplication, compare two products at every actual zero. At a zero in \(D\), their jets multiply as in \(J_\rho\); at a zero outside \(D\), both have zero full jet. The difference divided by \(\zeta\) is holomorphic near every zero by its full vanishing order, and away from the zeros ordinary division is holomorphic. These local quotients agree, producing an element of \(\mathcal A\). This proves that \(\iota_D\) is a multiplicative map. It takes the unit of the finite product to an idempotent \(e_D\) of \(\mathcal Q\), not necessarily to the global unit. Products of distinct single-zero images are zero.

The same argument shows equivariance for every recovered arithmetic multiplier:
\[
F_a\iota_D=\iota_D\!\left(\prod_{\rho\in D}F_{a,\rho}\right).
\tag{ZLB6.5}
\]
The product notation on the right is the componentwise operator on the finite product, not multiplication of branch measures. Under \(D\subset D'\), adding zero components commutes with \(\iota_D\); coordinate restriction also commutes with the local connecting sequences. Thus the finite-zero comparisons retain all multiplicities and are compatible under enlargement.

The chosen representative \(L_\rho\) itself is not claimed equivariant in \(\mathcal A\). Its exact defect is
\[
E_a(s)L_\rho(f_\rho)(s)
-L_\rho(F_{a,\rho}f_\rho)(s)
=\zeta(s)\,
\frac{E_a(s)P_\rho(z)-T_{m_\rho-1}(E_a(\rho+z)P_\rho(z))}
     {z^{m_\rho}},
\quad z=s-\rho.
\tag{ZLB6.6}
\]
The quotient is holomorphic because its numerator has zero Taylor coefficients through degree \(m_\rho-1\). Equation (ZLB6.6), rather than an unstated equality of representatives, proves (ZLB6.5). For \(f_\rho=[k_\rho]\), \(P_\rho=z^{m_\rho-1}\), so the defect is exactly \(\zeta(s)(a^s-a^\rho)/(s-\rho)\).

## ZLB7. The global boundary and finite resonances

The original sequence
\[
0\to\zeta\mathcal A\to\mathcal A\to\mathcal Q\to0
\tag{ZLB7.1}
\]
is preserved by multiplication by \(a^s\). For fixed actual \(\rho\) use \(g_a(s)=a^s-a^\rho\) as before. Its two-term complexes have the same connecting construction as ZLB2. The globally holomorphic function \(\zeta(s)/(s-\rho)\) gives an actual kernel class, because
\[
g_a(s)\frac{\zeta(s)}{s-\rho}
=\zeta(s)\frac{g_a(s)}{s-\rho}.
\tag{ZLB7.2}
\]
The quotient on the right is holomorphic on \(S\). Hence its global boundary is
\[
\left[\zeta(s)\frac{g_a(s)}{s-\rho}\right]
\in\zeta\mathcal A/g_a\zeta\mathcal A.
\tag{ZLB7.3}
\]
It is nonzero: vanishing would imply \(g_a(s)/(s-\rho)=g_a(s)h(s)\) with \(h\in\mathcal A\). On the nonempty open where \(g_a\ne0\), this forces \(h=1/(s-\rho)\); the identity theorem contradicts holomorphicity at \(\rho\). Restriction to the germ at \(\rho\) is precisely (ZLB3.4). No interpolation theorem for infinitely many prescribed jets is needed.

This also gives simultaneous finite compatibility without assuming distinct arithmetic eigenvalues. For a finite \(D\), let
\[
\Lambda_D=\{a^\rho:\rho\in D\},\qquad
P_D(t)=\prod_{\lambda\in\Lambda_D}(t-\lambda),\qquad
G_D(s)=P_D(a^s).
\tag{ZLB7.4}
\]
Repeated eigenvalues occur once in \(\Lambda_D\), while every zero and its own multiplicity remain in \(D\). At each \(\rho\in D\),
\[
G_D'(\rho)
=a^\rho\log a
\prod_{\substack{\lambda\in\Lambda_D\\\lambda\ne a^\rho}}
(a^\rho-\lambda)\ne0.
\tag{ZLB7.5}
\]
For every \(\rho\in D\), the actual function \(\zeta/(s-\rho)\) is killed in \(\mathcal Q\) by \(G_D\), and its connecting boundary is
\[
\left[\zeta(s)\frac{G_D(s)}{s-\rho}\right]
\in\zeta\mathcal A/G_D\zeta\mathcal A.
\tag{ZLB7.6}
\]
These finitely many boundary classes are linearly independent. Indeed, divide a proposed relation by the original generator \(\zeta\), restrict to a germ at a specified \(\sigma\in D\), and evaluate modulo \(G_D\): every term with \(\rho\ne\sigma\) vanishes, while the \(\sigma\)-term has value \(G_D'(\sigma)\ne0\). Thus its coefficient is zero, for every \(\sigma\). This proves that combining finitely many actual zero blocks does not cancel these particular local boundaries. It makes no claim about infinite topological direct products or a growth-restricted source not specified in (ZLB6.1).

## ZLB8. Full reflection multipliers and the exact chain maps

Let \(\rho'=1-\overline\rho\), \(w=t-\rho'\), and retain the original completion multiplier only as the source of the functional equation:
\[
C(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
A(t)=
\frac{\frac12(1-t)((1-t)-1)\pi^{-(1-t)/2}\Gamma((1-t)/2)}
     {\frac12t(t-1)\pi^{-t/2}\Gamma(t/2)}.
\tag{ZLB8.1}
\]
On \(S\) these are holomorphic units. The original function satisfies
\[
\zeta=A\,H\zeta,\qquad
(H_\rho f)(t)=\overline{f(1-\overline t)},\qquad
T_\rho f=A(t)H_\rho f.
\tag{ZLB8.2}
\]
Thus \(H_\rho\zeta=A^{-1}\zeta\), \(T_\rho\zeta=\zeta\), \(H_\rho z=-w\), and
\[
u_{\rho'}(w)=(-1)^m A(\rho'+w)\,
                 \overline{u_\rho(-\overline w)}.
\tag{ZLB8.3}
\]
This expression is holomorphic in \(w\). It retains the full local unit and full multiplier. The endpoint and trivial-zero exceptions lie outside this strip calculation; none of the unit assertions is extended to those points.

Write
\[
\lambda=a^\rho,\qquad
\mu=a^{\rho'}=\frac a{\overline\lambda},\qquad
V_a=M_{a^{1-t}},\qquad
b^{\mathrm{ref}}_{a,\rho}(t)=-\overline\lambda\,a^{-t}.
\tag{ZLB8.4}
\]
The reflection equations on the germ, ideal, and jet spaces are
\[
H_\rho(F_a-\lambda)
=(V_a-\overline\lambda)H_\rho,\qquad
V_a-\overline\lambda
=b^{\mathrm{ref}}_{a,\rho}(F_a-\mu).
\tag{ZLB8.5}
\]
The second identity follows by multiplication:
\(-\overline\lambda a^{-t}(a^t-\mu)
=-\overline\lambda+a\,a^{-t}\).
It is an identity of full germ functions, not only of their scalar values.

There are therefore two exact forms of the comparison. With target differential \(V_a-\overline\lambda\), the two degrees both use \(H_\rho\). With target differential \(F_a-\mu\), the chain isomorphism has degree maps
\[
\Phi_\rho^0=H_\rho,\qquad
\Phi_\rho^1=(b^{\mathrm{ref}}_{a,\rho})^{-1}H_\rho.
\tag{ZLB8.6}
\]
Indeed
\((F_a-\mu)\Phi_\rho^0=\Phi_\rho^1(F_a-\lambda)\).
All maps are conjugate-linear. The unit multiplier in degree one is essential. The weighted original-generator-fixing comparison similarly has
\[
\Psi_\rho^0=T_\rho,\qquad
\Psi_\rho^1=(b^{\mathrm{ref}}_{a,\rho})^{-1}T_\rho.
\tag{ZLB8.7}
\]
The multipliers commute with the multiplication differentials, proving this second chain identity. \(H_\rho\) is unital and multiplicative; \(T_\rho\) instead satisfies \(T(fg)=A^{-1}(Tf)(Tg)\). The degree-one maps in (ZLB8.6)–(ZLB8.7) are not asserted unital algebra maps.

These maps preserve the original ideal and the next-jet ideal: \(H(z\zeta)=-wA^{-1}\zeta\), and multiplication by a unit does not change the target ideal. They induce comparisons of (ZLB1.5), (ZLB4.3), and their connecting sequences. The boundary comparison is exactly
\[
\delta_{a,\rho'}\Phi_\rho^0
=\Phi_\rho^1\delta_{a,\rho},
\qquad
\delta_{a,\rho'}\Psi_\rho^0
=\Psi_\rho^1\delta_{a,\rho}.
\tag{ZLB8.8}
\]
It follows either from (ZLB2.3) and the chain identity or by the explicit calculation next.

On the actual original-function socle lift,
\[
H_\rho k_\rho=-A^{-1}k_{\rho'},\qquad
T_\rho k_\rho=-k_{\rho'}.
\tag{ZLB8.9}
\]
On the obstruction line, write \(A_0=A(\rho')\). Since
\((b^{\mathrm{ref}}_{a,\rho})^{-1}(\rho')=-\mu/\overline\lambda\), the induced maps are
\[
\Phi_\rho^1[\zeta]
=-\frac{\mu}{\overline\lambda A_0}[\zeta],
\qquad
\Psi_\rho^1[\zeta]
=-\frac{\mu}{\overline\lambda}[\zeta].
\tag{ZLB8.10}
\]
Consequently both routes on the \(H\)-comparison give
\(-\mu\log a\,A_0^{-1}[\zeta]\), and both routes on the \(T\)-comparison give
\[
-\mu\log a[\zeta].
\tag{ZLB8.11}
\]
Complex conjugation of the source scalar \(\lambda\log a\) is included in these equalities. Each chain isomorphism carries the nonzero boundary to a nonzero boundary. This transport makes no additional quotient of the fibres.

## ZLB9. Higher jets, reflection, and finite-set comparisons

The complete derivative map is also explicit. For a germ
\(f(\rho+z)=\sum_{j\ge0}c_jz^j\),
\[
T_\rho f(\rho'+w)
=A(\rho'+w)\sum_{j\ge0}(-1)^j\overline{c_j}w^j.
\tag{ZLB9.1}
\]
Its coefficient of \(w^k\) is
\[
\sum_{j=0}^{k}
\frac{A^{(k-j)}(\rho')}{(k-j)!}
(-1)^j\overline{c_j}.
\tag{ZLB9.2}
\]
For \(J\) use all \(0\le k<m\); for \(\mathcal B_\rho\) use all \(0\le k\le m\). The original full expression (ZLB8.1) defines every derivative of \(A\); OZR4.3–OZR4.6 give them with the Gamma derivatives, powers of \(\pi\), and endpoint contributions retained. Formula (ZLB9.2) does not replace them by a scalar on a higher-jet space. A scalar evaluation is used only on \(\mathcal N_\rho\), whose ideal quotient makes all higher coefficient terms exactly zero.

For the complexes with differential \(d_a^r\), the degree maps become
\[
(H_\rho,(b^{\mathrm{ref}}_{a,\rho})^{-r}H_\rho),
\qquad
(T_\rho,(b^{\mathrm{ref}}_{a,\rho})^{-r}T_\rho).
\tag{ZLB9.3}
\]
Equation (ZLB8.5), raised to the \(r\)-th power, proves the chain identities. In particular the full higher connecting maps (ZLB5.3) commute with these maps, including the derivatives of every multiplier occurring modulo \(z^rI\).

For a finite actual zero set \(D\), reflection gives \(rD\), with the same multiplicity at paired points. The local maps assemble componentwise. The global maps \(H,T\) on \(\mathcal Q\) commute with the finite-zero inclusions (ZLB6.4) and these local comparisons. To prove this without assuming equality of chosen representatives, compare their full jets at every actual zero. The two classes have the same jets on \(rD\) by (ZLB9.1)–(ZLB9.2), and zero jets elsewhere; their difference is divisible by \(\zeta\) globally, exactly as in the proof of (ZLB6.4). This proves the comparison on the actual quotient.

A comparison of complete branches that identifies their recovered arithmetic and the original function sends \(a\), \(s\), \(\zeta\), and each specified zero germ to their stated counterparts. Under that already specified identification all maps in ZLB1–ZLB7 commute by their formulas. No branch measures are added and no second copy of \(\zeta\) is multiplied into the function. Reflection is the more specific comparison (ZLB8.5), which interchanges \(F_a\) and \(aF_a^{-1}\); it is not misreported as fixing each individually marked \(F_a\).

## ZLB10. What the calculation says about the Deligne comparison

The operator \(F_a\) acts by the same eigenvalue \(\lambda=a^\rho\) on
\(\mathcal S_\rho\), \(\mathcal N_\rho\), \(O/d_aO\), and \(J/d_aJ\). On the socle this is its definition as \(\ker(F_a-\lambda)\); on the quotient groups it follows because \(F_a-\lambda\) acts as zero. In particular the nonzero boundary (ZLB3.4) intertwines equal eigenvalues.

The exact analytic modulus exponent is
\[
2\log_a|a^\rho|=2\Re\rho.
\tag{ZLB10.1}
\]
This is a calculated exponent of the analytic arithmetic character, not a claim that it is already a Deligne weight of an arithmetic sheaf. Every eigenvalue on \(J\) and on the next-jet extension \(\mathcal B_\rho\) equals \(\lambda\), so any cutoff based on (ZLB10.1) either retains both the kernel \(\mathcal N_\rho\) and quotient \(J\), or retains neither. Such a cutoff cannot retain the quotient while excluding this kernel.

This is the exact comparison with DC8: Deligne obtains a kernel of weights at least \(i+1\) and a quotient of weights at most \(i\); that separation makes the low-weight part map isomorphically to the quotient. Here the specified original-zeta germ extension has the same character on both sides, and its connecting boundary is a nonzero isomorphism of lines. No Tate factor has been obtained from this sequence: multiplication by the original \(\zeta\) is an \(F_a\)-equivariant isomorphism \(O\to I\), since both multiplications commute. Inserting a character factor on \(I\) would change that stipulated equivariant extension, not compute its existing action.

For an actual zero on the critical line, (ZLB10.1) equals one on both lines and (ZLB3.4) is still nonzero. Thus this boundary is an eigenvector-lift obstruction for the displayed analytic source, not a test whose vanishing is equivalent to RH. Nothing in this calculation asserts the existence of an off-critical zero.

The definition audit in ZLB0 matters here. A proof that the user's construction requires this particular lift has not been supplied by OZR5–6, DC5–9, or the maps constructed in this note. The actual conclusions are therefore confined to the explicit extension and its exact reflection and finite-zero comparisons. The new object determined by its failure to split is the concrete next-jet algebra (ZLB4.1), with the higher extension classes (ZLB5.8); it is not an arbitrary unrelated counterexample to the programme.

## ZLB11. The resulting connecting object

The calculated data can be displayed as a commuting connecting diagram, where the lower row uses the reflected differential and every vertical arrow is the exact map of ZLB8:
\[
\begin{array}{ccccc}
\mathcal S_\rho&\xrightarrow{\ \delta_{a,\rho}\ }&\mathcal N_\rho\\
\Psi_\rho^0\downarrow&&\downarrow\Psi_\rho^1\\
\mathcal S_{\rho'}&\xrightarrow{\ \delta_{a,\rho'}\ }&\mathcal N_{\rho'}.
\end{array}
\tag{ZLB11.1}
\]
The top map sends the original-function class \([\zeta/(s-\rho)]\) to
\(a^\rho\log a[\zeta]\). The target is the fibre at \(\rho\) of the conormal module of the original zero ideal:
\[
(I/I^2)\otimes_J(O/\mathfrak m_\rho)
\cong I/(I^2+\mathfrak m_\rho I)=I/\mathfrak m_\rho I,
\]
because \(I\subseteq\mathfrak m_\rho\), so \(I^2\subseteq\mathfrak m_\rho I\). Thus \([\zeta]\) here is a nonzero generator of that fibre, not the zero class of \(\zeta\) in \(J\). It sits as the retained square-zero kernel in the actual extension
\[
0\to I/\mathfrak m_\rho I
\to O/(\mathfrak m_\rho I)
\to O/I\to0.
\tag{ZLB11.2}
\]
The higher complexes retain all \(m_\rho\) original jet layers and their connecting images. The finite-zero maps use holomorphic representatives of the same original function, and the full reflection includes every factor of \(C\), \(A\), and \(b^{\mathrm{ref}}_{a,\rho}\). These are the complete maps proved here; none assigns an analytic vector or numerical distance to \(\tau\langle Z_1;\text{no }Z_2\rangle\).
