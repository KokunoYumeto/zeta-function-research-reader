"""Exact rational finite-measure checks; not a native arithmetic evaluation."""
import json
import sympy as s

x = s.Symbol('x', real=True)
nodes = [s.Rational(t) for t in (0, 1, 2, 4, 7, 9, 13)]
weights = [s.Rational(7, 3) * t for t in (1, 3, 2, 5, 4, 2, 1)]
records = []


def integral(f):
    return s.cancel(sum(w*f.subs(x, t) for w, t in zip(weights, nodes)))


def equal(a, b):
    if isinstance(a, s.MatrixBase) or isinstance(b, s.MatrixBase):
        return (s.Matrix(a)-s.Matrix(b)).applyfunc(s.cancel).is_zero_matrix is True
    return s.cancel(a-b) == 0


def check(label, condition):
    if not condition:
        raise RuntimeError(label)
    records.append(label)


for r, n, a in [(1, 0, s.Rational(4)), (2, 1, s.Rational(16)),
                 (3, 1, s.Rational(4)), (4, 2, s.Rational(36))]:
    mu = [integral(x**j) for j in range(2*r+2)]
    H = s.Matrix(r, r, lambda i, j: mu[i+j])
    D = s.Matrix(r, r, lambda i, j: mu[i+j+1])
    C = H[:, :n+1]
    e = s.eye(r)[:, -1]
    kappa = 1/(e.T*D.inv()*e)[0]
    Dt = D-kappa*e*e.T
    R = (D+a*H).inv()
    Fminus = C.T*R*C
    Fplus = C.T*(Dt+a*H).inv()*C
    F = s.Matrix(n+1, n+1, lambda i, j: integral(x**(i+j)/(x+a)))
    pcoeff = -H.inv()*s.Matrix(mu[r:2*r])
    p = x**r+sum(pcoeff[i]*x**i for i in range(r))
    tc = -D[:-1, :-1].inv()*D[:-1, -1] if r > 1 else s.zeros(0, 1)
    tpoly = x**(r-1)+sum(tc[i]*x**i for i in range(r-1))
    z = s.Matrix([(-a)**i for i in range(n+1)])
    lam = integral(p*p/(x+a))/p.subs(x, -a)**2
    eta = integral(x*tpoly*tpoly/(x+a))/(a*tpoly.subs(x, -a)**2)
    gamma = kappa/(p.subs(x, -a)**2*(1-kappa*(e.T*R*e)[0]))
    label = f'r{r}_n{n}_a{a}'
    check(label+'_original_mass', equal(mu[0], sum(weights)))
    check(label+'_radau_monic_minimum', equal(integral(x*tpoly*tpoly), kappa))
    check(label+'_lower_exact_error', equal(F-Fminus, lam*z*z.T))
    check(label+'_upper_exact_error', equal(Fplus-F, eta*z*z.T))
    check(label+'_rank_one_finite_gap', equal(Fplus-Fminus, gamma*z*z.T) and lam >= 0 and eta >= 0)
    check(label+'_all_signed_moments', all(equal(F[i, j],
          sum((-a)**l*mu[i+j-1-l] for l in range(i+j))+(-a)**(i+j)*F[0, 0])
          for i in range(n+1) for j in range(n+1)))
    check(label+'_highest_coefficient', equal(e.T*R*C, -z.T/p.subs(x, -a)))
    if n:
        u = s.Matrix([1+s.I]+list(range(1, n+1)))
        v = s.Matrix([2-s.I]+[s.I*j for j in range(1, n+1)])
        phase = (u.conjugate().T*z)[0]*(z.T*v)[0]
        check(label+'_complex_cross_term', equal((u.conjugate().T*(F-Fminus)*v)[0], lam*phase))
        # The original complex translation and phases, not a diagonal surrogate.
        c = s.Rational(9, 2)
        T = s.Matrix(n+1, n+1, lambda i, j: s.binomial(j, i)*c**(j-i)*s.I**i if i <= j else 0)
        check(label+'_literal_S_congruence', equal(T.conjugate().T*(F-Fminus)*T,
              lam*(T.conjugate().T*z)*(z.T*T)))

# Negative controls distinguish a missing mass factor and discarded complex phase.
check('reject_unit_mass_substitution', not equal(F-Fminus, lam*z*z.T/mu[0]))
check('reject_dropped_complex_phase', not equal((u.conjugate().T*(F-Fminus)*v)[0],
       lam*s.Abs(phase)))
print(json.dumps(dict(status='passed', exact_checks=len(records), negative_controls=2,
      fixture='finite rational positive measure with retained mass; not zeta-zero data',
      checks=records), ensure_ascii=False, indent=2))
