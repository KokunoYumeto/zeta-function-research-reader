"""Exact finite calibrations for KL.11--KL.20 and a shell-substitution control.

All measures are finite discrete fixtures. This is not an arithmetic moment,
analytic, or Lean certificate. The unchanged delivered checker supplies exact
fixtures through an isolated, hash-checked copy; no archive member is edited.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import shutil
import sys
import unittest
import sympy as sp

DEPENDENCY_SHA256 = "bc603e2ebda6104e10e5b48b0de56a7430a0c3276aa2023b2603040eee1cc410"
SOURCE = None
RECORDS = []
RANK_RECORDS = []
DERIVATIVE_RECORDS = []
HALF = sp.Rational(1, 2)


def clean(matrix):
    return sp.Matrix(matrix).applyfunc(lambda z: sp.cancel(sp.expand(z)))


def shell(k, n):
    return sorted(a for a in product(range(n + 1), repeat=k) if sum(a) == n)


def mono(variables, exponents):
    return sp.prod(z ** a for z, a in zip(variables, exponents))


def incidence(k, n):
    old, new = shell(k, n), shell(k, n + 1)
    result = sp.zeros(len(new), len(old))
    for j, a in enumerate(old):
        for i in range(k):
            b = list(a)
            b[i] += 1
            result[new.index(tuple(b)), j] += 1
    return result


def columns(matrix):
    return matrix.columnspace()


def hstack_or_empty(vectors, rows):
    return sp.Matrix.hstack(*vectors) if vectors else sp.zeros(rows, 0)


def division_maps(k, n):
    variables = sp.symbols(f"z0:{k}")
    old, new = shell(k, n), shell(k, n + 1)
    prime = shell(k - 1, n + 1) if k > 1 else []
    qmap, rmap = sp.zeros(len(old), len(new)), sp.zeros(len(prime), len(new))
    include = sp.zeros(len(new), len(prime))
    identities = []
    linear = sum(variables)
    for j, beta in enumerate(new):
        f = mono(variables, beta)
        q, r = sp.div(f, linear, variables[-1])
        q, r = sp.expand(q), sp.expand(r)
        for i, a in enumerate(old):
            qmap[i, j] = sp.Poly(q, *variables).coeff_monomial(mono(variables, a))
        if k > 1:
            for i, a in enumerate(prime):
                rmap[i, j] = sp.Poly(r, *variables[:-1]).coeff_monomial(mono(variables[:-1], a))
        identities.append((f, q, r, sp.expand(f.subs(variables[-1], -sum(variables[:-1])))))
    for j, a in enumerate(prime):
        include[new.index(tuple(a) + (0,)), j] = 1
    return dict(variables=variables, old=old, new=new, prime=prime,
                T=incidence(k, n), q=qmap, r=rmap, include=include,
                identities=identities, linear=linear)


def quotient_coordinates(Z):
    # Ordinary transpose: these are complex-linear annihilator coordinates.
    annihilators = Z.T.nullspace()
    Q = hstack_or_empty(annihilators, Z.rows).T
    if Q.rows:
        pivots = Q.rref()[1]
        embedding = sp.eye(Q.cols)[:, list(pivots)]
        section = embedding * (Q * embedding).inv()
    else:
        section = sp.zeros(Q.cols, 0)
    return Q, section


def polynomial_row(z, variables, exponents):
    return sp.Matrix([[sp.prod(z['u']['p'][a[i]].subs(SOURCE.s, variables[i])
                                  for i in range(z['k'])) for a in exponents]])


def relation_row(z, variables):
    return clean(polynomial_row(z, variables, z['next'])
                 - polynomial_row(z, variables, z['exps']) * z['coeff'] * z['next_jets'])


def ordered_division(poly, variables, modulus):
    remainder = sp.expand(poly)
    quotients = []
    for variable in variables:
        quotient, remainder = sp.div(remainder, modulus.subs(SOURCE.s, variable), variable)
        quotients.append(sp.expand(quotient))
        remainder = sp.expand(remainder)
    return quotients, remainder


def evaluated_source(polynomials, z, variables):
    return clean([[sp.prod(z['u']['v'].subs(SOURCE.s, x) for x in point)
                   * polynomial.subs(dict(zip(variables, point)), simultaneous=True)
                   for polynomial in list(polynomials)] for point in z['points']])


@lru_cache(None)
def negative_fixture():
    x, y = sp.symbols('x y')
    nodes = [HALF - sp.I, HALF, HALF + sp.I]
    points = list(product(nodes, repeat=2))
    evaluate = lambda polys: clean([[p.subs({x: a, y: b}) for p in polys] for a, b in points])
    R = sp.ones(9, 1)
    old = evaluate([y - HALF, x - HALF])
    P = clean(old * (old.H * old).inv() * old.H)
    D = sp.diag(*(a + b for a, b in points))
    A = sp.ones(1, 1)
    B = clean(D * R - R * A)
    C = clean((sp.eye(9) - P) * B)
    actual_top = sp.zeros(1, 2)
    homogeneous_top = sp.Matrix([[HALF, HALF]])
    epolys = [(y-HALF)**2, (x-HALF)*(y-HALF), (x-HALF)**2]
    E = evaluate(epolys)
    return dict(nodes=nodes, R=R, G=clean(R.H * R), A=A, B=B, C=C, P=P,
                top=actual_top, homogeneous=homogeneous_top, E=E,
                layer_gram=clean(E.H*E), U=sp.Matrix([[sp.Rational(2,3), 0, sp.Rational(2,3)]]))


class ContinuationTests(unittest.TestCase):
    def require(self, label, condition):
        passed = bool(condition)
        RECORDS.append({'test': self.id(), 'label': label, 'passed': passed})
        self.assertTrue(passed, label)

    def eq(self, label, left, right):
        difference = clean(sp.Matrix(left) - sp.Matrix(right))
        self.require(label, difference == sp.zeros(*difference.shape))

    def scalar(self, label, value):
        self.require(label, sp.cancel(sp.expand(value)) == 0)

    def test_01_incidence_ordered_division_and_cokernel(self):
        for k in range(1, 5):
            for n in range(5):
                z = division_maps(k, n)
                T, q, r, include = z['T'], z['q'], z['r'], z['include']
                label = f'k={k}, n={n}'
                inverse = q.col_join(r)
                forward = T.row_join(include)
                self.eq(label+' full ordered decomposition', inverse*forward, sp.eye(T.cols+r.rows))
                self.eq(label+' full reconstruction', forward*inverse, sp.eye(T.rows))
                self.require(label+' incidence injection', T.rank() == T.cols)
                expected = sp.binomial(n+k-1, k-2) if k > 1 else 0
                self.require(label+' cokernel dimension', r.rows == expected)
                for f, quotient, remainder, substituted in z['identities']:
                    self.scalar(label+' polynomial division', f-z['linear']*quotient-remainder)
                    self.scalar(label+' exact signed substitution', remainder-substituted)

    def test_02_actual_rank_kernel_and_whole_quotient(self):
        fixtures = [(1,1,False,False), (1,2,False,False), (1,3,True,False),
                    (1,3,True,True), (2,2,False,False), (2,3,False,False),
                    (2,2,True,False), (2,3,True,False),
                    (2,2,False,True), (2,3,True,True)]
        for k, N, repeated, asymmetric in fixtures:
            z = SOURCE.layer(k, N, repeated, asymmetric)
            label = f'k={k},N={N},repeated={repeated},asymmetric={asymmetric}'
            division = division_maps(k, N)
            T, top, Dtop = division['T'], z['top'], z['top_norm']
            Z = clean(Dtop.inv()*top.H)
            expected_C = clean(z['E']*T*Z*z['G'])
            self.eq(label+' KL13 full actual derivative map', z['C'], expected_C)
            self.eq(label+' original projection of B', (sp.eye(z['T'].rows)-z['Pold'])*z['B'], expected_C)
            rankA, rankC = top.rank(), z['C'].rank()
            self.require(label+' KL14 exact rank', rankA == rankC)
            kerAstar = hstack_or_empty(top.H.nullspace(), top.rows)
            kernel_image = clean(z['K']*kerAstar)
            self.eq(label+' KL14 mapped kernel', z['C']*kernel_image, sp.zeros(z['C'].rows, kernel_image.cols))
            self.require(label+' full kernel dimension', kernel_image.rank() == z['C'].cols-rankC)
            self.require(label+' original projection-loss rank', z['Y'].rank() == z['next_jets'].rank())
            self.require(label+' KL15 refined rank', z['W'].rank() <= 2*min(rankA,z['next_jets'].rank()))
            Qz, Sz = quotient_coordinates(Z)
            self.eq(label+' quotient annihilator', Qz*Z, sp.zeros(Qz.rows,Z.cols))
            self.require(label+' entire Z kernel', Qz.rank() == Z.rows-Z.rank())
            self.eq(label+' quotient section', Qz*Sz, sp.eye(Qz.rows))
            first = clean(Qz*division['q'])
            Q = first.col_join(division['r'])
            S = clean(T*Sz).row_join(division['include'])
            self.eq(label+' quotient inverse exact', Q*S, sp.eye(Q.rows))
            self.eq(label+' quotient kills derivative image', Q*T*Z, sp.zeros(Q.rows,Z.cols))
            self.require(label+' quotient dimension', Q.rows == z['E'].cols-rankC)
            error = clean(S*Q-sp.eye(z['E'].cols))
            self.require(label+' inverse modulo original image',
                         clean((T*Z).row_join(error)).rank() == rankC)
            self.require(label+' inverse in actual source layer',
                         clean(z['C'].row_join(z['E']*error)).rank() == rankC)
            RANK_RECORDS.append({'k':k,'N':N,'repeated':repeated,'asymmetric':asymmetric,
                                 'rank_actual_top':rankA,'rank_C':rankC,
                                 'rank_next_jet':z['next_jets'].rank(),
                                 'rank_W':z['W'].rank(),'layer_dimension':z['E'].cols,
                                 'quotient_dimension':Q.rows,'jet_deficit_dimension':Qz.rows,
                                 'incidence_cokernel_dimension':division['r'].rows})

    def test_03_derivative_on_original_relation_columns_two_levels(self):
        for k, N, repeated, asymmetric in [(1,1,False,False),(1,2,True,True),
                                           (2,2,False,False),(2,2,True,False),
                                           (2,2,False,True),(2,2,True,True)]:
            z = SOURCE.layer(k,N,repeated,asymmetric)
            after = SOURCE.layer(k,N+1,repeated,asymmetric)
            variables = sp.symbols(f'x0:{k}')
            first, second = relation_row(z,variables), relation_row(after,variables)
            Tnext = incidence(k,N+1)
            difference = clean(sum(variables)*first-second*Tnext)
            label=f'k={k},N={N},repeated={repeated},asymmetric={asymmetric}'
            self.eq(label+' original first e columns', evaluated_source(first,z,variables),z['E'])
            self.eq(label+' original next e columns', evaluated_source(second,after,variables),after['E'])
            actual_difference=clean(z['Dop']*z['E']-after['E']*Tnext)
            self.eq(label+' original derivative difference',evaluated_source(difference,z,variables),actual_difference)
            self.eq(label+' difference retained in old relation space',after['Pold']*actual_difference,actual_difference)
            self.eq(label+' induced quotient derivative',
                    (sp.eye(z['T'].rows)-after['Pold'])*z['Dop']*z['E'],after['E']*Tnext)
            self.eq(label+' derivative of old representatives',
                    after['Pold']*z['Dop']*z['oldB'],z['Dop']*z['oldB'])
            for poly in list(first)+list(second)+list(difference):
                quotients,remainder=ordered_division(poly,variables,z['u']['h'])
                self.scalar(label+' original complete-jet remainder',remainder)
                reconstruct=sum(z['u']['h'].subs(SOURCE.s,x)*q for x,q in zip(variables,quotients))
                self.scalar(label+' complete ordered primitive',reconstruct-poly)
                signed=sum((-1)**i*z['u']['h'].subs(SOURCE.s,x)*((-1)**i*q)
                           for i,(x,q) in enumerate(zip(variables,quotients)))
                self.scalar(label+' all Koszul signs retained',signed-poly)
            for poly in difference:
                degree=sp.Poly(poly,*variables).total_degree() if poly!=0 else -1
                self.require(label+' difference degree bound',degree<=N+1)
                quotients,_=ordered_division(poly,variables,z['u']['h'])
                for q in quotients:
                    qdegree=sp.Poly(q,*variables).total_degree() if q!=0 else -1
                    self.require(label+' primitive degree bound',qdegree<=N+1-z['d'])
            divnext=division_maps(k,N+1)
            self.eq(label+' consecutive cokernel kills derivative',divnext['r']*Tnext,
                    sp.zeros(divnext['r'].rows,Tnext.cols))
            self.require(label+' consecutive quotient injection',Tnext.rank()==z['E'].cols)
            self.require(label+' consecutive quotient cokernel',
                         after['E'].cols-Tnext.rank()==divnext['r'].rows)
            DERIVATIVE_RECORDS.append({'k':k,'N':N,'repeated':repeated,'asymmetric':asymmetric,
                                       'source_layer_dimension':z['E'].cols,
                                       'target_layer_dimension':after['E'].cols,
                                       'induced_derivative_rank':Tnext.rank(),
                                       'retained_difference_rank':actual_difference.rank(),
                                       'cokernel_dimension':divnext['r'].rows})

    def test_04_homogeneous_shell_substitution_counterexample(self):
        z=negative_fixture()
        self.eq('negative fixture original metric',z['G'],sp.Matrix([[9]]))
        self.eq('unprojected boundary lies in admitted relations',z['P']*z['B'],z['B'])
        self.require('unprojected boundary retained and nonzero',z['B'].rank()==1)
        self.eq('actual projected boundary vanishes',z['C'],sp.zeros(9,1))
        self.require('actual orthogonal shell rank zero',z['top'].rank()==0)
        self.require('raw homogeneous shell rank one',z['homogeneous'].rank()==1)
        self.require('actual KL14 rank equality',z['C'].rank()==z['top'].rank())
        self.require('incorrect shell substitution is detected',z['C'].rank()!=z['homogeneous'].rank())
        self.eq('original next layer Gram',z['layer_gram'],sp.Matrix([[6,0,4],[0,4,0],[4,0,6]]))


def main():
    global SOURCE
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path,required=True)
    parser.add_argument('--dependency',type=Path,
                        default=Path(__file__).resolve().parents[1]/'sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration/check_kernel_layer.py')
    parser.add_argument('--self-test-failure',action='store_true')
    args=parser.parse_args()
    dependency=args.dependency.resolve(strict=True)
    raw=dependency.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=DEPENDENCY_SHA256:
        raise ValueError('Unexpected dependency bytes; refusing to run')
    args.json.parent.mkdir(parents=True,exist_ok=True)
    isolated=args.json.parent/(args.json.stem+'_dependency')
    isolated.mkdir(exist_ok=True)
    copied=isolated/'check_kernel_layer.py'
    shutil.copyfile(dependency,copied)
    spec=importlib.util.spec_from_file_location('delivered_kernel_layer_fixture',copied)
    SOURCE=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SOURCE)
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ContinuationTests)
    if args.self_test_failure:
        class IncorrectHomogeneousSubstitution(unittest.TestCase):
            def runTest(self):
                z=negative_fixture()
                self.assertEqual(z['C'].rank(),z['homogeneous'].rank(),
                                 'deliberately replacing actual orthogonal shell by homogeneous shell')
        suite.addTest(IncorrectHomogeneousSubstitution())
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    unchanged=dependency.read_bytes()==raw
    record={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'success':result.wasSuccessful() and unchanged,'assertion_evaluations':len(RECORDS),
            'python':sys.version,'sympy':sp.__version__,'optimized':sys.flags.optimize,
            'self_test_failure':args.self_test_failure,'dependency':str(dependency),
            'dependency_copy':str(copied.resolve()),'dependency_sha256':DEPENDENCY_SHA256,
            'dependency_unchanged':unchanged,'rank_records':RANK_RECORDS,
            'two_level_derivative_records':DERIVATIVE_RECORDS,'assertions':RECORDS,
            'negative_fixture':{'h':'s-1/2','k':2,'N':1,'heights':[-1,0,1],'weights':[1,1,1],
                                'rank_actual_orthogonal_top':0,'rank_raw_homogeneous_top':1,
                                'rank_unprojected_boundary':1,'rank_actual_C':0},
            'scope':'Exact finite discrete-measure and polynomial calibrations for KL.11--KL.20; no arithmetic or Lean certificate'}
    args.json.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['tests_run','failures','errors','success','assertion_evaluations','sympy','optimized']}))
    return 0 if record['success'] else 1


if __name__=='__main__':
    raise SystemExit(main())
