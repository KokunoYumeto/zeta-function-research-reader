"""Independent finite replay of the saved decimal records; no quadrature run.

All source records are read-only. Exact-decimal arithmetic establishes facts
about their serialized rational values, not their analytic targets.
"""
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import math
import platform
import re
import sys
import time
import mpmath as mp

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'RH_Counterfactual_Workbench'
mp.mp.dps = 240


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, SRC / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def val(x):
    return mp.mpf(x.numerator) / x.denominator if isinstance(x, Q) else mp.mpf(x)


def fmt(x):
    return mp.nstr(val(x), 35)


def relative(x, y):
    return abs(val(x) - val(y)) / abs(val(y)) if y else abs(val(x))


def independent_recurrence(a):
    b = []
    for n in range(len(a) - 1):
        numerator = -(n + 1) * a[n + 1]
        for j in range(1, n + 1):
            numerator -= a[j] * b[n - j]
        b.append(numerator / a[0])
    return b


def independent_ldlt(b, shift, size):
    L = [[Q(int(i == j)) for j in range(size)] for i in range(size)]
    D, dets = [], []
    for j in range(size):
        pivot = b[2 * j + shift]
        for k in range(j):
            pivot -= L[j][k] ** 2 * D[k]
        if pivot == 0:
            raise ArithmeticError(('zero exact decimal pivot', shift, j))
        D.append(pivot)
        dets.append((dets[-1] if dets else Q(1)) * pivot)
        for i in range(j + 1, size):
            entry = b[i + j + shift]
            for k in range(j):
                entry -= L[i][k] * L[j][k] * D[k]
            L[i][j] = entry / pivot
    # This verifies the entire exact factorization, independently of signs.
    reconstruction = all(
        sum((L[i][k] * D[k] * L[j][k] for k in range(size)), Q(0))
        == b[i + j + shift]
        for i in range(size) for j in range(size)
    )
    return D, dets, reconstruction


def sig_digits(s):
    return len(Decimal(s).as_tuple().digits)


def saved_test_log(filename):
    raw = (ROOT / filename).read_bytes()
    content = raw.decode('utf-16' if raw.startswith((b'\xff\xfe', b'\xfe\xff')) else 'utf-8-sig')
    count = re.search(r'Ran (\d+) tests?', content)
    return {'log': filename, 'sha256': hashlib.sha256(raw).hexdigest(),
            'test_count': int(count.group(1)) if count else None,
            'reports_ok': content.rstrip().endswith('OK'),
            'execution_exit_code_observed_in_audit': 0}


def audit_record(filename, numeric):
    record = json.loads((SRC / filename).read_text())
    order = record['order']
    a = list(map(Q, record['a']))
    b = list(map(Q, record['b']))
    # Original moment coordinates: no rescaling of either moment or Hankel matrix.
    recovered_mu = [(-1) ** j * math.factorial(2 * j) * x for j, x in enumerate(a)]
    regenerated_a = [(-1) ** j * x / math.factorial(2 * j)
                     for j, x in enumerate(recovered_mu)]
    recurrence_b = independent_recurrence(a)
    recurrence_residual = []
    for n in range(len(b)):
        terms = [a[0] * b[n], (n + 1) * a[n + 1]]
        terms.extend(a[j] * b[n - j] for j in range(1, n + 1))
        numerator = abs(sum(terms, Q(0)))
        denominator = sum(map(abs, terms), Q(0))
        recurrence_residual.append(val(numerator / denominator))
    result = {
        'metadata': {k: record[k] for k in ['status', 'mpmath_version', 'order', 'dps',
            'gauss_legendre_degree', 'node_count', 'theta_terms', 'y_interval',
            'retained_g0', 'g0_direct_difference', 'seconds']},
        'a_count': len(a), 'b_count': len(b),
        'dimensions_valid': len(a) == 2 * order + 1 and len(b) == 2 * order
            and set(record['matrices']) == {'0', '1'}
            and all([row['dimension'] for row in record['matrices'][str(s)]]
                    == list(range(1, order + 1)) for s in (0, 1)),
        'node_count_metadata_valid': record['node_count'] == 3 * 2 ** (record['gauss_legendre_degree'] - 1),
        'significant_digit_ranges': {
            'a': [min(map(sig_digits, record['a'])), max(map(sig_digits, record['a']))],
            'b': [min(map(sig_digits, record['b'])), max(map(sig_digits, record['b']))],
            'pivots': [min(sig_digits(row['pivot']) for rows in record['matrices'].values() for row in rows),
                       max(sig_digits(row['pivot']) for rows in record['matrices'].values() for row in rows)]},
        'mass_matches_a0_exactly': Q(record['retained_g0']) == a[0],
        'mu_recovery_definition': 'mu[2*j] = (-1)^j * (2*j)! * Q(a[j]); saved decimals interpreted exactly',
        'mu_recovery_roundtrip_exact': regenerated_a == a,
        'mu_even_recovered_exact_rationals': [str(x) for x in recovered_mu],
        'recurrence_relative_errors_by_index': [fmt(relative(x, y)) for x, y in zip(recurrence_b, b)],
        'max_recurrence_relative_error': fmt(max(relative(x, y) for x, y in zip(recurrence_b, b))),
        'max_scaled_recurrence_residual': fmt(max(recurrence_residual)),
        'matrices': {},
    }
    # Source recurrence is replayed only on saved moments at 240-digit precision.
    aa, bb = numeric.log_moments(list(map(val, recovered_mu)))
    result['source_recurrence_replay_max_relative_error'] = fmt(max(relative(x, y) for x, y in zip(bb, recurrence_b)))
    for shift in (0, 1):
        exact_D, exact_det, reconstructed = independent_ldlt(b, shift, order)
        # Replay source's numeric LDL routine on the same serialized values.
        H = [[val(b[i + j + shift]) for j in range(order)] for i in range(order)]
        numeric_D = numeric.ldlt_pivots(H)
        Hb = [[val(recurrence_b[i + j + shift]) for j in range(order)] for i in range(order)]
        recurrence_D = numeric.ldlt_pivots(Hb)
        rows = record['matrices'][str(shift)]
        result['matrices'][str(shift)] = {
            'exact_decimal_factorization_verified': reconstructed,
            'all_exact_decimal_pivots_positive': all(d > 0 for d in exact_D),
            'all_stored_signs_match_exact_decimal_pivots': all(row['sign'] == (1 if d > 0 else -1) for row, d in zip(rows, exact_D)),
            'source_ldlt_replay_max_relative_error': fmt(max(relative(x, y) for x, y in zip(numeric_D, exact_D))),
            'rows': [{
                'dimension': j + 1,
                'stored_pivot': row['pivot'],
                'exact_decimal_pivot_approximation': fmt(d),
                'stored_vs_exact_decimal_pivot_relative_error': fmt(relative(Q(row['pivot']), d)),
                'stored_vs_recurrence_from_a_pivot_relative_error': fmt(relative(Q(row['pivot']), recurrence_D[j])),
                'stored_determinant': row['determinant'],
                'exact_decimal_determinant_approximation': fmt(det),
                'stored_vs_exact_decimal_determinant_relative_error': fmt(relative(Q(row['determinant']), det)),
            } for j, (row, d, det) in enumerate(zip(rows, exact_D, exact_det))],
        }
    return result


def main():
    start = time.monotonic()
    numeric = load_module('finite_audit_numeric', 'search_theta_moments.py')
    exact = load_module('finite_audit_exact', 'exact_witness_checks.py')
    names = ['exact_witness_checks.py', 'search_theta_moments.py',
             'exact_checks.log', 'exact_checks_optimized.log',
             'probe_120dps.json', 'probe_180dps.json']
    manifest = json.loads((SRC / 'MANIFEST.json').read_text())
    hashes = {name: hashlib.sha256((SRC / name).read_bytes()).hexdigest() for name in names}
    report = {
        'scope': 'Independent arithmetic audit; no quadrature rerun; no analytic interval certification',
        'python': sys.version, 'platform': platform.platform(), 'mpmath': mp.__version__,
        'audit_arithmetic_dps': mp.mp.dps,
        'source_sha256': hashes,
        'manifest_matches': {name: digest == manifest[name] for name, digest in hashes.items()},
        'exact_tests_normal': saved_test_log('FINITE_REPLAY_EXACT_NORMAL.log'),
        'exact_tests_optimized': saved_test_log('FINITE_REPLAY_EXACT_OPTIMIZED.log'),
        'records': {},
    }
    for filename in ['probe_120dps.json', 'probe_180dps.json']:
        report['records'][filename] = audit_record(filename, numeric)
    left = json.loads((SRC / 'probe_120dps.json').read_text())
    right = json.loads((SRC / 'probe_180dps.json').read_text())
    report['cross_probe_comparison'] = {
        'a_strings_identical': left['a'] == right['a'],
        'b_strings_identical': left['b'] == right['b'],
        'a_different_indices': [i for i, (x, y) in enumerate(zip(left['a'], right['a'])) if x != y],
        'b_different_indices': [i for i, (x, y) in enumerate(zip(left['b'], right['b'])) if x != y],
        'pivot_max_relative_errors': {
            str(s): fmt(max(relative(Q(x['pivot']), Q(y['pivot']))
                       for x, y in zip(left['matrices'][str(s)], right['matrices'][str(s)]))) for s in (0, 1)},
        'determinant_max_relative_errors': {
            str(s): fmt(max(relative(Q(x['determinant']), Q(y['determinant']))
                       for x, y in zip(left['matrices'][str(s)], right['matrices'][str(s)]))) for s in (0, 1)},
    }
    # API edge cases are independent of the successful valid-input unit tests.
    neg_shift = exact.enclose_quadratic([(Q(1), Q(1)), (Q(-1), Q(-1))], [Q(1)], shift=-1)
    integer_recurrence = exact.logarithmic_coefficients([3, -1], 1)
    report['api_edge_case_reproductions'] = {
        'negative_shift_not_rejected': {'input': {'intervals': [['1', '1'], ['-1', '-1']], 'c': ['1'], 'shift': -1},
            'output': neg_shift,
            'valid_shift_zero_output': exact.enclose_quadratic([(Q(1), Q(1)), (Q(-1), Q(-1))], [Q(1)], shift=0)},
        'integer_input_recurrence': {'repr': repr(integer_recurrence),
            'element_type': type(integer_recurrence[0]).__name__,
            'equals_exact_one_third': integer_recurrence[0] == Q(1, 3)},
        'negative_count_not_rejected': exact.logarithmic_coefficients([Q(1)], -1),
    }
    report['additive_strict_verifier'] = {
        'module': 'FINITE_REPLAY_STRICT_VERIFIER.py',
        'test_module': 'FINITE_REPLAY_STRICT_TESTS.py',
        'normal_and_optimized_logs': [saved_test_log('FINITE_REPLAY_STRICT_NORMAL.log'), saved_test_log('FINITE_REPLAY_STRICT_OPTIMIZED.log')],
        'archived_sources_modified': False,
        'input_contract': 'Fraction/int/rational-string only; bool and float rejected; shift/count are integers >=0; interval shape/order and sufficient lengths validated',
    }
    nilpotent_path = ROOT / 'FINITE_REPLAY_NILPOTENT_RECEIPT.json'
    if nilpotent_path.exists():
        nilpotent = json.loads(nilpotent_path.read_text())
        report['nilpotent_supplement'] = {'receipt': nilpotent_path.name,
            'all_passed': nilpotent['all_passed'], 'm': list(range(1, 9)),
            'lambda': nilpotent['lambda'], 'beta': nilpotent['beta']}
    report['seconds'] = time.monotonic() - start
    destination = ROOT / 'FINITE_REPLAY_RECEIPT.json'
    destination.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ['manifest_matches', 'cross_probe_comparison', 'api_edge_case_reproductions', 'seconds']}, indent=2))
    for name, rec in report['records'].items():
        print(name, 'dimensions', rec['dimensions_valid'], 'recurrence', rec['max_recurrence_relative_error'])
        for shift, mat in rec['matrices'].items():
            print('shift', shift, 'exact positive', mat['all_exact_decimal_pivots_positive'], 'last', json.dumps(mat['rows'][-1]))


if __name__ == '__main__':
    main()
