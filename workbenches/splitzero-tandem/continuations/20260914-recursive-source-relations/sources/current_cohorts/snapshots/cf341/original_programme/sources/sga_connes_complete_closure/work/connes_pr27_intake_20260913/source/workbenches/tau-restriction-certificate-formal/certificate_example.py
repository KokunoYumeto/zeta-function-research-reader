#!/usr/bin/env python3
"""Outward decimal display of an exact rational adaptive certificate.

The certificate uses only the original matrices and traces. The log interval
is an independent check on this declared Gaussian fixture, not an input.
"""
import json
import sympy as sp
from check_restriction import frame, adaptive, log_interval, CHIS

def outward(x, places, upper=False):
    scale=10**places
    n=int(sp.ceiling(x*scale) if upper else sp.floor(x*scale))
    sign='-' if n<0 else ''
    n=abs(n)
    return sign+str(n//scale)+'.'+str(n%scale).zfill(places)

p=64
lower=sp.S.Zero
upper=sp.S.Zero
blocks=[]
for i,j in [(1,3),(2,4)]:
    Ki=frame(CHIS[0],i)[2]
    Gj=frame(CHIS[0],j)[3]
    T=Ki*Gj
    H=sp.eye(T.rows)-T
    lo,hi=adaptive(H,p)
    lower+=lo
    upper+=hi
    blocks.append({'source_degrees':[i,j],'trace_power_64':str(sp.trace(H**p)),
        'lower_decimal':outward(lo,16),'upper_decimal':outward(hi,16,True)})
loglo,loghi=log_interval(sp.Rational(375,32),500)
if not (lower<=loglo<=loghi<=upper):
    raise AssertionError('independent rational logarithm enclosure is outside certificate')
if not upper-lower<sp.Rational(1,10**14):
    raise AssertionError('declared rational width not certified')
print(json.dumps({'status':'PASS','p':p,'moments_through':2*p,'blocks':blocks,
    'combined_lower_decimal':outward(lower,14),
    'combined_upper_decimal':outward(upper,14,True),
    'rational_width_less_than':'1/10^14',
    'source_mass':7,'arithmetic_packet':False,
    'certificate_inputs':'matrix traces only; no externally supplied spectral gap'},indent=2,sort_keys=True))
