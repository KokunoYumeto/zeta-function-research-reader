"""Exact algebra checks for NATIVE_PROLATE_LIE_DEFECT.tex.

All finite test data below are explicitly artificial algebra data, not sampled
zeta zeros and not numerical evidence for a native zero-discrepancy assertion.
Run with Python 3 and SymPy. No files or network resources are read or written.
"""
import itertools
import sympy as s

I = s.I
checks = 0


def exact(left, right=0, label=""):
    global checks
    if isinstance(left, s.MatrixBase) or isinstance(right, s.MatrixBase):
        left, right = s.Matrix(left), s.Matrix(right)
        assert left.shape == right.shape, (label, left.shape, right.shape)
        for row in range(left.rows):
            for col in range(left.cols):
                exact(left[row, col], right[row, col], f"{label}[{row},{col}]")
        return
    difference = s.simplify(s.expand(left - right))
    assert difference == 0, (label, difference)
    checks += 1


def comm(a, b):
    return a * b - b * a


def anti(a, b):
    return a * b + b * a


def jacobi(edges, size):
    result = s.zeros(size)
    for n in range(size - 1):
        result[n, n + 1] = result[n + 1, n] = edges[n]
    return result


def generators(edges, size, c):
    j = jacobi(edges, size)
    n = s.diag(*range(size))
    k = n + c * s.eye(size)
    h = -I * j
    b = comm(j, n) / (2 * I)
    ep, em = I * (k + b) / 2, I * (-k + b) / 2
    d = s.diag(*[
        (edges[r] ** 2 if r < size - 1 else 0)
        - (edges[r - 1] ** 2 if r else 0)
        for r in range(size)
    ])
    return j, n, k, h, b, ep, em, d - 2 * k


# Literal factors and every mixed/standard/quadratic bracket, fully symbolic.
a = s.symbols("a0:7", positive=True)
c = s.symbols("c", real=True)
j, n, k, h, b, ep, em, delta = generators(a, 5, c)
exact(comm(h, k), 2 * b, "HK")
exact(comm(h, b), 2 * k + delta, "HB")
exact(comm(k, b), -h / 2, "KB")
exact(comm(h, ep), 2 * ep + I * delta / 2, "HEplus")
exact(comm(h, em), -2 * em + I * delta / 2, "HEminus")
exact(comm(ep, em), h / 4, "literal third bracket")
exact(comm(k, ep), -I * h / 4, "KEplus")
exact(comm(k, em), -I * h / 4, "KEminus")
exact(comm(b, ep), I * h / 4, "BEplus")
exact(comm(b, em), -I * h / 4, "BEminus")
exact(comm(2 * ep, 2 * em), h, "standard third bracket")
exact(I * (2 * em - 2 * ep), 2 * k, "compact generator")
quad = h**2 + 8 * (ep * em + em * ep)
exact(quad, 4 * k**2 - j**2 - 4 * b**2, "quadratic identity")
exact(comm(quad, h), 4 * anti(b, delta), "QH")
exact(comm(quad, k), s.zeros(5), "QK")
exact(comm(quad, b), anti(h, delta), "QB")
exact(comm(quad, ep), I * anti(h, delta) / 2, "QEplus")
exact(comm(quad, em), I * anti(h, delta) / 2, "QEminus")
literal_cas = h**2 + 2 * (ep * em + em * ep)
exact(literal_cas, (quad + 3 * h**2) / 4, "literal Casimir")
exact(comm(literal_cas, k), s.Rational(3, 2) * anti(h, b), "noncentral C")

# Infinite expressions received at a finite cutoff retain the missing edge.
cut = 4
alpha = a[cut] ** 2
boundary = s.zeros(cut + 1)
boundary[cut, cut] = 1
full = generators(a, cut + 3, c)
jf, nf, kf, hf, bf, efp, efm, df = full
compress = lambda matrix: matrix[:cut + 1, :cut + 1]
exact(delta, compress(df) - alpha * boundary, "cutoff delta")
exact(compress(jf**2), j**2 + alpha * boundary, "cutoff square")
exact(compress(bf**2), b**2 + alpha * boundary / 4, "cutoff B square")
quad_full = hf**2 + 8 * (efp * efm + efm * efp)
exact(quad, compress(quad_full) + 2 * alpha * boundary, "cutoff Q")
t = s.symbols("t", real=True)
wf = -jf**2 + t * (nf + s.eye(cut + 3) / 4) - s.eye(cut + 3) / 4
w = -j**2 - alpha * boundary + t * (n + s.eye(5) / 4) - s.eye(5) / 4
exact(compress(wf), w, "cutoff prolate")
exact(s.trace(delta), -(cut + 1) * (cut + 2 * c), "finite trace")

# Exhaustive finite path checks, including paths crossing the cutoff.
path_edges = list(map(s.Integer, range(1, 11)))
jl = jacobi(path_edges, 4)
jbig = jacobi(path_edges, 11)
for power in range(7):
    fullpower, smallpower = jbig**power, jl**power
    for start in range(4):
        for end in range(4):
            total = 0
            for steps in itertools.product((-1, 1), repeat=power):
                pos = start
                maximum = pos
                weight = s.Integer(1)
                valid = True
                for step in steps:
                    nxt = pos + step
                    if nxt < 0:
                        valid = False
                        break
                    weight *= path_edges[min(pos, nxt)]
                    pos = nxt
                    maximum = max(maximum, pos)
                if valid and pos == end and maximum > 3:
                    total += weight
            exact(fullpower[end, start] - smallpower[end, start],
                  total, f"excursion {power}:{end},{start}")

# All-c recurrence: several c are witnesses against uniqueness of c=1/4.
r = s.symbols("r", integer=True, nonnegative=True)
exact((r + 1) * (r + 2 * c) - r * (r - 1 + 2 * c), 2 * (r + c),
      "all-c difference")
exact(4 * (r + c)**2 - 2 * ((r + 1) * (r + 2 * c)
      + r * (r - 1 + 2 * c)), 4 * c * (c - 1), "all-c Casimir")
for cv in [s.Rational(1, 4), s.Rational(3, 4), s.Integer(2)]:
    edges = [s.sqrt((j + 1) * (j + 2 * cv)) for j in range(7)]
    family = generators(edges, 7, cv)
    exact(family[-1][:6, :6], s.zeros(6), f"all-c {cv}")

# Hankel/Toda formulas on two exact finite-support measures. The second
# measure is not even, so the derivative checks do not only test tau'=0.
u = s.symbols("u", real=True)
for measure in [
    [(s.Integer(x), s.Integer(1 + abs(x))) for x in range(-5, 6)],
    [(s.Integer(x), s.Integer(7 + x)) for x in range(-5, 6)],
]:
    moment = lambda degree: sum(weight * x**degree for x, weight in measure)
    inner = lambda f, g: sum(weight * f.subs(u, x) * g.subs(u, x)
                             for x, weight in measure)
    polys, norms = [], []
    for degree in range(6):
        poly = u**degree
        for old, norm in zip(polys, norms):
            poly -= inner(poly, old) / norm * old
        poly = s.expand(poly)
        polys.append(poly)
        norms.append(inner(poly, poly))
    tau = [s.Integer(1)]
    for size in range(1, 7):
        tau.append(s.det(s.Matrix(size, size, lambda r, j: moment(r + j))))
    for degree in range(6):
        exact(norms[degree], tau[degree + 1] / tau[degree], "monic norm")
    for degree in range(5):
        exact(norms[degree + 1] / norms[degree],
              tau[degree + 2] * tau[degree] / tau[degree + 1]**2,
              "Hankel ratio")
    for size in range(1, 6):
        rows = list(range(size - 1)) + [size]
        first = s.det(s.Matrix(size, size,
                              lambda r, j: moment(rows[r] + j)))
        second = s.det(s.Matrix(size, size,
                               lambda r, j: moment(rows[r] + rows[j])))
        exact(tau[size] * second - first**2,
              tau[size + 1] * tau[size - 1], "Hankel Toda")

# Exact nonunit-mass polynomial data from the positive recurrence a_n=n+1.
# No claim that these are native zeta norms: these are formula stress tests.
mass = s.Integer(9)
s0 = s.Rational(3, 2)
S = s.symbols("S")
Q = [s.Integer(1), u]
for degree in range(1, 8):
    Q.append(s.expand(u * Q[-1] - degree**2 * Q[-2]))
omega = [mass * s.factorial(degree)**2 for degree in range(10)]
p = [s.expand(I**degree * poly.subs(u, (S - s0) / I))
     for degree, poly in enumerate(Q)]

def column(poly, var, size):
    return s.Matrix([s.expand(poly).coeff(var, r) for r in range(size)])

def native_matrix(degree):
    return s.Matrix.hstack(*[
        column(Q[n] / s.sqrt(omega[n]), u, degree + 1)
        for n in range(degree + 1)
    ])

def original_to_native(degree):
    tt = s.Matrix(degree + 1, degree + 1, lambda r, j:
                  s.binomial(j, r) * s0**(j-r) * I**r if r <= j else 0)
    return native_matrix(degree).inv() * tt

for degree in range(1, 7):
    exact((S - s0) * p[degree],
          p[degree + 1] - omega[degree] / omega[degree - 1] * p[degree - 1],
          "physical recurrence sign")
    dmat = original_to_native(degree)
    for j in range(degree + 1):
        exact(dmat * column(p[j], S, degree + 1),
              s.sqrt(omega[j]) * I**j * s.eye(degree + 1)[:, j],
              "full source phase coordinates")

def grading(poly):
    degree = s.degree(poly, S)
    if degree is s.S.NegativeInfinity:
        return s.Integer(0)
    basis = s.Matrix.hstack(*[column(p[j], S, degree + 1)
                             for j in range(degree + 1)])
    coeff = basis.inv() * column(poly, S, degree + 1)
    return s.expand(sum(j * coeff[j] * p[j] for j in range(degree + 1)))

chi = s.expand((S - (1 + I)) * (S - (2 - 2 * I)))
q = s.degree(chi, S)
rem = lambda poly: s.rem(poly, chi, S)
gamma = s.Matrix.hstack(*[column(p[j], S, q + 1)
                         for j in range(q + 1)]).inv() * column(chi, S, q + 1)
exact(rem(grading(chi)),
      sum((j - q) * gamma[j] * rem(p[j]) for j in range(q)),
      "first relation obstruction")
assert rem(grading(chi)) != 0
checks += 1
for qspecial in range(1, 6):
    special = p[qspecial]
    exact(s.rem(grading((S - s0) * special), special, S),
          2 * omega[qspecial] / omega[qspecial - 1] * p[qspecial - 1],
          "special relation obstruction")

L = 4
bcols = [column(rem(poly), S, q) for poly in p]
E = s.Matrix.hstack(*[I**(-j) * bcols[j] / s.sqrt(omega[j])
                      for j in range(L + 1)])
gram = E * E.conjugate().T
G = gram.inv()
R = E.conjugate().T * G
P = R * E
Z = s.eye(L + 1) - P
exact(E * R, s.eye(q), "onto and right inverse")
exact(P**2, P, "attained projection")
exact(P.conjugate().T, P, "Hermitian projection")
exact(R.conjugate().T * R, G, "attained norm")
edges = [s.Integer(j + 1) for j in range(8)]
j, n, k, h, b, ep, em, delta = generators(edges, L + 1, s.Rational(1, 4))
bar = lambda mat: s.simplify(E * mat * R)
for aa, bb in [(j, n), (h, ep), (ep, em), (j, b)]:
    exact(comm(bar(aa), bar(bb)),
          E * comm(aa, bb) * R - E * aa * Z * bb * R
          + E * bb * Z * aa * R, "compressed bracket")
boundary = s.zeros(L + 1)
boundary[L, L] = 1
t = s.Rational(7, 3)
w = -j**2 - edges[L]**2 * boundary + t * (n + s.eye(L + 1)/4) - s.eye(L + 1)/4
exact(bar(w), -bar(j)**2 + t * (bar(n) + s.eye(q)/4) - s.eye(q)/4
      - E*j*Z*j*R - edges[L]**2 * E*boundary*R, "two prolate corrections")
exact(G * E*j*Z*j*R, (Z*j*R).conjugate().T*(Z*j*R), "relation positivity")
exact(G * E*boundary*R, (boundary*R).conjugate().T*(boundary*R), "edge positivity")

def outer(left, right):
    return left * right.conjugate().T

expected_h, expected_b, expected_k, expected_w = [s.zeros(q) for _ in range(4)]
for degree in range(L + 1):
    expected_k += (degree + s.Rational(1, 4)) * outer(bcols[degree], bcols[degree]) / omega[degree]
    wn = -edges[degree]**2 - (edges[degree - 1]**2 if degree else 0) + t*(degree+s.Rational(1, 4))-s.Rational(1, 4)
    expected_w += wn * outer(bcols[degree], bcols[degree]) / omega[degree]
for degree in range(L):
    cross = outer(bcols[degree], bcols[degree + 1])
    expected_h += (cross - cross.conjugate().T) / omega[degree]
    expected_b += (cross + cross.conjugate().T) / (2 * omega[degree])
for degree in range(L - 1):
    cross = outer(bcols[degree], bcols[degree + 2])
    expected_w += (cross + cross.conjugate().T) / omega[degree]
exact(bar(h), expected_h * G, "explicit H phases")
exact(bar(b), expected_b * G, "explicit B phases")
exact(bar(k), expected_k * G, "explicit K phases")
exact(bar(w), expected_w * G, "explicit W phases")

Mu = s.Matrix.hstack(*[column(rem((S-s0)/I*S**r), S, q) for r in range(q)])
outgoing = I**(-(L+1)) * bcols[L+1] / s.sqrt(omega[L+1])
exact(bar(j), Mu - edges[L] * outgoing * s.eye(L+1)[L, :] * R,
      "algebraic multiplication and outgoing edge")
Ewide = s.Matrix.hstack(E, outgoing)
jrect = jacobi(edges, L+2)[:, :L+1]
exact(Ewide*jrect, Mu*E, "rectangular exact multiplication")
awide = jacobi(edges, L+3)**2
arect = awide[:, :L+1]
Ewider = s.Matrix.hstack(Ewide, I**(-(L+2))*bcols[L+2]/s.sqrt(omega[L+2]))
exact(Ewider*arect, (Ewider*arect*R)*E + Ewider*arect*Z,
      "general exact relation receiver")
wrect = -awide[:, :L+1]
for row in range(L+1):
    wrect[row, row] += t*(row+s.Rational(1, 4))-s.Rational(1, 4)
wfull = Ewider*wrect*R
exact(wfull, -Mu**2 + t*(bar(n)+s.eye(q)/4)-s.eye(q)/4,
      "full rectangular prolate receiver")
outgoing2 = (outer(bcols[L+1], bcols[L-1])/omega[L-1]
             + outer(bcols[L+2], bcols[L])/omega[L])*G
exact(bar(w), wfull-outgoing2, "full-compressed prolate bridge")
exact(bar(j), Mu+I/omega[L]*outer(bcols[L+1], bcols[L])*G,
      "outgoing multiplication fully expanded phase")
moment_j = jacobi(list(map(s.Integer, range(1, 12))), 12)
moments = [mass*(moment_j**r)[0, 0] for r in range(2*L+1)]
Hu = s.Matrix(L+1, L+1, lambda r, j: moments[r+j])
coefficient_native = native_matrix(L)
exact(coefficient_native.conjugate().T*Hu*coefficient_native,
      s.eye(L+1), "native full Gram")
TT = s.Matrix(L+1, L+1, lambda r, j:
              s.binomial(j, r)*s0**(j-r)*I**r if r <= j else 0)
DD = original_to_native(L)
exact(TT.conjugate().T*Hu*TT, DD.conjugate().T*DD,
      "original unscaled S Gram")

# Full repeated-root physical unit coefficients, independently expanded.
z = s.symbols("z")
roots = [(s.Integer(1)+I, 2), (s.Integer(2)-I, 3), (-I, 1)]
hh = s.prod((S-rho)**multiplicity for rho, multiplicity in roots)
ff = 3 + 2*S + S**2 + I*S**3
gg = s.expand(hh*ff)
units = {}
for rho, multiplicity in roots:
    other = [(sigma, mult) for sigma, mult in roots if sigma != rho]
    for order in range(multiplicity):
        received = 0
        for aorder in range(order+1):
            inverse_coefficient = 0
            for multi in itertools.product(range(order-aorder+1), repeat=len(other)):
                if sum(multi) != order-aorder:
                    continue
                inverse_coefficient += s.prod(
                    (-1)**ell*s.binomial(mult+ell-1, ell)/(rho-sigma)**(mult+ell)
                    for (sigma, mult), ell in zip(other, multi))
            received += s.diff(gg, S, multiplicity+aorder).subs(S, rho) \
                        / s.factorial(multiplicity+aorder)*inverse_coefficient
        direct = s.diff(ff, S, order).subs(S, rho)/s.factorial(order)
        exact(received, direct, "complete local unit coefficient")
        units[rho, order] = direct
rho1, m1 = roots[0]
rho2, m2 = roots[1]
z1, z2 = s.symbols("z1 z2")
testpoly = S**5+(1-I)*S**2+2
fulljet = s.expand(ff.subs(S, rho1+z1)*ff.subs(S, rho2+z2)
                  *testpoly.subs(S, rho1+rho2+z1+z2))
for j1 in range(m1):
    for j2 in range(m2):
        received = sum(
            units[rho1, j1-v1]*units[rho2, j2-v2]
            *s.diff(testpoly, S, v1+v2).subs(S, rho1+rho2)
            / (s.factorial(v1)*s.factorial(v2))
            for v1 in range(j1+1) for v2 in range(j2+1))
        exact(fulljet.coeff(z1, j1).coeff(z2, j2), received,
              "factorial-complete physical jet")
nil1 = s.Matrix([[0, 0], [1, 0]])
nil2 = s.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
nil = s.kronecker_product(nil1, s.eye(3)) + s.kronecker_product(s.eye(2), nil2)
exact(nil**4, s.zeros(6), "sum nilpotent upper order")
exact((nil**3)[5, 0], s.factorial(3)/(s.factorial(1)*s.factorial(2)),
      "sum nilpotent last nonzero coefficient")

# Pole residue factors in the analytic obstruction, for exact positive d.
for d in [s.Rational(1, 2), s.Integer(1), s.Rational(3, 2)]:
    density = mass*2**(2*d)/(4*s.pi*s.gamma(2*d)) \
              *s.gamma(d+I*z/2)*s.gamma(d-I*z/2)
    exact(s.residue(density, z, 2*I*d), -I*mass*2**(2*d-1)/s.pi,
          "nonremovable Gamma pole")

# Original interpolation-volume receiver with complex cross term retained.
for cutoff in range(q-1, 6):
    kk = sum((outer(bcols[j], bcols[j])/omega[j]
              for j in range(cutoff+1)), s.zeros(q))
    gg = kk.inv()
    xx, yy = bcols[cutoff], bcols[cutoff+1]
    aa = (xx.conjugate().T*gg*xx)[0]
    dd = (yy.conjugate().T*gg*yy)[0]
    zz = (xx.conjugate().T*gg*yy)[0]
    before = kk - outer(xx, xx)/omega[cutoff]
    after = kk + outer(yy, yy)/omega[cutoff+1]
    replaced = before + outer(yy, yy)/omega[cutoff+1]
    volume = (after.det()+before.det()-kk.det()-replaced.det())/kk.det()
    exact(volume, (aa*dd-zz*s.conjugate(zz))/(omega[cutoff]*omega[cutoff+1]),
          "full complex determinant ratio")
    exact(omega[cutoff+1]/omega[cutoff]*volume,
          (aa*dd-zz*s.conjugate(zz))/omega[cutoff]**2, "CV receiver")

print(f"PASS: {checks} exact scalar identities, including every matrix entry.")
print("Symbolic brackets, all-c examples, cutoff paths, Hankel Toda, original")
print("phases, relation non-descent, attained compression, and CV determinants.")
print("All example data are artificial; no zeta zero-location claim is tested.")
