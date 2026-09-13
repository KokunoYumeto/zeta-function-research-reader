#!/usr/bin/env python3
"""Exact source calibrations; these are not arithmetic zero or integral certificates."""
from __future__ import annotations
import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import unittest
import sympy as s

REPO = Path(__file__).resolve().parents[2]
path = REPO / 'workbenches/tau-source-resolvent/check_exact.py'
spec = importlib.util.spec_from_file_location('recovered_source_fixture', path)
if spec is None or spec.loader is None:
    raise RuntimeError('missing recovered fixture')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
need, equal, clean = f.need, f.equal, f.clean


def pd(M):
    return equal(M, M.H) and all(s.simplify(M[:a,:a].det()) > 0 for a in range(1, M.rows+1))


def matrices(q=2):
    N=2*q
    chi=s.expand((f.S-f.HALF)**q)
    M0=f.gram(N,1)
    M1=f.gram(N,1+(f.X+1)**2)
    return chi,M0,M1


def endpoints(M,chi):
    q=s.degree(chi,f.S)
    result=[]
    for N in [q-1,q,2*q-1,2*q]:
        B,C=f.presentation(N,chi)
        H,Z,R,G=f.canonical(M[:N+1,:N+1],B,C)
        rho=R.col_join(s.zeros(M.rows-N-1,q))
        P=clean(rho*G.inv()*rho.H*M)
        result.append((B,C,R,G,rho,P))
    return result


class Tests(unittest.TestCase):
    def test_scaled_secants_and_source_bounds(self):
        for q in [2,3]:
            chi,M0,M1=matrices(q)
            a=s.Rational(1,2);b=s.Integer(128)
            need(pd(M0) and pd(M1-a*M0) and pd(b*M0-M1),'original source enclosure')
            for N in [q-1,q,2*q-1,2*q]:
                B,C=f.presentation(N,chi)
                m0=M0[:N+1,:N+1];m1=M1[:N+1,:N+1]
                h0,z0,r0,g0=f.canonical(m0,B,C)
                h1,z1,r1,g1=f.canonical(m1,B,C)
                delta=clean(r1-r0)
                need(equal(g1-a*g0,r1.H*(m1-a*m0)*r1+a*delta.H*m0*delta),'lower scaled secant')
                need(equal(b*g0-g1,r0.H*(b*m0-m1)*r0+delta.H*m1*delta),'upper scaled secant')
                need(pd(g1-a*g0) and pd(b*g0-g1),'quotient enclosure')
                need(equal(delta,B*(z0-z1)),'original relation coefficient')
    def test_original_quotient_and_full_multiplicity(self):
        for q in [2,3]:
            chi,M0,M1=matrices(q)
            for N in [q-1,2*q]:
                B,C=f.presentation(N,chi)
                R0=f.canonical(M0[:N+1,:N+1],B,C)[2]
                R1=f.canonical(M1[:N+1,:N+1],B,C)[2]
                for col in range(q):
                    delta=sum((R1[row,col]-R0[row,col])*f.S**row for row in range(N+1))
                    need(s.rem(delta,chi,f.S)==0,'original complete repeated relation')
                if N==q-1:need(B.cols==0 and equal(R0,R1),'first degree has no hidden inverse')
    def test_weighted_projectors_and_tangent(self):
        chi,M0,M1=matrices()
        E=M1-M0
        for t in [0,s.Rational(1,3),1]:
            M=M0+t*E
            X=clean(M.inv()*E)
            es=endpoints(M,chi)
            for B,C,R,G,rho,P in es:
                need(equal(P*P,P),'projector')
                need(equal(P.H*M,M*P),'weighted adjoint')
                need(s.trace(P)==2,'trace is quotient dimension')
                need(s.cancel(s.trace(X*P)-s.trace(G.inv()*rho.H*E*rho))==0,'finite tangent pairing')
            need(not equal(M,E*M*E.inv()) if E.det()!=0 else True,'noncommuting fixture')
    def test_nested_overlap_and_loss(self):
        chi,M0,M1=matrices()
        M=(2*M0+M1)/3
        es=endpoints(M,chi)
        for i,j in [(0,2),(1,3)]:
            Gi=es[i][3];Gj=es[j][3]
            ri=es[i][4];rj=es[j][4]
            Pi=es[i][5];Pj=es[j][5]
            T=clean(Gi.inv()*Gj)
            need(equal(rj.H*M*ri,Gj),'original nested cross Gram')
            need(s.cancel(s.trace(Pi*Pj)-s.trace(T))==0,'overlap trace')
            need(s.cancel(s.trace((Pi-Pj)**2)-2*s.trace(s.eye(2)-T))==0,'loss trace')
    def test_four_contrast_and_retained_cross_term(self):
        chi,M0,M1=matrices()
        M=(M0+M1)/2
        E=M1-M0;X=clean(M.inv()*E)
        ps=[e[5] for e in endpoints(M,chi)]
        Q=clean(ps[0]+ps[1]-ps[2]-ps[3]);Q0=ps[0]-ps[2];Q1=ps[1]-ps[3]
        need(s.trace(Q)==0,'same common trace')
        c=s.trace(X)/M.rows
        need(s.cancel(s.trace((X-c*s.eye(M.rows))*Q)-s.trace(X*Q))==0,'scalar cancellation')
        need(s.cancel(s.trace(Q**2)-s.trace(Q0**2)-s.trace(Q1**2)-2*s.trace(Q0*Q1))==0,'mixed restriction term')
        need(s.trace(Q0*Q1)!=0,'fixture must detect omitted mixed term')
        sigma=s.cancel(s.trace(X**2)-s.trace(X)**2/M.rows)
        need(sigma>=0,'centered weighted variance')
        need(s.cancel(s.trace(X*Q)**2)<=s.cancel(sigma*s.trace(Q**2)),'centered trace bound')
    def test_all_mixed_source_pairings(self):
        M=s.Matrix([[3,1+s.I],[1-s.I,4]])
        Fs=[s.Matrix([[1,s.I],[2,1]]),s.Matrix([[2,0],[-s.I,3]]),s.Matrix([[0,1],[1,0]])]
        weights=[1,-1,1]
        actual=[weights[i]*Fs[i] for i in range(3)]
        total=sum(actual,s.zeros(2,2))
        cross=sum((A.H*M*B for A in actual for B in actual),s.zeros(2,2))
        diagonal=sum((A.H*M*A for A in actual),s.zeros(2,2))
        need(equal(total.H*M*total,cross),'all polarized terms with original signs')
        need(not equal(cross,diagonal),'different labels do not imply orthogonality')
        u=s.Matrix([1,s.I]);v=-u
        need(equal((u+v).H*M*(u+v),s.zeros(1,1)),'cancellation after common transport')
        need((u.H*M*u+v.H*M*v)[0,0]>0,'diagonal-only false formula detectable')
    def test_join_and_receiving_zero(self):
        # Exact finite calibration of an allowed diagram with identity transports
        # on three active one-dimensional fibres and the zero bottom fibre.
        def add(a,b):return (a[0]|b[0],a[1]+b[1])
        def quotient(a):return (a[0],0)
        elements=[(0,0)]+[(mask,v) for mask in [1,2,3] for v in [-1,0,1]]
        for xs in itertools.product(elements,repeat=3):
            total=(0,0);qtotal=(0,0);join=0
            for x in xs:
                total=add(total,x);qtotal=add(qtotal,quotient(x));join|=x[0]
            need(total[0]==join,'actual join')
            need(quotient(total)==qtotal==(join,0),'sum of original boundary images')
            if join:need(qtotal!=(0,0),'nonbottom fibre zero is not absence')
        need(add((1,1),(2,-1))==(3,0),'mixed cancellation retains joint label')
    def test_mass_and_common_source(self):
        chi,M0,M1=matrices()
        E0=endpoints(M0,chi);E1=endpoints(5*M0,chi)
        for a,b in zip(E0,E1):
            need(equal(a[2],b[2]),'source scale leaves original section unchanged')
            need(equal(b[3],5*a[3]),'literal mass in quotient Gram')
            need(equal(a[5],b[5]),'same weighted source projection')
        ratio0=E0[0][3].det()*E0[1][3].det()/(E0[2][3].det()*E0[3][3].det())
        ratio1=E1[0][3].det()*E1[1][3].det()/(E1[2][3].det()*E1[3][3].det())
        need(s.cancel(ratio0-ratio1)==0,'four endpoint common scalar cancellation')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--negative',choices=['diagonal-only','absent-join','omit-boundary'])
    arg=ap.parse_args()
    if arg.negative:
        if arg.negative=='diagonal-only':
            u=s.Matrix([1,s.I]);v=-u
            accepted=equal((u+v).H*(u+v),u.H*u+v.H*v)
        elif arg.negative=='absent-join':accepted=((1|2,0)==(0,0))
        else:
            chi,M0,M1=matrices();B,C=f.presentation(4,chi)
            r0=f.canonical(M0,B,C)[2];g0=f.canonical(M0,B,C)[3]
            g1=f.canonical(M1,B,C)[3]
            accepted=equal(g1,g0+r0.H*(M1-M0)*r0)
        print(json.dumps({'negative_control':arg.negative,'false_claim_accepted':bool(accepted)},sort_keys=True))
        raise SystemExit(0 if accepted else 1)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(stream=sys.stderr,verbosity=1).run(suite)
    print(json.dumps({'methods':result.testsRun,'success':result.wasSuccessful(),
      'source_mass':7,'changed_source_mass':21,'coordinate':'S=1/2+i*x',
      'arithmetic_certificate':False,'scope':'Canonical source sandwiches, original mixed joins and full cross Grams, weighted common-source projector traces.'},indent=2,sort_keys=True))
    if not result.wasSuccessful():raise SystemExit(1)

if __name__=='__main__':main()
