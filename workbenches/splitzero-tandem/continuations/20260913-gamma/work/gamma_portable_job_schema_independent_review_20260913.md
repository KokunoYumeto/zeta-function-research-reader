# Independent review of the 65 Gamma portable job descriptions

Date: 2026-09-13. Scope: static checker-interface and retained-evidence audit. No contributed checker, collector, stage command, replay, TeX build, publication, freeze or Lean command was executed by this review.

The reviewed job descriptions have no discovered checker-interface mismatch or missing input companion. All 65 labels are distinct; all 61 retained-result byte hashes match; all 60 retained JSON records satisfy every field declared in their job's `expected_fields`; all 29 declared normal/optimized comparisons agree on the complete retained mathematical record after removing only the listed optimization field. These statements concern existing contributed records. They do not report 65 fresh executions.

## Method and exact scope

The review read the entire job-description data, parsed all 11 distinct checker sources into Python syntax trees without importing them, examined every declared command-line argument, import and file I/O call, and read the command-line/output/failure paths and relevant control implementation directly. It resolved supporting `sources/local_gamma_continuations/...` members through the 249-member support inventory to their contributed `work/...` files; the original GP proof is pinned separately as an explicit edition proof/public file. Original-delivery paths were resolved to the extracted Gamma delivery. It hashed all declared scripts and companions, validated all retained-result hashes and expected fields, and compared each of the 29 pairs on the complete stored JSON objects. The checker programs themselves were never evaluated.

The source closure required by these concrete jobs is the 11 checker programs, three distinct non-script companions, the ordinary standard library, and the declared exact SymPy or python-flint runtime. No checker imports another local project module. The AST scan also found the original source checker's nested import of standard-library `itertools`; this requires no contributed companion.

The four runtime profiles are `sympy-1.14.0`, `sympy-1.13.1`, `python-flint-0.9.0` and `python-stdlib`. The exact version matters for the preserved full symbolic/interval records. The workflow's replay probe reads the actual dependency version and actual `sys.flags.optimize`/`__debug__` before executing the selected checker. This review inspected that invocation contract; it did not establish that every requested runtime is installed on a future replay host.

## Exact checker interfaces

All locators below refer to original contributed checker bytes, whose pins are listed later. Lines are one-based.

1. `check_gamma_descent.py`, lines 198-205: accepts optional `--json` and boolean `--fail-control`. The guard on line 200 raises before `unittest` loads/runs the `GammaDescent` suite and before the success/failure JSON writer. The positive jobs pass `--json {output}` and expect 17 methods, zero failures and zero errors. Each negative job supplies only `--fail-control`, expects exit 1, no JSON and stderr containing `deliberately false exact equality`. The guard executes zero regression methods. Its rejection remains active under `-O` because it calls `require`, rather than using `assert`. Its four jobs comprise two full positive runs and two startup guard runs.

2. `gamma_exact_coefficient_join_check_20260913.py`, lines 172-187: requires `--json`, accepts exactly the six declared `--mutant` names, computes the full result, writes JSON, and exits according to failed checks. Both modes preserve 143 checks. The complete declared mutant-to-failed-check map is:

   | Mutant | Exact failed check |
   |---|---|
   | `coefficient-factorial` | `generating-alpha-1/2-degree-4` |
   | `initial-mass` | `literal-mass-alpha-13/2` |
   | `coordinate-sign` | `original-S-congruence-k-3-n-3` |
   | `determinant-phase` | `original-S-determinant-k-1-n-3` |
   | `derivative-degree` | `finite-Gram-k-2-i-2-j-2-derivative-2` |
   | `cochain-sign` | `negative-section-cochain-k-3` |

   The job file checks the whole `failed_checks` list, so each of these 12 negative records identifies its actual single rejection. The author checker does not emit a self-script-hash field; the workflow independently pins and records its actual source bytes. No proof companion is read by this checker.

3. `gamma_seed_intervals_20260913_check.py`, lines 140-244: requires `--output`, accepts `--fault none|endpoint-factor|reference-mass|fourth-sign|tail-omission`, fixes Arb precision 256 and one arithmetic thread, then performs the original moment and tail calculations before evaluating the requested false statement. The four moments, reference mass and four coefficients form nine scalar enclosures. Each record includes 512 incomplete-gamma recurrence checks, its actual optimization integer and script hash. The positive job writes `status=passed, failed_fault_checks=0`; every fault writes `status=rejected, failed_fault_checks=1` before exiting 1. The tail-omission fault is the explicitly implemented cutoff-zero/zero-error comparison against the enclosed positive mass. It does not claim to rerun every possible omitted-tail perturbation. All ten job descriptions match these paths.

4. `gamma_seed_intervals_20260913_source_costs_check.py`, lines 62-114: requires `--output`, accepts `--input` and the four declared `--fault` values. The jobs explicitly pass the saved normal GS receipt, with byte hash `8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1`. Lines 67-73 verify its hash, success status and `fault=none`, then read the exact dyadic intervals. The calculation uses `fractions.Fraction` only. Every mutation computes the same source-cost intervals before rejecting its declared false comparison and writing the rejected JSON. This is eight concrete transports from the retained GS receipt; no new quadrature is claimed for these jobs.

5. `gamma_finite_metric_transfer_check_20260913.py`, lines 83-86 and 203-238: accepts `--output` and the five declared `--fault` names. All jobs provide the output option. The source writes its 121-check record before returning exit 0 or 1. Both modes expect zero failures for the positive run and exactly one for each of `mass`, `tensor-cross`, `boundary-sign`, `conjugation`, and `schur-denominator`. Its optimization field is the boolean `python_optimized`; this is the only field removed from its six full-record mode comparisons. No proof or external receipt is read by the checker.

6. `gamma_phase_fibre_transport_check_20260913.py`, lines 6-9 and 94-106: requires `--output`, accepts `--fault phase|mass|relative`, and reads the sibling `gamma_phase_fibre_transport_20260913.tex` when forming `proof_sha256`. Every job declares that exact companion, whose preserved hash is `9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76`. Its 61-check JSON is written before exit. The three fault modes produce 3, 1 and 4 failures respectively, exactly as the job file declares. The comparison removes only `optimized_python`. The finite polynomial calibration's own source states its exact scope; the replay job does not turn this into an analytic zeta-interval certificate.

7. `gamma_seed_coefficient_certificate_20260913.py`, lines 62-128: requires `--input` and `--output`, accepts boolean `--negative-control`. Its sole external input is the preserved TI receipt `toda_theta_input_tail_result_normal_20260912.json`, hash `2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc`. The checker also verifies the input receipt's original checker identity internally. Lines 67-93 validate and calculate the actual Gamma mass, coefficients and determinant correction. Lines 94-95 then reject the deliberately false bound before the output writer on line 121. Thus each negative job performs the coefficient calculation and produces no output JSON. The stderr substring includes `ValueError: deliberate false Gamma determinant-correction bound rejected`, the exact `require` exception. The two positive records contain `quadrature_rerun=false`; they transport the preserved infinite-tail-certified TI intervals and do not rerun their originating quadrature.

8. `gamma_exact_coefficient_join_typing_fixtures_20260913.py`, lines 8-15 and 106-111: no command-line parser and no external input. It raises explicit `RuntimeError` on a failed exact comparison and on failure to reject either of the two explicit sign controls. It emits one complete JSON object on stdout, with 37 checks, `all_pass=true`, and both negative-control fields true. `stdout-json` is the correct contract. Both modes are declared and their whole JSON records agree. The runtime/source pins are external evidence for its execution mode because this checker does not emit an optimization field.

9. `gamma_finite_metric_transfer_independent_check_20260913.py`, lines 124-134: no command-line parser, no external input and no optimization claim. It writes the fixed sibling `gamma_finite_metric_transfer_independent_check_result_20260913.json`, then prints a short status object. Therefore its job must read the sibling file rather than interpret stdout as the complete 37-check record. It declares exactly this fixed path and only normal mode.

10. `gamma_phase_fibre_projection_fixture_check_20260913.py`, lines 116-135: no command-line parser and no external input. It writes `Path(__file__).with_suffix('.json')`, then prints the same complete JSON object. The chosen `fixed-sibling-json` description resolves to `gamma_phase_fibre_projection_fixture_check_20260913.json`, exactly the file it writes. Its expected `checks` value is the complete 37-entry list of labels and booleans. Only normal mode is declared.

11. `gamma_toda_index_check_20260913.py`, lines 17-45: its 32 comparisons use `assert`; the only declared job is unoptimized and explicitly sets `optimized_execution_forbidden=true`. Its output is text, with exact marker `PASS 32 exact finite checks`. The retained `.json` file is a provenance receipt of the prior observed inline normal execution, not output emitted by this script. The job correctly uses `stdout-text`, rather than expecting a new JSON file. The old receipt records source sizes 1-4, six quotient-first determinants, six source/relation/quotient identities, six original-S/real-u relation determinants and six empty-packet identities, with the eight source determinants giving 32 in total. No optimized run or negative controls are claimed for this checker.

## Companion and output topology

There are exactly three distinct external data/proof companions read by the eleven scripts:

| Consumer | Companion within the copied support tree | How checked |
|---|---|---|
| GS source-cost jobs | `gamma_seed_intervals_20260913_normal.json` | Checker compares the full input-byte hash and success/fault fields before exact dyadic parsing. |
| GP author jobs | `gamma_phase_fibre_transport_20260913.tex` | Checker reads the sibling proof and returns its hash; the expected field is the exact contributed proof pin. |
| FE coefficient jobs | `toda_theta_input_tail_result_normal_20260912.json` | Checker compares input-byte hash, success/negative status and original TI checker identity. |

The fixed-sibling independent outputs already exist in the contributed inventory as retained evidence. Replay must remove only that one target from each newly created disposable support copy before taking its protected-input snapshot, then read the newly written sibling result. The inspected workflow follows that order at its fixed-output branch. It neither executes in the contributed source tree nor treats the old retained result as fresh output.

The schema's placeholder contract describes an isolated support location; the implementation substitutes `support`, `delivery` and `result.json` as paths relative to each fresh job directory. With that directory as the recorded subprocess working directory, those resolve to exactly the required isolated support root, delivered checker root and output path. The `runpy` invocation inserts the selected script's parent in `sys.path`; this preserves direct-script sibling lookup if one is later required. The present eleven scripts need no sibling module import.

## Mode comparisons and declarative metadata

There are 56 `json-option` jobs, four `absent` guard jobs, two `stdout-json` jobs, two `fixed-sibling-json` jobs and one `stdout-text` job. The first seven checker families account for 60 primary jobs; the remaining four families account for five independent jobs.

The 29 complete mode comparisons are: one original suite pair; seven GC pairs; five GS pairs; four source-cost pairs; six GMT pairs; four GP pairs; one FE positive pair; one GC-independent pair. Guards with no JSON are checked separately in each mode. The two one-mode fixed-sibling fixtures and the assertion-based Toda fixture have no invented optimized pair.

`companion_files`, `retained_result` and `proof_hash_field` are descriptive fields in this job file. At the inspected workflow revision, replay does not dispatch behavior through those three fields: it copies and pins the complete concrete support/delivery trees, pins the selected checker independently, checks `expected_fields`, and records the full protected-input hashes. The GP proof hash is already in `expected_fields`; GS/FE input pins are enforced inside their unchanged sources and repeated in positive expected fields. Thus there is no missing current companion or proof check caused by these descriptive fields. The review used every `retained_result` descriptor to validate the archived historical evidence independently. Replay compares newly produced normal/optimized records with one another and reports their fresh byte hashes; it does not claim fresh result byte identity with every historical retained record. Runtime-version strings and actual invocation records remain explicit.

The current concrete job descriptions do not supply `hash_fields`; that generic workflow hook is unused. Actual source and companion byte pins above establish the concrete relationships, and no extra effective hook is inferred from a field name.

## Audit result

No blocking or corrective finding was discovered within this bounded checker-schema audit. The following evidence inventory fixes the exact reviewed job/spec support bytes and enumerates all 65 jobs. It is a static review result, not authorization to claim a completed portable replay or a completed PDF build.

## Exact reviewed evidence pins

| Evidence | Bytes | SHA-256 |
|---|---:|---|
| `gamma_reader_portable_jobs_20260913.json` | 85832 | `f0eb93aa0644c282dceb21e5f979b68ea4e4b6a2cc1812fd5d6b9608e7f0b951` |
| `gamma_reader_support_inventory_20260913.json` | 402397 | `2f53b0fbf5c3e300d28b88b4945a7371e884754b373cd2461fc00d565fec2a05` |
| `gamma_edition_workflow_20260913.py` | 41644 | `6ae3617fc6abe5973bb89b89e8566c69e081f09b1c4e2577ec840eb5a45b18c4` |
| `gamma_edition_spec_20260913.json` | 9061 | `5780e4f4306365ef1a4e8775ae15522e78263b1d387808218caf2a3da0547081` |

The workflow pin records the version used for the limited invocation/output observations in this review. The separate parent review covers its complete staging/build/history behavior.

| Checker | Bytes | SHA-256 |
|---|---:|---|
| `check_gamma_descent.py` | 10597 | `e9ef0ae3e01180efc2c6fb24c1ccd46567b24423990225e382ca8231058c3d74` |
| `gamma_exact_coefficient_join_check_20260913.py` | 8654 | `76c8d17278b976e06ddf2c15e94c8b476dbf67dd47af9d54bd15df6a677bcaec` |
| `gamma_seed_intervals_20260913_check.py` | 11588 | `a67942a8a4d89ba5fbee1f5d8797793209cba26eadc6d450dd2efaac13c02e4c` |
| `gamma_seed_intervals_20260913_source_costs_check.py` | 5183 | `cd8a83921958727f85f36896c5794d8292358cdc56b3f017302324724b6fa63b` |
| `gamma_finite_metric_transfer_check_20260913.py` | 11349 | `51d90e2175a41642af1d0b2a05d3bb7ca307cfc0163e152f5630527f0c58713c` |
| `gamma_phase_fibre_transport_check_20260913.py` | 5763 | `1f866c9033cd7c14e72e2260f533544ea02ea33733ff2a69c5af6e08f9548945` |
| `gamma_seed_coefficient_certificate_20260913.py` | 6063 | `f1f5adc54e750545856c47bef10fbdb0519ff50454d9685d970b412047553c6e` |
| `gamma_exact_coefficient_join_typing_fixtures_20260913.py` | 5668 | `b87b189da75b5847ab0a5cace29ec00cb290a26e9c269c2daf3bb4efdac2710a` |
| `gamma_finite_metric_transfer_independent_check_20260913.py` | 7111 | `3eb2b57a2b89d99ea228024ec1e412fd889c75267ded03429ef05850f2c4afa6` |
| `gamma_phase_fibre_projection_fixture_check_20260913.py` | 6051 | `e2cf0a3f4a6ff87db683abd918e9740e328d39ad47085b629fac8a9f696fc7a2` |
| `gamma_toda_index_check_20260913.py` | 2427 | `8f48e6361e619b98ecd5e41e33b26428fffc1b48ee5f54b08395374e21c016aa` |

| Companion | Bytes | SHA-256 |
|---|---:|---|
| `gamma_phase_fibre_transport_20260913.tex` | 26655 | `9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76` |
| `gamma_seed_intervals_20260913_normal.json` | 11821 | `8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1` |
| `toda_theta_input_tail_result_normal_20260912.json` | 3663 | `2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc` |

The two JSON companions are support-inventory members. The GP proof is an explicitly pinned original proof/public file in the edition spec; it is additional to the 249 supporting members. Its current contributed support-tree copy matches the original work proof bytes.

## All 65 reviewed jobs

For JSON outputs, the field column records every expected field except the GP-independent complete 37-entry `checks` array, whose full array was read and matched and is indicated explicitly. Script, receipt, proof and input pins are preserved in the job file and the evidence table above. The review program compared every historical record hash and every expected field; no mismatch was found.

| # | Job | Mode | Exit | Output | Expected result |
|---:|---|---|---:|---|---|
| 1 | `original-gamma-normal` | normal | 0 | `json-option` | `{"status":"passed","test_methods":17,"failures":0,"errors":0,"scope":"exact polynomial/matrix calibrations; no arithmetic quadrature, Lean or RH certificate","sympy":"1.14.0"}` |
| 2 | `original-gamma-normal-startup-negative` | normal | 1 | `absent` | `deliberately false exact equality` |
| 3 | `gc-normal` | normal | 0 | `json-option` | `{"status":"passed","checks":143,"failed_checks":[],"mutant":null,"sympy":"1.14.0"}` |
| 4 | `gc-normal-coefficient-factorial` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["generating-alpha-1/2-degree-4"],"mutant":"coefficient-factorial","sympy":"1.14.0"}` |
| 5 | `gc-normal-initial-mass` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["literal-mass-alpha-13/2"],"mutant":"initial-mass","sympy":"1.14.0"}` |
| 6 | `gc-normal-coordinate-sign` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["original-S-congruence-k-3-n-3"],"mutant":"coordinate-sign","sympy":"1.14.0"}` |
| 7 | `gc-normal-determinant-phase` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["original-S-determinant-k-1-n-3"],"mutant":"determinant-phase","sympy":"1.14.0"}` |
| 8 | `gc-normal-derivative-degree` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["finite-Gram-k-2-i-2-j-2-derivative-2"],"mutant":"derivative-degree","sympy":"1.14.0"}` |
| 9 | `gc-normal-cochain-sign` | normal | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["negative-section-cochain-k-3"],"mutant":"cochain-sign","sympy":"1.14.0"}` |
| 10 | `gs-normal` | normal | 0 | `json-option` | `{"status":"passed","optimization_flag":0,"failed_fault_checks":0,"incomplete_gamma_recurrence_checks":512}` |
| 11 | `gs-normal_fault_endpoint-factor` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 12 | `gs-normal_fault_reference-mass` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 13 | `gs-normal_fault_fourth-sign` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 14 | `gs-normal_fault_tail-omission` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 15 | `gs-costs-normal` | normal | 0 | `json-option` | `{"status":"passed","optimization_flag":0,"failed_fault_checks":0,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 16 | `gs-costs-normal_fault_drop-cross-term` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 17 | `gs-costs-normal_fault_unit-mass` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 18 | `gs-costs-normal_fault_Q0-less-one` | normal | 1 | `json-option` | `{"status":"rejected","optimization_flag":0,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 19 | `gmt-normal` | normal | 0 | `json-option` | `{"check_count":121,"failed_count":0,"python_optimized":false,"fault":null,"sympy_version":"1.13.1"}` |
| 20 | `gmt-normal_mass` | normal | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":false,"fault":"mass","sympy_version":"1.13.1"}` |
| 21 | `gmt-normal_tensor_cross` | normal | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":false,"fault":"tensor-cross","sympy_version":"1.13.1"}` |
| 22 | `gmt-normal_boundary_sign` | normal | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":false,"fault":"boundary-sign","sympy_version":"1.13.1"}` |
| 23 | `gmt-normal_conjugation` | normal | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":false,"fault":"conjugation","sympy_version":"1.13.1"}` |
| 24 | `gmt-normal_schur_denominator` | normal | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":false,"fault":"schur-denominator","sympy_version":"1.13.1"}` |
| 25 | `gp-normal` | normal | 0 | `json-option` | `{"checks":61,"failed":0,"optimized_python":false,"fault":null,"proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 26 | `gp-normal-phase` | normal | 1 | `json-option` | `{"checks":61,"failed":3,"optimized_python":false,"fault":"phase","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 27 | `gp-normal-mass` | normal | 1 | `json-option` | `{"checks":61,"failed":1,"optimized_python":false,"fault":"mass","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 28 | `gp-normal-relative` | normal | 1 | `json-option` | `{"checks":61,"failed":4,"optimized_python":false,"fault":"relative","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 29 | `fe-normal` | normal | 0 | `json-option` | `{"status":"passed","optimization_flag":0,"input_receipt_sha256":"2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc","python_flint":"0.9.0"}` |
| 30 | `fe-normal-negative` | normal | 1 | `absent` | `ValueError: deliberate false Gamma determinant-correction bound rejected` |
| 31 | `gc-independent-normal` | normal | 0 | `stdout-json` | `{"count":37,"all_pass":true,"negative_controls":{"reversed_section_correction_sign_rejected":true,"unsigned_three_factor_primitive_rejected":true}}` |
| 32 | `original-gamma-optimized` | -O | 0 | `json-option` | `{"status":"passed","test_methods":17,"failures":0,"errors":0,"scope":"exact polynomial/matrix calibrations; no arithmetic quadrature, Lean or RH certificate","sympy":"1.14.0"}` |
| 33 | `original-gamma-optimized-startup-negative` | -O | 1 | `absent` | `deliberately false exact equality` |
| 34 | `gc-optimized` | -O | 0 | `json-option` | `{"status":"passed","checks":143,"failed_checks":[],"mutant":null,"sympy":"1.14.0"}` |
| 35 | `gc-optimized-coefficient-factorial` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["generating-alpha-1/2-degree-4"],"mutant":"coefficient-factorial","sympy":"1.14.0"}` |
| 36 | `gc-optimized-initial-mass` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["literal-mass-alpha-13/2"],"mutant":"initial-mass","sympy":"1.14.0"}` |
| 37 | `gc-optimized-coordinate-sign` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["original-S-congruence-k-3-n-3"],"mutant":"coordinate-sign","sympy":"1.14.0"}` |
| 38 | `gc-optimized-determinant-phase` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["original-S-determinant-k-1-n-3"],"mutant":"determinant-phase","sympy":"1.14.0"}` |
| 39 | `gc-optimized-derivative-degree` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["finite-Gram-k-2-i-2-j-2-derivative-2"],"mutant":"derivative-degree","sympy":"1.14.0"}` |
| 40 | `gc-optimized-cochain-sign` | -O | 1 | `json-option` | `{"status":"failed","checks":143,"failed_checks":["negative-section-cochain-k-3"],"mutant":"cochain-sign","sympy":"1.14.0"}` |
| 41 | `gs-optimized` | -O | 0 | `json-option` | `{"status":"passed","optimization_flag":1,"failed_fault_checks":0,"incomplete_gamma_recurrence_checks":512}` |
| 42 | `gs-optimized_fault_endpoint-factor` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 43 | `gs-optimized_fault_reference-mass` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 44 | `gs-optimized_fault_fourth-sign` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 45 | `gs-optimized_fault_tail-omission` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"incomplete_gamma_recurrence_checks":512}` |
| 46 | `gs-costs-optimized` | -O | 0 | `json-option` | `{"status":"passed","optimization_flag":1,"failed_fault_checks":0,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 47 | `gs-costs-optimized_fault_drop-cross-term` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 48 | `gs-costs-optimized_fault_unit-mass` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 49 | `gs-costs-optimized_fault_Q0-less-one` | -O | 1 | `json-option` | `{"status":"rejected","optimization_flag":1,"failed_fault_checks":1,"input_sha256":"8688e782d2283c8c236678c75785a6170504b5317067f7bb91cc237e67b616d1"}` |
| 50 | `gmt-optimized` | -O | 0 | `json-option` | `{"check_count":121,"failed_count":0,"python_optimized":true,"fault":null,"sympy_version":"1.13.1"}` |
| 51 | `gmt-optimized_mass` | -O | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":true,"fault":"mass","sympy_version":"1.13.1"}` |
| 52 | `gmt-optimized_tensor_cross` | -O | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":true,"fault":"tensor-cross","sympy_version":"1.13.1"}` |
| 53 | `gmt-optimized_boundary_sign` | -O | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":true,"fault":"boundary-sign","sympy_version":"1.13.1"}` |
| 54 | `gmt-optimized_conjugation` | -O | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":true,"fault":"conjugation","sympy_version":"1.13.1"}` |
| 55 | `gmt-optimized_schur_denominator` | -O | 1 | `json-option` | `{"check_count":121,"failed_count":1,"python_optimized":true,"fault":"schur-denominator","sympy_version":"1.13.1"}` |
| 56 | `gp-optimized` | -O | 0 | `json-option` | `{"checks":61,"failed":0,"optimized_python":true,"fault":null,"proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 57 | `gp-optimized-phase` | -O | 1 | `json-option` | `{"checks":61,"failed":3,"optimized_python":true,"fault":"phase","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 58 | `gp-optimized-mass` | -O | 1 | `json-option` | `{"checks":61,"failed":1,"optimized_python":true,"fault":"mass","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 59 | `gp-optimized-relative` | -O | 1 | `json-option` | `{"checks":61,"failed":4,"optimized_python":true,"fault":"relative","proof_sha256":"9f6f62da311c0f6c76761ee74e234b3c77d9441e2136908857208e798ac81e76","sympy":"1.13.1"}` |
| 60 | `fe-optimized` | -O | 0 | `json-option` | `{"status":"passed","optimization_flag":1,"input_receipt_sha256":"2d5ebb1a40f1f33cff8d227ae57d68fb3ae0a18d084b74973d08fcf2c1cc32cc","python_flint":"0.9.0"}` |
| 61 | `fe-optimized-negative` | -O | 1 | `absent` | `ValueError: deliberate false Gamma determinant-correction bound rejected` |
| 62 | `gc-independent-optimized` | -O | 0 | `stdout-json` | `{"count":37,"all_pass":true,"negative_controls":{"reversed_section_correction_sign_rejected":true,"unsigned_three_factor_primitive_rejected":true}}` |
| 63 | `gmt-independent-normal` | normal | 0 | `fixed-sibling-json` | `{"status":"passed","check_count":37,"sympy":"1.13.1"}` |
| 64 | `gp-independent-normal` | normal | 0 | `fixed-sibling-json` | `{"status":"passed","checks":"complete 37-entry passed check array matched"}` |
| 65 | `toda-index-independent-normal` | normal | 0 | `stdout-text` | `PASS 32 exact finite checks` |

Final static audit: 65/65 unique job labels; 11/11 checker interfaces resolved; 3/3 external companion byte pins matched; 61/61 historical result hashes matched; 60/60 historical JSON expected-field sets matched; 29/29 complete declared mode comparisons matched. Zero checker executions were performed.
