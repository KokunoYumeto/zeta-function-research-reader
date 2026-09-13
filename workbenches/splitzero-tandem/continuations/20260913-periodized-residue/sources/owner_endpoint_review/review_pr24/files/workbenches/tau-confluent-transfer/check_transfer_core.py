#!/usr/bin/env python3
"""Exact public core for the confluent transfer. No zeta-packet claims."""
import argparse
import json
import sys
import unittest
from functools import lru_cache
import sympy as s
x=s.Symbol('x')

def require(ok,msg='exact identity failed'):
    if not bool(ok): raise AssertionError(msg)

def eq(a,b=0):
    if isinstance(a,s.MatrixBase):
        if b==0:b=s.zeros(*a.shape)
        require(a.shape==b.shape,'matrix type mismatch')
        require(all(s.cancel(v)==0 for v in a-b),str(a-b))
    else:require(s.cancel(s.expand(a-b))==0,str(a-b))

def inv(M):return M.inv(method='DM')

class System:
    def __init__(self,roots,mass=7,atomic=False):
        self.roots=roots
        self.psi=s.expand(s.prod((x-z)**m for z,m in roots));self.Pi=s.expand(self.psi**2)
        self.q=s.degree(self.psi,x);self.r=2*self.q
        if atomic:
            nodes=list(range(-9,10));weights=[2+(j*j+3*j)%7 for j in range(19)]
            self.m=[sum(s.Integer(w)*t**d for w,t in zip(weights,nodes)) for d in range(32)]
        else:self.m=[s.Integer(0) if d%2 else s.Integer(mass)*s.factorial2(d-1) for d in range(32)]
        self.p=[s.Integer(1)];self.w=[];self.a=[s.Integer(0)];self.b=[]
        for j in range(13):
            P=self.p[j];norm=self.integral(P*P);require(norm>0)
            self.w.append(norm);self.b.append(self.integral(x*P*P)/norm)
            if j:self.a.append(norm/self.w[j-1])
            if j<12:self.p.append(s.expand((x-self.b[j])*P-self.a[j]*(self.p[j-1] if j else 0)))
        self.rows=[(z,j) for z,m in roots for j in range(2*m)]
        self.V=s.Matrix.hstack(*(self.jet(x**j) for j in range(self.r)))
    def integral(self,P,shift=0):return s.expand(sum(c*self.m[j[0]+shift] for j,c in s.Poly(s.expand(P),x).terms()))
    def H(self,n,weight=1,shift=0):return s.Matrix(n,n,lambda i,j:self.integral(weight*x**(i+j),shift))
    def det(self,n,weight=1):return self.H(n,weight).det(method='domain-ge') if n else s.Integer(1)
    def jet(self,P):return s.Matrix([s.expand(s.diff(P,x,j).subs(x,z)) for z,j in self.rows])
    @lru_cache(None)
    def F(self,n):return s.Matrix.hstack(*(self.jet(self.p[n+j]) for j in range(self.r)))
    @lru_cache(None)
    def d(self,n):return (inv(self.F(n))*self.jet(self.p[n+self.r])).applyfunc(s.cancel)
    def t(self,n):return -self.d(n)[0]
    def Q(self,n):
        P=self.p[n+self.r]-sum(self.d(n)[j]*self.p[n+j] for j in range(self.r))
        Q,R=s.div(s.expand(P),self.Pi,x);eq(R);return s.expand(Q)
    def gram(self,N):
        J=s.Matrix.hstack(*(s.Matrix([s.rem(x**j,self.psi,x).coeff(x,i) for i in range(self.q)]) for j in range(N+1)))
        H=self.H(N+1);K=J*inv(H)*J.T;G=inv(K)
        Kp=-J*inv(H)*self.H(N+1,shift=1)*inv(H)*J.T
        lp=s.cancel(-s.trace(Kp*G))
        T=s.Matrix.hstack(*(s.Matrix([s.rem(x**(j+1),self.psi,x).coeff(x,i) for i in range(self.q)]) for j in range(self.q)))
        A=s.eye(self.q)/2+s.I*T;W=A.conjugate().T*G+G*A-G
        eps=s.cancel(s.trace((inv(G)*W)**2)/2)
        return G,T,lp,eps

@lru_cache(None)
def model(kind='complex'):
    roots={'complex':((s.I,1),(-s.I,1)),'repeated':((0,2),),'mixed':((0,1),(s.I,1),(-s.I,1)),'quartet':((1+s.I,1),(1-s.I,1),(-1+s.I,1),(-1-s.I,1))}[kind]
    return System(roots)

class Checks(unittest.TestCase):
    def test_raw_factorials(self):
        for name in ['complex','repeated','mixed','quartet']:
            z=model(name);d=s.prod(s.factorial(j) for a,m in z.roots for j in range(2*m))
            for i,(a,m) in enumerate(z.roots):
                for b,n in z.roots[i+1:]:d*=(b-a)**(4*m*n)
            eq(z.V.det(method='domain-ge'),d)
    def test_relation_polynomial_and_norm(self):
        for name in ['complex','repeated','mixed']:
            z=model(name)
            for n in range(3):
                Q=z.Q(n);eq(s.Poly(Q,x).LC(),1)
                for j in range(n):eq(z.integral(Q*z.Pi*x**j))
                eq(z.integral(Q*Q*z.Pi),z.w[n]*z.t(n));require(z.t(n)>0)
    def test_discrete_transfer(self):
        z=model()
        for n in range(3):
            K=s.zeros(z.r)
            for j in range(z.r-1):K[j+1,j]=1
            K[:,z.r-1]=z.d(n)
            eq(z.F(n)*K,z.F(n+1));eq(K.det(),z.t(n))
    def test_hankel_identity(self):
        for name in ['complex','repeated','mixed','quartet']:
            z=model(name)
            for n in range(3):eq(z.det(n,z.Pi)/z.det(n),z.F(n).det(method='domain-ge')/z.V.det(method='domain-ge'))
    def test_quotient_volume(self):
        z=model()
        for n in range(3):
            N=n+z.q-1;G=z.gram(N)[0]
            eq(G.det(),s.prod(z.w[j] for j in range(n,n+z.q))*z.V.det()/z.F(n).det())
    def test_norm_gaps(self):
        z=model('mixed')
        for j in range(3):
            gap=z.psi*z.Q(j)-z.p[j+z.q]
            eq(z.integral(gap*gap),z.w[j]*z.t(j)-z.w[j+z.q])
    def test_phase_and_control(self):
        for z in [model(),System(((s.I,1),(-s.I,1)),atomic=True)]:
            n=2;N=n+z.q-1;G,T,lp,eps=z.gram(N)
            phase=sum(z.b[n:n+z.q])+z.a[n]*(inv(z.F(n))*z.jet(z.p[n-1]))[0]
            eq(lp,phase)
            nu0=z.w[n-1]*z.t(n-1);nu1=z.w[n]*z.t(n)
            eq(eps,(nu0-z.w[N])*(nu1-z.w[N+1])/(nu0*z.w[N])-(s.trace(T)-lp)**2)
    def test_mass_and_supported_depth(self):
        z=model();v=System(((s.I,1),(-s.I,1)),mass=21)
        eq(v.t(2),z.t(2));eq(v.gram(3)[0],3*z.gram(3)[0]);eq(v.gram(3)[3],z.gram(3)[3])
        require(s.rem(x**5,x**6,x)!=0);eq(s.rem(x**5,x**5,x),0)
        eq(s.rem(s.diff(x**3,x),x**3,x),3*x*x)
        tau=('absent',);e=('supported',0)
        require(tau!=e)
        def quotient(a):return tau if a==tau else ('supported',s.rem(a[1],x**3,x))
        require(quotient(('supported',x**3))==e and quotient(tau)==tau)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--negative-control',action='store_true');ap.add_argument('--output');args=ap.parse_args()
    if args.negative_control:require(False,'deliberate negative control')
    result=unittest.TextTestRunner(stream=sys.stderr,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    record={'tests_run':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'scope':'exact finite Gaussian/atomic fixtures; not actual zeta packets, interval certificates, or Lean proofs'}
    out=json.dumps(record,indent=2,sort_keys=True)
    if args.output:open(args.output,'w',encoding='utf-8').write(out+'\n')
    print(out);sys.exit(0 if result.wasSuccessful() else 1)
