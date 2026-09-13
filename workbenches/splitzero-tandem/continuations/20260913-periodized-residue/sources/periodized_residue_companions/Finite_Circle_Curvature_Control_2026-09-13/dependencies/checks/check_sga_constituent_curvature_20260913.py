"""Exact finite regressions for SC9--SC25; analytic proofs are in the TeX."""
from pathlib import Path
import argparse, json, sys, unittest
import sympy as s

S=s.symbols('S')
def zero(v):
    if isinstance(v,s.MatrixBase):
        return all(s.cancel(s.expand(x))==0 for x in v)
    return s.cancel(s.expand(v))==0
def col(poly,q):
    return s.Matrix([s.expand(poly).coeff(S,j) for j in range(q)])
def fixture(chi,g):
    chi=s.expand(chi); g=s.expand(g);q=s.degree(chi,S);p=q-s.degree(g,S)
    A=s.Matrix.hstack(*[col(s.rem(S**(j+1),chi,S),q) for j in range(q)])
    I=s.Matrix.hstack(*[col(g*S**j,q) for j in range(p)])
    R=s.zeros(q);R[0,q-1]=1
    ell=s.zeros(1,q);ell[0,q-1]=1
    Pi=s.eye(q)
    for j in range(q-1):Pi[j,j+1]=s.Rational(j+1,3)+s.I
    M=s.eye(q)
    for j in range(q-1):M[j+1,j]=s.Rational(j+2,5)
    G=s.Rational(7,2)*(M.T*M)
    return A,I,R,ell,Pi,G

fixtures=[((S-1)*(S-2),S-1),((S-1)**2*(S+2),S+2),
          ((S-1)**3*(S+2),(S-1)**2),((S-1)**3*(S+2),S+2)]

class CurvatureTests(unittest.TestCase):
    def test_exact_cyclic_ideals_and_acceleration(self):
        for chi,g in fixtures:
            A,I,R,ell,Pi,G=fixture(chi,g);p=I.cols;q=I.rows
            AF=(I.T*I).inv()*I.T*A*I
            self.assertTrue(zero(A*I-I*AF))
            self.assertEqual(list(ell*I),[0]*(p-1)+[1])
            Y=Pi*I;H=Y.conjugate().T*Y;N=s.eye(q)-Y*H.inv()*Y.conjugate().T
            u=2+3*s.I
            acceleration=N*Pi*(A*A/u**2-R/u)*I
            self.assertEqual(acceleration.rank(),1)
            self.assertTrue(zero(acceleration+N*Pi*R*I/u))
            self.assertEqual(len(acceleration.nullspace()),p-1)
    def test_all_parameter_normal_formula_and_coefficient(self):
        for chi,g in fixtures:
            A,I,R,ell,Pi,G=fixture(chi,g);q=I.rows
            Y=Pi*I;H=Y.conjugate().T*Y;N=s.eye(q)-Y*H.inv()*Y.conjugate().T
            u=2+3*s.I;e0=s.eye(q)[:,0];z=N*Pi*e0;L=ell*I
            c=(z.conjugate().T*z)[0]*(L*H.inv()*L.conjugate().T)[0]/13
            self.assertTrue(s.simplify(c)>0)
            for t in [0,s.Rational(2,3),1+2*s.I]:
                Y1=-Pi*(A+t*R)*I/u
                self.assertTrue(zero(N*Y1+t*z*L/u))
                curvature=s.trace(H.inv()*Y1.conjugate().T*N*Y1)
                self.assertTrue(zero(curvature-t*s.conjugate(t)*c))
    def test_theta_norm_and_schur_complement(self):
        for chi,g in fixtures:
            A,I,R,ell,Pi,G=fixture(chi,g);q=I.rows
            Y=Pi*I;H=Y.conjugate().T*Y;GF=I.T*G*I;U=Pi.inv()
            W=U.conjugate().T*G*U;PN=Y*GF.inv()*Y.conjugate().T*W
            e0=s.eye(q)[:,0];z=(s.eye(q)-PN)*Pi*e0
            schur=(e0.T*G*e0-e0.T*G*I*GF.inv()*I.T*G*e0)[0]
            self.assertTrue(zero((z.conjugate().T*W*z)[0]-schur))
            self.assertTrue(s.simplify(schur)>0)
            B=GF.inv()*H
            self.assertTrue(zero(H.inv()-B.inv()*GF.inv()))
            L=ell*I;normal=(s.eye(q)-Y*H.inv()*Y.conjugate().T)*Pi*R*I/(2+3*s.I)
            op=GF.inv()*normal.conjugate().T*normal
            self.assertEqual(op.rank(),1)
            self.assertTrue(zero(op*op-s.trace(op)*op))
    def test_moving_theta_metric_cancellation(self):
        for chi,g in fixtures:
            A,I,R,ell,Pi,G=fixture(chi,g);t=1+2*s.I;u=2+3*s.I
            At=A+t*R;Y=Pi*I;U=Pi.inv();W=U.conjugate().T*G*U
            Y1=-Pi*At*I/u
            Wt=U.conjugate().T*G*At*U/u
            self.assertTrue(zero(Y.conjugate().T*Wt*Y+Y.conjugate().T*W*Y1))
            self.assertTrue(zero(Y1.conjugate().T*W*Y+Y.conjugate().T*Wt.conjugate().T*Y))
    def test_three_minors_with_retained_theta_factors(self):
        for chi,g in fixtures:
            A,J,R,ell,Pi,G=fixture(chi,g);q=J.rows;p=J.cols
            Jminus=J[:,:p-1];Jplus=J.row_join(s.eye(q)[:,0])
            period=lambda T:(T.conjugate().T*Pi.conjugate().T*Pi*T).det()
            theta=lambda T:(T.conjugate().T*G*T).det()
            hg=period(J);hm=period(Jminus);hp=period(Jplus)
            Y=Pi*J;H=Y.conjugate().T*Y;N=s.eye(q)-Y*H.inv()*Y.conjugate().T
            z=N*Pi[:,0];L=ell*J
            c=(z.conjugate().T*z)[0]*(L*H.inv()*L.conjugate().T)[0]
            self.assertTrue(zero(c-hp*hm/hg**2))
            vg,vm,vp=theta(J),theta(Jminus),theta(Jplus)
            bg,bm,bp=hg/vg,hm/vm,hp/vp
            self.assertTrue(zero(c-vp*vm/vg**2*bp*bm/bg**2))
            if p==q-1:self.assertEqual(Jplus.det(),(-1)**(q-1))
    def test_explicit_collision_tor_representatives(self):
        for H in [S**3,(S-1)**3*(S+2),(S-1)**2*(S+2),S**3-S]:
            q=s.degree(H,S)
            A=s.Matrix.hstack(*[col(s.rem(S**(j+1),H,S),q) for j in range(q)])
            hp=s.diff(H,S)
            J=s.zeros(q)
            for (j,),c in s.Poly(hp,S).terms():J+=c*A**j
            for ww in J.nullspace():
                w=sum(ww[j]*S**j for j in range(q))
                v,r=s.div(s.expand(hp*w),H,S)
                self.assertTrue(zero(r))
                self.assertTrue(zero(s.rem(H*v,hp,S)))
                recovered,r=s.div(s.expand(H*v),hp,S)
                self.assertTrue(zero(r))
                self.assertTrue(zero(s.rem(recovered-w,H,S)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--json',type=Path);a=p.parse_args()
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(CurvatureTests))
    out={'methods':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
         'success':result.wasSuccessful(),'python':sys.version,'optimization':sys.flags.optimize,
         'sympy':s.__version__,'scope':'Declared exact cyclic algebra fixtures; no arithmetic zero packet or analytic period certificate.'}
    if a.json:a.json.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    sys.exit(0 if result.wasSuccessful() else 1)
