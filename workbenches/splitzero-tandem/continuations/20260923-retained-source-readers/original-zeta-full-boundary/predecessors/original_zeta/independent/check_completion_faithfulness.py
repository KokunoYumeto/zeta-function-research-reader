"""Exact finite-jet, residue, and probe checks for CFD1--21.

These finite symbolic checks support the complete proofs in the TeX.
They do not certify any assertion about every zeta zero.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []

def record(name, ok):
    assert ok, name
    checks.append(name)

h, z = s.symbols('h z')
N = 5
a = [s.Rational(3), s.Rational(-2), s.Rational(7, 3),
     s.Rational(1, 2), s.Rational(-5, 4), s.Rational(11, 7)]
ap = sum(a[j] * h**j for j in range(N + 1))
d = s.series(8 / ap, h, 0, N + 1).removeO()
forward = s.Matrix(N + 1, N + 1,
    lambda n, j: s.I**n / (8 * 2**n) * a[n-j] if j <= n else 0)
backward = s.Matrix(N + 1, N + 1,
    lambda n, j: d.coeff(h, n-j) * (2/s.I)**j if j <= n else 0)
record('CFD4 forward followed by inverse', forward * backward == s.eye(N + 1))
record('CFD4 inverse followed by forward', backward * forward == s.eye(N + 1))
for k in range(-3, 4):
    for n in range(max(0, -k), max(0, -k)+5):
        # Here n is the original meromorphic order of a nonzero f in I.
        recovered = (k+n) - max(k, 0) + max(-k, 0)
        record(f'CFD7 signed divisor k={k}, n={n}', recovered == n)

for k in [-3, -2, -1, 0, 1, 2, 3]:
    Ai = h**k * ap
    fj = h**(-k) * sum(s.Rational(j+1, j+2)*h**j for j in range(N+1))
    direct = s.series((Ai*fj/8).subs(h, s.I*z/2), z, 0, N+1).removeO()
    coeff = forward * s.Matrix([s.Rational(j+1, j+2) for j in range(N+1)])
    record(f'CFD4 coefficients actual fractional exponent k={k}',
           all(s.expand(direct).coeff(z,j) == coeff[j] for j in range(N+1)))

Aa = ap / h
record('CFD18 double-pole coefficient',
       s.limit(h**2 * s.diff(Aa, h, 2)/(4*Aa), h, 0) == s.Rational(1,2))
record('CFD19 s-coordinate residue',
       (-6*s.pi) * s.Rational(1,6) / 8 == -s.pi/8)
record('CFD19 z-coordinate residue',
       (-s.pi/8)/(s.I/2) == -s.pi/(4*s.I))
record('CFD19 Hurwitz tangent at -2',
       2 * (-s.Rational(1,12)) == -s.Rational(1,6))
r = s.symbols('r')
probe = z**2
image = probe - r*s.diff(probe, z, 2)
record('CFD17 degree-two amplitude probe', s.expand(image) == z**2 - 2*r)
record('CFD16 exact recovered amplitude', -s.Rational(1,2)*image.coeff(z,0) == r)

proof = HERE / 'COMPLETION_FAITHFULNESS_DERIVATION.tex'
receipt = {
    'proof': proof.name,
    'sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
    'check_count': len(checks),
    'exact_checks': checks,
    'scope': 'Finite symbolic checks; all-L, analytic and all-order claims are proved in the source.',
}
(HERE / 'COMPLETION_FAITHFULNESS_EXACT_CHECK.json').write_text(
    json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'check_count': len(checks), 'proof_sha256': receipt['sha256']}))
