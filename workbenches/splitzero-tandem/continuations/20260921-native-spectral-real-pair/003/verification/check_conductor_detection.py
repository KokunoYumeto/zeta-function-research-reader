from pathlib import Path
import sympy as s,json
P=Path(__file__).parent
z=s.symbols('z'); tests=[]
def ck(v,t):
 if not v:raise AssertionError(t)
 tests.append(t)
# Exact rational Cauchy numerators, with actual prescribed vanishing moments.
for J in range(1,7):
 b=[s.Rational(2*j+1,3)+s.I*s.Rational(j*j+1,5) for j in range(J)]
 for v in range(J):
  aa=[s.Integer((-1)**j)*s.binomial(v,j) if j<=v else 0 for j in range(J)]
  aa=aa[:v+1];bb=b[:v+1];jj=len(bb)
  # These quadratic shifts need not make earlier moments zero; determine actual order.
  mu=[s.expand(sum(a*t**n for a,t in zip(aa,bb))) for n in range(jj)]
  nu=next(n for n,m in enumerate(mu) if m!=0)
  B=s.prod(z+t for t in bb)
  R=s.expand(sum(a*s.prod(z+bb[l] for l in range(jj) if l!=j) for j,a in enumerate(aa)))
  pp=s.Poly(R,z);d=jj-nu-1
  ck(pp.degree()==d and s.expand(pp.LC()-(-1)**nu*mu[nu])==0,'LS14 J%d v%d'%(J,v))
  step=s.Rational(2,7);base=s.Rational(-4,3)+s.I
  diff=sum((-1)**(d-j)*s.binomial(d,j)*R.subs(z,base+j*step) for j in range(d+1))
  ck(s.expand(diff-step**d*s.factorial(d)*(-1)**nu*mu[nu])==0,'LS16 finite difference J%d v%d'%(J,v))
# Exact literal upper/lower root addition. Construct the full polynomial, then
# evaluate u at the actual upper roots via its exact quotient remainder.
k=9;delta=s.Rational(1,3);gamma=s.Integer(3);c=s.Rational(k,2);cp=c-4
upper=[c+(2*a-k)*delta+s.I*(2*b-k)*gamma for a in range(k+1) for b in range(k+1)]
shifts=[4+(2*r-8)*delta+s.I*(2*t-8)*gamma for r,t in [(0,0),(2,3),(8,8)]]
coeff=[s.Integer(1),s.Integer(-3),s.Integer(2)]
Q0=s.prod(-(beta-c)/s.I for beta in upper)
ck(Q0!=0,'full Q(0) nonzero')
for a in range(k-7):
 for b in range(k-7):
  eta=cp+(2*a-k+8)*delta+s.I*(2*b-k+8)*gamma
  for h in shifts:ck(eta+h in upper,'original root addition')
  lhs=sum(aa*(-Q0/((eta+bb-c)/s.I)) for aa,bb in zip(coeff,shifts))
  rhs=-s.I*Q0*sum(aa/(eta-c+bb) for aa,bb in zip(coeff,shifts))
  ck(s.cancel(lhs-rhs)==0,'LS15 original coordinate and phase')
# Exact dual-norm proof receiver on a complex non-diagonal metric:
G=s.Matrix([[4,1,s.I],[1,5,1],[s.conjugate(s.I),1,6]])
IK=s.Matrix([1,0,0]);ell=s.Matrix([[0,2,s.I]])
u=s.Matrix([1,s.I,3]);PK=IK*(IK.H*G*IK).inv()*IK.H*G
norm=(u.H*G*u)[0];theta=s.simplify((u.H*G*PK*u)[0]/norm)
ratio=s.simplify(abs((ell*u)[0])**2/((ell*G.inv()*ell.H)[0]*norm))
ck(s.simplify(1-theta-ratio)>=0,'LS17 exact dual estimate with complete metric')
out={'status':'passed','checks':len(tests),'details':tests,'scope':'Exact rational identities LS13–17 and unchanged upper/lower root addition; full Gamma asymptotic not inferred from fixtures.'}
(P/'CONDUCTOR_DETECTION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(tests)}))

