#!/usr/bin/env python3
"""Numerical theta-seed coefficients. Not interval arithmetic or a zero certificate."""
from pathlib import Path
import json, math
import mpmath as mp
import sympy as sp
z=sp.symbols('z')
q=[4*z*z-6*z]
for j in range(3):q.append(sp.expand(2*z*(q[-1]-sp.diff(q[-1],z))-q[-1]/2))
qcs=[[sp.Poly(p,z).nth(i) for i in range(sp.degree(p,z)+1)] for p in q]
x=sp.symbols('x');alpha=sp.Rational(13,2)
b=[sp.Integer(1),x]
for n in range(1,6):b.append(sp.expand(x*b[-1]-n*(n+alpha-1)*b[-2]))

def run(dps,cutoff):
    mp.mp.dps=dps
    moments=[mp.mpf('0')]*7
    for r,raw in enumerate(qcs):
        coeff=[mp.mpf(str(c)) for c in raw];total=mp.mpf('0')
        for n in range(1,cutoff+1):
            a=mp.pi*n*n
            for m in range(n,cutoff+1):
                b0=mp.pi*m*m;C=a+b0;ex=mp.exp(-C)
                I=[mp.sqrt(mp.pi)*mp.erfc(mp.sqrt(C))/(2*mp.sqrt(C))]
                for j in range(2*(len(coeff)-1)):
                    I.append((mp.mpf(j)+mp.mpf('.5'))/C*I[-1]+ex/(2*C))
                val=sum(coeff[i]*coeff[j]*a**i*b0**j*I[i+j]
                        for i in range(len(coeff)) for j in range(len(coeff)))
                total+=(1 if n==m else 2)*val
        moments[2*r]=8*total
    lam=mp.mpf(13)/4;c=mp.power(2,1-2*lam)*mp.gamma(2*lam)
    cs={}
    for j in [0,2,4,6]:
        p=sp.Poly(b[j],x)
        val=sum(mp.mpf(str(p.nth(i)))*moments[i] for i in range(j+1))
        cs[str(j)]=mp.nstr(val/(c*math.factorial(j)*mp.rf(2*lam,j)),45)
    return {'precision_digits':dps,'theta_integer_cutoff':cutoff,'reference_lambda':'13/4',
            'reference_mass':mp.nstr(c,45),'moments':{str(j):mp.nstr(moments[j],45) for j in [0,2,4,6]},
            'gamma_coefficients':cs,'scope':'Numerical truncated theta evaluation; no interval or integer-tail certificate; h=1 has zero finite arithmetic quotient.'}

if __name__=='__main__':
    result=[run(50,6),run(70,8)]
    out=Path(__file__).resolve().parent/'checks/seed_coefficients.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
