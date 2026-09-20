from pathlib import Path
import sympy as S,json
P=Path(__file__).parent
z,t=S.symbols('z t');checks=[]
def ck(v,name):
 if not v:raise AssertionError(name)
 checks.append(name)
for k,J,s,vflag in [(9,1,3,False),(9,2,2,True),(9,3,2,True),(13,2,3,False),(13,3,3,True)]:
 delta=S.Rational(1,3);gamma=S.Integer(3);c=S.Rational(k,2);cp=c-4
 bs=[4+(2*r-8)*delta-8*S.I*gamma for r in range(J)]
 aa=[(-1)**r*S.binomial(J-1,r) for r in range(J)] if vflag else [S.Integer(r+1) for r in range(J)]
 moments=[S.expand(sum(a*b**n for a,b in zip(aa,bs))) for n in range(J)]
 v=next(n for n,u in enumerate(moments) if u!=0)
 D=J*s-v-1
 lower=[cp+(2*a-k+8)*delta+S.I*(2*b-k+8)*gamma-c for a in range(k-7) for b in range(k-7)]
 assert D+1<=len(lower)
 nodes=lower[:D+1]
 B=S.prod(z+b for b in bs)
 C=S.Matrix([[S.cancel(sum(a*S.I**n/(x+b)**n for a,b in zip(aa,bs))) for n in range(1,s+1)] for x in nodes])
 # Reconstruct every coefficient from each coordinate data vector.
 denom=S.prod((b-bs[0]+t)**s for b in bs[1:])
 invden=S.series(S.S.One/denom,t,0,s).removeO()
 W=S.zeros(s,D+1)
 for ell,x in enumerate(nodes):
  Lag=S.prod((-bs[0]+t-nodes[j])/(x-nodes[j]) for j in range(D+1) if j!=ell)
  rec=S.Poly(S.expand(B.subs(z,x)**s*Lag*invden),t)
  for n in range(1,s+1):W[n-1,ell]=S.cancel(rec.nth(s-n)/(aa[0]*S.I**n))
 ck((W*C).applyfunc(S.simplify)==S.eye(s),'IK10 exact inverse k%d J%d s%d'%(k,J,s))
 for n in range(1,s+1):
  pp=S.cancel(B**s*sum(a*S.I**n/(z+b)**n for a,b in zip(aa,bs)))
  pp=S.Poly(S.expand(pp),z)
  target=S.I**n*(-1)**v*S.binomial(n+v-1,v)*moments[v]
  ck(pp.degree()==J*s-v-n and S.expand(pp.LC()-target)==0,'IK5–6 actual degree n%d k%d J%d'%(n,k,J))
 # Omitting the physical i^n changes the reconstruction.
 wrong=C*S.diag(*[S.I**(-n) for n in range(1,s+1)])
 ck((W*wrong-S.eye(s)).applyfunc(S.cancel)!=S.zeros(s),'negative missing physical phase')
 ck(C[:s-1,:].rank()<s,'negative insufficient observations')
# A small exact complex-metric fixture for the typed quotient receiver.
G=S.Matrix([[5,1,S.I,0],[1,6,1,0],[-S.I,1,7,1],[0,0,1,8]])
La=S.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1]])
Q=(La*G.inv()*La.H).inv();L=G.inv()*La.H*Q
Csel=S.Matrix([[0,1,S.I,0],[0,0,1,1]]);Gam=Csel*G.inv()*Csel.H
R=Csel*L
ck((Csel-R*La).applyfunc(S.cancel)==S.zeros(2,4),'IK12 original quotient factor')
ck((R*Q.inv()*R.H-Gam).applyfunc(S.cancel)==S.zeros(2),'IK12 exact attained covariance')
diff=Q-R.H*Gam.inv()*R
ck(all(S.simplify(x)>=0 for x in [diff[i,i] for i in range(3)]) and diff.rank()==1 and S.simplify(diff.trace())>0,'IK12 positive quotient loss')
out={'status':'passed','exact_checks':len(checks),'fixtures':'Five rational upper/lower root-grid shift fixtures; coefficients explicitly auxiliary, not asserted to equal the original period. One exact complex-metric quotient fixture.','checks':checks,'scope':'IK5–6, IK10 and IK12 finite identities; six-dimensional and larger examples do not evaluate native moments.'}
(P/'INVERSE_POWER_CONDUCTOR_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks)}))
