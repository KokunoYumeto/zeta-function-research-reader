# Full-jet kernel / supported-layer integration

Read `index.html` for the derivation, or `RESEARCH_NOTE.md` / `NOTE.tex` for its source. `HANDOFF.md` gives bounded targets for the existing Lean library. `INTEGRATION.patch` is add-only: it creates a new workbench and does not edit existing sources.

Run the new finite suite with Python and SymPy 1.14.0:

```sh
python check_kernel_layer.py --json result.json
python -O check_kernel_layer.py --json result-optimized.json
python check_kernel_layer.py --self-test-failure
```

The final command is supposed to exit with status 1. It is an execution control, not an additional claimed theorem. No external download, credential, zeta-zero approximation, or arithmetic quadrature is needed by the checker.

`SOURCE_REVIEW_RECEIPT.json` records the independently verified input archive and rerun of its nineteen tests. `KERNEL_LAYER_RECEIPT.json` records eighteen new exact finite checks. Their logs and mode comparisons are included. `CROSSCHECK_RECEIPT.json` compares the new implementation directly with the supplied source implementation on shared finite fixtures.

All new mathematical identities have written proofs. No new Lean execution or arithmetic interval certificate is claimed. No remote branch was modified in preparing this local supplement.
