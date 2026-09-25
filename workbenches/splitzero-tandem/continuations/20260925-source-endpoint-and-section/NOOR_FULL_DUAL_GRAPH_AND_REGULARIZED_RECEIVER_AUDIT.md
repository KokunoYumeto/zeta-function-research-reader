# Independent review of the full Noor graph and regularized receiver

Review date: 25 September 2026. Stable review locators **NHDA0–NHDA8**.

## NHDA0. Exact edition, source coverage and outcome

Reviewed proof: NOOR_FULL_DUAL_GRAPH_AND_REGULARIZED_RECEIVER.md, complete NHD0–NHD10.

Reviewed SHA256:

45D9E99FD92871FAD752A7433D86789D9356EAAB08FFB5F5508238BEE83A0F93.

The complete written proof was read. Its final right-branch notation repair, the corrected \(\qquad\), and the explicit denominator \(2\,a!\) were checked after the mathematical review. No mathematical defect remains identified in the scope below. This is an internal independent mathematical review, not external human peer review.

The receiving source NOOR_ORIGINAL_ZETA_JET_RECEIVER.md was read completely, NHR0–NHR9, at SHA256

37E08DEE8224D95394133EF39EE2FCBCC8267195BABE2EC192A58440A7A3D1C1.

Relevant synthesis inputs inspected were GSP0–GSP1, GSP4 and GSP7, with the convergence and topological conclusions in GSI6–GSI12. Their source hashes are respectively

FB436828944ACCD8AAC94183E729F6C55054F94E21FCCCDA06C4B1180CBA9598,

EB4BE8E83D351FCD77C6377B8AB386AA48D01705E0CD61F3D96254D61137DB14.

SDT0–SDT6 was reread, including the actual finite-net, quotient compactness, compact lifting, strong-subspace topology and bidual proofs, at SHA256

7F1A03A6225F1DFC22B167713C0DDBB154635B06F9479F6137B229845B67AEFC.

This audit does not newly read the entire human Noor paper. Its original-author-source identity and the received reading scope are documented in NHR1 and the incoming receipt. The current receipt inspected here has SHA256

4EC1F5E4A275FF37DAFD021DA2FC8C51C1A246EE4D11B6E4E6682B5682696184.

It includes a later NAD continuation. NHD0 reports its earlier receipt reading at a different hash; that is a historical reading record, not the hash of this subsequently extended receipt. The NHR proof itself still has the exact hash above.

The task's construction guide and correction chain were recalled. Every object in this audit occurs after complete-history arithmetic reconstruction. The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\), without arithmetic, a coordinate, a metric, or retracted addition on the support. No branch measures are pooled.

## NHDA1. The right-branch completion has the claimed original topology

The final notation
\[
I_{\mathrm{right}}=\{F\in\mathcal B:
F^{(a)}(\rho)=0\quad
(\Re\rho>1/2,\ 0\le a<m_\rho)\},
\quad
Q_{\mathrm{right}}=\mathcal B/I_{\mathrm{right}},
\quad
N_{\mathrm{right}}=I_{\mathrm{right}}/I
\]
is distinct from the normal-shift ideal \(I_+\) and source \(Q_+\) in ADM/FOD. No spectral translation occurs in forming this branch quotient.

Each indicated derivative evaluation is continuous by Cauchy's estimate on a fixed small circle in a vertical strip. Consequently \(I_{\mathrm{right}}\) is closed. The quotient \(Q_{\mathrm{right}}=Q/N_{\mathrm{right}}\) has the actual Fréchet quotient topology.

The use of SDT for this kernel is valid, for the reasons actually given there. SDT2's compact finite-net estimate is a property of the original weighted source norms. To prove bounded-compactness of a quotient by a closed kernel, SDT3 chooses representatives separately for the one stronger seminorm needed for each output seminorm; it does not assume one simultaneous bounded family of representatives. SDT4's compact lifting construction uses a complete Fréchet source and a closed kernel. It therefore applies first to \(A\to Q_{\mathrm{right}}\), then to \(Q\to Q_{\mathrm{right}}\), since the latter target has the just-proved bounded-compact property.

These statements give bounded lifts and hence the exact strong topological identification
\[
D_{\mathrm{right}}=(Q_{\mathrm{right}})'_\beta
\simeq N_{\mathrm{right}}^\perp\subset Q'_\beta.
\]
SDT6's compact absolutely convex hull argument gives
\[
(D_{\mathrm{right}})'=Q_{\mathrm{right}}
\]
through evaluation, with no added product topology on the jet data.

The Gaussian finite-rank operators \(K_j\) preserve \(N_{\mathrm{right}}\), since they are source multipliers. In the full formula
\[
K_j=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_{1/j}^{(a)}(\rho)}{a!}(L-\rho)^aP_\rho,
\]
a transpose applied to \(\lambda\in D_{\mathrm{right}}\) has no contribution from a block outside the right branch: such a block lies in \(N_{\mathrm{right}}\). Thus \(K_j'\lambda\in E_+\). GSP7's convergence on bounded sets is in the original strong topology, so \(K_j'\lambda\to\lambda\) there. The converse containment follows from the closed annihilator. This proves exactly
\[
\overline{E_+}^{\,Q'_\beta}=D_{\mathrm{right}}.
\]
All multiplicities remain in the finite formula. This is not a claim that the right span is dense in the entire ambient dual.

## NHDA2. Continuity holds exactly for a finite actual right divisor

Suppose the actual right zero set is infinite. Since the original entire divisor is discrete in the bounded real strip, its heights are unbounded. For a sequence \(|\Im\rho_j|\to\infty\), set
\[
\lambda_j=\rho_j\varepsilon_{\rho_j,0}.
\]
For every bounded \(K\subset Q\),
\[
\sup_{x\in K}|\lambda_j(x)|
\le
|\rho_j|(1+|\Im\rho_j|)^{-N}
\sup_{x\in K}q_{1,N}(x)\to0
\quad(N\ge2).
\]
The infimum in the quotient seminorm is legitimate because every representative correction lies in the original ideal and has zero value at \(\rho_j\). The bounded set has finite supremum for each such continuous seminorm. Hence \(\lambda_j\to0\) in the actual strong topology.

NHR's map is conjugate-linear, and its constant coefficient is exact:
\[
(R\lambda_j)(0)=
\overline{\rho_j}\,g_{\rho_j,0}(0)
=
\overline{\rho_j}\left(-\frac1{\overline{\rho_j}}\right)=-1.
\]
Since evaluation at zero has norm one on \(H^2\), \(R\) is not continuous even on the finite span with its induced strong topology. A continuous extension agreeing there would contradict this sequence.

For a finite actual right divisor, \(E_+\) is finite-dimensional, is closed, and equals \(D_{\mathrm{right}}\) by NHDA1. The finite projector
\[
P_{\mathrm{right}}=\sum_{\rho\in\mathscr Z_+}P_\rho
\]
is continuous on \(Q\). Its strong transpose has finite right-jet image, and \(R P_{\mathrm{right}}'\) is a continuous conjugate-linear extension to all \(Q'_\beta\). The empty divisor gives the zero map. Thus the stated equivalence is valid, including this degenerate case.

This argument neither determines the cardinality of the actual right divisor nor proves nonclosability. The displayed images are not asserted to converge in Hardy norm.

## NHDA3. The matching domain and its transpose preserve conjugations

With inner products linear in the first variable, NHR's step projection gives
\[
F_h(s)=\langle h,g_s\rangle
=\int_0^1 (U\Phi^{-1}h)(x)x^{s-1}\,dx
\quad(1/2<\Re s<1).
\]
Cauchy–Schwarz justifies the integral, and NHR2.2's locally uniform derivative estimates justify holomorphic differentiation:
\[
F_h^{(j)}(\rho)=\langle h,g_{\rho,j}\rangle.
\]
Every constraint
\[
\varepsilon_{\rho,j}(x)=\langle h,g_{\rho,j}\rangle
\]
is continuous and complex-linear in \((h,x)\). Their intersection is therefore a closed subspace of \(H^2\times Q_{\mathrm{right}}\). Full right jets separate \(Q_{\mathrm{right}}\), so the second coordinate is unique when it exists. Its graph topology is complete Fréchet, exactly as claimed for \(\mathscr A_+\) and \(J_+\).

For fixed \(h\), the expression
\[
\lambda\longmapsto\langle h,R\lambda\rangle
\]
is complex-linear: \(R\) is conjugate-linear and the inner product is conjugate-linear in the second variable. Its continuous extensions to \(D_{\mathrm{right}}\) correspond, by the bidual identification, to evaluation at \(x\in Q_{\mathrm{right}}\). Testing every \(\varepsilon_{\rho,j}\) gives precisely the graph constraints. This proves the maximality statement in NHD3.

The exclusion of \(h=1\) for an infinite right divisor is also valid. Its required values are \(-1/\rho\). No representative in \(\mathcal B\) can have those values along unbounded heights, because every representative has bounds by every inverse polynomial in the fixed strip.

The transpose
\[
\mathcal T_+=J_+':
D_{\mathrm{right}}\to(\mathscr A_+)'_\beta
\]
is continuous for strong topologies: a graph-bounded test set has bounded image under \(J_+\). The Hardy comparison is complex-linear on the conjugate space,
\[
\iota:\overline{H^2}\to(\mathscr A_+)'_\beta,
\qquad
\iota(\bar y)(h)=\langle h,y\rangle,
\]
and is continuous because the graph topology controls the Hardy norm. The exact finite comparison is
\[
\mathcal T_+\lambda=\iota(\overline{R\lambda}).
\]
Its kernels are the stated annihilators:
\[
\ker\iota=\overline{\mathscr A_+^\perp},
\qquad
\ker\mathcal T_+
=(\overline{J_+\mathscr A_+}^{\,Q_{\mathrm{right}}})^\perp.
\]
The first bar is conjugation of a closed subspace, not a new closure operation. No injectivity or density premise is inserted.

## NHDA4. The closed relation and maximal Hardy domain are exact

Consider the linear graph in \(D_{\mathrm{right}}\times\overline{H^2}\). A continuous complex-linear functional on that product is
\[
(\lambda,\bar y)\longmapsto\lambda(x)+\langle h,y\rangle
\]
for \(x\in Q_{\mathrm{right}}\), \(h\in H^2\). This uses the actual strong bidual above. It annihilates the initial finite graph exactly when
\[
\varepsilon_{\rho,j}(x)+\langle h,g_{\rho,j}\rangle=0
\]
for every right jet, or equivalently \(h\in\mathscr A_+\) and \(x=-J_+h\). Hahn–Banach separation of closed linear subspaces in the Hausdorff locally convex product then gives the full closure:
\[
G=\{(\lambda,\bar y):
\langle h,y\rangle=\lambda(J_+h)
\ \text{for all }h\in\mathscr A_+\}.
\]
This computes both containments, rather than only necessary equations.

The vertical part is exactly \(\overline{\mathscr A_+^\perp}\). Hence the initial operator is closable exactly when \(\mathscr A_+\) is Hardy dense. No density conclusion is inferred from the discontinuity example.

For a fixed \(\lambda\), existence of a Hardy representative is equivalent to
\[
|\lambda(J_+h)|\le C\|h\|_{H^2}
\quad(h\in\mathscr A_+)
\]
for some finite \(C\). The necessity is Cauchy–Schwarz. For sufficiency, extend the functional to \(H_0=\overline{\mathscr A_+}\) and apply the Hilbert representation theorem. It gives the unique \(y_0\in H_0\), and all representatives are
\[
y_0+\mathscr A_+^\perp.
\]
The norm formula in NHD5.4 follows from the norm of this extended functional. The assignment \(\lambda\mapsto y_0\) is conjugate-linear, with closed graph because all the displayed equalities are closed and \(H_0\) is closed.

For every original \(h_n\), the full formula
\[
F_{h_n}(s)=(1-n^{1-s})\frac{\zeta(s)}s
\]
has zero full jets at the actual right zeros. Therefore \(h_n\in\mathscr A_+\), \(J_+h_n=0\), and every \(y\) in \(G\) lies in \(\mathcal N^\perp\). Noor's received theorem applies exactly if \(y\) also lies in its stated adjoint domain. It then gives \(y=0\), with any source kernel still retained. It does not supply \(\lambda=0\).

## NHDA5. The raw cover and source companion commute on the complete graph

The jet identity
\[
W_n^*g_{\rho,j}=
n^{1-\overline\rho}\sum_{\ell=0}^j
\binom j\ell(-\log n)^{j-\ell}g_{\rho,\ell}
\]
has all nilpotent coefficients. Pairing with \(h\) conjugates its coefficients, giving the derivatives of \(n^{1-s}F_h(s)\). It follows that
\[
W_n\mathscr A_+\subset\mathscr A_+,
\qquad
J_+W_n=U_nJ_+,
\quad U_nF=n^{1-s}F.
\]
The graph action is continuous: \(W_n\) has Hardy norm \(\sqrt n\), while \(U_n\) is a continuous multiplier of the original quotient. Transposition yields NHD6.3 with its stated direction.

The map
\[
(\lambda,\bar y)\mapsto
(U_n'\lambda,\overline{W_n^*y})
\]
is continuous on the product, and preserves the finite graph by NHR7.2. It therefore preserves its closure \(G\). Equivalently, one can insert \(W_nh\) into the full graph equations.

The source identity
\[
T_n'=n(U_n')^{-1}
\]
is compatible with the source's invertible multiplier action. It supplies no global inverse for \(W_n^*\). The exact Hardy relations remain
\[
W_n^*W_n=nI,\qquad W_nW_n^*=nP_n.
\]
The nonzero complementary projection for \(n>1\) is retained.

## NHDA6. The corrected entire tests preserve the full original factors

Define \(A_0(s)=-1\) and
\[
A_m(s)=m^{1-s}-(m+1)^{1-s}\quad(m\ge1).
\]
All satisfy \(A_m(0)=-1\). Since the original full multiplier has \(8F_0(0)=1\),
\[
\psi_m(s)=\frac{A_m(s)+8F_0(s)}s
\]
is entire for every \(m\ge0\). This verifies the separate first coefficient; no power \(0^{1-s}\) is continued outside its stated strip.

At an original nontrivial zero \(\rho\ne0\),
\[
\psi_m^{(j)}(\rho)=
\sum_{k=0}^{j}\binom jk
\bigl(A_m^{(k)}(\rho)+8F_0^{(k)}(\rho)\bigr)
\frac{(-1)^{j-k}(j-k)!}{\rho^{j-k+1}}.
\]
For \(j<m_\rho\), every correction term vanishes by the complete zero order. Thus \(\psi_m^{(j)}(\rho)=\phi_m^{(j)}(\rho)\) to exactly the retained order. The factor eight, denominator \(s\), and the complete \(F_0\) are used before taking this jet comparison.

The polynomial bound in \(m\) is valid. Outside \(|s|<1\), direct numerator bounds on \(|\Re s|\le A\) give at most the stated power. Inside that disk, the divided function is entire and the maximum principle on radius two applies; there the power is at most three, covered by \(A+3\). The \(m=0\) case is bounded by the same estimate. For \(t>0\),
\[
F_{t,m}(s)=e^{ts^2}\psi_m(s)
\]
therefore lies in \(\mathcal B\), with the exact seminorm estimate NHD7.4. The inverse half-Mellin formula retains \(u^{-1/2}/\pi\), and its source membership follows from the already constructed isomorphism.

## NHDA7. Full strong-dual holomorphic continuity and the exact quotient discrepancy

For \(\lambda\in Q'_\beta\),
\[
\mathcal H_t\lambda(z)=
\sum_{m\ge0}\overline{\lambda([F_{t,m}])}z^m
\]
is conjugate-linear in \(\lambda\). The source seminorm bound is polynomial in \(m\), so each functional's series is holomorphic on the disk.

For every \(r<1\), the series
\[
K_{t,z}=\sum_{m\ge0}F_{t,m}\bar z^m
\]
converges uniformly for \(|z|\le r\) in every original source seminorm. Its image is a bounded subset of \(Q\), and
\[
\sup_{|z|\le r}|\mathcal H_t\lambda(z)|
=
\sup_{|z|\le r}|\lambda([K_{t,z}])|.
\]
This is a defining strong-dual seminorm. It proves the full continuity assertion into the compact-open holomorphic space, without an asserted boundary Hardy estimate.

The complete finite-jet comparison, with raw derivatives, is
\[
\mathcal H_t\varepsilon_{\rho,j}
=
\sum_{\ell=0}^j
\binom j\ell
\overline{g_t^{(j-\ell)}(\rho)}\,g_{\rho,\ell}.
\]
It is exactly \(R(m_{g_t}'\varepsilon_{\rho,j})\); no factorial or conjugation is missing. The finite matrix tends to identity as \(t\downarrow0\), proving the stated finite-span Hardy convergence only.

The continuous analytic coefficient operator \(\mathscr W_n^*\) has
\[
(\mathscr W_n^*f)_m=\sum_{a=0}^{n-1}f_{nm+a}.
\]
For \(r^{1/n}<R<1\), Cauchy's estimate gives precisely
\[
\sup_{|z|\le r}|\mathscr W_n^*f(z)|
\le
\frac{\sum_{a=0}^{n-1}R^{-a}}{1-rR^{-n}}
\sup_{|z|\le R}|f(z)|.
\]
The first telescoping block is
\[
\phi_0+\cdots+\phi_{n-1}=-\frac{n^{1-s}}s.
\]
For all \(m\), telescoping therefore gives the same formula, including \(m=0\). Restoring the original correction yields exactly
\[
\sum_{a=0}^{n-1}\psi_{nm+a}(s)-n^{1-s}\psi_m(s)
=
8F_0(s)\frac{n-n^{1-s}}s.
\]
The numerator \(n-n^{1-s}\) vanishes at zero, so this quotient is entire. Its Gaussian multiple lies in \(\mathcal B\) and has all the original nontrivial zero orders; hence it lies in \(I\). Passing through the actual quotient, applying \(\lambda\), and retaining the coefficient conjugations proves on the whole original strong dual
\[
\mathcal H_tU_n'=\mathscr W_n^*\mathcal H_t.
\]
This is the claimed global regularized intertwiner, not a globally invertible Hardy action.

## NHDA8. Review receipt and exact limits

A second independent mathematical checker reviewed NHD7–NHD9 against NHR2, NHR4 and NHR7. It independently obtained the derivative formula, strong-dual continuity, the first telescoping block, and the full discrepancy in NHDA6–NHDA7. No correction was requested. Its pass was on the pre-renaming mathematical text; the final naming and factorial typography repairs were inspected here and change none of those formulas.

The right-branch renaming and the two typography corrections are incorporated in the reviewed hash. No other mathematical correction was needed. The proof keeps the original source topology, actual divisor, full multiplicities, original \(\zeta\) factors and actual kernels. It neither establishes density of \(\mathscr A_+\) in \(H^2\), nor determines closability, nor decides whether the right divisor is finite. Its regularized map has target \(\mathcal O(\mathbb D)\), not an unproved global \(H^2\) target. No lifting-obstruction vanishing or RH conclusion is supplied by this review.

The receipt applies to the exact source hash in NHDA0. Any later mathematical changes require a review of the changed parts.

