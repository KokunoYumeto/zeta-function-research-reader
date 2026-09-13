# Verified original-SplitZero integration checkpoint

13 September 2026. The observed successful implementation commit is **`4ae454c2169482a8b56f947568b5fa7a30ca5225`**. GitHub Actions [run 34739521425, job 103676725193](https://github.com/KokunoYumeto/zeta-function-research-reader/actions/runs/34739521425/job/103676725193) completed successfully at approximately 05:13:18 UTC. The complete decoded job log was read after completion. This later status-only commit changes none of the verified source, audit, or workflow blobs; a later unobserved run is not claimed.

## Observed checks

All four new modules passed individual `lean --trust=0 -DwarningAsError=true` checks. The complete used local dependency closure contains **25 SplitZero source files**, each freshly compiled under those flags. It includes the original scalar, reconstruction, internal quotient, homology, Codex support-changing adapter, joint synchronization homotopy, conormal tower, Laplacian identities, homology example, tau base, and scalar-linear recovery.

The combined import and every **47 selected new transitive axiom reports** passed using only subsets of `propext`, `Classical.choice`, and `Quot.sound`. `residueInsertion` and `residue_image_line` report no axioms. The unchanged **73-target derived audit** also passed. The 47 declarations include definitions and interface lemmas; this is not a count of mathematical discoveries. This execution does not claim to have rerun every historical library audit.

Seven fail-closed parser cases passed normally and under `python -O`, with byte-identical successful records. The forbidden-axiom negative control failed in both modes. The **24 inherited checker tests** passed in both modes. The separate Lean negative control was rejected specifically because `rfl` cannot identify the original `SplitZero.e` with `SplitZero.tau`, not because an import, instance, or identifier was missing.

Lean remains **4.31.0**, compiler commit `68218e876d2a38b1985b8590fff244a83c321783`. Mathlib remains **`fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`**. The unchanged preparer recovered and verified the original scalar blob **`ff991f7383922e71cdf0e4a3bc85e89e18f808ef`**, 7,366 bytes. Twelve original source/configuration blob checks passed before integration compilation. Those pins are review gates: a genuine future correction requires inspecting the change and updating its documented pin, not permanently rejecting all upstream corrections.

## Exact new source identities

| Source | Git blob | SHA-256 |
|---|---|---|
| `SplitZeroQuotientTransport.lean` | `6b4a8beb67d168fdc40703658f1767d776cc643a` | `4139a6c9f263c689d4913320fd1aaf618dbe72b7ba6b6512ceb6337873121570` |
| `SplitZeroSourcePresentation.lean` | `2f859dbdccb7adcf3bd9031c5eaa7bed1772d004` | `d61c9460448053711ac34d315fcc92d8e111440c56c400c1cc0c8907d97caaa2` |
| `SplitZeroPeriodTransport.lean` | `9f74dd4a29a3a4c5829546c7e57e1f9e1555efb6` | `28940ac0ddbe92b7037bc7a7de742e95c245dc12c397e69afe8d339911ffd5fb` |
| `SplitZeroResidueSupport.lean` | `be7ef0d516a6ab030906976c74dbd17bb3519699` | `c86544a34a560180f496eb46d01430879d8e8ef85371e5d917b8561cfd9d02cd` |

The target manifest is Git blob `a91e09afdcfedc6f46d9bd5fbe9d99ce4208cddb`; the audit runner is `8070ea14da5abd54adc4583124ba6cfeba53d10b`; the workflow is `e3e352322e07aeac35c2431624488b9f4753f1dd`. The runner emits all 25 source hashes, the complete dependency order, and all axiom reports into `.integration-logs/receipt.json` and the public job log.

## Concurrent-main reconciliation

Work began on main `789339c2daff74167224a7bdd665879910c168fc`. During development main advanced to **`8572a3a05be6cbcb935b05262bafef9d686072ef`**, fronting the complete cohomology reader and its disclosed public source cut. The successful implementation commit preserves that entire main tree and adds only eight integration files. This status record is the ninth added file. No inherited mathematical file, reference archive, reader, dependency pin, or other session's branch was modified or deleted. Main was not changed or merged by this contribution.

## Development failures retained in history

The first run (`34738642430`) compiled quotient transport and then exposed two omitted explicit section-hypothesis binders in the new source-presentation file. They were repaired with `include hr in`, retaining the stated right-inverse assumption. The second run (`34738912392`) compiled the first two new modules and left a reflexive dependent-pair equality in the new period module. The third run (`34739255279`) compiled the first three and required an explicit membership conversion in the final quotient-operator constructor. All were corrected before the successful fourth run. No theorem was weakened to claim a result without its necessary hypotheses, and no strict check was disabled.

## Mathematical boundary

The new certificate covers actual maps on the original reconstructed `G(R)`-semimodules and original internal quotients. It retains the separate finite-observation kernel, explicit source-section and coefficient-operation transport defects, and the period-coordinate equivalence with its conjugated transports. Source sections are not presumed natural, and equality of finite jets is not substituted for proof of an original theta boundary.

The coefficient period equivalences are explicit inputs. Their analytic invertibility, the cyclic perfect-residue-pairing nonvanishing theorem, the constituent-curvature formula, the original source-metric comparisons, and the Deligne/exponential estimates keep their previous written-proof scope. No new analytic, finite-field-purity, or RH certificate is claimed by these four integration modules. The uploaded EGA archive and French Deligne source are not represented as newly fully read or republished here.

## Reproduction

From a checkout of the verified implementation commit with the inherited Lean toolchain available:

```bash
cd formal/splitzero
python3 prepare.py
lake update
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = fabf563a7c95a166b8d7b6efca11c8b4dc9d911f
lake exe cache get
lake build
python3 ../../workbenches/tau-split-integration/run_integration.py
python3 check_derived.py --prepare
lake env lean --trust=0 -DwarningAsError=true AuditDerived.lean > /tmp/splitzero-derived.log
python3 check_derived.py /tmp/splitzero-derived.log
```

The committed workflow includes the parser tests, normal/optimized inherited tests, and the separate false-zero identification control. Its read-only permissions and pinned actions remain visible in `.github/workflows/splitzero-period-integration.yml`.
