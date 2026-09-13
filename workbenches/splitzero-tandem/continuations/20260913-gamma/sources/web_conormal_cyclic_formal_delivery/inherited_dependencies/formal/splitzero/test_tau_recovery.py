import json
import tempfile
import unittest
from pathlib import Path
from check_tau_recovery import preflight

class TauTests(unittest.TestCase):
    def fixture(self, root, code='theorem x : True := by trivial\n'):
        (root/'TAU_RECOVERY_MODULES.txt').write_text('SplitZeroTest\n')
        (root/'TAU_RECOVERY_TARGETS.json').write_text(json.dumps({'SplitZeroTest':['SplitZero.Test.x']}))
        (root/'SplitZeroTest.lean').write_text(code, encoding='utf-8', newline='\n')
    def test_accept(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.fixture(p)
            self.assertEqual(len(preflight(p)[1]),1)
    def test_reject_escape(self):
        for token in ('sorry','admit','axiom','native_decide','unsafe','implemented_by'):
            with tempfile.TemporaryDirectory() as d:
                p=Path(d); self.fixture(p,token)
                with self.assertRaises(ValueError): preflight(p)
    def test_reject_module_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.fixture(p)
            (p/'TAU_RECOVERY_MODULES.txt').write_text('SplitZeroOther\n')
            with self.assertRaises(ValueError): preflight(p)
    def test_reject_missing_source(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.fixture(p); (p/'SplitZeroTest.lean').unlink()
            with self.assertRaises(FileNotFoundError): preflight(p)
    def test_reject_duplicate_targets(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.fixture(p)
            (p/'TAU_RECOVERY_TARGETS.json').write_text(json.dumps({'SplitZeroTest':['SplitZero.Test.x']*2}))
            with self.assertRaises(ValueError): preflight(p)
    def test_comments_not_proof_escapes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d); self.fixture(p,'/- sorry /- axiom -/ -/\ntheorem x : True := by trivial\n')
            self.assertEqual(len(preflight(p)[1]),1)
if __name__ == '__main__': unittest.main()
