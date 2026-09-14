#!/usr/bin/env python3
"""Numerical actual theta-seed masses; not interval arithmetic or an RH test."""
import argparse,json
from pathlib import Path
import mpmath as mp

def evaluate(dps:int,terms:int)->dict:
    if dps<25 or terms<1:raise ValueError('dps >=25 and terms >=1 required')
    with mp.workdps(dps):
        def f(x):
            return 2*mp.fsum((4*(mp.pi*n*n*x*x)**2-6*(mp.pi*n*n*x*x))*
                            mp.exp(-mp.pi*n*n*x*x) for n in range(1,terms+1))
        intervals=[mp.mpf(1),mp.mpf('1.25'),mp.mpf('1.5'),mp.mpf(2),mp.mpf(3),mp.mpf(5),mp.inf]
        mass=2*mp.quad(lambda x:f(x)**2,intervals)
        information=8*mp.quad(lambda x:mp.log(x)**2*f(x)**2,intervals)
        return {'dps':dps,'theta_terms':terms,'mass':mp.nstr(mass,35),
                'log_derivative_energy':mp.nstr(information,35),
                'energy_over_mass':mp.nstr(information/mass,35),
                'scope':'Numerical quadrature plus finite integer sum. No validated rounding or tail enclosure.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();out={'h':'1 (actual g=2 xi seed; not a nonempty arithmetic packet)',
        'runs':[evaluate(45,6),evaluate(65,8)]}
    args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
