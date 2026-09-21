from pathlib import Path
import sympy as s,json,hashlib
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
B0=Path(__file__).resolve().parent
p=1201
def vp(q):
 q=s.Rational(q); n,d=int(q.p),int(q.q);v=0
 if n==0:return None
 while n%p==0:n//=p;v+=1
 while d%p==0:d//=p;v-=1
 return v
def mod(q):
 q=s.Rational(q);return int(q.p)%p*pow(int(q.q)%p,-1,p)%p
r=s.symbols('r')
out=[]
for roots in [[p,306,16218,1082101],[p,306,21618,61251]]:
 S=sum(roots);A=-s.Rational(1,S)
 f=s.prod(r-ri for ri in roots);h=s.expand(A*f);coef=[s.expand(h).coeff(r,i) for i in [4,2,1,0]]
 V=s.Matrix([[ri**j for j in range(4)] for ri in roots])
 ds=[s.diff(h,r).subs(r,ri) for ri in roots]
 bv=[vp(di) for di in ds];mv=[n//2 for n in bv];eps=[n-2*m for n,m in zip(bv,mv)]
 Cmat=s.diag(V,s.diag(*[p**m for m in mv])*V)
 sn=smith_normal_form(Cmat,domain=ZZ)
 exps=sorted(vp(sn[j,j]) for j in range(8))
 Q=s.Matrix.hstack(*[s.Matrix([s.Poly(s.div(f,r-ri,r)[0],r).nth(j) for j in range(4)]) for ri in roots])
 assert V*Q==s.diag(*[di/A for di in ds])
 cond=s.diag(A*Q*s.diag(*[p**m for m in mv]),A*Q)
 condint=cond/A
 sc=smith_normal_form(condint,domain=ZZ)
 cexps=sorted(vp(sc[j,j]) for j in range(8))
 assert cexps==exps
 C0=coef[2];D0=coef[3]
 PiD=s.Matrix([[1,D0,D0**2]]);PiP=s.Matrix([[1,p,p**2]])
 assert PiP*s.diag(1,-C0/5,C0*C0/25)==PiD
 item={'roots':roots,'S':S,'coefficients':[str(x) for x in coef],'coefficient_residues':[mod(x) for x in coef],'D_i':[str(x) for x in ds],'derivative_valuations':bv,'m':mv,'epsilon':eps,'smith_exponents':exps,'conductor_quotient_exponents':cexps,'conductor_branch_exponents':[3*m+e for m,e in zip(mv,eps)],'prime_root_unit_residues':[mod(d/(p**b)) for d,b in zip(ds,bv)],'vC':vp(C0),'vD':vp(D0),'coefficient_extension_smith_exponents':[0,vp(C0),2*vp(C0)],'all8_conductor_generator_matrix':[[str(cond[i,j]) for j in range(8)] for i in range(8)]}
 out.append(item)
(B0/'DEFINING_PRIME_1201_EXACT_DATA.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([{k:v for k,v in x.items() if k not in ['all8_conductor_generator_matrix','D_i']} for x in out],indent=2))

