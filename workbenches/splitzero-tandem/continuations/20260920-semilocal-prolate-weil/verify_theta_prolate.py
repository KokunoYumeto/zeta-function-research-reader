"""Exact finite checks of PT1--16; samples are illustrative, not zeta-zero data.

The analytic proofs are in INDEPENDENT_CHECK.tex. These checks do not establish
an asymptotic estimate, a native zero location, or a strong-space assertion.
"""
import json
from itertools import product
import sympy as s

passed = []
negative = []


def equal(name, left, right=0):
    difference = s.simplify(s.expand_func(left - right))
    if difference != 0:
        raise AssertionError((name, difference))
    passed.append(name)


def unequal(name, left, right=0):
    difference = s.simplify(s.expand(left - right))
    if difference == 0:
        raise AssertionError((name, "deliberately incorrect identity passed"))
    negative.append(name)


x, t, z, sigma = s.symbols("x t z sigma", real=True)
v = s.symbols("v", positive=True)
p = s.pi
H = (p**2*x**4-s.Rational(3, 2)*p*x**2)*s.exp(-p*x**2)
h0 = 2**s.Rational(1, 4)*s.exp(-p*x**2)
h4 = (16*p**2*x**4-24*p*x**2+3)/(2*2**s.Rational(1, 4)*s.sqrt(3))*s.exp(-p*x**2)
c4 = s.sqrt(3)/2**s.Rational(11, 4)
c0 = -3/2**s.Rational(17, 4)
equal("literal Hermite coefficients", c4*h4+c0*h0, H)
equal("literal seed squared norm", c4**2+c0**2, 33/2**s.Rational(17, 2))
equal("Mellin Gamma recurrence coefficient",
      s.Rational(1, 2)*(sigma/2)*(sigma/2+1)-s.Rational(3, 4)*(sigma/2), sigma*(sigma-1)/8)

# Gaussian Fourier transform with the source's +2*pi*i*x*y kernel.
y = s.symbols("y", real=True)
Fgauss = s.exp(-p*y*y)
FH = p**2*s.diff(Fgauss, y, 4)/(2*p*s.I)**4-s.Rational(3, 2)*p*s.diff(Fgauss, y, 2)/(2*p*s.I)**2
equal("Fourier invariance of literal H", FH, H.subs(x, y))
equal("vanishing seed integral", FH.subs(y, 0), 0)

# Full Gaussian moments evaluate the squared norm independently of Hermite orthogonality.
Hpoly2 = s.Poly(s.expand((p**2*x**4-s.Rational(3, 2)*p*x**2)**2), x)
norm = 0
for (degree,), coefficient in Hpoly2.terms():
    norm += coefficient*s.gamma(s.Rational(degree+1, 2))/(2*p)**s.Rational(degree+1, 2)
equal("independent Gaussian squared norm", norm, 33/2**s.Rational(17, 2))

equal("factor-eight source seed", 2*(4*p**2*x**4-6*p*x**2)*s.exp(-p*x**2), 8*H)
equal("exact Mellin inverse coordinate", s.Rational(1, 2)-s.I*(s.I*(sigma-s.Rational(1, 2))), sigma)
equal("generator conjugacy on monomial",
      -x**s.Rational(1, 2)*x*s.diff(x**(-s.Rational(1, 2))*x**sigma, x),
      (s.Rational(1, 2)-sigma)*x**sigma)
equal("generator phase", -s.I*sigma, s.I*((s.Rational(1, 2)-sigma)-s.Rational(1, 2)))

B = (p*p*v**4+s.Rational(3, 2)*p*v**2)*s.exp(-p*v*v)
T = s.exp(-p*v*v)*(p*v**3/2+s.Rational(3, 2)*v)+s.Rational(3, 4)*s.erfc(s.sqrt(p)*v)
equal("complete Gaussian tail derivative", s.diff(T, v), -B)
equal("majorant derivative", s.diff(B, v),
      p*v*s.exp(-p*v*v)*(-2*p*p*v**4+p*v*v+3))
for nu in [s.Rational(-3, 2), s.Rational(-1, 2), 0, s.Rational(3, 2), s.Rational(7, 2), 4]:
    nu = s.sympify(nu)
    J = s.uppergamma((nu+1)/2, p*v*v)/(2*p**((nu+1)/2))
    equal(f"incomplete Gamma derivative nu={nu}", s.diff(J, v), -v**nu*s.exp(-p*v*v))

lam = s.symbols("lam", positive=True)
for alpha in [-s.Rational(2, 5), -s.Rational(1, 4), 0, s.Rational(1, 4), s.Rational(2, 5)]:
    expected = (lam**(s.Rational(1, 2)-alpha)-lam**(alpha-s.Rational(1, 2)))/(s.Rational(1, 2)-alpha)
    direct = s.integrate(v**(alpha-s.Rational(3, 2)), (v, 1/lam, lam))
    equal(f"interior exponent alpha={alpha}", direct, expected)
    equal(f"reflected interior exponent alpha={alpha}",
          s.integrate(v**(alpha-s.Rational(1, 2)), (v, 1/lam, lam)),
          (lam**(s.Rational(1, 2)+alpha)-lam**(-s.Rational(1, 2)-alpha))/(s.Rational(1, 2)+alpha))


def divided_jet(F, rho, j):
    return s.diff(F, t, j).subs(t, rho)/s.factorial(j)


# Each test divisor is artificial and illustrative; none is asserted to divide zeta.
packets = [
    [(s.Rational(1, 3)+2*s.I, 2), (s.Rational(2, 3)-2*s.I, 1)],
    [(s.Rational(2, 5)+s.I, 3), (s.Rational(3, 5)-s.I, 2)],
    [(s.Rational(1, 2), 4)],
    [(0, 1), (1, 2), (-2, 2)],
]
for packet_index, packet in enumerate(packets):
    packet = [(s.sympify(rho), multiplicity) for rho, multiplicity in packet]
    h = s.expand(s.prod((t-rho)**m for rho, m in packet))
    degree = s.degree(h, t)
    for offset in [0, 2, 4]:
        F = (1+2*s.I)*t**(degree+offset)+3*t**2+5*t-7
        interpolation = 0
        local = {}
        for rho, m in packet:
            b = s.prod((t-other)**multiplicity for other, multiplicity in packet if other != rho)
            coeff = [s.cancel(divided_jet(1/b, rho, j)) for j in range(m+4)]
            if offset == 0:
                others = [(other, multiplicity) for other, multiplicity in packet if other != rho]
                for a in range(m+4):
                    expanded_coefficient = (-1)**a*s.prod((rho-other)**(-multiplicity) for other, multiplicity in others)*sum(
                        s.prod(s.binomial(multiplicity+power-1, power)*(rho-other)**(-power)
                               for (other, multiplicity), power in zip(others, powers))
                        for powers in product(range(a+1), repeat=len(others)) if sum(powers) == a)
                    equal(f"root-difference inverse coefficient p{packet_index} root={rho} a{a}", coeff[a], expanded_coefficient)
            local[rho] = (b, coeff)
            truncated = sum(sum(coeff[j-r]*divided_jet(F, rho, r) for r in range(j+1))*(t-rho)**j for j in range(m))
            interpolation += b*truncated
        interpolation = s.Poly(s.expand(interpolation), t).as_expr()
        expected = s.rem(F, h, t)
        equal(f"Hermite polynomial p{packet_index} o{offset}", interpolation, expected)
        quotient, rem = s.div(F-interpolation, h, t)
        equal(f"divisibility p{packet_index} o{offset}", rem, 0)
        for root_index, (rho, m) in enumerate(packet):
            b, coeff = local[rho]
            for j in range(m):
                equal(f"preserved jet p{packet_index} o{offset} r{root_index} j{j}",
                      divided_jet(interpolation, rho, j), divided_jet(F, rho, j))
            for ell in range(m):
                exact = sum(coeff[j]*(divided_jet(F, rho, m+ell-j)-divided_jet(interpolation, rho, m+ell-j)) for j in range(ell+1))
                equal(f"divided quotient jet p{packet_index} o{offset} r{root_index} l{ell}",
                      divided_jet(quotient, rho, ell), exact)
                expanded = sum(coeff[a]*divided_jet(F, rho, m+ell-a) for a in range(m+ell+1))
                for other, multiplicity in packet:
                    if other == rho:
                        continue
                    other_coeff = local[other][1]
                    for j in range(multiplicity):
                        cj = sum(other_coeff[a]*divided_jet(F, other, j-a) for a in range(j+1))
                        expanded -= (-1)**ell*cj*s.binomial(multiplicity-j+ell-1, ell)*(rho-other)**(-(multiplicity-j+ell))
                equal(f"expanded cross-root quotient jet p{packet_index} o{offset} r{root_index} l{ell}",
                      divided_jet(quotient, rho, ell), expanded)
        equal(f"divisor unit p{packet_index} o{offset}", s.div(h*(t+1), h, t)[0], t+1)

# Negative controls reject exactly the tempting changes that would lose data.
unequal("reject Xi in place of Xi/4 at s=2", p/24, p/6)
unequal("reject missing source factor-eight", 8*H, H)
unequal("reject missing squared norm factor64", s.Rational(1, 64), 1)
unequal("reject reversed inverse-coordinate phase before symmetry", s.Rational(1, 2)-s.I*(-s.I*(sigma-s.Rational(1, 2))), sigma)
unequal("reject incomplete erfc coefficient", s.diff(T-s.Rational(3, 4)*s.erfc(s.sqrt(p)*v), v), -B)
unequal("reject zero quotient jet inferred from zero lower numerator jets", s.diff(t**3, t, 3).subs(t, 0)/s.factorial(3), 0)

print(json.dumps({"status": "PASS", "exact_identities": len(passed),
                  "deliberate_failure_controls": len(negative),
                  "sample_scope": "Artificial exact polynomial packets; not native zeta-zero data.",
                  "checks": passed, "negative_controls": negative}, indent=2))
