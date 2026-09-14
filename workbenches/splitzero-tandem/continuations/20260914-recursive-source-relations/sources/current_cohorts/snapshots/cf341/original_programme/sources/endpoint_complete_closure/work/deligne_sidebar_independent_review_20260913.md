# Independent full proof review of the Deligne/Split-Zero sidebar

Date: 2026-09-13. Reviewer: `deligne_sidebar_review`. This is a mathematical source review; it records no new Lean run, finite-checker execution, PDF rendering, or publication.

## Scope and inspected sources

I read the complete `work/deligne_split_sidebar_20260913.tex`, initially DS1–65 and then the added DS66–69, and the complete `work/deligne_translation_bridge_20260913.tex`, DT1–13. I then read every amended passage and the additional standalone period-invertibility proof. **The final accepted sidebar source has SHA256 `8601c882177ecbf64a374bded1641573f7cbba4d950dd8786e23d15b64307384`. The final accepted translation source has SHA256 `39163624c54704c203a69481ff4d7df4262afa108ac1e0989171d5ba8d700c42`.** Both hashes were independently obtained from the current files after those final reads. The earlier intermediate source identifiers were `dd4c45e552902e084d5413ea98ec8bdfefd0ee65336be718a5e990015214e323` for DS1–69 and `c4fbd1d9155b6dcd7d025ed832e114df58411b923b7598acf7da749d87dfe7fb` for DT1–13; these are retained only as review history.

The complete 1,510-line user paste at attachment `1f285372-dda6-457d-a82e-0bf484ccab65/pasted-text.txt` was read in disjoint line ranges. Its SHA256 is `83a5e8350531b58275c896c23534310a96d6e8d98c7e4c3f9439be48eebbbdc1`. It contains both the exponential comparison and logarithmic constituent-control contributions. Source instructions were treated as source material, not as independent authorization.

The extracted S20 current French records at `output/Deligne_Weil_II_S20_LaTeX/source_package/edition/source_language.ndjson`, SHA256 `a5edb9ba90a28beffa850e7112da3649a2f1528b0ea0096ed0d79bfb75e2d833`, were read at printed pages 201–207 in full, then at printed pages 150–152, 178, 215–216 for the precise conventions and exponential application. This review does not independently re-audit the native-page transcription or the entire Weil II proof. The source theorem is invoked at the verified displayed statement and hypotheses.

Relevant source locators are:

- Printed 150–152, §§1.1.7–1.1.13: geometric Frobenius is the inverse of the field substitution; the actions used in weights follow that convention.
- Printed 178, Corollary 1.8.12: the purity propagation statement requires a lisse mixed sheaf on a connected base; equal fibre dimensions alone do not supply it.
- Printed 203, Lemma 3.2.10 and §3.2.13: the strict upper bound is weight less than 2, and the tensor argument applies its bound to the square of the original eigenvalue.
- Printed 206, Corollaries 3.3.4–3.3.6: compact-support upper bound, ordinary lower bound with the displayed Poincaré-dual degree/twist, and purity of their common image.
- Printed 215–216, §§3.7.2–3.7.4: the degree-prime-to-characteristic exponential theorem, the lissity argument using local constancy at infinity, and mixed-family propagation from the monomial member.

## Findings and completed source corrections

The principal calculations below verify. The following corrections were sent to the author/root as soon as found. All six items are now incorporated and independently re-read in the final sources pinned above.

1. **Split kernel inclusion after DS10.** The represented preimage of supported zero does not contain external absence. If `f:V→W`, the exact statements are

   \[
   \mathsf S(f)^{-1}(\tau)=\{\tau\},\qquad
   \mathsf S(f)^{-1}(e_W)=(\ker f)^\bullet,
   \]
   \[
   \mathsf S(\ker f)=\{\tau\}\sqcup(\ker f)^\bullet
     =p_V^{-1}(\ker f).
   \]

   The two disjoint fibres both include into the last displayed split object. This supplies the exact bridge without asserting a false inclusion between the disjoint fibres. The final source contains these fibres, their common split carrier, and the amplitude preimage explicitly.

2. **Frobenius convention in DS44.** The word “arithmetic” there was replaced by geometric Frobenius to match the weight and Tate-twist conventions in DS7–8 and the Artin–Schreier scalar convention in DT12–13. The current French §1.1.7 settles the convention explicitly. The final source uses geometric Frobenius.

3. **The logarithmic/exponential join after DS68.** The middle logarithmic complex has `H0=F` and `H2=(E/F)⊗T`; its two induced actions do not reconstruct the original extension by themselves. The common full coefficient object is instead explicitly supplied by the outer comparison complexes:

   \[
   \mathbb H^0(\mathscr K_{\rm ord}(E))=E,
   \qquad\mathbb H^2(\mathscr K_c(E))=E\otimes\mathbb T,
   \]
   with `0→F→E` in degree zero and `E⊗T→(E/F)⊗T→0` in degree two. The special exponential chain map
   \[
   [\mathbb C[S]\xrightarrow{\chi}\mathbb C[S]dS]
      \longrightarrow E[-1],\qquad P\,dS\longmapsto[P]_\chi
   \]
   is zero in degree zero; its kernel differential is the isomorphism `P↦χP dS` onto `χC[S]dS`, hence the map is a quasi-isomorphism. This joins the two coefficient presentations while retaining `F→E→E/F`. It is not an asserted isomorphism of the differently graded middle complexes.

4. **Dual action and source category.** DS34 now specifies additive dual `−A^∨` and zero action on the scalar target, followed by the original integer-shifted action `kI−A^∨` and scalar k on that target. Both satisfy the explicit evaluation identity in DS5. The conjugate-linear coefficient map `c(λ)(v)=overline{λ(v)}` intertwines `kI−A^T` with `kI−A*` because k is real; direct coefficient conjugation proves the formula. DS19 states that the logarithmic connection complexes are complexes of sheaves of complex vector spaces. Their differentials satisfy Leibniz and are not O-linear; DS27 explicitly tensors over the constant field before its O-balanced wedge/evaluation map. The final DS5 also names the compatible invertible actions on source and target separately, with `f T_V=T_W f`.

5. **Already supplied root precision edits.** The current DS source includes the full Čech total differential convention and `rho=0` for the empty quotient in DS65. Both are correct. The latter is needed because a largest eigenvalue of an empty matrix is otherwise undefined.

6. **DT determinant denominators.** DT10–11 use the proved invertibility of the period matrix. The final source includes a complete proof before the determinant ratios: all monomial gamma factors and phases, the roots-of-unity polynomial argument, uniformly dominated ray derivatives, the coefficient-reduction ODE, the boundary cancellation, and the adjugate determinant derivative identity valid even at singular matrices. I read and checked the entire addition. It proves a nonzero period determinant on every stated `u≠0` fibre, without excluding repeated roots.

## DS1–9: image, cone, dual, and source weights

For a cochain map `c:C→D`, `B_C^m` lies in `K_c^m` because `c d_C=d_D c`. Thus the source kernel of `H^m(c)` is precisely `K_c^m/B_C^m`, and the map to `I_c^m` is surjective by definition. Both exact sequences DS2 follow with their displayed maps.

The cone differential on `D^m⊕C^{m+1}` has square zero because the mixed terms are `d_D c x−c d_C x`. Its projection lands in the shifted complex with differential `−d_C`. If `(y,x)` is a cocycle, then `d_Cx=0` and `cx=−d_Dy`, so the projected class belongs to the stated kernel. Conversely `cx=d_Dv` gives cone cocycle `(−v,x)`. If the projection is a boundary, a cone boundary removes the second component. A remaining `(y,0)` is a cone boundary precisely modulo a target boundary and the image of a source cocycle. This gives the full exact segment DS4, including both adjacent degrees and signs. A commuting action preserves every map.

For the pairing between `im f` and `im f^∨`, a change of preimage vector lies in `ker f`, and a change of functional representative lies in `ker f^∨`; each change leaves the scalar unchanged. Functionals on the target detect every nonzero image vector, and nonzero transposed functionals detect a source vector, so the pairing is perfect. Extending a basis of the image gives the annihilator descriptions in DS6. For an invertible action `T`, the dual action `(T^−1)^∨` makes evaluation invariant. For additive actions the direct evaluation computation gives

\[
\lambda(Av)+(b\lambda-\lambda\circ A)(v)=b\lambda(v).
\]

DS7–8 match the actual source theorem. For pure weight `n`, the compact-support group has upper weight `n+m`. The sheaf dual has weight `−n`, and `H_c^{2N−m}(F^∨)(N)` has upper weight `−n+(2N−m)−2N=−n−m`. It is the ordinary cohomology dual. Inverting eigenvalues gives the ordinary lower bound `n+m`. Because the common-image action is both a quotient action of the source and a subspace action of the target, a basis adapted to the kernel/image gives both bounds on precisely the same image eigenvalues. No assertion on cone eigenvalues follows from that common-image conclusion.

DS9 is valid: pure tensors of the individual images span the tensor image, and every one has an actual preimage. Extending bases proves injectivity of the indicated image tensor into the target tensor. The graded permutation signs and the `1/r!` projection are correct in characteristic zero.

## DS10–18: supported lift and compactified original source

The supported lift preserves both addition and the scalar law on supported vectors and on external absence. The quotient by `B` is the coequalizer of its inclusion and the map to supported zero: an equalizing morphism has equal values on `v` and `v+b`, because addition by the image of supported zero leaves the image of a supported vector unchanged. Conversely a well-defined quotient factor has the required equality and is unique. This argument concerns the split category and its specified supported zero. The corrected split-kernel formula above retains the distinction from external absence.

From the actual remainder/Gram formula, `B_N R_N=I` and `R_N^*O_NR_N=G_N`. With the original isometric source inclusion, `B_jΔ=0` and `R_j^*O_jΔ=0`. Expanding the source norm of `L_ij R_i=R_j+Δ` proves `Δ^*O_jΔ=G_i−G_j`, including the sign. It follows that every finite `R(z)` is a right inverse and has Gram `G_j+|z|²C`; all original null directions remain.

The vector bundle in DS15 uses the tautological line with the specified frames. In the finite chart `u≠0`, applying `B_j` to the proposed fibre map gives the vector `x0+u x1`, which vanishes only when both components vanish. At infinity the same observation kills `x0`, after which injectivity of `Δ|E1` kills `x1`. Thus the full map is a bundle injection and the source metric is smooth positive even at infinity.

The observation lattice is `E0 O+wE O`. Its cokernel is the actual `E1` residue fibre. The locally free resolution of that cokernel is `[mathscr E→EO]`; its derived restriction to infinity has differential `P0` in degrees `−1,0`, so both kernel and cokernel have dimension `r`. The negative fibre is intrinsically `E1⊗O(−D)|D`; it is not erased by ordinary specialization. Applying sheaf Hom to the line resolution gives Ext1 equal to `O(D)|D`, proving DS18 with its inverse line factor. Their evaluation is the displayed conormal/normal pairing.

## DS19–29: local comparison, global groups, and all signs

Transport through `alpha=P0+wP1` gives `alpha^−1 d alpha=P1 dw/w`. Its eigen-residues are 0 and 1, hence the horizontal monodromy is identity. In the original ambient lattice, this is simply the trivial differential restricted logarithmically. In the `E0` component the local power-series operator is `w∂w`; its only kernel and cokernel are constants. In the `E1` frame it is `w∂w+1`; division of the nth coefficient by `n+1` preserves convergence, so that stalk complex is acyclic. On the punctured disk the only Laurent one-form obstruction to a primitive is the residue coefficient. Thus the `E0` component realizes the ordinary extension and the `E1` component the compact extension, with actual stalk comparison maps. The compact extension by zero maps its flat sections to the lattice on the open chart, and both its stalk cohomology and the lattice cohomology vanish at the boundary.

The two bundle terms are `E0 O⊕E1 O(−1)` and `E0 O(−1)⊕E1 O(−2)`. The two-chart Laurent quotient gives the four line-bundle groups displayed in DS22. On the overlap, `dz/z=−dw/w` generates the surviving quotient for `Omega1`; all other one-form monomials extend to one chart. Thus the hypercohomology spectral calculation has only `E0` in total degree 0 and `E1⊗T` in total degree 2, with no possible remaining differential. This proves DS21.

The quotient complex in DS23 has two copies of the residue fibre and zero differential, since `w∂w` becomes zero modulo `w`. Ordinary global logarithmic cohomology is `E` in degree 0 and zero elsewhere. Therefore the boundary one-form maps isomorphically to `E1⊗T`. With the stated overlap difference `sV−sU` and total differential `δ+(-1)^p∇`, the degree-one boundary lift `(0,v dw/w)` has total differential `v dw/w` on the overlap. Hence the connecting map is

\[
v\,dw/w\longmapsto v\otimes[dw/w]
=-v\otimes[dz/z].
\]

The dual support-compatible lattice is `mathscr E^∨(−D)`. In the local frame its dual residue `−P1^∨` acquires `+I` from the additional `w` factor, leaving `P0^∨`. Its two summands therefore exchange compact and ordinary roles, and the groups are exactly those in DS26. Evaluation lands in `O(−D)` because of that extra line factor. The ordinary dual connection cancels the original connection under evaluation, leaving the induced connection on `O(−D)`. Wedge/evaluation then maps the tensor complex to `[O(−D)→Omega1]`; its tensor differential signs give Leibniz in total degrees 0, 1, and 2. There are no 2-forms on the curve.

The declared trace sends `[dz/z]` to 1, hence `[dw/w]` to −1. This equals the negative of the positively oriented w-circle integral divided by `2πi`. Forms extending to either chart have zero overlap residue, so this is well defined. Evaluation followed by that trace gives the perfect complementary-degree pairings. The sign is correct for the explicit convention; no change of orientation is needed.

## DS30–36: action-stable hull, dual annihilator, and metric pole

The infinity action is `diag(I,w^−1) A diag(I,w)`. Its sole possible pole is the block `w^−1 P1AP0`, proving regularity exactly when `AE0⊂E0`. Cayley–Hamilton proves that `F_A=Σ_{a=0}^{q−1}A^aE0` is invariant. Every invariant subspace containing `E0` contains it. The same argument on coherent submodules gives the minimal stable lattice `F_A O+wE O`, so DS32 gives its actual two quotient sheaves.

The constant differential preserves that lattice logarithmically and commutes with constant `A`. Any vector-space complement computes its groups, while inclusion and the boundary connecting quotient identify them intrinsically as `F_A` and `(E/F_A)⊗T`; the complement is not asserted invariant. The annihilator lattice in DS34 follows by testing a functional first on `wE` and then on `F_A`: it must be holomorphic with its constant coefficient in the annihilator. The corrected explicit dual action preserves it and makes evaluation equivariant with its declared scalar target.

An adapted coefficient basis makes every polynomial of `A` block upper triangular; the traces of its diagonal blocks sum to the full trace. This retains multiplicities and nilpotent-extension data in the original coefficient sequence, without asserting that constituent actions alone reconstruct the sequence. In the inclusion of the two lattices the newly admitted `F_A/E0` block is multiplied by `w`, so the determinant is `w^{s_A}`. The identity `G_M=J^*G_AJ` gives `det G_A=|w|^{-2s_A}det G_M`, proving the precise metric pole.

## DS37–45: curvature and actual source observation

The two expressions for `Z` agree because `K_jG_i−I=(K_j−K_i)G_i`. The first gives `G_jZ=C`, and the second gives `G_iZ=G_i(K_j−K_i)G_i`, so both asserted metric self-adjointness and nonnegativity hold. Write `f(t)=log det(I+tZ)`. Direct differentiation gives

\[
f'(t)+tf''(t)=\operatorname{Tr} Z(I+tZ)^{-2}.
\]

Since the dual determinant metric is `(det G)^−1`, its first Chern form is `i/(2π) ∂\bar∂ log det G`. In the displayed coordinate calculation this is `i/(2π)κ(|z|²) dz∧dbarz`. Polar integration with `i dz∧dbarz=2dx∧dy` converts its integral to `∫κ(t)dt`. A positive eigenvalue contributes 1 over the half-line, and a zero contributes 0. For `M(t)=tf'(t)`, the nonnegative Fubini identity gives the original logarithmic moment `f(1)` with no dropped factor of 2 or π.

`P_z` is the original O-orthogonal projection, so `N_z^*O N_z=C−|z|²CG(z)^−1C`. Multiplying out `G(z)=G_j(I+tZ)` in its trace gives `κ(t)`. Applying `B_j` yields the two opposite terms `barz G(z)^−1C` and `−barz G(z)^−1C`; only their sum is the original relation. The split quotient retains each prequotient piece before their sum reaches supported zero. The derivatives of the rational eigenvalue terms are `(-1)^n(n+1)! λ^{n+1}` at zero, proving the moment identities DS43.

The finite-dimensional exponential `exp(tA)` preserves the actual invariant sequence. On a primary block it has the exact finite nilpotent expansion in DS44. This is a valid operator-valued map from the original additive generator; the further exponential-family coefficient span is a distinct, explicitly constructed realization. DS45 follows by restriction to an invariant subspace and cyclic trace, without requiring the metric complement to be invariant. The constant-degree example `G_j=I,C=LI` has degree `r`, moment `r log(1+L)`, and exactly half the mass before `1/L`; these values follow by integrating `rL/(1+tL)^2`.

## DS46–52: every divisor power, meromorphic dual, and independent conormal depth

The inclusion from depth `m` to depth 1 has quotient basis `w^a` for `1≤a<m` in both degrees. The differential is multiplication by the nonzero integer `a` times `dw/w`, so the displayed `a^−1` map is an actual contracting homotopy. It commutes with the coefficient action. This proves the same hypercohomology groups at every positive depth and the supertrace with the original shift `[-k]`.

The higher dual cannot be replaced by a holomorphic depth-one lattice before its meromorphic terms are computed. Testing a functional on `w^mE` allows coefficients down to `w^{1−m}` after the `−D` twist. Testing it on `F` forces all coefficients from `w^{1−m}` through `w^0` to annihilate `F`. This proves exactly

\[
\mathcal M_{F,m}^\vee(-D)
=F^{ann}\mathcal O((m-1)D)+E^*\mathcal O(-D)
\subset E^*\mathcal O(*D).
\]

The omitted negative powers in the inclusion from depth-one dual have differential multiplication by their nonzero negative exponents; division by those same signed exponents contracts the quotient. The local residue on the quotient-dual frame is `1−m`, while the subspace-dual residue is 1. Thus the surviving dual groups and their divisor-twisted evaluation are correct at every depth, including `m=1` where that quotient is empty.

The tensor coefficient isomorphism in DS51 is proved by the unique expression `Σ_{b=0}^{m−1}w^b[P_b]_{I^a}`. Restriction in either depth commutes. The derivative `∂w` has the stated source depth `m+1` and target depth `m`, and `∂s_j I^{a+1}⊂I^a` follows by differentiating a product of `a+1` ideal generators. Hence the two derivatives are typed and commute. No derivative is asserted to descend within one fixed truncation when it does not.

For the actual pullback `z↦z^m`, differentiating `f(t^m)` gives `m²t^{m−1}κ(t^m)`. The substitution `s=t^m` gives total mass `mr`. In the logarithmic moment the factor `log(1/t)=m^−1 log(1/s)` cancels the additional factor m, so the original endpoint logarithmic moment is unchanged. Both are exact statements for the pulled-back metric.

## DS53–65: orthogonal lift, coupling subtraction, and source action

Start with `π Hbar=I`. Subtracting the displayed `I`-component gives the unique `G0`-orthogonal lift `H0`; another lift differs by `IU`, and the difference cancels in the formula. In coordinates `[I,H0]`, the metric block is exactly DS55, with off-diagonal `tD_F`. The triangular coefficient change to `[I,H_t]` has determinant 1. Multiplying its three block matrices gives the Schur complement `Q(t)` in DS56. Because every other lift is `H_tv+Ix` and the two terms are orthogonal, this is the actual quotient norm and its minimum is uniquely attained.

Differentiation of `πH_t=I` puts `H'_t` in `im I`; differentiation of the orthogonality equation then gives `H'_t=−Iβ_t`. In the derivative of `H_t^*G(t)H_t`, both moving-lift terms vanish by orthogonality. Hence `Q'=H_t^*CH_t`. Its derivative gives two adjoint equal terms, each `−β_t^*G_Fβ_t`, proving `Q''=−2β_t^*G_Fβ_t`. The second-order integral identity over the actual endpoints gives `D_F^*G_F(1)^−1D_F=2∫(1−t)β_t^*G_Fβ_t dt`. No unproved sign assumption is present.

The action defect lies in `im I` because `πA=A_Qπ`; injectivity of I gives the unique `a_t`. Differentiate it and use invariance of F to obtain `a'_t=β_tA_Q−A_Fβ_t`. On primary blocks the two left/right nilpotent multiplication operators commute, and every term of power `a+b−1` contains a vanishing factor. The finite geometric series in DS61 is therefore exactly the inverse for unequal primary eigenvalues. At equal eigenvalues the matrix-unit span is exactly the image, with the stated kernel retained. No inverse is asserted there.

Both compressed W identities follow by substitution. For the quotient compression, the extra `Ia_t` terms vanish against `H_t^*G I=0`, not through invariance of the metric complement. At source level, D acts in original theta variables; it does not differentiate the new scalar parameter or its coefficient lift. Thus multiplying the original primitive identity by `H_t` gives DS63 exactly. The first term is an original theta boundary, and the second is the lift of the actual arithmetic constituent and only dies after the further quotient by F. The two receiving split-zero maps are thereby explicitly different and composable.

Finally `Q(1)=Q_+−Π_F>0` implies that `Xi_F=Q_+^−1Π_F` is self-adjoint for `Q_+` and has spectrum in `[0,1)`. Taking endpoint determinants retains the same fixed `|det[I,H0]|²` on both sides before cancelling it. The logarithmic series for every eigenvalue gives DS64. The tail estimate in DS65 follows term by term from `λ^{p+1+a}≤rho^a λ^{p+1}` and `p+1+a≥p+1`. For the empty quotient use the now-stated `rho=0`. The two compressed positive matrices can then receive the existing two-trace bound, while retaining every nonnegative subtraction term.

## DS66–69 and DT1–13: the additional degree-one realization

For the exponential differential, a nonzero polynomial of degree a has image degree `a+q` with the same leading coefficient. Leading-term cancellation therefore produces a unique coefficient representative of degree less than q. This proves injectivity in degree zero, free cohomology of rank q, and compatibility with coefficient base change, including all repeated-root jets at `u=t=0`. The two commutators cancel exactly. In the chosen remainder basis the parameter connection has matrix `∂t−(A+tR)/u`. Its regular multiple `−u∂t+A+tR` preserves the ideal `(u,t)`, so it induces the original A on the special fibre. The theta deformation equations DS69 follow by cancelling the two equal added terms using `j_Er_N=I`. This computation is valid on the inherited full source domain and retains `ker j_E`.

For DT1–4, substitution `S=X+a` intertwines the full polynomial differentials. The retained potential is `Phi(X)−Phi(−a)`, so no additive constant is lost. The triangular binomial matrix has determinant 1, inverse from substitution by `−a`, and conjugates the translated companion to `A(t)+aI`. Powers of each translated primary nilpotent are conjugate with their original orders. Conjugating the connection gives `∇t−a/u`, agreeing with the explicit operator commutator.

For DT5–6, the exponent identity is

\[
\Phi_a(S)-tS=\Phi(X)-tX-\Phi(-a)-ta.
\]

The translated contours can be moved back because the integrand is entire and the connecting segments at radius R have exponent `−R^d/(d|u|)+O(R^{d−1})`, uniformly on their bounded lengths. The finite joining pieces cancel with their retained orientations. This proves the exact nonzero scalar `f_a=exp((−Phi(−a)−ta)/u)` and the period matrix formula. Since `∂t f_a=−a f_a/u`, it is precisely the scalar gauge that intertwines the two parameter connections. No extension of that exponential scalar through `u=0` is asserted; the coefficient specialization was already proved separately.

For DT7–11, the transported original Gram is `C_a^*G_NC_a`. Conjugating the original arithmetic action adds `(a+bara)G_N` to its control form; trace gives exactly `2q Re a`. The period Gram transports by the same congruence with additional scalar `|f_a|²`, hence the comparison operator is `|f_a|² C_a^−1 B_N C_a`. Its determinant is multiplied by `|f_a|^{2q}`. At the same `(u,t)` this factor and the original period determinant cancel between the same two indices, leaving exactly `det G_i/det G_j`.

The complete user source proves the needed period invertibility: at the monomial potential the nonzero gamma/phase factors multiply the matrix `(z_j^l−1)`, whose column dependence would give a degree-at-most-q polynomial vanishing on all q+1 roots of unity. It is therefore nonsingular. Coefficient differentiation descends by the displayed connection commutator and gives an ODE `Π'=Π B` along a coefficient path. Its determinant obeys `y'=(Tr B)y`, so the nonzero initial determinant remains nonzero. Thus the denominator of every period determinant ratio is nonzero, including at coincident critical points for fixed `u≠0`.

For DT12–13, all coefficients pass through the specified ring map to the finite field. The potential identity survives that map. Addition of the two Artin–Schreier torsor coordinates identifies their contracted product with the torsor of the sum potential, giving the exact tensor product of character lines. The translation is defined over the base field, hence preserves compact supports and commutes with geometric Frobenius. The constant character line contributes `psi(Tr gamma_a)`; its pth power is 1, so it preserves absolute values. This is the precisely typed finite-field scalar corresponding to the same original coefficient operation. It does not identify the additive arithmetic A with Frobenius.

The finite-field theorem hypotheses from printed 215–216 are met by the stated degree `d=q+1`, characteristic `p>d`, nonzero leading coefficient and empty smooth leading hypersurface in P0. The boundary change `b v^d=1`, `x_infty=wv` yields `x_infty^−d=b w^−d` exactly; its v-derivative has inverse `v/d`. This is the actual local family model used by the exponential source. Its lissity and mixedness are used together with Corollary 1.8.12, as required by the inspected source.

## Review disposition

**Accepted for integration at the two final source hashes above.** No mathematical defect remains in the stated logarithmic cohomology, higher-depth dual, source curvature, coupling subtraction, coefficient connection, period translation, or Artin–Schreier scalar formulas. All explicit wording/type corrections were incorporated and independently re-read. In particular the final join retains the full coefficient extension through the outer logarithmic complexes and the exponential special-fibre chain map; it makes no unsupported cohomology identification between the middle complexes.

This document is a complete proof review of those stated maps. It does not claim a uniform arithmetic upper estimate below the quartet threshold, and it certifies no unrun verification program. The author separately reports the final DS PDF build and visual checks; those outputs were not rerun or visually inspected by this reviewer, whose acceptance is of the exact mathematical sources identified above.
