"""Independent S-coordinate, matrix-level regression controls (not zeta packets)."""
import argparse
import hashlib
import json
import sys
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
S, u = s.symbols("S u", real=True)
I = s.I
c = s.Rational(3, 2)
points = list(range(-3, 4))
weights = [s.Integer(x) for x in [2, 5, 3, 7, 11, 13, 17]]

def cm(m):
    return m.applyfunc(s.cancel)

def eq(a, b, name):
    if isinstance(a, s.MatrixBase):
        ok = a.shape == b.shape and all(s.cancel(z) == 0 for z in a - b)
    else:
        ok = s.cancel(a - b) == 0
    if not ok:
        raise ArithmeticError(name + ": " + str(a - b))

def expect_wrong(a, b, name):
    try:
        eq(a, b, name)
    except ArithmeticError:
        return name
    raise ArithmeticError("Negative formula unexpectedly accepted: " + name)

def inner(p, r, derivative=0):
    pv, rv = s.expand(p.subs(S, c + I*u)), s.expand(r.subs(S, c + I*u))
    prod = s.conjugate(pv) * rv
    return s.cancel(s.expand(sum(w * x**derivative * prod.subs(u, x) for x, w in zip(points, weights))))

def matrix_gram(n, derivative=0, multiplier=s.Integer(1)):
    return s.Matrix(n, n, lambda i, j: inner(multiplier*S**i, multiplier*S**j, derivative))

def remainder(f, chi, q):
    p = s.Poly(s.rem(s.expand(f), chi, S), S)
    return s.Matrix([p.nth(j) for j in range(q)])

def monic(j):
    if j == 0:
        return s.Integer(1)
    coefficients = matrix_gram(j).inv() * s.Matrix([inner(S**i, S**j) for i in range(j)])
    return s.expand(S**j - sum(coefficients[i] * S**i for i in range(j)))

def fixture(phi, N):
    q = s.degree(phi, u)
    chi = s.expand(I**q * phi.subs(u, (S-c)/I))
    J = s.Matrix.hstack(*[remainder(S**j, chi, q) for j in range(N+1)])
    M, Mp, Mpp = [matrix_gram(N+1, j) for j in range(3)]
    Mi = M.inv()
    K = cm(J*Mi*J.H)
    G = cm(K.inv())
    R = cm(Mi*J.H*G)
    Kp = cm(-J*Mi*Mp*Mi*J.H)
    Kpp = cm(J*cm(2*Mi*Mp*Mi*Mp*Mi - Mi*Mpp*Mi)*J.H)
    Gp = cm(-G*Kp*G)
    Gpp = cm(2*G*Kp*G*Kp*G - G*Kpp*G)
    Rp = cm(-Mi*Mp*R + Mi*J.H*Gp)
    A = s.Matrix.hstack(*[remainder(S**(j+1), chi, q) for j in range(q)])
    T = (A-c*s.eye(q))/I
    ellp = s.trace(K*Gp)
    W = cm(A.H*G + G*A - 2*c*G)
    H = cm(K*W)
    eps2 = s.cancel(s.trace(H*H)/2)
    D = lambda n: s.Integer(1) if n == 0 else s.cancel(matrix_gram(n).det())
    B = lambda n: s.Integer(1) if n == 0 else s.cancel(matrix_gram(n, multiplier=chi).det())
    volume = lambda n: D(n+1)/B(n-q+1)
    eq(G.det(), volume(N), "literal S-source Schur determinant")
    eq(J*R, s.eye(q), "quotient lift")
    eq(J*Rp, s.zeros(q), "derivative remains original relation")

    # The comparison is performed in P_(N+1), with its original weighted Gram.
    Mf = matrix_gram(N+2)
    E = s.eye(N+2)[:, :N+1]
    PP = cm(E*M.inv()*E.H*Mf)
    XP = s.zeros(N+2)
    for j in range(N+1):
        XP[j,j] = -c/I
        XP[j+1,j] = 1/I
    XR = cm(XP*E*R)
    if N >= q:
        boundary = s.Matrix(N+2, N-q+1, lambda i,j: s.expand(chi*S**j).coeff(S,i))
        PB = cm(boundary*cm(boundary.H*Mf*boundary).inv()*boundary.H*Mf)
    else:
        PB = s.zeros(N+2)
    outgoing = cm((s.eye(N+2)-PP)*XR)
    incoming = cm(PB*XR)
    eq(E*Rp, -incoming, "R prime = negative literal relation projection")
    eq(Gpp-Gp*K*Gp, outgoing.H*Mf*outgoing-incoming.H*Mf*incoming, "full matrix curvature, not only trace")
    if outgoing.rank() > 1 or incoming.rank() > 1:
        raise ArithmeticError("Rank-one curvature maps violated")
    bn = remainder(monic(N), chi, q)
    bn1 = remainder(monic(N+1), chi, q)
    wn, wn1 = inner(monic(N),monic(N)), inner(monic(N+1),monic(N+1))
    cross = (bn.H*G*bn1)[0]/wn
    sigma = s.trace(T)
    eq(cross, I*(sigma-ellp), "original S cross phase with positive i")
    eq(Gp, R.H*Mp*R, "measure derivative included")
    if N == q-1:
        formula = (B(1)-wn1)/wn - (sigma-ellp)**2
        eq(eps2, formula, "minimal-degree endpoint")
        scalar = {"endpoint": str(s.cancel(formula))}
    else:
        d0 = s.cancel(volume(N)/volume(N-1))
        d1 = s.cancel(volume(N+1)/volume(N))
        aa = wn1/wn
        formula = aa*(1-d0)*(1/d1-1)-(sigma-ellp)**2
        eq(eps2, formula, "complete scalar radius")
        rho = s.cancel(volume(N-1)/volume(N+1))
        bound = s.cancel(aa*(rho-1)**2/(4*rho))
        if not (0 < d0 <= 1 and 0 < d1 <= 1 and eps2 <= bound):
            raise ArithmeticError("Finite contraction or upper bound failed")
        scalar = {"delta_N": str(d0), "delta_N_plus_1": str(d1), "upper_bound_squared": str(bound)}
    negatives = [expect_wrong(cross, -I*(sigma-ellp), "wrong original-coordinate phase sign"), expect_wrong(eps2, formula+(sigma-ellp)**2, "omitted nonzero phase square")]
    return {"phi_u": str(phi), "literal_chi_S": str(chi), "N": N, "q": int(q), "mass": str(sum(weights)), "det_G": str(s.cancel(G.det())), "ell_prime": str(s.cancel(ellp)), "sigma": str(sigma), "epsilon_squared": str(eps2), "outgoing_rank": outgoing.rank(), "incoming_rank": incoming.rank(), "scalar": scalar, "formula_negatives_rejected": negatives}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for phi, n in [(u*u+u+1,1), (u*u+u+1,2), (u*u+u+1,3), ((u-1)**2,2)]:
        row = fixture(phi,n)
        rows.append(row)
        print(json.dumps(row),flush=True)
    result = {"status":"pass", "python":sys.version, "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "source_checker_imported":False, "scope":"Independent exact finite atomic S-coordinate fixtures, including matrix curvature and actual sign/phase-loss mutations. Not zeta packets, not an analytic proof certificate.", "fixture_count":len(rows), "formula_negative_controls":sum(len(r["formula_negatives_rejected"]) for r in rows), "rows":rows}
    args.json.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__ == "__main__":
    main()
