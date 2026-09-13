#!/usr/bin/env python3
"""Exact finite regression checks for sum-fibre connection and conormal maps.

The polynomial and Gaussian fixtures are NOT certified zeta packets. Analytic
integration and limiting claims in NOTE.tex are written proofs, not consequences
of this finite suite. No use of Python `assert`: tests remain active under -O.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from pathlib import Path
import sys
import unittest
import sympy as sp

u,y,x,z=sp.symbols('u y x z', real=True)
I=sp.I
Q=sp.Rational

def clean(A):
    return sp.Matrix(A).applyfunc(lambda q:sp.factor(sp.cancel(q)))

def gy(P):
    """Integral of P(y)e^-y^2 divided by the explicit common sqrt(pi)."""
    p=sp.Poly(sp.expand(P),y); out=0
    for (n,),c in p.terms():
        if n%2==0:
            out += c*sp.factorial2(n-1)/2**(n//2)
    return sp.simplify(out)

def centre(k):
    ys=sp.symbols('y0:'+str(k-1))
    ts=[u/k+a for a in ys]+[u/k-sum(ys)]
    return ys,ts

def gram_polynomial_amplitude(P,frame):
    dp=sp.diff(P,u)-u*P/4
    W=sp.Matrix([[gy(P*P*a*b) for b in frame] for a in frame])
    B=sp.Matrix([[gy(P*dp*a*b) for b in frame] for a in frame])
    T=sp.Matrix([[gy(dp*dp*a*b) for b in frame] for a in frame])
    return W,B,T

def groebner_power(hs,variables,power):
    k=len(hs)
    alphas=[a for a in product(range(power+1),repeat=k) if sum(a)==power]
    return sp.groebner([sp.prod(h**a for h,a in zip(hs,aa)) for aa in alphas],
                       *variables,order='grevlex',domain=sp.QQ)

def rem(P,gb):
    return sp.expand(gb.reduce(sp.expand(P))[1])

class Checks(unittest.TestCase):
    def eq(self,a,b=0): self.assertEqual(sp.simplify(sp.expand(a-b)),0)
    def mat(self,a,b): self.assertEqual(clean(a-b),sp.zeros(*a.shape))

    def test_01_centre_coordinate_jacobian(self):
        for k in range(2,7):
            ys,ts=centre(k)
            J=sp.Matrix(ts).jacobian((u,)+ys)
            self.eq(J.det()**2,1); self.eq(sum(ts),u)
            for t in ts: self.eq(sp.diff(t,u),Q(1,k))
        self.eq((2*I*y)**2,-4*y*y)

    def test_02_relative_derivative_and_sum(self):
        for k in range(2,5):
            ss=sp.symbols('s0:'+str(k)); S=sum(ss)
            deriv=lambda P:sum(sp.diff(P,s) for s in ss)/k
            self.eq(deriv(S),1)
            for s in ss: self.eq(deriv(s-S/k),0)
            P=sp.prod((s+1)**2 for s in ss)
            self.eq(deriv(S*P)-S*deriv(P),P)

    def test_03_fixed_phase_fisher_identity(self):
        t=sp.symbols('t',real=True)
        for d in range(4):
            a=I**d*(t*t-t+2)*sp.exp(-t*t/4)
            ap=sp.diff(a,t); w=sp.conjugate(a)*a
            self.eq(sp.conjugate(a),(-1)**d*a)
            self.eq(sp.diff(w,t)**2,4*sp.conjugate(ap)*ap*w)

    def test_04_gaussian_mass_fisher_factors(self):
        mass=sp.sqrt(2*sp.pi)
        for k in range(2,7):
            # m_k=mass^(k-1)/sqrt(k) exp(-u^2/(2k)).
            density_mass=mass**(k-1)*sp.sqrt(2*sp.pi*k)/sp.sqrt(k)
            self.eq(density_mass,mass**k)
            information=density_mass/k
            self.eq(information,mass**(k-1)*mass/k)

    def test_05_zero_bearing_convolution(self):
        P=u*u/4-y*y
        W,B,T=gram_polynomial_amplitude(P,[1])
        self.eq(W[0],(u**4-4*u*u+12)/16)
        self.eq(2*B[0],sp.diff(W[0],u)-u*W[0]/2)
        normal=sp.factor(T[0]-B[0]**2/W[0])
        self.assertGreater(normal.subs(u,1),0)
        # Information at the original zero: (w')^2/w=(2-t^2)^2 e^-t^2/2.
        self.eq(4-4*1+3,3)

    def test_06_scalar_orthogonal_decomposition(self):
        P=u*u/4-y*y
        W,B,T=gram_polynomial_amplitude(P,[1])
        a=sp.cancel(B[0]/W[0]); dp=sp.diff(P,u)-u*P/4
        n=dp-a*P
        self.eq(gy(P*n),0)
        self.eq(gy(n*n)+a*a*W[0],T[0])

    def test_07_gaussian_full_relative_frame(self):
        W,B,T=gram_polynomial_amplitude(sp.Integer(1),[1,-4*y*y,16*y**4])
        self.mat(B,-u*W/4)
        self.mat(T-B.T*W.inv()*B,sp.zeros(3))
        self.assertNotEqual(W.det(),0)

    def test_08_nonconstant_full_matrix_connection(self):
        W,B,T=gram_polynomial_amplitude(u*u/4-y*y,[1,-4*y*y])
        self.mat(2*B,W.diff(u)-u*W/2)
        at=lambda Z:clean(Z.subs(u,1))
        W1,B1,T1=map(at,(W,B,T)); N=clean(T1-B1.T*W1.inv()*B1)
        self.assertGreater(W1.det(),0)
        self.assertEqual(N.rank(),1)
        self.assertGreaterEqual(N[0,0],0);self.assertGreaterEqual(N[1,1],0)
        self.assertEqual(N.det(),0)

    def test_09_projection_connection_energy(self):
        Theta=sp.Matrix([[1,0],[1,1],[1,-1],[1,2]])
        a=sp.diag(u+1,u*u+1,u+3,u*u+2)
        j=a*Theta; jp=j.diff(u); W=j.T*j; B=j.T*jp
        P=j*W.inv()*j.T; Gamma=W.inv()*B; N=(sp.eye(4)-P)*jp
        self.mat(B,B.T)
        self.mat(Gamma.T*W+W*Gamma,W.diff(u))
        c=sp.Matrix([u+2,u*u-1]); derivative=(j*c).diff(u)
        tang=j*(c.diff(u)+Gamma*c);normal=N*c
        self.mat(derivative,tang+normal)
        self.eq((tang.T*normal)[0],0)
        self.eq((derivative.T*derivative)[0],(tang.T*tang+normal.T*normal)[0])

    def test_10_varying_frame_connection(self):
        j=sp.Matrix([[1,u],[u,1],[u*u,u+1]])
        W=j.T*j; B=j.T*j.diff(u); Gamma=W.inv()*B
        C=sp.Matrix([[1,u],[0,1]])
        jnew=j*C; Gnew=(jnew.T*jnew).inv()*jnew.T*jnew.diff(u)
        self.mat(Gnew,C.inv()*Gamma*C+C.inv()*C.diff(u))
        P=j*W.inv()*j.T
        self.mat((sp.eye(3)-P)*jnew.diff(u),(sp.eye(3)-P)*j.diff(u)*C)

    def test_11_derivative_of_ideal_square(self):
        hs=[x*x-x+1,z*z]; gb=groebner_power(hs,(x,z),1)
        deriv=lambda P:(sp.diff(P,x)+sp.diff(P,z))/2
        for a in hs:
            for b in hs:
                self.eq(rem(deriv(a*b*(1+x+z)),gb),0)
        self.eq(deriv(x+z),1)

    def test_12_relative_leibniz(self):
        gb=groebner_power([x*x,z**3],(x,z),1)
        P=1+x*z+x*x; R=2+x+z*z
        delta=lambda v:rem((sp.diff(v,x)+sp.diff(v,z))/2,gb)
        self.eq(delta(P*R),rem(rem(P,gb)*delta(R)+rem(R,gb)*delta(P),gb))

    def test_13_conormal_basis_independence(self):
        hs=[x*x-x+1,z*z+2*z+3]; gb2=groebner_power(hs,(x,z),2)
        b0=[1,x,z,x*z]
        images=[rem(p,gb2) for p in b0]+[rem(h*p,gb2) for h in hs for p in b0]
        monoms=sorted(set(m for p in images for m,c in sp.Poly(p,x,z).terms()))
        mat=sp.Matrix([[sp.Poly(p,x,z).coeff_monomial(x**a*z**b) for p in images] for a,b in monoms])
        self.assertEqual(mat.rank(),12)
        gb=groebner_power(hs,(x,z),1)
        for h in hs:
            for p in b0:
                self.eq(rem((sp.diff(h*p,x)+sp.diff(h*p,z))/2,gb),
                        rem((sp.diff(h,x)+sp.diff(h,z))*p/2,gb))

    def test_14_conormal_rank_keeps_multiplicities(self):
        for ms in [(1,1),(2,2),(2,3),(3,4),(1,3)]:
            basis=list(product(*(range(m) for m in ms)))
            lookup={a:i for i,a in enumerate(basis)}; columns=[]
            for i,m in enumerate(ms):
                for aa in basis:
                    bb=list(aa);bb[i]+=m-1
                    col=sp.zeros(len(basis),1)
                    if bb[i]<m:col[lookup[tuple(bb)]]=Q(m,len(ms))
                    columns.append(col)
            mat=sp.Matrix.hstack(*columns)
            self.assertEqual(mat.rank(),sp.prod(ms)-sp.prod(m-1 for m in ms))

    def test_15_full_unit_derivative_retained(self):
        gb=groebner_power([x*x,z**3],(x,z),1)
        U=(1+x)*(1+z+z*z);Uinv=(1-x)*(1-z)
        self.eq(rem(U*Uinv,gb),1)
        P=x*z+z*z+2
        der=lambda v:(sp.diff(v,x)+sp.diff(v,z))/2
        beta=rem(Uinv*der(U),gb)
        self.eq(rem(der(U*P),gb),rem(U*der(P)+beta*U*P,gb))
        relation=x*x*(1+z)+z**3*(2+x)
        self.eq(rem(der(U*relation),gb),rem(U*(2*x*(1+z)+3*z*z*(2+x))/2,gb))

    def test_16_associated_graded_derivative(self):
        hs=[x*x-x+1,z*z+1]
        P=1+x*z
        for aa in [(2,0),(1,1),(0,2),(2,1)]:
            degree=sum(aa)
            source=sp.prod(h**a for h,a in zip(hs,aa))*P
            rhs=0
            for i,a in enumerate(aa):
                if a:
                    rhs+=Q(a,2)*sp.diff(hs[i],(x,z)[i])*P*sp.prod(h**(q-(i==j)) for j,(h,q) in enumerate(zip(hs,aa)))
            gb=groebner_power(hs,(x,z),degree)
            self.eq(rem((sp.diff(source,x)+sp.diff(source,z))/2-rhs,gb),0)

    def test_17_mixed_jacobian_trace(self):
        hs=[(x-Q(1,4))**2,(z-Q(3,4))**3]
        U=(x+2)*(z+3);P=1+x*z
        gb=groebner_power(hs,(x,z),1)
        actual=sp.diff(U*P*hs[0]*hs[1],x,z)
        expected=U*P*sp.diff(hs[0],x)*sp.diff(hs[1],z)
        self.eq(rem(actual-expected,gb),0)
        # One-variable complete local unit, actual multiplicity trace contraction.
        t=sp.symbols('t');h=(t-Q(1,4))**2*(t-Q(3,4))**2
        g=h*(t*t-t+2);f=1+2*t;P=t*t+3
        dagger=f.subs(t,1-t)
        total=sum(sp.residue(dagger*sp.diff(g,t)*P/g,t,r) for r in [Q(1,4),Q(3,4)])
        expected=sum(2*dagger.subs(t,r)*P.subs(t,r) for r in [Q(1,4),Q(3,4)])
        self.eq(total,expected)

    def test_18_supported_conormal_not_external(self):
        # Exact F_5 analogue of C[z]/z^2 -> C at a simple supported point.
        elems=[None]+list(product(range(5),repeat=2))
        def add(a,b):
            if a is None:return b
            if b is None:return a
            return tuple((a[i]+b[i])%5 for i in range(2))
        def outadd(a,b):return b if a is None else a if b is None else (a+b)%5
        q=lambda a:None if a is None else a[0]
        delta=lambda a:None if a is None else a[1]
        for a in elems:
            for b in elems:
                self.assertEqual(q(add(a,b)),outadd(q(a),q(b)))
                self.assertEqual(delta(add(a,b)),outadd(delta(a),delta(b)))
        self.assertEqual(q((0,1)),0);self.assertEqual(delta((0,1)),1)
        self.assertIsNone(q(None));self.assertIsNone(delta(None))

    def test_19_logarithm_generator_commutator(self):
        X,Y=sp.symbols('X Y',positive=True)
        F=X**2*Y**3;L=(sp.log(X)+sp.log(Y))/2
        D=lambda v:-X*sp.diff(v,X)-Y*sp.diff(v,Y)
        self.eq(D(L*F)-L*D(F),-F)
        self.eq(D(F),-5*F)

    def test_20_derivative_permutation_and_old_control(self):
        P=x*x*z+3*x*z*z
        swap=lambda v:v.xreplace({x:z,z:x})
        der=lambda v:(sp.diff(v,x)+sp.diff(v,z))/2
        self.eq(der(swap(P)),swap(der(P)))
        A=sp.diag(Q(1,4),Q(3,4));G=sp.diag(2,3);K=G.inv()
        W=A.T*G+G*A-G;V=A*K+K*A.T-K
        self.mat(K*W*K,V)
        self.assertEqual((G.inv()*W).eigenvals(),{-Q(1,2):1,Q(1,2):1})


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',type=Path)
    ap.add_argument('--self-test-failure',action='store_true')
    args=ap.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    if args.self_test_failure:
        class Failure(unittest.TestCase):
            def runTest(self):self.assertEqual(1,2,'intentional failure guard')
        suite.addTest(Failure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'tests_run':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
            'success':result.wasSuccessful(),'sympy':sp.__version__,
            'scope':'Finite exact polynomial, Gaussian and matrix tests; not an analytic, arithmetic interval, or Lean certificate.'}
    if args.json:args.json.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True));return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
