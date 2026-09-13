#!/usr/bin/env python3
"""Exploratory RH necessary-positivity search using the original g=2*xi.

No zero ordinates are input. Values come from the original theta seed.
This is arbitrary-precision quadrature, NOT validated interval arithmetic.
A negative numerical output is a candidate only, not an RH disproof.
"""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
import mpmath as mp

def theta_moments(max_index: int, dps: int, quad_degree: int,
                  theta_terms: int = 12, y_max: int = 4) -> list:
    """Return mu[2j]=integral_R y^(2j) exp(y/2) f0(exp(y)) dy.

    In the actual computation y=(z+1)*Y/2, with Jacobian Y/2,
    on [0,Y]. Reflection supplies factor 2; f0 has factor 2.
    Finite theta sum and finite y-range are recorded, not silently
    represented as exact integrals.
    """
    if min(dps, quad_degree, theta_terms, y_max) < 1 or max_index < 0:
        raise ValueError('Invalid quadrature parameter')
    mp.mp.dps = dps
    nodes = mp.calculus.quadrature.GaussLegendre(mp.mp).calc_nodes(
        quad_degree, mp.mp.prec)
    out = [mp.mpf(0) for _ in range(max_index+1)]
    Y, pi = mp.mpf(y_max), mp.pi
    for z, weight in nodes:
        y=(z+1)*Y/2
        x2=mp.exp(2*y)
        seed_half=mp.fsum((4*pi*pi*n**4*x2*x2 - 6*pi*n*n*x2)
                        *mp.exp(-pi*n*n*x2)
                        for n in range(1,theta_terms+1))
        base=4*mp.exp(y/2)*seed_half*weight*Y/2
        power=mp.mpf(1)
        for j in range(max_index+1):
            out[j]+=base*power
            power*=y*y
    return out

def log_moments(mu_even: list) -> tuple[list, list]:
    """F(w)=sum a_j w^j, F(z^2)=g(1/2+i*z); -F'/F=sum b_n w^n."""
    a=[(-1)**j*x/mp.factorial(2*j) for j,x in enumerate(mu_even)]
    if a[0] == 0:
        raise ZeroDivisionError('The retained mass F(0) must be nonzero')
    b=[]
    for n in range(len(a)-1):
        b.append((-(n+1)*a[n+1]
                  -mp.fsum(a[j]*b[n-j] for j in range(1,n+1)))/a[0])
    return a,b

def ldlt_pivots(matrix: list[list]) -> list:
    """Unpivoted LDL^T in the original monomial coordinates; no scaling."""
    n=len(matrix)
    L=[[mp.mpf(i==j) for j in range(n)] for i in range(n)]
    D=[]
    for j in range(n):
        d=matrix[j][j]-mp.fsum(L[j][k]*L[j][k]*D[k] for k in range(j))
        D.append(d)
        if d == 0:
            raise ArithmeticError(f'Zero pivot at index {j}; requires rank-sensitive analysis')
        for i in range(j+1,n):
            L[i][j]=(matrix[i][j]-mp.fsum(L[i][k]*L[j][k]*D[k]
                                         for k in range(j)))/d
    return D

def run(order: int, dps: int, degree: int, terms: int) -> dict:
    start=time.monotonic()
    mu=theta_moments(2*order, dps, degree, terms)
    a,b=log_moments(mu)
    results={}
    for shift in (0,1):
        H=[[b[i+j+shift] for j in range(order)] for i in range(order)]
        D=ldlt_pivots(H)
        det=mp.mpf(1); rows=[]
        for j,d in enumerate(D):
            det*=d
            rows.append({'dimension':j+1,'pivot':mp.nstr(d,80),
                         'determinant':mp.nstr(det,80),
                         'sign':int(mp.sign(d))})
        results[str(shift)]=rows
    direct=(mp.mpf(1)/2)*(mp.mpf(1)/2-1)*mp.pi**(-mp.mpf(1)/4)*mp.gamma(mp.mpf(1)/4)*mp.zeta(mp.mpf(1)/2)
    return {'status':'exploratory_not_interval_certified',
            'mpmath_version':mp.__version__, 'order':order, 'dps':dps,
            'gauss_legendre_degree':degree,'node_count':3*2**(degree-1),
            'theta_terms':terms,'y_interval':[0,4],
            'retained_g0':mp.nstr(mu[0],100),
            'g0_direct_difference':mp.nstr(mu[0]-direct,20),
            'a':[mp.nstr(x,100) for x in a],
            'b':[mp.nstr(x,100) for x in b],
            'matrices':results,'seconds':time.monotonic()-start}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--order',type=int,default=16)
    p.add_argument('--dps',type=int,default=120)
    p.add_argument('--quad-degree',type=int,default=8)
    p.add_argument('--theta-terms',type=int,default=12)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    if not 1<=args.order<=128:
        p.error('--order must be between 1 and 128')
    result=run(args.order,args.dps,args.quad_degree,args.theta_terms)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','order','dps','node_count','seconds']},indent=2))
    for shift,rows in result['matrices'].items():
        print('shift',shift,'positive pivots',sum(x['sign']>0 for x in rows),'of',len(rows))
        print('last',rows[-1])
if __name__=='__main__':
    main()
