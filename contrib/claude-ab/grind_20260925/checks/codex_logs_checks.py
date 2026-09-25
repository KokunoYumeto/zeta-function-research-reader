#!/usr/bin/env python3
# Checks for claude-ab note 41_ (the Codex session logs of 24-25 September 2026): the two scope corrections that
# Codex's own reviews recorded (ETR9 line 411; GJN0.8/GJNR8) are verified here on explicit examples.
# Written by Claude (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort, 25 September 2026 (22:00 UTC).
from collections import Counter
import sympy as sp

results = []


def check(label, desc, ok, detail=""):
    ok = bool(ok)
    results.append(ok)
    print(f"{len(results):3d} {'PASS' if ok else 'FAIL'}  {label}  {desc}" + (f"  -- {detail}" if detail else ""))


B, g = sp.symbols('B gamma', real=True)


def conv(m1, m2):
    out = Counter()
    for a, x in m1.items():
        for b, y in m2.items():
            out[sp.simplify(a + b)] += x * y
    return out


mu = Counter({B: 3})
nu = Counter({B: 1, B + sp.I * g: 2, B - sp.I * g: 2})
mu2, nu2 = conv(mu, mu), conv(nu, nu)
check("1", "ETR9 scope (Codex review): mu_B = 3 delta_B and nu_B = delta_B + 2 delta_{B+i gamma} + 2 delta_{B-i gamma} have the same mass 9 at 2B in degree d = 2",
      mu2[2 * B] == 9 and nu2[2 * B] == 9, f"c_2(2B) = {mu2[2*B]} and {nu2[2*B]}")
check("2", "... but different total masses (maximal-face dimensions) 3 and 5", sum(mu.values()) == 3 and sum(nu.values()) == 5)
check("3", "... and different degree-2 boundary divisors, so all boundary poles at one fixed degree still separate them",
      dict(mu2) != dict(nu2), f"supports {sorted(map(str, mu2))} vs {sorted(map(str, nu2))}")
s = sp.symbols('s')
check("4", "ETR9 scope: mu = delta_i, d = 1 gives zeta(s - i), whose only pole is at s = 1 + i (no real boundary pole)",
      sp.solve(sp.Eq(s - sp.I, 1), s) == [1 + sp.I])
# GJN0.8 / GJNR8: for D(s) F0(s) with D(s0) != 0 and F0 vanishing to order exactly m at s0,
# derivatives of order < m vanish and the m-th equals D(s0) F0^{(m)}(s0); higher ones need not vanish or be nonzero.
t = sp.symbols('t')
m = 2
F0 = (s - 1) ** m * (s - 3)  # vanishes to order exactly 2 at s0 = 1
D = sp.exp(t * s ** 2) / s
prod = D * F0
ders = [sp.simplify(sp.diff(prod, s, j).subs(s, 1)) for j in range(4)]
check("5", "GJN0.8/GJNR8 (Codex review): derivatives of order < m vanish at s0, and the m-th is D(s0) F0^{(m)}(s0) != 0",
      ders[0] == 0 and ders[1] == 0 and sp.simplify(ders[2] - D.subs(s, 1) * sp.diff(F0, s, 2).subs(s, 1)) == 0 and ders[2] != 0)
# a higher derivative can vanish identically for special parameters: choose t with d^3/ds^3 (D F0)(1) = 0
t0 = sp.solve(sp.Eq(ders[3], 0), t)
check("6", "... while a derivative of order > m can vanish for a special parameter (so 'vanishes precisely for j < m' overstates)",
      len(t0) > 0, f"third derivative vanishes at t = {t0}")
n_pass = sum(results)
print("=" * 100)
print(f"{len(results)} items: {n_pass} PASS, {len(results) - n_pass} FAIL")
