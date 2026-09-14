"""Bounded independent adversarial checks; repository source is never modified."""
import importlib.util
import json
import re
import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'source/workbenches/tau-specialization-curvature-formal'
sys.path.insert(0, str(SRC))
import check_specialization as specialization
import check_laplacian as laplacian

records = []
for label, mod in [('specialization', specialization), ('laplacian', laplacian)]:
    lines = ["'%s' depends on axioms: [propext, Classical.choice, Quot.sound]" % n for n in sorted(mod.EXPECTED)]
    valid = '\n'.join(lines)
    if set(mod.audit(valid)) != mod.EXPECTED:
        raise RuntimeError('positive audit control failed')
    bad = {
        'empty': '',
        'missing': '\n'.join(lines[:-1]),
        'duplicate': valid+'\n'+lines[0],
        'extra_target': valid+"\n'Unexpected.target' depends on axioms: [propext]",
        'sorryAx': valid.replace('propext', 'sorryAx', 1),
        'Lean.ofReduceBool': valid.replace('propext', 'Lean.ofReduceBool', 1),
        'custom_axiom': valid.replace('propext', 'Example.unprovedClaim', 1),
        'lean_error': valid+'\nerror: intentional independent diagnostic',
    }
    for name, data in bad.items():
        try:
            mod.audit(data)
        except AssertionError as exc:
            records.append({'suite':label,'negative':name,'result':'rejected','exception':str(exc)})
        else:
            raise RuntimeError(label+' accepted '+name)
    for name, data in {
        'extra_axiom_free_target': valid+"\n'Unexpected.target' does not depend on any axioms",
        'warning_text': valid+'\nwarning: hypothetical unrecognized diagnostic',
    }.items():
        accepted = False
        try:
            mod.audit(data)
            accepted = True
        except AssertionError:
            pass
        records.append({'suite':label,'parser_boundary_probe':name,'accepted':accepted})

mutants = [
    ('specialization','relation_sign','D=X-hi[\'R\']','D=X+hi[\'R\']','test_01_original_source_and_difference'),
    ('specialization','drop_action_pole','+P1*A*P0/w','+s.zeros(3)','test_06_action_pole_not_discarded'),
    ('specialization','curvature_factorial','s.factorial(n+1)*sum(l**(n+1)','s.factorial(n)*sum(l**(n+1)','test_12_curvature_jets_recover_trace_moments'),
    ('laplacian','gaussian_coefficient','-6*s.pi*x*x','-4*s.pi*x*x','test_01_original_gaussian_is_laplacian_image'),
    ('laplacian','drop_energy_cross_term','W*B-B.conjugate()','s.zeros(3)-B.conjugate()','test_04_centered_energy_keeps_cross_term'),
    ('laplacian','drop_jordan_square','+(2*rho-1)*N+N*N','+(2*rho-1)*N','test_05_full_jordan_laplacian'),
]
for label, name, original, replacement, test_name in mutants:
    path = SRC / ('check_'+label+'.py')
    code = path.read_text(encoding='utf-8')
    count = code.count(original)
    if count != 1:
        raise RuntimeError('mutation anchor count: '+name+': '+str(count))
    module = types.ModuleType('review_mutant_'+name)
    module.__file__ = str(path)
    exec(compile(code.replace(original,replacement),str(path)+' [in-memory mutation '+name+']','exec'),module.__dict__)
    suite = unittest.TestSuite([module.Tests(test_name)])
    result = unittest.TestResult()
    suite.run(result)
    if result.testsRun != 1 or len(result.failures) != 1 or result.errors:
        raise RuntimeError('mutation not killed by assertion: '+name+' '+repr(result.errors))
    records.append({'suite':label,'mutation':name,'original':original,'replacement':replacement,'test':test_name,'tests_run':1,'failures':1,'errors':0,'result':'killed','failure':result.failures[0][1]})
print(json.dumps({'status':'PASS','optimization':sys.flags.optimize,'rejected_audit_mutations':16,'killed_algebraic_mutations':6,'records':records},sort_keys=True,indent=2))
