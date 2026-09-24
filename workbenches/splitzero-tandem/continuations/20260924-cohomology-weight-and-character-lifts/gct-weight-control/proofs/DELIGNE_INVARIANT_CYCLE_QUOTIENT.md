# Deligne local invariant cycles: the exact quotient, boundary, and lift

Independent mathematical reconstruction, 24 September 2026. Stable proof locators DC0–DC12. The coefficients throughout the proved geometric theorem are rational ℓ-adic coefficients, with ℓ invertible on the geometric base.

## DC0. Source identity, actual coverage, and mathematical scope

The human source is Pierre Deligne, [La conjecture de Weil. II](https://www.numdam.org/item/PMIHES_1980__52__137_0/), Publications mathématiques de l'IHÉS 52 (1980), 137–252, §3.6, printed pp.212–215. Canonical disk-index identifiers are PUBUNIT-3D90B487DBD1CC3A259C6455 and PUBUNIT-574B0214207BBB2BDABCFFF9. The actual reading witness is the current French transcription [S20_FR_record_export.tex](https://www.numdam.org/item/PMIHES_1980__52__137_0/), SHA256 `d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351`. It is a transcription, not Deligne-authored TeX. No PDF was used and no source witness was edited.

The complete §3.6 witness was read at lines2468–2569. The proof of theorem3.6.1 is at lines2477–2553; the complex analytic remark3.6.4 is at lines2561–2569. Its arithmetic-reduction input §1.11.3 was read in the larger complete passage §§1.11.1–1.11.3, lines1491–1552; the local invariant-weight input §1.8.8 was read at lines1254–1281. The supporting programme derivations actually used are [DLM10–DLM11](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/DELIGNE_LOCAL_MONODROMY_RECONSTRUCTION.md), [DW10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/DELIGNE_FUNDAMENTAL_WEIGHT_RECONSTRUCTION.md), [MDB1, MDB4, MDB6, MDB8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/DELIGNE_MIXED_DUALITY_AND_BASE_COMPARISON.md), and the peer calculation [DWR11.3–DWR11.6](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/DELIGNE_WEIGHT_CONTROL_RECONSTRUCTION.md). They are local derivations, not substitutes for the source identity. These local proof links are not claimed to be publication receipts.

This note proves the source theorem for the henselian curve situation specified below. It then calculates the exact quotient, the remaining kernel of specialization, and a stronger splitting after the stated arithmetic reduction. It does not extend the theorem to every mixed-characteristic trait. It does not identify an analytic zeta receiver or a supporting point with this étale cohomology. SectionDC11 gives the actual arithmetic-base maps and the functorial quotient comparison that are available.

## DC1. The geometric objects and the specialization map

Let \(k\) be algebraically closed. Let \(S\) be the spectrum of the henselization of \(k[T]\) at \((T)\), let \(s\) and \(\eta\) be its closed and generic points, and choose a geometric generic point \(\bar\eta\). Let
\[
f:X\longrightarrow S
\tag{DC1.1}
\]
be proper. The hypotheses of Deligne3.6.1 are that \(X\) is essentially smooth over \(k\) and \(X_{\bar\eta}\) is smooth. Fix \(\ell\ne\operatorname{char}k\) and set \(E=\mathbb Q_\ell\); a finite scalar extension or \(\overline{\mathbb Q}_\ell\) can be used when splitting characteristic polynomials. All cohomology groups below use these coefficients. Negative cohomological degrees are zero.

Write
\[
I=\operatorname{Gal}(\bar\eta/\eta),\qquad
V_j=H^j(X_{\bar\eta},E),\qquad
A_i=H^i(X_s,E),\quad B_i=H^i(X_\eta,E),\quad C_i=V_i^I.
\tag{DC1.2}
\]
Proper base change over the strictly henselian trait gives
\[
\operatorname{res}_s:H^i(X,E)\xrightarrow{\sim}A_i.
\tag{DC1.3}
\]
Restriction to the generic fibre and then geometric generic fibre define
\[
\alpha_i:A_i\xrightarrow{\operatorname{res}_s^{-1}}H^i(X,E)
 \longrightarrow B_i,
\qquad
\pi_i:B_i\longrightarrow C_i.
\tag{DC1.4}
\]
The last arrow is the edge map calculated in DC3. The specialization is the exact composite
\[
\operatorname{sp}_i=\pi_i\alpha_i:A_i\longrightarrow C_i
 \hookrightarrow V_i.
\tag{DC1.5}
\]
When its target is written as \(C_i\), the final inclusion is understood separately. This description proves that the image is inertia-invariant; it does not yet prove that every invariant lies in the image.

## DC2. The reduction that makes weights available

Finite presentation and passage to the limit provide a smooth curve \(S'\) over \(k\), a point again denoted \(s\), and a proper model
\[
f':X'\longrightarrow S'
\tag{DC2.1}
\]
whose pullback to the henselization at \(s\) is (DC1.1). The total space \(X'\) is smooth over \(k\), and, after shrinking the curve around \(s\), the restriction of \(f'\) outside \(s\) is smooth. This is the first reduction in the source at line2483. Smoothness of the geometric generic fibre permits this shrinking; it does not assert that \(X_s\) is smooth.

Deligne next uses §1.11.3 to spread and specialize to \(k=\overline{\mathbb F}_q\). The input of that section controls the images of local inertia on finite coefficient quotients while spreading a smooth curve with its boundary and lisse sheaves. In particular it is a specialization argument for the geometric family and its cohomology, not a claim that arbitrary complex numbers have finite-field Frobenius actions. The relevant model and finitely many cohomological degrees then descend to a sufficiently large finite field. The source reduction is the justification for proving surjectivity in that arithmetic model and transferring the theorem back. No arithmetic Frobenius is assigned intrinsically to an arbitrary original \(k\)-model.

Retain the finite-field data
\[
(f'_0:X'_0\to S'_0,s_0)\quad\text{over }\mathbb F_q,\qquad
d_s=[k(s_0):\mathbb F_q],\qquad Q=q^{d_s}.
\tag{DC2.2}
\]
The source can enlarge \(\mathbb F_q\) so that \(s_0\) is rational; here the residue degree is retained instead. Henselization at \(s_0\), followed by the geometric residue-field extension, recovers the situation over \(\overline{\mathbb F}_q\). There is an exact sequence
\[
1\longrightarrow I\longrightarrow G_{\eta_0}
 \longrightarrow G_{k(s_0)}\longrightarrow1.
\tag{DC2.3}
\]
The arithmetic group acts on all maps subsequently constructed. Its inertia subgroup acts trivially on the resulting group-cohomology and special-fibre terms, so the cross of DC4 carries the residual action of \(G_{k(s_0)}\).

The Frobenius used for weights is geometric Frobenius \(F\). On the Tate line it acts by
\[
F|_{E(1)}=Q^{-1},\qquad
F|_{E(r)}=Q^{-r},\qquad
w_Q(\lambda)=2\log_Q|\iota(\lambda)|.
\tag{DC2.4}
\]
Here \(\iota:\overline{\mathbb Q}_\ell\hookrightarrow\mathbb C\) is the embedding used for the weight calculation. Thus duality negates a weight and twist \((r)\) subtracts \(2r\). Arithmetic Frobenius is \(F^{-1}\).

Decompose the smooth total model into connected components and work on each component. Its dimension is constant, and we write
\[
N=\dim X'.
\tag{DC2.5}
\]
This is the dimension of the total smooth model, not the dimension of a generic fibre. A component dominating the curve has generic-fibre dimension \(N-1\). A vertical component has empty generic fibre and zero invariant target; the formulas below still apply to its support cohomology. Components of different dimensions are treated separately and then combined by their finite direct sum. In particular a single \(N\) is never assigned to a union of components of different dimensions.

## DC3. Inertia cohomology and the full coinvariant term

The inertia group has an exact sequence
\[
1\longrightarrow I'\longrightarrow I
 \xrightarrow{t_\ell}\mathbb Z_\ell(1)\longrightarrow1,
\tag{DC3.1}
\]
where \(I'\) has pro-order prime to \(\ell\). It contains wild inertia and the tame factors at primes different from \(\ell\). For a finite continuous \(\mathbb Z/\ell^n[I]\)-module \(M\), the action of \(I'\) factors through a finite group \(G'\) of order prime to \(\ell\). The averaging operator
\[
e_{G'}=|G'|^{-1}\sum_{g\in G'}g
\tag{DC3.2}
\]
is an idempotent with image \(M^{I'}\). Its kernel is generated by \(gm-m\), so the quotient map induces the canonical isomorphism \(M^{I'}\simeq M_{I'}\). Averaging is an exact functor because division by \(|G'|\) is defined modulo \(\ell^n\); consequently \(H^b(I',M)=0\) for \(b>0\). The group extension spectral sequence reduces the computation to \(\mathbb Z_\ell(1)\).

For that procyclic group, choose a topological generator \(\gamma\). The two-term resolution has differential \(\gamma-1\). It computes invariants in degree zero, coinvariants in degree one, and zero in higher degrees. The degree-one identification must also retain its dependence on the generator. Projecting a continuous cocycle to coinvariants gives a homomorphism from \(\mathbb Z_\ell(1)\) to the coinvariant module; replacing \(\gamma\) by \(\gamma^a\), \(a\in\mathbb Z_\ell^\times\), multiplies evaluation by \(a\). The generator-independent target is therefore
\[
\operatorname{Hom}_{\mathbb Z_\ell}(\mathbb Z_\ell(1),M_I)
 =M_I(-1).
\tag{DC3.3}
\]
The resulting formulas, after the finite-coefficient calculation and rational passage, are
\[
H^0(I,V)=V^I,\qquad
H^1(I,V)=V_I(-1),\qquad
H^a(I,V)=0\quad(a\ge2).
\tag{DC3.4}
\]
The notation \(V_I\) denotes the quotient by the span of \(gv-v\), not a choice of complement to invariants.

The Frobenius factor in (DC3.4) can also be checked directly. Arithmetic Frobenius conjugates tame \(\ell\)-inertia by multiplication by \(Q\). Its action on a cocycle is
\[
(F^{-1}\cdot c)(g)=F^{-1}\bigl(c(FgF^{-1})\bigr).
\tag{DC3.5}
\]
Passing to coinvariants therefore gives \(Q^{-1}F^{-1}\) on degree one. Equivalently geometric Frobenius acts on \(V_I(-1)\) by \(QF\). This explicitly retains the \((-1)\) twist and its sign.

The Hochschild–Serre spectral sequence for \(X_\eta\to\eta\) is
\[
E_2^{a,b}=H^a(I,V_b)\Longrightarrow H^{a+b}(X_\eta,E).
\tag{DC3.6}
\]
Only columns \(a=0,1\) survive. No differential between surviving terms is possible after the second page. The resulting two-step filtration gives the canonical short exact sequence
\[
0\longrightarrow K_i:=V_{i-1,I}(-1)
 \xrightarrow{j_i}B_i
 \xrightarrow{\pi_i}C_i:=V_i^I
 \longrightarrow0.
\tag{DC3.7}
\]
The injection is the filtration inclusion and the surjection is the degree-zero edge map, so neither requires choosing a generator or a splitting. At finite coefficients the relevant groups are finite, hence their inverse systems satisfy the Mittag–Leffler condition. This supplies the exact inverse-limit row; tensoring with \(\mathbb Q_\ell\) gives (DC3.7). Possible integral torsion has not been declared absent. Every arrow is equivariant for the residual arithmetic action described in (DC2.3).

## DC4. Localization and duality with the total dimension retained

Put
\[
P_i=H^i_{X_s}(X,E),\qquad O_i=H^{i+1}_{X_s}(X,E).
\tag{DC4.1}
\]
The localization long exact sequence and proper base change give
\[
P_i\xrightarrow{g_i}A_i\xrightarrow{\alpha_i}B_i
 \xrightarrow{\partial_i}O_i\xrightarrow{g_{i+1}}A_{i+1}.
\tag{DC4.2}
\]
This is exact at every displayed internal term. In particular \(\ker\alpha_i=\operatorname{im}g_i\) and \(\ker\partial_i=\operatorname{im}\alpha_i\). The relation \(\operatorname{sp}_i=\pi_i\alpha_i\) and (DC3.7) form Deligne's exact cross.

For completeness, compute its top group without suppressing the support or dualizing factors. Excision for the henselian pullback identifies support cohomology on \(X\) with support cohomology on the finite-type smooth model \(X'\). Let \(u:X_s\hookrightarrow X'\) be the closed immersion, and let \(D_Y=R\mathcal Hom(-,K_Y)\) denote Verdier duality, with \(K_Y=Ra_Y^!E\). Smoothness of the total space of dimension \(N\) gives
\[
K_{X'}=E(N)[2N].
\tag{DC4.3}
\]
Duality for the closed immersion gives
\[
Ru^!E_{X'}
 =D_{X_s}(u^*D_{X'}E_{X'})
 =D_{X_s}E_{X_s}(-N)[-2N].
\tag{DC4.4}
\]
The fibre \(X_s\) is proper over \(k\). Global duality and (DC4.4) therefore yield the complete derived identity
\[
R\Gamma_{X_s}(X,E)
 \simeq R\operatorname{Hom}_E(R\Gamma(X_s,E),E)(-N)[-2N].
\tag{DC4.5}
\]
Over the field \(E\), taking cohomology of the dual complex introduces no additional Ext term. Consequently
\[
H^j_{X_s}(X,E)
 \simeq H^{2N-j}(X_s,E)^\vee(-N),
\tag{DC4.6}
\]
and, at the degree needed in the cross,
\[
O_i\simeq H^{2N-i-1}(X_s,E)^\vee(-N).
\tag{DC4.7}
\]
The pairing associated with (DC4.6) takes values in \(E(-N)\). No trivialization of that Tate line has been made. If geometric Frobenius has eigenvalue \(\lambda\) on the cohomology on the right before duality, the resulting eigenvalue in support cohomology is
\[
Q^N/\lambda;
\quad\text{at the operator level it is }Q^N(F^{-1})^{\mathsf t}.
\tag{DC4.8}
\]
This keeps the inverse, transpose, Tate factor, and any nontrivial Jordan structure. The finite-coefficient and integral versions require their own duality statements; the rational passage here is precisely the passage at which the source removes the torsion complication. No integral specialization-surjectivity theorem is inferred.

## DC5. The exact obstruction before any weight calculation

For the exact cross (DC3.7), (DC4.2), define
\[
\overline O_i=O_i/\partial_i j_i(K_i).
\tag{DC5.1}
\]
For \(c\in C_i\), choose \(b\in B_i\) with \(\pi_i(b)=c\) and put
\[
\operatorname{obs}_i(c)
 =[\partial_i b]\in\overline O_i.
\tag{DC5.2}
\]
If \(b'\) is another lift, exactness gives \(b'-b=j_i(k)\) for some \(k\in K_i\). Their boundaries differ by \(\partial_i j_i(k)\), so (DC5.2) is well-defined. It is linear and Frobenius-equivariant because the defining maps are.

If \(c=\operatorname{sp}_i(a)\), use \(b=\alpha_i(a)\). Localization gives \(\partial_i b=0\), so \(\operatorname{obs}_i(c)=0\). Conversely, if \(\operatorname{obs}_i(c)=0\), choose \(b\) lifting \(c\) and \(k\) such that \(\partial_i b=\partial_i j_i(k)\). Then \(b-j_i(k)\in\ker\partial_i=\operatorname{im}\alpha_i\), hence \(c\in\operatorname{im}\operatorname{sp}_i\). We have proved
\[
\ker\operatorname{obs}_i=\operatorname{im}\operatorname{sp}_i,
\qquad
\operatorname{im}\operatorname{obs}_i
 =\operatorname{im}\partial_i/\partial_i j_i(K_i),
\tag{DC5.3}
\]
and the exact quotient identification
\[
\operatorname{coker}\operatorname{sp}_i
 \xrightarrow{\sim}
 \operatorname{im}\partial_i/\partial_i j_i(K_i),
\qquad
[c]\longmapsto[\partial_i b].
\tag{DC5.4}
\]
This is an exact description of the missing lifts. It does not assert that the whole support group \(O_i\) vanishes.

There is also a kernel calculation before weights. For \(a\in\ker\operatorname{sp}_i\), there is a unique \(k\in K_i\) with \(\alpha_i(a)=j_i(k)\); it lies in \(\ker(\partial_i j_i)\). Every element of that kernel arises in this way by localization. Therefore
\[
0\longrightarrow\ker\alpha_i
 \longrightarrow\ker\operatorname{sp}_i
 \longrightarrow\ker(\partial_i j_i)
 \longrightarrow0.
\tag{DC5.5}
\]
This exact sequence records the information that would be lost by asserting only surjectivity.

## DC6. The three weight estimates used in the source proof

On \(U_0=S'_0\setminus\{s_0\}\), proper smooth base change makes
\[
\mathcal V_j=R^j(f'_0|_{U_0})_*E
\tag{DC6.1}
\]
a lisse sheaf with geometric generic fibre \(V_j\). Smooth proper cohomology is pure of weight \(j\), by Deligne3.3.9 applied to each closed fibre. The local invariant-weight theorem1.8.8(i), reconstructed in DLM10–DLM11, consequently gives
\[
C_i=V_i^I\text{ is mixed of weights }\le i.
\tag{DC6.2}
\]
Its mechanism is the monodromy weight filtration: the invariant primitive pieces of a pure sheaf of weight \(i\) occur in graded indices at most zero, with weights \(i+j\) for \(j\le0\); residual finite inertia invariants preserve the inequality. The source specifically uses this local theorem in its lemma3.6.2. It is not a theorem about arbitrary inertia representations without the pure geometric sheaf just specified.

The special fibre is proper, though it may be singular. The upper bound for compactly supported cohomology of a weight-zero constant sheaf, together with properness, gives
\[
H^r(X_s,E)\text{ has weights }\le r.
\tag{DC6.3}
\]
Applying this to \(r=2N-i-1\), then dualizing and retaining the \((-N)\) twist, gives
\[
w\bigl(H^{2N-i-1}(X_s,E)^\vee(-N)\bigr)
 \ge -(2N-i-1)+2N=i+1.
\tag{DC6.4}
\]
If the indicated degree is negative the group is zero, and the bound remains valid. Thus
\[
O_i\text{ has weights }\ge i+1,
\qquad A_i\text{ has weights }\le i.
\tag{DC6.5}
\]
These are source lemma3.6.3 and the sentence immediately following it. The total dimension \(N\) is essential to the degree and the \(2N\) contribution in (DC6.4).

## DC7. Exactness of the weight cutoff and the complete lifting proof

All terms of the cross are finite-dimensional mixed residual Frobenius modules. This follows for special-fibre terms from (DC6.3), for invariant and coinvariant terms from local monodromy and duality, and for \(B_i\) from (DC3.7). For a fixed embedding \(\iota\), define \(W_iM\), after scalar extension to split Frobenius, as the sum of generalized eigenspaces whose eigenvalues have weight at most \(i\). A Frobenius-equivariant map preserves the generalized eigenspaces: applying a power of \(F-\lambda\) before or after the map gives the same result. A short exact sequence restricts to a short exact sequence on each generalized eigenspace by the primary decomposition of the Frobenius polynomial. Taking the indicated finite direct sum proves exactness of \(W_i\).

This argument does not assume Frobenius semisimple. The weight decomposition can also be stated through the unique weight filtration over its coefficient field. Working after a splitting scalar extension suffices for surjectivity, since a finite-dimensional cokernel is zero exactly when its faithfully flat scalar extension is zero.

Apply \(W_i\) to (DC3.7). Since \(W_iC_i=C_i\), the resulting map
\[
W_iB_i\longrightarrow C_i
\tag{DC7.1}
\]
is onto. The map \(\partial_i\) sends \(W_iB_i\) into \(W_iO_i=0\). For any \(c\in C_i\), choose \(b_0\in W_iB_i\) mapping to \(c\). Then \(\partial_i b_0=0\), so exactness of localization gives an \(a\in A_i\) with \(\alpha_i(a)=b_0\). Consequently
\[
\operatorname{sp}_i(a)=\pi_i\alpha_i(a)=\pi_i(b_0)=c.
\tag{DC7.2}
\]
This proves Deligne3.6.1 in the arithmetic reduction, and the reduction in DC2 gives the stated geometric theorem. In terms of the exact obstruction,
\[
\operatorname{im}\partial_i=\partial_i j_i(K_i),
\qquad
\operatorname{coker}\operatorname{sp}_i=0.
\tag{DC7.3}
\]
Indeed an arbitrary \(b\) has the same image in \(C_i\) as a low-weight lift \(b_0\), so \(b-b_0=j_i(k)\), and \(\partial_i b=\partial_i j_i(k)\). Both \(K_i\) and \(O_i\) have been retained in this equation.

## DC8. A stronger consequence: the coinvariant term is exactly the boundary image

For any finite-dimensional representation \(V\), the annihilator of the span of \(gv-v\) is precisely the invariant subspace of the contragredient representation. Thus there is a canonical Frobenius-equivariant isomorphism
\[
(V_I)^\vee\xrightarrow{\sim}(V^\vee)^I.
\tag{DC8.1}
\]
The lisse sheaf \(\mathcal V_{i-1}^\vee\) is pure of weight \(1-i\). Apply the same local invariant theorem used in DC6 to this dual sheaf. It gives
\[
(V_{i-1}^\vee)^I\text{ has weights }\le1-i.
\tag{DC8.2}
\]
Dualizing (DC8.1), then applying the retained \((-1)\) twist in (DC3.7), proves
\[
V_{i-1,I}\text{ has weights }\ge i-1,
\qquad K_i=V_{i-1,I}(-1)\text{ has weights }\ge i+1.
\tag{DC8.3}
\]
When the indicated generic cohomology group vanishes, in particular in negative degree, the bounds hold vacuously. Degree-zero cohomology is retained and may be nonzero. In particular \(W_iK_i=0\). Exactness of the cutoff on (DC3.7) strengthens (DC7.1) to an isomorphism
\[
\pi_i|_{W_iB_i}:W_iB_i\xrightarrow{\sim}C_i.
\tag{DC8.4}
\]
Since \(A_i\) has weights at most \(i\), its image under \(\alpha_i\) is contained in \(W_iB_i\). Conversely \(\partial_i\) kills \(W_iB_i\), so localization puts that entire subspace in the image. Hence
\[
\operatorname{im}\alpha_i=W_iB_i=\ker\partial_i.
\tag{DC8.5}
\]
The intersection \(j_i(K_i)\cap W_iB_i\) is zero by disjoint generalized-eigenvalue weights; the dimensions in (DC3.7) and (DC8.4) give
\[
B_i=W_iB_i\oplus j_i(K_i),\qquad
\partial_i j_i:K_i\xrightarrow{\sim}\operatorname{im}\partial_i.
\tag{DC8.6}
\]
Surjectivity of the last arrow is (DC7.3); injectivity follows from (DC8.5) and the zero intersection. Thus the coinvariant term has not been removed: it is canonically the boundary image in this arithmetic Frobenius cross.

Inverting (DC8.4) defines a section
\[
s_i:C_i\longrightarrow B_i,\qquad
\pi_i s_i=\operatorname{id}_{C_i},\quad
\operatorname{im}s_i=W_iB_i.
\tag{DC8.7}
\]
It is the unique Frobenius-equivariant section, because the difference of two such sections is a Frobenius-equivariant map \(C_i\to K_i\), and all such maps are zero by their disjoint weight ranges. This uniqueness is a statement in the fixed arithmetic Frobenius model. The argument does not construct an intrinsic arithmetic Frobenius, or this splitting, on every original \(k\)-model before the reduction. It also does not give a canonical lift \(C_i\to A_i\).

## DC9. The exact quotient of the special-fibre classes

By (DC8.6), the right-hand term in (DC5.5) is zero. Combining (DC4.2) with (DC5.5) therefore gives
\[
\ker\operatorname{sp}_i=\ker\alpha_i=\operatorname{im}g_i.
\tag{DC9.1}
\]
Thus the invariant-cycle quotient, including its complete kernel, is
\[
A_i/\operatorname{im}\bigl(H^i_{X_s}(X,E)\xrightarrow{g_i}A_i\bigr)
 \xrightarrow{\sim}V_i^I,
\quad [a]\longmapsto\operatorname{sp}_i(a).
\tag{DC9.2}
\]
Its inverse sends \(c\) to the class of any special-fibre lift; two such lifts differ by exactly the displayed kernel. The set of lifts of any \(c\) is the nonempty affine coset
\[
\operatorname{sp}_i^{-1}(c)=a_0+\operatorname{im}g_i.
\tag{DC9.3}
\]
No selected representative \(a_0\) is preferred by the quotient theorem.

The full support sequence can be expressed without leaving its kernel implicit. In degree \(j-1\), (DC8.6) identifies the image of \(B_{j-1}\to P_j\) with the injected term \(K_{j-1}\). In degree \(j\), (DC9.1) identifies the image of \(P_j\to A_j\) with the specialization kernel. Using (DC4.6), the localization sequence therefore gives
\[
0\longrightarrow H^{j-2}(X_{\bar\eta},E)_I(-1)
 \xrightarrow{\partial_{j-1}j_{j-1}}
 H^{2N-j}(X_s,E)^\vee(-N)
 \xrightarrow{g_j}H^j(X_s,E)
 \xrightarrow{\operatorname{sp}_j}H^j(X_{\bar\eta},E)^I
 \longrightarrow0.
\tag{DC9.4}
\]
The middle arrow denotes the support-to-ordinary cohomology map transported through the exact duality isomorphism, not an arbitrarily chosen pairing. Exactness at the first nonzero term is the injectivity in (DC8.6), at the next two terms is localization and (DC9.1), and at the final term is DC7. All its groups and arrows therefore have explicit origins.

Neither (DC7.3) nor (DC9.4) says \(O_i=0\). In fact the next localization arrow gives
\[
O_i/\partial_i j_i(K_i)
 \xrightarrow{\sim}\operatorname{im}(g_{i+1})
 =\ker\operatorname{sp}_{i+1}.
\tag{DC9.5}
\]
This group can survive. What vanishes is the image of the obstruction map from \(C_i\) into that quotient. Equation(DC9.5) specifies exactly what the quotient itself records.

## DC10. Functoriality of the quotient and of the obstruction

Fix a residual field size \(Q\), the coefficient field, and geometric Frobenius convention. An exact cross consists of finite-dimensional Frobenius modules \((A,B,C,K,O)\) with an exact row \(0\to K\xrightarrow{j}B\xrightarrow{\pi}C\to0\), maps \(A\xrightarrow{\alpha}B\xrightarrow{\partial}O\) exact at \(B\), and specialization \(\pi\alpha\). A morphism of exact crosses is a tuple
\[
(f_A,f_B,f_C,f_K,f_O)
\tag{DC10.1}
\]
of Frobenius-equivariant maps satisfying
\[
f_B\alpha=\alpha'f_A,\quad
f_Bj=j'f_K,\quad
f_C\pi=\pi'f_B,\quad
f_O\partial=\partial'f_B.
\tag{DC10.2}
\]
The second and fourth equations send \(\partial jK\) into \(\partial'j'K'\), so they induce a map \(\bar f_O:O/\partial jK\to O'/\partial'j'K'\). Given \(c=\pi b\), compute
\[
\operatorname{obs}'(f_Cc)
 =[\partial'f_Bb]=[f_O\partial b]
 =\bar f_O(\operatorname{obs}(c)).
\tag{DC10.3}
\]
This proves functoriality of the obstruction, of its image, and of the cokernel identification (DC5.4). It is an actual commuting-map calculation.

For crosses having the weights proved above, \(f_B\) preserves \(W_i\). The characterization (DC8.7) therefore gives
\[
f_Bs_i=s'_if_C.
\tag{DC10.4}
\]
For the special-fibre quotient, \(f_A\) sends \(\ker\operatorname{sp}_i\) into \(\ker\operatorname{sp}'_i\) by (DC10.2), and its induced map is identified with \(f_C\) under (DC9.2). This is the precise sense in which the quotient and lift commute with a specified compatible comparison.

An isomorphism of the actual proper geometric models over their pointed curve induces such an isomorphism of crosses, by the naturality of restriction, proper base change, group cohomology, localization, and duality. When written contravariantly through pullback, all five arrows are reversed together. Equal total dimensions and residue degrees are then preserved. No arbitrary map between unrelated vector spaces is asserted to be induced by a geometric model map.

If the arithmetic model is extended by a residue-field degree \(e\), the geometric Frobenius becomes \(F^e\), its eigenvalues become \(\lambda^e\), and its residue cardinality becomes \(Q^e\). The weights and Tate contributions satisfy the exact formulas
\[
2\log_{Q^e}|\iota(\lambda^e)|=2\log_Q|\iota(\lambda)|,
\qquad (Q^e)^N=Q^{eN}.
\tag{DC10.5}
\]
Thus this field extension preserves the weight cut and every preceding formula with the specified replacement of Frobenius and residue cardinality.

## DC11. Typed comparison with the programme's global quotient

The programme's retained support is \(\tau\langle Z_1;\text{no }Z_2\rangle\). No addition or arithmetic operation on that supporting point occurs here. Its supplied winding carrier has the previously reconstructed quotient and endomorphism ring
\[
L=G/H,\qquad G\simeq\mathbb Z\times C_4,\quad H=\{0\}\times C_4,
\qquad R=\operatorname{End}_{\mathrm{Ab}}(L)\simeq\mathbb Z.
\tag{DC11.1}
\]
The complete group construction, rather than a selected prime or a numerical timing sample, is the input to these recovered arithmetic objects. As proved in MDB1, the ring isomorphism sends the integer \(n\) to the multiplication endomorphism \([n]\); it is independent of the sign of a generator of \(L\).

After this whole reconstruction there are actual unital ring maps, for every recovered prime \(p\) and positive integer \(h\),
\[
R\longrightarrow R/pR\simeq\mathbb F_p
 \longrightarrow\mathbb F_{p^h},
\tag{DC11.2}
\]
and therefore actual scheme maps
\[
\operatorname{Spec}\mathbb F_{p^h}
 \longrightarrow\operatorname{Spec}(R/pR)
 \longrightarrow\operatorname{Spec}R.
\tag{DC11.3}
\]
The arrows reverse because \(\operatorname{Spec}\) is contravariant. If the Deligne model has base field \(\mathbb F_q\), \(q=p^f\), its given structural map composes with (DC11.3) for \(h=f\). The special residue field has size \(Q=p^{fd_s}\), and its point composes through (DC11.3) for \(h=fd_s\). Thus the exact scheme-theoretic receiving map from an existing Deligne model to the recovered arithmetic base is
\[
X'_0\longrightarrow\operatorname{Spec}\mathbb F_q
 \longrightarrow\operatorname{Spec}R,
\qquad
\operatorname{Spec}k(s_0)\longrightarrow\operatorname{Spec}\mathbb F_q
 \longrightarrow\operatorname{Spec}R.
\tag{DC11.4}
\]
These maps make the relationship concrete. They do not construct \(X'_0\), its proper degeneration, its cohomology, or its purity from the point \(\tau\) alone. In particular none of those absent identifications is substituted for the actual hypotheses of DC1–DC2.

For a complete branch isomorphism \(B:L\to L'\), conjugation gives
\[
C_B:R\xrightarrow{\sim}R',\qquad f\longmapsto BfB^{-1},
\quad C_B([n])=[n].
\tag{DC11.5}
\]
Hence the induced map \(\operatorname{Spec}(C_B^{-1})\) preserves each recovered residue characteristic and the maps (DC11.2)–(DC11.4). Viewing the same given finite-field model over either identified arithmetic base gives the same étale cohomology cross. Its induced comparison is the identity under these identifications, so (DC10.3)–(DC10.4) prove commutation of its obstruction, quotient, and low-weight lift. This is a transport of the already specified model; it is not a rule assigning that model to every branch.

There are consequently two exact quotients with fully stated source objects: the group quotient \(G\twoheadrightarrow L\), and the cohomological quotient (DC9.2). The latter has the obstruction calculation (DC5.4) and the proved vanishing mechanism (DC6)–(DC8). Their present relationship is through the recovered arithmetic-base maps (DC11.2)–(DC11.4) and the compatible model comparisons of DC10. No isomorphism from a zeta zero-jet algebra or an analytic measurement space to \(A_i\), \(B_i\), or \(C_i\) has been used. In particular the proof establishes a quotient-and-lift theorem in its exact cohomological domain; it supplies no new verdict about zeros of the original Riemann zeta function.

## DC12. The complex analytic remark and the scope of the proof

The witness's §3.6.4 states a complex analytic analogue for a proper map \(f:X\to D\), with \(X\) smooth and \(f\) smooth over \(D^*=D\setminus\{0\}\), under its stated factorization through \(\mathbb P^n(\mathbb C)\times D\to D\). It gives a surjection
\[
H^i(X_0,\mathbb Q)\longrightarrow
 H^i(X_t,\mathbb Q)^{\pi_1(D^*,t)}.
\tag{DC12.1}
\]
The witness says the argument is parallel, using mixed Hodge weights in place of Frobenius weights, and cites J. Steenbrink, *Mixed Hodge structure on the vanishing cohomology*, Oslo symposium, 1976. That mixed Hodge construction has not been independently read or reconstructed in this bounded note. In particular the brief transcription's word “factorization” is not silently strengthened here into a claim that it explicitly printed an embedding hypothesis, nor used to extend (DC12.1) to an arbitrary proper analytic map.

The complete proof given in DC1–DC9 is the rational \(\ell\)-adic theorem3.6.1 with the source's arithmetic reduction. Its stronger statements (DC8.3)–(DC9.5) were derived from the same proved local invariant bounds, source duality, and exact sequences. They retain \(H^{i-1}(X_{\bar\eta})_I(-1)\), the total dimension \(N\), the full support degree \(2N-i-1\), the residue degree \(d_s\), the geometric Frobenius multiplier \(Q\), the multiplier \(Q^N\) in support duality, every specialization kernel, and the dependence of the canonical section on the fixed arithmetic Frobenius model.
