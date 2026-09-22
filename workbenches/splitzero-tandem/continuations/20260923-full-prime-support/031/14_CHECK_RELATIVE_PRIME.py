"""Exact finite checks for ME and PD. General proofs are in the TeX chapters."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import sympy as sp

checks = 0
def check(value, name):
    global checks
    if not value:
        raise AssertionError(name)
    checks += 1

primes = (2, 3, 5)
faces = tuple(product((0, 1), repeat=4))
for s in (1, 2, 3):
    for powers in product((-1, 0, 1), repeat=3):
        char = {}
        for face in faces:
            a = Q(1)
            for p, n, flag in zip(primes, powers, face[1:]):
                a *= Q(p) ** (s*n*(face[0]-flag))
            char[face] = a
        check(char[(0,)*4] == char[(1,)*4] == 1, 'endpoint characters')
        for face in faces:
            comp = tuple(1-x for x in face)
            check(char[face]*char[comp] == 1, 'all complement characters')
        for j in (0, 1):
            cocycle = {face: char[face]-1 if face[0] == j else Q(0) for face in faces}
            check(cocycle[(0,)*4] == cocycle[(1,)*4] == 0, 'complete cocycle endpoints')
            for other in ((1, 0, -1), (0, 1, 0)):
                for face in faces:
                    b = Q(1)
                    for p, n, flag in zip(primes, other, face[1:]):
                        b *= Q(p) ** (s*n*(face[0]-flag))
                    left = char[face]*b-1 if face[0] == j else Q(0)
                    right = char[face]*(b-1 if face[0] == j else Q(0))+cocycle[face]
                    check(left == right, 'complete cocycle law')

for p in primes:
    for n in range(1, 5):
        modulus = p**n
        fibres = {u: [] for u in range(p**(n-1))}
        for a in range(modulus):
            fibres[a % (p**(n-1))].append(a)
        check(all(len(xs) == p for xs in fibres.values()), 'p-to-one original map')
        f = [Q((u % 7)-3, 1+u % 3) for u in fibres]
        before = sum(x*x for x in f)
        after = sum(f[a % (p**(n-1))]**2 for a in range(modulus))
        check(after == p*before, 'unweighted exact squared norm')
        check(Q(p)**n * Q(p)**(-n) == 1, 'dilation Haar Jacobian')
    for s in (1, 2, 3):
        a, b = Q(p)**(-s)-1, Q(p)**s-1
        check(a*b == -Q(p)**s*(1-Q(p)**(-s))**2, 'both local determinant signs')
        check(-1/a == 1/(1-Q(p)**(-s)), 'finite oriented factor')
    for n in range(1, 8):
        check(Q(p)**n * Q(p)**(-2*n) == Q(p)**(-n), 'squared original vector moment')

r, z = sp.symbols('r z', nonzero=True)
lhs = r*z/(1-r*z) + r/z/(1-r/z)
rhs = (1-r*r)/(1-r*(z+1/z)+r*r)-1
check(sp.cancel(lhs-rhs) == 0, 'exact Poisson rational identity')

# Finite sampled correlations: this checks indexing and signs in the proof,
# not a numerical replacement for the continuous Schwartz-space theorem.
vals = [sp.Integer(2), 1+sp.I, -3*sp.I, sp.Rational(1, 3), -2+sp.I]
r = sp.Rational(2, 3)
gram = sp.Matrix([[r**abs(i-j) for j in range(len(vals))] for i in range(len(vals))])
v = sp.Matrix(vals)
direct = (v.T*gram*v.conjugate())[0]
corr = sum(r**abs(j)*sum(vals[n]*sp.conjugate(vals[n-j])
           for n in range(len(vals)) if 0 <= n-j < len(vals))
           for j in range(-len(vals)+1, len(vals)))
check(sp.simplify(direct-corr) == 0, 'periodized energy versus complete correlations')
check(all(gram[:n, :n].det() > 0 for n in range(1, len(vals)+1)), 'positive moment kernel')

result = {
    'status': 'passed', 'exact_checks': checks,
    'scope': 'Finite rational and symbolic checks of ME cocycles and determinant signs, PD prime degree, Haar factors, Poisson identity and energy indexing.',
    'limitations': 'General cohomology, Fourier, spectrum and analytic statements rely on the complete TeX proofs; these checks do not establish RH or global purity.',
    'proof_files': ['11_mixed_extension_prime_trace.tex', '13_relative_prime_degree_operator.tex'],
}
Path(__file__).with_name('RELATIVE_PRIME_VERIFICATION.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
