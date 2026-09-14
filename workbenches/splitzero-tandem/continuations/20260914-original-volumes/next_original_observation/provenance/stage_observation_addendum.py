from pathlib import Path
import hashlib
import json
import shutil

W = Path(r"C:\Users\[[user]]\Documents\math")
BASE = W / "work/backpropagation_20260913"
GW = BASE / "root/joint_schur_intake/growing_w_20260914"
SRC = GW / "original_observation_20260914"
DEST = W / "output/Split_Zero_Mixed_Boundary_Continuation_2026-09-14/22_ORIGINAL_VOLUMES/next_original_observation"

def digest(data):
    return hashlib.sha256(data).hexdigest()

providers = [
    ("OPG", SRC / "ORIGINAL_PERIOD_VECTOR_GENERATING_MAP.tex", "sources/OPG.tex", "d43c493eee0fc4e3e69f7383e7520b91900cdb183ed7c159bd9b2b473fdc5b04"),
    ("GMB", GW / "intrinsic_mixed_rows_20260914/ORIGINAL_GAMMA_MIXED_ROW_MORPHISM.tex", "originals/GMB.tex", "32c56427cb2f62c0d41bd2f6830813a84aa01b1bff21a39fd4291e9b54f35556"),
    ("BRU", BASE / "cumulative_graph_successor_v4/tex/mixed_boundary_v3/BRU.tex", "originals/BRU.tex", "9fb1e1fd9ebf62f37259ca42f658bd144295a1568a3522e0febcb5bd7528e9fa"),
    ("PDE", BASE / "cumulative_graph_successor_v4/tex/mixed_boundary_v3/PDE.tex", "originals/PDE.tex", "6573f900d3d92ea1f4ba62accff2fac4aeeff162eb88312aab054b7a86dbb101"),
    ("IPM", BASE / "next_phase_graph_intake/mixed_boundary_transfer_20260914/provenance/dependency_snapshots/reviewed_ipm_ial.tex", "originals/reviewed_ipm_ial.tex", "c60bca36815a9a41463a4514056530a71da3f3b59666a99971f2a17d76eb6866"),
    ("IGO", GW / "intrinsic_order_20260914/INTRINSIC_EXTERIOR_GAMMA_ORDER.tex", "originals/IGO.tex", "a086f4f2ea260621f5e1a1ec5ca2d0ce8843b464634d35f9affba276a472920f"),
    ("OGN", SRC / "GAMMA_SOURCE_NORMS.tex", "sources/OGN.tex", "8d5957fb08f2e1d6448a8130dc4cc5ff530cfae2791ef15d24fd274fceaf4542"),
    ("PGCC", SRC / "review/PERIOD_GAMMA_CONSTANT_CLOSURE.tex", "sources/PGCC.tex", "4df10819db4933332fc6d72992b26b1c9a9f0da11e1d8c813c1c0611e31a9f9c"),
    ("PERIOD_LOCATORS", SRC / "review/PERIOD_PROVIDER_LOCATORS.md", "review/PERIOD_PROVIDER_LOCATORS.md", None),
    ("OPR", SRC / "OBSERVATION_RECEIVING_INTERFACE.tex", "sources/OPR.tex", "b7de12c81133c7fb75e1bd3e46be3ca591988692ff6f6b8ef6ddecfbd4bfa92e"),
    ("OPG_REVIEW", SRC / "review/REVIEW.md", "review/OPG_REVIEW.md", "4b6aab4ccd085f91e4b1189573c32e242b95dd1e77ee66a14cb8929a5561645f"),
    ("OPG_ONLY_REVIEW_HISTORY", SRC / "review/OPG_ONLY_REVIEW_9d57f6c1.md", "review/history/OPG_ONLY_REVIEW_9d57f6c1.md", "9d57f6c1aae386e54c4509a72bce1be995daec25af5824e6247c210c88970900"),
    ("POGR", SRC / "review/PRIMARY_OBSERVATION_GENERATOR_REVIEW.tex", "review/PRIMARY_OBSERVATION_GENERATOR_REVIEW.tex", "69da3305e1acb8b5fe9977c5b8e5595ea79a4bb6cf8ebfa1594abfb0b6bdacfb"),
    ("OPG_REPORT", SRC / "OBSERVATION_RESULT_AND_PROVENANCE.md", "provenance/OBSERVATION_RESULT_AND_PROVENANCE.md", "4a98dc5db264ff4345097b6db3970d67494fc6b07d32e55278d8bf2f2240d35c"),
    ("MRI_FROZEN", GW / "baseline_20260914/receiving/spans/MIXED_ROW_RECEIVING_BODY.tex", "provenance/frozen_receivers/MRI.tex", "2261a40465c584838c4db65e6c8fb7f25299583e693a125d44c6d1864bb3533d"),
    ("BRI_FROZEN", GW / "baseline_20260914/receiving/spans/BASELINE_RECEIVING_BODY.tex", "provenance/frozen_receivers/BRI.tex", "34f42d054196e6c674a5c05aeb74bd718612e9181056ca54bbbc4d2ac9f04d84"),
]

DEST.mkdir(parents=True, exist_ok=True)
manifest = {"edition": "OPG1-26 separate accepted next-source addendum", "main_cut22_unchanged": True, "providers": [], "proof_spans": []}
data_by_key = {}
for key, original, relative, expected in providers:
    data = original.read_bytes()
    actual = digest(data)
    if expected is not None and actual != expected:
        raise RuntimeError(f"Source pin mismatch for {key}: {actual}")
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original, target)
    if target.read_bytes() != data:
        raise RuntimeError(f"Copy mismatch: {relative}")
    data_by_key[key] = data
    manifest["providers"].append({"id": key, "origin": str(original), "staged": relative, "sha256": actual, "bytes": len(data)})

spans = [
    ("BRU", None, b"The actual source interpolation is", "proofs/BRU1-3.tex", "BRU1-3 and complete original observation/image/section definitions"),
    ("PDE", None, b"Direct differentiation in the single parameter $t$ gives", "proofs/PDE1-13.tex", "PDE1-13 including all determinant derivations and the final quartet statement"),
    ("IPM", b"\\section{The actual entire theta amplitude and the finite period observation}", b"\\subsection{The exact finite-unit comparison and its nonzero receiving term}", "proofs/IPM1-7.tex", "IPM.1-IPM.7; dotted original equation tags preserved"),
    ("IGO", None, b"The natural line of the source of order $s$", "proofs/IGO1-3.tex", "IGO1-3 plus complete transform, exponential-domination and Gamma-positivity proofs"),
    ("GMB", None, None, "proofs/GMB1-16.tex", "GMB1-16 complete proof, exact original source bytes"),
]
for key, start_marker, end_marker, relative, scope in spans:
    data = data_by_key[key]
    start = 0 if start_marker is None else data.index(start_marker)
    end = len(data) if end_marker is None else data.index(end_marker, start)
    span = data[start:end]
    target = DEST / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(span)
    manifest["proof_spans"].append({"provider": key, "staged": relative, "start_byte": start, "end_byte_exclusive": end, "start_line": data[:start].count(b"\n") + 1, "end_line_inclusive": data[:end].count(b"\n"), "sha256": digest(span), "scope": scope})

manifest["claim_routes"] = [
    {"claim": "OPG original observation and primary inclusion", "proofs": ["OPG1-5", "BRU1-3"]},
    {"claim": "OPG polynomial period convergence", "proofs": ["IPM.5-7", "PDE1-3"], "note": "Only polynomial amplitudes enter OPG period integrals; their negative leading phase bound already proves convergence."},
    {"claim": "OPG original period isomorphism", "proofs": ["PDE4-13"], "note": "Invertibility already follows from the unsimplified positive Gamma factors and nonzero Fourier Vandermonde in PDE9-10. The supplied scalar supplement also proves the evaluated grid product used in PDE11."},
    {"claim": "OPG full source norms and masses", "proofs": ["IGO1-3", "OGN1-3", "OPG6-7"]},
    {"claim": "OPG actual mixed-row increments", "proofs": ["GMB1-16", "OPG15-18"]},
    {"claim": "OPG exact kernel and action defect", "proofs": ["OPG19-26"]},
    {"claim": "Exact source norms and original period determinant constant", "proofs": ["OGN1-3", "PGCC1-6"]},
    {"claim": "Exact old-degree minimum-section correction and original receiving factors", "proofs": ["OPR1-5", "MRI1-5", "BRI2"]},
]
(DEST / "SOURCE_DEPENDENCIES.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps({"destination": str(DEST), "providers": len(providers), "exact_proof_spans": len(spans), "manifest_sha256": digest((DEST / "SOURCE_DEPENDENCIES.json").read_bytes())}))
