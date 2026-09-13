#!/usr/bin/env python3
"""Numerical (not interval-certified) source and Gaussian calibrations."""
import argparse,json,math
from pathlib import Path
import mpmath as mp

p=argparse.ArgumentParser();p.add_argument('--digits',type=int,default=40);p.add_argument('--theta-cutoff',type=int,default=6);p.add_argument('--frequency-cutoff',type=int,default=90);p.add_argument('--output',required=True);args=p.parse_args()
mp.mp.dps=args.digits

def f0(x):
    return 2*mp.fsum((4*(mp.pi*n*n*x*x)**2-6*mp.pi*n*n*x*x)*mp.exp(-mp.pi*n*n*x*x) for n in range(1,args.theta_cutoff+1))

def gcrit(t):
    s=mp.mpf('0.5')+1j*t
    return s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

cuts=[1,mp.mpf('1.25'),mp.mpf('1.5'),2,3,5,mp.inf]
G=2*mp.quad(lambda x:f0(x)**2,cuts)
Ga=mp.quad(lambda x:(x*x+x**(-2))*f0(x)**2,cuts)
z0=gcrit(0)
rows=[]
for L in [1,2,4,8]:
    nmax=int(mp.floor(args.frequency_cutoff*L/(2*mp.pi)))
    raw=(abs(z0)**2+2*mp.fsum(abs(gcrit(2*mp.pi*n/L))**2 for n in range(1,nmax+1)))/L
    zero=abs(z0)**2/L
    rows.append({'L':L,'last_positive_frequency_index':nmax,'full_periodized_gram':mp.nstr(raw,32),
                 'zeroth_mode_gram':mp.nstr(zero,32),'nonzero_mode_gram':mp.nstr(raw-zero,32),
                 'relative_error_to_original':mp.nstr((raw-G)/G,12),
                 'formula_relative_bound_using_a_1_numerical_inputs':mp.nstr(2*Ga/(G*mp.expm1(L)),20)})
# Independent Gaussian correlation-versus-Fourier check.
gauss=[]
for L in [mp.mpf(2),mp.mpf(4),mp.mpf(8)]:
    count=60
    fourier=mp.pi/L*(1+2*mp.fsum(mp.exp(-2*mp.pi**2*n*n/L**2) for n in range(1,count+1)))
    corr=mp.sqrt(mp.pi/2)*(1+2*mp.fsum(mp.exp(-(n*L)**2/2) for n in range(1,count+1)))
    gauss.append({'L':int(L),'absolute_residual':mp.nstr(abs(fourier-corr),8),'gram':mp.nstr(fourier,30)})
report={'status':'numerical calibration, no validated rounding or tail enclosure supplied',
        'digits':args.digits,'theta_cutoff':args.theta_cutoff,'frequency_cutoff':args.frequency_cutoff,
        'arithmetic_seed_h':'1 (nonzero analytic seed, zero finite arithmetic quotient)',
        'original_source_gram':mp.nstr(G,40),'weighted_source_gram_a_1':mp.nstr(Ga,40),
        'g_at_half':mp.nstr(z0,40),'period_rows':rows,'gaussian_identity':gauss}
Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
