# Validation and integration record

## Source base

- Repository: `KokunoYumeto/zeta-function-research-reader`.
- Existing PR #8 head: `25689c5376166df37801229bc275ff5a896007d9`.
- Base tree: `9f5886220ba602b464397c418e919572fc046cd1`.
- New branch: `polyclank/tau-chain-descent-20260912`.
- The contribution is stacked on PR #8 and adds files only in `workbenches/tau-chain-descent/`.

The prior tau-base and finite-operator derivations are already published in #8 and are not counted as new work here. The supplied derived formalization note is used with its explicit scope, including its allowance of nonzero bottom fibres. `SplitZeroHomology.lean` was read at the base revision, including the actual `homology_intertwines` and `kernelAction` declarations. No Lean build was run in this continuation.

## Checks executed locally

Python **3.13.5**, SymPy **1.14.0**.

- Twelve unittest methods passed in the normal interpreter.
- The same twelve methods passed under `python -O`.
- Their JSON reports were byte-identical.
- A deliberately failing thirteenth test failed in both modes, with exit status 1.
- Assertions use unittest methods; optimized Python does not remove them.

The checker's finite model uses `V=k[t]/h`, `B=k[t]/h^2`, the inclusion by multiplication by h, and the specified quotient observation. It tests extension, remainder, homotopy, support, reflection, residue and trace identities. It is not asserted to equal the infinite-dimensional analytic source. No tested model centre is claimed to be a numerical zeta zero.

The written analytic derivations depend on the exact source spaces and range theorem of the pinned PR #8. These finite tests are not a proof certificate for those analytic inputs. Existing successful Lean workflow records, where cited by the supplied notes, certify their stated formal modules, not this research note.

## Exact authored identities

| File | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `RESEARCH_NOTE.md` | 24400 | `1ab370cf2db9fce70020bebbab76d3dbd3bd37d39e28c83114eeb0eccfa2f0b3` | `86db838e79d10a8fe7d4376303706c4ea64570a1` |
| `check_chain_descent.py` | 13468 | `1e2d02de6a31f2e623c9f1070cd4e2168c0b9902dac64609e504f138f9706ea6` | `a04626fcdff250ec340f6244a1d9b996d1bfad24` |

The Git blobs returned by the connector match the local Git blob hashes computed from the exact UTF-8 bytes. The final pull-request diff is checked separately after commit creation.

## Mathematical scope

New claims are the actual chain-extension class, scaling homotopies and their cocycle, the mixed-support naturality discrepancy and its synchronization map, strict reflection for the specified section, and the resulting finite cochain traces and tensor maps. They are submitted as written proofs for mathematical review. There is no positivity, purity, RH, GRH, or infinite-projector convergence claim.

Selected supplied Deligne TeX passages in 3.3 and 6.2 were read for the comparison and duality architecture. No full historical-proof audit is claimed. No PDF OCR was used. No copyrighted source corpus, private transcript, credentials, or font files are published.
