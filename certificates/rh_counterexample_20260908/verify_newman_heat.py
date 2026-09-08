"""Rigorous local real zeros of the actual de Bruijn--Newman heat integral.

No zeta values or zeta-zero inputs are used. A float theta-kernel quadrature
locates candidates only. Endpoint signs, derivative intervals, and omitted
n/u tail bounds certify the reported local zeros of the infinite integral.
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path

import flint
import scipy
from flint import acb, arb, ctx
from scipy.integrate import quad
from scipy.optimize import brentq

ctx.prec = 256
ctx.threads = 1
N = 8
UMAX = 2
TOL = arb(2)**(-170)


def scalar(q):
    if isinstance(q,Fraction):
        return arb(q.numerator)/q.denominator
    return arb(str(q))


def tail_bounds():
    pi = arb.pi()
    # For real u>=0 each Phi summand is nonnegative and bounded by its
    # first term: 2*pi*n²*e^(4u)>3. Thus no triangle-bound factor is lost.
    # On [0,2], u^k <=16 (k<=4), exp(tu²)<=e, e^(9u)<=e^18,
    # and |sin(zu)|,|cos(zu)|<=e^2 when |Im z|<=1. Length=2.
    # x^4 exp(-pi*x²) decreases for x>=8, so the sum n>=9 is at
    # most its integral from 8 to infinity. Two integrations by parts
    # and integral_N^infty exp(-pi*x²)dx <= exp(-pi*N²)/(2*pi*N)
    # give the displayed bracket, all evaluated with outward rounding.
    n = arb(N)
    omitted_n = (64*pi*pi*arb(21).exp()*(-pi*n*n).exp()
                 *(n**3/(2*pi)+3*n/(4*pi*pi)+3/(8*pi**3*n)))
    # u>=2: |Phi|<=6*pi²*e^(9u)*exp(-pi*e^(4u)). Indeed n^4<=
    # 16^(n-1), n²-1>=3(n-1), and the resulting geometric sum <3.
    assert 1/(1-16*(-3*pi).exp()) < 3
    # For k<=4, u^k<=u^4. Then
    # 4 log u+u²/4+10u <=29u²/4 <=8u² <=e^(4u) <=pi*e^(4u)/2.
    # Substitute v=e^(4u), bound 1/v<=e^-8, integrate exp(-pi*v/2).
    omitted_u = 3*pi*arb(-8).exp()*(-pi*arb(8).exp()/2).exp()
    return omitted_n,omitted_u


NTAIL, UTAIL = tail_bounds()
TAIL = NTAIL+UTAIL


def float_value(t,z):
    def integrand(u):
        e4 = math.exp(4*u)
        phi = sum((2*math.pi**2*n**4*math.exp(9*u)
                   -3*math.pi*n*n*math.exp(5*u))*math.exp(-math.pi*n*n*e4)
                  for n in range(1,N+1))
        return math.exp(t*u*u)*phi*math.cos(z*u)
    return sum(quad(integrand,j/4,(j+1)/4,epsabs=1e-14,
                    epsrel=1e-12,limit=100)[0] for j in range(8))


def heat(t,z,k=0,interval_parameter=False):
    """Ball enclosure of d_z^k H_t(z), k=0,1,2, for real t,z."""
    pi = arb.pi()
    evaluations = [0]
    def f(u,analytic):
        evaluations[0] += 1
        e4 = (4*u).exp()
        e5 = (5*u).exp()
        e9 = e5*e4
        phi = acb(0)
        for n in range(1,N+1):
            phi += (2*pi*pi*n**4*e9-3*pi*n*n*e5)*(-pi*n*n*e4).exp()
        trig = (z*u).cos() if k%2==0 else (z*u).sin()
        if k%4 in (1,2):
            trig = -trig
        return (t*u*u).exp()*phi*u**k*trig
    # A parameter ball gives an irreducible range, not quadrature error.
    # A relaxed integration target avoids futile refinement below that range;
    # the returned ball remains rigorous and must still exclude zero.
    tol = arb('1e-12') if interval_parameter else TOL
    vals = [acb.integral(f,arb(j)/4,arb(j+1)/4,
                         rel_tol=tol,abs_tol=tol,
                         eval_limit=12000,depth_limit=18) for j in range(8)]
    if not all(v.is_finite() and v.imag.contains(0) for v in vals):
        raise ArithmeticError("Nonfinite or non-real integration result")
    result = sum(v.real for v in vals)+arb(0,TAIL.upper())
    return result,evaluations[0]


def certify_root(tq):
    started = time.time()
    t = scalar(tq)
    approximate = brentq(lambda x:float_value(float(tq),x),26,31,xtol=1e-12)
    # Float search is not evidence. These decimal endpoint rationals are
    # independently checked by the complete infinite-integral enclosure.
    left = Fraction(format(approximate-4e-9,'.12f'))
    right = Fraction(format(approximate+4e-9,'.12f'))
    lval,leval = heat(t,scalar(left))
    rval,reval = heat(t,scalar(right))
    opposite = bool((lval>0 and rval<0) or (lval<0 and rval>0))
    if not opposite:
        raise ArithmeticError("Endpoint signs not certified")
    box = scalar((left+right)/2)+arb(0,scalar((right-left)/2).upper())
    deriv,deval = heat(t,box,1,True)
    second,seval = heat(t,box,2,True)
    if deriv.contains(0):
        raise ArithmeticError("Derivative zero exclusion failed")
    speed = second/deriv
    out = {
        "t_exact":str(tq),"left_exact":str(left),"right_exact":str(right),
        "width_exact":str(right-left),"root_box":str(box),
        "H_left_ball":str(lval),"H_right_ball":str(rval),
        "opposite_signs_certified":opposite,
        "Hprime_on_root_box":str(deriv),"Hsecond_on_root_box":str(second),
        "unique_simple_real_zero_in_box_certified":True,
        "local_implicit_root_speed_Hsecond_over_Hprime":str(speed),
        "integrand_evaluations":leval+reval+deval+seval,
        "elapsed_seconds":time.time()-started,
        "scope":"A unique simple real zero at this exact time, and its local real-analytic continuation speed. No continuation between separate reported times is certified here.",
    }
    print("ROOT",str(tq),str(box),"SPEED",str(speed),
          "seconds",out['elapsed_seconds'],flush=True)
    return out


def main():
    started = time.time()
    roots = []
    for tq in (Fraction(0),Fraction(1,20),Fraction(1,5)):
        roots.append(certify_root(tq))
        if roots[-1]['elapsed_seconds'] > 120:
            break
    script = Path(__file__)
    data = {
        "status":"local_real_root_certificates_not_RH_resolution",
        "script_sha256":hashlib.sha256(script.read_bytes()).hexdigest(),
        "software":{"python":platform.python_version(),
                    "python_flint":flint.__version__,"scipy":scipy.__version__},
        "precision_bits":256,"threads":1,"N":N,"u_cutoff":UMAX,
        "function":"H_t(z)=integral_0^infinity exp(t*u^2)*Phi(u)*cos(z*u) du",
        "Phi":"sum_(n>=1)(2*pi^2*n^4*exp(9u)-3*pi*n^2*exp(5u))*exp(-pi*n^2*exp(4u))",
        "zeta_function_calls":0,"zeta_zero_inputs":0,
        "source":"D. H. J. Polymath, arXiv:1904.12438, equations phidef and htdef in source TeX",
        "source_TeX_locator":"debruijn.tex lines 124-135",
        "source_TeX_sha256":"560a28fe31bec92dd793820222e9e73a1fc6958a08344033a946b2ccaba225e5",
        "uniform_tail_domain":"real 0<=t<=1/4, |Im z|<=1, z derivatives k=0,...,4",
        "omitted_n_tail_ball":str(NTAIL),"omitted_u_tail_ball":str(UTAIL),
        "total_uniform_absolute_tail_bound":str(TAIL),
        "tail_derivations":"See fully explicit inequalities in tail_bounds() in the hash-bound script. Both tails added as symmetric real error balls after interval quadrature.",
        "root_certificates":roots,
        "nonclaims":["No nonreal zero found; these certificates concern real roots only",
                      "No global zero-free region or RH conclusion",
                      "Separate-time boxes are not a certified connecting continuation tube",
                      "Software trusted: Arb integration and interval arithmetic, not formal proof-assistant verification"],
        "elapsed_seconds":time.time()-started,
    }
    script.with_name('newman_heat_results.json').write_text(
        json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print("DONE",data['elapsed_seconds'],flush=True)


if __name__ == '__main__':
    main()
