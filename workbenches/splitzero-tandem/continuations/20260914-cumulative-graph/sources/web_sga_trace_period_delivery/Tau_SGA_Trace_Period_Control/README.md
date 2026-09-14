# SGA trace and the arithmetic period determinant

Open `index.html` for the full offline MathML reader. `NOTE.tex` is the matching LaTeX source, generated from `RESEARCH_NOTE.md`. The delivery contains complete written proofs and finite exact checks, not a proof of RH.

The continuation reads the user's inline SGA 5 Exposé III and applies its residue/trace construction to the existing cyclic theta packet. It calculates the whole diagonal resolution and the exact determinant of the prior exponential period family. Coefficient derivatives recover the full cyclic characteristic polynomial. An invariant constituent's period minor detects the original aggregate real-part defect, while the original theta metric and its remaining volume estimate are retained explicitly.

- `SOURCE_REVIEW.md`: exact source scope, missing master dependencies, external research status.
- `HANDOFF.md`: bounded finite formalization targets using existing infrastructure.
- `PROGRAMME_STATE.md`: completed changes and unchanged quantitative target.
- `CHECKS.md` and `checks/`: actual execution evidence and its scope.
- `INTEGRATION.patch`: add-only patch beneath `workbenches/tau-sga-trace-period-control/`.

To reproduce finite checks:

```sh
python check_trace_period.py --json checks/exact-normal.json
python -O check_trace_period.py --json checks/exact-optimized.json
# Each command below must exit nonzero:
python check_trace_period.py --negative jacobian
python check_trace_period.py --negative quantum
python check_trace_period.py --negative newton
```

`period_numerics.py` needs mpmath; it performs independent, non-interval contour calibrations. `build_reader.py` needs pandoc and BeautifulSoup, and emits offline MathML plus LaTeX. The upload's external SGA component tree is not part of this package.
