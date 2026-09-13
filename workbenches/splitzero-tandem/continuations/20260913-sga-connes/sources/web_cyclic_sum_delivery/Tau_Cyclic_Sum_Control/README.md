# Cyclic arithmetic sum control

Start with `index.html` or `RESEARCH_NOTE.md`. `NOTE.tex` has the same mathematical content. The note constructs an injected sum-generated arithmetic module, its exact scalar convolution metric and rank-two control, and the full contracted conormal tower. The remaining uniform estimate is recorded explicitly.

Run the exact finite checks:

```sh
python check_cyclic_sum.py --json checks/local.json
python -O check_cyclic_sum.py --json checks/local-optimized.json
python check_cyclic_sum.py --fail-control   # deliberately exits with failure
```

Dependencies for tests: Python 3 and SymPy. The HTML uses native MathML, not external JavaScript. `build_reader.py` additionally uses pandoc and BeautifulSoup. No fonts or private transcript contents are bundled. `HANDOFF.md` is for the parallel formalization/integration session; no new Lean or remote GitHub execution is claimed.
