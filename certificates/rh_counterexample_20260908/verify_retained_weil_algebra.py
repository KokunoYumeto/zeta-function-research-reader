"""Exact regression checks for the retained Weil test algebra.

The full function-space proofs are in satellite 24. These checks certify
the displayed algebraic identities, not RH, source theorems, analytic
continuity, or the implementation of a proof assistant.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'retained_weil_algebra_results.json'


def checks():
    s, u, v, lam = sp.symbols('s u v lam', real=True)
    R = sp.Matrix([[0, -2*s], [1, 0]])
    B = sp.diag(2, -4*s)
    passed = []

    def check(label, statement):
        assert statement, label
        passed.append(label)

    check('root_square_factor_minus_two', R**2 == -2*s*sp.eye(2))
    check('componentwise_adjoint', R.T == sp.Matrix([[0, 1], [-2*s, 0]]))
    check('branch_trace_symmetry', R.T*B == B*R)
    check('positive_real_fibre_negative_trace_control',
          (sp.Matrix([[0, 1]])*B.subs(s, 1)*sp.Matrix([0, 1]))[0] == -4)
    for n in range(6):
        check(f'exact_even_power_{2*n}', R**(2*n) == (-2*s)**n*sp.eye(2))
        check(f'exact_odd_power_{2*n+1}', R**(2*n+1) == (-2*s)**n*R)
    coeffs = [sp.Rational(2, 3), -5, sp.I, 7, sp.Rational(-3, 2), 2-sp.I]
    A = sum(coeffs[2*n]*(-2*s)**n for n in range(3))
    C = -2*s*sum(coeffs[2*n+1]*(-2*s)**n for n in range(3))
    polyR = sum((coeffs[j]*R**j for j in range(len(coeffs))), sp.zeros(2))
    check('complex_polynomial_channel',
          sp.simplify(polyR[0, 0]-A) == 0 and sp.simplify(polyR[0, 1]-C) == 0)
    check('colliding_channel',
          sp.simplify((R*(R**2+2*lam*sp.eye(2)))[0, 1]-4*s*(s-lam)) == 0)
    d, a, c = 2*(s-1)**2, s+2, 3*s
    bez_u, bez_v = sp.Rational(1, 2), sp.Rational(-1, 6)
    check('bezout_constant_preserved', sp.expand(bez_u*a+bez_v*c) == 1)
    check('channel_kernel', sp.expand(d*a*(-c)+d*c*a) == 0)
    check('channel_section', sp.expand(d*a*bez_u+d*c*bez_v-d) == 0)
    check('kernel_parameter_inverse', sp.expand(-bez_v*(-c)+bez_u*a) == 1)

    f = u**5+(2+sp.I)*u**3+1
    star = lambda h: sp.conjugate(h.subs(u, -u))
    T = lambda h: -sp.I*sp.diff(h, u)
    check('derivative_star_sign', sp.simplify(star(T(f))-T(star(f))) == 0)
    check('conjugated_factor_operator',
          sp.simplify(T(sp.exp(sp.I*lam*u)*f)-lam*sp.exp(sp.I*lam*u)*f
                      -sp.exp(sp.I*lam*u)*T(f)) == 0)

    # Piecewise polynomial examples have C^9 matching at the endpoints.
    # They are finite-order regressions, not replacements of E=C_c^infty.
    bump = (1-u*u)**10
    check('finite_order_control_endpoint_jets',
          all(sp.diff(bump, u, j).subs(u, e) == 0 for j in range(10) for e in (-1, 1)))
    for k in range(1, 5):
        g = (-sp.I)**k*sp.diff(bump, u, k)
        moments = [sp.integrate(v**j*g.subs(u, v), (v, -1, 1)) for j in range(k)]
        check(f'primitive_moments_order_{k}', all(m == 0 for m in moments))
        primitive = sp.I**k/sp.factorial(k-1)*sp.integrate(
            (u-v)**(k-1)*g.subs(u, v), (v, -1, u))
        check(f'primitive_inverse_order_{k}', sp.expand(primitive-bump) == 0)

    phi = 1+s*s
    nodes = [(sp.Integer(0), 2, [1, 2]), (1+sp.I, 3, [3, sp.I, -2])]
    Q = 0
    for z, k, values in nodes:
        M = sp.prod((s-other)**degree for other, degree, _ in nodes if other != z)
        H = sum(values[j]*(s-z)**j for j in range(k))
        ratio = H/(M*phi)
        Aj = sum(sp.cancel(sp.diff(ratio, s, j).subs(s, z))/sp.factorial(j)*(s-z)**j
                 for j in range(k))
        Q += M*Aj
    Q = sp.Poly(sp.expand(Q), s).as_expr()
    check('Hermite_interpolant_degree', sp.degree(Q, s) <= sum(k for _, k, _ in nodes)-1)
    for z, k, values in nodes:
        check(f'Hermite_jets_at_{z}',
              all(sp.simplify(sp.diff(Q*phi, s, j).subs(s, z)/sp.factorial(j)-values[j]) == 0
                  for j in range(k)))
    arbitrary = s**8+(1+sp.I)*s**5+7*s-3
    for j in range(5):
        lhs = sp.diff(s*arbitrary, s, j)/sp.factorial(j)
        rhs = s*sp.diff(arbitrary, s, j)/sp.factorial(j)
        if j:
            rhs += sp.diff(arbitrary, s, j-1)/sp.factorial(j-1)
        check(f'factorial_jet_shift_{j}', sp.expand(lhs-rhs) == 0)
    Sjet = sp.Matrix([[lam, 0, 0], [1, lam, 0], [0, 1, lam]])
    Rjet = sp.BlockMatrix([[sp.zeros(3), -2*Sjet], [sp.eye(3), sp.zeros(3)]]).as_explicit()
    check('multiplicity_retained_in_root_square',
          Rjet**2 == -2*sp.diag(Sjet, Sjet))
    return {'status': 'pass', 'checks': passed,
            'scope': 'exact algebra and finite-order regression; full analytic proofs in satellite 24',
            'proof_assistant_verified': False, 'RH_counterexample': False,
            'trust_boundary': 'Python and SymPy exact arithmetic; no numerical zero test'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = checks()
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.write:
        RECEIPT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    else:
        assert json.loads(RECEIPT.read_text(encoding='utf-8')) == result, 'Stale receipt'
    print('RETAINED_WEIL_ALGEBRA_OK ' + json.dumps(result))


if __name__ == '__main__':
    main()
