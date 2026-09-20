from pathlib import Path
from itertools import combinations
import sympy as s,json,hashlib
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
B0=Path(__file__).resolve().parent
checks=[]
def zero(name,obj):
 vs=list(obj) if isinstance(obj,(s.MatrixBase,list,tuple)) else[obj]
 for i,v in enumerate(vs):
  if s.cancel(s.expand(v))!=0:raise AssertionError((name,i,v))
 checks.append({'name':name,'entries':len(vs),'passed':True})
def yes(name,truth,n=1):
 assert truth,name;checks.append({'name':name,'entries':n,'passed':True})
p=1201
yes('1201 primality by every possible prime divisor',all(p%q for q in s.primerange(2,35)),len(list(s.primerange(2,35))))
r=s.symbols('r')
ri=s.symbols('r0:4')
A=s.symbols('A',nonzero=True)
f=s.prod(r-a for a in ri)
V=s.Matrix([[a**j for j in range(4)] for a in ri])
Q=s.Matrix.hstack(*[s.Matrix([s.Poly(s.prod(r-a for j,a in enumerate(ri) if j!=i),r).nth(k) for k in range(4)]) for i in range(4)])
di=[A*s.prod(ri[i]-ri[j] for j in range(4) if j!=i) for i in range(4)]
zero('all labelled conductor evaluation entries',V*Q-s.diag(*[d/A for d in di]))
zero('quartic determinant sign',s.prod(di)-A**4*V.det()**2)
zero('complete cofactor determinant',Q.det()-V.det())
pm=s.symbols('pm0:4',nonzero=True)
Cp=s.diag(V,s.diag(*pm)*V)
JI=s.diag(A*Q*s.diag(*pm),A*Q)
alpha=s.diag(*[pm[i]*di[i] for i in range(4)])
zero('all8 original conductor columns evaluated',Cp*JI-s.diag(alpha,alpha))
# The residue inverse identity at arbitrary coefficients is already RD3;
# reconstruct it from all eight root evaluations with the retained units.
cross=s.diag(*[1/(pm[i]*di[i]) for i in range(4)])
BO=s.BlockMatrix([[s.zeros(4),cross],[cross,s.zeros(4)]]).as_explicit()
BE=Cp.T*BO*Cp
SW=s.BlockMatrix([[s.zeros(4),s.eye(4)],[s.eye(4),s.zeros(4)]]).as_explicit()
zero('complete exact dual-lattice identity',BE*JI-Cp.T*SW)
c0,P,d0=s.symbols('c0 P d0')
K=s.diag(1,-c0/5,c0*c0/25)
piP=s.Matrix([[1,P,P*P]])
piD=s.Matrix([[1,-P*c0/5,P*P*c0*c0/25]])
zero('entire scalar specialization square',piP*K-piD)
I=s.eye(8)
PP=s.kronecker_product(piP,I);PD=s.kronecker_product(piD,I)
zero('all24-to8 specialization entries',PP*s.kronecker_product(K,I)-PD)
kerD=s.BlockMatrix([[-d0*I,-d0*d0*I],[I,s.zeros(8)],[s.zeros(8),I]]).as_explicit()
zero('all16 specialization kernel columns',s.kronecker_product(s.Matrix([[1,d0,d0*d0]]),I)*kerD)
yes('complete kernel rank',kerD.rank()==16,1)
def vp(q):
 q=s.Rational(q);a,b=int(q.p),int(q.q);v=0
 if not a:return None
 while a%p==0:a//=p;v+=1
 while b%p==0:b//=p;v-=1
 return v
def mod(q):
 q=s.Rational(q);return int(q.p)%p*pow(int(q.q)%p,-1,p)%p
expected=[([1,0,0,1],[75,93,581,1126],[0,0,0,0,0,0,1,1]),([2,0,2,2],[850,42,640,449],[0,0,0,1,1,2,2,3])]
for hnum,roots in enumerate([[p,306,16218,1082101],[p,306,21618,61251]]):
 AA=-s.Rational(1,sum(roots));ff=s.prod(r-a for a in roots);hh=s.Poly(AA*ff,r)
 zero('witness'+str(hnum+1)+' exact ES relation',4/s.Rational(p)-sum(1/s.Rational(a) for a in roots[1:]))
 cv=[hh.nth(j) for j in [4,2,1,0]]
 res=[mod(q) for q in cv]
 yes('witness coefficient reductions'+str(hnum),res==[[410,100,0,0],[522,0,0,0]][hnum],4)
 dd=[s.diff(hh.as_expr(),r).subs(r,a) for a in roots]
 bb=[vp(d) for d in dd];mm=[b//2 for b in bb]
 yes('all derivative valuations'+str(hnum),bb==expected[hnum][0],4)
 yes('all derivative unit residues'+str(hnum),[mod(d/p**b) for d,b in zip(dd,bb)]==expected[hnum][1],4)
 vmat=s.Matrix([[a**j for j in range(4)] for a in roots])
 cm=s.diag(vmat,s.diag(*[p**m for m in mm])*vmat)
 sn=smith_normal_form(cm,domain=ZZ)
 yes('all8 integral inclusion Smith exponents'+str(hnum),sorted(vp(sn[j,j]) for j in range(8))==expected[hnum][2],8)
 qm=Q.subs(dict(zip(ri,roots)))
 jc=s.diag(qm*s.diag(*[p**m for m in mm]),qm)
 snc=smith_normal_form(jc,domain=ZZ)
 yes('all8 conductor quotient Smith exponents'+str(hnum),sorted(vp(snc[j,j]) for j in range(8))==expected[hnum][2],8)
 zero('specialized coefficient map'+str(hnum),s.Matrix([[1,p,p*p]])*s.diag(1,-cv[2]/5,cv[2]**2/25)-s.Matrix([[1,cv[3],cv[3]**2]]))
 derivative=s.Poly(s.diff(hh.as_expr(),r),r)
 reduced=sum(mod(derivative.nth(k))*r**k for k in range(4))
 zero('all original reduced primary relations'+str(hnum),s.rem(reduced,r**(hnum+2),r)-[200*r,3*r*r][hnum])
# Domain identity is exact for a full arbitrary Hermitian original Gram.
a,b,c,d=s.symbols('a b c d',real=True)
G=s.Matrix([[a,b+s.I*c],[b-s.I*c,d]])
D,Db=s.symbols('D Db')
den=1+D*Db+(D*Db)**2
Prow=s.Matrix([[1,D,D*D]])
Sec=s.Matrix([[1],[Db],[Db*Db]])/den
zero('minimum section constraint',Prow*Sec-s.ones(1))
Kern=s.Matrix([[-D,-D*D],[1,0],[0,1]])
zero('full kernel orthogonality',Prow*Kern)
# conjugate section row is Prow/den in formal D,Db variables
zero('exact minimum quadratic form',s.kronecker_product(Prow/den,G)*s.kronecker_product(Sec,s.eye(2))-G/den)
zero('complete covariance before metric choice',Prow*s.Matrix([[1],[Db],[Db*Db]])-s.Matrix([[den]]))
src=B0/'PRIME_SPECIALIZATION_BODY.tex'
out={'status':'PASS','check_groups':len(checks),'scalar_entries':sum(q['entries'] for q in checks),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'checks':checks,'scope':'Exact ring/evaluation/specialization identities, both complete1201examples and dense complex Gram minimum. General integral closure, ideal equality, all-case Smith classification and valuation criteria are proved in the sources.'}
(B0/'PRIME_SPECIALIZATION_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','check_groups','scalar_entries','source_sha256']}))
