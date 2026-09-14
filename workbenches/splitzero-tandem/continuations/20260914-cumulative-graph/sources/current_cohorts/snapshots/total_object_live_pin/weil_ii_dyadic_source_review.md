# Independent source review: Weil II 3.2.4(k) to 3.2.4(k+1)

Reviewer: `/root/weil_ii_bootstrap_detail/dyadic_source_review`.
Date: 2026-09-13. Scope: the original finite-field argument, with explicit checks of its source notation and the mathematical steps an expanded exposition must supply. This review does not claim that the Split-Zero programme has the required geometric construction.

## Controlling sources and inspection

- Current local English: `output/Deligne_Weil_II_S20_LaTeX/typed_latex/S20_EN_article_text.txt`, especially lines 1869–1985, with dependencies 1.4.1–1.4.4, 1.5.1, 1.8.1–1.8.4, 2.2.10, and 3.1.
- Current local French: the corresponding `S20_FR_article_text.txt`. The relevant complete passage agrees with the English on the points audited below.
- Controlling original: `output/Deligne_Weil_II_S20_LaTeX/source_package/source/20_AUTHORITY_DELIGNE_D032_WEIL_II_NUMDAM_117PP.pdf`. Full printed pages 200, 202, 203, 204 were visually inspected directly from the scan, without changing it. Their zero-based physical PDF page indices are 64, 66, 67, 68.
- Published primary-source record: <https://archive.numdam.org/articles/10.1007/BF02684780/>.

The argument is a dyadic induction using only the square at each step. It is not literally the large-product proof of Weil I. It recreates its error-shrinking mechanism after a stronger geometric calculation of the square.

## 1. Exact assertion, base case, and extension to a constructible sheaf

Fix the same finite field F_q and embedding iota throughout an induction step, and use Deligne's weight convention

\[
w_q(\alpha)=2\log_q|\iota\alpha|.
\]

Assertion B_k is the statement for **every** smooth curve U_0/F_q and every lisse pointwise iota-pure sheaf F_0 of weight zero:

\[
\operatorname{Spec}(F\mid H_c^1(U,F))
\subset\{\alpha:w_q(\alpha)\le1+2^{-k}\}.
\]

The universal quantifier is essential: B_k must later be applied to the new pure constituents on the pencil parameter curve, rather than only to the starting sheaf. The base bound is 1.8.2. If necessary remove one point from a projective curve first; compact-support cohomology of the resulting open surjects onto H_c^1 of the curve, by the same elementary exact sequence below. This avoids silently applying the affine Euler-product formula to a projective curve with an extra H_c^0 denominator.

For a dense open j:U_0→X_0 and any constructible G_0 on the curve X_0, the stalkwise exact sequence

\[
0\longrightarrow j_!j^*G_0\longrightarrow G_0\longrightarrow Q_0\longrightarrow0
\]

has Q_0 supported on finitely many points. Therefore H_c^1(X,Q)=0, and the long exact sequence gives a Frobenius-equivariant surjection

\[
H_c^1(U,j^*G)\twoheadrightarrow H_c^1(X,G).
\]

If j^*G_0 is lisse and pure of weight b, the rank-one twist of 1.2.7 and B_k give the bound b+1+2^{-k} on the target. This is 3.2.5(k). It requires neither purity nor absence of point-supported summands for G_0 on the whole curve. In a formulation using ordinary lisse sheaves, a weight-cancelling constant twist can be obtained from an appropriate root of an existing closed-point eigenvalue; that eigenvalue and its roots are l-adic units. A completely arbitrary complex scalar should not be inserted into an ordinary l-adic local system without this check.

## 2. Geometric square, real envelope, and the printed support error

Under 3.2.6(A–C), form X_0×X_0, V_0=U_0×U_0, and G_0=F_0 external-tensor F_0. Choose the Lefschetz pencil and blow-up from 3.1.1. Its compactified total space maps properly to A_0^*, a projective line. The open total space is denoted V-tilde; its map f to A_0^* is generally not proper. The letter f is used for both maps, and j denotes extension of the open total space into its compactification.

Write K_0=R^1f_!pi^*G_0 and w:W_0→A_0^* for the complement of the exceptional values. The sheaf G_0⊕G_0^∨ is lisse, pure of weight zero, and iota-real: its closed-point eigenvalues occur with their complex conjugates because their absolute values are one. Proposition 3.2.1 and Remark 3.2.2 make w^*R^1f_!pi^*(G_0⊕G_0^∨) iota-real. Thus w^*K_0 is a direct summand of an iota-real lisse sheaf, and 1.5.1 gives a finite filtration with lisse pointwise-pure successive quotients. Their weights are initially arbitrary real numbers.

**Source notation correction.** On printed page 202, formula (3.2.7.1) in the original scan really does print

\[
(R^1f_!\pi^*H_0)_{\bar x}=H^1(Y,\pi^*H),
\]

without a c, even though the surrounding sentence calls Y the open fibre. Both current S20 transcriptions preserve that printing. The mathematically correct identification used by the proof is

\[
(R^1f_!\pi^*H_0)_{\bar x}
=H_c^1(Y,\pi^*H)
=H^1(\overline Y,j_{Y!}\pi^*H).
\]

The first equality is compact-support base change; the second uses the proper fibre and extension by zero. It is not legitimate to replace H_c^1 of the open fibre by ordinary H^1 of that same open fibre. For example, constant coefficients on G_m give different Frobenius weights in these two groups. An exposition should explicitly state this source correction rather than hide it or blame the English export.

**Additional printed twist error.** Printed page 200, in the proof of 3.2.1, says H^0(X,F) is the dual of H_c^2(X,F^∨(−1)). With Deligne's convention Q_l(1) has weight −2, the exact scalar duality uses F^∨(1):

\[
H^0(X,F)^\vee\simeq H_c^2(X,F^\vee(1)).
\]

The printed group with (−1) is instead H^0(X,F)^∨(−2). Its reality implication survives because the extra q^2 scaling is real. An expanded proof should use the correct +1 formula or record the extra (−2) twist explicitly. This published defect is separate from 3.2.15, which correctly prints +1.

## 3. The exact local quotient that forces integrality

The point of 3.2.9 is stronger and more precise than saying that a mixed sheaf has an integer-indexed filtration.

At each exceptional value t, the calculations in 3.1 show the vanishing-cycle sheaves are concentrated at one exceptional point x and in degree one. Consequently,

\[
0\to K_{\bar t}\to K_{\bar\eta}\to\Phi_x^1
\to(R^2f_!\pi^*G)_{\bar t}
\to(R^2f_!\pi^*G)_{\bar\eta}\to0.
\]

In particular, the specialization/generization map K_t→K_eta is injective. A local section supported at t has zero generic value; the injectivity forces it to vanish. This proves 3.2.8 and makes the map K_0→w_*w^*K_0 injective.

Extend the filtration on w^*K_0 by intersection as Deligne does. At a puncture this is the elementary linear-algebra construction B_i=B∩V_i for B=K_t⊂V=K_eta. It gives injective maps

\[
B_i/B_{i-1}\hookrightarrow V_i/V_{i-1}.
\]

The cokernel A_t^i is the corresponding graded piece of V/B for the quotient filtration. Since V/B injects into Phi_x^1, A_t^i is a subquotient of Phi_x^1. Thus the derived short exact sequence is an actual sequence of local Weil representations:

\[
0\to (\operatorname{Gr}_G^iK)_{\bar t}
\to(\operatorname{Gr}_G^iK)_{\bar\eta}
\to A_t^i\to0.
\]

There are two independently proved restrictions on a **nonzero** A_t^i:

1. All its Frobenius weights are integers. Indeed, 1.8.4 applied to the original weight-zero F_0 makes the local monodromy graded pieces have integer weights. Hypothesis (A) gives trivial inertia on these pieces. Taking the two-factor tensor filtration gives locally constant integer-weight graded pieces of G_0 near the normal-crossing boundary. The explicit three local vanishing-cycle calculations are:

\[
\begin{array}{ll}
\text{interior node:}&\Phi_x^1=G_x(-1)\otimes\varepsilon(B),\\
\text{boundary tangency:}&\operatorname{Gr}\Phi_x^1=(\operatorname{Gr}G)_x\otimes\varepsilon(B),\\
\text{boundary crossing:}&\operatorname{Gr}\Phi_x^1=(\operatorname{Gr}G)_x\otimes\varepsilon(B).
\end{array}
\]

Here the branch sign representation has eigenvalues ±1 and weight zero, while (−1) raises weight by two. The results retain integral weights, and so do subquotients.

2. If the pure restriction of Q_i=Gr_G^iK_0 to W_0 has weight b_i, all Frobenius weights of its generic local representation lie in b_i+Z. This is exactly 1.8.4, now applied to **that new pure constituent**. Since A_t^i is its nonzero quotient, choose an eigenvalue lambda of A_t^i. For some integer j its weight is b_i+j. The first restriction says this is an integer. Therefore b_i is an integer.

The nonzero quotient is indispensable. If A_t^i=0 for every puncture, the generization maps on Q_i are isomorphisms. The image of each special stalk lies in local inertia invariants, so these isomorphisms force the inertia representations to be trivial and the sheaf to be lisse across every puncture. Thus Q_i is lisse on the full geometric projective line. Its geometric monodromy is trivial, and Q_i is geometrically constant. Its arithmetic Frobenius action need not be trivial and its weight has not been forced to zero. Nevertheless,

\[
H^1(\mathbf P^1_{\overline{\mathbf F}_q},Q_i)
=H^1(\mathbf P^1_{\overline{\mathbf F}_q},\overline{\mathbf Q}_\ell)\otimes Q_{i,\bar\eta}=0.
\]

This is the exact dichotomy: either the constituent contributes no H^1, or its weight is integral. It is not a global claim that every pure constituent automatically has integer weight.

## 4. Strict inequality plus integrality, then the outer H^1

At any closed point x of W_0, compact-support base change identifies the fibre of K_0 with H_c^1 of a smooth curve with weight-zero lisse coefficients. The earlier strict theorem 2.2.10 says all these eigenvalues have weights strictly less than two. Since the pure constituents are subquotients of that fibre, each pure constituent weight b_i is strictly less than two. This is 3.2.10.

For a constituent that can contribute to H^1 on the pencil line, the preceding section gives b_i∈Z. Hence

\[
b_i<2,\quad b_i\in\mathbf Z\quad\Longrightarrow\quad b_i\le1.
\]

This is the discrete exclusion that does the work: a weak bound b_i≤2 would not suffice. Applying 3.2.5(k) to Q_i on the projective parameter curve yields

\[
w_q\bigl(H^1(A^*,Q_i)\bigr)\le b_i+1+2^{-k}\le2+2^{-k}.
\]

The filtration long exact sequences show every eigenvalue on H^1(A^*,K) occurs on one of the H^1(A^*,Q_i). No splitting of the filtration is required. Thus E_2^{1,1} has the same upper bound, as asserted in 3.2.11.

## 5. The two outer Leray terms require both cohomology levels

The remaining total-degree-two terms are

\[
E_2^{0,2}=H^0(A^*,R^2f_!\pi^*G),\qquad
E_2^{2,0}=H^2(A^*,R^0f_!\pi^*G).
\]

There are **two** applications of the elementary curve calculation, as 3.2.12 states.

First apply 1.4 to the fibres. For a possibly singular fibre, pass to dense smooth opens on its components for H_c^2, using 1.4.1(b); the group is built from coinvariants of the weight-zero local system with a (−1) twist. Hence R^2f_!pi^*G has pointwise weights ≤2. For H_c^0, sections inject into stalks of the weight-zero coefficients, so R^0f_!pi^*G has pointwise weights ≤0. A zero group contributes no eigenvalues. The beta in the printed proof's expression beta+i is zero in this induction setup; it should not be left as an unexplained additional parameter.

Next apply the same calculation on the parameter curve. Global sections of a constructible sheaf of pointwise weights ≤2 have weights ≤2. One can justify this without assuming it lisse globally by evaluating at finitely many closed-point orbits whose geometric stalk maps jointly inject on H^0; Frobenius on each orbit is controlled by the closed-point stalk. H^2 depends only on a dense lisse open, where coinvariants add precisely the (−1) twist and therefore two to the pointwise bound zero. This proves the outer bound ≤2. Possible point-supported pieces do not produce an H^2 term, and their H^0 weights are already bounded by their actual stalks.

It would be incomplete to state the pointwise bounds on R^if_! and immediately identify them with bounds on both outer cohomology groups without this second application.

## 6. Leray, actual injection, and the factor of one half

The Frobenius-equivariant Leray spectral sequence is

\[
E_2^{p,q}=H^p(A^*,R^qf_!\pi^*G)\Longrightarrow
H_c^{p+q}(\widetilde V,\pi^*G).
\]

Each E_infinity term is a subquotient of its E_2 term. The finite filtration on total-degree-two cohomology has these E_infinity terms as graded pieces, so all its eigenvalues have weight ≤2+2^{-k}. No degeneration of Leray at E_2 is needed or asserted.

The preservation map is the composite of Kunneth's direct-summand inclusion and the blow-up pullback of 3.1.1.4:

\[
H_c^1(U,F)\otimes H_c^1(U,F)
\hookrightarrow H_c^2(V,G)
\hookrightarrow H_c^2(\widetilde V,\pi^*G).
\]

The blow-up formula 3.1.1.3 supplies an actual Frobenius-equivariant direct-sum decomposition, with the extra H^0(V∩A,G)(−1) in degree two. Consequently this composite does not kill a nonzero eigenvector tensor v⊗v. If Fv=alpha v, then the image is an eigenvector with eigenvalue alpha^2. Thus

\[
2w_q(\alpha)=w_q(\alpha^2)\le2+2^{-k},
\qquad w_q(\alpha)\le1+2^{-(k+1)}.
\]

Generalized eigenspaces and semisimplicity are unnecessary for this argument: every eigenvalue has an eigenvector over the algebraically closed coefficient field, and a nonzero vector has nonzero tensor square.

## 7. Removing auxiliary choices and duality

The original 3.2.14 says finite **surjective** cover with smooth source; it does not insert the word etale. The finite-field extensions used to define the general-position pencil and make exceptional points rational are harmless because

\[
w_{q^r}(\alpha^r)=w_q(\alpha).
\]

They do not themselves shrink the induction error. The cover that makes local monodromy unipotent retains the old cohomology through the following genuine pullback/trace injection, independently checked by `/root/weil_ii_bootstrap_detail/dyadic_source_review/cover_trace_check`.

Let g:U'→U be finite surjective between smooth curves and work over one connected target component. Its degree d is positive and constant. The map is finite flat: locally on the smooth target the finite modules are torsion-free over discrete valuation rings, so are free. For characteristic-zero l-adic coefficients E, define the sheaf trace g_*E→E at a geometric point u by

\[
(a_{u'})_{u'\mid u}\longmapsto
\sum_{u'\mid u}\operatorname{length}
\bigl(\mathcal O_{g^{-1}(u),u'}\bigr)a_{u'}.
\]

This includes ramification and inseparable multiplicities. Sheaf compatibility follows by decomposing the preimage of an etale neighbourhood into open-and-closed pieces: each piece is finite flat, and its rank is locally constant. The unit followed by trace is d times the identity. The projection formula therefore gives

\[
F\longrightarrow g_*g^*F\longrightarrow F,
\qquad \operatorname{Tr}_g\circ\eta=d\,\mathrm{id}_F.
\]

Since g is finite, it is proper and its geometric fibres have no higher etale cohomology. Thus Rg_*=g_*=g_!, and applying compact-support cohomology gives

\[
H_c^i(U,F)\xrightarrow{g^*}H_c^i(U',g^*F)
\xrightarrow{d^{-1}\operatorname{Tr}_g}H_c^i(U,F),
\qquad d^{-1}\operatorname{Tr}_g\circ g^*=\mathrm{id}.
\]

These maps commute with Frobenius when g is defined over the finite base field. No etaleness or prime-to-l degree assumption is needed: d is invertible in E even if l divides it. At a ramified point, a bare unweighted sum over the geometric fibre would be incorrect; the displayed lengths are essential.

Finally the sharp upper bound follows because B_k holds for every k. For the theorem's actual group H^1(X,j_*F), use 3.2.5(k), and then apply the same upper bound to F^∨(1), which is pointwise pure of weight −beta−2. The perfect pairing of 3.2.15 is

\[
H^1(X,j_*F)\times H^1(X,j_*F^\vee(1))\longrightarrow\overline{\mathbf Q}_\ell.
\]

To see the perfectness on these actual groups, express each as the image of its compact-to-ordinary cohomology map. Poincare duality on U identifies those two maps as transposes, up to the degree-one cup-product sign. Their kernels are the annihilators of the opposite images; quotienting by those kernels gives precisely the displayed nondegenerate pairing on the images. Hence alpha^{-1} is an eigenvalue in the second factor, with the corresponding algebraic multiplicity and without requiring semisimplicity, giving

\[
-w_q(\alpha)=w_q(\alpha^{-1})\le-\beta-1,
\qquad w_q(\alpha)\ge\beta+1.
\]

Together with the upper inequality this proves equality. The scalar target and the +1 twist must both be retained; otherwise a spurious factor q is introduced. Compactly supported H_c^1(U,F) alone need not be pure of weight beta+1: the equality is for the parabolic/intermediate image H^1(X,j_*F), as the paper states.

## Exact comparison datum for the programme

The reusable mechanism is the entire morphism chain: old cohomology tensor square injects into a square geometry; a Leray filtration carries it to a middle cohomology computation; every contributing pure constituent has a nonzero local defect quotient with integer weights; the earlier strict bound excludes weight two; the next cohomology contributes at most one plus the old error; division by the tensor exponent halves that error. A formal integer grading or support lattice alone is not the local defect quotient A_t^i. A comparison must identify its source, target, quotient map, Frobenius action, nonzero detection alternative, and vanishing of the undetected H^1. These are the actual elements used by Deligne, rather than a generic appeal to purity.

## Final exposition review status

The parent subsequently supplied `weil_ii_dyadic_bootstrap.tex`. The complete text and its revisions were independently reviewed, and the final file received **PASS** at SHA-256 `e72509638eafe7a324ab6387f21ac0ed53327760d43938a499179df8116065d1` (38182 bytes). Two final display-layout changes were checked by reconstructing the previously reviewed candidate and obtaining its exact prior SHA-256. The exact scope, corrections and final review receipt are recorded separately in `weil_ii_dyadic_bootstrap_independent_review.md`. Compilation and layout checks are the author's separate production work.
