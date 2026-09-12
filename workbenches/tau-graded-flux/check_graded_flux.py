#!/usr/bin/env python3
"""Exact finite regressions for the graded theta comparison.

All measures and packet polynomials used here are declared calibrations, not
measurements or certificates of Riemann-zeta zeros. No analytic theorem is
validated by the finite tests. There are no Python assert statements.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
import sys
import unittest
from functools import lru_cache
from pathlib import Path
import sympy as S

z, y = S.symbols('z y', real=True)
HALF = S.Rational(1, 2)
I = S.I


def simp(x):
    return S.expand(x)


def matrix_equal(a, b):
    return a.shape == b.shape and all(simp(x) == 0 for x in a - b)


@lru_cache(None)
def indices(k: int, degree: int):
    if degree < 0:
        return ()
    return tuple(sorted((a for a in itertools.product(range(degree + 1), repeat=k)
                         if sum(a) <= degree), key=lambda a: (sum(a), a)))


def shell(k, degree):
    return tuple(a for a in indices(k, degree) if sum(a) == degree)


def krons(xs):
    out = S.ones(1, 1)
    for x in xs:
        out = S.kronecker_product(out, x)
    return out


def powers_poly(xs, a):
    return S.prod(x ** n for x, n in zip(xs, a))


def companion(h):
    d = S.degree(h, z)
    return S.Matrix.hstack(*(residue(z ** (j + 1), h) for j in range(d)))


def residue(p, h):
    r = S.Poly(S.rem(p, h, z), z)
    return S.Matrix([r.nth(j) for j in range(S.degree(h, z))])


def tensor_generator(a, k):
    dim = a.rows
    return sum((krons([a if q == j else S.eye(dim) for q in range(k)])
                for j in range(k)), S.zeros(dim ** k))


def gaussian_integral(p):
    """3 times the centred real Gaussian expectation of p(y)."""
    p = S.Poly(simp(p), y)
    ans = 0
    for (n,), c in p.terms():
        if n % 2 == 0:
            ans += 3 * c * (1 if n == 0 else S.factorial2(n - 1))
    return simp(ans)


def gaussian_ip(p, q, weight=1):
    pp = simp(p.subs(z, HALF + I*y))
    qq = simp(q.subs(z, HALF + I*y))
    ww = simp(weight.subs(z, HALF + I*y)) if hasattr(weight, 'subs') else weight
    return gaussian_integral(S.conjugate(pp) * qq * S.conjugate(ww) * ww)


def orthogonal_polynomials(degree, ip):
    polys, norms = [], []
    for n in range(degree + 1):
        p = z ** n
        for u, norm in zip(polys, norms):
            p = simp(p - u * ip(u, p) / norm)
        norm = S.simplify(ip(p, p))
        if norm == 0:
            raise ValueError('Degenerate calibration measure at this degree')
        polys.append(p)
        norms.append(norm)
    return polys, norms


@lru_cache(None)
def gaussian_ops(n):
    return orthogonal_polynomials(n, gaussian_ip)


def data(h, unit, k, degree):
    polys, norms = gaussian_ops(degree + 1)
    vs = [residue(unit * p, h) for p in polys]
    n = S.degree(h, z) ** k
    c, flux, low, high = (S.zeros(n) for _ in range(4))
    for alpha in indices(k, degree):
        v = krons([vs[j] for j in alpha])
        norm = S.prod(norms[j] for j in alpha)
        c += v * v.H / norm
        if sum(alpha) == degree:
            w = S.zeros(n, 1)
            for j in range(k):
                beta = list(alpha)
                beta[j] += 1
                w += krons([vs[q] for q in beta])
            flux += (w * v.H + v * w.H) / norm
            low += v * v.H / norm
            high += w * w.H / norm
    return tuple(x.applyfunc(S.simplify) for x in (c, flux, low, high))


def direct_moment(h, unit, k, degree, weight=1):
    ids = indices(k, degree)
    moments = {(i,j):gaussian_ip(z**i, z**j, weight)
               for i in range(degree+1) for j in range(degree+1)}
    m = S.Matrix([[S.prod(moments[i,j] for i,j in zip(a,b))
                   for b in ids] for a in ids])
    js = [residue(unit*z**i, h) for i in range(degree+1)]
    jmat = S.Matrix.hstack(*(krons([js[i] for i in a]) for a in ids))
    c = (jmat*m.inv()*jmat.H).applyfunc(S.simplify)
    r = (m.inv()*jmat.H*c.inv()).applyfunc(S.simplify)
    return m, jmat, c, r


def terms(k, d, budget, degree):
    return tuple((a, b) for a in itertools.combinations(range(k), degree)
                 for b in indices(k, budget-(k-degree)*d))


def add_polynomial_column(out, row_index, col, support, p, xs):
    for ex, c in S.Poly(simp(p), *xs).terms():
        if c != 0:
            out[row_index[(support, ex)], col] += c


def differential(h, k, budget, degree):
    xs = S.symbols('x:'+str(k))
    d = S.degree(h,z)
    src, dst = terms(k,d,budget,degree), terms(k,d,budget,degree+1)
    rows = {a:i for i,a in enumerate(dst)}
    out = S.zeros(len(dst),len(src))
    for col,(support,alpha) in enumerate(src):
        for j in range(k):
            if j in support:
                continue
            sign = (-1)**sum(i < j for i in support)
            target = tuple(sorted(support+(j,)))
            p = sign*powers_poly(xs,alpha)*h.subs(z,xs[j])
            add_polynomial_column(out,rows,col,target,p,xs)
    return out


def division_homotopy(h, k, budget, degree):
    xs = S.symbols('x:'+str(k))
    d = S.degree(h,z)
    src, dst = terms(k,d,budget,degree), terms(k,d,budget,degree-1)
    rows = {a:i for i,a in enumerate(dst)}
    out = S.zeros(len(dst),len(src))
    for col,(support,alpha) in enumerate(src):
        for j in range(k):
            if j not in support or any(i not in support for i in range(j)):
                continue
            p = powers_poly(xs,alpha)
            for i in range(j):
                p = S.rem(p, h.subs(z,xs[i]), xs[i])
            p = S.div(p,h.subs(z,xs[j]),xs[j])[0] * (-1)**j
            target = tuple(i for i in support if i != j)
            add_polynomial_column(out,rows,col,target,p,xs)
    return out


def remainder_projection(h, k, budget):
    xs = S.symbols('x:'+str(k))
    d = S.degree(h,z)
    ts = terms(k,d,budget,k)
    rows = {a:i for i,a in enumerate(ts)}
    out = S.zeros(len(ts))
    for col,(support,alpha) in enumerate(ts):
        p = powers_poly(xs,alpha)
        for j in range(k):
            p = S.rem(p,h.subs(z,xs[j]),xs[j])
        add_polynomial_column(out,rows,col,support,p,xs)
    return out


def packet_chain_map(h, m, k, budget, degree):
    xs = S.symbols('x:'+str(k))
    d,l = S.degree(h,z),S.degree(m,z)
    src = terms(k,d,budget,degree)
    dst = terms(k,d+l,budget+k*l,degree)
    rows = {a:i for i,a in enumerate(dst)}
    out = S.zeros(len(dst),len(src))
    for col,(support,alpha) in enumerate(src):
        p = powers_poly(xs,alpha)*S.prod(m.subs(z,xs[j]) for j in support)
        add_polynomial_column(out,rows,col,support,p,xs)
    return out


def psd_exact(m):
    """Exact Schur test for rational Hermitian matrices."""
    a = S.Matrix(m)
    if not matrix_equal(a,a.H):
        return False
    while a.rows:
        p = S.simplify(a[0,0])
        if p < 0:
            return False
        if p == 0:
            if any(S.simplify(a[0,j]) != 0 for j in range(1,a.cols)):
                return False
            a = a[1:,1:]
        else:
            a = (a[1:,1:] - a[1:,:1]*a[:1,1:]/p).applyfunc(S.simplify)
    return True


class GradedFluxTests(unittest.TestCase):
    def assertMatrix(self,a,b):
        self.assertTrue(matrix_equal(a,b), msg=f'Matrices differ: {a-b}')

    def test_original_e_and_tau_quotient(self):
        tau = None
        def add(x,y):
            if x is tau: return y
            if y is tau: return x
            return ((x[0]+y[0])%5, (x[1]+y[1])%5)
        def q(x): return tau if x is tau else x[1]
        self.assertEqual(add((1,0),(4,0)),(0,0))
        self.assertEqual(q((1,0)),0)
        self.assertIs(q(tau),None)
        self.assertNotEqual(q((1,0)),q(tau))

    def test_full_koszul_d_squared(self):
        for h,k,budget in [(z*z-z+1,2,5),(z*z-z+1,3,6),(z-2,3,3)]:
            for p in range(k-1):
                a=differential(h,k,budget,p)
                b=differential(h,k,budget,p+1)
                self.assertMatrix(b*a,S.zeros(b.rows,a.cols))

    def test_filtered_division_homotopy_all_degrees(self):
        for h,k,budget in [(z*z-z+1,2,4),(z*z-z+1,3,5),(z-2,3,3)]:
            for p in range(k+1):
                size=len(terms(k,S.degree(h,z),budget,p))
                total=S.zeros(size)
                if p>0:
                    total+=differential(h,k,budget,p-1)*division_homotopy(h,k,budget,p)
                if p<k:
                    total+=division_homotopy(h,k,budget,p+1)*differential(h,k,budget,p)
                rhs=S.eye(size)-(remainder_projection(h,k,budget) if p==k else S.zeros(size))
                self.assertMatrix(total,rhs)

    def test_koszul_low_degree_cohomology_and_hilbert_count(self):
        for k,d in [(2,2),(3,2),(2,3)]:
            h=z**d+z+1
            for budget in range(0,k*d+1):
                ds=[differential(h,k,budget,p) for p in range(k)]
                for p in range(k):
                    size=len(terms(k,d,budget,p))
                    incoming=ds[p-1].rank() if p else 0
                    self.assertEqual(size-ds[p].rank()-incoming,0)
                top=len(terms(k,d,budget,k))-ds[-1].rank()
                expected=sum(sum(a)<=budget for a in itertools.product(range(d),repeat=k))
                self.assertEqual(top,expected)

    def test_packet_enlargement_chain_map_signs(self):
        h,m=z*z-z+1,z-2
        for k,budget in [(2,3),(3,4)]:
            for p in range(k):
                phi=packet_chain_map(h,m,k,budget,p)
                phi1=packet_chain_map(h,m,k,budget,p+1)
                self.assertMatrix(differential(simp(h*m),k,budget+k,p)*phi,
                                  phi1*differential(h,k,budget,p))

    def test_unscaled_norms_and_monic_recurrence(self):
        polys, norms=gaussian_ops(6)
        for j in range(7):
            self.assertEqual(S.Poly(polys[j],z).LC(),1)
            self.assertEqual(norms[j],3*S.factorial(j))
            if j<6:
                rhs=polys[j+1]+HALF*polys[j]-(j*polys[j-1] if j else 0)
                self.assertEqual(simp(z*polys[j]-rhs),0)

    def test_asymmetric_measure_retains_imaginary_diagonal(self):
        nodes=[-3,-1,0,2,5,7]
        weights=[2,1,3,4,6,1]
        def ip(p,q):
            return S.simplify(sum(w*S.conjugate(p.subs(z,HALF+I*x))*q.subs(z,HALF+I*x)
                                 for x,w in zip(nodes,weights)))
        ps,hs=orthogonal_polynomials(4,ip)
        aa=ip(ps[0],z*ps[0])/hs[0]
        self.assertNotEqual(S.im(aa),0)
        for j in range(4):
            a=S.simplify(ip(ps[j],z*ps[j])/hs[j])
            self.assertEqual(S.simplify(a+S.conjugate(a)),1)
            b=hs[j]/hs[j-1] if j else 0
            rhs=ps[j+1]+a*ps[j]-(b*ps[j-1] if j else 0)
            self.assertEqual(simp(z*ps[j]-rhs),0)

    def test_full_jet_recurrence_with_nonconstant_unit(self):
        h=(z-HALF)**2
        unit=2+3*z
        ps,hs=gaussian_ops(5)
        vs=[residue(unit*p,h) for p in ps]
        a=companion(h)
        for j in range(5):
            self.assertMatrix(a*vs[j],vs[j+1]+HALF*vs[j]-(j*vs[j-1] if j else S.zeros(2,1)))
        self.assertEqual((a-HALF*S.eye(2)).rank(),1)
        self.assertMatrix((a-HALF*S.eye(2))**2,S.zeros(2))

    def test_kernel_sum_equals_inverse_moment(self):
        h=(z-S.Rational(1,4))*(z-S.Rational(3,4))
        for k,degree in [(1,3),(2,3)]:
            c,_,_,_=data(h,2+z,k,degree)
            _,_,direct,_=direct_moment(h,2+z,k,degree)
            self.assertMatrix(c,direct)

    def test_tensor_total_degree_flux_identity(self):
        for h,unit,k,degree in [((z-HALF)**2,2+z,1,4),
                               ((z-S.Rational(1,4))*(z-S.Rational(3,4)),1,2,3),
                               ((z-HALF)**2,1,3,3)]:
            c,f,_,_=data(h,unit,k,degree)
            a=tensor_generator(companion(h),k)
            self.assertMatrix(a*c+c*a.H-k*c,f)

    def test_exact_congruence_to_original_control(self):
        h=(z-S.Rational(1,4))*(z-S.Rational(3,4))
        c,f,_,_=data(h,1,2,3)
        g=c.inv()
        a=tensor_generator(companion(h),2)
        w=a.H*g+g*a-2*g
        self.assertMatrix(c*w*c,f)
        self.assertMatrix(g*f*g,w)

    def test_last_shell_rank_factorization(self):
        h=z**3-z+1
        c,f,_,_=data(h,1,2,4)
        self.assertLessEqual(f.rank(),2*math.comb(4+2-1,2-1))
        self.assertMatrix(f,f.H)

    def test_dual_information_shell_update(self):
        h=(z-HALF)**2
        c,_,_,_=data(h,1,2,3)
        c1,_,low1,_=data(h,1,2,4)
        self.assertMatrix(c1-c,low1)
        self.assertTrue(psd_exact(c1-c))
        self.assertTrue(psd_exact(c.inv()-c1.inv()))

    def test_two_positive_shell_envelope(self):
        h=(z-S.Rational(1,4))*(z-S.Rational(3,4))
        c,f,l,u=data(h,1,2,3)
        eta=S.Rational(2)
        self.assertTrue(psd_exact(eta*l+u/eta-f))
        self.assertTrue(psd_exact(eta*l+u/eta+f))

    def test_raising_shell_bound_with_all_coefficients(self):
        h=(z-S.Rational(1,4))*(z-S.Rational(3,4))
        k,degree=2,3
        _,_,_,u=data(h,1,k,degree)
        _,_,next_shell,_=data(h,1,k,degree+1)
        # Gaussian calibration b_j=j, so max sum b_beta_j=M+1.
        self.assertTrue(psd_exact(k*(degree+1)*next_shell-u))

    def test_formal_generating_convolution(self):
        h=(z-HALF)**2
        v=[]
        ps,hs=gaussian_ops(4)
        for p,n in zip(ps,hs):
            q=residue(p,h)
            v.append(q*q.H/n)
        for degree in range(3,5):
            conv=sum((S.kronecker_product(v[i],v[j])
                      for i in range(degree+1) for j in range(degree+1-i)),S.zeros(4))
            self.assertMatrix(conv,data(h,1,2,degree)[0])

    def test_packet_tensor_metric_transport(self):
        # Declared Gaussian calibration with g/H=1 and g/h=m.
        h,m=z-S.Rational(1,4),z-S.Rational(3,4)
        H=simp(h*m)
        k,degree=2,0
        ml,jl,cl,rl=direct_moment(h,m,k,degree,weight=m)
        mu,ju,cu,ru=direct_moment(H,S.Integer(1),k,degree+k)
        f=packet_chain_map(h,m,k,degree,k)
        idem=S.invert(m,h)*m
        inj=krons([residue(idem,H)]*k)
        small=f*rl
        large=ru*inj
        diff=small-large
        self.assertMatrix(ju*diff,S.zeros(4,1))
        self.assertMatrix(large.H*mu*diff,S.zeros(1))
        self.assertMatrix(cl.inv(),inj.H*cu.inv()*inj+diff.H*mu*diff)
        self.assertNotEqual(S.simplify((diff.H*mu*diff)[0]),0)

    def test_same_metric_reflection_in_repeated_block(self):
        h=(z-HALF)**2
        cc=S.Matrix.hstack(*(residue((1-z)**j,h) for j in range(2)))
        c,f,_,_=data(h,1,1,3)
        self.assertMatrix(cc*S.conjugate(cc),S.eye(2))
        self.assertMatrix(cc.H*c.inv()*cc,S.conjugate(c.inv()))
        w=c.inv()*f*c.inv()
        self.assertMatrix(cc.H*w*cc,-S.conjugate(w))

    def test_exact_psd_guard_rejects_invalid_zero_pivot(self):
        self.assertFalse(psd_exact(S.Matrix([[0,1],[1,2]])))
        self.assertTrue(psd_exact(S.Matrix([[0,0],[0,2]])))
        self.assertFalse(psd_exact(S.diag(1,-1)))

    def test_full_eigenline_defect_not_erased(self):
        h=(z-S.Rational(1,4))*(z-S.Rational(3,4))
        c,f,_,_=data(h,1,2,3)
        a=companion(h)
        eig=(a-S.Rational(3,4)*S.eye(2)).nullspace()[0]
        v=krons([eig,eig])
        g=c.inv()
        w=g*f*g
        ratio=S.simplify((v.H*w*v)[0]/(v.H*g*v)[0])
        self.assertEqual(ratio,1)

    def test_source_hermite_leading_coefficients(self):
        f=4*z*z-6*z
        for n in range(6):
            herm=S.expand(S.hermite(2*n+4,S.sqrt(2*z)))
            coeff=S.simplify(S.Poly(f,z).LC()/S.Poly(herm,z).LC())
            self.assertEqual(coeff,S.Rational(1,2**(2*n+4)))
            f=S.expand(2*z*(f-S.diff(f,z)))

    def test_source_moment_projection(self):
        def integral(p):
            return sum(c*S.factorial(2*n)/(4**n*S.factorial(n))
                       for (n,),c in S.Poly(p,z).terms())
        def project(p):
            a=p.subs(z,0); b=integral(p)
            return S.expand(p-a-(b-a)*2*z)
        for p in [1+z+z*z, z**6-3*z, S.Integer(1),2*z]:
            v=project(p)
            self.assertEqual(v.subs(z,0),0)
            self.assertEqual(integral(v),0)
            self.assertEqual(project(v),v)
        self.assertEqual(project(S.Integer(1)),0)
        self.assertEqual(project(2*z),0)

    def test_source_exhaustion_commuting_projection_tower(self):
        hs=[S.expand(S.hermite(2*j,S.sqrt(2*z))) for j in range(9)]
        mat=S.Matrix([[S.Poly(p,z).nth(i) for p in hs] for i in range(9)])
        def integral(p):
            return sum(c*S.factorial(2*n)/(4**n*S.factorial(n))
                       for (n,),c in S.Poly(p,z).terms())
        def project(p):
            a=p.subs(z,0); b=integral(p)
            return S.expand(p-a-(b-a)*2*z)
        def source(n,p):
            c=mat.inv()*S.Matrix([S.Poly(p,z).nth(i) for i in range(9)])
            return project(sum(c[j]*hs[j] for j in range(n+3)))
        v=project(z**8+2*z**5-z**2)
        for n in range(4):
            for m in range(4):
                self.assertEqual(source(n,source(m,v)),source(min(n,m),v))
        f=4*z*z-6*z
        for n in range(4):
            self.assertEqual(source(n,f),f)
            f=S.expand(2*z*(f-S.diff(f,z)))

    def test_source_exact_hermite_derivative_signs(self):
        hs=[S.expand(S.hermite(2*j,S.sqrt(2*z))) for j in range(7)]
        for j in range(6):
            derivative=S.expand(2*z*(hs[j]-S.diff(hs[j],z)))
            rhs=hs[j+1]/4+hs[j]/2-(2*j*(2*j-1)*hs[j-1] if j else 0)
            self.assertEqual(S.expand(derivative-rhs),0)


class NegativeControl(unittest.TestCase):
    def test_deliberately_false_identity(self):
        self.assertEqual(S.Integer(1), S.Integer(2), 'intentional test harness failure')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    parser.add_argument('--negative',action='store_true')
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(GradedFluxTests)
    if args.negative:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(NegativeControl))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    receipt={
        'tests_run':result.testsRun,
        'failures':len(result.failures),
        'errors':len(result.errors),
        'success':result.wasSuccessful(),
        'calibration':'Exact finite polynomial and Gaussian/discrete data; not arithmetic zero certificates',
        'analytic_or_lean_certificate':False,
    }
    text=json.dumps(receipt,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text)
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
