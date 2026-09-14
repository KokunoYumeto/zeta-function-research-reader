# Central inverse-power traces and their original source maps

Independent review lane `restriction_trace_verify`, 13 September 2026. This lane owns only this review file. It has made no source edits, numerical reruns, Lean runs, or remote changes.

The entire `endpoint_restriction_join_review_20260913.md` was read, including Sections 2–4, 7 and 8, at SHA256 `8a8cc364ab4b6943b6fc83420afa9141bbc88f314cebe398c6f7d3fdfe2613c6`. The entire incoming `Tau_Endpoint_Restriction_Control/NOTE.tex` was read at SHA256 `ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6`. In particular its equations (17)–(34), including the arithmetic action and support maps, are direct inputs. The central comparison EP.49–EP.50f in `endpoint_product_sharpening_20260913.tex` was also read directly to verify the indices, constants, phases and contraction penalties; this was a targeted reading of that source. The primary join source had not yet been written when this first review was recorded; its later complete review is recorded separately below if performed.

## 1. Original types and the positive endomorphism

Retain the original monic source polynomials, their norms `omega_n`, the arithmetic mass `omega_0=mu_h^k`, the quotient `E=C[S]/(chi)` in the fixed ordered remainder basis, and every original root multiplicity. For every admitted degree `n>=q−1`, write

\[
 B_n=[b_0,\ldots,b_n],\quad O_n=\operatorname{diag}(\omega_0,\ldots,\omega_n),
 \quad K_n=B_nO_n^{-1}B_n^*,\quad G_n=K_n^{-1},
 \quad R_n=O_n^{-1}B_n^*G_n.
\]

The polynomial source has Hermitian form `O_n`, its quotient `E_n=(E,G_n)` has its actual least-lift form, and `R_n:E_n→P_n` is an isometry. Padding `L_(i,j):P_i→P_j` is an isometry. The original forward transport is `I_(i,j):E_i→E_j`, whose underlying vector-space map is the identity. Its metric adjoint is

\[
 T_{i,j}:E_j\longrightarrow E_i,\qquad T_{i,j}=K_iG_j.
\]

To distinguish a reverse map from an endomorphism without losing their exact relationship, put

\[
 U_{i,j}=T_{i,j}I_{i,j}:E_i\to E_i,
 \qquad V_{i,j}=I_{i,j}T_{i,j}:E_j\to E_j.
\]

Both have the same displayed matrix `K_iG_j` in the retained vector coordinates, and `I_(i,j) U_(i,j)=V_(i,j) I_(i,j)`. Their positive self-adjointness follows from

\[
 G_iU_{i,j}=G_j>0,\qquad G_jV_{i,j}=G_jK_iG_j>0.
\]

The degree inequality `0<K_i<=K_j` gives `0<U_(i,j)<=1` in `G_i` and `0<V_(i,j)<=1` in `G_j`. Denote their `q` positive eigenvalues by `g_(i,j,a)`, counting all multiplicities and all values equal to one. Spectral powers below are defined on these positive endomorphisms, and their traces agree by the displayed similarity. In formulas where `Tr(T_(i,j)^−s)` is used for brevity, it means this trace of the underlying positive endomorphism, with this precise typed construction retained.

Since `I^dagger I=U` and `T^dagger T=V`, the same scalar is the inverse Schatten observation of either original metric map:

\[
 \operatorname{Tr}U_{i,j}^{-s}
 =\operatorname{Tr}V_{i,j}^{-s}
 =\|I_{i,j}^{-1}\|_{S_{2s}}^{2s}
 =\|T_{i,j}^{-1}\|_{S_{2s}}^{2s}
 =\sum_{a=1}^{q}g_{i,j,a}^{-s}\qquad(s>0).
\]

For `0<2s<1`, the expression is still the indicated sum of singular-value powers; no triangle inequality for a Schatten norm is asserted.

## 2. The exact unit eigenvalues of the central pair

In the actual quartet application `k>=3` and

\[
 q=[1+k(m-1)](k+1)^2\ge16,
 \qquad L_{h,k}=2\delta[1+k(m-1)](k+1)
       \left\lfloor\frac{(k+1)^2}{4}\right\rfloor>0.
\]

For the central pair `(i,j)=(q,2q−1)`, kernel addition is the literal source identity

\[
 D=K_{2q-1}-K_q
 =\sum_{n=q+1}^{2q-1}\frac{b_nb_n^*}{\omega_n}.
\]

Thus `rho=rank D<=q−1`. Moreover `1−U=D G_(2q−1)` has this exact rank because `G_(2q−1)` is invertible. It is self-adjoint positive in the metric specified in Section 1. Consequently `U` has exactly `q−rho` eigenvalues equal to one and `rho` eigenvalues in `(0,1)`. Listing one of its unit eigenvalues separately and padding the other list with any additional ones gives

\[
 \operatorname{Spec}U_{q,2q-1}
 =\{1,\gamma_1,\ldots,\gamma_{q-1}\},\qquad 0<\gamma_a\le1.
\]

Its exact volume cost is

\[
 C_{\mathrm{mid}}=\log\frac{V_q}{V_{2q-1}}
 =-\sum_{a=1}^{q-1}\log\gamma_a\ge0.
\]

Every unit factor contributes zero to this cost and one to the inverse-power trace. Neither contribution is discarded.

## 3. Complete inverse-power lower bound

Set `X=L_(h,k)/(C_h^bal q)>0`. The inherited literal sufficient balanced norm constant is

\[
 C_h^{\mathrm{bal}}=256e^\pi\max(1,3/c_h)M_*
 \max(1,\vartheta_h^{-1})\max(1,b^{-3})6^{B_h/3},
\]

with `c_h`, `M_*`, `vartheta_h`, `b` and `B_h` retaining their original meanings in the proved lower-envelope and balanced norm dependency. The already proved balanced product, with all of its original phases and contraction factors, gives

\[
 C_{\mathrm{mid}}\ge A:=2(q-1)\log X+P_{\mathrm{mid}},
\]

where, writing `d_a=V_(q+a)/V_(q+a−1)`, its literal penalty is

\[
 \begin{split}
 P_{\mathrm{mid}}={}&-\log(1-d_0)-\log(1-d_{q-1})
 -2\sum_{a=1}^{q-2}\log(1-d_a)\\
 &+\sum_{a=0}^{q-2}\log\left(1+\frac{\phi_{q+a}^{,2}}{L_{h,k}^{,2}}\right).
 \end{split}
\]

All `0<d_a<1` and all phase squares are retained. Positivity of the radius and the exact product formulas prove these strict inequalities in the inherited balanced-product argument; this review does not replace them by an extra assumption. In particular `P_mid>=0`. Put `A_+=max{0,A}`; the two independently proved inequalities `C_mid>=0` and `C_mid>=A` give `C_mid>=A_+`.

For every real `s>0` apply the following elementary inequality to `x_a=−s log gamma_a`. If `bar x=(sum x_a)/(q−1)`, the inequality `exp(y)>=1+y` gives

\[
 \sum_a e^{x_a}=e^{\bar x}\sum_a e^{x_a-\bar x}
 \ge(q-1)e^{\bar x}.
\]

The scalar inequality used here follows by differentiating `exp(y)−1−y`, whose derivative changes sign only at zero and whose value there is zero. Therefore

\[
 \begin{split}
 \operatorname{Tr}U_{q,2q-1}^{-s}
 &=1+\sum_{a=1}^{q-1}\gamma_a^{-s}\\
 &\ge 1+(q-1)\exp\left(\frac{s C_{\mathrm{mid}}}{q-1}\right)\\
 &\ge 1+(q-1)\exp\left(\frac{s A_+}{q-1}\right)\\
 &=\max\left\{q,\ 1+(q-1)X^{2s}
                  \exp\left(\frac{sP_{\mathrm{mid}}}{q-1}\right)\right\}.
 \end{split}
\]

This maximum is the strongest bound implied solely by the stated cost lower bound, eigenvalues in `(0,1]`, and at least one unit eigenvalue. For `A>0` the spectrum consisting of one unit and `q−1` copies of `exp(−A/(q−1))` attains it; for `A<=0` the spectrum of `q` units attains it. These examples establish sharpness for those matrix facts, without asserting they are realizations of a specified arithmetic packet.

The exact active rank gives the stronger statement, whenever `rho>0`,

\[
 \operatorname{Tr}U_{q,2q-1}^{-s}
 \ge q-\rho+\rho\exp\left(\frac{sC_{\mathrm{mid}}}{\rho}\right)
 \ge q-\rho+\rho\exp\left(\frac{sA_+}{\rho}\right).
\]

This follows by applying the same proof to precisely the `rho` eigenvalues below one. It improves the `q−1` formula: for fixed `a>=0`, the function `r(exp(a/r)−1)` is decreasing for positive `r`, since its derivative is `exp(a/r)(1−a/r)−1<=0`; the last inequality follows by differentiating `exp(t)(1−t)` on `t>=0`. If `rho=0`, then `D=0`, `U=1`, `C_mid=0`, and the trace is exactly `q`; no division by zero is introduced.

## 4. Ordered transfer to both endpoint pairs

For positive Hermitian forms `M,N` on the original dual quotient coordinates, order the generalized eigenvalues increasingly and write

\[
 \lambda_a(M,N)=\min_{\dim F=a}\ \max_{0\ne x\in F}
                         \frac{x^*Mx}{x^*Nx}.
\]

The formula is proved in the previously read review by the eigenbasis and subspace-intersection argument. It uses the actual positive forms on the dual quotient. Its eigenvalues are those of `M N^−1` on `E`, because `N^−1M` on the dual and `M N^−1` on `E` are related by the invertible map `N`; this supplies the exact domain change.

For every nonzero vector `x`, source inclusion gives

\[
 \frac{x^*K_{q-1}x}{x^*K_{2q-1}x}
 \le\frac{x^*K_qx}{x^*K_{2q-1}x},\qquad
 \frac{x^*K_qx}{x^*K_{2q}x}
 \le\frac{x^*K_qx}{x^*K_{2q-1}x}.
\]

Taking the extrema in the displayed formula proves, for every `a=1,...,q`,

\[
 g_{q-1,2q-1,a}\le g_{q,2q-1,a},\qquad
 g_{q,2q,a}\le g_{q,2q-1,a}.
\]

Since `x↦x^−s` decreases for `x>0`, each endpoint pair separately satisfies

\[
 \operatorname{Tr}U_{q-1,2q-1}^{-s},\quad
 \operatorname{Tr}U_{q,2q}^{-s}
 \ \ge\ \max\left\{q,\ 1+(q-1)X^{2s}
               e^{sP_{\mathrm{mid}}/(q-1)}\right\}.
\]

The rank-refined central lower bound transfers in the same way. The endpoint maps are not asserted to have a unit eigenvalue; the central unit contributes its exact one through the ordered comparison, and its endpoint correspondent contributes at least one. Summing the two endpoint inequalities gives twice the displayed right side. Finally `L_(h,k)/q>=delta k/2` yields the further explicit consequence obtained by replacing `X` with `delta k/(2C_h^bal)` in these lower bounds, while the preceding formulas retain `L_(h,k)` and every finite penalty.

## 5. Principal-angle realization on the full original source

Fix any admitted pair `i<=j`. In the common source `P_j`, let

\[
 \ell_i=L_{i,j}R_i:E_i\hookrightarrow P_j,
 \qquad\ell_j=R_j:E_j\hookrightarrow P_j.
\]

Both are isometries. Let `Pi_i` and `Pi_j` be the orthogonal projections onto their actual images, and `P_(i,j)` the projection onto the entire lower-degree polynomial source. The least-lift formulas give

\[
 P_{i,j}\ell_j=\Pi_i\ell_j=\ell_iT_{i,j},
 \qquad \Pi_j\ell_i=\ell_j I_{i,j}.
\]

The second identity follows because `ell_i x−ell_j x` has zero arithmetic remainder and `ell_j E_j` is orthogonal to the full original relation space. The first follows directly from the first `i+1` coefficients `O_i^−1 B_i^* G_j`. Therefore

\[
 (\Pi_i\Pi_j)|_{\ell_iE_i}=\ell_iU_{i,j}\ell_i^{-1},\qquad
 (\Pi_j\Pi_i)|_{\ell_jE_j}=\ell_jV_{i,j}\ell_j^{-1}.
\]

Their full products on `P_j` additionally contain exactly `dim(P_j)−q` zero eigenvalues. Indeed `Pi_i Pi_j` has image `ell_iE_i`, is invertible on that image, and has kernel `ker Pi_j`; the other product has the corresponding reversed decomposition.

Choose a `G_i`-orthonormal eigenbasis `x_a` of `U`, with eigenvalues `g_a`. These are coordinates for proving the spectral statement; the original quotient basis, Gram matrices and monic source norms remain as above. Define

\[
 u_a=\ell_i x_a,\qquad v_a=\frac{\ell_j I_{i,j}x_a}{\sqrt{g_a}}.
\]

The identities `G_j=G_iU` and `ell_i^dagger ell_j=T` give

\[
 \langle u_a,u_b\rangle=\delta_{ab},\quad
 \langle v_a,v_b\rangle=\delta_{ab},\quad
 \langle u_a,v_b\rangle=\delta_{ab}\sqrt{g_a}.
\]

For `g_a=1` one has `u_a=v_a`. For `g_a<1` define

\[
 w_a=\frac{v_a-\sqrt{g_a}u_a}{\sqrt{1-g_a}}.
\]

The pairs `(u_a,w_a)` are mutually orthonormal. On each of their two-dimensional spans,

\[
 \Pi_i=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 \Pi_j=\begin{pmatrix}g_a&\sqrt{g_a(1-g_a)}\\
       \sqrt{g_a(1-g_a)}&1-g_a\end{pmatrix}.
\]

Their difference has eigenvalues `±sqrt(1−g_a)`, as its trace is zero and its determinant is `−(1−g_a)`. On the remaining common orthogonal complement both projections vanish. Thus, in particular,

\[
 \operatorname{Tr}_{P_j}|\Pi_i-\Pi_j|^{2m}
 =2\operatorname{Tr}_{E_i}(1-U_{i,j})^m\qquad(m\ge1).
\]

The same proof gives the identity for every real `m>0`, with positive spectral powers. The restricted map `mathcal R=Pi_i|_(ell_j E_j)` is exactly `ell_i T ell_j^−1` and is bijective. Its inverse singular-value-power sum is the trace in Sections 3–4. Inverses of the full projection products, which have the explicitly retained ambient zero eigenspaces, are never taken.

## 6. Arithmetic action and the actual relation correction

Retain the arithmetic action `A=M_S`. With

\[
 \mathsf H_n=G_n^{-1}(A^*G_n+G_nA-kG_n),\quad
 W_n=A^*G_n+G_nA-kG_n,\quad
 \mathsf V_n=AK_n+K_nA^*-kK_n,
\]

the original reverse map has the exact typed action defect

\[
 AT_{i,j}-T_{i,j}A
 =\mathsf H_iT_{i,j}-T_{i,j}\mathsf H_j
 =\mathsf V_iG_j-K_iW_j.
\]

Expansion cancels the two occurrences of `K_i A^* G_j` and of `kK_iG_j` and leaves `AK_iG_j−K_iG_jA`. Thus no eigenspace of the positive return is declared an arithmetic invariant merely from its spectral role. The forward identity transport intertwines `A` exactly; the return carries this displayed defect.

Its original relation correction is

\[
 \mathfrak d_{i,j}=\ell_i-\ell_jI_{i,j}
 =\ell_i(1-U_{i,j})-(1-P_{i,j})\ell_jI_{i,j}.
\]

Both summands on the right have the same arithmetic remainder `(1−U)x`; their difference is in `D_j∩D_i^perp`, and

\[
 B_j\mathfrak d_{i,j}=0,\qquad
 \mathfrak d_{i,j}^*O_j\mathfrak d_{i,j}=G_i-G_j.
\]

The original theta primitive of this relation, its support label, all full jets and every sign remain those in the incoming source construction. On one supported fibre, `T^tau` maps `u^bullet` to `(Tu)^bullet` and external `tau` to external `tau`. An actual relation goes to the supported quotient zero; external absence remains external absence. The analytic smallness of a return eigenvalue does not change either support operation.

## 7. Review conclusions and primary-source status

No correction was found in the previously read Sections 2–4, 7 and 8. Their stronger reference gap `1/(Tr(L_i^−1 U_j)−q+1)`, ordered finite-moment error, source-bracket construction, principal-angle blocks, and minimum-eigenvalue transfer are valid as written.

The extension here adds the complete real-exponent inverse-power trace inequality, its sharp maximum with `q`, the exact active-rank refinement, the ordered transfer of the whole spectrum to each endpoint, and the typed inverse-restriction interpretation. The full action defect and source relation correction accompany that spectral extension.

The first complete primary-source read, performed after this initial review, is recorded in Section 8. No numerical checker execution has been represented as a proof of these analytic inequalities.

## 8. Complete read of the first primary source and auxiliary proof

The actual complete `endpoint_restriction_join_20260913.tex`, ERJ.1–45, was read at SHA256 `1b485555492ff48bddf6d171490869a7572b13732031a3d0c4689c60c8273020`. This was a full read from the document class through the final document terminator, not a section-only review. The read covered the original source and full-jet injection, monic quotient/lift proofs, restriction and action, theta primitive, principal-angle blocks including ambient zero eigenspaces, arbitrary-degree remainder, every arithmetic scalar constant, positive source comparison, finite matrix errors, logarithmic tail and rational logarithm errors, interval-to-quotient map, fixed-pair convergence, four-volume scalar growth, exact central telescope, positive-real spectral compression, all inverse powers, ordered endpoint transfer, the auxiliary fixture claims, the empty packet and the identical-degree case.

No substantive error was found. In particular the arbitrary `s>=0` formal quotient expansion, `C_(2q)/C_(2q−1)<=147/5`, the coefficient `16R_0/(3D)` in the scalar majorant, the two distinct factors `r^(p+1)` and `(p+1)g` in the certificate, the reference-pair gap requirement, both signs when multiplying a logarithm interval by a negative binary exponent, and the exact `q` error multiplier agree with the complete proofs in this review and its read source dependencies. The central product keeps both single endpoint contractions, every doubled interior contraction, and every phase term.

Two precision improvements were sent during the author's already planned update: state `C_+=[V→B]` in cohomological degrees zero and one for ERJ.8, identifying the original compatible chain action, so that its two Koszul signs have their literal types; and use the direct tangent inequality proof of the exponential average in Section 3 above, which proves the result for each integer `q−1` in one finite step. The author was already incorporating the explicit `U=T I`, `V=I T` endomorphism types and the exact rank refinement supplied above. A subsequent review entry records the actual resulting bytes once those edits are present.

The complete auxiliary proof `endpoint_restriction_join_fixture_20260913.md`, F.1–35 and its full execution provenance section, was also read at SHA256 `f5ef0746d22ba641aa2fd0d50c0f19954fe9c367d8cacd0206aa1e28f6702b29`. Its gamma integral and beta substitution give the stated Fourier constants, literal masses, convolution and pointwise density identities. Its explicit original `S` Gram matrices, relation maps, monic polynomial tables, exact remainder extremizer, positive source comparison, return spectra, actual source projections, action commutator, determinant ratios and rational logarithm bounds substantiate the claims cited in the primary article. In particular the extremizer has remainder `(763/108)(S−1)`, squared lower-source norm `763/24`, and squared remainder norm `582169/2592`, so their ratio is exactly `763/108`. The original and comparison masses remain `9/16` and `27/70`.

The existing executable bytes have SHA256 `88bcee664a3812dd914e5d164de37d48f4388307e2359062ace360e988d9df14`; the existing full replay JSON has SHA256 `a8205b83417feb94baf903f53f9bdd0d2e38cf325fc28ceaac6a098530b4075d`, matching the proof record. This lane parsed the existing JSON and inspected all sixteen saved job outcomes without running the executable. Every saved job has 303 checks, unique labels, and empty stderr. The two unchanged calculations have zero failed checks and exit code zero. In each mode the seven altered calculations have respectively 20, 30, 36, 8, 24, 23 and 24 failed checks and exit code one, exactly as stated in the proof. The positive saved result records total ratio `3073295611/216513000` and direct trace sum `1446331/362340`. This verifies the primary article's inherited execution counts against their actual saved receipt; it does not claim a new replay or a full reread of the fixture executable.

## 9. Final complete primary-source review

After the author's precision additions, the entire primary `endpoint_restriction_join_20260913.tex` was read again at SHA256 `57f4736193c57fd2de845de9252e719a10b486124cb96a05faeaec54d7801e65`. This second complete read covered all original ERJ.1–45 and the new ERJ.11a and ERJ.42a. The `U=T I` and `Uhat=I T` types, their original identity similarity, the defined interpretation of endomorphism powers, the actual restricted inverse map and its singular-value powers, the cochain degrees and compatible chain action, the dual-to-quotient similarity in generalized eigenvalues, the explicit parentheses for trace of powers, the finite tangent proof, and the exact-rank bound are all present and mathematically correct.

The rank refinement handles `rho=0` exactly and transfers to both endpoint maps through the ordered spectrum, without declaring a unit eigenvalue for either endpoint. The trace maximum remains valid when `2(q−1)log X+P_mid` is negative. The first-window companion is retained as a separately proved dependency with its own constant; no comparison of unlike constants is used in the central estimate.

No unresolved mathematical issue remains in the reviewed primary source. This closes the independent mathematical source review for the exact bytes above and their listed full dependencies. Subsequent document-layout edits require their own file pin and confirmation of their actual scope; this review does not pre-certify unseen source changes, PDF layout, or source-package completeness.

## 10. Final layout pin and exact change verification

The final primary TeX was inspected at SHA256 `a655abd15a8d97c5a896ffefec2f868fab685685f817f290a60a501d6d13feb0`. Its only two changes from the fully reviewed source are: ERJ.38 uses a `gathered` environment with a line break in place of the horizontal `qquad` before the unchanged literal balanced constant; and the four-volume lower-limit expression after ERJ.44 is displayed, with its unchanged ratio written using `frac`.

Both changed passages were read directly. Their exact byte strings each occur once. Reversing only these two substitutions in memory, without writing or changing the primary file, produces SHA256 `57f4736193c57fd2de845de9252e719a10b486124cb96a05faeaec54d7801e65`, exactly the source fully reviewed in Section 9. This establishes the complete scope of the changes by byte identity, rather than relying on an asserted layout-only description. Neither change alters a hypothesis, map, sign, constant, power or conclusion. The mathematical review therefore extends to final source SHA256 `a655abd15a8d97c5a896ffefec2f868fab685685f817f290a60a501d6d13feb0`.

The author separately reports the clean compile and complete ten-page visual inspection. Those PDF checks remain the author's execution and visual-QA record, and are not represented here as newly performed by this independent source-review lane. No mathematical test was rerun for these layout changes.
