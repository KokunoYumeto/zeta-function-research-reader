# Final complete-source audit of CW.1–52

**Status: the entire current source CW.1–52 has been read and mathematically audited; no correction is required.** This review is for the fixed source at output/split_zero_rh_tandem_2026-09-12/tex/conormal_finite_weyl.tex. No proof source, checker, or frozen release was edited. No new mathematical tests, additional agents, or further mathematical extensions were started.

## Exact source scope

- Complete source: 34,006 bytes; SHA256 **731b72e56eb311c456424eb917b090f7d796c34948537112322d162164b41277**.
- CW.1–40 prefix: exactly the first 24,487 bytes; SHA256 **6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a**.
- Appended subsection CW.41–52: the remaining 9,519 bytes; SHA256 **51946d4de348fad2ce0752b0eedccc8b5fa79088c88615aea3e47f24e0b0559c**.

The boundary is immediately after the former final paragraph's explicit \(d\ge1\) projector domain. The appended subsection starts with the original arithmetic unit and complete tensor partial residues. All displayed tags CW.1 through CW.52 occur exactly once and in their stated order. The byte comparison and hashes retain the exact relationship to the previously sealed source; the final source was also read in full, including the preserved prefix.

Direct comparison verifies that the first 24,487 bytes equal the complete retained file work/conormal_finite_weyl_review_20260912/source.tex. The full 34,006 bytes also equal work/conormal_finite_weyl_final_review_20260912/source.tex, the author's final rendering input. Both comparisons returned literal byte equality.

The earlier complete mathematical audit is work/conormal_weyl_formula_audit_20260912.md. The direct PRC.1–11 precursor audit is work/conormal_partial_residue_independent_audit_20260912.md, SHA256 953bc7fc883a80fd06890475f74cd2d911fef2fd3da3898af419f2e2a538ef90, for precursor SHA256 47c8bb06be05a1bc4998518c62392fda6bdb6ebc1bd3a43f26dd1cfec34d7db2. The entire precursor's definitions and proofs have been carried into CW.42–52 with the equation references updated correctly.

## Complete retained proof read

CW.1–11 preserve the original monic polynomial and complete local orders. Repeated monic division proves the full \(h_i\)-adic decomposition and the \(E\)-module isomorphism \(E^k\to I/I^2\). The derivative is a derivation along \(\pi:E^{[2]}\to E\), so \(\Phi(a)=\pi a+\epsilon\delta a\) is a unital algebra homomorphism. Its image, kernel and exact sequence use the displayed complex-linear type for \(\Psi\). The local formula \(h_i'a_i=m_ic_i(0)z_i^{m_i-1}a_i|_{z_i=0}\) preserves every other coordinate and the complete multiplicity; summing all ordered local blocks gives the stated full conormal-row rank \(d^k-(d-r_0)^k\).

CW.12–22 retain \(Z=M_{\sum_i s_i-k/2}\), its thickened multiplication map, the rectangular sign \(Z\delta-\delta\widehat Z=-\pi\), and the canonical section defect. The identities \(\ell_iM_{h_i'}c_i=dI\) prove the commuting idempotents, complete joint decomposition, all multiplicities, trace and rank of the specified correction. The \(d=1\) endpoint is explicitly proved. The corrected CW.20 states the separate metric Hermiticity conditions for each projector and for their sum. The exact common metric transport also gives the original weight formula in CW.21. The typed map in CW.22 relates the section correction to the full conormal row without changing either domain.

CW.23–30 retain the full thickened unit, its inverse and \(\beta_h=U^{-1}\delta\widehat U\). The product rule proves the section derivative, and the fact that the defect lands in \(N=\ker\pi\) proves the complete correction conjugation. The Mellin identities apply to the declared original reference section. The actual degree-\(M\) minimum uses its own constrained coefficient minimum and retains the exact admitted difference \(a_M:E\to N\); its correction changes by \([Z,\delta a_M]\), preserving the trace. The fixed-section ranks are assigned only to their proved operator.

CW.31–38 retain the original \(g=2\xi\), \(g'=h'v_h+hv_h'\), complete residue poles, reflection and positive local-coordinate residue convention. The full ideal image and rank-one correction are related by the explicit precomposition in CW.35. The global logarithmic observation keeps the stated original domains; \([D,\log x]=-I\), the original intertwining identities and \(q\Theta=0\) give the displayed differential and dilation equivariance. CW.39–40 retain the algebra homomorphisms and the split-linear infinitesimal coefficient map with its product rule, including the distinction between supported zero and external absence. The \(h=1\) zero-quotient endpoint remains explicit.

## The appended full-unit corollary

CW.41 is correctly typed in the commutative algebra \(B=E[\epsilon]/(\epsilon^2)\). Its proof uses the previously established unital algebra map:

\[
 \Phi(\widehat U)=\pi(\widehat U)+\epsilon\delta\widehat U
 =U+\epsilon U\beta_h=U(1+\epsilon\beta_h).
\]

Since \(\epsilon^2=0\), multiplication in this same algebra gives

\[
 U(1+\epsilon\beta_h)\,U^{-1}(1-\epsilon\beta_h)=1.
\]

Applying \(\Phi\) to \(\widehat U\widehat U^{-1}=1\) therefore proves precisely
\(\Phi(\widehat U^{-1})=U^{-1}(1-\epsilon\beta_h)\).
The inverse sign is negative, and the full derivative term is retained. The following product-transport sentence uses exactly this algebra homomorphism, with no added section or quotient assumption.

## The appended complete partial-residue proof

CW.42–43 define \(\mathcal R_i:E\to E_{\widehat i}\). The proof descends through every generator of the original ideal: the own-variable difference is holomorphic after division by \(g\), and the other-variable differences vanish in the declared coefficient algebra. Reduction of the complete inverse unit gives
\(\mathcal R_i=\ell_iM_{v_i}^{-1}\).
The coefficient of \(s_i^{-1}\) at infinity, rather than the residue at infinity, supplies the positive sign. The positively oriented ordinary residue includes no extra \(2\pi i\); the contour version has exactly its displayed reciprocal factor.

CW.44–46 set \(A_i=M_{\gamma_i}c_i:E_{\widehat i}\to E\) and \(C_i=A_i\mathcal R_i:E\to E\). The complete original identity \(\gamma_i=v_i h_i'\) yields \(\mathcal R_iA_i=dI\). This proves injectivity of \(A_i\), surjectivity of \(\mathcal R_i\), \(C_i^2=dC_i\), rank \(d^{k-1}\), and trace \(d^k\). Tensor factors give the stated commutation exactly. The displayed right inverse also contracts to the identity in its declared coefficient algebra.

CW.47–49 preserve the actual product unit \(U=v_iU_{\widehat i}\). The maps \(c_i\) and \(\ell_i\) are \(E_{\widehat i}\)-linear, so the full other-variable unit cancels between its corresponding source and target actions. The remaining operator is exactly

\[
 M_U M_{h_i'}c_i\ell_iM_U^{-1}
 =M_{\gamma_i}c_i\ell_iM_{v_i}^{-1}=C_i.
\]

This proves \(\mathsf J_U=k^{-1}\sum_iC_i\) with the original \(1/k\). The term \(M_{\beta_h}\) remains in \(\mathsf D_U\); its commutator vanishes because it and the original \(Z\) are multiplication maps in the same commutative algebra.

CW.50–52 retain the complete iterated coefficient residue in all variables. Evaluating on pure tensors and extending linearly proves
\(\mathcal R_{\rm all}=\ell_h^{\otimes k}M_U^{-1}\)
and
\(C_1\cdots C_k=(\prod_i\gamma_i)\mathcal R_{\rm all}\).
The iterated evaluations operate in independent variables and introduce no permutation sign. At every retained centre the local logarithmic derivative is
\(g'/g=m_\rho/(s-\rho)+u_\rho'/u_\rho\),
with \(u_\rho\) nonvanishing. Therefore the column-functional contraction is \((\sum_\rho m_\rho)^k=d^k\). It is nonzero, proving the full product's rank one, exact eigenvalue and trace \(d^k\), and square equal to \(d^k\) times itself.

The final \(d=1\), \(k=1\), and \(h=1\) paragraphs agree with the earlier domains and formulas. Complete repeated fibres and mixed nilpotent coefficients survive in the coefficient algebras before the displayed final functionals are evaluated.

## Existing numerical and rendering evidence

The sealed finite checker and its four receipts remain attached to the unchanged CW.1–40 prefix, not relabelled as tests of newly appended formulas. Its report is output/split_zero_rh_tandem_2026-09-12/checks/conormal_finite_weyl_report.md, SHA256 03179fc8029ce92120ed518df62ac7fe508914dc6aeaa14f413278e0326abde9. The normal and optimized runs have identical arrays of 1,076 passing records: 991 exact checks and 85 negative controls. The two deliberate-failure runs have the same 1,076 passing records followed by one intentional false identity and both exit with code 1. These are exact finite calibration records with their declared units and metric; they do not replace the complete proofs above.

The proof author reports a clean nine-page final wrapper and visual inspection of all nine rendered pages. Rendering was not duplicated in this mathematical-audit lane. This report seals the exact complete proof source and the mathematical integration; the separate rendering receipt remains the rendering evidence.
