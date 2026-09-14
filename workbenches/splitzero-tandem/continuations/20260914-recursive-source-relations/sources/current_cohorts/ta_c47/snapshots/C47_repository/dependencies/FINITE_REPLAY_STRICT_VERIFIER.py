#!/usr/bin/env python3
"""Exact rational finite witness evaluator with an explicit input contract.

This additive derivative leaves the archived exact_witness_checks.py untouched.
Supported exact rationals: Fraction, int (excluding bool), or a string accepted
by Fraction (rational, finite decimal, or finite decimal exponent notation).
Floats and other implicit numeric conversions are rejected. Indices are Python
integers excluding bool. shift and count must be nonnegative.

An interval conclusion is valid for the analytic target only if the supplied
moment enclosures have been proved valid independently. This tool proves no
theta tail, quadrature, or roundoff bounds.

CLI: python FINITE_REPLAY_STRICT_VERIFIER.py INPUT.json
The JSON object must contain intervals and c, and may contain shift (default 0).
"""
from collections.abc import Sequence
from fractions import Fraction as Q
import argparse
import json
from pathlib import Path


def rational(value, label):
    if isinstance(value, bool) or not isinstance(value, (Q, int, str)):
        raise TypeError(f'{label} must be a Fraction, integer, or rational string')
    try:
        return Q(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f'{label} is not a finite rational') from exc


def nonnegative_integer(value, label):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f'{label} must be an integer')
    if value < 0:
        raise ValueError(f'{label} must be nonnegative')
    return value


def sequence(value, label):
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        raise TypeError(f'{label} must be a sequence')
    return value


def rational_sequence(value, label):
    return [rational(x, f'{label}[{i}]')
            for i, x in enumerate(sequence(value, label))]


def logarithmic_coefficients(a, count):
    count = nonnegative_integer(count, 'count')
    a = rational_sequence(a, 'a')
    if len(a) < count + 1 or a[0] == 0:
        raise ValueError('Need a nonzero constant and count+1 coefficients')
    b = []
    for n in range(count):
        b.append((-(n + 1) * a[n + 1]
                  - sum((a[j] * b[n - j] for j in range(1, n + 1)), Q(0))) / a[0])
    return b


def quadratic(b, c, shift=0):
    shift = nonnegative_integer(shift, 'shift')
    b = rational_sequence(b, 'b')
    c = rational_sequence(c, 'c')
    if not c or len(b) < 2 * len(c) - 1 + shift:
        raise ValueError('Need nonempty c and enough moment coefficients')
    return sum((c[i] * c[j] * b[i + j + shift]
                for i in range(len(c)) for j in range(len(c))), Q(0))


def enclose_quadratic(intervals, c, shift=0):
    shift = nonnegative_integer(shift, 'shift')
    c = rational_sequence(c, 'c')
    intervals = sequence(intervals, 'intervals')
    if not c or len(intervals) < 2 * len(c) - 1 + shift:
        raise ValueError('Need nonempty c and enough moment intervals')
    checked = []
    for k, interval in enumerate(intervals):
        pair = sequence(interval, f'intervals[{k}]')
        if len(pair) != 2:
            raise ValueError(f'intervals[{k}] must contain exactly two endpoints')
        lo, hi = [rational(x, f'intervals[{k}][{j}]') for j, x in enumerate(pair)]
        if lo > hi:
            raise ValueError(f'intervals[{k}] is reversed')
        checked.append((lo, hi))
    lower = upper = Q(0)
    for i, x in enumerate(c):
        for j, y in enumerate(c):
            lo, hi = checked[i + j + shift]
            factor = x * y
            terms = (factor * lo, factor * hi)
            lower += min(terms)
            upper += max(terms)
    return {'lower': str(lower), 'upper': str(upper),
            'strict_negative_given_valid_input_enclosures': upper < 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding='utf-8-sig'))
        if not isinstance(payload, dict) or not {'intervals', 'c'} <= payload.keys():
            raise ValueError('Input must be an object containing intervals and c')
        if payload.keys() - {'intervals', 'c', 'shift'}:
            raise ValueError('Unknown input fields')
        result = enclose_quadratic(payload['intervals'], payload['c'], payload.get('shift', 0))
    except (OSError, ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
