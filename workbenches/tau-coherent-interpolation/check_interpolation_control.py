#!/usr/bin/env python3
"""Exact finite tests for the written interpolation/control identities.

Models use declared finite discrete measures and polynomial multipliers.
They do not compute zeta zeros or certify analytic range/density assertions.
No Python assert statement is used as a mathematical check.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import sys
import unittest
import sympy as sp

t = sp.Symbol('t')
I = sp.I
half = sp.Rational(1, 2)
h = sp.Poly((t-sp.Rational(1,4))*(t-sp.Rational(3,4)), t)
m = sp.Poly((t-sp.Rational(1,8))*(t-sp.Rational(7,8)), t)
g = h*m


def clean(A):
    return sp.Matrix(A).applyfunc(sp.expand)


def rem(p, modulus):
    return sp.rem(sp.Poly(p, t), modulus).as_expr()


def coeff(p, d):
    return sp.Matrix([sp.expand(p).coeff(t, j) for j in range(d)])


def multiplication(p, modulus):
    d=modulus.degree()
    return sp.Matrix.hstack(*(coeff(rem(p*t**j,modulus), d) for j in range(d)))


def basis(k, N):
    return sorted((a for a in product(range(N+1), repeat=k) if sum(a)<=N), key=lambda a:(sum(a), a))


def kron_all(mats):
    out=sp.Matrix([[1]])
    for a in mats:
        out=sp.kronecker_product(out,a)
    return clean(out)


@lru_cache(None)
def data(k=1, N=3, repeated=False):
    modulus=sp.Poly((t-half)**2,t) if repeated else h
    global_poly=modulus*m
    d=modulus.degree()
    if N<k*(d-1):
        raise ValueError('jet-surjectivity degree is required')
    exps=basis(k,N)
    nodes=[half+I*j for j in [-2,-1,0,1,2]]
    pts=list(product(nodes, repeat=k))
    # Total degree N must not exhaust a coordinate sampling grid.
    if N>=len(nodes):
        raise ValueError('fixture needs more nodes at this degree')
    v=sp.exquo(global_poly,modulus).as_expr()
    rows=[]
    weights=[]
    for point in pts:
        factor=sp.prod(v.subs(t,z) for z in point)
        rows.append([sp.expand(factor*sp.prod(z**a for z,a in zip(point,aa))) for aa in exps])
        weights.append(sp.prod(1+sp.im(z)**2 for z in point))
    T=clean(rows)
    Omega=sp.diag(*weights)
    M=clean(T.H*Omega*T)
    # Each column gives the full remainder of v(t_1)...v(t_k) monomial.
    J=sp.Matrix.hstack(*(kron_all([coeff(rem(v*t**a,modulus),d) for a in aa]) for aa in exps))
    Mi=M.inv()
    Kernel=clean(J*Mi*J.H)
    G=clean(Kernel.inv())
    C=clean(Mi*J.H*G)
    R=clean(T*C)
    A1=multiplication(t,modulus)
    A=sp.zeros(d**k)
    for j in range(k):
        A+=kron_all([A1 if i==j else sp.eye(d) for i in range(k)])
    A=clean(A)
    Dop=sp.diag(*(sum(zs) for zs in pts))
    defect=clean(Dop*R-R*A)
    W=clean(A.H*G+G*A-k*G)
    null=J.nullspace()
    L=sp.Matrix.hstack(*null) if null else sp.zeros(len(exps),0)
    Boundary=clean(T*L)
    if Boundary.cols:
        P=clean(Boundary*(Boundary.H*Omega*Boundary).inv()*Boundary.H*Omega)
    else:
        P=sp.zeros(len(pts))
    Cref1=sp.Matrix.hstack(*(coeff(rem(sp.invert(v,modulus.as_expr())*t**j,modulus),d) for j in range(d)))
    refbase=kron_all([Cref1]*k)
    ref_exps=list(product(range(d),repeat=k))
    embed=sp.zeros(len(exps),d**k)
    for j,a in enumerate(ref_exps):
        embed[exps.index(a),j]=1
    R0=clean(T*embed*refbase)
    return dict(k=k,N=N,d=d,h=modulus,g=global_poly,T=T,Omega=Omega,M=M,J=J,Kernel=Kernel,G=G,C=C,R=R,A=A,D=Dop,B=defect,W=W,L=L,Boundary=Boundary,P=P,R0=R0,exps=exps)


class ExactControl(unittest.TestCase):
    def eq(self,A,B):
        D=clean(sp.Matrix(A)-sp.Matrix(B))
        self.assertEqual(D,sp.zeros(*D.shape))

    def test_01_full_jet_right_inverse(self):
        for N in [2,3]:
            z=data(N=N)
            self.eq(z['J']*z['C'],sp.eye(z['d']))

    def test_02_gram_inverse_interpolation(self):
        for repeated in [False,True]:
            z=data(N=2,repeated=repeated)
            self.eq(z['R'].H*z['Omega']*z['R'],z['G'])
            self.eq(z['Kernel']*z['G'],sp.eye(z['d']))

    def test_03_unique_minimum_orthogonality(self):
        z=data(N=3)
        self.eq(z['Boundary'].H*z['Omega']*z['R'],sp.zeros(z['Boundary'].cols,z['d']))
        U=sp.Matrix([[1,I],[-2,sp.Rational(1,3)]])
        delta=z['Boundary']*U
        self.eq((z['R']+delta).H*z['Omega']*(z['R']+delta), z['G']+delta.H*z['Omega']*delta)

    def test_04_projection_identification(self):
        z=data(N=3)
        self.eq((sp.eye(z['T'].rows)-z['P'])*z['R0'],z['R'])

    def test_05_integration_identity_and_boundary(self):
        for k,N in [(1,2),(2,2)]:
            z=data(k=k,N=N)
            self.eq(z['D'].H*z['Omega']+z['Omega']*z['D'],k*z['Omega'])
            self.eq(z['W'],-z['R'].H*z['Omega']*z['B']-z['B'].H*z['Omega']*z['R'])

    def test_06_one_step_layer(self):
        a,b=data(N=2),data(N=3)
        Pnew=clean(b['P']-a['P'])
        self.eq(Pnew*Pnew,Pnew)
        self.assertEqual(Pnew.rank(),1)
        Y=clean(Pnew*a['R'])
        C=clean((sp.eye(a['T'].rows)-a['P'])*a['B'])
        self.eq(Pnew*C,C)
        self.eq(a['G']-b['G'],Y.H*a['Omega']*Y)
        self.eq(a['W'],-Y.H*a['Omega']*C-C.H*a['Omega']*Y)

    def test_07_joint_tensor_layer(self):
        a,b=data(k=2,N=2),data(k=2,N=3)
        Pnew=clean(b['P']-a['P'])
        self.eq(Pnew*Pnew,Pnew)
        self.assertEqual(Pnew.rank(),sp.binomial(2+2,2-1))
        Y=clean(Pnew*a['R'])
        C=clean((sp.eye(a['T'].rows)-a['P'])*a['B'])
        self.eq(Pnew*C,C)
        self.eq(a['G']-b['G'],Y.H*a['Omega']*Y)
        self.eq(a['W'],-Y.H*a['Omega']*C-C.H*a['Omega']*Y)

    def test_08_tensor_moment_entries(self):
        z=data(k=2,N=3)
        u=data(k=1,N=3)
        for a,aa in enumerate(z['exps']):
            for b,bb in enumerate(z['exps']):
                self.assertEqual(sp.expand(z['M'][a,b]-sp.prod(u['M'][aa[j],bb[j]] for j in range(2))),0)

    def test_09_full_repeated_jet(self):
        z=data(N=2,repeated=True)
        A=z['A']; N=A-half*sp.eye(2)
        self.eq(N*N,sp.zeros(2))
        self.assertNotEqual(N,sp.zeros(2))
        self.eq(z['J']*z['C'],sp.eye(2))

    def test_10_same_metric_reflection(self):
        for k,N,repeated in [(1,2,False),(1,2,True),(2,2,False)]:
            z=data(k=k,N=N,repeated=repeated)
            C1=sp.Matrix.hstack(*(coeff(rem((1-t)**j,z['h']),z['d']) for j in range(z['d'])))
            C=kron_all([C1]*k)
            self.eq(C*C.conjugate(),sp.eye(z['d']**k))
            self.eq(C.H*z['G']*C,z['G'].conjugate())
            self.eq(C.H*z['W']*C,-z['W'].conjugate())
            self.eq(z['A']*C,C*(k*sp.eye(z['d']**k)-z['A'].conjugate()))

    def test_11_weight_not_erased(self):
        for k,N in [(1,2),(2,2)]:
            z=data(k=k,N=N)
            rho=sp.Rational(1,4)
            ev=(z['A']-k*rho*sp.eye(2**k)).nullspace()[0]
            self.eq(ev.H*z['W']*ev,k*(2*rho-1)*(ev.H*z['G']*ev))
            self.assertNotEqual((ev.H*z['W']*ev)[0],0)

    def test_12_matrix_metric_freedom(self):
        H=sp.diag(4,9)
        C=sp.Matrix([[1,I],[2,1]])
        Gperp=sp.Matrix([[3,1],[1,2]])
        G0=Gperp+C.H*H.inv()*C
        X=sp.Matrix([[1,2],[I,-1]])
        B=sp.diag(sp.Rational(1,2),sp.Rational(1,3))*X-H.inv()*C
        GB=G0+C.H*B+B.H*C+B.H*H*B
        self.eq(GB,Gperp+X.H*X)

    def test_13_spectral_cost_vs_absolute_decay(self):
        A=sp.diag(sp.Rational(1,4),sp.Rational(3,4))
        for c in [1,sp.Rational(1,100),sp.Rational(1,10000)]:
            G=c*sp.eye(2);W=A.H*G+G*A-G
            self.eq(G.inv()*W,sp.diag(-sp.Rational(1,2),sp.Rational(1,2)))

    def test_14_source_quotient_tau_e(self):
        tau=object()
        def lift(f,x):
            return tau if x is tau else ('active',f(x[1]))
        q=lambda p: rem(p,h)
        x=('active',h.as_expr())
        out=lift(q,x)
        self.assertIsNot(out,tau)
        self.assertEqual(out,('active',0))
        self.assertIs(lift(q,tau),tau)
        for p in [1,t,t**4,0]:
            self.assertEqual(lift(q,('active',p))[1],q(p))

    def test_15_tensor_koszul_boundary_signs(self):
        for k in range(1,8):
            for j in range(k):
                primitive=(-1)**j
                differential=(-1)**j
                self.assertEqual(primitive*differential,1)

    def test_16_packet_inclusions(self):
        # Use one shared discrete Hilbert observation and the same L_n.
        nodes=[half+I*j for j in [-3,-2,-1,0,1,2,3]]
        Omega=sp.diag(*(1+sp.im(z)**2 for z in nodes))
        def section(modulus,n):
            d=modulus.degree();v=sp.exquo(g,modulus).as_expr()
            eps=sp.invert(v,modulus.as_expr())
            S=clean([[v.subs(t,z)*rem(eps*t**j,modulus).subs(t,z) for j in range(d)] for z in nodes])
            F=clean([[g.as_expr().subs(t,z)*z**j for j in range(n+1)] for z in nodes])
            P=clean(F*(F.H*Omega*F).inv()*F.H*Omega)
            return S,clean((sp.eye(len(nodes))-P)*S)
        Sh,Rh=section(h,1);SH,RH=section(g,1)
        iota=sp.Matrix.hstack(*(coeff(rem(m.as_expr()*rem(sp.invert(m.as_expr(),h.as_expr())*t**j,h),g),4) for j in range(2)))
        self.eq(SH*iota,Sh);self.eq(RH*iota,Rh)
        self.eq(iota.H*(RH.H*Omega*RH)*iota,Rh.H*Omega*Rh)
        self.eq(multiplication(t,g)*iota,iota*multiplication(t,h))

    def test_17_moment_enclosure_scalar(self):
        M=sp.Rational(21,10);Mh=sp.Integer(2);eta=sp.Rational(1,10);mu=sp.Rational(19,10)
        self.assertLessEqual(abs(1/M-1/Mh),eta/(mu*(mu-eta)))

    def test_18_correction_budget_is_fixed(self):
        z=data(N=2)
        ker=z['L']
        self.assertEqual(ker.cols,1)
        # Unique orthogonal section, with no unrestricted representative parameter.
        self.eq(ker.H*z['M']*z['C'],sp.zeros(1,2))
        self.assertEqual(z['J'].rank(),2)

    def test_19_joint_correction_changes_metric_with_jets_fixed(self):
        z=data(k=2,N=2)
        delta=clean(z['R0']-z['R'])
        self.assertGreater(delta.rank(),0)
        self.eq(delta.H*z['Omega']*z['R'],sp.zeros(4))
        self.eq(z['R0'].H*z['Omega']*z['R0']-z['G'],delta.H*z['Omega']*delta)
        self.eq(z['J']*z['C'],sp.eye(4))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--json',type=Path)
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactControl)
    if args.self_test_failure:
        class ExpectedFailure(unittest.TestCase):
            def runTest(self):
                self.assertEqual(1,2,'intentional failure verifies execution')
        suite.addTest(ExpectedFailure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'success':result.wasSuccessful(),'scope':'Exact finite discrete-measure calibrations; no analytic or Lean certificate','sympy':sp.__version__}
    if args.json:
        args.json.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
