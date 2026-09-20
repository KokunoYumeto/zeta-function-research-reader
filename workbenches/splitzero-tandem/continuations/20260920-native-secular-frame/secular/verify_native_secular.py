"""Exact finite algebra checks; no numerical arithmetic-packet evaluation.

The positive test measure is (3/2) 1_[-1,1](u) du, of mass 3.
All arithmetic is symbolic rational/complex arithmetic in SymPy.
The checker uses explicit exceptions, so optimized Python does not skip checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as s

u, z, S = s.symbols("u z S")
I = s.I
counts = {"scalar_equalities": 0, "exact_inequalities": 0, "negative_controls": 0}
cases = []


def eq(x, y=0):
    if isinstance(x, s.MatrixBase) or isinstance(y, s.MatrixBase):
        a = x-y
        for v in a:
            eq(v)
        return
    counts["scalar_equalities"] += 1
    delta = s.cancel(s.expand(x-y))
    if delta != 0 and s.simplify(delta) != 0:
        raise ArithmeticError(f"Identity failed: {x} != {y}")


def yes(b, msg):
    counts["exact_inequalities"] += 1
    if not bool(b):
        raise ArithmeticError(msg)


def rejects_false_identity(x, y=0):
    counts["negative_controls"] += 1
    if isinstance(x, s.MatrixBase) or isinstance(y, s.MatrixBase):
        if all(s.cancel(s.expand(v)) == 0 for v in x-y):
            raise ArithmeticError("Deliberately false matrix identity was accepted")
        return
    if s.cancel(s.expand(x-y)) == 0:
        raise ArithmeticError("Deliberately false identity was accepted")


def inner(p, q):
    expr = s.Poly(s.expand(s.conjugate(p)*q), u)
    # u is a formal real integration variable; conjugation is only coefficientwise.
    return sum(coef * (s.Rational(3, j[0]+1) if j[0] % 2 == 0 else 0)
               for j, coef in expr.terms())


def norm_pair(p, q):
    pc = s.Poly(p, u)
    pp = sum(s.conjugate(pc.nth(j))*u**j for j in range(pc.degree()+1))
    poly = s.Poly(s.expand(pp*q), u)
    return sum(v*(s.Rational(3, j[0]+1) if j[0] % 2 == 0 else 0)
               for j, v in poly.terms())


def orthogonal(n):
    polys, norms = [], []
    for j in range(n+1):
        p = u**j
        for a, w in zip(polys, norms):
            p -= norm_pair(a, u**j)/w*a
        p = s.expand(p)
        w = norm_pair(p, p)
        yes(w > 0, "Positive source norm")
        for a in polys:
            eq(norm_pair(a, p))
        polys.append(p)
        norms.append(w)
    return polys, norms


Q, omega = orthogonal(8)


def vec(poly, chi):
    q = s.degree(chi, u)
    rem = s.Poly(s.rem(poly, chi, u), u)
    return s.Matrix([rem.nth(j) for j in range(q)])


def receiver(chi, L, center=s.Rational(3, 2), name=""):
    chi = s.expand(chi)
    q = s.degree(chi, u)
    Mu = s.Matrix.hstack(*[vec(u**(j+1), chi) for j in range(q)])
    ds = [vec(p, chi) for p in Q[:L+2]]
    K = s.zeros(q)
    for j in range(L+1):
        K += ds[j]*ds[j].T/omega[j]
    Gu = K.inv()
    for j in range(1, q+1):
        yes(Gu[:j, :j].det() > 0, "Original Gram positivity")
    ru, ellu = -ds[L+1]/omega[L], ds[L].T*Gu
    Au = Mu+ru*ellu
    eq(Au.T*Gu, Gu*Au)
    eq((ru*ellu)**2, s.zeros(q))
    eq((ellu*ru)[0])
    eq(Mu.charpoly(z).as_expr(), chi.subs(u, z))
    # A second construction: rectangular monomial multiplication and source Gram.
    monH = s.Matrix(L+1, L+1,
                    lambda a, b: s.Rational(3, a+b+1) if (a+b) % 2 == 0 else 0)
    red = s.Matrix.hstack(*[vec(u**j, chi) for j in range(L+1)])
    RR = monH.inv()*red.T*Gu
    eq(red*RR, s.eye(q))
    eq(RR.T*monH*RR, Gu)
    # Polynomial multiplication compressed in the source Gram (no Jacobi shortcut).
    xu = s.Matrix(L+1, L+1,
                  lambda a, b: s.Rational(3, a+b+2) if (a+b+1) % 2 == 0 else 0)
    eq(Au, Gu.inv()*RR.T*xu*RR)
    # Literal S-power map, non-unit mass and original phases.
    T = s.Matrix(q, q, lambda a, b:
                 s.binomial(b, a)*center**(b-a)*I**a if a <= b else 0)
    Ti = T.inv()
    G = T.conjugate().T*Gu*T
    bs = [Ti*(I**j*ds[j]) for j in range(L+2)]
    M = Ti*Mu*T
    r, ell = I*bs[L+1]/omega[L], bs[L].conjugate().T*G
    A = M+r*ell
    eq(T*A*Ti, Au)
    eq(A.conjugate().T*G, G*A)
    eq((ell*r)[0])
    Gamma = s.Matrix(q, q, lambda a, b:
                     s.binomial(b, a)*(2*center)**(b-a)*(-1)**a if a <= b else 0)
    eq(Gamma*Gamma, s.eye(q))
    eq(Gamma.conjugate().T*G*Gamma, G)
    eq(Gamma*A*Gamma, -A)
    for j, b in enumerate(bs):
        eq(Gamma*b, (-1)**j*b)
    chiZ = chi.subs(u, z)
    d = s.expand(Au.charpoly(z).as_expr())
    n = s.expand((ellu*(z*s.eye(q)-Mu).adjugate()*ru)[0])
    eq(d, chiZ-n)
    f = s.cancel(n/chiZ)
    eq(f.subs(z, -z), f)
    eq(d.subs(z, -z), (-1)**q*d)
    if n != 0:
        yes(s.degree(n, z) <= q-2, "Trace/parity degree bound")
    P, D = s.fraction(f)
    if P == 0:
        P, D = s.Integer(0), s.Integer(1)
    else:
        lead = s.LC(s.Poly(D, z))
        P, D = s.expand(P/lead), s.expand(D/lead)
    H = s.expand(D-P)
    invisible = s.cancel(chiZ/D)
    eq(d, invisible*H)
    eq(s.gcd(P, D), 1)
    eq(s.gcd(P, H), 1)
    if s.degree(H, z) > 0:
        eq(s.gcd(H, s.diff(H, z)), 1)
        yes(s.Poly(H, z).count_roots(-s.oo, s.oo) == s.degree(H, z),
            "Every active zero is real, exact Sturm count")
    yes(s.Poly(d, z).count_roots(-s.oo, s.oo) == s.degree(d, z),
        "Every compression zero is real, exact Sturm count")
    # Matrix inverse identity at two exact nonspectral values.
    for zz in [2+3*I, -1+4*I]:
        RM = (zz*s.eye(q)-Mu).inv()
        ff = (ellu*RM*ru)[0]
        RA = (zz*s.eye(q)-Au).inv()
        eq(RA, RM+RM*ru*ellu*RM/(1-ff))
        eq((ellu*RA*ru)[0], ff/(1-ff))
    # Full CRT pole series at every exact old root.
    roots = s.roots(chiZ, z)
    yes(sum(roots.values()) == q, "All old roots resolved exactly")
    projections = []
    for alpha, e in roots.items():
        factor, remainder = s.div(chiZ, (z-alpha)**e, z, extension=True)
        eq(remainder)
        ef = factor*sum(s.diff(1/factor, z, a).subs(z, alpha)*(z-alpha)**a/s.factorial(a)
                        for a in range(e))
        coef = s.Poly(s.cancel(s.expand(ef)), z)
        Pi = s.zeros(q)
        for j in range(coef.degree()+1):
            Pi += coef.nth(j)*Mu**j
        Pi = Pi.applyfunc(s.cancel)
        eq(Pi*Pi, Pi)
        eq((Mu-alpha*s.eye(q))**e*Pi, s.zeros(q))
        projections.append(Pi)
        cp = [(ellu*(Mu-alpha*s.eye(q))**j*Pi*ru)[0].simplify() for j in range(e)]
        p = max([j+1 for j, v in enumerate(cp) if v != 0], default=0)
        if s.im(alpha) != 0:
            yes(p == e, "Complete cancellation of every nonreal old pole")
        actual = 0
        while s.simplify(s.diff(d, z, actual).subs(z, alpha)) == 0:
            actual += 1
        predicted = e-p if p > 0 else e + int(s.simplify(f.subs(z, alpha)-1) == 0)
        yes(actual == predicted, "Exact old-root multiplicity formula")
        yes(actual <= 2, "Rank-one companion multiplicity bound")
    eq(sum(projections, s.zeros(q)), s.eye(q))
    for a in range(len(projections)):
        for b in range(a):
            eq(projections[a]*projections[b], s.zeros(q))
    # Original S determinant: sign and i^q both checked directly.
    MS = center*s.eye(q)+I*M
    B = center*s.eye(q)+I*A
    Bdag = G.inv()*B.conjugate().T*G
    eq(Bdag, 2*center*s.eye(q)-B)
    MSdag = G.inv()*MS.conjugate().T*G
    control = MS+MSdag-2*center*s.eye(q)
    control_explicit = (bs[L+1]*bs[L].conjugate().T
                       +bs[L]*bs[L+1].conjugate().T)*G/omega[L]
    eq(control, control_explicit)
    aa = (bs[L].conjugate().T*G*bs[L])[0]
    dd = (bs[L+1].conjugate().T*G*bs[L+1])[0]
    epsilon2 = s.cancel(aa*dd/omega[L]**2)
    eq(control**3, epsilon2*control)
    eq(s.trace(control**2), 2*epsilon2)
    for alpha in roots:
        yes(s.simplify(epsilon2-4*s.im(alpha)**2) >= 0,
            "Original eigenvalue bound with factor two")
    chiS = s.expand(I**q*chi.subs(u, (S-center)/I))
    dS = s.expand(B.charpoly(S).as_expr())
    eq(dS, I**q*d.subs(z, (S-center)/I))
    eq(dS, chiS+(bs[L].conjugate().T*G*(S*s.eye(q)-MS).adjugate()*bs[L+1])[0]/omega[L])
    rejects_false_identity(omega[0], 1)
    cases.append({"name": name, "degree": int(q), "L": L, "f": str(f),
                  "characteristic": str(d), "active": str(H),
                  "invisible": str(invisible)})
    return Mu, Au, Gu, ru, ellu, f


def nonnative_multiplicity_examples():
    data = [
        (s.Matrix([[0,-2],[1,3]]), s.Matrix([1,-1]),
         s.Matrix([[1,2]]), s.eye(2), "active_invisible_overlap"),
        (s.Matrix([[0,0,0],[1,0,0],[0,1,0]]), s.Matrix([0,1,0]),
         s.Matrix([[-1,1,0]]), s.Matrix([[1,0,0],[0,2,-1],[0,-1,1]]),
         "double_invisible_nonzero_pole"),
        (s.Matrix([[0,0],[1,0]]), s.Matrix([0,-1]),
         s.Matrix([[1,0]]), s.eye(2), "zero_transfer_double_root"),
    ]
    for M, r, ell, G, name in data:
        A = M+r*ell
        eq(A.conjugate().T*G, G*A)
        for j in range(1, M.rows+1):
            yes(G[:j,:j].det() > 0, "Example metric positive")
        chi = M.charpoly(z).as_expr()
        d = A.charpoly(z).as_expr()
        f = s.cancel((ell*(z*s.eye(M.rows)-M).inv()*r)[0])
        eq(d, chi*(1-f))
        rejects_false_identity(s.gcd(d, s.diff(d,z)), 1)
        spectral_projections = []
        for t in s.roots(d, z):
            V = s.Matrix.hstack(*(A-t*s.eye(M.rows)).nullspace())
            Pi = V*(V.conjugate().T*G*V).inv()*V.conjugate().T*G
            eq(Pi*Pi, Pi)
            eq(Pi.conjugate().T*G, G*Pi)
            eq(A*Pi, t*Pi)
            border = (t*s.eye(M.rows)-M).row_join(-r).col_join(
                ell.row_join(s.Matrix([[-1]])))
            for j in range(V.cols):
                vv = V[:,j]
                eq(border*vv.col_join(ell*vv), s.zeros(M.rows+1,1))
            spectral_projections.append((t,Pi))
        eq(sum((Pi for t,Pi in spectral_projections), s.zeros(M.rows)), s.eye(M.rows))
        eq(sum((t*Pi for t,Pi in spectral_projections), s.zeros(M.rows)), A)
        cases.append({"name": name, "f": str(f), "characteristic": str(d),
                      "scope": "general companion rank-one lemma; not native parity data"})


def full_jet_unit_examples():
    # Structural polynomial identities, not invented numerical zeta data.
    v, x, y = s.symbols("v x y")
    roots = [s.Rational(1,4)+2*I, s.Rational(1,4)-2*I,
             s.Rational(3,4)+2*I, s.Rational(3,4)-2*I]
    h = s.prod((v-rho)**2 for rho in roots)
    F = 1+v+v**3
    g = s.expand(h*F)
    units = {}
    for rho in roots:
        # NS30: full coefficient of inverse of every other primary factor.
        inv = s.prod((rho-sigma+x)**(-2) for sigma in roots if sigma != rho)
        U = []
        for rr in range(2):
            val = sum(s.diff(g,v,2+a).subs(v,rho)/s.factorial(2+a)
                      *s.diff(inv,x,rr-a).subs(x,0)/s.factorial(rr-a)
                      for a in range(rr+1))
            val = s.simplify(val)
            eq(val, s.diff(F,v,rr).subs(v,rho)/s.factorial(rr))
            U.append(val)
        yes(U[0] != 0, "Full physical unit is nonzero")
        unit_matrix = s.Matrix([[U[0],0],[U[1],U[0]]])
        inverse = s.Matrix([[1/U[0],0],[-U[1]/U[0]**2,1/U[0]]])
        eq(unit_matrix*inverse, s.eye(2))
        units[rho] = U
    testP = v**4+2*v+3
    for rho in roots:
        for sigma in roots:
            direct = s.expand(F.subs(v,rho+x)*F.subs(v,sigma+y)
                              *testP.subs(v,rho+sigma+x+y))
            for j1 in range(2):
                for j2 in range(2):
                    val = sum(units[rho][j1-n1]*units[sigma][j2-n2]
                              *s.diff(testP,v,n1+n2).subs(v,rho+sigma)
                              /(s.factorial(n1)*s.factorial(n2))
                              for n1 in range(j1+1) for n2 in range(j2+1))
                    eq(val, direct.coeff(x,j1).coeff(y,j2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--deliberate-error", action="store_true")
    args = parser.parse_args()
    if args.deliberate_error:
        eq(s.Rational(1,3), -s.Rational(1,3))
        raise ArithmeticError("Unreachable: false sign accepted")
    models = [
        (u, 0, "one_dimensional_zero"),
        (u**2+1, 1, "nonreal_pair_L1"),
        (u**2+1, 3, "nonreal_pair_L3"),
        ((u**2+1)**2, 3, "repeated_nonreal_L3"),
        ((u**2+1)**2, 5, "repeated_nonreal_L5"),
        (u**3, 2, "triple_zero_L2"),
        (u**3, 4, "triple_zero_L4"),
        ((u**2-1)**2, 3, "repeated_real_L3"),
        ((u**2-1)**2, 5, "repeated_real_L5"),
        (Q[3], 2, "all_invisible_orthogonal_quotient"),
    ]
    for chi, L, name in models:
        result = receiver(chi, L, name=name)
        if name == "nonreal_pair_L1":
            M,A,G,r,ell,f=result
            eq(M, s.Matrix([[0,-1],[1,0]]))
            eq(A, s.Matrix([[0,s.Rational(1,3)],[1,0]]))
            eq(G, s.diag(3,1))
            eq(f, s.Rational(4,3)/(z*z+1))
            rejects_false_identity(A.charpoly(z).as_expr(), M.charpoly(z).as_expr())
            rejects_false_identity((M-r*ell).T*G-G*(M-r*ell), s.zeros(2))
    nonnative_multiplicity_examples()
    full_jet_unit_examples()
    here = Path(__file__).resolve().parent
    receipt = {
        "status":"passed", "scope":"exact finite algebra, not arithmetic-packet numerics",
        "python_optimized":not __debug__, "python":sys.version,
        "sympy":s.__version__, "counts":counts, "cases":cases,
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_sha256":hashlib.sha256((here/"NATIVE_SECULAR_RECEIVER.tex").read_bytes()).hexdigest(),
    }
    destination = here/("CHECKS_OPTIMIZED.json" if not __debug__ else "CHECKS_NORMAL.json")
    destination.write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status":"passed","counts":counts,"receipt":str(destination)}))


if __name__ == "__main__":
    main()
