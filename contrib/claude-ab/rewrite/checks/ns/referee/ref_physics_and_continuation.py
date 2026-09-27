#!/usr/bin/env python3
"""ref_physics_and_continuation.py -- referee checks (numerical, mpmath; not certified) for note 51_ section 4:

(1) monodromy test: alpha_h continued (Newton, small steps) once around circles |x| = r returns to itself for r < x*
    and to the partner root for r > x* (independent of the Arb tiling);
(2) physical numbers: k* = q* c/(2 nu), omega* = i alpha* c^2/(2 nu), the Unruh temperature of the cutoff observer,
    nu = hbar c^2/(4 pi k_B T) (eta/s = 1/(4 pi) with zero equilibrium energy density), Matsubara limits, and the
    identity (w, q) = (omega, c k)/(2 pi T), i.e. the normalisation of Grozdanov-Kovtun-Starinets-Tadic;
(3) the k^4 unit conversion of the Compere-McFadden-Skenderis-Taylor comparison (sympy);
(4) the telegraph (Maxwell-Cattaneo / MIS-type) two-pole model calibrated to D = 1/2, tau_R = 1 (the k -> 0 data of the
    exact problem), whose collision is at q^2 = 1/2, alpha = -1/2, compared with the exact (q*^2, alpha*);
(5) the Matsubara limits: zeros of I'_alpha(q) near alpha = -n as q -> 0 (Hurwitz), with alpha + n ~ c_n q^(2n).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 20
def G(al, x, N=50):
    s = mp.mpc(0); base = mp.mpc(1)
    for m in range(N):
        if m > 0:
            base = base * x / (m * (m + al))
        s += (al + 2 * m) * base
    return s
def Ga(al, x, N=50):
    s = mp.mpc(0); base = mp.mpc(1); S = mp.mpc(0)
    for m in range(N):
        if m > 0:
            inv = 1 / (m + al); base = base * x * inv / m; S += inv
        s += base * (1 - (al + 2 * m) * S)
    return s
def newton(al, x):
    for _ in range(50):
        st = G(al, x) / Ga(al, x); al -= st
        if abs(st) < mp.mpf('1e-15'):
            break
    return al
qs = mp.mpf('0.778472800990330076180356446189'); ast = mp.mpf('-0.569714080972361784438457668663')
xs = qs ** 2 / 4
print(f"x* = q*^2/4 = {mp.nstr(xs, 20)}")

# (1) monodromy (adaptive continuation: a step is accepted only if Newton from the linear predictor converges and moves
#     the root by less than 1e-3 from the prediction; otherwise the step is halved)
print("(1) monodromy of alpha_h around |x| = r (N: adaptive numerical continuation)")
def newton_c(al, x, maxit=8):
    for it in range(maxit):
        st = G(al, x) / Ga(al, x); al -= st
        if abs(st) < mp.mpf('1e-14'):
            return al, True
    return al, False
def follow(al_prev, al, path_fn, t0, t1, dt0):
    """follow the root along x = path_fn(t) from t0 to t1; al_prev, al are the roots at t0 - dt0 and t0."""
    t = t0; dt = dt0; nsteps = 0; slope = (al - al_prev) / dt0
    while t < t1:
        dt = min(dt, t1 - t)
        pred = al + slope * dt
        new, ok = newton_c(pred, path_fn(t + dt))
        if ok and abs(new - pred) < mp.mpf('1e-3'):
            slope = (new - al) / dt; al = new; t += dt; nsteps += 1; dt *= 1.3
        else:
            dt /= 2
            if dt < mp.mpf('1e-12'):
                raise RuntimeError("step too small")
    return al, nsteps
for r in [mp.mpf('0.05'), mp.mpf('0.12'), mp.mpf('0.15'), xs * (1 - mp.mpf('1e-4')), xs * (1 + mp.mpf('1e-4')), mp.mpf('0.155')]:
    th0 = mp.mpf('0.3') if r > xs else mp.mpf(0)
    # radial approach from x = 0 along the ray arg x = th0
    ray = lambda s: s * mp.expj(th0)
    s0 = mp.mpf('1e-3'); a_prev, _ = newton_c(mp.mpc(-2 * s0 * 0.5), ray(s0 / 2)); a0_, _ = newton_c(mp.mpc(-2 * s0), ray(s0))
    start, n1 = follow(a_prev, a0_, ray, s0, r, s0 / 2)
    circ = lambda th: r * mp.expj(th)
    b_prev, _ = newton_c(start, circ(th0 - mp.mpf('1e-4')))
    end_, n2 = follow(b_prev, start, circ, th0, th0 + 2 * mp.pi, mp.mpf('1e-4'))
    print(f"   r = {mp.nstr(r, 10)} ({'<' if r < xs else '>'} x*): start alpha = {mp.nstr(start, 10)}, after one turn "
          f"{mp.nstr(end_, 10)}, |jump| = {mp.nstr(abs(end_ - start), 3)}  ({n1}+{n2} steps)")
print("   expected: no jump for r < x*; a jump to the partner root for r > x* (the circle encloses the branch point x*)")

# (2) physical numbers (c = hbar = k_B = 1 unless shown)
print("(2) physical numbers")
nu, c, hbar, kB = sp.symbols('nu c hbar k_B', positive=True)
rho_c = 2 * nu / c
a_acc = c ** 2 / rho_c                 # proper acceleration of the static observer at rho = rho_c
T = hbar * a_acc / (2 * sp.pi * c * kB)  # Unruh temperature, redshift factor 1 at rho_c
print("   T_Unruh(rho_c) =", sp.simplify(T), " ;  nu expressed through T:", sp.solve(sp.Eq(T, sp.Symbol('T')), nu))
print("   => nu = hbar c^2/(4 pi k_B T), i.e. eta/s = hbar/(4 pi k_B) for a fluid with eps = 0, eps + p = s T")
print("   Matsubara: omega_n = -i n c/rho_c = -2 pi i n k_B T/hbar ;  check:", sp.simplify(-sp.I * c / rho_c + 2 * sp.pi * sp.I * kB * T / hbar) == 0)
print(f"   k* = q*/2 (c/nu) = {mp.nstr(qs / 2, 18)} ; omega* = (alpha*/2) i (c^2/nu) = {mp.nstr(ast / 2, 12)} i")
print("   GKST normalisation: w = omega rho_c/c = omega/(2 pi T), q = k rho_c = c k/(2 pi T):",
      sp.simplify(rho_c / c - hbar / (2 * sp.pi * kB * T)) == 0)
print(f"   => critical point (frak q*^2, frak w*) = ({mp.nstr(qs**2, 15)}, {mp.nstr(ast, 12)} i): real momentum, imaginary frequency")

# (3) CMST unit conversion
tau_, t_, x_, k_, w_, rc = sp.symbols('tau t x k omega r_c', positive=True)
nu_ = sp.sqrt(rc)
omega_t = -sp.I * nu_ * k_ ** 2 - sp.I * sp.Rational(3, 2) * nu_ ** 3 * k_ ** 4    # (28) with c = 1
omega_tau = sp.sqrt(rc) * omega_t                                                            # t = sqrt(r_c) tau
# plane wave v ~ exp(-i omega_tau tau + i k x):  d_tau v - r_c d_x^2 v + (3/2) r_c^2 d_x^4 v = 0 ?
lhs = -sp.I * omega_tau + rc * k_ ** 2 + sp.Rational(3, 2) * rc ** 2 * k_ ** 4
print("(3) CMST: with t = sqrt(r_c) tau and nu = sqrt(r_c), (28) is the plane-wave relation of d_tau v - r_c d^2 v = -(3/2) r_c^2 d^4 v:",
      sp.simplify(lhs) == 0)
k6 = sp.Rational(29, 192) * 64      # 29 q^6/192 with q^6 = (k rho_c)^6, rho_c = 2 nu/c
print("   k^6 coefficient of omega: (c/rho_c)(29/192) rho_c^6 =", sp.simplify((c / rho_c) * sp.Rational(29, 192) * rho_c ** 6), "(note: 29 nu^5/(6 c^4))")

# (4) telegraph model
print("(4) telegraph / MIS-type two-pole model tau_R w^2 + i w - D q^2 = 0 with D = 1/2, tau_R = 1 (from the exact k -> 0 data)")
xx = sp.symbols('x')
alpha_tel = (-1 + sp.sqrt(1 - 8 * xx)) / 2          # alpha^2 + alpha + q^2/2 = 0, q^2 = 4x, hydro branch
print("   hydro branch series:", sp.series(alpha_tel, xx, 0, 5).removeO(), " (exact: -2x - 3x^2 - 29/3 x^3 - 2843/72 x^4)")
print(f"   collision: x = 1/8 (q^2 = 1/2), alpha = -1/2 ; exact: x* = {mp.nstr(xs, 10)} (q*^2 = {mp.nstr(qs**2, 10)}), alpha* = {mp.nstr(ast, 10)}")

# (5) Matsubara limits of the non-hydrodynamic zeros
print("(5) zeros of I'_alpha(q) near alpha = -n for small q (alpha + n)/q^(2n):")
F = lambda a, q: (mp.besseli(a - 1, q) + mp.besseli(a + 1, q)) / 2
for n_ in (1, 2, 3):
    row = []
    pred = (-1) ** (n_ + 1) * n_ / (mp.factorial(n_) ** 2 * 2 ** (2 * n_))
    for q in (mp.mpf('0.2'), mp.mpf('0.1'), mp.mpf('0.05')):
        z = mp.findroot(lambda a: F(a, q), -n_ + pred * q ** (2 * n_))
        row.append(mp.nstr((z + n_) / q ** (2 * n_), 8))
    print(f"   n = {n_}: {row}   predicted limit (-1)^(n+1) n/((n!)^2 4^n) = {mp.nstr(pred, 8)}")
print("   (n = 1: alpha + 1 -> q^2/4 = x, i.e. x ~ 1 + alpha, as in track_partner.py)")
