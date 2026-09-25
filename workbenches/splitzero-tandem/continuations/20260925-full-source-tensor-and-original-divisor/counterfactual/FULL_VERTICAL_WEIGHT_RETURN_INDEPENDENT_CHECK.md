# Independent check of the complete vertical receiving family

25 September 2026. Mathematical verification VWC0–VWC7. The complete [VWR0–VWR9 proof and the subsequently added VWR10](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/FULL_VERTICAL_WEIGHT_RETURN.md) were read. This check concerns their constructed coefficient receivers and exact maps, not a numerical weight assigned to primitive \(Z_1/\tau\). Source B1–B5/P1–P5/R1 and the complete relevant corpus references were checked in WHR0; none changes here.

## VWC0. Dependencies and scope

The independent calculation [WHR0–WHR12](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/counterfactual/WEIGHTED_HILBERT_RETURN_AND_EXACT_KERNEL.md) gives the full proof of weighted Fourier-dual approximation and the exact original summation-image annihilator. It retains the original Mellin transform, the factor two in \(\Sigma\), and every actual zero multiplicity. Alain Connes, [math/9811068v1, Section III, Theorem 1, and Appendix I](https://arxiv.org/abs/math/9811068v1), is the human source of the weighted Hilbert spectral mechanism; his parameter satisfies \(\delta_{\rm C}=2\delta\). VWR and WHR record actual author-source reading coverage. The original cohomology and supported pairing are the retained Connes–Consani coefficient construction and programme SSI/GZR/DCP proofs cited in those complete files.

## VWC1. The measure, norm, and complete prime action

For the exact measure in VWR2.1,
\[
u^{2\sigma-1}(1+(\log u)^2)^\delta\,du
=e^{2\sigma x}(1+x^2)^\delta\,dx,\qquad u=e^x.
\]
Thus \(U_\sigma b(x)=e^{\sigma x}b(e^x)\) has the claimed isometric inverse \(u^{-\sigma}g(\log u)\), and its positive Fourier transform is the original Mellin value at \(\sigma+it\). The alternate exponent \(u^{1-2\sigma}\) would select \(1-\sigma\), and is not the formula used in VWR.

The original action satisfies
\[
U_\sigma T_aU_\sigma^{-1}g(x)=a^\sigma g(x-\log a).
\]
After substitution \(x=y+\log a\), its squared norm is \(a^{2\sigma}\) times the ratio of the displayed logarithmic weights. The ratio maximum is the larger eigenvalue of a determinant-one symmetric matrix with trace \(2+(\log a)^2\). This gives exactly
\[
\|T_a\|=a^\sigma
\left(\frac{(\log a)^2+2+|\log a|\sqrt{(\log a)^2+4}}2\right)^{\delta/2}.
\]
Localized smooth bumps prove sharpness, including continuity at \(a=1\). Since \(\Lambda_+(nt)\leq n^2t^2+2\), the retained factor \(\Lambda_+(nt)^{\delta/(2n)}\) tends to one. Applied both to the quotient action and its inverse, the spectral-radius formula therefore gives exactly the circle \(|z|=p^\sigma\) as a spectral containment. No estimate at an individual finite \(n\) is omitted.

## VWC2. The closure proof holds for every stated vertical line

The exact dual density of \(F^{(j)}(\rho)\) in logarithmic coordinates is
\[
x^j e^{(\rho-\sigma)x}.
\]
Its squared dual norm is
\[
\int_{\mathbb R}|x|^{2j}e^{2(\Re\rho-\sigma)x}(1+x^2)^{-\delta}dx.
\]
It is finite precisely when \(\Re\rho=\sigma\) and \(j<\delta-1/2\); at the endpoint it diverges logarithmically. The direct Riesz representative in the original variable is \(u^{\bar\rho-2\sigma}(\log u)^j(1+(\log u)^2)^{-\delta}\), with the stated beta-integral norm.

The explicit source \(h_0\) has Mellin transform \((s-1)e^{s^2}/2\). Its actual original image \(b_0=\Sigma h_0\) therefore has transform \((s-1)\zeta(s)e^{s^2}\), with no unspecified scalar. On \(0<\sigma<1\), the factor \(s-1\) is nonzero, and this multiplier has exactly the original zeros on that line. For the positive Fourier convention, the correlation
\(\int (U_\sigma b_0)(x-y)w(x)dx\)
has transform
\(\widehat{U_\sigma b_0}(-t)\widehat w(t)\).
Thus the sign in VWR4.5 is correct. Its real support points are \(-\Im\rho\); inversion gives polynomial multiples of \(e^{i\Im\rho x}\), the correct original derivative functionals.

The cutoff proof is uniform in this coordinate calculation: every \(U_\sigma\) produces the same weighted space \(L^2((1+x^2)^\delta dx)\). The proof in WHR4 uses the estimate
\[
\|w(\cdot-z)\|_{L^2((1+x^2)^{-\delta}dx)}
\leq2^{\delta/2}(1+z^2)^{\delta/2}
\|w\|_{L^2((1+x^2)^{-\delta}dx)}
\]
and a Schwartz approximate identity. It gives convergence in the actual dual norm. Every finite frequency cutoff has only finitely many multiplier zeros. Local division and the exact zero order then force only delta derivatives below the original multiplicity. Localizing to one frequency and applying the weighted integrability calculation also forces \(j<\delta-1/2\). Conversely every allowed derivative annihilates the original \(J\). The norm-dense span of these functionals is therefore the whole annihilator, proving VWR4.3 on every stated line, without RH or an assertion about numerical spacing of zeros.

## VWC3. Full-family faithfulness and the location of the closure operation

By the proved original Mellin identification, the kernel of each receiver map is exactly \(I_{\sigma,\delta}/I\). If a class maps to zero in the whole family, choose, for each actual zero \(\rho\) and derivative order \(0\leq j<m_\rho\), the component
\[
\sigma=\Re\rho,\qquad N=j+1.
\]
Then \(j<N-1/2\), so that derivative vanishes. The defining ideal \(I\) imposes exactly all these conditions. This proves joint injectivity; no unrestricted-product identification is used.

The strict original-complex map is identity on the complete \(P\) and inclusion on \(A\). The kernel in degree zero stays \(\ker d\), and its algebraic degree-one map
\[
A/J\longrightarrow\mathcal H_{\sigma,\delta}/J
\]
is injective. The subsequent Hausdorff quotient has kernel \(C_{\sigma,\delta}/J\), and its intersection with the embedded original quotient is precisely \(I_{\sigma,\delta}/I\). Hence the claimed loss is in a specified closure step; it is not an inconsistency of primitive \(\tau\), or an omission of endpoint or extra closed coefficients.

## VWC4. The original mirror and its exact character

Since
\[
U_{1-\sigma}Rb(x)
=e^{(1-\sigma)x}e^{-x}b(e^{-x})
=U_\sigma b(-x),
\]
the mirror is an isometry from the \(\sigma\) receiver to the \(1-\sigma\) receiver. Its original identities \(RT_a=aT_{a^{-1}}R\) and \(F^{(j)}(\rho)\mapsto(-1)^jF^{(j)}(1-\rho)\) follow without a change of arithmetic parameter. The full Poisson identity proves that \(R\) preserves the original \(J\), so it carries their closures and quotients exactly as stated.

The paired radii are \(p^\sigma\) and \(p^{1-\sigma}\), with product \(p\). Under the Deligne convention \(|\alpha|=p^{w/2}\), this product character has weight \(2\); individual weight \(1\) would mean each radius is \(\sqrt p\). The phrase “weight-one paired action” must therefore be replaced by the actual character-\(a\) similitude, or by this explicitly stated convention. This is a terminology correction, not a change of the proved action.

## VWC5. The full residue pairing on the critical-family kernel

The functional-equation multiplier
\[
\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}
\]
is meromorphic globally and is holomorphic and nonzero at every nontrivial zero. Accordingly it must be called the full original meromorphic multiplier, not an entire function. The auxiliary \(F_*\) in VWR8.4, with all its displayed factors, is entire; its values \(F_*(0)=F_*(1)=1/8\) are correct, as are the stated values at negative even integers and the reciprocal-Taylor construction.

Let a nonzero original class in \(K_{\rm off}=I_{\rm line}/I\) have first nonzero Taylor degree \(\ell\) at a noncritical \(\rho\), of multiplicity \(m\). The complete original isolator at \(1-\rho\), of degree \(m-1-\ell\), has every other full zero jet zero. Thus the complete contour form has only that one possible residue. Its coefficient is exactly
\[
(-1)^{m-1-\ell}
\frac{F^{(\ell)}(\rho)}{\ell!}\,
\frac{m!}{\zeta^{(m)}(\rho)}.
\]
It is nonzero. Both classes lie in \(K_{\rm off}\), because their critical-line jets vanish. Reversing the slots gives
\[
(-1)^\ell\frac{G^{(\ell)}(\eta)}{\ell!}\,
\frac{m_\eta!}{\zeta^{(m_\eta)}(1-\eta)}
\]
for the reflected point \(1-\eta\), with the equal reflected multiplicity. This verifies two-sided nondegeneracy on the entire \(K_{\rm off}\), including arbitrary classes with infinitely many allowed jets: one nonzero original jet suffices for its actual isolating partner. The finite-residue use is justified by the full original contour decay already proved in GZR5 and retained in VWR8; no infinite residue sum was introduced.

For the truncated block, the annihilator of \(t^r\mathbb C[t]/t^m\) in the reflected block is exactly \(v^{m-r}\mathbb C[v]/v^m\). Multiplication by the full unit series \(\zeta(\rho+t)/t^m\) or its inverse preserves vanishing order. Testing \(t^r,\ldots,t^{m-1}\), successively, forces the first \(m-r\) reflected coefficients to vanish, and that vanishing suffices. This verifies the final block statement with all signs and multiplicities intact.

The VWR formulas checked here are mathematically valid with the two terminology corrections in VWC4–VWC5. Their conclusion is the faithful receiving comparison and its original residue form; no vanishing of \(K_{\rm off}\), numerical purity of the full source, or RH conclusion is asserted.

## VWC6. The global complex comes from the original coefficient sheaf

There is an exact stronger sheaf construction than the intermediate constant-diagram map. On the established three-point space \(Y=\{c_+,c_-,\eta\}\), set
\[
\mathcal F_{\sigma,\delta}
=\bigl(W_+\xrightarrow{\iota_{\sigma,\delta}r_+}
   \mathcal H_{\sigma,\delta}
   \xleftarrow{\iota_{\sigma,\delta}r_-}W_-\bigr),
\]
where \(\iota_{\sigma,\delta}:A\hookrightarrow\mathcal H_{\sigma,\delta}\) is VWR2's constructed inclusion. The sheaf on each minimal open \(U_\pm=\{c_\pm,\eta\}\) has its indicated closed-stalk value; the intersection has value \(\mathcal H_{\sigma,\delta}\); and the value on \(Y\) is the equal-restriction subspace. This proves the sheaf condition directly.

The original full sheaf maps to this one by identities at \(c_\pm\) and \(\iota_{\sigma,\delta}\) at \(\eta\). Both restriction squares commute. Each minimal open has exact section functor because it is stalk evaluation, so the two-open ordered Čech complex computes sheaf cohomology. It is precisely
\[
[W_+\oplus W_-\xrightarrow{\iota_{\sigma,\delta}(r_+-r_-)}
  \mathcal H_{\sigma,\delta}].
\]
Thus VWR6's strict original-complex comparison is the actual global cohomology map of this sheaf comparison. It is not necessary to replace the original sheaf by a constant diagram. All endpoint and extra closed summands are retained by their identity maps.

The actual source map \(f:X^{\rm dbl}\to Y\) then gives
\(f^{-1}\mathcal F\to f^{-1}\mathcal F_{\sigma,\delta}\).
At every original arithmetic point its amplitude map is \(\iota_{\sigma,\delta}\), and at each \(m_\pm\) it is the full identity on \(W_\pm\). Every arithmetic point is still a distinct source point. The original action maps commute with these restrictions and inclusions, proving the equivariant sheaf map as well. This argument uses algebraic sheaf cohomology of the displayed complex vector sheaves; their specified coefficient topologies give the subsequent closure operation, and are not silently substituted for a different derived category.

The subsequently added closure sheaf sequence VWR6.5–VWR6.6 is exact as well. At both closed stalks the projection is the identity, so its kernel is zero. At the generic stalk its kernel is exactly \(C_{\sigma,\delta}\), giving the sheaf \(j_{\eta!}C_{\sigma,\delta}\). The restrictions on the quotient sheaf are zero because the original restriction images lie in \(J\subset C_{\sigma,\delta}\). Its three-term Čech complexes are consequently exactly the ones displayed in VWR6.5. Lifting a degree-zero \(p\in P\) by the identity and applying the original differential gives the connecting morphism \(p\mapsto dp\), with no further sign. Since the image of \(d\) is \(J\), the image of \(C_{\sigma,\delta}\to\mathcal H_{\sigma,\delta}/J\) is \(C_{\sigma,\delta}/J\). This proves the full long exact row and locates the closure defect in its constructed generic-support sheaf; it does not relabel that support as Deligne's closed support.

## VWC7. Original explicit-formula signs, domain, and identity evaluation

The exact test-variable change in VWR10 is correct:
\[
h(v)=e^{-v/2}b(e^{-v}),\qquad
\int_{\mathbb R}h(v)e^{-(s-1/2)v}\,dv
=\int_0^\infty b(u)u^s\,\frac{du}{u}=F(s).
\]
Indeed \(u=e^{-v}\) reverses both integration endpoints and gives \(dv=-du/u\). At the prime repetitions,
\[
\frac{h(\log n)+h(-\log n)}{\sqrt n}
=n^{-1}b(n^{-1})+b(n).
\]
Thus both summands in the prime term, with \(\Lambda(p^r)=\log p\), have the displayed signs and factors.

The archimedean sign can also be checked directly from the original meromorphic functional-equation multiplier
\(\chi_\zeta(s)=\pi^{s-1/2}\Gamma((1-s)/2)/\Gamma(s/2)\).
The identity
\[
\frac{\zeta'}{\zeta}(s)
=\frac{\chi_\zeta'}{\chi_\zeta}(s)
 -\frac{\zeta'}{\zeta}(1-s)
\]
on the original two contours gives the sign relation
\[
Z(F)-F(1)
=-P_\zeta(b)
 -\frac1{2\pi i}\int_{\Re s=-1}^{\uparrow}
                 F(s)\frac{\chi_\zeta'}{\chi_\zeta}(s)\,ds.
\]
This is the usual contour step of the original explicit formula cited in VWR10; it is not an assertion of an unproved summation prescription. Between \(\Re s=-1\) and \(\Re s=1/2\), the logarithmic multiplier has the single pole at \(s=0\), with residue \(+1\). Therefore moving this last contour adds \(+F(0)\). Moreover
\[
-\frac{\chi_\zeta'}{\chi_\zeta}(s)
=\tfrac12\psi(s/2)+\tfrac12\psi((1-s)/2)-\log\pi.
\]
At \(s=1/2+it\), this gives exactly the two half-digamma terms in VWR10.1, including their arguments and the \(-\log\pi\) term. Consequently the full formula has \(+F(0)+F(1)\), \(+A_\infty(b)\), and \(-P_\zeta(b)\), as stated.

The passage from the cited compact tests to \(A\) is valid in every required topology. For a smooth cutoff \(\chi(\log u/R)\), equal to one on a growing logarithmic interval, the Leibniz rule expresses each Euler derivative of the difference as a finite sum supported on \(|\log u|\geq R\). Its \(p_{N,j}\) seminorm is bounded using \(p_{N+1,k}(b)\), \(k\leq j\), times a constant and an exponentially vanishing factor. Thus the cutoff functions converge in \(A\), and their Mellin transforms converge in every \(\mathcal B\) seminorm. The prime series is bounded by the absolutely summable series
\[
p_{N,0}(b)\sum_{n\geq2}(\log n)(n^{-N}+n^{-N-1}),\qquad N>2.
\]
The Gamma integrand has logarithmic growth and is controlled by decay power two of the Mellin transform. The zero-count estimate \(N(T)=O(T\log(\exp(1)T))\), with multiplicities counted, gives
\(\sum_\rho m_\rho(1+|\Im\rho|)^{-2}<\infty\);
the zeros lie in the fixed strip \(0<\Re\rho<1\). Hence the zero series is controlled by a single fixed-strip seminorm. Endpoint evaluations are continuous as well. All four contributions therefore pass to the limit. Every finite trivial-zero cutoff in VWR10.4 remains a finite identity; no convergence of the unbounded trivial-zero sum is assumed.

It follows that \(\Theta_{\rm off}\) is a continuous functional on \(A\), annihilates the actual \(J\), and descends to the original \(Q\). Its value at the original isolator \(b_{\rho,0}\) is exactly \(m_\rho\) at an off-critical zero, and zero otherwise. Thus its identical vanishing is equivalent to \(K_{\rm off}=0\); its value on an individual class need not detect higher nilpotent coordinates.

Finally the source \(h_*\) in VWR10.8 is even, has support away from zero and integral zero. The support radii are strictly less than \(1/10\). At the positive integers only \(n=1\) meets one of its bumps, and \(h_*(1)=1\). Therefore
\[
b_*(1)=2\sum_{n\geq1}h_*(n)=2,\qquad
b_*=\Sigma h_*\in J,\qquad \Theta_{\rm off}(b_*)=0.
\]
The functional equality \(\Theta_{\rm off}=c\,\operatorname{ev}_1\) on \(A\) forces \(2c=0\), hence \(c=0\), and then \(\Theta_{\rm off}=0\). This checks exactly the claimed scalar identity-evaluation comparison. It does not apply the semilocal Connes–Consani cutoff trace formula itself to this noncompact \(b_*\); the extended object being compared is only the scalar evaluation \(b\mapsto b(1)\), which is already continuous on \(A\).


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
