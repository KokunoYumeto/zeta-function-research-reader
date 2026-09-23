# Original zeta, the theta source, and the prime-boundary receiver

This correction is part of the Split-Zero cohomology and zeta-function research programme. It reconstructs the precise passage from the original Riemann zeta function to the programme's theta source, and repairs a receiver that otherwise loses two algebraic boundary classes for every rational prime. The full proofs are in [the reader](ORIGINAL_ZETA_RETURN.pdf) and [its LaTeX source](NOTE.tex).

The original zeta function remains explicit. Its Gamma, endpoint and powers-of-pi factors are retained, not treated as permission to replace the original function or its metric. This paper does not prove or disprove RH and does not claim that every earlier estimate has been reconstructed.

## What is calculated and why it matters

| Proof locator | Exact calculation | Use in the programme |
| --- | --- | --- |
| FR1–FR5 | The integer-dilation operator has Mellin multiplier zeta itself; its actual image has a Möbius inverse. Poisson summation retains both endpoint terms. | Specifies an original-zeta source before choosing a Gaussian. |
| FR6–FR14 | The Gaussian, its two moments, the operator D(D−1), and the full inverse by two tail integrals. | Restores the source and endpoint data behind the actual theta seed. |
| FR15–FR25 | The rational-scaling quotient splits into its moment-zero function and two classes per prime. The augmented receiver has an explicit inverse. | Identifies precisely what ordinary theta periodization does not see. The original seminorm still vanishes on the restored prime-boundary component. |
| FR26–FR31 | The full multiplier, its divisor, the valuation-shifted local-jet isomorphisms and the contour correction. | Restores the pole at 1 and all negative-even zeros without discarding their local coefficients. |
| FR32–FR38 | The returned original-zeta heat family, every drift and potential term, exceptional values, and the actual packet metric. | Prevents free heat dynamics or unweighted estimates from being transferred to zeta without their full comparison. |

The commuting diagram in the reader shows the precise projection that loses the boundary classes. Its reproducible source is inside NOTE.tex.

## Human sources and retained programme inputs

The calculation uses Ralf Meyer's [Zeta operator](https://arxiv.org/abs/math/0412277v3), Alain Connes's [adelic periodization](https://arxiv.org/abs/math/9811068v1), and Alain Connes and Caterina Consani's [trace and real Laplacian construction](https://arxiv.org/abs/2207.10419v1). Apostol's [zeta formulas](https://dlmf.nist.gov/25.4) and Askey and Roy's [Gamma formulas](https://dlmf.nist.gov/5.2) are cited through the named DLMF chapters. The paper gives source-specific locators and preserves the factor of two between the two periodization conventions.

[SOURCE_READING.json](SOURCE_READING.json) and [ADDITIONAL_SOURCE_READING.json](ADDITIONAL_SOURCE_READING.json) record exactly which primary-source passages were read, source versions and hashes. The three indexed TeX files were checked byte-for-byte against the corresponding official arXiv source downloads. This is bounded reading, not a claim to have inspected entire papers.

The unchanged [absolute-base source](sources/09_absolute_base_maps.tex) and [prime-boundary source](sources/21_prime_memory_and_actual_theta_receiver.tex) are retained as chapter sources, not standalone compilable papers. Their human citations remain intact. The current note supplies a complete proof of the algebra it uses. The latter source's PM9 wording should refer to the cofinal system of finite-prime-generated subgroups; the proof here does not use PM9.

## Checks and mathematical scope

[check_return.py](check_return.py) checks 327 exact identities and finite cases, including valuation-shifted jets, Möbius inversion and the full derivative product rule. The normal and optimized runs both pass; two deliberately erroneous alternatives are detected. Four theta/Mellin evaluations are numerical probes, not interval certificates. These tests supplement the written proofs rather than replacing them.

[RESULT_INDEX.json](RESULT_INDEX.json) maps the results to their proof locators and receiving calculations. [BUILD_CHECKS.json](BUILD_CHECKS.json) records the PDF compilation. [QA_COMPLETE.json](QA_COMPLETE.json) ties the inspected rendering to its exact PDF and TeX hashes.

The restored prime classes are not automatically visible to the old Hilbert seminorm. No new norm on them is chosen here. No additional full-lattice semiring or cochain isomorphism is claimed beyond the explicit recorded carrier map. Earlier determinant asymptotics, regularized traces and heat-contact estimates remain separate calculations; this correction does not certify them by renaming their functions.

## Rebuild

Run `python -B check_return.py` and `python -B -O check_return.py` for the local checks. Compile NOTE.tex twice with pdfLaTeX and job name ORIGINAL_ZETA_RETURN. The TeX contains the figure and complete bibliography. Protected human source archives and private working correspondence are not part of this public package.
