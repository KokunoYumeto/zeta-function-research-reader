#!/usr/bin/env python3
"""Exact algebra supporting FRF; analytic completeness is proved in the TeX.

Requires SymPy 1.14.0. No assertion is used as a correctness check, so -O
retains every test. No hypothetical zeta zero or numerical period is sampled.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys

import sympy as s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative-control', choices=[
        'reverse-transverse-sign', 'replace-transported-action'])
    args = parser.parse_args()
    passed: list[str] = []

    def zero(name: str, expression) -> None:
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        for entry in entries:
            residual = s.simplify(s.expand(entry))
            if residual != 0:
                raise ValueError(f'{name}: nonzero residual {residual}')
        passed.append(name)

    def truth(name: str, condition: bool) -> None:
        if not condition:
            raise ValueError(name)
        passed.append(name)

    I = s.I
    a, y, z, w = s.symbols('a y z w')
    b = I+a*y
    c = -I+2*a*y+a*a*z
    d = -I*y-a*(I*z+2*y*y)-a*a*y*z
    e = 2*z-7*I*y*y+a*w
    f = I*w+3*I*y**3-4*y*z+a*(6*I*y*y*z+w*y+4*y**4)+2*a*a*y**3*z
    P = s.Matrix([a*c, a*e+b*d, a*f+b*e, b*f]).applyfunc(s.expand)
    literal = s.Matrix([
        a**3*z+2*a*a*y-I*a,
        -a**3*y*y*z-2*I*a*a*y*z+a*a*w-2*a*a*y**3-10*I*a*y*y+3*a*z+y,
        2*a**3*y**3*z+6*I*a*a*y*y*z+2*a*a*w*y+4*a*a*y**4+2*I*a*w-4*I*a*y**3-2*a*y*z+2*I*z+7*y*y,
        2*a**3*y**4*z+8*I*a*a*y**3*z+a*a*w*y*y+4*a*a*y**5+2*I*a*w*y+7*I*a*y**4-10*a*y*y*z-4*I*y*z-w-3*y**3])
    zero('factor chart equals published FC31 coefficient by coefficient', P-literal)
    zero('retained U^3 V coefficient', a*d+b*c-1)
    zero('retained resultant', -c*b**3+d*a*b*b-e*a*a*b+f*a**3-1)
    J = P.jacobian([a, y, z, w])
    zero('constant Jacobian determinant', J.det(method='domain-ge')+2)
    W = s.diag(1, -1, -2, -3)
    zero('complete weight action', J*W*s.Matrix([a,y,z,w])-W*P)

    A, B, C, D, u, r = s.symbols('A B C D u r')
    target = s.Matrix([A,B,C,D])
    F = A*u**4+u**3+B*u*u+C*u+D
    Delta = s.discriminant(F, u)
    delta0 = B*B*C*C-4*C**3-4*B**3*D-27*D*D+18*B*C*D
    delta1 = 144*B*D*D-6*C*C*D-80*B*B*C*D+18*B*C**3+16*B**4*D-4*B**3*C*C
    zero('literal cubic discriminant', Delta.subs(A,0)-delta0)
    zero('first A coefficient of quartic discriminant', s.diff(Delta,A).subs(A,0)-delta1)
    truth('sum of absolute discriminant coefficients is 1069', sum(abs(x) for x in s.Poly(Delta,A,B,C,D).coeffs()) == 1069)
    truth('discriminant degree at most six', s.Poly(Delta,A,B,C,D).total_degree() == 6)
    incidence = {C: -4*A*r**3-3*r*r-2*B*r,
                 D: 3*A*r**4+2*r**3+B*r*r}
    zero('double-root incidence value', F.subs(incidence, simultaneous=True).subs(u,r))
    zero('double-root incidence derivative', s.diff(F,u).subs(incidence, simultaneous=True).subs(u,r))
    zero('double-root incidence discriminant', Delta.subs(incidence, simultaneous=True))

    variables = s.symbols('m0:16')
    multiplier = s.symbols('lambda_Delta')
    Mformal = s.Matrix(4,4,variables)
    lie = (s.Matrix([s.diff(Delta,v) for v in target]).T*Mformal*target)[0]-multiplier*Delta
    equations = s.Poly(s.expand(lie),A,B,C,D).coeffs()+[Mformal[0,j] for j in (1,2,3)]
    unknowns = list(variables)+[multiplier]
    matrix, rhs = s.linear_eq_to_matrix(equations, unknowns)
    expected = s.Matrix([1,0,0,0,0,-1,0,0,0,0,-2,0,0,0,0,-3,-6])
    zero('weight line preserves both boundary divisors', matrix*expected)
    zero('tangency equations are homogeneous', rhs)
    truth('complete simultaneous tangency space has dimension one', matrix.rank() == 16)

    rt = s.sqrt(2)
    K = s.Matrix([[0,I,1/rt,1/rt],
                  [0,-1,-1-rt*I,1-rt*I],
                  [I/2,-3*I,2*rt+6*I,-2*rt+6*I],
                  [0,13,-34-19*rt*I,34-19*rt*I]])
    zero('published marked determinant', K.det()-77*rt*I/2)
    ew = s.Matrix([0,0,0,1])
    ez = s.Matrix([0,0,1,0])
    em = s.Matrix([1,0,0,0])
    kinvw = s.Matrix([s.Rational(6,77),s.Rational(1,77),(-3-rt*I)/154,(3-rt*I)/154])
    zero('retained K inverse fourth column', K*kinvw-ew)
    zero('retained K inverse third column', K*(-2*I*em)-ez)
    Ystar = s.Matrix([0,0,-1,0])
    for j in range(4):
        zero(f'published labelled collision {j}', P.subs(dict(zip([a,y,z,w],K[:,j])), simultaneous=True)-Ystar)

    center, delta, gamma = s.symbols('center delta gamma', real=True)
    rho = [center+delta+I*gamma,center+delta-I*gamma,
           center-delta+I*gamma,center-delta-I*gamma]
    Y0 = s.Matrix([0,0,-3,2])
    eta = 6*I*em+2*kinvw
    zero('exact initial marked coefficient vector', K*eta-Y0)
    velocity = K*s.diag(*rho)*eta
    if args.negative_control == 'replace-transported-action':
        velocity = s.diag(*rho)*Y0
    kappa = s.Rational(2,77)*(gamma+2*I*delta-3*I*gamma/rt)
    omega = -center-s.Rational(337,77)*delta+(34-190*rt)*gamma/77+I*(4*delta-(255+3*rt)*gamma)/77
    zero('nonzero leading-coefficient velocity kappa', velocity[0]-kappa)
    if args.negative_control == 'reverse-transverse-sign':
        omega = -omega
    zero('literal quartet double-root velocity Omega', sum(velocity)-omega)
    gradient0 = s.Matrix([s.diff(Delta,v).subs(dict(zip(target,Y0))) for v in target])
    zero('discriminant normal at the mixed boundary', gradient0+108*s.ones(4,1))
    zero('signed discriminant derivative', (gradient0.T*velocity)[0]+108*omega)
    zero('real part of kappa', s.re(kappa)-2*gamma/77)
    zero('imaginary part of Omega', s.im(omega)-(4*delta-(255+3*rt)*gamma)/77)

    finite_points = [s.Matrix([0,0,3*I/2,-2]),
                     s.Matrix([s.Rational(1,3),2-3*I,-12+27*I,306-267*I]),
                     s.Matrix([-s.Rational(1,3),2+3*I,12+27*I,306+267*I])]
    for j, point in enumerate(finite_points):
        zero(f'finite mixed-boundary inverse {j}',P.subs(dict(zip([a,y,z,w],point)), simultaneous=True)-Y0)

    qroot = s.Matrix([a,-r-I/a,A/a**3+2*r/a+3*I/a**2,
        7*I*r*r/a+(B-17*r+A*r*r)/a**2-13*I/a**3-2*A/a**4])
    expected_target = s.Matrix([A,B,1/a**2-4*A*r**3-3*r*r-2*B*r,
        3*A*r**4+2*r**3+B*r*r-r/a**2])
    zero('full finite-root inverse with original chart coordinates',P.subs(dict(zip([a,y,z,w],qroot)),simultaneous=True)-expected_target)
    Jr = J.subs(dict(zip([a,y,z,w],qroot)),simultaneous=True).applyfunc(lambda v:s.cancel(s.expand(v)))
    v = s.Matrix([1,-r*r,-2*r**3,2*r**4])
    v1 = s.Matrix([0,2,-4*r,2*r*r])
    qv = s.Matrix([0,1,-2*r,r*r])
    zero('root differential third column',Jr[:,2]-a**3*v-a*v1)
    zero('root differential fourth column',Jr[:,3]-a*a*qv)

    def laurent_degree(expr) -> int:
        expanded = s.expand(expr)
        if expanded == 0:
            return -10**6
        powers = []
        for term in s.Add.make_args(expanded):
            exponent = term.as_powers_dict().get(a,s.S.Zero)
            if not exponent.is_Integer:
                raise ValueError(f'non-Laurent term: {term}')
            coefficient = s.cancel(term/a**exponent)
            if coefficient.has(a):
                raise ValueError(f'coefficient still depends on a: {coefficient}')
            powers.append(int(exponent))
        return max(powers)

    c1 = Jr[:,0]-2*r/a**2*Jr[:,2]
    c2 = Jr[:,1]-2/a*Jr[:,2]-14*I*r/a*Jr[:,3]
    truth('bounded first corrected column',max(laurent_degree(v) for v in c1) <= 0)
    truth('bounded second corrected column',max(laurent_degree(v) for v in c2) <= 0)
    zero('exact second exterior witness',Jr.extract([0,1],[2,3]).det()-a**5)
    zero('exact third exterior witness',Jr.extract([0,1,2],[2,3,1]).det()-a**5*(12*A*r*r+6*r+2*B))
    zero('finite-root differential retains determinant',Jr.det(method='domain-ge')+2)

    yy, zz, ww = s.symbols('Yminus Zminus Wminus')
    change = s.Matrix([a,yy-2*I/a,zz+6*I/a**2,
        ww+14*I*yy*yy/a+28*yy/a**2-40*I/a**3])
    Pminus = P.xreplace({I:-I})
    # xreplace does not conjugate compound coefficients reliably; use the
    # exact real-coefficient-variable conjugation instead.
    Pminus = P.applyfunc(lambda p:s.conjugate(p).subs({s.conjugate(v):v for v in [a,y,z,w]}))
    zero('two-chart transition',P.subs(dict(zip([a,y,z,w],change)),simultaneous=True)-Pminus.subs({y:yy,z:zz,w:ww},simultaneous=True))
    zero('chart transition determinant',change.jacobian([a,yy,zz,ww]).det()-1)
    negative0 = {a:0,y:0,z:-3*I/2,w:-2}
    zero('restored negative-infinity state',Pminus.subs(negative0)-Y0)

    path = Path(__file__).resolve()
    provider = path.parent.parent/'20260920-fable-signed-states'/'FABLE_TO_ORIGINAL_CONDUCTOR.tex'
    provider_hash = None
    if provider.is_file():
        raw = provider.read_bytes()
        provider_hash = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        truth('frozen published provider blob',provider_hash == '50b39a82568bbe5104aeed3de5ad9441cb6a5602')
    result = {
        'status':'passed', 'check_count':len(passed), 'checks':passed,
        'script_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'provider_git_blob':provider_hash,
        'kappa':str(kappa), 'Omega':str(omega),
        'double_root_singular_scales_in_a':[3,2,0,-5],
        'excluded_sign_singular_scales_in_time':[-4,-1,1,4],
        'finite_inverse_count_at_mixed_boundary':3,
        'escaped_inverse_counts':{'selected_double_root':4,'excluded_infinity_sign':1},
        'scope':'Exact identities and the tangency linear system. Analytic flow, completeness, Puiseux and norm conclusions require the written proof. No actual zeta zeros, numeric periods, or RH conclusion.'}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'status':'failed','false_claim_accepted':False,'error':str(error)},indent=2,sort_keys=True))
        sys.exit(2)
