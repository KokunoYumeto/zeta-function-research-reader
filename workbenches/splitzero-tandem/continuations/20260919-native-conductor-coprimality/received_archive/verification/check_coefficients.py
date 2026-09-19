"""Exact auxiliary checks for the displayed coefficient bookkeeping.
These do not verify the analytic norm asymptotics or evaluate an xi packet.
"""
import json
from pathlib import Path
import sympy as s

a,v,CB,A0,A1,B1,CS,eta,M,L2,L3,La=s.symbols('a v CB A0 A1 B1 CS eta M L2 L3 La')
q=(a+1)**2
Delta=16*a-48
CP=2*CB-8*A1+4*A0
CG=2*CB-4*A1
K2=CB-4*A1+2*B1-2*L2
Z=1024*(A1-2*B1)-176*CP+4*v*(A1-A0)-192+512*L2
Zd=4*CP+16*(2*B1-A1)
checks=[]
def check(name,expr):
    reduced=s.simplify(s.expand(expr))
    if reduced != 0:
        raise RuntimeError(f'{name}: {reduced}')
    checks.append(name)
for eps in (0,1):
    ell=s.Rational(eps,4)*(a-1)
    n=q-Delta+ell
    m=Delta-v
    H=2*Delta-v-ell
    # Terms omitted here are analytically O(a log a) or smaller.
    model=(CB*n*n+4*n*(H*A1-m*A0)+s.Rational(1,2)*m*m*(La-4*L2)
      +2*H*H*B1-(2*A0-s.Rational(3,4))*m*m-2*ell*ell*L2
      +CS*n-2*eta*M*q)
    result=(CB*q*q+(-16*CP+eps*CG/4)*a*q+128*q*La
      +q*(CS-2*eta*M-eps*CG/4+eps*K2/16-Z-eps*Zd))
    remainder=s.Poly(s.expand(model-result),a)
    for power in (4,3,2):
        check(f'lower-covariance-order-{eps}-power-{power}',remainder.coeff_monomial(a**power))
    upper=(CB*q*q+eps*CG*a*q/4+q*(CS-2*eta*M-eps*CG/4+eps*K2/16))
    combined=16*CP*a*q-128*q*La+(Z+eps*Zd)*q
    check(f'combined-order-{eps}',upper-result-combined)
# The complete q-coefficient of the actual proper-source ambient displacement.
Cdisp=1024*(A1-2*B1)-192+256*L2+288*L3
raw=(512*(2*A1-A0)-2048*B1+256*(2*A0-s.Rational(3,4))
     +288*(3*L2+L3)-128*(4*L2)-32*(3*L2))
check('proper-displacement-constant',raw-Cdisp)
# Endpoint ECL identities give the curvature coefficient.
lw,lz,lc=s.symbols('lw lz lc')
Lv=6*lw-2*lz-2
Fv=-7+2*lw+lc+Lv
CBv=9-8*L2+Fv
A1v=2*(1-L2)-(8-4*lw-2*lc)/4
B1v=lc/2-L2
check('gamma-curvature',CBv-4*A1v+2*B1v-2*L2-(4*lw-2*lz-4*L2))
# Character-clearing multiplier: all four nonzero characters are covered.
import itertools
for degree in range(7):
    for e in itertools.product(range(degree+1),repeat=4):
        if sum(e)!=degree: continue
        weight=sum((j+1)*e[j] for j in range(4))%5
        if weight==0: continue
        i=next(i for i in range(1,5) if 4*i%5==weight)
        coeff=[e[j]+4-(4 if j==i-1 else 0) for j in range(4)]
        if min(coeff)<0 or sum((j+1)*coeff[j] for j in range(4))%5:
            raise RuntimeError('character-clearing identity failed')
checks.append('character-clearing-through-degree-six')
# Sharp mixed/nonlinear identification is an endpoint identity, not two separate zeros.
print(json.dumps({'status':'passed','checks':checks,'count':len(checks),
 'scope':'exact coefficient and character bookkeeping only'},indent=2))
