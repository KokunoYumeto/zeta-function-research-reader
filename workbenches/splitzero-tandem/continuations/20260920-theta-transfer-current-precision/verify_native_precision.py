"""Exact finite checks of NATIVE_MOMENT_PRECISION.tex.

The rational measures here are TEST INSTANCES ONLY, never replacements for
the native arithmetic measures. The native density and moment caps are proved
in the TeX from the original envelope. No native numerical value is invented.
Checks remain active with python -O; this script deliberately uses no assert.
"""
from itertools import product
from math import isqrt
import sympy as s

Q = s.Rational
I = s.I
counts = {"identity": 0, "psd": 0, "scalar": 0, "negative": 0}


def eq(left, right, name):
    value = left - right
    if isinstance(value, s.MatrixBase):
        good = all(s.simplify(x) == 0 for x in value)
    else:
        good = s.simplify(value) == 0
    if not good:
        raise RuntimeError((name, value))
    counts["identity"] += 1


def le(left, right, name):
    value = s.simplify(right - left)
    if not (value.is_real and value >= 0):
        raise RuntimeError((name, left, right))
    counts["scalar"] += 1


def psd(matrix, name):
    z = matrix.applyfunc(s.simplify)
    if z != z.H:
        raise RuntimeError((name, "not Hermitian"))
    # Exact Schur elimination, valid also for positive semidefinite matrices.
    for k in range(z.rows):
        pivot = s.simplify(z[k, k])
        if not (pivot.is_real and pivot >= 0):
            raise RuntimeError((name, "negative pivot", k, pivot))
        if pivot == 0:
            if any(s.simplify(z[j, k]) != 0 for j in range(k + 1, z.rows)):
                raise RuntimeError((name, "zero pivot with nonzero column"))
        else:
            for i in range(k + 1, z.rows):
                for j in range(k + 1, z.cols):
                    z[i, j] = s.cancel(z[i, j] - z[i, k]*z[k, j]/pivot)
    counts["psd"] += 1


def interval_gram(t):
    return s.Matrix(t+1, t+1,
                    lambda i, j: Q(2**(i+j+1)-1, i+j+1))


def floor_g(t):
    J = interval_gram(t)
    return s.factor(J.det()/s.trace(J)**t)


def hankel(mu, t, shift=0):
    return s.Matrix(t+1, t+1, lambda i, j: mu[i+j+shift])


def weighted(mu, t, coefficients):
    return s.Matrix(t+1, t+1, lambda i, j:
                    sum(c*mu[i+j+l] for l, c in enumerate(coefficients)))


def test_moments(parity, scale=Q(1), degree=24):
    # scale*x^parity*(1_[1,2] dx + 2 delta_3 + 3 delta_5).
    return [scale*(Q(2**(j+parity+1)-1, j+parity+1)
                   + 2*3**(j+parity) + 3*5**(j+parity))
            for j in range(degree+1)]


def midpoint(mu, eps):
    return [m + eps*Q((-1)**j, j+1) for j, m in enumerate(mu)]


def ceil_sqrt(n):
    z = isqrt(n)
    return z if z*z == n else z+1


def quadratic_error(mu, hat, t, n, shift, coeffs, eps, density):
    d, e = t+1, n+1
    W, Wh = weighted(mu, t, coeffs), weighted(hat, t, coeffs)
    C = s.Matrix(d, e, lambda i, j: mu[i+j+shift])
    Ch = s.Matrix(d, e, lambda i, j: hat[i+j+shift])
    ell = density*floor_g(t)*sum(coeffs)
    cw = d*sum(coeffs)
    # Rational upper bounds for the displayed Frobenius/square-root constants.
    cc = Q(ceil_sqrt(d*e))
    uc = sum(C)
    P = Q(4, 3)*(cw*uc**2/ell**2 + (2*uc*cc+cc**2)/ell)
    F, Fh = C.H*W.inv()*C, Ch.H*Wh.inv()*Ch
    error = P*eps
    psd(error*s.eye(e) - (F-Fh), "quadratic upper norm")
    psd(error*s.eye(e) + (F-Fh), "quadratic lower norm")
    Ffloor = (density*floor_g(n))**2/s.trace(W)
    psd(F-Ffloor*s.eye(e), "quadratic positive floor")
    return F, Fh, error


def check_interval_grams():
    expected = [Q(1), Q(1, 40), Q(5, 981552)]
    for t in range(7):
        J = interval_gram(t)
        determinant = s.prod(Q(s.factorial(j)**4,
                               s.factorial(2*j)*s.factorial(2*j+1))
                             for j in range(t+1))
        eq(J.det(), determinant, "interval determinant product")
        B = s.Matrix(t+1, t+1,
                     lambda i, j: s.binomial(j, i) if i <= j else 0)
        Hil = s.Matrix(t+1, t+1, lambda i, j: Q(1, i+j+1))
        eq(J, B.T*Hil*B, "exact unipotent determinant morphism")
        g = floor_g(t)
        psd(J-g*s.eye(t+1), "rational interval spectral floor")
        le(Q(3, 8)**t*Q(1, (2*t+1)**(t+1))*Q(1, 4**(2*t*t+t)),
           g, "explicit binary-size floor")
        if t < len(expected):
            eq(g, expected[t], "small evaluated floor")
        print(f"g_{t} = {g}")


def check_weighted_hankels():
    for parity, scale, t in product((0, 1), (Q(1), Q(3, 5)), range(4)):
        mu = test_moments(parity, scale)
        density, d = scale, t+1
        eps = density*floor_g(t)/(128*d)
        hat = midpoint(mu, eps)
        families = [[1], [0, 1], [0, 0, 1], [0, 0, 0, 1]]
        for a in (Q(4), Q(16)):
            b = Q(9)
            families += [[a, 1], [0, a, 1], [0, a*b, a+b, 1]]
        for coeffs in families:
            W, Wh = weighted(mu, t, coeffs), weighted(hat, t, coeffs)
            ell = density*floor_g(t)*sum(coeffs)
            delta = d*sum(coeffs)*eps
            eye = s.eye(d)
            psd(W-ell*eye, "native-style weighted lower floor")
            psd(s.trace(W)*eye-W, "trace upper floor")
            psd(delta*eye-(W-Wh), "entry errors imply norm upper")
            psd(delta*eye+(W-Wh), "entry errors imply norm lower")
            psd(Wh-delta*eye-(ell-2*delta)*eye, "outward positive margin")
            psd(W.inv()-(Wh+delta*eye).inv(), "outward inverse lower")
            psd((Wh-delta*eye).inv()-W.inv(), "outward inverse upper")
            eta = delta/(ell*(ell-delta))
            psd(eta*eye-(W.inv()-Wh.inv()), "inverse perturbation upper")
            psd(eta*eye+(W.inv()-Wh.inv()), "inverse perturbation lower")
        for n, shift, coeffs in [(t, 0, [4, 1]),
                                  (max(0, t-1), 1, [0, 4, 1]),
                                  (max(0, t-1), 1, [0, 36, 13, 1])]:
            quadratic_error(mu, hat, t, n, shift, coeffs, eps, density)
        # Parity remains an exact shift; masses are not one.
        if parity == 0:
            next_mu = test_moments(1, scale)
            eq(s.Matrix(mu[1:]), s.Matrix(next_mu[:-1]), "exact parity shift")
            eq(mu[0], 6*scale, "original test mass retained")


def check_radau():
    for parity, r, a in product((0, 1), range(1, 5), (Q(4), Q(16))):
        n = min(1, r-1)
        mu = test_moments(parity, Q(3, 5))
        H, D = hankel(mu, r-1), hankel(mu, r-1, 1)
        C = H[:, :n+1]
        e = s.eye(r)[:, r-1]
        kap = 1/(e.T*D.inv()*e)[0]
        Dt = D-kap*e*e.T
        h = Q(3, 5)*floor_g(r-1)
        uh, ud, uk = s.trace(H), s.trace(D), D[r-1, r-1]
        WG, WR = D+a*H, Dt+a*H
        psd(Dt, "deflated semidefinite matrix")
        eq(Dt.det(), 0, "deflation exactly singular")
        psd(WR-a*h*s.eye(r), "Radau quantitative lower margin")
        denominator = 1-kap*(e.T*WG.inv()*e)[0]
        le(a*h/(ud+a*uh), denominator, "Schur denominator lower bound")
        cr = r*(1+a)+r*uk/h
        eps = min(Q(1), h/(128*r), a*h/(128*cr))
        hat = midpoint(mu, eps)
        Hh, Dh = hankel(hat, r-1), hankel(hat, r-1, 1)
        kh = 1/(e.T*Dh.inv()*e)[0]
        le(abs(kh-kap), r*uk*eps/h, "kappa same-fibre perturbation")
        WRh = Dh+a*Hh-kh*e*e.T
        rad = cr*eps
        psd(rad*s.eye(r)-(WR-WRh), "Radau error upper")
        psd(rad*s.eye(r)+(WR-WRh), "Radau error lower")
        psd(WR.inv()-(WRh+rad*s.eye(r)).inv(), "Radau inverse lower")
        psd((WRh-rad*s.eye(r)).inv()-WR.inv(), "Radau inverse upper")
        Fm, Fp = C.T*WG.inv()*C, C.T*WR.inv()*C
        z = s.Matrix([(-a)**j for j in range(n+1)])
        gamma = (Fp-Fm)[0, 0]
        eq(Fp-Fm, gamma*z*z.T, "exact rank-one gap")
        if n == 1:
            u, v = s.Matrix([1+I, 2-I]), s.Matrix([3-2*I, -1+I])
            eq((u.H*(Fp-Fm)*v)[0],
               gamma*(u.H*z)[0]*(z.T*v)[0], "complex rank-one cross phase")
            # Reversing the complex conjugation is genuinely wrong.
            wrong = gamma*(u.T*z)[0]*(z.T*v)[0]
            if s.simplify((u.H*(Fp-Fm)*v)[0]-wrong) == 0:
                raise RuntimeError("negative phase test unexpectedly passed")
            counts["negative"] += 1


def quotient(A, D):
    return (A*D.inv()*A.H).inv()


def check_receivers():
    N, c = 4, Q(9, 2)
    mu0, mu1 = test_moments(0), test_moments(1)
    H = s.diag(hankel(mu0, 2), hankel(mu1, 1))
    h = min(floor_g(2), floor_g(1))
    eps = h/(128*3)
    Hhat = s.diag(hankel(midpoint(mu0, eps), 2),
                  hankel(midpoint(mu1, eps), 1))
    delta = 3*eps
    Hlo, Hhi = Hhat-delta*s.eye(5), Hhat+delta*s.eye(5)
    theta = delta/h
    factor = 1/(1-2*theta)
    psd(H-Hlo, "direct source lower")
    psd(Hhi-H, "direct source upper")
    psd(factor*Hlo-Hhi, "explicit direct relative factor")
    T = s.Matrix(5, 5, lambda i, j:
                 s.binomial(j, i)*c**(j-i)*I**i if i <= j else 0)
    Ti = s.Matrix(5, 5, lambda i, j:
                  s.binomial(j, i)*(-c)**(j-i)*I**(-j) if i <= j else 0)
    Pi = s.zeros(5)
    for i, j in enumerate([0, 2, 4, 1, 3]):
        Pi[i, j] = 1
    L = Pi*T
    eq(T*Ti, s.eye(5), "original triangular inverse")
    eq(T.det(), I**(N*(N+1)//2), "exact determinant phase")
    As = s.Matrix([[1, I, 2-I, 0, 1], [0, 1, -I, 1+I, 2]])
    A = As*L.inv()
    Q0, Qlo, Qhi = quotient(A, H), quotient(A, Hlo), quotient(A, Hhi)
    eq(Q0, quotient(As, L.H*H*L), "original S quotient congruence")
    for M, name in [(Q0-Qlo, "observed lower"),
                    (Qhi-Q0, "observed upper"),
                    (factor*Qlo-Qhi, "same-fibre relative factor")]:
        psd(M, name)
    AA = A*A.H
    af = AA.det()/s.trace(AA)
    bf = s.trace(AA)
    psd(AA-af*s.eye(2), "actual-map determinant trace floor")
    psd(A*H.inv()*A.H-af/s.trace(H)*s.eye(2), "observed inverse lower margin")
    psd(Q0-h/bf*s.eye(2), "observed metric lower margin")
    u, v, w = s.Matrix([1+I, 2]), s.Matrix([2-I, -1+I]), s.Matrix([I, 1-I])
    U = s.Matrix.hstack(u, v, w)
    E, gap = Q0-Qlo, Qhi-Qlo
    psd(U.H*E*U, "entire joint observed remainder")
    psd(U.H*(gap-E)*U, "entire joint remainder upper")
    joint = U.H*E*U
    aa, bb, cc = joint[0, 0], joint[1, 1], joint[2, 2]
    z12, z13, z23 = joint[0, 1], joint[0, 2], joint[1, 2]
    det_expanded = (aa*bb*cc + 2*s.re(z12*z23*s.conjugate(z13))
                    - aa*z23*s.conjugate(z23)
                    - bb*z13*s.conjugate(z13)
                    - cc*z12*s.conjugate(z12))
    eq(joint.det(), det_expanded, "full three-vector complex determinant")
    cross = (u.H*E*v)[0]
    le(s.expand_complex(cross*s.conjugate(cross)),
       (u.H*gap*u)[0]*(v.H*gap*v)[0], "complex cross Cauchy bound")
    b1, b2 = (u.H*Q0*w)[0], (v.H*Q0*w)[0]
    m1, m2 = (u.H*Qlo*w)[0], (v.H*Qlo*w)[0]
    e1, e2 = b1-m1, b2-m2
    eq(s.conjugate(b1)*b2,
       s.conjugate(m1)*m2+s.conjugate(m1)*e2+s.conjugate(e1)*m2+s.conjugate(e1)*e2,
       "full signed current expansion")
    conductor = s.Matrix([[1+I, 2-I]])
    T0 = quotient(conductor, Q0)
    eq(T0, quotient(conductor*A, H), "unchanged conductor composition")
    Tlo, Thi = quotient(conductor, Qlo), quotient(conductor, Qhi)
    psd(T0-Tlo, "conductor full-fibre lower")
    psd(Thi-T0, "conductor full-fibre upper")
    psd(factor*Tlo-Thi, "conductor relative factor")
    # Every original source and conductor kernel is retained by the minima.
    zmin = H.inv()*A.H*Q0*u
    eq(A*zmin, u, "minimizer in exact original observation fibre")
    for kernel in A.nullspace():
        eq(kernel.H*H*zmin, s.zeros(1, 1), "full kernel orthogonality")
    # General four-sign statement is equivalent to rational ratio monotonicity.
    for values in product((Q(0), Q(1, 3), Q(1)), repeat=4):
        qs = [Qlo+x*(Qhi-Qlo) for x in values]
        actual = qs[0].det()*qs[1].det()/(qs[2].det()*qs[3].det())
        lower = Qlo.det()**2/Qhi.det()**2
        upper = Qhi.det()**2/Qlo.det()**2
        le(lower, actual, "four-endpoint lower signed ratio")
        le(actual, upper, "four-endpoint upper signed ratio")
    # Wrongly using all four lower determinants is not a lower ratio bound.
    wrong_lower = Q(1)
    actual = Qlo.det()**2/Qhi.det()**2
    if not actual < wrong_lower:
        raise RuntimeError("negative endpoint-sign test did not fail")
    counts["negative"] += 1


def check_scalar_budgets_and_failures():
    # Exact multinomial with nonzero mass and exact evenness.
    eta = [Q(3), Q(0), Q(7), Q(0), Q(11), Q(0), Q(19)]
    k, R = 3, 3
    cap = max(eta)
    eps = Q(1, 1000)
    tau = eps/(k**(2*R+1)*(cap+1)**(k-1))
    etah = [x+(tau*Q((-1)**j, j+1) if j % 2 == 0 else 0)
            for j, x in enumerate(eta)]

    def convmoment(inputs, degree):
        result = 0
        for exps in product(range(degree+1), repeat=k):
            if sum(exps) == degree:
                result += s.factorial(degree)*s.prod(
                    inputs[e]/s.factorial(e) for e in exps)
        return result

    for degree in range(0, 2*R+1, 2):
        le(abs(convmoment(eta, degree)-convmoment(etah, degree)), eps,
           "onefold explicit absolute moment budget")
    eq(convmoment(eta, 0), eta[0]**k, "convolution mass not normalized")
    # Midpoint positivity without a certified moment floor can fail.
    J = interval_gram(1)
    bad = s.Matrix([[J[0, 0], J[0, 1]+1], [J[1, 0]+1, J[1, 1]]])
    if not bad.det() < 0:
        raise RuntimeError("negative uncertified midpoint example not indefinite")
    counts["negative"] += 1
    # Residual certificate is checked as an exact norm-enclosing matrix bound.
    W = s.Matrix([[3, 1], [1, 2]])
    R0 = Q(99, 100)*W.inv()
    rr = Q(1, 100)
    eq(s.eye(2)-W*R0, rr*s.eye(2), "inverse residual identity")
    capR = s.trace(R0)
    radius = capR*rr/(1-rr)
    psd(radius*s.eye(2)-(W.inv()-R0), "certified approximate inverse upper")
    psd(radius*s.eye(2)+(W.inv()-R0), "certified approximate inverse lower")
    # A wrong scalar gamma can never be repaired by silently changing phases.
    z = s.Matrix([1, -4])
    u, v = s.Matrix([1+I, 1]), s.Matrix([I, 2-I])
    cross = (u.H*z*z.T*v)[0]
    if s.im(cross) == 0:
        raise RuntimeError("negative real-phase example unexpectedly real")
    counts["negative"] += 1


if __name__ == "__main__":
    check_interval_grams()
    check_weighted_hankels()
    check_radau()
    check_receivers()
    check_scalar_budgets_and_failures()
    print("PASS", counts, "total", sum(counts.values()))
    print("Native arithmetic moments were not assigned test-measure values.")
