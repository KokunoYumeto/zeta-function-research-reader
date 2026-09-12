"""Synthetic tests of report validation; these are not mathematical proof tests."""
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent

class AxiomReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.names = re.findall(r'^#print axioms (\S+)', (ROOT / 'Audit.lean').read_text(), re.M)
        if not cls.names:
            raise RuntimeError('No selected declarations in Audit.lean')
        cls.good = ''.join(f"'{n}' depends on axioms: [propext,\n Classical.choice, Quot.sound]\n" for n in cls.names)

    def run_check(self, text, valid):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'audit.log'
            p.write_text(text, encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'check_axioms.py'), str(p)],
                                    capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode == 0, valid, result.stdout + result.stderr)

    def test_standard_multiline(self): self.run_check(self.good, True)
    def test_no_axioms(self):
        self.run_check(''.join(f"'{n}' does not depend on any axioms\n" for n in self.names), True)
    def test_empty(self): self.run_check('', False)
    def test_missing(self): self.run_check(self.good.replace(self.names[-1], 'Missing.name'), False)
    def test_duplicate(self): self.run_check(self.good + f"'{self.names[0]}' depends on axioms: []\n", False)
    def test_sorry(self): self.run_check(self.good.replace('propext', 'sorryAx', 1), False)
    def test_custom(self): self.run_check(self.good.replace('propext', 'My.customAxiom', 1), False)
    def test_native_escape(self): self.run_check(self.good.replace('propext', 'Lean.ofReduceBool', 1), False)
    def test_extra(self): self.run_check(self.good + "'Extra.name' depends on axioms: []\n", False)

if __name__ == '__main__':
    unittest.main()
