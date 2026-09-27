"""ivG.py -- an independent rigorous evaluator of G(alpha, x) and dG/dalpha for the referee checks, written with
mpmath's interval arithmetic (mpmath.iv, rectangular complex intervals), NOT with Arb/python-flint.

G(alpha, x) = sum_{m>=0} (alpha + 2m) x^m / (m! (1+alpha)_m),  x = q^2/4   (note 51_, (51.1)).

Tail bound (derived independently for this referee file; valid for sup|alpha| <= a <= 0.95, sup|x| <= X, m >= MM):
  |t_m| <= b_m = (a+2m) X^m / (m! prod_{k<=m}(k-a)),   b_{m+1}/b_m <= rb := ((a+2MM+2)/(a+2MM)) X / ((MM+1)(MM+1-a)),
  |dt_m/dalpha| <= d_m = X^m/(m! prod(k-a)) (1 + (a+2m) H_m),  H_m = sum_{k<=m} 1/(k-a),
  d_{m+1}/d_m <= rd := 3 X / ((MM+1)(MM+1-a))   [the factor (1+(a+2m+2)H_{m+1})/(1+(a+2m)H_m) is <= 2 + 2.9/22 < 3],
  so the tails are <= b_MM/(1-rb) and d_MM/(1-rd).
"""
import mpmath
from mpmath import iv, mp
from mpmath.libmp import from_man_exp

iv.prec = 160
MM = 36

def ivreal_from_me(mid, rad):
    """exact interval [mid - rad, mid + rad] from (mantissa, exponent) pairs."""
    (m1, e1), (m2, e2) = mid, rad
    e = min(e1, e2)
    lo = (m1 << (e1 - e)) - (m2 << (e2 - e)); hi = (m1 << (e1 - e)) + (m2 << (e2 - e))
    return iv.mpf([mpmath.mpf(from_man_exp(lo, e)), mpmath.mpf(from_man_exp(hi, e))])

def ivbox(t):
    """t = (re_mid, re_rad, im_mid, im_rad) as (m, e) pairs -> iv complex box."""
    return iv.mpc(ivreal_from_me(t[0], t[1]), ivreal_from_me(t[2], t[3]))

def sup_abs(z):
    re, im = z.real, z.imag
    mr = max(abs(re.a), abs(re.b)); mi = max(abs(im.a), abs(im.b))
    return iv.sqrt(iv.mpf(mr) ** 2 + iv.mpf(mi) ** 2).b     # upper endpoint (an mpf)

def tails(a, X):
    a = iv.mpf(a); X = iv.mpf(X)
    prod = iv.mpf(1); H = iv.mpf(0); fact = iv.mpf(1)
    for k in range(1, MM + 1):
        prod *= (k - a); H += 1 / (k - a); fact *= k
    bM = (a + 2 * MM) * X ** MM / (fact * prod)
    dM = X ** MM / (fact * prod) * (1 + (a + 2 * MM) * H)
    rb = (a + 2 * MM + 2) / (a + 2 * MM) * X / ((MM + 1) * (MM + 1 - a))
    rd = 3 * X / ((MM + 1) * (MM + 1 - a))
    assert rb.b < 0.5 and rd.b < 0.5
    return (bM / (1 - rb)).b, (dM / (1 - rd)).b

def G_Ga(al, x, deriv=True):
    a = sup_abs(al); X = sup_abs(x)
    if not (a <= mpmath.mpf('0.95') and X <= mpmath.mpf('0.2')):
        raise ValueError("outside the domain")
    G = iv.mpc(0); Ga = iv.mpc(0); base = iv.mpc(1); S = iv.mpc(0)
    for m in range(MM):
        if m > 0:
            inv = 1 / (m + al)
            base = base * x * inv / m
            S = S + inv
        c = al + 2 * m
        G = G + base * c
        if deriv:
            Ga = Ga + base * (1 - c * S)
    tG, tGa = tails(a, X)
    e = iv.mpf([-tG, tG])
    G = G + iv.mpc(e, e)
    if deriv:
        e2 = iv.mpf([-tGa, tGa])
        Ga = Ga + iv.mpc(e2, e2)
    return G, Ga

def point_G_Ga(al, x, N=200):
    """non-rigorous mpmath point evaluation (for Newton guesses and the preconditioner Y)."""
    G = mp.mpc(0); Ga = mp.mpc(0); base = mp.mpc(1); S = mp.mpc(0)
    for m in range(N):
        if m > 0:
            inv = 1 / (m + al); base = base * x * inv / m; S += inv
        G += (al + 2 * m) * base; Ga += base * (1 - (al + 2 * m) * S)
    return G, Ga

def contains_interior(A, K):
    return (A.real.a < K.real.a and K.real.b < A.real.b and A.imag.a < K.imag.a and K.imag.b < A.imag.b)

def contains(A, K):
    return (A.real.a <= K.real.a and K.real.b <= A.real.b and A.imag.a <= K.imag.a and K.imag.b <= A.imag.b)

def contains_zero(z):
    return z.real.a <= 0 <= z.real.b and z.imag.a <= 0 <= z.imag.b
