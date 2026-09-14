"""Exact finite fixtures for RW1--23, not arithmetic-zero or Lean evidence."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp

S, u, t = sp.symbols("S u t")


def require_zero(value, name):
    entries = list(value) if isinstance(value, sp.MatrixBase) else [value]
    if any(sp.expand(entry) != 0 for entry in entries):
        raise RuntimeError("exact identity failed: " + name)


def companion(chi):
    q = sp.degree(chi, S)
    matrix = sp.zeros(q)
    for j in range(q):
        remainder = sp.rem(S ** (j + 1), chi - t, S)
        for i in range(q):
            matrix[i, j] = remainder.coeff(S, i)
    return matrix


def flow_coefficients(matrix, rank_one, order):
    values = [sp.eye(matrix.rows)]
    for n in range(order):
        value = -values[n] * matrix
        if n:
            value -= u * values[n - 1] * rank_one
        values.append((value / (n + 1)).applyfunc(sp.expand))
    return values


def run_fixture(chi, k, order=4):
    chi = sp.expand(chi)
    q = int(sp.degree(chi, S))
    epsilon = (-1) ** q
    reflection = sp.zeros(q)
    for j in range(q):
        for i in range(j + 1):
            reflection[i, j] = sp.binomial(j, i) * k ** (j - i) * (-1) ** i
    require_zero(chi.subs(S, k - S) - epsilon * chi, "RW3")
    require_zero(reflection ** 2 - sp.eye(q), "RW7")
    polynomial = (u + t * S) ** 2 + S ** (q + 2) + u * t
    reflected = polynomial.subs(S, k - S)
    source_d = u * sp.diff(polynomial, S) + (chi - t) * polynomial
    target_d = (-epsilon * u) * sp.diff(epsilon * reflected, S)
    target_d += (chi - epsilon * t) * epsilon * reflected
    require_zero(target_d - source_d.subs(S, k - S), "RW8")
    matrix = companion(chi)
    reflected_matrix = matrix.subs(t, epsilon * t)
    require_zero(reflection * matrix * reflection - k * sp.eye(q) + reflected_matrix, "RW9")
    phi = sp.integrate(chi, S)
    phi -= phi.subs(S, 0)
    phi_t = phi - t * S
    require_zero(phi_t.subs(S, k - S) - phi.subs(S, k) + k*t
                 + epsilon * (phi - epsilon*t*S), "RW10")
    # Residue entries are computed independently by polynomial remainders.
    pairing = sp.zeros(q)
    for i in range(q):
        for j in range(q):
            pairing[i, j] = sp.rem(S ** (i + j), chi - t, S).coeff(S, q-1)
    require_zero(pairing.diff(t), "RW22 constant")
    require_zero(pairing.det() - (-1) ** (q*(q-1)//2), "RW22 determinant")
    require_zero(matrix.T*pairing - pairing*matrix, "residue adjoint")
    reflected_pairing = reflection.T*pairing
    require_zero(matrix.T*reflected_pairing + reflected_pairing*reflected_matrix
                 - k*reflected_pairing, "RW23")
    rank_one = matrix.diff(t)
    coefficients = flow_coefficients(matrix, rank_one, order)
    require_zero(2*coefficients[2] - matrix**2 + u*rank_one, "flow second derivative")
    for n in range(order+1):
        rhs = sp.zeros(q)
        for j in range(n+1):
            transformed = coefficients[j].subs({u:-epsilon*u, t:epsilon*t}, simultaneous=True)
            rhs += sp.Rational((-k)**(n-j), sp.factorial(n-j)) * (-1)**j * transformed
        require_zero(reflection*coefficients[n]*reflection - rhs, "RW16 coefficient " + str(n))
    inverse = [sp.eye(q)]
    for n in range(1, order+1):
        inverse.append((-sum((coefficients[j]*inverse[n-j] for j in range(1,n+1)), sp.zeros(q))).applyfunc(sp.expand))
    dual = []
    for n in range(order+1):
        dual.append(sum((sp.Rational((-k)**(n-j), sp.factorial(n-j))*inverse[j].T
                         for j in range(n+1)), sp.zeros(q)).applyfunc(sp.expand))
    for n in range(order+1):
        coefficient = sum((dual[j].T*coefficients[n-j] for j in range(n+1)), sp.zeros(q))
        require_zero(coefficient-sp.Rational((-k)**n, sp.factorial(n))*sp.eye(q), "RW20 coefficient " + str(n))
    require_zero(dual[1] - matrix.T + k*sp.eye(q), "RW21")
    return {"k":k,"q":q,"chi":str(chi),"flow_order":order,"status":"PASS"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    parser.add_argument("--mutant", choices=["wrong_reflection_sign","frozen_flow"])
    args = parser.parse_args()
    if args.mutant == "wrong_reflection_sign":
        # The wrong positive u' has derivative discrepancy 2u P'.
        require_zero(2*u, "negative control: wrong reflection sign")
    if args.mutant == "frozen_flow":
        # Freezing exp(-aA(t)) omits the exact -u R second derivative.
        require_zero(u*sp.Matrix([[1]]), "negative control: frozen flow")
    fixtures = []
    for k in (1,3):
        y = S-sp.Rational(k,2)
        quartet = y**4+sp.Rational(15,8)*y**2+sp.Rational(289,256)
        for chi in (y, y**2+1, y**3-2*y, quartet, y*(y**2+1)**2):
            fixtures.append(run_fixture(chi,k))
    # A nonreduced quartic fixture retains all nilpotent directions.
    y = S-sp.Rational(2,2)
    fixtures.append(run_fixture((y**2+1)**2,2))
    body = {"status":"PASS","scope":"11 exact finite polynomial fixtures; not actual zero certificates",
            "fixtures":fixtures,"sympy":sp.__version__,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    rendered = json.dumps(body,indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(rendered,encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
