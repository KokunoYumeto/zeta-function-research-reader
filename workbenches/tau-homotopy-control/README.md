# Tau homotopy/control integration

Additive continuation of PR #10 at d26c283c2a58da57bb5a5a4d4bc8669019f6ebb7. The owner's newly supplied homotopy-classification proof is retained and integrated with the arithmetic boundary-control construction. Nothing in the original scalar core, formal modules, dependencies, or workflows is modified.

## Read and run

- `RESEARCH_NOTE.md`: proofs of the supported and continuous homotopy interface, coherent dilation families, and the source-constrained Gram/control family.
- `check_integration.py`: sixteen exact regression methods, including finite parameter families.
- `check-results.json` and `VALIDATION.md`: exact scope and reproduction.

```sh
python check_integration.py --json normal.json
python -O check_integration.py --json optimized.json
cmp normal.json optimized.json
python check_integration.py --deliberate-failure
# The final command must fail.
```

## Handoff to the formalization session

The supplied abstract theorem is correct. Keep BOTH `d H = Theta kappa` and `H d = 0`. The second equation is what makes the unique parameter factor through `Q = B / range Theta`.

Instantiate its analytic coefficient theorem at `R = C`. For the polynomial action, the actual Fourier type is `F : V^j -> V`, with `t` acting by `1-D` on the source. Continuity of the quotient parameter follows from the quotient topology; it is not part of an arbitrary algebraic linear-map declaration.

Reconstruct every homotopy with the original support-index map taking an active face to the joint face and bottom to bottom. Its vanishing cochain amplitude is the zero of that target fibre, not external tau. The difference between parameters remains the computed `Hom(H1,H0)` class.

For a fixed representative `R`, every homotopy parameter produces the SAME boundary `Theta k`. The map from homotopy parameters to the control form is constant. The parameter that changes the control problem is the representative change `R_b = R + Theta b`, with exact boundary change `k_b = k + D b - b A`.

The finite implementation target is the actual polynomial theta ansatz `b = Phi_m B`, with `D Phi_m = Phi_(m+1) S_m`. Its graph matrices produce `G_B = X_B* M_m X_B` and `W_B = -(X_B* M_m Y_B + Y_B* M_m X_B)`. Every column has an actual source function and an exact quotient/jet map.

The supplied Lean draft is uncompiled; its reported preceding tau-chart build failure is not a new certificate. This continuation did not run Lean. It supplies bounded mathematical interfaces and exact regression tests for the other session to use. No uniform weight bound, positivity, RH, GRH, or global kernel vanishing is asserted.
