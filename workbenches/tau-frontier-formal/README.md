# Finite frontier formalization

Owner-workbench continuation on a new additive branch based on verified PR #15,
commit 21970bbf4760d0bbca512a4a7996a2e38f968947. Existing files and other-session
branches are unchanged. Validation is pending until the exact-head CI completes.

Source: the owner's `Pasted markdown(20260912-171444).md`, titled Symmetric
Frontier Control, and the preceding Kernel Layer Integration supplement.
The local execution service did not mount/open the latest ZIP successfully in
this session; no source-archive manifest verification or 22-test rerun is claimed.
The complete visible markdown was used. No private transcript is republished.

Coordination: PR #16 was inspected at 40346cbda35df1bc0242b8fdd449670d4af19a80;
its six modules concern support changes, four-mask homotopies, orthogonal
representatives and rank-two control. PR #17 and its handoff were inspected at
33b29f706008124886614ba4bd55bffc489df9e2; its spectral-sum/relative-variable
programme is not duplicated here. Neither branch was changed.

The new files formalize the cross-term estimate, primal/antidual and invariant
coordinate identities, and finite signed group averaging through the existing
homology window. Mathlib supplies the general Reynolds projector; this is reuse,
not a claim that group averaging is new mathematics. The explicit arithmetic
incidence calculation, all-variable polynomial quotient, completed products and
uniform sublinear arithmetic estimate remain separate instantiations. The actual
cochain permutation action must supply its Koszul top-degree equation.

Use formal/splitzero/check_frontier.py and the added workflow. It preserves Lean
4.31.0 and Mathlib fabf563a7c95a166b8d7b6efca11c8b4dc9d911f. No new mathematical
axioms or proof escapes are accepted; the whitelist is propext, Classical.choice,
and Quot.sound. Test counts audit the harness and are not theorem counts.
