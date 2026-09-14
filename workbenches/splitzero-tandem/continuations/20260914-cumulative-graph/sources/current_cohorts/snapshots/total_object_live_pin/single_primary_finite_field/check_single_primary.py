"""Exact cyclotomic checks for SPF.18--29; no floating point arithmetic."""
from collections import Counter
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
X = sp.Symbol("X")


def generator(p):
    for a in range(2, p):
        if len({pow(a, j, p) for j in range(p - 1)}) == p - 1:
            return a
    raise AssertionError(p)


def reduce_counts(counts, modulus, cyclo):
    a = [int(counts.get(i, 0)) for i in range(modulus)]
    degree = len(cyclo) - 1
    for j in range(modulus - 1, degree - 1, -1):
        q = a[j]
        if q:
            for i, coefficient in enumerate(cyclo):
                a[j - degree + i] -= q * coefficient
    return a[:degree]


cases = []
case_count = 0
for p in (5, 7, 11, 13, 17, 19, 31, 43):
    primitive = generator(p)
    logs = {pow(primitive, j, p): j for j in range(p - 1)}
    for n in range(2, min(p, 8)):
        if (p - 1) % n:
            continue
        modulus = n * p
        polynomial = sp.Poly(sp.cyclotomic_poly(modulus, X), X)
        coefficients = list(reversed([int(a) for a in polynomial.all_coeffs()]))
        gauss = {}
        for j in range(1, n):
            gauss[j] = Counter((p * j * logs[z] + n * z) % modulus
                               for z in range(1, p))
            norm = Counter()
            for a, ac in gauss[j].items():
                for b, bc in gauss[j].items():
                    norm[(a - b) % modulus] += ac * bc
            norm[0] -= p
            assert not any(reduce_counts(norm, modulus, coefficients))
        for rho in range(min(p, 4)):
            inv_n = pow(n, -1, p)
            c = -pow(-rho, n, p) * inv_n % p
            for u in range(1, p):
                inv_u = pow(u, -1, p)
                difference = Counter()
                # Actual original phase, including its base value and n.
                for s in range(p):
                    phi = (pow(s - rho, n, p) - pow(-rho, n, p)) * inv_n % p
                    difference[n * (phi * inv_u % p)] -= 1
                # Exact Frobenius sum of SPF.19.
                for j, g in gauss.items():
                    shift = (n * (c * inv_u % p)
                             + p * j * logs[n * u % p]) % modulus
                    for exponent, coefficient in g.items():
                        difference[(exponent + shift) % modulus] += coefficient
                assert not any(reduce_counts(difference, modulus, coefficients)), (
                    p, n, rho, u)
                case_count += 1
        cases.append({"p": p, "n": n, "characters": n - 1,
                      "rho_count": min(p, 4), "u_count": p - 1})

source = ROOT / "single_primary_finite_field.tex"
text = source.read_text(encoding="utf-8")
import re
tags = re.findall(r"\\tag\{(SPF\.\d+)\}", text)
labels = re.findall(r"\\label\{([^}]+)\}", text)
references = re.findall(r"\\eqref\{([^}]+)\}", text)
assert tags == [f"SPF.{i}" for i in range(1, 30)]
assert len(labels) == len(set(labels))
assert set(references).issubset(labels)
report = {
    "status": "passed",
    "method": "integer polynomial reduction modulo Phi_(np), no floating point",
    "original_phase_trace_cases": case_count,
    "gauss_absolute_square": "G conjugate(G)=p for every nontrivial tested character",
    "cases": cases,
    "unique_equation_tags": len(tags),
    "unique_labels": len(labels),
    "references_resolved": len(references),
    "tex_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
}
(ROOT / "EXACT_CHECKS.json").write_text(json.dumps(report, indent=2) + "\n",
                                        encoding="utf-8")
print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))
