# Exact review of the independent coefficient-face attachment

Scope: review and edit proposals only. The main coordinator owns the new attachment and TO source. No TO or shared manuscript source is edited here. This review is an addition to the existing original-source logbook and preserves the distinction between constructing the represented object and proving an arithmetic estimate.

Delegation retained verbatim:

> Important actual-source omission found by main coordinator: read complete work/split_support_actual_control_audit_20260913.md MSA1–27 and work/mixed_support_full_carrier_morphisms_subreview_20260913.md, plus current TO lines83–128 and originalPS. TOgenerators do not explicitly adjoin PS D_(E_Z,n)=G(E_Z)^n with ALL independent coefficient faces; G(E_Z^n) onlyempty/full. Need bounded rigorous review of exact attachment to our ONE represented object, retaining separate originallegmask index. Mainiswritingtypedattachment so don'tduplicate it. Identify precise TOgenerator/CAU adjustments and prove maptransport naturally allfaces/full-unitsections/cochainboundary as needed, give root edittext. RootreadsMSA/incomingmixed-sheaf comparison and handlescumulativeartifact. Mathematical claim248editioncomplete mustbequalified untilfaceextensionintegrated. Do not editTOownedroot ormain sources.

## Complete reading and exact omission

Read all of `work/split_support_actual_control_audit_20260913.md` (MSA1–27, including its conclusion/source pins), all of `work/mixed_support_full_carrier_morphisms_subreview_20260913.md`, and all 342 lines of `shared_thread_audit/segment16_28/PACKET_SURVIVAL.tex`. Rechecked current TO generator and pointed-lift definitions, CAU's complete source-label paragraph, and AG6–13 full-unit source sections and divisor maps. The complete mixed-carrier audit itself cites the original V5 and mixed-ledger proofs; this review does not claim a separate complete rereading of those two much larger sources.

The omission is real and localizable: TO's displayed generating category and CAU's `(W,S)` labels have not explicitly adjoined `D_{E_h,n}=G(E_h)^n`, its independent coefficient-face diagram, and its synchronization/localization arrows. A single split lift `G(E_h^n)` contains exactly the empty and full coefficient masks. The CAU leg mask `S⊆{+,-}` is an independent label, not the coefficient mask `A⊆I_n`, where `I_n={0,…,n−1}`. Keeping one index cannot stand for keeping the other.

The former completeness assertion about the 248-page edition must therefore be scoped to the stated vertices until the new attachment has actually been integrated and checked. This is an integration omission despite the original PS mathematics already being present in the repository.

## Precise TO and CAU changes

The following is proposed insertion text at TO's generator paragraph, immediately after the AG/CAU observation generators. It is to be joined to the main coordinator's explicit formulas and labels, not inserted as an unproved reference:

```tex
For every actual full-order packet h, every n>=1, and every
coefficient mask A subset I_n, also adjoin the original PS face
E_h[A], its independent mixed carrier D_{E_h,n}=G(E_h)^n,
the negacyclic multiplication with coefficient variable t and
relation t^n+1=0, the amplitude and complete-mask maps, the
synchronization/localization map, and its specified nonunital
section. Adjoin their coefficientwise original source, quotient,
full-unit packet-section, divisor, arithmetic-action and integral
coefficient-Frobenius arrows, with every face transition and
boundary homotopy proved in the mixed-face attachment. The index A
is independent of the source-leg index S of CAU. Common vertices
are identified by these explicit coordinate maps. All faces remain
vertices of the represented category; no colimit over their
support-increasing arrows is taken.
```

At TO's general pointed-lift paragraph, add this category distinction:

```tex
The pointed lift applies to maps with fixed coefficient-mask
transport, including coordinatewise linear maps. The face-filling
arrow A->B is instead the specified map between labelled additive
face groups. It sends the face zero e_A to e_B; for A empty and
B nonempty it sends the all-absent coefficient tuple to e_B.
It is therefore not declared to preserve the global absent point.
Both types are arrows in the represented underlying-set category,
with their different structural types retained.
```

CAU's subsection title “All proper source and support fibres” should read “All proper source and original leg-support fibres”. Its first paragraph should state explicitly that `S` indexes the two original source legs. After CAU.29's fibre discussion add:

```tex
These are the original leg-mask fibres. For the independent PS
coefficient slots, the additional index is A subset I_n; it is
retained jointly with (W,S). On coefficient face A the complex is
the direct sum of A copies of the specified original leg complex.
All its maps act in each active coordinate. The coefficient-face
assembly and synchronization are the separately specified mixed
attachment, not the synchronized lift G of that direct sum.
```

No change to CAU's existing exact Mellin or kernel proofs is needed. They extend coefficientwise by the proof below. The phrase “All” must not be allowed to assert the stronger mixed claim before those extra vertices are attached.

## Exact transport on all faces

Let `M` be any one of the actual coefficient modules in the programme and define the face group

\[
M[A]=\bigoplus_{i\in A}M.
\]

Identify its labelled elements with the coefficient tuple having `m_i^bullet` in each active slot and `tau` in each inactive slot. Thus the labelled zero of this additive group is the tuple with supported zero exactly in `A`. The empty face has one element, the wholly absent coefficient tuple. For `A⊆B`, define `z_A^B:M[A]→M[B]` by zero insertion. It is linear, composes literally, and sends `e_A` to `e_B` under the labelled carrier identification. In particular these are *face-filling arrows*, not literal inclusions of fixed-mask subsets of the independent carrier. The direct sum groups have a terminal full-face diagram, whose colimit is `M^n`; taking that colimit would discard the separately labelled faces. The mixed carrier is instead their disjoint union with the labels retained.

For a linear map `f:M→N`, define `f[A]` by applying `f` in each active coordinate. For each coordinate in `B`, both composites in

\[
f[B]z_A^B=z_A^Bf[A]
\]

either equal `f(m_i)` when `i∈A`, or equal zero when `i∈B\A`. This proves the equality at every coordinate, hence its naturality for every face, including the empty face. The independent pointed map

\[
\prod_{i\in I_n}G(f):\prod_iG(M)\longrightarrow\prod_iG(N)
\]

preserves the coefficient mask exactly, including when a nonzero amplitude lies in `ker f`: the result is supported zero in the same slot. On face `A`, its supported-zero fibre is `(ker f)^A`. This proof applies to the original `q`, Mellin jets, `s_h`, `sigma_h`, `beta`, `j`, and every linear divisor map with its actual scalar category.

The independent coefficient index may be paired with the separate original index `(W,S)`. On that vertex use

\[
C_{W,S}[A]=\bigoplus_{i\in A} C_{W,S}.
\]

Its differential acts independently in each active coordinate. Zero insertion therefore commutes with both cochain differentials, and source/leg transition arrows commute with zero insertion by the preceding coordinate proof. For the full source, the original cohomology is

\[
H^1(C_{V,S}[A])=Q^A,
\]

while its degree-zero group is `V^A` for the joint leg mask and zero for a one-leg mask. The original diagonal and the independent coefficient slots are both retained. For proper `W`, the exact transition kernel is `(V/W)^A`, because finite direct sums preserve the original exact sequence CAU.28. Balancing gives the same statement at every analytic stalk by its proved flatness.

On the arithmetic subcomplex `C_U[A]=[V^A→B_U^A]`, the exact sequence is

\[
0\longrightarrow V^A\xrightarrow{\Theta^A}\mathscr B_U^A
\xrightarrow{q^A}(T_UQ)^A\longrightarrow0.
\]

Indeed every coordinate has the original exact sequence AG3. A vector in the kernel has a unique coordinatewise preimage under the injective `Theta`. Thus, within the fixed coefficient face, the boundary relation is exactly `(Theta V)^A`; taking the internal quotient changes amplitudes without deleting any slot.

The split differential is not an ordinary vector-space differential on the disjoint mixed carrier: its square lands at `e_A`, not at the wholly absent point. Even a zero linear term has independent split carrier `G(0)^n={tau,e}^n`. The correct cochain calculation is the original linear complex on every face and then its supported-zero equalizer/boundary coequalizer. This prevents replacing the face skeleton by one zero object at degrees outside the ordinary complex.

## Full-unit sections and the actual boundary homotopy

Retain AG6–8 with the original spectral variable `x`:

\[
v_h=g/h,\quad\upsilon_h=j_hv_h,\quad
\varepsilon_h=\upsilon_h^{-1},\quad
F_h=S_h\Theta\phi_*,\quad
s_hu=r_h(\varepsilon_hu)(D)F_h,
\]

\[
J_hs_h=1,\qquad q s_h=\sigma_h,\qquad
Ds_h-s_hM_x=\Theta\phi_*\ell_h,
\quad\ell_h(u)=[x^{d_h-1}]r_h(\varepsilon_hu).
\]

Here `h` is full-order at its retained centres, so `v_h` is a local unit at precisely those centres. Every coordinate of `s_h[A]` uses that same complete inverse unit, not only its value at a centre. The identities become

\[
J_h[A]s_h[A]=1,\quad q[A]s_h[A]=\sigma_h[A],
\]

\[
D[A]s_h[A]-s_h[A]M_x[A]
=\Theta[A]B_h[A],\qquad
B_h[A](u_i)=(\phi_*\ell_h(u_i))_{i\in A}.
\]

Both sides agree in every coordinate by AG8. The maps `B_h[A]` commute with every zero insertion because they are linear. As cochain maps from `E_h[A]` concentrated in degree one to `C_U[A]`, the last identity is the exact cochain homotopy between the two Euler composites: `B_h[A]` has degree minus one and `dB_h[A]` is their difference. Its quotient is zero, proving equivariance of `sigma_h[A]` on every independently supported face. Nothing asserts that `s_h` is multiplicative or `A`-linear before this boundary is accounted for.

For full packet divisors `h|H`, use AG10–12's exact maps `pi_{Hh}`, `iota_{hH}` and complete-unit identity

\[
s_H\iota_{hH}=s_h,\qquad \sigma_H\iota_{hH}=\sigma_h,
\qquad \ell_H\iota_{hH}=\ell_h.
\]

Applying them in each coordinate proves the same identities on every face and makes every divisor/face square commute. This retains the raw numerator map `mu_{H/h}=iota M_{[H/h]_h}` as a different arrow; it is not silently substituted for arithmetic zero extension. The induced split map `G(iota)^n` preserves all coefficient masks. It is not unital: its original unit maps to `(e_{hH}^bullet,tau,…,tau)`, where `e_{hH}` is the old-packet CRT idempotent.

For arbitrary `a>0`, the quotient scaling intertwining also has a concrete source homotopy. Write `L=log a`, `A_t=exp(tM_x)` and keep the original dilation `R_{exp(t)}`. Define the original `V`-valued integral

\[
B_{h,a}(u)=\int_0^L
R_{e^{L-t}}\phi_*\,\ell_h(A_tu)\,dt.
\]

The finite interval is oriented when `L<0`. The integrand is a smooth curve in the original Schwartz space, with the two original zero moments; its integral belongs to `V`. Differentiating `R_{e^{L-t}}s_hA_tu` gives

\[
-R_{e^{L-t}}(Ds_h-s_hM_x)A_tu.
\]

Integrating, using `Theta R=R Theta`, proves exactly

\[
R_as_h-s_hA_L=\Theta B_{h,a}.
\]

Its coefficientwise version commutes with all face insertions. This supplies a full source-level scaling homotopy where a mere claim that the section intertwines dilation would be false. On `sigma_h` the boundary vanishes and the original full nilpotent action survives.

There is also a strict balanced realization of the section's cohomology map. **Do not write `O tensor_A s_h`: that tensor arrow is not defined because the displayed section is not A-linear.** Instead retain

\[
e_h=r_h(\varepsilon_h),\quad
F'_h=e_h(D)F_h,\quad \phi'_h=e_h(D)\phi_*.
\]

The two-term free source `P_h=[A --h→ A]` in degrees zero and one has the actual A-linear cochain map

\[
P_h\longrightarrow C_U,\qquad
P\longmapsto P(D)\phi'_h\text{ in degree zero},\quad
P\longmapsto P(D)F'_h\text{ in degree one}.
\]

Indeed `h(D)F'_h=Theta phi'_h`, and all polynomial actions commute. For a polynomial `P`, the exact polynomial

\[
R_h(P)=\frac{P e_h-r_h(\varepsilon_h[P]_h)}h
\]

exists because the numerator has zero h-remainder. It gives

\[
P(D)F'_h-s_h([P]_h)=\Theta(R_h(P)(D)\phi_*).
\]

Thus the induced H1 map is precisely `sigma_h`, retaining the whole inverse unit. This strict chain map, and its direct sum on every coefficient face, can be tensored over A with O. The original finite-dimensional section remains a C-linear observation vertex, with its just-proved boundary homotopy. This gives an exact bridge rather than discarding the non-A-linear section.

These homotopy-to-equivariance assertions concern the original **full source V**. On a proper source `W`, the same target functions still define amplitude maps, but the source correction need not lie in W. Its residual class is precisely the class of `phi_* ell_h(u)` (or `B_{h,a}(u)`) in the retained transition kernel `V/W`, coordinatewise on face A. It cannot be declared an already-zero boundary in `Q_W` unless it is in W. The exact proper-source transition above transports it to the full quotient where it becomes zero. This avoids importing the full-source spectral property into every proper label.

## Mixed multiplication, synchronization, and arithmetic retract: correct types

At the finite algebra observation vertex only, retain PS's negacyclic product with `t^n+1=0`, unit `(1^bullet,tau,…,tau)`, and mask multiplication `A·B=A+B` in `Z/n`. Its support semiring is the cyclic convolution semiring of masks, not the independent *coordinatewise-product* semiring with intersection. The same carrier supports these two distinct multiplications only when they are explicitly marked as different vertices/structures; their formulas are not interchangeable.

The synchronized injection `G(B_n)→D_{E_h,n}` sends a supported polynomial to its fully supported coefficient tuple. It preserves zero, addition and multiplication, but sends `1` to `mathsf E_n=(1^bullet,e,…,e)` rather than the original unit. Synchronization sends every nonempty face to the full face with the same amplitudes. For a coefficientwise linear map `f`, synchronization commutes because both routes preserve the original empty/nonempty status and apply `f` to the same coefficients; this includes a map that kills all amplitudes. In particular divisor maps and original source maps give a natural synchronization square. Under the nonunital divisor injection the synchronization idempotent itself need not map to the larger synchronization idempotent; naturality follows from the coordinate formula, not from that false equality.

PS's retraction on the independent carrier is `r_n^tau` **after synchronization**. Explicitly it sends an empty mask to `tau` and every nonempty mask to the supported constant coefficient `(p(b_0))^bullet`. This is different from raw projection to coordinate zero, which returns `tau` when that coordinate is absent. The PS section and retraction therefore preserve the original arithmetic vector even on faces where synchronization fills previously absent slots; both their exact fibres must remain represented.

The original coefficient Frobenius is a signed permutation of slots. It carries `A` to `qA mod n`, and coordinatewise linear maps commute with that permutation and its signs. Thus the finite section/source/cohomology maps form actual equivariant face diagrams for coefficient Frobenius. Its original arithmetic action acts within every face by the full element `j_h(a^s)`; the preceding boundary calculation supplies its source-level comparison.

The arithmetic action is linear and support-preserving; it is not a negacyclic semiring automorphism. For `a,c>0`, coefficient multiplication and `j_h(a^s)j_h(c^s)=j_h((ac)^s)` give exactly

\[
(A_a b)\star(A_c d)=A_{ac}(b\star d).
\]

In particular the diagonal action with parameter `a` on both inputs has target action `A_{a^2}`, not `A_a`. The additional product arrow therefore carries this actual weight multiplication; an unchanged-target equivariance assertion would be false.

Negacyclic multiplication is a multiplication of the finite observation algebra in cohomological degree zero. Its packet source in `C_U` is in degree one. Consequently a degree-zero chain multiplication `C_U⊗C_U→C_U` cannot realize that product on degree-one cohomology, since the target's degree-two cohomology is zero. The actual AG tensor-DGA product is concatenation into length two and degree two. Keep these two explicitly different arrows; no source pointwise product or silent degree shift is licensed by the finite algebra.

## Local coherent comparison and all tensor faces

Apply CAU.9 coordinatewise. Its inverse takes each active coordinate `alpha_i` to the original function `S_h Theta(r_h(epsilon_h alpha_i)(D)phi_*)`; all active zero values remain supported zero. It gives

\[
(T_UQ)^A\xrightarrow{\sim}
\left(\bigoplus_{\rho\in U:g(\rho)=0}O_\rho/(g)\right)^A.
\]

There is one common finite actual packet containing the union of the finitely many supports of the finitely many active coordinates. Thus the source-level full-unit formula applies to the entire face without changing any coordinate, and the exact divisor identities prove independence of this common packet. Balancing gives `M^A=N_U^A⊕K^A`; the two-leg diagonal is retained separately as described above. Naturality with zero insertion follows from the linear coordinate formula, including at all zero jets.

For finite tensor products, retain the tuple of face labels `(A_1,…,A_k)` together with all original source-leg labels. Tensor each already-proved map over `C` and use the existing Koszul signs. Each equality of maps remains an equality on pure tensors and hence by linearity. Injective source sections stay injective by extending a basis over `C`; the full units are the product of the original coordinate multipliers and all nilpotent jets remain in the actual finite tensor quotient. Tensor closure of the represented category thus supplies all these faces without identifying their labels or replacing them by the single full face.

For each fixed packet, these source attachments are continuous in their actual finite-dimensional/source topologies. If `u=Σu_j e_j` and `F_j=s_h(e_j)`, every original seminorm satisfies `p(s_hu)≤Σ|u_j|p(F_j)`. Mellin jets are continuous by the original integral seminorm bounds, and `J_hs_h=1` supplies the inverse topology on the image. Fixed-face zero insertions are finite linear maps. With the labelled disjoint-union topology, addition and negacyclic multiplication are continuous on each face pair because the output masks are exactly union and cyclic sum and the amplitudes are polynomial maps. These are finite-stage facts. They assert neither a uniform estimate as h or n varies nor continuity of the infinite coherent section `s_U` for inherited subspace topologies; those stronger statements would require their own proved estimates or topology comparison.

## Review verdict

The proposed all-face attachment is rigorous with these types and maps. It is a necessary explicit addition to TO's generators, not a change to the original arithmetic function and not a substitution of a property list for the object. The exact source, coherent, tensor, synchronization, and Frobenius maps already prove its compatibility with the existing anchored assembly. Integration is still required in the main-owned source; no claim of that integration having happened is made in this review.

Independent child `assembly_symmetry_check` read the two complete audits and original PS and checked the critical face-map, supported-complex, and product-degree issues reported above. No shared manuscript files were changed by this subtask.
