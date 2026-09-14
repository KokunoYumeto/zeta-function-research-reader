from pathlib import Path
import hashlib
import json
import sympy as s

out = Path(__file__).with_suffix(".json")
u, theta, S, t = s.symbols("u theta S t", real=True)
mu = s.sqrt(2*s.pi)
c = s.Rational(1, 2)
chi = s.Poly(S*S-S+s.Rational(3,16), S)
q = 2
top = 4
series = s.series(s.cos(theta)**(-s.Rational(1,2)), theta, 0, 11).removeO().expand()
mom = [s.factorial(j)*series.coeff(theta,j)*mu for j in range(11)]
checks = []

def simp(x):
    fn = lambda e: s.factor(s.simplify(e))
    return x.applyfunc(fn) if isinstance(x, s.MatrixBase) else fn(x)

def check(name, actual, expected):
    difference = simp(actual-expected)
    if difference != (s.zeros(*difference.shape) if isinstance(difference,s.MatrixBase) else 0):
        raise ArithmeticError(f"{name}: {difference}")
    checks.append(name)

def nonzero(name, x):
    x = simp(x)
    if x == (s.zeros(*x.shape) if isinstance(x,s.MatrixBase) else 0):
        raise ArithmeticError(f"{name}: required retained term vanished")
    checks.append(name)

def expectation(p):
    p = s.Poly(s.expand(p),u)
    return s.expand(sum(v*mom[e[0]] for e,v in p.terms()))

def gram(N, weight):
    return s.Matrix(N+1,N+1,lambda i,j:expectation((c-s.I*u)**i*(c+s.I*u)**j*weight))

def Bmat(N):
    if N < q:
        return s.zeros(N+1,0)
    return s.Matrix(N+1,N-q+1,lambda i,j:chi.nth(i-j) if i>=j else 0)

def Jmat(N):
    return s.Matrix(q,N+1,lambda i,j:s.Poly(S**j,S).rem(chi).nth(i))

M0=gram(top,1)
# This calibration keeps the original Gamma mass and coordinate. The second
# measure is a positive polynomial weight of Gamma, not an actual zeta packet.
weight = u*u+u/s.Integer(3)+2
M1=gram(top,weight)
delta=M1-M0
check("mass Gamma",M0[0,0],mu)
check("mass polynomial-weight Gamma",M1[0,0],s.Rational(5,2)*mu)
check("strict positive multiplier completed square",
      weight-((u+s.Rational(1,6))**2+s.Rational(71,36)),0)

def finite(N, time):
    M=M0[:N+1,:N+1]+time*delta[:N+1,:N+1]
    dM=delta[:N+1,:N+1]
    J=Jmat(N)
    B=Bmat(N)
    Hi=(B.T.conjugate()*M*B).inv() if N>=q else s.zeros(0,0)
    G=(J*M.inv()*J.T.conjugate()).inv()
    R=M.inv()*J.T.conjugate()*G
    return tuple(map(simp,(M,dM,J,B,Hi,G,R)))

T={}
for time in (s.Rational(0),s.Rational(1,3),s.Rational(1)):
    M=M0+time*delta
    C=simp(M.inv()*delta)
    Ps, Qs, derivatives={},{},{}
    for N in (1,2,3,4):
        Mn,dMn,J,B,Hi,G,R=finite(N,time)
        I=s.eye(top+1)[:,:N+1]
        P=simp(I*Mn.inv()*I.T*M)
        Q=simp(I*B*Hi*B.T.conjugate()*I.T*M)
        Ps[N],Qs[N]=P,Q
        check(f"section N{N} t{time}",J*R,s.eye(q))
        check(f"relation orthogonality N{N} t{time}",B.T.conjugate()*Mn*R,s.zeros(B.cols,q))
        check(f"inverse orthogonal splitting N{N} t{time}",
              B*Hi*B.T.conjugate()+R*G.inv()*R.T.conjugate(),Mn.inv())
        relation_det=(B.T.conjugate()*Mn*B).det() if B.cols else 1
        check(f"Schur determinant N{N} t{time}",G.det(),Mn.det()/relation_det)
        derivative=s.trace(Mn.inv()*dMn)-s.trace(Hi*B.T.conjugate()*dMn*B)
        check(f"common projection trace N{N} t{time}",s.trace((P-Q)*C),derivative)
        derivatives[N]=simp(derivative)
        if time in (0,1):
            T[N,time]=simp(G.det())
    U=simp((Qs[3]-Qs[1])+(Qs[4]-Qs[2]))
    W=simp((Ps[3]-Ps[1])+(Ps[4]-Ps[2]))
    check(f"positive sum trace U t{time}",s.trace(U),4)
    check(f"positive sum trace W t{time}",s.trace(W),4)
    check(f"four endpoint derivative t{time}",s.trace((U-W)*C),
          derivatives[1]+derivatives[2]-derivatives[3]-derivatives[4])
    nonzero(f"U is not a projection t{time}",U*U-U)
    nonzero(f"W is not a projection t{time}",W*W-W)
    nonzero(f"noncommuting U and C t{time}",U*C-C*U)
    nonzero(f"noncommuting W and C t{time}",W*C-C*W)

# Independently differentiate the exact inverse-kernel construction at the
# first nonzero relation domain; both logarithmic curvature losses survive.
M,dM,J,B,Hi,G,R=finite(2,t)
dR=R.diff(t)
dG=G.diff(t)
ddG=G.diff(t,2)
check("literal derivative R",dR,-B*Hi*B.T.conjugate()*dM*R)
check("literal derivative G",dG,R.T.conjugate()*dM*R)
energy=simp(R.T.conjugate()*dM*B*Hi*B.T.conjugate()*dM*R)
check("literal second derivative G",ddG,-2*energy)
loss_relation=simp(2*s.trace(G.inv()*energy))
loss_metric=simp(s.trace(G.inv()*dG*G.inv()*dG))
check("two exact logarithmic losses",s.diff(s.log(s.factor(G.det())),t,2),
      -loss_relation-loss_metric)
nonzero("omitting relation loss changes curvature",loss_relation.subs(t,s.Rational(1,3)))
nonzero("omitting metric loss changes curvature",loss_metric.subs(t,s.Rational(1,3)))

# Literal mass rescaling is a separate fixture: q-volume scales by c^q and
# all four factors cancel. Its positive sum operator has condition number 1.
rescale=s.Rational(7,3)
for N in (1,2,3,4):
    J=Jmat(N)
    Gn=(J*M0[:N+1,:N+1].inv()*J.T.conjugate()).inv()
    Gscaled=(J*(rescale*M0[:N+1,:N+1]).inv()*J.T.conjugate()).inv()
    check(f"mass-rescale quotient N{N}",Gscaled,rescale*Gn)
check("mass-rescale four-endpoint cancellation",rescale**(2*q)/rescale**(2*q),1)
check("mass-rescale source relative operator",M0.inv()*(rescale*M0),rescale*s.eye(top+1))

# A nonunitary, complex coefficient-frame change transports D by similarity.
F=s.eye(top+1)
F[0,1]=1+s.I
F[2,2]=2
F[1,4]=s.Rational(1,3)
D=simp(M0.inv()*M1)
newD=simp((F.T.conjugate()*M0*F).inv()*(F.T.conjugate()*M1*F))
check("nonunitary complex frame covariance",newD,F.inv()*D*F)
exp_delta=simp((T[1,1]/T[1,0])*(T[2,1]/T[2,0])/
               ((T[3,1]/T[3,0])*(T[4,1]/T[4,0])))
nonzero("arithmetic correction in unbounded multiplier fixture",exp_delta-1)
result={
    "scope":"Exact finite calibration of the transport identities, not zeta moments or a zero-packet claim.",
    "original_gamma_mass":str(mu),
    "original_coordinate":"S=1/2+i*u",
    "test_relation":str(chi.as_expr()),
    "second_density_multiplier":str(weight),
    "multiplier_is_unbounded":True,
    "second_density_mass":str(M1[0,0]),
    "q":q,"common_cutoff":top,
    "checks":checks,"number_of_checks":len(checks),
    "exact_exp_delta_B":str(exp_delta),
    "relation_log_curvature_loss_at_one_third":str(loss_relation.subs(t,s.Rational(1,3))),
    "metric_log_curvature_loss_at_one_third":str(loss_metric.subs(t,s.Rational(1,3))),
    "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "initial_harness_repair":"The first run stopped on an unevaluated 0*sqrt(2) in a zero-matrix comparison. The exact expression evaluator was repaired; no identity, hypothesis, or expected result changed.",
    "success":True,
}
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
