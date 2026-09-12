import unittest
from check import audit, strip_comments, targets


class AuditChecks(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(audit("'x' depends on axioms: [propext,\n Classical.choice, Quot.sound]", ['x'])['x'],
                         ['Classical.choice', 'Quot.sound', 'propext'])

    def test_no_axioms(self):
        self.assertEqual(audit("'x' does not depend on any axioms", ['x']), {'x': []})

    def test_empty_log(self):
        with self.assertRaises(ValueError):
            audit('', ['x'])

    def test_missing(self):
        with self.assertRaises(ValueError):
            audit("'y' does not depend on any axioms", ['x'])

    def test_sorry(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: [sorryAx]", ['x'])

    def test_native(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: [Lean.ofReduceBool]", ['x'])

    def test_custom(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: [AssumedResult]", ['x'])

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            audit("'x' does not depend on any axioms\n'x' depends on axioms: []", ['x'])

    def test_required_duplicates(self):
        with self.assertRaises(ValueError):
            audit("'x' does not depend on any axioms", ['x', 'x'])

    def test_nested_comments(self):
        text = 'def x /- a /- inner -/ b -/ := 0\n-- theorem bad\ntheorem y := h'
        out = strip_comments(text)
        self.assertNotIn('bad', out)
        self.assertNotIn('inner', out)
        self.assertEqual(out.count('\n'), text.count('\n'))
        self.assertIn('theorem y', out)

    def test_unclosed_comment(self):
        with self.assertRaises(ValueError):
            strip_comments('/- unfinished')

    def test_real_sources(self):
        names = targets()
        for n in ['G', 'Boolean', 'Skeleton', 'Fiber', 'homEquiv', 'fiberModule',
                  'fiberDecomposition', 'corrected_assignment_extends_uniquely']:
            self.assertIn('SplitZero.' + n, names)


if __name__ == '__main__':
    unittest.main()
