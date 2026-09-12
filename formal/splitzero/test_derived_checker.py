import tempfile
import unittest
from pathlib import Path
from check_derived import audit, preflight, strip_comments


class DerivedCheckerTests(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(audit("'x' depends on axioms: [propext,\nQuot.sound]", ['x']),
                         {'x': ['Quot.sound', 'propext']})

    def test_no_axioms(self):
        self.assertEqual(audit("'x' does not depend on any axioms", ['x']), {'x': []})

    def test_empty(self):
        with self.assertRaises(ValueError):
            audit('', ['x'])

    def test_missing(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: []", ['x', 'y'])

    def test_unexpected(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: []\n'y' depends on axioms: []", ['x'])

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: []\n'x' does not depend on any axioms", ['x'])

    def test_bad_axioms(self):
        for bad in ['sorryAx', 'Lean.ofReduceBool', 'CustomUnproved']:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                audit("'x' depends on axioms: [" + bad + "]", ['x'])

    def test_bad_targets(self):
        for targets in [[], ['x', 'x']]:
            with self.subTest(targets=targets), self.assertRaises(ValueError):
                audit("'x' depends on axioms: []", targets)

    def test_nested_comments(self):
        self.assertEqual(strip_comments('/- a /- b -/ c -/\nx -- d\ny').strip(), 'x \ny')

    def test_unclosed_comment(self):
        with self.assertRaises(ValueError):
            strip_comments('/- missing')

    def test_manifest(self):
        spec, hashes = preflight()
        self.assertEqual(len(spec), 7)
        self.assertEqual(len(hashes), 7)
        self.assertIn('SplitZero.Homology.ChainMap.homologyKernelEquiv', spec['SplitZeroHomology'])

    def test_missing_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'DERIVED_TARGETS.json').write_text('{"SplitZeroMissing":["SplitZero.test"]}')
            with self.assertRaises(FileNotFoundError):
                preflight(root)


if __name__ == '__main__':
    unittest.main()
