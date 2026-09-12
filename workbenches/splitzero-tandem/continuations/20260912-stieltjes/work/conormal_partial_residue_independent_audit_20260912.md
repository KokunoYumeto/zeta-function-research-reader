# Independent audit of the partial original residue continuation

The full continuation PRC.1–11 was read and checked. **No mathematical correction is required.** This report applies to work/conormal_partial_residue_continuation_20260912.md, SHA256 47c8bb06be05a1bc4998518c62392fda6bdb6ebc1bd3a43f26dd1cfec34d7db2, and its stated sealed CW source, SHA256 6ca142ec052ad110e3c58ece4d81bf87a33fc18c8533c41deb863bceb300715a. Neither source was edited. This is a mathematical read; no tests or additional agents were run for it.

The complete positive-degree hypotheses are used: the monic packet \(h=\prod_\rho(s-\rho)^{m_\rho}\) includes each selected zero with its full order, \(d=\deg h\ge1\), and \(k\ge1\). Thus \(v_h=g/h\), with the original \(g=2\xi\), is holomorphic and invertible at every selected centre, and its full jet is a unit in \(E_h=\mathbb C[s]/(h)\). No simplicity or reflection-closure assumption is needed for these complex-linear residue operators. For comparison to the reflected CW form, the first argument is exactly the constant \(1\), whose reflected conjugate is still \(1\).

## Types and the coefficient-valued residue identity

Retain the specified factor order in \(E=E_h^{\otimes k}\). For \(F_i=E_{\widehat i}\), the maps have the exact types

\[
 \ell_i,\mathcal R_i:E\longrightarrow F_i,\qquad
 c_i:F_i\longrightarrow E,\qquad
 A_i=M_{\gamma_i}c_i:F_i\longrightarrow E,\qquad
 C_i=A_i\mathcal R_i:E\longrightarrow E.
\]

All these maps are \(F_i\)-linear, where the action on \(E\) is through the canonical constant-in-\(s_i\) inclusion. The residue in PRC.1 is well-defined: a change by \(h(s_i)p\) changes the integrand by \(p/v_h(s_i)\), holomorphic at each selected centre; a change by another generator \(h(s_j)p\) has zero class in \(F_i\). This argument applies to the entire defining ideal by linearity and multiplication by arbitrary polynomial coefficients.

For a representative \(u\), let \(p\) be the complete remainder of \(v_i^{-1}u\) in the \(i\)-th factor. Locally \(u/v_h-p\) is divisible by the full selected power of \(s_i-\rho\); hence \(u/g-p/h\) is holomorphic there. Coefficientwise partial fractions of \(p/h\), over the finite-dimensional algebra \(F_i\), therefore give

\[
 \mathcal R_i(u)=\ell_i(p)=\ell_iM_{v_i}^{-1}(u).
\]

The sign in this identity is positive: the coefficient of \(s_i^{-1}\) in the expansion at infinity equals the sum of the coefficients of \((s_i-\rho)^{-1}\) at finite poles. The residue at infinity itself would be the negative of that coefficient; PRC.2 explicitly uses the coefficient. The stated positively oriented contour convention contributes \(1/(2\pi i)\) per ordinary residue and no additional factor in the residue notation.

## Rank, multiplicities, and the exact CW conjugation

The literal derivative identity \(g'=h'v_h+hv_h'\) gives \(\gamma_i=v_i h_i'\) in \(E\). Consequently

\[
 \mathcal R_iA_i
 =\ell_iM_{h_i'}c_i=dI_{F_i},
\]

because \(h'\) has degree \(d-1\) and leading coefficient \(d\). This single typed identity proves that \(A_i\) is injective and \(\mathcal R_i\) is surjective. It yields

\[
 C_i^2=dC_i,\quad
 \operatorname{rank}C_i=\dim F_i=d^{k-1},\quad
 \operatorname{Tr}_E C_i
 =\operatorname{Tr}_{F_i}(\mathcal R_iA_i)=d^k.
\]

The explicit right inverse of \(\mathcal R_i\) is also correct:
\(\mathcal R_i(v_i s_i^{d-1}c_i(a))=a\).
Maps \(C_i\) and \(C_j\) act as the original one-factor endomorphism on distinct tensor factors, so their compositions commute without signs.

For the exact product unit \(U=v_iU_{\widehat i}\), the cancellation in PRC.8 is typed by

\[
 M_{U_{\widehat i}}c_i
 =c_iM_{U_{\widehat i}|F_i},\qquad
 \ell_iM_{U_{\widehat i}^{-1}}
 =M_{U_{\widehat i}^{-1}|F_i}\ell_i.
\]

Thus the full other-variable unit and its inverse cancel inside \(F_i\), while the original \(v_i\) remains:

\[
 M_U M_{h_i'}c_i\ell_iM_U^{-1}
 =M_{v_i h_i'}c_i\ell_iM_{v_i}^{-1}
 =C_i.
\]

This proves exactly the claimed \(\mathsf J_U=k^{-1}\sum_i C_i\) from CW.25. The full thickened unit derivative remains \(M_{\beta_h}\) in \(\mathsf D_U\). It commutes with the original \(Z=M_{\sum_i s_i-k/2}\) because both are multiplication in the same commutative algebra; its zero contribution to the commutator deletes no term from \(\mathsf D_U\).

An explicit connection to every CW joint eigenspace follows. With the original \(P_i=d^{-1}M_{h_i'}c_i\ell_i\), one has

\[
 \frac{C_i}{d}=M_U P_iM_U^{-1},\qquad
 \prod_{i\in T}\frac{C_i}{d}
 \prod_{i\notin T}\left(I-\frac{C_i}{d}\right)
 =M_U P_T M_U^{-1}.
\]

Hence the joint projector retains rank \((d-1)^{k-|T|}\), and \(\mathsf J_U\) acts on its image by \(d|T|/k\). This proves the exact relation between the partial-residue presentation and the complete CW spectrum in the original unit coordinates.

## Full tensor residue and endpoints

Ordered iterated residue evaluation on pure tensors is the product of the one-factor evaluations. Pure tensors span \(E\), so this proves both order independence and

\[
 \mathcal R_{\mathrm{all}}=\ell_h^{\otimes k}M_U^{-1},\qquad
 C_1\cdots C_k=q\,\mathcal R_{\mathrm{all}},
 \quad q=\prod_i\gamma_i.
\]

These are ordinary iterated coefficient residues; no graded wedge permutation is being performed. Therefore reordering the evaluations introduces no sign.

At every selected centre, the complete local factorization
\(g(s)=(s-\rho)^{m_\rho}u_\rho(s)\), with \(u_\rho(\rho)\ne0\), gives
\(g'/g=m_\rho/(s-\rho)+u_\rho'/u_\rho\).
Its residue is exactly \(m_\rho\), including repeated roots. Tensoring those literal one-variable contractions gives

\[
 \mathcal R_{\mathrm{all}}(q)
 =\left(\sum_\rho m_\rho\right)^k=d^k.
\]

Since \(d^k\ne0\), both the column \(q\) and the functional are nonzero. Their rank-one product has square \(d^k\) times itself, nonzero eigenvalue and trace \(d^k\), and kernel dimension \(d^k-1\). The exact link to the preceding correction sum is

\[
 d^{-k}C_1\cdots C_k=M_U P_{\{1,\ldots,k\}}M_U^{-1},
 \qquad
 \mathsf J_U(C_1\cdots C_k)=d(C_1\cdots C_k).
\]

Thus the full product's eigenvalue \(d^k\) and the correction sum's eigenvalue \(d\) on that same one-dimensional image are connected by the displayed projector.

For \(d=1\), \(E\) is one-dimensional and each \(C_i\) is the identity, so both the sum correction and full-product correction are the identity. For \(k=1\), \(F_i=\mathbb C\), and PRC.1–11 reduce to the constant-first-argument residue functional and rank-one operator of CW.31–33. The \(h=1\) endpoint is excluded from the positive-degree formulas and has the zero quotient; no negative-degree coefficient functional or false positive rank is asserted there.

All other-variable nilpotent coefficients survive in the partial residue codomain, and the full product applies the scalar residue only after the entire tensor input has been retained. The argument introduces no orthogonalization, metric assumption, or replacement of the original arithmetic unit.
