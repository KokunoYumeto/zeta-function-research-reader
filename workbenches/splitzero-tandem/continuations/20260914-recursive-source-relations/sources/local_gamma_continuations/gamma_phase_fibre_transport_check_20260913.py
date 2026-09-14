"""Exact independent finite calibrations for GP.7--GP.23; no analytic certificate."""
from pathlib import Path
import argparse, hashlib, json, sys
import sympy as s

p=argparse.ArgumentParser()
p.add_argument('--output',type=Path,required=True)
p.add_argument('--fault',choices=['phase','mass','relative'])
args=p.parse_args()
checks=[]
def check(name,actual,expected):
    if isinstance(actual,s.MatrixBase):
        ok=actual.shape==expected.shape and all(s.expand(v)==0 for v in actual-expected)
    else:
        ok=s.cancel(actual-expected)==0
    checks.append({'name':name,'passed':bool(ok)})
    return ok
def positive(name,M):
    checks.append({'name':name,'passed':all(M[:j,:j].det()>0 for j in range(1,M.rows+1))})

# A literal conditional two-atom fibre: parent masses 2,3, fibre mass 5.
H=s.diag(s.Rational(2,5),s.Rational(3,5))
one=s.Matrix([1,1]);a=s.Matrix([1+s.I,2-s.I])
b=(a.conjugate().T*H*a)[0];ak=(one.T*H*a)[0]
P=one*one.T*H
Q=a*(a.T if args.fault=='phase' else a.conjugate().T)*H/b
check('conditional original fibre mass',5*b,19)
check('conditional full complex amplitude',5*ak,8-s.I)
check('fibre P idempotent',P*P,P)
check('fibre Q idempotent',Q*Q,Q)
check('fibre Q weighted self-adjoint',Q.conjugate().T*H,H*Q)
check('fibre projector trace',s.trace((P-Q)**2),2*(1-s.conjugate(ak)*ak/b))
comm=P*Q-Q*P
check('fibre commutator HS',s.trace(H.inv()*comm.conjugate().T*H*comm),2*(s.conjugate(ak)*ak/b)*(1-s.conjugate(ak)*ak/b))
check('unscaled conditional variance',b-s.conjugate(ak)*ak,s.Rational(6,5))

# Independent gamma moments from derivatives of the original Laplace function.
# This polynomial calibration is not a bounded zeta multiplier. All its fixed
# moments exist; it tests algebraic identities, not GP.12 or strict quartet decay.
u,t,v,z,S=s.symbols('u t v z S',real=True)
mass=s.Rational(1,2); k=2
def moments(alpha,mu,degree):
    coeff=s.Poly(s.series(s.cos(z)**(-alpha),z,0,degree+1).removeO(),z)
    return [mu*s.factorial(j)*coeff.nth(j) for j in range(degree+1)]
one_m=moments(2,mass,14); sum_m=moments(4,mass**2,14)
def integral(poly):
    P0=s.Poly(s.expand(poly),u)
    return s.expand(sum(c*sum_m[j[0]] for j,c in P0.terms()))
def product_integral(poly):
    P0=s.Poly(s.expand(poly),t,v)
    return s.expand(sum(c*one_m[j[0]]*one_m[j[1]] for j,c in P0.terms()))
amp=(1+s.I*t/2)*(1+s.I*v/2)
dens=s.expand(amp*s.conjugate(amp))
akg=s.Rational(6,5)+s.I*u/2-u**2/20
# Determine the whole degree-four conditional density by independent
# product moment equations, using derivatives of cos(z)^(-2), cos(z)^(-4).
moment_matrix=s.Matrix(5,5,lambda i,j:sum_m[i+j])
rhs=s.Matrix([product_integral(dens*(t+v)**j) for j in range(5)])
bc=moment_matrix.inv()*rhs
bk=s.expand(sum(bc[j]*u**j for j in range(5)))
dk=s.expand(bk-akg*s.conjugate(akg))
for j in range(9):
    check(f'complex projected moment {j}',integral(akg*u**j),product_integral(amp*(t+v)**j))
    check(f'density projected moment {j}',integral(bk*u**j),product_integral(dens*(t+v)**j))
check('full original tensor mass',integral(bk)*(2 if args.fault=='mass' else 1),product_integral(dens))
check('full amplitude variance norm',integral(dk),product_integral(dens)-integral(akg*s.conjugate(akg)))
check('original S phase first pairing',integral((1-s.I*u)*(1+s.I*u)**2*bk),product_integral((1-s.I*(t+v))*(1+s.I*(t+v))**2*dens))

def gram(weight,N):
    return s.Matrix(N+1,N+1,lambda i,j:integral((1-s.I*u)**i*(1+s.I*u)**j*weight))
def section(M,B):
    R0=s.zeros(M.rows,2);R0[0,0]=R0[1,1]=1
    return R0-B*(B.conjugate().T*M*B).inv()*B.conjugate().T*M*R0 if B.cols else R0
quotient_records=[]
chi=(S-1)**2-2
for N in range(1,5):
    B=s.Matrix(N+1,max(0,N-1),lambda i,j:s.Poly(s.expand(chi*S**j),S).nth(i))
    Mh=gram(bk,N);Mc=gram(akg*s.conjugate(akg),N);Mr=gram(dk,N)
    check(f'N{N} complete Gram addition',Mh,Mc+Mr)
    positive(f'N{N} coherent Gram positive',Mc)
    positive(f'N{N} relative Gram positive',Mr)
    Rh=section(Mh,B);Rc=section(Mc,B)
    K=(B.conjugate().T*Mh*B).inv()*B.conjugate().T*Mr*Rc if B.cols else s.zeros(0,2)
    check(f'N{N} exact section correction',Rh,Rc-B*K)
    check(f'N{N} original relation orthogonality',B.conjugate().T*Mh*Rh,s.zeros(B.cols,2))
    Gh=Rh.conjugate().T*Mh*Rh;Gc=Rc.conjugate().T*Mc*Rc
    loss1=K.conjugate().T*B.conjugate().T*Mc*B*K
    loss2=Rh.conjugate().T*Mr*Rh
    check(f'N{N} both quotient positive terms',Gh,Gc+loss1+(s.zeros(2) if args.fault=='relative' else loss2))
    positive(f'N{N} strict quotient difference',Gh-Gc)
    check(f'N{N} determinant correction',Gh.det()/Gc.det(),(s.eye(2)+Gc.inv()*(loss1+loss2)).det())
    quotient_records.append({'N':N,'det_h':str(s.factor(Gh.det())),'det_coherent':str(s.factor(Gc.det())),'det_difference':str(s.factor((Gh-Gc).det()))})

proof=Path(__file__).with_name('gamma_phase_fibre_transport_20260913.tex')
result={'schema':'gamma-phase-fibre-exact-check-v1','optimized_python':not __debug__,
 'fault':args.fault,'checks':len(checks),'failed':sum(not c['passed'] for c in checks),
 'scope':'Exact finite conditional operator and complex gamma-polynomial calibration. No analytic zeta interval, bounded multiplier, or RH asymptotic certificate.',
 'one_factor_gamma_mass':str(mass),'tensor_mass':str(mass**2),
 'a_k':str(akg),'b_k':str(bk),'d_k':str(dk),'quotients':quotient_records,
 'results':checks,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'python':sys.version,'sympy':s.__version__}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:result[key] for key in ['checks','failed','fault','a_k','b_k','d_k']}))
raise SystemExit(1 if result['failed'] else 0)
