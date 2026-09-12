#!/usr/bin/env python3
"""Certified moments of the actual arithmetic measure |2 xi(1/2+it)|^2 dt/(2pi).

The proof and exact infinite-tail bound are in tex/arithmetic_moments.tex.
Arb encloses each retained incomplete-gamma term, and the proved tail bound is
added to its radius. No assumed zero locations and no synthetic measure enter.
Finite certificates concern exactly the printed matrix size and cutoff.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from math import comb
from pathlib import Path
import sys

import flint
from flint import arb, arb_mat, ctx


def add(a, b):
    return [((a[k] if k < len(a) else 0) +
             (b[k] if k < len(b) else 0)) for k in range(max(len(a), len(b)))]


def scale(a, c):
    return [c * v for v in a]


def euler_polynomial(p):
    # 2z(P-P'), retaining all coefficients in the original z=pi x^2.
    ans = [0] * (len(p) + 1)
    for k, v in enumerate(p):
        ans[k + 1] += 2 * v
        ans[k] -= 2 * k * v
    return ans


def polynomials(order):
    ps = [[0, -6, 4]]
    for _ in range(order):
        ps.append(euler_polynomial(ps[-1]))
    qs = []
    for j in range(order + 1):
        q = [0]
        for k in range(j + 1):
            q = add(q, scale(ps[k], (-1) ** k * comb(j, k)))
        qs.append(q)
    return ps, qs


def display(x):
    return x.str(65, more=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-order', type=int, default=5)
    parser.add_argument('--cutoff', type=int, default=7)
    parser.add_argument('--dps', type=int, default=110)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.max_order < 1 or args.cutoff < args.max_order + 2 or args.dps < 40:
        parser.error('require max-order >= 1, cutoff >= max-order+2, dps >= 40')
    ctx.dps = args.dps
    ctx.threads = 1
    root = Path(__file__).resolve().parents[1]
    target = args.output or root / 'checks' / 'arithmetic_moments.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    order, cutoff = args.max_order, args.cutoff
    ps, qs = polynomials(order)
    pi = arb.pi()
    half = arb(1) / 2
    records = []

    def record(name, passed, **data):
        records.append(dict(name=name, passed=bool(passed), **data))

    def integral(power, lam):
        s = arb(power) + half
        return lam.gamma_upper(s) / (2 * lam ** s)

    # Cached original-coordinate integrals n^(2a)m^(2b)pi^(a+b) I_(a+b).
    weights = {}
    for n in range(1, cutoff + 1):
        for m in range(1, cutoff + 1):
            lam = pi * (n * n + m * m)
            for k in range(2, 2 * (order + 2) + 1):
                weights[n, m, k] = (pi ** k) * integral(k, lam)

    def finite_entry(i, j, include_reflection=True):
        value = arb(0)
        for n in range(1, cutoff + 1):
            for m in range(1, cutoff + 1):
                for a in range(1, i + 3):
                    for b in range(1, j + 3):
                        c = ps[i][a] * ps[j][b]
                        if include_reflection:
                            c += qs[i][a] * qs[j][b]
                        if c:
                            value += 4 * c * (n ** (2*a)) * (m ** (2*b)) * weights[n, m, a+b]
        return value

    degrees = [j + 2 for j in range(order + 1)]
    caps_p = [sum((abs(v) * pi**a for a, v in enumerate(p)), arb(0)) for p in ps]
    caps_q = [sum((abs(v) * pi**a for a, v in enumerate(q)), arb(0)) for q in qs]
    totals, tails = [], []
    for j, degree in enumerate(degrees):
        ratio = ((arb(cutoff+2)/arb(cutoff+1)) ** (2*degree)
                 * (-pi*(2*cutoff+3)).exp())
        record('geometric_ratio_%d' % j, ratio < 1, enclosure=display(ratio))
        if not ratio < 1:
            raise ArithmeticError('Arb did not certify the explicit tail ratio < 1')
        tail = arb((cutoff+1)**(2*degree)) / (1-ratio)
        total = sum((arb(n**(2*degree)) * (-pi*(n*n-1)).exp()
                     for n in range(1, cutoff+1)), arb(0))
        total += tail * (-pi*((cutoff+1)**2-1)).exp()
        totals.append(total)
        tails.append(tail)

    def error_bound(i, j):
        lam = pi*((cutoff+1)**2+1)
        value = (4*(caps_p[i]*caps_p[j]+caps_q[i]*caps_q[j]) *
                 (tails[i]*totals[j]+totals[i]*tails[j]) *
                 integral(degrees[i]+degrees[j], lam))
        if not value > 0:
            raise ArithmeticError('Positive tail bound not certified')
        return value

    finite, bounds, enclosed = [], [], []
    for i in range(order+1):
        finite_row, bound_row, enclosed_row = [], [], []
        for j in range(order+1):
            val = finite_entry(i, j)
            bound = error_bound(i, j)
            # arb radius conversion rounds upward; bound.upper is directed up.
            cert = val + arb(0, bound.upper())
            finite_row.append(val)
            bound_row.append(bound)
            enclosed_row.append(cert)
        finite.append(finite_row)
        bounds.append(bound_row)
        enclosed.append(enclosed_row)
    for i in range(order+1):
        for j in range(order+1):
            record('symmetry_%d_%d' % (i,j),
                   (enclosed[i][j]-enclosed[j][i]).contains(0))
            if i < order and j < order:
                residual = enclosed[i+1][j]+enclosed[i][j+1]-enclosed[i][j]
                record('Euler_adjoint_%d_%d' % (i,j), residual.contains(0),
                       residual_enclosure=display(residual))

    def endpoint(polynomial):
        return 2*sum((sum((arb(c)*(pi*n*n)**a
                          for a,c in enumerate(polynomial)), arb(0))
                      *(-pi*n*n).exp() for n in range(1,cutoff+1)), arb(0))

    p_end = [endpoint(p) for p in ps]
    q_end = [endpoint(q) for q in qs]
    for i in range(order):
        for j in range(order):
            residual = (finite[i+1][j]+finite[i][j+1]-finite[i][j]
                        -p_end[i]*p_end[j]+q_end[i]*q_end[j])
            record('finite_cutoff_boundary_identity_%d_%d' % (i,j),
                   residual.contains(0), residual_enclosure=display(residual))

    determinants = [arb(1)]
    orthogonal_norms = []
    for size in range(1, order+2):
        matrix = arb_mat([[enclosed[i][j] for j in range(size)] for i in range(size)])
        determinant = matrix.det()
        determinants.append(determinant)
        record('positive_actual_Gram_determinant_%d' % size, determinant > 0,
               enclosure=display(determinant))
        norm = determinants[-1]/determinants[-2]
        orthogonal_norms.append(norm)
        record('positive_actual_monic_norm_%d' % (size-1), norm > 0,
               enclosure=display(norm))

    # Exact parity: reflected Euler polynomials, and arithmetic measure moments.
    for j in range(order):
        reflected_next = add(qs[j], scale(euler_polynomial(qs[j]), -1))
        record('reflected_polynomial_recurrence_%d' % j,
               reflected_next == qs[j+1], coefficients=reflected_next)
    for k in range(order+1):
        coeffs = [arb(comb(k,a))*(-half)**(k-a) for a in range(k+1)]
        central = sum((coeffs[i]*coeffs[j]*enclosed[i][j]
                       for i in range(k+1) for j in range(k+1)), arb(0))
        record('positive_actual_even_t_moment_%d' % (2*k), central > 0,
               enclosure=display(central))

    # Wrong omitted x<1 part and wrong Theta factor both must be excluded.
    wrong_half = finite_entry(0,0,False)
    record('negative_control_omitted_reflection', not enclosed[0][0].overlaps(wrong_half),
           wrong_enclosure=display(wrong_half))
    record('negative_control_lost_theta_factor_two',
           not enclosed[0][0].overlaps(enclosed[0][0]/4))
    # A wrong adjoint D*=-D would claim h10+h01=0.
    record('negative_control_lost_dx_shift',
           not (enclosed[1][0]+enclosed[0][1]).contains(0))

    if order == 5 and cutoff == 7 and args.dps >= 80:
        table_moments = [
            (0,0,'1.279007247846485140480','4.67e-22'),
            (0,1,'0.6395036239232425702398','3.33e-23'),
            (0,2,'-12.73579749060893715027','2.81e-21'),
            (1,1,'13.37530111453217972051','2.57e-21'),
            (1,2,'6.687650557266089860256','2.85e-22'),
            (2,2,'389.8820543216399270934','1.65e-20')]
        table_norms = [
            ('1.279007247846485140480','4.67e-22'),
            ('13.05554930257055843539','2.69e-21'),
            ('250.0089768190499145175','4.88e-20'),
            ('6694.666685525627506773','4.76e-19'),
            ('224298.1953314520556463','9.95e-18'),
            ('9383436.471794727053469','2.54e-16')]
        for i,j,c,r in table_moments:
            # Compare exact-decimal interval endpoints outwards, without
            # treating a widened parsed-radius interval as the printed one.
            inside = ((enclosed[i][j] - arb(c)).abs_upper() < arb(r))
            record('printed_moment_interval_%d_%d' % (i,j), inside,
                   decimal_center=c, decimal_radius=r)
        for k,(c,r) in enumerate(table_norms):
            inside = ((orthogonal_norms[k]-arb(c)).abs_upper() < arb(r))
            record('printed_monic_norm_interval_%d' % k, inside,
                   decimal_center=c, decimal_radius=r)
        record('printed_h00_analytic_tail_bound', bounds[0][0] < arb('1.150030e-83'))
        record('printed_all_analytic_tail_bounds',
               all(v < arb('2.961369e-63') for row in bounds for v in row))

    payload = dict(
        generated_utc=datetime.now(timezone.utc).isoformat(),
        status='pass' if all(r['passed'] for r in records) else 'fail',
        scope=('Certified finite original arithmetic moment matrix and its principal '
               'determinants using Arb plus the proved infinite double-series tail. '
               'This does not certify RH, zeros, an infinite asymptotic estimate, or all degrees.'),
        source=dict(phi_star='(4*pi^2*x^4-6*pi*x^2)*exp(-pi*x^2)',
                    theta='2*sum(phi_star(n*x), n>=1)', D='-x*d/dx',
                    measure='abs(2*xi(1/2+i*t))^2*dt/(2*pi)'),
        parameters=dict(max_order=order, cutoff=cutoff, precision_decimal_digits=args.dps),
        backend=dict(python=sys.version, python_flint=flint.__version__, optimized=not __debug__),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        proof_sha256=hashlib.sha256((root/'tex/arithmetic_moments.tex').read_bytes()).hexdigest()
            if (root/'tex/arithmetic_moments.tex').exists() else None,
        P_coefficients=ps, Q_coefficients=qs,
        finite_double_sums=[[display(v) for v in row] for row in finite],
        proved_absolute_tail_bounds=[[display(v) for v in row] for row in bounds],
        actual_moment_enclosures=[[display(v) for v in row] for row in enclosed],
        actual_monic_orthogonal_norms=[display(v) for v in orthogonal_norms],
        checks=records,
        counts=dict(passed=sum(r['passed'] for r in records), total=len(records)))
    target.write_text(json.dumps(payload, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(status=payload['status'], checks=payload['counts'], output=str(target),
                          h00=display(enclosed[0][0]),
                          last_Gram_determinant=display(determinants[-1]))))
    return 0 if payload['status']=='pass' else 1


if __name__=='__main__':
    raise SystemExit(main())
