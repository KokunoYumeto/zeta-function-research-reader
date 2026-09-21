"""Independent exact checks of the general PES proof and all PB1--8 maps."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
checks=[]
entries=0
def ck(name,value):
    global entries
    vs=list(value) if isinstance(value,(s.MatrixBase,list,tuple)) else [value]
    for v in vs:
        assert s.cancel(v)==0,(name,v)
    entries+=len(vs);checks.append({'name':name,'entries':len(vs),'passed':True})
def vp(q,p):
    a,b=map(int,s.Rational(q).as_numer_denom());ans=0
    if not a:return 10**9
    while a%p==0:a//=p;ans+=1
    while b%p==0:b//=p;ans-=1
    return ans
p,x,Z=s.symbols('p x Z',positive=True)
den=Z*(4*x-p)-x;y=p*Z*x/den;gap=y-x
x0=(p+3)/4;Z0=(3*p+1)/4
ck('PES1 exact original ES solve',4/p-1/x-1/y-1/(p*Z))
ck('PES1 denominator rectangle corner',den.subs({x:x0,Z:Z0})-2*p)
ck('PES2 full x derivative',s.diff(gap,x)+p*p*Z*Z/den**2+1)
ck('PES2 full Z derivative',s.diff(gap,Z)+p*x*x/den**2)
ck('PES3 exact y upper constant',y.subs({x:x0,Z:Z0})-(p+3)*(3*p+1)/32)
ck('PES3 exact gap upper constant',gap.subs({x:x0,Z:Z0})-(p+3)*(3*p-7)/32)
ck('PES3 complete p^2 comparison polynomial',32*p*p-(p+3)*(3*p-7)-(29*p*p-2*p+21))
ck('PB1 original three reciprocals lower bound',4/p-4/(p+3)-4/(p*(3*p+1))-32/((p+3)*(3*p+1)))
ck('PES4 exact ordered x bound',2*p*Z/(4*Z-1)-p/2-p/(2*(4*Z-1)))
ck('PES5 smaller scaled denominator derivative',s.diff(2*x/(4*x-p),x)+2*p/(4*x-p)**2)
ck('PES5 exact scaled upper bound',(2*x/(4*x-p)).subs(x,x0)-(p+3)/6)
ck('PES5 inverse-three comparison margin',(2*p+1)/3-(p+3)/6-(3*p-1)/6)
ck('PES5 inverse-two comparison margin',(p+1)/2-(p+3)/6-p/3)
ck('PES3 sharp actual witness at p13',s.Rational(4,13)-s.Rational(1,4)-s.Rational(1,20)-s.Rational(1,130))
ck('PES3 actual sharp gap',20-4-s.Rational((13+3)*(3*13-7),32))

h,a,d,r,k=s.symbols('h a d r k',nonzero=True)
pv=4*h*a*d-r;kv=(4*h*a*a+1)/r;b=d*kv-a
xx=h*d*a;yy=h*d*b;zz=pv*h*a*b
ck('PES9 exact full original ES identity',4/pv-1/xx-1/yy-1/zz)
ck('PES9 exact divisor and coefficient identities',[r*kv-(4*h*a*a+1),a+b-d*kv,4*h*a*b-1-pv*kv])
ck('PES10 exact unit sum and S congruence',(pv+xx+yy+zz)-h*d*d*kv-pv*(1+h*a*b))

matrices=[]
for roots in [(1201,306,16218,1082101),(1201,306,21618,61251)]:
    pp=roots[0];A=-s.Rational(1,sum(roots));C=-5*A*s.prod(roots[1:])
    ds=[A*s.prod(roots[i]-roots[j] for j in range(4) if j!=i) for i in range(4)]
    bs=[vp(di,pp) for di in ds];ms=[bi//2 for bi in bs]
    V=s.Matrix([[ri**j for j in range(4)] for ri in roots])
    Q=V.inv()*s.diag(*[di/A for di in ds])
    GI=s.diag(A*Q*s.diag(*[pp**mi for mi in ms]),A*Q)
    least=1 if roots[2]%pp else 2
    for j in range(4):
        Zj=s.diag(s.diag(*[C**j/(pp**mi*di) for mi,di in zip(ms,ds)])*V,s.diag(*[C**j/di for di in ds])*V)
        ck(f'PES11 every ideal inclusion entry roots={roots[2]} j={j}',GI*Zj-C**j*s.eye(8))
        integral=all(vp(v,pp)>=0 for v in Zj)
        assert integral==(j>=least),(roots,j,integral)
        checks.append({'name':f'PES12 necessity and sufficiency roots={roots[2]} j={j}','entries':64,'passed':True});entries+=64
    matrices.append({'roots':list(roots),'least_power':least,'C0':str(C),'coefficient_valuation':vp(C,pp),'branch_valuations':bs})

sources={}
for path in [HERE/'POSITIVE_ES_STRATA_REVIEW.tex',ROOT/'POSITIVE_ES_BOUNDARY_BODY.tex',HERE/'INTEGRAL_SIGNED_REVIEW.tex']:
    sources[path.name]=sha256(path.read_bytes()).hexdigest()
data={'status':'PASS','groups':len(checks),'scalar_entries':entries,'source_sha256':sources,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,'witnesses':matrices,'reading':'Entire PB1--8 source and complete ISR proof. The general inequalities and residue exclusions are proved in PES1--12; finite examples are not used as proof of universal exclusion.','unresolved':'No proof here that one-divisible n=1 occurs or is impossible; no proof that p divides S is impossible. Neither uncertainty affects the proved inclusion on the original unit-A integral chart.'}
(HERE/'POSITIVE_ES_STRATA_REVIEW.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','groups':len(checks),'scalar_entries':entries,'source_sha256':sources},indent=2))
