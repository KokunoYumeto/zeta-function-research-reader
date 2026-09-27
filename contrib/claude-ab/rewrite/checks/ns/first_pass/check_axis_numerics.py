"""Numerical margins of the analytic axis construction (reader L358-602; source App. B, pp. 144-150):
f0(z) = sum (-z/2)^a/(a!(a+1)!) = J_1(2 sqrt t)/sqrt t and f0 + z f0' = J_0(2 sqrt t), t = z/2.
The reader proves the bounds by alternating-series truncation; here they are recomputed exactly
(rationals) and compared with 50-digit Bessel values.  Also -W_* >= 2.87 and (H_*/d)' > 0.
These are floating-point confirmations of rigorous rational arguments, not interval certificates."""
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
res = []


def check(name, ok):
    ok = bool(ok)
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name)


t = sp.symbols('t', nonnegative=True)
cubic = 1 - t/2 + t**2/12 - t**3/144
check("f0 cubic truncation at t = 41/20 equals 305719/1152000 > 0.265", cubic.subs(t, sp.Rational(41, 20)) == sp.Rational(305719, 1152000) and sp.Rational(305719, 1152000) > sp.Rational(265, 1000))
check("cubic derivative -1/2 + t/6 - t^2/48 has negative discriminant (always < 0)", sp.discriminant(sp.diff(cubic, t), t) < 0)
check("tail ratio t/((n+1)(n+2)) < 1 for n >= 3, t <= 2.05 (alternating remainder >= 0)", sp.Rational(41, 20)/20 < 1)
quart = 1 - t + t**2/4 - t**3/36 + t**4/576
check("f0 + z f0' quartic truncation at t = 99/50 equals -75535511/400000000 < -0.188", quart.subs(t, sp.Rational(99, 50)) == -sp.Rational(75535511, 400000000))
dq = sp.diff(quart, t)
check("quartic derivative < 0 on [1.98, 2] (sampled exactly at 21 rational points)", all(dq.subs(t, sp.Rational(198, 100) + sp.Rational(k, 1000)) < 0 for k in range(21)))
# Bessel identities and actual values
f0 = lambda tt: (mp.besselj(1, 2*mp.sqrt(tt))/mp.sqrt(tt) if tt > 0 else mp.mpf(1))
g0 = lambda tt: mp.besselj(0, 2*mp.sqrt(tt))
ser_f0 = lambda tt: mp.nsum(lambda n: (-tt)**n/(mp.factorial(n)*mp.factorial(n + 1)), [0, mp.inf])
check("f0(z) = J_1(2 sqrt t)/sqrt t (series vs Bessel at t = 1.3)", abs(ser_f0(mp.mpf('1.3')) - f0(mp.mpf('1.3'))) < mp.mpf('1e-40'))
fmin = min(f0(mp.mpf(k)/1000*mp.mpf('2.05')) for k in range(0, 1001))
check("min of f0 on t in [0, 2.05] (1001 points) = %s >= 0.265" % mp.nstr(fmin, 12), fmin >= mp.mpf('0.265'))
check("actual f0 at t = 2.05: %s (margin above 0.265: %s)" % (mp.nstr(f0(mp.mpf('2.05')), 12), mp.nstr(f0(mp.mpf('2.05')) - mp.mpf('0.265'), 3)), f0(mp.mpf('2.05')) > mp.mpf('0.265'))
gmax = max(g0(mp.mpf('1.98') + mp.mpf(k)/10000*mp.mpf('0.02')) for k in range(0, 10001))
check("max of f0 + z f0' = J_0(2 sqrt t) on [1.98, 2] = %s <= -0.188" % mp.nstr(gmax, 12), gmax <= mp.mpf('-0.188'))
check("hence -2 z f0'/f0 >= 2 + 2(0.188)/1 = 2.376 > 2.36", 2 + 2*mp.mpf('0.188') > mp.mpf('2.36'))
h, eta, j0 = sp.symbols('h eta j_0', real=True)
D = sp.Rational(1, 2) - h
Us = 4*eta + j0
W = 1 - (1 - eta**2)*sp.diff(Us, eta) - 2*D*eta*Us
check("-W_* = 3 - 8 h eta^2 + (1 - 2h) j0 eta (exact)", sp.expand(-W - (3 - 8*h*eta**2 + (1 - 2*h)*j0*eta)) == 0)
check("-W_* >= 3 - 0.08 - 0.05 = 2.87 for h <= 0.01, j0 <= 0.05, |eta| <= 1 (corner values)",
      min((-W).subs({h: hv, j0: jv, eta: ev}) for hv in (0, sp.Rational(1, 100)) for jv in (0, sp.Rational(1, 20)) for ev in (-1, 0, 1)) >= sp.Rational(287, 100))
d = 1 - eta**2
Hs = D*eta + d*Us
check("(H_*/d)' = D(1+eta^2)/(1-eta^2)^2 + 4", sp.simplify(sp.diff(Hs/d, eta) - (D*(1 + eta**2)/(1 - eta**2)**2 + 4)) == 0)
print("\nsummary: %d checks, %d PASS, %d FAIL" % (len(res), sum(o for _, o in res), sum(not o for _, o in res)))

# heat-exterior profile as a Tricomi function: H(Z) = Z^(-1-h) U(1+h, 2, 1/Z)  (Gamma(1+h) cancels)
mp.mp.dps = 30
hh = mp.mpf(1)/137
Hq = lambda Z: mp.quad(lambda v: mp.e**(-v)*v**hh*(1 + Z*v)**(-hh), [0, 1, 10, mp.inf])/mp.gamma(1 + hh)
Ht = lambda Z: Z**(-1 - hh)*mp.hyperu(1 + hh, 2, 1/Z)
err = max(abs(Hq(Z) - Ht(Z)) for Z in (mp.mpf('0.05'), mp.mpf('0.5'), mp.mpf(2), mp.mpf(9)))
check("heat exterior H(Z) = Z^(-1-h) U(1+h, 2, 1/Z) (Tricomi; h = 1/137, 4 points), max err %s" % mp.nstr(err, 3), err < mp.mpf('1e-20'))
print("\nsummary (with Tricomi check): %d checks, %d PASS, %d FAIL" % (len(res), sum(o for _, o in res), sum(not o for _, o in res)))
