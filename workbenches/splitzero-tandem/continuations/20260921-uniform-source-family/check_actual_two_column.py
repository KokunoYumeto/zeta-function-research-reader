from pathlib import Path
import sympy as s,json
P=Path(__file__).parent;checks=[]
def ck(n,v):
 if not bool(v):raise AssertionError(n)
 checks.append(n)
def zero(A):return all(s.cancel(x)==0 for x in A)
def simp(A):return A.applyfunc(s.cancel)
def projector(B):return simp(B*(B.H*B).inv()*B.H)
W=s.Matrix([[1,s.I,2,0],[s.I,1,0,2],[1,2,s.I,1]])
T=s.Matrix([[1,0,s.I],[0,1,1],[1,1,0],[s.I,0,1]])
J=s.eye(3).row_join(W);R=(s.eye(3)-W*T).col_join(T)
X=s.eye(7)[:,:3];phi=s.eye(7)[:,3];B=X.row_join(R)
ck('physical:section',zero(J*R-s.eye(3)))
ck('physical:full_joint_source_rank',B.rank()==6)
PX=projector(X);PJ=projector(B);Pnext=projector(B.row_join(phi))
z=simp((s.eye(7)-PJ)*phi);h=s.cancel((z.H*z)[0]);w=simp(J*z);f=J*phi
ck('physical:nonzero_residual',h>0)
C=J*PX*J.H;CJ=simp(J*PJ*J.H);C1=C+f*f.H;CJ1=simp(J*Pnext*J.H)
gg=simp(w*w.H/h);Om=simp(CJ-C);Om1=simp(CJ1-C1)
ck('joint:rank_one_increment',zero(CJ1-CJ-gg))
ck('normal:exact_difference',zero(Om1-Om-gg+f*f.H))
GJ=CJ.inv();joint=s.cancel(1+(w.H*GJ*w)[0]/h)
ck('joint:rank_one_determinant',s.cancel(CJ1.det()/CJ.det()-joint)==0)
for eta in [s.Integer(0),s.Rational(1,7),s.Rational(2,3),s.Integer(1)]:
 Ce=simp((1-eta)*C+eta*CJ);G=simp(Ce.inv())
 nextC=simp((1-eta)*C1+eta*CJ1)
 a=s.cancel((1-eta)*(f.H*G*f)[0]);c=s.cancel(eta*(w.H*G*w)[0]/h)
 cross=s.cancel(eta*(1-eta)*(f.H*G*w)[0]*(w.H*G*f)[0]/h)
 det=s.cancel(nextC.det()/Ce.det());R0=s.cancel(C1.det()/C.det())
 ck(f'{eta}:full_cross_determinant',s.cancel(det-(1+a)*(1+c)+cross)==0)
 ck(f'{eta}:actual_two_sided_bound',1+a<=det<=(1+a)*joint)
 Z=s.cancel(Ce.det()/C.det());Z1=s.cancel(nextC.det()/C1.det())
 ck(f'{eta}:normal_source_factorization',s.cancel(det-R0*Z1/Z)==0)
 # Positive source range avoids taking a square root of h.
 F=f.row_join(w);H=s.diag(1/(1-eta),h/eta) if 0<eta<1 else None
 if H is not None:
  V=s.Matrix([[1,s.I],[1,2]]);FV=F*V;HV=V.H*H*V
  ck(f'{eta}:nondiagonal_source_gram',zero(FV*HV.inv()*FV.H-((1-eta)*f*f.H+eta*gg)))
  ck(f'{eta}:source_gram_determinant',s.cancel((HV+FV.H*G*FV).det()/HV.det()-det)==0)
out={'status':'passed','exact_checks':len(checks),'checks':checks,'scope':'Exact auxiliary complex physical source with one fixed section, all source projections and normal cross Grams. Tests TC4–9,12,15,24–25; not an actual xi quartet or asymptotic validation.'}
(P/'TWO_COLUMN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
