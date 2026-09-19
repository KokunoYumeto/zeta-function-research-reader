# Earlier Split Zero mathematics with proved RH-programme receivers

This register identifies the earlier manuscripts and exact receiving proofs used in this edition. The scope is the **whole** Split Zero / tau-base / mixed-cohomology route to RH. Coverage is not exhaustive. `READ_COVERAGE.json` distinguishes whole papers from selected complete sections. The accompanying `EXACT_CORPUS_RECEIVERS.tex` contains the definitions and complete proofs of the receivers below.

## 1. The old circle heat construction reproduces the actual theta source

**Earlier proof read:** `corpus_sources/corrected_wick_rotated_spline_wavelet_note.tex`, labels `mod:g0-fourier`, `mod:spline-primitive`, `mod:odd-square`, especially lines 646–774. The entire manuscript has been read; only the circle construction is imported.

It proves that the spatial derivative of the heat-evolved Haar step is

\[
C(t)=4\sum_{k\in\mathbb Z,\ k\text{ odd}}e^{-tk^2}.
\]

**Receiver now proved:** D1–D3 in `EXACT_CORPUS_RECEIVERS.tex`. In the original variable (x), operator (D=-x\partial_x), source (f_r=D^r\Theta\phi_*), and measure (dx),

\[
f_r^{[J]}=\tfrac14D^{r+1}(D-1)\sum_{j=0}^J C(\pi4^jx^2),\qquad
f_r-f_r^{[J]}=f_r(2^{J+1}x).
\]

The exact error norm is (2^{-(J+1)/2}\|f_r\|_{L^2(dx)}). The original complete transform is (\mathcal Mf_0=2\xi); the truncated source has transform ((1-2^{-(J+1)s})s^r2\xi(s)). Every original zero and multiplicity is retained. D2 gives the complete Gram correction including both cross terms for any original finite coefficient map.

**Why this can advance the programme:** it connects its original theta source to an existing geometric heat construction, and supplies a quantified finite realization of the entire source rather than merely matching spectral support. Its exact receiving map is (\phi\mapsto\phi-\phi(2^{J+1}\cdot)) in the original (V). That map generally leaves the fixed finite polynomial-Gaussian span, so it is not silently used to identify finite-cutoff minima.

**Human source:** the completed zeta convention is Apostol, *Introduction to Analytic Number Theory*, §12.8, also [DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4). The heat and dyadic receiver is proved directly; no physical interpretation is imported from the old paper.

## 2. The arithmetic-site Beurling tower gives a second genuine RH route

**Earlier proof read:** `corpus_sources/split_support_geometry_arithmetic_curve_v11910.tex`, complete denominator/Frobenius sections at lines 5688–6057 and Beurling sections starting at 7833. Labels include `thm:global-perfection`, `thm:direct-beurling-domination`, `thm:arithmetic-site-nyman`. These sections also occur in `v11`; the filenames do not establish a chronology or a newly discovered revision.

The earlier manuscript already proves the finite inclusion

\[
\operatorname{span}\{F_{1/n}:2\le n\le Q\}\subset
\operatorname{span}\{F_{a/\Lambda_Q}:1\le a<\Lambda_Q\},\quad
\Lambda_Q=\operatorname{lcm}(1,\ldots,Q),
\]

where (F_\alpha(y)=\{\alpha y\}-\alpha\{y\}) and the original norm is (L^2((1,\infty),y^{-2}dy)). It relates the cofinal denominator/Frobenius tower to the human Nyman–Beurling/Báez-Duarte criterion. This is an established alternate analytic route inside the earlier programme, not an estimate that can be inferred from the current seven allocations.

**Receiver now proved:** B1–B5. For any actual finite set of zeros with real part greater than (1/2), retaining multiplicity (m_\rho), the bounded divided-Mellin-jet map has exact Gram matrix

\[
\mathsf G_{(\rho,j),(\sigma,k)}=
\frac{(-1)^{j+k}(j+k)!}{j!k!(\rho+\bar\sigma-1)^{j+k+1}},\quad
b_{\rho,j}=\frac{(-1)^j}{\rho^{j+1}}.
\]

It annihilates every (F_\alpha), and every original finite approximation error has squared norm at least (b^*\mathsf G^{-1}b>0). One value observation gives ((2\Re\rho-1)/|\rho|^2). Multiplicity is neither discarded nor replaced by a simple-root convention.

The exact bridge into the current theta complex is (\mathcal T_+=R_{Z_+}J_+), using its original canonical section and full local unit (j_h(h/(2\xi))). It satisfies (q\mathcal T_+=\sigma_{Z_+}J_+), kills each Beurling atom, and sends the target constant to the nonzero original finite theta class (\sigma_{Z_+}b). This specifies an actual map and the attained quotient metric of its source; it does not identify that metric with the theta (L^2) metric.

**Why this matters:** it restores a previously developed RH approximation route and gives an exact, multiplicity-sensitive obstruction in its arithmetic-stage spaces. The useful unsolved calculation on this route is an actual upper estimate for these distances along the prescribed tower; no such estimate is inserted or claimed here.

**Human sources:** Arne Beurling, [A closure problem related to the Riemann zeta-function](https://doi.org/10.1073/pnas.41.5.312), PNAS 41 (1955), 312–314; Luis Báez-Duarte, [A strengthening of the Nyman–Beurling criterion](https://arxiv.org/abs/math/0202141), published 2003. Connes and Consani's [Geometry of the arithmetic site](https://doi.org/10.1016/j.aim.2015.11.045) supplies the human arithmetic-site setting. The exact denominator/LCM construction belongs to the named programme manuscript and is not falsely attributed to their article.

## 3. The existing compactified jet tail receives the actual global theta cohomology

**Earlier proof read:** `corpus_sources/split_zero_zeta_packet_geometry_integrated.tex`, complete local jet and compactification sections, lines 413–886; particularly `P1:prop:vector-tail-exact`.

For all actual nontrivial zeros and their full primary jet spaces (E_\rho), the paper proves

\[
0\to j_!\mathcal F\to j_*\mathcal F\to i_{\infty*}T\to0,
\qquad T=\prod E_\rho/\bigoplus E_\rho.
\]

**Receiver now proved:** T1–T3. Full Mellin jets descend from the original (\mathscr B\) to (Q=\mathscr B/\Theta V). The actual finite canonical sections are compatible under extension by zero and give (\sigma:\bigoplus E_\rho\hookrightarrow Q). Their compatibility is proved with the complete original numerator polynomial and (g=2\xi), not just by comparing zero supports. With (K) the all-jet kernel and (T_{\rm arith}) the actual tail image, one obtains

\[
0\to K\to Q/\sigma(\bigoplus E_\rho)\to T_{\rm arith}\to0,
\qquad T_{\rm arith}\hookrightarrow T.
\]

A compactly supported test-function construction proves (T_{\rm arith}\ne0). No assertion of surjectivity onto the unrestricted product tail or of vanishing of (K) is made.

**Why this matters:** finite primary blocks sit inside an actual global cohomological object with a nonzero infinity receiver. The map identifies exactly what finite packet arguments retain and what the global tail and all-jet kernel retain. This is available for a Deligne-style compactification/exact-sequence calculation without replacing the actual theta quotient by its zero divisor.

## 4. Both original endpoint states are retained in the Connes–Consani source bridge

**Earlier papers read:** the entire `globalization nte/shefy/nontrivial_zeta_packet_geometry_preprint.tex` and the entire `globalization cue/cue_split_zero_hurwitz_phase_preprint.tex`. The former invokes the trace realization; the latter proves the two-endpoint principal-part and orientation-parity identities.

**Human primary checked:** Connes and Consani, [Hochschild homology, trace map and ζ-cycles](https://arxiv.org/abs/2207.10419), especially Lemma 4.1 and Proposition 4.2, in the [author's published PDF](https://alainconnes.org/wp-content/uploads/Hochschild-homology-trace-map-and-%CE%B6-cycles-2023.pdf). The published page range is 83–101; the earlier local paper prints 83–104.

**Receiver proved in E1–E5:** let (\mathscr B_{01}=\mathscr B+\mathbb C\eta+\mathbb Cx^{-1}\eta), with the cutoff equal to one near zero. Then the actual Poisson formula gives boundary map

\[
(\phi(0),\int\phi)\longmapsto(-\phi(0),\int\phi).
\]

This map is invertible. It gives the exact cohomology isomorphism

\[
\mathscr B/\Theta V\cong\mathscr B_{01}/\Theta\mathcal S_{\rm ev},
\]

retaining both boundary states and the operator (D=-x\partial_x), whose endpoint action is (\operatorname{diag}(0,1)). The full inverse of (D(D-1):\mathcal S_{\rm ev}\to V) is written as two convergent integrals. Applied to the Gaussian it returns the original (\phi_*), so its theta transform remains (2\xi). The original Gaussian endpoint residues are ((-1,1)), precisely the earlier principal part (1/(s(s-1))).

Their spectral theorem uses a strong-Schwartz **closed** image. E5 proves the map from the original algebraic quotient to that closed quotient and retains its kernel (\overline{\Theta V}/\Theta V). Finite full Mellin jets remain continuous and the finite original sections survive. No Hilbert-density argument is used to erase the quotient.

**Why this matters:** it restores the exact endpoint complex underlying the trace realization and connects it to the programme's actual source. It is stronger than matching a named Laplacian or a spectral zero set: both boundary states, the quotient map, the differential operator and the topology are specified.

## 5. Earlier local phases determine the complete original Taylor-unit matrix

**Earlier proofs read:** full `globalization nte/shefy/zeta_zero_atomic_phase_packets.tex`, especially `thm:local-phase-packet`, and full `globalization nte/shefy/split_zero_zeta_analytic_completion.tex`, including the packet product and leading-jet transformation proofs.

The atomic-phase paper retains (\xi(\rho+z)=\lambda_\rho z^{m_\rho}\exp(\sum c_{\rho,n}z^n)). It explicitly credits Jacolm Tobley's unpublished correspondence for the phase-walk formalism; this attribution is preserved. The new computation does not need a human-source attribution for its elementary formal-series multiplication.

**Receiver U1–U3:** all coefficients of the actual (\varepsilon_Z=j_h(h/(2\xi))) are obtained by the finite recurrence

\[
\varepsilon_{\rho,0}=\frac{\prod_{\sigma\ne\rho}(\rho-\sigma)^{m_\sigma}}{2\lambda_\rho},\quad
\varepsilon_{\rho,r}=\frac1r\sum_{n=1}^r
\left((-1)^{n-1}\sum_{\sigma\ne\rho}\frac{m_\sigma}{(\rho-\sigma)^n}-nc_{\rho,n}\right)
\varepsilon_{\rho,r-n}.
\]

In the original increasing power basis this is exactly (V_Z^{-1}(\bigoplus T_\rho)V_Z), with the actual confluent evaluation matrix and local triangular multiplication matrices. The reflection and conjugation actions, including their full degree and jet signs, are proved. This gives entries of the canonical source lift and its cross terms. It does not replace the complete local unit by the scalar packet weight (|\lambda_\rho|).

## 6. The old jet-ideal chain gives an actual Deligne nilpotent filtration

**Earlier proofs read in full:** `globalization nte/shefy/zeta_boolean_jet_packet_shadows.tex` and `split_zero_zeta_divisor_refined_preprint.tex`. Their local ideal-chain theorem and chain/cube adjunctions retain every nilpotent layer. **Human theorem:** Pierre Deligne, [La conjecture de Weil II](https://www.numdam.org/item/PMIHES_1980__52__137_0/), §§1.6.1 and 1.6.7–1.6.10; the source translation's corresponding complete section was read.

**Receiver N1–N6:** in the actual primary factor at \(\rho\), the filtration is

\[
M_rE_\rho=\operatorname{span}\{(w-\rho)^j:m_\rho-1-2j\le r\}.
\]

Multiplication by \(w-\rho\) lowers its degree by two, and its \(r\)-th power maps grade \(r\) isomorphically to grade \(-r\). The original canonical section transports this filtration into actual theta cohomology. The full Taylor unit preserves it, acting on each grade by its actual complex leading scalar, including the root-difference product and derivative phase. The associated graded has an explicit \(\mathfrak{sl}_2\) raising operator \(Rt^j=j(m-j)t^{j-1}\), with the three commutators verified.

For the original attained metric \(G_N\), every graded quotient metric is the literal Schur minimum in the actual confluent basis. N4–N6 calculate these matrices, their determinant product with the full \(|\det V_Z|^2\) factor, and the singular values of the actual graded nilpotent isomorphisms. No cross blocks are erased. This supplies concrete matrices for the nilpotent part of mixed-state control; it does not assume arithmetic purity from the integer filtration labels.

## 7. The old finite-prime boundary index now has its missing actual lift

**Earlier proof read:** `globalization nte/4/split_zero_defect_preprint.tex`, complete sections at lines 425–1144, especially “Finite-prime boundary map”; also the corresponding primitive-defect sections. The old scalar cutoff is not itself in the required crossed product, so its winding needed a genuine projection and lift. This is now repaired in K1–K7, rather than left as a reason to discard the boundary construction.

Set \(\ell=\log p\), retain the original space \(Y_p=(\mathbb Z\cup\{\infty\})\times\mathbb R\), and retain the action \((m,y)\mapsto(m+1,y+\ell)\). Choose a compact continuous \(\chi\) satisfying \(\sum_n\chi(y-n\ell)^2=1\). The actual quotient projection and self-adjoint lift have finite convolution coefficients

\[
P_n(y)=\chi(y)\chi(y-n\ell),\quad
H_n(m,y)=\phi(y-m\ell)P_n(y),\quad H_n(\infty,y)=P_n(y),
\]

where \(\phi(t)=(1+e^t)^{-1}\). The full proof verifies compactness, continuity at the boundary, convolution, adjoints, the rank-one corner, and the generic algebra isomorphism. In its original logarithmic coordinate \(t=y-m\ell\), the exponential determinant is \(e^{2\pi i\phi(t)}\), which has winding \(-1\). Thus the **actual model extension** has \(\partial_p[P]=-1\).

**The full semilocal receiver is also proved:** K8–K10 define the original visible finite-unit-quotiented space with at most one zero coordinate. On its finite-prime edge the equivariant coordinate is \(y=\log|x|-\sum_{j\ne i}m_j\log p_j\). This gives the exact compact-operator tensor factor of the model extension, with common generic coordinate \(t=\log|x|-\sum_jm_j\log p_j\). The archimedean edge uses \(u=x\exp(-\sum_jm_j\log p_j)\) and retains both sign projections. The actual boundary row is therefore \(\delta_0=-(1,\ldots,1,1,1)\), with its primitive kernel and both K-groups computed. This restores a complete previously proposed branch of the arithmetic support construction.

Green's imprimitivity construction is cited to the human source, P. Green, *Acta Mathematica* 140 (1978), 191–250, [DOI 10.1007/BF02392308](https://doi.org/10.1007/BF02392308); here the needed generic representation, quotient projection and receiving coordinate maps are explicitly written and proved.

## 8. Earlier denominator inversion identifies the exact source obstruction

**Earlier proof read:** the complete denominator/carry and incidence-inversion sections of `split_support_geometry_arithmetic_curve_v11910.tex`, including `thm:mobius-history`. The finite divisor identity is classical Möbius inversion; the original source construction and the receiving proof are fully specified in MI1–MI9.

The actual inverse on positive \(x\) is

\[
(\mathcal I_\mu F)(x)=\tfrac12\sum_{n\ge1}\mu(n)F(nx),\qquad
\Theta\mathcal I_\mu F=F,\quad\mathcal I_\mu\Theta\phi=\phi.
\]

All derivatives converge absolutely locally, the infinity region is rapidly decreasing, and the zero region has an explicit \(O(x^{-1})\) bound. Hence the original global cohomology is exactly \(Q\cong\mathcal I_\mu(\mathscr B)/V\). This locates the obstruction in the original even-Schwartz source conditions at zero while retaining the zero-integral condition.

For each actual canonical finite section, MI5–MI7 calculate the inverse source using the complete original polynomial:

\[
\mathcal M(\mathcal I_\mu R_Zu)(w)
=\frac{r_Z(u)(w)}{h_Z(w)}\,
\frac{w(w-1)}2\pi^{-w/2}\Gamma(w/2).
\]

Every primary contributes its complete power/logarithm singularity \(x^{-\rho}P_\rho(-\log x)\); the remaining zero-end series is even and starts at \(x^2\). MI9 proves the exact threshold in the programme's original measure:

\[
\mathcal I_\mu R_Zu\in L^2(dx)
\quad\Longleftrightarrow\quad
u_\rho=0\text{ for all }\Re\rho\ge\tfrac12.
\]

The proof retains all frequencies and their cross terms; it does not assume pointwise orthogonality. A separate bounded Mellin-norm tail estimate is only asserted for \(\sigma>1\), and is explicitly not imported into \(dx\), where \(\sigma=1/2\). This is an exact analytic receiver from the earlier denominator machinery into the full source quotient, not a claim that the needed critical-line bound follows automatically.

## 9. The earlier tau-support space receives the entire original complex

**Earlier proofs read:** `split_support_geometry_arithmetic_curve_v11910.tex`, complete generic-point suspension and exact blueprint sections (2093–2221), and the fully read `split_zero_secondary_note.tex` support-diagram classification. The recipient is the full original \(\Theta:V\to\mathscr B\), not only the current finite cutoff.

S1–S4 give its exact sheaf realization on the underlying two-point space \(X=\operatorname{Spec}G(\mathbb C)\). The value on \(X\) is \(V\), the value on the new generic point is \(\mathscr B\), and restriction is the original \(\Theta\). An explicit two-term injective resolution proves

\[
R\Gamma_{\{z\}}(X,\mathcal F_\Theta)\simeq[V\xrightarrow{\Theta}\mathscr B],
\qquad H^1_{\{z\}}=Q.
\]

Every finite full Mellin-jet map and canonical section becomes an actual sheaf map to and from \(j_!E_Z\). Their cohomology maps are the original \(\overline J_Z\) and \(\sigma_Z\), and the original boundary source gives the explicit chain homotopy that makes the section \(D\)-equivariant on cohomology. Infinite original spaces are treated as algebraic sheaves; the finite primary recipients are finite-dimensional constructible sheaves.

The same arrow gives an actual \(G(\mathbb C)\)-semimodule \(M_\Theta=V\sqcup\mathscr B\), with mixed addition \(v\oplus b=\Theta v+b\). S5 proves its Bourne quotient by \(V\) is the split semimodule \(Q\sqcup\{\tau\}\). The unsupported-zero fiber is \(V\), while the supported-zero fiber is \(\Theta V\) inside the separate \(\mathscr B\) component. All original quotient maps and the operator descend exactly.

This supplies a geometric and a split-semimodule recipient for the whole analytic complex. The sheaf coefficient category is explicitly complex vector spaces on the underlying support space: it is not falsely presented as quasi-coherent localization over the generic Boolean structure stalk.

## 10. Actual reflection and the exact unweighted-completion receiver

**Earlier proof read in full:** `globalization nte/shefy/zeta_split_zero_compactified_shadows.tex`, including its jet equivariance and product/direct-sum compactification. RC1–RC10 supply the exact analytic recipient. On the original physical coordinate, inversion is \(\mathcal IF(x)=x^{-1}F(1/x)\), a unitary involution for the actual measure \(dx\), and \(\mathcal I\Theta\phi=\Theta\widehat\phi\). On the full primary jets its action is \((\mathsf Wu)_{\rho,j}=(-1)^j u_{1-\rho,j}\). The canonical original section intertwines this action strictly, with every derivative sign and multiplicity retained.

RC6 proves that the original derivative family \(\{D^rf_0:r\ge0\}\) is dense in \(L^2(dx)\), with no RH assumption. The proof establishes exponential integrability of the exact Mellin image \(2\xi(1/2+it)\), then uses an analytic Fourier transform to rule out any nonzero orthogonal vector. This gives the precise map \(Q\to L^2(dx)/\overline{\Theta V}=0\). The rapidly decreasing original topology and its continuous finite jets retain the nonzero classes.

The exact finite Gram minima in RC7 remain positive definite at every finite cutoff and tend to zero for each fixed finite divisor. RC10 constructs representatives with unchanged full jets and cohomology class but norm tending to zero. These minima use the explicitly displayed derivative relation span; no unidentified replacement of another programme denominator is made. The result identifies what this particular completion forgets, while retaining the original finite metrics for further estimates. It gives no uniform growing-divisor rate and does not assert programme failure. Root is separately carrying this through its already proved heat-metric comparison.

Human sources for the analytic tools are Stein–Shakarchi, *Fourier Analysis* (2003), Chapter 5, and the classical gamma asymptotic documented at [DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3). The Möbius calculation in section 8 now cites Apostol, *Introduction to Analytic Number Theory* (1976), Chapter 2, and its exact identity at [DLMF 27.5.2](https://dlmf.nist.gov/27.5.E2).

## 11. Full Hurwitz residues and bilateral interpolation into the actual zeros

**Earlier complete sections read:** `globalization cue/split_zero_cue_hurwitz_extensions.tex`, lines 595–1304, including compact Hurwitz averages, all-order zero motion, finite reconstruction and CUE observables. The two-endpoint residues there are correct. HU1–HU2 additionally evaluate every negative-even Gamma residue, including the strictly positive residue at \(-2\) for any nontrivial positive compact shift. Thus a two-endpoint subtraction alone cannot turn this particular shifted completion into an entire Mellin transform.

The actual repair is the complete bilateral lattice, with its missing central term retained:

\[
K_a(x)=2\sum_{n\in\mathbb Z}e^{-\pi(n+a)^2x^2},\qquad
F_a=D(D-1)K_a,\quad 0<a<1.
\]

HU3–HU6 prove \(F_a\) lies in the original rapidly decreasing space and calculate

\[
\mathcal MF_a(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)
[a^{-w}+\zeta(w,1+a)+\zeta(w,1-a)],
\quad\mathcal IF_a=4\sum_{n\ge1}\cos(2\pi na)\phi_*(nx).
\]

All negative-even poles cancel through the original reflected lattice and the explicit central term. The finite phase guard \(a\in[\epsilon,1-\epsilon]\) makes all endpoint estimates uniform without changing the physical coordinate.

HU7–HU10 prove the complete Mellin jets \(j(a)=J_ZF_a\) span every original finite divisor with all multiplicities. Their integral matrix \(\mathsf P=\int j(a)j(a)^*da\) is positive definite, and \(\mathsf Su=\int F_a j(a)^*\mathsf P^{-1}u\,da\) is an explicit right inverse of the original full jet map. The proof uses the complete \(a^{-\rho}\) logarithmic singularities and retains every cross-frequency term. The difference from the original canonical section is explicitly in \(\ker J_Z\); it is not identified with a theta-source relation. This is an additional actual test-family receiver, with a specified residual, rather than an assumed arithmetic sign or purity estimate.

Human provenance: Apostol, *Introduction to Analytic Number Theory* (1976), Chapter 12; the exact Bernoulli special value is equation (17), p. 264, documented at [DLMF 25.11.14](https://dlmf.nist.gov/25.11.E14). Gaussian Poisson summation uses the fixed convention and Stein–Shakarchi citation in the proof. This receiver awaits root mathematical review.

## Additional fully read branches and their present receiving status

- `period_holonomy_toeplitz_bridge.tex` proves the actual scalar prime-period map and the finite positive moment/Toeplitz test. Its extension through the earlier matrix-holonomy construction to the current positive-trace minimum is an available receiving calculation requiring work; no active owner or completed extension is asserted.
- `modular_cartan_realform_bridge_20260719.tex` and `full_noncommutative_k4_operation.tex` retain full noncommuting logarithmic/polar transport. Their complete finite matrix identities were read. The matrix-holonomy construction is an available receiving route. The old formula (g\mapsto(X\mapsto g^tXg)) is a **right** congruence action (an antihomomorphism under left composition); converting to a left representation requires (g^{-1}) or the corresponding opposite-group convention. This does not invalidate its displayed Cauchy–Green composition identity.
- `zeta_projective_infinity_k4.tex` was read in full. Its quartet sector (c_{-+}=4(\Re\rho-1/2)) exactly reconstructs the real displacement and its compactification. It supplies a faithful coordinate receiver for the existing quartet, not an estimate forcing this coordinate to vanish. Its pole-order/associator product does not on its own provide an arithmetic metric estimate.
- The Atlas source archive's complete packets 198, 199 and 200 were read. They contain exact regulator, Jordan and orthogonal-projector calculations, and explicitly retain missing cross-domain maps. No concrete new RH arithmetic receiver from their Brieskorn/Wilson data was found in those proofs; no analogy has been inserted into the programme.
- `split_zero_secondary_note.tex` was read in full. Its support-diagram equivalence supplies the correct fibrewise setting for supported zero amplitudes, and is already actually used in the programme's original labelled quotient maps. Its all-orders shifted-zeta and coprime-kernel formulas require their displayed convergence domains before continuation. They do not establish an RH zero-location estimate.

## Precise local repairs retained while reading

The spectral-packet paper's set equality with (\zeta(1/2-iz)=0) on the **whole** complex plane includes the images of trivial zeros. Its intended equality is correct on the stated strip or with (\xi) on the whole plane. All receivers above use the actual nontrivial divisor and full multiplicities. This is a local repair, not grounds for rejecting the construction.

The primitive-defect source's missing finite-prime Morita lift and its visible semilocal receiving coordinates have now been constructed in K1–K10. The value is proved for the explicitly specified finite-unit-quotiented space, rather than assigned to an unspecified crossed product by a rank comparison.

The old circle manuscript's unrelated manifold Laplacian-sign sentence is inconsistent with its displayed integration-by-parts convention. The imported circle operator (N=-(4\pi^2)^{-1}\partial_z^2), every Fourier factor, and every receiver above were checked directly.

Two further local corrections appeared in the selected complete sections of `zeta_split_zero_professional_preprint.tex`. Its general cyclotomic slider allows angles up to \(\pi\), so the printed ordinary arctangent must be replaced by the continuous upper-half-plane argument (or `atan2`); the inverse \(t=\sin\theta/\sin(\phi-\theta)\) remains valid across \(\theta=\pi/2\). The earlier refined divisor version with \(\phi=2\pi/5\) stays within the unproblematic chart.

Its blueprint paragraph also calls the fixed-pair inclusion \(\{\tau,e\}\hookrightarrow G(R)\) a semiring morphism. That inclusion preserves addition and multiplication but is **not unital**, since its domain identity is \(e\) and the target identity is \(1_R\). The exact unital maps already proved in the arithmetic-curve paper are \(p:G(R)\to R\), the support character \(\chi:G(R)\to\mathbb B\), and \(G(R)[e^{-1}]\cong\mathbb B\). The inclusion is correctly a map in the nonunital category, or the inclusion of the corner \(eG(R)\). The pointed multiplicative monoid \(\mathbb F_1=\{0,1\}\) has its unital map \(0\mapsto\tau,1\mapsto1_R\) to the underlying multiplicative monoid. This gives the strongest literal base/corner/quotient diagram without treating the Boolean fixed-pair inclusion as a unital base map.

## Reading remains open

There are further distinct manuscripts and long transcripts in the named roots, and multiple revisions need mathematical reconciliation. The whole arithmetic-curve manuscript has not yet been read: its complete denominator, Beurling, internal support, and lattice/valuation sections have. The two earliest Zenodo sources have been inspected at their actual semiring/F1 constructions; they are not falsely marked fully read. No corpus-wide coverage or completion is claimed.


The published proof clarifies U2 explicitly: divided-jet input `u` uses `V^-1 T u`; power-coefficient input `a` uses `V^-1 T V a`, with `u=V a`. Typographical repairs in MI8 and HM19 restore their displayed one-half factor and order relation. Prior source snapshots and the sealed HM edition are preserved.
