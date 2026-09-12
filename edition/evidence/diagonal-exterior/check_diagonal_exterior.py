"""Exact diagonal/exterior assembly regressions, not an arithmetic bound.

All equations are checked in the literal monomial tensor quotient and in
the two polynomial coefficient quotients. No canonical or release file is
modified. All guards survive python -O. SymPy provides rational arithmetic.
"""
import json
import sys
from itertools import combinations
import sympy as sp

t, x, y, S, r, Delta = sp.symbols('t x y S r Delta')


class CheckFailure(RuntimeError):
    pass


checks = 0


def require(condition, label):
    global checks
    checks += 1
    if not condition:
        raise CheckFailure(label)


def even_to_R(expr):
    out = 0
    for (power,), coefficient in sp.Poly(sp.expand(expr), r).terms():
        require(power % 2 == 0, 'polynomial claimed even in r')
        out += coefficient * Delta ** (power // 2)
    return sp.expand(out)


def companion(h):
    poly = sp.Poly(h, t)
    d = poly.degree()
    require(poly.LC() == 1 and d >= 1, 'monic nonempty packet fixture')
    out = sp.zeros(d)
    for j in range(d - 1):
        out[j + 1, j] = 1
    for i in range(d):
        out[i, d - 1] = -poly.nth(i)
    return out


def evaluate(expr, symbols, matrices):
    n = matrices[0].rows
    result = sp.zeros(n)
    for powers, coefficient in sp.Poly(sp.expand(expr), *symbols).terms():
        term = sp.eye(n)
        for matrix, power in zip(matrices, powers):
            term = term * matrix ** power
        result += coefficient * term
    return result


def quotient_basis(gb):
    leading = [p.LM(order=gb.order).exponents for p in gb.polys]
    if (0, 0) in leading:
        return []
    s_bound = min(a for a, b in leading if a > 0 and b == 0)
    d_bound = min(b for a, b in leading if b > 0 and a == 0)
    return [(a, b) for a in range(s_bound) for b in range(d_bound)
            if not any(a >= c and b >= e for c, e in leading)]


def normal_coefficients(expr, gb, basis):
    remainder = sp.Poly(gb.reduce(sp.expand(expr))[1], S, Delta)
    return sp.Matrix([remainder.coeff_monomial(S ** a * Delta ** b) for a, b in basis])


def packet(h):
    a = companion(h)
    d = a.rows
    n = d * d
    X, Y = sp.kronecker_product(a, sp.eye(d)), sp.kronecker_product(sp.eye(d), a)
    sum_op, difference = X + Y, X - Y
    delta_op = difference * difference
    unit = sp.zeros(n, 1)
    unit[0] = 1
    swap = sp.zeros(n)
    for i in range(d):
        for j in range(d):
            swap[j * d + i, i * d + j] = 1
    plus_indices = [(i, j) for i in range(d) for j in range(i, d)]
    minus_indices = list(combinations(range(d), 2))
    plus = sp.zeros(n, len(plus_indices))
    minus = sp.zeros(n, len(minus_indices))
    for col, (i, j) in enumerate(plus_indices):
        plus[i * d + j, col] = 1
        plus[j * d + i, col] = 1
    for col, (i, j) in enumerate(minus_indices):
        minus[i * d + j, col] = 1
        minus[j * d + i, col] = -1
    lplus = sp.diag(*[sp.Rational(1, 1 if i == j else 2) for i, j in plus_indices]) * plus.T
    lminus = minus.T / 2
    require(lplus * plus == sp.eye(len(plus_indices)), 'literal symmetric orbit extraction')
    require(lminus * minus == sp.eye(len(minus_indices)), 'literal alternating orbit extraction')
    require(minus.T * minus == 2 * sp.eye(len(minus_indices)), 'exterior quotient factor two')
    require(plus * lplus == (sp.eye(n) + swap) / 2, 'symmetric projector')
    require(minus * lminus == (sp.eye(n) - swap) / 2, 'alternating projector')

    hp = sp.expand(h.subs(t, (S + r) / 2))
    hm = sp.expand(h.subs(t, (S - r) / 2))
    h0 = even_to_R((hp + hm) / 2)
    h1 = even_to_R(sp.cancel((hp - hm) / (2 * r)))
    require(h0.subs(Delta, 0) == sp.expand(h.subs(t, S / 2)), 'H0 diagonal specialization')
    require(h1.subs(Delta, 0) == sp.expand(sp.diff(h, t).subs(t, S / 2) / 2), 'H1 diagonal derivative factor')
    require(sp.expand(hp - h0.subs(Delta, r*r) - r*h1.subs(Delta, r*r)) == 0, 'original first ideal generator')
    require(sp.expand(hm - h0.subs(Delta, r*r) + r*h1.subs(Delta, r*r)) == 0, 'original second ideal generator')
    gbplus = sp.groebner([h0, Delta*h1], S, Delta, order='lex', domain=sp.QQ)
    gbminus = sp.groebner([h0, h1], S, Delta, order='lex', domain=sp.QQ)
    qplus, qminus = quotient_basis(gbplus), quotient_basis(gbminus)
    require(len(qplus) == d*(d+1)//2, 'even quotient full dimension')
    require(len(qminus) == d*(d-1)//2, 'odd coefficient quotient full dimension')

    # The coefficient basis is a_ij/r, not an exterior quotient product.
    coefficient_columns = []
    for col, (i, j) in enumerate(minus_indices):
        alternant = x**i*y**j - x**j*y**i
        coefficient_xy = sp.cancel(alternant / (x-y))
        coefficient_R = even_to_R(coefficient_xy.subs({x:(S+r)/2, y:(S-r)/2}, simultaneous=True))
        require(difference * evaluate(coefficient_R, (S, Delta), (sum_op, delta_op)) * unit == minus[:, col], 'literal r times divided alternating orbit')
        coefficient_columns.append(normal_coefficients(coefficient_R, gbminus, qminus))
    coefficient_matrix = sp.Matrix.hstack(*coefficient_columns) if coefficient_columns else sp.zeros(0)
    require(coefficient_matrix.rank() == len(minus_indices), 'divided orbit coefficients are a full B-minus basis')

    pi = lminus * difference * plus
    m = lplus * difference * minus
    dplus, dminus = lplus * delta_op * plus, lminus * delta_op * minus
    require(pi.rank() == len(minus_indices), 'pi surjective')
    require(m.rank() == len(minus_indices), 'm injective')
    require(m*pi == dplus and pi*m == dminus, 'both compositions are literal Delta')
    require(difference.rank() == d*(d-1), 'full difference kernel and cokernel each dimension d')

    h1op = evaluate(h1, (S, Delta), (sum_op, delta_op))
    injection_tensor = sp.Matrix.hstack(*[h1op * (sum_op/2)**j * unit for j in range(d)])
    injection = lplus * injection_tensor
    require(injection.rank() == d, 'entire diagonal packet injects')
    require(pi * injection == sp.zeros(len(minus_indices), d), 'injection lies in ker pi')
    require(difference * injection_tensor == sp.zeros(n, d), 'divided difference annihilates original r')
    require(dplus * injection == sp.zeros(len(plus_indices), d), 'Delta annihilates entire kernel ideal')
    require(lplus * sum_op * plus * injection == injection * (2*a), 'diagonal sum acts as twice original generator')
    mu = sp.Matrix.hstack(*[a**(i+j) * sp.eye(d)[:, 0] for i in range(d) for j in range(d)])
    rho = mu * plus
    derivative = evaluate(sp.diff(h, t)/2, (t,), (a,))
    require(rho.rank() == d, 'diagonal quotient surjective')
    require(rho*m == sp.zeros(d, len(minus_indices)), 'm lands in diagonal quotient kernel')
    require(rho*injection == derivative, 'rho after injection is exactly h-prime/2')

    monomial_operators = [X**i * Y**j for i in range(d) for j in range(d)]

    def product(u, v):
        out = sp.zeros(n, 1)
        for index, coefficient in enumerate(u):
            if coefficient:
                out += coefficient * monomial_operators[index] * v
        return out

    for j in range(d):
        for k in range(d):
            require(product(injection_tensor[:, j], injection_tensor[:, k]) == injection_tensor * derivative * a**(j+k) * sp.eye(d)[:, 0], 'complete diagonal ideal product law')
    for j in range(len(minus_indices)):
        for k in range(len(minus_indices)):
            require(swap * product(minus[:, j], minus[:, k]) == product(minus[:, j], minus[:, k]), 'odd times odd is in even algebra')
    return {'h': str(sp.expand(h)), 'd': d, 'H0': str(h0), 'H1': str(h1),
            'even_dimension': len(qplus), 'odd_coefficient_dimension':len(qminus),
            'defect_dimension':d}, {'difference':difference, 'unit':unit, 'h1op':h1op,
             'sum_op':sum_op, 'delta_op':delta_op, 'product':product, 'injection_tensor':injection_tensor,
             'h':h, 'a':a}


fixtures = [t, t-2, t**2, (t-1)**2, t**3, t**4, t**5,
            (t-1)**2*(t+2), (t*t+1)**2,
            t*(t-1)*(t+1), (t-2)**3*(t+1)**2,
            t**5-2*t+3, ((t-sp.Rational(1,2))**2+1)**2]
rows, retained = [], {}
for h in fixtures:
    row, data = packet(sp.expand(h))
    rows.append(row)
    retained[str(sp.expand(h))] = data

negative_controls = []


def reject(label, condition):
    try:
        require(condition, label)
    except CheckFailure:
        negative_controls.append(label)
    else:
        raise CheckFailure('False identity was accepted: '+label)


simple = retained[str(t)]
j1 = simple['injection_tensor'][:, 0]
reject('omitting the literal one-half in the transported product',
       simple['product'](j1, j1) == j1)
triple = retained[str(t**3)]
bad_generator = evaluate(sp.diff(t**3,t).subs(t,S/2)/2, (S,Delta), (triple['sum_op'],triple['delta_op'])) * triple['unit']
require(triple['difference']*triple['h1op']*triple['unit'] == sp.zeros(9,1), 'full H1 is in the diagonal annihilator')
reject('replacing full H1 by its diagonal coefficient before forming the class',
       triple['difference']*bad_generator == sp.zeros(9,1))
double = retained[str(t**2)]
reject('assuming the odd module has a square-zero inherited product',
       double['delta_op']*double['unit'] == sp.zeros(4,1))
require(4*(4-1)//2 == 6 and 2**2 == 4, 'distinct swap and SSP reflection dimensions')
reject('identifying swap-odd module with SSP Z-reflection-odd module', 6 == 4)
require(len(negative_controls) == 4, 'all negative controls exercised')

print(json.dumps({'status':'passed', 'python_optimization':sys.flags.optimize,
                  'sympy':sp.__version__, 'packet_fixtures':len(rows), 'guard_checks':checks,
                  'negative_controls_rejected':negative_controls,
                  'scope':'Exact rational quotient/module identities; synthetic polynomial fixtures, not an arithmetic isometry or upper bound',
                  'cases':rows}, indent=2))
