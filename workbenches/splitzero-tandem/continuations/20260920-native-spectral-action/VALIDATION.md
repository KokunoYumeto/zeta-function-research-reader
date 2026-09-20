# What was checked

The publisher read all four complete proofs and all four executable checkers. Fresh local replays passed in normal and optimized Python with byte-identical results between modes:

| Checker | Exact checks | Deliberately wrong formulas rejected |
|---|---:|---:|
| Main spectral action | 600 | 4 |
| Independent original-metric action | 213 | 20 |
| Independent quartic term | 10 | 2 |
| Independent repeated-root endpoint and coordinate phases | 239 | 6 |
| Total per mode | 1,062 | 32 |

The checkers use explicit exceptions, not optimization-disabled assertions. They test finite exact algebra using SymPy 1.13.1, including complex nonidentity metrics, repeated eigenvalues, nilpotent endpoint blocks, full determinants, both signs and phases, complete multiplicities, and retained mixed terms. Their finite examples do not certify actual arithmetic moment values, an asymptotic estimate, or RH.

The exact two-panel scientific figure was rendered from the included generator and inspected. Its fixed metric, complete characteristic polynomial, labels, double-root point and sharp-bound point were checked against SA38–43. It is explicitly a comparison-measure example, not arithmetic zero sampling.

The source merger includes every proof body and bibliography. It namespaces local macros, equation labels and citation keys without deleting any mathematical text. One long repeated-node expression after SA10 is moved from inline to display math, with every symbol retained; the standalone source remains unchanged. Each of the three cumulative manuscripts retains its previous bytes exactly around one reversible complete insertion. The insertion record proves recovery of the preceding source. A fresh compilation of these large cumulative manuscripts is not claimed.

The final combined source passed two draft-mode compilation passes after the display adjustment: 23 pages, all references and citation keys resolved, no overfull or underfull boxes. The compilation record is retained separately by the publisher. Draft-mode compilation checks syntax, references and citations; it is not a PDF visual inspection. No PDF is read or generated for this source edition. Original human-source archives remain unchanged and are not copied into this public derivative.
