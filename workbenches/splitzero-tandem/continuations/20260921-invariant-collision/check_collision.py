"""Finite checks for IC1--42; no native arithmetic moments are claimed."""
from pathlib import Path
import itertools, json, hashlib
import sympy as sp
import numpy as np
import mpmath as mp

y=sp.symbols("y")
exact=[]; numerical=[]
def check(ok,label):
    if ok is not True and ok != sp.true: raise AssertionError(label)
    exact.append(label)
def zero(v,label):
    vals=list(v) if isinstance(v,sp.MatrixBase) else [v]
    check(all(sp.cancel(x)==0 for x in vals),label)
def star(a): return a.conjugate().T
def coeff(p,n):
    p=sp.Poly(p,y); return sp.Matrix([p.nth(j) for j in range(n)])
def amap(fn,n,m):
    return sp.Matrix.hstack(*(coeff(fn(y**j),m) for j in range(n)))
def roots(k):
    return [(2*b-k)*3-sp.I*(2*a-k)/4 for a in range(k+1) for b in range(k+1)]
def matpoly(p,M):
    out=sp.zeros(M.rows)
    for c in sp.Poly(p,y).all_coeffs(): out=out*M+c*sp.eye(M.rows)
    return out
def ncheck(ok,label):
    if not bool(ok): raise AssertionError(label)
    numerical.append(label)
def arr(a): return np.array(a.evalf(17).tolist(),dtype=complex)

# Every actual pivot box, without changing any root or coordinate.
for k in (9,13,29):
    rr=roots(k); q=(k+1)**2; qp=(k-7)**2; dd=q-qp
    for ra,rb in itertools.product(range(9),repeat=2):
        ins=[(a,b) for a in range(ra,ra+k-7) for b in range(rb,rb+k-7)]
        outer=[(a,b) for a,b in itertools.product(range(k+1),repeat=2) if (a,b) not in ins]
        check(len(ins)==qp and len(outer)==dd,"Actual interior/boundary cardinality "+str((k,ra,rb)))
        z=(2*rb-8)*3-sp.I*(2*ra-8)/4
        low=roots(k-8)
        actual=[(2*b-k)*3-sp.I*(2*a-k)/4 for a,b in ins]
        zero(sp.Matrix(actual)-sp.Matrix([r+z for r in low]),
             "Literal complex-translated original lower grid "+str((k,ra,rb)))
        check(all(a<=7 or a>=k-7 or b<=7 or b>=k-7 for a,b in outer),
              "Boundary edge guard "+str((k,ra,rb)))

# Exact q=100 conductor structure with a non-central pivot.
# Coefficients are an auxiliary finite fixture, not period evaluations.
k=9; q=100; qp=4; dd=96; m=56; jj=40
pivot=(3,4); ap=sp.Integer(2)
ac={(3,4):ap,(3,3):sp.I/3,(2,8):sp.Rational(2,5),(0,0):-sp.Rational(1,2)}
pairs=list(itertools.product(range(k+1),repeat=2))
lowpairs=list(itertools.product(range(k-7),repeat=2))
inter=[(pivot[0]+a,pivot[1]+b) for a,b in lowpairs]
bound=[p for p in pairs if p not in inter]
order=inter+bound
MA=sp.Matrix([[ac.get((a-i,b-j),0) for i,j in lowpairs] for a,b in order])
C=MA.T; T=C[:,:qp]; U=C[:,qp:]; F=-T.inv()*U
zero(T.det()-ap**qp,"Actual pivot determinant retains its coefficient and exponent")
zero(C*sp.Matrix.vstack(F,sp.eye(dd)),"Full conductor graph kernel")
B=sp.zeros(jj,m)
for j in range(jj):
    B[j,j]=sp.Rational(j+1,j+2)
    B[j,(j+3)%m]=sp.I/7
J=sp.Matrix.vstack(sp.eye(m),-B)
Z=sp.Matrix.vstack(B.T,sp.eye(jj))
zero(Z.T*J,"Complete additional observation is complex-linear transpose")
Cfull=sp.Matrix.vstack(C,sp.Matrix.hstack(sp.zeros(jj,qp),Z.T))
K=sp.Matrix.vstack(F*J,J)
zero(Cfull*K,"Original full observation kernel graph")
check(K.rank()==m and Cfull.rank()==q-m,"Full kernel and observation ranks")
qE=sp.Matrix.hstack(sp.zeros(dd,qp),sp.eye(dd))
jE=sp.Matrix.vstack(F,sp.eye(dd))
qB=sp.Matrix.hstack(sp.zeros(jj,qp),sp.eye(jj))
jB=sp.Matrix.vstack(sp.zeros(qp,jj),sp.eye(jj))
hom=sp.Matrix.vstack(sp.Matrix.hstack(T.inv(),sp.zeros(qp,jj)),sp.zeros(dd,qp+jj))
zero(sp.eye(q)-jE*qE-hom*Cfull,"Entire source homotopy identity")
zero(sp.eye(q-m)-jB*qB-Cfull*hom,"Entire output homotopy identity")
zero(Cfull*jE-jB*Z.T,"Exact reduced observation")
om=sp.Matrix([(2*b-k)*3-sp.I*(2*a-k)/4 for a,b in order])
Mdiag=sp.diag(*om); Mb=sp.diag(*om[qp:])
zero(qE*Mdiag-Mb*qE,"Arithmetic operator descends in original values")
defect=Mdiag*jE-jE*Mb
zero(defect[qp:,:],"Full section defect belongs to the removed interior")
check(defect[:qp,:]!=sp.zeros(qp,dd),"Actual algebraic section has nonzero arithmetic defect")
# No interior direction belongs to K.
check(J.rank()==m,"Boundary restriction is injective on every kernel column")

# A complete complex positive graph metric, all original q=100 rows retained.
W=sp.zeros(qp,dd)
for j in range(qp):
    W[j,j]=sp.I/sp.Integer(j+2)
    W[j,j+4]=sp.Rational(1,j+3)
A=sp.diag(2,3,5,7)
S=sp.diag(*[sp.Rational(j+2,j+1) for j in range(dd)])
G=sp.BlockMatrix([[A,A*W],[star(W)*A,S+star(W)*A*W]]).as_explicit()
HK=star(K)*G*K
Hhat=star(J)*S*J
XX=(F+W)*J
zero(HK-Hhat-star(XX)*A*XX,"Exact whole-kernel completed square with complex cross terms")
# The inverse-covariance boundary block equals the inverse of its Schur metric.
Ltri=sp.BlockMatrix([[sp.eye(qp),W],[sp.zeros(dd,qp),sp.eye(dd)]]).as_explicit()
Lin=sp.BlockMatrix([[sp.eye(qp),-W],[sp.zeros(dd,qp),sp.eye(dd)]]).as_explicit()
Cmetric=Lin*sp.diag(A.inv(),S.inv())*star(Lin)
zero(qE*Cmetric*star(qE)-S.inv(),"Attained boundary covariance through the entire interior")
# Numerical determinants avoid symbolic expansion of a large positive Gram.
Jn=arr(J); Xn=arr(XX); An=arr(A); Sn=arr(S)
Hhn=Jn.conj().T@Sn@Jn
Hkn=Hhn+Xn.conj().T@An@Xn
ld=lambda a: float(np.linalg.slogdet(a)[1])
graph=ld(np.eye(qp)+An@Xn@np.linalg.solve(Hhn,Xn.conj().T))
ncheck(abs((ld(Hkn)-ld(Hhn))-graph)<1e-10,
       "Full graph determinant via exact-rank Sylvester identity")

# Actual scalar-source divisibility at every original cutoff, auxiliary moment source.
rr=roots(1); QQ=sp.expand(sp.prod(y-r for r in rr)); qq=4
D=sp.expand((y-rr[0])*(y-rr[1]))
O=sp.expand((y-rr[2])*(y-rr[3]))
check(D!=sp.conjugate(D),"The test inner factor is genuinely unpaired")
zero(D*O-QQ,"Complete collision factorization in original coordinates")
MM=amap(lambda f:sp.rem(y*f,QQ,y),qq,qq)
DP=amap(lambda f:sp.rem(D*f,QQ,y),2,qq)
DQ=matpoly(D,MM)
zero(DQ[:,:2]-DP,"Actual multiplication word representatives")
pi=amap(lambda f:sp.div(sp.rem(D*f,QQ,y),D,y)[0],qq,2)
ro=amap(lambda f:sp.rem(f,O,y),qq,2)
zero(pi-ro,"Polynomial collision continuation equals the whole outer remainder")
Uker=amap(lambda f:O*f,2,qq)
zero(DQ*Uker,"Every interior primary direction is killed by the actual word")
zero(pi*Uker,"Every interior primary direction is killed by collision quotient")
check(DQ.rank()==2 and Uker.rank()==2,"Full collision rank, without rational inversion")
phys=sp.Rational(1,2)*sp.eye(qq)+sp.I*MM
SS=sp.symbols("SS")
DS=sp.expand(sp.I**2*D.subs(y,(SS-sp.Rational(1,2))/sp.I))
DSmat=sp.zeros(qq)
for c in sp.Poly(DS,SS).all_coeffs(): DSmat=DSmat*phys+c*sp.eye(qq)
zero(DQ-sp.I**(-2)*DSmat,"Exact physical monic phase")

nodes=list(range(-4,5)); weights=[sp.Rational(j+1,9) for j in range(9)]
for N in (3,4,7,8):
    H=sp.Matrix([[sum(w*x**(a+b) for x,w in zip(nodes,weights))
                  for b in range(N+1)] for a in range(N+1)])
    check(H.det()>0,"Complete original positive moment source "+str(N))
    JN=amap(lambda f:sp.rem(f,QQ,y),N+1,qq)
    GN=(JN*H.inv()*star(JN)).inv()
    # The weighted source uses D as an exact coefficient injection, at degree N.
    mulD=amap(lambda f:D*f,N-1,N+1)
    HD=star(mulD)*H*mulD
    JO=amap(lambda f:sp.rem(f,O,y),N-1,2)
    Gouter=(JO*HD.inv()*star(JO)).inv()
    zero(star(DP)*GN*DP-Gouter,"Exact entire-source word/outer metric equality "+str(N))
    # Prescribing boundary values before minimizing has the complete covariance.
    VO=sp.Matrix([[r**a for a in range(qq)] for r in rr[2:]])
    Gboundary=(VO*GN.inv()*star(VO)).inv()
    Eval=sp.Matrix([[r**a for a in range(N+1)] for r in rr[2:]])
    zero(Gboundary-(Eval*H.inv()*star(Eval)).inv(),
         "Full source and attained boundary minima agree "+str(N))

# Actual boundary-root inverse powers in the original coordinate order.
rrb=np.array([complex((2*b-k)*3-sp.I*(2*a-k)/4) for a,b in bound])
R=k*np.sqrt(9+1/16); varrho=min(abs(rrb))
ncheck(varrho**2>=9+1/16-1e-12,"Boundary roots retain the original nonzero radius")
for r in (1,2,4,8):
    V=np.array([[z**(-j) for j in range(1,r+1)] for z in rrb])
    TT=max(1,R*R*(1+1/varrho)/0.5)
    lower=1/(r*R*R*TT**(2*(r-1)))
    upper=dd/(varrho*varrho-1)
    ev=np.linalg.eigvalsh(V.conj().T@V)
    ncheck(ev[0]>=lower*(1-1e-7),"Inverse-power complete Vandermonde lower bound "+str(r))
    ncheck(ev[-1]<=upper*(1+1e-10),"Inverse-power complete Vandermonde upper bound "+str(r))

# The graph positive-variation estimate, with full complex forms and varying ratios.
As=[100,60,3,1]
Ss=[100,30,20,1]
hats=[]; graphs=[]; total=[]
for aa,bb in zip(As,Ss):
    hh=bb*Hhn
    hk=hh+aa*(Xn.conj().T@An@Xn)
    hats.append(ld(hh)); total.append(ld(hk)); graphs.append(ld(hk)-ld(hh))
ncheck(all(total[j]>=total[j+1]-1e-9 for j in range(3)),
       "Complete metric decreases under the positive-form source fixture")
bseq=[hats[0]-x for x in hats]
pos=sum(max(0,graphs[j+1]-graphs[j]) for j in range(3))
ncheck(pos<=bseq[-1]+1e-9,"Whole-window positive graph variation bound")
ncheck(any(graphs[j+1]>graphs[j]+1e-6 for j in range(3)),
       "Graph need not be pointwise decreasing")
Rhat=hats[0]+hats[1]-hats[2]-hats[3]
Rtotal=total[0]+total[1]-total[2]-total[3]
Rgraph=graphs[0]+graphs[1]-graphs[2]-graphs[3]
ncheck(abs(Rtotal-Rgraph-Rhat)<1e-9,"Four-cutoff graph receiver retains exact boundary return")

# Exact unpaired product bound on the outside interval, with all roots retained.
mp.mp.dps=60
for kk,piv in [(9,(0,0)),(9,(3,4)),(13,(8,8))]:
    rin=[complex((2*b-kk)*3-sp.I*(2*a-kk)/4)
         for a in range(piv[0],piv[0]+kk-7)
         for b in range(piv[1],piv[1]+kk-7)]
    rad=mp.mpf(kk)*mp.sqrt(mp.mpf(145)/16)
    cutoff=2*rad
    eta=2*len(rin)*rad/(cutoff-rad)
    for sign in (-1,1):
        for fac in (1,2,5):
            x=sign*fac*cutoff
            logratio=2*sum(mp.log(abs(1-mp.mpc(z.real,z.imag)/x)) for z in rin)
            ncheck(abs(logratio)<=eta,"Unpaired actual-root product distortion "+str((kk,piv,sign,fac)))

# Small exact Gamma generating-function coefficients test the claimed bound.
t,z=sp.symbols("t z")
series=sp.series((1+t*t)**(-sp.Rational(1,4))*sp.exp(z*sp.atan(t)),t,0,9).removeO().expand()
Mmass=mp.sqrt(2*mp.pi)
for degree in (1,2,4,8):
    for zz in (mp.mpc(3,mp.mpf(1)/4),mp.mpc(7,3),mp.mpc(0,8)):
        ev=mp.mpf(0)
        for j in range(degree+1):
            c=sp.Poly(series,t).nth(j)
            val=complex(c.subs(z,complex(zz)).evalf(30))
            rho=mp.factorial(j)/mp.rf(mp.mpf(1)/2,j)
            ev+=rho*abs(mp.mpc(val.real,val.imag))**2/Mmass
        rad=abs(zz)
        boundA=mp.e**2/Mmass*(degree+1)**mp.mpf("1.5")*(2*degree+1)**(rad+1)
        ncheck(ev<=boundA,"Full complex Gamma evaluation bound "+str((degree,str(zz))))

# Endpoint form estimate alone controls a poorly conditioned fixed restriction.
P=np.array([[1,1],[0,1e-3],[2j,2j],[0,1e-4]],complex)
ncheck(np.linalg.cond(P)>1000,"The retained restriction frame is poorly conditioned")
Pstar=P.conj().T@P
epsilon=0.08; clo=4.0; chi=1.2
center_return=2*(clo-chi)*2
rng=np.random.default_rng(419)
logs=[]
for center in (clo,clo,chi,chi):
    A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    U,_,V=np.linalg.svd(A); V=U@V
    eig=np.exp(center+np.array([-1,-.2,.3,1])*epsilon)
    Gsmall=(V*eig)@V.conj().T
    logs.append(ld(P.conj().T@Gsmall@P))
ret=logs[0]+logs[1]-logs[2]-logs[3]
ncheck(abs(ret-center_return)<=4*2*epsilon+1e-8,
       "All-direction metric bounds control the identical nonorthogonal frame")

# Full covariance activation before the complete boundary minimum.
Gn=arr(G); Cn=np.linalg.inv(Gn)
update=np.zeros((q,3),complex)
for j in range(q):
    update[j,j%3]=(1+1j*(j%5))/100
Om=update@update.conj().T
for alpha in (0.0,0.3,1.0):
    cov=Cn+alpha*Om
    metric=np.linalg.inv(cov)
    boundary=np.linalg.inv(cov[qp:,qp:])
    schur=metric[qp:,qp:]-metric[qp:,:qp]@np.linalg.solve(metric[:qp,:qp],metric[:qp,qp:])
    ncheck(np.linalg.norm(boundary-schur)<1e-10,
           "Full activated boundary Schur minimum "+str(alpha))
    Kn=arr(K); Jn=arr(J)
    xx=(arr(F)+np.linalg.solve(metric[:qp,:qp],metric[:qp,qp:]))@Jn
    hk=Kn.conj().T@metric@Kn
    hh=Jn.conj().T@boundary@Jn
    ncheck(np.linalg.norm(hk-hh-xx.conj().T@metric[:qp,:qp]@xx)<1e-9,
           "All-activation complete graph square "+str(alpha))

# Declared large-index algebraic guards, without assigning equilibrium constants.
large=2**37+1
qq=(large+1)**2; lowerq=(large-7)**2; deltaq=qq-lowerq
check(large%4==1 and lowerq>=sp.Rational(qq,2),
      "Explicit large-index original congruence and lower-degree guard")
check(sp.Rational(145,16)*large**2 <= sp.Rational(qq**2,4*2**64),
      "Explicit unpaired-root outside-radius guard")
check(sp.Rational(qq,2)>=2*deltaq+1,
      "Explicit all-direction source-degree guard")
check(8*sp.Rational(145,16)*large**2/qq<=8*sp.Rational(145,16),
      "Actual shrinking contour has bounded n rho squared")

receipt={"passed":True,"exact_check_count":len(exact),"numerical_check_count":len(numerical),
 "exact_checks":exact,"numerical_checks":numerical,
 "scope":"Actual quartet root coordinates and every pivot box; auxiliary conductor and full observation matrices with q=100; complete complex graph metric; exact full-source divisibility on the literal q=4 quartet with a positive discrete moment source; inverse-power and Gamma evaluation inequalities; unpaired product bound and nonorthogonal frame return. No fixture evaluates the actual period matrix or native xi moments, or certifies large-index analytic guards at k=9.",
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=Path(__file__).with_name("COLLISION_CHECKS.json")
out.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":True,"exact":len(exact),"numerical":len(numerical),"receipt":str(out)}))
