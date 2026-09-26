# Referee 21 (wbreader): Keller map F and escaping curve; NS-04(b) Kasner map round trip; S6-5 arithmetic.
import sympy as sp, numpy as np, itertools, math, random
x, y, w, tau = sp.symbols('x y w tau')
F = sp.Matrix([(1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y), y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y), 2*x - 3*x**2*y - x**3*w])
print("det DF =", sp.expand(F.jacobian([x, y, w]).det()))
for p in [(0, 0, sp.Rational(-1,4)), (1, sp.Rational(-3,2), sp.Rational(13,2)), (-1, sp.Rational(3,2), sp.Rational(13,2))]:
    print("  F", p, "=", list(F.subs({x: p[0], y: p[1], w: p[2]})))
zz = sp.sqrt(1-8*tau)
g = {x: 1/zz, y: -3*zz/2, w: 13*zz**2/2}
print("F(gamma(tau)) =", [sp.simplify(c.subs(g)) for c in F], "  (expect (2 tau - 1/4, 0, 0))")
gam = sp.Matrix([1/zz, -3*zz/2, 13*zz**2/2])
print("DF(gamma) gamma' =", [sp.simplify(c) for c in (F.jacobian([x, y, w]).subs(g) * gam.diff(tau))], " (expect (2,0,0))")
# Kasner: forward map, identities, inverse, surjectivity round trip from random Kasner data with P_w < 1/4
rng = np.random.default_rng(1)
def fwd(B):
    chi = math.sqrt(1 + 4/3*np.trace(B@B)); Pw = 0.25 - 0.75/chi; Pp = np.eye(3)/4 + (np.eye(3)/4 + B)/chi; return Pw, Pp
worst = 0
for _ in range(200):
    Bm = rng.normal(size=(3,3))*rng.uniform(0.01, 5); Bm = (Bm+Bm.T)/2; Bm -= np.trace(Bm)/3*np.eye(3)
    Pw, Pp = fwd(Bm)
    worst = max(worst, abs(Pw + np.trace(Pp) - 1), abs(Pw**2 + np.trace(Pp@Pp) - 1), np.abs((3*Pp + (Pw-1)*np.eye(3))/(1-4*Pw) - Bm).max())
    assert -0.5 <= Pw < 0.25
print("Kasner identities + inverse on 200 random tracefree B: max error", worst)
# surjectivity: random block-Kasner data (P_w, P_perp symmetric, trace/trace-square conditions, P_w<1/4)
worst = 0; made = 0
while made < 200:
    Pw = rng.uniform(-0.5, 0.25)
    # P_perp = aI + C with C tracefree symmetric: tr = 3a = 1 - Pw; tr P^2 = 3a^2 + tr C^2 = 1 - Pw^2
    a = (1-Pw)/3; t2 = 1 - Pw**2 - 3*a*a
    if t2 < 0: continue
    C = rng.normal(size=(3,3)); C = (C+C.T)/2; C -= np.trace(C)/3*np.eye(3); C *= math.sqrt(t2/np.trace(C@C))
    Pp = a*np.eye(3) + C
    B = (3*Pp + (Pw-1)*np.eye(3))/(1-4*Pw)
    Pw2, Pp2 = fwd(B); worst = max(worst, abs(Pw2-Pw), np.abs(Pp2-Pp).max(), abs(np.trace(B))); made += 1
print("Kasner surjectivity round trip (200 random data): max error", worst)
# tr B^2 >= 0 forces P_w >= -1/2 on the Kasner set: t2 = 1 - Pw^2 - (1-Pw)^2/3 = (2/3)(1-Pw)(1+2Pw)
print("t2 formula check:", all(abs((1-p**2-(1-p)**2/3) - (2/3)*(1-p)*(1+2*p)) < 1e-12 for p in np.linspace(-2,1,31)))
# S6-5: P(a) = a0(a0^2 - 3|v|^2) on D4
vals = set()
for a in itertools.product(range(-9, 10), repeat=4):
    if sum(a) % 2 == 0: vals.add(a[0]*(a[0]**2 - 3*(a[1]**2+a[2]**2+a[3]**2)))
gg = 0
for v in vals: gg = math.gcd(gg, v)
print("S6-5: gcd of P on D4 (|a_i|<=9):", gg, " 6 or -6 attained:", 6 in vals or -6 in vals)
G = sp.Matrix([[2,0,0,-1],[0,2,-1,0],[0,-1,2,-1],[-1,0,-1,2]])  # a Gram matrix of D4 (Cartan matrix)
print("det D4 =", G.det(), " det 6G =", (6*G).det(), " = 6^4*4 =", 6**4*4)
