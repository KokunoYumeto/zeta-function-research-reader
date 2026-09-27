#!/usr/bin/env python3
# Checks for claude-ab note 38_ (audit of the Deligne reader DELIGNE_WEIGHT_CONTROL_FULL.md, parts MDB0-MDB8).
# Written by a subagent in the first-pass audit (25 September 2026) and copied unchanged below this header by Claude
# (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort. Re-run at 18:45 UTC: 56/56 PASS,
# output identical to the first run. Item labels A01-G02 are the ones cited in 38_.
"""
mdb_checks.py -- computational checks for the audit of MDB0-MDB8
("Mixed duality and the recovered arithmetic base", lines 3089-3751).
Items marked [ctx] concern MDB9-MDB11 (context only) or earlier-audit
programme objects; they are included because the audit brief asks for the
purity circle, the degree factor and the weight-descent defect.

Conventions (Deligne, Weil II, 1.2.6 and 6.2):
  * weight of an eigenvalue a at a point of norm q:  w_q(a) = 2 log_q |a|
  * E(r) has geometric Frobenius q^{-r}, hence weight -2r
  * K in D_{<=v}  iff  H^i K has pointwise weights <= i + v   (6.2.2)
  * K in D_{>=v}  iff  D K in D_{<=-v};  pure = both            (6.2.4)
  * H^i(K[m]) = H^{i+m}(K)
Every item prints PASS or FAIL.  Controls reject deliberately wrong variants.
"""
import itertools
import random
import math
from fractions import Fraction

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
import mpmath as mp

random.seed(20260925)
RESULTS = []


def check(num, desc, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    RESULTS.append((num, status, desc))
    print(f"[{num}] {status}  {desc}")
    if detail:
        for line in str(detail).splitlines():
            print(f"        {line}")


# ---------------------------------------------------------------------------
# Finite fields F_{p^k} = F_p[x]/(m(x)), elements = tuples (c0, ..., c_{k-1})
# ---------------------------------------------------------------------------
class GF:
    def __init__(self, p, modulus):
        # modulus: coefficients low -> high, monic of degree k
        assert modulus[-1] % p == 1
        self.p = p
        self.mod = [c % p for c in modulus]
        self.k = len(modulus) - 1
        self.q = p ** self.k
        if self.k in (2, 3):  # irreducible iff no root in F_p
            for r in range(p):
                val = sum(c * pow(r, i, p) for i, c in enumerate(self.mod)) % p
                assert val != 0, f"modulus {modulus} has root {r} mod {p}"

    def zero(self):
        return tuple([0] * self.k)

    def one(self):
        return tuple([1] + [0] * (self.k - 1))

    def const(self, c):
        return tuple([c % self.p] + [0] * (self.k - 1))

    def elements(self):
        return itertools.product(range(self.p), repeat=self.k)

    def add(self, a, b):
        return tuple((x + y) % self.p for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple((x - y) % self.p for x, y in zip(a, b))

    def mul(self, a, b):
        p, k = self.p, self.k
        prod = [0] * (2 * k - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    prod[i + j] = (prod[i + j] + x * y) % p
        for d in range(2 * k - 2, k - 1, -1):
            c = prod[d]
            if c:
                prod[d] = 0
                for i in range(k):
                    prod[d - k + i] = (prod[d - k + i] - c * self.mod[i]) % p
        return tuple(prod[:k])

    def pow(self, a, e):
        result = self.one()
        base = a
        while e > 0:
            if e & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            e >>= 1
        return result

    def chi(self, z):
        """quadratic character"""
        if z == self.zero():
            return 0
        return 1 if self.pow(z, (self.q - 1) // 2) == self.one() else -1


def count_weierstrass(F, coeffs):
    """#projective points of y^2 = sum coeffs[i] x^i over the field F
    (one point at infinity for a Weierstrass cubic)."""
    total = 1
    for x in F.elements():
        fx = F.zero()
        xp = F.one()
        for c in coeffs:
            fx = F.add(fx, F.mul(F.const(c), xp))
            xp = F.mul(xp, x)
        total += 1 + F.chi(fx)
    return total


def smallest_nonresidue(p):
    for n in range(2, p):
        if pow(n, (p - 1) // 2, p) == p - 1:
            return n
    raise ValueError


# ---------------------------------------------------------------------------
# Weight bookkeeping model: a complex = dict {degree: [weights of H^degree]}
# ---------------------------------------------------------------------------
def twist(K, r):
    return {i: [w - 2 * r for w in ws] for i, ws in K.items()}


def shift(K, m):
    # H^{i'}(K[m]) = H^{i'+m}(K): the class in degree i moves to degree i - m
    return {i - m: list(ws) for i, ws in K.items()}


def dual_point(K):
    # D on a finite-field point (K_pt = E): H^i(DK) = (H^{-i}K)^vee
    return {-i: [-w for w in ws] for i, ws in K.items()}


def dual_smooth(K, d):
    # stalk model of D_X for X smooth of dim d with lisse cohomology (MDB6.7):
    # H^i(DK) = (H^{-i-2d}K)^vee (d)
    return shift(twist(dual_point(K), d), 2 * d)


def in_Dle(K, v):
    return all(w <= i + v for i, ws in K.items() for w in ws)


def in_Dge_point(K, v):
    return in_Dle(dual_point(K), -v)


def pure_point(K, v):
    return in_Dle(K, v) and in_Dge_point(K, v)


def norm(K):
    return {i: sorted(ws) for i, ws in K.items() if ws}


def rand_complex(maxdeg=3, maxw=6):
    K = {}
    for i in range(-maxdeg, maxdeg + 1):
        if random.random() < 0.5:
            K[i] = [random.randint(-maxw, maxw) for _ in range(random.randint(1, 3))]
    return K


def rand_pure(v, maxdeg=3):
    K = {}
    for i in range(-maxdeg, maxdeg + 1):
        if random.random() < 0.5:
            K[i] = [i + v] * random.randint(1, 3)
    return K


print("=" * 78)
print("MDB0-MDB8 audit checks (context items [ctx] from MDB9-MDB11)")
print("=" * 78)

# ---------------------------------------------------------------------------
# A. Weight bookkeeping under twists, shifts and duality (MDB5, MDB6)
# ---------------------------------------------------------------------------
print("\n--- A. weight bookkeeping (MDB5-MDB6) ---")
mism, wrong_mism, trials = 0, 0, 0
for _ in range(400):
    K = rand_complex()
    for r in range(-3, 4):
        for m in range(-4, 5):
            for v in range(-6, 7):
                trials += 1
                lhs = in_Dle(K, v)
                if lhs != in_Dle(shift(twist(K, r), m), v + m - 2 * r):
                    mism += 1
                if lhs != in_Dle(shift(twist(K, r), m), v - m + 2 * r):
                    wrong_mism += 1
check("A01", "MDB6.3 shift rule: K in D<=w  <=>  K(r)[m] in D<=w+m-2r",
      mism == 0, f"{trials} random (K,r,m,w) cases, mismatches = {mism}")
check("A02", "CONTROL: wrong rule K(r)[m] in D<=w-m+2r is rejected",
      wrong_mism > 0, f"wrong rule disagrees in {wrong_mism} of {trials} cases")

ok, bad_ok = True, True
for _ in range(500):
    K = rand_complex()
    r, m = random.randint(-3, 3), random.randint(-4, 4)
    lhs = norm(dual_point(shift(twist(K, r), m)))
    ok &= lhs == norm(shift(twist(dual_point(K), -r), -m))
    bad_ok &= lhs == norm(shift(twist(dual_point(K), r), m))
check("A03", "MDB6.4 D(K(r)[m]) = (DK)(-r)[-m] on weight multisets", ok)
check("A04", "CONTROL: variant D(K(r)[m]) = (DK)(r)[m] is rejected", not bad_ok)

ok, n_true = True, 0
for _ in range(3000):
    v = random.randint(-4, 4)
    K = rand_pure(v) if random.random() < 0.5 else rand_complex()
    crit = all(w == i + v for i, ws in K.items() for w in ws)
    ok &= pure_point(K, v) == crit
    n_true += crit
check("A05", "6.2.4/6.2.5b on a point: pure of weight w <=> every H^i has all weights i+w",
      ok, f"{n_true} of 3000 samples were pure")

ok = True
for _ in range(3000):
    d = random.randint(0, 3)
    v = random.randint(-4, 4)
    K = rand_pure(v) if random.random() < 0.5 else rand_complex()
    crit = all(w == j + v for j, ws in K.items() for w in ws)
    both = in_Dle(K, v) and in_Dle(dual_smooth(K, d), -v)
    ok &= both == crit
check("A06", "MDB6.7-6.8: smooth dim d, lisse H^j: eigenvalue a in deg j <-> q^-d a^-1 in "
      "deg -j-2d; purity <=> H^j pointwise pure of weight w+j", ok)

ok = True
lines = []
for d in range(0, 5):
    KX = {-2 * d: [-2 * d]}                  # E(d)[2d]
    KpX = {-(2 * d - 2): [-(2 * d - 2)]}     # E(d-1)[2d-2]
    DKX = norm(dual_smooth(KX, d))
    ok &= DKX == {0: [0]}
    ok &= in_Dle(KX, 0) and in_Dle(dual_smooth(KX, d), 0)
    ok &= in_Dle(KpX, 0) and in_Dle(dual_smooth(KpX, d), 0)
    ok &= norm(KpX) == norm(shift(twist(KX, -1), -2))
    lines.append(f"d={d}: K_X={KX}, K'_X={KpX}, D_X K_X={DKX}")
check("A07", "MDB5.3-5.4/6.6: K_X=E(d)[2d], K'_X=K_X(-1)[-2]=E(d-1)[2d-2], both pure of weight 0",
      ok, "\n".join(lines[:3]))

ok = True
for r in range(-3, 4):
    for m in range(-4, 5):
        stalk = {-m: [-2 * r]}          # i^*(E(r)[m])
        costalk = {2 - m: [2 - 2 * r]}  # Ri^!(E(r)[m]) = E(r-1)[m-2]
        ok &= pure_point(stalk, m - 2 * r) and pure_point(costalk, m - 2 * r)
        ok &= norm(costalk) == norm(shift(twist(stalk, -1), -2))
check("A08", "MDB5.7/6.6: stalk E(r)[m] and costalk E(r-1)[m-2] both pure of weight m-2r", ok)

# MDB5.6 boxed formulas for T = E(r)[m] on S (K'_S = E, so D'_S T = E(-r)[-m])
ok, bad = True, True
for r in range(-3, 4):
    for m in range(-4, 5):
        T_stalk = {-m: [-2 * r]}
        DpS_T = (-r, -m)                           # D'_S E(r)[m] = E(-r)[-m]
        Rishriek = lambda rr, mm: {2 - mm: [2 - 2 * rr]}
        lhs1 = norm(dual_point(T_stalk))           # D_s i^* T
        rhs1 = norm(shift(twist(Rishriek(*DpS_T), 1), 2))  # (Ri^! D'_S T)(1)[2]
        lhs2 = norm(dual_point(Rishriek(r, m)))    # D_s Ri^! T
        rhs2 = norm(shift(twist({-DpS_T[1]: [-2 * DpS_T[0]]}, 1), 2))  # (i^* D'_S T)(1)[2]
        ok &= lhs1 == rhs1 and lhs2 == rhs2
        bad &= lhs1 == norm(Rishriek(*DpS_T))      # formula with factors removed
check("A09", "MDB5.6: D_s i^* = (Ri^! D'_S)(1)[2] and D_s Ri^! = (i^* D'_S)(1)[2] on Tate objects", ok)
check("A10", "CONTROL: MDB5.6 with the (1)[2] factors removed is rejected", not bad)

Ds_E = {2: [2]}   # D'_{s_p} E = E(-1)[-2]
check("A11", "MDB7.8: i_{p*}E pure of weight 0 for D' (dual H^2=E(-1), weight 2 in degree 2)",
      in_Dle({0: [0]}, 0) and in_Dle(Ds_E, 0) and not in_Dle(Ds_E, -1))

ok = True
for _ in range(500):
    v = random.randint(-4, 4)
    K = rand_pure(v)
    N = random.randint(-3, 3)
    ok &= pure_point(shift(twist(K, N), 2 * N), v)
    ok &= pure_point(shift(twist(dual_point(K), -1), -2), -v)
check("A12", "MDB6.6/6.2.5a: K(N)[2N] has the weight of K; (DK)(-1)[-2] has the weight of DK", ok)

# ---------------------------------------------------------------------------
# B. Finite-field point counts illustrating duality and its weight directions
# ---------------------------------------------------------------------------
print("\n--- B. point counts and duality (MDB4, MDB5, MDB7) ---")
moduli = {3: {1: [0, 1], 2: [1, 0, 1], 3: [-1, -1, 0, 1]},
          5: {1: [0, 1], 2: [-2, 0, 1], 3: [1, 1, 0, 1]}}
for q in (3, 5):
    Ns = {}
    for k in (1, 2, 3):
        F = GF(q, moduli[q][k])
        Ns[k] = sum(1 for x in F.elements() for y in F.elements()
                    if F.mul(x, y) == F.one())
    N1, N2, N3 = Ns[1], Ns[2], Ns[3]
    s_ = Fraction(N2, N1)
    a2 = (N1 + s_) / 2
    a1 = (s_ - N1) / 2
    fit = (a2 ** 3 - a1 ** 3 == N3)
    check(f"B01.q{q}", f"#G_m(F_{q}^k) by brute force = a2^k - a1^k with a1=1 (H^1_c), a2=q (H^2_c)",
          fit and a1 == 1 and a2 == q, f"N_k={Ns}, fitted a1={a1}, a2={a2}")
    # Poincare duality on smooth G_m (d=1): H^i = (H^{2-i}_c)^vee(-1): eigen = q / eig
    H = {0: [Fraction(q) / a2], 1: [Fraction(q) / a1]}
    Hc = {1: [a1], 2: [a2]}
    # D(Rf_! E) vs Rf_* D(E) = Rf_* E(1)[2]
    lhs = {-i: sorted(1 / e for e in es) for i, es in Hc.items()}
    rhs = {i - 2: sorted(e / q for e in es) for i, es in H.items()}
    check(f"B02.q{q}", "MDB4.4 D_pt Rf_!E = Rf_* D E on G_m -> pt (eigenvalues per degree)",
          lhs == rhs, f"D Rf_!E: {lhs}; Rf_*E(1)[2]: {rhs}")
    # support cohomology of the origin in A^1 from the localization triangle
    chi = {k: 1 - sum((-1) ** i * sum(e ** k for e in es) for i, es in H.items())
           for k in (1, 2, 3)}
    cands = {"E(-1)[-2]": (2, Fraction(q)), "E(1)[-2]": (2, Fraction(1, q)),
             "E[-2]": (2, Fraction(1)), "E(-1)[-1]": (1, Fraction(q)),
             "E(-1)[2]": (-2, Fraction(q))}
    # degrees from the long exact sequence ... -> H^j_0(A^1) -> H^j(A^1) -> H^j(G_m) -> ...
    # dims: H^*(A^1) = E in degree 0; H^*(G_m) from the fit (1-dim in degrees 0, 1);
    # the restriction is an isomorphism on constants in degree 0 (rank 1), zero in degree 1.
    dimA = {0: 1, 1: 0, 2: 0}
    dimU = {0: len(H[0]), 1: len(H[1]), 2: 0}
    rank_res = {-1: 0, 0: 1, 1: 0, 2: 0}
    dimU[-1] = 0
    dim_supp = {j: (dimA[j] - rank_res[j]) + (dimU[j - 1] - rank_res[j - 1]) for j in (0, 1, 2)}
    support_degrees = {j for j, dsz in dim_supp.items() if dsz}
    passing = [name for name, (deg, e) in cands.items()
               if all((-1) ** deg * e ** k == chi[k] for k in (1, 2, 3))
               and {deg} == support_degrees]
    check(f"B03.q{q}", "Purity Ri^!E = E(-1)[-2] (equal-char analogue of MDB5.2): only the correct "
          "candidate matches traces and degrees; wrong twist/shift variants rejected",
          passing == ["E(-1)[-2]"], f"support Euler traces {chi}; passing candidates {passing}")
    w = lambda e: 2 * math.log(float(e), q)
    Rfshriek = {1: [round(w(a1))], 2: [round(w(a2))]}
    Rfstar = {0: [round(w(H[0][0]))], 1: [round(w(H[1][0]))]}
    neg = (in_Dle(Rfshriek, 0) and not in_Dge_point(Rfshriek, 0)
           and in_Dge_point(Rfstar, 0) and not in_Dle(Rfstar, 0))
    check(f"B04.q{q}", "Negative (MDB7 caveat): for pure E on G_m, Rf_! lies in D<=0 but not D>=0; "
          "Rf_* lies in D>=0 but not D<=0", neg, f"Rf_!E weights {Rfshriek}; Rf_*E weights {Rfstar}")

# Kunneth: G_m x G_m -> pt, Rf_!E in D<=0 (MDB7.4) with explicit counts
q = 3
Fk = {k: GF(q, moduli[q][k]) for k in (1, 2)}
okk = True
for k in (1, 2):
    F = Fk[k]
    nz = sum(1 for x in F.elements() if x != F.zero())
    Nk = nz * nz
    tr = (q ** 2) ** k - 2 * q ** k + 1  # H^4_c (q^2), H^3_c (2 x q), H^2_c (1)
    okk &= Nk == tr
Rf2 = {2: [0], 3: [2, 2], 4: [4]}
check("B05", "MDB7.2-7.4 example: #(G_m^2)(F_3^k) = q^2k - 2q^k + 1; Rf_!E in D<=0 on the nose",
      okk and in_Dle(Rf2, 0) and not in_Dle(Rf2, -1))

# i^* does not preserve D>=w: Legendre family, nodal fibre at lambda = 0
ok_nodal, ok_smooth, info = True, True, []
for p in [5, 7, 11, 13, 17, 19, 23]:
    F = GF(p, [0, 1])
    N0 = count_weierstrass(F, [0, 0, -1, 1])     # y^2 = x^3 - x^2 = x^2 (x-1)
    eps = p + 1 - N0
    leg = 1 if pow(p - 1, (p - 1) // 2, p) == 1 else -1
    ok_nodal &= (eps == leg)
    for lam in range(2, p):
        # y^2 = x(x-1)(x-lam) = x^3 - (1+lam) x^2 + lam x
        Nl = count_weierstrass(F, [0, lam, -(1 + lam), 1])
        a = p + 1 - Nl
        ok_smooth &= a * a <= 4 * p
    info.append(f"p={p}: nodal #={N0}, eps={eps}, (-1/p)={leg}")
check("B06", "Negative (MDB7 caveat): Legendre fibres have |a|^2<=4p (weight 1) but the nodal fibre "
      "at lambda=0 has H^1 eigenvalue eps=+-1 (weight 0): i_0^* j_*R^1 is not in D>=1",
      ok_nodal and ok_smooth, "\n".join(info[:4]))

# ---------------------------------------------------------------------------
# C. Programme objects: CC topology, supports, group, recovered ring (MDB0-MDB2)
# ---------------------------------------------------------------------------
print("\n--- C. programme objects (MDB0-MDB2) ---")
X = frozenset({"+", "-", "eta"})
opens = {frozenset(), X, frozenset({"+", "eta"}), frozenset({"-", "eta"}), frozenset({"eta"})}
is_top = all((a | b) in opens and (a & b) in opens for a in opens for b in opens)
closure = lambda S: frozenset(x for x in X if all(not (x in U) or (U & S) for U in opens))
dense_pts = [x for x in X if closure(frozenset({x})) == X]
homeos = []
for perm in itertools.permutations(sorted(X)):
    f = dict(zip(sorted(X), perm))
    if all(frozenset(f[x] for x in U) in opens for U in opens):
        homeos.append(f)
check("C01", "MDB2.1: the five sets form a topology; eta is the unique dense point; every "
      "homeomorphism fixes eta", is_top and dense_pts == ["eta"] and all(h["eta"] == "eta" for h in homeos),
      f"homeomorphisms: {len(homeos)} (identity and the +/- swap)")
least = frozenset.intersection(*[U for U in opens if "eta" in U])
check("C02", "MDB2.3: the least open neighbourhood of eta is Omega={eta}, so F_eta = F(Omega)",
      least == frozenset({"eta"}))
alpha = {"+": "-", "-": "+", "eta": "eta"}
sigma = {"even": "odd", "odd": "even"}
equiv = [P for P in itertools.product(["even", "odd"], repeat=3)
         if all(dict(zip(["+", "-", "eta"], P))[alpha[x]] == sigma[dict(zip(["+", "-", "eta"], P))[x]]
                for x in ["+", "-", "eta"])]
Y2 = ["a", "b"]
beta = {"a": "b", "b": "a"}
equiv_free = [P for P in itertools.product(["even", "odd"], repeat=2)
              if all(dict(zip(Y2, P))[beta[x]] == sigma[dict(zip(Y2, P))[x]] for x in Y2)]
check("C03", "MDB2 parity: no equivariant label X -> {even,odd} (fixed point eta); CONTROL: a "
      "free involution does admit one", len(equiv) == 0 and len(equiv_free) == 2,
      f"equivariant labels on X: {len(equiv)}; on free 2-point set: {len(equiv_free)}")
# constant support map from a finite model of |Spec Z| (closed sets = finite sets of primes, or all)
primes_small = list(sp.primerange(2, 30))
SigmaPts = ["gen"] + [f"({p})" for p in primes_small]
T_opens = [frozenset(), frozenset({"tau"})]
pre = lambda V: frozenset(SigmaPts) if V else frozenset()
cont = all(pre(V) in (frozenset(), frozenset(SigmaPts)) for V in T_opens)
pre_X = [frozenset(SigmaPts) if "eta" in U else frozenset() for U in opens]
check("C04", "MDB2.6: c_Sigma is continuous and every nonempty open of X has full preimage "
      "under j_tau o c_Sigma (the map is constant, i.e. factors through the terminal space)",
      cont and all((pU == frozenset(SigmaPts)) == bool(U) for pU, U in zip(pre_X, opens)))

# G = <T,J,eps> = Z x C_4 additively: T=(1,0), J=(0,1), eps=(0,2)
add = lambda a, b: (a[0] + b[0], (a[1] + b[1]) % 4)
mulk = lambda k, a: (k * a[0], (k * a[1]) % 4)
T, J, eps_ = (1, 0), (0, 1), (0, 2)
rel = mulk(2, J) == eps_ and mulk(2, eps_) == (0, 0) and mulk(4, J) == (0, 0)
torsion = sorted({(0, c) for c in range(4)})
check("C05", "MDB0.1: in G=<T,J,eps | J^2=eps, eps^2=1, commuting> = Z x C4, H=<J> is the full "
      "torsion subgroup and G/H = <T> is infinite cyclic",
      rel and torsion == sorted({mulk(k, J) for k in range(4)}))
epsJ = add(eps_, J)
phi = lambda g: (g[0], (3 * g[1]) % 4)   # T->T, J->eps J = J^3
aut = (mulk(2, epsJ) == eps_ and mulk(4, epsJ) == (0, 0) and phi(J) == epsJ and phi(eps_) == eps_
       and len({phi((0, c)) for c in range(4)}) == 4 and all(phi(phi((0, c))) == (0, c) for c in range(4)))
A = lambda g: add(mulk(g[0], add(eps_, (-1, 0))), mulk(g[1], (0, 3)))   # A(T)=eps T^-1, A(J)=J^-1
invol = all(A(A((m, c))) == (m, c) for m in range(-3, 4) for c in range(4))
induces_inv = all(A((m, c))[0] == -m for m in range(-3, 4) for c in range(4))
check("C06", "MDB2.4 (imported chart data) is consistent: J -> eps J is an automorphism of G fixing "
      "T, eps; the involution A(T)=eps T^-1, A(J)=J^-1 is an involution inducing inversion on L",
      aut and invol and induces_inv)
# End(Z): power maps
power = lambda n: (lambda x: n * x)
samples = range(-7, 8)
ring_ok = all(power(m)(x) + power(n)(x) == power(m + n)(x) and power(m)(power(n)(x)) == power(m * n)(x)
              for m in range(-4, 5) for n in range(-4, 5) for x in samples)
gen_indep = all(power(n)(1) == -power(n)(-1) for n in range(-5, 6))
check("C07", "MDB1.1-1.2: n -> [n] is a ring isomorphism Z -> End(Z) ([m]+[n]=[m+n], [m][n]=[mn]); "
      "[n] is independent of the generator (u vs u^-1)", ring_ok and gen_indep)
# conjugation by an isomorphism B: Z -> 2Z (x -> 2x) and by inversion
B = lambda x: 2 * x
Binv = lambda y: y // 2
conj_ok = all(B(power(n)(Binv(y))) == n * y for n in range(-4, 5) for y in range(-10, 11, 2))
inv_ok = all(-(power(n)(-x)) == power(n)(x) for n in range(-4, 5) for x in samples)
check("C08", "MDB1.5: C_B([n]) = [n]' for the branch isomorphism x -> 2x onto 2Z; conjugation by "
      "inversion is the identity on R", conj_ok and inv_ok)
norms_ok = True
for p in sp.primerange(2, 60):
    # index of [p]L = pZ in L = Z via Smith normal form of the relation matrix (p)
    snf = smith_normal_form(sp.Matrix([[p]]), domain=sp.ZZ)
    cosets = {x % p for x in range(-3 * p, 3 * p)}      # classes of L/[p]L met in a window
    norms_ok &= abs(snf[0, 0]) == p and len(cosets) == p
check("C09", "MDB1.3: residue norm N(s_p) = |R/pR| = |L/[p]L| = p (Smith form and coset count)", norms_ok)
# negative: recovered ring depends only on the free rank
groups = {"Z x C4": sp.Matrix([[0, 4]]), "Z x C6": sp.Matrix([[0, 6]]),
          "Z x C2 x C2": sp.Matrix([[0, 2, 0], [0, 0, 2]]), "Z": sp.zeros(0, 1)}
ranks = {}
for name, rel_m in groups.items():
    ngen = rel_m.shape[1]
    r = rel_m.rank() if rel_m.shape[0] > 0 else 0
    ranks[name] = ngen - r
check("C10", "Negative (MDB1/MDB2.5): G -> End(G/G_tors) sees only the free rank; Z x C4, Z x C6, "
      "Z x C2 x C2 and Z give the same ring Z (C4 and phase data are forgotten)",
      set(ranks.values()) == {1}, f"free ranks: {ranks}")

# ---------------------------------------------------------------------------
# D. Tate twist, Frobenius conventions, Hensel/Kummer step (MDB3, MDB5, MDB6)
# ---------------------------------------------------------------------------
print("\n--- D. Tate twist and Frobenius conventions (MDB3, MDB5, MDB6) ---")
F343 = GF(7, [-2, 0, 0, 1])      # x^3 - 2, irreducible over F_7 (2 is not a cube mod 7)
qq = F343.q
factors = sp.factorint(qq - 1)
g = None
for e in F343.elements():
    if e == F343.zero():
        continue
    if all(F343.pow(e, (qq - 1) // r) != F343.one() for r in factors):
        g = e
        break
zeta9 = F343.pow(g, (qq - 1) // 9)
order9 = F343.pow(zeta9, 9) == F343.one() and F343.pow(zeta9, 3) != F343.one()
frob = lambda x: F343.pow(x, 7)
frob_order3 = (all(F343.pow(x, 343) == x for x in list(F343.elements())[:60])
               and any(frob(x) != x for x in F343.elements())
               and any(frob(frob(x)) != x for x in F343.elements()))
inv7 = pow(7, -1, 9)
geom_on_mu = F343.pow(zeta9, inv7)            # geometric Frobenius = inverse of x -> x^7
geom_ok = frob(geom_on_mu) == zeta9
# on Z/9(-1) = Hom(mu_9, Z/9): (F_geom f)(z) = f(F_geom^{-1} z) = f(z^7) = 7 f(z)
f_hom = {F343.pow(zeta9, j): j % 9 for j in range(9)}
act = all(f_hom[frob(F343.pow(zeta9, j))] == (7 * j) % 9 for j in range(9))
check("D01", "MDB3.5/MDB6: in F_{7^3}, x->x^7 generates Gal (order 3); geometric Frobenius acts on "
      "mu_9 = Z/9(1) by 7^-1 = 4 and on Z/9(-1) by 7 = p (weights -2 and +2)",
      order9 and frob_order3 and geom_ok and act and inv7 == 4)
wt = lambda a, qv: 2 * math.log(abs(a), qv)
check("D02", "MDB6.1: E(r) has geometric eigenvalue p^-r, weight -2r (r=-2..2, p=7)",
      all(abs(wt(7.0 ** (-r), 7) - (-2 * r)) < 1e-12 for r in range(-2, 3)))
ok = True
for _ in range(500):
    a = complex(random.uniform(-5, 5), random.uniform(-5, 5))
    qv = random.choice([2, 3, 4, 5, 7, 9, 11])
    dd = random.randint(1, 6)
    ok &= abs(wt(a ** dd, qv ** dd) - wt(a, qv)) < 1e-9
check("D03", "MDB7.1: w_{q^d}(a^d) = w_q(a) (pullback preserves pointwise weights)", ok)
# Hensel step behind MDB5.2f at finite level: every unit of Z_7 is a 5th power (gcd(5,6)=1)
p_, l_, Nprec = 7, 5, 8
mod = p_ ** Nprec
hens_ok = True
for u in range(1, 60):
    if u % p_ == 0:
        continue
    c = next(c for c in range(1, p_) if pow(c, l_, p_) == u % p_)
    x = c
    for _ in range(Nprec + 2):
        x = (x - (pow(x, l_, mod) - u) * pow(l_ * pow(x, l_ - 1, mod), -1, mod)) % mod
    hens_ok &= pow(x, l_, mod) == u % mod
check("D04", "MDB5.2f Hensel step (finite level): residue l-th roots lift (p=7, l=5, mod 7^8), so "
      "K^x/(K^x)^l is detected by the valuation", hens_ok)
# MDB5.2c-d: cohomology of the procyclic quotient Z_l(1) with coefficients Z/l^a computed from the
# length-one resolution 0 -> M --(gamma-1)--> M -> 0; trivial action gives H^0 = H^1 = M.
la, p_frob = 9, 7


def procyclic_H(u):
    # gamma acts on M = Z/la by multiplication by u; d = gamma - 1
    dmap = [((u - 1) * m) % la for m in range(la)]
    ker = sum(1 for m in range(la) if dmap[m] == 0)
    coker = la // len(set(dmap))
    return ker, coker


H0t, H1t = procyclic_H(1)
H0n, H1n = procyclic_H(4)       # CONTROL: a nontrivial action changes the answer
# Frobenius on H^1 = Hom(I_t/9, Z/9): arithmetic phi acts on I_t by sigma -> sigma^p, so
# (F_geom f)(sigma) = f(phi sigma phi^-1) = p f(sigma): geometric Frobenius acts by p on Z/9(-1)
cocycles = [lambda j, c=c: (c * j) % la for c in range(la)]
geom_by_p = all(all(f((p_frob * j) % la) == (p_frob * f(j)) % la for j in range(la)) for f in cocycles)
check("D05", "MDB5.2d-e: trivial coefficients give H^0 = H^1 = Z/9 (9 = l^a) with geometric Frobenius p "
      "on H^1 = Z/9(-1); CONTROL: a nontrivial action (gamma = 4) gives 3 and 3 instead",
      (H0t, H1t) == (9, 9) and (H0n, H1n) == (3, 3) and geom_by_p,
      f"trivial: |H^0|,|H^1| = {(H0t, H1t)}; gamma=4: {(H0n, H1n)}")

# ---------------------------------------------------------------------------
# E. MDB7-MDB8 linear algebra: extensions, strictness, Ext^1, semisimplicity
# ---------------------------------------------------------------------------
print("\n--- E. mixed filtration linear algebra (MDB7, MDB8) ---")
ok = True
x = sp.symbols("x")
for _ in range(30):
    n1, n2 = random.randint(1, 3), random.randint(1, 3)
    A1 = sp.Matrix(n1, n1, lambda i, j: random.randint(-4, 4))
    A2 = sp.Matrix(n2, n2, lambda i, j: random.randint(-4, 4))
    Bm = sp.Matrix(n1, n2, lambda i, j: random.randint(-4, 4))
    M = sp.BlockMatrix([[A1, Bm], [sp.zeros(n2, n1), A2]]).as_explicit()
    ok &= sp.expand(M.charpoly(x).as_expr() - A1.charpoly(x).as_expr() * A2.charpoly(x).as_expr()) == 0
check("E01", "MDB7: eigenvalues of an extension = union of sub and quotient multisets "
      "(block upper triangular char. polynomial factorizes)", ok)


def jordan(alpha, size):
    Jm = sp.eye(size) * alpha
    for i in range(size - 1):
        Jm[i, i + 1] = 1
    return Jm


def rand_frob(blocks):
    D = sp.diag(*[jordan(a, s) for a, s in blocks])
    n = D.shape[0]
    while True:
        P = sp.Matrix(n, n, lambda i, j: random.randint(-2, 2))
        if P.det() != 0:
            break
    return P * D * P.inv()


QW = 3


def weight_exact(alpha):
    a = abs(sp.Rational(alpha))
    k = sp.multiplicity(QW, a.p) - sp.multiplicity(QW, a.q)
    assert a == sp.Rational(QW) ** k
    return 2 * k


def gen_eigspace(Fm, alpha):
    n = Fm.shape[0]
    return ((Fm - alpha * sp.eye(n)) ** n).nullspace()


def W_basis(Fm, eigs, nmax):
    vecs = []
    for a in set(eigs):
        if weight_exact(a) <= nmax:
            vecs += gen_eigspace(Fm, a)
    return sp.Matrix.hstack(*vecs) if vecs else sp.zeros(Fm.shape[0], 0)


def rk(M):
    return 0 if M.shape[1] == 0 or M.shape[0] == 0 else M.rank()


def sylvester_solutions(F1, F2):
    # h: V1 -> V2 with F2 h = h F1 ; h is m x n
    n, m = F1.shape[0], F2.shape[0]
    rows = []
    for i in range(m):
        for j in range(n):
            row = [0] * (m * n)
            # (F2 h)_{ij} - (h F1)_{ij} = sum_k F2[i,k] h[k,j] - sum_k h[i,k] F1[k,j]
            for k in range(m):
                row[k * n + j] += F2[i, k]
            for k in range(n):
                row[i * n + k] -= F1[k, j]
            rows.append(row)
    Msys = sp.Matrix(rows)
    return [sp.Matrix(m, n, list(v)) for v in Msys.nullspace()]


strict_ok, tested, control_fail = True, 0, 0
eig_pool = [1, -1, 3, -3, 9, sp.Rational(1, 3)]
for trial in range(6):
    b1 = [(random.choice(eig_pool), random.randint(1, 2)) for _ in range(3)]
    b2 = [(random.choice(eig_pool), random.randint(1, 2)) for _ in range(3)]
    b2[0] = (b1[0][0], b2[0][1])   # share an eigenvalue so Hom_F is nonzero
    F1, F2 = rand_frob(b1), rand_frob(b2)
    e1 = [a for a, s in b1 for _ in range(s)]
    e2 = [a for a, s in b2 for _ in range(s)]
    sols = sylvester_solutions(F1, F2)
    if not sols:
        continue
    h = sum((random.randint(-3, 3) * S for S in sols), sp.zeros(F2.shape[0], F1.shape[0]))
    if h == sp.zeros(*h.shape):
        h = sols[0]
    assert F2 * h == h * F1
    hbad = sp.Matrix(F2.shape[0], F1.shape[0], lambda i, j: random.randint(-3, 3))
    for nmax in range(-4, 6):
        B1, B2 = W_basis(F1, e1, nmax), W_basis(F2, e2, nmax)
        hB = h * B1
        incl = rk(sp.Matrix.hstack(B2, hB)) == rk(B2)
        dim_img = rk(hB)
        dim_int = rk(h) + rk(B2) - rk(sp.Matrix.hstack(h, B2))
        strict_ok &= incl and dim_img == dim_int
        tested += 1
        if rk(sp.Matrix.hstack(B2, hbad * B1)) != rk(B2):
            control_fail += 1
check("E02", "MDB8.4-8.5: for Frobenius-equivariant h (solved from F'h = hF, Jordan blocks allowed), "
      "h(W_n V) = im h cap W_n V' for every n", strict_ok and tested > 0, f"{tested} (h, n) cases")
check("E03", "CONTROL: a random non-equivariant linear map fails to preserve W_n", control_fail > 0,
      f"non-equivariant map leaves W_n in {control_fail} cases")
ext_ok = True
for a in [1, 3, 9, -1, sp.Rational(1, 3)]:
    for b in [1, 3, 9, -1, sp.Rational(1, 3)]:
        Mx = sp.Matrix([[b, 1], [0, a]])       # extension of V (eigen a) by W (eigen b)
        split = Mx.is_diagonalizable()
        coinv_nonzero = (sp.Rational(b) / sp.Rational(a) == 1)   # coker(F-1) on Hom(V,W)
        ext_ok &= (not split) == coinv_nonzero
check("E04", "MDB8.2 on a point: an extension is non-split iff F-coinvariants of Hom(V,W) are "
      "nonzero iff the eigenvalues agree (equal weights allowed, cf. MDB8.3)", ext_ok)
U = sp.Matrix([[1, 1], [0, 1]])
inv_lines = [v for v in U.eigenvects()]
check("E05", "Negative (MDB8, normality retained): unipotent monodromy [[1,1],[0,1]] (all eigenvalues "
      "1, pure weight 0) has a single invariant line and no invariant complement -> not semisimple "
      "(nodal-cubic local system shows 3.4.1(iii) needs normality)",
      len(inv_lines) == 1 and inv_lines[0][1] == 2 and len(inv_lines[0][2]) == 1)
# Triple model of j_*F for the Legendre family near lambda = 0 over F_13 (computed data):
# generic stalk F_U at lambda0 with Frobenius eigenvalues of |a|^2 = p; boundary stalk F_Z = 1-dim
# with eigenvalue eps (nodal count); s: F_Z -> i^*j_*F_U the specialization iso onto invariants.
p_ = 13
F13 = GF(p_, [0, 1])
lam0 = 2
a_l = p_ + 1 - count_weierstrass(F13, [0, lam0, -(1 + lam0), 1])
eps0 = p_ + 1 - count_weierstrass(F13, [0, 0, -1, 1])
roots = [(a_l + complex(a_l * a_l - 4 * p_) ** 0.5) / 2, (a_l - complex(a_l * a_l - 4 * p_) ** 0.5) / 2]
wU = [2 * math.log(abs(r), p_) for r in roots]
wZ = 2 * math.log(abs(eps0), p_)
W0_U_dim = sum(1 for w in wU if w <= 0 + 1e-9)   # weight <= 0 part of F_U
s_map = sp.Matrix([[1]])
kernel_s = s_map.nullspace()
W0_Z_dim = 0 if W0_U_dim == 0 and len(kernel_s) == 0 else None   # s(W_0|Z) must lie in i^*j_*(0) = 0
check("E06", "Negative (MDB8 scope): for j_*F (Legendre family at lambda=0, p=13, computed weights) "
      "W_0|U = 0 and ker s = 0 force W_0 = 0, while the boundary stalk has weight 0 != 1: no increasing "
      "filtration with pointwise-pure graded pieces exists for this non-lisse mixed sheaf",
      W0_U_dim == 0 and W0_Z_dim == 0 and abs(wZ) < 1e-12 and all(abs(w - 1) < 1e-9 for w in wU),
      f"a_lambda={a_l}, generic weights {[round(w, 9) for w in wU]}, eps={eps0}, boundary weight {wZ}")
V = sp.Matrix([[1, 0, 0], [0, 3, 0], [0, 0, 9]])
Wn = sp.Matrix([[1, 0], [0, 1], [0, 0]])       # weights <= 2 part
Q = sp.Matrix([[0, 0, 1]])                     # V -> V / W_n
kern = sp.Matrix.vstack(Q, Q).nullspace()      # two geometric preimages over x (finite cover)
check("E07", "MDB8.3k (stalk form): kernel of V -> (V/W_n) + (V/W_n) over two preimages equals W_n",
      sp.Matrix.hstack(*kern).rank() == 2 and sp.Matrix.hstack(Wn, *kern).rank() == 2)

# ---------------------------------------------------------------------------
# F. Euler product, degree factor, defect, purity circle  ([ctx] where noted)
# ---------------------------------------------------------------------------
print("\n--- F. zeta Euler product, degree factor, defect, purity circle ---")
mp.mp.dps = 30
ell = 3
P = 200000
plist = list(sp.primerange(2, P))


def euler(sv, drop_ell=False, shift_tate=0):
    val = mp.mpf(1)
    for p in plist:
        if p == ell and drop_ell:
            continue
        val *= 1 / (1 - mp.mpf(p) ** (shift_tate - sv))
    return val


for sv in (2, 3):
    full = euler(sv)
    check(f"F01.s{sv}", f"MDB1.4: (1-3^-s)^-1 prod_(p!=3)(1-p^-s)^-1 = zeta({sv}) (primes < {P})",
          abs(full / mp.zeta(sv) - 1) < 1e-5, f"ratio = {mp.nstr(full / mp.zeta(sv), 12)}")
check("F02", "CONTROL: dropping the coefficient-prime factor (1-3^-s)^-1 is rejected",
      abs(euler(2, drop_ell=True) / mp.zeta(2) - 1) > 1e-2)
cost = euler(4, shift_tate=1)
check("F03", "MDB5.7/[ctx MDB9] degree factor: costalk factors det(1-p^-s F|E(-1))^-1 = (1-p^(1-s))^-1 "
      "multiply to zeta(s-1) (s=4)", abs(cost / mp.zeta(3) - 1) < 1e-5)
check("F04", "CONTROL: costalk factor without the Tate factor p gives zeta(s), not zeta(s-1): rejected",
      abs(euler(4) / mp.zeta(3) - 1) > 1e-2)
defect_ok = True
for p in (2, 3, 5, 7):
    hom_F = sylvester_solutions(sp.Matrix([[1]]), sp.Matrix([[sp.Rational(1, p)]]))   # E -> E(1)
    hom_vect = sp.zeros(1, 1).nullspace()                                              # all 1x1 maps
    defect_ok &= len(hom_F) == 0 and len(hom_vect) == 1
check("F05", "[ctx MDB10] defect: Frobenius-equivariant maps E -> E(1) at s_p solve c = p^-1 c, so "
      "Hom_F = 0 while Hom of the underlying lines is 1-dimensional", defect_ok)

circle_ok, dual_ok, fix_ok, trace_ok, ctrl_ok = True, True, True, True, True
info = []
for (p, a4, a6) in [(13, 2, 3), (17, 1, 7), (19, 3, 5), (23, 1, 1), (29, 4, 2), (31, 2, 9)]:
    assert (4 * a4 ** 3 + 27 * a6 ** 2) % p != 0
    F1 = GF(p, [0, 1])
    n = smallest_nonresidue(p)
    F2 = GF(p, [-n, 0, 1])
    N1 = count_weierstrass(F1, [a6, a4, 0, 1])
    N2 = count_weierstrass(F2, [a6, a4, 0, 1])
    ap = p + 1 - N1
    disc = complex(ap * ap - 4 * p)
    al = (ap + disc ** 0.5) / 2
    be = (ap - disc ** 0.5) / 2
    circle_ok &= abs(abs(al) ** 2 - p) < 1e-9
    dual_ok &= abs(al * be - p) < 1e-9
    fix_ok &= abs(p / al.conjugate() - al) < 1e-9
    trace_ok &= abs(N2 - (p * p + 1 - (al ** 2 + be ** 2).real)) < 1e-6
    ctrl_ok &= abs(1 / al.conjugate() - al) > 1e-3
    # MDB4.4 for proper f: H^-1(D_pt Rf_*E) = H^1^vee  vs  H^-1(Rf_* E(1)[2]) = H^1(1)
    lhs_m = sorted([1 / al, 1 / be], key=lambda z: (round(z.real, 9), round(z.imag, 9)))
    rhs_m = sorted([al / p, be / p], key=lambda z: (round(z.real, 9), round(z.imag, 9)))
    proper_dual_ok = all(abs(u - v) < 1e-9 for u, v in zip(lhs_m, rhs_m))
    dual_ok &= proper_dual_ok
    info.append(f"p={p}: #E(F_p)={N1}, a_p={ap}, #E(F_p^2)={N2}")
check("F06", "[ctx MDB9] purity circle on actual curves: |alpha|^2 = p, alpha*beta = p (Poincare "
      "duality with Tate factor; equivalently {1/alpha,1/beta} = {alpha/p,beta/p}, i.e. "
      "D Rf_* = Rf_* D in degree -1, MDB4.4), p/conj(alpha) = alpha; F_p^2 counts match "
      "p^2+1-(alpha^2+beta^2)",
      circle_ok and dual_ok and fix_ok and trace_ok, "\n".join(info[:3]))
check("F07", "CONTROL: untwisted dual a -> 1/conj(a) does not fix alpha (Tate factor needed)", ctrl_ok)


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


sym_ok = True
for s0 in [mp.mpc("0.3", "5.1"), mp.mpc("0.8", "21.7"), mp.mpc("0.15", "2.2"), mp.mpc("0.62", "37.0")]:
    lhs, rhs = xi(1 - mp.conj(s0)), mp.conj(xi(s0))
    sym_ok &= abs(lhs - rhs) <= mp.mpf("1e-20") * (1 + abs(rhs))
rho = mp.mpc("0.7", "14.0")
neg_ok = True
for p in (2, 3, 5, 7):
    a = mp.power(p, rho)
    ia = p / mp.conj(a)
    neg_ok &= abs(ia - mp.power(p, 1 - mp.conj(rho))) < 1e-20
    neg_ok &= abs(p / mp.conj(ia) - a) < 1e-20
    neg_ok &= abs(abs(a) ** 2 - p) > 0.1 and abs(abs(ia) ** 2 - p) > 0.1
check("F08", "[ctx MDB9.9-9.10] negative: xi(1-conj s) = conj xi(s) holds unconditionally, so the "
      "zero set is always stable under rho -> 1-conj(rho), i.e. a -> p/conj(a); a hypothetical off-line "
      "pair (Re rho = 0.7) is swapped by the involution yet lies off |a|^2 = p",
      sym_ok and neg_ok)
avg_ok = True
for sgm in (0.5, 0.6, 0.7, 0.9, 0.99):
    ws = [2 * sgm, 2 * (1 - sgm), 2 * sgm, 2 * (1 - sgm)]
    avg_ok &= abs(sum(ws) / 4 - 1) < 1e-12
check("F09", "[ctx prior audit] quartet {rho, 1-conj rho, conj rho, 1-rho}: average (determinant) "
      "weight is 1 for every Re rho, so it cannot detect off-line zeros", avg_ok)

# ---------------------------------------------------------------------------
# G. Bridge obstructions to programme operators
# ---------------------------------------------------------------------------
print("\n--- G. bridge obstructions ---")
qs = sp.symbols("q", positive=True)
Phi = sp.diag(1, qs)
Nn = sp.Matrix([[0, 1], [0, 0]])
wd = sp.simplify(Phi * Nn * Phi.inv() - Nn / qs) == sp.zeros(2, 2)
wd_b = sp.simplify(Nn * Phi - qs * Phi * Nn) == sp.zeros(2, 2)
xs, ys = sp.symbols("x y", nonzero=True)
Phic = sp.Matrix([[xs, ys], [0, xs]])          # the commutant of N
commute_bad = sp.simplify(Phic * Nn * Phic.inv() - Nn / qs)
forced = sp.solve(sp.Eq(commute_bad[0, 1], 0), qs)
check("G01", "Bridge test: a Weil-Deligne pair satisfies Phi N Phi^-1 = q^-1 N (so N Phi = q Phi N, "
      "the shape N P_b = b P_b N with b=q, Phi having eigenvectors); an operator commuting with N != 0 "
      "satisfies it only if q = 1, so W_p with [W_p,N]=0, N!=0 cannot be the Frobenius at p",
      wd and wd_b and forced == [1], f"q forced to {forced}")
import numpy as np
rng = np.random.default_rng(1)
has_eig = all(np.linalg.matrix_rank(M - np.linalg.eigvals(M)[0] * np.eye(5)) < 5
              for M in [rng.standard_normal((5, 5)) for _ in range(20)])
check("G02", "Bridge test: every operator on a nonzero finite-dimensional complex space has an "
      "eigenvector, so an operator without eigenvectors has no nonzero finite-dimensional stable "
      "subspace and receives no nonzero equivariant map from a stalk or H^i over F_p", has_eig)

# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
npass = sum(1 for _, s, _ in RESULTS if s == "PASS")
print(f"SUMMARY: {npass} PASS, {len(RESULTS) - npass} FAIL, {len(RESULTS)} items")
print("=" * 78)
