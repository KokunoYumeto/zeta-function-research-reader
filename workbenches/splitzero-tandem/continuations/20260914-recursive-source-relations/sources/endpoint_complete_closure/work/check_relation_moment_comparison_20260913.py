"""Exact checks of RM.20--31; supplied source checker remains byte-exact."""
from pathlib import Path
import argparse,importlib.util,json,sys,unittest,hashlib
import sympy as s

p=argparse.ArgumentParser();p.add_argument('--source-checker',required=True);p.add_argument('--json');p.add_argument('--negative-control',choices=['action-order','rank-transfer']);args=p.parse_args()
spec=importlib.util.spec_from_file_location('incoming_relation_moments',args.source_checker)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def psd(M):
 from itertools import combinations
 return M==M.H and all(M.extract(I,I).det()>=0 for size in range(1,M.rows+1) for I in combinations(range(M.rows),size))

class Tests(unittest.TestCase):
 def test_01_comparator_original_metric_and_determinant(self):
  b=m.block(3,3,6);G=b['Gi'];K=b['Ki'];J=b['Kj'];D=s.Matrix([[1,s.I,0],[-s.I,1,0],[0,0,0]])/7
  U=J+D;Zp=(U-K)*G
  self.assertTrue(psd(G*(Zp-b['Z'])))
  self.assertTrue(m.eq(G*Zp,Zp.H*G))
  self.assertGreaterEqual((s.eye(3)+Zp).det(),(s.eye(3)+b['Z']).det())
  self.assertTrue(m.eq((s.eye(3)+Zp).det(),(U*G).det()))
 def test_02_comparator_action_defect_full_order(self):
  b=m.block(3,3,6);G=b['Gi'];K=b['Ki'];J=b['Kj'];A=b['A'];Gj=b['Gj']
  D=s.Matrix([[1,s.I,0],[-s.I,1,0],[0,0,0]])/7;Zp=b['Z']+D*G
  Hi=K*A.H*G+A-2*s.eye(3);Hj=J*A.H*Gj+A-2*s.eye(3)
  E=D*A.H*G-J*A.H*Gj*D*G
  self.assertTrue(m.eq(A*Zp-Zp*A,Hj*(s.eye(3)+Zp)-(s.eye(3)+Zp)*Hi+E))
  self.assertNotEqual(E,s.zeros(3))
 def test_03_singular_positive_form_quotient_contraction(self):
  J=s.Matrix([[1,1,0],[0,1,1],[1,0,1]]);H=s.diag(2,5);V=J[:,:2];Dp=V*H*V.H
  F=V*s.Matrix([[1,1],[0,1]]);O=s.diag(7,11);C=H.inv()*s.Matrix([[1,1],[0,1]])
  Jp=V*H;G=m.block(3,3,6)['Gi'];Jpd=V.H*G
  self.assertEqual(Dp.rank(),2)
  self.assertTrue(m.eq(Jp*C,F));self.assertTrue(m.eq(Jp*Jpd,Dp*G))
  self.assertTrue(psd(O-C.H*H*C));self.assertTrue(psd(Dp-F*O.inv()*F.H))
  kernel=Dp.nullspace()[0];self.assertTrue(m.eq(F.H*kernel,s.zeros(2,1)))
 def test_04_comparator_source_HS_and_wedge_gram(self):
  b=m.block(3,3,6);G=b['Gi'];R=b['Ri'];Oi=b['Oi'];J=s.Matrix([[1,1,0],[0,1,1],[1,0,1]])
  H=s.diag(2,5);Jp=J[:,:2]*H;Phi=R*Jp;Gram=Phi.H*Oi*Phi;Zp=Jp*H.inv()*Jp.H*G
  self.assertTrue(m.eq(s.trace(H.inv()*Gram),s.trace(Zp)))
  self.assertTrue(m.eq(Gram.det()/H.det(),(s.trace(Zp)**2-s.trace(Zp**2))/2))
 def test_05_rank_retains_full_null_action(self):
  G=s.Matrix([[2,1,0],[1,3,1],[0,1,4]]);F=s.Matrix([[1,1],[1,1],[0,0]]);O=s.diag(7,11)
  Z=F*O.inv()*F.H*G;Q=(s.eye(3)+Z).inv();N=F.H*G
  self.assertEqual(Z.rank(),1)
  for v in N.nullspace():self.assertEqual(Z*v,s.zeros(3,1));self.assertEqual(Q*v,v)
  self.assertTrue(m.eq((s.eye(3)+Z).det(),1+s.trace(Z)))
 def test_06_rank_information_strictly_sharpens(self):
  t1=s.Integer(11);t2=s.Integer(85);a,b=m.two_moment_parameters(2,t1,t2)
  self.assertEqual((a,b),(9,2));self.assertEqual((1+a)*(1+b),30)
  full=m.sharp_upper_interval(4,m.frac(t1),m.frac(t2));rank=m.log_fraction(m.frac(30))
  self.assertLess(rank.hi,full.lo)
 def test_07_comparator_can_increase_rank(self):
  Z=s.diag(1,0,0);Zp=s.diag(1,2,0)
  self.assertTrue(psd(Zp-Z));self.assertEqual((Z.rank(),Zp.rank()),(1,2))
  self.assertEqual((s.eye(3)+Z).det(),2);self.assertEqual((s.eye(3)+Zp).det(),6)
 def test_08_literal_q3_matrix_and_third_moment(self):
  b=m.block(3,3,6);Z=s.Matrix([[-29,-35,84],[42,48,-126],[-21,-21,69]])/8
  G=s.Matrix([[7,7,0],[7,s.Rational(49,5),s.Rational(28,5)],[0,s.Rational(28,5),s.Rational(126,5)]])
  self.assertEqual(Z,b['Z']);self.assertEqual(G,b['Gi']);self.assertEqual(s.trace(Z**3),s.Rational(273947,256))
  x=s.symbols('x');self.assertTrue(m.eq(Z.charpoly(x).as_expr(),(4*x-3)*(64*x*x-656*x+15)/256))
 def test_09_empty_degree_update_and_positive_volume(self):
  b=m.block(3,3,3);self.assertEqual(b['Z'],s.zeros(3));self.assertGreater(b['Gi'].det(),0)
  self.assertEqual((s.eye(3)+b['Z']).det(),1)
 def test_10_full_contraction_defect_is_comparator_excess(self):
  J=s.Matrix([[1,1,0],[0,1,1],[1,0,1]]);H=s.diag(2,5);V=J[:,:2];Jp=V*H
  F=V*s.Matrix([[1,1],[0,1]]);O=s.diag(7,11);C=H.inv()*s.Matrix([[1,1],[0,1]])
  G=m.block(3,3,6)['Gi'];Jpd=V.H*G;Cd=O.inv()*C.H*H;Loss=s.eye(2)-C*Cd
  Delta=V*H*V.H-F*O.inv()*F.H
  self.assertTrue(psd(H*Loss));self.assertTrue(m.eq(Jp*Loss*Jpd,Delta*G))

if args.negative_control:
 if args.negative_control=='rank-transfer':
  m.require(s.diag(1,2,0).rank()<=s.diag(1,0,0).rank(),'rejected: positive comparator may increase rank')
 else:
  b=m.block(3,3,6);D=s.diag(1,0,0);G=b['Gi'];J=b['Kj'];Gj=b['Gj'];A=b['A']
  correct=D*A.H*G-J*A.H*Gj*D*G
  incorrect=D*A.H-J*A.H*Gj*D*G
  m.require(m.eq(correct,incorrect),'rejected: original G_i is required in comparator action defect')
 raise SystemExit(0)
suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
names=[t.id().split('.')[-1] for t in suite]
result=unittest.TextTestRunner(verbosity=2).run(suite)
data={'passed':result.wasSuccessful(),'methods':result.testsRun,'names':names,'failures':len(result.failures),'errors':len(result.errors),'optimization':sys.flags.optimize,'debug':__debug__,'source_checker_sha256':hashlib.sha256(Path(args.source_checker).read_bytes()).hexdigest(),'scope':'finite exact comparator form, source quotient contraction, arithmetic action order, rank and Gaussian calibration; no arithmetic moment integral'}
if args.json:Path(args.json).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
raise SystemExit(not result.wasSuccessful())
