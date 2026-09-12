# Sum-fibre connection and conormal trace

Read `index.html` for the full derivation, or `NOTE.tex` / `RESEARCH_NOTE.md` for source. The new result is a quantitative mass-retaining spectral-sum derivative estimate, a full matrix connection, and its explicit passage through the original theta relation's conormal layer into the arithmetic Jacobian trace.

`HANDOFF.md` contains bounded targets for the parallel formalization session. `PROGRAMME_STATE.md` preserves both established inputs and remaining estimates.

Run:

    python check_sum_connection.py --json checks/local.json
    python -O check_sum_connection.py --json checks/local-optimized.json
    python check_sum_connection.py --self-test-failure

The last command must fail. The optional actual theta-seed computation is

    python evaluate_seed.py --output checks/seed-local.json

Its output is numerical, not an interval certificate. Finite tests are regression checks, not proofs of the analytic convergence or of RH.

Source archives were inspected and their manifests verified without OCR or PDF extraction. No other-session mathematical or formal source is modified.
