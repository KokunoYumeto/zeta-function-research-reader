from pathlib import Path
import sympy as s
import itertools,json,hashlib,sys
P=Path(__file__).parent
sys.path.insert(0,str(P.parent/'invariant_collision_20260921'))
from exact_reference import moments
checks=[]
def simp(A):return A.applyfunc(s.simplify) if isinstance(A,s.MatrixBase) else s.simplify(A)
def zero(A):return all(s.simplify(z)==0 for z in A) if isinstance(A,s.MatrixBase) else s.simplify(A)==0
def ok(label,v):
 assert bool(v),label
 checks.append(label)
def star(A):return A.conjugate().T
def covariance(E,W):return simp(W*(s.eye(E.cols)-star(E)*(E*star(E)).inv()*E)*star(W))
E=s.Matrix([[1,0,0]]);W=s.Matrix([[0,1,0],[0,0,1]]);C=covariance(E,W);etas=[]
for j,(e,w) in enumerate([(s.Matrix([1]),s.Matrix([1,s.I])),(s.Matrix([s.I]),s.Matrix([2,1]))]):
 A=E*star(E);kappa=1+(star(e)*A.inv()*e)[0];v=simp(w-W*star(E)*A.inv()*e)
 En=E.row_join(e);Wn=W.row_join(w);Cn=covariance(En,Wn)
 ok(f'original full-root covariance update {j}',zero(Cn-C-v*star(v)/kappa))
 etas.append(simp(v/s.sqrt(kappa)));E,W,C=En,Wn,Cn
ok('exact complex updated covariance',C==s.Matrix([[s.Rational(13,3),2-s.I],[2+s.I,3]]))
ok('projected determinant eight',C.det()==8)
ok('unprojected determinant thirteen',(W*star(W)).det()==13)
A=s.eye(2).row_join(s.Matrix.hstack(*etas));minorvalues=[simp(abs(A[:,J].det())**2) for J in itertools.combinations(range(4),2)]
ok('all six squared minors',sorted(minorvalues)==sorted([1,s.Rational(1,2),s.Rational(1,2),s.Rational(3,2),s.Rational(17,6),s.Rational(5,3)]))
ok('full Cauchy Binet sum',sum(minorvalues)==8)

# Complete weighted CI26 source; rational factors of the same mass M_sigma.
x,y,w=s.symbols('x y w');qp=2;maxM=9;maxD=qp+maxM;chip=x*(x-1)
mu=moments(maxD)
def moment(n):return s.Rational(int(mu[n//2]),2**(n//2)) if n%2==0 else 0
def ip(f,g):
 f=s.Poly(f,x);g=s.Poly(g,x)
 return s.cancel(sum(s.conjugate(f.nth(i))*g.nth(j)*s.conjugate(s.I)**i*s.I**j*moment(i+j) for i in range(f.degree()+1) for j in range(g.degree()+1)))
H=s.Matrix(maxM+1,maxM+1,lambda i,j:ip(chip*x**i,chip*x**j))
series=[s.series(num/(s.exp(4*s.I*w)-1),w,0,maxD+1).removeO().expand() for num in [s.exp(w)-1,s.exp(3*w)-s.exp(2*w)]]
def func(f,z):
 f=s.Poly(s.expand(f),x)
 return s.simplify(sum(f.nth(i)*s.factorial(i)*series[z].coeff(w,i) for i in range(f.degree()+1)))
pn=[s.Integer(1),y]
for n in range(1,maxD):pn.append(s.expand(y*pn[n]-n*(n-s.Rational(1,2))*pn[n-1]))
hn=[s.factorial(n)*s.rf(s.Rational(1,2),n) for n in range(maxD+1)]
Eall=s.Matrix(2,maxD+1,lambda i,n:pn[n].subs(y,[0,-s.I][i])/s.sqrt(hn[n]))
Wall=s.Matrix(2,maxD+1,lambda z,n:func(pn[n].subs(y,-s.I*x),z)/s.sqrt(hn[n]))
for M in range(3,maxM+1):
 D=qp+M-1;EE=Eall[:,:D+1];ee=Eall[:,D+1];WW=Wall[:,:D+1];ww=Wall[:,D+1]
 kk=simp(1+(star(ee)*(EE*star(EE)).inv()*ee)[0])
 vv=simp(ww-WW*star(EE)*(EE*star(EE)).inv()*ee)
 proj=H[:M,:M].inv()*H[:M,M];eta=x**M-sum(proj[j]*x**j for j in range(M));nu=simp(H[M,M]-(star(H[:M,M])*H[:M,:M].inv()*H[:M,M])[0])
 ff=s.Matrix([func(chip*eta,z) for z in range(2)])
 ok(f'exact original source pivot phase degree {D+1}',zero(nu-hn[D+1]*kk))
 ok(f'full two-row innovation phase degree {D+1}',zero(vv-s.I**(-(D+1))*ff/s.sqrt(hn[D+1])))
 ok(f'source and root innovation outer products degree {D+1}',zero(vv*star(vv)/kk-ff*star(ff)/nu))

# Nontrivial complex column exchanges and their entire residual covariance.
X=s.Matrix([[7+2*s.I,1,0,4-s.I,1],[1,8-s.I,1,2,3+s.I],[2,1,9+s.I,1,2]])
A=s.eye(3).row_join(X);chosen=[0,1,2];swaps=[];total=simp((A*star(A)).det())
while True:
 others=[j for j in range(A.cols) if j not in chosen];V=A[:,chosen];T=simp(V.inv()*A[:,others]);viol=[(i,j) for i in range(T.rows) for j in range(T.cols) if s.simplify(abs(T[i,j])**2)>4]
 if not viol:break
 i,j=viol[0];old=simp(abs(V.det())**2);factor=simp(abs(T[i,j])**2);chosen[i]=others[j];new=simp(abs(A[:,chosen].det())**2)
 ok(f'exact pivot gain {len(swaps)}',s.simplify(new-old*factor)==0 and new>4*old)
 swaps.append(dict(volume_before=str(old),factor=str(factor),volume_after=str(new)))
V=A[:,chosen];others=[j for j in range(A.cols) if j not in chosen];T=simp(V.inv()*A[:,others]);res=simp((s.eye(3)+T*star(T)).det())
ok('termination coefficient bound',all(s.simplify(abs(z)**2)<=4 for z in T))
ok('exact selected determinant factorization',s.simplify(abs(V.det())**2*res-total)==0)
ok('complete determinant residual bound',res>=1 and res<=(1+4*X.cols)**3)
ok('exact residual inverse retaining phases',zero((A*star(A)).inv()-star(V).inv()*(s.eye(3)+T*star(T)).inv()*V.inv()))
out=dict(status='passed',checks=len(checks),labels=checks,synthetic_minors=list(map(str,minorvalues)),pivot_swaps=swaps,selected_columns=chosen,full_determinant=str(total),residual_determinant=str(res),scope='Original-root/weighted-source identities on CI26 and declared complex finite fixtures; no numerical native period or RH coefficient supplied.',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'ROOT_INNOVATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ['labels','pivot_swaps']}))
