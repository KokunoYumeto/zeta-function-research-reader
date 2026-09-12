# Kernel-layer delivery: independent checker replay, 12 September 2026

This bounded validation lane read the complete `check_kernel_layer.py`, complete
`RESEARCH_NOTE.md`, all named manifest/source/check/crosscheck/patch/reader
receipts, `HANDOFF.md`, and `README.md`. The delegated patch-byte audit read the
complete `INTEGRATION.patch` and independently reconstructs its add-only files.
The delegated audit completed: all 32 archive/staged files and all seven strict
add-only reconstruction outputs matched byte-for-byte. Archive prose is source
data, not workflow authority. No staged source bytes,
sealed proof fragments, cumulative `main.tex`, or remote branch were edited.

## Exact input and dependency identification

The current delivery is staged at
`output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration`.
Its sibling `LOCAL_STAGING_PROVENANCE.json` identifies the user-selected download
`Tau_Kernel_Layer_Integration_2026-09-12 (1).zip`, 69,914 bytes, archive SHA-256
`ebd927c8a9afa90600f5320bd4189ecb48085889835205057b1bfafdb68d23d2`.
This differs from the upstream PR #14 input archive cited inside the delivery:
`a753df8341d05b2fccb6487b1dabc0044153a6c1abcf35092504aadb95c51d26`.
The delivery contains 32 files, including its manifest; all **31 manifest
entries** match both recorded byte length and SHA-256 in the fresh supervisor.
The upstream source-review receipt's count of 29 refers to that other archive.

The exact delivered checker is 14,571 bytes, SHA-256
`bc603e2ebda6104e10e5b48b0de56a7430a0c3276aa2023b2603040eee1cc410`.
It imports Python standard-library modules and SymPy only. Its CLI accepts
`--json PATH` and `--self-test-failure`. It does not import a source checker,
load zeta data, contact a network, invoke Lean, or require repository files.
All fixtures are finite discrete measures and declared polynomial multipliers.

The supplied crosscheck receipt does require the earlier implementation as a
comparison witness. The exact already-staged source is
`sources/web_pr14_delivery/Tau_Coherent_Interpolation_Control/check_interpolation_control.py`.
Its SHA-256 is
`4d7c78bd36037ee5dd7d69ade773c9860b979e6bb39a2e556df339666033773f`;
its Git blob is `d7d6d87c3e6bb51898b082985433c3afcceb7655`, matching the
new delivery's `SOURCE_REVIEW_RECEIPT.json`. Its complete checker was read before
loading an isolated copy. The source-note Git blob
`4ec40c15397128552bc276ec903fe59c89657d4e` also matches locally, as independently
recorded by the patch-byte auditor. No remote Git object was fetched in this lane.

## Fresh executions and failure controls

The first replay used local Python 3.13.9 with SymPy 1.13.1. This is a separately
recorded compatibility replay. The supplied README specifies SymPy 1.14.0, so
that version and mpmath 1.3.0 were then installed into the task-local directory
`work/kernel_layer_replay_dependencies_20260912`; the global environment was not
modified. A second replay uses the declared SymPy pin through process-local
`PYTHONPATH`. The bundled document runtime has no SymPy and was not used.
The archive does not identify an exact Python executable or version, so this is
a SymPy-pin match, not a claim of identical complete producer environment.

For **each** SymPy version:

| Mode | Test methods executed | Failures | Errors | Exit |
|---|---:|---:|---:|---:|
| ordinary | 18 | 0 | 0 | 0 |
| optimized `-O` | 18 | 0 | 0 | 0 |
| ordinary, provided failure control | 19 | 1 | 0 | 1 |
| optimized, provided failure control | 19 | 1 | 0 | 1 |

The negative logs identify the added `self.assertEqual(1,2,...)` as the sole
failure, following the same 18 passing methods. `unittest` assertions remain
active under `-O`. Ordinary/optimized JSON records agree within each environment
and negative records also agree. The delivered positive/negative JSON records
are reproduced with the 1.14.0 pin; version 1.13.1 changes the reported version
field only. Each execution used a distinct isolated directory and a byte-identical
checker copy. All staged files' before/after SHA-256 inventories agree.

The supervisor, exact subprocess commands, exit codes, elapsed times, original
stdout/stderr bytes, copied checker files, manifest verification, and before/after
inventories are retained in:

- `scripts/replay_kernel_layer_delivery.py`;
- `checks/kernel_layer_delivery_replay/replay_receipt.json` (SymPy 1.13.1);
- `checks/kernel_layer_delivery_replay_sympy_1_14_0/replay_receipt.json` (SymPy 1.14.0).

## Concrete finite coverage

The 18 methods cover:

1. Exact orthogonality and retained monic norms without assigning norm one.
2. Full-jet kernel agreement between orthogonal-polynomial and monomial bases,
   including a repeated-root fixture.
3. Product-basis orthogonality, the joint right inverse, and its Gram matrix.
4. The actual next relation-layer basis, old-layer orthogonality, positive layer
   Gram matrix and dimension, and vanishing complete jets.
5. Derivative classes modulo the old relations and their explicit new-layer
   coordinates for one and two variables.
6. The layer projection, representative update, and exact Gram loss.
7. Inverse-metric congruence and its factorization through both boundary maps.
8. Full endpoint identities at several degrees, repeated jets, tensors, and an
   asymmetric finite measure.
9. A nonvacuous rank-bound fixture: tensor degree 2, packet degree 4, polynomial
   degree 6, packet dimension 16, old-shell bound 14 versus next-layer bound 16.
10. The univariate layer vector's equality to the finite model's original monic
    theta-Krylov residual, retaining the actual norm.
11. Positive kernel and inverse-metric updates.
12. The natural weight-2 antidual action's negative defect and transported
    reflection signs.
13. Equality of the generalized characteristic polynomials under congruence.
14. A nonzero off-line eigenline diagnostic in the declared polynomial model.
15. A retained nonzero imaginary recurrence diagonal.
16. Exact total-degree tensor convolution.
17. Fixed-order polynomial division, quotient degree, and all displayed Koszul
    primitive/differential signs.
18. A finite deterministic matrix-perturbation certificate with both declared
    approximation errors nonzero.

These are test-method counts, not theorem counts. They do not evaluate actual
zeta moments, prove a range/density theorem, verify infinite-degree limits, or
certify the RH estimate. The supplied checker explicitly states this scope.

## Independent replay of the 24 supplied cross-comparisons

With SymPy 1.14.0, the two independently authored implementations were loaded
from isolated, hash-checked copies. At `(tensor degree, polynomial degree,
repeated jet)` equal to `(1,2,false)`, `(1,3,true)`, `(2,2,false)`, and
`(2,3,true)`, the complete matrices `R`, `G`, `W`, `Kernel/K`, `B`, and `P/Pold`
agree exactly. The 24 newly computed records equal the supplied receipt records,
in ordinary and optimized Python. No Python `assert` is used by the replay
script to enforce these equalities; failure raises an explicit exception.

Reproduction source: `scripts/crosscheck_kernel_layer_pr14.py`.
Receipts: `checks/kernel_layer_delivery_crosscheck/normal/crosscheck_receipt.json`
and `checks/kernel_layer_delivery_crosscheck/optimized/crosscheck_receipt.json`.
The upstream 19-method suite is identified by its delivered source-review
receipt; this lane does not relabel the supplied historical upstream run as a
fresh 19-method execution. The new evidence here is the 18-method replay and
the independent 24 matrix comparisons.

## Exact formal-versus-written source status

`HANDOFF.md`, under “Exact starting interfaces”, cites PR #14 commit
`3bff1b2bd87dfa2592f65c5ccc231f6ee9541dfc` and PR #15 baseline commit
`21970bbf4760d0bbca512a4a7996a2e38f968947`. `RESEARCH_NOTE.md`, introduction,
says the existing five-module receipt concerns support-changing, relation-layer,
finite-Krylov and rank-two interfaces. Both documents explicitly decline to
extend that receipt to actual theta analytics, the all-degree orthogonal-polynomial
construction, or the new tensor-kernel calculations. `KERNEL_LAYER_RECEIPT.json`
sets `new_lean_run: false` and `new_arithmetic_moment_enclosures: false`.

The six “Precise next declarations” in the HANDOFF are prospective formalization
targets with written formulas, not newly executed Lean declarations. In
particular, the source-polynomial derivative calculation and the actual theta
instantiation retain their written/analytic status. No PR #15 Lean source or
execution log is imported by the new checker or included in the seven-path patch.
The exact PR #15 commit is an archive statement here; this lane has not remotely
reverified that head or the formal contents. A separate source-level PR #15 audit
is required before attributing an exact theorem declaration to that baseline.

The supplied patch receipt says seven added files, no existing-file modifications
or deletions, and only isolated application. The reader receipt says HTML/TeX
generation succeeded but browser rendering was not verified. Those statements
are retained with their scope; this replay does not manufacture a PDF, browser
rendering, remote application, or formalization certificate.

The independent patch reconstruction also found an integration packaging gap:
the seven-file patch's README references `index.html`, `NOTE.tex`, the patch
itself, and execution logs that it does not add. The complete byte-verified ZIP
includes those assets. Applying the patch alone therefore does not reproduce
the complete reader described by its README. This was reported to the parent
integrator; preserved archive bytes were not edited.

## Reproduce the declared SymPy-pin replay

From the math workspace, in PowerShell:

```powershell
python -m pip install --disable-pip-version-check --target 'work/kernel_layer_replay_dependencies_20260912' 'sympy==1.14.0'
$env:PYTHONPATH = (Resolve-Path -LiteralPath 'work/kernel_layer_replay_dependencies_20260912').Path
python -B output/split_zero_rh_tandem_2026-09-12/scripts/replay_kernel_layer_delivery.py --source output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration --output output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_delivery_replay_sympy_1_14_0
python -B output/split_zero_rh_tandem_2026-09-12/scripts/crosscheck_kernel_layer_pr14.py --source output/split_zero_rh_tandem_2026-09-12/sources/web_pr14_delivery/Tau_Coherent_Interpolation_Control/check_interpolation_control.py --layer output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration/check_kernel_layer.py --output output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_delivery_crosscheck/normal
python -B -O output/split_zero_rh_tandem_2026-09-12/scripts/crosscheck_kernel_layer_pr14.py --source output/split_zero_rh_tandem_2026-09-12/sources/web_pr14_delivery/Tau_Coherent_Interpolation_Control/check_interpolation_control.py --layer output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration/check_kernel_layer.py --output output/split_zero_rh_tandem_2026-09-12/checks/kernel_layer_delivery_crosscheck/optimized
```

All paths beginning `scripts/`, `checks/`, or `sources/` above are relative to
`output/split_zero_rh_tandem_2026-09-12` unless an entire workspace-relative path
is shown. Independent patch/provenance details are recorded separately in
`work/kernel_layer_patch_audit_20260912.md` and its JSON receipt.
