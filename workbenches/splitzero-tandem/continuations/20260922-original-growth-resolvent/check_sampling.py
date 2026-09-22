"""Exact finite checks for CS1--24; no numerical native determinant claim."""
from pathlib import Path
from math import factorial
import hashlib,json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if not bool(value):
        raise AssertionError(name)
    checks.append(name)
def eq(name,a,b):
    if isinstance(a,s.MatrixBase):
        check(name,(a-b).applyfunc(s.simplify)==s.zeros(*a.shape))
    else:
        check(name,s.simplify(a-b)==0)
def positive(name,A):
    eq(name+' Hermitian',A,A.conjugate().T)
    for n in range(1,A.rows+1):
        check(name+f' leading minor {n}',s.simplify(A[:n,:n].det())>0)

w,y,t=s.symbols('w y t')
I=s.I
# Exact descending construction of a complete basis in nested kernels.
constraint=s.Matrix([[1,I,0,1],[0,1,1,0],[1,0,I,2],[0,0,1,1]])
chosen={}
for j in range(4,0,-1):
    for vec in constraint[:j-1,:].nullspace():
        out=vec
        for old in chosen.values():
            out=(out-old*(old.conjugate().T*out)[0]).applyfunc(s.simplify)
        norm=s.simplify((out.conjugate().T*out)[0])
        if norm!=0:
            chosen[j]=(out/s.sqrt(norm)).applyfunc(s.simplify)
            break
    check(f'nonempty descending nested selection j={j}',j in chosen)
    eq(f'actual nested constraints j={j}',constraint[:j-1,:]*chosen[j],s.zeros(j-1,1))
frame=s.Matrix.hstack(*(chosen[j] for j in range(1,5)))
eq('complete adapted basis is unitary',frame.conjugate().T*frame,s.eye(4))
check('complete adapted basis keeps all four directions',frame.rank()==4)

# The auxiliary exponential quotient has one pole-bearing and two entire rows.
Z=s.Matrix([[-s.Rational(1,2),s.Rational(1,2),-s.Rational(1,2),s.Rational(1,2)],[-1/s.sqrt(2),0,1/s.sqrt(2),0],[0,-1/s.sqrt(2),0,1/s.sqrt(2)]])
eq('original auxiliary coefficient rows are orthonormal',Z*Z.T,s.eye(3))
expvars=[1,s.exp(w/2),s.exp(w),s.exp(3*w/2)]
functions=[1/(1+s.exp(w/2))-s.Rational(1,2)+s.exp(w/2)/2,1/s.sqrt(2),s.exp(w/2)/s.sqrt(2)]
for j in range(3):
    eq(f'full exponential numerator retained j={j}',sum(Z[j,n]*expvars[n] for n in range(4)),functions[j]*(s.exp(w)-1))
eq('first conductor pole cancels in both late rows',Z[1:,:]*s.Matrix([1,-1,1,-1]),s.zeros(2,1))
check('early pole row is retained and does not cancel',(Z[:1,:]*s.Matrix([1,-1,1,-1]))[0]!=0)

# Full covariance and complete ideal in original y coordinates.
series=[s.series(A,w,0,7).removeO().expand() for A in functions]
moment_series=s.series(s.cos(t)**(-s.Rational(1,2)),t,0,13).removeO().expand()
nu=[s.factorial(n)*moment_series.coeff(t,n) for n in range(13)]
mass=s.symbols('M_sigma',positive=True)
sample_batch=s.Matrix(3,7,lambda j,n:(-I)**n*s.factorial(n)*series[j].coeff(w,n))
records=[]
for D in [4,5,6]:
    H=s.Matrix(D+1,D+1,lambda a,b:nu[a+b])
    L=sample_batch[:,:D+1]
    J=s.Matrix(D+1,D-1,lambda a,b:4*s.KroneckerDelta(a,b)+s.KroneckerDelta(a,b+2))
    G=(J.T*H*J).applyfunc(s.simplify)
    B=(L*H.inv()*L.conjugate().T).applyfunc(s.simplify)
    C=(L*J*G.inv()*J.T*L.conjugate().T).applyfunc(s.simplify)
    positive(f'exact full covariance D={D}',B)
    positive(f'exact complete ideal covariance D={D}',C)
    E=s.Matrix([[root**n for n in range(D+1)] for root in [2*I,-2*I]])
    eq(f'every lower root annihilates complete multiplication map D={D}',E*J,s.zeros(2,D-1))
    K=H.inv()-H.inv()*E.conjugate().T*(E*H.inv()*E.conjugate().T).inv()*E*H.inv()
    eq(f'complete ideal equals full-root constrained covariance D={D}',L*K*L.conjugate().T,C)
    eq(f'physical mass retained D={D}',L*J*(mass*G).inv()*J.T*L.conjugate().T,C/mass)
    # Small exact perturbations of ALL source moments and every shifted Q column.
    eps=s.Rational(1,10**12)
    dL=s.Matrix(3,D+1,lambda a,b:eps*((-I)**b)*(a+1)*(b+1))
    dJ=s.Matrix(D+1,D-1,lambda a,b:eps*(I*s.KroneckerDelta(a,b)+s.KroneckerDelta(a,b+1)))
    Lh=L+dL
    Jh=J+dJ
    Hh=s.Rational(17,16)*H
    Bh=(Lh*Hh.inv()*Lh.conjugate().T).applyfunc(s.simplify)
    Ch=(Lh*Jh*(Jh.conjugate().T*Hh*Jh).inv()*Jh.conjugate().T*Lh.conjugate().T).applyfunc(s.simplify)
    c=s.simplify(C.det()/s.trace(C)**2)
    b=s.simplify(B.det()/s.trace(B)**2)
    eta=s.Rational(1,64)
    eB2=s.simplify(s.trace(dL*H.inv()*dL.conjugate().T))
    eC2=s.simplify(s.trace(dL*J*G.inv()*J.T*dL.conjugate().T))
    delta2=s.simplify(s.trace(G.inv()*dJ.conjugate().T*H*dJ))
    check(f'full-source map error certified BEFORE Gram D={D}',eB2<=eta**2*b)
    check(f'ideal map error certified BEFORE Gram D={D}',eC2<=eta**2*c)
    check(f'full inclusion perturbation at most 1/64 D={D}',delta2<=eta**2)
    # ||Lhat H^-1/2||^2 <= trace(Lhat H^-1 Lhat*) is an exact Frobenius bound.
    Fh2=s.simplify(s.trace(Lh*H.inv()*Lh.conjugate().T))
    check(f'inclusion-induced functional error at most sqrt(c)/64 D={D}',Fh2*delta2<=eta**2*c)
    alpha=s.Rational(31,32)**2/(s.Rational(17,16)*s.Rational(65,64)**2)
    beta=s.Rational(33,32)**2/(s.Rational(15,16)*s.Rational(63,64)**2)
    positive(f'CS21 full lower bound D={D}',Ch-alpha*C)
    positive(f'CS21 full upper bound D={D}',beta*C-Ch)
    positive(f'full-source lower bound D={D}',Bh-s.Rational(3,4)*B)
    positive(f'full-source upper bound D={D}',s.Rational(5,4)*B-Bh)
    # Swapping the full ideal projection for the identity is a negative control.
    check(f'negative control unprojected matrix differs D={D}',C!=B)
    records.append({'D':D,'C_det_over_mass_power':str(s.factor(C.det())),'B_det_over_mass_power':str(s.factor(B.det()))})

alpha0=s.Rational(961,1088); beta0=s.Rational(1089,960)
check('sharper exact-J lower constant exceeds 3/4',alpha0>s.Rational(3,4))
check('sharper exact-J upper constant below 5/4',beta0<s.Rational(5,4))
check('inexact-J lower constant leaves output error 1/32',alpha>s.Rational(3,4)+s.Rational(1,32))
check('inexact-J upper constant leaves output error 1/32',beta<s.Rational(5,4)-s.Rational(1,32))

# Exact Fourier aliasing, including a finite sample error enclosure.
roots=[s.Integer(1),I,s.Integer(-1),-I]
radius=s.Rational(1,4)
for n in range(4):
    exact=s.simplify(sum((1-radius*z/3)**-1*z**(-n) for z in roots)/(4*radius**n))
    eq(f'exact Cauchy alias identity n={n}',exact-s.Rational(1,3)**n,s.Rational(1,3)**n*(radius/3)**4/(1-(radius/3)**4))
    error_values=[s.Rational(1,100)*(1,I,-1,-I)[j] for j in range(4)]
    coefficient_error=s.simplify(sum(error_values[j]*roots[j]**(-n) for j in range(4))/(4*radius**n))
    check(f'assembled scalar value tolerance n={n}',s.simplify(coefficient_error*s.conjugate(coefficient_error))<=(s.Rational(1,100)*radius**(-n))**2)

# Integer-only sample thresholds; no floating log or square root is used.
def ceil_log2_rational(num,den=1):
    z=max(0,num.bit_length()-den.bit_length())
    while (den<<z)<num:
        z+=1
    while z>0 and (den<<(z-1))>=num:
        z-=1
    return z
def ceil_half_log2_rational(num,den=1):
    return (ceil_log2_rational(num,den)+1)//2
for k in [17,21,29]:
    q=(k+1)**2; qp=(k-7)**2; r=8*k-112
    counts={}
    for eta_den in [32,64,1024]:
        # Exact synthetic bound A_j = 2^q (r/j)^qp, already >=1.
        vals=[]
        for j in range(1,r+1):
            num=16*r*eta_den**2*(1<<(2*q))*r**(2*qp)
            den=j**(2*qp)
            T=max(2*q+1,ceil_half_log2_rational(num,den))
            check(f'exact squared sample ceiling k={k} eta=1/{eta_den} j={j}',den*(1<<(2*T))>=num)
            vals.append(T)
        counts[eta_den]=sum(vals)
        base=ceil_half_log2_rational(16*r*eta_den**2*(1<<(2*q)))
        entropy=ceil_log2_rational(r**r,factorial(r))
        check(f'finite row-sum count certificate k={k} eta=1/{eta_den}',sum(vals)<=r*(2*q+2)+r*base+qp*entropy)
    check(f'tunable accuracy adds at most one sample per row per bit k={k}',counts[1024]-counts[32]<=5*r)

report={'status':'passed','exact_check_count':len(checks),'checks':checks,
    'covariance_fixtures':records,
    'scope':'Exact auxiliary exponential rows, full Gamma mass, complete root ideals, inexact inclusion certificate, Fourier samples and integer count ceilings. No original native period or limiting coefficient evaluated.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_sha256':hashlib.sha256((ROOT/'SAMPLING_PROOFS.md').read_bytes()).hexdigest()}
(ROOT/'SAMPLING_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'exact_check_count':len(checks),'native_coefficient_evaluated':False}))
