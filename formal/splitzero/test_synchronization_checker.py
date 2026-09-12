import unittest
from check_synchronization import audit, names


class SynchronizationChecker(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(audit("'x' depends on axioms: [propext,\nQuot.sound]", ['x']),
                         {'x': ['Quot.sound', 'propext']})

    def test_empty_axioms(self):
        self.assertEqual(audit("'x' does not depend on any axioms", ['x']), {'x': []})

    def test_missing(self):
        with self.assertRaises(ValueError):
            audit('', ['x'])

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            audit("'x' depends on axioms: []\n'x' does not depend on any axioms", ['x'])

    def test_forbidden(self):
        for bad in ['sorryAx', 'Lean.ofReduceBool', 'Unproved']:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                audit("'x' depends on axioms: [" + bad + "]", ['x'])

    def test_target_discovery(self):
        targets = names()
        for n in ['Mixed', 'Amplitude', 'synchronize_idempotent', 'amplitude_synchronize', 'mul_E_strict']:
            self.assertIn('SplitZero.Synchronization.' + n, targets)


if __name__ == '__main__':
    unittest.main()
