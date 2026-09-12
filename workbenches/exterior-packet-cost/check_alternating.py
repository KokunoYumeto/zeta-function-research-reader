"""Independent exact finite tests for the alternating packet review.

These fixtures verify algebraic identities, not an arithmetic upper estimate.
No source metric, representative, or coordinate is modified by this checker.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial
import json
import sys


class CheckFailure(RuntimeError):
    """A mathematical check failed, independently of Python optimization."""


def require(condition, label):
    if not condition:
        raise CheckFailure(label)


def sign(seq):
    return (-1) ** sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))


def determinant(matrix):
    size = len(matrix)
    if not size:
        return Fraction(1)
    work = [[Fraction(v) for v in row] for row in matrix]
    answer = Fraction(1)
    for col in range(size):
        pivot = next((r for r in range(col, size) if work[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[pivot], work[col] = work[col], work[pivot]
            answer *= -1
        leading = work[col][col]
        answer *= leading
        for j in range(col, size):
            work[col][j] /= leading
        for r in range(col + 1, size):
            factor = work[r][col]
            for j in range(col, size):
                work[r][j] -= factor * work[col][j]
    return answer


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def additive_action(vector, d, a):
    out = {}
    for tensor, value in vector.items():
        for pos, old in enumerate(tensor):
            for new in range(d):
                target = tensor[:pos] + (new,) + tensor[pos + 1:]
                out[target] = out.get(target, 0) + value * a[new][old]
    return {key: value for key, value in out.items() if value}


def orbit(j):
    return {p: sign(p) for p in permutations(j)}


counts = {"moments": 0, "nilpotent_blocks": 0, "factorial_minors": 0,
          "additive_orbit_columns": 0, "gram_inverse_cases": 0,
          "layer_dimensions": 0, "surviving_nilpotent_capacity_cases": 0}

# Exact subset moments, including d=1, k=1, k=d, and rational offsets.
for d in range(1, 10):
    for delta in ([Fraction((i * i + 3 * i) % 11 - 5, 7) for i in range(d)],
                  [Fraction(2, 3)] * d,
                  [Fraction(2 * i - d + 1, 5) for i in range(d)]):
        s1, s2 = sum(delta), sum(v * v for v in delta)
        for k in range(1, d + 1):
            values = [sum(delta[i] for i in j) for j in combinations(range(d), k)]
            require(len(values) == comb(d, k), f"subset count d={d}, k={k}")
            require(sum(values) == comb(d - 1, k - 1) * s1, f"first moment d={d}, k={k}, delta={delta}")
            expected = s2 if d == 1 else choose(d - 2, k - 1) * s2 + choose(d - 2, k - 2) * s1 * s1
            require(sum(v * v for v in values) == expected, f"second moment d={d}, k={k}, delta={delta}")
            if d > 1:
                centered = sum((v - Fraction(k, d) * s1) ** 2 for v in values)
                require(centered == Fraction(comb(d, k) * k * (d - k), d * (d - 1)) * (s2 - s1 * s1 / d), f"centered moment d={d}, k={k}, delta={delta}")
            counts["moments"] += 1

# Every local coefficient is formed in the original monomial-wedge basis.
for m in range(1, 11):
    for r in range(m + 1):
        bottom, top = tuple(range(r)), tuple(range(m - r, m))
        h = r * (m - r)
        vector = {bottom: 1}
        for _ in range(h):
            out = {}
            for j, value in vector.items():
                for slot, old in enumerate(j):
                    new = old + 1
                    if new >= m or new in j:
                        continue
                    target = j[:slot] + (new,) + j[slot + 1:]
                    require(tuple(sorted(target)) == target, f"local nilpotent target ordering m={m}, r={r}, target={target}")
                    out[target] = out.get(target, 0) + value
            vector = out
        coefficient = Fraction(factorial(h))
        for j in range(r):
            coefficient *= Fraction(factorial(j), factorial(m - r + j))
        require(coefficient.denominator == 1, f"integral nilpotent top coefficient m={m}, r={r}")
        require(vector == {top: coefficient.numerator}, f"exact nilpotent top transition m={m}, r={r}")
        require(all(a == m - r + p for p, a in enumerate(top)), f"nilpotent top exponent list m={m}, r={r}")
        minor = determinant([[Fraction(1, factorial(m - r + i - j)) if m - r + i - j >= 0 else 0 for j in range(r)] for i in range(r)])
        require(factorial(h) * minor == coefficient, f"factorial minor m={m}, r={r}")
        counts["nilpotent_blocks"] += 1
        counts["factorial_minors"] += 1

# Tensor-additive action against the signed replacement formula with no scaling.
for d in range(1, 5):
    a = [[(2 * i + 3 * j + 1) % 7 - 3 for j in range(d)] for i in range(d)]
    for k in range(1, d + 1):
        for j in combinations(range(d), k):
            expected = {}
            diagonal = sum(a[p][p] for p in j)
            for tensor, value in orbit(j).items():
                expected[tensor] = expected.get(tensor, 0) + diagonal * value
            for old in j:
                for new in range(d):
                    if new in j:
                        continue
                    replaced = tuple(new if v == old else v for v in j)
                    target = tuple(sorted(replaced))
                    coefficient = a[new][old] * sign(replaced)
                    for tensor, value in orbit(target).items():
                        expected[tensor] = expected.get(tensor, 0) + coefficient * value
            expected = {key: value for key, value in expected.items() if value}
            require(additive_action(orbit(j), d, a) == expected, f"additive orbit intertwining d={d}, k={k}, J={j}")
            counts["additive_orbit_columns"] += 1

# A nontrivial commuting positive Gram fixture B^(tensor k).
# Restricted unscaled Gram is k! times the matrix of B-minors;
# L G^-1 L* is 1/k! times the matrix of inverse-B minors.
for d in range(1, 7):
    u = list(range(1, d + 1))
    denom = 1 + sum(v * v for v in u)
    b = [[Fraction(int(i == j) + u[i] * u[j]) for j in range(d)] for i in range(d)]
    binv = [[Fraction(int(i == j)) - Fraction(u[i] * u[j], denom) for j in range(d)] for i in range(d)]
    for k in range(1, d + 1):
        basis = list(combinations(range(d), k))
        gram = [[factorial(k) * determinant([[b[i][j] for j in col] for i in row]) for col in basis] for row in basis]
        inverse = [[Fraction(1, factorial(k)) * determinant([[binv[i][j] for j in col] for i in row]) for col in basis] for row in basis]
        for i in range(len(basis)):
            for j in range(len(basis)):
                require(sum(gram[i][p] * inverse[p][j] for p in range(len(basis))) == int(i == j), f"commuting Gram inverse d={d}, k={k}, entry=({i},{j})")
        counts["gram_inverse_cases"] += 1


def weak_tuples(length, total, minimum=0):
    if length == 0:
        yield from [()] if total == 0 else []
        return
    for first in range(minimum, total // length + 1):
        for rest in weak_tuples(length - 1, total - first, first):
            yield (first,) + rest


for k in range(1, 8):
    shift = k * (k - 1) // 2
    for n in range(21):
        partitions = list(weak_tuples(k, n - shift)) if n >= shift else []
        strict = [j for j in combinations(range(n + 1), k) if sum(j) == n]
        require([(tuple(v + i for i, v in enumerate(p))) for p in partitions] == strict, f"alternating degree layer k={k}, degree={n}")
        counts["layer_dimensions"] += 1

# Show any repeated-root block is detected by some proper exterior degree.
for d in range(2, 30):
    for m in range(2, d + 1):
        for k in range(1, d):
            lower, upper = max(1, k - (d - m)), min(m - 1, k)
            require(lower <= upper, f"nonempty proper nilpotent occupancy interval d={d}, m={m}, k={k}")
            require(0 <= k - lower <= d - m, f"remaining sector capacity d={d}, m={m}, k={k}")
            require(lower * (m - lower) > 0, f"surviving proper nilpotent d={d}, m={m}, k={k}")
            counts["surviving_nilpotent_capacity_cases"] += 1

# These deliberately false identities must be rejected by the same check
# mechanism in ordinary and optimized Python. Catch only CheckFailure, so a
# programming error cannot be mistaken for a successful negative control.
negative_controls_rejected = []


def require_rejected(label, false_identity):
    try:
        require(false_identity, label)
    except CheckFailure:
        negative_controls_rejected.append(label)
    else:
        raise CheckFailure(f"Negative control was incorrectly accepted: {label}")


# d=k=2, G=id: I*GI=2, but dropping both 1/k! factors in L
# proposes I*G^-1 I=2 as its inverse and gives product 4, not 1.
negative_k = 2
restricted_identity_gram = Fraction(factorial(negative_k))
bad_inverse_without_factors = Fraction(factorial(negative_k))
require_rejected("omitted orbit factorial in inverse compression",
                 restricted_identity_gram * bad_inverse_without_factors == 1)

# d=4, k=2, delta=(1,0,0,0) has second moment 3. Substituting
# alpha for beta produces 4; this is a genuinely distinguishable fixture.
negative_delta = [1, 0, 0, 0]
observed_second = sum(sum(negative_delta[i] for i in j) ** 2 for j in combinations(range(4), 2))
bad_second = comb(3, 1) * sum(v * v for v in negative_delta) + comb(2, 0) * sum(negative_delta) ** 2
require(observed_second == 3 and bad_second == 4, "negative subset fixture values")
require_rejected("wrong subset second-moment coefficient", observed_second == bad_second)

# Compute the actual nilpotent index on every basis vector for m=4, r=2.
# The tensor/symmetric height r(m-1) would predict index 7, while the
# exterior operator dies first at power 5.
negative_m, negative_r = 4, 2
negative_n = [[int(i == j + 1) for j in range(negative_m)] for i in range(negative_m)]
negative_columns = [orbit(j) for j in combinations(range(negative_m), negative_r)]
observed_nilpotent_index = 0
while any(negative_columns):
    negative_columns = [additive_action(v, negative_m, negative_n) for v in negative_columns]
    observed_nilpotent_index += 1
    require(observed_nilpotent_index <= 10, "negative nilpotent fixture terminates")
require(observed_nilpotent_index == 5, "negative nilpotent fixture exact observed index")
require_rejected("tensor-height index incorrectly used for exterior nilpotent",
                 observed_nilpotent_index == negative_r * (negative_m - 1) + 1)

# In basis (00,01,10,11), G=diag(1,2,3,4)>0 fails to commute with
# the two-slot permutation. I=(0,1,-1,0)^T gives restricted Gram 5;
# L G^-1 L*=5/24, whereas the true inverse is 1/5.
noninvariant_diagonal = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
negative_orbit_column = [Fraction(0), Fraction(1), Fraction(-1), Fraction(0)]
restricted_noninvariant_gram = sum(v * v * g for v, g in zip(negative_orbit_column, noninvariant_diagonal))
bad_noninvariant_inverse = sum((v / 2) ** 2 / g for v, g in zip(negative_orbit_column, noninvariant_diagonal))
require(noninvariant_diagonal[1] != noninvariant_diagonal[2], "noninvariant Gram fixture fails permutation commutation")
require(restricted_noninvariant_gram == 5 and bad_noninvariant_inverse == Fraction(5, 24), "noninvariant Gram fixture exact values")
require_rejected("inverse compression wrongly extended to noninvariant Gram",
                 restricted_noninvariant_gram * bad_noninvariant_inverse == 1)
require(len(negative_controls_rejected) == 4, "all four negative controls rejected")

print(json.dumps({"status": "passed", "python_optimization": sys.flags.optimize,
                  "counts": counts, "total_exact_cases": sum(counts.values()),
                  "negative_controls_rejected": negative_controls_rejected,
                  "negative_control_count": len(negative_controls_rejected)}, indent=2))
