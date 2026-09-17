# Building the mathematical companion

The editable document is `RESEARCH_PROGRAMME.tex`, with the five included modules in `sources/` and the bibliography `REFERENCES.bib`. Keep that relative layout.

Use LuaLaTeX and BibTeX from a TeX distribution containing the packages declared by the driver. From this directory run:

```text
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_PROGRAMME.tex
bibtex RESEARCH_PROGRAMME
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_PROGRAMME.tex
lualatex -interaction=nonstopmode -halt-on-error RESEARCH_PROGRAMME.tex
```

The delivered PDF was built with these commands and visually inspected on every page. Its build receipt records missing-reference, missing-glyph and overflow checks. Successful compilation checks document production; it does not establish the mathematics or complete historical attribution.

The [726-page mathematical edition](https://doi.org/10.5281/zenodo.22803503) supplies the complete accepted proof corpus and its separate source package. This companion is an additional reading and attribution layer. R14/R09 page references retain the preserved 692-page predecessor's pagination; R726 denotes the accepted successor explicitly.
