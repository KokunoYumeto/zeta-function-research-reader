"""Exact finite audits for the fully proved sign-algebra/source correspondence.

No network access, external shelves, or generated mathematical inputs are used.
Finite checks complement the general proofs; they do not certify an unrestricted
complexity separation.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import random
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = 0
families: dict[str, int] = {}


def require(condition: bool, family: str, context: object = None) -> None:
    global checks
    if not condition:
        raise AssertionError((family, context))
    checks += 1
    families[family] = families.get(family, 0) + 1


def mask_of_tuple(t: tuple[int, ...]) -> int:
    result = 0
    for j in t:
        if j:
            result ^= 1 << (j - 1)
    return result


def group_multiply(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)] * len(a)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i ^ j] += ai * bj
    return out


def multiplier(z: list[list[int]]) -> list[F]:
    n = len(z)
    r = 1 << (n - 1)
    a = [F(0)] * r
    a[r - 1] = F(1, r)
    for row in z:
        b = [F(0)] * r
        for j, entry in enumerate(row):
            b[0 if j == 0 else 1 << (j - 1)] += entry
        a = group_multiply(a, b)
    return a


def permanent(z: list[list[int]]) -> int:
    result = 0
    for pi in permutations(range(len(z))):
        v = 1
        for i, j in enumerate(pi):
            v *= z[i][j]
        result += v
    return result


def signs(n: int):
    for tail in product((-1, 1), repeat=n - 1):
        yield (1,) + tail


def sign_value(z: list[list[int]], delta: tuple[int, ...]) -> F:
    n = len(z)
    value = F(1, 1 << (n - 1))
    for d in delta:
        value *= d
    for row in z:
        value *= sum(d * a for d, a in zip(delta, row))
    return value


def flagged_point(pi: tuple[int, ...]) -> tuple[int, ...]:
    n = len(pi)
    matrix = [[int(pi[i] == j) for j in range(n)] for i in range(n)]
    rows = [[int(any(matrix[i][:k + 1])) for k in range(n)] for i in range(n)]
    columns = [[int(any(matrix[i][j] for i in range(k + 1)))
                for k in range(n)] for j in range(n)]
    bits = [v for group in (matrix, rows, columns) for row in group for v in row]
    return tuple(2 * b - 1 for b in bits)


# Coefficient-by-coefficient parity proof and both common maps, all tuples.
for n in range(1, 7):
    r = 1 << (n - 1)
    full = r - 1
    pcounts = Counter()
    nonpermutation_masks = set()
    for tup in product(range(n), repeat=n):
        pmask = mask_of_tuple(tup)
        kmask = full ^ pmask
        pcounts[pmask] += 1
        is_perm = len(set(tup)) == n
        require((kmask == 0) == is_perm, 'all_tuple_trace_square', (n, tup))
        if not is_perm:
            nonpermutation_masks.add(kmask)
    require(len(pcounts) == r, 'K_surjection', n)
    require(nonpermutation_masks == set(range(1, r)), 'K_kernelS_trace_kernel', n)
    require(pcounts[full] == factorial(n), 'permutation_parity_fibre', n)
    require(sum(v - 1 for k, v in pcounts.items() if k != full)
            == n ** n - factorial(n) - r + 1, 'joint_kernel_rank', n)
    for mask in range(r):
        selected = tuple(j for j in range(1, n) if mask & (1 << (j - 1)))
        representative = selected + (0,) * (n - len(selected))
        require(mask_of_tuple(representative) == mask, 'explicit_K_section', (n, mask))

# Original source coordinates, with boundary retained, computed as exact rationals.
for x in (F(-1), F(0), F(1)):
    y, w = -3 * x / 2, (27 * x * x - 1) / 4
    fs = ((1 + x*y)**3*w + y*y*(1+x*y)*(4+3*x*y),
          y + 3*x*(1+x*y)**2*w + 3*x*y*y*(4+3*x*y),
          2*x - 3*x*x*y - x**3*w)
    require(fs == (F(-1, 4), F(0), F(0)), 'original_F_source_points', (x, y, w))
    e = ((x*x-x)/2, 1-x*x, (x*x+x)/2)
    require(e == tuple(F(int(i == int(x)+1)) for i in range(3)),
            'original_source_idempotents', x)
for n in range(1, 7):
    points = {flagged_point(pi) for pi in permutations(range(n))}
    require(len(points) == factorial(n), 'source_flag_unique_points', n)
    require(all(len(p) == 3*n*n and set(p) <= {-1, 1} for p in points),
            'source_flag_coordinate_count', n)

# Full regular multiplication matrices and split sign sums, independently compared
# with permutation enumeration and with transposed input matrices.
rng = random.Random(20260908)
for n in range(1, 7):
    r = 1 << (n - 1)
    cases = [[[int(i == j) for j in range(n)] for i in range(n)],
             [[1] * n for _ in range(n)],
             [[0] * n for _ in range(n)]]
    cases += [[[rng.randrange(-3, 4) for _ in range(n)] for _ in range(n)]
              for _ in range(4)]
    for z in cases:
        v = multiplier(z)
        expected = permanent(z)
        diagonal = [v[col ^ col] for col in range(r)]
        require(sum(diagonal) == expected, 'regular_matrix_trace', (n, z))
        eigenvalues = [sign_value(z, d) for d in signs(n)]
        require(sum(eigenvalues) == expected, 'split_trace', (n, z))
        require(sum(sign_value([list(row) for row in zip(*z)], d) for d in signs(n))
                == expected, 'column_orientation_transpose', (n, z))
        squared = group_multiply(v, v)
        require(r * squared[0] == sum(q*q for q in eigenvalues),
                'power_trace_two', (n, z))
        for prime in (3, 5, 7, 11):
            def mod_fraction(v: F) -> int:
                return v.numerator * pow(v.denominator, -1, prime) % prime
            require(sum(mod_fraction(a) for a in eigenvalues) % prime == expected % prime,
                    'odd_characteristic_trace', (n, prime, z))
    vi = multiplier(cases[0])
    require(vi == [F(1, r)] + [F(0)] * (r-1), 'identity_multiplier', n)
    require(sum(sign_value(cases[0], d)**2 for d in signs(n)) == F(1, r),
            'identity_second_trace', n)
    require((F(1, r)**2 == F(1, r)) == (n == 1), 'rational_idempotent_obstruction', n)

# Integral Hadamard evaluation lattice and trace-zero character orthogonality.
for n in range(1, 7):
    r = 1 << (n - 1)
    H = []
    for delta in signs(n):
        row = []
        for mask in range(r):
            a = 1
            for j in range(1, n):
                if mask & (1 << (j-1)):
                    a *= delta[j]
            row.append(a)
        H.append(row)
    for i in range(r):
        for j in range(r):
            require(sum(row[i]*row[j] for row in H) == r*int(i == j),
                    'integral_character_orthogonality', (n, i, j))
    if n >= 2:
        require(all(a % r != 0 for a in H[0]), 'integral_lattice_not_surjective', n)

# Exact common-tensor matrix ranks, independently using rational elimination.
for n in range(1, 5):
    r = 1 << (n - 1)
    tuples = list(product(range(n), repeat=n))
    pis = list(permutations(range(n)))
    index = {p: i for i, p in enumerate(pis)}
    S = sp.zeros(len(pis), len(tuples))
    K = sp.zeros(r, len(tuples))
    for j, t in enumerate(tuples):
        if t in index:
            S[index[t], j] = 1
        K[(r - 1) ^ mask_of_tuple(t), j] = sp.Rational(1, r)
    joint = S.col_join(-K)
    trace = sp.ones(1, len(pis)).row_join(sp.Matrix([[r]+[0]*(r-1)]))
    require(S.rank() == factorial(n), 'matrix_S_rank', n)
    require(K.rank() == r, 'matrix_K_rank', n)
    require(trace * joint == sp.zeros(1, len(tuples)), 'matrix_exact_composite', n)
    require(joint.rank() == factorial(n) + r - 1, 'matrix_exact_image_rank', n)
    if n >= 2:
        repeated = tuples.index((0,)*n)
        require(S[:, repeated] == sp.zeros(len(pis), 1) and K[:, repeated] != sp.zeros(r, 1),
                'K_does_not_factor_S', n)
        require(K[:, tuples.index(pis[0])] == K[:, tuples.index(pis[1])]
                and S[:, tuples.index(pis[0])] != S[:, tuples.index(pis[1])],
                'S_does_not_factor_K', n)

# Fixed noncommutative algebra D=Mat_2(Q): regular trace by a genuine
# 4x4 multiplication matrix, plus explicit row-contraction factorization.
basis = [sp.Matrix([[int((i,j) == (a,b)) for j in range(2)] for i in range(2)])
         for a in range(2) for b in range(2)]


def regular_trace_matrix2(x: sp.Matrix) -> sp.Expr:
    cols = [sp.Matrix(list(x * e)) for e in basis]
    return sp.Matrix.hstack(*cols).trace()


for n in range(1, 5):
    aa = [[sp.Matrix([[rng.randrange(-2, 3) for _ in range(2)] for _ in range(2)])
           for _ in range(n)] for _ in range(n)]
    c = sp.Matrix([[2, -1], [3, 1]])
    for cut in range(n + 1):
        heads = list(product(range(n), repeat=cut))
        tails = list(product(range(n), repeat=n-cut))
        prefixes = []
        for h in heads:
            x = sp.eye(2)
            for i, j in enumerate(h):
                x = x * aa[i][j]
            prefixes.append(x)
        suffixes = []
        for t in tails:
            x = sp.eye(2)
            for i, j in enumerate(t, cut):
                x = x * aa[i][j]
            suffixes.append(x)
        contraction = sp.Matrix([[regular_trace_matrix2(c*x*y) for y in suffixes]
                                 for x in prefixes])
        left = sp.Matrix([list(x) for x in prefixes])
        right = sp.Matrix([[regular_trace_matrix2(c*e*y) for y in suffixes] for e in basis])
        require(contraction == left*right, 'noncommutative_cut_factorization', (n, cut))
        require(contraction.rank() <= 4, 'noncommutative_cut_rank', (n, cut))

# Exact numerical sizes, including the endpoints n=1 and n=2.
for n in range(1, 51):
    require(comb(n, n//2) <= 2**(n-1), 'sign_dimension_upper_vs_lower', n)
    require((n+1)*comb(n, n//2) >= 2**n, 'exponential_middle_binomial', n)
    require(2**(n-1) < 3**(3*n*n), 'compressed_vs_original_rank', n)

out = {'status': 'passed', 'checks': checks, 'families': families,
       'proof_sha256': hashlib.sha256((ROOT/'compressed_permanent_trace.tex').read_bytes()).hexdigest(),
       'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope': 'Exact finite audits supplement general proofs of sign trace, common tensor maps, '
                'integral lattice and specialization, algebra obstruction, and fixed-algebra row rank. '
                'No unrestricted complexity separation is certified.'}
(ROOT/'verification.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, indent=2))
