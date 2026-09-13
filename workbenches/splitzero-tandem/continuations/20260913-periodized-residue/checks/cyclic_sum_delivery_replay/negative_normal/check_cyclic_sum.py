#!/usr/bin/env python3
"""Exact finite checks. Algebraic calibration inputs are not asserted zeta zeros.
No Python `assert` statements are used. --fail-control deliberately fails.
"""
from __future__ import annotations
import argparse, itertools, json, math, sys, unittest
from functools import lru_cache
from pathlib import Path
import sympy as sp
S,z = sp.symbols('S z')
I=sp.I

def eq(a,b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        aa,bb=sp.Matrix(a),sp.Matrix(b)
        if aa.shape != bb.shape or any(sp.simplify(x)!=0 for x in aa-bb):
            raise AssertionError(f'matrix mismatch {aa.shape}, {bb.shape}: {aa-bb}')
    elif sp.simplify(a-b)!=0:
        raise AssertionError(f'{a} != {b}')

def remvec(P,chi):
    q=sp.degree(chi,S)
    p=sp.Poly(sp.rem(sp.expand(P),chi,S),S)
    return sp.Matrix([p.nth(i) for i in range(q)])

def companion(chi):
    q=sp.degree(chi,S)
    return sp.Matrix.hstack(*[remvec(S**(j+1),chi) for j in range(q)])

def tuple_exponent(ms,r):
    return 1+sum(m-1 for m in ms)+(r-1)*max(ms)

def sum_data(roots,k,r=1):
    exps={}; dims={}
    for idx in itertools.product(range(len(roots)), repeat=k):
        lam=sp.simplify(sum(roots[j][0] for j in idx))
        ms=[roots[j][1] for j in idx]
        exps[lam]=max(exps.get(lam,0),tuple_exponent(ms,r))
        if r==1: dims[lam]=dims.get(lam,0)+math.prod(ms)
    chi=sp.expand(sp.prod((S-lam)**m for lam,m in exps.items()))
    return chi,exps,dims

def local_basis(ms,r):
    return [a for a in itertools.product(*[range(r*m) for m in ms])
            if sum(a[i]//ms[i] for i in range(len(ms)))<r]

def nilpotent_power(ms,r,p):
    basis=set(local_basis(ms,r))
    out={tuple(0 for _ in ms):sp.Integer(1)}
    for _ in range(p):
        nxt={}
        for a,c in out.items():
            for i in range(len(ms)):
                b=tuple(v+(j==i) for j,v in enumerate(a))
                if b in basis:nxt[b]=nxt.get(b,0)+c
        out=nxt
    return out

def tensor_sum(A,k):
    d=A.rows
    return sum((sp.kronecker_product(*[A if j==i else sp.eye(d) for j in range(k)])
                for i in range(k)),sp.zeros(d**k))

def orbit_inclusion(d,k):
    basis=list(itertools.product(range(d),repeat=k)); idx={a:i for i,a in enumerate(basis)}
    occupations=sorted(set(tuple(sorted(a)) for a in basis))
    cols=[]
    for a in occupations:
        col=sp.zeros(d**k,1)
        for b in set(itertools.permutations(a)):col[idx[b]]=1
        cols.append(col)
    return sp.Matrix.hstack(*cols)

def matrix_eval(P,A):
    p=sp.Poly(P,S)
    return sum((p.nth(i)*A**i for i in range(p.degree()+1)),sp.zeros(A.rows))

@lru_cache(None)
def gaussian_packet(chi,k,N,mass=sp.Integer(3)):
    chi=sp.expand(chi); A=companion(chi); center=sp.Rational(k,2)
    ps=[sp.Integer(1)]
    if N+1>=1:ps.append(S-center)
    for n in range(1,N+1):ps.append(sp.expand((S-center)*ps[-1]+k*n*ps[-2]))
    omegas=[mass**k*sp.Integer(k)**n*sp.factorial(n) for n in range(N+2)]
    bs=[remvec(p,chi) for p in ps]
    K=sum((bs[n]*bs[n].H/omegas[n] for n in range(N+1)),sp.zeros(A.rows))
    G=sp.simplify(K.inv()); Z=sp.simplify(A*K+K*A.H-k*K); W=sp.simplify(G*Z*G)
    return A,ps,omegas,bs,K,G,Z,W

def gauss_moment(n):
    return sp.Integer(0) if n%2 else (sp.factorial2(n-1) if n else sp.Integer(1))

def mass_moment_sequence(n,kind='vacuum',mass=sp.Integer(3)):
    mu=[];nu=[]
    for j in range(n+1):
        if kind=='vacuum':
            mu.append(mass*gauss_moment(j))
            nu.append(mass*gauss_moment(j+2)/4)
        else:
            mu.append(mass*gauss_moment(j+2))
            nu.append(mass*(gauss_moment(j)-gauss_moment(j+2)+gauss_moment(j+4)/4))
    return mu,nu

def formal_product_moments(mu,nu,k,n):
    M=sum(mu[j]*z**j/sp.factorial(j) for j in range(n+1))
    V=sum(nu[j]*z**j/sp.factorial(j) for j in range(n+1))
    mass=sp.series(M**k,z,0,n+1).removeO().expand()
    der=sp.series(V*M**(k-1)/k+sp.Rational(k-1,4*k)*z*z*M**k,z,0,n+1).removeO().expand()
    return ([mass.coeff(z,j)*sp.factorial(j) for j in range(n+1)],
            [der.coeff(z,j)*sp.factorial(j) for j in range(n+1)])

def integrate_poly_gauss(P,vars,mass=sp.Integer(3)):
    p=sp.Poly(sp.expand(P),*vars)
    return sp.simplify(mass**len(vars)*sum(c*sp.prod(gauss_moment(v) for v in powers)
                                        for powers,c in p.terms()))

def inner_from_moments(P,Q,mom):
    u=sp.Symbol('u',real=True)
    p=sp.Poly(sp.expand(sp.conjugate(P)*Q),u)
    return sp.simplify(sum(c*mom[e[0]] for e,c in p.terms()))

class ExactChecks(unittest.TestCase):
    def test_local_basis_dimension(self):
        for ms in ((1,1),(2,2),(2,3),(1,3,2)):
            for r in range(1,4):
                self.assertEqual(len(local_basis(ms,r)),math.prod(ms)*math.comb(r+len(ms)-1,len(ms)))
    def test_exact_nilpotence_at_every_depth(self):
        for ms in ((1,1),(2,2),(2,3),(1,2,2)):
            for r in range(1,4):
                ell=tuple_exponent(ms,r)
                self.assertTrue(nilpotent_power(ms,r,ell-1))
                self.assertFalse(nilpotent_power(ms,r,ell))
    def test_collision_minimal_polynomial(self):
        roots=((sp.Rational(1,4),1),(sp.Rational(1,2),1),(sp.Rational(3,4),1))
        chi,exps,dims=sum_data(roots,2)
        self.assertEqual(len(exps),5); self.assertEqual(sum(dims.values()),9)
        h=sp.prod(S-a for a,m in roots); A=tensor_sum(companion(h),2)
        eq(matrix_eval(chi,A),sp.zeros(9))
        U=matrix_eval(2+S,companion(h)); seed=sp.kronecker_product(U[:,0],U[:,0])
        C=sp.Matrix.hstack(*[A**j*seed for j in range(sp.degree(chi,S))])
        self.assertEqual(C.rank(),5)
        eq(A*C,C*companion(chi))
    def test_symmetric_cyclic_trace_complement(self):
        roots=((sp.Rational(1,4),1),(sp.Rational(1,2),1),(sp.Rational(3,4),1))
        h=sp.prod(S-a for a,m in roots); A=tensor_sum(companion(h),2)
        inc=orbit_inclusion(3,2); left=(inc.T*inc).inv()*inc.T
        As=left*A*inc; eq(A*inc,inc*As)
        chi,_,_=sum_data(roots,2); Ac=companion(chi)
        for j in range(6):eq(sp.trace(As**j)-sp.trace(Ac**j),1)
        eq(As.charpoly(S).as_expr(),chi*(S-1))
    def test_repeated_root_complement(self):
        h=(S-sp.Rational(1,2))**3; A=tensor_sum(companion(h),2)
        inc=orbit_inclusion(3,2); As=(inc.T*inc).inv()*inc.T*A*inc
        chi,_,_=sum_data(((sp.Rational(1,2),3),),2)
        self.assertEqual(sp.degree(chi,S),5); eq(As.charpoly(S).as_expr(),(S-1)**6)
        eq(matrix_eval(chi,A),sp.zeros(9))
    def test_naive_power_to_actual_thickening(self):
        X=S-1
        for r in range(1,5):
            chi,_,_=sum_data(((sp.Rational(1,2),2),),2,r)
            eq(chi,X**(2*r+1))
        self.assertTrue(nilpotent_power((2,2),2,4));self.assertFalse(nilpotent_power((2,2),2,5))
        eq(sp.rem(X**6,X**5,S),0)
        self.assertNotEqual(sp.rem(X**5,X**6,S),0)
    def test_derivative_tower(self):
        roots=((sp.Rational(1,4),1),(sp.Rational(1,2),2),(sp.Rational(3,4),1))
        for r in (1,2):
            chi,_,_=sum_data(roots,2,r); nxt,_,_=sum_data(roots,2,r+1)
            eq(sp.rem(sp.diff(nxt,S),chi,S),0)
            eq(sp.rem(nxt,chi,S),0)
    def test_e_relation_has_nonzero_derivative(self):
        X=S-1; low=X**3; high=X**5; rel=X**3
        eq(sp.rem(rel,low,S),0)
        self.assertNotEqual(sp.rem(rel,high,S),0)
        eq(sp.rem(sp.diff(rel,S),low,S),3*X**2)
    def test_conormal_row_for_sum_relation(self):
        x,y=sp.symbols('x y'); f=(x+y)**3
        quotients=(x+3*y,3*x+y)
        eq(f,x*x*quotients[0]+y*y*quotients[1])
        delta=lambda p:(sp.diff(p,x)+sp.diff(p,y))/2
        row=x*quotients[0]+y*quotients[1]
        GB=sp.groebner([x*x,y*y],x,y)
        eq(GB.reduce(sp.expand(delta(f)-row))[1],0)
    def test_weighted_unit_product_rule(self):
        x,y=sp.symbols('x y'); U=(2+x)*(3+y); f=(x+y)**3
        delta=lambda p:(sp.diff(p,x)+sp.diff(p,y))/2
        eq(delta(U*f),U*delta(f)+delta(U)*f)
    def test_exact_kernel_formula(self):
        chi=(S-1)**3;k=2;N=4
        A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,k,N)
        moments=[sp.Integer(3)**k*sp.Integer(k)**(j//2)*gauss_moment(j) if j%2==0 else 0 for j in range(2*N+1)]
        u=sp.Symbol('u',real=True);c=sp.Rational(k,2)
        M=sp.Matrix(N+1,N+1,lambda i,j:inner_from_moments((c+I*u)**i,(c+I*u)**j,moments))
        J=sp.Matrix.hstack(*[remvec(S**j,chi) for j in range(N+1)])
        eq(K,J*M.inv()*J.H)
    def test_minimum_and_degree_transition(self):
        chi=(S-1)**3;k=2;N=3
        A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,k,N)
        _,_,_,_,K2,G2,_,_=gaussian_packet(chi,k,N+1)
        f=bs[N+1];hh=om[N+1]+(f.H*G*f)[0]
        eq(K2,K+f*f.H/om[N+1]);eq(G2,G-G*f*f.H*G/hh)
    def test_control_rank_two(self):
        for chi,k,N in (((S-1)**3,2,4),((S-sp.Rational(1,2))*(S-1)*(S-sp.Rational(3,2)),2,4),((S-sp.Rational(3,2))**4,3,5)):
            A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,k,N)
            expected=(bs[N+1]*bs[N].H+bs[N]*bs[N+1].H)/om[N]
            eq(Z,expected);eq(W,A.H*G+G*A-k*G)
            self.assertLessEqual(Z.rank(),2)
    def test_exact_two_by_two_control(self):
        chi=(S-sp.Rational(1,2))*(S-1)*(S-sp.Rational(3,2));k=2;N=4
        A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,k,N)
        B=sp.Matrix.hstack(bs[N],bs[N+1]); gram=B.H*G*B
        eps2=sp.simplify(gram.det()/om[N]**2)
        R=sp.simplify(K*W)
        eq(sp.trace(R),0);eq(sp.trace(R*R),2*eps2)
        eq(R.charpoly(z).as_expr(),z*(z*z-eps2))
    def test_reflection_with_nonzero_imaginary_cross_term(self):
        chi=(S-(sp.Rational(1,2)+2*I))*(S-(1+2*I))*(S-(sp.Rational(3,2)+2*I))
        A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,2,3)
        cross=(bs[3].H*G*bs[4])[0]
        eq(sp.re(cross),0)
        C=sp.Matrix.hstack(*[remvec((2-S)**j,chi) for j in range(3)])
        eq(C.H*G*C,sp.conjugate(G));eq(C.H*W*C,-sp.conjugate(W))
    def test_amplified_off_line_eigenvalue_not_removed(self):
        roots=((sp.Rational(1,4),1),(sp.Rational(3,4),1));chi,exps,_=sum_data(roots,3)
        self.assertIn(sp.Rational(3,4),exps);self.assertIn(sp.Rational(9,4),exps)
        A,ps,om,bs,K,G,Z,W=gaussian_packet(chi,3,4)
        for val, mult, vects in A.eigenvects():
            v=vects[0];eq((v.H*W*v)[0],(2*sp.re(val)-3)*(v.H*G*v)[0])
    def test_raw_convolution_moments(self):
        mu,nu=mass_moment_sequence(8,'zero')
        mom,b=formal_product_moments(mu,nu,3,6)
        ts=sp.symbols('t0:3',real=True);u=sum(ts);base=sp.prod(ts)
        for r in range(7):eq(mom[r],integrate_poly_gauss(u**r*base**2,ts))
        eq(mom[0],mu[0]**3)
    def test_full_derivative_moment_formula(self):
        for k in (2,3):
            mu,nu=mass_moment_sequence(8,'zero');mom,b=formal_product_moments(mu,nu,k,4)
            ts=sp.symbols('t0:'+str(k),real=True);u=sum(ts);base=sp.prod(ts)
            deriv=(sum(sp.diff(base,t) for t in ts)-u*base/2)/k
            for r in range(5):eq(b[r],integrate_poly_gauss(u**r*deriv**2,ts))
            eq(b[0],nu[0]*mu[0]**(k-1)/k)
    def test_polynomial_graph_energy_with_all_cross_terms(self):
        k=2;mu,nu=mass_moment_sequence(10,'zero');mom,b=formal_product_moments(mu,nu,k,8)
        ts=sp.symbols('t0:2',real=True);u=sum(ts);base=sp.prod(ts);c=sp.Integer(1)
        for p in range(3):
            for q in range(3):
                P=(c+I*u)**p;Q=(c+I*u)**q
                dp=(sum(sp.diff(base*P,t) for t in ts)-u*base*P/2)/k
                dq=(sum(sp.diff(base*Q,t) for t in ts)-u*base*Q/2)/k
                direct=integrate_poly_gauss(sp.conjugate(dp)*dq,ts)
                uu=sp.Symbol('u',real=True);P1=(c+I*uu)**p;Q1=(c+I*uu)**q
                # Expanded four-term identity; real-line derivatives retained.
                crossmom=[-(r* mom[r-1])/2 if r else 0 for r in range(len(mom))]
                expected=inner_from_moments(P1,Q1,b)+inner_from_moments(sp.diff(P1,uu),sp.diff(Q1,uu),mom)
                expected+=inner_from_moments(P1,sp.diff(Q1,uu),crossmom)+inner_from_moments(sp.diff(P1,uu),Q1,crossmom)
                eq(direct,expected)
    def test_source_seed_packet_naturality(self):
        x,y=sp.symbols('x y');h=(S-sp.Rational(1,4))*(S-sp.Rational(3,4)); H=h*(S-sp.Rational(1,2))
        m=sp.cancel(H/h);a=m.subs(S,x)*m.subs(S,y)
        for p in (sp.Integer(1),S,S*S):
            left=a*p.subs(S,x+y)
            eq((x+y)*left,a*(S*p).subs(S,x+y))
        # A scalar-sum seed is generally not a polynomial of S alone.
        ss,rr=sp.symbols('ss rr');expr=sp.expand(a.subs({x:(ss+rr)/2,y:(ss-rr)/2},simultaneous=True))
        self.assertNotEqual(sp.diff(expr,rr),0)
    def test_split_zero_quotient_and_derivative_types(self):
        # External absence is None; supported field values are tuples.
        tau=None;e=('supported',sp.Integer(0))
        lift=lambda f:lambda x:None if x is None else ('supported',sp.expand(f(x[1])))
        X=S-1;rel=('supported',X**3)
        quotient=lift(lambda p:sp.rem(p,X**3,S));derivative=lift(lambda p:sp.rem(sp.diff(p,S),X**3,S))
        self.assertEqual(quotient(rel),e); self.assertIsNone(quotient(tau));self.assertIsNone(derivative(tau))
        self.assertNotEqual(derivative(rel),e);self.assertNotEqual(e,tau)
    def test_explicit_equivariant_retraction_retains_complement(self):
        X=sp.Symbol('X')
        N0=sp.Matrix([[0,0,0],[1,0,0],[0,1,0]])
        N=tensor_sum(N0,2);inc=orbit_inclusion(3,2);left=(inc.T*inc).inv()*inc.T
        Ns=left*N*inc
        unit=sp.Matrix([2,1,0]);w=left*sp.kronecker_product(unit,unit)
        ell=5; eta=sp.Matrix.hstack(*[Ns**j*w for j in range(ell)])
        theta=sp.zeros(1,6);theta[0,5]=1
        pi0=sp.Matrix.vstack(*[theta*Ns**(ell-1-j) for j in range(ell)])
        pv=pi0*w; poly=sum(pv[j]*X**j for j in range(ell))
        self.assertNotEqual(poly.subs(X,0),0)
        inv=sp.invert(poly,X**ell,X)
        Nc=sp.zeros(ell)
        for j in range(ell-1):Nc[j+1,j]=1
        mult=sp.zeros(ell)
        for j in range(ell):
            rr=sp.Poly(sp.rem(inv*X**j,X**ell,X),X)
            for i in range(ell):mult[i,j]=rr.nth(i)
        pi=mult*pi0;eq(pi*eta,sp.eye(ell));eq(pi*Ns,Nc*pi)
        eq((eta*pi)**2,eta*pi);eq(Ns*eta*pi,eta*pi*Ns)
        K=sp.Matrix.hstack(*pi.nullspace());self.assertEqual(K.cols,1)
        U=eta.row_join(K);self.assertEqual(U.rank(),6)
        H=sp.diag(*range(1,7)); self.assertTrue(any(x!=0 for x in eta.H*H*K))
    def test_cyclic_full_minimum_pythagoras(self):
        M=sp.diag(2,3,5,7,11)
        J=sp.Matrix([[1,0,1,0,1],[0,1,0,1,1]])
        T=sp.Matrix([[1,0,0],[0,1,0],[1,0,1],[0,1,1],[0,0,1]])
        K=J*M.inv()*J.T;R=M.inv()*J.T*K.inv()
        Mc=T.T*M*T;Jc=J*T
        Rc=T*Mc.inv()*Jc.T*(Jc*Mc.inv()*Jc.T).inv()
        delta=Rc-R
        eq(J*delta,sp.zeros(2));eq(R.T*M*delta,sp.zeros(2))
        eq(Rc.T*M*Rc,R.T*M*R+delta.T*M*delta)
    def test_negative_control(self):
        if FORCE_FAILURE:raise AssertionError('deliberate failure-control triggered')

FORCE_FAILURE=False
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--json',type=Path);ap.add_argument('--fail-control',action='store_true')
    args=ap.parse_args();FORCE_FAILURE=args.fail_control
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks))
    record={'test_methods':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'success':result.wasSuccessful(),'deliberate_failure':args.fail_control,'scope':'exact finite algebraic calibrations; no zeta-zero locations or analytic estimates certified'}
    if args.json:args.json.write_text(json.dumps(record,indent=2)+'\n')
    sys.exit(0 if result.wasSuccessful() else 1)
