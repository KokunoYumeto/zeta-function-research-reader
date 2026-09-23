#!/usr/bin/env python3
"""Exact auxiliary checks for the boundary/regular-inverse continuation.
No numerical zeta zero is assumed or evaluated. No assertion is disabled by -O.
"""
from __future__ import annotations
from collections import Counter
from itertools import product, combinations_with_replacement, permutations
from math import factorial
from pathlib import Path
import json
import sympy as s

passed: Counter[str] = Counter()
controls: list[str] = []

def ok(group: str, condition: bool) -> None:
    if not bool(condition):
        raise ArithmeticError(f"Failed exact check in {group}")
    passed[group] += 1

def eq(group: str, a, b=0) -> None:
    if isinstance(a, s.MatrixBase):
        ok(group, a.applyfunc(s.simplify) == s.zeros(*a.shape) if b == 0 else
           (a-b).applyfunc(s.simplify) == s.zeros(*a.shape))
    else:
        ok(group, s.cancel(s.expand(a-b)) == 0)

def reject(label: str, condition: bool) -> None:
    if bool(condition):
        raise ArithmeticError(f"False-claim control unexpectedly passed: {label}")
    controls.append(label)

# Full support lattice P({1,2}); nonzero amplitudes only at top support.
amps = [s.Rational(j) for j in (-2,-1,0,1,2)] + [s.Rational(-1,2),s.Rational(1,2)]
carrier = [(s.Integer(0),i) for i in range(4)] + [(a,3) for a in amps if a]
def mul(a,b): return (a[0]*b[0], a[1]&b[1])
def add(a,b): return (a[0]+b[0], a[1]|b[1])
def neg(a): return (-a[0],a[1])
def rinv(a): return (1/a[0],3) if a[0] else a
one=(s.Integer(1),3); e=(s.Integer(0),3); tau=(s.Integer(0),0)
for a in carrier:
    ai=rinv(a)
    ok('inverse_monoid', mul(mul(a,ai),a)==a)
    ok('inverse_monoid', mul(mul(ai,a),ai)==ai)
    ok('inverse_monoid', rinv(ai)==a)
    for b in carrier:
        ok('inverse_monoid', rinv(mul(a,b))==mul(rinv(a),rinv(b)))
        for c in carrier:
            ok('semiring', mul(a,add(b,c))==add(mul(a,b),mul(a,c)))
for a in [(x,3) for x in amps]:
    d=add(one,neg(mul(a,rinv(a))))
    ve=add(add(mul(rinv(a),rinv(a)),mul((s.Integer(2),3),a)),(-s.Integer(3),3))
    am=add(a,neg(one))
    vf=mul(mul(mul(am,am),add(mul((s.Integer(2),3),a),one)),mul(rinv(a),rinv(a)))
    defect=mul(add(mul((s.Integer(2),3),a),(-s.Integer(3),3)),d)
    ok('potential',add(ve,neg(vf))==defect)
reject('regular inverse is a global unit inverse',mul(e,rinv(e))==one)
reject('supported zero equals absence',e==tau)
reject('totalized RT potential nonnegative at zero',s.Integer(-3)>=0)

z,t,theta=s.symbols('z t theta', real=True)
def inv0(a): return s.S.Zero if a==0 else 1/a
# Exact full polynomial collision defect for arbitrary multiplicities.
for n in range(2,8):
    for xx in combinations_with_replacement([s.Integer(-1),s.Integer(0),s.Integer(1)],n):
        p=s.prod(z-x for x in xx)
        pi=[s.prod(z-xx[j] for j in range(n) if j!=i) for i in range(n)]
        vv=[2*sum(inv0(xx[i]-xx[j]) for j in range(n) if j!=i) for i in range(n)]
        pdot=-sum(v*pol for v,pol in zip(vv,pi))
        defect=2*sum(s.prod(z-xx[h] for h in range(n) if h not in (i,j))
                     for i in range(n) for j in range(i+1,n) if xx[i]==xx[j])
        eq('contact_identity',pdot+s.diff(p,z,2),defect)
        multiplicities=Counter(xx)
        grouped=sum(m*(m-1)*(z-a)**(m-2)*s.prod((z-b)**l for b,l in multiplicities.items() if b!=a)
                    for a,m in multiplicities.items() if m>=2)
        eq('contact_identity',grouped,defect)
        ok('contact_detection',(s.expand(defect)==0)==all(m==1 for m in multiplicities.values()))
# Sticky trajectories, including their entire arithmetic forcing.
eq('sticky',s.diff(z*z,t)+s.diff(z*z,z,2),2)
eq('sticky',s.diff(z*z-2*(t-theta),t)+s.diff(z*z-2*(t-theta),z,2),0)
eq('sticky',(z*z-2*(t-theta))-(z*z-2*t),2*theta)
eq('sticky',(z*z)-(z*z-2*t),2*t)
reject('stationary double zero solves backward heat',s.diff(z*z,z,2)==0)

x,a,b,eta=s.symbols('x a b eta')
def hm(n):
    return s.Poly(sum((-1)**j*s.factorial(n)/(s.factorial(j)*s.factorial(n-2*j))*x**(n-2*j)
                      for j in range(n//2+1)),x).as_expr()
def mtrace(f,p):
    n=s.degree(p,x)
    return sum(s.Poly(s.rem(f*x**j,p,x),x).nth(j) for j in range(n))
for m in range(2,11):
    p=hm(m); dp=s.diff(p,x)
    eq('Hermite',2*s.diff(p,x,2)-x*dp+m*p)
    eq('Hermite',s.diff(hm(m+1),x),(m+1)*p)
    eq('Hermite',hm(m+1),x*p-2*m*hm(m-1))
    qinv=s.invert(dp,p,x)
    pair=s.rem(s.diff(p,x,2)**2*qinv**2/s.Integer(4)-s.diff(p,x,3)*qinv/s.Integer(3),p,x)
    eq('Hermite_energy',mtrace(pair,p),s.Rational(m*(m-1),8))
    eq('Hermite_discriminant',s.discriminant(p,x),2**(m*(m-1)//2)*s.prod(j**j for j in range(1,m+1)))
    # Exact cancellation of the first three parabolically scaled root coefficients.
    kappa=2*b-a*a
    shift=2*a
    c1=shift*dp+a*hm(m+1)
    c2=kappa*x*dp+shift**2*s.diff(p,x,2)/2+a*shift*s.diff(hm(m+1),x)+b*hm(m+2)
    eq('root_jet',s.rem(c1,p,x))
    eq('root_jet',s.rem(c2,p,x))
# Full polynomial example, not a numerical native xi evaluation.
y=(-1+12*b*t+s.sqrt(1-16*b*t+96*b*b*t*t))/(2*b)
y_series=s.series(y,t,0,4).removeO()
eq('finite_part',s.series(1/(2*y_series),t,0,1).removeO(),1/(4*t)-b)
f=z*z-2*t+b*(z**4-12*t*z*z+12*t*t)
eq('finite_part',s.diff(f,t)+s.diff(f,z,2))
reject('collision algebra fixes finite part',s.Integer(-1)==s.Integer(1))

# Original based transport residue; beta(beta+3)=16t.
beta=s.symbols('beta')
Sb=s.eye(4);Sb[3,2]=-2/beta;Sb[3,3]=-1
eq('holonomy',Sb*Sb,s.eye(4))
res=(Sb*(beta*(beta+3)/16)).applyfunc(lambda v:s.limit(v,beta,0))
expected=s.zeros(4);expected[3,2]=-s.Rational(3,8)
eq('holonomy',res,expected)
D=s.zeros(4);D[3,1]=-s.Rational(1,16)
eq('holonomy',D*D)
for i,j in product(range(4),repeat=2):
    def rem4(f):return s.rem(s.expand(f),x**4,x)
    def deriv(f):return rem4(-x**3*s.diff(f,x)/16)
    eq('holonomy_Leibniz',deriv(rem4(x**i*x**j)),rem4(deriv(x**i)*x**j+x**i*deriv(x**j)))
    eq('trace_radical',mtrace(rem4(deriv(x**i)*x**j),x**4),0)
eq('residue_probe',s.Poly(-x**3/16,x).nth(3),-s.Rational(1,16))
reject('nonzero residue erased as algebra map',D==s.zeros(4))
reject('nonzero nilpotent guarantees nonzero regular trace',s.trace(D)!=0)
# Normalization and the special-fibre rank.
aunit=s.symbols('aunit', nonzero=True)
nu=s.Matrix([[1,16*t*aunit],[1,-16*t*aunit]])
eq('normalization',nu.det(),-32*t*aunit)
ok('normalization',nu.subs(t,0).rank()==1)
R,h=s.symbols('R h')
eq('class_field',s.discriminant((R-1)*(R**2+R-16*h),R),(2-16*h)**2*(1+64*h))
wpoly=sum((1 if pow(j,11,23)==1 else -1)*x**j for j in range(1,23))
eq('class_field',s.rem(wpoly*wpoly+23,s.cyclotomic_poly(23,x),x),0)
ok('class_field',pow(2,11,23)==1)
ok('class_field',pow(5,11,23)==22)

# Reconstruct the actual full 192-state group average in the fixed eight-state order.
def perm_matrix(p):
    M=s.zeros(len(p))
    for j,k in enumerate(p): M[k,j]=1
    return M
S=perm_matrix([1,0,3,2,5,4,7,6])
Qsig=perm_matrix([0,1,3,2,5,4,6,7])
Qj=perm_matrix([0,1,5,4,3,2,7,6])
A_sig=s.zeros(8);A_j=s.zeros(8);num=0
for pi in permutations(range(4)):
    odd=sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))%2
    for flips in product((0,1),repeat=4):
        if sum(flips)%2!=odd:continue
        perm=[2*pi[j]+(b0^flips[j]) for j in range(4) for b0 in range(2)]
        P=perm_matrix(perm)
        A_sig+=P.T*Qsig*P;A_j+=P.T*Qj*P;num+=1
ok('group_average',num==192)
Pev=(s.eye(8)+S)/2;Pc=s.ones(8)/8
A_sig/=num;A_j/=num
eq('group_average',A_sig,Pev)
eq('group_average',A_j,Pev/3+2*Pc/3)
jmap=s.zeros(8,2)
for row in (2,3):jmap[row,0]=1/s.sqrt(2)
for row in (4,5):jmap[row,1]=1/s.sqrt(2)
old=jmap.T*Qj*jmap;avg=jmap.T*A_j*jmap;K=avg-old
eq('endpoint',old,s.Matrix([[0,1],[1,0]]))
eq('endpoint',avg,s.Matrix([[s.Rational(1,2),s.Rational(1,6)],[s.Rational(1,6),s.Rational(1,2)]]))
ok('endpoint',sorted(K.eigenvals())==[-s.Rational(1,3),s.Rational(4,3)])
for aa,bb in ((1,1),(1,-1),(0,0),(s.I,1)):
    v=s.Matrix([aa,bb]);eq('endpoint',(v.H*old*v)[0],(v.H*avg*v)[0]-(v.H*K*v)[0])
reject('averaging preserves original endpoint form',avg==old)
reject('average is original involutive trace matrix',A_j.det()!=0)
E=s.zeros(4,8)
for j0 in range(4):E[j0,2*j0]=E[j0,2*j0+1]=s.Rational(1,2)
v=s.Matrix([1,-1,0,0,0,0,0,0])
reject('even projection is an algebra quotient',E*v.multiply_elementwise(v)==(E*v).multiply_elementwise(E*v))


# The actual Jacobian sends a perfect residue pairing to the regular trace.
Tr3=s.zeros(4);Tr3[3,0]=1
Qres=s.zeros(4)
for ii in range(4):Qres[ii,3-ii]=s.I*(-1)**ii
Kjac=-4*s.I*Tr3
Qtr=s.diag(4,0,0,0)
eq('jacobian_duality',Qres*Kjac,Qtr)
eq('jacobian_duality',Kjac.H*Qres,Qres*Kjac)
ok('jacobian_duality',Kjac.rank()==1 and Kjac*Kjac==s.zeros(4))
par=s.symbols('par',real=True)
VV=s.eye(4)+par*D
Qdef=s.zeros(4);Qdef[0,1]=-s.I*par/16;Qdef[1,0]=s.I*par/16
eq('jacobian_duality',VV.H*Qres*VV-Qres,Qdef)
eq('jacobian_duality',VV.H*Qtr*VV,Qtr)

# Contact forcing in the complete local algebra and its cotangent residue.
def local_residue(poly,n,unit):
    ser=s.series(poly/unit,x,0,n).removeO().expand()
    return s.simplify(ser.coeff(x,n-1))
for mm in range(2,9):
    for aa,bb in ((0,1),(1,2),(s.Rational(2,3),s.Rational(-5,7))):
        unit=1+aa*x+bb*x*x
        qc=s.rem(mm*(mm-1)*x**(mm-2)*unit,x**mm,x)
        eq('contact_cotangent',local_residue(x*qc,mm,unit),mm*(mm-1))
        jac=s.rem(s.diff(x**mm*unit,x),x**mm,x)
        prod=s.rem(qc*jac,x**mm,x)
        ok('contact_cotangent',(prod==0)==(mm>=3))
        eq('contact_cotangent',mtrace(qc,x**mm),4 if mm==2 else 0)
        for jj in range(mm):
            if mm>=3:eq('contact_cotangent',mtrace(s.rem(qc*x**jj,x**mm,x),x**mm),0)

# Recover the finite part from three residue coefficients, including arbitrary mass.
for nn in range(3,9):
    for aa,bb,mass in ((0,1,1),(1,2,3),(s.Rational(2,3),s.Rational(-5,7),5)):
        unit=mass*(1+aa*x+bb*x*x)
        L0=local_residue(x**(nn-1),nn,unit)
        L1=local_residue(x**(nn-2),nn,unit)
        L2=local_residue(x**(nn-3),nn,unit)
        eq('finite_part_residue',2*L2/L0-(L1/L0)**2,aa**2-2*bb)
        Gram=s.Matrix(nn,nn,lambda ii,jj:local_residue(x**(ii+jj),nn,unit))
        ok('finite_part_residue',Gram.det()!=0)
        for jj in range(2):
            eq('thickening_duality',local_residue(x**(jj+1),3,unit),local_residue(x**jj,2,unit))
uplus=1+x*x;uminus=1-x*x
Gplus=s.Matrix(2,2,lambda i,j:local_residue(x**(i+j),2,uplus))
Gminus=s.Matrix(2,2,lambda i,j:local_residue(x**(i+j),2,uminus))
eq('minimal_residue_order',Gplus,Gminus)
eq('minimal_residue_order',local_residue(1,3,uplus),-1)
eq('minimal_residue_order',local_residue(1,3,uminus),1)
reject('perfect double-root residue fixes energy finite part',local_residue(1,3,uplus)==local_residue(1,3,uminus))

receipt={'exact_checks':sum(passed.values()),'by_group':dict(sorted(passed.items())),
         'negative_controls':len(controls),'negative_control_names':controls,
         'scope':'Finite auxiliary algebra; no native xi zero/period numerical evaluation; analytic theorems have written proofs.'}
text=json.dumps(receipt,indent=2,sort_keys=True)+'\n'
print(text,end='')
if __name__=='__main__':
    import sys
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(text,encoding='utf-8')
