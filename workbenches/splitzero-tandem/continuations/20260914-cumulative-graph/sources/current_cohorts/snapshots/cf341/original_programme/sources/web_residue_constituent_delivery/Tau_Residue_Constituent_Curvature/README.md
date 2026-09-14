# Residue-driven constituent curvature

The complete 11-page note is `Residue_Constituent_Curvature.pdf`. Editable sources are `NOTE.md` and the standalone `NOTE.tex`. All 53 displayed equations and written proofs are retained.

The main additions are the exact rank-one transverse map for every nonzero proper invariant constituent (RC15), the entire-parameter constituent curvature formula (RC25), its original-source coefficient and endpoint variation certificate (RC29–36), and the corrected period realization of the arithmetic Laplacian (RC39–41).

`HANDOFF.md` identifies finite algebraic formalization targets and separates them from the written analytic inputs. No new Lean certificate, remote repository edit, or publication is claimed.

## Reproduce the finite calibration

The recorded environment was Python 3.13.5 with SymPy 1.14.0. From this directory:

```sh
python -m pip install 'sympy==1.14.0'
python run_checks.py normal
python run_checks.py optimized
```

Each batch runs the twelve-method checker and three false-formula controls. The success records agree byte for byte between the two recorded modes; every false-formula control exited with code 1. The command/output receipts are in `checks/`. They are finite symbolic regressions, not proofs of improper integrals or arithmetic asymptotics.

Compile the standalone document with `xelatex NOTE.tex` twice. `INTAKE.json` records the uploaded-source hashes actually measured in this continuation. The nine manifest copy entries agree. The supplied README differs from its historical manifest pin; the supplied independent review also names a different translation-TeX pin from the delivered file and its matching manifest. Original files were not edited.

`MANIFEST.json` seals the files in this package (other than itself). It does not authenticate prior attachments or silently import their reported execution scope.
