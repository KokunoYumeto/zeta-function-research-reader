"""Exact algebra fixtures for the original marked-family u connection.

These are finite symbolic fixtures, not claims that the fixture polynomials
are arithmetic zero packets. They check formulas proved in the companion audit.
"""
import json
import sympy as s

z, u, t = s.symbols('s u t')
fixtures = [z-3, z**2+2*z+5, (z-2)**2*(z+1), (z-2)**2*(z+1)**2]
results = []
for h in fixtures:
    h = s.expand(h)
    d = s.degree(h, z)
    phi = s.integrate(h, z)
    f = phi-t*z
    columns_a, columns_c, columns_b = [], [], []
    def column(p):
        return s.Matrix([s.expand(p).coeff(z, j) for j in range(d)])
    for b in range(d):
        qa, ra = s.div(z*z**b, h-t, z)
        qb, rb = s.div(f*z**b, h-t, z)
        if s.degree(qb, z) > d:
            raise RuntimeError('Division degree failed')
        if s.expand(f*z**b-(u*s.diff(qb,z)+(h-t)*qb)-(rb-u*s.diff(qb,z))) != 0:
            raise RuntimeError('Exact differential reduction failed')
        columns_a.append(column(ra))
        columns_c.append(column(rb))
        columns_b.append(column(s.diff(qb,z)))
    A=s.Matrix.hstack(*columns_a)
    C=s.Matrix.hstack(*columns_c)
    B=s.Matrix.hstack(*columns_b)
    Ku=-C/u**2+B/u
    Kt=-A/u
    flat=Kt.diff(u)-Ku.diff(t)+Ku*Kt-Kt*Ku
    conditions = {
        'flat': flat.applyfunc(s.simplify)==s.zeros(d),
        'B_t_zero': B.diff(t)==s.zeros(d),
        'trace_B': s.simplify(s.trace(B)-s.Rational(d,2))==0,
        'critical_trace_derivative': s.simplify(s.diff(s.trace(C),t)+s.trace(A))==0,
        'B_diagonal': all(s.simplify(B[j,j]-s.Rational(j+1,d+1))==0 for j in range(d)),
    }
    for rho, m in s.roots(h,z).items():
        conditions[f'critical_jet_{rho}_{m}'] = s.rem(phi-phi.subs(z,rho),(z-rho)**m,z)==0
    if not all(conditions.values()):
        raise RuntimeError(str(conditions))
    results.append({'h':str(h),'degree':int(d),'checks':conditions,'A':str(A),'C':str(C),'B':str(B)})
print(json.dumps({'status':'PASS','arithmetic_packet_claim':False,'fixtures':results},indent=2))
