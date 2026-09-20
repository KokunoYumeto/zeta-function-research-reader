"""Exact checks for COMPRESSION_AUDIT.md; no numerical tolerances."""
import argparse
import json
import sys

import sympy as s


COUNT = 0
I = s.I
M = s.Symbol("M", positive=True)
x = s.Symbol("x")
POLYS = [s.Integer(1), x, x**2 - s.Rational(1, 2)]
GAMMAS = [M, M / 2]


def simp(a):
    if isinstance(a, s.MatrixBase):
        return a.applyfunc(s.simplify)
    return s.simplify(a)


def eq(name, a, b):
    global COUNT
    difference = simp(a - b)
    zero = s.zeros(*difference.shape) if isinstance(difference, s.MatrixBase) else 0
    if difference != zero:
        raise RuntimeError(f"{name}: exact nonzero residual {difference}")
    COUNT += 1


def neq(name, a, b):
    global COUNT
    difference = simp(a - b)
    zero = s.zeros(*difference.shape) if isinstance(difference, s.MatrixBase) else 0
    if difference == zero:
        raise RuntimeError(f"{name}: expected a nonzero exact residual")
    COUNT += 1


def kernel(vectors, d=2):
    n = vectors[0].rows
    return sum(
        (vectors[j] * vectors[j].H / GAMMAS[j] for j in range(d)),
        s.zeros(n),
    )


def audit(y, c, v, label):
    n, r = v.shape
    w = v.H * v
    p = v * w.inv() * v.H
    q = s.eye(n) - p
    a = v.H * c * v
    b = v.H * y * v
    h = b * w.inv()
    ell = q * y.H * v
    g = q * c * v
    e = ell.H * g
    delta = e - e.H
    boundary = v.H * (y * c - c * y.H) * v
    eq(label + ": P self-adjoint", p, p.H)
    eq(label + ": P idempotent", p * p, p)
    eq(label + ": PV=V", p * v, v)
    eq(label + ": QV=0", q * v, s.zeros(n, r))
    eq(label + ": C self-adjoint", c, c.H)
    eq(label + ": E leakage pairing", e, v.H * y * q * c * v)
    eq(label + ": Delta skew-Hermitian", delta.H, -delta)
    eq(label + ": exact displacement", h * a - a * h.H, boundary - delta)
    return dict(W=w, P=p, Q=q, A=a, B=b, H=h, L=ell, G=g,
                E=e, Delta=delta, boundary=boundary)


def receiver(y, c, v, u, values, vectors, label):
    gram = u.H * u
    f = v.H * y * u
    t = u.H * c * v
    eq(label + ": orthogonal receiver", u.H * v, s.zeros(u.cols, v.cols))
    eq(label + ": receiver Q", u * gram.inv() * u.H, values["Q"])
    eq(label + ": receiver E", f * gram.inv() * t, values["E"])
    delta = f * gram.inv() * t - t.H * gram.inv() * f.H
    eq(label + ": receiver Delta", delta, values["Delta"])
    gd, gm = v.H * vectors[2], v.H * vectors[1]
    generators = s.Matrix.hstack(gd, gm, f, t.H)
    m = u.cols
    middle = s.zeros(2 + 2 * m)
    middle[0, 1] = 1 / GAMMAS[1]
    middle[1, 0] = -1 / GAMMAS[1]
    middle[2:2+m, 2+m:2+2*m] = -gram.inv()
    middle[2+m:2+2*m, 2:2+m] = gram.inv()
    eq(label + ": generator factorization", generators * middle * generators.H,
       values["H"] * values["A"] - values["A"] * values["H"].H)


def jets(p, nodes):
    return s.Matrix([s.diff(p, x, k).subs(x, node)
                     for node, multiplicity in nodes for k in range(multiplicity)])


def jet_matrix(nodes):
    blocks = []
    for node, multiplicity in nodes:
        block = node * s.eye(multiplicity)
        for k in range(1, multiplicity):
            block[k, k-1] = k
        blocks.append(block)
    return s.diag(*blocks)


def coeff(p, n):
    p = s.Poly(p, x)
    return s.Matrix([p.nth(j) for j in range(n)])


def main(negative):
    y = s.diag(0, I)
    vectors = [s.Matrix([p.subs(x, 0), p.subs(x, I)]) for p in POLYS]
    c = kernel(vectors)
    v = s.Matrix([1, I])
    values = audit(y, c, v, "nonreal Gamma fixture")
    eq("Gamma C", c, s.Matrix([[1, 1], [1, 3]]) / M)
    eq("Gamma full CD", y*c-c*y.H,
       (vectors[2]*vectors[1].H-vectors[1]*vectors[2].H)/GAMMAS[1])
    eq("Gamma W", values["W"], s.Matrix([[2]]))
    eq("Gamma A", values["A"], s.Matrix([[4/M]]))
    eq("Gamma H", values["H"], s.Matrix([[I/2]]))
    eq("Gamma compressed boundary", values["boundary"], s.Matrix([[6*I/M]]))
    eq("Gamma E", values["E"], s.Matrix([[(1+I)/M]]))
    eq("Gamma Delta", values["Delta"], s.Matrix([[2*I/M]]))
    eq("original scalar mass", values["Delta"].subs(M, s.sqrt(2*s.pi)),
       s.Matrix([[2*I/s.sqrt(2*s.pi)]]))
    neq("nonzero correction", values["Delta"], s.zeros(1))
    receiver(y, c, v, s.Matrix([I, 1]), values, vectors, "Gamma receiver")
    if negative == "drop-correction":
        eq("NEGATIVE CONTROL: omitted correction",
           values["H"]*values["A"]-values["A"]*values["H"].H,
           values["boundary"])
        raise RuntimeError("unreachable negative control")

    compressed_vectors = [v.H*f for f in vectors]
    rho = [v.H*y*values["Q"]*f for f in vectors[:2]]
    eq("CD19 degree-zero compressed recurrence",
       values["H"]*compressed_vectors[0], compressed_vectors[1]-rho[0])
    eq("CD19 degree-one compressed recurrence",
       values["H"]*compressed_vectors[1],
       compressed_vectors[2]+compressed_vectors[0]/2-rho[1])
    eq("CD19 correction sum", values["Delta"],
       sum(((rho[j]*compressed_vectors[j].H
             -compressed_vectors[j]*rho[j].H)/GAMMAS[j] for j in range(2)),
           s.zeros(1)))
    center = s.Symbol("c", real=True)
    physical_y = center*s.eye(2)+I*y
    physical_h = center*s.eye(1)+I*values["H"]
    h1, h2 = I*vectors[1], -vectors[2]
    eq("CD21 physical full displacement",
       physical_y*c+c*physical_y.H-2*center*c,
       (h2*h1.H+h1*h2.H)/GAMMAS[1])
    compressed_h1, compressed_h2 = v.H*h1, v.H*h2
    eq("CD22 physical compressed displacement",
       physical_h*values["A"]+values["A"]*physical_h.H-2*center*values["A"],
       (compressed_h2*compressed_h1.H+compressed_h1*compressed_h2.H)/GAMMAS[1]
       -I*values["Delta"])
    scale = s.Symbol("scale", positive=True)
    eq("mass covariance C", c.subs(M, scale*M), c/scale)
    eq("mass covariance correction", values["Delta"].subs(M, scale*M),
       values["Delta"]/scale)

    beta = s.Symbol("beta", positive=True)
    cb = s.Matrix([[1, 1], [1, 1+1/beta]]) / M
    fb2 = s.Matrix([-beta, -1-beta])
    eq("general beta boundary", y*cb-cb*y.H,
       (fb2*vectors[1].H-vectors[1]*fb2.H)/(M*beta))
    betaval = audit(y, cb, v, "general beta")
    eq("general beta correction", betaval["Delta"], s.Matrix([[I/(M*beta)]]))

    nodes = [0, I, 2]
    y3 = s.diag(*nodes)
    vectors3 = [s.Matrix([p.subs(x, node) for node in nodes]) for p in POLYS]
    c3 = kernel(vectors3)
    v3 = s.Matrix([[1, I], [I, 1], [1, 0]])
    val3 = audit(y3, c3, v3, "nonscalar frame")
    eq("nonscalar Gram", val3["W"], s.diag(3, 2))
    receiver(y3, c3, v3, s.Matrix([-1, -I, 2]), val3, vectors3,
             "nonscalar receiver")
    k = val3["W"].inv()*val3["B"]
    neq("operator placements differ", k, val3["H"])
    neq("reversed orientation fails", k*val3["A"]-val3["A"]*k.H,
        val3["boundary"]-val3["Delta"])
    if negative == "wrong-orientation":
        eq("NEGATIVE CONTROL: reversed placement", k*val3["A"]-val3["A"]*k.H,
           val3["boundary"]-val3["Delta"])
        raise RuntimeError("unreachable negative control")
    change = s.Matrix([[1, I], [0, 2]])
    changed = audit(y3, c3, v3*change, "frame covariance")
    eq("H dual covariance", changed["H"],
       change.H*val3["H"]*change.H.inv())
    eq("Delta congruence", changed["Delta"], change.H*val3["Delta"]*change)

    invariant = audit(y3, c3, s.eye(3)[:, :2], "diagonal invariant subspace")
    eq("diagonal invariant L", invariant["L"], s.zeros(3, 2))
    eq("diagonal invariant correction", invariant["Delta"], s.zeros(2))
    stable_c = audit(y3, s.eye(3), v3, "kernel stable subspace")
    eq("kernel stable G", stable_c["G"], s.zeros(3, 2))
    eq("kernel stable correction", stable_c["Delta"], s.zeros(2))

    j2 = jet_matrix([(I, 2)])
    fj2 = [jets(p, [(I, 2)]) for p in POLYS]
    cj2 = kernel(fj2)
    vj2 = s.Matrix([0, 1])
    jval = audit(j2, cj2, vj2, "Jordan invariant fixture")
    eq("Jordan invariance", j2*vj2, I*vj2)
    eq("Jordan full CD", j2*cj2-cj2*j2.H,
       (fj2[2]*fj2[1].H-fj2[1]*fj2[2].H)/GAMMAS[1])
    eq("Jordan correction", jval["Delta"], s.Matrix([[4*I/M]]))
    eq("Jordan compressed boundary", jval["boundary"], s.Matrix([[8*I/M]]))
    neq("Jordan adjoint invariance fails", jval["L"], s.zeros(2, 1))

    confluent_nodes = [(I, 3), (s.Integer(2), 1)]
    n = sum(multiplicity for _, multiplicity in confluent_nodes)
    j = jet_matrix(confluent_nodes)
    fj = [jets(p, confluent_nodes) for p in POLYS]
    cj = kernel(fj)
    vj = s.Matrix([[1, I], [I, 1], [1, 0], [0, 2]])
    alljet = audit(j, cj, vj, "all-jet frame")
    eq("all-jet CD", j*cj-cj*j.H,
       (fj[2]*fj[1].H-fj[1]*fj[2].H)/GAMMAS[1])
    fac = s.diag(*[s.factorial(k) for _, mult in confluent_nodes
                   for k in range(mult)])
    jdiv = fac.inv()*j*fac
    eq("literal order-two subdiagonal", j[2, 1], s.Integer(2))
    eq("divided order-two subdiagonal", jdiv[2, 1], s.Integer(1))
    fdiv = [fac.inv()*f for f in fj]
    cdiv = kernel(fdiv)
    eq("factorial kernel congruence", cj, fac*cdiv*fac)
    eq("dual factorial frame", vj.H*cj*vj, (fac*vj).H*cdiv*(fac*vj))
    neq("Euclidean Gram is not preserved by factorial map",
        vj.H*vj, (fac*vj).H*(fac*vj))

    qpoly = s.expand(s.prod((x-node)**multiplicity
                           for node, multiplicity in confluent_nodes))
    transform = s.Matrix.hstack(*[jets(x**ell, confluent_nodes)
                                 for ell in range(n)])
    rq = s.Matrix.hstack(*[coeff(s.rem(x**(ell+1), qpoly, x), n)
                          for ell in range(n)])
    eq("quotient-jet intertwining", transform*rq, j*transform)
    avec = [coeff(s.rem(p, qpoly, x), n) for p in POLYS]
    kq = kernel(avec)
    eq("quotient kernel congruence", cj, transform*kq*transform.H)
    eq("quotient CD", rq*kq-kq*rq.H,
       (avec[2]*avec[1].H-avec[1]*avec[2].H)/GAMMAS[1])
    vhat = transform.H*vj
    metric = transform.inv()*transform.H.inv()
    eq("metric identity", metric, (transform.H*transform).inv())
    eq("transport A", alljet["A"], vhat.H*kq*vhat)
    eq("transport W", alljet["W"], vhat.H*metric*vhat)
    eq("transport B", alljet["B"], vhat.H*rq*metric*vhat)
    eq("transport H", alljet["H"],
       (vhat.H*rq*metric*vhat)*(vhat.H*metric*vhat).inv())
    transported_e = (vhat.H*rq*(s.eye(n)-metric*vhat*alljet["W"].inv()*vhat.H)
                     *kq*vhat)
    eq("transport E", alljet["E"], transported_e)
    neq("untransported Euclidean Gram differs", alljet["W"], vhat.H*vhat)

    print(json.dumps({"status": "passed", "checks": COUNT,
                      "arithmetic": "exact SymPy",
                      "mass": "M > 0; original M=sqrt(2*pi)",
                      "fixture_scope": "algebra only; not actual OCF periods"},
                     sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative", choices=["drop-correction", "wrong-orientation"])
    arguments = parser.parse_args()
    try:
        main(arguments.negative)
    except Exception as error:
        print(f"FAILED after {COUNT} checks: {error}", file=sys.stderr)
        raise
