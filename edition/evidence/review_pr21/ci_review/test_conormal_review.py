"""Offline exact-source conormal checker tests; temporary fixtures only."""
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "prior/formal/splitzero"))
spec = importlib.util.spec_from_file_location("review_conormal", ROOT / "files/formal/splitzero/check_conormal_cyclic.py")
conormal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conormal)


class ConormalTests(unittest.TestCase):
    def fixture(self, root, manifest=None, source="theorem ok : True := by trivial\n"):
        (root / "CONORMAL_CYCLIC_TARGETS.json").write_text(json.dumps(manifest if manifest is not None else {"SplitZeroProbe":["SplitZero.Probe.ok"]}), encoding="utf-8")
        (root / "SplitZeroProbe.lean").write_text(source, encoding="utf-8")

    def test_actual_sources_prepare_and_raw_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = ROOT / "files/formal/splitzero/CONORMAL_CYCLIC_TARGETS.json"
            spec = json.loads(manifest.read_text(encoding="utf-8"))
            for name in [manifest.name]+[m+".lean" for m in spec]:
                (root / name).write_bytes((manifest.parent / name).read_bytes())
            with patch.object(conormal, "ROOT", root):
                actual, hashes = conormal.prepare()
            names = [n for ns in actual.values() for n in ns]
            self.assertEqual([len(ns) for ns in actual.values()], [16, 13])
            self.assertEqual((root / "CONORMAL_CYCLIC_MODULES.txt").read_text().splitlines(), list(spec))
            audit_source = (root / "AuditConormalCyclic.lean").read_text()
            self.assertEqual([line.removeprefix("#print axioms ") for line in audit_source.splitlines() if line.startswith("#print axioms ")], names)
            evidence = json.loads((Path(__file__).resolve().parent / "LOG_AUDIT_RECEIPT.json").read_text())
            self.assertEqual(set(evidence["new_raw_axiom_reports"]), set(names))
            self.assertEqual(hashes, {Path(row["path"]).name:row["sha256"] for row in evidence["source_bindings"] if Path(row["path"]).name in hashes})

    def test_empty_or_malformed_manifest_rejected(self):
        for value in ({}, [], {"SplitZeroProbe":[]}, {"../escape":["SplitZero.x"]}):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp); self.fixture(root, value)
                with patch.object(conormal,"ROOT",root), self.assertRaises(ValueError):
                    conormal.prepare()

    def test_invalid_duplicate_target_rejected(self):
        for names in (["SplitZero.x"]*2, ["Elsewhere.x"], [1], ["SplitZero.x; run"]):
            with self.subTest(names=names), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp); self.fixture(root,{"SplitZeroProbe":names})
                with patch.object(conormal,"ROOT",root), self.assertRaises(ValueError): conormal.prepare()

    def test_all_forbidden_tokens_rejected(self):
        for token in ("sorry","admit","axiom","unsafe","implemented_by","native_decide"):
            with self.subTest(token=token), tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp); self.fixture(root,source=token)
                with patch.object(conormal,"ROOT",root), self.assertRaises(ValueError): conormal.prepare()

    def test_comment_only_tokens_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); self.fixture(root,source="/- sorry /- unsafe -/ axiom -/\n-- admit\ntheorem ok : True := by trivial\n")
            with patch.object(conormal,"ROOT",root): self.assertEqual(len(conormal.prepare()[0]),1)

    def test_missing_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); self.fixture(root,{"SplitZeroMissing":["SplitZero.Missing.ok"]})
            with patch.object(conormal,"ROOT",root), self.assertRaises(FileNotFoundError): conormal.prepare()

    def test_incomplete_extra_duplicate_axioms_rejected(self):
        good="'SplitZero.x' depends on axioms: [propext, Quot.sound]\n"
        self.assertEqual(conormal.audit(good,["SplitZero.x"]),{"SplitZero.x":["Quot.sound","propext"]})
        for bad in ("",good+good,good+"'SplitZero.y' does not depend on any axioms\n",good.replace("Quot.sound","sorryAx"),good.replace("Quot.sound","Lean.ofReduceBool")):
            with self.subTest(bad=bad), self.assertRaises(ValueError): conormal.audit(bad,["SplitZero.x"])


if __name__ == "__main__": unittest.main()
