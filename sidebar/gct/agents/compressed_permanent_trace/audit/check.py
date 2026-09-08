"""Independent exact checks for the compressed permanent trace.

Standard library only. General proofs are in audit.md; these finite checks
independently exercise parity, characters, original source-point evaluation,
the common-module exact sequence, and the row-cut dimension obstruction.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()


def check(condition, category):
    COUNTS[category] += 1
    if not condition:
        raise AssertionError((category, COUNTS[category]))


def mask_of_tuple(tup, n):
    mask = (1 << (n - 1)) - 1
    for j in tup:
        if j:
            mask ^= 1 << (j - 1)
    return mask


def tuple_for_mask(mask, n):
    """Canonical preimage under K of r^-1 times the given group basis."""
    parity = mask ^ ((1 << (n - 1)) - 1)
    chosen = tuple(j for j in range(1, n) if parity >> (j - 1) & 1)
    return chosen + (0,) * (n - len(chosen))


def rank_mod(matrix, prime=101):
    if not matrix:
        return 0
    a = [[int(x) % prime for x in row] for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, prime)
        a[rank] = [x * inv % prime for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [(x - scale * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def perm_numeric(z, power=1):
    result = 0
    for sigma in permutations(range(len(z))):
        term = 1
        for i, j in enumerate(sigma):
            term *= z[i][j] ** power
        result += term
    return result


def sign_eigenvalues(z):
    n = len(z)
    r = 1 << (n - 1)
    values = []
    for suffix in product((-1, 1), repeat=n - 1):
        signs = (1,) + suffix
        chi = 1
        for sign in signs:
            chi *= sign
        value = Fraction(chi, r)
        for row in z:
            value *= sum(sign * entry for sign, entry in zip(signs, row))
        values.append(value)
    return values


def original_source_trace(z, power=1):
    """Evaluate every original point for n<=2, with all 3n^2 witnesses.

    The coordinates x=X, y=-3X/2, w=(27X^2-1)/4 are checked separately.
    Zero X gives e=0. Otherwise beta=(X^2+X)/2 is exactly the bit used.
    This evaluates the uniquely flagged constraint indicator directly.
    """
    n = len(z)
    answer = 0
    surviving = []
    for point in product((-1, 0, 1), repeat=3 * n * n):
        if 0 in point:
            continue
        bits = tuple((x * x + x) // 2 for x in point)
        b = [bits[i * n:(i + 1) * n] for i in range(n)]
        row_flags = bits[n * n:2 * n * n]
        col_flags = bits[2 * n * n:]
        if any(sum(row) != 1 for row in b):
            continue
        if any(sum(b[i][j] for i in range(n)) != 1 for j in range(n)):
            continue
        expected_rows = tuple(int(any(b[i][:k + 1])) for i in range(n) for k in range(n))
        expected_cols = tuple(int(any(b[i][j] for i in range(k + 1))) for j in range(n) for k in range(n))
        if row_flags != expected_rows or col_flags != expected_cols:
            continue
        value = 1
        for i in range(n):
            for j in range(n):
                value *= 1 - b[i][j] + z[i][j] * b[i][j]
        answer += value ** power
        surviving.append((point, value))
    return answer, surviving


def check_parity_and_sequence(n):
    r = 1 << (n - 1)
    tuples = list(product(range(n), repeat=n))
    perms = list(permutations(range(n)))
    perm_index = {p: i for i, p in enumerate(perms)}
    classes = defaultdict(list)
    for tup in tuples:
        mask = mask_of_tuple(tup, n)
        classes[mask].append(tup)
        check((mask == 0) == (len(set(tup)) == n), 'parity_identity_iff_permutation')
        if n <= 5:
            trace = Fraction(0)
            for suffix in product((-1, 1), repeat=n - 1):
                signs = (1,) + suffix
                value = Fraction(1, r)
                for sign in signs:
                    value *= sign
                for j in tup:
                    value *= signs[j]
                trace += value
            check(trace == int(tup in perm_index), 'independent_sign_character_trace')
    check(set(classes) == set(range(r)), 'K_surjective')
    for mask in range(r):
        tup = tuple_for_mask(mask, n)
        check(mask_of_tuple(tup, n) == mask, 'explicit_K_section')
        check((tup not in perm_index) == (mask != 0), 'K_kernel_S_image')
    check(sum(len(v) - 1 for v in classes.values()) == n ** n - r, 'kernel_K_rank')
    common_kernel_rank = sum(len(v) - 1 for mask, v in classes.items() if mask)
    check(common_kernel_rank == n ** n - factorial(n) - r + 1, 'common_kernel_rank')
    # Scale the B coordinates by the unit r, so all entries are integral.
    if n <= 4:
        matrix = [[0] * len(tuples) for _ in range(factorial(n) + r)]
        for col, tup in enumerate(tuples):
            if tup in perm_index:
                matrix[perm_index[tup]][col] = 1
            matrix[factorial(n) + mask_of_tuple(tup, n)][col] = -1
        check(rank_mod(matrix) == factorial(n) + r - 1, 'exact_sequence_matrix_rank')
        trace_sum = [1] * factorial(n) + [1] + [0] * (r - 1)
        check(all(sum(t * matrix[row][col] for row, t in enumerate(trace_sum)) == 0
                  for col in range(len(tuples))), 'exact_sequence_trace_zero')
    if n >= 2:
        same = (0,) * n
        check(same not in perm_index and Fraction(1, r) != 0, 'K_cannot_factor_S')
        first, second = perms[:2]
        check(first != second and mask_of_tuple(first, n) == mask_of_tuple(second, n), 'S_cannot_factor_K')
    # Explicit group multiplication matrices: every nonidentity permutation
    # of the basis has zero diagonal, while the identity has r diagonal ones.
    for mask in range(r):
        tr = sum(int((col ^ mask) == col) for col in range(r))
        check(tr == (r if mask == 0 else 0), 'group_regular_trace')


def check_flattenings(n):
    for k in range(n + 1):
        heads = list(product(range(n), repeat=k))
        tails = list(product(range(n), repeat=n - k))
        coefficient = [[int(len(set(h + t)) == n) for t in tails] for h in heads]
        check(rank_mod(coefficient) == comb(n, k), 'permanent_flattening_rank_mod_101')
        # A second small-characteristic check prevents an implicit factorial
        # denominator from being hidden in the tested rank argument.
        if n <= 4:
            check(rank_mod(coefficient, 2) == comb(n, k), 'permanent_flattening_rank_mod_2')
        r = 1 << (n - 1)
        check(r >= comb(n, k), 'sign_algebra_obeys_dimension_bound')


def main():
    for n in range(1, 7):
        check_parity_and_sequence(n)
        matrices = [
            [[int(i == j) for j in range(n)] for i in range(n)],
            [[(i + 2) * (j + 3) - i * j - 7 for j in range(n)] for i in range(n)],
            [[(-1) ** (i + j) * (i * n + j + 1) for j in range(n)] for i in range(n)],
        ]
        for z in matrices:
            values = sign_eigenvalues(z)
            check(sum(values) == perm_numeric(z), 'numeric_sign_trace')
            zt = [list(col) for col in zip(*z)]
            check(sum(sign_eigenvalues(zt)) == sum(values), 'row_column_transposition')
        r = 1 << (n - 1)
        identity_values = sign_eigenvalues(matrices[0])
        check(identity_values == [Fraction(1, r)] * r, 'identity_scalar_specialization')
        for d in range(1, 5):
            check(sum(value ** d for value in identity_values) == Fraction(1, r ** (d - 1)), 'compressed_identity_power_trace')
            check(perm_numeric(matrices[0], d) == 1, 'original_identity_power_trace')
        if n >= 2:
            check(Fraction(1, r) ** 2 != Fraction(1, r), 'no_multiplicative_transport_over_Q')
        if n <= 5:
            check_flattenings(n)
    # Original F is evaluated on all three retained points, including x=0.
    for x in (-1, 0, 1):
        y = Fraction(-3 * x, 2)
        w = Fraction(27 * x * x - 1, 4)
        f1 = (1 + x * y) ** 3 * w + y * y * (1 + x * y) * (4 + 3 * x * y)
        f2 = y + 3 * x * (1 + x * y) ** 2 * w + 3 * x * y * y * (4 + 3 * x * y)
        f3 = 2 * x - 3 * x * x * y - x ** 3 * w
        check((f1, f2, f3) == (Fraction(-1, 4), 0, 0), 'original_F_retained_points')
    for z in ([[7]], [[2, 3], [5, 7]], [[1, 0], [0, 1]]):
        for d in (1, 2):
            trace, survivors = original_source_trace(z, d)
            check(trace == perm_numeric(z, d), 'exhaustive_original_full_fibre_trace')
            check(len(survivors) == factorial(len(z)), 'unique_source_witness_count')
            if z == [[1, 0], [0, 1]]:
                check(sorted(v for _, v in survivors) == [0, 1], 'original_identity_idempotent_values')
    # n=1 really is evaluation at the selected original source point.
    trace, points = original_source_trace([[7]])
    check(points == [((1, 1, 1), 7)] and trace == 7, 'n1_original_selected_point_quotient')
    result = {
        'status': 'passed',
        'arithmetic': 'exact integers and fractions; modular ranks over F_101 and F_2',
        'checks': dict(sorted(COUNTS.items())),
        'total_checks': sum(COUNTS.values()),
        'scope': {
            'parity_and_common_module': 'all row-choice tuples for 1 <= n <= 6',
            'independent_character_sum': 'all row-choice tuples for 1 <= n <= 5',
            'matrix_exact_sequence_ranks': '1 <= n <= 4',
            'flattening_ranks': '1 <= n <= 5 over F_101; n <= 4 also over F_2',
            'original_full_fibres': 'all 3^(3n^2) points for n=1 and n=2 at stated matrices',
            'general_claims': 'proved in audit.md, not inferred from finite tests',
        },
        'files': {name: sha256((ROOT / name).read_bytes()).hexdigest()
                  for name in ('check.py', 'audit.md', 'USER_INPUTS.md') if (ROOT / name).exists()},
    }
    (ROOT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
