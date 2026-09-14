#!/usr/bin/env python3
"""Exact finite checks for the displayed holonomy/quotient identities.
No arithmetic zero data, numerical quadrature, or Lean theorem is certified.
Assertions use explicit exceptions and also run under python -O.
"""
from __future__ import annotations
import argparse, itertools, json, sys
import sympy as s

I=s.I; S=s.Symbol('S'); R=s.Rational
CASES=[]
def case(fn): CASES.append(fn); return fn
def equal(a,b,msg='identity'):
    d=a-b
    ok=all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0
    if not ok: raise ArithmeticError(f'{msg}: {d}')
def require(p,msg):
    if not p: raise ArithmeticError(msg)
def psd(A):
    equal(A,A.H,'Hermitian')
    for n in range(1,A.rows+1):
        for ix in itertools.combinations(range(A.rows),n):
            v=s.simplify(A.extract(ix,ix).det())
            require(v.is_nonnegative is True,f'negative/unknown principal minor {v}')
def pd(A):
    equal(A,A.H)
    for n in range(1,A.rows+1):
        v=s.simplify(A[:n,:n].det()); require(v.is_positive is True,'nonpositive leading minor')
def quotient(M,J):
    K=J*M.inv()*J.H; G=s.simplify(K.inv()); C=s.simplify(M.inv()*J.H*G)
    return G,C

def jmatrix(chi,N):
    q=s.degree(chi,S)
    return s.Matrix(q,N+1,lambda r,c:s.Poly(s.rem(S**c,chi,S),S).nth(r))
def bmatrix(chi,N):
    q=s.degree(chi,S)
    return s.Matrix(N+1,max(0,N-q+1),lambda r,c:s.Poly(chi*S**c,S).nth(r))
def coeff(p,N):return s.Matrix([s.Poly(s.expand(p),S).nth(r) for r in range(N+1)])
def mmoment(points,weights,N):
    V=s.Matrix([[x**j for j in range(N+1)] for x in points])
    return s.simplify(V.H*s.diag(*weights)*V)

def block_fixture(q=2,eta=R(1,3)):
    H=s.Matrix(q,q,lambda i,j:1 if i==j else 0)
    D=s.zeros(2*q)
    D[:q,q:]=eta*H;D[q:,:q]=eta*H
    U=s.eye(2*q)
    for i in range(2*q-1):U[i,i+1]=R(i+1,5)
    U[0,2*q-1]=I/7
    M=7*U.H*U
    A=7*U.H*(s.eye(2*q)+D)*U
    B=7*U.H*(s.eye(2*q)-D)*U
    J=jmatrix((S-1)**q,2*q-1)
    return M,[A,B],J

def ccoef(M,inc,unit,ell):
    MF=inc.H*M*inc
    dist=(unit.H*(M-M*inc*MF.inv()*inc.H*M)*unit)[0]
    l=ell*inc
    return s.simplify(dist*(l*MF.inv()*l.H)[0])

@case
def split_fibres_preserve_absence_and_supported_kernel():
    tau=('absent',); e=('ell',s.Integer(0))
    def lift(x):return tau if x==tau else (x[0],s.Integer(0)*x[1])
    equal(lift(('ell',7))[1],0)
    require(lift(('ell',7))==e,'supported target')
    require(lift(tau)==tau and e!=tau,'absence')

@case
def finite_cover_full_laurent_basis():
    for m in range(1,8):
        for n in range(-17,18):
            a,j=divmod(n,m)
            require(0<=j<m and m*a+j==n,'Laurent reconstruction')
        # multiplication crossing the retained basis boundary
        for i in range(m):
            for j in range(m):
                a,b=divmod(i+j,m); require(a*m+b==i+j,'basis product')

@case
def character_projectors_complete_orthogonal():
    for m,zeta in [(2,s.Integer(-1)),(4,I)]:
        T=s.zeros(m)
        for a in range(m):T[a,(a+1)%m]=1
        P=[sum((zeta**(j*a)*T**a for a in range(m)),s.zeros(m))/m for j in range(m)]
        equal(sum(P,s.zeros(m)),s.eye(m))
        for j in range(m):
            equal(P[j].H,P[j]);equal(P[j]*P[j],P[j]);equal(T*P[j],zeta**(-j)*P[j])
            for l in range(m):equal(P[j]*P[l],P[j] if j==l else s.zeros(m))

@case
def fourier_inverse_retains_cover_factor():
    for m,zeta in [(2,s.Integer(-1)),(4,I)]:
        U=s.Matrix(m,m,lambda j,a:zeta**(j*a)/s.sqrt(m))
        equal(U.H*U,s.eye(m));equal(U*U.H,s.eye(m))
        v=s.Matrix([R(a+1,3)+I*R(a,7) for a in range(m)])
        equal(U.H*(U*v),v)

@case
def phase_mean_filters_only_correlations_divisible_by_cover_degree():
    for m,zeta in [(2,s.Integer(-1)),(4,I)]:
        for n in range(-13,14):
            avg=sum(zeta**(j*n) for j in range(m))/m
            equal(avg,1 if n%m==0 else 0)

@case
def shifted_sampling_refinement_keeps_sum_coordinate():
    for m in range(1,7):
        th=R(2,7); L=R(5,3)
        for a in range(m):
            for n in range(-4,5):
                # frequencies in units 2*pi
                equal((n+(th+a)/m)/(L/m),(m*n+a+th)/L)

@case
def repeated_jet_quotient_and_original_relation():
    chi=(S-1)**2;N=3;J=jmatrix(chi,N);B=bmatrix(chi,N)
    M=mmoment([1+I*x for x in [-2,-1,0,1,2]],[7,11,13,11,7],N)
    pd(M);G,C=quotient(M,J)
    equal(J*B,s.zeros(2,2));equal(J*C,s.eye(2));equal(B.H*M*C,s.zeros(2,2))
    equal(C.H*M*C,G);pd(G)

@case
def exact_mean_variance_uses_original_boundary_columns():
    M,Ms,J=block_fixture();B=bmatrix((S-1)**2,3)
    G,C=quotient(M,J);Gs=[];Var=s.zeros(2)
    for Mj in Ms:
        Gj,Cj=quotient(Mj,J);Gs.append(Gj)
        X=(B.H*Mj*B).inv()*B.H*Mj*C
        equal(C-Cj,B*X);equal(J*(C-Cj),s.zeros(2))
        Var+=X.H*(B.H*Mj*B)*X/2
    equal(G-sum(Gs,s.zeros(2))/2,Var);psd(Var)

@case
def sharp_quadratic_constant_with_literal_mass_seven():
    for eta in [R(1,7),R(1,3),R(3,4)]:
        M=7*s.eye(2);J=s.Matrix([[1,0]])
        Ms=[7*s.Matrix([[1,sg*eta],[sg*eta,1]]) for sg in [1,-1]]
        G,C=quotient(M,J);Gavg=sum((quotient(A,J)[0] for A in Ms),s.zeros(1))/2
        equal(Gavg,(1-eta**2)*G);equal(G[0],7)

@case
def matrix_quadratic_comparison_under_nonunitary_coordinates():
    for q in [1,2,3]:
        eta=R(1,3);M,Ms,J=block_fixture(q,eta)
        G,C=quotient(M,J);Ga=sum((quotient(A,J)[0] for A in Ms),s.zeros(q))/2
        psd(G-Ga);psd(Ga-(1-eta**2)*G)

@case
def inverse_chord_and_inverse_mean_block():
    eta=R(2,5);M,Ms,J=block_fixture(2,eta)
    Ks=[];Gs=[]
    for Mt in Ms:
        upper=(2*M.inv()-M.inv()*Mt*M.inv())/(1-eta**2)
        psd(upper-Mt.inv())
        G,C=quotient(Mt,J);K=G.inv();Ks.append(K);Gs.append(G)
        psd(K.row_join(s.eye(2)).col_join(s.eye(2).row_join(G)))
    Kbar=sum(Ks,s.zeros(2))/2;Gbar=sum(Gs,s.zeros(2))/2
    psd(Gbar-Kbar.inv())

@case
def asymmetric_chord_bound():
    a=R(1,2);b=R(5,4)
    # probabilities chosen so the literal source mean is M
    p=(b-1)/(b-a)
    M=s.Matrix([[5,1],[1,3]]);J=s.Matrix([[1,0]])
    Ms=[a*M,b*M];G,_=quotient(M,J)
    Ga=p*quotient(Ms[0],J)[0]+(1-p)*quotient(Ms[1],J)[0]
    equal(p*Ms[0]+(1-p)*Ms[1],M)
    psd(Ga-(a*b/(a+b-1))*G);psd(G-Ga)

@case
def equal_jet_cochain_split_and_contractible_complement():
    chi=(S-1)**2;N=3;J=jmatrix(chi,N);B=bmatrix(chi,N)
    seed=coeff(2+3*S,N);m=3
    rel=[s.Matrix([1,-2]),s.Matrix([3,4]),s.Matrix([-2,1])]
    Ps=[seed+B*z for z in rel];av=sum(Ps,s.zeros(N+1,1))/m
    ds=[P-av for P in Ps]
    equal(sum(ds,s.zeros(N+1,1)),s.zeros(N+1,1))
    for P,d in zip(Ps,ds):equal(J*P,J*seed);equal(J*d,s.zeros(2,1));equal(av+d,P)
    # identity differential on the zero-sum relation component has h=I
    W=s.eye((m-1)*B.cols);equal(W*W,W)

@case
def degree_raising_map_commutes_with_actual_remainder():
    for chi in [(S-1)**2,S**3+2*S+1]:
        q=s.degree(chi,S);N=q+1;J=jmatrix(chi,N);Jp=jmatrix(chi,N+1)
        U=s.zeros(N+2,N+1)
        for c in range(N+1):U[c+1,c]=1
        A=jmatrix(chi,q)[:,1:q+1]
        equal(Jp*U,A*J)

@case
def unchanged_unit_and_theta_primitive():
    chi=(S-1)**2;N=3;J=jmatrix(chi,N)
    M,Ms,J0=block_fixture(2);G,C=quotient(M,J)
    u=s.Matrix([[0,-1],[1,2]]) # multiplication by S modulo (S-1)^2
    require(u.det()!=0,'retained unit invertible')
    for Mt in Ms:
        Gt,Ct=quotient(Mt,J)
        equal(u*J*Ct,u)
        for c in range(2):
            pol=sum((Ct[r,c]-C[r,c])*S**r for r in range(N+1))
            qq,rr=s.div(pol,chi,S);equal(rr,0);equal(pol,s.expand(chi*qq))

@case
def original_sampled_action_keeps_boundary_control_sign():
    q=2;N=3;k=2;chi=(S-1)**2;J=jmatrix(chi,N)
    pts=[1+I*x for x in [-3,-2,-1,0,1,2,3]];w=[2,3,5,7,11,13,17]
    V=s.Matrix([[x**r for r in range(N+1)] for x in pts]);W=s.diag(*w);M=V.H*W*V
    G,C=quotient(M,J);A=jmatrix(chi,q)[:,1:q+1]
    RR=V*C;D=s.diag(*pts);BB=D*RR-RR*A
    equal(D.H*W+W*D,k*W)
    equal(A.H*G+G*A-k*G,-(RR.H*W*BB+BB.H*W*RR))

@case
def finite_phase_interlaced_moment_identity():
    m=4;N=3;k=2;short=[]
    allpts=[];allweights=[]
    for j in range(m):
        ns=[m*n+j for n in range(-2,3)]
        pts=[R(k,2)+I*R(a,m) for a in ns]
        ww=[R(7,1+a*a) for a in ns]
        short.append(mmoment(pts,ww,N));allpts+=pts;allweights += [x/m for x in ww]
    long=mmoment(allpts,allweights,N)
    equal(sum(short,s.zeros(N+1))/m,long)
    J=jmatrix((S-1)**2,N);G,C=quotient(long,J)
    Gavg=s.zeros(2);cost=s.zeros(2)
    for Mt in short:
        Gt,Ct=quotient(Mt,J);Gavg+=Gt/m;cost+=(C-Ct).H*Mt*(C-Ct)/m
    equal(G-Gavg,cost);psd(cost)

@case
def residue_constituent_comparison_retains_unit_and_dual_factor():
    M,Ms,J=block_fixture(2,R(1,3));G,C=quotient(M,J)
    Ga=sum((quotient(Mt,J)[0] for Mt in Ms),s.zeros(2))/2
    inc=s.Matrix([-1,1]);unit=s.Matrix([1,0]);ell=s.Matrix([[0,1]])
    cg=ccoef(G,inc,unit,ell);ca=ccoef(Ga,inc,unit,ell)
    require(cg>0 and ca>0,'proper invariant constituent')
    require(s.simplify(ca-R(8,9)*cg).is_nonnegative,'lower residue bound')
    require(s.simplify(R(9,8)*cg-ca).is_nonnegative,'upper residue bound')

@case
def translation_congruence_keeps_coefficient_but_not_trace_shift():
    a=R(2,3)+I/5;T=s.Matrix([[1,a],[0,1]])
    M=s.Matrix([[7,1+I],[1-I,5]])
    inc=s.Matrix([0,1]);unit=s.Matrix([1,0]);ell=s.Matrix([[0,1]])
    ca=ccoef(T.H*M*T,T.inv()*inc,T.inv()*unit,ell*T)
    equal(ca,ccoef(M,inc,unit,ell))
    A=s.Matrix([[0,0],[1,0]]);Aa=T.inv()*(A+a*s.eye(2))*T
    equal(s.trace(Aa)-s.trace(A),2*a)

@case
def further_sampling_quotient_retains_explicit_jet_kernel():
    chi=(S-I)**2*(S-1);q=3;J=jmatrix(chi,q-1)
    equal(J,s.eye(q))
    ev=s.Matrix([[I**j for j in range(q)]])
    v=coeff(S-I,q-1)
    equal(ev*v,s.zeros(1,1));require(v!=s.zeros(q,1),'retained source jet')
    require(ev.rank()==1 and q-ev.rank()==2,'completion kernel dimension')

@case
def holomorphic_schur_extension_retains_parameter_without_conjugating_it():
    z=s.Symbol('z', nonzero=True); eta=R(1,5)
    off=eta*(z+1/z)/2
    Mz=7*s.Matrix([[1,off],[off,1]])
    C=s.Matrix([1,0]);B=s.Matrix([0,1])
    # Stars apply only to the fixed coefficient columns, not to z.
    Gz=C.H*Mz*C-C.H*Mz*B*(B.H*Mz*B).inv()*B.H*Mz*C
    equal(Gz[0],7*(1-eta**2*(z+1/z)**2/4))
    for v in [R(2),I*2,1+I]:
        equal(Gz.subs(z,v)[0],7*(1-eta**2*(v+1/v)**2/4))

@case
def phase_quotient_quadrature_has_its_own_retained_fourier_terms():
    z=s.Symbol('z', nonzero=True);eta=R(1,3)
    p=7*(1-eta**2*(z+1/z)**2/4)
    mean=7*(1-eta**2/2)
    avg2=sum(p.subs(z,a) for a in [1,-1])/2
    avg4=sum(p.subs(z,a) for a in [1,I,-1,-I])/4
    equal(avg4,mean);equal(mean-avg2,7*eta**2/2)
    require(s.simplify(mean-avg2)!=0,'quadrature is not silently exact after quotient')

def negative(name):
    if name=='erase-variance':
        eta=R(1,3);M=7*s.eye(2);J=s.Matrix([[1,0]])
        Ms=[7*s.Matrix([[1,e*eta],[e*eta,1]]) for e in [1,-1]]
        equal(quotient(M,J)[0],sum((quotient(A,J)[0] for A in Ms),s.zeros(1))/2,'false quotient interchange')
    elif name=='support-is-absence':
        require(('ell',0)==('absent',),'false support collapse')
    elif name=='omit-fourier-factor':
        U=s.Matrix([[1,1],[1,-1]]);equal(U.H*U,s.eye(2),'false missing sqrt(m)')
    else:raise ValueError(name)

def main():
    p=argparse.ArgumentParser();p.add_argument('--negative',choices=['erase-variance','support-is-absence','omit-fourier-factor'])
    args=p.parse_args()
    if args.negative:negative(args.negative);raise ArithmeticError('negative control did not reject')
    names=[]
    for fn in CASES:fn();names.append(fn.__name__)
    print(json.dumps({'status':'pass','count':len(names),'methods':names,'scope':'exact finite coefficient and positive-matrix identities; no analytic integral or Lean certification'},indent=2,sort_keys=True))
if __name__=='__main__':main()
