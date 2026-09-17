"""Compile only the new additive supplement and record actual PDF checks."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
BUILD = HERE.parent / "build"
STEM = "DUAL_WEB_PROOF_SUPPLEMENT"
ENGINE = Path(r"LOCAL_ACCOUNT_ROOT\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = json.loads((HERE / "INSERTION_MANIFEST.json").read_text(encoding="utf-8"))
    if not manifest.get("root_mathematical_seal"):
        raise RuntimeError("Mathematical source seal is missing")
    BUILD.mkdir(exist_ok=True)
    source = HERE / f"{STEM}.tex"
    runs_path = BUILD / "BUILD_RUNS.json"
    runs = json.loads(runs_path.read_text(encoding="utf-8")) if runs_path.exists() else []
    source_sha = digest(source)
    previous = None
    for iteration in range(1, 6):
        args = [str(ENGINE), "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-synctex=1", f"-output-directory={BUILD}", str(source)]
        start = time.monotonic()
        attempt = len(runs) + 1
        pass_log = BUILD / f"PASS_{attempt}.txt"
        with pass_log.open("wb") as stream:
            process = subprocess.run(args, cwd=HERE, stdout=stream, stderr=subprocess.STDOUT)
        auxiliary = {suffix: digest(BUILD / f"{STEM}{suffix}") for suffix in [".aux", ".toc", ".out"] if (BUILD / f"{STEM}{suffix}").exists()}
        runs.append({"attempt": attempt, "iteration_in_current_run": iteration, "source_sha256": source_sha, "args": args, "return_code": process.returncode, "seconds": round(time.monotonic() - start, 3), "auxiliary_sha256": auxiliary})
        (BUILD / "BUILD_RUNS.json").write_text(json.dumps(runs, indent=2) + "\n", encoding="utf-8")
        print(f"pass {iteration}: exit={process.returncode}, seconds={runs[-1]['seconds']}", flush=True)
        if process.returncode:
            raise RuntimeError(pass_log.read_text(encoding="utf-8", errors="replace")[-8000:])
        if auxiliary == previous:
            break
        previous = auxiliary
    else:
        raise RuntimeError("References did not stabilize in five passes")
    pdf = BUILD / f"{STEM}.pdf"
    reader = PdfReader(pdf)
    log = (BUILD / f"{STEM}.log").read_text(encoding="utf-8", errors="replace")
    all_text = "\n\n".join(f"=== PAGE {i+1} ===\n{page.extract_text()}" for i, page in enumerate(reader.pages))
    (BUILD / "PDF_TEXT.txt").write_text(all_text, encoding="utf-8")
    citations = manifest["citation_keys"]
    destinations = reader.named_destinations
    missing_cites = [key for key in citations if "cite." + key not in destinations]
    warnings = [line for line in log.splitlines() if "Warning" in line]
    overfull = re.findall(r"Overfull \\[^\n]*", log)
    undefined = bool(re.search(r"(?:Reference|Citation).*?undefined|There were undefined references", log))
    missing_glyph = "Missing character:" in log
    qa = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "status": "compiled_pending_visual_inspection",
        "pdf": {"path": str(pdf), "sha256": digest(pdf), "bytes": pdf.stat().st_size, "pages": len(reader.pages)},
        "source": {"path": str(source), "sha256": digest(source)},
        "engine": str(ENGINE),
        "passes_current_run": iteration,
        "total_recorded_compiler_attempts": len(runs),
        "auxiliary_files_stable": True,
        "overfull_boxes": overfull,
        "undefined_references_or_citations": undefined,
        "missing_glyph_warnings": missing_glyph,
        "missing_human_citation_destinations": missing_cites,
        "warnings": warnings,
        "cumulative_sources_compiled": False,
        "frozen_predecessor_pdfs_rebuilt": False,
        "rendered_visual_inspection": "pending",
    }
    (BUILD / "BUILD_QA.json").write_text(json.dumps(qa, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(qa, indent=2))
    if undefined or missing_glyph or missing_cites:
        raise RuntimeError("PDF reference/glyph validation failed")
    manifest["compilation_performed"] = True
    manifest["compilation_record"] = str(BUILD / "BUILD_QA.json")
    manifest["compilation_scope"] = "Additive supplement only; cumulative TeX sources verified structurally and by byte recovery, not recompiled."
    (HERE / "INSERTION_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
