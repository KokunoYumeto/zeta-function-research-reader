# Referee 21 (wbreader): is the fibre F^{-1}(-1/4,0,0) exactly the three displayed points (over C)?
import sympy as sp
x, y, w = sp.symbols('x y w')
F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y) + sp.Rational(1,4)
F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y)
F3 = 2*x - 3*x**2*y - x**3*w
G = sp.groebner([F1, F2, F3], w, y, x, order='lex')
print("lex Groebner basis (last element univariate in x):")
for g in G.exprs: print("  ", sp.factor(g))
sols = sp.solve([F1, F2, F3], [x, y, w], dict=True)
print("solutions:", sols)
