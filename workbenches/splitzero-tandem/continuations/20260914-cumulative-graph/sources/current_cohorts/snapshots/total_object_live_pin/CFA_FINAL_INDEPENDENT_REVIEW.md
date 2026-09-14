# Independent final mathematical review of the coefficient-face cochain attachment

- Review date: 2026-09-13.
- Reviewer: `assembly_symmetry_check` subagent, independent of the source author.
- Reviewed source: `work/rh_counterfactual_20260913/total_object/coefficient_face_cochain_attachment.tex`.
- Exact reviewed byte length: **38,816**.
- Exact reviewed SHA256: **7377e5445f25ce4c4b9eac2fd1cd2765144ce639da482f54ede3bf4bc8512961**.
- Scope: the entire source, CFA.1–CFA.38, including CFA.22a–CFA.22d and all intervening prose. The final byte content was read in two complete, untruncated portions, each accompanied by the same independently calculated source hash.

**Verdict: no unresolved mathematical error found in this exact source.** All requested repairs are present. This is a mathematical source review, not a LaTeX compilation or rendered-page review. The separate semiring and weight modules are not certified by this receipt.

## Face complexes and supported cohomology

CFA.1–CFA.7 retain the exact sequence `0 → V → B_U → T_U Q → 0`. Finite direct sums give the displayed face sequences without an additional exactness hypothesis. The joint source coordinates `u = phi − Fourier(psi)` and `v = (phi + Fourier(psi))/2` have the displayed inverse; the differential is exactly `Theta u`. Consequently the degree-zero joint diagonal is `W[A]`, while the degree-one group is `Q_W[A]` for all three nonempty source-leg masks.

Zero insertion sends `e_A` to `e_B`, including the empty-face arrow. The source distinguishes this support-changing map from the coordinatewise pointed lift, which preserves the support mask even when its amplitude is zero. The independent carrier is a labelled disjoint union, not the colimit with terminal full face. Its supported cycle and boundary calculations are exactly the ordinary linear ones within each fixed face. The retained zero amplitude carrier is `G(0)^n`, so neither the empty packet nor the ordinary zero degrees erase the independent faces.

## Full units, source sections, and divisor transport

In CFA.9, `v_h = g/h` is a unit at precisely the retained full-order packet factors. Multiplication by its complete jet inverse proves `J_h s_h = 1`. If `P_h(u) = r_h(epsilon_h u)`, then

\[
xP_h(u)-P_h(A_hu)=h\ell_h(u).
\]

This proves CFA.10 with its exact original theta boundary and proves CFA.11 coordinatewise. It also verifies the declared scalar type: `s_h` is complex-linear and gives a cochain map from the packet in degree one; its Euler compatibility is a homotopy, not polynomial linearity.

For `H = b h`, the complete-jet identity

\[
r_H(\varepsilon_H\iota_{hH}u)=b\,r_h(\varepsilon_hu)
\]

holds because its product with the full unit `v_H` has the required old jets and zero jets at every added factor. Its degree is below `deg H`. Together with `b(D)F_H = F_h`, this verifies every identity in CFA.14, including the exact source-section identity and the top-coefficient identity. The raw numerator map retains its factor `[b]_h`; it is not identified with the nonunital arithmetic zero extension.

## Dilation and proper source labels

The integral in CFA.15 exists in the original Schwartz space. On its compact parameter interval the displayed dilation seminorm identity bounds every required derivative; completeness supplies the integral. Evaluation at zero and integration are continuous functionals and vanish on every integrand.

For `L = log a`, the derivative of `R_{exp(L-t)}` is `−D R_{exp(L-t)}`. Therefore CFA.16 integrates, with the stated orientation also when `L < 0`, to

\[
R_as_h-s_h\exp(LA_h)=\Theta B_{h,a}.
\]

This verifies the sign, the endpoint terms, the case `a = 1`, and the divisor identity `B_{H,a} iota_{hH} = B_{h,a}`. Quotienting gives exact dilation equivariance. Before quotienting, the displayed map remains a complex-linear source homotopy.

CFA.23–CFA.25 retain the original residual class in `V/W`. The final source explicitly names the maps `V/W → V/W'` and `Q_W → Q_W'` and their respective kernel identifications with `W'/W`. Dilation actually changes the target label to `R_aW`, and the residual class of CFA.25 lies in `V/R_aW`. No fixed-label dilation invariance or vanishing of this proper-source residual is assumed.

## Strict balanced maps and their full divisor homotopies

The map `kappa_h` in CFA.20 is polynomial-linear in both degrees. Its cochain identity is `h(D)F'_h = Theta phi'_h`. The explicit polynomial quotient in CFA.21 proves that its degree-one map agrees with the original `sigma_h` after quotienting. Thus balancing this free-complex map is well-defined; balancing `s_h` itself is not asserted. Flatness of each analytic stalk follows from its torsion-freeness over the polynomial PID by the stated finite-free-submodule argument.

For CFA.22a, the free divisor map has degree-zero multiplier `a_hH` and degree-one multiplier `b a_hH`. Its cochain identity is `H a_hH = b a_hH h`, and its cohomology map is exactly the arithmetic zero extension.

For CFA.22b, reduction modulo `h` proves that

\[
w_{hH}=(a_{hH}e_H-e_h)/h
\]

is a polynomial. The two components of `kappa_H L_hH − kappa_h` are respectively `K_hH h` and `Theta K_hH`, verifying the displayed homotopy with its sign and degree.

For CFA.22c, the polynomial expressions `a_hH a_HJ` and `a_hJ` both reduce to `(J/h)^{-1}` modulo `h`. Thus the displayed `eta` is a polynomial. The two components of the divisor-composition difference are multiplication by `h eta` and `J eta`, exactly `dT + Td`.

For CFA.22d, both degree-one coefficients are

\[
\frac{a_{hH}a_{HJ}e_J-e_h}{h}:
\qquad
b a_{hH}w_{HJ}+w_{hH}=w_{hJ}+\eta e_J.
\]

All other components vanish by degree. This verifies the additional attachment-composition identity. The text correctly restricts the polynomial-linearity assertion to the homotopies in CFA.22b–CFA.22c; it does not extend that assertion to the earlier finite-dimensional section homotopies.

## Mixed-observation types and tensor signs

CFA.26 preserves all empty and supported-zero cases because a coordinatewise pointed linear lift never removes an active slot. Its application to divisor synchronization uses the explicit filling formula, not an inapplicable unital localization property. CFA.27 retains the trace factor `1/n` and distinguishes the synchronized retraction from raw projection to coefficient slot zero.

The signed coefficient permutation commutes with each complex-linear coordinate map, including the source homotopies. The arithmetic convolution identity in CFA.29 has target parameter `ac`; in particular the diagonal parameter `a` has target parameter `a^2`. The finite degree-zero convolution is kept distinct from tensor-DGA concatenation of degree-one packet classes.

CFA.30–CFA.32 use the original Mellin isomorphism, full-unit inverse, and the original balanced inclusion and projection. The final source explicitly restricts CFA.32's analytic stalk to `s_0 in U`. Applying the maps to finitely many active coordinates requires only a common finite packet. Strict section compatibility under enlarging that packet was proved in CFA.14.

In CFA.34, the degree-minus-one map crosses precisely the preceding input degrees, giving the sign

\[
(-1)^{\sum_{j<i}|x_j|}.
\]

The surviving terms of `dH + Hd` are `g_1 ⊗ ... ⊗ g_(i−1) ⊗ (f_i−g_i) ⊗ f_(i+1) ⊗ ... ⊗ f_k`; they telescope to the tensor of the `f_i` minus the tensor of the `g_i`. Thus the formula has the correct ordering and signs. The finite packet tensor quotient in CFA.35 follows from the full remainder bases and retains every actual local multiplicity.

## Continuity and the graded attachment category

CFA.36 is the direct finite-basis seminorm estimate. For CFA.37, the bounds on the two halves of the Mellin integral are exactly

\[
\frac{p_+(F)}{(N-\sigma)^{j+1}}
+\frac{p_-(F)}{(N+\sigma)^{j+1}},\qquad N>|\sigma|.
\]

The factorials cancel against the Taylor-jet factor `1/j!`. A sufficiently small neighborhood of the fixed spectral point still has an integrable dominating function, justifying the derivatives. The quotient continuity assertion uses `J_h Theta = 0`. These facts prove precisely the fixed-packet embedding assertions in the source. No uniform estimate or infinite-stage topology identification is asserted.

CFA.38 uses the actual graded Hom differential

\[
\partial f=d_{\rm target}f-(-1)^{|f|}f d_{\rm source}.
\]

Its square is zero, and its composition rule has the displayed degree sign. A degree-minus-one homotopy satisfies `partial H = dH + Hd`. The attachment imposes the corresponding linear relation `f − g = partial H`, without falsely identifying the unmodified cochain paths. Independently typed mixed-carrier maps remain in the underlying-set representation and are not declared cochain maps.

No mathematical edits were made by this reviewer. This receipt records the exact reviewed source version and the completed independent checks.
