# Finite native moments, complex resolvents and arithmetic observations

The Split-Zero cohomology programme starts with the theta source whose Mellin transform is `2ξ`, divides out a specified finite zero divisor with its full multiplicities, and measures its polynomial classes in the resulting arithmetic convolution norm. The unresolved estimates concern that particular norm and its quotient by the original theta relations—not a freely chosen metric.

This edition calculates two-sided finite-moment bounds for the integrals entering that norm. For each original parity block and positive resolvent parameter, the complete matrix uncertainty lies on **one explicitly calculated rank-one segment**. Consequently every complex cross-term retains its phase and shares the same real error parameter. A second complete derivation supplies complementary moment bounds, convergence at a fixed pole, an untilted-moment construction, and explicit finite stopping certificates. Both derivations carry their bounds through the unchanged observation fibres, the full conductor map and the four signed determinant endpoints.

## Read the complete mathematics

- [Complete LaTeX with both new proofs](COMPLETE_PROOFS.tex).
- [Rank-one resolvent proof, RR1–16](NATIVE_RESOLVENT_RANK_ONE.tex).
- [Complete native moment, convergence and endpoint proof](NATIVE_RESOLVENT_MOMENT_ENCLOSURES.tex).
- [Diagram with full equations, explanations and citations](FIGURE_CAPTION.md).
- [Machine-readable results and their programme uses](RESULT_INDEX.json).
- [Human-source versions and actual uses](HUMAN_SOURCE_USE.json).

The main human quadrature source is Jörn Zimmerling, Vladimir Druskin and Valeria Simoncini, [arXiv:2407.21505v3](https://arxiv.org/abs/2407.21505v3), §§3–5. The original author LaTeX, both appendices and bibliography were read. The present proofs calculate its receiver for these unbounded arithmetic measures and the actual dependent polynomial block. The parity multiplier preserves the attribution to Aptekarev, López Lagomasino and Martínez-Finkelshtein, [arXiv:1410.1261v1](https://arxiv.org/abs/1410.1261v1); [the complete earlier parity proof](providers/PARITY_POLLACZEK_NATIVE_RECEIVER.tex) and [full conductor continuation](providers/NATIVE_TRUNCATION_CONDUCTOR_RETURN.tex) are included.

The [four original-observation and source-kernel figures](original_source_figures/FIGURE_CAPTIONS.md) explain the preceding results022–024, with complete captions and proof locators. Their eight complete proofs remain in the [preceding source edition](../20260920-original-observation-source-kernel/README.md).

The parallel [marked-observation edition](../20260920-marked-observation-illustrated/README.md), result025, contains its entire cumulative LaTeX, seven figures, the literal original coordinate maps and all inverse branches. It is also included, in full, in the three [cumulative manuscript successors](cumulative), alongside the new moment proofs. [Exact insertion identities](CUMULATIVE_INSERTION.json) show that no preceding proof was deleted. The integrated full Fable principal deliberately repeats its earlier development so its new proofs remain attached to their complete definitions.

## Verification and what remains

The rank-one checker passed36 exact finite checks in normal and optimized Python, including two deliberately wrong alternatives that were rejected. The independent moment checker passed592 exact finite positive-semidefinite checks in normal Python; no optimized run of that assert-based checker is claimed. [The independent mathematical review](INDEPENDENT_RANK_ONE_REVIEW.md) covers RR1–16; [the moment verification record](MOMENT_CHECKS.md) specifies its scope. Atomic test measures check universal identities; they are not substituted for the arithmetic measure.

The actual native moments still need evaluated or certified values. Fixed-pole convergence is not a growing-degree estimate for the signed projected arithmetic current. No RH conclusion is claimed. These are complete source editions, including LaTeX and SVG/PNG figures; no new PDF, Zenodo deposit or Overleaf update is represented by this GitHub edition.
