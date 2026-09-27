# Independent check (claude-ab) of copy-newresults' Theorem A on the window [100,1000], Delta=1,
# using mpmath zeros (independent of the copy's Arb data) and an independently written right-hand side.
import mpmath as mp, math
mp.mp.dps = 25
T1, T2, D = 100.0, 1000.0, 1.0
Phi = lambda x: 0.5*mp.erfc(-x/mp.sqrt(2))
h = lambda u: Phi((u-T1)/D) - Phi((u-T2)/D)
# LHS: sum over zeros with gamma up to 1000 + 12*D
lhs = mp.mpc(0); n = 1; cnt = 0
while True:
    rho = mp.zetazero(n)
    g = rho.imag
    if g > T2 + 12*D: break
    c1 = rho*mp.zeta(rho+1)/mp.zeta(rho, derivative=1)
    lhs += c1*h(g); n += 1; cnt += 1
# RHS pieces
main = (T2-T1)/(4*mp.pi) + 1j*(T2**2-T1**2)/(4*mp.pi) - 1j*(T2-T1)
def b(n):
    r = mp.mpf(1)/n; m = n; p = 2
    while p*p <= m:
        if m % p == 0:
            r *= (1-p)
            while m % p == 0: m //= p
        p += 1
    if m > 1: r *= (1-m)
    return r
def phi(n):
    r = n; m = n; p = 2
    while p*p <= m:
        if m % p == 0:
            r -= r//p
            while m % p == 0: m //= p
        p += 1
    if m > 1: r -= r//m
    return r
PR = mp.mpc(0)
for k in range(2, 6000):
    xi = mp.log(k); gh = mp.e**(-D**2*xi**2/2)
    if gh < mp.mpf('1e-40'): break
    E0 = (mp.e**(-1j*T1*xi) - mp.e**(-1j*T2*xi))/(1j*xi)
    # int (1/2 + i u) h(u) e^{-i u xi} du, computed from Hhat = gh*E0 and i*Hhat'(xi)
    E0p = (-T1*mp.e**(-1j*T1*xi) + T2*mp.e**(-1j*T2*xi))/xi - E0/xi
    Hhat = gh*E0; Hhat_p = -D**2*xi*gh*E0 + gh*E0p
    I = 0.5*Hhat + 1j*(1j*Hhat_p)
    PR += b(k)*k**(-0.5)*I/(2*mp.pi)
LB = mp.mpc(0)
for k in range(2, 200000):
    xi = math.log(k); gh = math.exp(-D**2*xi**2/2)
    term = (phi(k)/k)*math.sqrt(k)*gh/xi
    if term < 1e-22: break
    LB += -(phi(k)/k)*mp.sqrt(k)*gh*(mp.e**(1j*T2*xi) - mp.e**(1j*T1*xi))/xi
rhs = main + PR + LB
print("zeros used:", cnt)
print("LHS =", mp.nstr(lhs, 14)); print("RHS =", mp.nstr(rhs, 14))
print("relative difference:", mp.nstr(abs(lhs-rhs)/abs(lhs), 3))
print("copy reported: 59.581503+77852.853542i")
