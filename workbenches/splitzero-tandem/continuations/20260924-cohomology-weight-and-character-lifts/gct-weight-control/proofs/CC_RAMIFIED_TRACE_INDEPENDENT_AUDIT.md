# Independent audit of the ramified trace and residue action

Bounded mathematical review, 24 September 2026. Review locators GTA0–GTA8.

## GTA0. Reviewed object and outcome

Read the complete [CC_RAMIFIED_TRACE_AND_RESIDUE_ACTION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_RAMIFIED_TRACE_AND_RESIDUE_ACTION.md), GTR0–GTR9, at SHA-256
6c625c9619f0fa96ee8798503c18cee833f6bb1b27f75233fea821d7ce31c056.
Checked its support conventions against CSP6–CSP8 and its winding comparison against CDW9–CDW10. CDI's coefficient duals and the complete SDT proof were already read and proved in this task.

The weighted sheaf trace, its finite-proper direct-image argument, the transfer degrees and support signs, the original-zeta residue factors and all multiplicity entries are correct. Two carrier clarifications are recommended: retain \(\kappa'\) in the full jet formula GTR5.4, and retain \(q':Q'\to A'\) when comparing the residue action with the normal coefficient dual in GTR6. Their exact formulas are GTA4 and GTA5 below. No change of a numerical factor or orientation sign is required.

Both clarifications were subsequently incorporated by the author of GTR. GTA8 records the reread of those revisions and the complete new GTR10 at the final hash. They are resolved changes, not outstanding corrections.

No shared GTR file was edited. This audit concerns the actual reconstructed coefficient spaces and receiving sphere. It assigns no operation, coordinate or metric to \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\), and makes no new claim about the missing Deligne weight comparison.

## GTA1. Ramified stalks and the endpoint kernels

Let \(b_n(z)=z^n\), with the two poles fixed. A sufficiently small disk at either pole has one connected preimage disk. In the specified sheaf a section on that disk is \(v_p\in V_p\), with generic restriction \(r_pv_p\in A\). An interior subdisk of the target disk has \(n\) distinct inverse-image disks. The restriction of the same source section to each is \(r_pv_p\). Thus the generic finite-sheet trace is
\[
(r_pv_p,\ldots,r_pv_p)\longmapsto n\,r_pv_p.
\tag{GTA1.1}
\]
The proposed pole map \(v_p\mapsto nv_p\) has exactly that restriction. Hence the interior trace and pole trace glue.

The restriction identity by itself would allow an additional map with image in \(E_p=\ker r_p\); it would not determine the endpoint trace. GTR2 explicitly fixes the entire pole stalk by its local multiplicity \(n\), so it selects
\[
\operatorname{Tr}_{n,p}|_{E_p}=n\,1_{E_p}
\tag{GTA1.2}
\]
on both endpoint coordinates at each pole. This is a specified weighted trace, not an inference that zero generic restriction erases those coordinates.

The pullback unit is diagonal on the \(n\) interior sheets and is the identity on a pole stalk. Hence its composite with the trace is \(n\) on the interior coefficient and on every pole coefficient:
\[
\operatorname{Tr}_n u_n=n\,1_{\mathscr F}.
\tag{GTA1.3}
\]
All local formulas are finite continuous linear maps. They are natural for coefficient morphisms because such morphisms commute with finite sums and scalar multiplication.

The local multiplicities are indeed \(n\) at zero and infinity and \(1\) elsewhere. At zero the local quotient by \(z^n\) has basis \(1,z,\ldots,z^{n-1}\). In the local coordinate \(w=1/z\), the infinity map is also \(w\mapsto w^n\). At a nonzero finite point, \(nz^{n-1}\ne0\). Grouping roots for the composition multiplies these local multiplicities, giving the stated composition of trace maps.

## GTA2. Exact direct image for this finite proper map

Here is the full stalk argument for any sheaf \(\mathscr G\) of complex vector spaces on the source sphere. Let \(b_n^{-1}(y)=\{x_1,\ldots,x_r\}\). Choose pairwise disjoint neighborhoods \(N_i\) of these finitely many points. Properness gives a neighborhood \(U\) of \(y\) with
\[
b_n^{-1}(U)\subset\bigcup_iN_i.
\tag{GTA2.1}
\]
For this particular map one can use compactness of the sphere: the image of the closed complement of \(\bigcup_iN_i\) is compact and does not contain \(y\); its complement supplies \(U\). This also gives the general finite-proper argument used in GTR.

There is a natural map
\[
(b_{n*}\mathscr G)_y\longrightarrow
\bigoplus_{i=1}^r\mathscr G_{x_i}
\tag{GTA2.2}
\]
by restricting germs. It is surjective: represent a finite family of germs by sections on disjoint \(N_i\), shrink \(U\) as in (GTA2.1), and glue their restrictions on the disjoint sets \(b_n^{-1}(U)\cap N_i\). It is injective: if all germs of a represented section vanish at the \(x_i\), shrink the \(N_i\) so that its restrictions are zero, and then apply (GTA2.1) again.

Thus (GTA2.2) is an isomorphism. Finite direct sums of vector spaces are exact, and sheaf exactness is detected stalkwise, so \(b_{n*}\) is exact. Therefore \(Rb_{n*}=b_{n*}\). For derived global sections, inverse image on vector-space sheaves is exact and is left adjoint to direct image; hence \(b_{n*}\) preserves injectives. The equality \(\Gamma(Y,b_{n*}\mathscr G)=\Gamma(Y,\mathscr G)\), applied to an injective resolution, gives the claimed derived global-section identification.

This is an argument in the stated category of vector-space sheaves. It uses no finite-dimensionality of \(A\), \(V_p\) or the stalks, and does not assert exactness in an unstated category of topological vector spaces.

## GTA3. Global, local-support and annular transfer degrees

The degree-zero pullback on each chart coefficient is the identity. On the annular degree-zero coefficient it is also the identity. On its positive angular generator,
\[
b_n^*\frac{d\arg z}{2\pi}
=n\frac{d\arg z}{2\pi}.
\tag{GTA3.1}
\]
The same positive factor occurs at infinity in the positive \(w=1/z\) local circle. The positive sphere integral is
\[
\int_Yb_n^*\omega_Y
=2n^2\int_0^\infty
\frac{r^{2n-1}}{(1+r^{2n})^2}\,dr
=n\int_0^\infty\frac{dt}{(1+t)^2}=n,
\quad t=r^{2n}.
\tag{GTA3.2}
\]
Thus on \(Z,Q,A\) in global degrees \(0,1,2\), pullback is \((1,1,n)\). The source of \(Q\) in degree one is the quotient of overlap constants, not the annular angular class. This distinction accounts for its factor \(1\).

Each of these maps is invertible on its displayed complex vector space. Equation (GTA1.3) therefore determines transfer as
\[
(\operatorname{Tr}_n^0,\operatorname{Tr}_n^1,
\operatorname{Tr}_n^2)=(n,n,1).
\tag{GTA3.3}
\]
The same calculation on the local support cone \([V_p\to A\to0\,A]\) gives \((1,1,n)\) for pullback and \((n,n,1)\) for transfer on \(E_p,Q,A\). On the punctured sphere the factors are \((1,n)\) and \((n,1)\).

The support signs survive these factors. The positive local angular boundary is minus the positive local fundamental class. At infinity \(d\arg w=-d\arg z\), so the global positive \(z\)-loop has boundary
\[
a\longmapsto(-a,a).
\tag{GTA3.4}
\]
Both positive local fundamental classes map to the positive sphere class, so the next map is \((c_+,c_-)\mapsto c_++c_-\). Transfer has factor \(1\) on all three terms in this angular-to-degree-two part of the localization row. The earlier maps
\[
a\longmapsto([a],[a]),\qquad
(q_+,q_-)\longmapsto q_+-q_-
\tag{GTA3.5}
\]
have factor \(n\) on their source and target. The original endpoint map also has factor \(n\). Hence the complete localization row commutes with transfer, including its distinct diagonal, difference, negative-positive boundary and sum.

The matrix \((n,n,1)\) is a continuous cochain map on the stated model, since \(r_+-r_-\) commutes with multiplication by \(n\). It realizes the just-computed cohomological values. GTR correctly says this does not prove uniqueness of a cochain representative from its cohomology.

In particular the displayed identities involving the chosen cochain representatives hold on that model. This calculation does not by itself claim that two arbitrary continuous cochain maps with the same cohomological values admit a continuous chain homotopy. GTR's explicit qualification avoids making that stronger assertion.

## GTA4. Inverse coefficients, transpose factors and every jet

The inverse coefficient actions in GTR4.1 are the original actions at \(n^{-1}\). On the complete three-term model,
\[
\mathsf B_n=(\rho(n),T_n,nT_n),\qquad
\mathsf U_n=(n\rho(n^{-1}),nT_{n^{-1}},T_{n^{-1}}).
\tag{GTA4.1}
\]
The first differential commutes with the source/overlap entries because \(r_p\rho_p(a)=T_ar_p\). The other differential is zero. Multiplication in each degree gives \(n\), so the two compositions are both \(n\,1\).

Ordinary transpose reverses composition but adds no new sign to these degree-zero chain maps. The three rows in GTR4.5 therefore follow exactly, and
\[
\mathsf U_n'=n(\mathsf B_n^{-1})',\qquad
\langle\mathsf U_n'\lambda,\mathsf B_nx\rangle
=n\langle\lambda,x\rangle.
\tag{GTA4.2}
\]
The four original endpoint characters of \(n\rho(n^{-1})'\) are \(n,1,1,n\), because the plus-chart inverse characters are \(1,n^{-1}\) and the minus-chart inverse characters are \(n^{-1},1\).

The residue covariance follows before evaluating a single residue:
\[
\frac{F(s)(T_nG)(1-s)}{\zeta(s)}
=n\,\frac{n^{-s}F(s)G(1-s)}{\zeta(s)}.
\tag{GTA4.3}
\]
Thus \(\iota T_n=n(T_{n^{-1}}^{\mathcal Q})'\iota\); conjugating through \(\kappa\) gives GTR5.3 exactly.

The scalar and every nilpotent coefficient in GTR5.4 are correct. The complete formula with all carriers shown is
\[
\boxed{
\mathsf U_n'\kappa'\delta_{\rho,j}
=n^{1-\rho}\sum_{h=0}^j
\frac{(-\log n)^{j-h}}{(j-h)!}
\kappa'\delta_{\rho,h}.}
\tag{GTA4.4}
\]
Here \(\delta_{\rho,j}([F])=F^{(j)}(\rho)/j!\) lies in \(\mathcal Q'\), whereas \(\mathsf U_n'\) on degree-minus-one cohomology acts on \(Q'\). To prove (GTA4.4), take the coefficient of \(t^j\) in
\[
n^{1-\rho}e^{-t\log n}F(\rho+t).
\tag{GTA4.5}
\]
This is exactly the finite sum displayed. An equivalent editorial repair is to declare explicitly that \(\mathsf U_n'\) in GTR5.4 has been transported to \(\mathcal Q'\) by \((\kappa')^{-1}\mathsf U_n'\kappa'\). Without one of these declarations the formula suppresses a nontrivial comparison map, though its coefficients are unchanged.

## GTA5. The exact carrier for the normal-dual comparison

The normal coefficient in GTR6 is the full \(A\), while the residue dual lives on \(Q=A/J\). Retain the actual quotient and its transpose,
\[
q:A\to Q,\qquad
q':Q'_\beta\xrightarrow{\ \sim\ }J^\perp\subset A'_\beta.
\tag{GTA5.1}
\]
SDT5.6 proves that the latter is a closed strong topological embedding. The original coefficient actions preserve \(J\), so
\[
qT_a^A=T_a^Qq,\qquad
(T_a^A)'q'=q'(T_a^Q)'.
\tag{GTA5.2}
\]
Define the three operators on their actual domains:
\[
S_{\mathrm{res},n}=n(T_{n^{-1}}^Q)'\quad\text{on }Q',
\]
\[
N_{\mathrm{contra},n}=n^{-1}(T_{n^{-1}}^A)'
\quad\text{on }A',\qquad
N_{\mathrm{tr},n}=(T_{n^{-1}}^A)'
\quad\text{on }A'.
\tag{GTA5.3}
\]
Equation (GTA5.2) then proves the fully typed comparison
\[
\boxed{
q'S_{\mathrm{res},n}
=n^2N_{\mathrm{contra},n}q'
=nN_{\mathrm{tr},n}q'.}
\tag{GTA5.4}
\]
This is the exact \(n^2,n\) comparison intended in GTR6. It is an intertwining statement through the actual annihilator inclusion; it is not a literal equality between operators on different vector spaces.

The intermediate receiver matters. The strongly dense finite-jet image in \(Q'\) maps to a strongly dense subspace of \(J^\perp\), not of the whole \(A'\). The annihilator is proper: \(J\ne0\), since the retained source has Mellin image \(F_0\) with \(F_0(0)=1/8\); Hahn–Banach supplies a continuous functional on \(A\) nonzero on a nonzero element of \(J\). Thus not every normal-dual coefficient is a zeta-quotient functional. Equation (GTA5.4) supplies the strongest exact inclusion needed here without replacing the full normal coefficient by its quotient.

## GTA6. Winding, connecting maps and original arithmetic

CDW9.5 maps \(a[\vartheta]\) to \(-a\) in positive sphere integration. Substituting it into CDW10.5 gives precisely
\[
a[\vartheta]\longmapsto
-[(1-E_+(s))(\Theta a)(s-1)]_{\mathcal I\cap\mathcal I_+}.
\tag{GTA6.1}
\]
Its kernel is \(J[\vartheta]\) by the proved exact quotient map. Multiplication by this common minus sign commutes with pullback and transfer. GTR6.1 therefore retains the correct orientation without changing their tables.

Naturality of trace for \(J\to A\to Q\) gives the two connecting-map identities in GTR7.3. The second also follows algebraically from the first:
\[
\delta T_n^Q=nT_n^J\delta
\ \Longrightarrow\
\delta(T_n^Q)^{-1}
=n^{-1}(T_n^J)^{-1}\delta
\ \Longrightarrow\
\delta(nT_{n^{-1}}^Q)=T_{n^{-1}}^J\delta.
\tag{GTA6.2}
\]
Thus it imposes no additional independent constraint. This agrees with GTR's stated scope.

The retained exceptional factors also check directly. At \(s=-2r\), the Laurent coefficient of \(\Gamma(s/2)\) is \(2(-1)^r/r!\), and \(\zeta(s)=(s+2r)\zeta'(-2r)+O((s+2r)^2)\). Multiplying by the retained \(s(s-1)\pi^{-s/2}/8\) yields
\[
F_0(-2r)=
\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r),
\tag{GTA6.3}
\]
as in GTR8.3. Its second expression follows from the unchanged functional equation. The raw summation factor \(2\), the comparison \(\Theta=\mathcal M_0/2\), both endpoint values \(1/8\), and the full \(\chi(s)\) are retained. In the residue reversal \(s=1-z\), the differential is \(ds=-dz\), giving precisely the local reflection sign already present in RD.

## GTA7. Exact strong-topology extension

For every continuous linear operator \(U\) on \(Q\), its transpose is strongly continuous, because for every bounded \(B\subset Q\),
\[
p_B(U'\lambda)=p_{U(B)}(\lambda),
\tag{GTA7.1}
\]
and \(U(B)\) is bounded. Apply this to the actual degree-one \(\mathsf U_n=nT_{n^{-1}}\). The isomorphism \(\kappa\) also transposes to a strong topological isomorphism, since both it and its inverse preserve bounded sets.

SDT7 proves
\[
\overline{\mathscr D_{\mathrm{fin}}}^{\,\beta(\mathcal Q',\mathcal Q)}
=\mathcal Q'_\beta,
\tag{GTA7.2}
\]
and proves that this strong dual is complete. Equip \(\mathcal Q_{\mathrm{fin}}\) with exactly the residue seminorms
\[
p_B^{\mathrm{res}}(G)=
\sup_{F\in B}\left|
\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(s)G(1-s)}{\zeta(s)}\,ds\right|,
\qquad B\subset\mathcal Q\text{ bounded}.
\tag{GTA7.3}
\]
Then GTR5.3 extends uniquely by continuity to its Hausdorff completion:
\[
\widehat{\mathcal Q_{\mathrm{fin}}^{\,\mathrm{res}}}
\xrightarrow[\ \kappa'\widehat\iota\ ]{\ \sim\ }Q'_\beta,
\qquad
(\kappa'\widehat\iota)\,\widehat T_n
=\mathsf U_n'(\kappa'\widehat\iota).
\tag{GTA7.4}
\]
The completion is for the explicitly constructed residue topology, not for an assumed topology inherited from \(\mathcal Q\). It concerns a complete functional receiver, not an asserted density of finite-support classes in the primal quotient. Composing with \(q'\) yields the completed invariant receiver \(J^\perp\subset A'_\beta\), with exactly the factors in (GTA5.4).

An independent mathematical reviewer separately checked GTR2–GTR3, the proper finite-fibre stalk argument, both pole endpoint kernels, and CSP6–CSP7's support signs; it found no error. This audit and that check do not assert positivity, a Verdier/continuous-dual identification, or a Deligne weight bound.

## GTA8. Accepted revised GTR0–GTR10 and the full completion action

Reread the revised GTR5.4, the complete carrier comparison GTR6.0, and all of GTR10. The final reviewed GTR file has SHA-256
8ede942ee574e1f96fdc2b6247c8786491abe3fc6401c24f157625f8f2fb9811.
The revised GTR5.4 retains every \(\kappa'\) as in (GTA4.4), and GTR6.0 supplies exactly (GTA5.4), including the strong annihilator inclusion. Both domain issues are resolved.

The new GTR10 satisfies the exact seminorm identities
\[
p_B^{\mathrm{res}}(T_aG)
=a\,p_{T_{a^{-1}}B}^{\mathrm{res}}(G),\qquad
p_B^{\mathrm{res}}(\mathsf V_aG)
=p_{T_aB}^{\mathrm{res}}(G).
\tag{GTA8.1}
\]
The first follows from the multiplier \(a^{1-s}=a\,a^{-s}\) in the reflected second argument; the second follows from
\(a\,a^{-(1-s)}=a^s\). Since \(a>0\), its absolute value is precisely the prefactor \(a\) in the first seminorm identity. The images of bounded sets are bounded by continuity of the original \(T_a\).

These identities prove continuity of the two actions and their inverses in the specified residue topology. Their extensions to the Hausdorff completion are continuous automorphisms. On the dense finite-support domain,
\[
T_aT_b=T_{ab},\qquad
\mathsf V_a\mathsf V_b=\mathsf V_{ab},\qquad
T_a\mathsf V_a=a\,1.
\tag{GTA8.2}
\]
Continuity and the Hausdorff target extend all three identities to the completion. The same equalizer argument extends the intertwining maps to the whole completed dual receiver, giving GTR10.6 with \(\mathsf U_n'\) and \(\mathsf B_n'\) in their correct degree-minus-one positions.

The completed pairing is evaluation. Its expression as the limit of finite original-zeta residue pairings is independent of the chosen representing net because the convergence is uniform on every bounded subset of \(\mathcal Q\). It is nondegenerate in the completed variable by the proved topological isomorphism to \(\mathcal Q'_\beta\), and in the primal variable because all full zero jets belong to this dual and separate classes. This argument does not imply joint continuity or positivity, neither of which GTR10 asserts.

The resulting identities are
\[
\widehat{\mathcal R}(T_nF,\widehat T_nh)
=n\,\widehat{\mathcal R}(F,h),\qquad
\widehat{\mathcal R}(F,\widehat{\mathsf V}_nh)
=\widehat{\mathcal R}(T_nF,h).
\tag{GTA8.3}
\]
They follow directly from \(T_n'\mathsf U_n'=n\,1\) and the two completed intertwining identities. Thus no new residue-convergence hypothesis is needed.

Finally, the map \(h\mapsto(h,-h)\) in GTR10.10 is the continuous anti-diagonal on the two degree-minus-one costalk receivers. The map into the full overlap dual is
\[
h\longmapsto q'\mathfrak I(h),\qquad
(q'\mathfrak I(h))(a)
=\widehat{\mathcal R}([\Theta a],h),
\tag{GTA8.4}
\]
which keeps the raw-to-Mellin factor \(1/2\) inside \(\Theta\). Its range is exactly \(J^\perp\), with the strong topology proved in SDT5.6. This agrees with the carrier calculation GTA5 and preserves both the four endpoint lines and the additional normal-dual directions outside that annihilator.

No additional correction is requested for the revised GTR0–GTR10 at the final hash.
