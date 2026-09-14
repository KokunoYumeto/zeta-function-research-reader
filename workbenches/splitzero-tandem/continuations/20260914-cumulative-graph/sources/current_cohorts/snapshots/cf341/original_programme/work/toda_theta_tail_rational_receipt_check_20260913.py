"""Independent exact-rational audit of saved theta-seed interval endpoints.

This script does not evaluate the analytic seed or run Arb.  It checks only
the arithmetic relations among the saved endpoints and receipt identities.
"""
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'toda_theta_tail_rational_receipt_review_20260913.json'
AUTHOR_SCRIPT = ROOT / 'toda_theta_input_tail_check_20260912.py'
FILES = {
    'normal': ROOT / 'toda_theta_input_tail_result_normal_20260912.json',
    'optimized': ROOT / 'toda_theta_input_tail_result_optimized_20260912.json',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def is_power_of_two(value):
    return value > 0 and value & (value - 1) == 0


author_sha = sha(AUTHOR_SCRIPT.read_bytes())
snapshots = {mode: path.read_bytes() for mode, path in FILES.items()}
documents = {mode: json.loads(data) for mode, data in snapshots.items()}
review = {
    'schema': 'toda-theta-saved-endpoints-independent-rational-review-v1',
    'reviewed_at_utc': datetime.now(timezone.utc).isoformat(),
    'status': 'passed',
    'arithmetic': 'fractions.Fraction; no floating-point comparisons',
    'reviewer_script_sha256': sha(Path(__file__).read_bytes()),
    'author_script_sha256': author_sha,
    'scope': (
        'Saved decimal and dyadic endpoint arithmetic, positive recorded mass, '
        'consistency of the recorded ratio interval with external-endpoint '
        'interval division, and mode-pair identity. No Arb evaluation, analytic '
        'tail proof, or independent certification of an analytic value is claimed.'
    ),
    'files': {},
}
for mode, document in documents.items():
    require(document['status'] == 'passed', mode + ': status')
    require(document['negative_control'] is False, mode + ': negative-control flag')
    require(document['optimization_flag'] == (mode == 'optimized'), mode + ': optimization flag')
    require(document['script_sha256'] == author_sha, mode + ': author script identity')
    intervals = {}
    records = {}
    for name, item in document['results'].items():
        decimal_lower, decimal_upper = Fraction(item['lower']), Fraction(item['upper'])
        exact_lower = Fraction(item['exact_lower_dyadic'])
        exact_upper = Fraction(item['exact_upper_dyadic'])
        raw_denominators = [int(item[key].split('/')[1])
                            for key in ('exact_lower_dyadic', 'exact_upper_dyadic')]
        require(all(is_power_of_two(d) for d in raw_denominators), name + ': raw dyadic denominators')
        require(all(is_power_of_two(d.denominator) for d in (exact_lower, exact_upper)), name + ': reduced dyadic denominators')
        require(decimal_lower < exact_lower < exact_upper < decimal_upper, name + ': strict decimal enclosure')
        require(decimal_upper - decimal_lower == Fraction(3, 10**40), name + ': decimal width')
        intervals[name] = (exact_lower, exact_upper, decimal_lower, decimal_upper)
        records[name] = {
            'strict_decimal_enclosure': True,
            'raw_dyadic_denominator_exponents': [d.bit_length() - 1 for d in raw_denominators],
            'reduced_dyadic_denominator_exponents': [d.denominator.bit_length() - 1 for d in (exact_lower, exact_upper)],
            'decimal_width_exact': str(decimal_upper - decimal_lower),
            'decimal_width_equals_3_times_10_to_minus_40': True,
            'lower_decimal_margin_exact': str(exact_lower - decimal_lower),
            'upper_decimal_margin_exact': str(decimal_upper - exact_upper),
        }
    require(set(intervals) == {'M1_0', 'M1_one_tenth', 'M1_second_0', 'a1_tensor_coefficient'}, mode + ': result names')
    mass_lower, mass_upper, mass_decimal_lower, _ = intervals['M1_0']
    numerator_lower, numerator_upper, _, _ = intervals['M1_second_0']
    ratio_lower, ratio_upper, ratio_decimal_lower, ratio_decimal_upper = intervals['a1_tensor_coefficient']
    require(mass_decimal_lower > 0 and mass_lower > 0, mode + ': positive mass')
    require(numerator_lower > 0, mode + ': positive numerator for division order')
    quotient_lower = numerator_lower / mass_upper
    quotient_upper = numerator_upper / mass_lower
    overlap_lower = max(quotient_lower, ratio_lower)
    overlap_upper = min(quotient_upper, ratio_upper)
    require(overlap_lower < overlap_upper, mode + ': nonempty ratio/division overlap')
    require(ratio_decimal_lower < quotient_lower < quotient_upper < ratio_decimal_upper, mode + ': displayed ratio encloses external division')
    review['files'][mode] = {
        'name': FILES[mode].name,
        'sha256': sha(snapshots[mode]),
        'bytes': len(snapshots[mode]),
        'optimization_flag': document['optimization_flag'],
        'script_identity_matches_current_author_script': True,
        'records': records,
        'recorded_mass_strictly_positive': True,
        'ratio_comparison': {
            'naive_division_rule': '[numerator_lower / mass_upper, numerator_upper / mass_lower]',
            'naive_lower_exact': str(quotient_lower),
            'naive_upper_exact': str(quotient_upper),
            'strict_overlap': True,
            'overlap_lower_exact': str(overlap_lower),
            'overlap_upper_exact': str(overlap_upper),
            'ratio_dyadic_contains_naive_division': ratio_lower <= quotient_lower and quotient_upper <= ratio_upper,
            'naive_division_contains_ratio_dyadic': quotient_lower <= ratio_lower and ratio_upper <= quotient_upper,
            'displayed_decimal_ratio_strictly_contains_naive_division': True,
            'logical_scope': (
                ('The saved dyadic ratio interval contains every quotient of '
                 'inputs in the saved positive numerator and mass dyadic intervals. '
                 if ratio_lower <= quotient_lower and quotient_upper <= ratio_upper
                 else 'Overlap establishes compatibility of the two saved intervals; '
                      'it does not alone certify enclosure of the exact quotient. ')
                + 'The displayed decimal ratio also strictly encloses the external '
                  'interval division. These are endpoint arithmetic conclusions; '
                  'this review does not independently certify that the analytic '
                  'numerator and mass lie inside their saved dyadic intervals.'
            ),
        },
    }
normal = {key: value for key, value in documents['normal'].items() if key != 'optimization_flag'}
optimized = {key: value for key, value in documents['optimized'].items() if key != 'optimization_flag'}
require(normal == optimized, 'mode pair differs beyond optimization flag')
review['mode_pair_identical_except_optimization_flag'] = True
review['counts'] = {
    'receipt_files': 2,
    'result_records': sum(len(document['results']) for document in documents.values()),
    'raw_and_reduced_dyadic_denominators_each': 16,
    'strict_decimal_enclosures': 8,
    'exact_decimal_width_checks': 8,
    'positive_mass_checks': 2,
    'ratio_division_compatibility_checks': 2,
    'displayed_decimal_ratio_encloses_naive_division_checks': 2,
}
for mode, path in FILES.items():
    require(path.read_bytes() == snapshots[mode], 'receipt changed during audit: ' + mode)
require(sha(AUTHOR_SCRIPT.read_bytes()) == author_sha, 'author script changed during audit')
OUTPUT.write_text(json.dumps(review, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': review['status'], 'output': OUTPUT.name,
                  'sha256': sha(OUTPUT.read_bytes()), 'counts': review['counts'],
                  'input_hashes': {m: r['sha256'] for m, r in review['files'].items()},
                  'ratio_relations': {m: {k: v for k, v in r['ratio_comparison'].items()
                      if k.startswith('ratio_dyadic_') or k.startswith('naive_division_contains')}
                      for m, r in review['files'].items()}}, indent=2))
