"""Negative controls: deliberately wrong variants of verified identities must FAIL.
This guards against vacuous PASSes in check_leading_field.py and check_order_n_equations.py."""
import sympy as sp

q, X = sp.symbols('q X', positive=True)
eta = sp.symbols('eta', real=True)
h = sp.symbols('h', positive=True)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
d = 1 - eta**2
L = 1 - 2*h*eta**2
r = sp.sqrt(2*q*X)
qt_, et_, Xt_ = -1/L, D*eta/(q*L), X/(q*L)
qz_, ez_, Xz_ = 2*eta*q**(1-D)/L, d/(q**D*L), -2*eta*X/(q**D*L)
Dt = lambda e: qt_*sp.diff(e, q) + et_*sp.diff(e, eta) + Xt_*sp.diff(e, X)
Dz = lambda e: qz_*sp.diff(e, q) + ez_*sp.diff(e, eta) + Xz_*sp.diff(e, X)
Dr = lambda e: (r/q)*sp.diff(e, X)
pw = lambda e: sp.simplify(sp.powsimp(sp.powdenest(sp.expand_power_base(e, force=True), force=True), force=True))

Ff = sp.Function('F')(X, eta)
M = sp.Function('M')(X, eta)
U = sp.diff(M, X)
E = sp.sqrt(2*X)*Ff
Pi = sp.Function('Pi')(X, eta)
out = []

# control 1: continuity with the wrong moment coefficient (D -> A)
V0bad = (2*eta*X*U - 2*A*eta*M - d*sp.diff(M, eta))/L
u_z = q**(-A)*U
out.append(("C1 continuity with 2A eta M instead of 2D eta M", pw(sp.diff(V0bad, X)/q + Dz(u_z)) != 0))

# control 2: A15 with the sign of the shear coefficient a flipped
V0 = (2*eta*X*U - 2*D*eta*M - d*sp.diff(M, eta))/L
u_th = q**(-A)*E
u_r = V0/r
W = 1 - (2*D*eta*M + d*sp.diff(M, eta))/X
Hc = D*eta + d*U
H = sp.sqrt(2*X)*E
l = X*sp.diff(sp.log(H), X)
Sq = -W*l - h*(1 - 2*eta*U) - Hc*sp.diff(sp.log(E), eta)
Qs = sp.Function('Qs')(X, eta)
subsQ = {sp.Derivative(Qs, X): (Sq - (1 + l)*Qs)/X}
a_sh = 1 - 2*X*sp.diff(sp.log(E), X)
mat = lambda e: Dt(e) + u_r*Dr(e) + u_z*Dz(e)
R0th = mat(u_th) + u_r*u_th/r - (Dr(Dr(u_th)) + Dr(u_th)/r - u_th/r**2)
T0bad = Ff*(X*Qs/L + a_sh)
lhs = R0th + (Dr(q**(-A-sp.Rational(1, 2))*T0bad) + 2/r*q**(-A-sp.Rational(1, 2))*T0bad)
out.append(("C2 R0_theta identity with s_shear = (-a, .) instead of (a, .)", pw(sp.expand(lhs).subs(subsQ)) != 0))

# control 3: the q-derivative map with D and A swapped
f = sp.Function('f')(X, eta)
b = sp.symbols('b')
Zbad = (2*b*eta*f + d*sp.diff(f, eta) - 2*eta*X*sp.diff(f, X))/L
out.append(("C3 d_z(q^b f) with q^(b-A) instead of q^(b-D)", pw(Dz(q**b*f) - q**(b-A)*Zbad) != 0))

# control 4: Kasner inverse with a wrong factor
x, y = sp.symbols('x y', real=True)
strain = [x, y, -x-y]
chi = sp.sqrt(1 + sp.Rational(4, 3)*sum(v*v for v in strain))
pw_ = sp.Rational(1, 4) - sp.Rational(3, 4)/chi
pt = [sp.Rational(1, 4) + (sp.Rational(1, 4) + v)/chi for v in strain]
out.append(("C4 Kasner inverse with 2P instead of 3P", sp.simplify((2*pt[0] + pw_ - 1)/(1 - 4*pw_) - x) != 0))

for name, ok in out:
    print(("PASS" if ok else "FAIL") + "  (wrong variant correctly rejected) " + name)
print("summary: %d controls, %d correctly rejected" % (len(out), sum(o for _, o in out)))
