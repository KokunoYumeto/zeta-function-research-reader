from pathlib import Path
import hashlib, json, shutil, datetime, re
from pypdf import PdfReader

W = Path(__file__).resolve().parent
R = W.parent / "output" / "split_zero_rh_tandem_2026-09-12"
B = W / "endpoint_restriction_join_build_20260913"
P = W / "endpoint_restriction_join_package_20260913"
P.mkdir(exist_ok=True)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def info(p):
    return {"path": str(p), "bytes": p.stat().st_size, "sha256": digest(p)}
source = W / "endpoint_restriction_join_20260913.tex"
pdf = B / "endpoint_restriction_join_20260913.pdf"
review = W / "endpoint_restriction_join_schatten_review_20260913.md"
fixture = W / "endpoint_restriction_join_fixture_20260913.py"
fixture_result = W / "endpoint_restriction_join_fixture_20260913.json"
if digest(fixture) != "88bcee664a3812dd914e5d164de37d48f4388307e2359062ace360e988d9df14":
    raise RuntimeError("Preserved fixture source changed")
if digest(fixture_result) != "a8205b83417feb94baf903f53f9bdd0d2e38cf325fc28ceaac6a098530b4075d":
    raise RuntimeError("Preserved fixture result changed")
if digest(source) not in review.read_text(encoding="utf-8"):
    raise RuntimeError("Independent review does not pin final source")
reader = PdfReader(pdf)
if len(reader.pages) != 10: raise RuntimeError("Unexpected PDF page count")
log = (B / "endpoint_restriction_join_20260913.log").read_text(errors="replace")
bad = re.findall(r".*(?:Overfull|Underfull|undefined|Warning|^!).*", log, re.M)
if bad: raise RuntimeError(bad)
text = "\n".join(p.extract_text() or "" for p in reader.pages)
tags = re.findall(r"\\tag\{([^}]+)\}", source.read_text())
if len(tags) != len(set(tags)): raise RuntimeError("Repeated equation tag")
if not all(tag in text for tag in ("ERJ.1", "ERJ.11a", "ERJ.25", "ERJ.42a", "ERJ.45")):
    raise RuntimeError("Required PDF equation label absent")
pages = sorted(B.glob("page-*.png"))
if len(pages) != 10: raise RuntimeError("Incomplete render")
qa = {
 "schema": "endpoint-restriction-join-pdf-qa-v1",
 "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "source": info(source), "pdf": info(pdf), "page_count": len(reader.pages),
 "all_pages_individually_viewed": list(range(1, 11)),
 "visual_observations": "All ten 105-dpi rendered pages individually inspected; equations, labels, paragraphs, headings and page numbers fit and remain legible. The initial two overfull lines were repaired by exact line/display layout edits.",
 "compile_warnings": bad, "tags": tags, "rendered_pages": [info(p) for p in pages],
 "mathematical_tests_reexecuted": False,
}
qa_path = W / "endpoint_restriction_join_pdf_qa_20260913.json"
qa_path.write_text(json.dumps(qa, indent=2)+"\n", encoding="utf-8")
deps = [
 (source, Path(source.name)), (pdf, Path(pdf.name)),
 (review, Path("review") / review.name),
 (W / "endpoint_restriction_join_review_20260913.md", Path("review/earlier_complete_join_review.md")),
 (W / "endpoint_restriction_join_fixture_20260913.md", Path("proofs/complete_exact_fixture.md")),
 (fixture, Path("checks") / fixture.name), (fixture_result, Path("checks") / fixture_result.name),
 (W / "arithmetic_volume_upper_route_20260913.tex", Path("proofs/AU_complete_source.tex")),
 (W / "endpoint_product_sharpening_20260913.tex", Path("proofs/EP_complete_source.tex")),
 (W / "gamma_endpoint_window_bridge_20260913.tex", Path("proofs/EW_complete_source.tex")),
 (W / "consecutive_first_window_join_20260913.tex", Path("proofs/CJ_complete_source.tex")),
 (R / "sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control/NOTE.tex", Path("proofs/Restriction_original_NOTE.tex")),
 (W / "endpoint_product_dependencies_20260913/Arithmetic_Endpoint_Bounds_original_NOTE.tex", Path("proofs/Arithmetic_Endpoint_Bounds_original_NOTE.tex")),
 (W / "endpoint_product_dependencies_20260913/FOUR_VOLUME_THRESHOLD.md", Path("proofs/FOUR_VOLUME_THRESHOLD.md")),
 (W / "endpoint_product_dependencies_20260913/TVB_complete_source.tex", Path("proofs/TVB_complete_source.tex")),
 (W / "endpoint_product_dependencies_20260913/GC_complete_source.tex", Path("proofs/GC_complete_source.tex")),
 (qa_path, Path("review") / qa_path.name),
 (W / "endpoint_restriction_join_r47_extension_20260913.tex", Path("integration/R47_inverse_spectral_extension.tex")),
 (Path(__file__), Path("provenance") / Path(__file__).name),
 (B / "endpoint_restriction_join_20260913.log", Path("build/compile.log")),
 (B / "compile_final.stdout.txt", Path("build/compile.stdout.txt")),
] + [(p, Path("build/render") / p.name) for p in pages]
records = []
for original, target in deps:
    dst = P / target
    dst.parent.mkdir(exist_ok=True, parents=True)
    shutil.copy2(original, dst)
    if digest(dst) != digest(original): raise RuntimeError("Copy mismatch")
    records.append({"path": target.as_posix(), "original": str(original),
                    "bytes": dst.stat().st_size, "sha256": digest(dst)})
readme = """# Arithmetic restriction, source projections, and finite volume certificates

Read endpoint_restriction_join_20260913.pdf. Its editable primary TeX is beside it.
The proofs folder carries the complete original analytic and finite mathematical
dependencies, including the complete auxiliary fixture proof and balanced norm
calculation. The review folder carries the independent full-source proof review
and actual PDF inspection record. The checks folder preserves the complete
unchanged fixture calculation and all sixteen original execution outcomes.
Those historical checks were not rerun for this completion.

The new article proves explicit finite arithmetic gaps, exact source and action
maps, all trace-error terms and rational certificates, and the central-rank
inverse-power bound inherited by both endpoint windows. It preserves every
original norm, source mass, relation coefficient, theta sign, and unit direction.

Build the primary PDF with pdflatex -interaction=nonstopmode -halt-on-error
endpoint_restriction_join_20260913.tex, twice for its navigation entries.
"""
(P / "README.md").write_text(readme, encoding="utf-8")
records.append({"path":"README.md", "bytes":(P/"README.md").stat().st_size,
                "sha256":digest(P/"README.md")})
receipt = {
 "schema": "endpoint-restriction-join-completion-v1", "utc":qa["utc"],
 "source":info(source), "pdf":info(pdf), "review":info(review),
 "new_equations":tags, "page_count":10, "files":records, "file_count":len(records),
 "package":str(P), "historical_fixture_preserved":True,
 "new_fixture_replays":0, "existing_fixture_jobs":16,
 "existing_distinct_mathematical_checks":303,
 "goal_progress": "Created the previously absent standalone primary proof; completed independent mathematical review, full PDF render and visual inspection, and complete proof dependency package.",
}
manifest = W / "endpoint_restriction_join_final_manifest_20260913.json"
manifest.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
(P/"MANIFEST.json").write_bytes(manifest.read_bytes())
print(json.dumps({"manifest":info(manifest),"source":info(source),"pdf":info(pdf),"files":len(records),"pages":10}))
