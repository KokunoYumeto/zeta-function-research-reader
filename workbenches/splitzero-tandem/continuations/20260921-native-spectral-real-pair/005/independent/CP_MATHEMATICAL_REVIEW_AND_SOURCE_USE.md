# Continuous cubic pole positivity: proof and source receipt

The completed proof is CONTINUOUS_POLE_CUBIC_POSITIVITY.tex, CP1–29.
Proof SHA-256: CBBD6160FCF8E300D3E03E30B43474271AAD7F1824B831DCC356893AB5535EFB.

The full reflected Weil matrix satisfies T3(2+iτ) ≥ μ_* I for every real |τ| ≤ 2,970,000,000,000. Here

\[
\mu_*=\frac{135\cdot1200^6}{52\cdot2560009^7}
-\frac{23296}{243\cdot10^{28}}>4\cdot10^{-28}.
\]

The exact rational certificate also verifies μ_* > 10^-27. This is a continuous interval result, not interpolation between the five previously certified sample poles.

## Actual inputs and reading coverage

The existing provider SOURCE_ROUTING.json and SOURCE_READING_LEDGER.json were read before routing to primary sources. Index hits were used as paths, not mathematical evidence.

- Dave Platt and Tim Trudgian, The Riemann hypothesis is true up to 3·10^12, arXiv:2004.09765v1, original author TeX. Canonical source ID PUBUNIT-8FD792C15B5C6472FBDED93E. Read the original first 150 lines, including Theorem 1 (label bank), its exact height, introduction and computational-method discussion. This turn does not claim a fresh complete-paper reading. Source SHA-256 c6c29099c943dd2c74ee1b9dc6efc373d3102269bf41b14494687ced8225a75c. Used only to place all zeros through T0=3·10^12 on the critical line.
- Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, Counting zeros of the Riemann zeta function, arXiv:2107.06506v1, original author TeX. Read lines 1–329: original title/authors, introduction, exact positive-height counting convention, Theorem 1.1 and Corollary 1.2 (labels main-thm and main-bound-1), surrounding qualifications, and beginning of the following section. Source SHA-256 3faa3cb45ee34b5fcd96f84ed036de2af1c3dcea75723776410e2ac359ff5021. Used the original unconditional corollary exactly, both for short-interval zero existence and the entire high-zero tail.
- The whole provider WEIL_POSITIVITY_AND_ARITHMETIC_CERTIFICATES.tex was read. Its finite pole computations motivated the extension; no fresh Arb values, finite zero lists, or empirical interpolation were used in CP.
- Original WCF2/WCF5–6 and FC21–32, FC56a, SE1–17, RW1–20 were used for the actual source quotient, moments, rational coefficient receiver and separate source/target Gamma norms. WCF6 was read directly for the upper-diagonal index and the inverse weights in CP29.

The exact human theorems are cited inputs, not claims reproved by the short algebra certificate. Their original source archives remain intact in the provider's source store. No PDF reading was used.

## Independent mathematical check

A separate mathematical derivation agent read CP1–18 and independently checked:

- CP5's short-interval count, including its signs and endpoints.
- The four intervals and negative-height conjugation throughout the closed pole range.
- The original h=3 chord factor and inverse-column coefficient bound 1,3,3,1.
- The distinct denominator products 15,3,3,15 and the factor 208/45.
- Every factor two and multiplicity in the reflected tail, including the strict tail cutoff and the negative Stieltjes boundary term.
- The derivative bound 54621/15625 < 4.
- The exact positive integer difference in CP13 and both final rational margins.

Its conclusion was acceptance without a substantive error. This check did not claim additional literature reading.

The original-conductor return CP19–29 was then completed directly. It keeps Bτ=Rτ^-1 Cκ Ψ, all coefficients of Rτ and its inverse, the complete native Gamma measure and the explicit g0(τ) polynomial. The source constant J_A retains every finite inverse coefficient and every original positive weight. The full eight-state form now has exactly its original four-dimensional evaluation-graph kernel; there is no extra arithmetic kernel anywhere in the proved pole interval.

## Executed exact certificate

verify_continuous_pole_cubic_positivity.py passed. Its captured output and CONTINUOUS_POLE_CUBIC_POSITIVITY_CERTIFICATE.json contain exact rational constants and the script hash. It checks the endpoint arithmetic, all rational bounds, exponential finite-sum lower bound, chord identity, original native moments and all four inverse-convolution coefficients. The JSON explicitly identifies the imported human theorems as inputs rather than numerical certificates generated here.

No claim about higher rational degrees, poles outside the proved interval, or global RH is made by this bounded result.
