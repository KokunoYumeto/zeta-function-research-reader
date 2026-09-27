# Referee check: the polynomial map of Section 6.1 (det DF = -2, the three-point fibre, the escaping curve).
import sympy as sp
x, y, w, tau = sp.symbols('x y w tau')
F = sp.Matrix([(1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y),
               y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y),
               2*x - 3*x**2*y - x**3*w])
J = F.jacobian([x, y, w])
print("det DF =", sp.expand(J.det()))
for P in [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]:
    print(P, "->", list(F.subs({x: P[0], y: P[1], w: P[2]})))
# the full fibre over (-1/4, 0, 0)
sol = sp.solve([F[0] + sp.Rational(1, 4), F[1], F[2]], [x, y, w], dict=True)
print("all solutions of F = (-1/4,0,0):", sol)
# the curve gamma(tau) = (1/z, -3z/2, 13 z^2/2), z = sqrt(1-8 tau): is F(gamma) affine in tau?
z = sp.sqrt(1 - 8*tau)
g = {x: 1/z, y: -sp.Rational(3, 2)*z, w: sp.Rational(13, 2)*z**2}
Fg = [sp.simplify(sp.expand(c.subs(g))) for c in F]
print("F(gamma(tau)) =", Fg)
# gamma' = DF^{-1} c with c = dF(gamma)/dtau ?
c = [sp.diff(v, tau) for v in Fg]
gam = sp.Matrix([1/z, -sp.Rational(3, 2)*z, sp.Rational(13, 2)*z**2])
lhs = J.subs(g) * gam.diff(tau)
print("DF(gamma) gamma' - c =", [sp.simplify(lhs[i] - c[i]) for i in range(3)])
# divergence of V = DF^{-1} c for constant c
cc = sp.Matrix(sp.symbols('c1 c2 c3'))
Vf = sp.simplify(J.adjugate() * cc / J.det())
print("div V =", sp.simplify(sum(sp.diff(Vf[i], v) for i, v in enumerate([x, y, w]))))
