"""Exact finite checks for the proved integral Schur-image construction.

Standard library only. Writes solely beside this script. Determinant polynomial
expansion is independent of the recursive shuffle straightening calculation.
The finite checks supplement, rather than replace, the all-ring proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json
import math
import time

ROOT = Path(__file__).resolve().parent
START = time.time()
COUNTS = Counter()


def check(condition, category):
    if not condition:
        raise AssertionError(category)
    COUNTS[category] += 1


def add_into(target, source, scalar=1):
    for key, value in source.items():
        target[key] = target.get(key, 0) + scalar * value
        if not target[key]:
            del target[key]


def mul_poly(left, right):
    result = {}
    for u, a in left.items():
        for v, b in right.items():
            key = tuple(sorted(u + v))
            result[key] = result.get(key, 0) + a * b
    return {key: value for key, value in result.items() if value}


def parity(sequence):
    return (-1) ** sum(sequence[i] > sequence[j]
                       for i in range(len(sequence))
                       for j in range(i + 1, len(sequence)))


@lru_cache(None)
def column_poly(column):
    if len(set(column)) != len(column):
        return {}
    result = {}
    for sigma in permutations(range(len(column))):
        key = tuple((r, column[sigma[r]]) for r in range(len(column)))
        result[key] = result.get(key, 0) + parity(sigma)
    return {key: value for key, value in result.items() if value}


@lru_cache(None)
def tableau_poly(tableau):
    result = {(): 1}
    for column in tableau:
        result = mul_poly(result, column_poly(column))
    return result


def sorted_column(column):
    if len(set(column)) != len(column):
        return None, 0
    return tuple(sorted(column)), parity(column)


def standard(tableau):
    return all(all(a <= b for a, b in zip(left, right))
               for left, right in zip(tableau, tableau[1:]))


@lru_cache(None)
def straighten(tableau):
    for c, (left, right) in enumerate(zip(tableau, tableau[1:])):
        for k0, (a_entry, b_entry) in enumerate(zip(left, right)):
            if a_entry > b_entry:
                prefix = left[:k0]
                tail = left[k0:]
                head = right[:k0 + 1]
                suffix = right[k0 + 1:]
                shuffled = tail + head
                size = len(tail)
                original = tuple(range(size))
                result = {}
                for chosen in combinations(range(len(shuffled)), size):
                    if chosen == original:
                        continue
                    complement = tuple(i for i in range(len(shuffled))
                                       if i not in chosen)
                    new_left, sign_left = sorted_column(
                        prefix + tuple(shuffled[i] for i in chosen))
                    new_right, sign_right = sorted_column(
                        tuple(shuffled[i] for i in complement) + suffix)
                    if not sign_left or not sign_right:
                        continue
                    smaller = tableau[:c] + (new_left, new_right) + tableau[c + 2:]
                    check(smaller < tableau, 'strict_shuffle_descent')
                    epsilon = (-1) ** sum(s - j for j, s in enumerate(chosen))
                    add_into(result, straighten(smaller),
                             -epsilon * sign_left * sign_right)
                return result
    return {tableau: 1}


def column_lengths(shape):
    return tuple(sum(row >= j for row in shape)
                 for j in range(1, shape[0] + 1)) if shape else ()


@lru_cache(None)
def fillings(shape, n):
    return tuple(product(*(tuple(combinations(range(n), h))
                           for h in column_lengths(shape))))


@lru_cache(None)
def basis(shape, n):
    return tuple(t for t in fillings(shape, n) if standard(t))


def partitions(total, largest=None):
    if not total:
        yield ()
    else:
        for first in range(min(total, largest or total), 0, -1):
            for rest in partitions(total - first, first):
                yield (first,) + rest


def expansion_poly(coordinates):
    result = {}
    for tableau, coefficient in coordinates.items():
        add_into(result, tableau_poly(tableau), coefficient)
    return result


def leading(poly, rows, n):
    def key(monomial):
        multiplicities = Counter(monomial)
        return tuple(multiplicities[(r, i)]
                     for r in range(rows) for i in range(n))
    return max(poly, key=key)


def determinant(matrix):
    size = len(matrix)
    return sum(parity(sigma) * math.prod(matrix[r][sigma[r]]
                                         for r in range(size))
               for sigma in permutations(range(size)))


@lru_cache(None)
def map_coordinates(shape, matrix, tableau):
    options = []
    for source_column in tableau:
        current = []
        for target_column in combinations(range(len(matrix)), len(source_column)):
            minor = tuple(tuple(matrix[r][c] for c in source_column)
                          for r in target_column)
            coefficient = determinant(minor)
            if coefficient:
                current.append((target_column, coefficient))
        options.append(current)
    result = {}
    for choices in product(*options):
        target = tuple(column for column, _ in choices)
        coefficient = math.prod(value for _, value in choices)
        add_into(result, straighten(target), coefficient)
    return result


def substitute_poly(poly, matrix):
    result = {}
    for monomial, coefficient in poly.items():
        term = {(): coefficient}
        for r, i in monomial:
            linear = {((r, j),): matrix[j][i] for j in range(len(matrix))
                      if matrix[j][i]}
            term = mul_poly(term, linear)
        add_into(result, term)
    return result


def matmul(left, right):
    return tuple(tuple(sum(left[i][k] * right[k][j]
                           for k in range(len(right)))
                       for j in range(len(right[0])))
                 for i in range(len(left)))


def diagonal(values):
    return tuple(tuple(value if i == j else 0 for j in range(len(values)))
                 for i, value in enumerate(values))


def content(tableau, n):
    count = Counter(i for column in tableau for i in column)
    return tuple(count[i] for i in range(n))


def weight(tableau, values):
    return math.prod(value ** exponent
                     for value, exponent in zip(values, content(tableau, len(values))))


for n in range(0, 5):
    for degree in range(7):
        for shape in partitions(degree):
            leading_monomials = set()
            for tableau in basis(shape, n):
                poly = tableau_poly(tableau)
                expected = tuple(sorted((r, value)
                                        for column in tableau
                                        for r, value in enumerate(column)))
                actual = leading(poly, len(shape), n)
                check(actual == expected and poly[actual] == 1,
                      'monic_diagonal_leading_term')
                check(actual not in leading_monomials,
                      'distinct_semistandard_leading_terms')
                leading_monomials.add(actual)
            for tableau in fillings(shape, n):
                coordinates = straighten(tableau)
                check(all(standard(t) for t in coordinates),
                      'straightening_lands_in_basis')
                check(expansion_poly(coordinates) == tableau_poly(tableau),
                      'independent_integer_polynomial_identity')
                check(all(content(t, n) == content(tableau, n) for t in coordinates),
                      'content_preserved_exactly')

# Rectangular maps are checked both by exterior-minor coordinates and by
# direct substitution in independently expanded flag polynomials.
f = ((1, 2), (-1, 0), (2, 1))
g = ((2, 1, -1), (0, -2, 3))
gf = matmul(g, f)
for shape in [(), (1,), (2,), (1, 1), (2, 1), (2, 2), (3, 1), (1, 1, 1)]:
    for tableau in basis(shape, 2):
        image = map_coordinates(shape, f, tableau)
        check(expansion_poly(image) == substitute_poly(tableau_poly(tableau), f),
              'rectangular_map_vs_polynomial_substitution')
        composed = {}
        for intermediate, coefficient in image.items():
            add_into(composed, map_coordinates(shape, g, intermediate), coefficient)
        check(composed == map_coordinates(shape, gf, tableau),
              'functor_composition_exact_over_integers')
        check(map_coordinates(shape, diagonal((1, 1)), tableau) == {tableau: 1},
              'identity_map')
    for tableau in basis(shape, 3):
        check(expansion_poly(map_coordinates(shape, g, tableau)) ==
              substitute_poly(tableau_poly(tableau), g),
              'rectangular_map_vs_polynomial_substitution')

for values in [(-2, 0, 3), (2, -3, 5), (0, 0, 0), (1, -1, 1)]:
    for degree in range(6):
        for shape in partitions(degree):
            for tableau in basis(shape, len(values)):
                scalar = weight(tableau, values)
                expected = {tableau: scalar} if scalar else {}
                check(map_coordinates(shape, diagonal(values), tableau) == expected,
                      'signed_and_zero_diagonal')
                modulus = 12
                kernel = {x for x in range(modulus) if scalar * x % modulus == 0}
                image = {scalar * x % modulus for x in range(modulus)}
                divisor = math.gcd(scalar, modulus)
                check(len(kernel) == divisor and modulus // len(image) == divisor,
                      'zero_divisor_kernel_and_cokernel_mod_12')

nested_cases = []
for inner_shape, outer_shape, values in [
        ((2,), (2, 1), (-2, 3)),
        ((1, 1), (2, 1), (-2, 0, 3)),
        ((2, 1), (2, 2), (-2, 3)),
        ((), (3,), (-2, 0, 3)),
        ((2,), (), (-2, 0, 3))]:
    inner_basis = basis(inner_shape, len(values))
    inner_weights = tuple(weight(t, values) for t in inner_basis)
    for outer in basis(outer_shape, len(inner_basis)):
        outer_content = content(outer, len(inner_basis))
        exponents = tuple(sum(outer_content[j] * content(t, len(values))[i]
                              for j, t in enumerate(inner_basis))
                          for i in range(len(values)))
        scalar = math.prod(value ** exponent for value, exponent in zip(values, exponents))
        expected = {outer: scalar} if scalar else {}
        check(map_coordinates(outer_shape, diagonal(inner_weights), outer) == expected,
              'nested_diagonal_matches_exact_schur_map')
        check(sum(exponents) == sum(inner_shape) * sum(outer_shape),
              'nested_total_degree_retained')
    nested_cases.append({'inner_shape': inner_shape, 'outer_shape': outer_shape,
                         'original_diagonal': values, 'inner_rank': len(inner_basis),
                         'outer_rank': len(basis(outer_shape, len(inner_basis)))})

receipt = {
    'status': 'pass',
    'scope': 'Finite exact checks supplement the all-commutative-ring proof; no finite check is used as an all-rank proof.',
    'checks': dict(COUNTS),
    'total_checks': sum(COUNTS.values()),
    'integer_basis_test_scope': {'ranks': list(range(5)), 'degrees': list(range(7))},
    'nested_cases': nested_cases,
    'source_sha256': hashlib.sha256((ROOT / 'integral_schur_basis.tex').read_bytes()).hexdigest(),
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'elapsed_seconds': round(time.time() - START, 3),
}
(ROOT / 'verification.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt))
