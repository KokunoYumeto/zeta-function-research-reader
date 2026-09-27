# claude-ab checks of HSW5.2, HSW6A.4/HSW6B.6 and OPD4.2/OPD5.2 (25 September continuation, counterfactual lane).
# The identities are tested on an explicit synthetic Mellin function with an artificial off-critical pair, because
# HSW6B/OPD4 are statements about any b_0 in A whose Mellin transform vanishes at rho (zeta enters only through G).
import mpmath as mp
mp.mp.dps = 25
ok = True
# (1) HSW5.2: int_0^oo h0(v) v^s dv/v = (s-1) e^{s^2} / 2 for h0(v) = (log v - 2)/(8 sqrt pi) exp(-(log v)^2/4)
for s in (mp.mpf('0.3'), mp.mpc('0.5', '2.0'), mp.mpc('1.7', '-0.4')):
    val = mp.quad(lambda x: (x-2)/(8*mp.sqrt(mp.pi))*mp.exp(-x**2/4 + s*x), [-mp.inf, 0, mp.inf])
    ok &= abs(val - (s-1)*mp.exp(s**2)/2) < 1e-18
print("HSW5.2 Mellin transform of h0 checked at three points:", ok)
# (2) synthetic: phi_g(x) = exp(-x^2/4)/(2 sqrt pi) has Mellin (in x = log u) int phi_g(x) e^{s x} dx = e^{s^2};
#     L = -u d/du = -d/dx acts as multiplication by s.  Off-critical pair rho = 1/2+d+i g, rho_flat = 1/2-d+i g.
d, g = mp.mpf('0.3'), mp.mpf('5')
rho, rhof = mp.mpc(0.5+d, g), mp.mpc(0.5-d, g)
phi   = lambda x: mp.exp(-x**2/4)/(2*mp.sqrt(mp.pi))
dphi  = lambda x: -x/2*phi(x)
ddphi = lambda x: (x**2/4 - mp.mpf(1)/2)*phi(x)
Lop = lambda f, df: (lambda x: -df(x))
# b_rho = (L - rho_flat) phi ; b_rhof = (L - rho) phi ; b0 = (L - rho)(L - rho_flat) phi = L^2 phi - (rho+rhof) L phi + rho rhof phi
b_rho  = lambda x: -dphi(x) - rhof*phi(x)
b_rhof = lambda x: -dphi(x) - rho*phi(x)
b0     = lambda x: ddphi(x) + (rho+rhof)*dphi(x) + rho*rhof*phi(x)
ip = lambda f, h: mp.quad(lambda x: mp.conj(f(x))*h(x)*mp.exp(x), [-mp.inf, 0, mp.inf])   # <f,h> in L^2(du), u = e^x
n_rho, n_rhof = ip(b_rho, b_rho).real, ip(b_rhof, b_rhof).real
# OPD4.2: (Re rho - 1/2) ||b_rho||^2 = -Re <b_rho, b0>
lhs, rhs = (rho.real-0.5)*n_rho, -ip(b_rho, b0).real
print("OPD4.2: (beta-1/2)||b_rho||^2 = %s, -Re<b_rho,b0> = %s" % (mp.nstr(lhs, 15), mp.nstr(rhs, 15))); ok &= abs(lhs-rhs) < 1e-15
# OPD5.2: equal norms, opposite real pairings for the reflected partner
ok &= abs(n_rho - n_rhof) < 1e-15 and abs(ip(b_rhof, b0).real + ip(b_rho, b0).real) < 1e-15
print("OPD5.2: ||b_rho||^2 = %s = ||b_rhof||^2 = %s" % (mp.nstr(n_rho, 15), mp.nstr(n_rhof, 15)))
# HSW6A.4 + HSW6B.6: the Poisson-swept value int |G(1/2+it)|^2 P_d(t-g) dt equals 2 d ||b_rho||^2, where G = (s-rho)(s-rhof) e^{s^2}
G = lambda s: (s-rho)*(s-rhof)*mp.exp(s**2)
H = mp.quad(lambda t: abs(G(mp.mpc(0.5, t)))**2 * d/(mp.pi*((t-g)**2 + d**2)), [-mp.inf, g-5, g, g+5, mp.inf])
print("HSW6B.6: harmonic value = %s, 2 delta ||b_rho||^2 = %s" % (mp.nstr(H, 15), mp.nstr(2*d*n_rho, 15))); ok &= abs(H - 2*d*n_rho) < 1e-12
print("ALL PASS" if ok else "FAIL")
