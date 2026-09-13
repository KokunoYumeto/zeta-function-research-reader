"""Additional bounded symbolic fixtures for the written PR24/Gamma endpoint interface."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
import sympy as s

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('public_transfer_core',ROOT/'files/workbenches/tau-confluent-transfer/check_transfer_core.py')
t=importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
x=t.x
records=[]
def check(name,left,right):
    t.eq(left,right)
    records.append({'name':name,'result':'pass','exact_value':str(s.cancel(left))})

z=t.model()
check('Gaussian relation coefficient vartheta_1',z.t(1),22)
check('Gaussian relation coefficient vartheta_2',z.t(2),s.Rational(86,3))
check('Gaussian quotient polynomial Qhat_2',z.Q(2),x*x-s.Rational(11,3))
G,T,lp,eps=z.gram(3)
t.eq(G,s.diag(s.Rational(7,3),s.Rational(21,11)))
check('Gaussian epsilon squared',eps,s.Rational(400,99))

# Endpoint window degrees 3,4, with four volumes at 2,3,4,5 and a=n-q=1.
def volume(N): return z.gram(N)[0].det()
def W(a): return s.prod(z.w[j] for j in range(a,a+z.q))
N0=3; window=2; a=N0-z.q
direct=volume(N0-1)*volume(N0)/(volume(N0+window-1)*volume(N0+window))
transfer=W(a)*W(a+1)*z.F(a+window).det()*z.F(a+window+1).det()/(W(a+window)*W(a+window+1)*z.F(a).det()*z.F(a+1).det())
check('Four-volume endpoint ratio equals fixed-width transfer ratio',transfer,direct)
check('Two-endpoint norm ratio',z.w[N0+window]/z.w[N0],s.prod(z.w[j+1]/z.w[j] for j in range(N0,N0+window)))

# Literal Gamma reference alpha=1, mass 1, with the same psi=x^2+1.
theta=s.Symbol('theta')
moments=[s.diff(1/s.cos(theta),theta,j).subs(theta,0) for j in range(9)]
def gamma_integral(P): return sum(coef*moments[monomial[0]] for monomial,coef in s.Poly(s.expand(P),x).terms())
ref_D=lambda n:s.prod(s.factorial(j)**2 for j in range(n))
ref_B=lambda n:s.Matrix(n,n,lambda i,j:gamma_integral(z.Pi*x**(i+j))).det() if n else s.Integer(1)
X=lambda n:z.det(n)/ref_D(n)
Y=lambda n:z.det(n,z.Pi)/ref_B(n)
ref_F2_over_V=ref_B(2)/ref_D(2)
actual_F2_over_V=z.F(2).det()/z.V.det()
check('Gamma transfer determinant correction Y_2/X_2',actual_F2_over_V/ref_F2_over_V,Y(2)/X(2))
check('Gamma quotient correction X_4/Y_2',volume(3)/(ref_D(4)/ref_B(2)),X(4)/Y(2))

# The published atomic fixture is actually symmetric, so its tested phase vanishes.
published=t.System(((s.I,1),(-s.I,1)),atomic=True)
check('Published atomic fixture has zero odd moments',sum(abs(published.m[j]) for j in range(1,32,2)),0)
check('Published atomic phase is zero',s.trace(published.gram(3)[1])-published.gram(3)[2],0)
# Independently use the explicitly positive asymmetric weights (10+node)*old_weight.
atomic=t.System(((s.I,1),(-s.I,1)),atomic=True)
nodes=list(range(-9,10)); weights=[(10+node)*(2+(j*j+3*j)%7) for j,node in enumerate(nodes)]
atomic.m=[sum(s.Integer(w)*node**d for w,node in zip(weights,nodes)) for d in range(32)]
atomic.p=[s.Integer(1)]; atomic.w=[]; atomic.a=[s.Integer(0)]; atomic.b=[]
for j in range(13):
    Pj=atomic.p[j]; norm=atomic.integral(Pj*Pj); t.require(norm>0)
    atomic.w.append(norm); atomic.b.append(atomic.integral(x*Pj*Pj)/norm)
    if j: atomic.a.append(norm/atomic.w[j-1])
    if j<12: atomic.p.append(s.expand((x-atomic.b[j])*Pj-atomic.a[j]*(atomic.p[j-1] if j else 0)))
Ga,Ta,la,ea=atomic.gram(3)
computed_log_derivative=sum(atomic.b[2:4])+atomic.a[2]*(t.inv(atomic.F(2))*atomic.jet(atomic.p[1]))[0]
check('Asymmetric additional solve gives the nonzero quotient log derivative',computed_log_derivative,la)
P=atomic.gram(2)[0].det(); M=Ga.det(); Q=atomic.gram(4)[0].det()
alpha=atomic.w[4]/atomic.w[3]; phase=s.trace(Ta)-la
t.require(phase!=0,'asymmetric phase must be nonzero')
nu_previous=atomic.w[1]*atomic.t(1); nu_current=atomic.w[2]*atomic.t(2)
gap_energy=(nu_previous-atomic.w[3])*(nu_current-atomic.w[4])/(nu_previous*atomic.w[3])-phase**2
check('Asymmetric original norm gaps give the full phase-retaining control',gap_energy,ea)
coarse=alpha*(P-Q)**2/(4*P*Q)
imbalance=alpha*(2*M-P-Q)**2/(4*P*Q)
check('Asymmetric atomic full two-loss identity',ea,coarse-imbalance-phase**2)
records.append({'name':'Asymmetric retained phase','result':'nonzero exact rational','exact_value':str(s.cancel(phase))})

# A non-reflection-stable symbolic root shows why the dagger hypothesis is needed.
delta=s.Symbol('delta',real=True,nonzero=True)
gamma=s.Symbol('gamma',real=True)
psi=x-gamma+s.I*delta
Pi=s.expand((x-gamma-s.I*delta)*psi)
root=gamma-s.I*delta
check('Without dagger stability Pi derivative at the original root is nonzero',s.diff(Pi,x).subs(x,root),-2*s.I*delta)
t.require(s.expand(Pi-psi**2)!=0,'Pi is not psi squared without dagger stability')

# A finite-moment cancellation example: individual transfer entries exceed the invariant cutoff.
m2=s.Symbol('m2',positive=True); m3=s.Symbol('m3',real=True)
F=s.Matrix([[0,-m2],[1,-m3/m2]])
check('Higher third moment cancels from q=1 N=1 transfer determinant',F.det(),m2)
check('The corresponding quotient volume uses only moments through degree two',m2/F.det(),1)
zero=t.System(((0,1),))
check('Norm gap can be zero in an allowed real-root Gaussian fixture',zero.w[0]*zero.t(0)-zero.w[1],0)

result={'created_utc':datetime.now(timezone.utc).isoformat(),'head':'dfcbba5cbf7fec8c9301fe242c13e741d762013e','checks':records,'scope':'Additional exact Gaussian/atomic/symbolic fixtures only. The missing-hypothesis example is not a claim about an actual zeta zero. No arithmetic interval certificate, uniform estimate, or Lean execution.'}
(ROOT/'INTERFACE_CHECK_RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
