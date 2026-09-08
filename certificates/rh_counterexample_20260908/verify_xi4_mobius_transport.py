"""Exact regressions for the unchanged xi4 Mobius/coordinate calculation.

The analytic endpoint proof is in the reader, not established by these finite
regressions. Read-only unless --write; one capped process, no zero search.
"""
from resource_ceiling import install_memory_ceiling
RESOURCE = install_memory_ceiling()
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
s, z, t, u, v = sp.symbols('s z t u v')
c0, c1, c2 = -sp.Rational(59, 275184), sp.Rational(1, 1296), sp.Rational(3, 132496)


def td(f):
    return (c0*f.subs(s,s+3)-sp.diff(f,s).subs(s,s+3)/336
            +c1*f.subs(s,s+sp.Rational(9,2))+c2*f.subs(s,s+sp.Rational(13,2)))


def commutator(f):
    return ((3*c0-sp.Rational(1,336))*f.subs(s,s+3)
            -sp.diff(f,s).subs(s,s+3)/112
            +sp.Rational(9,2)*c1*f.subs(s,s+sp.Rational(9,2))
            +sp.Rational(13,2)*c2*f.subs(s,s+sp.Rational(13,2)))


def heat(f):
    degree = sp.Poly(f,s).degree()
    return sum((-t/4)**k*sp.diff(f,s,2*k)/sp.factorial(k)
               for k in range(int(degree)//2+1))


def checks():
    passed = []
    def eq(name, left, right):
        assert sp.expand(left-right) == 0, name
        passed.append(name)

    eq('original_mass', c0+c1+c2, sp.Rational(127,219024))
    eq('original_first_moment', 3*c0-sp.Rational(1,336)+sp.Rational(9,2)*c1+sp.Rational(13,2)*c2, 0)
    w = sp.exp(-3*sp.I*u)*(c0+sp.I*u/336)+c1*sp.exp(-sp.Rational(9,2)*sp.I*u)+c2*sp.exp(-sp.Rational(13,2)*sp.I*u)
    iwprime = sp.exp(-3*sp.I*u)*(3*c0-sp.Rational(1,336)+sp.I*u/112)+sp.Rational(9,2)*c1*sp.exp(-sp.Rational(9,2)*sp.I*u)+sp.Rational(13,2)*c2*sp.exp(-sp.Rational(13,2)*sp.I*u)
    eq('full_iw_prime', sp.I*sp.diff(w,u), iwprime)
    for d in range(9):
        f = s**d
        eq(f'commutator_degree_{d}', td(s*f)-s*td(f), commutator(f))
        eq(f'heat_commutation_degree_{d}', td(heat(f)), heat(td(f)))
        af = td(heat(f))
        eq(f'full_conjugated_coordinate_degree_{d}', td(heat(s*f)), s*af-t*sp.diff(af,s)/2+commutator(heat(f)))
        H = z**d
        f_from_H = H.subs(z,sp.Rational(1,2)-sp.I*s)
        exact_numerator = (c0*H.subs(z,z-3*sp.I)+sp.I*sp.diff(H,z).subs(z,z-3*sp.I)/336
                           +c1*H.subs(z,z-sp.Rational(9,2)*sp.I)
                           +c2*H.subs(z,z-sp.Rational(13,2)*sp.I))
        eq(f'Mellin_shift_derivative_degree_{d}', td(f_from_H).subs(s,sp.I*(z-sp.Rational(1,2))), exact_numerator)

    # Gaussian transform differentiation and the exact gamma recurrence.
    y = sp.symbols('y', real=True)
    G = sp.exp(-sp.pi*y*y)
    transformed = 4*sp.pi**2*sp.diff(G,y,4)/(2*sp.pi)**4+6*sp.pi*sp.diff(G,y,2)/(2*sp.pi)**2
    assert sp.simplify(transformed-(4*sp.pi**2*y**4-6*sp.pi*y**2)*G) == 0
    passed.append('Hermite_self_duality_original_2pi')
    eq('Hermite_Mellin_polynomial', (4*(z/2)*(z/2+1)-6*(z/2))/2, z*(z-1)/2)

    # Finite Euler product and logarithmic derivative identities. The symbols
    # X_p and ell_p stand for p^(-ia) and log(p); no division by 1-X_p.
    for k in range(1,129):
        primes = list(sp.factorint(k))
        X = {p:sp.Symbol(f'X{p}') for p in primes}
        ell = {p:sp.Symbol(f'L{p}') for p in primes}
        J, L = sp.Integer(0), sp.Integer(0)
        for d in sp.divisors(k):
            mu = sp.mobius(d)
            term = mu*sp.prod(X[p]**e for p,e in sp.factorint(d).items())
            J += term
            L += term*sum(e*ell[p] for p,e in sp.factorint(d).items())
        eq(f'divisor_product_{k}', J, sp.prod(1-X[p] for p in primes))
        eq(f'logarithmic_divisor_{k}', L, sum(-X[p]*ell[p]*sp.prod(1-X[q] for q in primes if q!=p) for p in primes))
        eq(f'Mobius_inverse_{k}', sum(sp.mobius(d) for d in sp.divisors(k)), int(k==1))

    r, h, R, F0, F1, X1, X2 = sp.symbols('r h R F0 F1 X1 X2', nonzero=True)
    ds = -r*h-h*h/2
    ratio = (F0+F1*ds)/(X1*ds+X2*ds*ds/2)
    expanded = sp.series(ratio,h,0,1).removeO()
    eq('cover_principal_and_constant', expanded,
       -F0/(X1*r*h)+F1/X1-F0*X2/(2*X1**2)+F0/(2*X1*r*r))
    B = sp.Symbol('B')
    matrix = sp.Matrix([[0,-2*B],[1,0]])
    assert matrix**2 == -2*B*sp.eye(2)
    passed.append('full_two_component_cover_square')
    for m in range(1,8):
        a = sp.symbols(f'a0:{m}')
        b = sp.symbols(f'b0:{m}')
        product = sp.expand(sum(a[j]*v**j for j in range(m))*sum(b[j]*v**j for j in range(m)))
        for q in range(m):
            eq(f'all_multiplicity_{m}_principal_{q}', product.coeff(v,q), sum(a[q-n]*b[n] for n in range(q+1)))
    return passed


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    passed=checks()
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    source=ROOT/'tex/satellites/29e_xi4_mobius_endpoint.tex'
    pole=HERE/'xi4_trace_pole_results.json'
    saved_pole=json.loads(pole.read_text(encoding='utf-8'))
    assert saved_pole['unique_simple_real_Xi_zero'] and saved_pole['status']=='pass'
    data={'schema_version':1,'status':'pass','resource':RESOURCE,
          'script_sha256':digest(Path(__file__)), 'manuscript_sha256':digest(source),
          'pole_receipt_sha256':digest(pole),'check_count':len(passed),'checks':passed,
          'analytic_scope':'Finite exact regressions supplement, not replace, the complete convergence and endpoint proofs in the manuscript.',
          'endpoint_results':'For actual time-zero inverse: not O(x^(-beta)) for beta<1/2; weighted absolute integral diverges for sigma<=1/2; all derivatives O(x^(-j-1)).',
          'RH_counterexample':False,'Lean_used':False}
    if args.write:
        (HERE/'xi4_mobius_transport_results.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,indent=2))


if __name__=='__main__':
    main()
