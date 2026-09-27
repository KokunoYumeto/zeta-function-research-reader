#!/usr/bin/env python3
"""Referee v2, script r02.  Carleman's formula after the substitution z = w^2
(Nevanlinna's formula for the angle |arg w| < pi/4), in w-coordinates:

  sum_{rho0 < r_n < R} (r_n^-2 - r_n^2 R^-4) cos(2 phi_n)
      = (2/(pi R^2)) int_{-pi/4}^{pi/4} log|f(R e^{i phi})| cos(2 phi) dphi
      + (1/pi) int_{rho0}^{R} (r^-2 - r^2 R^-4) log|f(r e^{i pi/4}) f(r e^{-i pi/4})| dr/r
      + A(R),        A(R) bounded (it converges as R grows).

Test function f(w) = sin(pi (w^2 - 1/2)) e^w (w + 2): its zeros in the closed sector are
w_m = sqrt(m + 1/2), m >= 0, on the positive axis; none on the rays.  Its growth,
log|f(r e^{i phi})| ~ pi r^2 |sin 2 phi|, is of the same Gaussian type as the reader's L(w)
(indicator v^2/(4t) there).  If A(R) converges, the weights and the factor 1/pi on the ray
term (k/(2 pi) with k = 2), which the referee's improvement of Prop 3.11 uses, are right.
"""
import mpmath as mp
mp.mp.dps = 30

def logabs_f(w):
    return mp.log(abs(mp.sin(mp.pi * (w * w - mp.mpf(1) / 2)))) + mp.re(w) + mp.log(abs(w + 2))

rho0 = mp.mpf('0.3')
rows = []
for N in (16, 36, 64, 100, 144):
    R = mp.sqrt(N)          # R^2 = N sits halfway between the zeros w^2 = m + 1/2
    zero_side = mp.fsum((1 / (m + mp.mpf(1) / 2) - (m + mp.mpf(1) / 2) / R**4) for m in range(0, N))  # all m + 1/2 < R^2
    arc = (2 / (mp.pi * R**2)) * mp.quad(lambda p: logabs_f(R * mp.expj(p)) * mp.cos(2 * p),
                                         mp.linspace(-mp.pi / 4, mp.pi / 4, 41))
    e = mp.expj(mp.pi / 4)
    ray = (1 / mp.pi) * mp.quad(lambda r: (r**-2 - r**2 / R**4) * (logabs_f(r * e) + logabs_f(r * mp.conj(e))) / r,
                                mp.linspace(rho0, R, 25))
    A = zero_side - arc - ray
    rows.append((N, zero_side, arc, ray, A))
    print(f"R^2 = {N:4d}: zero side {mp.nstr(zero_side, 12)}, arc {mp.nstr(arc, 12)}, rays {mp.nstr(ray, 12)}, remainder A(R) = {mp.nstr(A, 12)}")

diffs = [abs(rows[i + 1][4] - rows[i][4]) for i in range(len(rows) - 1)]
growth = rows[-1][1] - rows[0][1]
ok = diffs[-1] < 1e-3 and diffs[-1] < diffs[0] and growth > 2
print(("[PASS] " if ok else "[FAIL] ") + "remainder A(R) converges while the zero side grows like 2 log R "
      f"(successive differences {[mp.nstr(d, 3) for d in diffs]}, zero-side growth {mp.nstr(growth, 6)})")
print("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED")
