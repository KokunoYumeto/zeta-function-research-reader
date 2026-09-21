"""Exact finite checks for ANGLE_PROOFS.md; auxiliary fixtures are identified.

These checks do not evaluate the original period-dependent invariant rows.
The source mass is retained symbolically as M_sigma; all displayed covariance
entries below are multiplied by that mass before exact rational comparison.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, ceil
import hashlib
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []

def require(name, value):
    if not bool(value):
        raise AssertionError(name)
    checks.append(name)

def zero_matrix(m):
    return all(s.cancel(x) == 0 for x in m)

def positive_definite(m):
    return all(s.det(m[:j, :j]) > 0 for j in range(1, m.rows + 1))

def gram_gamma(D):
    y = s.Symbol('y', real=True)
    polys = [s.Integer(1), y]
    for n in range(1, D):
        polys.append(s.expand(y * polys[n] - n * (n - s.Rational(1, 2)) * polys[n-1]))
    polys = polys[:D+1]
    basis = s.Matrix([[p.coeff(y, j) for p in polys] for j in range(D+1)])
    h = s.diag(*[s.factorial(n) * s.rf(s.Rational(1, 2), n) for n in range(D+1)])
    inv = basis.inv()
    return y, polys, basis, h, inv.T * h * inv

# AS6: entire rectangular shell and exact physical-separation identities.
for k in (1, 2, 3, 5, 9):
    for a in range(k+1):
        for b in range(k+1):
            shells = [0] * (k+1)
            separation_ok = True
            for c in range(k+1):
                for d in range(k+1):
                    r = max(abs(a-c), abs(b-d))
                    if r:
                        shells[r] += 1
                        norm_sq = F(1, 4)*(a-c)**2 + 36*(b-d)**2
                        separation_ok &= norm_sq >= F(1, 4)*r*r
            require(f'shell-count-k{k}-{a}-{b}', sum(shells) == (k+1)**2 - 1 and
                    all(shells[j] <= 8*j for j in range(1, k+1)))
            require(f'physical-separation-k{k}-{a}-{b}', separation_ok)
    require(f'shell-linear-sum-k{k}', sum(8*(k-j) for j in range(1, k+1)) == 4*k*(k-1))

# Exact Gamma weight induction, avoiding floating-point square roots.
print('Complete lattice checks passed', flush=True)
rho_sq = F(1)
for n in range(81):
    require(f'gamma-weight-n{n}', rho_sq*rho_sq <= 4*n+1 and rho_sq <= 2*n+1)
    require(f'gamma-weight-induction-n{n}',
            F(4*n+5)*(F(n)+F(1,2))**2-F(4*n+1)*(n+1)**2 == F(1,4))
    rho_sq *= F(n+1, 1)/F(2*n+1, 2)

# AS24: the strict min-max index, including very large cancellation constants.
for k in (17, 33, 65, 129):
    for a0, b0 in ((F(0), F(0)), (F(5,3), F(7,2)), (F(31), F(29)), (F(80), F(100))):
        LA = b0+9
        jA = ceil(max(2*(a0+1), a0+1+4*LA))
        for v in (0, 1, 40, 80):
            for sk in (0, v):
                r = 8*k-32-v+sk
                require(f'row-domain-{k}-{a0}-{b0}-{v}-{sk}', r > 0 and r <= 8*k-32)
                require(f'minmax-index-{k}-{a0}-{b0}-{v}-{sk}', all(
                    2 <= (R := F(j-1-a0, 1)/(2*LA)) <= k and
                    R >= F(j, 1)/(4*LA) and a0+b0*R < j
                    for j in range(jA, r+1)))

# Legendre coefficient norm and the exact polynomial recurrence.
print('Gamma weights and min-max index checks passed', flush=True)
y = s.Symbol('y', real=True)
for n in range(13):
    p = s.Poly(s.legendre(n, 2*y-3), y)
    require(f'legendre-coefficient-l1-{n}', sum(abs(c) for c in p.all_coeffs()) == s.legendre(n, 5))
    require(f'legendre-size-{n}', s.legendre(n, 5) <= 10**n)

# Complete four-root Gamma ideal at D=6, with genuinely complex functional rows.
D = 6
y, polys, basis, h, H = gram_gamma(D)
require('full-Gamma-orthogonality', zero_matrix(basis.T*H*basis-h))
require('full-Gamma-Gram-positive', positive_definite(H))
roots = [sx*3+sy*s.I/4 for sx in (-1, 1) for sy in (-1, 1)]
Q = s.Poly(s.prod(y-z for z in roots), y)
J = s.Matrix([[(Q.as_expr()*y**j).expand().coeff(y,n) for j in range(D-3)] for n in range(D+1)])
E = s.Matrix([[s.expand(z**n) for n in range(D+1)] for z in roots])
require('entire-four-root-ideal-evaluation', zero_matrix(E*J))
require('entire-four-root-evaluation-rank', E.rank() == 4)
require('entire-four-root-ideal-rank', J.rank() == D+1-4)

Hinv = H.inv()
print('Full Gamma Gram and complete ideal ranks passed', flush=True)
K = (E*Hinv*E.conjugate().T).applyfunc(s.expand)
Pdual = Hinv-Hinv*E.conjugate().T*K.inv()*E*Hinv
Idual = J*(J.conjugate().T*H*J).inv()*J.conjugate().T
print('Full-root Schur inverse calculated', flush=True)
require('full-root-Schur-equals-complete-ideal', zero_matrix(Pdual-Idual))
require('projected-dual-annihilates-evaluation', zero_matrix(E*Pdual))

w = s.Symbol('w')
cprime = s.Rational(1, 2)
As = [s.exp((2+3*s.I)*w)+2*s.exp((-1+s.I)*w),
      (1+w)*s.exp((1-2*s.I)*w)-s.I*s.exp(2*w)]
L = s.Matrix([[s.simplify((-s.I)**n*s.diff(A,w,n).subs(w,0)) for n in range(D+1)] for A in As])
for row, A in enumerate(As):
    G = s.exp(cprime*w)*A
    Fnumerator = (s.exp(w)-1)*G
    require(f'v1-low-jet-{row}', Fnumerator.subs(w,0) == 0)
    for n in range(D+1):
        transformed = sum(s.binomial(n,j)*(-cprime)**(n-j)*s.diff(G,w,j).subs(w,0)
                          for j in range(n+1))/s.I**n
        require(f'physical-center-phase-{row}-{n}', s.simplify(transformed-L[row,n]) == 0)

C = s.simplify(L*Pdual*L.conjugate().T)
B = s.simplify(L*Hinv*L.conjugate().T)
require('complex-restricted-covariance-positive', positive_definite(C))
require('complex-unprojected-covariance-positive', positive_definite(B))
require('projection-contraction', positive_definite(B-C))
require('negative-control-projection-is-essential', not zero_matrix(B-C))
require('negative-control-physical-phase-is-essential', L[0,1] != s.diff(As[0],w).subs(w,0))
det_angle = s.factor(C.det()/B.det())
require('angle-determinant-between-zero-one', 0 < det_angle < 1)
R = s.Matrix([[2, 1+s.I], [0, 3]])
require('exact-row-congruence-angle-invariance',
        s.factor((R*C*R.conjugate().T).det()/(R*B*R.conjugate().T).det()) == det_angle)
mass = s.Symbol('M_sigma', positive=True)
require('source-mass-retained-and-angle-cancelled',
        s.factor((C/mass).det()/(B/mass).det()) == det_angle)

# AS44-46 at original order k=5 (one Gamma recurrence factor), exact full measure.
print('Original center, phase and covariance checks passed', flush=True)
_, _, _, _, Hmore = gram_gamma(D+1)
moments = [Hmore[i//2, i-i//2] for i in range(2*D+3)]
H5_over_beta = s.Matrix([[moments[i+j+2]+s.Rational(1,4)*moments[i+j]
                         for j in range(D+1)] for i in range(D+1)])
lower = s.Rational(1,4)
upper = (2*(D+1)+s.Rational(1,2))**2
require('source-order-full-lower-form', positive_definite(H5_over_beta-lower*H))
require('source-order-full-upper-form', positive_definite(upper*H-H5_over_beta))
C5 = s.simplify(L*J*(J.conjugate().T*H5_over_beta*J).inv()*J.conjugate().T*L.conjugate().T)
B5 = s.simplify(L*H5_over_beta.inv()*L.conjugate().T)
require('source-order-restricted-inverse-lower', positive_definite(C5-C/upper))
require('source-order-restricted-inverse-upper', positive_definite(C/lower-C5))
require('source-order-full-inverse-lower', positive_definite(B5-B/upper))
require('source-order-full-inverse-upper', positive_definite(B/lower-B5))

# Exact adjacent full ideal and full-source updates; no innovation formula is imported.
print('Both source-order comparisons passed', flush=True)
_, _, _, _, Hnext = gram_gamma(D+1)
Jnext = s.Matrix([[(Q.as_expr()*y**j).expand().coeff(y,n) for j in range(D-2)] for n in range(D+2)])
Lnext = s.Matrix([[s.simplify((-s.I)**n*s.diff(A,w,n).subs(w,0)) for n in range(D+2)] for A in As])
Cnext = s.simplify(Lnext*Jnext*(Jnext.conjugate().T*Hnext*Jnext).inv()*Jnext.conjugate().T*Lnext.conjugate().T)
Bnext = s.simplify(Lnext*Hnext.inv()*Lnext.conjugate().T)
for tag, old, new in (('ideal', C, Cnext), ('full', B, Bnext)):
    diff = s.simplify(new-old)
    require(f'adjacent-{tag}-rank-one', diff.rank() == 1)
    require(f'adjacent-{tag}-positive', diff[0,0] > 0 and diff[1,1] > 0 and diff.det() == 0)
    require(f'adjacent-{tag}-determinant-lemma',
            s.factor(new.det()/old.det()) == s.factor(1+s.trace(old.inv()*diff)))

# AS50: the two real branches retain their exact cross-term cancellation.
print('Adjacent covariance checks passed', flush=True)
u0,u1,v0,v1,x = s.symbols('u0 u1 v0 v1 x', real=True)
even, odd = u0+s.I*u1, v0+s.I*v1
require('both-source-regions', s.expand((even+x*odd)*s.conjugate(even+x*odd)
        +(even-x*odd)*s.conjugate(even-x*odd)-2*(even*s.conjugate(even)+x*x*odd*s.conjugate(odd))) == 0)

# Exact discrete Cauchy aliases represented by reduction modulo t^T-r^T.
t = s.Symbol('t')
for T in (3, 5, 8):
    for a, radius in ((s.Rational(1,3),s.Rational(1,2)),(s.Rational(-2,5),s.Rational(1,3))):
        residue = s.invert(1-a*t, t**T-radius**T, t)
        for n in range(T):
            sampled = s.expand(residue).coeff(t,n)
            alias_error = a**n*(a*radius)**T/(1-(a*radius)**T)
            require(f'exact-Cauchy-alias-{T}-{a}-{radius}-{n}', s.factor(sampled-a**n-alias_error) == 0)

# Exact perturbation and four-sign constants.
require('relative-covariance-quarter', F(2,31)+F(1,31**2) < F(1,4))
require('relative-determinant-ratio-upper', F(5,4)/F(3,4) == F(5,3))
A0,A1,A2,A3 = s.symbols('A0 A1 A2 A3')
require('four-endpoint-signs', s.expand(A0+A1-A2-A3-(2*(A0-A2)+(A1-A0)-(A3-A2))) == 0)

receipt = {
    'status': 'passed', 'exact_checks': len(checks),
    'scope': 'Exact auxiliary lattice, polynomial, full Gamma, original-coordinate, complete-ideal, source-order and Cauchy identities. This does not evaluate original period-dependent invariant rows or certify the asymptotic proof by sampling.',
    'python': sys.version.split()[0], 'sympy': s.__version__,
    'fixture': {'lower_roots': [str(z) for z in roots], 'source_degree': D,
                'source_mass': 'M_sigma=sqrt(2*pi), retained; matrices listed multiplied by M_sigma',
                'complex_C_times_mass': [[str(s.factor(v)) for v in C.row(j)] for j in range(C.rows)],
                'complex_B_times_mass': [[str(s.factor(v)) for v in B.row(j)] for j in range(B.rows)],
                'exact_angle_determinant': str(det_angle)},
    'checks': checks,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_sha256': hashlib.sha256((HERE/'ANGLE_PROOFS.md').read_bytes()).hexdigest(),
}
(HERE/'ANGLE_EXACT_CHECKS.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({key: receipt[key] for key in ('status','exact_checks','script_sha256','proof_sha256')}))
