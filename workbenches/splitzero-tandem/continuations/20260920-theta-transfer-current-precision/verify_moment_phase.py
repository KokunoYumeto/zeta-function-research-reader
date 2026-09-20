"""Exact tests of the native moment-to-complex-product composition.

All finite examples are universal identity checks, NOT native arithmetic
values. No assert statements: the checks also run under python -O.
"""
from itertools import product
import sympy as s

Q, I = s.Rational, s.I
counts = {"identity": 0, "psd": 0, "inequality": 0, "negative": 0}


def eq(a, b, label):
    v = a-b
    good = (all(s.simplify(z) == 0 for z in v) if isinstance(v, s.MatrixBase)
            else s.simplify(v) == 0)
    if not good:
        raise RuntimeError((label, v))
    counts["identity"] += 1


def le(a, b, label):
    v = s.simplify(b-a)
    if not (v.is_real and v >= 0):
        raise RuntimeError((label, a, b))
    counts["inequality"] += 1


def psd(matrix, label):
    z = matrix.applyfunc(s.simplify)
    if z != z.H:
        raise RuntimeError((label, "not Hermitian"))
    for k in range(z.rows):
        p = s.simplify(z[k, k])
        if not (p.is_real and p >= 0):
            raise RuntimeError((label, "negative Schur pivot", p))
        if p == 0:
            if any(s.simplify(z[j, k]) != 0 for j in range(k+1, z.rows)):
                raise RuntimeError((label, "nonzero residual column"))
        else:
            for i in range(k+1, z.rows):
                for j in range(k+1, z.cols):
                    z[i, j] = s.cancel(z[i, j]-z[i, k]*z[k, j]/p)
    counts["psd"] += 1


def abs2(z):
    return s.simplify(z*s.conjugate(z))


def norm2(z, G):
    return s.simplify((z.H*G*z)[0])


def projection(G, frame):
    return frame*(frame.H*G*frame).inv()*frame.H*G


def pairings(G, P, A, x):
    a, b = P*x, (s.eye(x.rows)-P)*x
    return s.simplify((a.H*G*A*b)[0]), s.simplify((b.H*G*A*a)[0])


def scalar_checks():
    for theta, u, v in product((Q(1, 256), Q(1, 32), Q(1, 8), Q(1, 4)),
                              range(4), range(4)):
        kappa = 1/(1-2*theta)
        shift = theta/s.sqrt(1-2*theta)
        root = s.sqrt(1+shift**2)
        radius = shift*v*v+shift*u*v+shift**2*v*v+(kappa-1)*(u+shift*v)*root*v
        coefficient = theta*(4*s.sqrt(2)*u*v+(2+s.sqrt(2))*v*v)
        le(radius, coefficient, "full PD11 scalar coefficients")
        le(coefficient, 6*theta*(u*u+v*v), "strong scalar square bound")
        le(radius, 8*theta*v*(u+v), "proposed first constant")
        le(8*theta*v*(u+v), 12*theta*(u*u+v*v), "proposed second constant")
        le(6*theta+36*theta**2, 15*theta, "strong product constant")
        le(48*theta+576*theta**2, 192*theta, "proposed product constant")
        eq(6*(u*u+v*v)-4*s.sqrt(2)*u*v-(2+s.sqrt(2))*v*v,
           6*(u-s.sqrt(2)*v/3)**2+(Q(8, 3)-s.sqrt(2))*v*v,
           "exact scalar positive-square decomposition")
    for rootk in (Q(5, 4), Q(4, 3), Q(7, 5)):
        kap = rootk**2
        B = 2*kap/(kap+1)
        X = (kap-1)*rootk/(kap+1)
        D = (kap**2+1)/(kap+1)
        E = s.Matrix([[B, X], [X, D]])
        psd(E-s.eye(2), "sharp projection lower metric")
        psd(kap*s.eye(2)-E, "sharp projection upper metric")
        eq(X/B, (kap-1)/(2*rootk), "exact sharp projection displacement")
    # Dropping the metric-change term is false even with no projection change.
    A = s.Matrix([[0, 1], [1, 0]])
    x = s.Matrix([1, 1])
    P = s.diag(1, 0)
    z0, w0 = pairings(s.eye(2), P, A, x)
    z, w = pairings(2*s.eye(2), P, A, x)
    if z == z0 or w == w0:
        raise RuntimeError("negative omitted-metric test failed")
    counts["negative"] += 1


def moment(j):
    # Positive test measure 1_[1,2] dx + 2 delta_3, mass three.
    return Q(2**(j+1)-1, j+1)+2*3**j


def hankel(mu, parity):
    return s.Matrix(2, 2, lambda i, j: mu[i+j+parity])


def composition_checks():
    mu = [moment(j) for j in range(5)]
    H = s.diag(hankel(mu, 0), hankel(mu, 1))
    h, upper, dsrc = Q(1, 40), s.trace(H), 2
    psd(H-h*s.eye(4), "test source interval lower floor")
    psd(upper*s.eye(4)-H, "test source trace upper floor")
    eq(mu[0], 3, "test measure mass retained")
    maps = [s.Matrix([[1, I, 1-I, 0], [0, 1, I, 1+I]]),
            s.Matrix([[2-I, 0, 1, I], [1, 1+I, 0, 2]])]
    actions = [s.Matrix([[1+I, 2-I], [3+I, 4-I]]),
               s.Matrix([[0, -3-I], [1, Q(9, 2)]])]
    classes = [s.Matrix([2-I, 2+2*I]), s.Matrix([1, I]), s.zeros(2, 1)]
    K = s.Matrix([1, I])
    Lambda = s.Matrix([[I, -1]])
    eq(Lambda*K, s.zeros(1, 1), "same original-style fixed kernel")
    for theta, J in product((Q(1, 32), Q(1, 8), Q(1, 4)), maps):
        eps = theta*h/dsrc
        mh = [m+eps*Q((-1)**j, j+1) for j, m in enumerate(mu)]
        Hhat = s.diag(hankel(mh, 0), hankel(mh, 1))
        delta = dsrc*eps
        Hlo, Hhi = Hhat-delta*s.eye(4), Hhat+delta*s.eye(4)
        kappa = 1/(1-2*theta)
        for matrix, label in [(Hlo-h*s.eye(4)/2, "source positive midpoint margin"),
                               (H-Hlo, "source lower order"),
                               (Hhi-H, "source upper order"),
                               (kappa*Hlo-Hhi, "source relative order"),
                               (upper*s.eye(4)-Hlo, "stronger source upper order")]:
            psd(matrix, label)
        W = (J*J.H).inv()
        G0, G = (J*Hlo.inv()*J.H).inv(), (J*H.inv()*J.H).inv()
        for matrix, label in [(G0-h*W/2, "quotient lower W floor"),
                               (upper*W-G0, "stronger quotient upper W floor"),
                               (G-G0, "quotient native lower order"),
                               (kappa*G0-G, "quotient native relative order")]:
            psd(matrix, label)
        P0, P = projection(G0, K), projection(G, K)
        eq(P0*P0, P0, "midpoint projection idempotence")
        eq(P*P, P, "native projection idempotence")
        eq(G0*P0, P0.H*G0, "midpoint metric orthogonality")
        eq(G*P, P.H*G, "native metric orthogonality")
        for A, x in product(actions, classes):
            # Certified finite upper norm; actual original constants remain symbolic.
            B2 = s.simplify(s.trace(W.inv()*A.H*W*A))
            psd(B2*W-A.H*W*A, "literal-map W action norm cap")
            Mbar2 = 4*upper*B2/h
            C2 = s.simplify(Mbar2*upper**2*norm2(x, W)**2)
            psd(Mbar2*G0-A.H*G0*A, "proposed action norm comparison")
            a, b = P0*x, (s.eye(2)-P0)*x
            e = (P-P0)*x
            le(norm2(e, G0), theta**2/(1-2*theta)*norm2(b, G0),
               "sharp fixed-vector projection bound")
            z0, w0 = pairings(G0, P0, A, x)
            z, w = pairings(G, P, A, x)
            for midpoint in (z0, w0):
                le(abs2(midpoint), C2/4, "strong midpoint mixed-pairing cap")
            for difference in (z-z0, w-w0):
                le(abs2(difference), 36*C2*theta**2, "strong pairing radius")
                le(abs2(difference), 576*C2*theta**2, "proposed pairing radius")
            dz, dw = z-z0, w-w0
            err = s.conjugate(z)*w-s.conjugate(z0)*w0
            eq(err, s.conjugate(dz)*w0+s.conjugate(z0)*dw+s.conjugate(dz)*dw,
               "full complex three-term product error")
            le(abs2(err), (15*C2*theta)**2, "strong composed product tolerance")
            le(abs2(err), (192*C2*theta)**2, "proposed composed product tolerance")
            if x == K or x == s.zeros(2, 1):
                eq(s.Matrix([z, w, z0, w0]), s.zeros(4, 1), "zero-complement case")
            elif s.simplify(s.conjugate(z)*w-z*w) != 0:
                counts["negative"] += 1
            else:
                raise RuntimeError("negative missing-conjugation check unexpectedly equal")


if __name__ == "__main__":
    scalar_checks()
    composition_checks()
    print("PASS", counts, "total", sum(counts.values()))
    print("Both 192 and the stronger 15 use the same C; no native values assigned.")
