"""Bounded pointwise L1 tests for the actual de Bruijn--Newman heat integral.

L1(t,x)=H'_t(x)^2-H_t(x)H''_t(x). The 33 exact rational points are
calibration only; no interval mesh or claim of global positivity is made.
The imported heat evaluator includes rigorous n- and u-truncation tails.
An exact polynomial heat-flow control verifies that negative L1 is detected.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
import time
from fractions import Fraction
from pathlib import Path

sys.dont_write_bytecode = True

import flint
from flint import arb, ctx


DIRECTORY = Path(__file__).resolve().parent
DEPENDENCY = DIRECTORY / 'verify_newman_heat.py'
PRIOR_CERTIFICATE = DIRECTORY / 'newman_heat_results.json'
SOURCE = Path('[local]/Documents/arxiv_latex/_topic_fetch/'
              'RG_flow_thermodynamics_and_heat_flow_RH/1904.12438/debruijn.tex')
DEPENDENCY_BYTES = DEPENDENCY.read_bytes()
DEPENDENCY_HASH = hashlib.sha256(DEPENDENCY_BYTES).hexdigest()
PRIOR_BYTES = PRIOR_CERTIFICATE.read_bytes()
PRIOR_HASH = hashlib.sha256(PRIOR_BYTES).hexdigest()
PRIOR_DATA = json.loads(PRIOR_BYTES)
assert PRIOR_DATA['script_sha256'] == DEPENDENCY_HASH
SOURCE_HASH = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert SOURCE_HASH == PRIOR_DATA['source_TeX_sha256']

# Loading does not execute the dependency's root-search main, write a new
# receipt, or create bytecode caches. Its theta integral is the only evaluator.
spec = importlib.util.spec_from_file_location('certified_newman_heat',DEPENDENCY)
heat_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(heat_module)
ctx.prec = 256
ctx.threads = 1

TIMES = (Fraction(0),Fraction(1,20),Fraction(1,5))
POINTS = tuple(range(20,61,4))
assert len(TIMES)*len(POINTS) == 33


def classification(value):
    if not value.is_finite():
        return 'nonfinite_inconclusive'
    if value > 0:
        return 'strict_positive_certified'
    if value < 0:
        return 'strict_negative_certified'
    if value == 0:
        return 'exact_zero'
    return 'zero_containing_inconclusive'


def polynomial_control():
    # Q_t(z)=(z-a)^2+b^2-2t, a=3,b=1. It solves d_t Q=-d_z^2 Q.
    # At x=a: Q=1-2t, Q'=0, Q''=2; hence L1=-2+4t.
    # Its actual zeros are 3 +/- i*sqrt(1-2t) for these three t<1/2.
    rows = []
    for t in TIMES:
        c = Fraction(1)-2*t
        exact = -2*c
        q = heat_module.scalar(c)
        qp = arb(0)
        qpp = arb(2)
        value = qp*qp-q*qpp
        assert c > 0 and value < 0
        rows.append({'t_exact':str(t),'a_exact':'3','b_exact':'1',
                     'Q_at_center_exact':str(c),'L1_exact':str(exact),
                     'L1_ball':str(value),'classification':classification(value),
                     'nonreal_roots_exact':'3 +/- i*sqrt('+str(c)+')'})
    return {'function':'Q_t(z)=(z-3)^2+1-2t',
            'heat_equation_exact':'partial_t Q=-2=-partial_z^2 Q',
            'laguerre_formula_exact':'L1(t,x)=2*(x-3)^2-2+4*t',
            'negative_center_domain_exact':'t<1/2',
            'role':'Exact manufactured polynomial control, not the zeta heat kernel',
            'rows':rows}


def main():
    started = time.time()
    results = []
    total_evaluations = 0
    for tq in TIMES:
        for x in POINTS:
            t = heat_module.scalar(tq)
            row = {'t_exact':str(tq),'x_exact':str(x)}
            try:
                values = [heat_module.heat(t,arb(x),k)
                          for k in range(3)]
                h,hp,hpp = [v[0] for v in values]
                calls = sum(v[1] for v in values)
                total_evaluations += calls
                laguerre = hp*hp-h*hpp
                row.update({'H_ball':str(h),'Hprime_ball':str(hp),
                            'Hsecond_ball':str(hpp),'L1_ball':str(laguerre),
                            'L1_lower_ball':str(laguerre.lower()),
                            'L1_upper_ball':str(laguerre.upper()),
                            'classification':classification(laguerre),
                            'integrand_evaluations':calls})
            except (ArithmeticError,ValueError) as error:
                # An unsuccessful enclosure remains explicitly inconclusive.
                row.update({'classification':'evaluation_failure_inconclusive',
                            'error':str(error)})
            results.append(row)
        print('TIME',str(tq),[(r['x_exact'],r['classification']) for r in results
                              if r['t_exact']==str(tq)],flush=True)
    counts = {key:sum(r['classification']==key for r in results)
              for key in sorted({r['classification'] for r in results})}
    script = Path(__file__)
    data = {
        'status':'bounded_pointwise_centered_L1_calibration_not_RH_resolution',
        'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
        'dependencies':[
            {'file':DEPENDENCY.name,'sha256':DEPENDENCY_HASH,
             'role':'Full theta-kernel derivative evaluator and proved tail bounds'},
            {'file':PRIOR_CERTIFICATE.name,'sha256':PRIOR_HASH,
             'role':'Existing evaluator/source provenance certificate; not used as numerical input'},
            {'file':'debruijn.tex','sha256':SOURCE_HASH,
             'source':'D. H. J. Polymath, arXiv:1904.12438',
             'locator':'lines 124-135; equations phidef,htdef'}],
        'software':{'python':platform.python_version(),
                    'python_flint':flint.__version__},
        'precision_bits':256,'threads':1,'zeta_function_calls':0,'zeta_zero_inputs':0,
        'times_exact':[str(t) for t in TIMES],'x_exact':[str(x) for x in POINTS],
        'point_count':len(results),'counts':counts,
        'integrand_evaluations_total':total_evaluations,
        'formula':'L1(t,x)=Hprime(t,x)^2-H(t,x)*Hsecond(t,x)',
        'full_function':'H_t(z)=integral_0^infinity exp(t*u^2)*Phi(u)*cos(z*u) du, with the exact Polymath theta kernel',
        'uniform_absolute_tail_bound_per_derivative':str(heat_module.TAIL),
        'tail_scope':'Each H,Hprime,Hsecond ball includes the full omitted-n and omitted-u error, not merely finite numerical quadrature',
        'points':results,'exact_polynomial_control':polynomial_control(),
        'certificate_interpretation':
            'A strictly negative L1 is a necessary-real-rootedness violation. Positive values at these exact points do not establish positivity between them or elsewhere. The criterion is a mathematical implication, not an assumed RH input.',
        'nonclaims':['No scan or certificate over time/space intervals',
                     'No RH conclusion from a finite set of positive point values',
                     'The manufactured polynomial control is not a zeta counterexample',
                     'Inconclusive balls are never counted as positive',
                     'Arb software is trusted, not proof-assistant verified'],
        'elapsed_seconds':time.time()-started,
    }
    target = script.with_name('centered_laguerre_results.json')
    target.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print('COUNTS',counts,'SECONDS',data['elapsed_seconds'],flush=True)


if __name__ == '__main__':
    main()
