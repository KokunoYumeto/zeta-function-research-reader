# Original observation and retained kernel

A complementary continuation of the original OPG/OPR and OCS source, integrated with the existing SplitZero formal library. Four new Lean modules pass the strict check at **`8e78bc7c240b04d297ade6afdadfd863e0c6db7b`**, GitHub Actions **34891954305**. See [STATUS.md](STATUS.md) for the exact source, audit and finite-execution scope.

[Complete proofs and original maps](RESEARCH_NOTE.md) · [Concurrent-main source join](LATEST_INTAKE.md) · [Receiving interface](HANDOFF.md) · [Development failures and repairs](DEVELOPMENT.md)

The metric result constructs the original minimum observation section and its corrected full kernel Gram. The dynamical result constructs the largest action-invariant submodule of the actual observation kernel. The residue result identifies that submodule with the common annihilator of the actual observation rows, using the previously proved monic residue equivalence. The polynomial-gcd/primary-socle description and explicit reconstruction have complete written proofs with exact repeated-root regressions; their status is separated from the named Lean declarations.

All original supports, mixed cross terms, arithmetic unit/period maps, source metrics, and the upstream infinite theta quotient remain attached. The observation kernel is not identified with original theta boundaries. The result does not assert that the actual period rows have trivial common annihilator or provide the remaining absolute common-kernel arithmetic asymptotic.
