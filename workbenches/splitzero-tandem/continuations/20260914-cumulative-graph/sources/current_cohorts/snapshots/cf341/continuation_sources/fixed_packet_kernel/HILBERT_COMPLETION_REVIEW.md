# Independent Hilbert-completion review

Parent assignment, verbatim:

> Please boundedly independently review operator-vanishing corollary now being written fixed_packet_hilbert_completion.tex (wait until file exists, no edits). Focus ||T_N||→0 with all derivative triangular entries, K^-1=T* (TKT*)^-1 T, actual G≤A_kGσ, density χP in original L2 and exact algebraic0→P/χP→L2/χP→L2/P→0, original canonical lifts and theta representative. I am writing proof/source formulas; no need web or numerical test. Send urgent issues; saved brief review.

The owner subsequently specified the final filename `hilbert_completion_geometry.tex`. This review did not edit that source. The parent retains the complete original user-input provenance.

## Independent derivation before reading the completed source

The already reviewed fixed-Gamma theorem implies the required operator conclusion, beyond its determinant conclusion. On an off-critical block every lower triangular entry of multiplication by \((C_{\epsilon_i}(w)N^{\epsilon_iw/2})^{-1}\) is bounded by a constant times \(N^{-|\delta_i|/2}(1+\log N)^{m_i-1}\). On a critical block the largest diagonal entry is \((\log N)^{-1/2}\). Both vanish. Thus \(\|T_N\|\to0\) in the actual fixed finite-dimensional jet frame. If \(A_N=T_NK_NT_N^*\to H>0\), then

\[
K_N^{-1}=T_N^*A_N^{-1}T_N,\qquad
\|K_N^{-1}\|\le C\|T_N\|^2\longrightarrow0.
\]

The exact original CRT map gives \(G_N^\sigma=E_\chi^*K_N^{-1}E_\chi\to0\). The retained arithmetic quotient comparison \(0<G_N^{\rm ar}\preceq A_kG_N^\sigma\) therefore yields operator-norm convergence to zero for the original arithmetic Gram. Since the original canonical lift satisfies \(\|R_Nx\|_{L^2(m)}^2=x^*G_N^{\rm ar}x\), its full operator norm tends to zero as well.

For every fixed polynomial P with original remainder x, taking N large enough for P to lie in the degree-N source gives \(P-R_Nx\in\chi\mathbb C[S]\) and \(\|P-(P-R_Nx)\|\to0\). Hence polynomial density proves density of the original ideal \(\chi\mathbb C[S]\). The density of polynomials also follows directly from the two-sided exponential moment of the original measure: an orthogonal vector defines an exponentially integrable measure with all moments zero, whose analytic Fourier transform is therefore zero, forcing that vector to vanish almost everywhere.

With \(\mathcal P=\mathbb C[S]\subset\mathcal H=L^2(m)\), the sequence

\[
0\longrightarrow\mathcal P/\chi\mathcal P
\longrightarrow\mathcal H/\chi\mathcal P
\longrightarrow\mathcal H/\mathcal P
\longrightarrow0
\]

is exact in complex vector spaces. No everywhere-defined action of the unbounded multiplication operator S on \(\mathcal H\) is available from this argument. With their inherited norm-quotient topologies, all three displayed quotients are indiscrete. If the left term is instead identified with E carrying its ordinary finite-dimensional Hausdorff topology, the injection into \(\mathcal H/\chi\mathcal P\) is not a topological embedding. The sequence splits algebraically, so no blanket prohibition on algebraic splitting or on splitting between indiscrete quotients is valid.

For the original map \(J:\mathcal P\to E\) with E in its ordinary Hausdorff topology, the vanishing lifts imply that the graph closure contains every \((0,x)\). The graph itself contains \((P,JP)\); adding a vertical vector gives \((P,x)\) for arbitrary x in the closure. Polynomial density then gives the entire \(\mathcal H\oplus E\). In particular J is not closable when \(q=\dim E\ge1\), and there is no continuous extension \(\mathcal H\to E\).

## Full source verification: FKG.1–FKG.23

The completed `hilbert_completion_geometry.tex` was read in full, including the original tensor-source representative and the complete quartet calculation. No decisive defect was found. The operator argument and the topological statements have the precise scope established above. The owner narrowed the introduction to the actual complete counterfactual quartet so that it invokes exactly the established arithmetic envelope.

FKG.2 is the correct Taylor product formula: for \(d=j-l\), its entry is \(N^{-\epsilon_iw_i/2}\sum_{r=0}^d a_i^{[r]}(w_i)(-\epsilon_i\log N/2)^{d-r}/(d-r)!\). Hence the bound includes every triangular derivative entry. The inverse-congruence identity, positive eigenvalue lower bound for \(A_N\), and the rate FKG.5 are valid. FKG.6 uses the actual canonical least-norm lift in the arithmetic form. The comparison FKG.7 follows by taking the arithmetic minimum and evaluating its upper bound on the Gamma minimizer; no commutation of the two Grams is assumed.

FKG.8 retains the full unit \(\upsilon_h\) in the original injection. Thus the nonzero class in FKG.9 is independent of N while its actual canonical source norm tends to zero. The k Mellin Plancherel factors in FKG.10 are exactly \((2\pi)^{-k}\); they are already contained in \(\prod_iw_h(t_i)\). Passing to the sum coordinate has determinant one. Consequently the tensor-source norm equality preserves both its original measure \(dx_1\cdots dx_k\) and every scalar factor.

FKG.11 is monic division of the literal difference of the original arithmetic lifts. In FKG.12, vanishing in the tensor residue algebra implies zero final multivariable remainder, so successive monic division gives an exact polynomial identity. The primitive FKG.13 has one degree-zero factor in position i and k−1 degree-one factors. Its written \((-1)^{i-1}\) cancels the tensor differential sign from the preceding i−1 factors. The commuting Euler operators then give exactly FKG.14. The retained source `algebra/counterfactual_algebra.tex`, CA.29–CA.30, confirms the same Gaussian seed \((4\pi^2x^4-6\pi x^2)e^{-\pi x^2}\) and its Mellin theta identity. No original unit or nilpotent coefficient is replaced.

The direct density argument in FKG.15 is valid: after the exponential moment at any \(\eta<\pi/2\), the finite measure \(\overline f\,m_{h,k}\,du\) has an exponential moment at every smaller order than \(\eta/2\), by Cauchy–Schwarz. Orthogonality to polynomials in S is equivalent to vanishing of all u moments because \(S=c+iu\) is invertible affine. Its analytic Fourier transform is consequently identically zero. Fourier uniqueness gives f=0 almost everywhere. FKG.16–FKG.17 then show density of the original relation ideal using the canonical lift approximation itself.

All arrows in FKG.18 are well-defined and exact as complex-linear maps. Injectivity of the embedded polynomial evaluation ensures that the kernel of j is exactly literal divisibility by χ. The kernel of π is precisely the image of polynomial cosets. FKG.19 is the correct Hausdorff reduction map and has zero target because the ideal is dense. The source does not make a false claim that the algebraic sequence cannot split.

FKG.20 correctly chooses N_j after fixing the polynomial P_j and the possibly large vector x−JP_j. This adaptive order is necessary and sufficient for the norm correction to be below 1/j. It proves the full graph closure, not merely noncontinuity on selected vectors. The explicit condition q≥1 gives nonclosability. The support-preserving lifts leave τ fixed and send a killed amplitude to its specified supported zero; no original arithmetic class is identified with the external point.

The roots and multiplicities in FKG.21 match the retained HT.1–HT.2 exactly. The nonzero top coefficient of the sum of the k nilpotents gives index \(\ell_k=1+k(m-1)\); all pairs of independent real/imaginary sign counts occur, and \(\delta\gamma\ne0\) makes the resulting sums distinct. Summing their real deviations gives

\[
\mathcal A_\chi
=\delta\ell_k(k+1)\sum_{a=0}^k|2a-k|
=2\delta\ell_k(k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\]

This equals the original \(\mathcal L_{h,k}\) exactly as defined in `shared_thread_audit/segment55_67/actual_holonomy_counterfactual.tex`, HT.8. Critical roots exist exactly when k is even and then number k+1, each of multiplicity \(\ell_k\), so \(\mathcal B_\chi=(k+1)\ell_k^2\) in that case and zero otherwise. The distinction between the proved Gamma logarithmic correction and the merely leading arithmetic rate in FKG.23 is stated correctly.

The final added source formula FKG.17a was read and checked. It extends the isometry in FKG.10 on the precise closed source subspace \(\mathcal C=\overline{\mathcal V(\mathcal P)}\) in the original tensor L² space: polynomial density extends \(\mathcal V\) uniquely to an isometry \(\mathscr H_{h,k}\to\mathcal C\). Its range is closed and contains the dense original image, so it is onto. The actual exact boundaries \(\mathcal V(\chi\mathcal P)\) are dense in \(\mathcal C\). The source correctly restricts its density claim to this displayed closed source subspace.

The separate density reviewer read the original `output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/nested_relative_frame_density.tex`, lines 1–287, including ND.3–ND.12. It confirmed the required exponential decay, analytic Fourier transform, Gaussian formula and sign, absolute Fubini interchange, approximate identity, and uniqueness for finite complex measures. That full source review found no missing density or uniqueness premise in FKG.15–FKG.20.

Final reviewed source SHA-256: `C001D1CD77F46A0918AD6B45E0734C2D437C53664ED38F04C23B182FA2FE8D08`. The final two-line gathered layout of FKG.17a was also inspected; its mathematics is unchanged. All FKG.1–FKG.23 claims, including FKG.17a, pass this review. No changes to the mathematical source are requested.
