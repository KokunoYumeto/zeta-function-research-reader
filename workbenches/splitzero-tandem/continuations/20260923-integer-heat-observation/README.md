# Recovering the original integer heat source from samples

The [seven-page proof](INTEGER_HEAT_OBSERVATION.pdf) and [complete LaTeX](NOTE.tex) calculate a faithful discrete observation of the programme's original Gaussian integer source. Its kernel is kept exactly as `(4πT)^(-1/2) exp(-x²/(4T))`.

Integer samples recover every source coefficient through an explicit Fourier multiplier inverse and a rapidly decaying interpolation kernel. The same map carries the existing supported-zero action, every lower lattice label, the independent graph mass, and heat evolution. Circle periodization instead records the mass in each label and forgets the top integer profile. Half-integer samples remain injective but have a dense, nonclosed range and no uniform inverse bound; a finite alternating source demonstrates the difference.

The original function, amplitudes, source norm, graph factor two, time and circle measures remain in the formulas. These calculations do not assign a positive replacement norm to an old arithmetic kernel, apply a finite-mass construction to the infinite theta comb, or decide RH. They provide the specified source-observation maps for continuing the original-zeta reconstruction.

## Proofs and human provenance

- [IS1–22 and IS7a–b](NOTE.tex): full definitions, inverse, convergence, sharp comparison bounds, arithmetic action, periodization and half-shift proof.
- [Labelled heat and original theta](sources/LABELLED_HEAT_AND_ORIGINAL_THETA.tex), LH1–15, and [supported-zero mass completion](sources/SUPPORTED_ZERO_MASS_COMPLETION.tex), MCB1–19: complete unchanged shared programme inputs. Their previous Gram and mass results are not claimed as new here.
- Gröchenig, Romero and Stöckler, [arXiv:1612.00651v2](https://arxiv.org/abs/1612.00651v2): primary author TeX used for the stable-shift and Gaussian sampling framework. Its attributions to Jia–Micchelli and Ron are recorded as secondary witnesses, not originals inspected here.
- Reinhardt and Walker, [DLMF Chapter 20](https://dlmf.nist.gov/20): theta-series context.
- [Source identities and actual reading coverage](SOURCE_IDENTITY.json); [machine-readable results](RESULT_INDEX.json).

## Reproduction and scope of checks

Run `python check_sampling.py` and `python -O check_sampling.py`: each passes 238 exact finite checks, 18 non-certified numerical checks and two deliberate-error controls. These are tests of the formulas, not substitutes for the analytic proofs. `python draw_sampling.py` regenerates the [figure](sampling.svg); `pdflatex NOTE.tex` twice builds the reader. The independent mathematical derivation agrees with the inverse, its domains, graph factors and shifted-sampling result. [Build checks](BUILD_CHECKS.json) and [render inspection](QA_COMPLETE.json) record the delivered artifact.

This addendum belongs to the larger [Split-Zero and zeta research collection](https://github.com/KokunoYumeto/zeta-function-research-reader), whose other papers, full sources and immutable editions remain retained.
