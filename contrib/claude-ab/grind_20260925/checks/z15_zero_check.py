# claude-ab: zeros of Z_{1/5}(s) = zeta(s,1/5) + zeta(s,4/5) with Re s > 1/2, found by a grid search on
# F(s) = (1-5^{-s}) zeta(s) + L(s, chi_5) (= 2 * 5^{-s} Z_{1/5}(s)) and re-verified here independently with the
# Hurwitz form at 30 digits (Newton refinement started from the 12-digit values).
import mpmath as mp
mp.mp.dps = 30
Z = lambda s: mp.zeta(s, mp.mpf(1)/5) + mp.zeta(s, mp.mpf(4)/5)
chi5 = [0, 1, -1, -1, 1]
F = lambda s: (1 - mp.power(5, -s))*mp.zeta(s) + mp.dirichlet(s, chi5)
found = [('0.543068840726', '15.7040482679'), ('0.709072123805', '29.9481698117'), ('0.669819888337', '43.7596602283'),
         ('0.646663732665', '61.0369079062'), ('0.668233503475', '64.8940709677'), ('0.579063331157', '75.5714257059'),
         ('0.653573724349', '79.5064291171'), ('0.556532008817', '107.216273768'), ('0.673716802912', '110.759409181'),
         ('0.633284132472', '120.652085316'), ('0.568142386919', '127.454740226'), ('0.579739424979', '134.833936498'),
         ('0.703571420088', '141.678876384')]
ok = True
for b, g in found:
    r = mp.findroot(Z, mp.mpc(b, g))
    rel = abs(Z(r))/abs(Z(r + mp.mpf('0.01')))
    agree = abs(r - mp.mpc(b, g)) < 1e-8   # inputs carry 12 significant digits
    ok &= rel < 1e-20 and agree and r.real > 0.5 and abs(F(r)) < 1e-20
    print("beta = %s  gamma = %s   |Z| = %s   (relative %s)" % (mp.nstr(r.real, 20), mp.nstr(r.imag, 20), mp.nstr(abs(Z(r)), 3), mp.nstr(rel, 3)))
# the identity Z_{1/5} = 5^s F / 2 at a test point
s0 = mp.mpc('0.61', '33.3'); ok &= abs(Z(s0) - mp.power(5, s0)*F(s0)/2) < 1e-25*abs(Z(s0))
# the reflected partner Phi_{1/5}(s) = 2 sum_k cos(2 pi k/5) k^{-s}, computed from Hurwitz values, against the closed form
Phi = lambda s: 2*mp.fsum(mp.cos(2*mp.pi*r/5)*mp.power(5, -s)*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 6))
Phi_cf = lambda s: ((mp.power(5, 1-s) - 1)*mp.zeta(s) + mp.sqrt(5)*mp.dirichlet(s, chi5))/2
s1 = mp.mpc('0.77', '21.9'); ok &= abs(Phi(s1) - Phi_cf(s1)) < 1e-25*abs(Phi(s1))
r0 = mp.findroot(Z, mp.mpc(found[0][0], found[0][1]))
print("Phi_{1/5} at the lowest zero of Z_{1/5}: |Phi| = %s (nonzero: the reflection pairs Z_{1/5} with a different function)" % mp.nstr(abs(Phi(r0)), 6))
ok &= abs(Phi(r0)) > 1e-3
print("the 13 listed zeros (not a complete count; see 08_ for the argument-principle count 24) verified, and the Phi_{1/5} checks pass:", ok)
