#!/usr/bin/env python3
"""Numerical evaluation of NOTE (68), (73)--(76).
Not interval-certified: quadrature nodes are IEEE doubles; mpmath evaluates
zeta and the removable quotient at configurable working precision.
No root multiplicity or asymptotic theorem is certified by this script.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
import mpmath as mp

def g(s):
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

def ratio(a,b):
    ev=mp.det(mp.matrix([[a[0],a[1],a[2]],[a[1],a[2],a[3]],[a[2],a[3],a[4]]]))
    return a[0]*a[1]**2*b[1]**2*(b[0]*b[2]-b[1]**2)/(ev*(a[1]*a[3]-a[2]**2)**2)

def evaluate(order,dps,cutoff):
    mp.mp.dps=dps
    rho=mp.zetazero(1); gamma=mp.im(rho)
    bounds=[mp.mpf(x) for x in (0,4,8,12)]+[gamma-mp.mpf('0.5'),gamma+mp.mpf('0.5')]+[mp.mpf(x) for x in (18,24,32,45,60,80) if x<cutoff]+[mp.mpf(cutoff)]
    bounds=sorted(set(bounds))
    xs,ws=np.polynomial.legendre.leggauss(order)
    a=[mp.mpf('0')]*5; direct=[mp.mpf('0')]*3
    for left,right in zip(bounds,bounds[1:]):
        mid=(left+right)/2; width=(right-left)/2
        for xf,wf in zip(xs,ws):
            t=mid+width*mp.mpf(float(xf)); wt=width*mp.mpf(float(wf))
            h=gamma**2-t**2; gg=g(mp.mpf('0.5')+1j*t)
            if abs(h)<mp.power(10,-dps//2):
                quotient=1j*mp.diff(g,rho)/(-2*gamma)
            else: quotient=gg/h
            density=abs(quotient)**2/(2*mp.pi)
            seed=abs(gg)**2/(2*mp.pi)
            power=mp.mpf(1)
            for j in range(5):
                a[j]+=2*wt*density*power
                if j<3:direct[j]+=2*wt*seed*power
                power*=t*t
    b=[gamma**4*a[j]-2*gamma**2*a[j+1]+a[j+2] for j in range(3)]
    mass=mp.sqrt(2*mp.pi)
    ag=[mass*v for v in [1,mp.mpf(1)/2,mp.mpf(7)/4,mp.mpf(139)/8,mp.mpf(5473)/16]]
    bg=[gamma**4*ag[j]-2*gamma**2*ag[j+1]+ag[j+2] for j in range(3)]
    ba=mp.log(ratio(a,b)); br=mp.log(ratio(ag,bg))
    text=lambda x:mp.nstr(x, min(dps-5,30))
    return {'order_per_interval':order,'working_decimal_precision':dps,
            'positive_axis_cutoff':cutoff,'gamma_approximation':text(gamma),
            'arithmetic_even_moments_0_to_8':[text(v) for v in a],
            'seed_even_moments_from_relation':[text(v) for v in b],
            'seed_even_moments_direct':[text(v) for v in direct],
            'log_four_volume_arithmetic':text(ba),'log_four_volume_gamma':text(br),
            'signed_arithmetic_minus_gamma':text(ba-br),
            'warning':'Numerical quadrature only. Double-precision quadrature nodes. No interval tail/rounding/root certification.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--order',type=int,default=48);p.add_argument('--dps',type=int,default=35);p.add_argument('--cutoff',type=int,default=80);p.add_argument('--out',default='first_pair.json');a=p.parse_args()
    t=time.perf_counter(); result=evaluate(a.order,a.dps,a.cutoff);result['elapsed_seconds']=time.perf_counter()-t
    Path(a.out).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
