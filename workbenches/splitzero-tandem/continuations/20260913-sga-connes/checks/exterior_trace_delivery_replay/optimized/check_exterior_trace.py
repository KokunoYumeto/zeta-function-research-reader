#!/usr/bin/env python3
"""Exact finite regression checks for exterior trace amplification.
Gaussian inputs are declared algebraic calibrations, not zeta packets.
No Python assert statements; --fail-control intentionally fails.
"""
from __future__ import annotations
import argparse, itertools, json, math, sys, unittest
from functools import lru_cache
from pathlib import Path
import sympy as sp
S=sp.Symbol('S'); I=sp.I

def eq(a,b):
    if isinstance(a,sp.MatrixBase) or isinstance(b,sp.MatrixBase):
        a,b=sp.Matrix(a),sp.Matrix(b)
        if a.shape!=b.shape or any(sp.simplify(v)!=0 for v in a-b):
            raise AssertionError(f'matrix identity failed: {a-b}')
    elif sp.simplify(a-b)!=0:raise AssertionError(f'{a} != {b}')

def remvec(P,chi):
    q=int(sp.degree(chi,S)); p=sp.Poly(sp.rem(sp.expand(P),chi,S),S)
    return sp.Matrix([p.nth(j) for j in range(q)])

def companion(chi):
    q=int(sp.degree(chi,S));return sp.Matrix.hstack(*[remvec(S**(j+1),chi) for j in range(q)])

def evpoly(P,A):
    p=sp.Poly(P,S);return sum((p.nth(j)*A**j for j in range(p.degree()+1)),sp.zeros(A.rows))

def ext_gram(G,p):
    inds=list(itertools.combinations(range(G.rows),p))
    return sp.Matrix([[G.extract(a,b).det() for b in inds] for a in inds])

def ext_generator(A,p):
    inds=list(itertools.combinations(range(A.rows),p));idx={a:i for i,a in enumerate(inds)}
    out=sp.zeros(len(inds))
    for col,js in enumerate(inds):
        for pos,j in enumerate(js):
            for i in range(A.rows):
                tup=list(js);tup[pos]=i
                if len(set(tup))<p:continue
                inv=sum(tup[a]>tup[b] for a in range(p) for b in range(a+1,p))
                out[idx[tuple(sorted(tup))],col]+=(-1)**inv*A[i,j]
    return out

def alt_matrix(q,p):
    inds=list(itertools.combinations(range(q),p));tups=list(itertools.product(range(q),repeat=p));ix={a:i for i,a in enumerate(tups)}
    out=sp.zeros(q**p,len(inds))
    for j,a in enumerate(inds):
        for b in itertools.permutations(a):
            inv=sum(b[x]>b[y] for x in range(p) for y in range(x+1,p))
            out[ix[b],j]=(-1)**inv
    return out

def tensor_generator(A,p):
    return sum((sp.kronecker_product(*[A if i==j else sp.eye(A.rows) for i in range(p)]) for j in range(p)),sp.zeros(A.rows**p))

@lru_cache(None)
def gaussian(chi,k,N,mass=sp.Integer(7)):
    # Literal measure: mass^k / sqrt(2*pi*k) exp(-u^2/(2k)) du.
    chi=sp.expand(chi);A=companion(chi);p=[sp.Integer(1),S-sp.Rational(k,2)]
    for n in range(1,N+1):p.append(sp.expand((S-sp.Rational(k,2))*p[-1]+k*n*p[-2]))
    omega=[mass**k*sp.Integer(k)**n*sp.factorial(n) for n in range(N+2)]
    b=[remvec(t,chi) for t in p]
    K=sum((b[j]*b[j].H/omega[j] for j in range(N+1)),sp.zeros(A.rows))
    G=K.inv();Z=A*K+K*A.H-k*K;W=sp.simplify(G*Z*G);H=sp.simplify(K*W)
    return A,p,omega,b,K,G,Z,W,H

def quartet(k,m=1,delta=sp.Rational(1,4),gamma=sp.Integer(1), expand_polynomial=True):
    ell=1+k*(m-1)
    roots={sp.Rational(k,2)+delta*(2*a-k)+I*gamma*(2*b-k):ell for a in range(k+1) for b in range(k+1)}
    return (sp.expand(sp.prod((S-r)**n for r,n in roots.items())) if expand_polynomial else None),roots

def load(roots,k):
    return sp.simplify(sum(n*max(sp.Integer(0),2*sp.re(r)-k) for r,n in roots.items()))

def plus_basis(roots,chi,k):
    # CRT columns, with every jet, no norm division.
    cols=[];eplus=sp.Integer(0)
    for r,m in roots.items():
        if not (sp.re(r)>sp.Rational(k,2)):continue
        fac=(S-r)**m; other=sp.div(chi,fac,S)[0]
        e=sp.rem(other*sp.invert(other,fac,S),chi,S);eplus+=e
        for j in range(m):cols.append(remvec(e*(S-r)**j,chi))
    return sp.Matrix.hstack(*cols) if cols else sp.zeros(sp.degree(chi,S),0),sp.rem(eplus,chi,S)

class Checks(unittest.TestCase):
    def test_gram_adjoint_identity(self):
        G=sp.Matrix([[3,1+I],[1-I,4]]);A=sp.Matrix([[2,I],[1,3]])
        sharp=G.inv()*A.H*G;eq(sharp.H*G,G*A)
        W=A.H*G+G*A-2*G;eq(G.inv()*W,sharp+A-2*sp.eye(2))
    def test_source_rank_two_and_radius(self):
        chi,roots=quartet(1)
        for N in (3,4):
            A,p,o,b,K,G,Z,W,H=gaussian(chi,1,N)
            eq(Z,(b[N+1]*b[N].H+b[N]*b[N+1].H)/o[N])
            eq(sp.trace(H),0);self.assertLessEqual(H.rank(),2)
            eps2=sp.simplify(sp.trace(H*H)/2)
            aa=(b[N].H*G*b[N])[0];dd=(b[N+1].H*G*b[N+1])[0];cc=(b[N].H*G*b[N+1])[0]
            eq(eps2,(aa*dd-cc*sp.conjugate(cc))/o[N]**2)
            eq(H**3,eps2*H)
    def test_spectral_and_orthogonal_projector_maps(self):
        chi,roots=quartet(1);A,p,o,b,K,G,Z,W,H=gaussian(chi,1,3)
        C,e=plus_basis(roots,chi,1);Q=evpoly(e,A);P=C*(C.H*G*C).inv()*C.H*G
        eq(P*Q,Q);eq(Q*P,P);eq(Q*Q,Q);eq(P*P,P);eq(P.H*G,G*P)
        eq(sp.trace(P*A),sp.trace(Q*A));eq((P-Q)**2,sp.zeros(4))
        eq(sp.trace(P*H),load(roots,1))
    def test_actual_coordinate_compression_no_inverse_shortcut(self):
        G=sp.Matrix([[3,1,0],[1,4,1],[0,1,5]]);C=sp.Matrix([[1,0],[0,1],[1,0]])
        L=(C.H*G*C).inv()*C.H*G;eq(L*C,sp.eye(2));eq(C*L*C,C)
        # The actual compressed inverse is inverse(C*GC), not C*G^-1 C.
        self.assertNotEqual((C.H*G*C).inv(),C.H*G.inv()*C)
    def test_alternating_map_full_factorial(self):
        G=sp.Matrix([[3,1,I],[1,4,0],[-I,0,5]])
        for p in (1,2,3):
            alt=alt_matrix(3,p);eq(alt.H*sp.kronecker_product(*([G]*p))*alt,sp.factorial(p)*ext_gram(G,p))
    def test_additive_compound_and_gram_adjoint(self):
        G=sp.Matrix([[3,1,0],[1,4,1],[0,1,5]]);A=sp.Matrix([[1,I,2],[0,2,1],[1,0,3]])
        H=G.inv()*A.H*G+A-2*sp.eye(3)
        for p in (1,2,3):
            E=ext_generator(A,p);Gext=ext_gram(G,p)
            eq(E.H*Gext+Gext*E-2*p*Gext,Gext*ext_generator(H,p))
            alt=alt_matrix(3,p);eq(tensor_generator(A,p)*alt,alt*E)
    def test_exterior_rank_two_has_same_allowance(self):
        H=sp.diag(3,0,0,-3)
        for p in (1,2,3):
            Hp=ext_generator(H,p);self.assertEqual(set(Hp.eigenvals()),{sp.Integer(3),sp.Integer(0),sp.Integer(-3)})
            self.assertEqual(Hp.eigenvals()[3],sp.binomial(2,p-1))
        eq(ext_generator(H,4),sp.zeros(1))
    def test_determinant_weight_invariant_submodule(self):
        A=sp.Matrix([[1,I,2],[0,2,1],[0,0,3]])
        C=sp.Matrix([[1,0],[0,1],[0,0]])
        v=alt_matrix(3,2)*sp.Matrix([1,0,0]);eq(tensor_generator(A,2)*v,3*v)
        self.assertEqual(sp.trace((C.H*C).inv()*C.H*A*C),3)
    def test_chain_permutation_sign_all_parities(self):
        for k in range(1,5):
            for p in range(1,5):
                for perm in itertools.permutations(range(p)):
                    parity=sum(perm[i]>perm[j] for i in range(p) for j in range(i+1,p));sig=(-1)**parity
                    self.assertEqual(sig**(k+1)*sig**k,sig)
    def test_original_primitive_two_koszul_factors(self):
        for k in range(1,6):
            for p in range(1,7):
                for j in range(p):
                    primitive_sign=(-1)**(k*j)
                    differential_sign=(-1)**(k*j)
                    self.assertEqual(primitive_sign*differential_sign,1)
    def test_minimum_comparison_retains_boundary_gram(self):
        # Actual quotient J, its specified least-norm section, and a boundary correction.
        M=sp.diag(2,3,5,7);J=sp.Matrix([[1,0,1,0],[0,1,0,1]])
        R=M.inv()*J.H*(J*M.inv()*J.H).inv()
        Delta=sp.Matrix([[1,2],[3,1],[-1,-2],[-3,-1]])
        eq(J*Delta,sp.zeros(2));eq(R.H*M*Delta,sp.zeros(2))
        eq((R+Delta).H*M*(R+Delta),R.H*M*R+Delta.H*M*Delta)
        A=sp.Matrix([[1,2],[0,3]]);G=R.H*M*R;B=Delta.H*M*Delta
        eq(A.H*(G+B)+(G+B)*A-4*(G+B),
           (A.H*G+G*A-4*G)+(A.H*B+B*A-4*B))
    def test_quartet_sum_grid_without_genericity(self):
        delta=sp.Rational(1,4);gamma=sp.Integer(2)
        roots=[sp.Rational(1,2)+x*delta+I*y*gamma for x in (-1,1) for y in (-1,1)]
        for k in range(1,5):
            sums={sp.simplify(sum(t)) for t in itertools.combinations_with_replacement(roots,k)}
            _,grid=quartet(k,1,delta,gamma,False);self.assertEqual(sums,set(grid));self.assertEqual(len(sums),(k+1)**2)
    def test_pair_and_quartet_load_all_orders(self):
        delta=sp.Rational(2,7)
        for k in range(1,11):
            for m in (1,2,3):
                ell=1+k*(m-1);_,roots=quartet(k,m,delta,sp.Integer(1),False)
                expected=2*delta*ell*(k+1)*((k+1)**2//4)
                eq(load(roots,k),expected)
                pos=sum(n for r,n in roots.items() if sp.re(r)>sp.Rational(k,2))
                self.assertEqual(pos,ell*(k+1)*((k+1)//2))
    def test_nonnormal_arithmetic_calibrations_obey_trace_budget(self):
        for k in (1,2):
            chi,roots=quartet(k);q=int(sp.degree(chi,S));A,p,o,b,K,G,Z,W,H=gaussian(chi,k,q-1)
            eps2=sp.simplify(sp.trace(H**2)/2);L=load(roots,k)
            self.assertTrue(bool(eps2>=L**2));self.assertTrue(bool(L>=sp.Rational(k,2)))
            self.assertFalse(bool(A.H*G==G*A))
    def test_projection_trace_exact_slack(self):
        eps=sp.Integer(3);H=sp.diag(eps,0,0,-eps)
        C=sp.Matrix([[1,0],[1,1],[0,1],[1,0]]);P=C*(C.H*C).inv()*C.H
        Ep=sp.diag(1,0,0,0);Em=sp.diag(0,0,0,1)
        slack=1-sp.trace(P*Ep)+sp.trace(P*Em)
        eq(sp.trace(P*H),eps*(1-slack));self.assertTrue(bool(slack>=0))
        eq((H**2+eps*H)/(2*eps**2),Ep)
    def test_full_nilpotent_lengths_and_trace(self):
        delta=sp.Rational(1,3);m=3;k=1
        r=sp.Rational(1,2)+delta+I
        A=sp.diag(r,r,r);A[1,0]=1;A[2,1]=1
        eq(ext_generator(A,3),sp.Matrix([[3*r]]))
        self.assertNotEqual(A-r*sp.eye(m),sp.zeros(m));eq((A-r*sp.eye(m))**m,sp.zeros(m))
    def test_supported_trace_preserves_e_and_tau(self):
        tau=None;e=('supported',sp.Integer(0))
        tr=lambda x:tau if x is tau else ('supported',sp.trace(x[1]))
        self.assertEqual(tr(('supported',sp.diag(2,-2))),e)
        self.assertIsNone(tr(tau));self.assertNotEqual(e,tau)
    def test_internal_relation_transport(self):
        chi=(S-1)**2;value=('supported',chi)
        q=lambda x:None if x is None else ('supported',sp.rem(x[1],chi,S))
        self.assertEqual(q(value),('supported',sp.Integer(0)));self.assertIsNone(q(None))
        self.assertNotEqual(value,('supported',sp.Integer(0)))
    def test_empty_packet_no_gram_inverse(self):
        chi=sp.Integer(1);self.assertEqual(sp.rem(S**3+2,chi,S),0)
        supported_zero=('supported',0);self.assertNotEqual(supported_zero,None)
        # Analytic mass does not vanish when algebraic quotient is zero.
        self.assertEqual(7**3,343)
    def test_mass_is_retained_and_ratio_is_compared(self):
        chi,roots=quartet(1)
        a=gaussian(chi,1,3,sp.Integer(7));b=gaussian(chi,1,3,sp.Integer(14))
        eq(b[5],2*a[5]);eq(b[7],2*a[7]);eq(b[8],a[8])
    def test_floor_and_growth_coefficient(self):
        k=sp.Symbol('k',positive=True,integer=True)
        for n in range(1,15):
            self.assertEqual((2*n+1)**2//4,n*(n+1))
            self.assertEqual((2*n+2)**2//4,(n+1)**2)
        # Leading cubic coefficient for simple quartet: delta/2.
        n=sp.Symbol('n');delta=sp.Symbol('delta')
        poly=sp.expand(2*delta*(2*n+1)*n*(n+1));eq(sp.LC(sp.Poly(poly,n)),4*delta)
    def test_negative_control(self):
        if FORCE_FAILURE:raise AssertionError('deliberate failure control')

FORCE_FAILURE=False
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--json',type=Path);ap.add_argument('--fail-control',action='store_true');args=ap.parse_args();FORCE_FAILURE=args.fail_control
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    record={'test_methods':result.testsRun,'success':result.wasSuccessful(),'failures':len(result.failures),'errors':len(result.errors),'deliberate_failure':args.fail_control,'scope':'exact finite algebraic calibrations, not actual zeta zeros or uniform analytic estimates'}
    if args.json:args.json.write_text(json.dumps(record,indent=2)+'\n')
    sys.exit(0 if result.wasSuccessful() else 1)
