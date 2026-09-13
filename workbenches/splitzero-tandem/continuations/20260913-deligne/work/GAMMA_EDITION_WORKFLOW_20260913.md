# Gamma continuation: complete H-based source package and portable replay

This workflow prepares the cumulative Gamma edition from the immutable Toda edition H. It performs no GitHub operation, no merge, no frozen-edition replacement, and no Zenodo operation. The integration owner runs its explicit local commands after the reader build and reviews are complete. Preparing these files does not claim that collection, staging, replay or publication has already happened.

The exact baseline is `release_20260913h`, at commit `16fc4dbb817b82023c6126e636f1c6df28d4cecd`: 946 files, 424 pages, 38 full proof chapters, 39 TeX inputs including `tex/main.tex`, and 18 complete source appendices. The specification pins all three special baseline files. Every other H member is checked against the complete H public manifest, including its byte count. H's inherited `base_commit` field names an earlier ancestor; it is not substituted for the actual H commit above.

The Gamma cut adds exactly five full chapters: GC coefficient joining; GS seed intervals; GS source costs; GMT finite metric transfer; and GP phase/fibre transport. This gives 43 proof chapters and 44 TeX inputs. It adds the whole delivered `RESEARCH_NOTE.md` as appendix 19. The delivered alternate `NOTE.tex` and all other members of the 38-file Gamma archive remain byte-exact source files. The original archive SHA256 is `4b93cc5e9db76fdc6dec406c05197e2de5d7daab5957a855ee8b77711652b61a`; the complete appended Markdown witness SHA256 is `886c82e2562d9b4846adb44640d28a34552e38eb2518a3cd47f90dbbedd95e5b`.

## Exact membership and dependencies

`gamma_edition_spec_20260913.json` is the executable edition declaration. Its public file list is explicit. Its `support_inventory` is the independently assembled five-proof support closure, containing 249 members, and is itself hash-pinned. The support inventory records original paths, archive paths, byte counts, SHA256 hashes, lane membership, terminal manifests, exclusions, and dependency edges. The five original proof sources are separately pinned; they are not counted as support duplicates.

The collector retains every support file at its declared `sources/local_gamma_continuations/` location. It checks every byte against the inventory before staging. This includes complete mathematical reviews, primary results, formula-mutant results, independent fixture results, replay scripts and receipts, all retained proof-review PNGs and contact sheets, and the FE certificate's exact TI input receipt. The existing complete TI proof remains inherited from H. The collector does not use a `gamma*` glob: concurrent endpoint-window work belongs to a later cut.

All 946 H members are copied into a fresh sibling stage. This retains the complete existing reader source, full older proof sources, all older source packages, exact historical receipts and standalone builder dependencies. The additional `cyclic_publication_contract_20260912.py` is included explicitly because H does not contain that dependency of the new workflow. The new workflow never imports a publisher module.

The cumulative reader's final build receipt must identify precisely all 44 current TeX inputs and all 19 source appendices. Every inherited proof other than the declared cumulative main/conclusion updates must equal its H bytes. All inherited source witnesses and converted appendices must equal their H bytes. The source assembly must include each complete converted appendix exactly once. The five originals and the integrated fragments remain related by the recorded fragment transformations.

The collector reads the actual completed PDF, build receipt, source receipt, source audit, final integration review and visual receipts. It derives their hashes and page count from those files. There are no fabricated final PDF, page, build, QA or review hashes in the specification. Missing or inconsistent final evidence yields a `pending` inventory and prevents staging.

The final source audit path is `build/source_audit_20260913i.json`; its `checks` must pin every current TeX input, and its `sources` must pin each original and converted appendix. The final review path is `logbook/gamma_final_integration_review_20260913.md`. The cumulative visual approval must identify the current PDF and every page. Its component receipts are included automatically, along with every contact sheet explicitly named in the final QA receipt. Additional reviewed page images or comparison receipts belong in the specification's explicit `public_files` list. A broad sweep of native QA folders is not used.

## Public metadata and immutable history

Every original member of the user-supplied Gamma archive remains byte-exact, as do the original five proofs and the actual portable checker programs. Local machine locators in generated JSON, Markdown, text and traceback metadata are converted to `package:`, `workspace:`, `corpus:Chatnotes`, `corpus:SSD-transcript-mirror`, `corpus:OS`, `corpus:SSD-downloads`, `runtime:research-python` and `local:user-profile` aliases. The public manifest records the original SHA256, public SHA256, public byte count, and whether aliasing changed the bytes. Original receipts that pin other original receipts keep that historical meaning; the public manifest supplies their original/public correspondence.

Two explicitly named historical local helpers contain fixed machine paths: `replay_gamma_convolution_20260913.py` and `stage_gamma_convolution_20260913.py`. Only their locator text is aliased in the public copy. Their original hashes remain recorded. They are historical native helpers and are not selected as portable replay entrypoints. The 65 selected jobs instead invoke actual checker programs with relative arguments and complete companion trees.

Every overwritten H JSON/Markdown/log receipt and all three H special files are preserved with exact previous public bytes under `history/20260913-toda/`. `RECEIPT_LOCATORS.json` records original and historical locations, hashes, byte counts, and H's actual commit. H's earlier history is inherited as well. The new public manifest and README describe the Gamma edition itself and link to the root-readable PDF. No historical receipt is relabelled as a new Gamma execution.

## Local commands for the integration owner

Run these from the task workspace with Python 3.12 or later. The collector and stage names are already fixed in the specification. The stage command refuses an existing target; it never deletes or merges a previous stage.

```text
python -B work/gamma_edition_workflow_20260913.py inspect
python -B work/gamma_edition_workflow_20260913.py collect
python -B work/gamma_edition_workflow_20260913.py stage
python -B work/gamma_edition_workflow_20260913.py replay
```

`inspect` is read-only and returns exit code 2 while final evidence is pending. `collect` copies only explicitly declared work artifacts into the current package and writes `checks/gamma_integration_manifest.json`. `stage` recomputes the inventory and requires exact equality with the collected inventory. It creates `github_stage_gamma` as a fresh H-derived sibling. The configured later frozen name is `release_20260913i`, and the intended remote prefix is `workbenches/splitzero-tandem/continuations/20260913-gamma`; this workflow does not create either a frozen edition or a remote commit.

`replay` copies the complete contributed stage into a new isolated directory and rebuilds the reader. It requires identical text on every page and the exact contributed page count. PDF metadata may differ; both contributed and rebuilt PDF hashes are recorded. Missing glyphs, overfull boxes, undefined references, multiply defined labels and TeX errors fail the replay. The contributed source, stage and immutable H directory remain unchanged. A replay receipt path must be fresh, so earlier executions cannot be silently overwritten.

## Portable replay from an exported package

The package contains this workflow, its specification, the complete path-contract dependency and the exact job description. A fresh exported-package replay does not read the original machine's workspace or historical native helpers. Run from the exported package root:

```text
python -B work/gamma_edition_workflow_20260913.py replay --package . --receipt ../gamma-replay.json --runtime-map ../gamma-runtimes.json
```

The receipt must reside outside the contributed package. The runtime map is a host configuration file; it is not an assertion that particular environment paths exist in the package. For each runtime profile it may declare a Python executable and/or a module directory. For example, a machine with separate environments can supply:

```json
{
  "sympy-1.14.0": {"python": "/path/to/sympy114/bin/python"},
  "sympy-1.13.1": {"python": "/path/to/sympy113/bin/python"},
  "python-flint-0.9.0": {"python": "/path/to/flint09/bin/python"},
  "python-stdlib": {"python": "/path/to/python"}
}
```

These are illustrative host locators, not delivered executables. On Windows use the actual environment's `python.exe` path with valid JSON escaping. The local task default uses its existing `work/kernel_layer_replay_dependencies_20260912` module directory for SymPy 1.14.0; an exported replay does not assume that local directory exists. Required checker versions are SymPy 1.14.0, SymPy 1.13.1 and python-flint 0.9.0. The invoking workflow also needs `pypdf`; the reader rebuild needs XeLaTeX and the fonts/packages named in the source. No dependency is installed by the workflow.

An optional `--checks-only` explicitly omits the PDF rebuild and records that narrower execution. Such a receipt cannot be described as a complete portable reader rebuild. The ordinary command above performs both the rebuild and the full checker plan.

## Exact checker and rejection scopes

The portable job description contains 65 jobs: 60 primary executions and five independent executions, with 29 explicitly declared normal/optimized JSON comparison pairs. Every job receives fresh copies of the complete support and delivered-source trees. All selected scripts, proofs, imports and input receipts retain their relative topology. Checker arguments use relative `support/`, `delivery/` and `result.json` paths; fixed-sibling output programs run only in disposable copies, with the declared old output removed from that copy before execution.

The workflow supports each actual output contract: explicit JSON output option, absence of a JSON output after a rejected guard, JSON on stdout, a fixed JSON filename beside a checker, and an exact stdout marker for the assertion-based Toda index fixture. The Toda fixture is normal-mode only because optimization would remove its assertions.

The original Gamma source suite has 17 test methods in its positive executions. Its deliberate startup equality guard runs zero regression methods and writes no JSON. The GC checker runs 143 checks and each of six mutants fails its specified one check. The GS jobs retain their 512 recurrence checks and certified scalar results; GS source-cost jobs use exact saved dyadic inputs. The GMT checker runs 121 checks and each of five mutants fails one check. The GP checker runs 61 checks; its phase, mass and relative mutants fail respectively 3, 1 and 4 checks. FE transports its exact saved TI input and rejects the deliberate false bound without writing success JSON. Independent GC, GMT and GP fixture scopes, and the normal-only 32-assertion Toda index scope, remain explicitly declared in the job description.

A pre-check runtime probe records observed optimization, `__debug__`, Python version, executable and actual library version before entering each checker. It runs even for startup guards. Every invocation records the actual argv, cwd, environment overrides, expected and observed exit status, timeout, script hash, complete copied input hashes, stdout/stderr hashes and parsed result. The workflow removes ambient `PYTHONPATH` and `PYTHONOPTIMIZE` before applying the declared runtime profile. It does not reconstruct execution flags from a later result or infer unexecuted test methods.

Normal and optimized records are compared in full after removing only the job description's explicit actual-mode field. A numerical enclosure, finite symbolic calibration, failed mutant, or production receipt does not prove a general growing-degree RH estimate. The package carries the full proved mathematics and its exact verification scopes; it makes no additional Lean claim.
