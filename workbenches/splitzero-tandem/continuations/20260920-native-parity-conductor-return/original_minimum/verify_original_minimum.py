"""Exact finite diagnostics for EQ1--20, not zeta-zero/asymptotic evidence.

Uses an unchanged positive discrete physical-coordinate Gram and a literal
finite differential conductor, with a nontrivial polynomial-relation kernel.
Failures use explicit exceptions and remain active under python -O.
"""
import itertools
import json
from pathlib import Path
import sympy as s

checks = []
def check(name, truth):
    if not truth:
        raise RuntimeError(name)
    checks.append(name)
    print('PASS '+name, flush=True)
def zero(a):
    return all(s.cancel(x) == 0 for x in a)

i=s.I
N=6; v=1; u=s.symbols('u'); centre=s.Rational(3,2)
H=s.Matrix(N+1,N+1,lambda r,t:sum(
    (centre-i*y)**r*(centre+i*y)**t for y in range(-4,5)))
H=H.applyfunc(s.expand)
check('positive physical Gram: all exact leading minors',
      all(H[:r,:r].det()>0 for r in range(1,N+2)))
mu=[0,2,3,-1,i,2-i,4+i]
raw=s.Matrix(N,N+1,lambda r,t:s.binomial(t,r)*mu[t-r] if r<=t else 0)
chi=u**5+u+1
reduce=s.Matrix(5,N,lambda r,t:s.rem(u**t,chi,u).coeff(u,r))
C=reduce*raw
A=C.col_join(s.Matrix([[1,0,0,0,0,0,0]]))
Cbar=s.eye(5).row_join(s.zeros(5,1))
check('full observation and conductor surjective', A.rank()==6 and C.rank()==5)
check('actual factor relation',zero(Cbar*A-C))
Hi=H.inv(); Q=(A*Hi*A.H).inv(); T=(C*Hi*C.H).inv()
L=Hi*C.H*T; R=Q.inv()*Cbar.H*T
check('successive quotient identity',zero(T-(Cbar*Q.inv()*Cbar.H).inv()))
check('attained source lift',zero(C*L-s.eye(5)))
check('attained observation lift',zero(Cbar*R-s.eye(5)))
check('exact source to observation receiver',zero(A*L-R))
check('attained observation energy',zero(R.H*Q*R-T))
Iw=s.eye(5)[:,:4]; TW=Iw.H*T*Iw
HL=H[:1,:1]; HLR=H[:1,1:5]; HRL=H[1:5,:1]; HR=H[1:5,1:5]
S=HR-HRL*HL.inv()*HLR
B=s.Matrix(4,4,lambda r,t:s.binomial(v+t,r)*mu[v+t-r] if r<=t else 0)
inc=s.eye(7)[:,:5]
Low=inc*(-HL.inv()*HLR).col_join(s.eye(4))*B.inv()
Glow=B.H.inv()*S*B.inv(); D=Low-L*Iw
check('literal restricted conductor lift',zero(C*Low-Iw))
check('full low-degree quotient energy',zero(Low.H*H*Low-Glow))
check('all lift-difference columns in full kernel',zero(C*D))
check('EQ9 exact positive lift correction',zero(Glow-TW-D.H*H*D))
check('negative control: equating two minima fails',not zero(Glow-TW))

O=s.Matrix([[1,2,3,4],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
E=s.Matrix([[0,0,0,0],[1,2,0,1],[0,1,1,2],[1,0,2,1]])
Y=s.eye(4);Y[0,2]=i;Y[1,3]=s.Rational(1,3)
G=TW; Hlabel=Y.H*TW*Y
H8=(Hlabel+E.H*G*E).row_join(E.H*G*O).col_join(
    (O.H*G*E).row_join(O.H*G*O))
Hi_formula=Hlabel.inv().row_join(-Hlabel.inv()*E.H*O.H.inv()).col_join(
    (-O.inv()*E*Hlabel.inv()).row_join(
     O.inv()*(G.inv()+E*Hlabel.inv()*E.H)*O.H.inv()))
Eval=E.row_join(O)
check('EQ15 full eight-state inverse',zero(H8*Hi_formula-s.eye(8)))
check('EQ14 inherited quotient',zero(Eval*Hi_formula*Eval.H-G.inv()))
section=s.zeros(4).col_join(O.inv())
check('unique section retains all eval values',zero(Eval*section-s.eye(4)))
check('section exact energy',zero(section.H*H8*section-G))
kernel=s.eye(4).col_join(-O.inv()*E)
check('exact graph kernel',zero(Eval*kernel))
check('kernel original label energy',zero(kernel.H*H8*kernel-Hlabel))
check('negative control: removing cross blocks changes quotient',
      not zero(Eval*s.diag(Hlabel+E.H*G*E,O.H*G*O).inv()*Eval.H-G.inv()))
mix=[]
for pair in itertools.combinations(range(4),2):
    Dj=s.diag(*[-1 if r in pair else 1 for r in range(4)])
    BJ=O*(s.eye(4)-Dj)*O.inv()*E
    g=s.diag(s.eye(4),Dj)
    check(f'pair {pair} exact action defect',zero(Eval*g*kernel-BJ))
    check(f'pair {pair} rank exactly two',BJ.rank()==2)
    obsdef=R*Iw*BJ
    check(f'pair {pair} unchanged observation energy',zero(obsdef.H*Q*obsdef-BJ.H*G*BJ))
    mix.append(BJ)
check('all mixing images span target',s.Matrix.hstack(*mix).rank()==4)
small=s.Matrix([[1,i,2,3]])
check('nonzero one-dimensional observation detects some flip',any(not zero(small*b) for b in mix))
b=s.Matrix([1,i,2-i,3,4,i]); target=Cbar*b; res=b-R*target
check('terminal-like exact remainder belongs to kernel',zero(Cbar*res))
check('EQ20 full retained class Pythagoras',zero(b.H*Q*b-target.H*T*target-res.H*Q*res))

# Independently re-enter the upstream polynomial; use the 24-term determinant.
a,y,z,w=s.symbols('a y z w')
P=s.Matrix([
 a**3*z+2*a**2*y-i*a,
 -a**3*y**2*z-2*i*a**2*y*z+a**2*w-2*a**2*y**3-10*i*a*y**2+3*a*z+y,
 2*a**3*y**3*z+6*i*a**2*y**2*z+2*a**2*w*y+4*a**2*y**4+2*i*a*w-4*i*a*y**3-2*a*y*z+2*i*z+7*y**2,
 2*a**3*y**4*z+8*i*a**2*y**3*z+a**2*w*y**2+4*a**2*y**5+2*i*a*w*y+7*i*a*y**4-10*a*y**2*z-4*i*y*z-w-3*y**3])
J=P.jacobian([a,y,z,w]);det=0
for p in itertools.permutations(range(4)):
    sign=(-1)**sum(p[j]>p[k] for j in range(4) for k in range(j+1,4))
    det+=sign*s.prod(J[j,p[j]] for j in range(4))
check('FC31 independently expanded determinant',s.expand(det)==-2)
for label,point in [('M',(0,0,i/2,0)),('N',(i,-1,-3*i,13))]:
    check('FC31 collision '+label,zero(P.subs(dict(zip((a,y,z,w),point)))-s.Matrix([0,0,-1,0])))
out={'scope':'Exact finite diagnostics; no hypothetical zeta input and no asymptotic inference',
     'passed':len(checks),'checks':checks}
Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'negative_controls':2,'status':'all pass'}))
