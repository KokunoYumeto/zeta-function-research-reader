# Terminal endpoint checker closure

The existing **74 direct jobs and 34 mode comparisons remain unchanged**. The terminal window checker, arithmetic checker, balanced checker and corrected PR24 checker have the exact hashes already pinned by that plan. The new window wrapper runs the same four direct jobs sequentially. No checker, wrapper, build, remote operation or source mutation was performed by this audit.

The local readback receipt identifies commit `952ef9fee1e1419b6858d920354de8fa99430b7d` and the source plan uses corrected PR24 predecessor `5e67416c467166cb8729f47cea941c22a9f5f33c`. This audit read those local receipts and their explicitly named files; it did not perform a new remote fetch.

## Exact checker mapping

| Existing checker location | SHA-256 | Jobs | Terminal relationship |
| --- | --- | ---: | --- |
| `sources/local_endpoint_continuations/gamma_endpoint_window_bridge_fixture_20260913.py` | `56be6cbd66ffd5272440e95f01104a0154bf0c4b5a2bab1d0a60cb7945071048` | 14 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |
| `sources/local_endpoint_continuations/gamma_endpoint_window_bridge_supplement_20260913.py` | `f96250bf8f00975dd782de79d2f03e05fdee8df997982b304635a250e721599e` | 10 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |
| `sources/local_endpoint_continuations/gamma_endpoint_window_bridge_projection_review_calibration_20260913.py` | `d2540cfc1ffb2eda9eb18966a8478090da5c564b0b7d78a11a0de130a0cce435` | 1 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |
| `sources/local_endpoint_continuations/gamma_endpoint_window_bridge_projection_review_final_numeric_20260913.py` | `f190440ad83e94aa9f590c63cf508e6149ff1b126ccb4ce9713939f024974943` | 1 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |
| `sources/web_arithmetic_endpoint_delivery/Tau_Arithmetic_Endpoint_Bounds/check_endpoint_bounds.py` | `dcf57f151fd34865907bfa80f8fc063e5d46dbf69201ebee7e0a9b19b26fd2b7` | 4 | terminal published same bytes; original arithmetic dispatch and receipts match existing four jobs |
| `sources/owner_endpoint_review/review_pr24/files/workbenches/tau-confluent-transfer/check_transfer_core.py` | `fcaef2ee4c972cb71255ed3365930b3a558edc2b66dce5567301b38aff7ed4aa` | 4 | historical original core preserved; final correction uses separate prior proposed bytes |
| `sources/owner_endpoint_review/review_pr24/proposed/check_transfer_core.py` | `0016d317a0300423a2bc14d12249214a57d677a05a177c3b3fe4f83f59488046` | 4 | terminal corrected core equals prior proposed bytes; original historical core preserved separately |
| `sources/owner_endpoint_review/review_pr24/check_interfaces.py` | `9189d4d390691abd7a3d954c7ef5830fbb6f0da18791f4562a2b000715f0b11b` | 2 | historical interface remains bound to original core; preserve exact relative import |
| `sources/owner_endpoint_review/arithmetic_endpoint_review/check_balanced_window.py` | `bdab1875a749ce5d5bdb0b1a4790cbeeab7d085dfafa65161c79582426588f69` | 4 | terminal published same bytes; same-directory and source_stage fallback select identical imported source |
| `sources/owner_endpoint_review/window_product_review/verify_window_product.py` | `7c9b0d3a241c14a2ed08efbab1e06c89b7d48fc6d67118299d32a364819bf395` | 4 | terminal published same bytes; new wrapper covers the same existing four jobs |
| `sources/local_endpoint_continuations/endpoint_product_check_20260913.py` | `3fa6384c6b97d56426af84b15e7e5650a4ec69cde542eef73baee5d34f2a2e82` | 14 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |
| `sources/local_endpoint_continuations/endpoint_product_independent_checker_20260913.py` | `c42eabd7dd1dd1ba4e865e4aceadd07b8584e288756b7a70381f083287761956` | 12 | outside owner arithmetic/PR24 terminal publication; carried from pinned previous EW/EP preparation without a new checker read or replay |

## Full wrapper and source read

`run_verification_modes.py` is 2,329 bytes, SHA-256 `b6c0d7f5e54642c4ea0068f0307dac4d95b59215e504f4caceb4a83415c9a8b6`. The complete 2,329-byte wrapper and complete 16,488-byte `verify_window_product.py` were read. The wrapper runs normal, optimized, negative normal and negative optimized modes, using the same interpreter and a 60-second subprocess timeout for each. It writes eight raw streams, two named positive receipts, the current portable receipt and its terminal receipt. Its success criterion requires zero positive exits, nonzero negative exits with the expected Gaussian failure text, and identical complete positive check arrays.

All 15 selected publication source/evidence files were rehashed against both SOURCE_PLAN and FULL_BYTES_READBACK. All eight raw terminal stream hashes match the terminal receipt. Raw streams are intentionally absent from the owner public whitelist; the negative tracebacks contain machine-dependent paths. The full wrapper is portable when copied with its checker to a disposable replay directory. Its original output directory must remain untouched by later checks.

## Exact mode counts and controls

| Suite | Each positive normal / optimized mode | Each negative mode |
| --- | --- | --- |
| Window portable | 11,483 exact + 4 display = 11,487 passing records; exit 0 | The same 11,487 records pass, then one intentional Gaussian equality fails: 11,488 check invocations, exit 1, no fresh JSON |
| Arithmetic original | 18 methods; zero failures or errors; exit 0 | One failed startup guard before loading the suite: zero methods, exit 1, no JSON |
| Balanced arithmetic | 12,017 checks; exit 0 | One failed startup guard before mathematical loops: zero loop checks, exit 1, no JSON |
| PR24 corrected and original, separate witnesses | 8 methods per positive mode, with identical normal / optimized records for the respective checker | Intentional startup guard before the suite: zero methods, exit 1 |
| PR24 historical interface | 18 result records: 17 helper pass records and one nonzero rational record; additional direct assertions are not counted by that record total | No negative job in the existing plan |

The complete saved window positive check arrays were independently recounted and compared. Every record passes, and the receipts differ only in `created_utc` and `elapsed_seconds`. Their hashes are `215e695a2dd38bac81dcea969a2d96a9c296b296602769b0df9dd4de53c4051a` and `fdccc046446a3499bc5fab8ca63e05d87d37a2966fb99967f5206303dd7fa361`. The terminal receipt SHA-256 is `c60f2839296ed1249bb23148a55283629c982a68c27826e68f03c5b895f3b410`.

Historical attached window mode has 11,484 exact records plus four displays because it additionally verifies one parent-source hash. That extra positive source pin and the portable mode's intentional failing Gaussian record are different check invocations; equal total counts do not identify them. The portable checker opens no local source dependencies unless `--attachment` is supplied. The existing portable jobs omit that argument.

## Existing per-mode expectation ledger

The following rows transcribe the existing plan exactly; they are not new executions. Every optimized partner is retained in the JSON. The owner terminal audit above covers its named suites; EW and EP expectations remain attributed to their earlier pinned preparation.

| Normal-mode job | Expected exit | Count and failure fields |
| --- | ---: | --- |
| `ew-fixture-normal` | 0 | checks_count=416, failure_count=0 |
| `ew-fixture-normal-mass` | 1 | checks_count=416, failure_count=23 |
| `ew-fixture-normal-tensor_cross` | 1 | checks_count=416, failure_count=8 |
| `ew-fixture-normal-schur_z` | 1 | checks_count=416, failure_count=60 |
| `ew-fixture-normal-window_ratio` | 1 | checks_count=416, failure_count=15 |
| `ew-fixture-normal-omega_denominator` | 1 | checks_count=416, failure_count=15 |
| `ew-fixture-normal-endpoint_half` | 1 | checks_count=416, failure_count=35 |
| `ew-supplement-normal` | 0 | checks_count=331, failure_count=0 |
| `ew-supplement-normal-paired_prefix_power` | 1 | checks_count=331, failure_count=15 |
| `ew-supplement-normal-paired_first_power` | 1 | checks_count=331, failure_count=15 |
| `ew-supplement-normal-omit_quadratic_radius` | 1 | checks_count=331, failure_count=27 |
| `ew-supplement-normal-coefficient_mass` | 1 | checks_count=331, failure_count=32 |
| `ew-independent-remainder-kernel` | 0 | expected_check_count=6, mathematical_checks=6 |
| `ew-independent-final-numeric` | 0 | expected_check_count=67, mathematical_checks=63 |
| `original-arithmetic-normal` | 0 | methods=18 |
| `original-arithmetic-normal-startup-negative` | 1 | startup guard; zero test methods and no formula mutation |
| `pr24-public_core_normal` | 0 | errors=0, failures=0, tests_run=8 |
| `pr24-public_core_normal_negative` | 1 | One startup failure; zero mathematical methods; no JSON |
| `pr24-proposed_core_normal` | 0 | errors=0, failures=0, tests_run=8 |
| `pr24-proposed_core_normal_negative` | 1 | One startup failure; zero mathematical methods; no JSON |
| `pr24-interfaces_normal` | 0 | 18 result records: 17 helper passes and one nonzero rational value |
| `owner-balanced-normal` | 0 | checks=12017 |
| `owner-window-normal` | 0 | checks_total=11487, exact_checks=11483, approximate_display_checks=4 |
| `owner-balanced-normal-startup-negative` | 1 | startup guard before mathematical loops |
| `owner-window-normal-gaussian-negative` | 1 | actual final Gaussian equality changed after the complete portable suite |
| `ep-source-normal-none` | 0 | checks_executed=415, failed_count=0 |
| `ep-source-normal-mass` | 1 | checks_executed=415, failed_count=6 |
| `ep-source-normal-interior` | 1 | checks_executed=415, failed_count=13 |
| `ep-source-normal-beta` | 1 | checks_executed=415, failed_count=25 |
| `ep-source-normal-schur` | 1 | checks_executed=415, failed_count=26 |
| `ep-source-normal-phase` | 1 | checks_executed=415, failed_count=5 |
| `ep-source-normal-raw_factorial` | 1 | checks_executed=415, failed_count=2 |
| `ep-scalar-normal-none` | 0 | check_count=2453, failed_count=0 |
| `ep-scalar-normal-local-remainder` | 1 | check_count=2453, failed_count=1 |
| `ep-scalar-normal-budget-denominator` | 1 | check_count=2453, failed_count=218 |
| `ep-scalar-normal-endpoint-orientation` | 1 | check_count=2451, failed_count=120 |
| `ep-scalar-normal-phase-feasibility` | 1 | check_count=2453, failed_count=8 |
| `ep-scalar-normal-interior-multiplicity` | 1 | check_count=2453, failed_count=3 |

## PR24 dependency preservation

The corrected core is 7,019 bytes with SHA-256 `0016d317a0300423a2bc14d12249214a57d677a05a177c3b3fe4f83f59488046`; its complete corrected proof is 14,807 bytes with SHA-256 `47eb717484d92c96a062a0990a4567a0929e33e1038742e538b610fcc157b9d6`. They match the prior proposed-source witnesses. The full independent PR24 read and all terminal implementation receipt paths are retained in the companion audit.

`check_interfaces.py` retains SHA-256 `9189d4d390691abd7a3d954c7ef5830fbb6f0da18791f4562a2b000715f0b11b` and its original relative import. It tests the original atomic fixture, including two zero-phase checks. Replacing that dependency with the corrected fixture would change the object being checked. Preserve the exact original core `fcaef2ee4c972cb71255ed3365930b3a558edc2b66dce5567301b38aff7ed4aa` alongside the corrected core and its separate four dispatches.

The balanced checker selects a same-directory `check_endpoint_bounds.py` first, then the original `source_stage/Tau_Arithmetic_Endpoint_Bounds/check_endpoint_bounds.py` fallback. The terminal public layout uses the first; the existing cumulative replay uses the second. Both companion files have SHA-256 `dcf57f151fd34865907bfa80f8fc063e5d46dbf69201ebee7e0a9b19b26fd2b7`. The finite module imported in either layout therefore has identical bytes.

## Durable task provenance

The full assigned request is retained verbatim in the JSON. Work stayed inside the assigned checker/dependency lane. The parent owns the complete user-input log and integration inventory. The earlier inventories, cumulative source and publication stage were not edited. The two preparation scripts only read named files, parse source/JSON, compare hashes/data and write this task's work artifacts.

No additional direct jobs or dependency rewrites are required. Carry the terminal wrapper, mode receipts and PR24 terminal implementation evidence into the next finite source inventory while retaining all historical source witnesses.
