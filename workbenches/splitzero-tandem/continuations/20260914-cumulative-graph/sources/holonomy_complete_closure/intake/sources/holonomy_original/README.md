# All-holonomy descent of the original theta quotient

Owner-directed SplitZero research continuation, 13 September 2026.

Open `index.html` for the offline, responsive MathML reader. `NOTE.md` is the editorial master, `NOTE.tex` the standalone LaTeX derivation, and `HANDOFF.md` the bounded formalization targets. The delivery contains new proofs and finite checks, not a claimed proof of RH or a Lean certificate.

The principal result is an exact quotient-mean identity, whose positive difference is the norm of original theta relations. A sharp relative source bound gives the quadratic quotient bound `(1-eta^2)G <= mean(G_theta) <= G`. Complete circle holonomy recovers the full source, finite cyclic covers retain all characters, and explicit Fourier estimates make the quotient mean finitely computable. The new residue-constituent coefficient is transported through those same metrics.

Run the finite checks:

```
python scripts/check_holonomy.py
python -O scripts/check_holonomy.py
```

SymPy is required. Native MathML needs no network connection. Rebuilding requires Pandoc and BeautifulSoup; inspecting the reader requires Playwright and an available Chromium executable. `scripts/inspect_reader.py` uses the local `/usr/bin/chromium` and injects the already-read HTML and CSS into a blank page; it does not fetch external resources.

The repository path proposed by the add-only patch is `workbenches/tau-holonomy-descent-control/`. This session does not merge or modify repository files. `SOURCE_REVIEW.md` and `VALIDATION.json` state the actual reading and execution scope. Literature/source corpora are not redistributed. A record of one repaired finite-test implementation error is preserved rather than erased.
