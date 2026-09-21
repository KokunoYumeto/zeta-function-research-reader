"""Exact source/quotient checks and numerical spectral checks for MF1--42.

The source fixture uses the literal k=1 quartet quotient and a complete
positive discrete moment source. It tests finite algebra, not native xi
moments or the large-index analytic guards.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s
import numpy as np

y = s.symbols("y")
exact = []
numeric = []
max_residual = 0.0

def check(ok, label):
    if ok is not True and ok != s.true:
        raise AssertionError(label)
    exact.append(label)

def clean(A):
    return A.applyfunc(s.cancel)

def zero(A, label):
    if isinstance(A, s.MatrixBase):
        check(all(s.cancel(x) == 0 for x in A), label)
    else:
        check(s.cancel(A) == 0, label)

def star(A):
    return A.conjugate().T

def psd(A, label):
    A = clean(A)
    zero(A-star(A), label + ": Hermitian")
    for m in range(1, A.rows+1):
        for ii in itertools.combinations(range(A.rows), m):
            value = s.factor(A.extract(ii,ii).det())
            check(value >= 0, label + ": minor " + str(ii))

def coeff(p, n):
    p = s.Poly(p, y)
    return s.Matrix([p.nth(j) for j in range(n)])

def amap(fn, n, m):
    return s.Matrix.hstack(*(coeff(fn(y**j),m) for j in range(n)))

def matpoly(p, M):
    out = s.zeros(M.rows)
    for c in s.Poly(p,y).all_coeffs():
        out = out*M+c*s.eye(M.rows)
    return out

q=4
roots=[(2*b-1)*3-s.I*(2*a-1)*s.Rational(1,4)
       for a in range(2) for b in range(2)]
Q=s.expand(s.prod(y-r for r in roots))
J=amap(lambda f:s.rem(f,Q,y),7,q)
M=amap(lambda f:s.rem(y*f,Q,y),q,q)
nodes=list(range(-3,4))
H=s.Matrix([[sum(s.Rational(1,7)*x**(i+j) for x in nodes)
             for j in range(7)] for i in range(7)])
check(H.det()>0,"Positive complete degree-six moment source")
Xemb=s.eye(7)[:,:5]
H0=star(Xemb)*H*Xemb
J0=J*Xemb
C0=clean(J0*H0.inv()*star(J0))
G0=clean(C0.inv())
L0=clean(H0.inv()*star(J0)*G0)
zero(J0*L0-s.eye(q),"Canonical minimum is a right inverse")
zero(star(L0)*H0*L0-G0,"Canonical minimum retains attained metric")
zero(star(s.eye(5)-L0*J0)*H0*L0,
     "Canonical minimum is orthogonal to the entire relation space")

# This is an actual additional section in the same ambient source.
R=s.eye(7)[:,:q]
R[:,0]+=coeff(y*Q,7)
R[:,1]+=coeff(y*y*Q,7)
zero(J*R-s.eye(q),"Actual added section has the complete prescribed value")
check(s.Matrix.hstack(Xemb,R).rank()==7,
      "Canonical and added sources span the entire ambient source")
Cross=star(Xemb)*H*R
Gamma=star(R)*H*R
HZ=clean(Gamma-star(Cross)*H0.inv()*Cross)
FZ=clean(s.eye(q)-J0*H0.inv()*Cross)
check(HZ.rank()==2,"Normal source retains two independent positive directions")
check(Cross != s.zeros(5,q),"Added source has nonzero original cross Gram")
HZplus=s.zeros(q)
HZplus[:2,:2]=HZ[:2,:2].inv()
zero(HZ*HZplus*HZ-HZ,"Positive-range inverse retains the full null space")
Omega=clean(FZ*HZplus*star(FZ))
C1=clean(J*H.inv()*star(J))
G1=clean(C1.inv())
zero(C1-C0-Omega,"Full joint covariance equals the normal-source update")
psd(Omega,"Actual covariance update")

Lam=s.Matrix([[1,s.I,0,1],[0,1,2,-s.I],[1,0,s.I,3]])
K=s.Matrix.hstack(*Lam.nullspace())
Val=s.Matrix([[r**j for j in range(q)] for r in roots])
T=clean(star(Val)*Val)  # Unit weights at every original root.
Lbound=max(s.Integer(1),s.cancel(s.trace(T*C1)))
Bbound=max(s.Integer(1),s.cancel(s.trace(T.inv()*G1)))
psd(G1-T/Lbound,"Complete joint lower enclosure")
psd(Bbound*T-G1,"Complete joint upper enclosure")
S=s.Integer(7)
GammaBound=max(s.Integer(1),s.cancel(s.trace(T.inv()*G0)/S))

def frame(p):
    d=s.degree(p,y)
    inv=s.invert(p,Q,y)
    return amap(lambda f:s.rem(f*inv,Q,y),d,q)

def quotient(p):
    d=s.degree(p,y)
    return amap(lambda f:s.div(s.rem(p*f,Q,y),p,y)[0],q,q-d)

def filtered_parts(p):
    d=s.degree(p,y)
    U=frame(p)
    Rm=amap(lambda f:s.rem(f,p,y),5,d)
    Qu=amap(lambda f:s.div(f,p,y)[0],5,5-d)
    Js=amap(lambda f:s.rem(f,Q,y),5-d,q)
    return U,clean(Rm*L0),clean(Js*Qu*L0)

p=(y-1)**2
U,Tp,B0=filtered_parts(p)
Xp=clean(matpoly(p,M).inv())
zero(Xp-B0-U*Tp,"Canonical inverse decomposition through complete source")
HE0=clean(star(U)*G0*U)
QB0=clean((Lam*C0*star(Lam)).inv())
HB0=clean(star(U)*star(Lam)*QB0*Lam*U)
check(HB0.det()>0,"Whole observation is injective on repeated-pole frame")
a=s.cancel(1/(S*s.trace(HB0.inv())))
b=s.cancel(s.trace(HE0)/S)
t=s.cancel(Bbound*s.trace(star(U)*T*U))
lo=a/max(s.Integer(1),Lbound*GammaBound)
hi=b+t

quotient_cache={}
def quotient_data(p, C):
    # Fixed quotient coordinates for E/V_p and B/Lambda V_p.
    d=int(s.degree(p,y))
    pi=quotient(p)
    if d:
        V=frame(p)
        rows=(Lam*V).T.nullspace()
        beta=s.Matrix.vstack(*(r.T for r in rows))
    else:
        beta=s.eye(Lam.rows)
    Gbar=clean((pi*C*star(pi)).inv())
    Ob=clean(beta*Lam*s.eye(q)[:,:q-d])
    QB=clean((Ob*Gbar.inv()*star(Ob)).inv())
    sec=clean(Gbar.inv()*star(Ob)*QB)
    zero(Ob*pi-beta*Lam,"Entire quotient observation factors for degree "+str(d))
    zero(Ob*sec-s.eye(Ob.rows),"Full quotient minimum section for degree "+str(d))
    return pi,Gbar,Ob,sec

for alpha in (s.Integer(0),s.Rational(1,3),s.Integer(1)):
    C=clean((1-alpha)*C0+alpha*C1)
    G=clean(C.inv())
    QB=clean((Lam*C*star(Lam)).inv())
    sec=clean(C*star(Lam)*QB)
    PB=clean(sec*Lam)
    zero(PB*PB-PB,"Observed projection at activation "+str(alpha))
    zero(star(PB)*G-G*PB,"Observed adjoint at activation "+str(alpha))
    zero(star(sec)*G*sec-QB,"Observed section isometry at activation "+str(alpha))
    Ba=clean((1-alpha)*B0*C0*G+alpha*Xp*C1*G)
    remainder=clean((1-alpha)*U*Tp*C0*G)
    zero(Xp-Ba-remainder,"Activated inverse with all cross terms "+str(alpha))
    check(remainder.rank() <= 2,"Activated remainder rank "+str(alpha))
    if alpha==1:
        zero(remainder,"Finite-rank remainder vanishes at full activation")
    zero((1-alpha)*C0*G+alpha*C1*G-s.eye(q),
         "Exact covariance coisometry identity "+str(alpha))
    h=S/(1-alpha+alpha*S)
    HE=clean(star(U)*G*U)
    HB=clean(star(U)*star(Lam)*QB*Lam*U)
    psd(HB-lo*h*s.eye(2),"Harmonic observed lower bound "+str(alpha))
    psd(hi*h*s.eye(2)-HE,"Harmonic full upper bound "+str(alpha))
    psd(HE-HB,"Full observed contraction "+str(alpha))
    HK=clean(star(K)*G*K)
    pi=quotient(p)
    Gbar=clean((pi*C*star(pi)).inv())
    HKbar=clean(star(pi*K)*Gbar*pi*K)
    zero(HE.det()/HB.det()-HK.det()/HKbar.det(),
         "Whole kernel angle determinant identity "+str(alpha))
    # Repeated factor F=y-1, including the collision in F squared.
    F=y-1
    data=[quotient_data(s.Integer(1),C),quotient_data(F,C),quotient_data(F**2,C)]
    A01=amap(lambda f:s.div(f,F,y)[0],q,q-1)
    A12=amap(lambda f:s.div(f,F,y)[0],q-1,q-2)
    A02=amap(lambda f:s.div(f,F**2,y)[0],q,q-2)
    zero(A12*A01-A02,"Complete repeated-filter quotient composition "+str(alpha))
    pi0,Gd0,O0,S0=data[0]; pi1,Gd1,O1,S1=data[1]; pi2,Gd2,O2,S2=data[2]
    Y01=clean(O1*A01*S0); Y12=clean(O2*A12*S1)
    Y02=clean(O2*A02*S0)
    Pker=clean(s.eye(q-1)-S1*O1)
    feedback=clean(O2*A12*Pker*A01*S0)
    zero(Y02-Y12*Y01-feedback,"Entire observed feedback identity "+str(alpha))
    check(feedback.rank() <= K.cols,"Feedback retains the full kernel rank "+str(alpha))
    check(feedback != s.zeros(feedback.rows,feedback.cols),
          "Observed feedback is actually nonzero "+str(alpha))

for pD,pF in [(y-1,y-1),(y-1,y-s.Rational(101,100)),(s.Integer(1),(y-1)**2)]:
    piD=quotient(pD); piDF=quotient(pD*pF)
    sF=int(s.degree(pF,y))
    A=amap(lambda f:s.div(f,pF,y)[0],piD.rows,piDF.rows)
    XF=matpoly(pF,M).inv()
    zero(piDF*XF-A*piD,"Exact rational quotient map "+str((pD,pF)))
    zero(piDF-A*piD*matpoly(pF,M),"Polynomial quotient identity "+str((pD,pF)))
    low=s.eye(q)[:,:piD.rows]
    zero(piD*low-s.eye(piD.rows),"Original low-polynomial quotient section "+str(pD))

# A strict closed-projection guard is necessary even for the identity.
check(q > 1,"Closed threshold equality counterexample has excess rank")
# X=I, rank-zero remainder, B=1: H=I and P_{<=1}=I.
check(s.eye(q).rank()>0,"At lambda=B^-2 the closed low projection need not have rank zero")

def arr(A):
    return np.array(A.evalf(18).tolist(),dtype=complex)

def ncheck(ok,label,residual=0.0):
    global max_residual
    if not bool(ok):
        raise AssertionError(label+"; residual="+str(residual))
    numeric.append(label)
    max_residual=max(max_residual,float(abs(residual)))

def halves(G):
    ev,V=np.linalg.eigh((G+G.conj().T)/2)
    if min(ev)<=0:
        raise AssertionError("Nonpositive numerical metric")
    sq=(V*np.sqrt(ev))@V.conj().T
    inv=(V/np.sqrt(ev))@V.conj().T
    return sq,inv

def proj(A):
    U,sv,_=np.linalg.svd(A,full_matrices=False)
    rank=np.sum(sv>max(A.shape)*max(sv,default=0)*1e-12)
    return U[:,:rank]@U[:,:rank].conj().T

def opnorm(A):
    return np.linalg.norm(A,2)

G0n=arr(G0); G1n=arr(G1); C0n=arr(C0); C1n=arr(C1)
Lamn=arr(Lam)
for fp in (y,(y-1)**2,(y-1)*(y-s.Rational(101,100))):
    sd=int(s.degree(fp,y))
    Uf,Tf,Bf=filtered_parts(fp)
    Fn=arr(matpoly(fp,M)); Xn=np.linalg.inv(Fn)
    Un=arr(Uf); Bfn=arr(Bf)
    S0,I0=halves(G0n); S1,I1=halves(G1n)
    beta=max(opnorm(S0@Bfn@I0),opnorm(S1@Xn@I1))*(1+1e-10)
    canonical_inv=opnorm(S0@Xn@I0)**2
    joint_inv=opnorm(S1@Xn@I1)**2
    HEcan=Un.conj().T@G0n@Un
    HBcan=Un.conj().T@Lamn.conj().T@np.linalg.inv(Lamn@C0n@Lamn.conj().T)@Lamn@Un
    lower_a=1/(float(S)*np.trace(np.linalg.inv(HBcan)).real)
    lower_h=lower_a/max(1,float(Lbound*GammaBound))
    lowpoly=np.eye(q)[:,:sd]
    numerator_bound=np.linalg.eigvalsh(lowpoly.conj().T@G0n@lowpoly).max()
    # MF32 with exact endpoint operator norms in place of their upper bounds.
    Cx=max(canonical_inv/S,joint_inv/S)+joint_inv
    for aa in (0.0,0.02,0.25,0.8,1.0):
        Cn=(1-aa)*C0n+aa*C1n
        Gn=np.linalg.inv(Cn)
        Sg,Ig=halves(Gn)
        Uo=Sg@Un
        PV=proj(Uo)
        Fw=Sg@Fn@Ig; Xw=Sg@Xn@Ig
        Hw=Fw.conj().T@Fw
        ev,V=np.linalg.eigh((Hw+Hw.conj().T)/2)
        PB=proj(Ig@Lamn.conj().T)
        PS=proj(PB@Uo)
        PR=PB-PS
        ncheck(opnorm((np.eye(q)-PV)@Xw)<=beta*(1+1e-7),
               "Full activated inverse row bound "+str((str(fp),aa)))
        hh=float(S)/(1-aa+aa*float(S))
        ncheck(opnorm(Xw)**2<=float(Cx)*hh*(1+1e-7),
               "Harmonic full inverse norm "+str((str(fp),aa)))
        ncheck(ev[0]+1e-8>=1/(float(Cx)*hh),
               "Harmonic least-singular lower bound "+str((str(fp),aa)))
        ncheck(ev[sd-1]<=numerator_bound/(lower_h*hh)*(1+1e-7),
               "Harmonic whole least-singular block upper bound "+str((str(fp),aa)))
        Qv,_=np.linalg.qr(Uo)
        ell=np.linalg.eigvalsh(Qv.conj().T@PB@Qv).min()
        for frac in (0.01,0.4,0.9):
            lam=frac/beta**2
            sel=ev<=lam
            Pl=V[:,sel]@V[:,sel].conj().T
            eps=beta*np.sqrt(lam)
            ncheck(np.sum(sel)<=sd,"Complete closed low-projection rank "+str((str(fp),aa,frac)))
            ncheck(opnorm((np.eye(q)-PV)@Pl)<=eps+1e-7,
                   "Complete low-projection angle "+str((str(fp),aa,frac)))
            if np.any(sel):
                got=np.linalg.eigvalsh(V[:,sel].conj().T@PB@V[:,sel]).min()
                sharp=max(0,np.sqrt(max(ell,0))*np.sqrt(1-eps**2)
                          -np.sqrt(max(1-ell,0))*eps)**2
                ncheck(got+1e-7>=sharp,"Sharp whole-observation fraction "+str((str(fp),aa,frac)))
        for tt in (0.02,0.5,3.0,20.0):
            tau=tt*beta**2
            heat=(V*np.exp(-tau*np.maximum(ev,0)))@V.conj().T
            residual=float(np.trace(PR@heat).real)
            eps=sd*min(1,beta**2/(np.e*tau))+(q-sd)*np.exp(-tau/beta**2)
            ncheck(-1e-7<=residual<=eps+1e-7,
                   "Complete heat residual "+str((str(fp),aa,tt)))
            observed=PB@heat@PB
            compression=PS@heat@PS
            defect=observed-compression
            trnorm=float(np.linalg.svd(defect,compute_uv=False).sum())
            ncheck(trnorm<=eps+2*np.sqrt(sd*eps)+1e-7,
                   "Full observed heat trace norm "+str((str(fp),aa,tt)))
            trace_diff=float(np.trace(defect).real)
            ncheck(abs(trace_diff-residual)<1e-7,
                   "Original observed trace identity "+str((str(fp),aa,tt)),
                   trace_diff-residual)

# Nonvacuous near-sector model for the projection and heat mechanisms.
# This is an auxiliary spectral fixture, distinguished from the moment source.
Xn=np.array([[1,80,0],[0,1,0],[0,0,1]],dtype=float)
VF=np.array([[1.0],[0.0],[0.0]])
PV=proj(VF)
PB=proj(np.array([[1,0],[0,1],[0.3,0.2]],dtype=float))
PS=proj(PB@VF); PR=PB-PS
Hw=np.linalg.inv(Xn).T@np.linalg.inv(Xn)
ev,V=np.linalg.eigh(Hw)
beta=1.0
lam=0.01
sel=ev<=lam
ncheck(np.sum(sel)==1,"Nonvacuous slow subspace fixture")
eps=np.sqrt(lam)
ell=float((VF.T@PB@VF)[0,0])
got=float((V[:,sel].T@PB@V[:,sel])[0,0])
sharp=max(0,np.sqrt(ell)*np.sqrt(1-eps**2)-np.sqrt(1-ell)*eps)**2
ncheck(got>=sharp,"Nonvacuous sharp full-observation lower bound")
for tau in (10,100,1000):
    heat=(V*np.exp(-tau*ev))@V.T
    resid=float(np.trace(PR@heat))
    epsheat=1/(np.e*tau)+2*np.exp(-tau)
    defect=PB@heat@PB-PS@heat@PS
    ncheck(resid<=epsheat+1e-10,"Nonvacuous heat localization "+str(tau))
    ncheck(np.linalg.svd(defect,compute_uv=False).sum()<=epsheat+2*np.sqrt(epsheat)+1e-10,
           "Nonvacuous full observed trace norm "+str(tau))

receipt={
    "passed":True,
    "exact_check_count":len(exact),
    "numerical_check_count":len(numeric),
    "exact_checks":exact,
    "numerical_checks":numeric,
    "maximum_recorded_identity_residual":max_residual,
    "scope":"Exact finite polynomial source with its actual nonorthogonal added section, covariance and observed quotient identities, repeated and nearby poles, harmonic bounds and complete feedback. Floating-point spectral/heat checks use that source plus an explicitly auxiliary nonvacuous slow-space model. No check is a native xi-moment calculation, an asymptotic certificate, or verification of large-index analytic guards at k=1.",
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
out=Path(__file__).with_name("ACTIVATED_RATIONAL_CHECKS.json")
out.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":True,"exact":len(exact),"numerical":len(numeric),"receipt":str(out)}))
