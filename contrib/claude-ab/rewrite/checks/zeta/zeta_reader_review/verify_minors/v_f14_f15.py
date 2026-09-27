#!/usr/bin/env python3
"""F14 and F15 verification (independent code).

F14: a = 3, F = {2, 5, 7, 10}, t = 0.2.  For J = 2, 5, 8 take the evaluations at s_j = 2 pi i j/log 3,
     j = 1..J+|F|; the combinations killing the |F| generators with n in F form a space of dimension exactly J
     (the |F| x (J+|F|) condition matrix has full rank |F|); every such combination kills 3^k generators
     (k = 1..30).  Same for the xi-multiplied family (the ideal case), with xi(s_j) != 0 checked.
F15: the constants zeta(2)(1+4pi^2)/pi and zeta(2)(1/pi + 8pi/5); the integral int (1+|t|)^{-7/2} dt = 4/5;
     the edge bound |1/zeta(-1+it)| <= 4 pi^2 zeta(2) (1+|t|)^{-3/2} on a grid; and, for three test pairs (F, G),
     the direct edge integrals of |F(s)G(1-s)/zeta(s)| compared with the two bound constants.
"""
import mpmath as mp

mp.mp.dps = 30

def xi(s):
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def gen(n, s, t):
    return mp.exp(t * s * s) * (n - mp.mpf(n) ** (1 - s)) / s

def h(n, s):
    """generator without the Gaussian: (n - n^{1-s})/s"""
    return (n - mp.mpf(n) ** (1 - s)) / s

def main():
    t = mp.mpf('0.2'); a = 3; Fset = [2, 5, 7, 10]
    print("F14: infinite codimension (a = 3, F = %s, t = 0.2)" % Fset)
    print("  Lambda = sum_j c_j ev_{s_j} kills g_t h_n  <=>  sum_j c'_j h_n(s_j) = 0 with c'_j = c_j g_t(s_j);")
    print("  it kills xi g_t h_n <=> sum_j c''_j h_n(s_j) = 0 with c''_j = c_j g_t(s_j) xi(s_j).  g_t(s_j), xi(s_j) != 0,")
    print("  so both cases reduce to the null space of H = [h_n(s_j)] (n in F).")
    m = len(Fset)
    for J in (2, 5, 8):
        pts = [2j * mp.pi * j / mp.log(a) for j in range(1, J + m + 1)]
        minxi = min(abs(xi(s)) for s in pts)
        rows = [[h(n, s) for s in pts] for n in Fset]
        HF = mp.matrix([r[:m] for r in rows])
        detHF = mp.det(HF)
        colnorm = mp.fprod(mp.sqrt(mp.fsum(abs(HF[i, j]) ** 2 for i in range(m))) for j in range(m))
        reldet = abs(detHF) / colnorm
        assert reldet > 1e-8
        basis = []
        for k in range(m, len(pts)):
            cF = mp.lu_solve(HF, mp.matrix([-r[k] for r in rows]))
            basis.append([cF[i] for i in range(m)] + [mp.mpf(1) if j == k else mp.mpf(0) for j in range(m, len(pts))])
        worst = 0
        for c in basis:
            for n in Fset:
                scale = mp.fsum(abs(cj * h(n, s)) for cj, s in zip(c, pts))
                worst = max(worst, abs(mp.fsum(cj * h(n, s) for cj, s in zip(c, pts))) / scale)
            for k in range(1, 31):
                scale = mp.fsum(abs(cj) for cj in c) * a ** k
                worst = max(worst, abs(mp.fsum(cj * h(a ** k, s) for cj, s in zip(c, pts))) / scale)
        # the J null vectors are independent (identity block in the free coordinates)
        print("  J=%d: |F| x (J+|F|) condition matrix has rank %d (Hadamard ratio %.3f); annihilating combinations: dimension %d;"
              " max relative residual on the generators n in F and n = 3^k (k<=30): %.1e; min |xi(s_j)| = %s"
              % (J, m, float(reldet), len(basis), float(worst), mp.nstr(minxi, 4)))
        assert len(basis) == J and worst < 1e-20 and minxi > 0
    print("  => for every J the closure of N_S (and of xi N_S in I_zeta) has codimension >= J: infinite codimension")
    # F = empty: every generator vanishes at every s_j, j != 0 (including negative j), but not at s = 0
    print("  F = empty: max |h(3^k, s_j)|, |j| <= 5, k <= 20: %.1e ; h(3, s->0) = %s = 3 log 3"
          % (float(max(abs(h(a ** k, 2j * mp.pi * jj / mp.log(a))) / a ** k for k in range(1, 21) for jj in (-5, -3, -1, 1, 2, 5))),
             mp.nstr(h(3, mp.mpf(10) ** -25), 12)))

    print("F15: residue-duality constants")
    z2 = mp.zeta(2)
    c_old = z2 * (1 + 4 * mp.pi ** 2) / mp.pi
    c_new = z2 * (1 / mp.pi + 8 * mp.pi / 5)
    I72 = mp.quad(lambda x: (1 + abs(x)) ** mp.mpf(-3.5), [-mp.inf, 0, mp.inf])
    I2 = mp.quad(lambda x: (1 + abs(x)) ** -2, [-mp.inf, 0, mp.inf])
    print("  zeta(2)(1+4pi^2)/pi = %s ; zeta(2)(1/pi + 8pi/5) = %s" % (mp.nstr(c_old, 8), mp.nstr(c_new, 8)))
    print("  int (1+|t|)^{-7/2} = %s (4/5) ; int (1+|t|)^{-2} = %s (2)" % (mp.nstr(I72, 12), mp.nstr(I2, 12)))
    print("  right edge: (1/2pi) zeta(2) * 2 = zeta(2)/pi = %s ; left edge: (1/2pi) 4pi^2 zeta(2) * 4/5 = %s = 8pi zeta(2)/5"
          % (mp.nstr(z2 / mp.pi, 8), mp.nstr(2 * mp.pi * z2 * I72, 8)))
    assert abs(I72 - mp.mpf(4) / 5) < 1e-20 and abs(c_new - (z2 / mp.pi + 2 * mp.pi * z2 * I72)) < 1e-20
    worst = 0
    for tt in list(mp.linspace(0, 5, 51)) + list(mp.linspace(5, 400, 400)):
        v = (1 / abs(mp.zeta(mp.mpc(-1, tt)))) / (4 * mp.pi ** 2 * z2 * (1 + tt) ** mp.mpf(-1.5))
        worst = max(worst, v)
    print("  max over t in [0,400] of |1/zeta(-1+it)| / (4pi^2 zeta(2)(1+t)^{-3/2}) = %s (<= 1)" % mp.nstr(worst, 5))
    assert worst <= 1
    # direct edge integrals versus the bounds, for three test pairs
    def b21(Ff):
        # sup_{|sigma|<=2, t} (1+|t|)|F|: sample
        best = 0
        for sg in mp.linspace(-2, 2, 17):
            for tt in mp.linspace(-60, 60, 481):
                best = max(best, (1 + abs(tt)) * abs(Ff(mp.mpc(sg, tt))))
        return best
    tests = [
        (lambda s: mp.exp(s * s / 4), lambda s: mp.exp(s * s / 4)),
        (lambda s: mp.exp((s - 0.5) ** 2) , lambda s: mp.exp((s - 0.5) ** 2)),
        (lambda s: mp.exp(s * s / 10) / (1 + s * s / 50), lambda s: mp.exp(s * s / 3)),
    ]
    for k, (Ff, Gg) in enumerate(tests):
        edge = lambda sig: mp.quad(lambda tt: abs(Ff(mp.mpc(sig, tt)) * Gg(1 - mp.mpc(sig, tt)) / mp.zeta(mp.mpc(sig, tt))), [-60, -10, 0, 10, 60]) / (2 * mp.pi)
        tot = edge(2) + edge(-1)
        bb = b21(Ff) * b21(Gg)
        print("  test %d: (1/2pi)(int_{Re 2} + int_{Re -1}) |F G(1-s)/zeta| = %s <= 8.79 b b = %s <= 21.19 b b = %s ; ratio to 8.79 bound %s"
              % (k + 1, mp.nstr(tot, 6), mp.nstr(c_new * bb, 6), mp.nstr(c_old * bb, 6), mp.nstr(tot / (c_new * bb), 4)))
        assert tot <= c_new * bb
    print("ALL F14/F15 CHECKS PASS")

if __name__ == "__main__":
    main()
