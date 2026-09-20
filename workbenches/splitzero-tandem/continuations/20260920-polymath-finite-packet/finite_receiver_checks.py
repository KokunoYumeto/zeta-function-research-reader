"""Bounded exact symbolic checks and an Arb source-error certificate for PMH.

This is not an RH test. It checks one small, explicitly stated disk and the
coordinate/cutoff/jet identities. Original functions and their factors remain
unchanged. All analytic claims are proved in POLYMATH_NATIVE_HEAT_RECEIVER.tex.
"""
import json
import math
import sys
import sympy as sp
from flint import acb, arb, ctx
_require_count = 0

def require(predicate, message='A verification predicate failed.'):
    """Checks remain active under python -O and -OO."""
    global _require_count
    _require_count += 1
    if not predicate:
        raise RuntimeError(message)

def corrected_rtn_constant_checks():
    """Finite arithmetic in the corrected Gaussian proof; see Appendix A."""
    ctx.dps = 80
    a_min = (arb(100) / (2 * arb.pi())).sqrt()
    require(a_min > 3)
    c = arb(11) / 12
    log3 = arb(3).log()
    logsqrt2 = arb(2).log() / 2
    A = c + (1 + log3 / 2) ** 2 + arb(1) / 4
    absorbed = arb('.2') * (log3 ** 2 / 2 + (A - arb('3.49')) / 96).exp()
    require(A > arb('3.49') and absorbed < arb('.366'))
    require(arb('.029') * (logsqrt2 ** 2 / 2).exp() < arb('.031'))
    require(logsqrt2 < 1)
    require(arb('.036') * arb('.445') * arb.pi().sqrt() < arb('.0285'))
    require(arb('.036') * arb('.247') < arb('.0285') * arb('.353'))
    require(arb('.036') * arb('.098') < arb('.0285') * arb('.353') ** 2)
    require(arb('.445') ** 2 / (1 - arb('.445') ** 2) < arb('.247'))
    require(arb('.445') ** 3 * arb.pi().sqrt() / (2 * (1 - arb('.445') ** 2)) < arb('.098'))
    require(arb(2).sqrt() / (4 * arb.pi() ** 2) < arb('.036'))
    require(1 / ((3 - 2 * arb(2).log()) * arb.pi()).sqrt() < arb('.445'))
    require(arb(2).sqrt() * arb.pi().sqrt() / (4 * arb.pi()) < arb('.2'))
    require(arb('1.1') ** 2 / 7 < arb('.173'))
    v_bounds = []
    for r in (32, 33):
        gamma = arb(math.factorial(15)) if r == 32 else arb(math.factorial(32)) * arb.pi().sqrt() / (arb(4) ** 16 * math.factorial(16))
        v = arb(1) / 2 * arb('1.1') ** r * gamma * (arb(r - 1) / 2) ** (arb(1 - r) / 2)
        require(v < arb('.0005'))
        v_bounds.append(str(v))
    require(arb('1.21') * (-arb(31) / 33).exp() < 1)
    high_bounds = []
    for k in (14, 15):
        gamma = arb(math.factorial(6)) if k == 14 else arb(math.factorial(14)) * arb.pi().sqrt() / (arb(4) ** 7 * math.factorial(7))
        f = arb('1.1') ** k * gamma * (-(k - 4) ** 2 + (k - 4) * arb(2).log()).exp()
        require(f < arb('1e-30'))
        high_bounds.append(str(f))
    require(arb('2.42') * 14 * arb(-44).exp() < 1)
    require(2 * arb('1e-30') < arb('.007936'))
    require(arb('3.49') - arb(10) / 3 > 0)
    require(arb('3.49') * 94 - arb(10) / 3 * 96 > 0)
    require((1 + c / 100) / 97 < 1)
    return {'corrected_pointwise_constant_c': '11/12', 'delta1_A': str(A), 'delta1_absorbed_coefficient': str(absorbed), 'reserved_optimal_remainder_bases': v_bounds, 'high_tail_bases': high_bounds, 'unchanged_final_constants': ['0.397', '0.865', '5/3', '3.49']}

def symbolic_checks():
    s, t, q = sp.symbols('s t q')
    ell = sp.symbols('ell', real=True)
    alpha = 1 / (2 * q) + 1 / (q - 1) + sp.log(q / (2 * sp.pi)) / 2
    for r in range(1, 8):
        explicit = (-1) ** r * sp.factorial(r) / (2 * q ** (r + 1)) + (-1) ** r * sp.factorial(r) / (q - 1) ** (r + 1) + (-1) ** (r - 1) * sp.factorial(r - 1) / (2 * q ** r)
        require(sp.simplify(sp.diff(alpha, q, r) - explicit) == 0)
    lam = alpha - ell + t * (alpha - ell) * sp.diff(alpha, q) / 2
    log_term = sp.log(q) + sp.log(q - 1) - q * sp.log(sp.pi) / 2 + (q / 2 - sp.Rational(1, 2)) * sp.log(q / 2) - q / 2 + t * alpha ** 2 / 4 + t * ell ** 2 / 4 - (q + t * alpha / 2) * ell
    require(sp.simplify(sp.diff(log_term, q) - lam) == 0)
    require(sp.simplify(sp.diff(log_term, t) - (alpha - ell) ** 2 / 4) == 0)
    z = sp.symbols('z')
    polynomial = sum(((j + 2) * z ** j for j in range(11)))
    coordinate = -2 * sp.I * (s - sp.Rational(1, 2))
    for j in range(9):
        left = sp.diff(16 * polynomial.subs(z, coordinate), s, j)
        right = 16 * (-2 * sp.I) ** j * sp.diff(polynomial, z, j).subs(z, coordinate)
        require(sp.expand(left - right) == 0)
    terms = sp.symbols('T1:10')
    for n in range(9):
        for k in range(9):
            signed = sum(terms[k:n]) if n >= k else -sum(terms[n:k])
            require(sp.expand(sum(terms[:n]) - sum(terms[:k]) - signed) == 0)
    roots = [1 + sp.I, 1 + sp.I, -2 + 3 * sp.I, -2 + 3 * sp.I, -2 + 3 * sp.I]
    powers = [None] + [sp.expand(sum((r ** j for r in roots))) for j in range(1, 6)]
    elementary = [sp.Integer(1)]
    for k in range(1, 6):
        elementary.append(sp.expand(sum(((-1) ** (j - 1) * elementary[k - j] * powers[j] for j in range(1, k + 1))) / k))
    reconstructed = sum(((-1) ** k * elementary[k] * s ** (5 - k) for k in range(6)))
    require(sp.expand(reconstructed - sp.prod((s - r for r in roots))) == 0)
    h = sp.symbols('h')
    local_unit = 7 + 3 * h - 2 * h ** 2 + 5 * h ** 3 + 11 * h ** 4
    coefficients = [local_unit.coeff(h, j) for j in range(5)]
    quotient = []
    for r in range(4):
        quotient.append(sp.cancel(((r + 1) * coefficients[r + 1] - sum((coefficients[k] * quotient[r - k] for k in range(1, r + 1)))) / coefficients[0]))
    require(sp.series(sp.diff(local_unit, h) / local_unit - sum((quotient[r] * h ** r for r in range(4))), h, 0, 4).removeO() == 0)
    return {'alpha_derivatives_orders': [1, 7], 'coordinate_jet_orders': [0, 8], 'cutoff_pairs': 81, 'packet_degree': 5, 'packet_multiplicities': [2, 3], 'local_unit_jet_orders': [0, 3]}

def alpha(q):
    return 1 / (2 * q) + 1 / (q - 1) + (q / (2 * arb.pi())).log() / 2

def alpha_prime(q):
    return -1 / (2 * q ** 2) - 1 / (q - 1) ** 2 + 1 / (2 * q)

def alpha_second(q):
    return 1 / q ** 3 + 2 / (q - 1) ** 3 - 1 / (2 * q ** 2)

def m0(q):
    return arb(1) / 8 * (q * (q - 1) / 2) * (-q * arb.pi().log() / 2).exp() * (2 * arb.pi()).sqrt() * ((q / 2 - arb(1) / 2) * (q / 2).log() - q / 2).exp()

def mt(q, t):
    return (t * alpha(q) ** 2 / 4).exp() * m0(q)

def term(q, t, n):
    ell = arb(n).log()
    return mt(q, t) * (t * ell ** 2 / 4 - (q + t * alpha(q) / 2) * ell).exp()

def term_prime(q, t, n):
    ell = arb(n).log()
    lam = alpha(q) - ell + t * (alpha(q) - ell) * alpha_prime(q) / 2
    return term(q, t, n) * lam

def term_second(q, t, n):
    ell = arb(n).log()
    lam = alpha(q) - ell + t * (alpha(q) - ell) * alpha_prime(q) / 2
    lam_prime = alpha_prime(q) + t * (alpha_prime(q) ** 2 + (alpha(q) - ell) * alpha_second(q)) / 2
    return term(q, t, n) * (lam ** 2 + lam_prime)

def eps(q, t, n):
    ell = arb(n).log()
    return ((t ** 2 / 8 * abs(alpha(q) - ell) ** 2 + t / 4 + arb(1) / 6) / (abs(q.imag) - arb('3.33'))).exp() - 1

def tilde_eps(q, t):
    tau = abs(q.imag)
    a = ((tau + arb.pi() * t / 8) / (2 * arb.pi())).sqrt()
    return (arb('0.397') * (q.real * arb(9).log()).exp() / (a - arb('0.865')) + 5 / (3 * (tau - 6))) * (arb('3.49') / (tau - 4)).exp()

def source_error(s, t, n):
    tau = s.imag
    tp = tau + arb.pi() * t / 8
    ea = sum((abs(term(s, t, k)) * eps(s, t, k) for k in range(1, n + 1)))
    eb = sum((abs(term(1 - s, t, k)) * eps(1 - s, t, k) for k in range(1, n + 1)))
    ec = (t * arb.pi() ** 2 / 64).exp() * abs(m0(acb(0, tp))) * (1 + tilde_eps(s, t) + tilde_eps(1 - s, t))
    return 16 * (ea + eb + ec)

def finite_certificate():
    ctx.dps = 80
    t = arb(1) / 4
    center = acb(arb(1) / 4, 128)
    radius = arb(1) / 32
    half_side = arb(1) / 256
    box = acb(arb(arb(1) / 4, radius), arb(128, radius))
    cutoff_argument = box.imag / (2 * arb.pi()) + t / 16
    n = 4
    require(cutoff_argument > n * n)
    require(cutoff_argument < (n + 1) ** 2)
    require(box.real > 0 and box.real < 1 and (box.imag > 100))
    q_center = 16 * sum((term(center, t, k) + term(1 - center, t, k) for k in range(1, n + 1)))
    q1 = 16 * sum((term_prime(box, t, k) - term_prime(1 - box, t, k) for k in range(1, n + 1)))
    u1 = abs(q1).upper()
    eta0 = source_error(box, t, n).upper()
    reach = arb(2).sqrt() * half_side
    a = abs(q_center).lower() - reach.upper() * u1
    margin = a - eta0
    require(margin > 0, 'The stated finite certificate did not pass.')
    require(margin > arb('2.29e-40'))
    require(eta0 < arb('2.42e-40'))
    require(u1 < arb('1.71e-39'))
    derivative_radius = radius - reach
    eta1 = eta0 / derivative_radius
    eta2 = 2 * eta0 / derivative_radius ** 2
    delta1 = eta1 / margin + u1 * eta0 / (a * margin)
    return {'precision_decimal_digits': ctx.dps, 'time': '1/4', 'center_s': '1/4 + 128 i', 'outer_disk_radius_s': '1/32', 'square_half_side_s': '1/256', 'canonical_cutoff': n, 'canonical_cutoff_argument': str(cutoff_argument), 'literal_abs_Q_center': str(abs(q_center)), 'source_eta0_upper': str(eta0), 'Qprime_upper': str(u1), 'finite_stopping_margin': str(margin), 'eta1': str(eta1), 'eta2': str(eta2), 'delta1': str(delta1), 'enclosed_g_zero_count': 0, 'scope': 'Only the stated small square at t=1/4; not RH or an all-height certificate.'}

def nonempty_packet_certificate(expected_count=1, requested_cutoff=4):
    """A bounded, actual one-root packet: 128 contour segments, cutoff 4."""
    t0 = arb(1) / 4
    time_half_width = arb(1) / 4096
    t = arb(t0, time_half_width)
    require(t > 0 and t < arb(1) / 2)
    radius = arb(1) / 16
    n = requested_cutoff
    vertices = [acb(arb(1) / 10, arb(507) / 4), acb(arb(9) / 10, arb(507) / 4), acb(arb(9) / 10, arb(513) / 4), acb(arb(1) / 10, arb(513) / 4)]
    steps = 32
    nodes = []
    for edge in range(4):
        start, end = (vertices[edge], vertices[(edge + 1) % 4])
        nodes.extend((start + (end - start) * j / steps for j in range(steps)))

    def value(s):
        return 16 * sum((term(s, t0, k) + term(1 - s, t0, k) for k in range(1, n + 1)))
    minimum_margin = None
    maximum_delta1 = arb(0)
    velocity_bound = arb(0)
    phase = arb(0)
    values = [value(node) for node in nodes]
    for j, start in enumerate(nodes):
        end = nodes[(j + 1) % len(nodes)]
        center = (start + end) / 2
        length = abs(end - start)
        reach = length / 2
        box = acb(arb(center.real, radius), arb(center.imag, radius))
        require(box.real > 0 and box.real < 1 and (box.imag > 100))
        cutoff_argument = box.imag / (2 * arb.pi()) + t / 16
        require(cutoff_argument > n * n and cutoff_argument < (n + 1) ** 2)
        q_center = value(center)
        q1 = 16 * sum((term_prime(box, t, k) - term_prime(1 - box, t, k) for k in range(1, n + 1)))
        u1 = abs(q1).upper()
        qt = 16 * sum(((term(box, t, k) * (alpha(box) - arb(k).log()) ** 2 + term(1 - box, t, k) * (alpha(1 - box) - arb(k).log()) ** 2) / 4 for k in range(1, n + 1)))
        ut = abs(qt).upper()
        eta0 = source_error(box, t, n).upper()
        a = abs(q_center).lower() - reach.upper() * u1 - time_half_width * ut
        margin = a - eta0
        require(margin > 0, f'Packet boundary segment {j} failed.')
        if minimum_margin is None or margin.lower() < minimum_margin:
            minimum_margin = margin.lower()
        d = radius - reach
        eta1 = eta0 / d
        eta2 = 2 * eta0 / d ** 2
        delta1 = (eta1 / margin + u1 * eta0 / (a * margin)).upper()
        if delta1 > maximum_delta1:
            maximum_delta1 = delta1
        q2 = 16 * sum((term_second(box, t, k) + term_second(1 - box, t, k) for k in range(1, n + 1)))
        u2 = abs(q2).upper()
        velocity_bound += length.upper() * (u2 + eta2) / (8 * arb.pi() * margin)
        ratio = values[(j + 1) % len(nodes)] / values[j]
        require(ratio.real > 0)
        phase += ratio.arg()
    winding = phase / (2 * arb.pi())
    require(winding > arb(expected_count) - arb(1) / 2 and winding < arb(expected_count) + arb(1) / 2, 'The winding interval rejects the requested count.')
    require(minimum_margin > arb('1.0e-42'))
    require(minimum_margin > arb('1.2475e-41') and minimum_margin < arb('1.2476e-41'))
    require(velocity_bound < 1102)
    return {'time_interval': ['1023/4096', '1025/4096'], 'rectangle_real': ['1/10', '9/10'], 'rectangle_imag': ['507/4', '513/4'], 'orientation': 'counterclockwise', 'segments': len(nodes), 'outer_disk_radius_s': '1/16', 'canonical_cutoff': n, 'minimum_stopping_margin': str(minimum_margin), 'winding_interval': str(winding), 'enclosed_g_zero_count': 1, 'maximum_log_derivative_error_delta1': str(maximum_delta1), 'moving_root_speed_upper': str(velocity_bound.upper()), 'full_exterior_at_root_upper': str((2 * velocity_bound).upper()), 'scope': 'One moving simple packet throughout the stated time interval, certified without an assumed zero location or real-zero hypothesis.'}

def deliberate_failure(name):
    """Each branch mutates one required feature and must raise RuntimeError."""
    s, z, h = sp.symbols('s z h')
    coordinate = -2 * sp.I * (s - sp.Rational(1, 2))
    original = 16 * (1 + z + z ** 2).subs(z, coordinate)
    if name == 'missing_factor16':
        altered = (1 + z + z ** 2).subs(z, coordinate)
        require(sp.expand(original - altered) == 0, 'Rejected missing original factor 16.')
    elif name == 'wrong_coordinate_sign':
        altered = 16 * (2 * sp.I) * sp.diff(1 + z + z ** 2, z).subs(z, coordinate)
        require(sp.expand(sp.diff(original, s) - altered) == 0, 'Rejected the wrong affine derivative sign.')
    elif name == 'wrong_cutoff':
        nonempty_packet_certificate(requested_cutoff=5)
    elif name == 'wrong_winding':
        nonempty_packet_certificate(expected_count=0)
    elif name == 'discarded_unit_mass':
        unit = 7 + 3 * h - 2 * h ** 2
        exact = sp.diff(unit, h).subs(h, 0) / unit.subs(h, 0)
        altered = sp.diff(unit, h).subs(h, 0)
        require(exact == altered, 'Rejected changing the original unit mass 7 to 1.')
    elif name == 'discarded_multiplicity':
        original_packet = (s - (1 + sp.I)) ** 2 * (s - (-2 + 3 * sp.I)) ** 3
        altered_packet = (s - (1 + sp.I)) * (s - (-2 + 3 * sp.I))
        require(sp.expand(original_packet - altered_packet) == 0, 'Rejected deletion of multiplicities 2 and 3.')
    else:
        raise ValueError('Unknown deliberate-failure name.')
    raise ValueError('A deliberate alteration unexpectedly passed.')

def rejection_controls():
    names = ('missing_factor16', 'wrong_coordinate_sign', 'wrong_cutoff', 'wrong_winding', 'discarded_unit_mass', 'discarded_multiplicity')
    rejected = []
    for name in names:
        try:
            deliberate_failure(name)
        except RuntimeError:
            rejected.append(name)
    require(len(rejected) == len(names), 'Not all deliberate failures were rejected.')
    return rejected
if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--deliberate-failure':
        ctx.dps = 80
        deliberate_failure(sys.argv[2])
    else:
        receipt = {'symbolic': symbolic_checks(), 'corrected_RTN_constants': corrected_rtn_constant_checks(), 'arb_certificate': finite_certificate(), 'nonempty_packet': nonempty_packet_certificate(), 'deliberate_failures_rejected': rejection_controls()}
        receipt['active_require_calls'] = _require_count
        print(json.dumps(receipt, indent=2))
