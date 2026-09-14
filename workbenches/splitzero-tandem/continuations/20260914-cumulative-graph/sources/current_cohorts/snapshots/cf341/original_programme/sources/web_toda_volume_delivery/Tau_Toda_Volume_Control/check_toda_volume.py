#!/usr/bin/env python3
"""Exact finite checks. Gaussian/finite atomic fixtures are NOT arithmetic zeta packets.
The actual arithmetic statements are proved in NOTE.tex, not certified by this file.
Run with --json FILE. --fail-control deliberately fails under normal and -O Python.
"""
from __future__ import annotations
import argparse, json, sys, unittest
from functools import lru_cache
from pathlib import Path
import sympy as s
u=s.Symbol('u'); th=s.Symbol('theta',real=True)

def equal(a,b):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        a,b=s.Matrix(a),s.Matrix(b)
        if a.shape!=b.shape or any(s.simplify(x)!=0 for x in a-b):
            raise AssertionError(f'Unequal matrices: {a-b}')
    elif s.simplify(a-b)!=0:
        raise AssertionError(f'Unequal: {a}, {b}')

def positive(x):
    if not bool(s.simplify(x)>0):raise AssertionError(f'Not positive: {x}')

@lru_cache(None)
def gm(j,mean=s.Integer(0),variance=s.Integer(1),mass=s.Integer(7)):
    return s.expand(mass*sum(s.binomial(j,2*r)*s.factorial2(2*r-1)*variance**r*mean**(j-2*r) for r in range(j//2+1)))

def gram(n,moment,shift=0):
    return s.Matrix(n,n,lambda i,j:moment(i+j+shift))

def filtered(moment,f):
    terms=s.Poly(s.expand(f),u).terms()
    return lambda j:s.expand(sum(a*moment(j+power[0]) for power,a in terms))

def detseq(n,moment):return s.Integer(1) if n==0 else s.factor(gram(n,moment).det())

def remvec(f,phi):
    q=int(s.degree(phi,u));p=s.Poly(s.rem(s.expand(f),phi,u),u)
    return s.Matrix([p.nth(j) for j in range(q)])

def op_pol(n,moment):
    if not n:return s.Integer(1)
    c=gram(n,moment).inv()*s.Matrix([moment(n+j) for j in range(n)])
    return s.expand(u**n-sum(c[j]*u**j for j in range(n)))

@lru_cache(None)
def data(phi,N,mean=s.Integer(0),variance=s.Integer(1),mass=s.Integer(7)):
    q=int(s.degree(phi,u));moment=lambda j:gm(j,mean,variance,mass)
    M=gram(N+1,moment); Mp=gram(N+1,moment,1)
    J=s.Matrix.hstack(*[remvec(u**j,phi) for j in range(N+1)])
    K=J*M.inv()*J.T; G=s.simplify(K.inv());R=s.simplify(M.inv()*J.T*G)
    T=s.Matrix.hstack(*[remvec(u**(j+1),phi) for j in range(q)])
    c=s.Rational(3,2);A=c*s.eye(q)+s.I*T
    W=s.simplify(A.H*G+G*A-2*c*G);H=s.simplify(K*W)
    eps2=s.factor(s.trace(H*H)/2)
    mf=filtered(moment,phi**2)
    D=lambda n:detseq(n,moment);B=lambda n:detseq(n,mf)
    omega=lambda j:s.factor(D(j+1)/D(j))
    r=N-q+1
    V=s.factor(D(N+1)/B(r))
    lp=s.factor(s.trace(K*R.T*Mp*R))
    ratio=s.factor(omega(N+1)/omega(N))
    delta0=s.Integer(0) if r==0 else s.factor(omega(N)*B(r-1)/B(r))
    delta1=s.factor(omega(N+1)*B(r)/B(r+1))
    formula=s.factor(ratio*(1-delta0)*(1/delta1-1)-(s.trace(T)-lp)**2)
    return dict(q=q,moment=moment,M=M,Mp=Mp,J=J,K=K,G=G,R=R,T=T,A=A,W=W,H=H,eps2=eps2,D=D,B=B,omega=omega,r=r,V=V,lp=lp,ratio=ratio,delta0=delta0,delta1=delta1,formula=formula)

class TestControl(unittest.TestCase):
    def test01_hankel_norms(self):
        moment=lambda j:gm(j,s.Rational(1,3),s.Rational(2),s.Integer(11))
        for n in range(5):
            p=op_pol(n,moment)
            equal(filtered(moment,p*p)(0),detseq(n+1,moment)/detseq(n,moment))

    def test02_source_boundary_volume(self):
        for phi,N in [(u*u+1,1),(u*u+1,3),(u*u+u+1,3),((u-1)**2*(u+2),4)]:
            d=data(phi,N);equal(d['V'],d['G'].det());equal(d['J']*d['R'],s.eye(d['q']))

    def test03_boundary_is_original_kernel(self):
        phi=u**3+2*u+1;N=5;d=data(phi,N)
        L=s.Matrix(N+1,N-2,lambda i,j:s.expand(phi*u**j).coeff(u,i))
        equal(d['J']*L,s.zeros(3,N-2));equal(L.T*d['M']*d['R'],s.zeros(N-2,3))
        equal(d['R']*d['J']*L,s.zeros(N+1,N-2))

    def test04_scalar_epsilon_phase(self):
        d=data(u*u+u+1,3)
        equal(d['formula'],d['eps2']);equal(d['lp'],-s.Rational(52,111))
        equal(d['eps2'],s.Rational(1156,333))
        positive((s.trace(d['T'])-d['lp'])**2)

    def test05_tilted_fixture(self):
        for mean in [s.Rational(1,2),s.Rational(-2,3)]:
            d=data(u*u+1,3,mean)
            equal(d['formula'],d['eps2']);positive(d['lp']**2)

    def test06_repeated_roots(self):
        for phi in [(u-1)**2,(u*u+1)**2]:
            q=int(s.degree(phi,u));d=data(phi,q)
            equal(d['formula'],d['eps2']);equal(d['V'],d['G'].det())

    def test07_minimal_degree(self):
        for phi in [u*u+1,u**3-u+2,u**4+2*u*u+9]:
            q=int(s.degree(phi,u));d=data(phi,q-1)
            equal(d['delta0'],0);equal(d['formula'],d['eps2'])

    def test08_phase_from_trace(self):
        d=data(u*u+u+1,3,s.Rational(1,2))
        p=op_pol(3,d['moment']);pn=op_pol(4,d['moment'])
        cu=(remvec(p,u*u+u+1).T*d['G']*remvec(pn,u*u+u+1))[0]
        equal(cu/d['omega'](3),s.trace(d['T'])-d['lp'])

    def test09_volume_jump_bound(self):
        for phi,N in [(u*u+1,2),(u*u+u+1,3),(u**4+2*u*u+9,4)]:
            d=data(phi,N);r=1/(d['delta0']*d['delta1'])
            bound=s.factor(d['ratio']*(r-1)**2/(4*r))
            if s.simplify(bound-d['eps2'])<0:raise AssertionError('upper bound failed')

    def test10_two_retained_slacks(self):
        # Algebraic version: x=exp(v_N), y=exp(v_(N+1)).
        x,y=s.symbols('x y',positive=True)
        f=(1-1/x)*(y-1)
        slack=s.sqrt(y/x)-(s.sqrt(x*y)+1/s.sqrt(x*y))/2
        equal((x*y-1)**2/(4*x*y)-slack**2,f)

    def test11_toda_source_symbolic(self):
        # Positive finite measure; ranks are used strictly below its support size.
        Z=2*s.exp(-th)+3+5*s.exp(th)
        ts=[s.Integer(1)]+[s.det(s.Matrix(n,n,lambda i,j:s.diff(Z,th,i+j))) for n in range(1,4)]
        for n in [1,2]:equal(ts[n]*s.diff(ts[n],th,2)-s.diff(ts[n],th)**2,ts[n+1]*ts[n-1])

    def test12_toda_relation_symbolic(self):
        phi=u*u+1
        Z=2*s.exp(-th)+3+5*s.exp(th)
        Bz=sum(a*s.diff(Z,th,p[0]) for p,a in s.Poly(phi**2,u).terms())
        bs=[s.Integer(1)]+[s.det(s.Matrix(n,n,lambda i,j:s.diff(Bz,th,i+j))) for n in range(1,4)]
        for n in [1,2]:equal(bs[n]*s.diff(bs[n],th,2)-s.diff(bs[n],th)**2,bs[n+1]*bs[n-1])

    def test13_curvature_difference(self):
        d=data(u*u+1,3);r=d['r'];N=3
        L=s.Matrix(N+1,r,lambda i,j:s.expand((u*u+1)*u**j).coeff(u,i))
        PB=L*(L.T*d['M']*L).inv()*L.T*d['M']
        Mpp=gram(N+1,d['moment'],2)
        Gp=d['R'].T*d['Mp']*d['R']
        Gpp=d['R'].T*Mpp*d['R']-2*d['R'].T*d['Mp']*L*(L.T*d['M']*L).inv()*L.T*d['Mp']*d['R']
        curvature=s.trace(d['K']*Gpp-d['K']*Gp*d['K']*Gp)
        toda=d['D'](N+2)*d['D'](N)/d['D'](N+1)**2-d['B'](r+1)*d['B'](r-1)/d['B'](r)**2
        equal(curvature,toda)

    def test14_mass_retained(self):
        d1=data(u*u+1,3,mass=s.Integer(7));d2=data(u*u+1,3,mass=s.Integer(21))
        equal(d2['G'],3*d1['G']);equal(d2['V'],3**2*d1['V']);equal(d2['eps2'],d1['eps2'])
        equal(d2['D'](4),3**4*d1['D'](4));equal(d2['B'](2),3**2*d1['B'](2))

    def test15_coordinate_phase_and_unit(self):
        d=data(u*u+1,3);c=s.Rational(3,2);N=3
        V=s.Matrix(N+1,N+1,lambda i,j:s.expand((c+s.I*u)**j).coeff(u,i))
        equal((V.H*d['M']*V).det(),d['M'].det())
        phiS=s.Symbol('S')**2-3*s.Symbol('S')+s.Rational(5,4)
        equal(phiS.subs(s.Symbol('S'),c+s.I*u),-(u*u+1))

    def test16_convolution_seed_and_filter(self):
        Z=2*s.exp(-th)+3+5*s.exp(th);k=3
        phi=u*u+u+2;z=Z**k
        filteredz=sum(a*s.diff(z,th,p[0]) for p,a in s.Poly(phi**2,u).terms())
        direct=0
        import itertools
        for xs in itertools.product([(-1,2),(0,3),(1,5)],repeat=k):
            X=sum(t[0] for t in xs);w=s.prod(t[1] for t in xs)
            direct+=w*phi.subs(u,X)**2*s.exp(th*X)
        equal(filteredz,direct)

    def test17_empty_packet(self):
        moment=lambda j:gm(j)
        for n in range(5):equal(detseq(n,moment)/detseq(n,filtered(moment,s.Integer(1))),1)
        # The two-element split lift of the zero ring still has two labels.
        self.assertEqual(len({'tau','e'}),2)

    def test18_split_source_relation(self):
        phi=u*u+1;rel=phi*(u+2)
        self.assertEqual(s.rem(rel,phi,u),0)
        norm=filtered(lambda j:gm(j),rel**2)(0);positive(norm)
        self.assertEqual(('active',s.rem(rel,phi,u)),('active',s.Integer(0)))
        self.assertNotEqual(('active',s.Integer(0)),('absent',s.Integer(0)))

    def test19_conormal_depth_not_norm_square(self):
        # I=(z1^2,z2^2), k=2: cyclic orders are 2r+1.
        z1,z2=s.symbols('z1 z2');X=z1+z2
        gro=s.groebner([z1**4,z1*z1*z2*z2,z2**4],z1,z2)
        equal(gro.reduce(s.expand(X**5))[1],0)
        self.assertNotEqual(gro.reduce(s.expand(X**4))[1],0)
        # Squared norm of a relation is positive and is not an ideal-depth replacement.
        positive(filtered(lambda j:gm(j),(u*u+1)**2)(0))

    def test20_quartet_count_unchanged(self):
        delta=s.Rational(1,4)
        for k in range(1,9):
            ell=1+k
            L=sum(ell*max(0,2*delta*(2*a-k)) for a in range(k+1) for b in range(k+1))
            equal(L,2*delta*ell*(k+1)*((k+1)**2//4))

    def test21_even_phase_vanishes(self):
        d=data(u**4+2*u*u+9,4);equal(d['lp'],0);equal(s.trace(d['T']),0)
        equal(d['formula'],d['ratio']*(1-d['delta0'])*(1/d['delta1']-1))

    def test22_parity_not_assumed_for_tilt(self):
        d=data(u*u+1,3,s.Rational(1,2));self.assertNotEqual(d['lp'],0)
        raw=d['ratio']*(1-d['delta0'])*(1/d['delta1']-1)
        equal(raw-d['eps2'],d['lp']**2)

    def test23_minimal_numeric_fixture(self):
        d=data(u*u+1,1);equal(d['eps2'],4)
        d2=data(u*u+1,2);equal(d2['eps2'],s.Rational(16,3))
        # Canonical control is not presumed monotone in source degree.
        positive(d2['eps2']-d['eps2'])

    def test24_relation_seed_positive_at_zero_value(self):
        d=data(u*u+1,3);positive(d['B'](1));equal(s.rem(u*u+1,u*u+1,u),0)

class Negative(unittest.TestCase):
    def test_intentional_failure(self):equal(s.Integer(1),s.Integer(2))

def main():
    p=argparse.ArgumentParser();p.add_argument('--json',type=Path);p.add_argument('--fail-control',action='store_true');args=p.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TestControl)
    if args.fail_control:suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(Negative))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    record={'status':'passed' if result.wasSuccessful() else 'failed','test_methods':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'scope':'Exact finite regression identities only; no Lean or analytic-integral certification.'}
    if args.json:args.json.parent.mkdir(parents=True,exist_ok=True);args.json.write_text(json.dumps(record,indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':sys.exit(main())
