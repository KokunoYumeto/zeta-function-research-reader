"""Replay the delivered 24 cross-implementation finite matrix comparisons."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--layer", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    identities = {"source": (args.source.resolve(strict=True),
                             "4d7c78bd36037ee5dd7d69ade773c9860b979e6bb39a2e556df339666033773f"),
                  "layer": (args.layer.resolve(strict=True),
                            "bc603e2ebda6104e10e5b48b0de56a7430a0c3276aa2023b2603040eee1cc410")}
    modules = {}
    file_records = {}
    for name, (path, expected) in identities.items():
        if sha(path) != expected:
            raise ValueError(f"Unexpected {name} checker bytes")
        target = args.output / path.name
        shutil.copyfile(path, target)
        file_records[name] = {"source": str(path), "copy": str(target.resolve()),
                              "sha256": sha(target),
                              "git_blob": hashlib.sha1(b"blob " + str(path.stat().st_size).encode()
                                                       + b"\0" + path.read_bytes()).hexdigest()}
        modules[name] = load(target, "crosscheck_" + name)
    source, layer = modules["source"], modules["layer"]
    import sympy as sp
    records = []
    key_pairs = [("R", "R"), ("G", "G"), ("W", "W"),
                 ("Kernel", "K"), ("B", "B"), ("P", "Pold")]
    for k, degree, repeated in [(1, 2, False), (1, 3, True),
                                (2, 2, False), (2, 3, True)]:
        before = source.data(k=k, N=degree, repeated=repeated)
        after = layer.layer(k, degree, repeated)
        for source_key, new_key in key_pairs:
            difference = layer.clean(before[source_key] - after[new_key])
            equal = difference == sp.zeros(*difference.shape)
            records.append({"tensor_degree": k, "polynomial_degree": degree,
                            "repeated_jet": repeated, "source_key": source_key,
                            "new_key": new_key, "equal_exactly": equal})
            if not equal:
                raise ValueError(f"Crosscheck failed: {records[-1]}")
    vendor_path = args.layer.parent / "CROSSCHECK_RECEIPT.json"
    vendor = json.loads(vendor_path.read_text())
    same = records == vendor["records"] and len(records) == vendor["exact_matrix_comparisons"]
    unchanged = all(sha(path) == expected for path, expected in identities.values())
    receipt = {"created_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version, "optimized": sys.flags.optimize,
               "sympy": sp.__version__, "source_files": file_records,
               "exact_matrix_comparisons": len(records), "records": records,
               "vendor_receipt_sha256": sha(vendor_path),
               "vendor_records_reproduced_exactly": same,
               "staged_sources_unchanged": unchanged,
               "scope": "Shared finite discrete polynomial fixtures only; no zeta or Lean certificate",
               "success": same and unchanged}
    (args.output / "crosscheck_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"success": receipt["success"], "comparisons": len(records),
                      "sympy": sp.__version__, "optimized": sys.flags.optimize}))
    return 0 if receipt["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
