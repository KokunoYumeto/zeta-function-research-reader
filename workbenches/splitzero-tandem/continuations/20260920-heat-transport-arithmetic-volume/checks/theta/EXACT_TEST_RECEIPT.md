# Exact test receipt — SZ-20260920-046

Commands executed from this directory: `python exact_tests.py` and
`python -O exact_tests.py`. Both use explicit runtime exceptions;
none of the mathematical checks depends on Python assertion statements.

Both processes completed with exit code 0 and identical output:

```text
CONTROL REJECTED: wrong forward-heat sign
CONTROL REJECTED: wrong heat coefficient 1/2 in place of 1/4
CONTROL REJECTED: wrong Rodgers--Tao factor 8 in place of 16
CONTROL REJECTED: omitted exterior term in selected-packet velocity
PASS: Original Gaussian polynomial and all Mellin factors
PASS: Euler and Mellin noncommuting squares, including both scalar signs
PASS: Theta integer weights and full tensor sum of logarithmic squares
PASS: Repeated divisor Weyl transport and complete local unit inverse
PASS: Volterra integrating-factor sign and repeated-factor order independence
PASS: Rodgers--Tao factor 16, xi factor 8, and backward heat sign
PASS: Simple selected-packet root and paired trace formulas with full exterior
PASS: Repeated-root contour traces, multiplicities, and retained exterior ratio
PASS: Attained finite quotient metric, exact lift, and first metric derivative
PASS: Exact sum-collision cyclic exponents versus full tensor dimension
PASS: Four deliberate heat-factor, heat-sign, and exterior-omission controls
PASS: 11 exact check groups; no arithmetic zero approximation used.
```

The script uses exact SymPy algebra. Its finite polynomial examples are explicitly synthetic and are not presented as actual zeta-zero packets. Analytic convergence, source-space continuity, all complex-time multipliers, repeated actual-zero Volterra inversion, and the full original finite metric specialization are proved in the TeX, not inferred from the symbolic checks.

The source-level validator was executed as both `python static_checks.py` and `python -O static_checks.py`. Every check uses an explicit exception. It checks environment nesting, braces, control characters, the local vocabulary directive, unique labels, resolved cross-references, bibliography keys, and the contour-domain repair. It does not render the document. Rendering and publication were not assigned to this independent derivation.

Both final validator executions completed with exit code 0:

```text
PASS: DEBRUIJN_THETA_TRANSPORT.tex environment nesting, braces, controls, and vocabulary
PASS: WEIGHTED_THETA_METRIC_SECTIONS.tex environment nesting, braces, controls, and vocabulary
PASS: all 78 labels unique, all references and citations resolved
```

Final SHA-256 values:

| File | SHA-256 |
| --- | --- |
| DEBRUIJN_THETA_TRANSPORT.tex | 5d56168e0f686e318f25f711dd168104d53b6a3b73012b494c59c3f7495fbd07 |
| weighted_theta/WEIGHTED_THETA_METRIC_SECTIONS.tex | c441752fd032cc0ecc994ef5cd601e4044134297d8cabe1db5c3e5b5f65ea6be |
| exact_tests.py | 5d206c948fa64cae5f0db8f85ae83e7522483618095551ab2b26b08b304155f1 |
| static_checks.py | 0a8403f81ed21dcd0f7b1a3fc2dc253ef97b42154872176a070d2e57da969242 |

The four deliberate-error controls must raise the explicit test exception.
If any incorrect formula is accepted, the control raises a failure instead.
They verify rejection of the wrong heat sign, wrong heat coefficient,
missing whole-line factor, and omitted exterior term in both execution modes.

Final status: proofs and checkers frozen for parent replay and integration.
