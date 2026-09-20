"""Independent exact audit of MR11--MR23 finite receiver algebra.

The coefficient frames and six-node moments are declared test fixtures,
not arithmetic period samples or replacements of the original source.
"""

from itertools import combinations, product
from math import factorial
import json
import sympy as sp
import check_identities as base

I, S = sp.I, base.S


def receiver(name, roots, pi, Z, ds):
    q, m, r = len(roots), pi.rows, Z.cols
    base.check(name + ": rank partition", m + r, q)
    base.check(name + ": bilinear frame annihilation", pi * Z, sp.zeros(m, r))
    U = pi.T
    base.check(name + ": complementary Euclidean frame", U.conjugate().T * Z.conjugate(),
               sp.zeros(m, r))
    g = base.det(pi.conjugate() * pi.T) / base.det(Z.T * Z.conjugate())
    full_roots = tuple((v, 1) for v in roots)
    full_vander = base.vander(full_roots)
    full_chi = base.poly(full_roots)
    subsets = list(combinations(range(q), r))
    values = []
    for d in ds:
        t, n = d - r, d - q
        H = base.source_gram(d)
        E = base.jets(full_roots, d)
        C = (E * H.inv() * E.conjugate().T).applyfunc(base.scalar)
        actual = base.det(pi.conjugate() * C.inv() * pi.T)
        complement = base.det(Z.T * C * Z.conjugate())
        base.check(f"{name} d={d}: complementary determinant", actual,
                   g * complement / base.det(C))
        A = 0
        coefficients = {}
        polynomials = {}
        for subset in subsets:
            subset_roots = tuple(full_roots[j] for j in subset)
            z = base.det(Z.extract(subset, range(r)))
            coefficients[subset] = z * base.vander(subset_roots)
            polynomials[subset] = base.poly(subset_roots)
        for left, right in product(subsets, repeat=2):
            Tl = base.multiplication(polynomials[left], t, d)
            Tr = base.multiplication(polynomials[right], t, d)
            B = base.det(Tr.conjugate().T * H * Tl)
            A += coefficients[left] * sp.conjugate(coefficients[right]) * B
        A = base.scalar(A)
        base.check(f"{name} d={d}: full mixed relation sum", A,
                   base.det(H) * complement)
        Tfull = base.multiplication(full_chi, n, d)
        Bfull = base.det(Tfull.conjugate().T * H * Tfull)
        base.check(f"{name} d={d}: MR18 ratio", actual,
                   g * A / (full_vander * sp.conjugate(full_vander) * Bfull))
        base.check(f"{name} d={d}: numerator degree", t, n + m)
        if d == q:
            integral = 0
            for labels in product(range(len(base.NODES)), repeat=t):
                zs = [base.C + I * base.NODES[j] for j in labels]
                delta = sp.prod(zs[b] - zs[a] for a in range(t) for b in range(a + 1, t))
                phi = sum(coefficients[subset] * sp.prod(
                    polynomials[subset].subs(S, z) for z in zs) for subset in subsets)
                amplitude = base.scalar(delta * phi)
                integral += sp.prod(base.WEIGHTS[j] for j in labels) * amplitude * sp.conjugate(amplitude)
            base.check(name + ": MR20 full integral", A, integral / factorial(t))
        a = sp.Rational(7, 3)
        base.check(f"{name} d={d}: mass determinant exponent",
                   base.det(pi.conjugate() * (C/a).inv() * pi.T), a ** m * actual)
        values.append((actual, A, Bfull))
    if len(values) == 4:
        left = values[0][0] * values[1][0] / (values[2][0] * values[3][0])
        numerator = values[0][1] * values[1][1] / (values[2][1] * values[3][1])
        denominator = values[0][2] * values[1][2] / (values[2][2] * values[3][2])
        base.check(name + ": MR19 exact four-return cancellation", left, numerator / denominator)
    return [str(x[0]) for x in values]


def main():
    records = {}
    records["q2_m1_r1"] = receiver(
        "q2_m1_r1", (1 + I, 2 - I), sp.Matrix([[1, I]]),
        sp.Matrix([[-I], [1]]), (2, 3, 4, 5))
    records["q3_m2_r1"] = receiver(
        "q3_m2_r1", (1 + I, -1 + 2*I, 2 - I),
        sp.Matrix([[1, I, 2], [0, 1, 1 - I]]),
        sp.Matrix([[-1 + I], [-1 + I], [1]]), (3,))
    records["q3_m1_r2"] = receiver(
        "q3_m1_r2", (1 + I, -1 + 2*I, 2 - I),
        sp.Matrix([[1, I, 2]]), sp.Matrix([[-I, -2], [1, 0], [0, 1]]), (3,))
    print(json.dumps({"status": "passed", "exact_check_count": len(base.CHECKS),
                      "checks": base.CHECKS, "restriction_determinants": records,
                      "fixture_role": "Finite algebra only; not actual period data"}, indent=2))


if __name__ == "__main__":
    main()
