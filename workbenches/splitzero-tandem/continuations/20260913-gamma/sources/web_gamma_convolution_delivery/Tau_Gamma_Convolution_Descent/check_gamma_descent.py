#!/usr/bin/env python3
"""Exact finite calibrations; not zeta-zero, analytic-integral, or Lean certificates.
The mass argument is retained. moment_factor is the coefficient in moment=mass*factor.
Explicit guards remain active under python -O.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json, math, sys, unittest
from pathlib import Path
import sympy as s
x,z,S=s.symbols('x z S',real=True)

def require(c,m='failed exact check'):
    if not c: raise RuntimeError(m)

def equal(a,b,m='exact equality'):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        d=s.Matrix(a)-s.Matrix(b)
        require(all(s.simplify(v)==0 for v in d),m+': '+str(d))
    else: require(s.simplify(s.expand(a-b))==0,m+': '+str(a-b))

@lru_cache(None)
def poly(alpha,n):
    if n==0:return s.Integer(1)
    if n==1:return x
    return s.expand(x*poly(alpha,n-1)-(n-1)*(n+alpha-2)*poly(alpha,n-2))

@lru_cache(None)
def moment_factor(alpha,n):
    if n==0:return s.Integer(1)
    if n%2:return s.Integer(0)
    p=s.Poly(poly(alpha,n),x)
    return s.expand(-sum(p.nth(j)*moment_factor(alpha,j) for j in range(n)))

def integral(p,alpha,mass=1):
    return s.expand(mass*sum(c*moment_factor(alpha,a[0]) for a,c in s.Poly(s.expand(p),x).terms()))

def joint_integral(p,vs,alpha,mass):
    return s.expand(mass**len(vs)*sum(c*s.prod(moment_factor(alpha,j) for j in a)
                 for a,c in s.Poly(s.expand(p),*vs).terms()))

def compositions(n,k):
    if k==1:yield (n,)
    else:
        for j in range(n+1):
            for rest in compositions(n-j,k-1):yield (j,)+rest

def multinomial(a):
    return s.Integer(math.factorial(sum(a))//math.prod(math.factorial(j) for j in a))

def coeffs(B,alpha):
    return [s.cancel(integral(B*poly(alpha,j),alpha)/(s.factorial(j)*s.rf(alpha,j)))
            for j in range(int(s.degree(B,x))+1)]

def projected(B,alpha,k):
    cs=coeffs(B,alpha)
    ser=s.Poly(s.expand(sum(cs[j]*s.rf(alpha,j)*z**j for j in range(len(cs)))**k),z)
    return s.expand(sum(ser.nth(n)/s.rf(k*alpha,n)*poly(k*alpha,n) for n in range(ser.degree()+1)))

def conv_moment(B,alpha,k,n,mass):
    one=[integral(B*x**j,alpha,mass) for j in range(n+1)]
    return s.expand(sum(multinomial(a)*s.prod(one[j] for j in a) for a in compositions(n,k)))

def gram(alpha,k,N,B,mass):
    c=s.Rational(k,2)
    return s.Matrix(N+1,N+1,lambda i,j:integral((c-s.I*x)**i*(c+s.I*x)**j*B,k*alpha,mass**k))

def quotient(M,chi,N):
    q=int(s.degree(chi,S))
    if q==0:return s.zeros(0),s.zeros(0,N+1),s.zeros(N+1,0),s.eye(N+1)
    J=s.Matrix(q,N+1,lambda i,j:s.Poly(s.rem(S**j,chi,S),S).nth(i))
    B=s.Matrix(N+1,max(0,N-q+1),lambda i,j:s.Poly(chi*S**j,S).nth(i))
    G=(J*M.inv()*J.conjugate().T).inv();R=M.inv()*J.conjugate().T*G
    return G,J,R,B

def psd(M):
    import itertools
    require(M==M.conjugate().T,'Hermitian input')
    for r in range(1,M.rows+1):
        for inds in itertools.combinations(range(M.rows),r):
            d=s.simplify(M.extract(inds,inds).det())
            require(d.is_nonnegative is True,'nonnegative principal minor: '+str(d))

class GammaDescent(unittest.TestCase):
    def test_01_literal_gamma_mass(self):
        for lam in [s.Rational(1,4),s.Rational(1,2),s.Integer(1)]:
            c=2**(1-2*lam)*s.gamma(2*lam)
            for k in range(1,6):
                ck=2**(1-2*k*lam)*s.gamma(2*k*lam)
                kap=2**(k-1)*s.gamma(2*lam)**k/s.gamma(2*k*lam)
                equal(kap*ck,c**k)
    def test_02_norms_with_mass(self):
        mass=s.Symbol('c_lambda',positive=True)
        for a in [s.Rational(1,2),s.Rational(3,2),s.Integer(3)]:
            for i in range(6):
                for j in range(6):
                    equal(integral(poly(a,i)*poly(a,j),a,mass),mass*s.factorial(i)*s.rf(a,i) if i==j else 0)
    def test_03_full_addition(self):
        a=s.Rational(1,2)
        for k,nmax in [(2,7),(3,5)]:
            vs=s.symbols('t:'+str(k),real=True)
            for n in range(nmax+1):
                rhs=sum(multinomial(idx)*s.prod(poly(a,j).subs(x,v) for j,v in zip(idx,vs)) for idx in compositions(n,k))
                equal(poly(k*a,n).subs(x,sum(vs)),rhs)
    def test_04_projection_pairings(self):
        a=s.Rational(3,2);mass=7
        for idx in [(0,0),(1,0),(1,1),(2,1),(2,0,1)]:
            k=len(idx);n=sum(idx);vs=s.symbols('t:'+str(k),real=True)
            p=s.prod(poly(a,j).subs(x,v) for j,v in zip(idx,vs))
            c=s.prod(s.rf(a,j) for j in idx)/s.rf(k*a,n)
            for m in range(n+3):
                equal(joint_integral(p*poly(k*a,m).subs(x,sum(vs)),vs,a,mass),
                      integral(c*poly(k*a,n)*poly(k*a,m),k*a,mass**k))
    def test_05_normal_norm(self):
        a=s.Rational(1,2);mass=5
        for idx in [(3,),(0,0),(1,0),(1,1),(2,1),(1,0,1)]:
            k=len(idx);n=sum(idx);vs=s.symbols('t:'+str(k),real=True)
            c=s.prod(s.rf(a,j) for j in idx)/s.rf(k*a,n)
            p=s.prod(poly(a,j).subs(x,v) for j,v in zip(idx,vs))
            residual=p-c*poly(k*a,n).subs(x,sum(vs))
            rhs=mass**k*(s.prod(s.factorial(j)*s.rf(a,j) for j in idx)-s.factorial(n)*s.prod(s.rf(a,j)**2 for j in idx)/s.rf(k*a,n))
            equal(joint_integral(residual**2,vs,a,mass),rhs);require(rhs>=0)
    def test_06_coefficient_transform(self):
        a=s.Rational(1,2);mass=3
        for B in [1+x*x,2+x+x*x]:
            for k in [1,2,3]:
                C=projected(B,a,k)
                for n in range(7):equal(integral(x**n*C,k*a,mass**k),conv_moment(B,a,k,n,mass))
    def test_07_mass_not_replaced(self):
        a=s.Rational(3,2);mass=s.Symbol('literal_mass',positive=True);B=2+x+x*x
        for k in [2,3,4]:equal(integral(projected(B,a,k),k*a,mass**k),integral(B,a,mass)**k)
    def test_08_finite_moment_exactness(self):
        a=s.Rational(1,2);B=1+x*x+x**4;cs=coeffs(B,a);BL=sum(cs[j]*poly(a,j) for j in range(3))
        for k in [2,3]:
            full=projected(B,a,k);trunc=projected(BL,a,k)
            for j in range(3):equal(integral(x**j*(full-trunc),k*a,5**k),0)
            require(s.simplify(integral(x**4*(full-trunc),k*a,5**k))!=0,'retain omitted moment')
    def test_09_amplitude_phase(self):
        a=s.Rational(1,2);mass=3;k=2;t1,t2=s.symbols('t1 t2',real=True)
        amp=(t1+s.I)*(t2+s.I);P=2+(1+s.I)*(1+s.I*(t1+t2));Q=(1+s.I*(t1+t2))**2-s.I
        lhs=joint_integral(s.conjugate(amp*P)*amp*Q,(t1,t2),a,mass)
        rhs=integral(s.conjugate(2+(1+s.I)*(1+s.I*x))*((1+s.I*x)**2-s.I)*projected(1+x*x,a,k),2*a,mass**2)
        equal(lhs,rhs)
    def test_10_tilted_reference_determinants(self):
        X=s.symbols('tan_theta',real=True)
        for a in [s.Rational(1,2),s.Integer(3)]:
            f=[s.Integer(1)]
            for j in range(8):f.append(s.expand((1+X*X)*s.diff(f[-1],X)+a*X*f[-1]))
            for n in range(1,5):
                for value in [s.Integer(0),s.Rational(1,3)]:
                    M=s.Matrix(n,n,lambda i,j:7*f[i+j].subs(X,value))
                    equal(M.det(),7**n*s.prod(s.factorial(j)*s.rf(a,j) for j in range(n))*(1+value**2)**(n*(n-1)//2))
    def test_11_source_boundary_factorization(self):
        a=s.Rational(1,2);k=2;mass=3;Bk=projected(1+x*x,a,k);chi=(S-1)**2-s.Rational(1,4);vals={}
        for N in [1,2,3,4]:
            Mh=gram(a,k,N,Bk,mass);Mr=gram(a,k,N,s.Integer(1),mass)
            Gh,J,Rh,B=quotient(Mh,chi,N);Gr,Jr,Rr,Br=quotient(Mr,chi,N)
            Dh=Mh.det();Dr=Mr.det();Bh=(B.conjugate().T*Mh*B).det();Brd=(B.conjugate().T*Mr*B).det()
            equal(Gh.det(),Dh/Bh);equal(Gh.det()/Gr.det(),(Dh/Dr)/(Bh/Brd))
            Rc=Rr-B*(B.conjugate().T*Mh*B).inv()*B.conjugate().T*Mh*Rr if B.cols else Rr
            equal(Rc,Rh);equal(J*Rc,s.eye(2));vals[N]=(Dh,Dr)
        D2,D3,D4=(vals[n][0] for n in [1,2,3]);R2,R3,R4=(vals[n][1] for n in [1,2,3])
        equal(D4*D2/D3**2,3*(3+k*a-1)*(D4/R4)*(D2/R2)/(D3/R3)**2)
    def test_12_quotient_metric_upper(self):
        Mr=s.diag(2,3,5,7);Mh=s.Matrix([[2,1,0,0],[1,4,1,0],[0,1,5,1],[0,0,1,6]])
        psd(Mh);psd(3*Mr-Mh);J=s.Matrix([[1,0,1,2],[0,1,-1,1]])
        Gh=(J*Mh.inv()*J.T).inv();Gr=(J*Mr.inv()*J.T).inv();psd(3*Gr-Gh)
        require(s.simplify(Gh.det()/Gr.det())<=9,'quotient dimension exponent')
    def test_13_seed_bound_factors(self):
        q=(x*x+s.Rational(25,4))*(x*x+s.Rational(81,4))-(x*x+s.Rational(1,4))**2
        require(all(c>=0 for c in s.Poly(s.expand(q),x).all_coeffs()))
        shifted=s.prod((j+s.Rational(1,4))**2+x*x/4 for j in range(3))
        equal(shifted,s.Rational(1,64)*(x*x+s.Rational(1,4))*(x*x+s.Rational(25,4))*(x*x+s.Rational(81,4)))
    def test_14_supported_relation(self):
        chi=(S-1)**2+s.Rational(3,2);absent=('tau',None)
        def q(v):
            if v==absent:return absent
            label,p=v;return (label,s.rem(p,chi,S))
        v=('V_3',s.expand(chi*(S+2)))
        require(v[1]!=0);require(q(v)==('V_3',0));require(q(absent)==absent)
        require(q(v)!=absent);require(q(('V_4',0))!=q(v))
    def test_15_empty_packet(self):
        M=gram(s.Rational(1,2),2,3,s.Integer(1),3)
        G,J,R,B=quotient(M,s.Integer(1),3)
        require(G.shape==(0,0) and G.det()==1);equal(B,s.eye(4));equal(M.det()/(B.T*M*B).det(),1);require(M[0,0]==9)
    def test_16_density_pythagoras(self):
        a=s.Rational(1,2);mass=3;k=3;B=1+x+x*x;vs=s.symbols('t:3',real=True)
        full=s.prod(B.subs(x,v) for v in vs);C=projected(B,a,k)
        lhs=joint_integral((full-C.subs(x,sum(vs)))**2,vs,a,mass)
        rhs=integral(B*B,a,mass)**k-integral(C*C,k*a,mass**k)
        equal(lhs,rhs);require(rhs>=0)
    def test_17_source_finite_closure(self):
        a=s.Rational(3,2);mass=2;k=2;B=1+x*x+x**6;cs=coeffs(B,a)
        BL=sum(cs[j]*poly(a,j) for j in range(5))
        equal(gram(a,k,2,projected(B,a,k),mass),gram(a,k,2,projected(BL,a,k),mass))

def main():
    p=argparse.ArgumentParser();p.add_argument('--json',type=Path);p.add_argument('--fail-control',action='store_true');args=p.parse_args()
    if args.fail_control:require(False,'deliberately false exact equality')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(GammaDescent))
    rec={'status':'passed' if result.wasSuccessful() else 'failed','test_methods':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'scope':'exact polynomial/matrix calibrations; no arithmetic quadrature, Lean or RH certificate','sympy':s.__version__}
    if args.json:args.json.write_text(json.dumps(rec,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
