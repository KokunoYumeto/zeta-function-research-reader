"""Exact finite algebra checks, not a replacement for the arithmetic source.

Run with Python and SymPy. --negative-control deliberately corrupts one
identity and must exit with failure in both normal and optimized Python.
The program uses explicit checks, never Python assert statements.
"""

from itertools import product
from math import factorial
import argparse
import json
import sympy as sp

I = sp.I
S, U, V, WBAR = sp.symbols("S U V WBAR")
C = sp.Rational(3, 2)
NODES = tuple(map(sp.Integer, (-2, -1, 0, 1, 2, 3)))
WEIGHTS = tuple(map(sp.Integer, (1, 2, 3, 4, 5, 6)))
CHECKS = []


def scalar(value):
    return sp.cancel(sp.expand_complex(value))


def check(name, actual, expected):
    difference = actual - expected
    if isinstance(difference, sp.MatrixBase):
        valid = all(scalar(x) == 0 for x in difference)
    else:
        valid = scalar(difference) == 0
    if not valid:
        raise RuntimeError(f"FAILED: {name}; difference={difference}")
    CHECKS.append(name)


def det(matrix):
    return scalar(matrix.det())


def conj(value):
    return sp.conjugate(value)


def poly(roots, variable=S):
    return sp.expand(sp.prod((variable - v) ** m for v, m in roots))


def degree(roots):
    return sum(m for _, m in roots)


def vander(roots):
    return sp.prod(
        (roots[b][0] - roots[a][0]) ** (roots[a][1] * roots[b][1])
        for a in range(len(roots)) for b in range(a + 1, len(roots))
    )


def source_gram(d, coordinate="S", scale=1):
    zs = tuple(C + I * x for x in NODES) if coordinate == "S" else NODES
    return sp.Matrix(d, d, lambda r, j: scalar(sum(
        scale * w * conj(z) ** r * z ** j for z, w in zip(zs, WEIGHTS)
    )))


def jets(roots, d):
    rows = [(v, r) for v, m in roots for r in range(m)]
    return sp.Matrix(len(rows), d, lambda row, j:
        sp.binomial(j, rows[row][1]) * rows[row][0] ** (j - rows[row][1])
        if j >= rows[row][1] else 0)


def multiplication(p, n, d, variable=S):
    return sp.Matrix(d, n, lambda j, r:
        sp.Poly(sp.expand(p * variable ** r), variable).nth(j))


def monic_orthogonals(H):
    d = H.rows
    vectors, norms = [], []
    for j in range(d):
        x = sp.zeros(d, 1)
        x[j] = 1
        for previous, norm in zip(vectors, norms):
            x -= previous * scalar((previous.conjugate().T * H * x)[0] / norm)
            x = x.applyfunc(scalar)
        norm = scalar((x.conjugate().T * H * x)[0])
        if not (norm.is_positive is True):
            raise RuntimeError("Source fixture lost positive norm")
        vectors.append(x)
        norms.append(norm)
    return vectors, norms


def coordinate_matrix(d):
    return sp.Matrix(d, d, lambda r, j:
        sp.binomial(j, r) * C ** (j - r) * I ** r if r <= j else 0)


def check_case(name, n, roots_chi, roots_psi, integrate=False):
    q = degree(roots_chi)
    if degree(roots_psi) != q:
        raise RuntimeError("Checker requires equal degrees")
    d = n + q
    chi, psi = poly(roots_chi), poly(roots_psi)
    H = source_gram(d)
    Hinv = H.inv() if d else sp.zeros(0, 0)
    Echi, Epsi = jets(roots_chi, d), jets(roots_psi, d)
    Tchi, Tpsi = multiplication(chi, n, d), multiplication(psi, n, d)
    cross = (Tpsi.conjugate().T * H * Tchi).applyfunc(scalar)
    displayed = sp.Matrix(n, n, lambda r, j: scalar(sum(
        weight * (C + I*x)**r * chi.subs(S, C + I*x)
        * conj((C + I*x)**j * psi.subs(S, C + I*x))
        for x, weight in zip(NODES, WEIGHTS)
    )))
    check(name + ": displayed matrix transpose", displayed, cross.T)
    B = det(displayed)
    kernel = (Echi * Hinv * Epsi.conjugate().T).applyfunc(scalar)
    Jchi, Jpsi = jets(roots_chi, q), jets(roots_psi, q)
    check(name + ": confluent Vandermonde chi", det(Jchi), vander(roots_chi))
    check(name + ": confluent Vandermonde psi", det(Jpsi), vander(roots_psi))
    check(name + ": main mixed identity", B,
          det(H) * det(kernel) / (vander(roots_chi) * conj(vander(roots_psi))))
    reverse = det(Tchi.conjugate().T * H * Tpsi)
    check(name + ": conjugate orientation", reverse, conj(B))

    vectors, norms = monic_orthogonals(H)
    check(name + ": monic norm product", det(H), sp.prod(norms))
    CfromOP = sp.zeros(q, q)
    for p, norm in zip(vectors, norms):
        CfromOP += (Echi * p) * (Epsi * p).conjugate().T / norm
    check(name + ": orthogonal kernel jets", kernel, CfromOP)
    Fchi = sp.prod(factorial(r) for _, m in roots_chi for r in range(m))
    Fpsi = sp.prod(factorial(r) for _, m in roots_psi for r in range(m))
    ordinary = sp.diag(*[factorial(r) for _, m in roots_chi for r in range(m)])
    ordinary = ordinary * kernel * sp.diag(*[
        factorial(r) for _, m in roots_psi for r in range(m)])
    check(name + ": ordinary derivative factorials", det(ordinary),
          Fchi * Fpsi * det(kernel))

    if integrate:
        integrated = 0
        for labels in product(range(len(NODES)), repeat=n):
            zs = [C + I * NODES[t] for t in labels]
            fc = sp.Matrix(n, n, lambda t, j: zs[t] ** j * chi.subs(S, zs[t]))
            fp = sp.Matrix(n, n, lambda t, j: zs[t] ** j * psi.subs(S, zs[t]))
            integrated += sp.prod(WEIGHTS[t] for t in labels) * det(fc) * conj(det(fp))
        check(name + ": finite determinant integration", B, integrated / factorial(n))

    scale = sp.Rational(7, 3)
    check(name + ": mass boundary power", det(scale * cross), scale ** n * B)
    check(name + ": mass kernel power", det(kernel / scale), det(kernel) / scale ** q)
    check(name + ": mass source power", det(scale * H), scale ** d * det(H))

    Ld, Lq = coordinate_matrix(d), coordinate_matrix(q)
    Hu = source_gram(d, "u")
    check(name + ": original coordinate Gram", H, Ld.conjugate().T * Hu * Ld)
    check(name + ": coefficient determinant phase", det(Ld), I ** (d*(d-1)//2))
    uc = tuple(((v-C)/I, m) for v, m in roots_chi)
    up = tuple(((v-C)/I, m) for v, m in roots_psi)
    Euc, Eup = jets(uc, d), jets(up, d)
    Ac = sp.diag(*[I ** (-r) for _, m in roots_chi for r in range(m)])
    Ap = sp.diag(*[I ** (-r) for _, m in roots_psi for r in range(m)])
    check(name + ": divided jet coordinate map", Echi, Ac * Euc * Ld)
    Ku = Euc * (Hu.inv() if d else sp.zeros(0, 0)) * Eup.conjugate().T
    check(name + ": mixed derivative phases", kernel, Ac * Ku * Ap.conjugate().T)
    tc = multiplication(poly(uc, U), n, d, U)
    tp = multiplication(poly(up, U), n, d, U)
    check(name + ": multiplier chart phase", chi.subs(S, C + I * U), I ** q * poly(uc, U))
    check(name + ": mixed boundary coordinate determinant", B,
          det(tp.conjugate().T * Hu * tc))

    if roots_chi == roots_psi:
        Hnext = source_gram(d + 1)
        Tnext = multiplication(chi, n + 1, d + 1)
        relation_gram = Tnext.conjugate().T * Hnext * Tnext
        _, relation_norms = monic_orthogonals(relation_gram)
        Enext = jets(roots_chi, d + 1)
        Knext = Enext * Hnext.inv() * Enext.conjugate().T
        check(name + ": relation monic norm determinant ratio", relation_norms[-1],
              det(relation_gram) / B)
        check(name + ": relation monic norm kernel ratio", relation_norms[-1],
              (det(Hnext) / det(H)) * det(Knext) / det(kernel))
        if q:
            rem = sp.Matrix(q, d, lambda j, r:
                sp.Poly(sp.rem(S ** r, chi, S), S).nth(j))
            check(name + ": literal jet remainder factorization", Echi, Jchi * rem)
            section = Hinv * Echi.conjugate().T * kernel.inv() * Jchi
            G = Jchi.conjugate().T * kernel.inv() * Jchi
            check(name + ": minimum section quotient", rem * section, sp.eye(q))
            check(name + ": minimum section orthogonality",
                  Tchi.conjugate().T * H * section, sp.zeros(n, q))
            check(name + ": minimum section Gram", section.conjugate().T * H * section, G)
            check(name + ": original quotient volume", det(G), det(H) / B)
            check(name + ": jet quotient volume", det(G),
                  vander(roots_chi) * conj(vander(roots_chi)) / det(kernel))
            Ju = jets(uc, q)
            Gu = Ju.conjugate().T * Ku.inv() * Ju
            check(name + ": quotient coordinate Gram", G, Lq.conjugate().T * Gu * Lq)
            check(name + ": quotient mass power", det(scale * G), scale ** q * det(G))
        else:
            check(name + ": zero quotient determinant", det(H) / B, 1)
    return B


def check_confluence():
    eps, delta = sp.symbols("eps delta", real=True)
    v, w = 1 + I, 2 - I
    # Polynomial kernel with six independent monomials; exact Taylor
    # confluence is checked without using the matrix inverse identity.
    polynomial = sum((j + 2) * V ** j * WBAR ** j for j in range(6))
    rows = [v, v + eps, v + 2 * eps]
    cols = [conj(w), conj(w) + delta, conj(w) + 2 * delta]
    ordinary_eval = sp.Matrix(3, 3, lambda r, s:
        polynomial.subs({V: rows[r], WBAR: cols[s]}))
    # Finite differences divide by the exact within-cluster Vandermondes,
    # 2 eps^3 and 2 delta^3, without expanding an unnecessarily large
    # symbolic determinant. These are exact invertible row/column maps
    # when eps and delta are nonzero; cancellation gives their limit.
    def differences(t):
        return sp.Matrix([[1, 0, 0], [-1/t, 1/t, 0],
                          [1/(2*t**2), -1/t**2, 1/(2*t**2)]])
    transformed = differences(eps) * ordinary_eval * differences(delta).T
    confluent_limit = transformed.applyfunc(lambda x:
        sp.cancel(sp.expand(x)).subs({eps: 0, delta: 0}))
    divided = sp.Matrix(3, 3, lambda r, s:
        sp.diff(polynomial, V, r, WBAR, s).subs({V: v, WBAR: conj(w)})
        / (factorial(r) * factorial(s)))
    check("direct double confluence entries with triple roots", confluent_limit, divided)
    check("direct double confluence determinant with triple roots", det(confluent_limit), det(divided))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-control", action="store_true")
    args = parser.parse_args()
    check("fixture mass is retained", sum(WEIGHTS), 21)
    if args.negative_control:
        check("deliberate corruption must fail", sp.Integer(1), sp.Integer(2))
    cases = [
        ("both empty", 0, (), (), True),
        ("zero relation degree", 2, (), (), True),
        ("n zero triple", 0, ((1+I, 3),), ((1+I, 3),), True),
        ("n zero mixed multiplicities", 0, ((1+I, 3),), ((-1+I, 2), (2-I, 1)), False),
        ("mixed multiplicities", 1, ((1+I, 3),), ((-1+I, 2), (2-I, 1)), True),
        ("double versus simple", 2, ((1+I, 2),), ((-1+I, 1), (2-I, 1)), True),
        ("triple diagonal", 2, ((1+I, 3),), ((1+I, 3),), True),
        ("complex cross value", 1, ((1+I, 1),), ((2-I, 1),), True),
    ]
    results = {}
    for case in cases:
        results[case[0]] = str(check_case(*case))
    if scalar(sp.im(sp.sympify(results["complex cross value"]))) == 0:
        raise RuntimeError("Complex cross fixture did not test a non-real determinant")
    CHECKS.append("mixed cross determinant is genuinely non-real")
    check_confluence()
    print(json.dumps({
        "status": "passed", "exact_check_count": len(CHECKS),
        "fixture_mass": "21", "arithmetic_source_evaluated": False,
        "fixture_role": "Exact determinant algebra only; no source replacement",
        "sympy_version": sp.__version__, "case_determinants": results,
        "checks": CHECKS,
    }, indent=2))


if __name__ == "__main__":
    main()
