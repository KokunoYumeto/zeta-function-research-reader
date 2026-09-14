"""Exact symbolic checks for the full single-primary connection.

The symbol rho remains symbolic. These checks verify the proved algebra;
they do not supply an arithmetic zero or its order.
"""
from pathlib import Path
import hashlib
import json
import re
import sympy as s

rho, y, x, u = s.symbols("rho y s u")
results = []
for m in range(1, 8):
    n = m+1
    p = s.Matrix(m, m, lambda a,b:
                 s.binomial(b,a)*rho**(b-a) if a <= b else 0)
    ip = s.Matrix(m, m, lambda a,b:
                  s.binomial(b,a)*(-rho)**(b-a) if a <= b else 0)
    j = s.Matrix(m, m, lambda a,b: int(a == b+1))
    diag = s.diag(*[s.Rational(a+1,n) for a in range(m)])
    bmat = s.zeros(m)
    for b in range(m):
        bmat[b,b] = s.Rational(b+1,n)
        if b:
            bmat[b-1,b] = -s.Rational(b,n)*rho
    amat = ip*(rho*s.eye(m)+j)*p
    c = -(-rho)**n/n
    phase = ((x-rho)**n-(-rho)**n)/n
    def zero(z):
        if isinstance(z,s.MatrixBase):
            return all(s.simplify(v) == 0 for v in z)
        return s.simplify(z) == 0
    assert zero(p*ip-s.eye(m))
    assert zero(p*bmat*ip-diag)
    assert zero(n*(bmat*amat-amat*bmat)-(amat-rho*s.eye(m)))
    for b in range(m):
        quotient = (x-rho)*x**b/n
        assert zero(phase*x**b-(x-rho)**m*quotient-c*x**b)
        assert zero(s.diff(quotient,x)-sum(bmat[a,b]*x**a for a in range(m)))
    # Test the exact differential correction for every basis Taylor
    # coefficient, without assigning a numerical unit.
    for a in range(m):
        vpoly = (x-rho)**a
        for b in range(m):
            product = vpoly*(x-rho)**b
            quotient, rem = s.div(product,(x-rho)**m,x)
            corrected = rem-u*s.diff(quotient,x)
            assert zero(product-((x-rho)**m*quotient
                        +u*s.diff(quotient,x))-corrected)
    results.append({"m": m, "n": n, "pascal_inverse": True,
                    "exact_B": True, "arithmetic_commutator": True,
                    "unit_differential_remainder": True})

path=Path(__file__).with_name("single_primary_boundary_control.tex")
body=path.read_text(encoding="utf-8")
tags=re.findall(r"\\tag\{(SP\.\d+)\}",body)
assert len(tags)==len(set(tags))==36, tags
out={"checks": results, "tags": tags, "source_sha256":
     hashlib.sha256(path.read_bytes()).hexdigest()}
Path(__file__).with_name("single_primary_symbolic_checks.json").write_text(
    json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps({"exact_symbolic_cases":len(results),"unique_SP_tags":len(tags)}))
