"""Exact auxiliary verification of RG1--54. Run with Python or Python -O."""
from pathlib import Path
from itertools import combinations, permutations
from fractions import Fraction
import argparse
import hashlib
import json
import sys
import sympy as S

sys.stdout.reconfigure(encoding="utf-8")
HERE=Path(__file__).resolve().parent
checks=[]
negative=[]
witness={}
def require(value,name):
    if value is not True and value != S.true:
        raise RuntimeError(name+": "+str(value))
    checks.append(name)
def equal(a,b,name):
    if isinstance(a,S.MatrixBase):
        require(all(S.simplify(x)==0 for x in a-b),name)
    else:
        require(S.simplify(a-b)==0,name)
def psd(A,name):
    equal(A,A.H,name+"/Hermitian")
    for n in range(1,A.rows+1):
        for ids in combinations(range(A.rows),n):
            require(S.simplify(A.extract(ids,ids).det())>=0,name+"/minor/"+str(ids))
def differs(a,b,name):
    value=any(S.simplify(x)!=0 for x in a-b) if isinstance(a,S.MatrixBase) else S.simplify(a-b)!=0
    require(value,name)
    negative.append(name)
i=S.I
L=S.Matrix([[1,0,0],[i,1,0],[1,1+i,1]])
A=L*L.H
D=L*S.diag(9,4,1)*L.H
equal((D-S.Symbol("t")*A).det(),(9-S.Symbol("t"))*(4-S.Symbol("t"))*(1-S.Symbol("t")),"relative characteristic polynomial")
psd(D-A,"increasing original form")
differs(A*D,D*A,"noncommuting endpoint forms")
J=S.Matrix([[1,1],[i,2],[2,1-i]])
Ar=J.H*A*J
Dr=J.H*D*J
psd(Dr-Ar,"restriction lower endpoint")
psd(9*Ar-Dr,"restriction upper endpoint")
require(S.simplify((Dr-4*Ar).det())<=0,"restriction middle crossing: full interlacing")
pi=S.Matrix([[1,i,0],[0,1,1]])
Qa=(pi*A.inv()*pi.H).inv()
Qd=(pi*D.inv()*pi.H).inv()
psd(Qd-Qa,"quotient monotonicity")
psd(9*Qa-Qd,"quotient top interlacing")
require(S.simplify((Qd-4*Qa).det())<=0,"quotient middle crossing: full interlacing")
y=S.Matrix([1+i,2-i])
xmin=A.inv()*pi.H*Qa*y
equal(pi*xmin,y,"quotient minimizer maps to its specified fibre")
equal((xmin.H*A*xmin)[0],(y.H*Qa*y)[0],"attained quotient value")
z=pi.nullspace()[0]
equal((z.H*A*xmin)[0],0,"quotient minimizer orthogonal to kernel")
equal(((xmin+z).H*A*(xmin+z))[0],(y.H*Qa*y)[0]+(z.H*A*z)[0],"entire affine fibre square completion")
witness["restriction_relative_polynomial"]=str(S.factor((Dr-S.Symbol("t")*Ar).det()/Ar.det()))
witness["quotient_relative_polynomial"]=str(S.factor((Qd-S.Symbol("t")*Qa).det()/Qa.det()))

# Complete complementary minima in a fixed oblique frame, ranks one and two.
T=S.Matrix([[1,i,1],[1,1,0],[i,0,1]])
require(T.det()!=0,"oblique frame invertible")
At=T.H*A*T
Dt=T.H*D*T
for m in (1,2):
    a=At[:m,:m]; b=At[:m,m:]; d=At[m:,m:]
    aa=Dt[:m,:m]; bb=Dt[:m,m:]; dd=Dt[m:,m:]
    sigma=d-b.H*a.inv()*b
    sigmad=dd-bb.H*aa.inv()*bb
    equal(At.det(),a.det()*sigma.det(),f"complete determinant factor rank{m}")
    equal(Dt.det(),aa.det()*sigmad.det(),f"complete upper determinant factor rank{m}")
    P=S.zeros(3-m,3)
    for j in range(3-m): P[j,m+j]=1
    equal(sigma,(P*At.inv()*P.H).inv(),f"Schur equals attained quotient rank{m}")
    psd(sigmad-sigma,f"complement increases rank{m}")
    loss=S.cancel(sigmad.det()/sigma.det())
    upper=S.prod([9,4,1][:3-m])
    require(1<=loss<=upper,f"full complementary loss rank{m}")
    equal(Dt.det()/At.det(),(aa.det()/a.det())*loss,f"gain factorization rank{m}")
    u=S.Matrix([1+i,2-i,3]); v=S.Matrix([2,1+i,-i])
    u1=u[:m,:]; u2=u[m:,:]; v1=v[:m,:]; v2=v[m:,:]
    correction=((u2-b.H*a.inv()*u1).H*sigma.inv()*(v2-b.H*a.inv()*v1))[0]
    equal((u.H*At.inv()*v)[0],(u1.H*a.inv()*v1)[0]+correction,f"full inverse mixed term rank{m}")
    require(S.simplify(correction)!=0,f"inverse complementary term nonzero rank{m}")
    witness[f"Schur_gain_rank{3-m}"]=str(loss)
differs(Qd,pi*D*pi.H,"restriction and attained quotient are distinct exact forms")

# Every chronology and every selected subset: actual gains vs selected-only gain.
U=S.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1]])/2
equal(U*U.H,S.eye(3),"innovation source rows orthonormal")
X=S.diag(2,1,1)*U
cols=[L*X[:,j] for j in range(4)]
dets={}
for mask in range(16):
    C=A.copy()
    for j in range(4):
        if mask & (1<<j): C+=cols[j]*cols[j].H
    dets[mask]=S.cancel(C.det()/A.det())
equal(dets[15],20,"full relative growth determinant")
differs(cols[0]*cols[0].H*cols[1]*cols[1].H,cols[1]*cols[1].H*cols[0]*cols[0].H,"chronological updates noncommuting")
strict_examples=0
for order in permutations(range(4)):
    prefix=0; pivots={}
    for j in order:
        after=prefix|(1<<j)
        pivots[j]=dets[after]/dets[prefix]
        prefix=after
    for mask in range(16):
        h=mask.bit_count()
        actual=S.prod(pivots[j] for j in range(4) if mask & (1<<j))
        selected=dets[mask]
        top=S.prod([5,2,2][:min(h,3)])
        require(actual>=1,f"selected actual positivity/{order}/{mask}")
        require(actual<=selected,f"selected chronological to selected-only/{order}/{mask}")
        require(selected<=top,f"selected exterior-rank bound/{order}/{mask}")
        if actual<selected: strict_examples+=1
require(strict_examples>0,"chronological inequality is strictly necessary")
witness["strict_selected_comparisons"]=strict_examples

# Full-root innovation with all complex cross terms.
E=S.Matrix([[1,i,1,0],[0,1,1,i]])
W=S.Matrix([[1,2,i,1],[i,1,0,3]])
e=S.Matrix([1-i,2]); w=S.Matrix([2+i,1-i])
G=E*E.H; P=S.eye(4)-E.H*G.inv()*E
En=E.row_join(e); Wn=W.row_join(w)
Pn=S.eye(5)-En.H*(En*En.H).inv()*En
kap=(1+(e.H*G.inv()*e)[0])
vv=w-W*E.H*G.inv()*e
t=(-E.H*G.inv()*e).col_join(S.Matrix([1]))
equal(En*t,S.zeros(2,1),"new full-root kernel direction")
equal((t.H*t)[0],kap,"new direction exact squared norm")
Pemb=S.zeros(5); Pemb[:4,:4]=P
equal(Pn,Pemb+t*t.H/kap,"entire full-root projector update")
C=W*P*W.H; Cn=Wn*Pn*Wn.H
equal(Cn,C+vv*vv.H/kap,"full-root covariance update")
differs(Cn,C+w*w.H/kap,"missing complex root cross terms changes covariance")
require(C.det()>0,"auxiliary original projected covariance positive")

# Exact unequal-mass Wasserstein calculation by CDF intervals.
def measure(values):
    out={}
    for a in values: out[a]=out.get(a,S.Rational(0))+S.Rational(1,len(values))
    return out
def W1(a,b):
    xs=sorted(set(a)|set(b)); fa=fb=out=S.Rational(0)
    for j,x in enumerate(xs[:-1]):
        fa+=a.get(x,0); fb+=b.get(x,0)
        out+=abs(fa-fb)*(xs[j+1]-x)
    return S.simplify(out)
xs=[S.Rational(3),S.Rational(2),S.Rational(1),S.Rational(0),S.Rational(-1)]
cc=S.Rational(1)
for h in (0,1,2):
    r=len(xs); s=r-h
    ys=[(xs[j]+xs[j+h])/2 for j in range(s)]
    padded=ys+[-cc]*h
    delta=S.Rational(h,r)
    equal(W1(measure(xs),measure(padded)),(sum(xs)-sum(padded))/r,f"padding stochastic mean cost h{h}")
    top=(sum(xs[:h])+h*cc)/r
    require(W1(measure(xs),measure(padded))<=top,f"padding complete top-rank cost h{h}")
    equal(W1(measure(padded),measure(ys)),delta*(sum(ys)/s+cc),f"removing padding exact mass cost h{h}")
    require(W1(measure(xs),measure(ys))<=top+delta*(sum(ys)/s+cc),f"unequal mass W1 triangle h{h}")
require(W1(measure(xs),measure(xs[:3]))>0,"unequal empirical ranks cannot use identical weights")

# Exact radius defect: R=log(64), tanh(R)=4095/4097, original circle is larger.
k=S.Integer(257); q=(k+1)**2
rho_old=1-S.Rational(1,4*q); rho_new=S.Rational(4095,4097)
equal((1+rho_new)/(1-rho_new),64**2,"adaptive radius Cayley identity")
require(rho_old>rho_new,"fixed original circle outside radius log64")
equal((1-rho_new)/(1+rho_new),S.Rational(1,4096),"adaptive exponential radius coordinate")
require(1-rho_old**2>=S.Rational(1,4*q),"finite denominator-circle guard")
witness["radius_defect"]={"k":257,"q":int(q),"R":"log(64)","rho_old":str(rho_old),"rho_adaptive":str(rho_new),"strict_fixed_circle_failure":True}

# Exact aliasing from a rational analytic function via the sampling quotient ring.
wvar=S.Symbol("w"); aa=(1+i)/16; rr=S.Integer(2)
for nt in (5,6,7):
    modulus=wvar**nt-rr**nt
    interpolant=S.invert(1-aa*wvar,modulus)
    for n in range(nt):
        coeff=S.expand(interpolant).coeff(wvar,n)
        exact=aa**n/(1-(aa*rr)**nt)
        equal(coeff,exact,f"entire positive alias series/T{nt}/n{n}")
        equal(coeff-aa**n,aa**n*(aa*rr)**nt/(1-(aa*rr)**nt),f"alias error/T{nt}/n{n}")
differs(S.expand(S.invert(1-aa*wvar,wvar**5-rr**5)).coeff(wvar,0),1,"alias is nonzero and cannot be silently removed")

# Whole-ideal covariance using original Gamma moments and physical phases.
tvar=S.Symbol("t"); dim=5
series=S.series(S.cos(tvar)**(-S.Rational(1,2)),tvar,0,2*dim).removeO()
mom=[S.factorial(n)*series.coeff(tvar,n) for n in range(2*dim-1)]
H0=S.Matrix(dim,dim,lambda a,b:mom[a+b])
JI=S.zeros(dim,3)
for j in range(3): JI[j,j]=4; JI[j+2,j]=1
ER=S.Matrix([[root**j for j in range(dim)] for root in [2*i,-2*i]])
equal(ER*JI,S.zeros(2,3),"all auxiliary lower roots annihilate entire ideal")
require(JI.rank()==3,"full lower ideal dimension")
vals=[[(aa**n) for n in range(dim)],[(S.Rational(1,2)**n)/S.factorial(n) for n in range(dim)]]
LM=S.Matrix(2,dim,lambda a,n:(-i)**n*S.factorial(n)*vals[a][n])
ideal=LM*JI*(JI.H*H0*JI).inv()*JI.H*LM.H
proj=H0.inv()-H0.inv()*ER.H*(ER*H0.inv()*ER.H).inv()*ER*H0.inv()
equal(ideal,LM*proj*LM.H,"whole ideal Gram inverse equals full-root projection")
Mmass=S.sqrt(2*S.pi)
equal((Mmass*(JI.H*H0*JI)).inv(),(JI.H*H0*JI).inv()/Mmass,"original Gamma mass retained by inverse")
LMwrong=S.Matrix(2,dim,lambda a,n:S.factorial(n)*vals[a][n])
wrong=LMwrong*JI*(JI.H*H0*JI).inv()*JI.H*LMwrong.H
differs(ideal.det(),wrong.det(),"dropping original derivative phase changes determinant")
witness["full_ideal_det_inverse_mass_coordinates"]=str(S.simplify(ideal.det()))
witness["physical_covariance_mass_factor"]="1/sqrt(2*pi)"

# Whole-map relative error and a complete Gram error with explicit rational constants.
K=S.Matrix([[1,0,0],[0,3,0]])
eta=S.Rational(1,8)
Err=eta*S.Matrix([[0,1,0],[i,0,0]])
equal(Err*Err.H,eta**2*S.eye(2),"exact map error squared norm")
CC=K*K.H; Khat=K+Err; Chat=Khat*Khat.H
psd(Chat-(1-eta)**2*CC,"map-relative lower form")
psd((1+eta)**2*CC-Chat,"map-relative upper form")
tau=S.Rational(1,16); Hhat=S.diag(1+tau,1-tau,1)
Chat2=Khat*Hhat.inv()*Khat.H
psd(Chat2-(1-eta)**2/(1+tau)*CC,"map plus full-Gram lower form")
psd((1+eta)**2/(1-tau)*CC-Chat2,"map plus full-Gram upper form")

# Exact factorial exterior ceilings and monotonicity.
for rank in range(1,9):
    exponent=4
    Kcap=S.Integer(rank)**exponent*3
    previous=S.Integer(1)
    for h in range(rank+1):
        bound=Kcap**h/S.factorial(h)**exponent
        require(bound>=previous,f"all-rank factorial ceiling monotone/r{rank}/h{h}")
        previous=bound

proof=HERE/"RELATIVE_GROWTH_PROOFS.md"
if not proof.exists(): proof=HERE/"GROWTH_PROOFS.md"
require(proof.exists(),"companion complete proof exists")
proof_text=proof.read_text(encoding="utf-8")
for n in range(1,55):
    require("\\tag{RG"+str(n)+"}" in proof_text,f"proof locator RG{n}")
require(chr(0) not in proof_text,"proof contains no null bytes")
banned="pl"+"ain"
import re
require(re.search(r"\b"+banned+r"\b",proof_text,re.I) is None,"authored vocabulary check")
out={"status":"PASS","exact_checks":len(checks),"negative_controls":negative,
     "scope":"Exact auxiliary fixtures; no native period-dependent values or RH closure inferred.",
     "proof_file":proof.name,"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     "python":sys.version.split()[0],"sympy":S.__version__,"optimized":not __debug__,
     "witnesses":witness,"checks":checks}
parser=argparse.ArgumentParser()
parser.add_argument("--out",default=str(HERE/"GROWTH_CHECKS.json"))
args=parser.parse_args()
Path(args.out).write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({k:out[k] for k in ("status","exact_checks","negative_controls","proof_sha256","checker_sha256","optimized")},indent=2))

