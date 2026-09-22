# Numerical spot-checks of ChatGPT Pro's A2 formulas (25), (29), (21)-(22) for the control density.
import mpmath as mp
mp.mp.dps = 30
g1 = mp.im(mp.zetazero(1)); g2 = mp.im(mp.zetazero(2))
G14 = mp.gamma(mp.mpf(1)/4)
ok = True
# (25): |Gamma(1/4+it/2)|^2 <= Gamma(1/4)^2 (1+t^2)^(-1/4) / cosh(pi t/2) <= 2 Gamma(1/4)^2 (1+t^2)^(-1/4) e^{-pi|t|/2}
for t in [0, 0.3, 1, 2, 5, 14.1, 30, 80, 150]:
    t = mp.mpf(t)
    lhs = abs(mp.gamma(mp.mpf(1)/4 + 1j*t/2))**2
    mid = G14**2*(1+t**2)**(-mp.mpf(1)/4)/mp.cosh(mp.pi*t/2)
    rhs = 2*G14**2*(1+t**2)**(-mp.mpf(1)/4)*mp.e**(-mp.pi*abs(t)/2)
    ok &= (lhs <= mid*(1+mp.mpf('1e-25'))) and (mid <= rhs*(1+mp.mpf('1e-25')))
    print('(25) t=%-6s lhs/mid=%s mid/rhs=%s' % (mp.nstr(t,4), mp.nstr(lhs/mid,8), mp.nstr(mid/rhs,8)))
# (29): |zeta(1/2+it)|^2 <= 4 (t^2+1/4)/(sqrt2-1)^2
for t in [0, 1, 5, 14.134725, 20, 50, 100, 300]:
    t = mp.mpf(t)
    lhs = abs(mp.zeta(mp.mpf(1)/2 + 1j*t))**2
    rhs = 4*(t**2+mp.mpf(1)/4)/(mp.sqrt(2)-1)**2
    ok &= lhs <= rhs
    print('(29) t=%-8s ratio=%s' % (mp.nstr(t,6), mp.nstr(lhs/rhs,6)))
# (21) and (22): control density and its value at t = gamma_1 (continuous extension)
def xi2(s):  # 2 xi(s)
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def w_def(t):  # |2xi/Q1|^2/(2pi) directly
    s = mp.mpf(1)/2 + 1j*t
    Q1 = ((s-mp.mpf(1)/2)**2 + g1**2)*((s-mp.mpf(1)/2)**2 + g2**2)
    return abs(xi2(s)/Q1)**2/(2*mp.pi)
def w21(t):
    return (t**2+mp.mpf(1)/4)**2*abs(mp.gamma(mp.mpf(1)/4+1j*t/2))**2*abs(mp.zeta(mp.mpf(1)/2+1j*t))**2/(2*mp.pi**1.5*(t**2-g1**2)**2*(t**2-g2**2)**2)
for t in [0.5, 3, 10, 25, 40]:
    t = mp.mpf(t); r = w21(t)/w_def(t); ok &= abs(r-1) < mp.mpf('1e-20')
    print('(21) t=%-5s w21/wdef=%s' % (mp.nstr(t,3), mp.nstr(r,25)))
zp = mp.diff(lambda s: mp.zeta(s), mp.mpf(1)/2 + 1j*g1)
w22 = (g1**2+mp.mpf(1)/4)**2*abs(mp.gamma(mp.mpf(1)/4+1j*g1/2))**2*abs(zp)**2/(8*mp.pi**1.5*g1**2*(g2**2-g1**2)**2)
eps = mp.mpf('1e-12')
wnear = w_def(g1+eps)
print('(22) formula =', mp.nstr(w22,15), ' limit value =', mp.nstr(wnear,15), ' rel diff =', mp.nstr(abs(w22/wnear-1),3))
ok &= abs(w22/wnear-1) < mp.mpf('1e-9')
print('ALL CHECKS PASS' if ok else 'SOME CHECK FAILED')
