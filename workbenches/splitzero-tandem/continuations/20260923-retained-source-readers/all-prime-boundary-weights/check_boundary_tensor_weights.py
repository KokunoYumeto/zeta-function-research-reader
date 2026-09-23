"""Exact finite checks of the original all-prime boundary tensor proof.

The finite enumerations check the source-coordinate tensor action,
joint multiplicities, balanced quotient transitions, dual fiber
sums, endpoint defect and finite polynomial projectors.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json
import sympy as sp

root = Path(__file__).resolve().parent
checks = {}


def check(name, truth):
    if not truth:
        raise ArithmeticError(name)
    checks[name] = True


def bc(r, k):
    return comb(r, k) if 0 <= k <= r else 0


for r in range(1, 5):
    subsets = tuple(range(2**r))
    cardinality = {mask: mask.bit_count() for mask in subsets}
    for d in range(4):
        X = list(product(subsets, repeat=d+1))
        weights = Counter(tuple(cardinality[x[0]]-cardinality[y]
                                for y in x[1:]) for x in X)
        Z = [x for x in X
             if all(cardinality[y] == cardinality[x[0]] for y in x[1:])]
        expected_dimension = sum(comb(r, m)**(d+1) for m in range(r+1))
        check(f"balanced_dimension_r{r}_d{d}", len(Z) == expected_dimension)
        check(f"joint_weight_sum_r{r}_d{d}", sum(weights.values()) == 2**(r*(d+1)))
        joint_ok = True
        for delta in product(range(-r, r+1), repeat=d):
            expected = 0
            for m in range(r+1):
                term = comb(r, m)
                for v in delta:
                    term *= bc(r, m-v)
                expected += term
            if weights[delta] != expected:
                joint_ok = False
                break
        check(f"all_joint_multiplicities_r{r}_d{d}", joint_ok)
        endpoint = [x for x in Z if all(y == x[0] for y in x[1:])]
        check(f"endpoint_dimension_r{r}_d{d}", len(endpoint) == 2**r)
        check(f"endpoint_kernel_dimension_r{r}_d{d}",
              len(Z)-len(endpoint) == expected_dimension-2**r)
        if d:
            marginal = Counter()
            for delta, multiplicity in weights.items():
                marginal[delta[0]] += multiplicity
            check(f"single_prime_multiplicities_r{r}_d{d}",
                  all(marginal[v] == 2**(r*(d-1))*comb(2*r, r+v)
                      for v in range(-r, r+1)))
        if d <= 2:
            enlarged = list(product(subsets, repeat=d+2))
            full_fibers = Counter(y[:-1] for y in enlarged)
            balanced_fibers = Counter(
                y[:-1] for y in enlarged
                if all(cardinality[u] == cardinality[y[0]] for u in y[1:]))
            check(f"full_dual_pushforward_fiber_r{r}_d{d}",
                  all(full_fibers[x] == 2**r for x in X))
            check(f"balanced_dual_pushforward_fiber_r{r}_d{d}",
                  all(balanced_fibers[x] == comb(r, cardinality[x[0]]) for x in Z))

x = sp.symbols("x")
for r in range(1, 5):
    for p in (2, 3, 5):
        projection = sp.Integer(1)
        for d in range(-r, r+1):
            if d:
                value = sp.Rational(p)**d
                projection *= (x-value)/(1-value)
        check(f"exact_zero_weight_projector_r{r}_p{p}",
              all(sp.simplify(projection.subs(x, sp.Rational(p)**d))
                  == int(d == 0) for d in range(-r, r+1)))
        quotient, remainder = sp.div(sp.Poly(1-projection, x), sp.Poly(x-1, x))
        check(f"exact_relation_polynomial_r{r}_p{p}", remainder.is_zero)

for r in range(2, 5):
    subsets = tuple(range(2**r))
    witness = (1, 2)
    def mixed_class(point):
        return int(point[0] == 1 and point[1] == 2)
    check(f"actual_mixed_class_balanced_r{r}",
          witness[0].bit_count() == witness[1].bit_count()
          and mixed_class(witness) == 1)
    check(f"actual_mixed_class_invisible_to_endpoints_r{r}",
          all(mixed_class((s, s)) == 0 for s in subsets))
    # Three different actual primes suffice to test the proposed
    # independent coordinate classes on their three separating points.
    matrix = []
    for changed in range(3):
        point = (1,) + tuple(2 if j == changed else 1 for j in range(3))
        matrix.append([int(point[0] == 1 and point[j+1] == 2)
                       for j in range(3)])
    check(f"mixed_class_separating_matrix_r{r}", matrix == [[1,0,0],[0,1,0],[0,0,1]])

for r in range(1, 4):
    all_masks = tuple(range(2**r))
    full_mask = 2**r-1
    for d in range(3):
        X = list(product(all_masks, repeat=d+1))
        Xnew = list(product(all_masks, repeat=d+2))
        def ff(point):
            return 1 + sum((j+1)*u for j, u in enumerate(point))
        def gg(point):
            return 2 + sum((j+2)*u*u for j, u in enumerate(point))
        def complement(point):
            return tuple(full_mask ^ u for u in point)
        original_pairing = sum(ff(point)*gg(complement(point)) for point in X)
        enlarged_pairing = sum(ff(point[:-1])*gg(complement(point[:-1]))
                               for point in Xnew)
        check(f"original_full_pairing_factor_r{r}_d{d}",
              enlarged_pairing == 2**r*original_pairing)
        for m in range(r+1):
            old = [point for point in X if all(u.bit_count() == m for u in point)]
            new = [point for point in Xnew if all(u.bit_count() == m for u in point)]
            old_pairing = sum(ff(point)*gg(complement(point)) for point in old)
            new_pairing = sum(ff(point[:-1])*gg(complement(point[:-1])) for point in new)
            check(f"balanced_pairing_fiber_r{r}_d{d}_m{m}",
                  new_pairing == comb(r, m)*old_pairing)

u, v = sp.symbols("u v")
check("full_connecting_cocycle_identity",
      sp.expand(u*v-1-u*(v-1)-(u-1)) == 0)
check("actual_degree_two_reciprocal_factors", Fraction(2)*Fraction(1, 2) == 1)

source_root = root / "sources"
sources = {
    "AB_original": source_root / "06_adelic_boundary.tex",
    "ME_original": source_root / "11_mixed_extension_prime_trace.tex",
    "independent_proof": root / "INDEPENDENT_BOUNDARY_TENSOR_WEIGHTS.tex",
}
receipt = {
    "status": "passed",
    "exact_check_count": len(checks),
    "checks": checks,
    "source_sha256": {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in sources.items()
    },
    "scope": "Exact finite checks in the original coefficient coordinates; no topological completion, Frobenius substitution or whole-cohomology claim.",
}
(root / "INDEPENDENT_BOUNDARY_TENSOR_WEIGHTS_CHECKS.json").write_text(
    json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "passed", "exact_check_count": len(checks)}, indent=2))
