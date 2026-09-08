"""Exact checks of integral maps, Tor factors and characteristic-dependent jets.

The general module proofs are in tex/integral_coefficient_conductor.tex.
This checks the original four-term coefficient independently of its factors.
"""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
q, t = s.symbols('q t')
r = q - 1/q
quantum = lambda n: sum(q**(n-1-2*j) for j in range(n))
h = quantum(7)*quantum(3)
original = q**10-q**4-q**-4+q**-10
records = []

def check(name, condition, **data):
    if not condition:
        raise AssertionError(name)
    records.append({'name': name, 'passed': True, **data})

V = s.diag(1, 1, 1, r**2)
H = s.diag(1, 1, 1, h)
DC = s.diag(1, 1, 1, original)
check('all entries of coefficient-conductor factorization',
      all(s.cancel(x) == 0 for x in DC-V*H))
check('integral Tor comparison and second jet',
      h.subs(q, 1) == 21 and
      s.limit(original/(q-1)**2, q, 1) == 84 and
      s.diff(original, q, 2).subs(q, 1) == 168)
check('retained semilinear deck involution',
      all(s.cancel(f.subs(q, 1/q)-f) == 0 for f in (r**2, h, original)))
poly = s.Poly(s.expand((1+t)**20-(1+t)**14-(1+t)**6+1), t)
unit_inverse = s.series((1+t)**-10, t, 0, 14).removeO()
series_original = s.Poly(s.expand(poly.as_expr()*unit_inverse), t)

for prime, expected_order, expected_lead in [(3, 4, 1), (5, 2, 4),
                                          (7, 8, 5), (11, 2, 7), (13, 2, 6)]:
    coeffs = [int(series_original.nth(j)) % prime for j in range(14)]
    order = next(j for j, c in enumerate(coeffs) if c)
    check(f'original coefficient jet in characteristic {prime}',
          order == expected_order and coeffs[order] == expected_lead,
          characteristic=prime, order=order, leading_coefficient=coeffs[order])
    # Multiplication on F_p[t]/t^N: rank follows by explicit elimination,
    # without presuming the coefficient's factorization or order.
    N = 12
    matrix = [[coeffs[i-j] if i >= j else 0 for j in range(N)] for i in range(N)]
    rank = 0
    for col in range(N):
        pivot = next((i for i in range(rank, N) if matrix[i][col] % prime), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inv = pow(matrix[rank][col] % prime, -1, prime)
        matrix[rank] = [(x*inv) % prime for x in matrix[rank]]
        for i in range(N):
            if i != rank:
                factor = matrix[i][col]
                matrix[i] = [(x-factor*y) % prime for x, y in zip(matrix[i], matrix[rank])]
        rank += 1
    check(f'truncated multiplication kernel in characteristic {prime}',
          rank == N-expected_order, truncation=N, rank=rank, kernel_dimension=N-rank)

for prime in [3, 7]:
    difference = s.cancel((quantum(prime)-r**(prime-1))*q**(prime-1))
    check(f'exact quantum integer identity in characteristic {prime}',
          s.Poly(difference, q, modulus=prime).is_zero)

out = {'all_passed': True, 'scope': 'exact symbolic identities and explicit finite jet matrices; general proofs in TeX',
       'checks': records}
(ROOT/'checks/integral_coefficient.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps({'all_passed': True, 'checks': len(records)}))
