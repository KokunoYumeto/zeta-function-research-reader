# Executed verification and scope

## New exact suite

`check_exponential.py` passed **22 named finite test methods** under ordinary Python and under `python -O`. The two successful JSON records are byte-identical. The implementation uses Sympy 1.14.0; the complete environment string and checker hash are in `VALIDATION.json`.

The suite exercises the polynomial direct-sum algorithm, special fibre, t-connection and coefficient-direction commutators, reduced connection flatness, companion polar operator, residue determinant and duality, repeated-root Jacobian trace, source finite-rank deformation, logarithmic Čech differentials at multiple orders, retained constant boundary jets, action hull, ramification factors, curvature current degrees, root-of-unity period matrix, rank-one period differential equation, period/source metric ratios, and original represented-zero/absence cases.

Raw receipts: `checks/normal.json`, `checks/normal.log`, `checks/optimized.json`, `checks/optimized.log`.

Three deliberately false formulas were tested separately in **each** mode. All returned status 1 and were rejected:

1. Reverse the sign of the t-connection.
2. Erase the surviving logarithmic boundary class.
3. Assign degree zero to the saturated determinant while omitting its boundary delta current.

Their individual logs and `checks/negative-controls.json` are retained. These controls test specified false variants, not every possible implementation error.

## Parent replay

The supplied predecessor archive's **41 manifest entries** verified. Its unchanged `check_specialization.py` passed **23 methods** in normal and optimized runs. The two JSON outputs agree byte-for-byte. Raw receipts are `checks/parent-*`; the archive hash and manifest count are in `checks/parent-manifest.json`.

This replay tests those finite identities. It does not turn the predecessor's infinite-dimensional analytic claims into formal certificates.

## Development repairs retained

An early checker comparison used syntactic equality between logarithmic expressions that differ only in symbolic presentation. It was repaired to test their exact simplified difference, and the failed development log remains. No theorem or tested matrix identity was weakened.

The first reader build rejected the legacy TeX font command `\rm` in several formulas. It was replaced by the explicit `\mathrm{...}` typesetting command; equation content was unchanged. The early MathML warning log is retained, and the final build has no math-conversion warnings.

## Written analytic and imported mathematical scope

The period-contour convergence, holomorphic parameter differentiation, determinant propagation, and full-rank comparison have complete written proofs in the note. Finite symbolic tests do not certify those analytic operations.

The exponential-sheaf purity and lissity conclusion is an application of the stated Deligne theorem under the checked degree/characteristic/leading-term hypotheses. It is not re-proved by the finite checker. The source-reading record discloses unresolved transcription cross-references and does not claim a new complete audit of Deligne's proof.

No new Lean source was compiled, no arithmetic interval quadrature certificate was produced, and no uniform estimate proving the desired endpoint nonconcentration was established. No remote branch was changed.

## Reader and integration

The HTML is rebuilt from the full mathematical Markdown using native MathML. Displayed equation labels are restored explicitly and matched against the source. Desktop and mobile rendering results are recorded in `checks/reader-validation.json`; screenshots are visual review evidence, not mathematical certificates.

The add-only integration patch targets `workbenches/tau-deligne-exponential-comparison/`. It is checked in an isolated local Git repository and its applied files are matched byte-for-byte. Its receipt is `checks/integration.json`. The delivery does not include the literature source corpus or font files.
