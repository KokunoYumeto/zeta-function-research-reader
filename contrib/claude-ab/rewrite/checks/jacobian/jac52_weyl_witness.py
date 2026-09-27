#!/usr/bin/env python3
"""jac52_weyl_witness.py -- note 52_, Proposition 52.3: prints the explicit endomorphism of the Weyl algebra A_3,
x_i -> F_i, d_i -> D_i = sum_k (DF^{-1})_{ki} d_k, for the Jacobian-conjecture counterexample F of Alpoege (20 July 2026).

Output: the nine coefficient polynomials (DF^{-1})_{ki} (entry k of the vector field D_i), with total degree and number of
terms, printed in expanded form.  Denominators are 1 or 2 (DF^{-1} = adj(DF)/(-2), adj(DF) integral).
The relations [D_i, F_j] = delta_ij and [D_i, D_j] = 0 are checked in jac52_checks.py (item 52.7).
"""
import sympy as sp
x, y, w = sp.symbols('x y w')
F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y)
F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y)
F3 = 2*x - 3*x**2*y - x**3*w
F = sp.Matrix([F1, F2, F3])
DF = F.jacobian([x, y, w])
Dinv = (DF.adjugate()/(-2)).applyfunc(sp.expand)     # DF^{-1}
names = ('d_x', 'd_y', 'd_w')
print("F1 =", sp.expand(F1)); print("F2 =", sp.expand(F2)); print("F3 =", sp.expand(F3))
print("det DF =", sp.expand(DF.det()))
print()
for i in range(3):
    print(f"D_{i+1} = sum_k (DF^-1)_(k,{i+1}) d_k, with")
    for k in range(3):
        e = Dinv[k, i]
        P = sp.Poly(e, x, y, w)
        print(f"  coefficient of {names[k]} (degree {P.total_degree()}, {len(P.terms())} terms):")
        print("    " + str(e))
    print()
# sanity: D_i(F_j) = delta_ij
ok = all(sp.expand(sum(Dinv[k, i]*sp.diff(F[j], v) for k, v in enumerate((x, y, w))) - (1 if i == j else 0)) == 0
         for i in range(3) for j in range(3))
print("sanity D_i(F_j) = delta_ij:", "PASS" if ok else "FAIL")
