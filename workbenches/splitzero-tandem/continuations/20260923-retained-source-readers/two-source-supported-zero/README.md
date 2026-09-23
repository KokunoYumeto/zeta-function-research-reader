# Supported zero on an evaluated arithmetic source plane

This 16-page paper calculates the reflected Weil form on two specified original-theta sources and carries that form into the original even-source prime boundary. It then calculates the supported-zero action, its square-zero metric defect, the unique time at which that defect vanishes, and the resulting local cohomology and its full arithmetic support.

Read `NOTE.pdf`; its complete source is `NOTE.tex`, `TWO_SOURCE_SUPPORTED_ZERO.tex`, and the unchanged preceding `ACTUAL_ENDPOINT_PAIRING.tex`. The appendix contains the entire scalar source, contour, residual and infinite-tail proof. TS1–34, TS25a, TS28a and TS32a are proved in full. No RH conclusion or whole-space positivity is claimed.

The current results are SZ-20260923-149,150,151 in `RESULT_INDEX.json`. The theta time t=1/32 and coefficient heat time T remain separate. In particular the spectrum map sends the local cohomology point to the supported-zero prime, while restriction of its module has support V(e), retaining every ordinary integer prime.

`certify_pair.py` reproduces the100-bit original-source interval calculation in `PAIR_CERTIFICATE.json`; it uses Python, python-flint and SymPy. `certify_pairing.py` and `CERTIFICATE.json` preserve the scalar predecessor. These computations use the complete prime/Gamma receiver with every residual bound, without a zero list or an RH assumption. The independent complete derivations are PP1–63, LS1–37 and TB1–50 in the three accompanying Markdown files.

`draw_geometry.py` reproduces the two PDF/PNG diagrams using Matplotlib. Compile the paper with LuaLaTeX on `NOTE.tex`. All included sources and figures are present; no downloaded author archive is needed for this build.

Human sources are Brad Rodgers and Terence Tao, [arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), phidef/htdef/hoz/sas; Alain Connes, [arXiv:math/9811068v1](https://arxiv.org/abs/math/9811068v1), SectionIII and AppendixII; and Fredrik Johansson with the FLINT contributors, [rigorous integration documentation](https://raw.githubusercontent.com/flintlib/flint/master/doc/source/acb_calc.rst). Bounded original-TeX reading, exact versions and programme foundations are identified in `SOURCE_READING.json` and the proof's clickable citations. Original-author archives are linked at their hosts rather than redistributed here.

The preceding scalar proof is public at [AP1–28](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/acd7016b8232a56f31ae3e69fb800571e8789080/workbenches/splitzero-tandem/continuations/20260923-retained-source-readers/arithmetic-pairing/ACTUAL_ENDPOINT_PAIRING.tex). Its separate published edition remains unchanged.
