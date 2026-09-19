"""Exact auxiliary diagnostics; not an arithmetic-period or analytic proof certificate."""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path
import sympy as sp

checks=[]
def check(name: str, value: bool) -> None:
    if not bool(value):
        raise RuntimeError(name)
    checks.append(name)

a,v,CB,a0,a1,b1,Cs,eta,Minv,L2,L3,La=sp.symbols('a v CB a0 a1 b1 Cs eta Minv L2 L3 La')
CG=2*CB-4*a1
Cp=2*CB-8*a1+4*a0
K2=CB-4*a1+2*b1-2*L2
q=(a+1)**2
Q=(a-7)**2
Delta=q-Q
Z=1024*(a1-2*b1)-176*Cp+4*v*(a1-a0)-192+512*L2
Zd=4*Cp+16*(2*b1-a1)
for eps in (0,1):
    ell=sp.Rational(eps,4)*(a-1)
    n=Q+ell
    m=Delta-v
    H=2*Delta-v-ell
    original=CB*n**2+4*n*(H*a1-m*a0)+m**2*(La-4*L2)/2+2*H**2*b1-(2*a0-sp.Rational(3,4))*m**2-2*ell**2*L2+Cs*n-2*eta*Minv*a**2
    claimed=CB*q**2+(-16*Cp+eps*CG/4)*a*q+128*q*La+q*(Cs-2*eta*Minv-eps*CG/4+eps*K2/16-Z-eps*Zd)
    diff=sp.Poly(sp.expand(original-claimed),a)
    for power in (4,3,2):
        check(f'lower covariance order {power}, Gamma lane {eps}',sp.expand(diff.coeff_monomial(a**power))==0)
    upper=CB*q**2+eps*CG*a*q/4+q*(Cs-2*eta*Minv-eps*CG/4+eps*K2/16)
    combined=16*Cp*a*q-128*q*La+q*(Z+eps*Zd)
    check(f'complete matched return, Gamma lane {eps}',sp.expand(upper-claimed-combined)==0)

b=8*a+24
M=Delta-v
nonlog=4*b*Delta*(2*a1-a0)-8*b*(2*Delta-v)*b1+2*(2*a0-sp.Rational(3,4))*M*b
logs=(b**2*(La-3*L2)-(M+b)**2*(La-3*L2-L3)+M**2*(La-4*L2))/2
coeff=sp.Poly(sp.expand(nonlog+logs),a).coeff_monomial(a**2)
check('proper-source ambient displacement coefficient',sp.expand(coeff-(-128*La+1024*(a1-2*b1)-192+256*L2+288*L3))==0)

lw,lz,lc=sp.symbols('lw lz lc')
L=6*lw-2*lz-2
lam=8-4*lw-2*lc
F=-lam/2-3+L
sub={CB:9-8*L2+F,a1:2*(1-L2)-lam/4,b1:lc/2-L2}
check('K2 closed ECL identity',sp.expand(K2.subs(sub)-(4*lw-2*lz-4*L2))==0)

for i in range(1,5):
    weights=[j-i for j in range(1,5) if j!=i]
    for r in range(5):
        n=sum(sum(w*c for w,c in zip(weights,alpha))%5==r for alpha in itertools.product(range(5),repeat=3))
        check(f'fixed charge count i={i}, r={r}',n==25)
for vv in range(1,9):
    n=sum(sum(bb)<=vv-1 for bb in itertools.product(range(vv),repeat=3))
    check(f'fixed nilpotent monomial count v={vv}',n==math.comb(vv+2,3))

ok=True
for exps in itertools.product(range(9),repeat=4):
    if sum(exps)>8:
        continue
    w=sum((j+1)*e for j,e in enumerate(exps))%5
    if w:
        i=(4*w)%5
        cleared=[e+4 for e in exps]
        cleared[i-1]-=4
        ok=ok and min(cleared)>=0 and sum((j+1)*e for j,e in enumerate(cleared))%5==0
check('proper-kernel character clearing, all monomials through degree eight',ok)
check('corner jet nilpotence order',max(i+j for i in range(8) for j in range(8))==14)
check('two-active corner homogenization degree',4+5*14==74)
check('exceptional corner homogenization degree',12+5*14==82)

x=sp.symbols('x')
roots=[sp.Integer(j) for j in (1,2,3,4)]
obs=sp.Matrix([[1,2,3,4]])
A=sp.diag(*roots)
stack=sp.Matrix.vstack(*[obs*A**j for j in range(4)])
R=sp.zeros(4)
for i,lam0 in enumerate(roots):
    e=sp.prod((x-mu)/(lam0-mu) for mu in roots if mu!=lam0)
    for j in range(4):
        R[i,j]=sp.expand(e).coeff(x,j)/obs[0,i]
check('explicit full-packet observation inverse',R*stack==sp.eye(4))
check('one-step kernel is nontrivial',len(obs.nullspace())==3)
check('short-stack dimension guard',sp.Matrix.vstack(*[obs*A**j for j in range(3)]).rank()==3)

out={'kind':'exact auxiliary identities only','count':len(checks),'checks':checks,'not_checked':['analytic estimates','actual xi packet','actual period matrices or their exceptional minors','native projected metric values']}
print(json.dumps(out,indent=2))
