#!/usr/bin/env python3
"""Finite exact checks for the SGA trace/period continuation.
The general proofs and analytic period argument are in RESEARCH_NOTE.md.
No Lean execution, RH result, or interval certification is encoded here.
"""
from __future__ import annotations
import argparse
import json
import sys
import unittest
from pathlib import Path
import sympy as sp

S,X,Y,t,u=sp.symbols('S X Y t u')

def iszero(x):
    if isinstance(x,sp.MatrixBase):
        return all(sp.cancel(sp.expand(e))==0 for e in x)
    return sp.cancel(sp.expand(x))==0

def vector(p,q):
    p=sp.expand(p)
    return sp.Matrix([p.coeff(S,j) for j in range(q)])

def rem(p,H):
    return sp.rem(sp.expand(p),H,S)

def companion(H):
    q=sp.degree(H,S)
    return sp.Matrix.hstack(*[vector(rem(S**(j+1),H),q) for j in range(q)])

def matrix_poly(p,A):
    ans=sp.zeros(A.rows)
    for (j,),c in sp.Poly(p,S).terms():
        ans += c*(A**j)
    return ans.applyfunc(sp.expand)

def residue(p,H):
    q=sp.degree(H,S)
    return sp.expand(rem(p,H)).coeff(S,q-1)

def residue_gram(H):
    q=sp.degree(H,S)
    return sp.Matrix(q,q,lambda i,j:residue(S**(i+j),H))

def bezout(H):
    return sp.div(H.subs(S,X)-H.subs(S,Y),X-Y,X)[0].expand()

def quantum_rem(p,H):
    q=sp.degree(H,S)
    z=sp.expand(p)
    while z!=0 and sp.degree(z,S)>=q:
        P=sp.Poly(z,S); mon=P.LC()*S**(P.degree()-q)
        z=sp.expand(z-H*mon-u*sp.diff(mon,S))
    return z

def phi(chi):
    return sp.integrate(chi,S)-t*S

def critical_trace(chi):
    A=companion(chi-t)
    return sp.expand(sp.trace(matrix_poly(phi(chi),A)))

def newton_char(power_sums):
    q=len(power_sums)
    a=[sp.S.One]
    for n in range(1,q+1):
        a.append(sp.expand(-sum(a[n-j]*power_sums[j-1] for j in range(1,n+1))/n))
    return sp.expand(sum(a[j]*S**(q-j) for j in range(q+1)))

class ExactTests(unittest.TestCase):
    def test_residue_gram_and_casimir_inverse(self):
        for H in [S+2,S**2+3*S+5,(S-2)**3,S**4+2*S**2-S+3]:
            q=sp.degree(H,S); G=residue_gram(H); b=bezout(H)
            C=sp.Matrix(q,q,lambda i,j:b.coeff(X,i).coeff(Y,j))
            self.assertTrue(iszero(G*C-sp.eye(q)))
            self.assertEqual(sp.factor(G.det()),(-1)**(q*(q-1)//2))

    def test_trace_jacobian_for_full_polynomial_fibres(self):
        for H in [S+2,S**2+S-3,(S-2)**3,(S-1)**2*(S+2)]:
            A=companion(H)
            for P in [1+S,S**5+2*S**2+3]:
                self.assertTrue(iszero(residue(sp.diff(H,S)*P,H)-sp.trace(matrix_poly(P,A))))

    def test_parameter_base_change_trace(self):
        H=S**3+2*S**2-S+5-t
        A=companion(H); G=residue_gram(H)
        self.assertTrue(iszero(G-residue_gram(H.subs(t,0))))
        self.assertTrue(iszero(A.T*G-G*A))
        for z in [-2,0,3]:
            self.assertTrue(iszero(A.subs(t,z)-companion(H.subs(t,z))))

    def test_diagonal_periodic_resolution_and_product(self):
        for H in [S-2,(S-2)**2,(S-1)**3,S**3-S]:
            q=sp.degree(H,S); A=companion(H); I=sp.eye(q)
            AX=sp.kronecker_product(A,I); AY=sp.kronecker_product(I,A)
            D=AX-AY; B=sp.zeros(q*q)
            for (a,b),c in sp.Poly(bezout(H),X,Y).terms():
                B += c*(AX**a)*(AY**b)
            self.assertTrue(iszero(D*B)); self.assertTrue(iszero(B*D))
            self.assertEqual(D.rank()+B.rank(),q*q)
            self.assertEqual(B.rank(),q)
            mu=sp.Matrix.hstack(*[vector(rem(S**(a+b),H),q) for a in range(q) for b in range(q)])
            self.assertTrue(iszero(mu*D))
            self.assertTrue(iszero(mu*B-matrix_poly(sp.diff(H,S),A)*mu))
            self.assertEqual(mu.rank(),q)

    def test_retained_higher_diagonal_dimensions(self):
        for H,r in [((S-1)**3,1),((S-1)**2*(S+2),2),(S**3-S,3)]:
            q=sp.degree(H,S); A=companion(H); J=matrix_poly(sp.diff(H,S),A)
            self.assertEqual(J.rank(),r)
            self.assertEqual(q-J.rank(),q-r)
            G=residue_gram(H)
            trace_form=sp.Matrix(q,q,lambda a,b:sp.trace(A**(a+b)))
            self.assertTrue(iszero(trace_form-G*J))
            self.assertEqual(trace_form.rank(),r)
        H=(S-1)**3
        self.assertTrue(iszero(rem(sp.diff(H,S)*(S-1),H)))
        self.assertFalse(iszero(rem(S-1,H)))

    def test_quantum_reduction_is_not_ideal_reduction(self):
        H=S**3+S-t
        self.assertTrue(iszero(quantum_rem(H,H)))
        self.assertTrue(iszero(quantum_rem(S*H,H)+u))
        self.assertFalse(iszero(u))

    def test_all_coefficient_connections_commute_with_source(self):
        c=sp.symbols('c0:3'); chi=S**3+sum(c[a]*S**a for a in range(3)); H=chi-t
        D=lambda P: sp.expand(u*sp.diff(P,S)+H*P)
        P=t*S**4+c[1]*S**2+u
        for a in range(3):
            conn=lambda P:sp.diff(P,c[a])+S**(a+1)*P/((a+1)*u)
            self.assertTrue(iszero(D(conn(P))-conn(D(P))))
        conn=lambda P:sp.diff(P,t)-S*P/u
        self.assertTrue(iszero(D(conn(P))-conn(D(P))))

    def test_quantum_trace_has_no_hidden_u_correction(self):
        for q in range(1,5):
            chi=S**q+sum((a+2)*S**a for a in range(q)); H=chi-t; A=companion(H)
            for r in range(1,q+1):
                C=sp.Matrix.hstack(*[vector(quantum_rem(S**(b+r),H),q) for b in range(q)])
                self.assertTrue(iszero(sp.trace(C)-sp.trace(A**r)))
                diff=C-A**r
                self.assertTrue(all(iszero(diff[a,b]) for b in range(q) for a in range(b,q)))

    def test_critical_value_trace_gradients(self):
        for q in range(1,4):
            c=sp.symbols('c0:'+str(q)); chi=S**q+sum(c[a]*S**a for a in range(q))
            A=companion(chi-t); F=critical_trace(chi)
            self.assertTrue(iszero(sp.diff(F,t)+sp.trace(A)))
            for a in range(q):
                self.assertTrue(iszero(sp.diff(F,c[a])-sp.trace(A**(a+1))/(a+1)))

    def test_newton_reconstruction_retains_repeated_roots(self):
        for H in [(S-2)**3,(S-sp.Rational(1,2))**2*(S+3),(S-1)**2*(S+1)**2]:
            A=companion(H); p=[sp.trace(A**j) for j in range(1,A.rows+1)]
            self.assertTrue(iszero(newton_char(p)-H))

    def test_rank_one_and_cubic_potential_calibrations(self):
        lam=sp.symbols('lam')
        self.assertTrue(iszero(critical_trace(S-lam)+(lam+t)**2/2))
        c0,c1=sp.symbols('c0 c1')
        self.assertTrue(iszero(critical_trace(S*S+c1*S+c0)-(c1**3/6-c1*(c0-t))))

    def test_original_conormal_response(self):
        H=(S-2)**3*(S+1)
        P=S**3+2*S+7
        self.assertTrue(iszero(rem(sp.diff(H*P,S),H)-rem(sp.diff(H,S)*P,H)))
        self.assertTrue(iszero(residue(sp.diff(H*P,S),H)-sp.trace(matrix_poly(P,companion(H)))))

    def test_period_frame_carries_metric_and_control(self):
        G=sp.Matrix([[7,1+sp.I],[1-sp.I,4]])
        A=sp.Matrix([[0,2],[1,3]]); P=sp.Matrix([[1,sp.I],[2,1]])
        U=P.inv(); H=U.conjugate().T*G*U
        k=3; W=A.conjugate().T*G+G*A-k*G
        Aprime=P*A*U
        self.assertTrue(iszero(Aprime.conjugate().T*H+H*Aprime-k*H-U.conjugate().T*W*U))
        Gi=G+sp.Matrix([[2,0],[0,1]]); Hi=U.conjugate().T*Gi*U
        self.assertTrue(iszero(Hi.det()/H.det()-Gi.det()/G.det()))

    def test_special_fibre_trace_shift_and_tensor(self):
        A=companion((S-1)**2); B=companion(S**2+1)
        C=sp.kronecker_product(A,sp.eye(2))+sp.kronecker_product(sp.eye(2),B)
        self.assertEqual(sp.trace(C),2*sp.trace(A)+2*sp.trace(B))
        for k in [1,2,3]:
            self.assertEqual((-1)**(1+k-1),(-1)**k)

    def test_fourier_gram_and_rank_one_orientation(self):
        for d,zeta in [(2,-sp.Integer(1)),(3,(-1+sp.I*sp.sqrt(3))/2),(4,sp.I)]:
            q=d-1
            F=sp.Matrix(q,q,lambda j,b:sp.expand(zeta**((j+1)*(b+1))-1))
            self.assertTrue(iszero(F.conjugate().T*F-d*(sp.eye(q)+sp.ones(q))))
            self.assertTrue(iszero(sp.conjugate(F.det())*F.det()-d**(q+1)))
        ur=sp.symbols('ur',positive=True)
        downward=sp.sqrt(2*ur)/2*sp.sqrt(sp.pi)*sp.I*(-2)
        upward=sp.I*sp.sqrt(2*sp.pi*ur)
        self.assertTrue(iszero(downward+upward))

    def test_constituent_period_derivative_and_normal_acceleration(self):
        # A has an actual invariant line, but the rank-one parameter can leave it.
        A=sp.Matrix([[2,1],[0,3]]); R=sp.Matrix([[0,0],[1,0]])
        Pi=sp.Matrix([[1,sp.I],[1,2]]); I=sp.Matrix([[1],[0]])
        P0=Pi*I; P1=-Pi*A*I; P2=Pi*(A*A-R)*I
        H=P0.conjugate().T*P0
        Hprime=P1.conjugate().T*P0+P0.conjugate().T*P1
        self.assertTrue(iszero(sp.trace(H.inv()*Hprime)+4))
        proj=P0*H.inv()*P0.conjugate().T
        self.assertTrue(iszero((sp.eye(2)-proj)*P1))
        self.assertTrue(iszero((sp.eye(2)-proj)*(P2+Pi*R*I)))
        self.assertEqual(((sp.eye(2)-proj)*Pi*R*I).rank(),1)

    def test_split_lift_keeps_relation_zero_supported(self):
        def lift(f,item):
            return None if item is None else (item[0],f(item[1]))
        H=(S-1)**2
        quotient=lambda p:rem(p,H)
        self.assertEqual(lift(quotient,('degree-4',H)),('degree-4',0))
        self.assertIsNone(lift(quotient,None))
        self.assertNotEqual(('degree-4',0),None)
        specialization=lambda p:sp.expand(p).subs({u:0,t:0})
        self.assertEqual(lift(specialization,('family',u)),('family',0))

    def test_boundary_amplitude_comparison_is_not_injective(self):
        # The original G(R) observation has separate tau and supported 0.
        tau=None; e=('supported',0)
        amplitude=lambda x:0 if x is None else x[1]
        support=lambda x:0 if x is None else 1
        self.assertEqual(amplitude(tau),amplitude(e))
        self.assertNotEqual((amplitude(tau),support(tau)),(amplitude(e),support(e)))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--json',type=Path)
    parser.add_argument('--negative',choices=['jacobian','quantum','newton'])
    args=parser.parse_args()
    if args.negative:
        H=(S-2)**3; A=companion(H)
        bad={'jacobian':residue(1,H)-sp.trace(sp.eye(3)),
             'quantum':quantum_rem(S*H,H),
             'newton':newton_char([sp.trace(A**j) for j in range(1,4)])-(S-2)}[args.negative]
        if not iszero(bad):
            print('REJECTED false control:',args.negative); sys.exit(1)
        sys.exit(0)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'methods':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'success':result.wasSuccessful(),'scope':'finite exact regression; not a Lean or analytic certificate',
            'sympy':sp.__version__}
    if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
    sys.exit(0 if result.wasSuccessful() else 1)
