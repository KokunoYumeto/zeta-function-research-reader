"""Exact finite checks supplementing the written proofs; no zero-location claim.

Synthetic rational complex points verify algebraic identities only. These are
not substituted for the original zeta divisor in ENDPOINT_GRAM_PROOFS.tex.
"""
from pathlib import Path
import json
import sympy as s


def zero_matrix(a):
    return all(s.cancel(v) == 0 for v in a)


def packet(points):
    slots = [(rho, j) for rho, m in points for j in range(m)]
    gram = s.Matrix([
        [(-1)**(j+l)*s.binomial(j+l, j)/(rho+s.conjugate(sig)-1)**(j+l+1)
         for sig, l in slots] for rho, j in slots])
    a = s.zeros(len(slots))
    for k, (rho, j) in enumerate(slots):
        a[k, k] = rho
        if j:
            a[k, k-1] = 1
    e = s.Matrix([int(j == 0) for _, j in slots])
    return slots, gram, a, e


checks = {}
points = [(s.Rational(3, 4)+s.I*s.Rational(2, 3), 2),
          (s.Rational(4, 5)-s.I*s.Rational(3, 5), 1)]
slots, g, a, e = packet(points)
checks['Cauchy_displacement_nonstable_divisor'] = zero_matrix(a*g+g*a.H-g-e*e.H)
det_rhs = s.Integer(1)
for rho, m in points:
    det_rhs /= (rho+s.conjugate(rho)-1)**(m*m)
for i, (rho, m) in enumerate(points):
    for sig, n in points[i+1:]:
        det_rhs *= (((rho-sig)*s.conjugate(rho-sig))/
                    ((rho+s.conjugate(sig)-1)*s.conjugate(rho+s.conjugate(sig)-1)))**(m*n)
checks['confluent_determinant'] = s.simplify(g.det()-det_rhs) == 0
checks['inverse_metric_displacement'] = zero_matrix(a.H*g.inv()+g.inv()*a-g.inv()-g.inv()*e*e.H*g.inv())
checks['trace_defect'] = s.simplify((e.H*g.inv()*e)[0]-sum(m*(2*s.re(rho)-1) for rho,m in points)) == 0

rho = s.Rational(3, 4)+s.I*s.Rational(2, 3)
slots, g, a, e = packet([(rho, 2), (s.conjugate(rho), 2)])
c = s.zeros(4)
for k, (point, j) in enumerate(slots):
    c[k, slots.index((s.conjugate(point), j))] = 1
app = a.T
checks['linear_conjugation_permutation'] = zero_matrix(c*g*c-s.conjugate(g)) and zero_matrix(c*app-a.H*c)

# Each local lower triangular Taylor unit is retained before reversal.
u1 = s.Matrix([[3+s.I, 0], [2-4*s.I, 3+s.I]])
u2 = s.conjugate(u1)
rev = s.Matrix([[0,1],[1,0]])
u = s.diag(rev*u1, rev*u2)
checks['principal_part_action'] = zero_matrix(u*a-app*u)
T = s.symbols('T', real=True)
# Scalar exponentials can be any block scalars; choose explicit nonzero ones
# to verify the boundary equation in exact rational arithmetic.
et = s.diag(3*s.Matrix([[1,T],[0,1]]), 5*s.Matrix([[1,T],[0,1]]))
mt = g*c*et*u
ell = e.H*c*et*u
checks['typed_boundary_equation'] = zero_matrix(mt*a-(s.eye(4)-a)*mt-e*ell)
checks['typed_metric_pullback'] = zero_matrix(mt.H*g.inv()*mt-u.H*et.H*s.conjugate(g)*et*u)

minor_checks = []
legendre_checks = []
for m in range(1, 8):
    h = s.Matrix([[s.Rational(1, s.factorial(i)*s.factorial(j)*(i+j+1)) for j in range(m)] for i in range(m)])
    n = s.zeros(m)
    for j in range(m-1):
        n[j,j+1] = 1
    b = s.Matrix([1/s.factorial(j) for j in range(m)])
    e0 = s.eye(m)[:,0]
    hi = h.inv()
    legendre_checks.append(zero_matrix(n.T*h+h*n-b*b.T+e0*e0.T))
    legendre_checks.append((b.T*hi*b)[0] == m*m)
    legendre_checks.append((e0.T*hi*e0)[0] == m*m)
    legendre_checks.append((e0.T*hi*b)[0] == (-1)**(m-1)*m)
    legendre_checks.append(h.det() == s.prod(s.factorial(j)/s.factorial(m+j) for j in range(m)))
    for r in range(1,m+1):
        mat = s.Matrix([[0 if m-r+j-i < 0 else 1/s.factorial(m-r+j-i) for j in range(r)] for i in range(r)])
        minor_checks.append(mat.det() == s.prod(s.factorial(j)/s.factorial(m-r+j) for j in range(r)))
checks['all_extreme_minors_m1_to_m7'] = all(minor_checks)
checks['critical_Gram_kernel_m1_to_m7'] = all(legendre_checks)

# Verify the exact finite singular metric at a real single block by symbolic
# differentiation and the value at T=0; this retains every nilpotent entry.
for m in range(1, 5):
    slots, gr, ar, er = packet([(s.Rational(3,4), m)])
    nr = ar.T-s.Rational(3,4)*s.eye(m)
    pr = sum((T**j/s.factorial(j)*nr**j for j in range(m)), s.zeros(m))
    singular = s.exp(T/2)*pr.T*gr*pr-gr
    row = er.T*pr
    checks[f'exact_singular_integral_m{m}'] = zero_matrix(singular.diff(T)-s.exp(T/2)*row.T*row) and zero_matrix(singular.subs(T,0))

assert all(checks.values()), checks
out = {'status': 'all exact checks passed', 'checks': checks,
       'scope': 'Finite algebraic verification; full analytic and source proofs are in ENDPOINT_GRAM_PROOFS.tex.'}
Path(__file__).with_name('EXACT_CHECK_RESULTS.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps(out, indent=2))
