# Numerical checks for PRIME_ZERO_AND_WEIL_POSITIVITY.md (mpmath, 30 digits).
# (1) Riemann's theta derivation: the n = 0 lattice term (the prime 0) contributes exactly
#     1/(s-1) - 1/s to Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s); the n != 0 terms give an entire integral.
# (2) Soule's limit for a point with counting function N(q) = 1: lim_{q->1} (q-1)/(1-q^{-s}) = 1/s.
# (3) Exact factorisation Lambda(s) = (1/s) * 2 pi^{-s/2} Gamma(1+s/2) * zeta(s).
# (4) Control completion: the pole residues of Lambda*Q0/Q1 are those of Lambda times c = Q0(0)/Q1(0) > 0.
# (5) The pole plane W_0(f) = 2 Re(a conj b), a = fhat(i/2), b = fhat(-i/2), is indefinite (signature (1,1)).
import mpmath as mp
mp.mp.dps = 30
ok = True

def Lam(s):
    return mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)

def psi(x):  # sum_{n>=1} exp(-pi n^2 x)
    return mp.nsum(lambda n: mp.e**(-mp.pi*n*n*x), [1, mp.inf])

print('(1) zero-term decomposition of Lambda(s)')
for s in [mp.mpf('2.5'), mp.mpc('0.3', '4.0'), mp.mpc('-1.7', '0.9')]:
    integral = mp.quad(lambda x: psi(x)*(x**(s/2) + x**((1-s)/2))/x, [1, 2, 5, mp.inf])
    zero_term = 1/(s-1) - 1/s
    lhs = Lam(s)
    err = abs(lhs - (integral + zero_term))
    ok &= err < mp.mpf('1e-20')
    print('   s=%s  Lambda=%s  entire part=%s  zero term=%s  |diff|=%s' % (
        mp.nstr(s, 5), mp.nstr(lhs, 15), mp.nstr(integral, 15), mp.nstr(zero_term, 15), mp.nstr(err, 3)))

print('(2) Soule limit for N(q)=1')
for s in [mp.mpf('0.7'), mp.mpf('2'), mp.mpf('5.5')]:
    q = 1 + mp.mpf('1e-15')
    val = (q-1)/(1 - q**(-s))
    ok &= abs(val - 1/s) < mp.mpf('1e-13')
    print('   s=%s  (q-1)/(1-q^-s) at q=1+1e-15: %s   1/s=%s' % (mp.nstr(s, 3), mp.nstr(val, 16), mp.nstr(1/s, 16)))

print('(3) Lambda(s) = (1/s) * 2 pi^{-s/2} Gamma(1+s/2) zeta(s)')
for s in [mp.mpf('0.37'), mp.mpc('0.5', '14.134725'), mp.mpc('-2.2', '1.3')]:
    rhs = (1/s) * 2 * mp.pi**(-s/2) * mp.gamma(1 + s/2) * mp.zeta(s)
    err = abs(Lam(s) - rhs)
    ok &= err < mp.mpf('1e-25') * max(1, abs(rhs))
    print('   s=%s  |diff|=%s' % (mp.nstr(s, 6), mp.nstr(err, 3)))

print('(4) control completion: residue factor c = Q0(0)/Q1(0)')
g1 = mp.im(mp.zetazero(1)); g2 = mp.im(mp.zetazero(2))
for d0, G0 in [(mp.mpf('0.25'), mp.mpf('1000')), (mp.mpf('0.01'), mp.mpf('50'))]:
    a = d0 + 1j*G0
    Q0 = lambda s: ((s-mp.mpf(1)/2)**2 - a**2)*((s-mp.mpf(1)/2)**2 - mp.conj(a)**2)
    Q1 = lambda s: ((s-mp.mpf(1)/2)**2 + g1**2)*((s-mp.mpf(1)/2)**2 + g2**2)
    c0 = Q0(mp.mpf(0))/Q1(mp.mpf(0)); c1 = Q0(mp.mpf(1))/Q1(mp.mpf(1))
    eps = mp.mpf('1e-12')
    res0 = eps*Lam(eps)*Q0(eps)/Q1(eps)             # residue at s=0 of Lambda*Q0/Q1 (approx.)
    res1 = eps*Lam(1+eps)*Q0(1+eps)/Q1(1+eps)       # residue at s=1
    ok &= (mp.im(c0) == 0 or abs(mp.im(c0)) < mp.mpf('1e-25')) and mp.re(c0) > 0 and abs(c0 - c1) < mp.mpf('1e-20')
    print('   delta0=%s gamma0=%s  c=Q0(0)/Q1(0)=%s  (c at s=1: %s)  res0=%s  res1=%s' % (
        mp.nstr(d0, 3), mp.nstr(G0, 5), mp.nstr(mp.re(c0), 12), mp.nstr(mp.re(c1), 12),
        mp.nstr(mp.re(res0), 10), mp.nstr(mp.re(res1), 10)))

print('(5) the pole plane is indefinite')
# f = bump centred at u0: fhat(i/2) = int f e^{u/2}, fhat(-i/2) = int f e^{-u/2}
def bump(u, u0, w):
    t = (u-u0)/w
    return mp.e**(-1/(1-t*t)) if abs(t) < 1 else mp.mpf(0)
def ab(coeffs):
    fa = lambda u: sum(c*bump(u, u0, mp.mpf('0.5')) for c, u0 in coeffs)
    a = mp.quad(lambda u: fa(u)*mp.e**(u/2), [-4, -2, 0, 2, 4])
    b = mp.quad(lambda u: fa(u)*mp.e**(-u/2), [-4, -2, 0, 2, 4])
    return a, b
for coeffs in [[(1, mp.mpf(-2)), (1, mp.mpf(2))], [(1, mp.mpf(-2)), (-1, mp.mpf(2))]]:
    a, b = ab(coeffs)
    W0 = 2*mp.re(a*mp.conj(b))
    print('   f = %s : a=%s b=%s  W_0 = 2Re(a conj b) = %s' % (
        coeffs, mp.nstr(a, 8), mp.nstr(b, 8), mp.nstr(W0, 8)))
a1, b1 = ab([(1, mp.mpf(-2)), (1, mp.mpf(2))]); a2, b2 = ab([(1, mp.mpf(-2)), (-1, mp.mpf(2))])
ok &= (2*mp.re(a1*mp.conj(b1)) > 0) and (2*mp.re(a2*mp.conj(b2)) < 0)
print('ALL CHECKS PASS' if ok else 'SOME CHECK FAILED')
