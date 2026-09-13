"""Record completed visual inspection and pin the complete local research handoff."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PREFIX = "gamma_seed_intervals_20260913"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


visual = {"schema": "gamma-seed-visual-review-v1", "status": "passed", "artifacts": []}
for stem, count, contacts, native in [
    (PREFIX, 9, ["contact-01.png", "contact-02.png", "contact-03.png"], ["page-8.png"]),
    (PREFIX+"_source_costs_standalone", 4, ["contact-01.png"], ["page-4.png"]),
]:
    render_path = ROOT / (stem+"_render.json")
    render = json.loads(render_path.read_text(encoding="utf-8"))
    pdf = ROOT / (stem+".pdf")
    if render["pdf_sha256"] != sha(pdf) or render["pages"] != count:
        raise RuntimeError("render and PDF pins do not agree")
    if any(render["log_counts"].values()) or render["out_of_page_words"]:
        raise RuntimeError("PDF build/geometry audit found an issue")
    visual["artifacts"].append({"pdf": pdf.name, "pdf_sha256": sha(pdf), "pages": count,
                                "render_receipt": render_path.name, "render_receipt_sha256": sha(render_path),
                                "pages_actually_viewed": list(range(1, count+1)),
                                "viewed_contact_images": contacts, "additional_native_images": native,
                                "result": "No clipping, overlap, broken formulas or missing glyphs observed; equation numbers and complete interval displays fit."})
(ROOT / (PREFIX+"_visual_review.json")).write_text(json.dumps(visual, indent=2)+"\n", encoding="utf-8")
base = json.loads((ROOT / (PREFIX+"_replay.json")).read_text(encoding="utf-8"))
cost = json.loads((ROOT / (PREFIX+"_source_costs_replay.json")).read_text(encoding="utf-8"))
if base["proof_sha256"] != sha(ROOT / (PREFIX+".tex")):
    raise RuntimeError("original executed proof changed")
if cost["proof_fragment_sha256"] != sha(ROOT / (PREFIX+"_source_costs.tex")):
    raise RuntimeError("source-cost proof changed after replay")
if base["checker_sha256"] != sha(ROOT / (PREFIX+"_check.py")) or cost["checker_sha256"] != sha(ROOT / (PREFIX+"_source_costs_check.py")):
    raise RuntimeError("executed checker changed")
excluded = {PREFIX+"_manifest.json", PREFIX+"_log.md"}
members = []
for path in sorted(ROOT.glob(PREFIX+"*")):
    candidates = sorted(path.rglob("*")) if path.is_dir() else [path]
    for candidate in candidates:
        if not candidate.is_file() or candidate.name in excluded or candidate.suffix in [".aux", ".out", ".log"]:
            continue
        members.append({"path": candidate.relative_to(ROOT).as_posix(), "bytes": candidate.stat().st_size, "sha256": sha(candidate)})
manifest = {"schema": "gamma-seed-complete-proof-handoff-v1", "status": "complete", "files": members,
            "proofs": [{"path": PREFIX+".tex", "equations": "GS.1–GS.40", "standalone_pdf_pages": 9},
                       {"path": PREFIX+"_source_costs.tex", "equations": "GS.41–GS.50", "self_scoped_fragment": True,
                        "standalone_wrapper": PREFIX+"_source_costs_standalone.tex", "standalone_pdf_pages": 4}],
            "execution": {"moment_positive_runs": 2, "moment_negative_runs_rejected": 8,
                          "cost_positive_runs": 2, "cost_negative_runs_rejected": 6,
                          "moment_distinct_scalar_enclosures": 9, "cost_distinct_scalar_enclosures": 10,
                          "cost_new_quadrature_performed": False},
            "preserved_base_proof_sha256": sha(ROOT / (PREFIX+".tex")),
            "preserved_base_pdf_sha256": sha(ROOT / (PREFIX+".pdf")),
            "scope": "Original infinite analytic seed moments, exact arithmetic gamma coefficients and fixed-degree all-k source costs. No selected packet or growing polynomial-degree bound.",
            "private_or_ephemeral_exclusions": [PREFIX+"_log.md", "*.aux", "*.out", "*.log"]}
out = ROOT / (PREFIX+"_manifest.json")
out.write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "complete", "files": len(members), "manifest_sha256": sha(out), "manifest": str(out)}))
