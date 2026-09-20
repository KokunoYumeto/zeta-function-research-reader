"""Finite full-Weil matrices from Arb series, without a truncated zero list.

The incoming formula (32) identifies these coefficients with the complete
Weil form. The derivation is in the accompanying checked mathematical note.
All comparisons below are ball comparisons; indeterminate signs are not passed.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import flint
from flint import acb,arb,acb_series,acb_mat,ctx

P=Path(__file__).parent
ctx.prec=768
ctx.cap=12
ctx.threads=1
n=8
rows=[]
for tau in [0,14,21,100,1000]:
    omega=acb(2,tau)
    h=arb(3)
    z=acb_series([0,1])
    s=(omega+(1-omega.conjugate())*z)/(1+z)
    xi=s*(s-1)/2*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
    ld=xi.derivative()/xi/s.derivative()
    coeff=[2*ld[0].real]+[ld[j] for j in range(1,n+1)]
    minors=[]
    for d in range(1,n+2):
        a=acb_mat([[coeff[j-i] if j>=i else coeff[i-j].conjugate()
                    for j in range(d)] for i in range(d)])
        determinant=a.det()
        minors.append({'size':d,'determinant_ball':str(determinant),
                       'real_lower':str(determinant.real.lower()),
                       'strictly_positive':bool(determinant.real>0),
                       'imaginary_contains_zero':bool(determinant.imag.contains(0))})
    margins=[coeff[0]-abs(coeff[j]) for j in range(1,n+1)]
    rows.append({'omega_real':2,'omega_imag':tau,'degree':n,
                 'coefficients':[str(c) for c in coeff],
                 'two_mode_margins':[str(v) for v in margins],
                 'two_mode_positive':[bool(v>0) for v in margins],
                 'leading_minors':minors,
                 'positive_definite_certified':all(v['strictly_positive'] and v['imaginary_contains_zero'] for v in minors)})
    print(tau,'positive-definite:',rows[-1]['positive_definite_certified'],
          'two-mode margins positive:',rows[-1]['two_mode_positive'])
receipt={'created_utc':datetime.now(timezone.utc).isoformat(),
         'library':'python-flint '+flint.__version__,'precision_bits':ctx.prec,'series_cap':ctx.cap,
         'thread_count':ctx.threads,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'method':'Arb formal series of the full completed xi and exact Mobius map; derivative ratio gives xi-prime/xi. The determinant of every leading principal matrix is enclosed and tested with a strict real ball comparison.',
         'not_a_zero_sweep':True,'zero_tail_truncated':False,'rows':rows,
         'scope':'Only these five poles and degrees 0 through 8. No global RH result or negative certificate.'}
(P/'ARITHMETIC_BALL_CERTIFICATES.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
