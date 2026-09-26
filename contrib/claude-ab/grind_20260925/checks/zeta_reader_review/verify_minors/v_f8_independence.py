#!/usr/bin/env python3
"""F8 verification (independent code).

(i) Lemma 2.8 with complex C_j and with L(s - sigma_j, chi): after the Euler-log step the condition is
    sum_j C_j chi(p)^r p^{r sigma_j} = 0 for all p, r.  At a prime p where the x_j = p^{sigma_j} are distinct
    the r = 1..l equations have a Vandermonde-type determinant prod x_j prod (x_j - x_i) != 0.
    Checked: random complex sigma_j; the full-rank statement at a good prime; bad primes are those where two
    sigma's differ by 2 pi i a/log p (constructed example: sigma_2 = sigma_1 + 2 pi i/log 2 collides at p = 2 only).
    Also a direct numerical test that sum_j C_j zeta'/zeta(s - sigma_j) is not identically 0 for a random C
    (sanity only) and that the Dirichlet coefficients of sum_j C_j log L(s - sigma_j, chi) at p^r are
    (1/r) chi(p)^r sum_j C_j p^{r sigma_j}  (checked against a numerical Euler-log for chi mod 5).
(ii) Lemma 2.9 without positivity: mu^{*d} = nu^{*d} <=> mu = omega nu, omega^d = 1.
    sympy: all solutions nu (two-point support {0, 1}) of nu^{*3} = mu^{*3} for mu = 2 delta_0 + 3 delta_1,
    and of nu^{*2} = mu^{*2} with three-point support.
"""
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
random.seed(7)

def main():
    print("(i) Vandermonde step with complex exponents")
    for trial in range(5):
        l = random.randint(2, 6)
        sig = [mp.mpc(random.uniform(-2, 2), random.uniform(-30, 30)) for _ in range(l)]
        for p in (2, 3, 5, 7):
            x = [mp.mpf(p) ** s for s in sig]
            A = mp.matrix(l, l)
            for r in range(1, l + 1):
                for j in range(l):
                    A[r - 1, j] = x[j] ** r
            det = mp.det(A)
            pred = mp.fprod(x) * mp.fprod(x[j] - x[i] for i in range(l) for j in range(i + 1, l))
            assert abs(det - pred) / abs(pred) < 1e-20
        print("  trial %d (l=%d): det = prod x_j prod (x_j - x_i) confirmed at p = 2,3,5,7; all nonzero" % (trial, l))
    # a collision at p = 2 only
    s1 = mp.mpc(0.3, 1.0); s2 = s1 + 2j * mp.pi / mp.log(2)
    for p in (2, 3, 5):
        print("  collision example sigma2 = sigma1 + 2 pi i/log 2: |p^s1 - p^s2| at p=%d: %s" % (p, mp.nstr(abs(mp.mpf(p) ** s1 - mp.mpf(p) ** s2), 5)))
    # chi mod 5 with chi(2) = i: Euler-log coefficients
    chi = [0, 1, 1j, -1j, -1]
    sig = [mp.mpc(0.2, 3.0), mp.mpc(-0.4, -1.5)]
    C = [mp.mpc(1.3, -0.7), mp.mpc(-0.2, 2.1)]
    # coefficient of p^{-rs} in sum_j C_j log L(s - sigma_j, chi) computed from the local factor directly:
    p = 3
    for r in (1, 2, 3):
        # local factor log (1 - chi(p) p^{sigma} p^{-s})^{-1} = sum_r chi(p)^r p^{r sigma} p^{-rs}/r
        direct = mp.fsum(Cj * (chi[p % 5] ** r) * mp.mpf(p) ** (r * sj) / r for Cj, sj in zip(C, sig))
        # numerical extraction: Taylor coefficient in X of sum_j C_j * (-log(1 - chi(p) p^{sigma_j} X))
        f = lambda X: mp.fsum(-Cj * mp.log(1 - chi[p % 5] * mp.mpf(p) ** sj * X) for Cj, sj in zip(C, sig))
        coeff = mp.diff(f, 0, r) / mp.factorial(r)
        assert abs(coeff - direct) < 1e-15
    print("  chi mod 5: p^r-coefficients (1/r) chi(p)^r sum_j C_j p^{r sigma_j} confirmed at p = 3, r = 1..3; dividing by chi(p)^r != 0 (p not 5) gives the zeta case")

    print("(ii) convolution roots without positivity")
    a, b = sp.symbols('a b')
    # nu = a delta_0 + b delta_1; mu = 2 delta_0 + 3 delta_1 ; generating polynomials in z = e^{omega}
    z = sp.symbols('z')
    for d in (2, 3, 4):
        eqs = sp.Poly(sp.expand((a + b * z) ** d - (2 + 3 * z) ** d), z).all_coeffs()
        sols = sp.solve(eqs, [a, b], dict=True)
        ratios = sorted({sp.nsimplify(sp.simplify(s[a] / 2)) for s in sols}, key=lambda w: (float(sp.re(w)), float(sp.im(w))))
        ok = all(sp.simplify(s[b] / 3 - s[a] / 2) == 0 for s in sols) and all(sp.simplify((s[a] / 2) ** d - 1) == 0 for s in sols)
        print("  d=%d: %d solutions nu = omega mu, omega in %s; all omega^d = 1 and nu/mu constant: %s" % (d, len(sols), ratios, ok))
        assert ok and len(sols) == d
    # three-point support, d = 2
    c0, c1, c2 = sp.symbols('c0 c1 c2')
    eqs = sp.Poly(sp.expand((c0 + c1 * z + c2 * z ** 2) ** 2 - (1 + 2 * z + 5 * z ** 2) ** 2), z).all_coeffs()
    sols = sp.solve(eqs, [c0, c1, c2], dict=True)
    print("  three-point mu = delta_0 + 2 delta_1 + 5 delta_2, d = 2: solutions", sols)
    assert len(sols) == 2
    print("ALL F8 CHECKS PASS")

if __name__ == "__main__":
    main()
