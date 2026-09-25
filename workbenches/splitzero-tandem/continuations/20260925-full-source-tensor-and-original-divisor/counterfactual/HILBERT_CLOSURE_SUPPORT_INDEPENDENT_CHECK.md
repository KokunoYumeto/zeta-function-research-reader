# Hybrid residue cones and the complete closed-support rows

25 September 2026. Independent mathematical verification CHC1–CHC8. All constructions below are on the retained complex receiving spaces. Primitive source `Z1/tau` receives no parity, addition, coefficient, or numerical weight.

## CHC0. Mathematical purpose and inputs

This derivation verifies the whole Hilbert closure defect on the original closed support, including the precise pullback sheaf, both supported localization rows, and the full comparison from the original residue cones through an intermediate cone to the restricted residue cones. The original endpoint pairs and both complete extra closed copies remain in every complex. The cyclic calculation retains the entire additional intermediate cokernel component.

Human sources are Alain Connes and Caterina Consani, [*Schemes over \(\mathbb F_1\) and zeta functions*, arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), for the coefficient sheaf and original restrictions; Alain Connes, [*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, arXiv:math/9811068v1, §III and Appendix I](https://arxiv.org/abs/math/9811068v1), for the Hilbert spectral realization; Ralf Meyer, [*A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277v3](https://arxiv.org/abs/math/0412277v3), for the closed-image framework; and Pierre Deligne, [*La conjecture de Weil. II*, §§3.6.1–3.6.3](https://www.numdam.org/item/PMIHES_1980__52__137_0/), for the closed-support lifting cross. The source kinds, exact retained reading coverage and operation prerequisites are those stated in [HCS0](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/HILBERT_CLOSURE_CLOSED_SUPPORT_AND_RESTRICTION.md).

Read ORE8 and its ORE1 definitions, SCT1–SCT4, VWR5–VWR8, ASD1–ASD6, and UOS3/UOS5–UOS6 as needed to retain the original maps and signs. The exact source synthesis, the continuous isomorphism `Sigma:S→J`, and injectivity of the original residue map `D_zeta:Q→chi Q'` are their stated proved inputs. No fresh literature search is performed or represented as source reading.

Throughout, the topology on `B` is the inherited topology from `A`, and `K=B/J` has its quotient topology. Both choices of `B` are closed in `A`, contain `J`, and give a closed Fréchet subspace `K` of `Q=A/J`. For `B=A∩C`, closedness follows from continuity of `A→H_delta`; for `Boff`, it follows from continuity of all the full critical-line Mellin jets. The natural identification of `B/J` with its image in `A/J` is topological: quotient seminorms for `B/J` are the restrictions of the corresponding quotient seminorms for `A/J`, because in either case the infimum ranges over the same `J`.

## CHC1. Stalks, pullbacks, and the original support complexes

Write `X_3={c_+,eta,c_-}` for the original three-point receiving space, and `Z={c_+,c_-}` for its closed subset. Let `j` include the generic open point, and let `i` include `Z`. Keep
\[
P=W_+\oplus W_-
=V_+\oplus V_-\oplus V_{\rm extra},
\qquad
E=\mathbb C^4\oplus V_{\rm extra},
\]
\[
d(p)=r_+v_+-r_-v_-,\qquad
d_Z(p)=(r_+v_+,r_-v_-),\qquad
H=\ker d=S_{\rm Fourier\ graph}\oplus E.
\]
Here the four endpoints and both complete extra copies have zero restriction, and
\[
r_+(h,c)=\Sigma h,\qquad r_-(g,d)=R\Sigma g=\Sigma\widehat g.
\]
Both restriction images are exactly `J`. In particular `ker d_Z=E` and `im d_Z=J^2`.

For every coefficient space `T` containing `J` through the specified inclusions, put
\[
\mathcal F_T=(W_+\xrightarrow{r_+}T\xleftarrow{r_-}W_-).
\]
Its global and closed-supported complexes, in degrees zero and one, are
\[
D_T=[P\xrightarrow d T],\qquad
D_{Z,T}=[P\xrightarrow{d_Z}T^2].
\tag{CHC1.1}
\]
The supported-to-global map is identity on `P` and
\((t_+,t_-)\mapsto t_+-t_-\) in degree one. This is a cochain map because the latter composed with `d_Z` is exactly `d`.

Let `V=H_delta` and `C=closure_V(J)`. The pullback has stalks
\[
(\mathcal F_A\times_{\mathcal F_V}\mathcal F_C)_{c_\pm}
=W_\pm\times_{W_\pm}W_\pm=W_\pm,
\]
\[
(\mathcal F_A\times_{\mathcal F_V}\mathcal F_C)_\eta
=A\times_V C=A\cap C.
\]
All its restriction maps are the original `r_±`. Therefore it equals `F_B` when `B=A∩C`. Its pullback topology at the generic stalk is the inherited `A` topology: the additional map into `C` is already continuous on this closed subspace.

For `Boff=M_0^{-1}I_line` and one fixed finite `delta`, only
\[
B_{\rm off}\subseteq A\cap C
\tag{CHC1.2}
\]
is established in general. The finite receiver retains only the derivatives below its strict cutoff, whereas `Boff` kills every critical-line derivative. Thus `F_Boff` is a subobject of the displayed pullback; equality requires that the chosen cutoff retain every actual critical multiplicity. Without such a bound, the full critical family gives the exact identity
\[
B_{\rm off}=\bigcap_{N\ge1}(A\cap C_{1/2,N}).
\tag{CHC1.3}
\]
All subsequent algebraic support and cone statements apply to either closed `B` containing `J`.

## CHC2. Complete closed-support localization for F_B and j!B

Put `pi_B:B→K=B/J`. From CHC1.1,
\[
H_Z^0(\mathcal F_B)=E,\quad
H^0(\mathcal F_B)=H,\quad
H_Z^1(\mathcal F_B)=K^2,\quad
H^1(\mathcal F_B)=K,
\]
and every higher group vanishes. Generic restriction has cohomology `B` in degree zero only. The complete localization row is
\[
0\longrightarrow E\xrightarrow{\iota}H
\xrightarrow{\mathrm{res}}B
\xrightarrow{b\mapsto(\pi_Bb,\pi_Bb)}K^2
\xrightarrow{(k_+,k_-)\mapsto k_+-k_-}K
\longrightarrow0,
\tag{CHC2.1}
\]
where
\[
\mathrm{res}((h,c),(\widehat h,d),w)=\Sigma h.
\]
Its image is `J`; its kernel is exactly `E`. The kernel of the diagonal quotient map is also `J`, and the remaining exactness is the diagonal/difference identity on `K^2`. This verifies every map directly.

For `j!B`, both closed stalks are zero. Its global and supported complexes are
\[
R\Gamma(j_!B)=[0\to B],\qquad
R\Gamma_Z(j_!B)=[0\to B^2],
\tag{CHC2.2}
\]
with the same difference map in degree one. Thus its entire nonzero localization row is
\[
0\longrightarrow B\xrightarrow{b\mapsto(b,b)}B^2
\xrightarrow{(b_+,b_-)\mapsto b_+-b_-}B
\longrightarrow0.
\tag{CHC2.3}
\]
The initial `H_Z^0` and `H^0` groups are both zero. The morphism `j!B→F_B` induces the complete map from this row to CHC2.1: the two initial zero groups map to `E,H`, the generic `B→B` map is identity, and the two later maps are `pi_B^2` and `pi_B`. This keeps the generic extension separate from closed-supported cohomology while computing their exact relation.

Let `P_Z` denote the sheaf on the discrete closed set with stalks `W_+,W_-`, so that `Gamma(Z,P_Z)=P`. There is a stalkwise exact sequence
\[
0\to j_!B\to\mathcal F_B\to i_*P_Z\to0.
\tag{CHC2.4}
\]
Its complete nonzero global and supported cohomology rows are respectively
\[
0\to H\to P\xrightarrow d B\xrightarrow{\pi_B}K\to0,
\tag{CHC2.5}
\]
\[
0\to E\to P\xrightarrow{d_Z}B^2
\xrightarrow{\pi_B^2}K^2\to0.
\tag{CHC2.6}
\]
The connecting maps have the displayed positive signs: lift `p∈P` by identity into degree zero of `D_B` or `D_{Z,B}`, and apply the actual differential. The map from CHC2.6 to CHC2.5 is `E→H`, identity on `P`, difference `B^2→B`, and difference `K^2→K`. Its commutativity is the identity `difference ∘ d_Z=d`.

The entire continuous-dual localization row for `F_B`, with the original uniform twist `chi(a)=a`, is
\[
0\to Y_B\xrightarrow{y\mapsto(y,-y)}Y_B^2
\xrightarrow{(y_+,y_-)\mapsto\pi_B'(y_++y_-)}\chi B'
\xrightarrow{\mathrm{res}_B'}\chi H'
\xrightarrow{\iota'}\chi E'\to0,
\tag{CHC2.7}
\]
where `Y_B=chi K'` and
\(\mathrm{res}_B'\alpha=(\Sigma_B'\alpha,0_E)\).
The summation map `Sigma_B:S→J⊂B` retains its original inverse and topology. Hence restriction to `J` is onto by Hahn–Banach, giving the complete `S'` coordinate. All remaining exactness follows from the dual quotient theorem ASD2. These rows are strictly exact for weak-* topologies; each transpose is also strong-dual continuous. Dualizing CHC2.3 gives the split row
\[
0\to\chi B'\xrightarrow{\alpha\mapsto(\alpha,-\alpha)}
(\chi B')^2\xrightarrow{(\alpha_+,\alpha_-)\mapsto\alpha_++\alpha_-}
\chi B'\to0.
\tag{CHC2.8}
\]

## CHC3. Exact comparison with the Hilbert closure sequence

For `C⊂V`, write `Q_V=V/C`, and set
\[
\overline{\mathcal F}_V=(W_+\xrightarrow0Q_V\xleftarrow0W_-).
\]
The exact VWR6 sequence is
\[
0\to j_!C\to\mathcal F_V\to\overline{\mathcal F}_V\to0.
\tag{CHC3.1}
\]
The inclusion `B→C`, the original map `F_B→F_V`, and the map
\(i_*P_Z\to\overline{\mathcal F}_V\) that is identity on both closed stalks and zero on the generic stalk give a morphism from CHC2.4 to CHC3.1. On global cohomology it is the following exact-row diagram:
\[
\begin{array}{ccccccccccccc}
0&\to&H&\to&P&\xrightarrow d&B&\to&K&\to&0&\to&0\\
&&\Vert&&\Vert&&\downarrow&&\downarrow&&\downarrow\\
0&\to&H&\to&P&\xrightarrow d&C&\to&V/J&\to&V/C&\to&0.
\end{array}
\tag{CHC3.2}
\]
The middle comparison sends `[b]_J` to the same class in `V/J` and is injective. Its image lies in `C/J`. For `B=A∩C`, that image is exactly the intersection of `Q⊂V/J` with `C/J`. For `Boff`, it is the indicated smaller subspace, with its exact full-family definition CHC1.3.

The complete supported cohomology row of CHC3.1 is
\[
0\to E\to P\xrightarrow{d_Z}C^2
\to(V/J)^2\to(V/C)^2\to0.
\tag{CHC3.3}
\]
The connecting map is `d_Z`, again by lifting degree-zero cochains. The map from CHC2.6 to this row is identity on `E,P`, inclusion on `B^2`, inclusion on `K^2`, and the zero map into the final term. The map from CHC3.3 to the lower row of CHC3.2 is `E→H`, identity on `P`, and difference on each subsequent pair. This establishes all signs and all endpoint/extra terms at once.

The intermediate `F_C` has localization row
\[
0\to E\to H\to C\to(C/J)^2\to C/J\to0,
\tag{CHC3.4}
\]
with the same diagonal quotient and difference maps. The maps `F_B→F_C→F_V` give identity on `E,H` and the actual inclusions on the other terms. Together with
\(0\to C/J\to V/J\to V/C\to0\), this computes the closure step without deleting its non-Hausdorff term.

These `C,V` cohomology rows are algebraic sheaf/cochain rows with their displayed quotient topologies. No exact continuous-dual localization row for `F_C` is inferred: `J` is dense in `C`, and the original Fréchet inverse `J→S` need not be continuous for the inherited Hilbert topology. The valid continuous-dual rows above use `B` with its inherited `A` topology.

## CHC4. Hybrid residue complexes and their full cohomology

Write `beta:B→A`, `kappa:K→Q`, and `pi_A:A→Q`. They satisfy
\[
\pi_A\beta=\kappa\pi_B.
\]
Let
\[
Y=\chi Q',\qquad \widetilde A=\chi A',\qquad
\Psi_A=\pi_A'D_\zeta\pi_A.
\]
The proposed hybrid complexes in degrees `−1,0,1,2` are exactly
\[
K^\times=[P\xrightarrow{-d}B
\xrightarrow{\Psi_A\beta}\widetilde A
\xrightarrow{d_A'}\chi P'],
\tag{CHC4.1}
\]
\[
L^\times=[P\xrightarrow{-d}B
\xrightarrow{(\Psi_A\beta,-\Psi_A\beta)}\widetilde A^2
\xrightarrow{d_{Z,A}'}\chi P'].
\tag{CHC4.2}
\]
Their final maps remain the original ones:
\[
d_A'\alpha=(r_+'\alpha,-r_-'\alpha,0_{\rm extra}),
\qquad
d_{Z,A}'(\alpha_+,\alpha_-)
=(r_+'\alpha_+,r_-'\alpha_-,0_{\rm extra}).
\]
The products of consecutive differentials vanish because `pi_A d=0` and `pi_A'Y` annihilates both restriction images `J`.

Put
\[
T_K=Y/D_\zeta\kappa(K).
\tag{CHC4.3}
\]
Their complete ordinary cohomology is
\[
\begin{array}{c|cc}
n&H^nK^\times&H^nL^\times\\\hline
-1&H&H\\
0&0&0\\
1&T_K&T_K\oplus Y\\
2&\chi H'&\chi E'.
\end{array}
\tag{CHC4.4}
\]
All other degrees vanish. Indeed the kernel of `Psi_A beta` is exactly `J`: `pi_A'` and `D_zeta` are injective, and `kappa` is an inclusion. This proves degree zero. The degree-one cycle spaces are exactly `pi_A'Y` and `(pi_A'Y)^2`; the boundary images are `pi_A'D_zeta K` and its anti-diagonal. Hence their quotients are as stated, through the precise coordinates
\[
[(\pi_A'\lambda_+,\pi_A'\lambda_-)]
\longmapsto
\left(\left[\frac{\lambda_+-\lambda_-}{2}\right],
\frac{\lambda_++\lambda_-}{2}\right).
\tag{CHC4.5}
\]
Its inverse sends `([lambda],mu)` to the class of
\((\pi_A'(\lambda+\mu),\pi_A'(-\lambda+\mu))\).
Changing `lambda` by `D_zeta k` changes that pair by exactly a boundary. Finally the cokernels of the unchanged last differentials are the full original `chi H'` and `chi E'`, by restriction to `H` and `E`. Thus every retained coefficient is present.

## CHC5. Maps to the original cones and the unchanged SCT triangle

The maps `K×→K_zeta` and `L×→L_zeta` are identity in degrees `−1,1,2` and `beta` in degree zero. Every differential square commutes. Their cohomology maps are identity on `H`, the natural quotient
\[
T_K\longrightarrow C_\zeta:=Y/D_\zeta Q
\]
in degree one (together with identity on `Y` for `L`), and identity on `chi H'` or `chi E'` in degree two.

The degreewise quotient of each injection is `(A/B)[0]`. Its connecting map is positive:
\[
[a]_B\longmapsto[D_\zeta\pi_Aa]\in T_K,
\tag{CHC5.1}
\]
or the same class in the first summand of `T_K⊕Y`. This follows by lifting `a` to degree zero and applying `+Psi_A`. It yields the exact row
\[
0\to Q/K\xrightarrow{\overline D_\zeta}T_K
\to C_\zeta\to0.
\tag{CHC5.2}
\]
Injectivity follows from injectivity of the full residue map, not from a restriction of its pairing.

The hybrid supported comparison `J×:K×→L×` is identity in degrees `−1,0,2` and anti-diagonal in degree one. Its degreewise quotient is still the entire original dual overlap:
\[
0\to K^\times\xrightarrow{\mathcal J^\times}L^\times
\xrightarrow{\nu}\widetilde A[-1]\to0,
\qquad \nu^1(\alpha_+,\alpha_-)=\alpha_++\alpha_-.
\tag{CHC5.3}
\]
The symmetric graded section is `(alpha/2,alpha/2)` and its connecting cochain is unchanged:
\[
\theta\alpha=
\left(\frac{r_+'\alpha}{2},\frac{r_-'\alpha}{2},0_{\rm extra}\right).
\tag{CHC5.4}
\]
Restriction to the actual Fourier graph gives `Sigma'alpha`, including both halves. Thus its complete ordinary nontrivial row is
\[
0\to T_K\xrightarrow{t\mapsto(t,0)}T_K\oplus Y
\xrightarrow{(t,y)\mapsto2\pi_A'y}\widetilde A
\xrightarrow{\alpha\mapsto(\Sigma'\alpha,0_E)}\chi H'
\xrightarrow{\iota'}\chi E'\to0.
\tag{CHC5.5}
\]
The degree-`−1` map is identity on the full `H`; degree zero is zero. The explicit contraction of SCT2 applies without alteration, because its proof uses only CHC5.3, the same graded section, and the same connecting cochain.

## CHC6. Restriction to B-dual cones and the possible radical

Continuous restriction gives the surjection `beta':A'→B'`, by Hahn–Banach. Define
\[
Y_B=\chi K',\qquad
D_B=\kappa'D_\zeta\kappa:K\to Y_B,
\qquad
\Psi_B=\pi_B'D_B\pi_B=\beta'\Psi_A\beta.
\]
The genuine `B`-restricted cones are
\[
K_B=[P\xrightarrow{-d}B\xrightarrow{\Psi_B}\chi B'
\xrightarrow{d_B'}\chi P'],
\]
\[
L_B=[P\xrightarrow{-d}B\xrightarrow{(\Psi_B,-\Psi_B)}(\chi B')^2
\xrightarrow{d_{Z,B}'}\chi P'].
\tag{CHC6.1}
\]
The hybrid-to-restricted maps are identity on `P,B,P'`, and `beta'` on each degree-one dual term. The final square is the actual transpose identity
\[
d_B'\beta'=d_A',\qquad
d_{Z,B}'(\beta'\oplus\beta')=d_{Z,A}'.
\]

Set `R_B=ker D_B` and `T_B=Y_B/D_BK`. Directly repeating the cycle/boundary calculation yields
\[
\begin{array}{c|cc}
n&H^nK_B&H^nL_B\\\hline
-1&H&H\\
0&R_B&R_B\\
1&T_B&T_B\oplus Y_B\\
2&\chi H'&\chi E'.
\end{array}
\tag{CHC6.2}
\]
Thus the hybrid degree-zero vanishing does not require the restricted residue form to be nondegenerate. The maps in degree one are
\[
[y]\longmapsto[\kappa'y],\qquad
([y],z)\longmapsto([\kappa'y],\kappa'z).
\tag{CHC6.3}
\]
They are onto because `K` is closed in `Q` and continuous functionals on it extend to `Q`.

Let `Z_B=chi(Q/K)'`, viewed as the annihilator of `K` in `Y`. The kernels of the two degreewise restriction maps are `Z_B[-1]` and `Z_B^2[-1]`, respectively, through `pi_A'`. Consequently the exact middle rows are
\[
0\to R_B\xrightarrow{k\mapsto D_\zeta\kappa k}Z_B
\to T_K\to T_B\to0,
\tag{CHC6.4}
\]
\[
0\to R_B\xrightarrow{k\mapsto(D_\zeta\kappa k,-D_\zeta\kappa k)}Z_B^2
\to T_K\oplus Y\to T_B\oplus Y_B\to0.
\tag{CHC6.5}
\]
The connecting signs are positive in the first row and the stated anti-diagonal in the second, because they are the actual degree-zero differentials of a lifted `B` representative. In CHC6.5 the middle map is the half-difference/half-sum of the pair, with the first coordinate reduced modulo `D_zeta K`. Degree `−1` and degree two maps are identities on their complete terms.

For `Boff`, VWR8 proves `R_B=0` on both sides. For the finite critical receiver `B=A∩C_delta`, the residue restriction can have a radical. At a critical zero of multiplicity `m`, write `r=r_delta(rho)`. Its retained kernel block is
\[
t^r\mathbb C[t]/(t^m).
\]
The original full residue form pairs it with the reflected block, whose same cutoff is `r`. VWR8's exact germ computation says that the annihilator of the reflected ideal of order `r` is the ideal of order `m-r`; the full invertible zeta germ and the substitution `v=-t` preserve these orders. Intersecting with the original block gives exactly
\[
t^{\max(r,m-r)}\mathbb C[t]/(t^m).
\tag{CHC6.6}
\]
Every off-critical block in \(K\) is whole, and has zero radical by its actual reflected isolator. Globally, \(R_B\) consists exactly of classes with all off-critical jets zero and critical jets zero through order \(\max(r,m-r)-1\). Necessity is tested by the actual global isolators in \(K\).

Here is the full original-space proof of sufficiency, without an infinite residue expansion. Let \(F\in\mathcal M_0B\) satisfy those orders and let \(G\in\mathcal M_0B\) be arbitrary. The product \(F(s)G(1-s)\) belongs to the original entire Mellin space \(\mathcal B\): each factor is holomorphic and rapidly decreasing on each bounded vertical strip, and reflection carries such a strip to another bounded strip. At every off-critical zero the first factor vanishes to full multiplicity. At a critical-line zero the sum of the two vanishing orders is at least \(\max(r,m-r)+r\ge m\), since reflected zeros have the same full multiplicity and the same cutoff. Hence the product belongs to the full ideal \(I=\mathcal M_0J\). By the actual original synthesis theorem [OMS1–OMS5](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/ORIGINAL_MELLIN_SPECTRAL_SYNTHESIS.md), there exists an actual \(h\in S\) such that
\[
F(s)G(1-s)=\mathcal M_0\Sigma h(s)
=2\zeta(s)\mathcal M_Sh(s).
\tag{CHC6.7}
\]
The factor \(2\) is retained. Since \(h\) is even and \(h(0)=0\), one has \(h(v)=O(v^2)\) at zero, and the same estimate holds after every Euler derivative. Thus \(\mathcal M_Sh(s)\) is holomorphic on \(\Re s>-2\). Integration by parts with \(v\partial_v\) shows decay faster than any inverse power of \(|\Im s|\), uniformly on every closed bounded strip inside that half-plane. The boundary terms vanish at both ends by the displayed order at zero and Schwartz decay at infinity.

Consequently the original integrand \(F(s)G(1-s)/\zeta(s)\) has the exact continuation \(2\mathcal M_Sh(s)\) on the strip \(-1\le\Re s\le2\), including its values at all original zeros and at the original pole. Cauchy's theorem on a rectangle with vertical sides \(-1\) and \(2\) and horizontal sides at \(\pm T\) gives equality of the two vertical integrals as \(T\to\infty\); each horizontal integral tends to zero by the proved uniform decay and its fixed length \(3\). These are exactly the two original contours in [GZR](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/original-character-lifting/tau_lifting_weights_20260924/GLOBAL_ORIGINAL_ZETA_RESIDUE_DUALITY_INDEPENDENT.md). Their difference is zero. Reversing the two input roles proves the other radical statement by the same full synthesis. No unrestricted jet product, unproved spectral-density assertion, or infinite residue summation is used.

In particular a critical block with \(0<r<m\) contributes a radical of dimension \(\min(r,m-r)\). Therefore CHC6.2 must retain \(R_B\) at finite cutoffs unless its vanishing has separately been proved.
## CHC7. Cyclic consequence for the hybrid SCT map

This consequence uses precisely the original ORE/SCT convention and does not replace a separate derivation of the `B`-restricted cyclic sequence. Let `q` be a nonzero polynomial in the original generator. For any of these complexes,
\[
\mathscr H^n(M)=M^n\oplus M^{n-1},\qquad
\partial^n(u,v)=(d_Mu,d_Mv-(-1)^nq u).
\tag{CHC7.1}
\]
The quotient in CHC5.3 has Hom complex `tilde A --(+q)→tilde A` in degrees one and two; the original `q` on `tilde A` is onto by ORE3. The hybrid table must nevertheless retain `T_K/qT_K` and `ker q|T_K`, since invertibility of `q` on `C_zeta` does not imply invertibility on `T_K` in CHC5.2.

The full groups are
\[
\begin{array}{c|cc}
n&H^n\mathscr H(K^\times)&H^n\mathscr H(L^\times)\\\hline
-1&\ker(q:H\to H)&\ker(q:H\to H)\\
0&H/qH&H/qH\\
1&\ker(q:T_K\to T_K)&\ker(q:T_K\to T_K)\oplus\ker(q:Y\to Y)\\
2&T_K/qT_K\oplus\ker(q:\chi H'\to\chi H')
&T_K/qT_K\oplus Y/qY\oplus\ker(q:\chi E'\to\chi E')\\
3&(\chi H')/q(\chi H')&(\chi E')/q(\chi E').
\end{array}
\tag{CHC7.2}
\]
All other groups vanish. The degree-two splitting on `K×` is specified by the original equivariant plus-chart extension of the `S'` coordinate of `H'`, together with the identity endpoint/extra extension. A `q`-annihilated `h'` therefore has an actual degree-two lift `(u,0)` with `qu=0`. The general two-term-resolution cohomology sequence shows that the complementary subspace is exactly `T_K/qT_K`. The degree-two `L×` splitting uses the retained direct subcomplex `chi E'` and its unchanged degree-one half-difference/half-sum.

Write `delta_q:ker q|tilde S→Y/qY` for the original ORE connecting class, and let `p:Y/qY→T_K/qT_K` be the actual quotient. In these specified coordinates, the degree-two hybrid supported map is
\[
([t],\eta,e)\longmapsto
\left([t]-\frac12p\delta_q(\eta),
-\frac12\delta_q(\eta),e\right).
\tag{CHC7.3}
\]
Proof: extend `eta` by the plus-chart cochain `u`, choose `alpha` with `Sigma'alpha=eta`, and put `q alpha=pi_A'y_alpha`. In the target Hom complex subtract the boundary of `((alpha,0),0)`. Formula CHC7.1 leaves `(0,(-q alpha,0))`. Its half-difference and half-sum are both `−y_alpha/2`; only the first is reduced modulo `D_zeta K`. This proves both surviving components and their signs. The class from `T_K/qT_K` maps to the first summand by identity, and endpoint/extra classes map by identity. Changing `alpha` changes `y_alpha` by `qY`, so CHC7.3 is independent of the lift.

In degree one the map is `t↦(t,0)`, in degrees `−1,0` it is identity, and in degree three it is the actual restriction `chi H'/q→chi E'/q`, an isomorphism because `q` is onto on the complementary `tilde S` coordinate. The quotient's connecting map sends `gamma∈ker q|tilde A` to `(0,Sigma'gamma,0)` in degree two. To check its zero first coordinate, compare `theta gamma` with the plus-chart extension of `Sigma'gamma`: their difference is `d_A'(-gamma/2)`, and the Hom boundary has no second component because `q gamma=0`.

Here is the complete cochain proof of the degree-two splitting and its behavior under both requested comparison maps. Let
\[
s_+:\chi H'=\widetilde S\oplus\chi E'\longrightarrow\chi P'
\]
extend a Schwartz functional only on the plus chart, and extend each of the four endpoint and both extra functionals on its retained coordinate. Restriction back to `H` is identity. This section is equivariant: the Fourier graph is parametrized by its plus Schwartz coordinate, whose action is exactly the plus-chart action; each endpoint and extra coordinate is unchanged. Therefore `q s_+=s_+q`.

A degree-two hybrid `K` cocycle is `(u,v)∈chi P'⊕tilde A` satisfying
\[
d_A'v=q u.
\]
Put `h'=u|_H`; then `qh'=0`. Since `u-s_+h'` annihilates `H`, choose `alpha∈tilde A` with
\[
d_A'\alpha=u-s_+h'.
\]
Subtract the actual degree-one boundary
\(\partial^1(\alpha,0)=(d_A'\alpha,q\alpha)\).
The remaining cocycle is
\[
(s_+h',v-q\alpha),\qquad v-q\alpha=\pi_A'y
\quad\text{for a unique }y\in Y.
\]
Its splitting coordinate is exactly
\[
([y]\bmod(D_\zeta K+qY),h')
\in T_K/qT_K\oplus\ker q|_{\chi H'}.
\tag{CHC7.4}
\]
If `alpha` is changed by `pi_A'z`, then `y` changes by `−qz`. A general degree-one boundary from `(alpha,b)` adds
\((d_A'alpha,qalpha+Psi_A beta b)\), so it changes `y` only by an element of `qY+D_zeta K`. Conversely those changes are exactly such boundaries. Thus CHC7.4 is a well-defined isomorphism, and its section is the displayed `(s_+h',0)`. This also verifies the placement and sign of the `T_K/qT_K` summand.

For `L×`, a degree-two cocycle is `(u,(v_+,v_-))`. Its endpoint/extra restriction is `e∈ker q|chi E'`. Choose `w=(alpha_+,alpha_-)` with `d_{Z,A}'w=u-e`, which exists because the cokernel of `d_{Z,A}'` is exactly `chi E'`. Subtract the boundary `(d_{Z,A}'w,qw)`. The remaining two degree-one entries annihilate `J`; write them as `pi_A'y_+` and `pi_A'y_-`. Their precise coordinates are
\[
\left(\left[\frac{y_+-y_-}{2}\right]\bmod(D_\zeta K+qY),
\left[\frac{y_++y_-}{2}\right]\bmod qY,e\right).
\tag{CHC7.5}
\]
Different choices of `w` add `q` of a degree-one cycle; degree-zero `B` boundaries add only the anti-diagonal `D_zeta K`. Consequently these are exactly the cohomology coordinates in CHC7.2, independent of all lifts.

Under the maps to the original cones, the plus-chart and endpoint/extra extensions are unchanged. Since `q` is invertible on `C_zeta`, the induced maps on the above degree-two coordinates are exactly
\[
H^2\mathscr H(K^\times)\to H^2\mathscr H(K_\zeta):
([t],\eta,e)\longmapsto(\eta,e),
\]
\[
H^2\mathscr H(L^\times)\to H^2\mathscr H(L_\zeta):
([t],[y],e)\longmapsto([y],e).
\tag{CHC7.6}
\]
Applying these maps to CHC7.3 gives exactly ORE8.8, `(η,e)↦(−delta_q(η)/2,e)`. Thus the disappearance of the first component in the original cones is a proved quotient consequence, not a sign convention.

For restriction to `B`, put `s:T_K→T_B`, `s([y])=[kappa'y]`, and let `s_q` and `kappa'_q` be its and `kappa'`'s maps modulo `q`. Both original extension rows commute with restriction, so the connecting classes satisfy
\[
\delta_{q,B}(\eta)=\kappa'_q\delta_{q,A}(\eta).
\tag{CHC7.7}
\]
This is also a direct lift computation: `alpha` with `Sigma_A'alpha=eta` restricts to `beta'alpha` with `Sigma_B'beta'alpha=eta`, and
\(q\beta'\alpha=\beta'\pi_A'y_\alpha
=\pi_B'\kappa'y_\alpha\).
The same `s_+` is used in `P'` on both sides, and the choices `alpha` and `w` above can be restricted by `beta'`. Hence the degree-two comparison maps are exactly
\[
([t],\eta,e)\longmapsto(s_q[t],\eta,e),
\qquad
([t],[y],e)\longmapsto(s_q[t],\kappa'_q[y],e).
\tag{CHC7.8}
\]
They remain valid even if `R_B` is nonzero, because degree-two Hom cohomology depends on `H^1` and `H^2` of the cones; the degree-zero radical affects a different degree. If `p_B:Y_B/qY_B→T_B/qT_B`, then `s_q p=p_B kappa'_q`. Together with CHC7.7 this proves that CHC7.8 carries CHC7.3 to the exact `B`-restricted degree-two formula
\[
([t_B],\eta,e)\longmapsto
\left([t_B]-\tfrac12p_B\delta_{q,B}(\eta),
-\tfrac12\delta_{q,B}(\eta),e\right).
\tag{CHC7.9}
\]
No injectivity or quotient disappearance for the restricted pairing has been assumed in deriving these commuting squares.

## CHC8. Verified outcome

The proposed hybrid complexes, their maps, and their ordinary cohomology are correct. The complete closed-support and closure rows are CHC2–CHC3, with `d_Z` carrying two positive restrictions and the global differential carrying their difference. The exact pullback assertion needs `B=A∩C` at the stated fixed receiver. For `Boff`, the full-family intersection CHC1.3 is the unconditional statement. Restricting both residue slots to a finite-cutoff `B` can produce the explicit radical CHC6.6; it does not affect hybrid degree-zero vanishing. In cyclic hybrid calculations the extra `T_K/qT_K` component in CHC7.3 must be retained.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
