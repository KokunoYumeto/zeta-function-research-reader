"""Exact original marked-coordinate and quartet interpolation certificates."""
import sympy as s

i, r = s.I, s.sqrt(2)
K = s.Matrix([[0, i, 1/r, 1/r],
              [0, -1, -1-r*i, 1-r*i],
              [i/2, -3*i, 2*r+6*i, -2*r+6*i],
              [0, 13, -34-19*r*i, 34-19*r*i]])
ca = s.Matrix([-4*r-180*i/77, -30*i/77,
               (47*r-64*i)/154, (47*r+64*i)/154])
cw = s.Matrix([s.Rational(6, 77), s.Rational(1, 77),
               (-3-r*i)/154, (3-r*i)/154])
assert (K*ca-s.Matrix([1, 0, 0, 0])).applyfunc(s.simplify) == s.zeros(4, 1)
assert (K*cw-s.Matrix([0, 0, 0, 1])).applyfunc(s.simplify) == s.zeros(4, 1)
for c in [ca, cw]:
    assert all(s.simplify(v*s.conjugate(v)) > 0 for v in c)
assert s.simplify(K.det()-77*r*i/2) == 0
print("Full original K inverse columns for ea and ew verified; all8 entries nonzero.")

k, delta, gamma, S = s.symbols("k delta gamma S", positive=True)
roots = [k*(s.Rational(1, 2)+eps*delta+i*eta*gamma)
         for eps, eta in [(1,1), (1,-1), (-1,1), (-1,-1)]]
V = s.Matrix([[root**n for root in roots] for n in range(4)])
det_expected = -64*k**6*delta**2*gamma**2*(delta**2+gamma**2)
assert s.expand(V.det()-det_expected) == 0
for active_mask in range(1, 16):
    active = [j for j in range(4) if (active_mask >> j) & 1]
    for j in active:
        pol = s.sympify(s.prod((S-roots[l])/(roots[j]-roots[l]) for l in active if l != j))
        for l in active:
            assert s.simplify(pol.subs(S, roots[l])) == int(l == j)
print("Actual k-scaled quartet Vandermonde and all15 nonempty support Lagrange systems verified.")
print("All exact corner observation coefficient checks passed.")
