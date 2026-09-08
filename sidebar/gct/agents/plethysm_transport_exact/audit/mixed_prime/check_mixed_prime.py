"""Independent exact checks for the integral-specialization subsection."""
from pathlib import Path
from math import comb, factorial
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[1] / 'plethysm_transport.tex'

def trim(a):
    return {i: v for i, v in a.items() if v}

def add(a, b):
    c = dict(a)
    for i, v in b.items():
        c[i] = c.get(i, 0) + v
    return trim(c)

def mul(a, b):
    c = {}
    for i, v in a.items():
        for j, w in b.items():
            c[i+j] = c.get(i+j, 0) + v*w
    return trim(c)

def power(a, n):
    c = {0: 1}
    for _ in range(n):
        c = mul(c, a)
    return c

def mod(a, p):
    return trim({i: v % p for i, v in a.items()})

def quantum(n):
    return {n-1-2*j: 1 for j in range(n)}

def binomial(n, j):
    v = 1
    for i in range(j):
        v *= n-i
    return v // factorial(j)

def jet(a, j):
    return sum(v*binomial(i, j) for i, v in a.items())

C = {10: 1, 4: -1, -4: -1, -10: 1}
r = {1: 1, -1: -1}
t = {1: 1, 0: -1}
u = {0: 1, -1: 1}
h = mul(quantum(7), quantum(3))
checks = []

def check(name, expression):
    assert expression, name
    checks.append(name)

check('original retained Laurent equality', C == mul(power(r, 2), h))
check('exact r=t*u', r == mul(t, u))
check('h(1)=21', sum(h.values()) == 21)
check('primitive vertical coefficients', set(C.values()) == {1, -1})
check('characteristic-zero order and lead', [jet(C, j) for j in range(3)] == [0, 0, 84])

residual = []
for ell in (3, 7, 5, 11, 13, 17, 19):
    expected_order = 4 if ell == 3 else 8 if ell == 7 else 2
    expected_lead = 1 if ell == 3 else 5 if ell == 7 else 84 % ell
    values = [jet(C, j) % ell for j in range(expected_order+1)]
    check(f'residual exact order {ell}', values[:-1] == [0]*expected_order and values[-1] == expected_lead)
    residual.append({'prime': ell, 'order': expected_order, 'leading_residue': expected_lead})

mixed = []
for ell, other in ((3, 7), (7, 3)):
    phi = {j: 1 for j in range(ell)}
    phi2 = {j: (-1)**j for j in range(ell)}
    check(f'quantum cyclotomic identity {ell}', quantum(ell) == mul({1-ell: 1}, mul(phi, phi2)))
    check(f'quantum Frobenius identity {ell}', mod(quantum(ell), ell) == mod(power(r, ell-1), ell))
    E = [comb(ell, j+1) for j in range(ell)]
    check(f'Eisenstein coefficients {ell}', E[0] == ell and E[-1] == 1 and all(a % ell == 0 for a in E[:-1]))
    U = mul(power(u, 2), mul({1-ell: 1}, mul(phi2, quantum(other))))
    check(f'exact mixed factorization {ell}', C == mul(power(t, 2), mul(phi, U)))
    check(f'mixed unit constant {ell}', sum(U.values()) == 4*other and sum(U.values()) % ell != 0)
    for k in range(1, 9):
        check(f'power identity {ell},{k}', power(C, k) == mul(power(t, 2*k), mul(power(phi, k), power(U, k))))
    mixed.append({'prime': ell, 'E_coefficients': E, 'U_constant': sum(U.values())})

for k in range(1, 13):
    m, n = 3**k, 7**k
    inverse_n_mod_m = pow(n, -1, m)
    inverse_m_mod_n = pow(m, -1, n)
    e3, e7 = n*inverse_n_mod_m, m*inverse_m_mod_n
    check(f'CRT idempotents {k}', e3 % m == 1 and e3 % n == 0 and e7 % m == 0 and e7 % n == 1 and (e3+e7) % (m*n) == 1)

raw = SOURCE.read_bytes()
text = raw.decode('utf-8')
start = text.index('\\subsection{Integral specialization, residual primes and exact orders}')
end = text.index('\\subsection{The original shape and an actual specialized source projector}', start)
subsection = text[start:end].encode('utf-8')
result = {
    'status': 'PASS',
    'scope': 'Integral specialization, residual primes and exact orders only',
    'source': str(SOURCE),
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'subsection_sha256': hashlib.sha256(subsection).hexdigest(),
    'checks_passed': len(checks),
    'checks': checks,
    'residual_checks': residual,
    'mixed_checks': mixed,
    'manual_proof_audit': 'AUDIT.md',
    'findings': [],
    'limitations': 'Finite computation corroborates identities; the accompanying audit gives the all-k Tor and module arguments. Other subsections are outside this audit.'
}
(HERE/'review.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': 'PASS', 'checks_passed': len(checks), 'subsection_sha256': result['subsection_sha256']}))
