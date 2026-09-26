#!/usr/bin/env python3
"""F12 and F13 verification (independent code).

F12(i): (1+|g|)^M |F^(r)(rho)/r!| <= 2^r ((1+|g|)/(1/2+|g|))^M b_{2,M}(F) whenever |Re rho| <= 3/2.
        Tested with F = exp(s^2/100) at the first 20 zeros (r <= 3, M <= 4) and at off-zero points with
        Re rho in {-1.5, 0, 1.5} and small heights (where the factor is close to 2).  Constant at the zeros:
        (1+g1)/(1/2+g1) with g1 = 14.1347...
F12(ii): J(Q) subset of Lambda_m: the tail estimate p_M(P - P_{<=T}) <= (1+T)^{-1} p_{M+1}(P) (a one-line inequality,
        checked on a random rapidly decreasing tuple).
F13(ii): the inputs for a complex primitive character chi mod 5 (chi(2) = i, odd):
        |1/L(2+it)| <= zeta(2);  the closed form |L(-1+it,chi)| = q^{3/2}/(2 pi^2) |1-it| sqrt(pi|t| tanh(pi|t|/2)/2) |L(2-it, conj chi)|
        (odd case), hence |L(-1+it)| >= c (1+|t|)^{3/2} for |t| >= 1 and L(-1, chi) = 0 (trivial zero);
        polynomial growth of L on a strip (sampled); the good-height mechanism needs chi and conj chi separately:
        the zeros of L(s,chi) are not symmetric under s -> conj(s) (first zero of L(s,chi) vs of L(s, conj chi)).
"""
import mpmath as mp

mp.mp.dps = 30

def F(s):
    return mp.exp(s * s / 100)

def b2M(M):
    # sup_{|sigma|<=2, t} (1+|t|)^M |exp((sigma+it)^2/100)| = e^{4/100} sup_t (1+|t|)^M e^{-t^2/100}
    f = lambda t: (1 + t) ** M * mp.exp(-t * t / 100)
    tstar = mp.findroot(lambda t: M / (1 + t) - 2 * t / 100, 7) if M > 0 else mp.mpf(0)
    return mp.exp(mp.mpf(4) / 100) * max(f(tstar), f(0))

def main():
    print("F12(i) sharper jet-decay constant")
    zeros = [mp.zetazero(k) for k in range(1, 21)]
    g1 = zeros[0].imag
    print("  (1+g1)/(1/2+g1) = %s" % mp.nstr((1 + g1) / (mp.mpf(0.5) + g1), 8))
    worst = 0
    for rho in zeros:
        g = abs(rho.imag)
        for r in range(0, 4):
            der = abs(mp.diff(F, rho, r)) / mp.factorial(r)
            for M in range(0, 5):
                lhs = (1 + g) ** M * der
                rhs = 2 ** r * ((1 + g) / (mp.mpf(0.5) + g)) ** M * b2M(M)
                worst = max(worst, lhs / rhs)
    print("  zeros 1..20, r<=3, M<=4: max lhs/rhs = %s (must be <= 1)" % mp.nstr(worst, 5))
    assert worst <= 1
    worst2 = 0
    for beta in (mp.mpf(-1.5), mp.mpf(0), mp.mpf(1.5)):
        for g in (mp.mpf(0), mp.mpf(0.3), mp.mpf(2), mp.mpf(9)):
            rho = mp.mpc(beta, g)
            for r in range(0, 3):
                der = abs(mp.diff(F, rho, r)) / mp.factorial(r)
                for M in range(0, 5):
                    lhs = (1 + g) ** M * der
                    rhs = 2 ** r * ((1 + g) / (mp.mpf(0.5) + g)) ** M * b2M(M)
                    worst2 = max(worst2, lhs / rhs)
    print("  off-zero points |Re| <= 3/2: max lhs/rhs = %s (must be <= 1)" % mp.nstr(worst2, 5))
    assert worst2 <= 1

    print("F12(ii) tail estimate for Lambda_m")
    import random
    random.seed(3)
    heights = sorted(random.uniform(14, 5000) for _ in range(400))
    P = [mp.exp(-mp.sqrt(h)) * random.uniform(0.5, 1) for h in heights]   # rapidly decreasing
    for M in (0, 1, 3):
        for T in (50, 500, 2000):
            tail = max(((1 + h) ** M * p for h, p in zip(heights, P) if h > T), default=0)
            bound = (1 + mp.mpf(T)) ** -1 * max((1 + h) ** (M + 1) * p for h, p in zip(heights, P))
            assert tail <= bound
    print("  p_M(P - P_{<=T}) <= (1+T)^{-1} p_{M+1}(P): holds for M in {0,1,3}, T in {50,500,2000}")

    print("F13(ii) L(s,chi) inputs, chi mod 5 with chi(2) = i (odd, complex)")
    chi = [0, 1, 1j, -1j, -1]
    chib = [0, 1, -1j, 1j, -1]
    L = lambda s, c=chi: mp.dirichlet(s, c)
    mx = max(abs(1 / L(mp.mpc(2, t))) for t in mp.linspace(-100, 100, 801))
    print("  max |1/L(2+it,chi)| on [-100,100] = %s <= zeta(2) = %s" % (mp.nstr(mx, 6), mp.nstr(mp.zeta(2), 6)))
    assert mx <= mp.zeta(2)
    q = 5
    worst_cf, minratio = 0, mp.inf
    for t in list(mp.linspace(-100, -1, 199)) + list(mp.linspace(1, 100, 199)):
        s = mp.mpc(-1, t)
        closed = mp.mpf(q) ** 1.5 / (2 * mp.pi ** 2) * abs(mp.mpc(1, -t)) * mp.sqrt(mp.pi * abs(t) * mp.tanh(mp.pi * abs(t) / 2) / 2) * abs(L(mp.mpc(2, -t), chib))
        val = abs(L(s))
        worst_cf = max(worst_cf, abs(val - closed) / val)
        minratio = min(minratio, val / (1 + abs(t)) ** 1.5)
    print("  closed form for |L(-1+it,chi)| (odd case): max rel. error %.2e on 1 <= |t| <= 100" % worst_cf)
    print("  min |L(-1+it,chi)|/(1+|t|)^{3/2} on 1 <= |t| <= 100: %s" % mp.nstr(minratio, 5))
    print("  L(-1,chi) = %s (trivial zero of an odd character)" % mp.nstr(abs(L(mp.mpf(-1))), 3))
    assert worst_cf < 1e-20 and minratio > 0.1
    # even characters: coth in place of tanh (Legendre mod 5; a cubic character mod 7, complex and even)
    w7 = mp.exp(2j * mp.pi / 3)
    dlog7 = {1: 0, 3: 1, 2: 2, 6: 3, 4: 4, 5: 5}             # 3 is a primitive root mod 7
    cub7 = [0] + [w7 ** dlog7[n] for n in range(1, 7)]
    cub7b = [mp.conj(c) for c in cub7]
    for name, (qq, ch, chb) in {'(./5)': (5, [0, 1, -1, -1, 1], [0, 1, -1, -1, 1]), 'cubic mod 7': (7, cub7, cub7b)}.items():
        worst_e = 0
        for t in list(mp.linspace(-60, -0.5, 60)) + [mp.mpf(0)] + list(mp.linspace(0.5, 60, 60)):
            val = abs(mp.dirichlet(mp.mpc(-1, t), ch))
            if t == 0:
                closed = mp.mpf(qq) ** 1.5 / (2 * mp.pi ** 2) * mp.sqrt(mp.mpf(1)) * abs(mp.dirichlet(2, chb))   # limit of sqrt(pi|t|coth(pi|t|/2)/2) is 1
            else:
                closed = mp.mpf(qq) ** 1.5 / (2 * mp.pi ** 2) * abs(mp.mpc(1, -t)) * mp.sqrt(mp.pi * abs(t) / mp.tanh(mp.pi * abs(t) / 2) / 2) * abs(mp.dirichlet(mp.mpc(2, -t), chb))
            worst_e = max(worst_e, abs(val - closed) / val)
        print("  even %s: closed form with coth, max rel. error %.2e on |t| <= 60 (incl. t = 0, where L(-1) != 0)" % (name, worst_e))
        assert worst_e < 1e-20
    # growth on the strip |Re s| <= 2 (sampled): log|L|/log(t) bounded
    grow = max(mp.log(abs(L(mp.mpc(x, t)))) / mp.log(t) for x in (-2, -1, 0, 0.5, 1, 2) for t in (50, 100, 200, 400))
    print("  max log|L(x+it)|/log t over x in [-2,2], t in {50..400}: %s (polynomial growth)" % mp.nstr(grow, 4))
    # asymmetry of zeros under conjugation
    r1 = mp.findroot(lambda s: L(s), mp.mpc(0.5, 6.18))
    r2 = mp.findroot(lambda s: L(s, chib), mp.mpc(0.5, 8.4))
    print("  a zero of L(s,chi): %s; |L(conj rho, chi)| = %s (conjugate is not a zero); |L(conj rho, conj chi)| = %s"
          % (mp.nstr(r1, 10), mp.nstr(abs(L(mp.conj(r1))), 4), mp.nstr(abs(L(mp.conj(r1), chib)), 4)))
    print("  a zero of L(s,conj chi): %s  (the zero sets differ; good heights for t<0 come from conj chi)" % mp.nstr(r2, 10))
    print("ALL F12/F13 CHECKS PASS")

if __name__ == "__main__":
    main()
