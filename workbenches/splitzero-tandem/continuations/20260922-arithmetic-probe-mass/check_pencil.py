"""Independent exact checks for the original-kernel pencil continuation."""
from pathlib import Path
import json,hashlib,importlib.util,time,sys
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE=Path(__file__).resolve().parent
I=s.I
u,v=s.symbols("u v",nonzero=True)
checks=[]
def eq(name,a,b=0):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        a=s.Matrix(a);b=s.zeros(*a.shape) if b==0 else s.Matrix(b)
        rr=(a-b).applyfunc(s.simplify)
        if rr!=s.zeros(*rr.shape):raise AssertionError((name,rr))
    else:
        rr=s.simplify(a-b)
        if rr!=0:raise AssertionError((name,rr))
    checks.append({"name":name,"kind":"exact","pass":True})
def yes(name,truth):
    if not truth:raise AssertionError(name)
    checks.append({"name":name,"kind":"exact","pass":True})
def clean(A):return s.Matrix(A).applyfunc(s.simplify)
def rank(A):return len(DomainMatrix.from_Matrix(clean(A)).convert_to(s.QQ.algebraic_field(I)).rref()[1])
def basis(A):
    cs=clean(A).columnspace()
    return s.Matrix.hstack(*cs) if cs else s.zeros(A.rows,0)
def null(A):
    cs=clean(A).nullspace()
    return s.Matrix.hstack(*cs) if cs else s.zeros(A.cols,0)
def direct_chain(lengths):
    q=sum(a+1 for a in lengths);M=s.zeros(q);La=s.zeros(len(lengths),q)
    chain=[];pos=0
    for a,nu in enumerate(lengths):
        ids=list(range(pos,pos+nu+1));chain.append(ids)
        for j in range(nu):M[ids[j+1],ids[j]]=1
        M[ids[0],ids[-1]]=a+2
        M[ids[-1],ids[-1]]+=(a+1+I)/3
        La[a,ids[-1]]=1;pos+=nu+1
    for a,ids in enumerate(chain):
        M[chain[(a+1)%len(chain)][0],ids[-1]]+=(1+I)/7
    yes("fixture original action invertible "+str(lengths),M.det()!=0)
    return M,La,chain
def construct(M,La,IK):
    q=M.rows;filt=[null(La)];power=s.eye(q);stack=La
    for d in range(q):
        if filt[-1].cols==0:break
        power=clean(power*M);stack=stack.col_join(clean(La*power));filt.append(null(stack))
    if filt[-1].cols:raise ValueError("not observable")
    targets=[];hidden=[];lens=[]
    for h in range(len(filt)-1,0,-1):
        span=basis(filt[h].row_join(M*filt[h]))
        leaders=[]
        for col in range(filt[h-1].cols):
            x=filt[h-1][:,col]
            if rank(span.row_join(x))>span.cols:
                leaders.append(x);span=span.row_join(x)
        for x in leaders:
            lens.append(h)
            for j in range(h+1):
                xj=M**j*x;targets.append(xj)
                if j<h:hidden.append(xj)
    T=s.Matrix.hstack(*targets) if targets else s.zeros(q,0)
    for j in range(q):
        ej=s.eye(q)[:,j]
        if rank(T.row_join(ej))>T.cols:
            T=T.row_join(ej);lens.append(0)
    Knew=s.Matrix.hstack(*hidden) if hidden else s.zeros(q,0)
    Y,params=IK.gauss_jordan_solve(Knew)
    if params.rows:raise ValueError("nonunique original coordinate solve")
    return T,Y,lens,filt

start=time.time()
# A nonunitary change of coefficient frame and a nontrivial original kernel frame.
M0,L0,ch=direct_chain([4,2,0])
q=M0.rows
F=s.eye(q)
for j in range(q):F[j,j]=j+1
for j in range(q-1):F[j,j+1]=(1+I)/3
M=clean(F*M0*F.inv());La=clean(L0*F.inv())
hidden=[j for ids in ch for j in ids[:-1]]
IK0=F*s.eye(q)[:,hidden]
Y0=s.eye(len(hidden))
for j in range(len(hidden)-1):Y0[j,j+1]=(1-I)/2
IK=IK0*Y0
X,Y,lens,filt=construct(M,La,IK)
eq("constant ambient coefficient isomorphism",rank(X),q)
eq("constant original hidden coefficient isomorphism",rank(Y),len(hidden))
eq("recovered entire index multiset",s.Matrix(sorted(lens)),s.Matrix([0,2,4]))
p=0;kcols=[];bcols=[];idsnew=[]
for nu in lens:
    ids=list(range(p,p+nu+1));idsnew.append(ids);kcols.extend(ids[:-1]);bcols.append(ids[-1]);p+=nu+1
EK=s.eye(q)[:,kcols];EB=s.eye(q)[:,bcols]
eq("original source coordinate map",IK*Y,X*EK)
Ah=X.inv()*M*X
canonical=s.zeros(q,len(kcols));col=0
for ids in idsnew:
    for a,b in zip(ids[:-1],ids[1:]):
        canonical[a,col]=u;canonical[b,col]=-v;col+=1
eq("entire homogeneous pencil equivalence",X.inv()*(u*IK-v*M*IK)*Y,canonical)
TB=La*X*EB
yes("terminal observed coordinate isomorphism",TB.det()!=0)
eq("complete observation after coefficient maps",La*X,TB*EB.H)
for j in range(len(filt)+1):
    cols=[ids[r] for ids in idsnew for r in range(max(0,len(ids)-1-j))]
    candidate=X*s.eye(q)[:,cols]
    Kj=filt[j] if j<len(filt) else s.zeros(q,0)
    eq(f"exact filtration dimension {j}",Kj.cols,len(cols))
    eq(f"exact filtration subspace {j}",rank(Kj.row_join(candidate)),Kj.cols)
# Compare the incoming implementation as an independent second construction.
import types
source_record=next(x for x in json.loads((HERE/"SOURCE_LEDGER.json").read_text(encoding="utf-8"))["retained_source_offsets"] if x["file"]=="incoming/src/probe_mass.py")
source_bank=(HERE/"RETAINED_COMPLETE_PROOF_SOURCES.tex").read_bytes()
source_bytes=source_bank[source_record["offset"]:source_record["offset"]+source_record["length"]]
if hashlib.sha256(source_bytes).hexdigest()!=source_record["sha256"]:raise ArithmeticError("Incoming module hash mismatch")
received=types.ModuleType("received_probe_mass")
received.__file__="incoming/src/probe_mass.py"
sys.modules[received.__name__]=received
exec(compile(source_bytes,received.__file__,"exec"),received.__dict__)
rr=received.kernel_pencil_chains(M,La)
eq("received algorithm independent index match",s.Matrix(sorted(rr["indices"])),s.Matrix(sorted(lens)))
eq("received ambient isomorphism rank",rank(rr["X"]),q)
eq("received original hidden map rank",rank(rr["Y"]),len(hidden))
print("chain construction checked",flush=True)

# Canonical sections, gluing, both variables and the physical word.
P=s.zeros(len(ch),q)
for a,ids in enumerate(ch):
    nu=len(ids)-1
    for j,pos in enumerate(ids):P[a,pos]=u**j*v**(nu-j)
c=s.Rational(17,2);Aphys=c*s.eye(q)+I*M0
for a,ids in enumerate(ch):
    nu=len(ids)-1
    for j in range(nu):
        for r0 in range(nu-j):
            x=s.eye(q)[:,ids[r0]]
            polynomial=s.zeros(len(ch),1);polynomial[a]=u**r0*v**(nu-j-1-r0)
            eq(f"section chart u {a},{j},{r0}",P*M0**(j+1)*x/u**(j+1),polynomial)
            eq(f"section chart v {a},{j},{r0}",P*x/v**(j+1),polynomial)
            telesc=sum((M0**r*x/(u**(r+1)*v**(j+1-r)) for r in range(j+1)),s.zeros(q,1))
            eq(f"canonical gluing {a},{j},{r0}",(u*s.eye(q)-v*M0)*telesc,x/v**(j+1)-M0**(j+1)*x/u**(j+1))
            if r0<nu-j-1:
                phinext=P*M0**(j+2)*x/u**(j+2)
                eq(f"section inclusion variable v {a},{j},{r0}",v*phinext,polynomial)
                eq(f"section M variable u {a},{j},{r0}",u*phinext,P*M0**(j+2)*x/u**(j+1))
                eq(f"full physical action {a},{j},{r0}",(c*v+I*u)*phinext,P*M0**(j+1)*Aphys*x/u**(j+1))
            if r0<nu-j-2:
                word=Aphys**2+(2-I)*Aphys+3*s.eye(q)
                hword=(c*v+I*u)**2+(2-I)*(c*v+I*u)*v+3*v*v
                eq(f"physical word exact homogenization {a},{j},{r0}",P*M0**(j+1)*word*x/u**(j+1),hword*P*M0**(j+3)*x/u**(j+3))
vec=s.Matrix([j+1+I*(j%2) for j in range(q)])
Gc=s.eye(q)+vec*vec.H
for j in range(3):
    kj=[ids[r] for ids in ch for r in range(max(0,len(ids)-1-j))]
    kjn=[ids[r] for ids in ch for r in range(max(0,len(ids)-2-j))]
    J=s.eye(q)[:,kj];Jn=s.eye(q)[:,kjn]
    inc=J.H*Jn;mul=J.H*M0*Jn;hj=J.H*Gc*J
    eq(f"section-space original current {j}",I*(inc.H*hj*mul-mul.H*hj*inc),Jn.H*I*(Gc*M0-M0.H*Gc)*Jn)
print("canonical sections and physical action checked",flush=True)

# Complete short/long metric and current, with nonzero terminal coupling.
Mc,Lc,chains=direct_chain([1,3,0]);q=Mc.rows
Sids=chains[0]+chains[2];Lids=chains[1]
KS=[chains[0][0]];KL=chains[1][:-1]
BS=[chains[0][-1],chains[2][-1]];BL=[chains[1][-1]]
vec=s.Matrix([1,I,1,2,-I,1,1+I])
Gc=s.eye(q)+vec*vec.H
def block(rows,cols):return Gc.extract(rows,cols)
A=block(Sids,Sids)-block(Sids,KL)*block(KL,KL).inv()*block(KL,Sids)
B=block(Sids,BL)-block(Sids,KL)*block(KL,KL).inv()*block(KL,BL)
C=block(BL,BL)-block(BL,KL)*block(KL,KL).inv()*block(KL,BL)
Is=s.eye(len(Sids))[:,[Sids.index(x) for x in KS]]
Hk=block(KS,KS)-block(KS,KL)*block(KL,KL).inv()*block(KL,KS)
Hs=block(Sids,Sids)-block(Sids,Lids)*block(Lids,Lids).inv()*block(Lids,Sids)
BK=Is.H*B
eq("hidden-only short minimum",Hk,Is.H*A*Is)
eq("complete ambient successive minimum",Hs,A-B*C.inv()*B.H)
eq("exact rank-one metric defect",Hk-Is.H*Hs*Is,BK*C.inv()*BK.H)
eq("metric defect actually nonzero",rank(Hk-Is.H*Hs*Is),1)
CK=C-BK.H*Hk.inv()*BK
eq("complete determinant correction",Hk.det()/((Is.H*Hs*Is).det()),C.det()/CK.det())
hfull=block(KS+KL,KS+KL)
eq("complete kernel Schur determinant",hfull.det(),block(KL,KL).det()*Hk.det())
Z=-block(Lids,Lids).inv()*block(Lids,Sids)
ns,nl=len(Sids),len(Lids)
Mss=Mc.extract(Sids,Sids);Msl=Mc.extract(Sids,Lids);Mls=Mc.extract(Lids,Sids);Mll=Mc.extract(Lids,Lids)
Ebl=s.eye(nl)[:,[Lids.index(x) for x in BL]]
Ebs=s.eye(ns)[:,[Sids.index(x) for x in BS]]
eq("short-to-long terminal factor",Mls,(Mls*Ebs)*Ebs.H)
eq("long-to-short terminal factor",Msl,(Msl*Ebl)*Ebl.H)
yes("actual long-to-short terminal defect",Msl!=s.zeros(ns,nl))
bb=Mss+Msl*Z;cc=Msl;dd=Mls+Mll*Z-Z*Mss-Z*Msl*Z;ee=Mll-Z*Msl
Um=s.eye(ns+nl);Um[ns:,0:ns]=Z
Gord=Gc.extract(Sids+Lids,Sids+Lids);Mord=Mc.extract(Sids+Lids,Sids+Lids)
Dmetric=s.diag(Hs,block(Lids,Lids))
eq("full attained metric congruence",Um.H*Gord*Um,Dmetric)
Ab=s.Matrix.vstack(bb.row_join(cc),dd.row_join(ee))
eq("all four attained action blocks",Um.inv()*Mord*Um,Ab)
pi=s.eye(ns+nl)[:ns,:];lift=s.eye(ns).col_join(Z)
PL=s.zeros(ns+nl);PL[ns:,:ns]=-Z;PL[ns:,ns:]=s.eye(nl)
eq("complete compression defect",pi*Mord-bb*pi,pi*Mord*PL)
eq("terminal factor of compression defect",pi*Mord*PL,Msl*(-Z).row_join(s.eye(nl)))
Jexpected=I*(Dmetric*Ab-Ab.H*Dmetric)
eq("full physical current transport",Um.H*I*(Gord*Mord-Mord.H*Gord)*Um,Jexpected)
Jss=I*(Hs*bb-bb.H*Hs);Jsl=I*(Hs*cc-dd.H*block(Lids,Lids))
Jll=I*(block(Lids,Lids)*ee-ee.H*block(Lids,Lids))
eq("all current cross blocks",Jexpected,s.Matrix.vstack(Jss.row_join(Jsl),Jsl.H.row_join(Jll)))
yes("nonzero coupled current cross term",Jsl!=s.zeros(ns,nl))
corr=I*(Hs*Msl*Z-Z.H*Msl.H*Hs)
eq("short current connection correction",Jss-I*(Hs*Mss-Mss.H*Hs),corr)
yes("rank bound for current connection correction",rank(corr)<=2*len(BL))
# The kernel minimum still gives exactly the short pencil.
Lks=s.eye(q)[:,KS]-s.eye(q)[:,KL]*block(KL,KL).inv()*block(KL,KS)
proj=s.eye(q)[Sids,:]
eq("moving hidden lift preserves quotient pencil",proj*(u*s.eye(q)-v*Mc)*Lks,u*Is-v*Mss*Is)
# Nested observations and current.
fullterm=BS+BL
ob=s.eye(q)[fullterm,:];qs=(ob*Gc.inv()*ob.H).inv();Lb=Gc.inv()*ob.H*qs
obsS=s.eye(q)[BS,:];qshort=(obsS*Gc.inv()*obsS.H).inv()
redlift=Hs.inv()*Ebs*qshort
Qss=qs[:2,:2];Qsl=qs[:2,2:];Qls=qs[2:,:2];Qll=qs[2:,2:]
eq("short observed complete metric",qshort,(Ebs.H*Hs.inv()*Ebs).inv())
eq("same metric from original observed Schur",qshort,Qss-Qsl*Qll.inv()*Qls)
perm=s.eye(q)[:,Sids+Lids]
Lshort=perm*lift*redlift
eq("nested original attained section",Lshort,Gc.inv()*obsS.H*qshort)
Zb=-Qll.inv()*Qls
eq("original full section restricts to short minimum",Lb*(s.eye(2).col_join(Zb)),Lshort)
MB=ob*Mc*Lb
Ub=s.eye(3);Ub[2:,:2]=Zb
Qdiag=s.diag(qshort,Qll);MBnew=Ub.inv()*MB*Ub
eq("observed current full congruence",Ub.H*I*(qs*MB-MB.H*qs)*Ub,I*(Qdiag*MBnew-MBnew.H*Qdiag))
eq("short observed current matches ambient compression",Lshort.H*I*(Gc*Mc-Mc.H*Gc)*Lshort,redlift.H*Jss*redlift)
b=s.Matrix([1,I,2]);beta=b[2:,:]-Zb*b[:2,:]
bp=b[:2,:].col_join(beta)
eq("all phases of original scalar current",(b.H*I*(qs*MB-MB.H*qs)*b)[0],(bp.H*I*(Qdiag*MBnew-MBnew.H*Qdiag)*bp)[0])
print("complete metric and coupled current checked",flush=True)

# A nested metric family shows why the two short metrics cannot be interchanged.
lo=s.eye(q);hi=s.eye(q)
lo[KS[0],BL[0]]=lo[BL[0],KS[0]]=s.Rational(1,2)
hi[KS[0],BL[0]]=hi[BL[0],KS[0]]=s.Rational(1,2);hi[BL[0],BL[0]]=s.Rational(1,2)
yes("negative-return fixture positive",all(lo[:j,:j].det()>0 and hi[:j,:j].det()>0 for j in range(1,q+1)))
eq("negative-return fixture source nesting rank",rank(lo-hi),1)
eq("original complete hidden metric unchanged",lo.extract(KS+KL,KS+KL),hi.extract(KS+KL,KS+KL))
lo_short=lo.extract(KS,KS)-lo.extract(KS,Lids)*lo.extract(Lids,Lids).inv()*lo.extract(Lids,KS)
hi_short=hi.extract(KS,KS)-hi.extract(KS,Lids)*hi.extract(Lids,Lids).inv()*hi.extract(Lids,KS)
eq("ambient lower endpoint short metric",lo_short[0],s.Rational(3,4))
eq("ambient upper endpoint short metric",hi_short[0],s.Rational(1,2))
eq("ambient substituted return ratio",lo_short.det()/hi_short.det(),s.Rational(3,2))
# A scalar decrease attains the complete long-block width with its actual mass.
h=len(KL)
eq("long determinant return attains dimension bound",(block(KL,KL).det()/(block(KL,KL)/2).det())**2,2**(2*h))
long=[9]*128
eq("sharp combinatorial tail",sum(max(a-8,0) for a in long),128)
eq("sharp complete long hidden dimension",sum(long),1152)
eq("sharp complete long ambient dimension",sum(a+1 for a in long),1280)
for depth in range(9):
    ls=[1,2,3,8,9,12,80];sel=[a for a in ls if a>depth]
    tail=sum(a-depth for a in sel)
    eq(f"exact long hidden count depth{depth}",sum(sel),depth*len(sel)+tail)
    eq(f"exact long ambient count depth{depth}",sum(a+1 for a in sel),(depth+1)*len(sel)+tail)
    yes(f"long sector inequality depth{depth}",sum(sel)<=(depth+1)*tail and sum(a+1 for a in sel)<=(depth+2)*tail)
print("all checks passed",len(checks),flush=True)
proof=HERE/"PENCIL_PROOFS.md"
out={"status":"PASS","exact_checks":len(checks),"elapsed_seconds":time.time()-start,
     "proof_sha256_at_run":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "checks":checks,"sympy_version":s.__version__,
     "scope":"Independent exact auxiliary fixtures; no native period, source moment, EIQ value or current sign is assigned."}
(HERE/"PENCIL_CHECKS.json").write_text(json.dumps(out,indent=2),encoding="utf-8")


# Additional independent finite checks for PEN27 and literal-M transport.
"""Focused exact checks added for PEN27 and the literal M parameter transport."""
from pathlib import Path
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b=0):
    if isinstance(a,s.MatrixBase):
        b=s.zeros(*a.shape) if b==0 else s.Matrix(b)
        rr=(a-b).applyfunc(s.simplify)
        if rr!=s.zeros(*rr.shape):raise ArithmeticError((name,rr))
    elif s.simplify(a-b)!=0:raise ArithmeticError(name)
    checks.append({"name":name,"pass":True,"kind":"exact"})
I=s.I
vec=s.Matrix([1,I,2,1-I])
H=s.eye(4)+vec*vec.H;C=H.inv()
short=[0];long=[1,2,3];cap=[0,3]
Hshort=H.extract(short,short)-H.extract(short,long)*H.extract(long,long).inv()*H.extract(long,short)
Ccap=C.extract(cap,cap)
W=Ccap[1:,1:]-Ccap[1:,:1]*Ccap[:1,:1].inv()*Ccap[:1,1:]
eq("captured and whole-short covariance relation",C[:1,:1].inv(),Hshort)
eq("complete captured Schur determinant",Ccap.det(),C[0,0]*W.det())
eq("additional captured rank equals s ell",W.rows,1)
eK=(H.det()/(H/2).det())**2
eX=((2*Ccap).det()/Ccap.det())**2
eY=(Hshort.det()/(Hshort/2).det())**2
eW=((2*W).det()/W.det())**2
eq("exact return bridge after exponentiation",eX/eY,eW)
eq("bridge width attained on coherent nested metrics",eW,2**2)
eq("omitted-depth width attained",eK/eX,2**4)
eq("whole-long allowance decomposes into both pieces",eK/eY,(eK/eX)*(eX/eY))
eq("whole-long complete dimension",eK/eY,2**6)
# 021 used A=M/a. The literal-M chains are obtained with a^j.
a=s.Rational(17,3);nu=3
M=s.zeros(4)
for j in range(3):M[j+1,j]=1
M[:,3]=s.Matrix([2,1,I,3])
FA=s.diag(*[a**(-j) for j in range(4)])
D=s.diag(*[a**j for j in range(4)])
eq("literal original chain coordinate restoration",FA*D,s.eye(4))
A=M/a
for j in range(3):eq(f"auxiliary chain relation {j}",A*FA[:,j],FA[:,j+1])
u,v=s.symbols("u v")
IK=s.eye(4)[:,:3]
eq("exact homogeneous parameter transport",(u*s.eye(4)-v*M)*IK,(u*s.eye(4)-a*v*A)*IK)
G=s.eye(4)+s.ones(4,4)
eq("exact metric congruence of restored frame",D.H*(FA.H*G*FA)*D,G)
proof=HERE/"PENCIL_PROOFS.md"
out={"status":"PASS","exact_checks":len(checks),"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),"checks":checks}
(HERE/"BRIDGE_CHECKS.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print("focused exact checks",len(checks),"PASS")

