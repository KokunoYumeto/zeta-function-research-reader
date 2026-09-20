# Exact validation of the native secular receiver

The standalone proof is NATIVE_SECULAR_RECEIVER.tex, equations NS1–NS37.
The original source and result031 remain unchanged.

## Completed checks

- verify_native_secular.py passed in normal Python and optimized Python.
- Each run passed 2,694 scalar equalities, 148 exact inequalities and
  15 negative controls: 2,857 checks in each mode.
- Both explicit --deliberate-error runs exited 1 with the intended
  "ArithmeticError: Identity failed: 1/3 != -1/3". Optimized Python
  does not disable the checks.
- The models use a specified positive measure of mass 3 and exact
  symbolic arithmetic, including nonreal poles, repeated real and
  nonreal poles, zero poles, a fully invisible orthogonal quotient,
  active/invisible overlap, and double invisible roots.
- The direct source-moment compression is compared independently
  with the outgoing-column expression. Original S phases, coordinate
  congruences, full CRT projectors, every local pole order, both
  resolvents, bordered old-root eigenvector systems, spectral
  projections and the rank-two arithmetic defect are checked.
- Exact polynomial jet tests retain every local unit coefficient,
  its inverse, and all tensor jet coefficients, including equal-sum
  collisions. These are structural algebra tests, not invented
  numerical zeta data.
- The final draft-mode LaTeX compile reports 8 pages with no
  unresolved references, overfull boxes, underfull boxes or LaTeX
  warnings. No PDF was created or read; visual inspection is not
  claimed.

The shell command's trailing text search returned exit 1 because it
found no warning patterns; the LaTeX and both checker runs in that
command completed successfully. Earlier test assembly encountered
a SymPy radical-division representation issue in the degree-four
orthogonal model. The checker now performs exact algebraic-field
polynomial division, and uses the degree-three orthogonal quotient
as its fully invisible model. This was not a failed mathematical
identity.

## Exact source pins

- Connes–Consani–Moscovici, original mc2arXiv.tex, arXiv:2511.22755v1:
  cd02adff07e89dcd343cf0dfc06a14d7190cef43e1978e20706028dda92fa71b.
- Frozen result031 NATIVE_PROLATE_LIE_DEFECT.tex:
  7f8fa549c99b725a8641c43419e561e8bf0ac90c5a37e342d797a80651d76a3f.
- Final proof:
  ee8525847499b26553bb7c8a4470a382fa202238208dcf2ce02377601ceade76.
- Checker:
  c08ffad99e9e33a449600b0a91b64a93945763ad90cc156221a57cabfb9c3d01.

The normal and optimized JSON receipts independently record their
current proof and checker hashes. If a later edit changes either,
those receipts must be regenerated; stale human-readable pins
above must not be treated as current.

## Independent mathematical review

The independent_active_factor folder contains a full reduced-factor
proof with all multiplicity cases and exact examples, and a complete
sign/coordinate/CRT/jet audit. The two suggested wording corrections
have been applied: the excluded claim is that every original root
lies on the centre line, not the proved finite strip bound; and the
rank-two control is explicitly G-selfadjoint. The separate original
distance-to-spectrum bound remains, while NS37 sharpens its strip
consequence by a factor two.

## Scope

The result is finite and uses the actual arithmetic quotient and
attained metric. It proves no decay estimate for the canonical
allowance, no limiting spectral convergence, and no assertion that
all original arithmetic roots lie on the centre line. The manuscript
gives the complete exact morphisms instead of substituting a
real-rooted determinant without its comparison.
