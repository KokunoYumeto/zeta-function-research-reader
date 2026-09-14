"""Substantive in-memory mutants of only the new periodized finite suite."""
from pathlib import Path
import hashlib
import io
import json
import sys
import unittest

SOURCE = Path(r'workspace:\output\split_zero_rh_tandem_2026-09-12\sources\web_periodized_source_delivery\Tau_Periodized_Source_Control\check_periodized.py')
text = SOURCE.read_text(encoding='utf-8')
changes = [
    ('omit_actual_zero_gram', 'test_zeroth_mode_metric',
     'M=F.conjugate().T*F+z.conjugate().T*z/L', 'M=F.conjugate().T*F'),
    ('break_same_remainder_section', 'test_source_quotient_comparison',
     'C=M.inv()*J.conjugate().T*G', 'C=M.inv()*J.conjugate().T*G+s.ones(M.rows,J.rows)'),
    ('drop_half_density_weight', 'test_half_density_generator',
     '-s.diff(psi,r)+s.Rational(k,2)*psi,', '-s.diff(psi,r),'),
    ('double_cutoff_frequency_scale', 'test_finite_fourier_tail_coefficient',
     'rhs=(L/(2*s.pi*J))**(2*p-1)/s.Integer(2*p-1)',
     'rhs=(L/(s.pi*J))**(2*p-1)/s.Integer(2*p-1)'),
    ('drop_laplacian_k_boundary', 'test_weight_boundary_and_laplacian',
     '(D-k*s.eye(4))*B+B*A)', 'D*B+B*A)'),
    ('erase_completion_radical', 'test_completed_sample_quotient_retains_exact_radical',
     'G=s.Rational(7,3)*J.T*J', 'G=s.Rational(7,3)*J.T*J+s.eye(3)'),
    ('drop_complex_correlation_conjugation', 'test_discrete_correlation_unfolding',
     'right+=f.conjugate().T*g', 'right+=f.T*g'),
]
records = []
for name, method, old, new in changes:
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one mutation site for {name}; got {text.count(old)}')
    namespace = {'__name__': 'periodized_source_review_mutant', '__file__': str(SOURCE)}
    exec(compile(text.replace(old, new, 1), str(SOURCE) + ' [in-memory ' + name + ']', 'exec'), namespace)
    output = io.StringIO()
    suite = unittest.TestSuite([namespace['ExactTests'](method)])
    result = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
    killed = result.testsRun == 1 and len(result.failures) == 1 and len(result.errors) == 0
    records.append({'mutation': name, 'method': method, 'original': old,
                    'replacement': new, 'tests_run': result.testsRun,
                    'failures': len(result.failures), 'errors': len(result.errors),
                    'killed_by_assertion_failure': killed, 'output': output.getvalue()})
    if not killed:
        print(json.dumps(records, indent=2))
        raise RuntimeError('Mutation did not fail at the intended mathematical assertion: ' + name)
report = {'scope': 'Seven finite-interface source mutations, not analytical theorem proofs.',
          'python_optimization': sys.flags.optimize,
          'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'mutation_count': len(records), 'all_killed_by_one_assertion': True,
          'errors': 0, 'mutations': records}
print(json.dumps(report, indent=2))
