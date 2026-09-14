# Independent full crosswalk for R63 and R64

This is a bounded integration review of the exact current-results fragment, against the complete proof bodies H1–H66 (with H49a–g), HDI1–HDI24, HCD1–HCD29 (with HCD2a–c, HCD18a and HCD19a), and CQ1–CQ29. Those complete bodies were read. The review retains the original source, coefficient frames, measures, full primary multiplicities, and each map's domain. R65–R66 have a separate disjoint review. No numerical test, mathematical test suite, Lean execution, source rewrite or remote action is claimed.

The initially reviewed R63–R66 fragment has SHA-256 `73c3aeae19c3ac94563bcbb5f91fc75527f02cef7ea9bd8a50c42b2c1b5027a1`. Two domain qualifications from the full proofs must be explicit in that fragment: a common maximal source for the four-volume bound, and the actual finite-source circumference for the bounded Bochner-mean splitting. The final receipt will bind the corrected fragment and record these dispositions. Neither issue changes the underlying full proofs.

## Exact input objects and isometries in R63

Fix the original full-order packet (h), tensor degree (k\geq1), (g=2\xi), literal cyclic polynomial (\chi=\chi_{h,k}), degree (q>0), and (E=\mathbb C[S]/(\chi)). For (N\geq q-1), let (P_N=\mathbb C[S]_{\leq N}), (J_N:P_N\twoheadrightarrow E) be remainder modulo (\chi), and (B_N=\ker J_N=\chi P_{N-q}). The empty relation space at (N=q-1) is retained. The original source map is (\mathcal V P=P(D_1+\cdots+D_k)F_h^{\otimes k}), with the same theta inclusion and full jet unit as H7–H8.

H9 specifies (r=\log x_k), (z_i=\log x_i-\log x_k), and

\[
(\mathcal U_kF)(r,z)=e^{(kr+\sum_i z_i)/2}
 F(e^{r+z_1},\ldots,e^{r+z_{k-1}},e^r).
\]

The logarithmic coordinate determinant is one, while the exponential factor squared is exactly the Jacobian from the original positive coordinates. Thus this map is an isometry into (L^2(\mathbb R,dr;\mathcal K)), where (\mathcal K=L^2(\mathbb R^{k-1},dz)). No relative variable is discarded. Direct differentiation gives (\mathcal U_kD^{(k)}=(-\partial_r+k/2)\mathcal U_k). Set (\Psi_N=\mathcal U_k\mathcal V|_{P_N}) and (M_N=\Psi_N^*\Psi_N), retaining its complete original mass.

For (L>0), H11–H14 define

\[
\mathcal Z_{L,\theta}\psi(r)=\sum_{a\in\mathbb Z}e^{ia\theta}\psi(r+aL),
\quad 0\leq r<L,
\]

with the original finite-source convergence, and extend the complete phase transform by Hilbert-space density. For almost every fixed (r), the vector sequence (a\mapsto\psi(r+aL)) is square summable. Its Fourier-series Parseval identity is

\[
\int_0^{2\pi}\|\mathcal Z_{L,\theta}\psi(r)\|_{\mathcal K}^2
\frac{d\theta}{2\pi}=\sum_{a\in\mathbb Z}\|\psi(r+aL)\|_{\mathcal K}^2.
\]

Integration over (0\leq r<L) gives the original full source norm. Fourier coefficient inversion is exactly

\[
\psi(r+aL)=\int_0^{2\pi}e^{-ia\theta}\mathcal Z_{L,\theta}\psi(r)
\frac{d\theta}{2\pi}.
\]

The inverse reconstructs an arbitrary square-integrable phase field by its translation-index Fourier coefficients, so the isometry is onto its stated direct integral. Applying this identity to all pairs of finite source columns proves (\int M_{N,\theta}\,d\theta/(2\pi)=M_N). R63 has the correct signs and Fourier measure.

The boundary identity is (f(r+L)=e^{-i\theta}f(r)); its basis is (L^{-1/2}e^{-i(2\pi n+\theta)r/L}). In a coefficient integral, substituting (y=r+aL) cancels (e^{ia\theta}e^{-ia(2\pi n+\theta)}=1). This gives precisely (L^{-1/2}\widehat\psi((2\pi n+\theta)/L)), with the source convention (\widehat\psi(u)=\int\psi(r)e^{iur}\,dr). In particular the ((\theta,n)=(0,0)) term remains (L^{-1}\widehat\Psi_N(0)^*\widehat\Psi_N(0)).

## Finite cover, coefficient algebra and original factors

For (m\geq1) and (\theta_j=2\pi j/m), H18 defines (Q_jf(r)=m^{-1}\sum_{a=0}^{m-1}e^{ia\theta_j}f(r+aL)) on the circle of length (mL). The finite character identity (m^{-1}\sum_a e^{ia(\theta_j-\theta_l)}=\delta_{jl}) gives the mutually orthogonal projections, their sum (I), and quasi-periodic boundary multiplier (e^{-i\theta_j}). The full map and inverse are

\[
f\longmapsto(\sqrt m\,Q_jf|_{[0,L]})_j,
\qquad
f(r+aL)=m^{-1/2}\sum_j e^{-ia\theta_j}g_j(r).
\]

For each (r) the finite Fourier identity preserves the sum of the (m) original interval norms. The reconstruction formula proves both compositions equal identity, with no lost (m)-factor. Expanding (Q_j\mathcal Z_{mL,0}\psi) and writing each translation index uniquely as (a+mb) gives (m^{-1}\mathcal Z_{L,\theta_j}\psi). Taking norms and polarizing therefore gives exactly (M_N(mL,0)=m^{-1}\sum_jM_N(L,\theta_j)), as stated in R63.

For the literal ring homomorphism (\mathbb C[z,z^{-1}]\to\mathbb C[w,w^{-1}]), (z\mapsto w^m), write every integer exponent uniquely as (mn+j), (0\leq j<m). This proves the full free basis (1,w,\ldots,w^{m-1}), including negative exponents. The product (w^jw^l) equals (w^{j+l}) if (j+l<m), and (z w^{j+l-m}) otherwise. R63 correctly retains this multiplication carry and makes no arithmetic Frobenius identification. The actual circle restriction in H23 matches the same projectors.

## Canonical section, original relation and quadratic quotient loss

On the positive-definite phase domain of H24–H28 and HCD2a–c, put

\[
G=(JM^{-1}J^*)^{-1},\quad C=M^{-1}J^*G,
\quad G_\theta=(JM_\theta^{-1}J^*)^{-1},
\quad C_\theta=M_\theta^{-1}J^*G_\theta.
\]

Direct multiplication gives (JC=JC_\theta=I_E), (B^*MC=0), and (B^*M_\theta C_\theta=0), where (B\) is multiplication by the unchanged (\chi) in the original relation coordinates. Since (J(C-C_\theta)=0), uniqueness in the injective relation coordinates gives

\[
C-C_\theta=BX_\theta,\qquad
X_\theta=(B^*M_\theta B)^{-1}B^*M_\theta C.
\]

Expanding (C=C_\theta+BX_\theta) in (C^*M_\theta C), both cross terms vanish by the stated orthogonality. Thus the exact phase identity is

\[
C^*M_\theta C=G_\theta+X_\theta^*(B^*M_\theta B)X_\theta.
\]

Integrating uses (\int M_\theta=M), giving (G=\overline G+\mathscr D) and the full relation-norm expression in R63. At zero relation dimension (J) is invertible, both sections are (J^{-1}), and every correction map into or through the zero relation space is zero. The theta primitive is the inherited primitive of the literal (\chi\)-multiple; no change of relation ideal is made.

The original weighted source correlations give

\[
-\delta_LM\preceq M_\theta-M\preceq\delta_LM,
\qquad\delta_L=\kappa_{a,N}/(e^{aL}-1).
\]

For each positive integer translate the weighted Cauchy–Schwarz bound is (e^{-a|s|}\sqrt{(v^*M_{a,+}v)(v^*M_{a,-}v)}). Pairing the two signs, using (2\sqrt{uv}\leq u+v), and summing the literal geometric series yields the displayed constant. If (\delta_L<1), the inverse-chord identity

\[
\frac{2-x}{1-\delta_L^2}-\frac1x
=\frac{\delta_L^2-(x-1)^2}{x(1-\delta_L^2)}\geq0
\]

on (1-\delta_L\leq x\leq1+\delta_L), applied to the original (M)-self-adjoint operator (M^{-1}M_\theta), yields

\[
\int JM_\theta^{-1}J^*\,d\mu
\preceq(1-\delta_L^2)^{-1}G^{-1}.
\]

The pointwise positive block matrix with diagonal blocks (G_\theta^{-1},G_\theta) and identity cross blocks remains positive on integration. Its Schur complement then gives (\overline G\succeq(\int G_\theta^{-1})^{-1}\succeq(1-\delta_L^2)G). Together with the relation identity, this proves exactly the stated quadratic interval.

For the four-volume assertion, the common source must contain all four endpoint sources. H42–H43 explicitly choose, for example, the original cutoff (N_*=2q+2), compute its (\kappa_{a,N_*}), and restrict the single phase inequality to every smaller endpoint source. Write (d_N=\log\det\overline G_N-\log\det G_N). Each endpoint then obeys (q\log(1-\delta_L^2)\leq d_N\leq0). In the signed sum (d_{q-1}+d_q-d_{2q-1}-d_{2q}), its two positive and two negative summands give absolute bound (2q\log(1/(1-\delta_L^2))). Computing (\delta_L) at one arbitrary unrelated cutoff would not prove this common bound; the final fragment must name the containing source. The exponent and factor (2q) are correct with that qualification.

The compact source in HDI22–24 has (\psi_0=\sqrt7 f), (\psi_1=\sqrt7(\eta f(\cdot-L)+\sqrt{1-\eta^2}g_1)), with disjoint unit-norm functions obtained by displaying their original positive integrals (\alpha,\beta). Its original Gram is (7I_2) and its phase Gram is (7\bigl(\begin{smallmatrix}1&\eta e^{i\theta}\\\eta e^{-i\theta}&1\end{smallmatrix}\bigr)). With (J=(1\;0)) and (B=(0\;1)^T), matrix multiplication gives (C_\theta=(1,-\eta e^{-i\theta})^T), (G_\theta=7(1-\eta^2)) and (\mathscr D=7\eta^2). R63 correctly uses this as the full-circle sharpness calibration with displayed source map; it does not claim that these constructed columns are an arithmetic packet.

## R64 bounded common-image complex and metric

The bounded Hilbert splitting is proved at fixed finite (N) using HCD2. Its actual source-dependent choice is: choose (\beta>0) for the existing finite weighted Grams and (0<\eta<1), then take

\[
L\geq\beta^{-1}\log(1+\kappa_{\beta,N}/\eta).
\]

It follows that (\delta_L\leq\eta<1), and the original coefficient bounds are (a=(1-\delta_L)\lambda_{\min}(M)>0) and (b=(1+\delta_L)\lambda_{\max}(M)<\infty). These prove equivalence of the actual phase Hilbert norm and coefficientwise (L^2). The stated calculation concerns this domain; the later sampled-density and completion maps below are defined for every (L>0).

Let (\mathscr B=L^2(\Theta;B_N)) with its restricted phase source norm, and let (\mathscr P^{\mathrm{eq}}) consist of fields (P\) whose (JP(\theta)) equals one fixed (x\in E) almost everywhere. The spaces are closed because (J\) is bounded in the coefficient norm and the constant (E)-fields form a closed range of the bounded repetition-of-mean idempotent. Repetition (\Delta v(\theta)=v) is an isometry from the original (M)-norm, by (\int M_\theta=M). The coefficient Bochner mean exists, commutes with (J), and satisfies

\[
\|\operatorname{av}P\|_M^2\leq b\int\|P(\theta)\|_{\rm coeff}^2d\mu
\leq(b/a)\|P\|_{\mathscr P}^2.
\]

Consequently (P\mapsto(\operatorname{av}P,P-\Delta\operatorname{av}P)) and ((v,b^0)\mapsto\Delta v+b^0) are bounded inverse coefficient maps. In degree one, the second component has (J)-image (x-x=0) and mean zero; in degree zero it is already relation-valued. Under these maps the inclusion differential becomes the original inclusion on the first summand and the identity on the mean-zero relations. The full degree-minus-one map (hP=P-\Delta\operatorname{av}P) therefore obeys (dh+hd=I-\Delta\operatorname{av}) in both degrees, as R64 states. Neither the splitting nor this contraction is declared orthogonal. Its induced cohomology map is the actual identity on the full (E).

The explicit phase section (C_\theta=M_\theta^{-1}J^*G_\theta) is bounded and measurable because all matrix bounds and inverses are uniformly defined at this cutoff. Any field of common image (x) equals (C_\theta x+b_\theta), with (b_\theta\in B_N). Orthogonality gives the exact norm decomposition

\[
\int P^*M_\theta P\,d\mu=x^*\overline Gx+\int b_\theta^*M_\theta b_\theta\,d\mu.
\]

This proves the quotient metric (\overline G) on the unchanged (E).

To check the weighted mean-zero relation formula, put (\overline C=\int C_\theta\,d\mu), (a_C=C-\overline C) and (h_\theta=C_\theta-\overline C). Both are relation-valued, and (\int h_\theta=0). Phase orthogonality gives (a_C^*M_\theta C_\theta=0), so

\[
\int a_C^*M_\theta h_\theta\,d\mu=-a_C^*M\overline C
=-a_C^*M(C-a_C)=a_C^*Ma_C.
\]

The last equality uses the original orthogonality (a_C^*MC=0). The adjoint cross term has the same value. Expanding (C-C_\theta=a_C-h_\theta) with both cross terms intact gives

\[
\mathscr D=\int h_\theta^*M_\theta h_\theta\,d\mu-a_C^*Ma_C.
\]

Both the minus sign and the original coefficient metric in R64 are correct.

## Completed phase quotient, full primary kernel and global map

For arbitrary (L>0), retain (u_n=(2\pi n+\theta)/L), (S_n=k/2+iu_n), and (\nu_n=(2\pi/L)m_{h,k}(u_n)). The positive-support Hilbert source is the weighted sequence space on (I_\theta=\{n:\nu_n>0\}); zero-weight coordinates are the explicit null subspace when expressed on all integers. HDI12 and HCD19a retain the source-density envelope (m_{h,k}(u)\leq A_bB_b^{k-1}e^{-b|u|}) for (0<b<\pi/2). Thus the original sampled measure and its literal (\lvert\chi\rvert^2)-multiple have positive exponential moments, with the exact factor (2\pi/L) and both shifted tails.

For completeness, if (f) is orthogonal to all polynomial sequences for either of those measures, Cauchy–Schwarz makes (\sum_n\overline f_n\mu_ne^{zu_n}) normally convergent and holomorphic on a nonempty strip. All derivatives at zero vanish because the powers of (u=(S-k/2)/i) are evaluations of polynomials in the original (S). Holomorphic uniqueness makes the series zero. Integrating (F(it)e^{-itu_m}) over (0\leq t\leq L), with its factor (1/L), retains the shifted phase and gives exactly (\overline f_m\mu_m=0). Every positive-support coordinate vanishes. This proves polynomial density for both weights.

Let (Z_\theta=\{n:\nu_n>0,\chi(S_n)=0\}). Multiplication by the literal (\chi) is an isometry from the (\lvert\chi\rvert^2\nu)-weighted sequence domain onto the subspace of the original sampled space vanishing at (Z_\theta). The inverse divides by (\chi(S_n)) on its nonzero coordinates; its squared norm is exactly the original squared norm, and the remaining coordinates are the specified null classes. Density therefore identifies this subspace with the closed polynomial relations. The quotient is restriction to (Z_\theta), with norm (\sum_{n\in Z_\theta}\nu_n|v_n|^2). This proves the exact receiving metric, rather than only its dimension.

The actual map (E\to\mathbb C^{Z_\theta}), ([P]\mapsto(P(S_n))), is onto by the literal Lagrange polynomials at the distinct nodes. Its kernel is ((p_\theta)/(\chi)), where (p_\theta=\prod_{n\in Z_\theta}(S-S_n)). The original polynomial (\chi) remains nonreduced. Writing its full factorization (\prod_\lambda(S-\lambda)^{m_\lambda}), the original Taylor map to the primary factors has coordinates (P^{(j)}(\lambda)/j!). Its inverse uses (e_\lambda=[q_\lambda u_\lambda]_\chi), where (q_\lambda=\chi/(S-\lambda)^{m_\lambda}) and (u_\lambda) is the Taylor polynomial of (1/q_\lambda) through degree (m_\lambda-1). Divisibility by the full prime powers proves that these are the complete orthogonal idempotents summing to one. At a sampled positive-mass factor the quotient retains the constant coordinate and the kernel contains every positive power of its nilpotent coordinate; at an unsampled or zero-mass factor the entire primary factor is in the kernel. These maps intertwine multiplication by (\lambda+\varepsilon_\lambda) with the receiving scalar action.

For (k=1), the annihilator ideal of multiplication by (S) on the original cyclic algebra is ((h)): an annihilator must kill the original unit, which forces divisibility by (h), and (h) itself annihilates the algebra. Hence ((\chi_{h,1})=(h)); a nonunit leading coefficient remains in the analytic source (g/h). Full selected-order cancellation at a sampled root (\rho) gives (\nu_n=L^{-1}|g^{(r)}(\rho)/h^{(r)}(\rho)|^2>0). Both Taylor factorials cancel together, and the leading coefficient remains in (h^{(r)}). The R64 mass is correct. The general positive-support kernel also retains zeros at any other lattice coordinates.

The embedding (v_n\mapsto\sqrt{\nu_n}v_n) realizes the receiving field in ordinary (\ell^2(\mathbb Z)), with diagonal projection (1_{\{\nu_n>0\}}1_{\{\chi(S_n)=0\}}). Both indicators are measurable. A fixed root on the line (\Re S=k/2) fixes exactly one phase (L\Im\lambda\pmod{2\pi}) in the half-open interval. There are only finitely many such phases. Every receiving field section consequently has squared norm supported on a measure-zero set. Its direct integral is zero. The explicit evaluation section of any class of (E) represents this zero almost-everywhere class; the exact coefficient map has kernel all of (E), while each pointwise exceptional map and its positive mass remain defined.

Finally HCD28 constructs the actual cochain map: evaluate the polynomial fields in both degrees. The all-phase source identity makes this evaluation an isometry on its stated domain; relation-valued fields land in the completed relation subspace. The quotient image of a common class is precisely its phasewise evaluation. The relation closure in the full integral is proved by testing all measurable indicators times (\chi S^j), taking the countable intersection of the resulting full-measure orthogonality sets, and using the proved fibre density. Thus its receiving complex is the identity inclusion complex, and the degree-one map is exactly (E\to0) with kernel (E).

On each original represented label (\lambda), the lifted map is ((\lambda,v)\mapsto(\lambda,fv)), with (\tau\mapsto\tau). Its two inverse images are

\[
\widetilde f^{-1}\{(\lambda,0)\}=\{(\lambda,v):v\in\ker f\},
\qquad\widetilde f^{-1}\{\tau\}=\{\tau\}.
\]

This retains nonzero source kernel vectors and external absence as distinct source elements while proving the exact relation between them and the receiving objects. R64 carries precisely this operation.

## Disposition

All displayed R63 and R64 formulas, signs, constants, isometries, primary kernels and split preimage statements agree with the complete proofs. The final acceptance requires only the explicitly recorded domain propagation: one containing cutoff for the four endpoint error, and the computed finite-source circumference for the bounded common-image splitting. The shifted-density and completed-space maps retain their full (L>0) domain. The separately pinned final receipt must verify the actual corrected fragment before declaring those two integration findings closed.


## Final successor acceptance

The actual corrected complete R63–R66 fragment has SHA-256 `49cb621b34aeb18f3ae12af31a3a125f7f4782adce436fd5eb2279ad8034708c`. Its bounded delta was read. R63 now computes the common four-endpoint bound on the unchanged maximal source `N_*=2q+2`. R64 now states the explicit fixed-cutoff circumference from HCD2a–c before asserting bounded coefficient maps; its later completion passage explicitly applies for every `L>0`. These close both findings of this component. R66's separately reviewed scale correction says squared norm in both places and retains the original positive mass. The exact recorded four replacement blocks invert to the entire 9,642-byte initially reviewed fragment with its original SHA-256, proving no other current-results text was changed.

R63 and R64 are accepted in full at this successor. All formulas and maps in this component have the complete calculations above and exact full proof dependencies below. There are no remaining findings.
