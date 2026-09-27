import subprocess
pages = []
for p in range(1, 26):
    t = subprocess.run(['pdftotext', '-layout', '-f', str(p), '-l', str(p), '../../../../ym_reader/ymreader.pdf', '-'], capture_output=True, text=True).stdout
    pages.append(t)
keys = ["inputs checked independently here", "with inputs checked independently", "Twenty-three of them", "only on Zenodo", "the other twenty are only",
        "Status. Conditional on the computed", "which the workbench had not done", "holds with audited inputs only", "Lemma 3.3 (ground-state", "For real 𝑣",
        "Proposition 3.4 (spectral", "Corollary 3.5 (the gap", "Generalised here relative", "Proposition 3.6 (the standing", "Theorem 4.1 (heat remainder",
        "Status. Audited, given the analytic", "superseded", "Proposition 4.2 (the constants", "the factor 255 is derived here", "Other radii",
        "Proposition 4.3 (relaxation", "Proposition 4.4 (the benchmark", "eleven digits", "kinetic-row constants", "Superseded quantitatively",
        "Proposition 5.1 (the first", "as the attribution file of 21 September says", "neither is a hypothesis", "Proposition 7.1 (the collapse",
        "it does not show that the true analyticity", "𝑒−𝑇𝑎0", "re-centring its norm inequality cannot", "recomputes every constant",
        "Implied", "a new script that", "credited by the workbench to Schütte", "Mass gaps at strong coupling are classical", "What the theorem is and is not",
        "Checked exhaustively", "the constant is the girth", "The earlier edition’s bound", "Finite heat time", "Heat on |𝜉 | < 3/256"]
for k in keys:
    hits = [i + 1 for i, t in enumerate(pages) if k in t]
    print(f"{k!r}: pages {hits}")
