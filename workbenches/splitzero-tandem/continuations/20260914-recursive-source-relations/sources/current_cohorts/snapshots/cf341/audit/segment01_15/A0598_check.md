# A0598 independent algebra and map audit

## Scope and durable audit record

Source: output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0001_U0015.md, message A0598, lines **1136–1994**. All 859 lines were read. All line pins below refer to that source. This audit did not inspect the linked notebook, ZIP, cited books/papers, or earlier workbench results. An imported assertion whose proof is outside the excerpt is not classified as false merely for that reason.

Delegated instruction, verbatim:

> Bounded independent adversarial audit, read-only source output/tau_f1_transcript_audit_2026-09-13/sources/audit_segment_U0001_U0015.md, fully read lines 1136–1994 (A0598, 859 lines). Audit every explicit algebra/map in this message; strongest valid consequences and exact errors/circularities. No invented replacement program, no sources beyond given text unless needed to check cited definitions. Do not browse root browser. You may write only work/rh_counterfactual_20260913/shared_thread_audit/segment01_15/A0598_check.md. Send exact source line pins. Parent independently reading complete segment.

Completed work: full unnumbered read; numbered audit; exact hand calculations of the Mellin, Fourier, matrix, convolution, thermal, and differential identities; an independent subagent double-check of lines 1581–1755 and 1913–1949; arithmetic verification of the reported reduction ratio. No browser, Lean, or external source was used. This is the only file written by this audit.

## Findings

1. **The central displayed algebra is sound.** The Mellin coefficient, matrix-defect signs, quartet cross-pairing, toy-model zeros, heat-coordinate factor \(1/4\), gap equation, and swirl conjugation check. It would be inaccurate to dismiss A0598 as entirely verbal analogy.
2. **Its actual chosen background has a stronger exact identity than the text states:**
   \[
   L_e(w)=\frac{\xi(w+1/2)}{4\pi^2},\qquad e(-y)=e(y),
   \]
   and the kernel in the message's Riemann-heat normalization is
   \[
   \Phi(u)=2\pi^2e(2u)
   =\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
   \]
   The proof below retains the original constants. This exact relation links sections 6 and 8 internally; it supplies no negative Weil witness.
3. **The NS energy limit at 1354–1355 requires \(h<1/6\), absent locally.** The cited NS source may supply it. The exponent multiplication itself is correct.
4. **The quartet formula at 1572 suppresses multiplicity:** one copy contributes \(4\operatorname{Re}(a\bar b)\); common root multiplicity \(m\) gives \(4m\operatorname{Re}(a\bar b)\).
5. **The RH-driving collision estimate is expressly unproved** at 1739–1755. The displayed criterion is a correct conditional obstruction, not a completed counterexample.
6. **The arithmetic trace and prior four-jet claims are imported.** Lines 1481–1490 omit the representation, trace domain, and local distributions; lines 1891–1897 omit \(T\), its ideal, and the lift. The block calculation does not prove these identifications.
7. **The finite search cannot be reproduced from this excerpt.** Its archimedean formula, coefficients, matrices, quadrature, and rigorous error bounds are absent. The text correctly disclaims certification. The normalized numerical ratio does not by itself verify the separately reported unnormalized fixed-core Schur percentage.

## BC heat, pole, and state calculations

**Pins: 1154–1228.** On \(\ell^2(\mathbb N_{\ge1})\), \(N|n\rangle=n|n\rangle\) and \(H=\log N\) are self-adjoint diagonal operators on their maximal domains. The scalar Gamma integral is
\[
\int_0^\infty x^{\beta/2-1}e^{-\pi xn^2}\,dx
=\Gamma(\beta/2)(\pi n^2)^{-\beta/2}.
\]
Multiplication by \(\pi^{\beta/2}/\Gamma(\beta/2)\) gives \(n^{-\beta}\), exactly as displayed. The operator integral converges in norm for \(\operatorname{Re}\beta>0\): near zero, its norm is bounded by \(x^{\operatorname{Re}\beta/2-1}\), and at infinity by that power times \(e^{-\pi x}\). Tracing requires \(\operatorname{Re}\beta>1\). For real \(\beta>1\), nonnegativity justifies the sum/integral interchange.

The unitary map \(|n\rangle\mapsto e^{in\theta}/\sqrt{2\pi}\) onto the positive-frequency circle subspace sends \(N^2\) to \(-\partial_\theta^2\). Thus the circle-Laplacian statement at 1183 is valid for this subspace; it is not an NS-generator identification.

For \(\theta(x)=1+2\sum_{n\ge1}e^{-\pi xn^2}\), Poisson gives \(\theta(x)=x^{-1/2}\theta(1/x)\), hence exactly 1197–1200. The leading integral is
\[
\frac12\int_0^1x^{(\beta-1)/2-1}\,dx=\frac1{\beta-1}.
\]
The next theta term \(-1/2\) contributes \(-1/\beta\) after integration and continuation. The leading \(s=1\) pole coefficient is correct. The calculation does not create off-line zeros, as 1228 acknowledges.

**Pins: 1234–1240.** KMS classification is cited, not proved by the Gamma integral. What that integral proves here is failure of the trace-class Gibbs expression at \(\beta=1\). This is compatible with the separately cited algebraic KMS-state existence.

**Pins: 1246–1272.** Termwise differentiation for \(\beta>1\) gives the stated mean. With
\[
\zeta(1+\epsilon)=\epsilon^{-1}+\gamma_E+O(\epsilon),
\]
one obtains \(-\zeta'/\zeta=\epsilon^{-1}-\gamma_E+O(\epsilon)\). For \(X_\epsilon=\epsilon\log n\) and real \(s\ge0\),
\[
\mathbb E(e^{-sX_\epsilon})
=\frac{\zeta(1+(1+s)\epsilon)}{\zeta(1+\epsilon)}
\longrightarrow\frac1{1+s},
\]
which proves the exponential distributional limit. The transform identity extends to \(\operatorname{Re}s>-1\); it is not asserted valid at arbitrary \(s\). Escape itself also follows directly, since for fixed \(R\),
\[
\mathbb P_\epsilon(\log n\le R)
=\frac{\sum_{n\le e^R}n^{-1-\epsilon}}{\zeta(1+\epsilon)}
\longrightarrow0.
\]

**Pins: 1276–1312.** For \(t<1\), \(\tau=1-t>0\), \(s=-\log\tau\), and \(\Lambda=e^s\), the character identity is exactly
\[
\Lambda^{\delta+i\gamma}
=e^{\delta s}e^{i\gamma s}
=\tau^{-\delta}e^{-i\gamma\log\tau}.
\]
This is a representation of the positive multiplicative group, using its real logarithm. No NS object is mapped into it; 1312 explicitly acknowledges that missing identification.

**Pins: 1316–1333.** In the Gibbs representation,
\[
\operatorname{Tr}(N^{-\beta}N^{-it})/\zeta(\beta)
=\zeta(\beta+it)/\zeta(\beta).
\]
It is the characteristic function with the \(e^{-itE}\) sign convention. If \(\zeta(z)=(z-\rho)^ma(z)\), \(a(\rho)\ne0\), then
\[
-\zeta'/\zeta=-m/(z-\rho)-a'/a.
\]
The Laurent coefficient is correct. This concerns the continued response, not divergence of a real-temperature Gibbs state.

## NS exponents and the explicit concentration example

**Pins: 1343–1358.** The cylindrical volume has scale \(\ell_r^2\ell_z=\tau^{3/2-h}\), and squared velocity has scale \(\tau^{-1-2h}\). The product is \(\tau^{1/2-3h}\). It tends to zero precisely for \(h<1/6\), is constant order at \(h=1/6\), and diverges for \(h>1/6\). The arrow to zero therefore uses a range absent from this excerpt. The claimed smooth-force and global-energy properties are imported NS results, not consequences of these exponents alone.

**Pins: 1373–1394.** For \(E_n=\log n>1\), the two weights in \(\rho_n\) are positive and sum to one. Since the support energies are \(0,E_n\),
\[
\operatorname{Tr}(\rho_nH^k)=E_n^{k-1}\quad(k>0).
\]
The difference from the ground-state projector has eigenvalues \(-1/E_n,+1/E_n\), so its trace norm is \(2/E_n\). All the states commute with \(H\) and are stationary. Their diverging stronger moment under trace-norm convergence is exact. No KMS property is inferred or claimed for them.

## Operator defect and arithmetic trace

**Pins: 1402–1424.** The crossed-product/cooling/cokernel/\(HC_0\) chain names constructions but does not define its morphisms or trace domains. It is not a proof of the composite. The cited spectral theorems might supply them. The established diagonal \(H\) has spectrum \(\{\log n\}\), so off-line zeta zeros would not contradict its self-adjointness. The excerpt supplies no equality of those two spectra.

**Pins: 1430–1477.** With the exact displayed decomposition,
\[
-\tfrac12U^*[2P-I,U]=P-U^*PU,
\qquad
U^*PU=\begin{pmatrix}C^*C&C^*D\\D^*C&D^*D\end{pmatrix}.
\]
The bottom-right defect entry is \(I-D^*D=B^*B\), by unitarity. Thus both the matrix and its quadratic form are correct:
\[
\langle(x,y),\mathscr D(x,y)\rangle
=\|By\|^2-\|Cx\|^2-2\operatorname{Re}\langle Cx,Dy\rangle.
\]
When \(C=0\), \(UU^*=I\) gives \(DD^*=I\), so \(D^*D\) is a projection and \(B^*B=I-D^*D\) is a projection. This proves positivity and the projection statement at 1473. Conversely \(\mathscr D\ge0\) forces \(C=0\) by testing \((x,0)\). In finite dimension triangular unitarity also forces \(B=0\); a nonzero such positive projection is an infinite-dimensional phenomenon.

For compact \(C\),
\[
\mathscr D-\begin{pmatrix}0&0\\0&B^*B\end{pmatrix}
=\begin{pmatrix}-C^*C&-C^*D\\-D^*C&0\end{pmatrix}
\]
is compact. This proves positivity modulo compact operators from the displayed data, without proving ordinary positivity. Since \(\mathscr D\) is a difference of orthogonal projections, it is self-adjoint and has norm at most one.

**Pins: 1481–1494, 1980–1987.** Equality of this operator trace with \(-\sum_vW_v(g*g^*)\) is an additional arithmetic trace theorem. It does not follow from the block multiplication. Positivity of \(\vartheta(g*g^*)\) requires the specified *-representation and involution; its trace product requires the stated domain. These objects are not defined here. The text is correct that an arbitrary negative rank-one weight cannot replace an admissible convolution weight. A negative vector of \(\mathscr D\) is not an exhibited negative arithmetic trace.

**Pins: 1506–1520.** For normalized \(e_N\) and \(\epsilon_N>0\), the perturbation has norm \(2\epsilon_N\to0\), and changes the eigenvalue on \(e_N\) from \(\epsilon_N\) to \(-\epsilon_N\). This example is correct and establishes only instability near a vanishing gap, not the arithmetic sign.

## Quartet, interpolation, and finite thermal model

**Pins: 1524–1553.** For a nontrivial off-line zero, conjugation and \(s\mapsto1-s\) produce the displayed four centered roots, with equal multiplicity. For the matrices,
\[
e^{sG_\pm}=e^{\pm\delta s}
\begin{pmatrix}\cos\gamma s&-\sin\gamma s\\
\sin\gamma s&\cos\gamma s\end{pmatrix}.
\]
The rotation/growth statements are exact; no NS intertwiner has been constructed.

**Pins: 1555–1577.** The involution later defined at 1851 gives
\[
L_{h*h^*}(w)=L_h(w)\overline{L_h(-\bar w)}.
\]
For real \(h\), the quartet terms are \(a\bar b,\bar a b,b\bar a,\bar b a\). Their sum is \(4\operatorname{Re}(a\bar b)\), multiplied by the common zero multiplicity if applicable. On the imaginary \(w\)-axis, each summand is \(|L_h(w)|^2\). This proves the cross-pairing statement exactly.

The interpolation assertion is consistent and can be checked without assuming that an actual off-line zero exists. For fixed \(\delta\gamma\ne0\), the six real functions
\[
e^{\delta y}\cos\gamma y,\ e^{\delta y}\sin\gamma y,\
e^{-\delta y}\cos\gamma y,\ e^{-\delta y}\sin\gamma y,\
e^{y/2},\ e^{-y/2}
\]
are linearly independent on any interval, because their six complex exponential exponents are distinct. For a compact smooth \(\psi\ge0\) positive on an interval, their Gram matrix \(G_{ij}=\int\psi f_if_j\) is positive definite. Indeed a zero quadratic value forces an analytic combination to vanish on that interval, hence all coefficients vanish. Setting
\[
h=\psi\sum_i(G^{-1}t)_if_i,\quad t=(1,0,-1,0,0,0)
\]
imposes \(a=1,b=-1,L_h(\pm1/2)=0\). This verifies existence at the level stated, not the unseen implementation. The other zeta zeros remain in the full form, exactly as 1575–1577 acknowledge. No circular assumption of an actual quartet is hidden here.

**Pins: 1585–1628.** Tracing gives \(3e^{-\eta}+2\cos z\), and multiplication by \(e^\eta\) gives \(F_\eta=3+2e^\eta\cos z\). Its real-parameter denominator \(3+2e^\eta\) is positive. Differentiation gives \(\partial_\eta F_\eta=-F_\eta''\). With \(R=\tfrac32e^{-\eta}\), the zero equation is \(\cos z=-R\). For \(R>1\), all zeros are
\[
z=(2k+1)\pi\pm i\operatorname{arcosh}R,\quad k\in\mathbb Z.
\]
The nearest four are the displayed quartet. At \(R=1\), all odd multiples of \(\pi\) are double because \(F'=0,F''=3\). For \(0<R<1\), all zeros are real: if \(z=x+iy\) had \(y\ne0\), the vanishing imaginary part forces \(\sin x=0\), making the real part's absolute value at least one. This proves every stated model claim while its Gibbs state stays positive.

## Exact Mellin identity for the chosen background and Riemann kernel

**Pins: 1773–1792; internal connection to 1634–1669 and 1889.** Use the Fourier convention \(\widehat f(\xi)=\int f(v)e^{-2\pi iv\xi}\,dv\). For \(g(v)=e^{-\pi v^2}\),
\[
\widehat{v^2g}=(1/(2\pi)-\xi^2)g,\qquad
\widehat{v^4g}=(\xi^4-3\xi^2/\pi+3/(4\pi^2))g.
\]
Their displayed linear combination yields \(\widehat\phi=\phi\). Also
\(\int v^2g=1/(2\pi)\) and \(\int v^4g=3/(4\pi^2)\), so \(\phi(0)=0,\int\phi=0\). The Fourier convention is required to specify the claimed identity.

Evenness, self-Fourier invariance, and \(\phi(0)=0\) imply by Poisson
\[
\sum_{n\ge1}\phi(nx)=x^{-1}\sum_{n\ge1}\phi(n/x).
\]
Thus \(\mathcal E\phi(x)=\mathcal E\phi(1/x)\), and \(e(y)=e(-y)\). Gaussian decay at \(y\to+\infty\) and reflection give faster-than-exponential decay at both ends; \(L_e(w)\) is entire.

Set \(s=w+1/2\), retaining the source's centered coordinate. For \(\operatorname{Re}s>1\), absolute convergence and \(t=nx\) give
\[
L_e(w)=\zeta(s)\int_0^\infty\phi(t)t^{s-1}\,dt.
\]
The exact integral is
\[
\begin{aligned}
\int_0^\infty\phi(t)t^{s-1}\,dt
&=\tfrac12\pi^{-(s+4)/2}\Gamma((s+4)/2)
-\tfrac{3}{4\pi}\pi^{-(s+2)/2}\Gamma((s+2)/2)\\
&=\frac{s(s-1)}8\pi^{-s/2-2}\Gamma(s/2).
\end{aligned}
\]
For \(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\), analytic continuation proves
\[
\boxed{L_e(w)=\xi(w+1/2)/(4\pi^2)}
\]
everywhere. This gives exact vanishing with the zeta multiplicities. Identifying it with a particular source's named quotient radical still requires that source's test space and pairing. In the ordinary zero-evaluation pairing, all mixed pairings with this uncut background vanish term by term.

By evenness and \(y=2u\),
\[
\frac18\xi(1/2+iz/2)
=\frac{\pi^2}2\int_{\mathbb R}e(y)e^{izy/2}\,dy
=2\pi^2\int_0^\infty e(2u)\cos(zu)\,du.
\]
Consequently the kernel with the normalization at 1635–1637 is
\[
\Phi(u)=2\pi^2e(2u)
=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Uniqueness follows from Fourier injectivity for the even integrable extensions. For \(u\ge0\), every summand is positive, as its prefactor equals
\(\pi n^2e^{5u}(2\pi n^2e^{4u}-3)>0\). Moreover,
\[
0<\Phi(u)\le C e^{9u}e^{-\pi e^{4u}},
\]
since the remaining sum is bounded by a constant times
\(\sum n^4e^{-\pi(n^2-1)}<\infty\).

This quantitative estimate fills an exposition gap at 1640. Bare “super-exponential decay,” if meaning faster than every \(e^{-cu}\), is insufficient to justify multiplication by \(e^{\eta u^2}\) for every positive \(\eta\): \(e^{-u^{3/2}}\) is a counterexample. The actual kernel has the required stronger bound.

The denominator \(2H_\eta(0)\) is exactly its symmetric total mass and is finite and positive for all real \(\eta\). Symmetry gives the normalized Fourier identity. The quantitative bound permits every needed parameter derivative, yielding
\[
\partial_\eta\log H_\eta(0)=\mathbb E_\eta[u^2],\qquad
\partial_\eta^2\log H_\eta(0)
=\mathbb E_\eta[u^4]-\mathbb E_\eta[u^2]^2.
\]
These positive probability measures do not force all zeros of their characteristic functions to be real.

## Heat coordinates, Dirichlet terms, and collision criterion

**Pins: 1676–1688.** The threshold theorem and Rodgers–Tao bound are imported. Their stated logical combination gives \(RH\Longleftrightarrow\Lambda=0\). No positive lower bound is exhibited here.

**Pins: 1690–1713.** The kernel gives \(\partial_\eta H_\eta=-\partial_z^2H_\eta\). For \(z=-2i(s-1/2)\),
\[
\partial_s^2\Xi_\eta=8(-2i)^2H_\eta''=-32H_\eta'',\qquad
\partial_\eta\Xi_\eta=-8H_\eta''.
\]
Thus the factor \(+1/4\) is exact; substitution gives \(\Xi_0(s)=\xi(s)\).
The raw Dirichlet identity follows from
\(\partial_s^2n^{-s}=(\log n)^2n^{-s}\).
For \(\eta<0\), its magnitude on compact \(s\)-sets is eventually bounded by \(n^{-2}\), proving absolute locally uniform convergence. For \(\eta>0\),
\[
\left|e^{\eta(\log n)^2/4}n^{-s}\right|
=e^{\eta(\log n)^2/4-(\operatorname{Re}s)\log n}\to\infty.
\]
The raw evolved series is not thereby the completed heat family; the completion multiplier does not commute with \(\partial_s^2\). A0598 does not explicitly make that invalid identification.

**Pins: 1717–1755.** The zero-motion formula uses the cited but unreproduced summation convention. Its algebraic subtraction is correct. With
\[
S=\sum_{j\notin\{a,b\}}\frac1{(b-x_j)(a-x_j)},
\]
one gets \(d'=4/d-2dS\) and \((d^2)'=8-4d^2S\). For neighboring real roots every exterior denominator product is positive. Omitting \(S\) is a two-root model, not a justified step for the actual Riemann dynamics.

The excerpt's asserted bound \(d^2S\le\theta<2\) would give \(q'=(d^2)'\ge c=8-4\theta>0\), hence
\[
q(\eta)\le q(\eta_1)-c(\eta_1-\eta).
\]
Thus its comparison \(q(\eta_1)<c\eta_1\) is the correct one for failure of distinct real continuation at positive time. This audit verifies that implication, not its unproved premise. If another collision invalidates the simple-real evolution first, the calculation alone does not identify the selected pair as first. The missing actual estimate is acknowledged at 1755.

## Compact packets, pole cancellation, and finite numerics

**Pins: 1761–1769, 1792–1823.** The bump is \(C_c^\infty\), with all boundary derivatives zero. The packet supports satisfy
\[
\operatorname{supp}p_+\subset[0.05L,0.91L],\qquad
\operatorname{supp}p_-\subset[-0.91L,-0.05L].
\]
The bracket \(f\) in 1810–1812 is in \(C_c^\infty([-L,L])\), as is \(h_c=(D_y^2-1/4)f\). Two integrations by parts give
\[
L_{h_c}(w)=(w^2-1/4)L_f(w),
\]
so pole cancellation at \(w=\pm1/2\) is exact.
The background is even. Reflection splits packets into even and odd combinations; for a reflection-invariant real Weil form the cross-pairing between even background and odd channels is zero. This symmetry does not determine the remaining sign.

**Pins: 1827–1847.** For the real symmetric restricted form, the quadratic expansion is exact. Under its explicitly assumed \(A>0\),
\[
q_0+2b^{\mathsf T}c+c^{\mathsf T}Ac
=(c+A^{-1}b)^{\mathsf T}A(c+A^{-1}b)
+q_0-b^{\mathsf T}A^{-1}b.
\]
This proves both minimizer and minimum, without proving positive definiteness of the unseen actual matrix. It minimizes unnormalized \(Q\) with fixed core coefficient. It does not minimize \(Q/\|h\|_2^2\), whose denominator changes with the coefficients.

**Pins: 1851–1861.** Convolution gives support in \([-2L,2L]\), proving the exact prime cutoff \(p^m\le e^{2L}\). Also \(k(-y)=\overline{k(y)}\), so the displayed prime contribution is real. The coefficient and sign are consistent with the claimed centered explicit-formula convention, but the undefined \(W_\infty\) prevents complete independent evaluation from this excerpt. Stating that code contains its origin regularization and tail is not a displayed proof of the implementation.

**Pins: 1863–1883, 1991.** There are \(3\cdot3\cdot2=18\) parameter choices. The quoted core value divided by the finest-grid value is \(69.14125006987673\); the normalized decrease is \(98.55368539187624\%\). This checks “roughly 69.” It does not check the separate fixed-core Schur decrease without the associated coefficients and norms. The last two grid values differ by \(3.3279\times10^{-13}\), demonstrating reported numerical stabilization, not a rigorous error bound. The 29 check groups and numerical implementation are not present in the excerpt. The message correctly reports no negative candidate and no interval certification.

## Mellin operations and omitted quotient data

**Pins: 1887–1905.** With the source's transform and endpoint decay, the exact operations are
\[
L_{f(\cdot-a)}(w)=e^{aw}L_f(w),\qquad
L_{\partial_yf}(w)=-wL_f(w),\qquad
L_{yf}(w)=\partial_wL_f(w).
\]
Translation and differentiation multiply the Mellin transform and preserve its zeta divisor. Multiplication by \(y=\log x\) differentiates it. For this message's particular \(e\),
\[
L_{ye}(w)=\xi'(w+1/2)/(4\pi^2).
\]
At a zero \(\rho\) of multiplicity \(m\), writing
\(\xi(s)=(s-\rho)^ma(s)\), \(a(\rho)\ne0\), shows that the derivative has exactly order \(m-1\), with coefficient \(ma(\rho)\ne0\). This verifies the one-order-loss mechanism including multiple zeros. For an arbitrary \(T\) with extra vanishing factors, the remaining order depends on those factors; multiplication by \(\log x\) is not an automatic quotient certificate for every \(T\).

The actual claim \([(\log x)T]\ne0\) at 1894 is not checkable without \(T\), the ideal, and the four-jet map. The excerpt qualifies it by trace-ideal hypotheses at 1897. The weighted-\(L^2\) radical-density and terminal-jet/right-inverse claims are also imported without spaces and proofs here. The exact Mellin operations prove a real relationship, but not those omitted quotient identifications or a sign.

The smooth/holomorphic claim at 1905 is correct on a connected holomorphic domain: infinite-order interior vanishing makes the Taylor series zero, and the identity theorem propagates that vanishing. The already displayed bump supplies nonzero smooth flat germs. Two entire functions agreeing on an open set agree everywhere; smooth test cutoffs do not authorize local modification of the entire \(\xi\).

## Modular flow, swirl operator, and unproved composite

**Pins: 1913–1918.** For the declared convention and faithful Gibbs density \(\rho=Z^{-1}e^{-\beta H}\), spectral calculus yields
\[
\rho^{-is}=Z^{is}e^{i\beta sH},\qquad
\rho^{is}=Z^{-is}e^{-i\beta sH}.
\]
The scalar phases cancel, proving the sign at 1917. The opposite modular-time convention reverses the sign; that is not an error here because the convention is explicit.

**Pins: 1926–1949.** The map \(\mathcal Uu(y)=e^yu(e^y)\) is unitary from \(L^2((0,\infty),r\,dr)\) to \(L^2(\mathbb R,dy)\):
\[
\int_{\mathbb R}|e^yu(e^y)|^2dy=\int_0^\infty|u(r)|^2r\,dr.
\]
For \(u(r)=r^{-1}b(\log r)\),
\[
u_r=r^{-2}(b'-b),\qquad
u_{rr}=r^{-3}(b''-3b'+2b),
\]
hence
\[
(\partial_{rr}+r^{-1}\partial_r-r^{-2})u
=r^{-3}(b''-2b').
\]
Multiplication by \(r=e^y\) gives exactly
\[
\mathcal U\mathcal L_{\rm sw}\mathcal U^{-1}b
=\nu e^{-2y}(b''-2b')
=\nu\partial_y(e^{-2y}\partial_yb).
\]
The identity holds on \(C_c^\infty\) and on transported operator domains. Since closed realizations and endpoint conditions are absent, the excerpt alone proves a differential-expression identity rather than equality of unspecified closed operators. Integration by parts also gives the exact transformed quadratic form
\[
-\langle b,\mathcal U\mathcal L_{\rm sw}\mathcal U^{-1}b\rangle
=\nu\int_{\mathbb R}e^{-2y}|b'(y)|^2dy.
\]
This proves a relation between the original energy geometry and log-coordinate diffusion. It does not include the nonlinear NS dynamics or the arithmetic trace.

**Pins: 1911, 1920–1924, 1951–1965.** The gravity/horizon theorems are cited, with hypotheses and constructions absent here. The four-step composite at 1954–1960 is expressly still unproved. No complete state-space map, observable intertwiner, dynamics intertwiner, units dictionary, or trace-preserving morphism is supplied. This establishes that A0598 has not constructed the composite, not that such a relation is impossible.

## Conclusion

A0598 contains correct exact mathematics and a recoverable exact relation from its chosen global arithmetic background to the Riemann heat kernel. Its statement that no negative witness was established is consistent with the displayed work. Its limitations are locally omitted hypotheses/domains, imported trace/quotient results without definitions, unverified artifact/numerical reports, and the explicitly unproved estimate at the point where an RH disproof would have to occur. A generic negative defect vector, a positive-state toy quartet, finite interpolation at hypothetical roots, or positive finite numerical tests cannot be promoted to an established sign for the full arithmetic pairing.
