#!/usr/bin/env python3
"""ref_prop514_margins.py -- exponent bookkeeping for the referee comments on Proposition 51.4 of note 51_.

Classical lower bounds at a singular time T for smooth solutions (Leray 1934; see Robinson-Sadowski-Silva 2012):
  ||grad u(t)||_2^2 >= c (T-t)^(-1/2),   ||u(t)||_p >= c_p (T-t)^(-(p-3)/(2p))  (3 < p <= infinity).
Construction (conditional, Prop. 51.4): ||u||_p^p >= c tau^(3/2 - h - p(1/2+h)), enstrophy >= c tau^(-1/2-3h).
The 'margin' is the ratio (construction lower bound)/(classical lower bound) as a power of tau.
"""
import sympy as sp
h, p, tau = sp.symbols('h p tau', positive=True)
constr_Lp = (sp.Rational(3, 2) - h) / p - (sp.Rational(1, 2) + h)          # exponent of tau in ||u||_p (not p-th power)
leray_Lp = -(p - 3) / (2 * p)
margin = sp.simplify(constr_Lp - leray_Lp)
print("L^p (p > 3): construction exponent", sp.simplify(constr_Lp), "; Leray exponent", sp.simplify(leray_Lp),
      "; margin exponent", sp.factor(margin), "  (= -h(1 + 1/p))")
print("   p = infinity limit of the margin:", sp.limit(margin, p, sp.oo), " (the Type II factor tau^-h)")
print("   p = 3: construction exponent", sp.simplify(constr_Lp.subs(p, 3)), " (critical norm; Seregin 2012 needs only divergence)")
print("enstrophy: construction exponent -1/2-3h vs Leray -1/2: margin tau^(-3h)")
print("L^2_t L^inf_x: integrand tau^(-1-2h) vs Leray's tau^(-1): margin tau^(-2h); divergence is automatic for any singular")
print("   solution because ||u(t)||_inf >= c (T-t)^(-1/2) already gives a divergent integral")
print("vorticity sup: tau^(-1-h) vs the scaling rate tau^(-1): margin tau^(-h); int ||omega||_inf = infinity is again automatic")
ph = (3 - 2 * h) / (1 + 2 * h)
print("L^p norms blow up for p > p_h =", ph, "; for p_h < p < 3 (subcritical, not required by any criterion):",
      "e.g. h = 1/200: p_h =", ph.subs(h, sp.Rational(1, 200)), "=", float(ph.subs(h, sp.Rational(1, 200))))
