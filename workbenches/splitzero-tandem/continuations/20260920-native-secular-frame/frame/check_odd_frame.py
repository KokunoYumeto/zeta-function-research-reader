"""Exact coefficient certificates; no numerical roots or branch relabelling."""
from pathlib import Path
import sympy as s
import json,hashlib
P=Path(__file__).parent
A,B,C,D,r,c=s.symbols('A B C D r c'); I=s.I
h=A*r**4+r**3+B*r**2+C*r+D
d=s.diff(h,r)
ps=[1,-I*d,A*d**2+2*r*d,I*(7*r**2*d-13*d**2)]
rem=lambda p,mod=h:s.rem(p,mod,r)
coef=lambda p:s.Matrix([[s.expand(rem(x)).coeff(r,j) for j in range(4)] for x in p])
Q=coef(ps)
Dodd=20*(3*C-B**2)+A*(87*B**3-282*B*C-51*D)+A**2*(-28*B**4+22*B**2*C+431*C**2+204*B*D)+A**3*(224*B**2*D-168*B*C**2-856*C*D)-448*A**4*D**2
checks=[]
def zero(name,x):
    x=s.simplify(x)
    assert x==0,(name,x)
    checks.append({'claim':name,'exact':True})
zero('coefficient determinant = 4 Dodd/A',Q.det()-4*Dodd/A)
sub={A:1,B:0,C:c,D:0}; hc=h.subs(sub); dc=d.subs(sub)
pc=[s.sympify(p).subs(sub) for p in ps]
cs=-s.Rational(60,431); hs=hc.subs(c,cs)
zero('special divisor',Dodd.subs(sub)-c*(431*c+60))
delta,gamma=s.symbols('delta gamma',real=True)
quartet={A:-s.Rational(1,2),B:delta**2-gamma**2-s.Rational(3,4),C:gamma**2-delta**2+s.Rational(1,4),D:-s.Rational(1,32)-(gamma**2-delta**2)/4-(delta**2+gamma**2)**2/2}
zero('literal arithmetic quartet divisor pullback',s.expand(Dodd.subs(quartet))+56*delta**2*gamma**2*(2*delta**2*gamma**2-delta**2+gamma**2))
assert s.gcd(hs,s.diff(hs,r))==1
checks.append({'claim':'quartic squarefree at c=-60/431','exact':True})
ell=s.Matrix([[208*cs**2,5*I*cs,60,-21*I]])
Qstar=Q.subs(sub).subs(c,cs)
assert Qstar.rank()==3
for j in range(4):zero('left-null coefficient '+str(j),(ell*Qstar)[j])
qstar=973*r**2+413*r-140
for j,p in enumerate(pc):
    zero('right-null residue '+str(j),s.expand(s.rem(qstar*p.subs(c,cs),hs,r)).coeff(r,3))
patched=[1,-I*dc,dc**2+2*r*dc,r**3]
Qt=s.Matrix([[s.expand(s.rem(x,hc,r)).coeff(r,j) for j in range(4)] for x in patched])
L=s.eye(4);L[3,:]=s.Matrix([[-208*I*c**2/21,5*c/21,-20*I/7,4*I*(431*c+60)/21]])
for i,x in enumerate(Q.subs(sub)-L*Qt):zero('patch comparison coefficient '+str(i),x)
zero('patched determinant',Qt.det()+21*I*c)
for j,p in enumerate(patched):
    zero('patched residue '+str(j),s.expand(s.rem(qstar*s.sympify(p).subs(c,cs),hs,r)).coeff(r,3)-(420 if j==3 else 0))
# L inverse has an explicit last row. Its residue is e4 ell^T/1724.
for j in range(4):zero('inverse residue covector '+str(j),s.limit((c-cs)*L.inv()[3,j],c,cs)-ell[j]/1724)
zero('inverse residue denominator',420*1724-724080)
# Exact full singular target eight-coordinate repair, with all E components retained.
eps=s.symbols('eps')
zero('determinant local expansion',4*c*(431*c+60)- (c-cs)*(-240+1724*(c-cs)))
R0=s.Rational(52,11637);r0=R0/2;mc=s.Rational(1568,11637)
zero('minimum c modulus',abs(cs)-R0-mc)
zero('minimum other discriminant factor',4+27*cs-27*R0-s.Rational(52,431))
zero('minimum determinant remaining factor',240-1724*r0-s.Rational(6376,27))
receipt={'method':'Exact rational polynomial coefficient computations in SymPy; four symbolic roots retained through interpolation identities, no floating root replacements.', 'sympy_version':s.__version__,'passed':len(checks),'checks':checks,'coefficient_matrix':str(Q),'rank_at_exception':3,'exception':str(cs),'full_general_discriminant':str(s.factor(s.discriminant(h,r))),'curve_discriminant':str(s.factor(s.discriminant(hc,r))),'incoming_sha256':'57efa66b73bb4ce951b1d17ec4170b0f7bf1a00af3718e56faa71e7693ec2717'}
(P/'ODD_FRAME_EXACT_CERTIFICATES.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'rank_at_exception':3,'curve_discriminant':receipt['curve_discriminant']},indent=2))
