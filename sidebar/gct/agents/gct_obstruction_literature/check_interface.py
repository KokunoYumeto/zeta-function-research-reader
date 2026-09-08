"""Exact finite checks for the maps proved for every n in the TeX section."""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
records = []
for n in (1, 2, 3):
    D, q = 4*n+1, 5*n+1
    variables = []
    for i in range(1, n+1):
        variables.extend(s.symbols(f'a{i} b{i} c{i} r{i} t{i}'))
    z = s.Symbol('z')
    variables.append(z)
    M = s.zeros(D)
    expected = 0
    for i in range(n):
        a,b,c,r,t = variables[5*i:5*i+5]
        j = 4*i
        for k in range(4):
            M[j+k,j+k] = z
        for k in range(3):
            M[j+k,j+k+1] = -r
        for k,v in enumerate((-2*a,b,-2*z,c)):
            M[j+k,D-1] = v
        M[D-1,j] = -t
        expected += t*(c*r**3-2*z**2*r**2+b*r*z**2-2*a*z**3)
    expected *= z**(4*n-4)
    L = s.Matrix(list(M)).jacobian(variables)
    p = s.eye(D*D)[:q,:]
    inclusion = p.T
    assert p*inclusion == s.eye(q)
    assert L.rank() == q
    A = L*p
    assert A*inclusion == L
    assert A.rank() == q
    assert D*D-q > 0
    assert s.expand(M.det(method='domain-ge')-expected) == 0
    # Every omitted coordinate vector is annihilated by the exact p and A.
    assert p[:,q:] == s.zeros(q,D*D-q)
    assert A[:,q:] == s.zeros(D*D,D*D-q)
    # One exact invertible member of the proved epsilon pencil.
    epsilon = next(k for k in range(1, D*D+2) if (A+k*s.eye(D*D)).det() != 0)
    records.append({'n':n,'D':D,'source_variable_count':q,
                    'ambient_variable_count':D*D,'rank_L':q,'rank_A':q,
                    'annihilator_dimension_lower_bound':D*D-q,
                    'invertible_pencil_parameter':epsilon,
                    'homogeneous_determinant_identity':True,
                    'coordinate_left_inverse_and_endomorphism_extension':True})

# The derivative-annihilator proof uses distinct row/column multidegrees.
Y = s.Matrix(3,3,s.symbols('Y0:9'))
cofactors = [Y.cofactor(i,j) for i in range(3) for j in range(3)]
monomials = sorted({mon for c in cofactors for mon in s.Poly(c,list(Y)).monoms()})
C = s.Matrix([[s.Poly(c,list(Y)).coeff_monomial(mon) for c in cofactors] for mon in monomials])
assert C.rank() == 9
result = {'status':'passed','scope':'Exact finite checks n=1,2,3; general proof is in gct_obstruction_interface.tex',
          'records':records,'D3_cofactor_independence_rank':9}
(ROOT/'interface_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
