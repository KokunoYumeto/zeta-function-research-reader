# Independent review of the finite-circle propagation

Review date: 2026-09-13. Outcome: **mathematical PASS for the reviewed two-bound cut**. Two presentation repairs and an R58 byte-hash metadata repair were sent to the author; their status is recorded separately below.

I read every line of the original and revised periodized_source_intake_proofs.tex and periodized_curvature_control_bridge.tex, and the complete R58_OLD.tex and R58_NEW.tex. This is a review of the full affected proof contexts and their original source maps, not a compilation or search receipt. I made no source edits.

## Physical file pins at the time of review

| File below this directory | SHA-256 |
|---|---|
| originals/tex/periodized_source_intake_proofs.tex | 227e6307140c35e9be8ec93e973973c9e4b265a8acf2506c6a3056ffb6c91e8f |
| staged/tex/periodized_source_intake_proofs.tex | af9881317aff2260043d13217f4659a2137cbd94dd6b3282aae0033fb38ee51e |
| originals/tex/periodized_curvature_control_bridge.tex | f443846eec3381061b34428c6c2970e8e49f7a276f9b861bd55b1eb82882e80e |
| staged/tex/periodized_curvature_control_bridge.tex | 15b2ec82c244a645e132951ef5d124fc35fd4a0afed1a43d2f07d572e7734914 |
| conclusion_replacements/R58_OLD.tex | c79b1efcdac8e2757c4e97f502aac1a06229d9082050bdecd60197a9e56f8380 |
| conclusion_replacements/R58_NEW.tex | b321b188340b933d7a0c781711c16c8ca170cd61dfe33653f34a4d6011d4ff0d |

The two revised proof-file pins match PATCH_MANIFEST.json v2. R58_MAP.json at this cut recorded different old/new hashes, apparently of line-ending-converted text rather than the physical files. That issue was reported with the exact physical hashes above. This review uses the physical bytes.

## Actual source and restriction maps

The retained source is the original polynomial image under \(\mathcal V_{h,k}\), followed by the explicitly invertible map \(\mathcal U_k\). The coordinates \(y_i=r+z_i\), \(y_k=r\) have ordered determinant \((-1)^{k-1}\); the density \(e^{kr+\sum z_i}\) and square-root factor in \(\mathcal U_k\) make the displayed norm equality exact. Differentiation gives \(\mathcal U_kD^{(k)}=(-\partial_r+k/2)\mathcal U_k\), retaining the original sum coordinate.

The original polynomial inclusions commute with this fixed column map. They therefore pull back the original, weighted, derivative and sampled degree-\(D\) Grams to their degree-\(N\) counterparts. In particular, the map \(I_{2q,D}:\mathcal P_{2q}\hookrightarrow\mathcal P_D\), \(D=2q+2\), gives exactly
\[
M^{(0)}=I_{2q,D}^*M_DI_{2q,D}=M_{2q},\qquad
M^{(1)}=I_{2q,D}^*M_D(L,J)I_{2q,D}=M_{2q}(L,J).
\]
The new four-determinant calculation uses these two forms on \(\mathcal H=\mathcal P_{2q}\); the two extra degrees remain available for the generator raises. There is no enlargement of the four-determinant trace dimension to \(2q+3\), and no substitution of Gamma moments for sampled arithmetic moments.

In all these restrictions, the remainder map is the same \(J_N:\mathcal P_N\to E\). The canonical section \(C_N=M_N^{-1}J_N^*G_N\) satisfies \(J_NC_N=I\) and \(C_N^*M_NC_N=G_N\). Writing a lift as \(C_Nv+z\), \(J_Nz=0\), makes the cross term vanish and proves its minimum norm. Consequently the sampled and original sections differ in \(\ker J_N=\chi\mathcal P_{N-q}\). The displayed monic division and tensor signs continue to give that difference's original theta primitive; the revised metric bounds do not remove the relation-valued difference.

## Fourier factors, positivity and the zero coefficient

The orthonormal mode \(L^{-1/2}e^{-2\pi inr/L}\) has coefficient \(L^{-1/2}\widehat\psi(2\pi n/L)\). Thus its zero coefficient is \(L^{-1/2}\widehat\psi(0)\), its constant function contribution is \(L^{-1}\widehat\psi(0)\), and the augmented unscaled vector \(\widehat\psi(0)\) carries the metric factor \(L^{-1}\). The identity \(M(L)=M^\times(L)+L^{-1}Z_0^*Z_0\) retains all three roles without interchanging them.

Plancherel in the \(k-1\) original relative variables gives \(\|\widehat\psi(u)\|_{\mathcal K}^2=2\pi m_{h,k}(u)\). Hence the scalar sampled moment weights are exactly \((2\pi/L)m_{h,k}(2\pi n/L)\); R58's vector-valued and scalar formulas agree. The finite cutoff includes \(n=0\), with its original \(L^{-1}\) contribution. Nothing in the new common-source restriction removes it.

The positive omitted Fourier Gram supplies an asymmetric bound. Weighted correlation Cauchy--Schwarz and both nonzero lattice directions give the period coefficient \(1/(e^{aL}-1)\); integration by parts and both frequency tails give \((L/(2\pi J))^{2p-1}/(2p-1)\). Therefore
\[
\alpha M_N\preceq M_N(L,J)\preceq\beta M_N,\quad
\alpha=1-\eta_P-\eta_T>0,\quad\beta=1+\eta_P.
\]
The budgets and explicit choices FC3a prove \(\alpha>0\), including the zero derivative-Gram case. Positivity of the sampled Gram follows from this bound, including \(k=1\), without an unsupported assertion that every sampled weight is strictly positive. Restriction and the quotient minimum preserve these factors exactly.

## Reproduced finite algebra at PSA24a--PSA25

In the new path \(M(x)=(1-x)M^{(0)}+xM^{(1)}\), the actual relation matrix remains \(B_N:\mathcal P_{N-q}\to\mathcal P_N\); its common-source column is \(I_NB_N\). Substitution gives precisely the projector formula in PSA24c and its original relation Gram \(B_N^*I_N^*M(x)I_NB_N\).

The ordered frame \([s_N,B_N]\) has determinant one because \(\chi\) is monic. Its Schur complement is the same remainder minimum Gram already proved in PSA17--PSA18. Thus PSA24d's determinant ratio computes that actual Gram, not a new quotient norm. Differentiating it gives \((\log V_N)'=\operatorname{Tr}((P_N-Q_N)C)\), and the four signs give \(\mathcal B'=\operatorname{Tr}((U-W)C)\).

The full nested flags give the two spectra \(0^{[q]},1^{[2]},2^{[q-1]}\). Their rank is \(q+1\), trace \(2q\), and trace of the square \(4q-2\). The repeated eigenvalue is retained. Decomposing each operator into its rank-\(q+1\) range projection and rank-\(q-1\) eigenvalue-two projection gives the printed AW bound by the complete ordered projection-trace inequalities. The common range projection is dominated by both \(U,W\); subtracting it gives trace-norm bound \(4q-2s\). The trace-square identity and Cauchy--Schwarz give the retained cross-trace refinement. Subtracting the scalar midpoint of \(C\)'s spectrum leaves its pairing with \(U-W\) unchanged, giving the factor \(d/2\). Both bounds concern the same derivative and hence admit their pointwise minimum.

Every eigenvalue \(b_j\) of \(D_{L,J}=(M^{(0)})^{-1}M^{(1)}\) lies in \([\alpha,\beta]\). The exact factorization gives \(c_j(x)=(b_j-1)/(1-x+xb_j)\), in the same order, and \(\int_0^1c_j=\log b_j\). Consequently PSA25 correctly proves
\[
|\mathcal B(L,J)-\mathcal B|
\le\mathcal J_{L,J}
\le\log\frac{b_{q+2}}{b_q}
2\sum_{j=1}^{q-1}\log\frac{b_{2q+2-j}}{b_j}
\le(2q-1)\log(\beta/\alpha).
\]
The coefficient is \(1+2(q-1)=2q-1\). Borel rank strata and bounded positive Grams justify the minimum integral. This explicitly strengthens the earlier coefficient \(2q\) at the original proof site while preserving its asymmetric source allowance.

## FC13a, R58, and limits of the transferred statement

FC13a uses exactly the restriction and signed determinant proof just reviewed. Its source operator acts on \(\mathcal P_{2q}\). FC13 remains a separate dimension-free residue estimate on \(E\); the inserted canonical-section identities give the exact norm-preserving arrow from the quotient to each original source and retain its sampling difference. No equality between the source trace and residue scalar is inferred.

The preceding FC9--FC13 source/quotient minimum and inverse-order arguments remain unchanged. The following FC14--FC29 generator and commutator transfer remains unchanged, including the square-root isometry, the ordered commutator, its convergent Sylvester integral and the original residue terms. FC13a does not replace any of those controls by a determinant bound.

R58_NEW reproduces the same four-determinant minimum and relative-spectrum formula, with the same \(D=2q+2\) source restriction, original \(\alpha,\beta\), zero mode, Taylor-source data and primitive. The coefficient update is made in the result paragraph itself. Fixed positive budgets give an error bounded by a constant times \(q_k\); dividing by \(q_k\log k\) tends to zero as \(k\to\infty\). This makes no bound on the required \(L,J\) or the original weighted and derivative Grams, which remain explicitly evaluated quantities.

At \(q=1\), the four endpoint degrees are \(0,1,1,2\); the middle factors coincide. The relation domain at \(N=0\) is zero and has determinant one. The eigenvalue-two multiplicity is zero, the indexed sums are empty, and the estimate is \(\log(b_3/b_1)\le\log(\beta/\alpha)\). The two generator raises still fit in \(D=4\). No dimension restriction from the proper-constituent residue subsection (\(q>1\)) is imposed on this finite-source result.

The same-arrow extension to sampled forms uses proved positive source bounds; it requires no positivity of an unrelated coefficient matrix. A later nonlinear moment-specific refinement must retain the actual moment measure on \(S=k/2+iu\); this two-bound cut does not assert such a refinement for arbitrary positive matrices.

## Requested presentation repairs

In the reviewed PSA cut, the prose “squared trace” should read “trace of the square.” Its displayed formula already means \(\operatorname{Tr}(U^2)=\operatorname{Tr}(W^2)=4q-2\).

The display written \(\operatorname{Tr}(U-W)^2\) should be parenthesized as \(\operatorname{Tr}((U-W)^2)\). The subsequent argument unambiguously uses the latter; it must not be read as \((\operatorname{Tr}(U-W))^2\), which is zero. The formula's mathematical content in the proof is correct.

The author was notified of both presentation repairs and of the physical R58 hash mismatch. The algebraic acceptance above is tied to the displayed physical file pins and does not certify later unreviewed changes.
