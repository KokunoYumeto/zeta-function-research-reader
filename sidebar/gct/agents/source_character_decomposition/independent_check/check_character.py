"""Exact Jacobi--Trudi calculation; Python standard library only.

No semistandard tableaux are enumerated. The stored exponents (a,b) mean
x1**a*x2**(degree-a)*y1**b*y2**(degree-b), not a change of the original
GL(2) x GL(2) representation. Homogeneous degrees are retained explicitly.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import prod
from pathlib import Path
import json


SHAPE = (7, 5, 3, 0)
DEGREE = sum(SHAPE)


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def complete(k):
    """h_k(x1*y1,x1*y2,x2*y1,x2*y2), with exact multiplicities.

    Given a=n11+n12 and b=n11+n21, n11 ranges from max(0,a+b-k)
    to min(a,b), inclusive. Every monomial in h_k has coefficient one.
    """
    if k < 0:
        return {}
    return {
        (a, b): min(a, b) - max(0, a + b - k) + 1
        for a in range(k + 1)
        for b in range(k + 1)
        if min(a, b) >= max(0, a + b - k)
    }


def multiply(left, right):
    ans = defaultdict(int)
    for (a, b), coeff in left.items():
        for (c, d), other in right.items():
            ans[a + c, b + d] += coeff * other
    return dict(ans)


def determinant(matrix):
    return sum(sign(p) * prod(matrix[i][p[i]] for i in range(len(matrix))) for p in permutations(range(len(matrix))))


def calculate():
    # Last row of the 4x4 Jacobi--Trudi matrix is (0,0,0,1).
    # Thus this 3x3 minor preserves the full original partition (7,5,3,0).
    indices = [[SHAPE[i] - i + j for j in range(3)] for i in range(3)]
    assert indices == [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    h = {k: complete(k) for k in range(1, 10)}
    character = defaultdict(int)
    terms = []
    for p in permutations(range(3)):
        ks = [indices[i][p[i]] for i in range(3)]
        assert sum(ks) == DEGREE
        term = {(0, 0): 1}
        for k in ks:
            term = multiply(term, h[k])
        sg = sign(p)
        terms.append({"sign": sg, "complete_degrees": ks})
        for weight, coefficient in term.items():
            character[weight] += sg * coefficient
    character = {weight: value for weight, value in character.items() if value}
    assert all(value > 0 for value in character.values())
    assert all(3 <= a <= 12 and 3 <= b <= 12 for a, b in character)
    for a in range(16):
        for b in range(16):
            value = character.get((a, b), 0)
            assert value == character.get((15 - a, b), 0)
            assert value == character.get((a, 15 - b), 0)
            assert value == character.get((b, a), 0)

    def highest(a, b):
        return (character.get((a, b), 0) - character.get((a + 1, b), 0)
                - character.get((a, b + 1), 0) + character.get((a + 1, b + 1), 0))

    multiplicities = {(a, b): highest(a, b) for a in range(8, 16) for b in range(8, 16)}
    assert all(m >= 0 for m in multiplicities.values())
    assert all(m == 0 for (a, b), m in multiplicities.items() if a > 12 or b > 12)
    reconstruction = defaultdict(int)
    for (a, b), multiplicity in multiplicities.items():
        for i in range(15 - a, a + 1):
            for j in range(15 - b, b + 1):
                reconstruction[i, j] += multiplicity
    assert {weight: v for weight, v in reconstruction.items() if v} == character

    weyl_dimension = prod(Fraction(SHAPE[i] - SHAPE[j] + j - i, j - i)
                          for i in range(4) for j in range(i + 1, 4))
    irreducible_dimension = sum(m * (2 * a - 14) * (2 * b - 14)
                               for (a, b), m in multiplicities.items())
    assert weyl_dimension.denominator == 1
    assert weyl_dimension == sum(character.values()) == irreducible_dimension == 1260

    # Separate Weyl-alternant evaluation catches indexing/sign mistakes in JT.
    alternant_checks = []
    for x1, x2, y1, y2 in [(2, 3, 5, 7), (3, 5, 7, 11), (1, 2, 3, 7)]:
        z = (x1 * y1, x1 * y2, x2 * y1, x2 * y2)
        numerator = determinant([[zj ** (SHAPE[i] + 3 - i) for zj in z] for i in range(4)])
        denominator = determinant([[zj ** (3 - i) for zj in z] for i in range(4)])
        assert denominator != 0
        alternant = Fraction(numerator, denominator)
        expanded = sum(coeff * x1 ** a * x2 ** (15 - a) * y1 ** b * y2 ** (15 - b)
                       for (a, b), coeff in character.items())
        assert expanded == alternant
        alternant_checks.append({"x1_x2_y1_y2": [x1, x2, y1, y2], "value": expanded})

    return {
        "method": "Jacobi-Trudi determinant with exact complete-symmetric characters; no tableaux enumeration",
        "field": "characteristic zero; polynomial GL2 x GL2 modules",
        "shape": list(SHAPE),
        "degree": DEGREE,
        "jacobi_trudi_indices": indices,
        "jacobi_trudi_terms": terms,
        "dimension": int(weyl_dimension),
        "highest_weight_row_a": list(range(8, 13)),
        "highest_weight_column_b": list(range(8, 13)),
        "highest_weight_matrix": [[multiplicities[a, b] for b in range(8, 13)] for a in range(8, 13)],
        "irreducibles": [{"lambda": [a, 15 - a], "mu": [b, 15 - b], "multiplicity": m}
                         for (a, b), m in multiplicities.items() if m],
        "requested_weights": [{"weight": [a, 15 - a, b, 15 - b], "multiplicity": character.get((a, b), 0)}
                              for a, b in [(12, 9), (11, 9), (10, 9)]],
        "weight_row_a": list(range(16)),
        "weight_column_b": list(range(16)),
        "full_weight_matrix": [[character.get((a, b), 0) for b in range(16)] for a in range(16)],
        "validation": {"nonnegative_character": True, "three_symmetries": True,
                       "full_character_reconstruction": True, "three_dimension_methods": True,
                       "independent_weyl_alternant_evaluations": alternant_checks},
    }


if __name__ == "__main__":
    result = calculate()
    destination = Path(__file__).with_name("result.json")
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ["dimension", "highest_weight_matrix", "requested_weights"]}, indent=2))
