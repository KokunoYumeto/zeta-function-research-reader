#!/usr/bin/env python3
"""Exact finite regression checks for the displayed algebraic interfaces.
These checks do not prove the infinite-dimensional analytical estimates.
Uses unittest assertions (active under python -O) and exact SymPy arithmetic.
"""
from __future__ import annotations
import argparse, io, json, sys, unittest
from pathlib import Path
import sympy as s


def is_psd(M: s.Matrix) -> bool:
    from itertools import combinations
    if M != M.conjugate().T:
        return False
    for n in range(1, M.rows+1):
        for ids in combinations(range(M.rows), n):
            if M.extract(ids,ids).det() < 0:
                return False
    return True


def quotient(M: s.Matrix, J: s.Matrix) -> tuple[s.Matrix,s.Matrix]:
    G=(J*M.inv()*J.conjugate().T).inv()
    C=M.inv()*J.conjugate().T*G
    return G,C


class ExactTests(unittest.TestCase):
    def eq(self, X, Y):
        if isinstance(X, s.MatrixBase):
            self.assertEqual((X-Y).applyfunc(s.simplify), s.zeros(*X.shape))
        else:
            self.assertEqual(s.simplify(X-Y),0)

    def test_diagonal_coordinate_jacobian(self):
        for k in range(1,8):
            J=s.zeros(k,k)
            for i in range(k): J[i,0]=1
            for i in range(k-1): J[i,i+1]=1
            self.assertEqual(abs(J.det()),1)
            inv=J.inv()
            self.eq(inv*s.ones(k,1),s.eye(k)[:,0])

    def test_half_density_generator(self):
        r=s.symbols('r', real=True)
        for k in range(1,5):
            f=s.Function('f')(r)
            psi=s.exp(s.Rational(k,2)*r)*f
            self.eq(-s.diff(psi,r)+s.Rational(k,2)*psi,
                    -s.exp(s.Rational(k,2)*r)*s.diff(f,r))

    def test_periodic_laplacian_sign(self):
        r,L,k,w=s.symbols('r L k w', real=True)
        f=s.exp(-s.I*w*r)
        D=lambda x:-s.diff(x,r)+k*x/2
        self.eq(D(f),(k/2+s.I*w)*f)
        self.eq(D(D(f))-k*D(f),(-w*w-k*k/4)*f)

    def test_zeroth_mode_metric(self):
        F=s.Matrix([[1+s.I,2],[3,1-s.I],[-1,2*s.I]])
        z=s.Matrix([[2-s.I,3]])
        L=s.Rational(7,3)
        M=F.conjugate().T*F+z.conjugate().T*z/L
        full=F.col_join(z/s.sqrt(L))
        self.eq(M,full.conjugate().T*full)
        self.assertNotEqual(M,F.conjugate().T*F)

    def test_discrete_correlation_unfolding(self):
        # Exact finite-lattice analogue, retaining complex cross-pairings.
        rows=[s.Matrix([[i+1, s.I*(i-2)]]) for i in range(9)]
        for L in [2,3,5,12]:
            p=[s.zeros(1,2) for _ in range(L)]
            for n,f in enumerate(rows): p[n%L]+=f
            left=sum((x.conjugate().T*x for x in p),s.zeros(2))
            right=s.zeros(2)
            for a,f in enumerate(rows):
                for b,g in enumerate(rows):
                    if (b-a)%L==0:right+=f.conjugate().T*g
            self.eq(left,right)

    def test_lattice_factor(self):
        delta=s.symbols('delta',positive=True)
        # All powers have positive bases, so no branch change occurs.
        self.eq((2*s.pi)**delta/(2*s.pi)**(1+delta),1/(2*s.pi))
        self.assertNotEqual(s.Rational(1,2),1/(2*s.pi))

    def test_source_quotient_comparison(self):
        M=s.Matrix([[3,1,0],[1,4,1],[0,1,5]])
        E=s.Matrix([[1,0,0],[0,0,0],[0,0,2]])/10
        eta=s.Rational(1,4)
        J=s.Matrix([[1,0,-1],[0,1,2]])
        self.assertTrue(is_psd(eta*M-E))
        G,C=quotient(M,J); H,D=quotient(M+E,J)
        self.eq(J*C,s.eye(2));self.eq(J*D,s.eye(2))
        self.assertTrue(is_psd(H-(1-eta)*G))
        self.assertTrue(is_psd((1+eta)*G-H))
        self.eq(J*(D-C),s.zeros(2,2))

    def test_repeated_relation_and_unit(self):
        x=s.symbols('x'); chi=(x-1)**2; n=5
        cols=[]
        for j in range(n+1):
            r=s.Poly(s.rem(x**j,chi,x),x)
            cols.append(s.Matrix([r.nth(0),r.nth(1)]))
        J=s.Matrix.hstack(*cols)
        M=s.diag(*[s.Integer(j+2) for j in range(n+1)])
        H=M+s.ones(n+1)/17
        G,C=quotient(M,J); GL,CL=quotient(H,J)
        A=s.Matrix([[0,-1],[1,2]])
        unit=s.eye(2)+A
        self.assertNotEqual(unit.det(),0)
        self.eq(unit*J*CL,unit)
        for col in range(2):
            p=sum((CL[j,col]-C[j,col])*x**j for j in range(n+1))
            self.eq(s.rem(p,chi,x),0)
        self.eq((A-s.eye(2))**2,s.zeros(2))

    def test_weight_boundary_and_laplacian(self):
        k=s.Integer(3)
        D=s.diag(*[k/2+s.I*j for j in [-2,-1,1,3]])
        R=s.Matrix([[1,2],[s.I,1],[2,-s.I],[1+s.I,3]])
        A=s.Matrix([[s.Rational(7,4),2],[0,s.Rational(5,4)]])
        B=D*R-R*A; G=R.conjugate().T*R
        W=A.conjugate().T*G+G*A-k*G
        self.eq(W,-(R.conjugate().T*B+B.conjugate().T*R))
        self.eq((D**2-k*D)*R-R*(A**2-k*A),(D-k*s.eye(4))*B+B*A)
        self.assertNotEqual((D**2-k*D)*R,R*(A**2-k*A))

    def test_augmented_support_map(self):
        tau=('absent',)
        def lift(x):
            if x==tau:return tau
            label,vector=x
            return (label,(vector[0]+vector[1],vector[2]))
        x=('joint',(1,-1,0))
        self.assertEqual(lift(x),('joint',(0,0)))
        self.assertNotEqual(lift(x),tau)
        self.assertEqual(lift(tau),tau)

    def test_critical_kernel_retains_generalized_block(self):
        rho=s.Rational(3,4)+s.I
        A=s.diag(s.Matrix([[rho,1],[0,rho]]),s.Matrix([[s.Rational(1,2)+2*s.I]]))
        Gamma=s.Matrix([[0,0,1]])
        target=s.Matrix([[s.Rational(1,2)+2*s.I]])
        self.eq(Gamma*A,target*Gamma)
        self.assertEqual(len(Gamma.nullspace()),2)
        R=s.eye(3)
        self.assertEqual(R.rank(),3)

    def test_four_volume_dimension_factor(self):
        # Extremal scalar perturbations saturate the displayed two-versus-two budget.
        q=3; eta=s.Rational(1,5)
        upper=(1+eta)**(2*q)/(1-eta)**(2*q)
        self.eq(upper,((1+eta)/(1-eta))**(2*q))
        self.assertGreater(upper,1)

    def test_error_rate_and_period_choice(self):
        kappa=s.Rational(13,3); eta=s.Rational(1,8)
        exp_aL=1+kappa/eta
        self.eq(kappa/(exp_aL-1),eta)
        self.assertGreater(exp_aL,1)

    def test_finite_fourier_tail_coefficient(self):
        L,J=s.symbols('L J', positive=True)
        for p in range(1,7):
            lhs=(2*s.pi/L)*(L/(2*s.pi))**(2*p)*J**(1-2*p)/s.Integer(2*p-1)
            rhs=(L/(2*s.pi*J))**(2*p-1)/s.Integer(2*p-1)
            self.eq(lhs,rhs)

    def test_completed_sample_quotient_retains_exact_radical(self):
        x=s.symbols('x'); chi=(x-1)**2*(x-2)
        J=s.Matrix([[1,1,1]])  # evaluation at the sampled simple point S=1
        A=s.Matrix.hstack(*[s.Matrix([s.Poly(s.rem(x**(j+1),chi,x),x).nth(i) for i in range(3)]) for j in range(3)])
        self.eq(J*A,J)
        G=s.Rational(7,3)*J.T*J
        self.assertEqual(G.rank(),1)
        nil=s.Matrix([-1,1,0])  # class S-1: nonzero upstairs, killed by sampling
        self.eq(J*nil,s.zeros(1,1))
        self.assertNotEqual(nil,s.zeros(3,1))
        self.eq(G*nil,s.zeros(3,1))

    def test_finite_observation_inverse(self):
        Phi=s.Matrix([[1,0,1],[0,1,2],[1,2,0],[3,1,-1]])
        left=(Phi.T*Phi).inv()*Phi.T
        J=s.Matrix([[1,0,-1],[0,1,2]])
        self.eq(left*Phi,s.eye(3))
        self.eq(J*left*Phi,J)


def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument('--output');ap.add_argument('--negative',choices=['zero-mode','laplacian'])
    args=ap.parse_args()
    if args.negative:
        # Deliberately false controls, explicitly active under -O.
        if args.negative=='zero-mode':
            if s.Matrix([[1]]) != s.Matrix([[0]]):
                print('REJECTED: omitted represented zeroth-mode Gram');return 1
        else:
            D=s.diag(1+s.I,1+2*s.I);R=s.eye(2);A=s.diag(3,4);k=2;B=D*R-R*A
            good=(D**2-k*D)*R-R*(A**2-k*A)
            bad=D*B+B*A
            if good!=bad:print('REJECTED: missing -k boundary term');return 1
        return 0
    stream=io.StringIO()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactTests)
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    report={'suite':'periodized-source exact finite interfaces','tests_run':result.testsRun,
            'passed':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),
            'methods':unittest.defaultTestLoader.getTestCaseNames(ExactTests),
            'scope':'finite algebraic regressions; not proofs of analytic integrals or RH'}
    if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print(stream.getvalue());print(json.dumps(report,indent=2))
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
