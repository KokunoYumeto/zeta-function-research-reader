#!/usr/bin/env python3
"""Exact finite regression checks. General proofs are in NOTE.tex.
No arithmetic zeta-zero data or analytic interval claims are encoded here.
"""
from __future__ import annotations
import argparse, json, sys, unittest
from pathlib import Path
import sympy as sp

S,u,t,w,z=sp.symbols('S u t w z')

def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(sp.cancel(e)==0 for e in x)
    return sp.cancel(sp.expand(x))==0

def D(P, chi):
    return sp.expand(u*sp.diff(P,S)+(chi-t)*P)

def reduction(P,chi):
    q=sp.degree(chi,S); rem=sp.expand(P); quotient=sp.S.Zero
    while rem!=0 and sp.degree(rem,S)>=q:
        pol=sp.Poly(rem,S); mon=pol.LC()*S**(pol.degree()-q)
        quotient+=mon;rem=sp.expand(rem-D(mon,chi))
    return sp.expand(quotient),sp.expand(rem)

def coeff(P,q):
    return sp.Matrix([sp.expand(P).coeff(S,j) for j in range(q)])

def companion(chi):
    q=sp.degree(chi,S)
    return sp.Matrix.hstack(*[coeff(reduction(S**(j+1),chi)[1],q) for j in range(q)])

def residue_gram(chi):
    q=sp.degree(chi,S); y=sp.symbols('y')
    # coefficient S^-1 at infinity, i.e. coefficient y^1 after S=1/y
    def entry(a,b):
        return sp.series((S**(a+b)/chi).subs(S,1/y),y,0,2).removeO().expand().coeff(y,1)
    return sp.Matrix(q,q,entry)

class ExactTests(unittest.TestCase):
    def test_polynomial_direct_sum_and_specialization(self):
        for chi in [S-sp.Rational(3,4), S**2+2*S-3, (S-2)**3, S**4+S**2+3*S-1]:
            q=sp.degree(chi,S)
            for P in [S**(q+3)+(u+t)*S**2+1, (u+t)*S**(2*q)+t*S+u, D(S**3+t,chi)]:
                Q,R=reduction(P,chi)
                self.assertTrue(zero(P-D(Q,chi)-R))
                self.assertTrue(R==0 or sp.degree(R,S)<q)
                expected=sp.rem(P.subs({u:0,t:0}),chi,S)
                self.assertTrue(zero(R.subs({u:0,t:0})-expected))

    def test_connection_commutator_with_full_parameters(self):
        chi=S**3+2*S**2-3*S+5
        P=S**5+u*t*S**2+t**2+u
        T=lambda a: sp.diff(a,t)-S*a/u
        self.assertTrue(zero(D(T(P),chi)-T(D(P,chi))))
        self.assertTrue(zero(D(S*P,chi)-S*D(P,chi)-u*P))

    def test_connection_descends_on_nonconstant_relation(self):
        chi=(S-1)**3
        Q=t*S**4+u*S**2+t**2
        F=D(Q,chi)
        self.assertTrue(zero(reduction(sp.diff(F,t)-S*F/u,chi)[1]))

    def test_companion_and_polar_coefficient(self):
        for q in range(1,5):
            chi=S**q+sum((j+2)*S**j for j in range(q))
            A=companion(chi); A0=A.subs(t,0)
            R=sp.zeros(q);R[0,q-1]=1
            self.assertTrue(zero(A-A0-t*R))
            self.assertEqual(sp.factor(A.charpoly(S).as_expr()),sp.factor(chi-t))
            v=sp.Matrix([t**(j+1)+u for j in range(q)])
            polar=-u*v.diff(t)+A*v
            self.assertTrue(zero(polar.subs({u:0,t:0})-A0*v.subs({u:0,t:0})))

    def test_multiplication_does_not_descend_but_connection_does(self):
        chi=S**3-2*S+1
        self.assertTrue(zero(reduction(chi-t,chi)[1]))
        self.assertTrue(zero(reduction(S*(chi-t),chi)[1]+u))
        self.assertFalse(zero(u))

    def test_residue_pairing_independent_of_t(self):
        for chi in [S+2,S**2+3*S+7,(S-2)**3,S**4+2*S**3+S**2+5*S+6]:
            self.assertTrue(zero(residue_gram(chi-t)-residue_gram(chi)))

    def test_residue_duality_determinant_and_horizontality(self):
        for chi in [S+2,S**2+3*S+7,(S-2)**3,S**4+2*S**3+S**2+5*S+6]:
            q=sp.degree(chi,S);B=residue_gram(chi);A=companion(chi)
            self.assertEqual(sp.factor(B.det()),(-1)**(q*(q-1)//2))
            self.assertTrue(zero(A.T*B-B*A))
            v=sp.Matrix([t**(j+1) for j in range(q)])
            vv=sp.Matrix([u+(j+2)*t**2 for j in range(q)])
            lhs=sp.diff((v.T*B*vv)[0],t)
            rhs=((v.diff(t)-A*v/u).T*B*vv+v.T*B*(vv.diff(t)+A*vv/u))[0]
            self.assertTrue(zero(lhs-rhs))

    def test_jacobian_trace_with_repeated_roots(self):
        for chi in [(S-2)**3,(S+1)**2*(S-3),S**2-2]:
            q=sp.degree(chi,S);A=companion(chi).subs(t,0);B=residue_gram(chi)
            f=S+2;g=S**2-1
            fvec=coeff(sp.rem(f,chi,S),q)
            gv=coeff(sp.rem(sp.diff(chi,S)*g,chi,S),q)
            pairing=(fvec.T*B*gv)[0]
            mat=(A+2*sp.eye(q))*(A**2-sp.eye(q))
            self.assertTrue(zero(pairing-sp.trace(mat)))

    def test_source_rank_one_deformation_preserves_boundary(self):
        A=sp.Matrix([[0,3],[1,-2]]);Rop=sp.Matrix([[0,1],[0,0]])
        r=sp.Matrix([[1,0],[0,1],[2,3]])
        jet=sp.Matrix([[1,0,0],[0,1,0]])
        Q=sp.eye(3)-r*jet
        # D = r A jet + boundary-valued map; the latter is killed by jet
        K=sp.Matrix([[2,-1,3],[1,0,2],[-2,4,1]])
        Dop=r*A*jet+Q*K
        Dt=Dop+t*r*Rop*jet
        self.assertTrue(zero(jet*Dt-(A+t*Rop)*jet))
        self.assertTrue(zero(Dt*r-r*(A+t*Rop)-(Dop*r-r*A)))
        self.assertTrue(zero((Dt-Dop)*Q))
        PP=sp.Matrix(2,2,sp.symbols('p0:4'))
        self.assertTrue(zero(-u*(-PP*(A+t*Rop)/u)*jet-PP*jet*Dt))
        G=r.T*r
        W=A.T*G+G*A-sp.Rational(5)*G
        At=A+t*Rop
        self.assertTrue(zero(At.T*G+G*At-5*G-W-t*(G*Rop+Rop.T*G)))

    def test_logarithmic_cech_cohomology_all_orders(self):
        for m in range(1,11):
            # H1(O(-m)) columns a=1,...,m-1, H1(O(-m-1)) rows b=1,...,m
            dd=sp.zeros(m,m-1)
            for a in range(1,m): dd[a,a-1]=-a
            self.assertEqual(dd.rank(),m-1)
            res=sp.zeros(1,m);res[0,0]=1
            self.assertTrue(zero(res*dd))
            self.assertEqual(m-dd.rank(),1)

    def test_local_positive_residue_jet_contraction(self):
        for m in range(1,12):
            dg=sp.diag(*range(1,m)) if m>1 else sp.zeros(0)
            hh=sp.diag(*[sp.Rational(1,j) for j in range(1,m)]) if m>1 else sp.zeros(0)
            self.assertTrue(zero(dg*hh-sp.eye(m-1)))
            self.assertTrue(zero(hh*dg-sp.eye(m-1)))
            # constant jet not included in this contraction
            extended=sp.diag(*range(m))
            self.assertEqual(extended.rank(),m-1)

    def test_log_connection_inclusion_and_pullback(self):
        f=1+3*w+2*w**3
        for m in range(1,8):
            dm=lambda a: w*sp.diff(a,w)+m*a
            d1=lambda a: w*sp.diff(a,w)+a
            self.assertTrue(zero(d1(w**(m-1)*f)-w**(m-1)*dm(f)))
            self.assertTrue(zero(sp.diff(z**m,z)/z**m-m/z))

    def test_action_hull_and_regularized_matrix(self):
        A=sp.Matrix([[1,0,0],[1,2,0],[0,1,3]])
        e0=sp.Matrix([1,0,0]);cols=sp.Matrix.hstack(e0,A*e0,A**2*e0)
        self.assertEqual(cols.rank(),3)
        for m in range(1,5):
            J=sp.diag(1,w**m,w**m)
            Ah=J.inv()*A*J
            self.assertEqual(Ah[1,0],w**(-m))
            self.assertTrue(zero(J*Ah-A*J))
        # a proper invariant hull retains a quotient action
        A2=sp.Matrix([[1,2,3],[0,1,4],[0,0,5]])
        J=sp.diag(1,w**3,w**3)
        Ah=J.inv()*A2*J
        self.assertFalse(any(sp.denom(sp.cancel(v)).has(w) for v in Ah))
        self.assertEqual(sp.trace(A2**3),1+sp.trace(A2[1:3,1:3]**3))

    def test_curvature_pullback_and_log_moment_antiderivative(self):
        x=sp.symbols('x',positive=True)
        for m in range(1,6):
            f=sp.log(1+3*x**m)+sp.log(1+7*x**m)
            kappa=sp.diff(x*sp.diff(f,x),x)
            target=m*m*x**(m-1)*(3/(1+3*x**m)**2+7/(1+7*x**m)**2)
            self.assertTrue(zero(kappa-target))
            self.assertEqual(sp.limit(x*sp.diff(f,x),x,sp.oo),2*m)
            self.assertEqual(sp.limit(x*sp.diff(f,x),x,0),0)
            self.assertEqual(sp.simplify(f.subs(x,1)-sp.log(4)-sp.log(8)),0)

    def test_current_degrees_and_metric_pole_factors(self):
        for q in range(1,8):
            for f0 in range(q+1):
                for f1 in range(f0,q+1):
                    for m in range(1,5):
                        original=m*(q-f0); added=m*(f1-f0)
                        self.assertEqual(original-added,m*(q-f1))
        C=sp.diag(0,5,7);G=sp.diag(2,3,11)
        for m in range(1,5):
            hM=sp.diag(2,5+3*w**(2*m),7+11*w**(2*m))
            j=sp.diag(1,w**m,w**m)
            hs=j.inv().T*hM*j.inv()
            self.assertTrue(zero(hs.det()-w**(-4*m)*hM.det()))
            self.assertTrue(zero(hs-(G+w**(-2*m)*C)))

    def test_specialization_and_supported_zero(self):
        # Ordinary finite vector calculations take place inside fixed supported fibres.
        tau=('absent',None)
        lifted=lambda x:('supported',sp.expand(x))
        specialize=lambda v: tau if v==tau else lifted(v[1].subs({u:0,t:0}))
        self.assertEqual(specialize(tau),tau)
        self.assertEqual(specialize(lifted(u)),lifted(0))
        self.assertNotEqual(lifted(0),tau)
        chi=S**3+2*S+1;P=S**2+t
        self.assertTrue(zero(reduction(chi*P-t*P+u*sp.diff(P,S),chi)[1]))
        self.assertTrue(zero(sp.rem(sp.diff(chi*P,S),chi,S)-sp.rem(sp.diff(chi,S)*P,chi,S)))

    def test_rank_one_calibration_keeps_original_coefficient(self):
        chi=S-sp.Rational(3,4)
        self.assertEqual(companion(chi)[0,0],sp.Rational(3,4)+t)
        self.assertEqual(residue_gram(chi),sp.ones(1))
        self.assertEqual(sp.integrate(chi,S),S**2/2-sp.Rational(3,4)*S)


    def test_all_coefficient_connections_descend(self):
        cs=sp.symbols('c0:3');chi=S**3+sum(cs[a]*S**a for a in range(3))
        P=S**5+u*t*S**2+cs[0]*cs[2]
        for a in range(3):
            Conn=lambda f:sp.diff(f,cs[a])+S**(a+1)*f/((a+1)*u)
            self.assertTrue(zero(D(Conn(P),chi)-Conn(D(P,chi))))
            self.assertTrue(zero(reduction(Conn(D(P,chi)),chi)[1]))

    def test_reduced_coefficient_connection_is_flat(self):
        for q in [2,3]:
            cs=sp.symbols('c0:'+str(q));chi=S**q+sum(cs[a]*S**a for a in range(q))
            At=-companion(chi)/u
            for a in range(q):
                Ba=sp.Matrix.hstack(*[coeff(reduction(S**(a+b+1)/((a+1)*u),chi)[1],q) for b in range(q)])
                curvature=At.diff(cs[a])-Ba.diff(t)+Ba*At-At*Ba
                self.assertTrue(zero(curvature))

    def test_root_of_unity_period_matrix_is_nonsingular(self):
        x=sp.symbols('x')
        for d in range(2,9):
            phi=sp.cyclotomic_poly(d,x);q=d-1
            Fgram=sp.zeros(q)
            for l in range(1,d):
                for m in range(1,d):
                    expr=sum((x**((-j*l)%d)-1)*(x**((j*m)%d)-1) for j in range(1,d))
                    Fgram[l-1,m-1]=sp.rem(expr,phi,x)
            self.assertTrue(zero(Fgram-d*(sp.eye(q)+sp.ones(q))))
            self.assertEqual(Fgram.det(),d**d)

    def test_rank_one_period_and_source_metric_ratio(self):
        vv=sp.symbols('vv',positive=True);lam=sp.symbols('lam',real=True)
        period=sp.I*sp.sqrt(2*sp.pi*vv)*sp.exp(-(lam+t)**2/(2*vv))
        self.assertTrue(zero(sp.diff(period,t)+(lam+t)*period/vv))
        H=sp.Matrix([[5,1],[1,7]])
        Gi=sp.Matrix([[7,2],[2,4]]);Gj=sp.Matrix([[3,1],[1,2]])
        Bi=Gi.inv()*H;Bj=Gj.inv()*H
        self.assertEqual(Bj.det()/Bi.det(),Gi.det()/Gj.det())
        self.assertTrue(zero(Bi.T*Gi-Gi*Bi))


    def test_infinity_etale_chart_retains_all_coefficients(self):
        v=sp.symbols('v')
        for q in range(1,6):
            cs=sp.symbols('c0:'+str(q));d=q+1
            chi=S**q+sum(cs[a]*S**a for a in range(q))
            Phi=sp.integrate(chi,S)
            beta=(sp.Rational(1,d)+sum(cs[a]*w**(q-a)/sp.Integer(a+1) for a in range(q))-t*w**q)/u
            self.assertTrue(zero(((Phi-t*S)/u).subs(S,1/w)-w**(-d)*beta))
            relation=v**d-1/beta
            self.assertTrue(zero(sp.rem(beta*v**d-1,relation,v)))
            self.assertTrue(zero(sp.rem((v/d)*sp.diff(beta*v**d-1,v)-1,relation,v)))
            self.assertEqual(beta.subs(w,0),1/(d*u))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--json',type=Path)
    parser.add_argument('--negative-control',choices=['connection-sign','erase-log-boundary','omit-curvature-atom'])
    args=parser.parse_args()
    if args.negative_control:
        if args.negative_control=='connection-sign':
            chi=S**2+1;P=S+t
            wrong=lambda a:sp.diff(a,t)+S*a/u
            valid=zero(D(wrong(P),chi)-wrong(D(P,chi)))
        elif args.negative_control=='erase-log-boundary':
            m=4;dd=sp.zeros(m,m-1)
            for a in range(1,m):dd[a,a-1]=-a
            valid=(m-dd.rank()==0)
        else:
            x=sp.symbols('x',positive=True)
            f=sp.log(1+5*x**3)+sp.log(1+7*x**3)
            mass=sp.limit(x*sp.diff(f,x),x,sp.oo)-sp.limit(x*sp.diff(f,x),x,0)
            valid=(mass==0) # omitting the atom claims degree zero for a positive mass of six
        if not valid:
            print('REJECTED:',args.negative_control);return 1
        print('UNEXPECTED ACCEPTANCE');return 0
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactTests)
    names=[test.id().split('.')[-1] for test in suite]
    res=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'suite':'Deligne exponential/logarithmic exact finite regressions',
            'tests':res.testsRun,'passed':res.wasSuccessful(),'names':names,
            'errors':len(res.errors),'failures':len(res.failures),'sympy':sp.__version__,
            'scope':'Finite algebraic checks; not a Lean or arithmetic-integral certificate.'}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(record,indent=2)+'\n')
    return 0 if res.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
