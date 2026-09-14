# Deligne exponential comparison — 13 September 2026

Open `index.html` for the offline MathML reader; `NOTE.tex` and `RESEARCH_NOTE.md` contain the complete editable proof.

The continuation calculates the logarithmic cohomology of the predecessor's actual curve and then builds a polynomial-exponential cohomology family from the original cyclic relation χ. It proves a free rank-q specialisation, the exact parameter connection containing the original sum operator, a constant residue duality, and an explicit full-rank contour-period map. The original theta representatives and their source metric remain attached through concrete maps.

`SOURCE_REVIEW.md` records the actual Deligne reading and historical transcription qualifications. `HANDOFF.md` gives bounded targets for the parallel formalization. `CHECKS.md` distinguishes finite regression checks from written analytic proof and imported Deligne theorems.

No RH or new uniform purity estimate is claimed. No remote branch was modified.

To rebuild and replay:

```sh
python check_exponential.py --json checks/normal.json
python -O check_exponential.py --json checks/optimized.json
python build_reader.py
```

The checker uses Sympy. The reader builder uses Pandoc and BeautifulSoup. Generated HTML uses native MathML and embedded CSS, with no external JavaScript or web fonts. Only references and a hash reading record are supplied, not the Deligne source corpus.
