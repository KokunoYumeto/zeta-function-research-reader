from fractions import Fraction as Q
import unittest
import FINITE_REPLAY_STRICT_VERIFIER as strict


class StrictVerifierTests(unittest.TestCase):
    def test_integer_recurrence_is_exact(self):
        self.assertEqual(strict.logarithmic_coefficients([3, -1], 1), [Q(1, 3)])

    def test_negative_and_nonintegral_indices_rejected(self):
        for shift in [-1, 0.5, '0', True, Q(0)]:
            with self.subTest(shift=shift):
                with self.assertRaises((TypeError, ValueError)):
                    strict.enclose_quadratic([[-2, -1]], [1], shift)
                with self.assertRaises((TypeError, ValueError)):
                    strict.quadratic([-1], [1], shift)
        for count in [-1, 0.5, '0', True, Q(0)]:
            with self.assertRaises((TypeError, ValueError)):
                strict.logarithmic_coefficients([1], count)

    def test_float_and_bool_rationals_rejected(self):
        for value in [0.5, float('nan'), float('inf'), True, 1j]:
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    strict.enclose_quadratic([[value, 1]], [1])
                with self.assertRaises(TypeError):
                    strict.enclose_quadratic([[0, 1]], [value])
                with self.assertRaises(TypeError):
                    strict.logarithmic_coefficients([1, value], 1)

    def test_exact_string_input_and_nonzero_shift(self):
        self.assertEqual(strict.enclose_quadratic([['0', '0'], ['-1/3', '-0.25']], ['2'], 1),
            {'lower': '-4/3', 'upper': '-1', 'strict_negative_given_valid_input_enclosures': True})

    def test_malformed_intervals_rejected(self):
        for intervals in [[[2, 1]], [[0]], [[0, 1, 2]], ['01'], [[0, 'nan']], [[0, '1/0']]]:
            with self.subTest(intervals=intervals):
                with self.assertRaises((TypeError, ValueError)):
                    strict.enclose_quadratic(intervals, [1])

    def test_insufficient_or_empty_data_rejected(self):
        for intervals, c, shift in [([], [1], 0), ([[0, 1]], [], 0), ([[0, 1]], [1], 1)]:
            with self.assertRaises(ValueError):
                strict.enclose_quadratic(intervals, c, shift)
        with self.assertRaises(ValueError):
            strict.logarithmic_coefficients([0, 1], 1)
        with self.assertRaises(ValueError):
            strict.logarithmic_coefficients([], 0)

    def test_original_nonreal_example_and_interval(self):
        a = [Q(7), -Q(3360, 289), Q(1792, 289), Q(0)]
        b = strict.logarithmic_coefficients(a, 3)
        self.assertEqual(strict.quadratic(b, [-1, 1]), -Q(3500576, 24137569))
        eps = Q(1, 10**8)
        interval = strict.enclose_quadratic([(v - eps, v + eps) for v in b], [-1, 1])
        self.assertEqual(Q(interval['lower']), -Q(3500576, 24137569) - 4 * eps)
        self.assertEqual(Q(interval['upper']), -Q(3500576, 24137569) + 4 * eps)
        self.assertTrue(interval['strict_negative_given_valid_input_enclosures'])

    def test_endpoint_enclosure_with_mixed_products(self):
        # Explicitly check every corner of a three-interval box.
        import itertools
        intervals = [[Q(-2), Q(3)], [Q(-5), Q(7)], [Q(11), Q(13)]]
        c = [Q(-2, 3), Q(7, 5)]
        result = strict.enclose_quadratic(intervals, c)
        for b in itertools.product(*intervals):
            value = strict.quadratic(b, c)
            self.assertLessEqual(Q(result['lower']), value)
            self.assertLessEqual(value, Q(result['upper']))


if __name__ == '__main__':
    unittest.main(verbosity=2)
