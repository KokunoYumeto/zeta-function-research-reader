# Gaussian traces in the original arithmetic quotient

The Split-Zero programme starts with the theta function whose Mellin transform is (2\xi), divides out a fixed finite zero packet with its complete multiplicities, and studies polynomial representatives of the resulting arithmetic classes. Those representatives carry the norm of the actual arithmetic convolution measure. This edition calculates a Gaussian trace in that original metric, rather than replacing it with a convenient reference metric.

The calculation first transfers a full relation-polynomial ensemble from the Gamma reference measure to the arithmetic measure. It proves the limiting spectrum of the least-norm quotient compression and then carries that spectrum through the original observation map. The comparison retains the full root polynomial, both source and relation masses, and the finite rank-one coupling. The independent endpoint proof calculates the density and its second moment with explicit interval bounds.

For multiplicity (m_0=1), the proved five-orbit observation domain (|u|\ge R_*), and the four original cutoffs (q-1,q,2q-1,2q) with signs (+,+,-,-), the signed Gaussian-trace limit at (t=1/1024) is strictly below (-657061/960000). This is a sign of that particular signed combination. It is not a sign assigned to each positive trace, to the complete Weil form, or to the unresolved logarithmic terms. There is no effective finite-(k) threshold or RH conclusion in this edition. The full arithmetic compression law has the broader multiplicity domain stated in NG1–20.

## Complete proofs and reproducible checks

- [Complete integrated LaTeX](COMPLETE_PROOFS.tex), with both full proofs and the inspected illustration.
- [Arithmetic transfer, NG1–27](NATIVE_GAUSSIAN_TRANSFER.tex) and [independent density, moment and sign proof, GM1–25](GAUSSIAN_EQUILIBRIUM_MOMENTS.tex).
- [Results, exact domains and uses](RESULT_INDEX.json), [effects on earlier calculations](BACKWARD_RECEIVERS.md), and [human-source citations and reading coverage](SOURCE_USE_LEDGER.json).
- [Independent mathematical derivation](NATIVE_TRANSFER_INDEPENDENT_DERIVATION.md), [verification details](VALIDATION.md), and [root replay](checks/ROOT_REPLAY.json).
- [Illustration](GAUSSIAN_NATIVE_MECHANISM.png), [exact caption](FIGURE_CAPTION.md), and [reproducible figure source](make_gaussian_figure.py).
- [Three complete cumulative successors and exact insertion records](CUMULATIVE_INSERTION.json). Each contains both complete new proofs and preserves every preceding source byte outside the explicit insertion.

The human inputs are credited at their points of use: Koornwinder and collaborators for the orthogonal-polynomial formulas, Forrester's treatment of Andréief's integral identity, Carlson for elliptic-integral conventions, and Johansson for Arb interval arithmetic. The original 1886 Andréief paper is cited through Forrester, not represented as independently read. Programme manuscripts identify the earlier arithmetic constructions; they are not substituted for human scholarly sources.

This is a complete source edition. No new PDF, Zenodo deposit, Overleaf update or timer change is claimed.
