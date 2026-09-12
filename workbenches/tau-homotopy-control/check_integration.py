#!/usr/bin/env python3
"""Finite exact regression tests; not Lean or analytic-source certification."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import unittest
import sympy as s


def zero(M: s.MatrixBase) -> bool:
    return all(s.simplify(x) == 0 for x in M)


def theta_model(dv=2, de=2):
    theta = s.eye(dv + de)[:, :dv]
    q = s.eye(dv + de)[dv:, :]
    F = s.Matrix([[1, 2], [0, 3]]) if dv == 2 else s.eye(dv)
    diff = theta.row_join(-theta * F)
    gamma = s.eye(dv).col_join(F.inv())
    return theta, q, F, diff, gamma


def homotopy(F, k, alpha, q):
    return (k + alpha*q).col_join(F.inv()*alpha*q)


def exp_nilpotent(M, t):
    out = s.eye(M.rows)
    power = s.eye(M.rows)
    for j in range(1, M.rows + 1):
        power = power * M
        out += power * t**j / s.factorial(j)
    if not zero(power):
        raise ValueError('fixture is not nilpotent in stated dimension')
    return out


class Exact(unittest.TestCase):
    def eqm(self, A, B):
        self.assertEqual(A.shape, B.shape)
        self.assertTrue(zero(A-B), f'nonzero matrix difference: {A-B}')

    def test_all_homotopies_finite_fields(self):
        for p,F in [(2,1),(3,2),(5,2)]:
            theta=s.Matrix([1,0]); q=s.Matrix([[0,1]])
            diff=theta.row_join(-F*theta); k=s.Matrix([[0,1]])
            valid=[]; first=[]
            for a in itertools.product(range(p),repeat=4):
                H=s.Matrix(2,2,a)
                if all(int(x)%p==0 for x in diff*H-theta*k):
                    first.append(tuple(a))
                    if all(int(x)%p==0 for x in H*diff): valid.append(tuple(a))
            expected=[]
            for alpha in range(p):
                H=(k+alpha*q).col_join(pow(F,-1,p)*alpha*q)
                expected.append(tuple(int(x)%p for x in H))
            self.assertEqual(set(valid),set(expected))
            self.assertEqual(len(valid),p)
            self.assertEqual(len(first),p*p)

    def test_noninvolutive_F_inverse_parameter(self):
        theta,q,F,d,gamma=theta_model()
        a=s.Matrix([[2,-1],[s.Rational(1,3),4]])
        k=s.Matrix([[1,3],[-2,5]])*q
        H=homotopy(F,k,a,q)
        self.eqm(d*H,theta*k); self.eqm(H*d,s.zeros(4,4))
        extracted=F*H[2:,:]
        self.eqm(extracted,a*q)
        self.assertFalse(zero(F*F-s.eye(2)))

    def test_difference_and_no_incoming_boundary(self):
        theta,q,F,d,gamma=theta_model()
        a=s.Matrix([[1,2],[3,4]]); b=s.Matrix([[0,-1],[2,0]])
        k=a*q
        diff=homotopy(F,k,a,q)-homotopy(F,k,b,q)
        self.eqm(diff,gamma*(a-b)*q)
        self.eqm(d*diff,s.zeros(4,4));self.eqm(diff*d,s.zeros(4,4))
        self.assertFalse(zero(diff))

    def test_second_equation_detects_wrong_lift(self):
        theta,q,F,d,gamma=theta_model()
        k=s.zeros(2,4); b=s.Matrix([[1,0,0,0],[0,0,0,0]])
        H=(k+b).col_join(F.inv()*b)
        self.eqm(d*H,theta*k)
        self.assertFalse(zero(H*d))

    def test_fourier_reflected_module(self):
        D=s.diag(s.Rational(1,4),s.Rational(3,4))
        F=s.Matrix([[0,2],[s.Rational(1,2),0]])
        self.eqm(F*D,(s.eye(2)-D)*F)
        self.eqm(D*F,F*(s.eye(2)-D))
        self.assertFalse(zero(D*F-F*D))

    def test_coherent_dilation_parameters(self):
        t,u,r=s.symbols('t u r',real=True)
        DV=s.Matrix([[0,1],[0,0]]); DQ=s.Matrix([[0,2],[0,0]])
        L=s.Matrix([[2,3],[-1,4]])
        def alpha(z):
            return (exp_nilpotent(DV,z-r)*L*exp_nilpotent(DQ,r)).applyfunc(lambda x:s.integrate(x,(r,0,z)))
        self.eqm(alpha(t+u),exp_nilpotent(DV,t)*alpha(u)+alpha(t)*exp_nilpotent(DQ,u))
        self.eqm(alpha(t).diff(t).subs(t,0),L)
        b=s.Matrix([[1,-1],[2,3]])
        cob=exp_nilpotent(DV,t)*b-b*exp_nilpotent(DQ,t)
        self.eqm(cob.diff(t).subs(t,0),DV*b-b*DQ)

    def test_supported_homotopies(self):
        p=5; invF=3; coeff=2
        def add(a,b):return (a[0]|b[0],tuple((x+y)%p for x,y in zip(a[1],b[1])))
        def mul(c,a):
            if c is None:return (0,(0,0))
            return (a[0],tuple(c*x%p for x in a[1]))
        def H(a):
            if a[0]==0:return (0,(0,0))
            z=a[1][1]
            return (3,((1+coeff)*z%p,invF*coeff*z%p))
        xs=[(0,(0,0))]+[(m,(x,y)) for m in [1,2,3] for x,y in itertools.product(range(p),repeat=2)]
        for a in xs:
            for c in [None,0,1,2,4]:self.assertEqual(H(mul(c,a)),mul(c,H(a)))
            for b in xs:self.assertEqual(H(add(a,b)),add(H(a),H(b)))
        self.assertEqual(H((1,(0,0))),(3,(0,0)))
        self.assertNotEqual(H((1,(0,0))),H((0,(0,0))))

    def test_homotopy_control_is_constant(self):
        theta,q,F,d,gamma=theta_model()
        rep=s.Matrix([[1,2],[3,4],[1,0],[0,1]])
        k0=s.Matrix([[1,3],[-2,5]]); k=k0*q
        for a in [s.zeros(2),s.eye(2),s.Matrix([[3,-2],[7,1]])]:
            H=homotopy(F,k,a,q)
            boundary=d*H*rep
            self.eqm(boundary,theta*k0)
            W=-(rep.conjugate().T*boundary+boundary.conjugate().T*rep)
            expected=-(rep.T*theta*k0+(theta*k0).T*rep)
            self.eqm(W,expected)

    def test_section_gauge_block(self):
        DV=s.Matrix([[0,1],[0,0]]); A=s.Matrix([[2,1],[0,3]])
        k=s.Matrix([[1,2],[3,4]]); b=s.Matrix([[3,-1],[2,5]])
        old=DV.row_join(k).col_join(s.zeros(2).row_join(A))
        U=s.eye(2).row_join(b).col_join(s.zeros(2).row_join(s.eye(2)))
        new=DV.row_join(k+DV*b-b*A).col_join(s.zeros(2).row_join(A))
        self.eqm(U.inv()*old*U,new)
        rep=s.Matrix([[1,2],[3,4],[1,0],[0,1]])
        theta=s.eye(4)[:,:2]; change=theta*b
        dg=rep.T*change+change.T*rep+change.T*change
        self.eqm((rep+change).T*(rep+change)-rep.T*rep,dg)
        def W(G):return A.T*G+G*A-G
        self.eqm(W((rep+change).T*(rep+change))-W(rep.T*rep),W(dg))

    def test_polynomial_degree_is_carried(self):
        for m in range(5):
            d=2; A=s.Matrix([[0,-2],[1,3]]); ell=s.Matrix([[2,1]])
            B=s.Matrix(m+1,d,lambda i,j:(i+1)*(j+2)-3)
            I=s.eye(m+2)[:,:m+1]; S=s.zeros(m+2,m+1)
            for j in range(m+1):S[j+1,j]=1
            e0=s.eye(m+2)[:,0]
            K=e0*ell+S*B-I*B*A
            X=s.eye(d).col_join(I*B); Y=s.zeros(d).col_join(K)
            D=s.zeros(d+m+3,d+m+2);D[:d,:d]=A
            D[d,:d]=ell
            for j in range(m+2):D[d+j+1,d+j]=1
            embed=s.zeros(d+m+3,d+m+2)
            for j in range(d+m+2):embed[j,j]=1
            self.eqm(D*X-embed*X*A,embed*Y)

    def test_master_gram_actual_integrals_calibration(self):
        # Calibration functions p(x)e^-x; not zeta source functions.
        x=s.symbols('x',positive=True)
        rho=s.Rational(1,3)+s.I/5
        def Der(p):return s.expand(x*p-x*s.diff(p,x))
        def ip(p,q):
            z=s.Poly(s.expand(s.conjugate(p)*q),x)
            return s.simplify(sum(c*s.factorial(k[0])/2**(k[0]+1) for k,c in z.terms()))
        for m in range(4):
            polys=[s.Integer(1),x-rho]
            for j in range(m+1):polys.append(Der(polys[-1]))
            M=s.Matrix(len(polys),len(polys),lambda i,j:ip(polys[i],polys[j]))
            B=s.Matrix([(-1)**j*s.Rational(j+1,j+2)+s.I/7 for j in range(m+1)])
            I=s.eye(m+2)[:,:m+1]; S=s.zeros(m+2,m+1)
            for j in range(m+1):S[j+1,j]=1
            K=s.eye(m+2)[:,0]+S*B-I*B*rho
            X=s.Matrix([1]).col_join(I*B); Y=s.Matrix([0]).col_join(K)
            G=X.conjugate().T*M*X
            W=-(X.conjugate().T*M*Y+Y.conjugate().T*M*X)
            self.eqm(W,(s.conjugate(rho)+rho-1)*G)
            p=sum(polys[j]*X[j] for j in range(len(polys)))
            boundary=Der(p)-rho*p
            self.assertEqual(s.simplify(ip(p,boundary)+ip(boundary,p)+W[0]),0)
            self.assertEqual(s.simplify(ip(p,p)-G[0]),0)

    def test_extension_class_change_is_multiple_of_h(self):
        t=s.symbols('t')
        h=(t-s.Rational(1,3))**2*(t-s.Rational(2,3))
        z=s.Poly(2+t+t**2,t)
        for p in [0,t,1+t**3,3-2*t+t**5]:
            new=z.as_expr()+h*p
            self.assertEqual(s.rem(new,h,t),s.rem(z.as_expr(),h,t))

    def test_residue_dual_control(self):
        A=s.Matrix([[s.Rational(1,2),1],[0,s.Rational(1,2)]])
        S=s.Matrix([[0,1],[-1,0]])
        G=s.Matrix([[3,1+s.I],[1-s.I,4]])
        self.eqm(A.conjugate().T*S+S*A,S)
        W=A.conjugate().T*G+G*A-G
        GD=S.conjugate().T*G.inv()*S
        WD=A.conjugate().T*GD+GD*A-GD
        self.eqm(WD,-S.conjugate().T*G.inv()*W*G.inv()*S)

    def test_tensor_control_and_unchanged_boundary(self):
        A=s.Matrix([[s.Rational(1,2),2],[0,s.Rational(1,2)]])
        G=s.Matrix([[2,1],[1,3]]); W=A.T*G+G*A-G
        An=s.kronecker_product(A,s.eye(2))+s.kronecker_product(s.eye(2),A)
        Gn=s.kronecker_product(G,G)
        Wn=s.kronecker_product(W,G)+s.kronecker_product(G,W)
        self.eqm(An.T*Gn+Gn*An-2*Gn,Wn)

    def test_nonzero_boundary_can_have_zero_control(self):
        D=s.diag(s.Rational(1,2)+s.I,s.Rational(1,2)+2*s.I)
        A=s.Rational(1,2)+2*s.I;theta=s.Matrix([1,0]);rep=s.Matrix([1,1])
        boundary=D*rep-rep*A
        self.eqm(boundary,-s.I*theta)
        self.assertFalse(zero(boundary))
        self.eqm(-(rep.conjugate().T*boundary+boundary.conjugate().T*rep),s.zeros(1))
        self.eqm(D.conjugate().T+D,s.eye(2))

    def test_one_dimensional_spectral_floor(self):
        for rho in [s.Rational(1,4)+2*s.I,s.Rational(1,2)+s.I,s.Rational(3,4)-s.I]:
            for metric in [s.Rational(1,3),2,7]:
                W=s.simplify(s.conjugate(rho)*metric+metric*rho-metric)
                self.assertEqual(s.simplify(W/metric),2*s.re(rho)-1)


class Negative(unittest.TestCase):
    def runTest(self):
        self.fail('deliberate negative control; must fail in normal and optimized modes')


class Recording(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs); self.passed=[]
    def addSuccess(self,test):
        self.passed.append(test.id()); super().addSuccess(test)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',type=Path)
    ap.add_argument('--deliberate-failure',action='store_true')
    args=ap.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Exact)
    if args.deliberate_failure:suite.addTest(Negative())
    result=unittest.TextTestRunner(verbosity=2,resultclass=Recording).run(suite)
    report={'scope':'finite exact regression models; no Lean or analytic certification',
            'python':platform.python_version(),'sympy':s.__version__,
            'tests_run':result.testsRun,'success':result.wasSuccessful(),
            'passed':result.passed,
            'failures':[t.id() for t,_ in result.failures],
            'errors':[t.id() for t,_ in result.errors],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':raise SystemExit(main())
