#!/usr/bin/env python3
"""Checks for the finding on reader Prop 3.11 (Nyman-Beurling in B) and open question 5.

For Lambda in B' annihilating g_t(s)(n - n^{1-s})/s (n in S), L(w) = Lambda(K_w),
K_w(s) = g_t(s)(e^w - e^{(1-s)w})/s, is entire, vanishes at 0 and at log n (n in S), and
   log|L(u+iv)| <= v^2/(4t) + alpha(|u|+|v|) + M log(2+|w|) + C          (*)
where ONLY alpha, M, C depend on Lambda: the quadratic coefficient 1/(4t) comes from
sup_tau exp(-t tau^2 + tau v) = exp(v^2/(4t)) and is the same for every Lambda.
Jensen at 0 then bounds int_0^R n(x)/x dx <= R^2/(8t) + O(R); Carleman's formula for the right
half-plane bounds sum (1/r - r/R^2) cos(theta) <= R/(3 pi t) + O(log R).
For S = {2^a 3^b}: nu(x) ~ x^2/(2 log2 log3), so L == 0 (hence Lambda = 0) once
   Jensen:   t > log2*log3/2      ~ 0.3808
   Carleman: t > log2*log3/(2 pi) ~ 0.1212
"""
import mpmath as mp, numpy as np
mp.mp.dps = 30
ok = True

# (a) Carleman's formula (Titchmarsh, Theory of Functions 3.7) checked numerically on
#     f(z) = sin(pi z) * exp(c z^2) * (z + 3)   (zeros in Re z > 0: the positive integers)
c = mp.mpf('0.37'); rho = mp.mpf('0.5')
f = lambda z: mp.sin(mp.pi*z)*mp.exp(c*z*z)*(z + 3)
logabs = lambda z: mp.log(abs(f(z)))
diffs = []
for R in [mp.mpf('10.5'), mp.mpf('20.5'), mp.mpf('40.5'), mp.mpf('80.5')]:
    lhs = mp.fsum((1/mp.mpf(k) - mp.mpf(k)/R**2) for k in range(1, int(R) + 1))
    I1 = mp.quad(lambda th: logabs(R*mp.expj(th))*mp.cos(th), mp.linspace(-mp.pi/2, mp.pi/2, 41))/(mp.pi*R)
    I2 = mp.quad(lambda y: (1/y**2 - 1/R**2)*(logabs(1j*y) + logabs(-1j*y)), [rho, 1, 2, 5, 10, 20, 40, 80, R][:([rho, 1, 2, 5, 10, 20, 40, 80, R].index(R) + 1) if R in [80] else None])/(2*mp.pi) if False else mp.quad(lambda y: (1/y**2 - 1/R**2)*(logabs(1j*y) + logabs(-1j*y)), [rho] + [x for x in [1, 2, 5, 10, 20, 40] if x < R] + [R])/(2*mp.pi)
    D = lhs - I1 - I2
    diffs.append(D)
    print(f"(a) R={mp.nstr(R,4):>5}: zero sum = {mp.nstr(lhs,10):>12}   (1/piR)int = {mp.nstr(I1,10):>12}   (1/2pi)int = {mp.nstr(I2,10):>12}   remainder A(R) = {mp.nstr(D,10)}")
ok &= abs(diffs[-1] - diffs[-2]) < 1e-3 and abs(diffs[-2] - diffs[-3]) < 5e-3
print("    remainder A_rho(f,R) converges as R grows (Carleman: bounded inner boundary term) ->", ok)
print("    (the Gaussian factor exp(c z^2) contributes +2cR/(3pi) and -2cR/(3pi) to the two integrals: they cancel)")

# (b) the growth (*) for a concrete continuous functional that is spread along the imaginary axis:
#     Lambda(F) = sum_{|k|<=K} F(i k)/(1+k^2)   (|Lambda(F)| <= pi*coth(pi) b_{0,0}(F))
t = mp.mpf('0.2'); K = 200
def Kw(s, w):
    if abs(s) < mp.mpf('1e-20'):
        return mp.exp(t*s*s)*w*mp.exp(w)          # limit s -> 0 of (e^w - e^{(1-s)w})/s = w e^w
    return mp.exp(t*s*s)*(mp.exp(w) - mp.exp((1 - s)*w))/s
L = lambda w: mp.fsum(Kw(1j*k, w)/(1 + k*k) for k in range(-K, K + 1))
print("(b) log|L(iv)| against v^2/(4t) (t = 0.2) for Lambda = sum F(ik)/(1+k^2):")
for v in [10, 20, 30, 40]:
    val = mp.log(abs(L(1j*v)))
    print(f"    v={v:3d}: log|L(iv)| = {mp.nstr(val,8):>12}   v^2/(4t) = {mp.nstr(v*v/(4*t),8):>10}   difference = {mp.nstr(val - v*v/(4*t),6)}")
    ok &= val <= v*v/(4*t) + 10*mp.log(2 + v)
print("    log|L(u)| on the real axis is only linear in u:")
for u in [10, 20, 40]:
    print(f"    u={u:3d}: log|L(u)| = {mp.nstr(mp.log(abs(L(u))),8)}")

# (c) the lattice S = {2^a 3^b}: counting nu(x) and Carleman's sum
l2, l3 = np.log(2.0), np.log(3.0)
kappa = 1/(2*l2*l3)
def nu(x):
    return sum(int(np.floor((x - a*l2)/l3)) + 1 for a in range(int(x/l2) + 1)) - 1
for x in [50, 200, 800]:
    print(f"(c) nu({x}) = {nu(x)},  kappa x^2 = {kappa*x*x:.1f},  ratio {nu(x)/(kappa*x*x):.4f}")
R = 400.0
pts = np.array([a*l2 + b*l3 for a in range(int(R/l2) + 1) for b in range(int(R/l3) + 1) if 0 < a*l2 + b*l3 < R])
carl = np.sum(1/pts - pts/R**2)
print(f"    Carleman sum at R={R}: {carl:.3f};  (4/3) kappa R = {4*kappa*R/3:.3f}")
ok &= abs(carl/(4*kappa*R/3) - 1) < 0.03   # O(log R / R) correction; ratio 1.060, 1.020, 1.006 at R = 100, 400, 1600
tJ = l2*l3/2; tC = l2*l3/(2*np.pi)
print(f"(d) thresholds for S = {{2^a3^b}}: Jensen t > log2 log3/2 = {tJ:.5f};  Carleman t > log2 log3/(2 pi) = {tC:.5f}")

# (e) the final step g_t B dense in B: h_N = e^{t s^2} P_N(-t s^2) -> 1 locally uniformly, |h_N| <= e^{2 t sigma^2}
t = mp.mpf('0.3')
F = lambda s: mp.exp(mp.mpf('0.05')*s*s)                      # an element of B
def hN(s, Nn):
    z = -t*s*s
    return mp.exp(t*s*s)*mp.fsum(z**j/mp.factorial(j) for j in range(Nn + 1))
print("(e) sup over |sigma|<=1, |tau|<=60 of (1+|tau|)^2 |F h_N - F| and max |h_N| e^{-2t sigma^2}:")
for Nn in [10, 40, 120]:
    sup = 0; supb = 0
    for sig in [-1, 0, 1]:
        for tau in np.linspace(-60, 60, 241):
            s = mp.mpc(sig, tau)
            h = hN(s, Nn)
            sup = max(sup, (1 + abs(tau))**2*abs(F(s)*h - F(s)))
            supb = max(supb, abs(h)*mp.exp(-2*t*sig*sig))
    print(f"    N={Nn:4d}: {mp.nstr(sup,4):>10}   {mp.nstr(supb,6)}")
    ok &= (supb - 1) <= mp.mpf("1e-20")
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
