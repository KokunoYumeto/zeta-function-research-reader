"""Finite-sum Arb certificate for the cooled prime-2 Gaussian Mellin detector.

The certified computation uses no zeta function, no zero table, and no RH
assumption. It evaluates the finite n-sum of exact Gaussian antiderivatives
on epsilon <= lambda <= R, then adds proved lower/upper/omitted-sum bounds.
Only after every certificate is fixed is a separate direct-zeta diagnostic run.

Trust boundary: python-flint / FLINT Arb and acb special-function enclosures;
the implementation is not proof-assistant verified. One worker; O(1) summation
storage. The only output file is cooled_mellin_results.json beside this script.
"""
from __future__ import annotations

import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import flint
import psutil
from flint import acb, arb, ctx

PRECISION_BITS = 192
ctx.prec = PRECISION_BITS
ctx.threads = 1
A_EXACT = Fraction(1, 400)
R_EXACT = Fraction(2)
B_EXACT = Fraction(100)
POINTS = [(Fraction(3, 10), Fraction(14)), (Fraction(7, 10), Fraction(14))]
CONFIGURATIONS = [(Fraction(1, 1000), 2000), (Fraction(1, 10000), 20000)]


def rational_ball(value: Fraction) -> arb:
    return arb(value.numerator) / value.denominator


def real_record(value: arb) -> dict:
    return {'ball': str(value), 'lower_ball': str(value.lower()),
            'upper_ball': str(value.upper()), 'finite': bool(value.is_finite())}


def complex_record(value: acb) -> dict:
    return {'ball': str(value), 'real': real_record(value.real),
            'imag': real_record(value.imag), 'absolute_value': real_record(abs(value)),
            'contains_zero': bool(value.contains(0)),
            'finite': bool(value.is_finite())}


def exact_parameters(sigma: Fraction, ordinate: Fraction, epsilon: Fraction, n_max: int) -> dict:
    return {'a': str(A_EXACT), 'epsilon': str(epsilon), 'R': str(R_EXACT),
            'upper_tail_b': str(B_EXACT), 'N': n_max,
            's_real': str(sigma), 's_imag': str(ordinate),
            'N_times_epsilon': str(n_max * epsilon)}


def proved_error_bounds(sigma_exact: Fraction, epsilon_exact: Fraction, n_max: int) -> dict:
    """No zeta input: zeta(b) <= 1 + 1/(b-1), b > 1."""
    assert sigma_exact > 0
    assert B_EXACT > max(Fraction(1), sigma_exact)
    assert 0 < epsilon_exact < R_EXACT
    assert n_max * epsilon_exact >= 1
    a = rational_ball(A_EXACT)
    sigma = rational_ball(sigma_exact)
    epsilon = rational_ball(epsilon_exact)
    outer = rational_ball(R_EXACT)
    b = rational_ball(B_EXACT)
    derivative_l1_majorant = a.exp() * (1 + 1/a + (1 + 1/(2*a)).sqrt())
    low = derivative_l1_majorant * epsilon**(sigma+1) / (4*(sigma+1))
    high = (1 + 1/(b-1)) * (a*b*b).exp() * outer**(sigma-b)
    erfc_argument = ((arb(n_max)*epsilon).log() - 2*a) / (2*a.sqrt())
    omitted_uniform = a.exp() / (2*epsilon) * erfc_argument.erfc()
    middle = omitted_uniform * (outer**sigma-epsilon**sigma) / sigma
    total = low + high + middle
    assert all(value.is_finite() and value >= 0
               for value in (derivative_l1_majorant, low, high, middle, total))
    return {'low': low, 'high': high, 'middle': middle, 'total': total,
            'derivative_l1_majorant': derivative_l1_majorant,
            'omitted_sum_uniform_bound': omitted_uniform,
            'erfc_argument': erfc_argument}


def finite_gaussian_mellin(sigma_exact: Fraction, ordinate_exact: Fraction,
                          epsilon_exact: Fraction, n_max: int) -> acb:
    """Analytic integration term by term; no numerical quadrature or zeta.

    Integral term = (-1)^(n+1) n^(-s) exp(a s^2)/2 * (erf(z_R)-erf(z_eps)).
    Evaluate the identical erfc(z_eps)-erfc(z_R) to avoid subtracting two
    near-unit erf values in the Gaussian tail. Arb encloses all arithmetic.
    """
    a = rational_ball(A_EXACT)
    s = acb(rational_ball(sigma_exact), rational_ball(ordinate_exact))
    log_epsilon = rational_ball(epsilon_exact).log()
    log_outer = rational_ball(R_EXACT).log()
    denominator = 2*a.sqrt()
    shift = 2*a*s
    total = acb(0)
    for n in range(1, n_max+1):
        log_n = arb(n).log()
        z_epsilon = (log_n + log_epsilon - shift) / denominator
        z_outer = (log_n + log_outer - shift) / denominator
        term = (-s*log_n).exp() * (z_epsilon.erfc()-z_outer.erfc())
        total = total + term if n % 2 else total - term
    total *= (a*s*s).exp()/2
    if not total.is_finite():
        raise ArithmeticError('Nonfinite finite-Gaussian-sum enclosure')
    return total


def evaluate(sigma: Fraction, ordinate: Fraction, epsilon: Fraction, n_max: int):
    started = time.perf_counter()
    finite = finite_gaussian_mellin(sigma, ordinate, epsilon, n_max)
    errors = proved_error_bounds(sigma, epsilon, n_max)
    # If |true-finite| <= E, then each Cartesian error coordinate lies in [-E,E].
    # Use the upper endpoint, never the midpoint, as the added radius.
    error_upper = errors['total'].upper()
    error_box = acb(arb(0, error_upper), arb(0, error_upper))
    complete = finite + error_box
    assert complete.is_finite()
    record = {
        'parameters_exact': exact_parameters(sigma, ordinate, epsilon, n_max),
        'finite_sum_enclosure': complex_record(finite),
        'analytic_error_bounds': {name: real_record(value) for name, value in errors.items()},
        'error_radius_upper_bound_used': str(error_upper),
        'complete_detector_enclosure': complex_record(complete),
        'detector_nonzero_at_this_exact_point_certified': not complete.contains(0),
        'elapsed_seconds': time.perf_counter()-started,
        'certificate_uses_zeta': False,
        'certificate_uses_zero_table': False,
    }
    print(json.dumps({'point': [str(sigma), str(ordinate)], 'epsilon': str(epsilon),
                      'N': n_max, 'finite': str(finite), 'analytic_error': str(errors['total']),
                      'complete': str(complete), 'nonzero': not complete.contains(0),
                      'seconds': record['elapsed_seconds']}), flush=True)
    return record, complete


def separate_zeta_diagnostic(sigma: Fraction, ordinate: Fraction, certificates) -> dict:
    """Diagnostic ONLY: invoked after all independently computed certificates."""
    a = rational_ball(A_EXACT)
    s = acb(rational_ball(sigma), rational_ball(ordinate))
    factor = (a*s*s).exp() * (1-((1-s)*arb(2).log()).exp())
    direct = factor*s.zeta()
    return {'s_exact': {'real': str(sigma), 'imag': str(ordinate)},
            'classification': 'separate_direct_zeta_diagnostic_not_used_in_certificate',
            'direct_detector_ball': complex_record(direct),
            'nonzero_prefactor_ball': complex_record(factor),
            'differences_from_independent_enclosures_contain_zero':
                [bool((complete-direct).contains(0)) for complete in certificates]}


def antiderivative_self_test() -> dict:
    """Independent acb log-coordinate quadrature of one term; no zeta."""
    a = rational_ball(A_EXACT)
    s = acb(arb(3)/10, 14)
    lower = -arb(1000).log()
    upper = arb(2).log()
    exact = (a*s*s).exp()/2 * (
        ((upper-2*a*s)/(2*a.sqrt())).erf()
        - ((lower-2*a*s)/(2*a.sqrt())).erf())
    def integrand(v, analytic):
        return (-(v*v)/(4*a)+s*v).exp()/(4*arb.pi()*a).sqrt()
    independent = acb.integral(integrand, lower, upper,
                               abs_tol=arb(2)**-100, rel_tol=arb(2)**-100,
                               eval_limit=50000)
    passed = independent.is_finite() and (exact-independent).contains(0)
    if not passed:
        raise ArithmeticError('Single-term Gaussian antiderivative self-test failed')
    return {'passed': bool(passed), 'classification': 'independent_single_term_validation_not_used_to_form_bounds',
            'parameters': {'n': 1, 'a': '1/400', 's_real': '3/10', 's_imag': '14',
                           'epsilon': '1/1000', 'R': '2'},
            'analytic_antiderivative': complex_record(exact),
            'independent_log_coordinate_integral': complex_record(independent)}


def main() -> None:
    started = time.perf_counter()
    source = Path(__file__).resolve()
    target = source.with_name('cooled_mellin_results.json')
    self_test = antiderivative_self_test()
    records = []
    enclosed_by_point = {}
    for sigma, ordinate in POINTS:
        enclosed_by_point[(sigma, ordinate)] = []
        for epsilon, n_max in CONFIGURATIONS:
            record, complete = evaluate(sigma, ordinate, epsilon, n_max)
            records.append(record)
            enclosed_by_point[(sigma, ordinate)].append(complete)
    # The separate zeta evaluation cannot affect any already constructed bound.
    diagnostics = [separate_zeta_diagnostic(sigma, ordinate, enclosed_by_point[(sigma, ordinate)])
                   for sigma, ordinate in POINTS]
    if not all(all(row['differences_from_independent_enclosures_contain_zero']) for row in diagnostics):
        raise ArithmeticError('Separate diagnostic is incompatible with an independent enclosure')
    memory = psutil.Process().memory_info()
    measured_peak_bytes = getattr(memory, 'peak_wset', memory.rss)
    if measured_peak_bytes >= 5_000_000_000:
        raise MemoryError('Measured process peak reached the 5,000,000,000-byte budget')
    output = {
        'status': 'bounded_finite_cooled_mellin_evaluations_complete_not_RH_resolution',
        'script_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'software': {'python': platform.python_version(), 'python_flint': flint.__version__,
                     'psutil': psutil.__version__},
        'precision_bits': PRECISION_BITS, 'threads': 1,
        'measured_process_peak_working_set_bytes': measured_peak_bytes,
        'memory_budget_bytes': 5_000_000_000,
        'storage': 'O(1) finite summation; no retained arrays of summands',
        'kernel': 'g_a(lambda)=exp(-(log(lambda))^2/(4a))/sqrt(4*pi*a)',
        'cooled_function': 'C_2,a(lambda)=sum_{n>=1}(-1)^(n+1)g_a(n*lambda)',
        'mellin_convention': 'integral_0^infinity C_2,a(lambda)*lambda^s d(lambda)/lambda',
        'finite_antiderivative': '(-1)^(n+1)*n^(-s)*exp(a*s^2)/2*(erf((log(n*R)-2*a*s)/(2*sqrt(a)))-erf((log(n*epsilon)-2*a*s)/(2*sqrt(a))))',
        'stable_equivalent_used': 'erfc(z_epsilon)-erfc(z_R)',
        'bound_formulas': {
            'B2': 'exp(a)*(1+1/a+sqrt(1+1/(2*a)))',
            'low': 'B2*epsilon^(sigma+1)/(4*(sigma+1))',
            'high': '(1+1/(b-1))*exp(a*b^2)*R^(sigma-b)',
            'middle': 'exp(a)/(2*epsilon)*erfc((log(N*epsilon)-2*a)/(2*sqrt(a)))*(R^sigma-epsilon^sigma)/sigma',
            'high_bound_avoids_zeta': 'zeta(b) <= 1+1/(b-1), proved by the integral test',
        },
        'independent_certificates': records,
        'antiderivative_self_test': self_test,
        'separate_zeta_diagnostics': diagnostics,
        'trust_boundary': 'FLINT Arb/acb arithmetic and complex error-function enclosures; not a Lean verification of software',
        'nonclaims': ['No RH counterexample found or asserted',
                      'Nonzero point enclosures are not zero-free-region certificates',
                      'The evaluated function is a cooling-map image, not a nonzero cokernel class',
                      'Diagnostic zeta values are not computation inputs to the certified finite sum or error bounds'],
        'elapsed_seconds': time.perf_counter()-started,
    }
    target.write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print('RESULT '+str(target)+' elapsed '+str(output['elapsed_seconds']), flush=True)


if __name__ == '__main__':
    main()
