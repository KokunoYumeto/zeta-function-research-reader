# Tau Relation Moment Control

Continuation of the original canonical endpoint restriction calculation.

Open `index.html` for a self-contained MathML reader. `NOTE.tex` and
`RESEARCH_NOTE.md` contain the complete derivation. `HANDOFF.md` specifies finite
formalization targets and their actual source maps. `PROGRAMME_STATE.md` records
what has advanced and what has not been proved.

The main finite upper bound uses two traces of the original source cost and
requires no independently supplied lower restriction gap. The generic optimal
determinant inequality is classical; this contribution applies it to the
unchanged arithmetic source, relation layers, and consecutive-window theorem.

Run the finite checks:

```sh
python check_relation_moments.py --json checks/replay.json
python -O check_relation_moments.py --json checks/replay-optimized.json
python check_relation_moments.py --negative-control
```

The final command must fail: it intentionally omits an actual cross-pairing.
These checks are finite algebraic calibrations, not new Lean or arithmetic
quadrature certificates. No remote repository change was performed.
