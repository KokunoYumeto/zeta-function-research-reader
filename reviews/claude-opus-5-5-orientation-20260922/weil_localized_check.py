# Numerical calibration of the localized Weil identity on an ACTUAL on-line zero pair.
# Conventions: repo satellites/22_rh_counterexample_routes.tex eq:rh-weil-convention and eq:rh-full-weil-test.
#   f^(z)=∫ f(u) e^{-iuz} du ; W(f,f)=Σ_ρ m_ρ conj(f^(conj γ_ρ)) f^(γ_ρ),  γ_ρ=(ρ-1/2)/i
#   W(f,f)= ĥ(i/2)+ĥ(-i/2) + ∫ ĥ(t)[Re ψ(1/4+it/2)/(2π) - log π/(2π)] dt - Σ_{n≥2} Λ(n)/√n (h(log n)+h(-log n)),
#   ĥ(z)=f^(z) conj(f^(conj z)), h(u)=(1/2π)∫ ĥ(t) e^{itu} dt.
# Test function: f^(z) = 2ξ(1/2+iz)/(γ1^2 - z^2), i.e. v_h(1/2+iz) with h(s)=(s-1/2)^2+γ1^2 (m=1).
import mpmath as mp
mp.mp.dps = 30
g1 = mp.im(mp.zetazero(1))
def xi(s):
    if abs(s) < mp.mpf('1e-25') or abs(s-1) < mp.mpf('1e-25'):
        return mp.mpf(1)/2   # xi(0)=xi(1)=1/2
    return s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
def fhat(z):
    s = mp.mpf(1)/2 + 1j*z
    return 2*xi(s)/(g1**2 - z**2)
# value at the zero (removable singularity): derivative quotient
def fhat_at(z0):
    d = mp.diff(lambda z: 2*xi(mp.mpf(1)/2+1j*z), z0)
    return d/(-2*z0)
F1 = fhat_at(g1)
zero_side = 2*mp.re(F1*mp.conj(F1))   # ρ=1/2±iγ1; ĥ(γ)=f^(γ)conj f^(γ)=|f^|^2 since γ real
# check that fhat is real on the real axis (it should be: ξ(1/2+it) real)
print('F1 =', F1)
pole = fhat(0.5j)*mp.conj(fhat(mp.conj(0.5j))) + fhat(-0.5j)*mp.conj(fhat(mp.conj(-0.5j)))
def hhat(t):  # real t
    if abs(t-g1) < mp.mpf('1e-8') or abs(t+g1) < mp.mpf('1e-8'):
        return abs(F1)**2
    v = fhat(t); return mp.re(v*mp.conj(v))
Gw = lambda t: (mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2)) - mp.log(mp.pi))/(2*mp.pi)
T = 140
nodes = [mp.mpf(x) for x in range(0, T+1, 2)]
def evenint(fun):
    return 2*mp.quad(fun, nodes)
gamma_term = evenint(lambda t: hhat(t)*Gw(t))
def h(u):
    return evenint(lambda t: hhat(t)*mp.cos(t*u))/(2*mp.pi)
def vonmangoldt(n):
    for p in range(2, n+1):
        if n % p == 0:
            k = n
            while k % p == 0: k //= p
            return mp.log(p) if k == 1 else 0
    return 0
prime_terms = []
total_prime = mp.mpf(0)
for n in range(2, 60):
    L = vonmangoldt(n)
    if L == 0: continue
    hv = h(mp.log(n))
    term = L/mp.sqrt(n)*2*hv
    total_prime += term
    prime_terms.append((n, mp.nstr(term, 8)))
print('prime terms (n, Λ(n)/√n·2h(log n)):', prime_terms[:12])
explicit_side = pole + gamma_term - total_prime
print('zero side   =', mp.nstr(zero_side, 20))
print('pole        =', mp.nstr(mp.re(pole), 20))
print('gamma term  =', mp.nstr(gamma_term, 20))
print('prime total =', mp.nstr(total_prime, 20))
print('explicit    =', mp.nstr(mp.re(explicit_side), 20))
print('difference  =', mp.nstr(mp.re(explicit_side) - zero_side, 5))
