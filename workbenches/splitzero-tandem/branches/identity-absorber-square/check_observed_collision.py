"""Exact complex-overlap checks in an auxiliary six-dimensional metric model.

This verifies formula implementations and negative controls. It is not an
evaluation of a native arithmetic period and does not replace the proofs.
"""
from pathlib import Path
import json
import sympy as S

root=Path(__file__).resolve().parent
checks=[];negative=[]
def equal(name,x,y):
    z=x-y
    ok=all(S.simplify(c)==0 for c in z) if isinstance(z,S.MatrixBase) else S.simplify(z)==0
    assert ok,name
    checks.append(name)
def different(name,x,y):
    z=x-y
    ok=any(S.simplify(c)!=0 for c in z) if isinstance(z,S.MatrixBase) else S.simplify(z)!=0
    assert ok,name
    negative.append(name)

I=S.I;eye=S.eye(6);scale=S.diag(2,3,4,5,6,7);G=scale.H*scale
w=S.Matrix([1,I,1,1,1,2]);V=eye-2*w*w.H/(w.H*w)[0]
J=scale.inv()*V[:,:4]
dag=lambda X:X.H*G
e=scale.inv()*eye[:,0];f=scale.inv()*eye[:,1];eps=S.Rational(3,2)
u=dag(J)*e;v=dag(J)*f;U=u.row_join(v);gram=U.H*U
a,r,d=gram[0,0],gram[0,1],gram[1,1];Delta=S.factor(gram.det())
assert a>0 and Delta>0 and S.im(r)!=0
P=U*gram.inv()*U.H;A=U*U.H;Psrc=e*dag(e)+f*dag(f);Pobs=J*dag(J)
R=eps*f*dag(e);Pe=e*dag(e)
C0=S.diag(1,2,4,7,11,16)+S.ones(6)
C0[0,2]=1+I;C0[2,0]=1-I
C=scale.inv()*C0*scale;CB=dag(J)*C*J
s,t,z=S.symbols('s t z')
F=R+s*Pe;FB=dag(J)*F*J;lam=a*s+eps*r;star=-eps*r/a
Rs=S.simplify(FB.subs(s,star));W0=I*(FB.subs(s,0)-FB.subs(s,0).H)
Ws=I*(Rs-Rs.H)
equal('Observation isometry in nonidentity metric',dag(J)*J,S.eye(4))
equal('Source Hermitian action',C.H*G,G*C)
equal('Source deformation identity',F*F,s*F)
equal('Observed rank-one formula',FB,(eps*v+s*u)*u.H)
equal('Observed deformation relation',FB*FB,lam*FB)
equal('Complete hidden product',dag(J)*F*(eye-Pobs)*F*J,(s-lam)*FB)
equal('Measured support defect',A-A*A,dag(J)*Psrc*(eye-Pobs)*Psrc*J)
equal('Range projection',P*P,P)
equal('Collision square zero',Rs*Rs,S.zeros(4))
different('Collision remains nonzero',Rs,S.zeros(4))
different('Native observed fibre is not the collision',FB.subs(s,0),Rs)
different('Measured support retains its nonidempotent defect',A*A,A)
equal('Original trace gives collision height',S.im(star),S.trace(W0)/(2*a))
equal('Original signed current correction',Ws-W0,2*eps*S.im(r)*u*u.H/a)
equal('Original current plane',P*W0,W0)
equal('Collision current plane',P*Ws,Ws)
equal('Both kernels have dimension two',S.Integer(4-W0.rank()),S.Integer(4-Ws.rank()))
equal('Original current annihilates exact complement',W0*(S.eye(4)-P),S.zeros(4))
equal('Collision current annihilates exact complement',Ws*(S.eye(4)-P),S.zeros(4))

M0=CB+FB.subs(s,0);Ms=CB+FB
p0=S.factor((z*S.eye(4)-M0).det());ps=S.factor((z*S.eye(4)-Ms).det())
q0=S.factor((u.H*(z*S.eye(4)-M0).adjugate()*u)[0])
equal('Full characteristic polynomial receiver',ps,p0-s*q0)
for tt,ss,zz in [(0,star,2+3*I),(S.Rational(1,3),S.Rational(5,7),-2+2*I)]:
    Mt=Ms.subs(s,tt);Mss=Ms.subs(s,ss)
    Gt=(zz*S.eye(4)-Mt).inv();Gs=(zz*S.eye(4)-Mss).inv()
    mt=(u.H*Gt*u)[0];den=S.simplify(1-(ss-tt)*mt)
    assert den!=0
    predicted=Gt+(ss-tt)*Gt*u*u.H*Gt/den
    equal('Full resolvent receiver '+str(tt),Gs,predicted)
    equal('Scalar resolvent receiver '+str(tt),(u.H*Gs*u)[0],mt/den)
    x=S.Matrix([1,I,2,-1]);y=S.Matrix([2,1-I,0,3])
    equal('Marked ordered inverse pairing '+str(tt),(x.H*Gs*y)[0],(x.H*Gt*y)[0]+(ss-tt)*(x.H*Gt*u)[0]*(u.H*Gt*y)[0]/den)
    source=zz*S.eye(4)-Mt
    qtt=(u.H*source.adjugate()*u)[0]
    qss=(u.H*(zz*S.eye(4)-Mss).adjugate()*u)[0]
    equal('Adjugate polynomial invariance '+str(tt),qtt,qss)
    sco=tt+1/mt
    singular=zz*S.eye(4)-Ms.subs(s,sco)
    equal('Failed inverse constructs exact eigenvector '+str(tt),singular*Gt*u,S.zeros(4,1))
    equal('Failed inverse has one-dimensional kernel '+str(tt),S.Integer(4-singular.rank()),S.Integer(1))

out={'scope':'Auxiliary six-dimensional positive nonidentity metric with complex overlapping observed columns; exact rational arithmetic. No native period evaluation.',
     'a':str(a),'r':str(r),'Delta':str(Delta),'s_star':str(star),'checks':checks,'negative_controls':negative,'passed':True}
(root/'OBSERVED_COLLISION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'negative_controls':len(negative),'passed':True}))
