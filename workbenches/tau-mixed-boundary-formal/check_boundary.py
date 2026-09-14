#!/usr/bin/env python3
"""Independent exact boundary checks; polynomial fixtures, not zero-location tests."""
from __future__ import annotations
from itertools import product
import argparse,json,math
import sympy as S
v,a=S.symbols('v a');rho=S.Rational(3,4)

def require(p,message):
    if not bool(p):raise AssertionError(message)

def check_case(m,k):
    inds=list(product(range(m),repeat=k));where={b:i for i,b in enumerate(inds)}
    p=len(inds);powers=[k+sum(b) for b in inds]
    N=S.zeros(p);R=S.zeros(p)
    for b in inds:
        for i in range(k):
            c=list(b)
            if c[i]+1<m:
                c[i]+=1;N[where[tuple(c)],where[b]]+=1
            else:
                c[i]=0;R[where[tuple(c)],where[b]]+=1
    A=k*rho*S.eye(p)+N+a*v**m*R
    L=k*rho*S.eye(p)+v*(N+a*R)
    D=S.diag(*(v**n for n in powers));F=S.diag(*(v**(n-1) for n in powers))
    require((L*D-D*A).applyfunc(S.expand)==S.zeros(p),'lattice intertwiner')
    require((L*F-F*A).applyfunc(S.expand)==S.zeros(p),'divided intertwiner')
    basis=[(i,j) for i,n in enumerate(powers) for j in range(n)]
    pos={x:i for i,x in enumerate(basis)}
    socle=[pos[(i,n-1)] for i,n in enumerate(powers)]
    v_kernel=[pos[(i,j)] for i,j in basis if j+1==powers[i]]
    require(v_kernel==socle,'all and only v-kernel coordinates')
    C=S.zeros(len(basis),p)
    for i,row in enumerate(socle):C[row,i]=1
    out=S.zeros(len(basis),p)
    for src,j in ((i,n-1) for i,n in enumerate(powers)):
        out[pos[(src,j)],src]+=k*rho
        for dst in range(p):
            coeff=N[dst,src]+a*R[dst,src]
            if coeff!=0 and j+1<powers[dst]:out[pos[(dst,j+1)],src]+=coeff
    require(out==C*(k*rho*S.eye(p)+N),'full nilpotent on socle')
    require(L.subs(v,0)==k*rho*S.eye(p),'ordinary quotient scalar action')
    require(sum(powers)==k*(m+1)*p//2,'complete ordered length')
    require(N**(k*(m-1)+1)==S.zeros(p),'sum nilpotency upper')
    unit=S.zeros(p,1);unit[0,0]=1
    last=N**(k*(m-1))*unit
    coeff=math.factorial(k*(m-1))//math.factorial(m-1)**k
    require(last[-1,0]==coeff,'top multinomial including repeated jets')
    return {'m':m,'k':k,'full_rank':p,'cyclic_length':1+k*(m-1),'torsion_rank_over_Q_a':len(basis),'socle_rank':len(socle)}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--negative',choices=['nilpotent-zero','omit-jacobian','empty-absence','diagonal-gram']);args=parser.parse_args()
    if args.negative:
        if args.negative=='nilpotent-zero':accepted=S.Matrix([[0,0],[1,0]])==S.zeros(2)
        elif args.negative=='omit-jacobian':accepted=(0+1+2)==(1+2+3)
        elif args.negative=='empty-absence':accepted=(frozenset({1}),frozenset())==(frozenset(),frozenset())
        else:accepted=(S.Matrix([[1]])+S.Matrix([[1]])).T*(S.Matrix([[1]])+S.Matrix([[1]]))==S.Matrix([[2]])
        print(json.dumps({'control':args.negative,'false_claim_accepted':bool(accepted)},sort_keys=True))
        raise SystemExit(0 if accepted else 1)
    cases=[check_case(m,k) for m,k in [(1,1),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2)]]
    require(cases[3]['full_rank']==4 and cases[3]['cyclic_length']==3,'mixed complement retained')
    F0=S.Matrix([[1],[0]]);F1=S.Matrix([[1],[1]]);M=S.Matrix([[2,1],[1,3]])
    full=(F0+F1).T*M*(F0+F1)
    cross=F0.T*M*F0+F1.T*M*F1+F0.T*M*F1+F1.T*M*F0
    require(full==cross,'complete polarized mixed Gram')
    require(full!=F0.T*M*F0+F1.T*M*F1,'cross terms genuinely present')
    require((frozenset({1}),frozenset())!=(frozenset(),frozenset()),'present empty inner face')
    print(json.dumps({'success':True,'cases':cases,'cross_gram':str(full),'scope':'Exact full ordered diagonal lattice and socle action; no l-adic or analytic certification.'},sort_keys=True))
if __name__=='__main__':main()
