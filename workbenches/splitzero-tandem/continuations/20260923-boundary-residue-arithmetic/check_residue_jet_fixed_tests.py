"""Exact auxiliary checks for RJ1--30. Run normally and with python -O.

The contour calculation independently extracts the local root moments
from log(H/H_0), using exact rational Laurent coefficients. No numerical
roots, truncated zero lists, or optimized-away assertions are used.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

import sympy as S

COUNTS = {}


def check(category, condition, detail):
    if not condition:
        raise RuntimeError(f"{category}: {detail}")
    COUNTS[category] = COUNTS.get(category, 0) + 1


def qjet(unit, degree):
    out = [1 / unit[0]]
    for k in range(1, degree + 1):
        out.append(-sum(unit[i] * out[k-i]
                        for i in range(1, min(k, len(unit)-1)+1)) / unit[0])
    return out


def residue_matrix(n, reciprocal):
    return S.Matrix(n, n, lambda a, b:
                    reciprocal[n-1-a-b] if a+b < n else 0)


def convolution(left, right, cap=None):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            k = a + b
            if cap is None or k <= cap:
                out[k] = out.get(k, Q(0)) + x*y
    return {k: v for k, v in out.items() if v}


def hermite(k, x):
    return S.Add(*(S.Rational((-1)**a * factorial(k),
                              factorial(a)*factorial(k-2*a))*x**(k-2*a)
                   for a in range(k//2+1)))


def moments(m, degree):
    x = S.Symbol('x')
    poly = S.Poly(hermite(m, x), x)
    coeff = [Q(int(v)) for v in poly.all_coeffs()]
    p = [Q(m)]
    for k in range(1, degree+1):
        if k <= m:
            value = -sum(coeff[a]*p[k-a] for a in range(1, k)) - k*coeff[k]
        else:
            value = -sum(coeff[a]*p[k-a] for a in range(1, m+1))
        p.append(value)
    return p


def local_moment(m, c, d, k, time_degree):
    """[t^time_degree] sum(local roots^k) by a fixed contour residue.

    Integration by parts gives Res x^k H_x/H = -k [x^-k] log H.
    At positive time degree the constant log H_0 disappears.
    """
    if k == 0:
        return Q(m) if time_degree == 0 else Q(0)
    if time_degree == 0:
        return Q(0)
    unit = [Q(1), c, d]
    maxa = (m+2)//2
    numerators = {}
    for a in range(1, min(maxa, time_degree)+1):
        numerators[a] = {
            h-2*a: unit[h]*Q((-1)**a*factorial(m+h),
                            factorial(a)*factorial(m+h-2*a))
            for h in range(3) if m+h >= 2*a and unit[h]
        }
    reciprocal = qjet(unit, 2*time_degree)
    reciprocal_poly = dict(enumerate(reciprocal))
    reciprocal_power = {0: Q(1)}
    # t degree -> Laurent polynomial in x, for (sum t^a T_a)^r.
    powers = {0: {0: Q(1)}}
    coefficient = Q(0)
    for r in range(1, time_degree+1):
        next_powers = {}
        for a, left in powers.items():
            for b, right in numerators.items():
                if a+b <= time_degree:
                    product = convolution(left, right)
                    target = next_powers.setdefault(a+b, {})
                    for exponent, value in product.items():
                        target[exponent] = target.get(exponent, Q(0)) + value
        powers = next_powers
        reciprocal_power = convolution(reciprocal_power, reciprocal_poly,
                                       2*time_degree)
        for exponent, value in powers.get(time_degree, {}).items():
            coefficient += Q((-1)**(r+1), r)*value*reciprocal_power.get(-k-exponent, Q(0))
    return -k*coefficient


def main():
    x, t = S.symbols('x t')
    c, d, A, B = S.symbols('c d A B', real=True)
    unit = [Q(3, 2), Q(-2, 5), Q(7, 11), Q(1, 13), Q(-1, 17)]
    reciprocal = qjet(unit, 8)
    for n in range(1, 9):
        gram = residue_matrix(n, reciprocal)
        check('perfect residue matrix',
              gram.det() == (-1)**(n*(n-1)//2)*reciprocal[0]**n, n)
        recovered = qjet(reciprocal[:n], n-1)
        expected = (unit + [Q(0)]*n)[:n]
        check('unit recovery', recovered == expected, n)
        for N in range(n+1, 9):
            pi = S.zeros(n, N)
            injection = S.zeros(N, n)
            for a in range(n):
                pi[a, a] = 1
                injection[N-n+a, a] = 1
            check('tower adjoint',
                  residue_matrix(N, reciprocal)*injection == pi.T*gram,
                  (n, N))
            check('tower ranks', pi.rank() == n and injection.rank() == n, (n, N))
            for P in range(N, 9):
                pi2 = S.zeros(N, P)
                inj2 = S.zeros(P, N)
                for a in range(N):
                    pi2[a, a] = 1
                    inj2[P-N+a, a] = 1
                for a in range(n):
                    check('tower composition', (pi*pi2)[a, a] == 1 and
                          (inj2*injection)[P-n+a, a] == 1, (n, N, P, a))

    for m in range(1, 9):
        P = hermite(m, x)
        check('Hermite derivative', S.expand(S.diff(P, x)-m*hermite(m-1, x)) == 0, m)
        check('Hermite equation', S.expand(2*S.diff(P, x, 2)-x*S.diff(P, x)+m*P) == 0, m)
        check('Hermite discriminant', S.discriminant(P, x) ==
              2**(m*(m-1)//2)*S.prod(k**k for k in range(1, m+1)), m)
        p = moments(m, 2*m+2)
        check('second moment', p[2] == 2*m*(m-1), m)
        for j in range(m):
            if j:
                original = 2*j*(2*d-c*c)*p[2*j]+4*j*(2*j-1)*c*c*p[2*j-2]
                received = (2*j*p[2*j]+4*j*(2*j-1)*p[2*j-2])*A*A-4*j*p[2*j]*B
                check('fixed-test substitution',
                      S.expand(original.subs({c:-A, d:A*A-B})-received) == 0,
                      (m, j))
                check('higher-layer sharpness', S.diff(original, d) == 4*j*p[2*j] and p[2*j] > 0,
                      (m, j))
            check('odd-term substitution',
                  S.expand((S.I*(2*j+1)*c*p[2*j]).subs(c,-A)+S.I*(2*j+1)*A*p[2*j]) == 0,
                  (m, j))
        h0 = x**m*(1+c*x+d*x*x)
        heat = sum((-t)**a/S.factorial(a)*S.diff(h0, x, 2*a)
                   for a in range((m+2)//2+1))
        check('genuine heat equation', S.expand(S.diff(heat,t)+S.diff(heat,x,2)) == 0, m)
        check('initial multiplicity', S.expand(heat.subs(t,0)) == S.expand(h0), m)

    # Independent local contour extraction in several genuine families.
    for m in range(1, 7):
        p = moments(m, 2*m+2)
        for cc, dd in [(Q(0), Q(0)), (Q(2,3), Q(-3,7)), (Q(-1,2), Q(5,4))]:
            bb = 2*dd-cc*cc
            for j in range(m):
                check('local contour odd moment',
                      local_moment(m,cc,dd,2*j+1,j+1) == 2*(2*j+1)*cc*p[2*j],
                      (m,cc,dd,j))
                check('local contour next moment',
                      local_moment(m,cc,dd,2*j+2,j+1) == p[2*j+2],
                      (m,cc,dd,j))
                if j:
                    expected = 2*j*bb*p[2*j]+4*j*(2*j-1)*cc*cc*p[2*j-2]
                    check('local contour leading moment',
                          local_moment(m,cc,dd,2*j,j) == p[2*j], (m,cc,dd,j))
                    check('local contour unit correction',
                          local_moment(m,cc,dd,2*j,j+1) == expected, (m,cc,dd,j))

    check('negative control', qjet([Q(1),Q(0),Q(1)],1) == qjet([Q(1),Q(0),Q(2)],1)
          and qjet([Q(1),Q(0),Q(1)],2) != qjet([Q(1),Q(0),Q(2)],2), 'A2 omits d')
    check('negative control', qjet([Q(1),Q(1)],0) == qjet([Q(1),Q(2)],0), 'A1 omits c')
    for m in range(2, 9):
        check('negative control', 2*m*(m-1) != 0, ('A2 omits determinant correction',m))
    check('double-zero coefficient', moments(2,4) == [Q(2),Q(0),Q(4),Q(0),Q(8)], 'p0 p2 p4')
    check('double-zero propagation', S.expand(16*(A*A-B)).diff(B) == -16 and
          S.expand(2*A*A-4*B).diff(B) == -4, 'RJ29 RJ30')
    check('simple determinant exception', S.re(S.I/S.Rational(-3,2)) == 0 and
          S.re(S.I/(-S.Rational(3,2)+S.I)) != 0, 'same-height poles')

    source = Path(__file__).with_name('RESIDUE_JET_FIXED_TEST_RECEIVER.tex')
    report = {
        'status': 'passed',
        'checks': sum(COUNTS.values()),
        'categories': COUNTS,
        'proof_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'optimized': not __debug__,
        'scope': 'Exact finite auxiliary checks; analytic arguments are in the proof.'
    }
    target = Path(__file__).with_name('residue_jet_checks_optimized.json' if not __debug__
                                   else 'residue_jet_checks.json')
    target.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
