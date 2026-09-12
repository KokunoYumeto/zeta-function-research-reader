"""Exact recurrence audit, including full repeated jets and singular Q_n.

Gaussian vertical moments calibrate identities only; no arithmetic nu_Z
estimate is inferred. Every assertion uses explicit exceptions under -O.
"""
import json
import sys
from pathlib import Path
import sympy as sp

Q = sp.Rational
s = sp.Symbol('s')
v = Q(1, 16)
q = [sp.Integer(1), s-Q(1, 2)]
for n in range(1, 7):
    q.append(sp.expand((s-Q(1, 2))*q[n]+n*v*q[n-1]))
kappa = [sp.factorial(n)*v**n for n in range(len(q))]
checks = []
cases = []

def eq(label, actual, expected):
    difference = actual-expected
    values = list(difference) if isinstance(difference, sp.MatrixBase) else [difference]
    if any(sp.simplify(x) != 0 for x in values):
        raise RuntimeError(f'{label}: difference {difference}')
    checks.append(label)

def column(poly, h):
    r = sp.Poly(sp.rem(poly, h, s), s)
    return sp.Matrix([r.nth(0), r.nth(1)])

packet_polynomials = {
    'reflected_pair': (s-Q(3,4))*(s-Q(1,4)),
    'repeated_off_line': (s-Q(3,4)-sp.I/Q(7))**2,
    'critical_two_nodes': (s-Q(1,2))**2+v,
    'critical_repeated_centre': (s-Q(1,2))**2,
}

for name, h in packet_polynomials.items():
    h = sp.expand(h)
    A = sp.Matrix.hstack(column(s, h), column(s*s, h))
    c = sp.Matrix([1, 0])
    columns = [column(poly, h) for poly in q]
    qm = []
    for poly in q:
        coeff = sp.Poly(sp.rem(poly, h, s), s)
        qm.append(coeff.nth(0)*sp.eye(2)+coeff.nth(1)*A)
    kernels = [sum((columns[k]*columns[k].H/kappa[k] for k in range(N+1)), sp.zeros(2)) for N in range(7)]
    for n in range(2, 6):
        label = f'{name}/n{n}'
        K = kernels[n-1]
        Knew = kernels[n]
        if sp.simplify(K.det()) == 0 or sp.simplify(Knew.det()) == 0:
            raise RuntimeError(f'{label}: kernel unexpectedly singular')
        M = K.inv()/kappa[n-1]
        Mnew = Knew.inv()/kappa[n]
        C, R, following = columns[n], columns[n-1], columns[n+1]
        a = n*v
        b = Q(1,2)
        inner = lambda u, w: sp.simplify((u.H*M*w)[0])
        alpha = inner(R, R)
        beta = inner(C, C)
        gamma = inner(C, R)
        t = (A-b*sp.eye(2))*C+a*R
        alpha_new = sp.simplify((C.H*Mnew*C)[0])
        beta_new = sp.simplify((following.H*Mnew*following)[0])
        gamma_new = sp.simplify((following.H*Mnew*C)[0])
        eq(label+'/polynomial_recurrence', t, following)
        eq(label+'/kernel_step', Knew-K, C*C.H/kappa[n])
        eq(label+'/displacement', A*K+K*A.H-K, (C*R.H+R*C.H)/kappa[n-1])
        eq(label+'/alpha_step', alpha_new, beta/(a+beta))
        eq(label+'/beta_step', beta_new, (inner(t,t)-inner(C,t)*inner(t,C)/(a+beta))/a)
        eq(label+'/gamma_step', gamma_new, inner(t,C)/(a+beta))
        eq(label+'/trace_invariant', sp.re(gamma), sp.re(sp.trace(A))-1)
        eq(label+'/real_gamma_step', sp.re(gamma_new), sp.re(gamma))
        eq(label+'/imaginary_gamma_step', sp.im(gamma_new), (beta*sp.im(b)-sp.im(inner(C,A*C))-a*sp.im(gamma))/(a+beta))
        delta = sp.simplify(alpha*beta-gamma*sp.conjugate(gamma))
        delta_new = sp.simplify(alpha_new*beta_new-gamma_new*sp.conjugate(gamma_new))
        eq(label+'/kernel_determinant', Knew.det()/K.det(), (a+beta)/a)
        U = A+sp.eye(2)
        G = U.H*K.inv()*U
        Gnew = U.H*Knew.inv()*U
        eq(label+'/source_determinant', Gnew.det()/G.det(), 1-alpha_new)
        if sp.simplify(beta) == 0:
            eq(label+'/exception_C', C, sp.zeros(2,1))
            eq(label+'/exception_delta', delta, 0)
            eq(label+'/exception_next_delta', delta_new, 0)
            eq(label+'/exception_beta', beta_new, a*alpha)
        else:
            P = sp.eye(2)-C*C.H*M/beta
            p = P*R
            w = P*A*C
            eq(label+'/projection_idempotent', P*P, P)
            eq(label+'/projection_self_adjoint', P.H*M, M*P)
            eq(label+'/current_transverse_energy', delta, beta*inner(p,p))
            eq(label+'/next_transverse_energy', delta_new, beta*inner(w+a*p,w+a*p)/(a*(a+beta)))
            eq(label+'/energy_change', delta_new-delta, beta*(inner(w,w)+2*a*sp.re(inner(w,p))-a*beta*inner(p,p))/(a*(a+beta)))
        if sp.simplify(qm[n].det()) != 0 and sp.simplify(qm[n+1].det()) != 0:
            Sn = kappa[n-1]*qm[n].inv()*K*qm[n].H.inv()
            Snew = kappa[n]*qm[n+1].inv()*Knew*qm[n+1].H.inv()
            Rn = qm[n].inv()*qm[n-1]
            Tn = A-b*sp.eye(2)+a*Rn
            eq(label+'/typed_isometry', qm[n].H*M*qm[n], Sn.inv())
            eq(label+'/resolvent_step', Snew, Tn.inv()*(a*Sn+c*c.H)*Tn.H.inv())
            eq(label+'/resolvent_determinant', Snew.det()/Sn.det(), a*(a+beta)/(Tn.det()*sp.conjugate(Tn.det())))
        cases.append({'packet': name, 'n': n, 'q_n_singular': sp.simplify(qm[n].det()) == 0, 'beta_zero': sp.simplify(beta) == 0})

receipt = {'scope': 'exact identities in explicit Gaussian moment packets; includes repeated jets and quadrature intersections; no arithmetic estimate', 'python_optimization': sys.flags.optimize, 'checks_passed': len(checks), 'cases': cases, 'checks': checks}
suffix = '.optimized.json' if sys.flags.optimize else '.json'
Path(__file__).with_suffix(suffix).write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'checks_passed': len(checks), 'cases': len(cases), 'singular_q_n_cases': sum(x['q_n_singular'] for x in cases), 'zero_beta_cases': sum(x['beta_zero'] for x in cases)}))
