#!/usr/bin/env python3
"""Exact finite checks for the canonical endpoint-restriction construction.

Fixtures are declared Gaussian polynomial quotients, never asserted zeta packets.
No Python assert statement is used.  Arithmetic integrals are not certified here.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import sys
import unittest
import sympy as s

x, S, z = s.symbols('x S z')


def clean(M):
    return M.applyfunc(s.simplify) if isinstance(M, s.MatrixBase) else s.simplify(M)


def must(cond, msg='exact verification failed'):
    if not bool(cond):
        raise ArithmeticError(msg)


def same(a,b):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        must(a.shape == b.shape,'shape mismatch')
        must(all(s.simplify(t)==0 for t in a-b),'matrix identity failed')
    else:
        must(s.simplify(a-b)==0,'scalar identity failed')


def positive_definite(M):
    if M.rows==0: return True
    same(M,M.conjugate().T)
    return all(bool(s.simplify(M[:n,:n].det())>0) for n in range(1,M.rows+1))


@lru_cache(None)
def fixture(chi_expr, max_degree=7, mass=s.Integer(7), variance=s.Integer(1), centre=s.Integer(1)):
    """Monic S polynomials for S=centre+i*x, with Gaussian mass and variance.
    The measure has the specified mass; it is not rescaled in the construction.
    """
    chi=s.Poly(chi_expr,S); q=chi.degree()
    polys=[s.Integer(1), S-centre]
    for n in range(1,max_degree):
        polys.append(s.expand((S-centre)*polys[-1]+n*variance*polys[-2]))
    polys=polys[:max_degree+1]
    weights=[mass*variance**n*s.factorial(n) for n in range(max_degree+1)]
    B=s.zeros(q,max_degree+1)
    for n,p in enumerate(polys):
        r=s.Poly(s.rem(p,chi.as_expr(),S),S)
        for a in range(q): B[a,n]=r.nth(a)
    A=s.zeros(q)
    for a in range(q):
        r=s.Poly(s.rem(S**(a+1),chi.as_expr(),S),S)
        for b in range(q): A[b,a]=r.nth(b)
    return {'chi':chi.as_expr(),'q':q,'p':polys,'w':weights,'B':B,'A':A,'centre':centre}


def level(F,n):
    q=F['q']; must(n>=q-1)
    B=F['B'][:,:n+1]; O=s.diag(*F['w'][:n+1]); Oi=O.inv()
    K=clean(B*Oi*B.conjugate().T); G=clean(K.inv())
    R=clean(Oi*B.conjugate().T*G)
    return {'B':B,'O':O,'K':K,'G':G,'R':R,'V':clean(G.det())}


def window(F,i,j):
    lo,hi=level(F,i),level(F,j); q=F['q']
    E=s.zeros(j+1,i+1)
    E[:i+1,:]=s.eye(i+1)
    P=E*E.T
    T=clean(lo['K']*hi['G']); H=clean(s.eye(q)-T)
    return {'lo':lo,'hi':hi,'embed':E,'P':P,'T':T,'H':H,
            'Delta':clean(hi['K']-lo['K'])}


def cb_weights(F,j):
    q=F['q']; B=F['B']
    out={}
    for I in combinations(range(j+1),q):
        d=B[:,I].det()
        out[I]=s.simplify(s.conjugate(d)*d/s.prod(F['w'][a] for a in I))
    return out


def log_interval(value,terms=48):
    """Rigorous rational bounds for log of a positive rational number."""
    value=s.Rational(value); must(value>0)
    if value==1: return s.Rational(0),s.Rational(0)
    if value<1:
        a,b=log_interval(1/value,terms); return -b,-a
    e=0; y=value
    while y>=2: y/=2; e+=1
    def series(t):
        v=(t-1)/(t+1)
        lo=2*sum(v**(2*j+1)/s.Integer(2*j+1) for j in range(terms))
        tail=2*v**(2*terms+1)/(s.Integer(2*terms+1)*(1-v*v))
        return lo,lo+tail
    a,b=series(y); c,d=series(s.Rational(2))
    return a+e*c,b+e*d


def gap_certificate(loK,hiK):
    """Returns a verified rational lower bound g for loK >= g hiK."""
    for n in range(1,65):
        g=s.Rational(1,2**n)
        if positive_definite(clean(loK-g*hiK)):
            return g
    raise ArithmeticError('fixture gap was not enclosed')


def log_volume_bounds(H,g,p=2,terms=48):
    """Rigorous rational lower/upper bounds from moments and a proven gap."""
    q=H.rows; r=1-s.Rational(g)
    must(0<g<=1); must(p>=1)
    if r==0:
        same(H,s.zeros(q)); return s.Rational(0),s.Rational(0)
    lower=sum(s.trace(H**m)/s.Integer(m) for m in range(1,p+1))
    _,logup=log_interval(1/g,terms)
    coeff=(logup-sum(r**m/s.Integer(m) for m in range(1,p+1)))/r**(p+1)
    upper=clean(lower+coeff*s.trace(H**(p+1)))
    return clean(lower),upper


class ExactChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.F=fixture((S-1)**2,8)
        cls.O=fixture((S-1)**2-s.Rational(1,9),7)
        cls.R=fixture((S-1)**2*(S+2),7)

    def test_01_actual_quotient_and_weighted_residual(self):
        for F in [self.F,self.O,self.R]:
            for n in [F['q']-1,F['q']+1]:
                L=level(F,n)
                same(L['B']*L['R'],s.eye(F['q']))
                same(L['R'].conjugate().T*L['O']*L['R'],L['G'])
                for b in L['B'].nullspace():
                    same(b.conjugate().T*L['O']*L['R'],s.zeros(1,F['q']))

    def test_02_metric_adjoint(self):
        for F in [self.F,self.O,self.R]:
            W=window(F,F['q']-1,F['q']+2)
            same(W['lo']['G']*W['T'],W['hi']['G'])
            same(W['T'].conjugate().T*W['lo']['G'],W['hi']['G'])

    def test_03_polynomial_restriction(self):
        for F in [self.F,self.O,self.R]:
            W=window(F,F['q']-1,F['q']+2)
            same(W['embed']*W['lo']['R']*W['T'],W['P']*W['hi']['R'])

    def test_04_coherent_return_maps(self):
        for F in [self.F,self.R]:
            i=F['q']-1; j=i+1; ell=i+3
            a,b,c=window(F,i,j),window(F,j,ell),window(F,i,ell)
            same(a['T']*b['T'],c['T'])
            same(c['T'].det(),c['hi']['V']/c['lo']['V'])

    def test_05_retained_theta_relation(self):
        for F in [self.F,self.O,self.R]:
            W=window(F,F['q']-1,F['q']+2)
            D=W['embed']*W['lo']['R']-W['hi']['R']
            same(W['hi']['B']*D,s.zeros(F['q']))
            same(D.conjugate().T*W['hi']['O']*D,W['lo']['G']-W['hi']['G'])
            same(D,W['embed']*W['lo']['R']*W['H']-(s.eye(W['P'].rows)-W['P'])*W['hi']['R'])

    def test_06_source_leakage_form(self):
        W=window(self.R,2,6)
        C=clean(W['hi']['G']*W['H'])
        same(C,C.conjugate().T)
        same(C,W['hi']['R'].conjugate().T*W['hi']['O']*(s.eye(7)-W['P'])*W['hi']['R'])
        g=gap_certificate(W['lo']['K'],W['hi']['K'])
        must(positive_definite(W['lo']['K']-g*W['hi']['K']))

    def test_07_action_commutator_not_erased(self):
        for F in [self.O,self.R]:
            W=window(F,F['q']-1,F['q']+2); A=F['A']; w=2*F['centre']
            Vi=A*W['lo']['K']+W['lo']['K']*A.conjugate().T-w*W['lo']['K']
            Wj=A.conjugate().T*W['hi']['G']+W['hi']['G']*A-w*W['hi']['G']
            same(A*W['T']-W['T']*A,Vi*W['hi']['G']-W['lo']['K']*Wj)
        must(any(clean(t)!=0 for t in A*W['T']-W['T']*A))

    def test_08_cauchy_binet_full_jets(self):
        for F,j in [(self.F,5),(self.O,5),(self.R,5)]:
            weights=cb_weights(F,j)
            must(all(t>=0 for t in weights.values()))
            same(sum(weights.values()),level(F,j)['K'].det())

    def test_09_degree_generating_polynomial(self):
        for F,i,j in [(self.F,1,4),(self.R,2,5)]:
            W=window(F,i,j); weights=cb_weights(F,j)
            Z=sum(t*z**sum(a>i for a in I) for I,t in weights.items())
            same(s.expand(Z),(W['lo']['K']+z*W['Delta']).det())
            same(Z.subs(z,0),W['lo']['K'].det())
            same(Z/W['hi']['K'].det(),(W['T']+z*W['H']).det())

    def test_10_degree_occupation_moments(self):
        F=self.R; W=window(F,2,5)
        Z=(W['lo']['K']+z*W['Delta']).det()
        total=Z.subs(z,1)
        mean=s.diff(Z,z).subs(z,1)/total
        second=(s.diff(Z,z,2)+s.diff(Z,z)).subs(z,1)/total
        same(mean,s.trace(W['H']))
        same(second-mean**2,s.trace(W['H']-W['H']**2))

    def test_11_confluent_raw_derivatives_and_unit(self):
        F=self.R; q=F['q']; nodes=[(1,2),(-2,1)]
        T=s.Matrix([[s.diff(S**j,S,r).subs(S,a) for j in range(q)] for a,m in nodes for r in range(m)])
        expected=s.prod(s.factorial(r) for a,m in nodes for r in range(m))*(-3)**(2*1)
        same(T.det(),expected)
        U=F['A']+5*s.eye(q); Q=T*U
        W=window(F,2,5)
        Ki=Q*W['lo']['K']*Q.conjugate().T; Kj=Q*W['hi']['K']*Q.conjugate().T
        same(Ki*Kj.inv(),Q*W['T']*Q.inv())
        same(Kj.det()/Ki.det(),W['hi']['K'].det()/W['lo']['K'].det())

    def test_12_mass_is_retained(self):
        F2=fixture((S-1)**2,8,s.Integer(35))
        for n in [1,3,4]:
            a,b=level(self.F,n),level(F2,n)
            same(b['G'],5*a['G']); same(b['K'],a['K']/5)
        same(window(F2,1,4)['T'],window(self.F,1,4)['T'])

    def test_13_exact_calibration_spectrum(self):
        a,b=window(self.F,1,3),window(self.F,2,4)
        same(a['T'].charpoly(z).as_expr(),(z-s.Rational(2,3))*(z-s.Rational(2,5)))
        same(b['T'].charpoly(z).as_expr(),(z-s.Rational(4,5))*(z-s.Rational(2,5)))
        same(1/(a['T'].det()*b['T'].det()),s.Rational(375,32))

    def test_14_log_interval_and_trace_enclosures(self):
        for F,i,j in [(self.F,1,3),(self.F,2,4),(self.O,1,4),(self.R,2,5)]:
            W=window(F,i,j); g=gap_certificate(W['lo']['K'],W['hi']['K'])
            low,up=log_volume_bounds(W['H'],g,p=2)
            l,u=log_interval(W['lo']['V']/W['hi']['V'])
            must(low<=l); must(up>=u)

    def test_15_zero_relation_versus_absence(self):
        F=self.F
        d=F['B'][:,[0,2]].det(); same(d,0)
        present=('degree-3',s.Integer(0)); absent=('absent',None)
        must(present!=absent)
        weights=cb_weights(F,3); must((0,2) in weights); same(weights[(0,2)],0)
        must((0,4) not in weights)

    def test_16_empty_and_no_new_columns(self):
        K=s.zeros(0,0); same(K.det(),1)
        L=level(self.F,3)
        T=L['K']*L['G']; same(T,s.eye(2))
        same(s.eye(2)-T,s.zeros(2))
        must(log_interval(1)==(s.Rational(0),s.Rational(0)))

    def test_17_relative_old_new_eigenvalue_map(self):
        W=window(self.R,2,5)
        X=clean(W['Delta']*W['lo']['G'])
        same(W['H'],X*(s.eye(3)+X).inv())
        same(W['T'],(s.eye(3)+X).inv())

    def test_18_polynomial_degree_action_square(self):
        F=self.R
        for n in [2,3,4]:
            D=s.zeros(n+2,n+1)
            for j in range(n+1):
                coeffs=s.Poly(S*F['p'][j],S)
                remainder=coeffs.as_expr()
                for a in range(n+1,-1,-1):
                    c=s.Poly(remainder,S).nth(a)
                    D[a,j]=c; remainder=s.expand(remainder-c*F['p'][a])
                same(remainder,0)
            same(F['B'][:,:n+2]*D,F['A']*F['B'][:,:n+1])

    def test_19_rectangular_arithmetic_inclusion(self):
        F=self.F; E=s.Matrix([[2,0],[1,1],[0,3]])
        fixed=clean((E.conjugate().T*E).det())
        must(fixed>0)
        for I in combinations(range(5),2):
            B=F['B'][:,I]
            image=E*B
            same((image.conjugate().T*image).det(),fixed*s.conjugate(B.det())*B.det())
        L=(E.conjugate().T*E).inv()*E.conjugate().T
        same(L*E,s.eye(2))
        W=window(F,1,3)
        same(L*(E*W['T']*L)*E,W['T'])


def calibrations():
    F=fixture((S-1)**2,8); rows=[]
    for i,j in [(1,3),(2,4)]:
        W=window(F,i,j); g=s.Rational(2,5)
        # Here the exact spectrum establishes this non-strict lower gap.
        lo,hi=log_volume_bounds(W['H'],g,p=2)
        ll,uu=log_interval(W['lo']['V']/W['hi']['V'])
        rows.append({'i':i,'j':j,'gap_eigenvalues':[str(t) for t in W['T'].eigenvals()],
                     'volume_ratio':str(W['lo']['V']/W['hi']['V']),
                     'trace1':str(s.trace(W['H'])),'trace2':str(s.trace(W['H']**2)),
                     'log_volume_decimal':str(s.N((ll+uu)/2,18)),
                     'trace_upper_decimal':str(s.N(hi,18))})
    return {'measure':'Gaussian polynomial fixture, literal mass 7 and variance 1; not zeta data',
            'S_coordinate':'S=1+i*x','chi':'(S-1)^2','windows':rows,
            'total_log_volume':str(s.N(s.log(s.Rational(375,32)),18))}


def main():
    p=argparse.ArgumentParser(); p.add_argument('--json',type=Path); p.add_argument('--inject-failure',action='store_true'); p.add_argument('--calibration',type=Path)
    args=p.parse_args()
    if args.inject_failure: must(False,'intentional negative control')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExactChecks))
    receipt={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
             'passed':result.wasSuccessful(),'scope':'exact finite polynomial/matrix fixtures; no arithmetic integral certification'}
    if args.json: args.json.write_text(json.dumps(receipt,indent=2)+'\n')
    if args.calibration: args.calibration.write_text(json.dumps(calibrations(),indent=2)+'\n')
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__': sys.exit(main())
