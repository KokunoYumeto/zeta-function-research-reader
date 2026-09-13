#!/usr/bin/env python3
"""Exact finite regressions for residue-driven constituent curvature.

These are rational polynomial/complex matrix fixtures, not zeta-zero packets,
interval quadratures, or a substitute for the written analytic proof.
Assertions remain active under python -O through explicit exceptions.
"""
from __future__ import annotations
import argparse
import json
import platform
import sys
import unittest
from typing import Any
import sympy as s

S = s.Symbol('S')

def require(value: Any, message: str) -> None:
    if not bool(value):
        raise AssertionError(message)

def zero(x: Any) -> bool:
    if isinstance(x, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in x)
    return s.simplify(x) == 0

def eq(x: Any, y: Any, message: str = 'exact identity failed') -> None:
    require(zero(x-y), message)

def positive(x: Any) -> None:
    require(s.simplify(x).is_positive is True, f'not certified positive: {x}')

def column(p: Any, q: int) -> s.Matrix:
    p = s.Poly(p, S)
    return s.Matrix([p.nth(i) for i in range(q)])

def algebra(chi: Any) -> tuple[s.Matrix, s.Matrix, s.Matrix, s.Matrix]:
    chi = s.Poly(chi, S).monic().as_expr()
    q = s.degree(chi, S)
    A = s.Matrix.hstack(*[column(s.rem(S**(j+1), chi, S), q) for j in range(q)])
    e = s.eye(q)[:, 0]
    ell = s.eye(q)[q-1, :]
    R = e*ell
    beta = s.Matrix(q,q,lambda i,j: s.Poly(s.rem(S**(i+j),chi,S), S).nth(q-1))
    return A, e, R, beta

def constituent(chi: Any, d: Any) -> tuple[s.Matrix, s.Matrix]:
    q, r = int(s.degree(chi,S)), int(s.degree(d,S))
    I = s.Matrix.hstack(*[column(s.expand(d*S**j),q) for j in range(q-r)])
    pi = s.Matrix.hstack(*[column(s.rem(S**j,d,S),r) for j in range(q)])
    return I, pi

def model(q: int) -> s.Matrix:
    return s.eye(q)+s.Matrix(q,q,lambda i,j: (s.Rational(i+1,j+2)+s.I/3) if i<j else 0)

def pairing_cost(M: s.Matrix, I: s.Matrix) -> Any:
    q = M.rows
    e, ell = s.eye(q)[:,0], s.eye(q)[q-1,:]
    MF = I.H*M*I
    P = I*MF.inv()*I.H*M
    a = (e.H*M*(s.eye(q)-P)*e)[0]
    b = (ell*I*MF.inv()*I.H*ell.H)[0]
    return s.simplify(a*b)

FIXTURES = [
    (S**2, S),
    (S**3+S, S),
    (S**3+S, S**2+1),
    ((S-2)**3*(S+1), (S-2)**2),
    ((S-2)**3*(S+1), S+1),
]

class Tests(unittest.TestCase):
    def test_01_perfect_residue_and_multiplication_trace(self):
        for chi in [S-2, S**2, S**3+S, (S-2)**3*(S+1)]:
            A,e,R,beta=algebra(chi); q=A.rows; ell=s.eye(q)[q-1,:]
            eq(beta.det(), (-1)**(q*(q-1)//2))
            eq(A.T*beta,beta*A)
            jac=sum((s.Poly(s.diff(chi,S),S).nth(j)*A**j for j in range(q)),s.zeros(q))
            for j in range(q+1):
                eq(s.trace(A**j),(ell*jac*A**j*e)[0])

    def test_02_generated_matrix_algebra(self):
        for chi in [S-2,S**2,S**3+S,(S-2)**3*(S+1)]:
            A,e,R,beta=algebra(chi);q=A.rows
            cols=[s.Matrix(list(A**i*R*A**j)) for i in range(q) for j in range(q)]
            require(s.Matrix.hstack(*cols).rank()==q*q,'generated algebra not full')

    def test_03_full_constituent_rank_and_kernel(self):
        for chi,d in FIXTURES:
            A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
            ell=s.eye(q)[q-1,:]
            eq(pi*I,s.zeros(pi.rows,I.cols))
            require(pi.rank()==pi.rows,'quotient not onto')
            eq(pi*A*I,s.zeros(pi.rows,I.cols))
            eq(pi*R*I,pi*e*(ell*I))
            require((pi*R*I).rank()==1,'leakage is not rank one')
            require((ell*I).rank()==1,'restricted residue is zero')
            require(len((pi*R*I).nullspace())==I.cols-1,'wrong kernel dimension')

    def test_04_source_cost_positive_with_nonorthogonal_constituents(self):
        for chi,d in FIXTURES:
            A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
            M=model(q).H*model(q)+s.eye(q)
            positive(pairing_cost(M,I))

    def test_05_exact_normal_velocity_all_parameters(self):
        for chi,d in FIXTURES[:3]:
            A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
            B=model(q);P=B*I;HF=P.H*P;proj=P*HF.inv()*P.H
            for t in [s.Integer(0),s.Integer(2),s.I]:
                u=2+s.I;Pprime=-B*(A+t*R)*I/u
                eq((s.eye(q)-proj)*Pprime, -t/u*(s.eye(q)-proj)*B*R*I)
                require(((s.eye(q)-proj)*Pprime).rank()==(0 if t==0 else 1),'wrong normal rank')

    def test_06_curvature_factorization(self):
        for chi,d in FIXTURES[:3]:
            A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
            B=model(q);P=B*I;HF=P.H*P;proj=P*HF.inv()*P.H
            t,u=1+s.I,2+s.I
            Pprime=-B*(A+t*R)*I/u
            lhs=s.trace(HF.inv()*Pprime.H*(s.eye(q)-proj)*Pprime)
            rhs=s.conjugate(t)*t/(s.conjugate(u)*u)*pairing_cost(B.H*B,I)
            eq(lhs,rhs);positive(rhs)

    def test_07_normal_acceleration_and_quartic_coefficient(self):
        chi,d=S**3+S,S
        A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
        B=model(q);P=B*I;HF=P.H*P;proj=P*HF.inv()*P.H;u=s.Integer(2)
        Psecond=B*(A*A/u**2-R/u)*I
        N=(s.eye(q)-proj)*Psecond
        eq(N,-(s.eye(q)-proj)*B*R*I/u)
        eq(s.trace(HF.inv()*N.H*N),pairing_cost(B.H*B,I)/u**2)
        require(N.rank()==1,'normal acceleration vanished')
        # Independently expand the actual scalar log Gram through t^2 bart^2.
        A,e,R,beta=algebra(S**2); I,pi=constituent(S**2,S)
        B=model(2);u=s.Integer(2)
        jets=[B,-B*A/u]
        jets.append(-(jets[1]*A+jets[0]*R)/(2*u))
        x,y=s.symbols('x y')
        ps=[b*I for b in jets]
        h=sum((ps[i].H*ps[j])[0]*y**i*x**j for i in range(3) for j in range(3))
        h0=(ps[0].H*ps[0])[0]
        Z=s.expand(h/h0-1)
        def trunc(poly):
            return sum(c*x**a*y**b for (a,b),c in s.Poly(s.expand(poly),x,y).terms() if a<=2 and b<=2)
        power=s.Integer(1);logjet=s.Integer(0)
        for n in range(1,5):
            power=trunc(power*Z)
            logjet+=(-1)**(n+1)*power/s.Integer(n)
        mixed=s.Poly(s.expand(logjet),x,y).coeff_monomial(x**2*y**2)*4
        eq(mixed,pairing_cost(B.H*B,I)/u**2)

    def test_08_source_endpoint_determinant_enclosure(self):
        for chi,d in FIXTURES[:3]:
            A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
            Gj=model(q).H*model(q)+s.eye(q)
            Gi=Gj+s.diag(*list(range(1,q+1)))
            ci,cj=pairing_cost(Gi,I),pairing_cost(Gj,I)
            detratio=s.simplify(Gi.det()/Gj.det())
            require(s.simplify(cj-ci/detratio).is_nonnegative is True,'lower endpoint enclosure')
            require(s.simplify(ci*detratio-cj).is_nonnegative is True,'upper endpoint enclosure')

    def test_09_period_to_source_condition_enclosure(self):
        I,pi=constituent(S**3+S,S**2+1)
        G=s.diag(2,3,4);H=s.diag(4,12,8)
        cG,cH=pairing_cost(G,I),pairing_cost(H,I)
        require((cH-cG/2).is_nonnegative is True,'lower condition enclosure')
        require((2*cG-cH).is_nonnegative is True,'upper condition enclosure')

    def test_10_laplacian_forcing_with_rank_one_term(self):
        A,e,R,beta=algebra((S-2)**3*(S+1));q=A.rows
        B=model(q);u=2+s.I;k=s.Integer(3);t=s.Rational(2,3);At=A+t*R
        B1=-B*At/u;B2=B*At*At/u**2-B*R/u
        eq(u**2*B2+k*u*B1+u*B*R,B*(At*At-k*At))
        require(not zero(u**2*B2+k*u*B1-B*(At*At-k*At)),'omitted forcing undetected')

    def test_11_original_metric_laplacian_transport(self):
        A,e,R,beta=algebra(S**3+S);q=A.rows;k=s.Integer(2)
        G=model(q).H*model(q)+s.eye(q);B=model(q)
        W=A.H*G+G*A-k*G;L=A*A-k*A
        eq(L.H*G-G*L,A.H*W-W*A)
        eq(G*L,W*A-A.H*G*A)
        Gt=B.inv().H*G*B.inv();At=B*A*B.inv();Lt=B*L*B.inv();Wt=B.inv().H*W*B.inv()
        eq(At.H*Gt+Gt*At-k*Gt,Wt)
        eq(Lt.H*Gt-Gt*Lt,At.H*Wt-Wt*At)

    def test_12_translation_preserves_curvature_not_trace(self):
        chi=S**3+S;d=S**2+1;a=2+s.I;u=2;k=3;f=3+s.I
        A,e,R,beta=algebra(chi);q=A.rows;I,pi=constituent(chi,d)
        Aa,ea,Ra,betaa=algebra(s.expand(chi.subs(S,S-a)))
        C=s.Matrix(q,q,lambda r,b:s.binomial(b,r)*a**(b-r) if r<=b else 0)
        eq(C.det(),1);eq(C*Aa*C.inv(),A+a*s.eye(q));eq(C*Ra*C.inv(),R)
        Ia=C.inv()*I;B=model(q);Ba=f*B*C
        eq(pairing_cost(Ba.H*Ba,Ia),pairing_cost(B.H*B,I))
        G=B.H*B+s.eye(q);Ga=C.H*G*C
        W=A.H*G+G*A-k*G;Wa=Aa.H*Ga+Ga*Aa-k*Ga
        eq(s.trace(Ga.inv()*Wa)-s.trace(G.inv()*W),2*q*s.re(a))


def negative_control(name: str) -> None:
    A,e,R,beta=algebra(S**2); I,pi=constituent(S**2,S)
    B=s.eye(2);u=s.Integer(1);t=s.Integer(2);P=B*I;H=P.H*P;proj=P*H.inv()*P.H
    if name=='rank':
        require((pi*R*I).rank()==0,'intentional rank negative control: actual rank is one')
    elif name=='laplacian':
        B1=-B*A/u;B2=B*A*A/u**2-B*R/u
        eq(u**2*B2+B1,B*(A*A-A),'intentional Laplacian negative control: forcing was omitted')
    elif name=='curvature':
        Pprime=-B*(A+t*R)*I/u
        actual=s.trace(H.inv()*Pprime.H*(s.eye(2)-proj)*Pprime)
        eq(actual,pairing_cost(B.H*B,I)/u**2,'intentional curvature negative control: |t|^2 was omitted')
    else:
        raise ValueError(name)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative',choices=['rank','laplacian','curvature'])
    args=parser.parse_args()
    if args.negative:
        negative_control(args.negative)
        return 0
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    names=[t.id().split('.')[-1] for t in suite]
    result=unittest.TestResult();suite.run(result)
    out={'status':'PASS' if result.wasSuccessful() else 'FAIL',
         'methods':result.testsRun,'tests':names,
         'errors':[{'test':str(t),'traceback':err} for t,err in result.errors],
         'failures':[{'test':str(t),'traceback':err} for t,err in result.failures],
         'scope':'exact finite algebra and matrix jets; no zeta packet, contour quadrature or Lean certificate',
         'python':platform.python_version(),'sympy':s.__version__}
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
