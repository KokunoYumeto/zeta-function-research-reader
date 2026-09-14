# Final full-source review: conormal finite Weyl fragment

Date: 12 September 2026. Reviewer lane: `support_relation_read`.

Reviewed source:

`package:/tex/conormal_finite_weyl.tex`

Exact SHA256:

`6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a`

Read **all 649 lines**, including every definition, theorem and proof in **CW.1–40**, the reflection paragraph, metric qualifications, analytic source realization, minimum-section change, residue calculation, supported maps and `h=1` endpoint. This report is a mathematical source review. No source edits, Lean execution, new test execution, new subagent, or rendering was performed in this bounded task. The author's separate checker and rendering records were not substituted for the mathematical reading.

**Verdict: clean at the hash above. No mathematical correction is requested.** The supplied revision includes the separate Hermitian conditions for the individual projectors and for their sum; those conditions are now exact. The checks below give the scope and the algebra supporting this verdict.

## 1. The thickening, full conormal row and dual-number map — CW.1–11

The standing degree is `d≥1`, the packet has all complete local multiplicities, and `P=C[s_1,...,s_k]`, `I=(h(s_i))`, `E=P/I`, `E^[2]=P/I²`. Therefore the monic division argument has its required positive-degree hypothesis. Its triangular leading monomials are `s_i^(d a_i+b_i)`, `0≤b_i<d`, so the ordered multi-exponents uniquely specify their leading monomials. This proves the asserted free-module expansion over `C[h_1,...,h_k]`, without removing any remainder coordinate or relation coefficient.

Modulo `I²`, the expansion retains its degree-zero coefficient and precisely the `k` degree-one relation coefficients. Thus the map

\[
\iota_N:E^k\longrightarrow I/I^2,
\qquad (a_i)\longmapsto\left[\sum_i h_i\widetilde a_i\right]
\]

is onto and injective. Its independence from the lifts follows because `h_i I⊆I²`. Multiplication on `I/I²` factors through `E`, making this the claimed `E`-module isomorphism. The dimensions `(k+1)d^k` and `kd^k` follow from these retained coefficients.

The derivative `∂Σ=k^(-1)Σpartial_i` maps `I²` into `I` by the product rule. Hence the rectangular map `δ:E^[2]→E` is defined, with

\[
\delta(ab)=\pi(a)\delta(b)+\pi(b)\delta(a),\qquad
\delta\iota_N(a_i)=\frac1k\sum_i h_i'a_i.
\]

The exhibited class `[h_i]` obstructs factoring through `π`: its quotient is zero, whereas `h_i'/k` is nonzero in `E` because `h'` has degree `d−1` and leading coefficient `d` over characteristic zero. The following exact map retains both coefficients:

\[
\Phi(a)=\pi(a)+\epsilon\delta(a),\qquad
\Phi:E^{[2]}\longrightarrow E[\epsilon]/(\epsilon^2).
\]

Multiplication gives

\[
\Phi(a)\Phi(b)=\pi(a)\pi(b)+\epsilon
(\pi(a)\delta(b)+\pi(b)\delta(a))=\Phi(ab),
\]

and `δ1=0` proves unitality. Its kernel is exactly the conormal row kernel; the inclusion in CW.8 is the natural inclusion of that subspace of `N` into `E^[2]`.

Writing `jfrak=(h_i')⊂E`, the induced derivative `bar∂Σ:E→E/jfrak` is well-defined: changing a polynomial lift by `Σh_i p_i` changes the derivative in `E` by `k^(-1)Σh_i'[p_i]`. Its product rule is along the quotient `E→E/jfrak`. This proves the image constraint in CW.7. Conversely the displayed original monic remainder `σ(q)` and an arbitrary solution of

\[
t-\delta[\sigma(q)]=\frac1k\sum_i h_i'a_i
\]

produce the exact preimage `[σ(q)]+ι_N(a_i)`. Thus the source proves the entire image, including the freedom in the conormal kernel, rather than only an image inclusion. The final map `Ψ(q+εt)=[t]−bar∂Σq` is complex-linear and onto, with precisely that image as kernel. It is not claimed to be a ring quotient or an `E`-linear cokernel.

In every ordered local block `h_i=z_i^(m_i)c_i(z_i)`, the source keeps the correct formula

\[
h_i'a_i=m_i c_i(0)z_i^{m_i-1}\,a_i|_{z_i=0}.
\]

It reads the input's constant coefficient in the indicated variable, while retaining its other-variable coefficients. This repairs the original delivery's ambiguous top-coefficient wording. The image ideal is spanned by monomials having at least one top local exponent, so its dimension is `Πm_i−Π(m_i−1)`. Summing all ordered centre tuples gives

\[
\operatorname{rank}(\delta|_N)=d^k-(d-r_0)^k,
\quad\dim\ker\Phi=(k-1)d^k+(d-r_0)^k,
\quad\dim\operatorname{im}\Phi=2d^k-(d-r_0)^k.
\]

All simple and repeated factors are included. The reflection paragraph has the required sign: coordinatewise reflected conjugation anticommutes with `δ`, so setting `ε†=−ε` makes `Φ` commute with reflection. Reflection stability is introduced explicitly where used; it is not silently assumed for all earlier algebraic assertions.

## 2. Canonical section, finite commutator and projectors — CW.12–22

The section `j=[σ]_(I²):E→E^[2]` is correctly declared complex-linear. The two multiplication maps `Z` and `Zhat` retain distinct source rings. Since `∂Σ(S−k/2)=1`, the full product rule gives

\[
Z\delta-\delta\widehat Z=-\pi.
\]

For the monic remainder, multiplying by `s_i` creates only the original top coefficient outside its degree range. Subtracting `h_i` times that coefficient is the exact division step. Thus

\[
t_Z=\widehat Zj-jZ=\iota_N(c_i\ell_i)_i,
\qquad
[Z,\delta j]=-I+\delta t_Z.
\]

The minus sign and the coefficient `1/k` in

\[
J=\delta t_Z=\frac1k\sum_i M_{h_i'}c_i\ell_i
\]

are both correct. No arbitrary conormal coefficients have been substituted for the particular top-coefficient map of the section.

The identity `ell_i M_(h_i') c_i=d I` follows from the original monic derivative's leading coefficient. Consequently

\[
P_i=d^{-1}M_{h_i'}c_i\ell_i
\]

is idempotent of rank `d^(k−1)`. Distinct-variable maps commute as tensor factors. The source's direct sum `C h' ⊕ {polynomials of degree≤d−2}` is exact, since subtracting `ell(p)h'/d` kills precisely the top coefficient. Taking its tensor products gives the pairwise annihilating idempotents `P_T`, their sum `I`, and their dimensions `(d−1)^(k−|T|)` for `d>1`.

On the `T` range, `J=(d/k)ΣP_i` has eigenvalue `d|T|/k`; these values are distinct for distinct cardinalities. Therefore all stated multiplicities, the rank `d^k−(d−1)^k`, and the kernel `∩ker ell_i` follow. The trace is

\[
\frac dk\sum_i\operatorname{rank}P_i
=\frac dk\,k d^{k-1}=d^k.
\]

The `d=1` case is proved separately: every `P_i=I`, hence `J=I` on the one-dimensional space. No ambiguous `0^0` multiplicity is needed.

The metric statements in the reviewed revision are correct individually:

\[
\widetilde P_i=G_M^{1/2}P_iG_M^{-1/2}
\text{ is Hermitian}\iff P_i^*G_M=G_MP_i,
\]

and

\[
\widetilde J=G_M^{1/2}JG_M^{-1/2}
\text{ is Hermitian}\iff J^*G_M=G_MJ.
\]

One condition is not substituted for the other. All maps are explicit isometries or similarities with the original metric retained. Since `A_k=Z+(k/2)I`, its weight satisfies

\[
G_M^{-1/2}W_MG_M^{-1/2}
=G_M^{-1/2}Z^*G_M^{1/2}+G_M^{1/2}ZG_M^{-1/2}
=\widetilde Z^*+\widetilde Z.
\]

The rank comparison between the full conormal row and this finite-section correction uses exactly the composite `E→E^k→N→E` in CW.22. It therefore does not conflate `d^k−(d−r_0)^k` with `d^k−(d−1)^k`.

## 3. The complete arithmetic unit and actual minimum — CW.23–30

The original entire factor `Uhat=[Πv_h(s_i)]_(I²)` has a well-defined finite Taylor class and invertible residue value at every retained point, since the removed orders are complete. The square-zero inverse argument in the source is exact: if `Uhat b=1+n`, then `b(1−n)` is its inverse because `n²=0`.

The arithmetic section is

\[
j_U=M_{\widehat U}jM_U^{-1},\qquad\pi j_U=I,
\]

and applying the rectangular product rule gives

\[
D_U=\delta j_U=M_{\beta_h}+M_U D_0M_U^{-1},
\qquad\beta_h=U^{-1}\delta\widehat U.
\]

This equation differentiates the actual thickened unit before reduction. In particular the derivative of the inverse is not silently removed; its contribution is inside the exact finite map `D_0 M_U^(-1)` on the original remainder coordinates.

The multiplication maps commute with `Z` and `Zhat` in their respective rings, so

\[
t_U=M_{\widehat U}t_ZM_U^{-1}.
\]

Since `t_Z` takes values in `N`, the term `(δUhat)πt_Z` vanishes in exactly the specified quotient. Hence

\[
J_U=\delta t_U=M_UJM_U^{-1},\qquad
[Z,D_U]=-I+J_U.
\]

The asserted complete spectrum and ranks follow by this explicit similarity. No metric orthogonality is inferred from it.

The source function `R_ref^(k)u=T_h^(k)σ(U^(-1)u)` has Mellin transform `(Πv_h)σ(U^(-1)u)`, whose class modulo `I²` is exactly `j_Uu`. Since multiplication by `L_k=k^(-1)Σlog x_i` differentiates that Mellin transform by `∂Σ`, CW.27 follows with no additional factor of `i`. That factor occurs only when one differentiates the real line coordinate `u`, whereas the present equation uses the complex Mellin derivative.

For the actual total-degree family `M≥k(d−1)`, all monic remainder basis vectors fit within the degree bound, and multiplication by the original unit makes the full jet map onto. Its positive coefficient Gram gives the unique constrained minimum

\[
p_{M,u}=\mathcal M_M^{-1}\mathcal J_M^*
(\mathcal J_M\mathcal M_M^{-1}\mathcal J_M^*)^{-1}u.
\]

Multiplying by `mathcal J_M` proves its full jet is `u`; pairing with any vector in `ker mathcal J_M` gives zero in the original coefficient Gram. Pythagoras proves the stated minimum. Therefore `j_M=Uhat[p_M]` is a section and `a_M=j_M−j_U` takes values in the original conormal module. Its displayed numerator is a relation from this same allowed polynomial family.

The minimum's exact section correction obeys

\[
J_M^{\mathrm{sec}}=\delta(\widehat Zj_M-j_MZ)
=J_U+[Z,\delta a_M].
\]

Indeed CW.12 gives `δ Zhat a_M=Z δ a_M+πa_M`, and the final term is zero. This yields the displayed commutator difference with the correct sign. Its trace vanishes by cyclicity, so `Tr J_M^sec=d^k`. The reviewed text does not import the fixed-section rank or spectrum into this changed section. The map `a_M` and its entire commutator remain in the claim.

## 4. Residue factorization and global source map — CW.31–38

For `k=1`, the exact identity `[g']_h=U h'` gives

\[
J_Uu=[g']_h\,\ell(U^{-1}u).
\]

Its column and row are nonzero; its trace is `ell(U^(-1)[g'])=ell(h')=d`. This is a rank-one correction even when multiplication by `[g']` on the full algebra has the larger rank `r_0`.

For the explicitly reflection-stable packet, changing either polynomial representative in

\[
R_{\mathcal Z}(f,u)=\sum_\rho\operatorname{Res}_\rho
\frac{\widetilde f^\dagger\widetilde u}{g}\,ds
\]

adds a locally holomorphic function, because `h†=(−1)^d h` and `g=hv_h`, with `v_h` nonvanishing at the selected centres. If `p=rem_h(U^(-1)f†u)`, these residues equal the residues of `p/h`. Its partial fractions retain every pole order. The sum of the simple-pole coefficients equals its `1/s` coefficient at infinity, because terms of higher pole order contribute no `1/s` term. Since `h` is monic and `deg p<d`, that coefficient is exactly `ell(p)`. Therefore

\[
R_{\mathcal Z}(f,u)=\ell(U^{-1}f^\dagger u),\qquad
J_Uu=[g']_h R_{\mathcal Z}(1,u).
\]

This establishes the full residue factorization in CW.32–33, including the positive sign of the finite residues. A residue at infinity would carry its separate negative convention; the source correctly speaks instead of the `1/s` coefficient.

Mellin differentiation of the original source identity gives

\[
J_h((\log x)\Theta\phi)=[g']_h[H_\phi]_h.
\]

All polynomial inputs occur from `phi=P(D)phi_*`. On each complete local block, `[g']` is a nonzero constant times `z^(m−1)`, so multiplication by it has rank one on that block. Summing gives the exact full image rank `r_0`. Precomposition with `c_1 ell M_U^(-1)` recovers the previously proved rank-one section correction, as stated in CW.35. Thus the source supplies the exact morphism between the two presentations rather than replacing their input maps.

The local expansion `g=z^m v` gives `g'/g=m/z+v'/v`; the second term is holomorphic. Hence

\[
R_{\mathcal Z}(f,[g']_h[P]_h)
=\sum_\rho m_\rho\overline{f(1-\overline\rho)}P(\rho),
\]

with full reflected conjugation and all original multiplicities.

For `nu=q(log x)Theta:V→Q`, the bound `|log x|≤x+x^(-1)` and

\[
D^j((\log x)F)=(\log x)D^jF-jD^{j-1}F
\]

prove that logarithmic multiplication preserves the specified two-sided test space. The stated derivative identity holds for `j≥1` by induction using `D log x=−1`. With `DTheta=ThetaD` and `qTheta=0`,

\[
D_Q\nu-\nu D_V=q[D,\log x]\Theta=-q\Theta=0.
\]

For `Lambda_aF(x)=F(ax)`, the commutator is exactly `(log x)Lambda_a−Lambda_a(log x)=−log(a)Lambda_a`; its image after `qTheta` is zero, proving `nu Lambda_a=Lambda_a nu`. The induced jet `bar J_h:Q→E_h` exists because `J_hTheta=0`. No endomorphism of `Q` defined by bare logarithmic multiplication is asserted.

## 6. Supported maps and endpoint — CW.39–40 and final paragraph

The constant extraction from `E[epsilon]/epsilon²` is a unital algebra map. Infinitesimal coefficient extraction is complex-linear with the relative product rule in CW.39. Their composites with `Phi` are exactly `pi` and `delta`.

Consequently `G(Phi)` and `G(pr_0)` have their stated semiring type. The infinitesimal extraction has the split-linear coefficient type; its value on the supported unit is supported zero. For every supported conormal input, `G(Phi)` returns `(epsilon delta n)^bullet`, retaining its derivative coefficient. The algebraic kernel goes to active supported zero, while external `tau` goes to external `tau`. All declared section and vector maps admit their fixed-support split-linear lifts; no linear map is incorrectly promoted to a multiplicative map.

The final `h=1` paragraph gives `I=P`, hence `E=E^[2]=N=0`; the finite quotient maps are zero and the theta seed remains the original function. The preceding projector formulas divide by `d` only within their explicitly declared domain `d≥1`.

## Seal and integration scope

This review found **no remaining correction** in the supplied source edition. It verifies the written mathematics in CW.1–40, with its stated original analytic inputs; it does not certify an RH estimate, an analytic interval computation, or a Lean proof. In particular it accepts neither an arbitrary section in place of the actual minimum nor a Hermitian claim based only on algebraic idempotence. The exact section-change map, metric transports, full conormal coefficients, kernel/cokernel, residue units, and support types have all been retained in the checked equations.

The source hash was checked before reading and is to be checked once more when this report is delivered. Any later source edit requires review of its changed statements before reusing this seal.
