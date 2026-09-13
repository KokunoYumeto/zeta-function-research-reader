#!/usr/bin/env python3
"""Exact regression checks for the full-jet kernel / supported-layer bridge.

All fixtures are finite discrete measures and polynomial multipliers, NOT zeta
packets. General proofs are in RESEARCH_NOTE.md. The optional source checker
is independently rerun and cross-compared by the separate review receipt.
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

s = sp.Symbol('s')
HALF = sp.Rational(1, 2)


def clean(a):
    return sp.Matrix(a).applyfunc(lambda x: sp.cancel(sp.expand(x)))


def exponents(k: int, degree: int):
    if k < 1 or degree < 0:
        raise ValueError('positive tensor degree and nonnegative polynomial degree required')
    return sorted((a for a in product(range(degree+1), repeat=k) if sum(a)<=degree),
                  key=lambda a:(sum(a), a))


def kron(mats):
    out = sp.ones(1, 1)
    for a in mats:
        out = sp.kronecker_product(out, a)
    return clean(out)


def remainder_column(poly, h):
    r = sp.rem(sp.Poly(poly, s), sp.Poly(h, s)).as_expr()
    return sp.Matrix([sp.expand(r).coeff(s,j) for j in range(sp.degree(h,s))])


def multiplication(h):
    return sp.Matrix.hstack(*(remainder_column(s**(j+1),h) for j in range(sp.degree(h,s))))


@lru_cache(None)
def one_variable(max_degree: int, repeated: bool=False, asymmetric: bool=False, wide: bool=False):
    if wide:
        h=sp.prod(s-r for r in [sp.Rational(1,8),sp.Rational(1,4),sp.Rational(3,4),sp.Rational(7,8)])
        v=sp.Integer(1)
        heights=[-4,-3,-2,-1,1,2,3,4]
    else:
        h=(s-HALF)**2 if repeated else (s-sp.Rational(1,4))*(s-sp.Rational(3,4))
        v=(s-sp.Rational(1,8))*(s-sp.Rational(7,8))
        heights=list(range(-2,3))
    nodes=[HALF+sp.I*j for j in heights]
    if max_degree>=len(nodes):
        raise ValueError('fixture requires more nodes for a strictly positive moment matrix')
    weights=[sp.Integer(1+j*j)*(2 if asymmetric and j>0 else 1) for j in heights]
    omega=sp.diag(*weights)
    vals=clean([[sp.expand(v.subs(s,z)*z**j) for j in range(max_degree+1)] for z in nodes])
    moment=clean(vals.H*omega*vals)
    coeffs=[]; polynomials=[]; norms=[]; jets=[]
    for j in range(max_degree+1):
        c=sp.zeros(max_degree+1,1);c[j]=1
        if j:
            lower=moment[:j,:j].inv()*moment[:j,j]
            for i in range(j):c[i]=-lower[i]
        p=sp.expand(sum(c[i]*s**i for i in range(j+1)))
        norm=sp.simplify((c.H*moment*c)[0])
        if norm.is_positive is not True:
            raise ValueError('positive exact fixture norm required')
        coeffs.append(c);polynomials.append(p);norms.append(norm)
        jets.append(remainder_column(v*p,h))
    return dict(h=sp.expand(h),v=sp.expand(v),nodes=nodes,weights=weights,omega=omega,
                moment=moment,p=polynomials,norms=norms,jets=jets,coeffs=coeffs)


@lru_cache(None)
def kernel(k: int, degree: int, repeated: bool=False, asymmetric: bool=False, wide: bool=False):
    u=one_variable(degree+1,repeated,asymmetric,wide)
    d=sp.degree(u['h'],s)
    if degree<k*(d-1):raise ValueError('full-jet surjectivity threshold not met')
    aa=exponents(k,degree)
    def aj(a):return kron([u['jets'][j] for j in a])
    def nj(a):return sp.prod(u['norms'][j] for j in a)
    jets=sp.Matrix.hstack(*(aj(a) for a in aa))
    norms=[nj(a) for a in aa]
    K=clean(jets*sp.diag(*(1/n for n in norms))*jets.H)
    A1=multiplication(u['h']);A=sp.zeros(d**k)
    for i in range(k):A+=kron([A1 if j==i else sp.eye(d) for j in range(k)])
    A=clean(A)
    old=[a for a in aa if sum(a)==degree]
    nxt=[b for b in exponents(k,degree+1) if sum(b)==degree+1]
    top=sp.Matrix.hstack(*(aj(a) for a in old))
    top_norm=sp.diag(*(nj(a) for a in old))
    outgoing=[]
    for a in old:
        column=sp.zeros(d**k,1)
        for i in range(k):
            b=list(a);b[i]+=1;column+=aj(tuple(b))
        outgoing.append(column)
    outgoing=sp.Matrix.hstack(*outgoing)
    next_jets=sp.Matrix.hstack(*(aj(b) for b in nxt))
    next_norm=sp.diag(*(nj(b) for b in nxt))
    F=sp.zeros(len(nxt),d**k)
    for ib,b in enumerate(nxt):
        for i in range(k):
            if b[i]:
                a=list(b);a[i]-=1;a=tuple(a)
                F[ib,:]+=aj(a).H/nj(a)
    V=clean(A*K+K*A.H-k*K)
    endpoint=clean(outgoing*top_norm.inv()*top.H+top*top_norm.inv()*outgoing.H)
    return dict(k=k,M=degree,d=d,u=u,exps=aa,jets=jets,norms=norms,K=K,A=A,V=V,
                top=top,top_norm=top_norm,outgoing=outgoing,next=nxt,
                next_jets=next_jets,next_norm=next_norm,F=F,endpoint=endpoint)


@lru_cache(None)
def layer(k: int, degree: int, repeated: bool=False, asymmetric: bool=False):
    z=kernel(k,degree,repeated,asymmetric);u=z['u']
    points=list(product(u['nodes'],repeat=k))
    weight_map=dict(zip(u['nodes'],u['weights']))
    omega=sp.diag(*(sp.prod(weight_map[x] for x in point) for point in points))
    def values(aa):
        return clean([[sp.prod(u['v'].subs(s,x)*u['p'][j].subs(s,x)
                                     for j,x in zip(a,point)) for a in aa] for point in points])
    T=values(z['exps']);Tplus=values(z['next'])
    G=clean(z['K'].inv())
    coeff=clean(sp.diag(*(1/n for n in z['norms']))*z['jets'].H*G)
    R=clean(T*coeff)
    E=clean(Tplus-R*z['next_jets'])
    H=clean(z['next_norm']+z['next_jets'].H*G*z['next_jets'])
    Y=clean(-E*H.inv()*z['next_jets'].H*G)
    C=clean(E*z['F']*G)
    Kplus=clean(z['K']+z['next_jets']*z['next_norm'].inv()*z['next_jets'].H)
    Gplus=clean(Kplus.inv())
    Rplus=clean(R-Y)
    Dop=sp.diag(*(sum(point) for point in points))
    B=clean(Dop*R-R*z['A'])
    W=clean(z['A'].H*G+G*z['A']-k*G)
    null=z['jets'].nullspace()
    if null:
        oldB=clean(T*sp.Matrix.hstack(*null))
        Pold=clean(oldB*(oldB.H*omega*oldB).inv()*oldB.H*omega)
    else:
        oldB=sp.zeros(T.rows,0);Pold=sp.zeros(T.rows)
    return dict(z,points=points,omega=omega,T=T,Tplus=Tplus,G=G,coeff=coeff,R=R,
                E=E,H=H,Y=Y,C=C,Kplus=Kplus,Gplus=Gplus,Rplus=Rplus,Dop=Dop,
                B=B,W=W,Pold=Pold,oldB=oldB)


class KernelLayerTests(unittest.TestCase):
    def eq(self,A,B):
        D=clean(sp.Matrix(A)-sp.Matrix(B))
        self.assertEqual(D,sp.zeros(*D.shape))

    def test_01_monic_norms_not_rescaled(self):
        u=one_variable(4)
        change=sp.Matrix.hstack(*u['coeffs'])
        self.eq(change.H*u['moment']*change,sp.diag(*u['norms']))
        for p in u['p']:self.assertEqual(sp.Poly(p,s).LC(),1)
        self.assertNotEqual(u['norms'][0],1)

    def test_02_full_kernel_source_crosscheck(self):
        # Independent direct monomial formula on the same discrete measure.
        for repeat in [False,True]:
            z=kernel(1,2,repeat);u=z['u']
            rawJ=sp.Matrix.hstack(*(remainder_column(u['v']*s**j,u['h']) for j in range(3)))
            self.eq(z['K'],rawJ*u['moment'][:3,:3].inv()*rawJ.H)

    def test_03_joint_kernel_orthogonal_product_basis(self):
        z=layer(2,2)
        self.eq(z['T'].H*z['omega']*z['T'],sp.diag(*z['norms']))
        self.eq(z['jets']*z['coeff'],sp.eye(4))
        self.eq(z['R'].H*z['omega']*z['R'],z['G'])

    def test_04_actual_next_relation_layer_basis(self):
        z=layer(2,2)
        self.eq(z['Pold']*z['E'],sp.zeros(*z['E'].shape))
        self.eq(z['E'].H*z['omega']*z['E'],z['H'])
        self.assertEqual(z['E'].rank(),sp.binomial(2+2,2-1))
        self.eq(z['jets']*(-z['coeff']*z['next_jets'])+z['next_jets'],sp.zeros(4,4))

    def test_05_derivative_class_coefficients(self):
        for k,M in [(1,2),(2,2)]:
            z=layer(k,M)
            self.eq((sp.eye(z['T'].rows)-z['Pold'])*z['B'],z['C'])
            self.eq(z['Pold']*(z['B']-z['C']),z['B']-z['C'])
            self.assertNotEqual(z['C'],sp.zeros(*z['C'].shape))

    def test_06_projection_coordinates_and_metric_loss(self):
        z=layer(2,2)
        PE=clean(z['E']*z['H'].inv()*z['E'].H*z['omega'])
        self.eq(PE*PE,PE)
        self.eq(PE*z['R'],z['Y'])
        self.eq(z['E'].H*z['omega']*z['Rplus'],sp.zeros(4,4))
        self.eq(z['G']-z['Gplus'],z['Y'].H*z['omega']*z['Y'])
        self.eq(z['Rplus'].H*z['omega']*z['Rplus'],z['Gplus'])

    def test_07_inverse_metric_control_congruence(self):
        for k,M in [(1,2),(2,2)]:
            z=layer(k,M)
            self.eq(z['K']*z['W']*z['K'],z['V'])
            self.eq(z['W'],z['G']*z['V']*z['G'])
            self.eq(z['V'],-(z['Y']*z['K']).H*z['omega']*(z['C']*z['K'])
                    -(z['C']*z['K']).H*z['omega']*(z['Y']*z['K']))

    def test_08_endpoint_for_full_jets_and_tensors(self):
        for k,M,r,a in [(1,2,False,False),(1,3,True,False),(2,2,False,False),
                         (2,3,False,False),(2,2,True,False),(1,3,False,True)]:
            z=kernel(k,M,r,a)
            self.eq(z['V'],z['endpoint'])
            self.eq(z['V'],z['next_jets']*z['F']+z['F'].H*z['next_jets'].H)

    def test_09_nonvacuous_sharper_shell_rank(self):
        z=kernel(2,6,wide=True)
        improved=2*sp.binomial(6+2-1,2-1)
        source=2*sp.binomial(6+2,2-1)
        self.assertEqual((improved,source,z['d']**2),(14,16,16))
        from sympy.polys.matrices import DomainMatrix
        self.assertLessEqual(DomainMatrix.from_Matrix(z['V']).rank(),improved)
        self.eq(z['V'],z['endpoint'])

    def test_10_univariate_layer_is_original_theta_vector(self):
        for M in [2,3]:
            z=layer(1,M);u=z['u'];n=M-z['d'];g=sp.expand(u['h']*u['v'])
            f=clean([[g.subs(s,x)*x**j for j in range(n+2)] for x in u['nodes']])
            old=f[:,:n+1]
            P=clean(old*(old.H*u['omega']*old).inv()*old.H*u['omega'])
            residual=clean((sp.eye(len(u['nodes']))-P)*f[:,n+1])
            self.eq(z['E'],residual)
            self.eq(z['H'],residual.H*u['omega']*residual)

    def test_11_positive_shell_kernel_update(self):
        z=layer(2,2);nextz=kernel(2,3)
        self.eq(z['Kplus'],nextz['K'])
        A=z['next_jets'];G=z['G']
        self.eq(z['Gplus'],G-G*A*z['H'].inv()*A.H*G)

    def test_12_natural_dual_control_sign(self):
        z=kernel(2,2);dual=2*sp.eye(4)-z['A'].H
        self.eq(dual.H*z['K']+z['K']*dual-2*z['K'],-z['V'])
        C1=sp.Matrix.hstack(*(remainder_column((1-s)**j,z['u']['h']) for j in range(z['d'])))
        C=kron([C1,C1]);Cd=C.T
        self.eq(Cd.H*z['K']*Cd,z['K'].conjugate())
        self.eq(Cd.H*z['V']*Cd,-z['V'].conjugate())

    def test_13_generalized_characteristic_polynomials(self):
        z=layer(1,2);lam=sp.Symbol('lambda')
        self.assertEqual(sp.factor((lam*z['G']-z['W']).det()/z['G'].det()
                         -(lam*z['K']-z['V']).det()/z['K'].det()),0)

    def test_14_eigenline_diagnostic_survives_congruence(self):
        z=layer(2,2);rho=sp.Rational(1,4)
        v=(z['A']-2*rho*sp.eye(4)).nullspace()[0]
        xi=z['G']*v
        self.eq(xi.H*z['V']*xi,2*(2*rho-1)*(xi.H*z['K']*xi))
        self.assertNotEqual((xi.H*z['V']*xi)[0],0)

    def test_15_imaginary_diagonal_not_deleted(self):
        u=one_variable(4,asymmetric=True)
        p=u['p'][1];norm=u['norms'][1]
        diagonal=sp.simplify(sum(w*sp.conjugate(u['v'].subs(s,x)*p.subs(s,x))*x*
                                  u['v'].subs(s,x)*p.subs(s,x)
                                  for x,w in zip(u['nodes'],u['weights']))/norm)
        self.assertEqual(sp.re(diagonal),HALF)
        self.assertNotEqual(sp.im(diagonal),0)
        self.eq(kernel(1,3,asymmetric=True)['V'],kernel(1,3,asymmetric=True)['endpoint'])

    def test_16_degree_convolution(self):
        z=kernel(2,3);u=z['u'];A=[clean(a*a.H/n) for a,n in zip(u['jets'],u['norms'])]
        conv=sp.zeros(4)
        for i in range(4):
            for j in range(4-i):conv+=sp.kronecker_product(A[i],A[j])
        self.eq(conv,z['K'])

    def test_17_original_polynomial_relations_and_koszul_signs(self):
        z=layer(2,2);u=z['u'];x,y=sp.symbols('x y');variables=(x,y)
        polys=[sp.prod(u['p'][a[i]].subs(s,variables[i]) for i in range(2)) for a in z['exps']]
        for ib,b in enumerate(z['next']):
            pnext=sp.prod(u['p'][b[i]].subs(s,variables[i]) for i in range(2))
            c=z['coeff']*z['next_jets'][:,ib]
            relation=sp.expand(pnext-sum(polys[j]*c[j] for j in range(len(polys))))
            remainder=relation;reconstructed=sp.Integer(0)
            for i,t in enumerate(variables):
                q,remainder=sp.div(remainder,u['h'].subs(s,t),t)
                if q!=0:self.assertLessEqual(sp.Poly(q,*variables).total_degree(),3-z['d'])
                primitive=(-1)**i*q
                reconstructed+=(-1)**i*u['h'].subs(s,t)*primitive
            self.assertEqual(sp.expand(remainder),0)
            self.assertEqual(sp.expand(reconstructed-relation),0)

    def test_18_exact_relative_certificate(self):
        # A scalar-multiple metric fixture keeps both approximation errors nonzero.
        K=sp.diag(2,3);A=sp.diag(sp.Rational(1,4),sp.Rational(3,4))
        Kh=K+sp.Rational(1,100)*sp.eye(2);Ah=A+sp.Rational(1,1000)*sp.eye(2)
        etaK=sp.Rational(1,100);etaA=sp.Rational(1,1000);eps=sp.Rational(3,5)
        V=A*K+K*A.H-K;Vh=Ah*Kh+Kh*Ah.H-Kh
        etaV=(2*sp.Rational(751,1000)+1)*etaK+2*etaA*(sp.Rational(301,100)+etaK)
        for sign in [-1,1]:
            self.assertTrue(all(a>=0 for a in (eps*Kh+sign*Vh-(eps*etaK+etaV)*sp.eye(2)).diagonal()))
            self.assertTrue(all(a>=0 for a in (eps*K+sign*V).diagonal()))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path)
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(KernelLayerTests)
    if args.self_test_failure:
        class DeliberateFailure(unittest.TestCase):
            def runTest(self):self.assertEqual(1,2,'deliberate nonzero exit control')
        suite.addTest(DeliberateFailure())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'success':result.wasSuccessful(),'sympy':sp.__version__,
            'scope':'Exact finite polynomial/discrete-measure regression; no analytic or Lean certificate'}
    if args.json:args.json.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':sys.exit(main())
