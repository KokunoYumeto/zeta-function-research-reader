# Coherent arithmetic interpolation control

Additive continuation of the tau-base programme and PR #11. The other session's PR #12 formalization is referenced without changing its branch.

The full research note proves:

- a full-jet moment-matrix formula for the original orthogonal theta representatives;
- compatibility across nested actual arithmetic packets;
- density of the one-seed theta derivative family in the stated L2 observation, with the original stronger quotient retained;
- same-metric reflection control, without choosing an arbitrary positive metric;
- joint total-degree tensor representatives and a calculated next-layer boundary form.

Run `python check_interpolation_control.py --json check-results.json`. The script requires SymPy and uses exact finite discrete calibration measures. It does not measure zeta zeros or certify the analytic theorems.

Read `HANDOFF.md` for bounded formalization targets and the exact separation of certificates from analytic inputs. No RH/GRH conclusion is claimed. No existing mathematical source, scalar definition, workflow, dependency, or formalization file is replaced.
