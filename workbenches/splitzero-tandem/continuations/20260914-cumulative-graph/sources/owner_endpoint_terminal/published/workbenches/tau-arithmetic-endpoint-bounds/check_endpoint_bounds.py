#!/usr/bin/env python3
"""Exact finite regressions, not a certificate of the analytic estimates.

Declared fixtures use unnormalized Laplace convolution moments. No listed
polynomial or root is asserted to be an arithmetic zeta packet.
"""
from __future__ import annotations
import argparse
import json
import math
import sys
import unittest
from functools import lru_cache
from pathlib import Path
import sympy as sp

u, S = sp.symbols('u S', real=True)


def ck(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def eq(x, y) -> None:
    if isinstance(x, sp.MatrixBase) or isinstance(y, sp.MatrixBase):
        d = sp.Matrix(x) - sp.Matrix(y)
        ck(all(sp.simplify(z) == 0 for z in d), f'matrix mismatch: {d}')
    else:
        ck(sp.simplify(x-y) == 0, f'mismatch: {x} versus {y}')


def laplace_moment(j: int, k: int = 3, amplitude: int = 1):
    if j < 0 or k < 1:
        raise ValueError('nonnegative order and positive tensor degree required')
    if j % 2:
        return sp.S.Zero
    a = j // 2
    return sp.Integer(2 * amplitude) ** k * sp.factorial(2*a) * sp.binomial(k+a-1, a)


def inner(p, q, k: int = 3, amplitude: int = 1):
    pp = sp.Poly(sp.expand(sp.conjugate(p)*q), u)
    return sum(c*laplace_moment(j[0], k, amplitude) for j,c in pp.terms())


@lru_cache(None)
def orthogonal(max_degree: int, k: int = 3, amplitude: int = 1):
    polynomials=[]; norms=[]
    for n in range(max_degree+1):
        p=u**n
        for v,h in zip(polynomials,norms):
            p -= inner(v,u**n,k,amplitude)/h*v
        p=sp.expand(p)
        polynomials.append(p)
        norms.append(sp.factor(inner(p,p,k,amplitude)))
    return tuple(polynomials),tuple(norms)


def col(p,n):
    return sp.Matrix([sp.expand(p).coeff(u,j) for j in range(n+1)])


def moment_matrix(n,k=3,amplitude=1):
    return sp.Matrix(n+1,n+1,lambda i,j:laplace_moment(i+j,k,amplitude))


@lru_cache(None)
def quotient(n, chi_expr=u**2+1, k=3):
    chi=sp.Poly(chi_expr,u); q=chi.degree()
    if n<q-1:
        raise ValueError('degree does not surject to quotient')
    if q==0:
        return sp.zeros(n+1,0),sp.zeros(0,0),sp.zeros(0,n+1)
    J=sp.Matrix.hstack(*[col(sp.rem(u**i,chi.as_expr(),u),q-1) for i in range(n+1)])
    M=moment_matrix(n,k)
    K=J*M.inv()*J.T
    G=K.inv()
    R=M.inv()*J.T*G
    return R,G,J


def norm_legendre(n,L):
    return sp.Rational(2,2*n+1)*L**(2*n+1)*(sp.Rational(2)**n*sp.factorial(n)**2/sp.factorial(2*n))**2


class EndpointTests(unittest.TestCase):
    def test_01_ellipse_and_nonzero_anchor(self):
        r=(3+sp.sqrt(13))/2
        eq(r-1/r,3)
        eq((-sp.I*r+1/(-sp.I*r))/2,-3*sp.I/2)
        eq(sp.Rational(1,2)+sp.I*(-3*sp.I/2),2)
        eq((sp.Rational(8)+sp.Rational(1,8))/2,sp.Rational(65,16))
        eq((sp.Rational(8)-sp.Rational(1,8))/2,sp.Rational(63,16))
        ck(bool(r<4),'middle radius bound')

    def test_02_lipschitz_interval_mass_algebra(self):
        for M in [sp.Rational(1),sp.Rational(7,3),sp.Rational(10)]:
            for ratio in [sp.Rational(1,8),sp.Rational(1,2),sp.Rational(1)]:
                m=M*ratio; length=m/(2*M)
                eq(length*(m/2)**2,m**3/(8*M))
                ck(bool(length<=sp.Rational(1,2)),'one-sided interval fits')

    def test_03_legendre_exact_minimum_norms(self):
        for n in range(8):
            for L in [sp.Rational(1),sp.Rational(3,2)]:
                pn=sp.legendre(n,u/L)*L**n*2**n*sp.factorial(n)**2/sp.factorial(2*n)
                eq(sp.Poly(pn,u).LC(),1)
                integral=sp.integrate(sp.expand(pn**2),(u,-L,L))
                eq(integral,norm_legendre(n,L))
                low=sp.Rational(2,2*n+1)*L**(2*n+1)/4**n
                ck(bool(integral>=low),'central-binomial lower estimate')

    def test_04_legendre_orthogonal_phase_and_error(self):
        for n in range(1,5):
            L=sp.Rational(2)
            pn=sp.legendre(n,u/L)*L**n*2**n*sp.factorial(n)**2/sp.factorial(2*n)
            q=sp.I**n*pn+(1+sp.I)*sum(u**j for j in range(n))
            diff=q-sp.I**n*pn
            eq(sp.integrate(sp.expand(sp.conjugate(q)*q),(u,-L,L)),
               norm_legendre(n,L)+sp.integrate(sp.expand(sp.conjugate(diff)*diff),(u,-L,L)))

    def test_05_original_scaling_coordinate(self):
        for k in [3,4,7]:
            c=sp.Rational(k,2); P=S**4+(1+sp.I)*S**2+2
            f=P.subs(S,c+sp.I*u)
            eq(sp.diff(f,u),sp.I*sp.diff(P,S).subs(S,c+sp.I*u))
            eq(sp.expand(f).coeff(u,4),sp.I**4)
            eq((S*P).subs(S,c+sp.I*u),(c+sp.I*u)*f)

    def test_06_unnormalized_convolution_moments(self):
        z=sp.symbols('z')
        for k in range(1,5):
            series=sp.series((2/(1-z*z))**k,z,0,12).removeO()
            for j in range(10):
                eq(sp.expand(series).coeff(z,j)*sp.factorial(j),laplace_moment(j,k))
            eq(laplace_moment(0,k),2**k)

    def test_07_laplace_third_convolution_and_mass(self):
        x=sp.symbols('x',nonnegative=True)
        m3=(x*x+3*x+3)*sp.exp(-x)/2
        eq(2*sp.integrate(m3,(x,0,sp.oo)),8)
        for j in [0,2,4,6]:
            eq(2*sp.integrate(x**j*m3,(x,0,sp.oo)),laplace_moment(j,3))
        ck(all(c>=0 for c in sp.Poly((x*x+3*x+3)/2-sp.Rational(3,2),x).all_coeffs()),'positive remainder')

    def test_08_exact_fixture_norm_envelopes(self):
        for n,k in [(3,3),(4,3),(4,4)]:
            _,norms=orthogonal(2*n,k)
            lower=norm_legendre(n,sp.Integer(n))*sp.Rational(1,3)**(n+k)
            ck(bool(norms[n]>=lower),'declared Laplace lower envelope')
            upper=sp.factorial(4*n)*2**(4*n)*2*sp.Rational(8,3)**k
            ck(bool(norms[2*n]<=upper),'Laplace exponential upper bound')

    def test_09_factorial_degree_budget(self):
        for n in range(1,15):
            expr=sp.factorial(4*n)/norm_legendre(n,sp.Integer(n))
            ck(bool(expr<=(64*n)**(2*n)),'factorial and monic-norm part')

    def test_10_mass_scaling_retains_then_cancels(self):
        p,h=orthogonal(6,3,1)
        p7,h7=orthogonal(6,3,7)
        for a,b in zip(p,p7): eq(a,b)
        for a,b in zip(h,h7): eq(b,7**3*a)
        eq(h7[6]/h7[3],h[6]/h[3])
        ck(h7[0]!=1,'mass not assigned one')

    def test_11_original_relation_and_leading_maps(self):
        chi=u**2+1
        for n in range(2,6):
            p=u**(n-2)+2
            eq(sp.rem(chi*p,chi,u),0)
            eq(sp.Poly(chi*p,u).LC(),sp.Poly(p,u).LC())
        for n in [1,2,3,4]:
            R,G,J=quotient(n)
            eq(J*R,sp.eye(2)); eq(R.T*moment_matrix(n)*R,G)

    def test_12_block_relation_gram_and_update(self):
        i,j=2,5
        Ri,Gi,Ji=quotient(i); Rj,Gj,Jj=quotient(j)
        Ri=Ri.col_join(sp.zeros(j-i,2))
        pol,norm=orthogonal(j)
        T=sp.Matrix.hstack(*[col(pol[a],j) for a in range(i+1,j+1)])
        F=Jj*T; Om=sp.diag(*norm[i+1:j+1]); M=moment_matrix(j)
        B=T-Ri*F; H=Om+F.T*Gi*F
        eq(Jj*B,sp.zeros(2,j-i))
        eq(B.T*M*B,H); eq(B.T*M*Ri,-F.T*Gi)
        eq(Rj,Ri+B*H.inv()*F.T*Gi)
        eq(Gj,Gi-Gi*F*H.inv()*F.T*Gi)
        eq(Gi.det()/Gj.det(),(sp.eye(j-i)+Om.inv()*F.T*Gi*F).det())

    def test_13_four_endpoint_blocks(self):
        q=2; pol,norm=orthogonal(2*q)
        ratios=[]
        for i,j in [(q-1,2*q-1),(q,2*q)]:
            Ri,Gi,Ji=quotient(i); Rj,Gj,Jj=quotient(j)
            F=sp.Matrix.hstack(*[Jj*col(pol[a],j) for a in range(i+1,j+1)])
            Om=sp.diag(*norm[i+1:j+1])
            ratios.append((sp.eye(j-i)+Om.inv()*F.T*Gi*F).det())
        _,G0,_=quotient(q-1); _,G1,_=quotient(q)
        _,G2,_=quotient(2*q-1); _,G3,_=quotient(2*q)
        eq(ratios[0]*ratios[1],G0.det()*G1.det()/(G2.det()*G3.det()))

    def test_14_raw_confluent_transfer_volume(self):
        pol,norm=orthogonal(7)
        roots=[sp.I,-sp.I]
        def jets(p):
            return sp.Matrix([sp.expand(sp.diff(p,u,j).subs(u,z)) for z in roots for j in [0,1]])
        V=sp.Matrix.hstack(*[jets(u**j) for j in range(4)])
        Fs={a:sp.Matrix.hstack(*[jets(pol[j]) for j in range(a,a+4)]) for a in range(4)}
        for N in [1,2,3,4]:
            a=N-1; _,G,_=quotient(N)
            eq(G.det(),sp.prod(norm[j] for j in range(a,a+2))*V.det()/Fs[a].det())

    def test_15_endpoint_product_telescopes(self):
        omega=[sp.Rational(j*j+3,j+1) for j in range(15)]
        V=[sp.Rational(1,(j+1)*(j+2)) for j in range(15)]
        for n,r in [(2,1),(2,4),(4,5)]:
            eq(sp.prod(omega[j+1]/omega[j] for j in range(n,n+r)),omega[n+r]/omega[n])
            eq(sp.prod(V[j-1]/V[j+1] for j in range(n,n+r)),V[n-1]*V[n]/(V[n+r-1]*V[n+r]))

    def test_16_quartet_dimension_and_trace(self):
        delta=sp.Rational(1,5)
        for k in range(3,9):
            for mult in [1,2,3]:
                ell=1+k*(mult-1); q=ell*(k+1)**2
                L=sum(ell*2*delta*(2*a-k) for a in range(k+1) for _b in range(k+1) if 2*a>k)
                eq(L,2*delta*ell*(k+1)*((k+1)**2//4))
                ck(bool(L/q>=delta*k/2),'aggregate lower bound')
                ck(q>=k,'admitted q-window')

    def test_17_supported_relation_maps(self):
        # One supplied support fibre, plus external absence; coefficient model only.
        tau=None; chi=u**2+1
        def quotient_split(x):
            return tau if x is tau else sp.rem(x,chi,u)
        def add(x,y):
            return y if x is tau else x if y is tau else sp.expand(x+y)
        for x in [tau,sp.S.Zero,sp.S.One,u,chi,u*chi]:
            for y in [tau,sp.S.Zero,u+1]:
                eq_or_none=lambda a,b: self.assertIs(a,b) if a is None or b is None else eq(a,b)
                eq_or_none(quotient_split(add(x,y)),add(quotient_split(x),quotient_split(y)))
        self.assertIs(quotient_split(tau),None)
        eq(quotient_split(chi),0)
        self.assertIsNot(quotient_split(chi),None)

    def test_18_empty_packet_keeps_analytic_mass(self):
        R,G,J=quotient(2,sp.Integer(1))
        self.assertEqual(G.shape,(0,0)); eq(G.det(),1)
        ck(laplace_moment(0,3)==8,'analytic fixture mass persists')
        ck(None!=sp.S.Zero,'external and supported zero remain distinct')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fail-control',action='store_true')
    args=parser.parse_args()
    if args.fail_control:
        ck(False,'intentional verification-control failure')
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(EndpointTests)
    names=[t.id().split('.')[-1] for t in suite]
    result=unittest.TestResult(); suite.run(result)
    payload={'status':'PASS' if result.wasSuccessful() else 'FAIL','methods':result.testsRun,
             'tests':names,'failures':[{'test':str(t),'traceback':msg} for t,msg in result.failures],
             'errors':[{'test':str(t),'traceback':msg} for t,msg in result.errors],
             'scope':'exact finite algebraic fixtures; not analytic sampling or a Lean certificate'}
    print(json.dumps(payload,indent=2,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
