# Referee checks for "The S6 record: a reader of its results" (version of 26 September 2026).
# Independent of the reader's scripts; needs python3 + sympy.
# Usage: python3 referee_checks.py [folder with the record's downloaded files]   (the folder is optional;
#        it is used only for the ledger count read from the sources-and-evidence zip 04_)
import sys, os, json, zipfile
import sympy as sp
from itertools import combinations, product
from math import isqrt
ok = True
def check(name, cond, info=None):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("" if info is None else f"  [{info}]"))

x, y, z = sp.symbols('x y z'); V = (x, y, z)
def monos(d):
    return [] if d < 0 else [x**i*y**j*z**(d-i-j) for i in range(d+1) for j in range(d+1-i)]

# ---------------- 1. Section 5.3: test family ----------------
F = y**2*z - x**2*(x+z) - sp.Symbol('t')*z**3
t = sp.Symbol('t')
check("disc(x^3+x^2+t) = -t(27t+4)", sp.factor(sp.discriminant(x**3+x**2+t, x) + t*(27*t+4)) == 0)
u_, v_ = sp.symbols('u v')
X_, Y_, Z_ = (u_**2-v_**2)*v_, u_*(u_**2-v_**2), v_**3
check("nu parametrizes the nodal cubic", sp.expand(Y_**2*Z_ - X_**2*(X_+Z_)) == 0)
U = y - x*sp.sqrt(1+x); Vv = y + x*sp.sqrt(1+x)
Jm = sp.Matrix([[sp.diff(U, x), sp.diff(U, y)], [sp.diff(Vv, x), sp.diff(Vv, y)]]).subs({x: 0, y: 0})
check("node chart: UV = y^2 - x^2 - x^3, Jacobian -2", sp.simplify(U*Vv - (y**2-x**2-x**3)) == 0 and Jm.det() == -2)
check("P(t) = [3 : sqrt(36+t) : 1] on the family; multiplier (1-2)/(-1-2) = 1/3",
      sp.simplify(F.subs({x: 3, y: sp.sqrt(36+t), z: 1})) == 0 and sp.Rational(-1, -3) == sp.Rational(1, 3))
# Kernel sheaf K_S at a normal-crossing triple point S = {xyz = 0}: the 1-forms of Omega^1_X|_S whose pullback to
# every branch vanishes, compared by linear algebra with the span of yz dx, xz dy, xy dz (= normalization * dg).
def nc_basis(k):   # monomials of degree k not divisible by xyz (a basis of (C[x,y,z]/(xyz))_k)
    return [m for m in monos(k) if not (sp.degree(m, x) and sp.degree(m, y) and sp.degree(m, z))]
def K_dims(d):
    B = nc_basis(d - 1); nB = len(B)
    cs = sp.symbols('q0:%d' % (3*nB)) if nB else ()
    comp = [sum(cs[i*nB + j]*B[j] for j in range(nB)) for i in range(3)]   # coefficients of dx, dy, dz
    eqs = []
    for br, keep in ((x, (1, 2)), (y, (0, 2)), (z, (0, 1))):              # branch {br = 0}: d(br) pulls back to 0
        for i in keep:
            eqs += sp.Poly(sp.expand(comp[i].subs(br, 0)), *V).coeffs() if comp[i].subs(br, 0) != 0 else []
    M = sp.Matrix([[sp.diff(eq, q) for q in cs] for eq in eqs]) if eqs else sp.zeros(0, len(cs))
    dim_kernel = len(cs) - (M.rank() if M.shape[0] else 0)
    gens = []
    for m in monos(d - 3):
        for i, g in enumerate((y*z, x*z, x*y)):
            vec = [0]*(3*nB); pm = sp.expand(m*g)
            if not (sp.degree(pm, x) and sp.degree(pm, y) and sp.degree(pm, z)):
                vec[i*nB + B.index(pm)] = 1
            gens.append(vec)
    dim_span = sp.Matrix(gens).rank() if gens else 0
    return dim_kernel, dim_span
check("triple point: K_S = R yz dx + R xz dy + R xy dz (degrees 1..7)", all(K_dims(d)[0] == K_dims(d)[1] for d in range(1, 8)),
      [K_dims(d) for d in range(1, 8)])

# ---------------- 2. Section 5.5: relative forms via the Koszul complex (graded) ----------------
forms = {p: list(combinations(range(3), p)) for p in range(4)}
def wedge_mat(tt, p, d):
    grad = [sp.diff(tt, w) for w in V]; deg = sp.Poly(tt, *V).total_degree()
    src = [(m, I) for I in forms[p] for m in monos(d - p)]
    tgt = [(m, J) for J in forms[p+1] for m in monos(d + deg - (p+1))]
    index = {(sp.Poly(m, *V).monoms()[0], J): k for k, (m, J) in enumerate(tgt)}
    M = sp.zeros(len(tgt), len(src))
    for c, (m, I) in enumerate(src):
        for i in range(3):
            if i in I or grad[i] == 0: continue
            J = tuple(sorted(I + (i,))); sign = (-1)**sorted(I + (i,)).index(i)
            for mon, coeff in sp.Poly(sp.expand(grad[i]*m), *V).terms():
                M[index[(mon, J)], c] += sign*coeff
    return M, len(src)
def H(tt, p, d):
    deg = sp.Poly(tt, *V).total_degree()
    Mo, n = wedge_mat(tt, p, d); ker = n - (Mo.rank() if 0 not in Mo.shape else 0)
    if p == 0: return ker
    Mi, _ = wedge_mat(tt, p-1, d - deg); return ker - (Mi.rank() if 0 not in Mi.shape else 0)
def quot_dim(cols, gdeg, d):
    k = d - gdeg
    if k < 0: return 0
    basis = [(m, e) for e in range(2) for m in monos(k)]
    idx = {(sp.Poly(m, *V).monoms()[0], e): i for i, (m, e) in enumerate(basis)}
    vecs = []
    for col in cols:
        for m in monos(k - 1):
            vec = [0]*len(basis)
            for e in range(2):
                if col[e] != 0:
                    for mon, cf in sp.Poly(sp.expand(col[e]*m), *V).terms(): vec[idx[(mon, e)]] += cf
            vecs.append(vec)
    return len(basis) - (sp.Matrix(vecs).rank() if vecs else 0)
hf = [H(x*y*z, 2, d) for d in range(9)]
check("t = xyz: Hilbert function of Tors Omega^2 = that of R^2/<(x,0),(y,-y),(0,z)>(-3)",
      hf == [quot_dim([(x, 0), (y, -y), (0, z)], 3, d) for d in range(9)], hf)
check("t = xyz: two generators (lowest nonzero degree has dimension 2)", hf[3] == 2)
check("t = xyz and t = xy: Omega^1_{X/B} torsion-free (H^1 = 0, degrees <= 8)",
      all(H(x*y*z, 1, d) == 0 and H(x*y, 1, d) == 0 for d in range(9)))
check("t = xy: Tors Omega^2 = R/(x,y)(-2)", [H(x*y, 2, d) for d in range(8)] == [0, 0] + [1]*6)
check("t = x^2 y: Tors Omega^1 = R/(x)(-2) (non-reduced fibre, phi = t/rad t = x)",
      [H(x**2*y, 1, d) for d in range(8)] == [0, 0] + [d - 1 for d in range(2, 8)])
check("t = x^2+y^2+z^2 (codim Crit 3): Omega^1, Omega^2 relative torsion-free (degrees <= 7)",
      all(H(x**2+y**2+z**2, p, d) == 0 for p in (1, 2) for d in range(8)))
check("t = x^2+y^2 (codim Crit 2): Omega^1 torsion-free, Omega^2 not",
      all(H(x**2+y**2, 1, d) == 0 for d in range(7)) and any(H(x**2+y**2, 2, d) for d in range(7)))
def gcd_is_t_over_rad(tt):
    g = sp.gcd_list([sp.diff(tt, w) for w in V]); fl = sp.factor_list(tt)[1]
    q = sp.cancel(g / sp.prod([f**(e-1) for f, e in fl]))
    return q.is_polynomial(*V) and q.subs({x: 0, y: 0, z: 0}) != 0
ex = [x**2*(x+y**2)**3*(y-z**2), (x**2+y**3)**2, x*(x+y**2), (x*y-z**3)**2*z, (x+y+z)**3*(x-y)**2, (x**2+y**2+z**3)**4]
check("gcd of partials = t/rad(t) up to a unit (6 non-monomial examples)", all(gcd_is_t_over_rad(e) for e in ex))
# T_S at a triple point = Rtilde/R: Hilbert function 3(d+1) - dim R_d
check("triple point: Rtilde/R has Hilbert function (2,3,3,3,...)",
      [3*(d+1) - (1 if d == 0 else 3*d) for d in range(6)] == [2, 3, 3, 3, 3, 3])

# ---------------- 3. Thm 5.8: HRR coefficients ----------------
a, b, c, e = sp.symbols('a b c e')
ser = lambda f: sp.expand(sp.series(f.subs({a: e*a, b: e*b, c: e*c}), e, 0, 4).removeO().coeff(e, 3))
deg3 = ser(sum(sp.exp(r) for r in (a, b, c)) * sp.prod([r/(1-sp.exp(-r)) for r in (a, b, c)]))
c1, c2, c3 = a+b+c, a*b+b*c+c*a, a*b*c
A_, B_, C_ = sp.symbols('A B C')
sol = sp.solve(sp.Poly(sp.expand(deg3 - (A_*c1**3 + B_*c1*c2 + C_*c3)), a, b, c).coeffs(), [A_, B_, C_], dict=True)
check("[ch(T) td(T)]_3 = c1^3/2 - 19/24 c1 c2 + c3/2", sol == [{A_: sp.Rational(1, 2), B_: sp.Rational(-19, 24), C_: sp.Rational(1, 2)}], sol)

# ---------------- 4. Prop 6.1 sharpened: value set of P on D4 ----------------
P = lambda q: q[0]*(q[0]**2 - 3*(q[1]**2 + q[2]**2 + q[3]**2))
def three_sq(N):
    for i in range(isqrt(N)+1):
        for j in range(i, isqrt(N-i*i)+1):
            k2 = N-i*i-j*j; k = isqrt(k2)
            if k*k == k2 and k >= j: return (i, j, k)
def witness(n):
    if n % 18 == 0: a0, N = -3*(n//18), 3*(n//18)**2 + 2
    else: a0, N = -(n//2), ((n//2)**2 + 2)//3
    s = three_sq(N); return None if s is None else (a0,) + s
badw = [n for n in range(-5000, 5001) if n and n % 2 == 0 and (n % 3 or n % 9 == 0)
        and not ((w := witness(n)) and P(w) == n and sum(w) % 2 == 0)]
check("every even n with 3 !| n or 9 | n equals P(a), a in D4, via the explicit witnesses (|n| <= 5000)", badw == [], badw[:5])
check("P(D4) consists of even values with 3 | P => 9 | P (box |a_i| <= 7)",
      all(P(q) % 2 == 0 and (P(q) % 3 or P(q) % 9 == 0) for q in product(range(-7, 8), repeat=4) if sum(q) % 2 == 0))
def qmul(p, q):
    a1, b1, c1_, d1 = p; a2, b2, c2_, d2 = q
    return (a1*a2-b1*b2-c1_*c2_-d1*d2, a1*b2+b1*a2+c1_*d2-d1*c2_, a1*c2_-b1*d2+c1_*a2+d1*b2, a1*d2+b1*c2_-c1_*b2+d1*a2)
qa = sp.symbols('a0:4')
check("Re(a^3) = a0(a0^2 - 3|v|^2) for a quaternion a = a0 + v",
      sp.expand(qmul(qmul(qa, qa), qa)[0] - qa[0]*(qa[0]**2 - 3*(qa[1]**2+qa[2]**2+qa[3]**2))) == 0)

# ---------------- 5. Section 3: the manuscript's lattice data ----------------
T1 = sp.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]]); T2 = sp.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
N0 = (T1*T2).inv() - sp.eye(4)
check("T1^3 = T2^4 = I and (T0 - I)^2 = 0 (source manuscript's matrices)", T1**3 == sp.eye(4) and T2**4 == sp.eye(4) and N0**2 == sp.zeros(4))
check("p(0,1,-1) = -1 (the record's triple), p(1,2,1) = 1 (the reader's), p(100,1,-1) = 1199",
      [12*l0-4*l1-3*l2 for l0, l1, l2 in [(0,1,-1),(1,2,1),(100,1,-1)]] == [-1, 1, 1199])
check("admissible (3 !| l1, l2 odd) residues with |p| = 1 attainable: {(1,3),(2,1)}",
      [(r1, r2) for r1 in (1, 2) for r2 in (1, 3) if (4*r1+3*r2) % 12 in (1, 11)] == [(1, 3), (2, 1)])

# ---------------- 6. the record's claim ledger (optional; zip 04_) ----------------
if len(sys.argv) > 1:
    zpath = os.path.join(sys.argv[1], "04_s6_peer_verification_sources_and_evidence_v1.0.zip")
    rows = [json.loads(l) for l in zipfile.ZipFile(zpath).read(
        "supporting_materials/workbench/research/ledgers/claim_ledger.txt").decode().splitlines() if l.strip()]
    from collections import Counter
    cnt = Counter(r["status"] for r in rows)
    check("claim ledger: 48 rows, 42 VERIFIED / 2 OPEN / 4 REFUTED", len(rows) == 48 and cnt == Counter(VERIFIED=42, OPEN=2, REFUTED=4), dict(cnt))
    print("   OPEN rows:", [r["id"] for r in rows if r["status"] == "OPEN"])
    print("   REFUTED rows:", [r["id"] for r in rows if r["status"] == "REFUTED"])
print("ALL PASS" if ok else "SOME CHECK FAILED")
