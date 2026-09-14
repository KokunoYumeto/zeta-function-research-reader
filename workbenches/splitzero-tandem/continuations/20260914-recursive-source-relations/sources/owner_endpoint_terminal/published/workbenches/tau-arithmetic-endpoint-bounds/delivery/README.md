# Arithmetic endpoint bounds

Open `index.html` for the self-contained mathematical reader. `NOTE.tex` and
`RESEARCH_NOTE.md` are editable sources. `HANDOFF.md` specifies the new analytic
input and bounded finite integration targets for the parallel formalization.

This note proves the actual arithmetic norm-window bound A_(n,n)<=C_h n for
n>=k>=3 and composes it with PR #23's endpoint-selection theorem. It does not
prove the remaining four-volume bound or RH.

Run:

```sh
python check_endpoint_bounds.py
python -O check_endpoint_bounds.py
python build_reader.py
```

The checker uses SymPy and declared finite Laplace fixtures; its tests do not
certify the infinite analytic theorem. The HTML build uses Pandoc/MathML with
inline CSS. No font or external literature corpus is bundled.
