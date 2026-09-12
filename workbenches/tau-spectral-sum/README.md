# Spectral-sum descent

Add-only mathematical continuation of PR #14, preserving the original split-zero core, other sessions' branches, and the tau-base arithmetic quotient.

Read RESEARCH_NOTE.md for the exact filtered symmetric-square quotient, one-parameter matrix-weight realization, free sum-action resolution, dual and trace, and full nilpotent fibres. HANDOFF.md gives bounded formalization targets. VALIDATION.json records finite regression evidence and its limits.

Run `python check_sum_core.py --json result.json` with SymPy installed. The public checker contains eight test methods; the expanded conversation delivery has its own 24-method suite. Neither is an analytic or Lean certificate. The deliberate false control is `--self-test-failure` and must exit nonzero.

No uniform sublinear tensor bound, purity theorem, RH or GRH is asserted. The contribution makes the product-to-one-parameter operation explicit while retaining its relative fibre, original theta relations, complete jets, arithmetic local unit and support transitions.
