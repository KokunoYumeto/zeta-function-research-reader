# Independent review of the source-image closure in every positive receiver

25 September 2026. Complete mathematical review of `SOURCE_MEASURE_CLOSURE_AND_ORIGINAL_QUOTIENT.md`, SMC0–SMC10. Accepted final version SHA256: `29ef32bf1c52ec8f754fb00d33f112b9d7bfce7d77b2e3e997cd0be040455702`.

The complete source text was read at the initial hash `a759b99c54c30f934ca57cc40ebc004b189e0f663a04b6bab8f90abfac770753`. One typographical correction was identified in SMC4.4: its first branch then read `a_0,1_{\{\gamma\}}`. The accepted final version was checked and now displays the mathematically required product \(a_0\,1_{\{\gamma\}}\). Its surrounding sentence and every subsequent norm computation already used that product. No mathematical correction to a theorem or proof was found, and no requested correction remains open.

## SMCR1. Scope and exact prior inputs

SPF0–SPF11 was independently derived in `SOURCE_POSITIVE_MEASURES_AND_DESCENT.md`, SHA256 `5f912f03e64e2deed940cbe9efe08d3b040855bc63c9ffe5320dd1c4f361d8a8`. It classifies all continuous positive transfer forms on the actual prequotient source. SMC's density argument is independent of SPF's cyclic representation, as claimed: SMC1 directly proves totality of the original Gaussian orbit for any permitted measure.

The original density proof was also read directly in `PRIME_MONODROMY_STACKED_HISTORY.md`, M9.1–M9.6, including its full Gaussian multiplier, Fourier sign and \(1/(2\pi)\) Plancherel constant. The older theorem is exactly density of \(\mathcal E(S_0^{\rm even})\) in \(L^2(du/u)\). This review's use of that historical source concerns these analytic formulas and their density proof, not any superseded supporting-algebra assignment elsewhere in that historical file.

The identities \(\Theta J=\mathcal I\) and the original Fréchet quotient are retained established SSI inputs. The AST identification \(R=Q/N_O\) and its strict strong-dual row are also prior inputs explicitly identified by SMC. This review checks the full receiving calculations, not a new proof of every ancestor source theorem or geometric identification.

## SMCR2. Arbitrary-measure density and ideal closure

SMC1's Gaussian orbit has source representatives in \(\mathcal B\), with exact values \(e^{it\lambda}e^{-\lambda^2}\). Orthogonality gives a finite complex measure \(h e^{-\lambda^2}\mu\): its finite variation follows from Cauchy–Schwarz and the polynomial interval bound. The Fourier uniqueness proof is complete on precisely this finite-measure domain. Gaussian convolution followed by continuous compactly supported tests gives zero measure, and its strictly positive density gives \(h=0\) almost everywhere. Thus the entire source image is dense even when the measure has a continuous part.

In SMC2 the full multiplier belongs to \(\mathcal B\), so its critical-line restriction is bounded. It has exactly the actual line-zero set as its zero set there. Therefore the bounded multiplier applied to the dense source image has dense image in the closure of its full operator range. The functions \(h_k\) and \(v_k\) in SMC3.2 are well-defined measurable Hilbert vectors, with \(\|v_k\|\le k\|h\|\), and prove that this range closure is all functions supported off \(\Gamma\). The reverse containment follows because every original ideal vector vanishes at every point of \(\Gamma\). This proves the complete equality
\[
\overline{j_\mu\mathcal I}=L^2(\mathbb R\setminus\Gamma,\mu)
\]
without asserting \(F_0\mathcal B=\mathcal I\) or a uniformly bounded reciprocal multiplier. The orthogonal quotient and its inverse are exactly restriction and extension by zero.

## SMCR3. Quotient infimum and full original jets

The infimum in SMC4.1 is the distance to the actual source image of \(\mathcal I\). Taking its closure does not change this distance; orthogonal projection then gives exactly the stated integral over \(\Gamma\). This does not claim a minimizing element exists inside the original ideal.

The restricted measure on the closed discrete set is atomic, and each atom's mass is \(w_\rho=m_\rho c_\rho\). The exact kernel is therefore the source classes whose values vanish at every positive-mass line atom. All higher jets and all off-line blocks remain in that kernel. After the indicated product correction, SMC4.4 is the exact full-block map. Its indicator has squared norm \(m_\rho c_\rho\), including zero-mass atoms. The direct-descent criterion and the projected-quotient construction are correctly distinct.

## SMCR4. Involution and change of positive measure

The linear source involution \(F(s)\mapsto F(1-s)\) becomes \(h(\lambda)\mapsto h(-\lambda)\) from \(L^2(\mu)\) to \(L^2(\mu^-)\), with \(\mu^-\) the actual reflected measure. The change-of-variables calculation proves the stated isometry and inverse. Since \(-\Gamma=\Gamma\), the quotient restriction commutes with it. Equality of the original forms forces equality of the two finite Gaussian-weighted Fourier measures and hence \(\mu=\mu^-\). Thus invariance is not presumed for a nonsymmetric measure.

The comparison criterion in SMC6 is exact. Domination \(\nu\le C\mu\) gives a bounded same-function map of norm at most \(\sqrt C\). For necessity, density in \(L^2(\mu+\nu)\) supplies simultaneous convergence in both norms, allowing the inequality to be tested on every bounded-set indicator. Exhaustion then gives domination on all Borel sets. This avoids the incorrect inference of a measure inequality from density in only one of the two spaces. The least domination constant is the squared norm; the claim includes zero measures with the corresponding zero-space interpretation. The projection and reflected-divisor receiving maps have the stated domains.

## SMCR5. Full Mellin constants and attribution of the earlier density theorem

For \(a_{\log}(x)=e^{x/2}a(e^x)\), the substitution \(u=e^x\) gives
\(\|a_{\log}\|^2=\int_0^\infty|a(u)|^2du\). The exact transform is one half of the positive-sign Fourier integral, whose Plancherel constant is \(2\pi\). Therefore its squared norm is \((\pi/2)\int|a|^2du\), and the precise receiver measure is \((2/\pi)d\lambda\). The constants in SMC7.1–SMC7.2 are correct.

The comparison \(\mathcal T k=2u^{-1/2}k\) has squared norm factor four, obeys \(\Sigma=\mathcal T\mathcal E\), and satisfies \(\Theta\mathcal T=\mathcal M\) with the exact earlier centered Mellin convention. Thus SMC7.4 is correctly attributed to the earlier M9 density proof and transported with all its factors. The new arbitrary-measure theorem independently specializes to it because \(\Gamma\) is Lebesgue-null. Atomic descended measures cannot be dominated by this ambient Lebesgue measure unless every atom is zero, which proves the asserted absence of a nonzero ambient-norm-bounded descended form.

## SMCR6. Simultaneous receiver and the actual specialization seminorm

The Lebesgue and line-atomic measures are mutually singular. Restriction to their two disjoint measurable supports gives the displayed direct-sum isometry, and the joining inverse is well defined modulo the respective null sets. The direct Gaussian-density proof applies to their sum measure, so it proves density of simultaneous source observations in the whole direct sum, not just each coordinate separately. SMC3 then gives exactly the continuous summand as the ideal closure. The source norm in SMC8.3 retains both observations and their exact constants.

For the actual AST kernel \(N_O\), all finite line-value isolators lie in \(N_O\). They are dense in every weighted atomic receiver that results from SMC4. Their inherited seminorm completion is therefore the same as the completion of \(Q\), with kernel \(N_O\cap N_\mu\). Taking distance to \(N_O\) gives zero seminorm on the original quotient \(R\). This is an inherited completion statement; SMC correctly makes no assertion that every form intrinsic to \(N_O\) extends to \(Q\), or that the original Fréchet obstruction quotient itself is zero.

## SMCR7. Original factors and arithmetic complement

The exceptional values in SMC2.3 agree with the complete original multiplier: the values at zero and one are \(1/8\); the values at negative one and two are \(\pi/24\); the negative-even coefficient retains the original trivial-zero derivative and the Gamma residue. The full local germ and the four-factor Leibniz expression retain every unit derivative. These comparisons preserve the original zeta rather than replacing it by a changed divisor.

The original Weil pairing in SMC9 retains the whole off-line reflected contribution \(W_O\), every multiplicity, both endpoints, the Gamma logarithmic derivative and \(-\log\pi\), all prime-power coefficients, and the finite original trivial-divisor terms with their signs. The positive receiver constructed from the measure gives \(W_L\), and the file explicitly keeps \(W_O\) as their difference. It makes no claim that the original AST boundary vanishes, that RH follows from the selected positive measure, or that all original jets survive the positive completion.

The review therefore accepts the final stated mathematical receiving arguments, including the verified notation repair in SMC4.4. No rendering, packaging, publication or new whole-human-paper reading is represented by this review.
