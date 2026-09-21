"""Exact finite checks accompanying the complete RLA and RQT proofs."""
from pathlib import Path
import hashlib,json
import sympy as S
B=Path(__file__).resolve().parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
alpha,beta,t=S.symbols('alpha beta t')
sig=alpha+beta; pi=alpha*beta
C=S.Matrix([[0,-pi],[1,sig]])
groups=[]; entries=0
def check(name,value):
    global entries
    vv=list(value) if isinstance(value,S.MatrixBase) else [value]
    for v in vv:
        assert S.cancel(S.expand(v))==0,(name,v)
    entries+=len(vv);groups.append(name)
def h(n):return sum(alpha**(n-j)*beta**j for j in range(n+1)) if n>=0 else S.S.Zero
q=t*t-sig*t+pi
for n in range(1,11):
    CN=S.Matrix([[-pi*h(n-2),-pi*h(n-1)],[h(n-1),h(n)]])
    check(f'RLA13 companion power {n}',C**n-CN)
    check(f'RLA13 remainder {n}',S.rem(t**n,q,t)-(-pi*h(n-2)+h(n-1)*t))
    check(f'RLA15 determinant {n}',CN.det()-pi**n)
    for root in [alpha,beta]:
        check(f'RLA16 evaluation {n} {root}',(S.Matrix([[1,root]])*CN-root**n*S.Matrix([[1,root]])))
for n in range(9):
    coeff=h(n)/pi**(n+1)
    prev=h(n-1)/pi**n if n>=1 else 0
    prev2=h(n-2)/pi**(n-1) if n>=2 else 0
    check(f'RLA19 quadratic reciprocal {n}',pi*coeff-sig*prev+prev2-(1 if n==0 else 0))
for N in range(1,8):
    u=[S.Rational(2,3)]+[S.Rational((-1)**j*(j+2),j+3) for j in range(1,N)]
    v=[1/u[0]]
    for n in range(1,N):v.append(-sum(u[j]*v[n-j] for j in range(1,n+1))/u[0])
    L=lambda co:S.Matrix(N,N,lambda i,j:co[i-j] if i>=j else 0)
    check(f'RLA11 unit inverse {N}',L(u)*L(v)-S.eye(N))
    g=[sum(u[j]*([pi,-sig,1][k-j]) for j in range(N) if 0<=k-j<=2) for k in range(N)]
    check(f'RLA11 full unit factor {N}',L(g)-L(u)*L([pi,-sig,1][:N]+[0]*max(0,N-3)))

# Genuine original Gamma weight choices. Coefficient samples test universal
# identities; they are not new evaluated programme parameters or certificates.
for N in [2,3,4,5]:
  for s in [1,9]:
    rho=[S.sqrt(S.factorial(j)/S.rf(S.Rational(s,2),j)) for j in range(N+2)]
    for order in [0,1,2]:
      g=[S.Rational(j+2,j+3)+S.I*S.Rational((-1)**j,j+4) for j in range(N+2)]
      for j in range(order):g[j]=0
      R=S.Matrix(N,N+2,lambda i,j:g[j-i]*rho[j]/rho[i] if j>=i else 0)
      H=R[:,2:]; L=R[:,:2]
      # Rational diagonal similarities keep exact computation small.
      Hi=H.inv();Z=(Hi*L).applyfunc(S.simplify)
      M=(S.eye(N)+Z*Z.H).inv().applyfunc(S.simplify)
      W=(S.eye(2)+Z.H*Z).inv().applyfunc(S.simplify)
      K=S.eye(2).col_join(-Z); A=Z.H.col_join(S.eye(N))
      Proj=(A*M*A.H).applyfunc(S.simplify)
      check(f'RQT3 kernel N{N}s{s}v{order}',R*K)
      check(f'RQT4 right inverse N{N}s{s}v{order}',R*A*M*Hi-S.eye(N))
      check(f'RQT4 orthogonality N{N}s{s}v{order}',K.H*A)
      check(f'RQT5 complement N{N}s{s}v{order}',Proj+K*W*K.H-S.eye(N+2))
      check(f'RQT6 covariance N{N}s{s}v{order}',R*R.H-H*(S.eye(N)+Z*Z.H)*H.H)
      Zb=Z[-2:,:];B0=R[:,:N]
      check(f'RQT11 determinant N{N}s{s}v{order}',Zb.det()*H.det()-g[0]**N)
      J=S.eye(N+2)[:,order:order+N];Av=R*J;Ev=J.H*Proj*J
      check(f'RQT8 volume N{N}s{s}v{order}',Ev.det()*(R*R.H).det()-Av.det()*S.conjugate(Av.det()))
      if order==2:
        check(f'RQT8 actual order-two metric N{N}s{s}',Ev-S.eye(N))
      if order==0:
        w=S.Matrix([S.Rational(j+1,3)+S.I/(j+2) for j in range(N)])
        ell=Zb.inv()*w[-2:,:];mid=w[:-2,:]-Z[:-2,:]*ell
        check(f'RQT12 exact inverse N{N}s{s}',B0*ell.col_join(mid)-H*w)
      # Eigenvalue proof without irrational matrix square roots: the trace
      # and determinant of V*V equal those of W Zb* Zb.
      F=K[:N,:];E0=S.eye(N)-F*W*F.H
      Vsq=W*Zb.H*Zb
      lam=S.symbols('lambda')
      check(f'RQT10 angle polynomial N{N}s{s}v{order}',
            E0.charpoly(lam).as_expr()-(lam-1)**(N-2)*Vsq.charpoly(lam).as_expr())

e,f,hv,kv,r0,r1,rm,rd,rp,rpp=S.symbols('e f h k rho0 rho1 rhom rhod rhop rhopp',nonzero=True)
corner=S.Matrix([[hv*rm/r0,kv*rd/r0],[0,hv*rd/r1]])
tail=S.Matrix([[e*rp/rm,f*rpp/rm],[0,e*rpp/rd]])
omega=S.Matrix([[e*hv*rp/r0,(f*hv+e*kv)*rpp/r0],[0,e*hv*rpp/r1]])
check('RQT21 complete leading angle corner',corner*tail-omega)
check('RQT21 determinant with complete upper-right entry',omega.det()-e**2*hv**2*rp*rpp/(r0*r1))
check('RQT20 nonresonant last-row factor',S.Matrix([[0,kv*rd/r0]])*tail-S.Matrix([[0,e*kv*rpp/r0]]))
L,kappa=S.symbols('L kappa')
check('RQT22 finite-ratio crossover',corner.subs(kv,kv+L*kappa)*tail-omega.subs(kv,kv+L*kappa))
receipt={'status':'PASS','groups':len(groups),'scalar_identities':entries,
 'coverage':groups,'checker_sha256':sha(Path(__file__)),
 'source_sha256':{n:sha(B/n) for n in ['independent/REAL_PAIR_LOCAL_ALGEBRA.tex','REAL_PAIR_MOVING_QUOTIENT.tex','independent/REAL_PAIR_ANGLE_CONSTANTS.tex']},
 'limits':'Universal companion powers checked through10; inverse-unit identities through cutoff7; exact matrix checks N2..5 at both original source orders s1 and9, on all three algebraic order strata. Sample coefficients test matrix identities only. Analytic existence, all-degree claims and original certified point use the complete cited proofs, not these finite samples.'}
(B/'independent/REAL_PAIR_LOCAL_OBJECT_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='coverage'},indent=2))
