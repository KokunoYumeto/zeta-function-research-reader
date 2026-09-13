"""Exact finite calibrations of CT.3--4 and CT.17--26.

Discrete positive calibration measures only; no arithmetic zeros or
infinite analytic integrals are asserted.  The original PR14 script is
loaded without editing it or creating bytecode beside its source.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import sympy as s

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/web_pr14_delivery/Tau_Coherent_Interpolation_Control/check_interpolation_control.py'
spec = importlib.util.spec_from_file_location('pr14_original', SOURCE)
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
records = []


def check(name, condition):
    if not bool(condition):
        raise RuntimeError(name)
    records.append(name)


def eq(name, left, right):
    difference = s.Matrix(left) - s.Matrix(right)
    check(name, all(s.cancel(s.expand(x)) == 0 for x in difference))


t = s.Symbol('t')
half = s.Rational(1, 2)


def model(modulus, global_poly, k, degree):
    d = modulus.degree()
    exps = original.basis(k, degree)
    nodes = [half + s.I * j for j in [-2, -1, 0, 1, 2]]
    points = list(itertools.product(nodes, repeat=k))
    multiplier = s.exquo(global_poly, modulus).as_expr()
    T = original.clean([[s.prod(multiplier.subs(t, z) * z**a for z, a in zip(point, exp))
                         for exp in exps] for point in points])
    Omega = s.diag(*(s.prod(1 + s.im(z)**2 for z in point) for point in points))
    M = original.clean(T.H * Omega * T)
    C0 = s.Matrix.hstack(*(original.kron_all([original.coeff(original.rem(t**a, modulus), d)
                                             for a in exp]) for exp in exps))
    unit = original.kron_all([original.multiplication(multiplier, modulus)] * k)
    J = original.clean(unit * C0)
    K = original.clean(C0 * M.inv() * C0.H)
    G = original.clean((J * M.inv() * J.H).inv())
    R = original.clean(T * M.inv() * J.H * G)
    null = J.nullspace()
    B = T * s.Matrix.hstack(*null) if null else s.zeros(T.rows, 0)
    P = original.clean(B * (B.H * Omega * B).inv() * B.H * Omega) if null else s.zeros(T.rows)
    A1 = original.multiplication(t, modulus)
    A = s.zeros(d**k)
    for j in range(k):
        A += original.kron_all([A1 if i == j else s.eye(d) for i in range(k)])
    W = original.clean(A.H * G + G * A - k * G)
    return dict(T=T, Omega=Omega, M=M, C0=C0, J=J, K=K, unit=unit,
                G=G, R=R, B=B, P=P, A=A, W=W, exps=exps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', type=Path, required=True)
    parser.add_argument('--self-test-failure', action='store_true')
    args = parser.parse_args()
    h = s.Poly(t-s.Rational(1,4), t)
    H = s.Poly((t-s.Rational(1,4))*(t-s.Rational(3,4)), t)
    extra = s.Poly((t-s.Rational(1,8))*(t-s.Rational(7,8)), t)
    g = H * extra
    m = s.exquo(H,h).as_expr()
    iota = original.coeff(original.rem(m * s.invert(m,h.as_expr()), H), 2)
    for k, degree in [(1,1),(2,0)]:
        small = model(h,g,k,degree)
        large = model(H,g,k,degree+k)
        I = original.kron_all([iota] * k)
        prefix = f'k{k}-M{degree}'
        for label,z in [('h',small),('H',large)]:
            eps = z['unit'].inv()
            eq(prefix+label+'-unit-kernel', z['G'], eps.H*z['K'].inv()*eps)
            eq(prefix+label+'-source-Gram', z['R'].H*z['Omega']*z['R'],z['G'])
            eq(prefix+label+'-boundary-orthogonality',z['B'].H*z['Omega']*z['R'],s.zeros(z['B'].cols,z['R'].cols))
        eq(prefix+'-action',large['A']*I,I*small['A'])
        eq(prefix+'-boundary-inclusion',large['P']*small['B'],small['B'])
        E = original.clean(large['P']-small['P'])
        eq(prefix+'-difference-projection',E*E,E)
        Z = original.clean(E*small['R'])
        eq(prefix+'-representative-transport',large['R']*I,small['R']-Z)
        loss = original.clean(Z.H*small['Omega']*Z)
        eq(prefix+'-Gram-transport',I.H*large['G']*I,small['G']-loss)
        correction = original.clean(small['A'].H*loss+loss*small['A']-k*loss)
        eq(prefix+'-control-transport',I.H*large['W']*I,small['W']-correction)
        expected = s.binomial(degree+k+k,k)-2**k-s.binomial(degree+k,k)+1
        check(prefix+'-additional-layer-dimension',E.rank()==expected)
        if k==1:
            eq(prefix+'-exact-one-variable-naturality',loss,s.zeros(1))
        else:
            check(prefix+'-strict-joint-Gram-loss',loss[0,0]>0)

    z = original.data(k=2,N=2)
    nxt = original.data(k=2,N=3)
    E = original.clean(nxt['P']-z['P'])
    Y = original.clean(E*z['R'])
    C = original.clean((s.eye(z['T'].rows)-z['P'])*z['B'])
    loss = original.clean(z['G']-nxt['G'])
    Ginv = z['G'].inv()
    eq('tensor-layer-factorization',z['W'],-Y.H*z['Omega']*C-C.H*z['Omega']*Y)
    eq('tensor-layer-loss',loss,Y.H*z['Omega']*Y)
    check('positive-loss-rank',loss.rank()==Y.rank())
    eigenvalues = [s.Rational(1,2),s.Integer(1),s.Integer(1),s.Rational(3,2)]
    departure = s.cancel(s.trace(Ginv*z['A'].H*z['G']*z['A'])-sum(abs(v)**2 for v in eigenvalues))
    second = s.cancel(s.trace(Ginv*z['W']*Ginv*z['W']))
    check('full-tensor-departure',s.cancel(second-4*sum((v-1)**2 for v in eigenvalues)-2*departure)==0)
    check('departure-nonnegative',departure>=0)
    tau = s.cancel(s.trace(Ginv*loss))
    pi = s.cancel(nxt['G'].det()/z['G'].det())
    chi = s.cancel(s.trace(Ginv*C.H*z['Omega']*C))
    check('loss-determinant-lower',1-pi<=tau)
    check('relative-flux',1<=tau*chi)
    check('relative-loss-below-rank',tau<loss.rank())
    check('same-metric-zero-trace',s.trace(Ginv*z['W'])==0)
    if args.self_test_failure:
        check('deliberate-failure',False)
    result = {'success':True,'records':records,'checks':len(records),
              'scope':'Exact finite discrete-measure calibration; no arithmetic zero or infinite-integral certificate.',
              'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'sympy':s.__version__}
    args.json.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
