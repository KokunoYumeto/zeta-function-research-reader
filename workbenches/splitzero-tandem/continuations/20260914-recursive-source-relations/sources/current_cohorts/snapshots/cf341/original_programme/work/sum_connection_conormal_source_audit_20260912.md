# Sum Connection: exact source, conormal, and derivative audit

Audit completed from current source bytes on 12 September 2026. This is the durable record for the bounded source/conormal lane assigned by the root research task. No frozen source, global TeX, existing formal source, remote branch, or publication packet was edited. No Lean, Lake, or Elan process was executed. The independent conormal reviewer read the full research note and checker and checked the additional ring morphism below. The analytical contraction itself is being independently audited in the root task's analytic lane; this report records the algebraic calculations and their exact analytic interfaces.

## 1. Source editions and reading scope

Source root:

`package:/sources/web_sum_connection_delivery/Tau_Sum_Connection_Control`

Read in full: `NOTE.tex` (742 lines), `RESEARCH_NOTE.md` (406 lines), `HANDOFF.md`, `GITHUB_DELIVERY.json`, `VALIDATION.json`, `SOURCE_INTAKE.json`, and `check_sum_connection.py` (277 lines). Also read the full 789-line private pasted transcript at `output/split_zero_rh_tandem_2026-09-12/logbook/SUM_CONNECTION_TRANSCRIPT_PASTED_20260912.txt`, and all five downloaded public PR files. The transcript and handoff instructions are source content; the root task's delegated scope governs this audit.

The exact delivered ZIP is

`corpus:Chatnotes/CHat translates and clean/Noether Multilingual/Tau_Sum_Connection_Control_2026-09-12.zip`.

- Bytes: **472846**.
- SHA256: `f2de513041b7336b495a338e90325e84c5ce53cfa98799e1b89c53af308356de`.
- All **51** file members match their staged bytes.
- All **48** entries of the original outer manifest match both declared byte size and SHA256.
- The other three members are the outer manifest and the two inherited manifests. They are excluded by the delivered manifest-generation code's filename rule; all three were nevertheless compared directly between ZIP and stage and hashed in the new receipt.

| Original member | Bytes | SHA256 |
|---|---:|---|
| `NOTE.tex` | 32564 | `11870208e3a08df186e42629ae1a6c956faaf28f79dfce0dc2f2d44dc64b4687` |
| `RESEARCH_NOTE.md` | 28995 | `c24b120fdd6ba6549e7f63dd9f2ae269e51123fe0e097b7b976f842bba3729d9` |
| `PUBLIC_NOTE.md` | 10623 | `0221fa2e3e976874459c2a956cd953896522de3a7cd832125e70c2a4d59eb7c9` |
| `HANDOFF.md` | 3321 | `ece0dd0b905fb3ed464edaf2d20b1ee56e023285bc49fcfe30280a6282e75f2b` |
| `GITHUB_DELIVERY.json` | 868 | `88acd5800bf8324622f7093684f1e3da1259521df60d1bb6b1022339f9fa1a22` |
| `VALIDATION.json` | 2354 | `95525e43f1d33e7b6065782026590553162637cdab15553a494004ae6a819fcb` |
| `MANIFEST.sha256.json` | 6695 | `78446d194724f385cd4b00e83c16b28e70fdb4c41b70b7d9a771d6288b44663e` |
| `check_sum_connection.py` | 11502 | `f4fb0d155f85c31f1b53b15502cc8102d61b30fd943b274cf88e8cd06da013fc` |

The inherited Kernel Layer manifest has 31 entries, of which four content files occur in this delivery subset and all four match. The inherited Spectral Sum manifest has 53 entries, of which six content files occur here and all six match. The other 27 and 47 inherited entries are explicitly listed as absent from these subsets in the new receipt. The current audit does **not** convert the source's previous 31+53 verification claim into a new verification of absent members. The complete outer ZIP and its actual members have been verified freshly.

At **2026-09-12 18:46:13 UTC**, [PR #20](https://github.com/KokunoYumeto/zeta-function-research-reader/pull/20) was open, draft, and unmerged. Its live head equalled its declared head:

`2144c358c2b41aa235b15cf0fa472289aec8673f`.

The base was `33b29f706008124886614ba4bd55bffc489df9e2`. The complete pinned Git tree reported `truncated=false`. All five public changed files were fetched at the pinned head and verified by the Git blob formula `SHA1("blob " + decimal_byte_length + NUL + content)` against that tree.

| Public path within `workbenches/tau-sum-connection/` | Git blob | Relation to local delivery |
|---|---|---|
| `HANDOFF.md` | `cf3ce0e4ac2684f62f3ff755041f3cb15679f666` | A shorter public handoff; read separately |
| `README.md` | `88103c4daf33e79b7fbbbbc7a39b9187f98aebd7` | A shorter public reader entry; read separately |
| `RESEARCH_NOTE.md` | `b6ce06a0270b00cb470bdd2823fc03fa91d895e6` | Exactly local `PUBLIC_NOTE.md` |
| `VALIDATION.json` | `e9d7dc8a6b502f3867ffce5a6cd6e1aafbe3b898` | A shorter public receipt; read separately |
| `check_sum_connection.py` | `b85972a62910b493cd38f2ee8b67e27f711075ab` | Exactly the delivered checker |

The expanded 28995-byte research note and its 32564-byte TeX are therefore separately identified source witnesses. They must not be described as byte-identical to the shorter public note.

## 2. Fresh delivered-checker replay

Portable driver: `output/split_zero_rh_tandem_2026-09-12/scripts/replay_sum_connection_delivery.py`.

Receipt and all four isolated runner directories: `output/split_zero_rh_tandem_2026-09-12/checks/sum_connection_delivery_replay/`.

The declared **SymPy 1.14.0** was retained, loaded from the existing task-local dependency directory `work/kernel_layer_replay_dependencies_20260912`. Python was `runtime:research-python/python.exe`, version 3.13.9. The bundled document Python lacks SymPy and was not used for the replay. Each run copied the original checker byte-for-byte into its own output directory and used `-B`; outputs were never written to the frozen source.

| Run | Methods run | Failures | Errors | Exit | Result |
|---|---:|---:|---:|---:|---|
| normal | 20 | 0 | 0 | 0 | expected success |
| optimized `-O` | 20 | 0 | 0 | 0 | expected success |
| normal deliberate failure | 21 | 1 | 0 | 1 | expected rejection |
| optimized deliberate failure | 21 | 1 | 0 | 1 | expected rejection |

The successful JSON records are byte-identical. All frozen source bytes were compared before and after and are unchanged. No Python `assert` statement is used by the supplied checker; unittest assertions remain active under optimization.

These are **method counts**, not theorem counts. Tests 11–16 check selected rational polynomial ideal, conormal, unit and graded formulas. Test 17 checks a two-variable mixed Jacobian and a one-variable multiplicity residue using real coefficients. It does not exercise general nonreal conjugation, all cochain signs, arbitrary orders, or any infinite analytic claim. Tests 3–10 are declared phase/Gaussian/matrix fixtures, not actual certified zero packets. Test 5's final scalar moment expression and test 4's arithmetic mass rearrangements are finite calibration records, not independent quadrature certificates. The general assertions below have direct proofs.

## 3. Exact original rings, sequence and conormal coefficients

Retain a monic polynomial

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad d=\deg h>0,
\]

with every selected zero and multiplicity. Let

\[
\mathcal P=\mathbb C[s_1,\ldots,s_k],\quad h_i=h(s_i),\quad
I=(h_1,\ldots,h_k),\quad E=\mathcal P/I,\quad A=\mathcal P/I^2.
\]

Here `A` is used for the thickened ring in this report, and is not the paper's arithmetic multiplication matrix. Quotienting gives the exact sequence of complex vector spaces and the square-zero algebra extension

\[
0\longrightarrow I/I^2\xrightarrow{\mathrm{incl}}A
\xrightarrow{\pi}E\longrightarrow0.
\]

The kernel assertion is literal: a polynomial class in `A` maps to zero exactly when its polynomial lies in `I`. A product of two such kernel classes lies in `I²`, hence is zero in `A`.

Here is the full division argument used in source (5.3). Every monomial `s_i^N` can be written by division of its exponent `N=dq+a`, `0≤a<d`, and repeated monic division by `h_i`, as a linear combination of `s_i^a h_i^q`. Each subtraction decreases the degree, so it terminates. The leading monomial of `s_i^a h_i^q` is `s_i^{a+dq}` with coefficient one. Distinct pairs `(a,q)` have distinct leading degrees. Choosing the greatest leading degree in any finite linear dependence proves independence. Applying this argument in the ordered variables proves the unique finite expansion

\[
P=\sum_{\substack{0\le a_i<d\\\alpha\in\mathbb N^k}}
c_{a,\alpha}s^a h^\alpha.
\]

Equivalently, `P` is free over `C[h_1,...,h_k]` on the basis `s^a`, `0≤a_i<d`. Under this free-module identification, `I^r` has exactly the terms with `|α|≥r`. Thus

\[
I^r/I^{r+1}=\bigoplus_{|\alpha|=r}E[h^\alpha].
\]

The coefficient lifts do not alter their classes: replacing a lift by an element of `I` moves `h^α` times that difference into `I^{r+1}`. This proves the exact `E`-linear isomorphism

\[
\iota:E^k\xrightarrow{\sim}I/I^2,\qquad
(a_i)\longmapsto\left[\sum_i h_i\widetilde a_i\right]_{I^2},
\]

and the algebra isomorphism

\[
\operatorname{gr}_I\mathcal P\simeq E[\eta_1,\ldots,\eta_k],
\qquad \eta_i\longmapsto[h_i].
\]

In particular `rank_E(I^r/I^{r+1})=binom(r+k−1,k−1)` and `dim_C A=(k+1)d^k`. This is the rank of the **graded module**, not of a derivative image.

The zero-dimensional seed `h=1` must be handled separately: `I=P`, all displayed quotients and conormal modules vanish, and their maps are the zero maps. The positive-degree freeness proof above is not asserted for the degree-zero polynomial `1`. This repairs the overly broad applicability sentence at source NOTE lines 131–133 without changing the analytic theta-seed calculation.

## 4. Derivative, cotangent presentation, and local coefficient correction

Define

\[
\partial=\partial_S^{\mathrm{rel}}=\frac1k\sum_{i=1}^k\partial_{s_i},
\qquad S=\sum_i s_i.
\]

The factor `1/k` makes `∂S=1` and `∂(s_i−S/k)=0`. For any product of `r+1` elements of `I`, the product rule differentiates one factor and leaves at least `r` factors from `I`; multiplication by an arbitrary polynomial does not alter this conclusion. Hence `∂I^{r+1}⊆I^r` and there is a well-defined complex-linear map

\[
\partial_r:\mathcal P/I^{r+1}\longrightarrow\mathcal P/I^r,
\qquad[P]\longmapsto[\partial P],\quad r\ge1.
\]

For `r=1`, write `δ=∂_1`. The polynomial product rule proves

\[
\delta(ab)=\pi(a)\delta(b)+\pi(b)\delta(a),\qquad\delta(S)=1.
\]

On the retained conormal coefficients,

\[
\delta\iota(a_i)=\frac1k\sum_i[h_i']_I a_i.
\]

The omitted-looking terms have their exact destination:

\[
\partial\sum_i h_i\widetilde a_i
=\frac1k\sum_i h_i'\widetilde a_i+\sum_i h_i\partial\widetilde a_i;
\]

the final sum lies in `I`. Therefore the restriction is `E`-linear. The whole map `δ:A→E` is a derivation along `π`, not an `E`-linear endomorphism.

The full conormal differential sends the basis class `[h_i]` to `h_i' ds_i`, so it is the diagonal map

\[
d_I:I/I^2\longrightarrow\bigoplus_iE\,ds_i,
\qquad(a_i)\longmapsto\sum_i h_i'a_i\,ds_i.
\]

Contraction `Σb_i ds_i↦k^{-1}Σb_i` gives exactly `δ|_{I/I²}`. The sequence `h_1,...,h_k` is regular: after quotienting by its first `i−1` elements, the next polynomial is monic in the unused variable `s_i`, so multiplying a nonzero polynomial by it retains the nonzero leading coefficient. The Koszul complex is a resolution by induction: adjoining each monic non-zero-divisor forms the mapping cone of its injective multiplication on the preceding degree-zero quotient, so the cone has only that next quotient in degree zero. Taking the differentials of the polynomial variables and of the degree-minus-one Koszul generators gives the displayed two-term cotangent complex, in cohomological degrees `−1,0`, with differential `d(h_i)=h_i' ds_i`. This also identifies the map to universal differentials before contraction. The standard classification agrees with the [naive cotangent presentation, Stacks 00S0](https://stacks.math.columbia.edu/tag/00S0) and the [complete-intersection result, Stacks 08SH](https://stacks.math.columbia.edu/tag/08SH), both opened for this audit. The packet-specific matrices and division proof above supply the concrete calculation.

**Correction of the source's local sentence.** NOTE lines 476–477 and research note line 266 say the conormal multiplication “detects the `z^{m−1}` coefficient.” If the local polynomial is `h=z^m q(z)`, `q(0)≠0`, and the input coefficient is `a=Σ_{j=0}^{m−1}a_jz^j`, the exact calculation is

\[
[h'a]_{z^m}
=[(m z^{m-1}q+z^m q')a]_{z^m}
=m q(0)a_0 z^{m-1}.
\]

It reads the input's **constant** coefficient and outputs the top surviving coefficient with its retained factor and local unit. For `m=2,q=1`, input `a=z` has a nonzero top coefficient and maps to zero; input `a=1` maps to `2z`. Thus the original sentence's input/output wording must be repaired. Its rank formula is correct.

For a full ordered local block

\[
E_{\boldsymbol\rho}=\mathbb C[z_1,\ldots,z_k]/(z_i^{m_i}),
\]

the image ideal of the conormal row is

\[
J_\partial=(h_1',\ldots,h_k')=(z_1^{m_1-1},\ldots,z_k^{m_k-1}).
\]

Each multiplier `m_i q_i(0)/k` is nonzero. The quotient by this ideal has the basis `z^a` with `0≤a_i<m_i−1`, with the empty-basis convention when any `m_i=1`. Writing `D_loc=Πm_i` and `Q_loc=Π(m_i−1)`,

\[
\dim J_\partial=D_{\rm loc}-Q_{\rm loc},\qquad
\dim\ker(\delta|_{I/I^2})=(k-1)D_{\rm loc}+Q_{\rm loc}.
\]

Globally, if `r_0` is the number of distinct roots of the original `h`, summing the ordered local blocks gives

\[
\dim J_\partial=d^k-(d-r_0)^k,\qquad
\dim\ker(\delta|_{I/I^2})=(k-1)d^k+(d-r_0)^k.
\]

These refer to the **full conormal row**. They do not state the rank of the different finite-section Weyl correction obtained by feeding only the particular section coefficients `ell_i` into that row. The latter is being developed by the root's finite-Weyl lane and has its own exact source map.

## 5. Full unit, original theta map, and residue trace

Retain `g=2xi`, `v_h=g/h`, and `U=Π_i v_h(s_i)`. The finite Taylor class `Uhat` in `A` is well-defined without replacing a coefficient. One explicit construction is univariate Hermite interpolation of each factor modulo `h_i²`, followed by multiplication and the ring quotient

\[
\mathcal P/(h_1^2,\ldots,h_k^2)\longrightarrow\mathcal P/I^2.
\]

The map exists because `(h_i²)_i⊆I²`. It retains the distinction between the separate doubled jets and the first **ideal-power** thickening; the latter additionally kills each mixed relation `h_i h_j`. Any two univariate interpolants differ by `h_i²` times a holomorphic factor and hence give the same class. Locally this quotient is finite dimensional, so finite Taylor data suffice.

The image `U` in `E` is invertible because `v_h` is nonzero at every selected zero, with its full exact multiplicity already removed by `h`. A lift of its inverse satisfies `Uhat Vhat=1+n`, where `n∈I/I²` and `n²=0`. Thus `Vhat(1−n)` is an explicit inverse to `Uhat`. This proves invertibility with the original unit retained.

Define `Jhat(P)=Uhat[P]_{I²}`, `J(P)=U[P]_I`, and

\[
\beta_h=U^{-1}\delta\widehat U.
\]

The exact typed conjugation is

\[
U^{-1}\delta M_{\widehat U}
=\delta+M_{\beta_h}\pi:A\longrightarrow E.
\]

It follows directly from `δ(Uhat a)=Uδ(a)+(δUhat)π(a)`. On actual source functions the Mellin transform of `L_k T_h^(k)P`, where `L_k=k^{-1}Σ log x_i`, is `∂(UP)`. Consequently

\[
J^{(k)}\mathscr L_k\mathcal T_h^{(k)}P
=\delta\widehat{\mathcal J}P
=\mathcal J(\partial P)+\beta_h\mathcal JP,
\qquad
\beta_h=\frac1k\sum_i j\!\left(\frac{v_h'}{v_h}\right)(s_i).
\]

For the original relation `P=Σh_iP_i`, the second term has factor `[P]_I=0` and the exact surviving output is

\[
J^{(k)}\mathscr L_k\mathcal T_h^{(k)}P
=\frac Uk\sum_i h_i'[P_i]_I.
\]

The original identity `g'=v_hh'+v_h'h` proves `[v_hh']_h=[g']_h`; all other `v_h` factors remain. No scalar unit has been assigned one.

For coordinatewise reflection `f†(s)=overline(f(1−bar(s)))`, the packet hypotheses give `h†=(−1)^d h`, `v_h†=(−1)^d v_h`, and `U†=(−1)^{kd}U`. Direct differentiation gives `(∂f)†=−∂(f†)`. It follows that

\[
\beta_h^\dagger=-\beta_h.
\]

This uses reflected conjugation, not a suppressed ordinary transpose or an assumed reality condition on arbitrary coefficients.

The one-variable source equation is obtained before quotienting:

\[
\mathcal M(\log x\,\Theta\phi)=g'H_\phi+gH_\phi',\qquad
J_h(\log x\,\Theta\phi)=j_h(g')j_h(H_\phi).
\]

For `phi=P(D)phi_*`, the actual source has `H_phi=P`, hence all polynomial remainders occur. With the inherited residue convention

\[
\mathscr R_Z(f,b)=\sum_{\rho\in Z}\operatorname{Res}_{s=\rho}
\frac{f^\dagger(s)b(s)}{g(s)}\,ds,
\]

the pairing is well-defined on the complete remainder classes: changing either representative by `h` times a holomorphic function changes the integrand by a holomorphic function, since `g/h` is a unit at the packet and reflection preserves its ideal. Locally `g=z^{m_\rho}u_\rho(z)` with `u_\rho(0)≠0`, so

\[
\frac{g'}g=\frac{m_\rho}{z}+\frac{u_\rho'}{u_\rho}.
\]

The second term is holomorphic. Therefore

\[
\mathscr R_Z\bigl(f,J_h(\log x\,\Theta(P(D)\phi_*))\bigr)
=\sum_\rho m_\rho\overline{f(1-\bar\rho)}P(\rho).
\]

On each local monomial basis, multiplication by `f†P` has constant diagonal `f†(rho)P(rho)` and all nonconstant coefficients strictly raise local degree. Its trace is precisely the displayed sum with all multiplicities. This proves the multiplication-trace interpretation; it is not a positivity assertion.

The pasted transcript's global map also has an exact proof. Put `nu=q(log x)Theta:V→Q`, where `q:B→Q` is the original quotient and `D=−x∂x`. Since `DTheta=ThetaD`, `[D,log x]=−1`, and `qTheta=0`,

\[
D_Q\nu-\nu D_V=q[D,\log x]\Theta=-q\Theta=0.
\]

For dilations `(Lambda_aF)(x)=F(ax)`, `a>0`, one has `(log x)Lambda_a−Lambda_a(log x)=−log(a)Lambda_a`. The additional term again factors through `qTheta`, so `nu` intertwines the original dilations. Its finite jet on polynomial source vectors has image `(g')⊂E_h`, of dimension `r_0`, with the retained local output `m_rho u_rho(0)a_0 z^{m_rho−1}`. The original map is `V→Q`; no logarithmic endomorphism of `Q` has been introduced.

## 6. Every derivative layer and the ordered mixed formula

For `|α|=r≥1`, the exact product rule is

\[
\partial(h^\alpha P)
=\frac1k\sum_i\alpha_i h_i'h^{\alpha-e_i}P+h^\alpha\partial P.
\]

The last term lies in `I^r`. Its destination in the associated graded is therefore zero **in the stated quotient** `I^{r−1}/I^r`. The remaining terms prove

\[
\operatorname{gr}_{-1}(\partial)
=\frac1k\sum_i h_i'\partial_{\eta_i}.
\]

The quotient maps commute with these derivative maps wherever the levels match, because all compositions send a representative polynomial to its same derivative in the same final quotient. This proves the source's all-order assertion without extrapolation from test 16's finite examples.

For the ordered mixed derivative, every coordinate derivative occurs exactly once. In expanding

\[
\partial_{s_1}\cdots\partial_{s_k}\left(UP\prod_i h_i\right),
\]

the only term without an undifferentiated `h_i` is the term in which each `partial_i` differentiates its own `h_i`. All other terms lie in the original ideal `I`. Thus

\[
\left[\partial_{s_1}\cdots\partial_{s_k}
\left(UP\prod_i h_i\right)\right]_I
=\left[UP\prod_i h_i'\right]_I
=\left[P\prod_i g'(s_i)\right]_I.
\]

There is no factorial and no `k^{−k}`: this is the product of the individual derivatives, not `partial^k`. Under Mellin transformation it is multiplication by `Π_i log x_i`. The ordered iterated residue with `ds_1∧...∧ds_k` gives

\[
\sum_{\boldsymbol\rho}\left(\prod_i m_{\rho_i}\right)
f^\dagger(\boldsymbol\rho)P(\boldsymbol\rho),
\]

because the same local logarithmic-residue computation applies in the specified variable order. It is the ordinary multiplication trace on the full product local algebra. The cochain summand in degree `k` separately contributes the supertrace factor `(−1)^k`; this factor is not merged with the ordinary residue formula.

For the original primitive of `h_iP_i`, the preceding `i−1` factors have cochain degree one, so the product differential supplies `(−1)^{i−1}`. The primitive itself has that same prefactor, making the resulting boundary coefficient positive. The coefficient class `[P_i]_I` in the conormal module records that boundary with both signs retained. Higher Koszul syzygies remain part of the original complex.

## 7. New exact ring morphism joining the quotient and derivative

The source gives the quotient ring map `pi` and a different, complex-linear derivative map `delta`. Their exact ring-level relation is the following additional continuation, independently reviewed in this lane.

Introduce a specified dual-number variable `epsilon` and set

\[
B_\epsilon=E[\epsilon]/(\epsilon^2),\qquad
\Phi:A\longrightarrow B_\epsilon,
\quad\Phi(a)=\pi(a)+\epsilon\delta(a).
\]

Then `Phi` is a unital complex-algebra homomorphism. Additivity and complex scalar preservation follow from the definitions. Also `delta(1)=0`, so `Phi(1)=1`. Finally

\[
\begin{aligned}
\Phi(a)\Phi(b)
&=\pi(a)\pi(b)+\epsilon\bigl(\pi(a)\delta(b)+\pi(b)\delta(a)\bigr)\\
&=\pi(ab)+\epsilon\delta(ab)=\Phi(ab).
\end{aligned}
\]

The exact kernel is

\[
\ker\Phi
=\iota\left\{(a_i)\in E^k:\frac1k\sum_i h_i'a_i=0\right\}.
\]

Indeed the two dual-number coefficients vanish exactly when `pi(a)=delta(a)=0`. The first condition places `a` in the retained conormal module and the second imposes the displayed row. This kernel is an ideal in `A`, since multiplication on its square-zero conormal ideal factors through `pi` and the row kernel is an `E`-submodule.

Put `J_partial=(h_i')⊂E`, retaining this ideal separately from the full-jet map also denoted `J` in the paper. The polynomial derivative induces the complex-linear map

\[
\bar\partial:E\longrightarrow E/J_\partial,
\qquad[P]_I\longmapsto[\partial P]_{I+(h_i')_i}.
\]

This is well-defined because changing `P` by `Σh_iP_i` changes its derivative modulo `I` by `k^{−1}Σh_i'[P_i]_I∈J_partial`. If `lambda:E→E/J_partial` is the quotient map, it satisfies

\[
\bar\partial(qq')=\lambda(q)\bar\partial(q')+
\lambda(q')\bar\partial(q).
\]

The full image ring is precisely

\[
\boxed{\operatorname{im}\Phi
=\{q+\epsilon r\in B_\epsilon:\lambda(r)=\bar\partial(q)\}.}
\]

For the forward inclusion, apply the preceding definitions to any polynomial representative. For the reverse inclusion, let `sigma:E→A` be the **complex-linear** section taking the unique monic remainder in the original variables. The condition on `q+epsilon r` means

\[
r-\delta\sigma(q)=\frac1k\sum_i h_i'a_i
\]

for some `a_i∈E`. For arbitrary polynomial lifts `tilde a_i`, the element

\[
a=\sigma(q)+\left[\sum_i h_i\widetilde a_i\right]_{I^2}
\]

then has `Phi(a)=q+epsilon r`. The factor `1/k` is kept in choosing the coefficients. Different choices change `a` by exactly the kernel computed above. If another complex-linear section is chosen, its difference from `sigma` lies in `I/I²`, and the derivative difference lies in `J_partial`; hence the image description is independent of the section. No ring splitting is asserted.

The image condition defines a subalgebra directly: the epsilon coefficient in a product is `qr'+q'r`, and its image under `lambda` equals `bar partial(qq')` by the displayed derivation rule. Projection to `q` gives the square-zero extension

\[
0\longrightarrow\epsilon J_\partial\longrightarrow
\operatorname{im}\Phi\longrightarrow E\longrightarrow0.
\]

The exact complex-linear map

\[
F:B_\epsilon\longrightarrow E/J_\partial,
\qquad F(q+\epsilon r)=\lambda(r)-\bar\partial(q)
\]

is onto, because `F(epsilon r)=lambda(r)`, and its kernel is `im Phi`. Thus the complete vector-space sequence is

\[
0\longrightarrow\ker\Phi\longrightarrow A
\xrightarrow{\Phi}B_\epsilon\xrightarrow{F}E/J_\partial
\longrightarrow0.
\]

This cokernel is a complex-vector-space cokernel. The image contains `1` and may be proper, so it is not an ideal by which `B_epsilon` is being quotiented as a ring. Nor is `F` generally `E`-linear under the standard `E`-module structure.

On a local ordered block, all dimensions and retained directions are

\[
\dim\ker\Phi=(k-1)D_{\rm loc}+Q_{\rm loc},\quad
\dim\operatorname{im}\Phi=2D_{\rm loc}-Q_{\rm loc},\quad
\dim\operatorname{coker}\Phi=Q_{\rm loc}.
\]

Globally replace `D_loc` by `d^k` and `Q_loc` by `(d−r_0)^k`. These identities follow from the proven conormal row image and the exact sequence; no relation direction has been removed merely to obtain a ring morphism.

Reflection extends to `B_epsilon` by the exact rule

\[
(q+\epsilon r)^\dagger=q^\dagger-\epsilon r^\dagger,
\qquad\epsilon^\dagger=-\epsilon.
\]

Since `delta(a†)=−delta(a)†`, one obtains `Phi(a†)=Phi(a)†`. This sign is required by the original reflected derivative; it is not a free choice of a positive involution.

The original arithmetic unit also remains visible:

\[
\Phi(\widehat U)=U+\epsilon\delta\widehat U
=U(1+\epsilon\beta_h),\qquad
\Phi(\widehat U)^{-1}=U^{-1}(1-\epsilon\beta_h).
\]

The equality `Phi(Uhat a)=Phi(Uhat)Phi(a)` transports the arithmetic product derivative through this same ring map.

Finally, let `pr_0,pr_epsilon:B_epsilon→E` be coefficient extraction. Then

\[
\pi=\operatorname{pr}_0\Phi,\qquad
\delta=\operatorname{pr}_\epsilon\Phi.
\]

The first extraction is a ring map; the second is complex-linear. Applying the original split functor produces the exact typed diagram

\[
G(A)\xrightarrow{G(\Phi)}G(B_\epsilon),\qquad
G(\pi)=G(\operatorname{pr}_0)G(\Phi),\qquad
\delta^\tau=(\operatorname{pr}_\epsilon)^\tau G(\Phi).
\]

For a complex-linear map `T`, its split lift sends `tau→tau` and `v^bullet→(Tv)^bullet`. It preserves addition by linearity for two active arguments and by the external-zero law if either argument is tau. It preserves the `G(C)` action because an active scalar acts by the original complex scalar and the absent scalar sends both sides to tau. Consequently it sends active zero to active zero. `G(Phi)` additionally preserves products because `Phi` is a ring map. Thus the derivative's failure to be a unital ring map is connected to an explicitly proved ring morphism, with its exact kernel and image retained.

## 8. Display corrections and integration handoff

1. Correct NOTE 476–477 / research note 266 by the exact local coefficient calculation in section 4 above.
2. Make NOTE 557 / research note 318 explicitly say `rank_E(I^r/I^{r+1})`, not derivative-image rank.
3. Scope the positive-degree monic freeness proof to `d>0`; state the `h=1` zero-quotient case separately.
4. In NOTE (8.2), lines 666–669 / research note 388–391, the bare derivative arrow has codomain `Add(graph)`, not the ordered-pair graph itself. Replace it by the derivative followed by the actual pair map `Z→(Pi_u Z,(1−Pi_u)Z)`, restricted to the derivative image. The source's equations (4.9)–(4.11) already prove this lift and its inverse by addition; no analytic hypothesis changes.

The full `Phi` proof, image/kernel formulas, reflection sign, and global scaling-equivariant source map were sent to the root and `arithmetic_moment_exact` for the cumulative finite-Weyl chapter. The root owns source-author/tandem messages and global integration. This lane did not modify the public draft or frozen delivered sources.

Next integration action: use the full original local note as the proof witness, carry these exact display corrections into the authored cumulative text, and keep the published shorter PR note separately linked. The analytic lane must preserve the original derivative-to-graph map when connecting its contraction to the finite packet metric; the source's scalar Fisher estimate by itself supplies no bound for the complete arithmetic weight form.

## 9. Reproduction

With Python and the declared SymPy 1.14.0 available, the driver takes explicit source/archive/output paths. On the audited machine the exact dependency setting was:

```powershell
$env:PYTHONPATH = 'workspace:\work\kernel_layer_replay_dependencies_20260912'
& 'runtime:research-python\python.exe' -B 'package:\scripts\replay_sum_connection_delivery.py' --source 'package:\sources\web_sum_connection_delivery\Tau_Sum_Connection_Control' --archive 'corpus:Chatnotes\CHat translates and clean\Noether Multilingual\Tau_Sum_Connection_Control_2026-09-12.zip' --output 'package:\checks\sum_connection_delivery_replay' --remote
```

The driver is portable: it does not hard-code those paths and refuses to run with another SymPy version. Its output includes runtime, commands, all source/member hashes, fresh logs, negative-control results, and pinned remote tree/blob evidence. For a new replay use a fresh output directory to keep earlier evidence immutable.
