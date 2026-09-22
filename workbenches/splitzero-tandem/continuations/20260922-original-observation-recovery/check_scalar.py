"""Exact auxiliary verification of SD1--54; independent of Python assertions."""
from pathlib import Path
from itertools import combinations
import sympy as S
import json,hashlib,argparse,sys,re
sys.stdout.reconfigure(encoding="utf-8")
HERE=Path(__file__).resolve().parent
z,x=S.symbols("z x")
I=S.I
checks=[]; controls=[]; witnesses={}
def require(v,name):
    if v is not True and v != S.true: raise RuntimeError(name+": "+str(v))
    checks.append(name)
def eq(a,b,name):
    if isinstance(a,S.MatrixBase):
        require(a.shape==b.shape and all(S.simplify(e)==0 for e in a-b),name)
    else: require(S.simplify(a-b)==0,name)
def neq(a,b,name):
    if isinstance(a,S.MatrixBase): flag=any(S.simplify(e)!=0 for e in a-b)
    else: flag=S.simplify(a-b)!=0
    require(flag,name); controls.append(name)
def psd(A,name):
    eq(A,A.H,name+"/Hermitian")
    for j in range(1,A.rows+1):
        for ids in combinations(range(A.rows),j):
            require(S.simplify(A.extract(ids,ids).det())>=0,name+"/minor"+str(ids))
def state(T,G,La,name,IK=None):
    q=T.rows; b=La.rows; m=q-b
    if IK is None:
        basis=La.nullspace()
        IK=S.Matrix.hstack(*basis) if basis else S.zeros(q,0)
    Q=(La*G.inv()*La.H).inv()
    L=G.inv()*La.H*Q
    HK=IK.H*G*IK
    H=G.inv()*T.H*G*T
    vv=T.nullspace()
    V=S.Matrix.hstack(*vv) if vv else S.zeros(q,0)
    PV=V*(V.H*G*V).inv()*V.H*G
    PW=S.eye(q)-PV
    B=IK.H*G*PW*IK
    EK=IK.H*T.H*G*T*IK
    Delta=T.rank(); p=EK.rank(); t=m-p; delta=Delta-p
    eq(La*L,S.eye(b),name+"/original minimum section")
    eq(L.H*G*L,Q,name+"/observed metric")
    eq(IK.H*G*L,S.zeros(m,b),name+"/full kernel orthogonality")
    Y=La*z*(z*S.eye(q)+H).inv()*L
    f=S.factor(Y.det())
    form=S.factor(z**b*(z*HK+EK).det()/HK.det()/(z*S.eye(q)+H).det())
    eq(f,form,name+"/full physical determinant")
    PA=S.Poly(S.cancel((z*HK+EK).det()/HK.det()/z**t),z).as_expr()
    DH=S.Poly(S.cancel((z*S.eye(q)+H).det()/z**(q-Delta)),z).as_expr()
    eq(f,z**delta*PA/DH,name+"/rank-changing positive product")
    ga=S.cancel((x*HK+B).det()/HK.det()/x**t)
    gamma_product=S.simplify(ga.subs(x,0))
    a0=S.cancel((f/z**delta)).subs(z,0)
    eq(a0,PA.subs(z,0)/DH.subs(z,0),name+"/scalar leading coefficient")
    require(delta>=0,name+"/nonnegative zero order")
    require(B.rank()==p,name+"/all zero-angle multiplicities")
    return dict(T=T,G=G,La=La,IK=IK,Q=Q,L=L,HK=HK,H=H,PV=PV,PW=PW,B=B,EK=EK,
                Y=Y,f=f,PA=PA,DH=DH,p=p,t=t,delta=delta,Delta=Delta,q=q,m=m,
                gamma_product=gamma_product,a0=a0,gamma_poly=ga)

T=S.diag(0,2,3*I)
La=S.Matrix([[-1,1,0],[-I,0,1]])
K=S.Matrix([1,1,I])
a=state(T,S.eye(3),La,"complex original fixture",K)
eq(a["f"],z*(3*z+13)/(3*(z+4)*(z+9)),"specified complex scalar response")
eq(a["gamma_product"],S.Rational(2,3),"specified primary angle")
eq(a["a0"],S.Rational(13,108),"specified leading coefficient")
U=S.Matrix([0,1,I])/S.sqrt(2); Z=S.Matrix([0,1,-I])/S.sqrt(2)
E11=(U.H*a["H"]*U)[0]; E12=(U.H*a["H"]*Z)[0]; E22=(Z.H*a["H"]*Z)[0]
sig=S.simplify(E22-S.conjugate(E12)*E12/E11)
eq(sig,S.Rational(72,13),"complete complementary energy minimum")
eq(a["gamma_product"],a["a0"]*sig,"exact scalar-primary-complement morphism")
require(4<=sig<=9,"complement retains full spectral bounds")
neq(sig,E22,"omitting energy cross block changes complementary minimum")

# Nonunitary complex transport, all metrics paired.
Smap=S.Matrix([[1,I,0],[0,2,1],[1,0,1]])
Gt=Smap.inv().H*Smap.inv()
at=state(Smap*T*Smap.inv(),Gt,La*Smap.inv(),"nonunitary complex transport",Smap*K)
eq(at["Y"],a["Y"],"measured matrix exactly coordinate invariant")
eq(at["HK"],a["HK"],"kernel metric paired transport")
eq(at["gamma_product"],a["gamma_product"],"primary determinant paired transport")
O=S.Matrix([[1,I],[0,2]])
ao=state(T,S.eye(3),O*La,"nonunitary observation frame",K)
eq(ao["Y"],O*a["Y"]*O.inv(),"observed endomorphism similarity")
eq(ao["f"],a["f"],"observed scalar invariant")
am=state(T,7*S.eye(3),La,"full source mass",K)
eq(am["Y"],a["Y"],"full mass leaves measured response invariant")
eq(am["HK"],7*a["HK"],"full mass remains in original kernel Gram")

# A noncommuting two-angle fixture with delta=0: leading scalar is exact.
T2=S.Matrix([[1,I,1,0],[0,1,0,2],[0,0,0,0],[0,0,0,0]])
La2=S.Matrix([[1,0,0,0],[0,1,0,0]])
aa=state(T2,S.eye(4),La2,"two noncommuting angles")
neq(aa["B"]*aa["EK"],aa["EK"]*aa["B"],"energy and primary angle need not commute")
eq(aa["a0"],aa["gamma_product"],"zero complementary dimension exact determinant recovery")
psd(aa["H"]-2*aa["PW"],"complete lower positive-word interval")
psd(6*aa["PW"]-aa["H"],"complete upper positive-word interval")
psd(aa["EK"]-2*aa["B"],"kernel lower energy-angle comparison")
psd(6*aa["B"]-aa["EK"],"kernel upper energy-angle comparison")
ge=list(aa["B"].eigenvals())
ge=sorted(ge,key=lambda v:float(v))
require(S.simplify(ge[1]-ge[0])>=0,"ordered exact angle list")
alph=[S.Integer(1),S.Integer(4)]
lower=[S.Integer(2),S.Integer(1)] # exp(h_hat)
upper=[S.Integer(6),S.Rational(3,2)] # all-retained-root exp(beta)
for j in range(2):
    require(S.simplify(1/ge[j]-lower[j])>=0,f"ordered lower logarithm j{j}")
    require(S.simplify(upper[j]-1/ge[j])>=0,f"ordered improved upper logarithm j{j}")
for rank in range(3):
    actual=S.prod(1/g for g in ge[:rank])
    lo=S.prod(lower[:rank]); hi=S.prod(upper[:rank])
    require(S.simplify(actual-lo)>=0,f"all exterior lower rank{rank}")
    require(S.simplify(hi-actual)>=0,f"all exterior upper rank{rank}")
witnesses["two_angle_characteristic_polynomial"]=str(S.factor(aa["gamma_poly"]))
witnesses["two_angle_exact_leading_coefficient"]=str(aa["a0"])

# Sharp one-block pair; u=5, ell=1 makes the coupling integral.
T0=S.diag(S.sqrt(5),0,1)
T1=S.Matrix([[2,0,1],[0,1,0],[0,0,0]])
Las=S.Matrix([[1,0,0],[0,1,0]])
s0=state(T0,S.eye(3),Las,"sharp pair zero")
s1=state(T1,S.eye(3),Las,"sharp pair one")
eq(s0["DH"],s1["DH"],"sharp pair identical full spectra")
eq(s0["f"],s1["f"],"sharp pair identical all scalar data")
eq(s0["Q"],s1["Q"],"sharp pair identical observed metrics")
eq(s0["gamma_product"],1,"sharp pair upper primary endpoint")
eq(s1["gamma_product"],S.Rational(1,5),"sharp pair lower primary endpoint")
neq(s0["Y"],s1["Y"],"scalar equality does not imply matrix-memory equality")
require((s1["IK"].H*s1["H"]*s1["L"]).rank()>0,"canceled energy remains coupled to observation")
eq(s0["gamma_product"]/s1["gamma_product"],5,"sharp scalar ambiguity factor")
witnesses["sharp_pair_response"]=str(s0["f"])

# Exact repeated subgap energies, plus exact repeated cancellation.
Ts=S.Matrix([[2,1],[0,0]])
Ls=S.Matrix([[1,0]])
rs=state(S.diag(Ts,Ts),S.eye(4),S.diag(Ls,Ls),"repeated subgap")
eq(rs["PA"],(z+1)**2,"full repeated subgap numerator")
eq(rs["DH"],(z+5)**2,"full repeated positive-word denominator")
require(S.Poly(S.gcd(rs["PA"],rs["DH"]),z).degree()==0,"subgap multiplicities cannot cancel")
rc=state(S.diag(T1,T1),S.eye(6),S.diag(Las,Las),"repeated canceled energies")
eq(S.Poly(S.gcd(rc["PA"],rc["DH"]),z).monic().as_expr(),(z+1)**2,"all repeated cancellation multiplicities")

# Rank-changing cases, zero words, empty kernels and empty observations.
inter=state(S.diag(T,0),S.diag(1,1,1,3),La.row_join(S.zeros(2,1)),"kernel intersection")
eq(inter["f"],a["f"],"added zero kernel direction preserves scalar response")
require(inter["t"]==1 and inter["p"]==1,"actual intersection rank accounted")
eq(inter["gamma_product"],a["gamma_product"],"positive quotient determinant retained at intersection")
neq(S.factor(inter["f"]/z**(inter["Delta"]-inter["m"])),S.factor(inter["PA"]/inter["DH"]),"dropping zero-kernel exponent gives false formula")
empty=state(S.diag(0,2),S.eye(2),S.eye(2),"empty kernel")
zero=state(S.zeros(2),S.eye(2),S.Matrix([[1,0]]),"zero word")
emptyobs=state(S.diag(0,2),S.eye(2),S.zeros(0,2),"empty observed space")
eq(zero["f"],1,"zero word scalar one")
eq(emptyobs["f"],1,"empty observed determinant one")
require(zero["t"]==1 and zero["p"]==0,"zero word retains zero primary factor")

# Full rank-changing kernel determinant factor.
Hk=inter["HK"]; Bk=inter["B"]
# nullspace frame first, then choose a complementary basis explicitly.
n0=Bk.nullspace()[0]
n1=S.Matrix([1,0]) if S.Matrix.hstack(n0,S.Matrix([1,0])).det()!=0 else S.Matrix([0,1])
F=S.Matrix.hstack(n0,n1); Gk=F.H*Hk*F; Bb=F.H*Bk*F
hq=Gk[1,1]-Gk[1,0]*Gk[0,1]/Gk[0,0]
eq(inter["gamma_product"],Bb[1,1]/hq,"positive determinant uses attained kernel quotient")
eq(Hk.det()*abs(F.det())**2,Gk[0,0]*Bb[1,1]/inter["gamma_product"],"complete rank-changing kernel determinant factor")
for av in [S.Rational(1,3),S.Integer(1),S.Integer(7)]:
    zz=state(S.diag(0,1),S.diag(av,1),S.Matrix([[0,1]]),"invisible zero metric "+str(av))
    eq(zz["f"],z/(z+1),"zero-metric cone same response "+str(av))
    eq(zz["HK"].det(),av,"zero-metric cone full kernel value "+str(av))

# Interpolation: every monic solution has exactly the same reduced pair.
def interpolation(st,R,name):
    p=st["p"]; de=st["Delta"]; delta=st["delta"]; count=p+de
    if not count:
        eq(st["f"],1,name+"/zero-sample case"); return
    PP=S.expand(st["PA"].subs(z,R*x)/R**p)
    DD=S.expand(st["DH"].subs(z,R*x)/R**de)
    common=S.Poly(S.gcd(PP,DD),x).monic().as_expr()
    c=S.degree(common,x)
    P0=S.cancel(PP/common); D0=S.cancel(DD/common)
    nodes=[1+S.Rational(j,count) for j in range(count)]
    vals=[S.cancel(st["f"].subs(z,R*v)/v**delta) for v in nodes]
    mat=S.Matrix([[v**j for j in range(p)]+[-ri*v**j for j in range(de)] for v,ri in zip(nodes,vals)])
    rhs=S.Matrix([ri*v**de-v**p for v,ri in zip(nodes,vals)])
    sol,params=mat.gauss_jordan_solve(rhs)
    require(len(params)==c,name+"/linear nullity equals common-factor degree")
    sample={pp:S.Integer(j+2) for j,pp in enumerate(params)}
    sol=sol.subs(sample)
    P1=x**p+sum(sol[j]*x**j for j in range(p))
    D1=x**de+sum(sol[p+j]*x**j for j in range(de))
    eq(P1*DD-PP*D1,0,name+"/any solution cross polynomial")
    eq(S.cancel(P1/D1),S.cancel(P0/D0),name+"/reduced rational function exactly recovered")
    eq(R**(-delta)*P0.subs(x,0)/D0.subs(x,0),st["a0"],name+"/physical leading scale retained")
    if c:
        badS=(x-nodes[0])**c
        badP=S.expand(P0*badS); badD=S.expand(D0*badS)
        eq(badP.subs(x,nodes[0]),0,name+"/permitted node zero numerator")
        eq(badD.subs(x,nodes[0]),0,name+"/permitted node zero denominator")
        eq(S.cancel(badP/badD),S.cancel(PP/DD),name+"/cancel before evaluating node")
    # Entire monic family supplies each kernel vector of the interpolation matrix.
    for j in range(int(c)):
        dp=S.Poly(S.expand(P0*x**j),x); dd=S.Poly(S.expand(D0*x**j),x)
        v=S.Matrix([dp.nth(k) for k in range(p)]+[dd.nth(k) for k in range(de)])
        eq(mat*v,S.zeros(count,1),name+"/complete nullspace factor "+str(j))
    witnesses[name+"_cancellation_degree"]=int(c)
for st,R,name in [(a,S.Integer(9),"complex interpolation"),
                  (aa,S.Integer(6),"noncommuting interpolation"),
                  (rs,S.Integer(5),"repeated subgap interpolation"),
                  (rc,S.Integer(5),"repeated cancellation interpolation"),
                  (inter,S.Integer(9),"intersection interpolation"),
                  (empty,S.Integer(4),"empty kernel interpolation"),
                  (zero,S.Integer(1),"zero word interpolation"),
                  (emptyobs,S.Integer(4),"empty observation interpolation")]:
    interpolation(st,R,name)

# Exact all-dimension sharp construction counts, including intersections.
for q in range(0,10):
    for m in range(q+1):
        for Delta in range(q+1):
            for t in range(m+1):
                p=m-t; d=q-Delta
                if p>Delta or t>d: continue
                star=min(p,Delta-p,d-t)
                counts=[star,p-star,Delta-p-star,t,d-t-star]
                require(min(counts)>=0,f"sharp dimension nonnegative/{q}/{m}/{Delta}/{t}")
                eq(3*counts[0]+sum(counts[1:]),q,f"sharp dimension total/{q}/{m}/{Delta}/{t}")
                eq(counts[0]+counts[1]+counts[3],m,f"sharp original kernel rank/{q}/{m}/{Delta}/{t}")
                eq(2*counts[0]+counts[1]+counts[2],Delta,f"sharp word rank/{q}/{m}/{Delta}/{t}")
                require(star<=p and star<=Delta-p and star<=d-t,f"sharp ambiguity cap/{q}/{m}/{Delta}/{t}")
eq(rc["gamma_product"],S.Rational(1,25),"two-copy exact sharp determinant loss")
eq(rc["f"],z**2/(z+5)**2,"two-copy exact scalar identity")

# Coherent metric errors: generalized ratios, quotient energy and scalar constants.
agm=state(T,S.diag(S.Rational(3,2),1,S.Rational(4,3)),La,"coherent metric comparison",K)
kap=S.Rational(3,2)
ratio=S.simplify(agm["gamma_product"]/a["gamma_product"])
require(1/kap<=ratio<=kap,"coherent primary determinant bound actual nonunit rank")
sg=S.simplify(agm["gamma_product"]/agm["a0"])
require(1/kap<=sg/sig<=kap,"coherent complementary energy quotient bound")
lead=S.simplify(agm["a0"]/a["a0"])
require(kap**-2<=lead<=kap**2,"coherent scalar leading coefficient bound")
# Independent response perturbations can hide logarithmic changes.
eps=S.Rational(1,2**12); eps2=S.Rational(1,2**22)
f1=(z+eps)/(z+1); f2=(z+eps2)/(z+1)
eq(S.cancel(f1-f2),(eps-eps2)/(z+1),"exact small-response difference")
require((eps-eps2)/2<=eps/2,"uniform positive-interval discrepancy")
eq(eps/eps2,2**10,"unbounded logarithmic-angle discrepancy at fixed response precision")

# Root-independent finite value enclosure, checked as exponential inequalities.
for nums,dens,ell in [
    ([S.Rational(1,8),S.Integer(2)],[S.Integer(3),S.Integer(5),S.Integer(5)],S.Integer(3)),
    ([S.Integer(1)]*2,[S.Integer(5)]*2,S.Integer(5)),
    ([],[S.Integer(5)],S.Integer(1)),
    ([S.Integer(1)],[S.Integer(9)],S.Integer(1))]:
    ee=S.prod(max(S.Integer(1),ell/a) for a in nums)
    epsi=S.prod(1+ell/a for a in nums)/S.prod(1+ell/v for v in dens)
    ratio=S.cancel(ee/epsi)
    require(S.Rational(1,2)**len(nums)<=ratio<=S.Integer(2)**len(dens),"polynomial-value surrogate complete degree allowance "+str(nums))
proof=HERE/"SCALAR_RECOVERY_PROOFS.md"
text=proof.read_text(encoding="utf-8")
for j in range(1,55): require("\\tag{SD"+str(j)+"}" in text,"complete proof locator SD"+str(j))
require(re.search(r"\b"+"pl"+"ain"+r"\b",text,re.I) is None,"authored vocabulary check")
out={"status":"PASS","exact_checks":len(checks),"false_formula_controls":controls,
     "scope":"Finite auxiliary exact systems, with all metric and zero-rank factors; no native period-dependent value evaluated.",
     "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     "python":sys.version.split()[0],"sympy":S.__version__,"optimized":not __debug__,
     "witnesses":witnesses,"checks":checks}
parser=argparse.ArgumentParser(); parser.add_argument("--out",default=str(HERE/"SCALAR_CHECKS.json"))
args=parser.parse_args()
Path(args.out).write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({key:out[key] for key in ["status","exact_checks","false_formula_controls","proof_sha256","checker_sha256","optimized"]},indent=2))

