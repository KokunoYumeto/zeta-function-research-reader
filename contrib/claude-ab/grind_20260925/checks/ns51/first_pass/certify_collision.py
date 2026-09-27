"""Interval (Arb, python-flint) certificate for the Rindler pole collision of the vacuum-hydrodynamics
continuation (manuscripts/RESEARCH.md (29)-(33); README L145-152, which says the location is
"not interval certified").

F(alpha, q) := I'_alpha(q) = (I_{alpha-1}(q) + I_{alpha+1}(q))/2   (derivative in the argument q).
Claim to certify: there is a real point (alpha*, q*) near (alpha_c, q_c) = (-0.5697140809723..., 0.7784728009903...)
with F = 0 and dF/dalpha = 0 (a multiple zero in alpha: two real hydrodynamic-branch zeros collide), and
F_q > 0, F_alphaalpha > 0 there (so the zero is exactly double and splits as a square root, (33)).

Method (existence; only enclosures of F are needed):
  I = [a0 - da, a0 + da], J = [q0 - dq, q0 + dq].
  (i)   F > 0 on {a0 - da, a0 + da} x J;
  (ii)  F(a0, q0 - dq) < 0;
  (iii) F > 0 on I x {q0 + dq}.
  g(q) = min_{alpha in I} F(alpha, q) is continuous, g(q0 - dq) < 0 < g(q0 + dq); at a zero q* of g the minimiser
  alpha* is interior by (i), hence F(alpha*, q*) = 0 and F_alpha(alpha*, q*) = 0.
Nondegeneracy on the whole box: F_q = I''_alpha(q) = (1 + alpha^2/q^2) I_alpha - I'_alpha/q (Bessel ODE) is enclosed
directly; F_alphaalpha is enclosed by a second divided difference with step h plus a Cauchy-estimate remainder
|E| <= (h^2/12) * 4! * M / (rho - r_I - h)^4, where M bounds |F(., q)| on the complex circle |alpha - a0| = rho
(complex Arb evaluation on 256 arcs).
"""
from flint import arb, acb, ctx
import math

ctx.prec = 256
a0 = arb("-0.569714080972361784438457668663")
q0 = arb("0.778472800990330076180356446189")
dq = arb("1e-20")
da = arb("1.5e-10")


def F(a, q):
    return (q.bessel_i(a - 1) + q.bessel_i(a + 1))/2


def iv(lo, hi):
    """arb ball enclosing [lo, hi]"""
    mid = (lo + hi)/2
    rad = (hi - lo)/2
    return arb(mid, rad.upper())


ok_all = True
out = []

# (i) endpoints of I, q over J (subdivided)
nq = 16
okc = True
worst = None
for side in (-1, 1):
    a = a0 + side*da
    for k in range(nq):
        qlo = q0 - dq + 2*dq*k/nq
        qhi = q0 - dq + 2*dq*(k + 1)/nq
        val = F(a, iv(qlo, qhi))
        if not (val > 0):
            okc = False
        worst = val if worst is None else (val if val.lower() < worst.lower() else worst)
out.append(("(i) F > 0 on the alpha-endpoints of I for all q in J (16 q-cells per side); smallest enclosure %s" % worst.str(5), okc))
# (ii)
v2 = F(a0, q0 - dq)
out.append(("(ii) F(a0, q0 - dq) < 0: %s" % v2.str(5), bool(v2 < 0)))
# nondegeneracy on the whole box B = I x J
A = iv(a0 - da, a0 + da)
Q = iv(q0 - dq, q0 + dq)
Iv = Q.bessel_i(A)
Ipv = F(A, Q)
Fq = (1 + A*A/(Q*Q))*Iv - Ipv/Q
out.append(("F_q = I''_alpha(q) > 0 on the box: %s" % Fq.str(12), bool(Fq > 0)))
# F_alphaalpha by a divided difference with Cauchy remainder
h = arb("1e-3")
D2 = (F(A + h, Q) - 2*F(A, Q) + F(A - h, Q))/(h*h)
rho = arb("0.05")
M = arb(0)
narc = 256
for k in range(narc):
    th_lo = 2*math.pi*k/narc
    th_hi = 2*math.pi*(k + 1)/narc
    th = iv(arb(th_lo), arb(th_hi))
    z = acb(a0) + acb(rho*th.cos(), rho*th.sin())
    qz = acb(Q)
    val = (qz.bessel_i(z - 1) + qz.bessel_i(z + 1))/2
    M = arb(max(M.upper(), abs(val).upper()))
rI = da
remainder = (h*h/12)*24*M/((rho - rI - h)**4)
Faa = arb(D2.mid(), (D2.rad() + remainder.upper()))
out.append(("F_alphaalpha on the box in %s (divided difference %s, remainder <= %s, M = %s)" % (Faa.str(8), D2.str(8), remainder.str(3), M.str(3)), bool(Faa > 0)))
# (iii) F > 0 on I x {q0 + dq}: point enclosures at 101 equispaced alpha_k plus the linear-interpolation
# error bound |F - L| <= (max|F_alphaalpha|/8) s^2 on each cell (max from the box enclosure above).
npts = 100
s = 2*da/npts
vals = [F(a0 - da + s*k, q0 + dq) for k in range(npts + 1)]
M2 = Faa.upper()
interp = arb(M2)*s*s/8
lower = min(v.lower() for v in vals)
lb = arb(lower) - interp
out.append(("(iii) F > 0 on I x {q0 + dq}: min point enclosure lower end %s, interpolation error <= %s" % (arb(lower).str(5), interp.str(3)), bool(lb > 0)))
for name, ok in out:
    print(("PASS" if ok else "FAIL") + "  " + name)
    ok_all = ok_all and ok
print()
if ok_all:
    print("CERTIFIED: there is (alpha*, q*) with |alpha* - a0| < 1.5e-10 and |q* - q0| < 1e-20 at which F = F_alpha = 0,")
    print("with F_q > 0 and F_alphaalpha > 0 there (a nondegenerate double zero; the square-root split (33) follows).")
    print("Box: q* in [0.778472800990330076180356446189 +/- 1e-20], alpha* in [-0.569714080972361784438457668663 +/- 1.5e-10].")
else:
    print("NOT CERTIFIED")
