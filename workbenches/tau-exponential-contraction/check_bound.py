#!/usr/bin/env python3
"""Finite exact regressions and separate high-precision diagnostics.
No actual zeta packet, arithmetic integral, or Lean certificate is asserted.
Requires sympy and mpmath. All tests use explicit exceptions (also under -O).
"""
from __future__ import annotations
import argparse, json, math
from fractions import Fraction as F
from pathlib import Path
import sympy as s
import mpmath as mp


def need(condition: bool, label: str) -> None:
    if not condition:
        raise ArithmeticError(label)


def log_interval(x: F, terms: int = 24) -> tuple[F,F]:
    need(x >= 1, 'positive log argument')
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo,lo+tail


def gamma_moments(order: int):
    """Exact Taylor coefficients of cos(t)^(-1/2); mass is SEVEN."""
    cs=[F(0)]*(order+1)
    for j in range(0,order+1,2):
        cs[j]=F((-1)**(j//2),math.factorial(j))
    fs=[F(1)]
    for n in range(1,order+1):
        fs.append(-sum((F(2*n-j,2)*cs[j]*fs[n-j] for j in range(1,n+1)),F(0))/n)
    return [s.Rational(7*x.numerator*math.factorial(n),x.denominator) for n,x in enumerate(fs)]


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--negative',choices=['ratio','penalty_count','factor','constant'])
    args=ap.parse_args()
    counts={}
    lo,hi=log_interval(F(50000,45927))
    need(lo>F(84969826010092,10**15),'certified lower rate')
    need(hi<F(84969826010093,10**15),'certified upper rate')
    need(sum((F(5,2)**j/F(math.factorial(j)) for j in range(7)),F(0))>12,'exp(5/2)>12')
    need(F(35,36)>F(81,100),'sqrt(35)/6>9/10')
    need(F(1,36)+(F(5,2)-F(9,10))/72==F(1,20),'elliptic majorant rational arithmetic')
    need(F(100,81)*F(500,567)==F(50000,45927),'band product')
    if args.negative=='constant':
        need(F(100,81)*F(500,567)==F(50000,45928),'deliberately changed rate denominator')
    counts['exact_universal_constant_checks']=6

    y,z=s.symbols('y z')
    moments=gamma_moments(40)
    ps=[s.Integer(1),y]
    for n in range(1,12):
        ps.append(s.expand(y*ps[-1]-s.Rational(n)*(n-s.Rational(1,2))*ps[-2]))
    def integ(poly):
        p=s.Poly(s.expand(poly),y)
        return sum(c*moments[int(i[0])] for i,c in p.terms())
    for n in range(12):
        norm=7*s.factorial(n)*s.rf(s.Rational(1,2),n)
        need(integ(ps[n]**2)==norm,f'Gamma norm {n}')
        for j in range(n):
            need(integ(ps[n]*ps[j])==0,f'Gamma orthogonality {n},{j}')
    gen=sum(ps[n]*z**n/s.factorial(n) for n in range(10))
    ode=s.Poly(s.expand((1+z*z)*s.diff(gen,z)-(y-z/2)*gen),z)
    need(all(ode.coeff_monomial(z**j)==0 for j in range(9)),'generating ODE')
    counts['exact_gamma_norm_and_pair_checks']=12+66+1

    blocks=0
    for k in range(3,102):
        r=k//3
        bs=[3]*r
        bs[-1]+=k%3
        need(sum(bs)==k and all(3<=b<=5 for b in bs),'block partition')
        for N in range(8):
            need(N+1<=2*N+r,'top degree face bound')
        blocks+=1
    counts['exact_block_partitions']=blocks
    counts['exact_top_face_checks']=blocks*8

    fixtures=[y**2, y**4-s.Rational(15,8)*y**2+s.Rational(289,256), (y*y+1)**2]
    tested=0
    for phi in fixtures:
        q=s.degree(phi,y)
        hn=[7*s.factorial(n)*s.rf(s.Rational(1,2),n) for n in range(2*q+1)]
        cols=[]
        for n in range(2*q+1):
            rem=s.Poly(s.rem(ps[n],phi,y),y)
            cols.append(s.Matrix([rem.nth(j) for j in range(q)]))
        V={};G={};eps={};d={}
        Ay=s.zeros(q)
        for j in range(q):
            pp=s.Poly(s.rem(y**(j+1),phi,y),y)
            Ay[:,j]=s.Matrix([pp.nth(i) for i in range(q)])
        for N in range(q-1,2*q+1):
            KN=s.zeros(q)
            for n in range(N+1): KN+=cols[n]*cols[n].T/hn[n]
            GN=KN.inv();G[N]=GN;V[N]=s.factor(GN.det())
            if N>=q:
                d[N]=s.factor(V[N]/V[N-1])
                r=N-q
                J=s.Matrix(r+1,r+1,lambda i,j:integ(phi**2*y**(i+j)))
                eta=s.factor(J.det()/(J[:-1,:-1].det() if r else 1))
                need(d[N]==hn[N]/eta,'original monic relation ratio')
                if args.negative=='ratio': need(d[N]==eta/hn[N],'deliberate inverse norm ratio')
            if N<2*q:
                HH=s.I*(Ay-KN*Ay.T*GN)
                eps[N]=s.factor(s.trace(HH*HH)/2)
                need(s.trace(HH)==0,'total reflection trace')
                need((cols[N].T*GN*cols[N+1])[0]==0,'adjacent parity pairing')
                tested+=1
        for N in range(q-1,2*q):
            bn=hn[N+1]/hn[N]
            rhs=bn*(1/d[N+1]-1)*(1 if N==q-1 else 1-d[N])
            need(s.factor(eps[N]-rhs)==0,'canonical local radius')
            if args.negative=='factor' and N==q:
                need(s.factor(eps[N]-bn*(1/d[N+1]-1))==0,'deliberately omitted contraction')
        wm={N:(1 if N in (q-1,2*q-1) else 2) for N in range(q-1,2*q)}
        exponents={n:0 for n in range(q,2*q+1)}
        for N,w in wm.items():
            exponents[N+1]+=w
            if N>=q: exponents[N]+=w
        need(sum(exponents.values())==4*q-1,'penalty exponent count')
        if args.negative=='penalty_count': need(sum(exponents.values())==4*q,'deliberate endpoint count')
        left=s.prod(eps[N]**wm[N] for N in wm)
        total=V[q-1]*V[q]/(V[2*q-1]*V[2*q])
        window=hn[2*q-1]*hn[2*q]/(hn[q-1]*hn[q])
        penalties=s.prod((1-d[n])**e for n,e in exponents.items())
        need(s.factor(left-total*window*penalties)==0,'weighted complete action product')
    counts['exact_canonical_radius_rows']=tested
    counts['exact_full_action_products']=len(fixtures)

    # Independent diagnostic: exact elementary exponential-weight moments,
    # high precision only at this stage (not interval arithmetic).
    mp.mp.dps=180
    diagnostics=[]
    for q in (1,2,4,8,16):
        for r in sorted(set((0,1,q//2,q))):
            if r>q: continue
            n=q+r
            alpha=mp.pi/2
            def moment(t):
                return mp.mpf(0) if t%2 else 2*mp.factorial(2*q+t)/alpha**(2*q+t+1)
            H=mp.matrix(r+1,r+1)
            for i in range(r+1):
                for j in range(r+1): H[i,j]=moment(i+j)
            if r:
                leading=mp.lu_solve(H[:-1,:-1],mp.matrix([H[i,r] for i in range(r)]))
                eta=H[r,r]-sum(H[r,i]*leading[i] for i in range(r))
            else: eta=H[0,0]
            lower=(50*mp.pi*n/63)*mp.mpf(n)**(2*n)*mp.e**(-2*n)*(mp.mpf(100)/81)**q*(mp.mpf(500)/567)**r
            need(eta>=lower,'two-band monic minimum numerical diagnostic')
            diagnostics.append({'q':q,'r':r,'log_minimum_over_bound':mp.nstr(mp.log(eta/lower),20)})
    for q in list(range(1,30))+[100,1000]:
        W=2*(mp.loggamma(4*q+1)-mp.loggamma(2*q+1))-4*q*mp.log(2)+mp.log(mp.mpf(2*q-1)/(2*(4*q-1)))
        C=4*q*mp.log(q)+(8*mp.log(2)-4)*q-mp.log(2)
        err=mp.mpf(1)/(16*q)+mp.mpf(1)/(4*q-2)
        need(C-err<=W<=C,'Gamma window interval diagnostic')
    counts['high_precision_monic_minimum_diagnostics']=len(diagnostics)
    counts['high_precision_window_diagnostics']=31
    print(json.dumps({'status':'pass','scope':'Exact finite structural regressions and separately labelled high-precision diagnostics; no actual arithmetic packet, no Lean run.', 'counts':counts,'rate_interval':['0.084969826010092','0.084969826010093'],'diagnostics':diagnostics},sort_keys=True,indent=2))

if __name__=='__main__':
    main()
