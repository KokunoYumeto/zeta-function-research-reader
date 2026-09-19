#!/usr/bin/env python3
"""Exact algebra for FRF-X; completeness itself has a separate written proof.

SymPy 1.14.0. All checks remain active under python -O.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--negative-control', choices=['omit-resultant-square'])
    args = parser.parse_args()
    checks: list[str] = []

    def zero(name: str, expression) -> None:
        entries = list(expression) if isinstance(expression,s.MatrixBase) else [expression]
        for entry in entries:
            value = s.factor(s.expand(entry))
            if value != 0:
                raise ValueError(f'{name}: nonzero residual {value}')
        checks.append(name)

    def truth(name: str, condition: bool) -> None:
        if not condition:
            raise ValueError(name)
        checks.append(name)

    a,b,c,d,e,f = s.symbols('a b c d e f')
    coordinates = s.Matrix([a,b,c,d,e,f])
    H = a*d+b*c
    R = -c*b**3+d*a*b*b-e*a*a*b+f*a**3
    product = s.Matrix([a*c,a*e+b*d,a*f+b*e,b*f])
    total = s.Matrix([H,R,*product])
    J = total.jacobian(coordinates)
    expected = 2*R if args.negative_control == 'omit-resultant-square' else 2*R**2
    zero('full six-coordinate determinant is twice the resultant square',J.det(method='domain-ge')-expected)
    # Verify the adjugate lift without specializing away the original resultant.
    formal_velocity = s.Matrix(s.symbols('v0:4'))
    rhs = s.Matrix([0,0,*formal_velocity])
    lifted = J.adjugate(method='berkowitz')*rhs/2
    zero('ambient lifted-field identity retains R squared',J*lifted-R**2*rhs)

    vector = s.diag(1,0,0,-1,-2,-3)*coordinates
    zero('completed weight field preserves both constraints',s.Matrix([H,R]).jacobian(coordinates)*vector)
    zero('completed weight field returns exactly the target weight field',product.jacobian(coordinates)*vector-s.diag(1,-1,-2,-3)*product)

    A,B,C,D,u = s.symbols('A B C D u')
    target = s.Matrix([A,B,C,D])
    Delta = s.discriminant(A*u**4+u**3+B*u*u+C*u+D,u)
    matrix_variables = s.symbols('m0:16')
    multiplier = s.symbols('lambda_Delta')
    M = s.Matrix(4,4,matrix_variables)
    lie = (s.Matrix([s.diff(Delta,v) for v in target]).T*M*target)[0]-multiplier*Delta
    coefficients = s.Poly(s.expand(lie),A,B,C,D).coeffs()
    linear,rhs_tangent = s.linear_eq_to_matrix(coefficients,[*matrix_variables,multiplier])
    expected_tangent = s.Matrix([1,0,0,0,0,-1,0,0,0,0,-2,0,0,0,0,-3,-6])
    zero('unconstrained discriminant tangency admits the stated weight line',linear*expected_tangent)
    zero('unconstrained tangency equations have zero right hand side',rhs_tangent)
    truth('without imposing hyperplane invariance the full tangency space still has dimension one',linear.rank() == 16)
    free_row = M[0,1]*B+M[0,2]*C+M[0,3]*D
    lie0 = s.Poly(s.expand(lie.subs(A,0)),B,C,D)
    top6 = sum(coef*B**powers[0]*C**powers[1]*D**powers[2]
               for powers,coef in lie0.terms() if sum(powers) == 6)
    zero('degree six forces the original leading hyperplane to be invariant',top6-free_row*(16*B**4*D-4*B**3*C*C))

    path = Path(__file__).resolve()
    print(json.dumps({
        'status':'passed', 'check_count':len(checks), 'checks':checks,
        'script_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'constraint_and_product_jacobian':'2 * resultant**2',
        'tangency_space_dimension':1,
        'scope':'Polynomial identities on all six factor coefficients and the unrestricted linear target tangency system. Completeness and chart continuation require the written FRF-X proof.'
    },sort_keys=True,indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'status':'failed','false_claim_accepted':False,'error':str(error)},sort_keys=True,indent=2))
        sys.exit(2)
