# claude-ab checks of the character-lifting core (MCL5-MCL9, ORE4-ORE5) at actual zeros.
# m = 1: D = zeta at its first zero rho_1.  m = 2: D = zeta^2 at rho_1 (tests every m-dependent sign/factorial),
# with functional-equation multiplier chi_D = chi_zeta^2.
import mpmath as mp
from math import comb, factorial
mp.mp.dps = 40
N = 7                       # Taylor order kept
ok = True
def taylor(f, z0, n):       # coefficients c_k of f(z0+t) = sum c_k t^k
    return mp.taylor(f, z0, n)
def ser_mul(a, b, n):
    return [mp.fsum(a[i]*b[k-i] for i in range(k+1)) for k in range(n+1)]
def ser_inv(a, n):
    r = [1/a[0]]
    for k in range(1, n+1):
        r.append(-mp.fsum(a[i]*r[k-i] for i in range(1, k+1))/a[0])
    return r
chi_z = lambda s: mp.pi**(s-mp.mpf(1)/2)*mp.gamma((1-s)/2)/mp.gamma(s/2)   # zeta(s) = chi(s) zeta(1-s)  (ORE5.3)
rho = mp.zetazero(1)
# sanity: ORE5.3 at a generic point
s0 = mp.mpc('0.3', '7.7'); ok &= abs(mp.zeta(s0) - chi_z(s0)*mp.zeta(1-s0)) < mp.mpf(10)**-30
for m in (1, 2):
    D   = (lambda s: mp.zeta(s)) if m == 1 else (lambda s: mp.zeta(s)**2)
    chi = (lambda s: chi_z(s))   if m == 1 else (lambda s: chi_z(s)**2)
    b = 1 - rho
    cr = taylor(D, rho, N+m); cb = taylor(D, b, N+m)
    # exact multiplicity m at rho and at b
    ok &= all(abs(cr[k]) < mp.mpf(10)**-25 for k in range(m)) and abs(cr[m]) > mp.mpf(10)**-5
    ok &= all(abs(cb[k]) < mp.mpf(10)**-25 for k in range(m)) and abs(cb[m]) > mp.mpf(10)**-5
    u_r = cr[m:m+N+1]; u_b = cb[m:m+N+1]                       # u(t) = D(.+t)/t^m   (ORE4.4)
    # (ORE5.4) u_b(t) = (-1)^m chi(b+t) u_rho(-t)
    ch = taylor(chi, b, N)
    u_r_neg = [u_r[k]*(-1)**k for k in range(N+1)]
    rhs = [(-1)**m*c for c in ser_mul(ch, u_r_neg, N)]
    d54 = max(abs(u_b[k]-rhs[k]) for k in range(N+1))
    # v_k from 1/(2 u_rho)  (ORE4.4-4.5) and the recursion (ORE4.5)
    v = [x/2 for x in ser_inv(u_r, N)]
    v_rec = [mp.mpf(factorial(m))/(2*cr[m]*factorial(m))]      # v_0 = m!/(2 zeta^(m)(rho)) with zeta^(m)/m! = cr[m]
    for k in range(1, N+1):
        v_rec.append(-mp.fsum(u_r[l]*v_rec[k-l] for l in range(1, k+1))/u_r[0])
    drec = max(abs(v[k]-v_rec[k]) for k in range(N+1))
    # (ORE5.5)-(ORE5.6) key germ identity: u_b(t) * sum v_k (-t)^k = (-1)^m chi(b+t)/2
    v_neg = [v[k]*(-1)**k for k in range(N+1)]
    lhs = ser_mul(u_b, v_neg, N); tgt = [(-1)**m*c/2 for c in ch]
    d56 = max(abs(lhs[k]-tgt[k]) for k in range(N+1))
    # MCL5.7 lift in the basis A_n (raw derivatives): Lambda_j = j! sum_k v^{(j-k)}(0)/((j-k)!(m+k)!) A_{m+k},
    # v^{(i)}(0) = i! v_i.  Check Sigma' Lambda_j = S_j using MCL5.1: Sigma' A_n = 2 sum_k C(n,k) D^{(n-k)}(rho) S_k.
    Dder = [cr[k]*factorial(k) for k in range(N+m+1)]          # D^{(k)}(rho)
    def SigmaA(n):                                             # vector over S_0..S_n
        return {k: 2*comb(n, k)*Dder[n-k] for k in range(n+1)}
    d57 = 0
    for j in range(0, 4):
        Lam = {m+k: factorial(j)*(factorial(j-k)*v[j-k])/(factorial(j-k)*factorial(m+k)) for k in range(j+1)}
        img = {}
        for n, c in Lam.items():
            for k, w in SigmaA(n).items():
                img[k] = img.get(k, 0) + c*w
        for k in range(0, m+4):
            want = 1 if k == j else 0
            d57 = max(d57, abs(img.get(k, 0) - want))
    # MCL6.4: (T_a^t - a^rho)^{m+j} Lambda_j = a^{(m+j) rho} j! m!/(2 D^{(m)}(rho)) (log a)^{m+j} A_0, and the next power kills it
    d64 = 0
    for a in (2, 3):
        la = mp.log(a); ar = mp.mpf(a)**rho
        def T(vec):                                            # T_a^t A_n = a^rho sum_k C(n,k) (log a)^{n-k} A_k
            out = {}
            for n, c in vec.items():
                for k in range(n+1):
                    out[k] = out.get(k, 0) + c*ar*comb(n, k)*la**(n-k)
            return out
        for j in range(0, 3):
            Lam = {m+k: factorial(j)*(factorial(j-k)*v[j-k])/(factorial(j-k)*factorial(m+k)) for k in range(j+1)}
            w = dict(Lam)
            for _ in range(m+j):
                Tw = T(w); w = {k: Tw.get(k, 0) - ar*w.get(k, 0) for k in set(Tw) | set(w)}
            pred = ar**(m+j)*factorial(j)*factorial(m)/(2*Dder[m])*la**(m+j)
            d64 = max(d64, abs(w.get(0, 0)-pred), max([abs(c) for k, c in w.items() if k != 0] + [0]))
            Tw = T(w); w2 = {k: Tw.get(k, 0) - ar*w.get(k, 0) for k in set(Tw) | set(w)}
            d64 = max(d64, max(abs(c) for c in w2.values()))
    # MCL9.6 / ORE4.9: top coefficient of the connecting representative N^r Lambda_{r-1}, N A_n = n A_{n-1}
    d96 = 0
    for r in range(1, 4):
        j = r-1
        Lam = {m+k: factorial(j)*(factorial(j-k)*v[j-k])/(factorial(j-k)*factorial(m+k)) for k in range(j+1)}
        w = dict(Lam)
        for _ in range(r):
            w = {n-1: n*c for n, c in w.items() if n >= 1}
        pred = factorial(j)*m/(2*Dder[m])
        d96 = max(d96, abs(w.get(m-1, 0)-pred))
        ok &= all(n <= m-1 for n in w)                         # representative lies in the kernel span A_0..A_{m-1}
    print("m=%d: ORE5.4 dev %s | v-recursion dev %s | ORE5.6 germ dev %s | MCL5.4 lift dev %s | MCL6.4 dev %s | MCL9.6 dev %s"
          % (m, mp.nstr(d54,3), mp.nstr(drec,3), mp.nstr(d56,3), mp.nstr(d57,3), mp.nstr(d64,3), mp.nstr(d96,3)))
    ok &= max(d54, drec, d56, d57, d64, d96) < mp.mpf(10)**-20
print("ALL PASS" if ok else "FAIL")
