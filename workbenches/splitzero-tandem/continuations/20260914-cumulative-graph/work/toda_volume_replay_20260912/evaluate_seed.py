#!/usr/bin/env python3
"""Numerical (not interval-certified) evaluation of the ORIGINAL h=1 theta seed.
No nonempty arithmetic packet is inferred from h=1.
"""
import json
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parent

def seed_mass(theta,cutoff):
    ans=mp.mpc(0);coef={1:-6,2:4}
    for m in range(1,cutoff+1):
        for n in range(1,cutoff+1):
            C=mp.pi*(m*m*mp.exp(1j*theta)+n*n*mp.exp(-1j*theta))
            for r,ar in coef.items():
                for s,bs in coef.items():
                    nu=r+s+mp.mpf('0.5')
                    ans+=4*ar*bs*(mp.pi*m*m)**r*(mp.pi*n*n)**s*mp.exp(1j*theta*(r-s))*mp.gammainc(nu,C,mp.inf)/C**nu
    return ans

def source_seed(x,j,cutoff):
    # p0=4z^2-6z; p1=2z(p0-p0')=8z^3-28z^2+12z.
    if j==0:p=lambda z:4*z*z-6*z
    elif j==1:p=lambda z:8*z**3-28*z*z+12*z
    else:raise ValueError(j)
    return 2*mp.fsum(p(mp.pi*n*n*x*x)*mp.exp(-mp.pi*n*n*x*x) for n in range(1,cutoff+1))

out=[]
for digits,cutoff in [(50,6),(70,8)]:
    mp.mp.dps=digits
    mass=seed_mass(mp.mpf(0),cutoff)
    tilt=seed_mass(mp.mpf('0.1'),cutoff)
    mu2=2*mp.quad(lambda x:(source_seed(x,1,cutoff)-mp.mpf('0.5')*source_seed(x,0,cutoff))**2,[1,mp.mpf('1.25'),mp.mpf('1.5'),2,3,mp.inf])
    out.append({'digits':digits,'integer_cutoff':cutoff,'M1_0':mp.nstr(mass.real,40),'M1_0_imaginary_residual':mp.nstr(mass.imag,8),'M1_0_1':mp.nstr(tilt.real,40),'M1_second_derivative_0':mp.nstr(mu2,40),'first_recurrence_per_tensor_factor':mp.nstr(mu2/mass.real,40)})
record={'status':'numerical evaluations only','scope':'No directed-rounding or omitted-tail certificate; h=1 is the analytic seed with zero finite-packet quotient.','values':out}
(ROOT/'checks'/'arithmetic_seed_numeric.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
