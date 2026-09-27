#!/usr/bin/env python3
"""s6_monodromy_checks.py -- note 52_, Part B: the integral monodromy of the S6 manuscript's (3,4,inf) period system.

V = Z^4 with basis (gamma, u, w, delta); T1, T2 from the manuscript's (2.2); Q0 the invariant alternating form of its
Lemma 2.8 (Q0(gamma,delta) = 1, Q0(u,w) = 6).  G = <T1, T2>.  G_Z := {g in Sp(Q0, Z) : g gamma = gamma}.
Claims checked here:
 (B1) relations, invariance of Q0, elementary divisors (1,1,6,6) (type (1,6));
 (B2) G_Z = Levi (SL2(Z) on <u,w>, fixing gamma, delta) x| Heis(Z), Heis(Z) = {h(p,r,s)} with the stated law;
 (B3) pi(T1), pi(T2) generate SL2(Z);  c = [T1, T2^2] = h(1, 0, -6);
 (B4) H' = {h(p,r,s) : 6 | s, s/6 = p^2 + p r + r^2 mod 2} is a subgroup of Heis(Z) of index 12, normalized by G_Z;
      G n Heis = H' (proof in the note); hence [G_Z : G] = 12;
 (B5) independent: the images of G and G_Z in GL4(Z/D) for D = 2, 3, 4, 6, 8, 9, 12 have index ratios 2, 3, 4, 6, 4, 3, 12;
 (B6) the ES-09 affine action (dual matrices on Lambda, hyperplane gamma-hat = 1): G and G_Z have the same orbits mod D <= 9.
"""
import sympy as sp, numpy as np, itertools, time
from sympy.matrices.normalforms import smith_normal_form
T0t = time.time()
res = []
def check(name, cond):
    ok = bool(cond); res.append((name, ok)); print(("PASS" if ok else "FAIL") + "  " + name, flush=True)

T1 = sp.Matrix([[1, 0, -6, 2], [0, -1, 1, 1], [0, -1, 0, 1], [0, 0, 0, 1]])
T2 = sp.Matrix([[1, 6, 0, -3], [0, 0, -1, 1], [0, 1, 0, 0], [0, 0, 0, 1]])
I4 = sp.eye(4)
Q0 = sp.Matrix([[0, 0, 0, 1], [0, 0, 6, 0], [0, -6, 0, 0], [-1, 0, 0, 0]])
check("(B1) T1^3 = T2^4 = I, T0 = (T1T2)^-1 with (T0 - I)^2 = 0, rank(T0 - I) = 2",
      T1**3 == I4 and T2**4 == I4 and ((T1*T2).inv() - I4)**2 == sp.zeros(4) and ((T1*T2).inv() - I4).rank() == 2)
check("(B1) Q0 is T1- and T2-invariant (manuscript Lemma 2.8)", T1.T*Q0*T1 == Q0 and T2.T*Q0*T2 == Q0)
check("(B1) Q0 has elementary divisors (1,1,6,6): type (1,6)", list(smith_normal_form(Q0, domain=sp.ZZ).diagonal()) == [1, 1, 6, 6])
Xa = sp.Matrix(4, 4, lambda i, j: 0)
xs = sp.symbols('x0:6'); kk = 0
for i in range(4):
    for j in range(i + 1, 4):
        Xa[i, j] = xs[kk]; Xa[j, i] = -xs[kk]; kk += 1
eqs = list(T1.T*Xa*T1 - Xa) + list(T2.T*Xa*T2 - Xa)
solX = sp.linsolve(eqs, xs)
free_params = set().union(*[sp.sympify(e).free_symbols for e in list(solX)[0]]) & set(xs)
check("(B1) the T1,T2-invariant alternating forms form a 1-dimensional space (Q0 unique up to scalar; primitive integral up to sign)",
      len(free_params) == 1 and sp.expand(Xa.subs(dict(zip(xs, list(solX)[0]))) - (list(free_params)[0]/6)*Q0) == sp.zeros(4))
T0m = (T1*T2).inv(); Nm = T0m - I4
imN = Nm.columnspace(); kerN = Nm.nullspace()
span_gu = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
check("(B1) N = T0 - I: im N = ker N = <gamma, u> (a Lagrangian for Q0)",
      sp.Matrix.hstack(*imN).rank() == 2 and sp.Matrix.hstack(span_gu, *imN).rank() == 2
      and len(kerN) == 2 and sp.Matrix.hstack(span_gu, *kerN).rank() == 2 and (span_gu.T*Q0*span_gu) == sp.zeros(2))
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
def wedge(av, bv):
    return sp.Matrix([av[k]*bv[l] - av[l]*bv[k] for (k, l) in pairs])
N2 = sp.Matrix.hstack(*[wedge(Nm[:, i], I4[:, j]) + wedge(I4[:, i], Nm[:, j]) for (i, j) in pairs])
W2 = sp.Matrix.hstack(*[wedge(T0m[:, i], T0m[:, j]) for (i, j) in pairs])
check("(B1) on Lambda^2 V: the induced log-monodromy N2 has N2^2 != 0 and N2^3 = 0, and Lambda^2 T0 = exp(N2) (Kulikov type III shape)",
      N2**2 != sp.zeros(6) and N2**3 == sp.zeros(6) and W2 == sp.eye(6) + N2 + N2**2/2)
# (B2) general element of the stabilizer: fixes gamma, preserves the flag <gamma> < <gamma,u,w>, symplectic
p, r, s, au, aw, e = sp.symbols('p r s a_u a_w e')
H = sp.Matrix([[1, au, aw, s], [0, 1, 0, p], [0, 0, 1, r], [0, 0, 0, 1]])   # trivial on the graded pieces
sol = sp.solve(list(H.T*Q0*H - Q0), [au, aw], dict=True)
check("(B2) a unipotent element trivial on the graded pieces is symplectic iff a_u = -6 r, a_w = 6 p", sol == [{au: -6*r, aw: 6*p}])
def h(pp, rr, ss):
    return sp.Matrix([[1, -6*rr, 6*pp, ss], [0, 1, 0, pp], [0, 0, 1, rr], [0, 0, 0, 1]])
p1, r1, s1, p2, r2, s2 = sp.symbols('p1 r1 s1 p2 r2 s2')
check("(B2) law: h(p1,r1,s1) h(p2,r2,s2) = h(p1+p2, r1+r2, s1+s2+6(p1 r2 - p2 r1))",
      sp.expand(h(p1, r1, s1)*h(p2, r2, s2) - h(p1+p2, r1+r2, s1+s2+6*(p1*r2 - p2*r1))) == sp.zeros(4))
M = sp.Matrix(2, 2, sp.symbols('m11 m12 m21 m22'))
L = sp.eye(4); L[1:3, 1:3] = M
check("(B2) Levi elements (M on <u,w>, fixing gamma, delta) are Q0-symplectic iff det M = 1",
      sp.expand(L.T*Q0*L - Q0) == sp.Matrix([[0]*4, [0, 0, 6*(M.det() - 1), 0], [0, -6*(M.det() - 1), 0, 0], [0]*4]))
check("(B2) Levi conjugation: L h(p,r,s) L^-1 = h(M(p,r), s) (for det M = 1)",
      sp.simplify((L*h(p, r, s)*L.inv() - h(*(list(M*sp.Matrix([p, r]))), s)).subs(M[1, 1], (1 + M[0, 1]*M[1, 0])/M[0, 0])) == sp.zeros(4))
R = T1[1:3, 1:3]; S = T2[1:3, 1:3]
check("(B3) Levi images: R = pi(T1) of order 3, S = pi(T2) of order 4, S R = [[1,0],[-1,1]], S (S R) S^-1 = [[1,1],[0,1]]: they generate SL2(Z)",
      R**3 == sp.eye(2) and S**4 == sp.eye(2) and S*R == sp.Matrix([[1, 0], [-1, 1]]) and S*(S*R)*S.inv() == sp.Matrix([[1, 1], [0, 1]]))
c = T1*T2**2*T1.inv()*(T2**2).inv()
check("(B3) c = [T1, T2^2] = h(1, 0, -6)", c == h(1, 0, -6))
# (B4) H' subgroup and index
def inHp(pp, rr, ss):
    return ss % 6 == 0 and (ss//6 - (pp*pp + pp*rr + rr*rr)) % 2 == 0
ok_closed = all(inHp(a1 + a2, b1 + b2, c1 + c2 + 6*(a1*b2 - a2*b1))
                for a1, b1, a2, b2 in itertools.product(range(-3, 4), repeat=4)
                for c1 in [6*((a1*a1 + a1*b1 + b1*b1) % 2) + 12*k for k in (-1, 0, 1)]
                for c2 in [6*((a2*a2 + a2*b2 + b2*b2) % 2) + 12*k for k in (-1, 0, 1)])
check("(B4) H' is closed under the law (sampled; the proof is the identity q(x+y) = q(x) + q(y) + omega(x,y) mod 2 for q = p^2+pr+r^2)", ok_closed)
q = lambda x: (x[0]**2 + x[0]*x[1] + x[1]**2) % 2
om = lambda x, y: (x[0]*y[1] - x[1]*y[0]) % 2
check("(B4) q(x+y) = q(x) + q(y) + omega(x,y) mod 2 on all of (Z/2)^2", all((q((x[0]+y[0], x[1]+y[1])) - q(x) - q(y) - om(x, y)) % 2 == 0
                                                                        for x in itertools.product(range(2), repeat=2) for y in itertools.product(range(2), repeat=2)))
check("(B4) q is SL2(Z/2)-invariant (q = 1 exactly on the three nonzero vectors)", [q(x) for x in itertools.product(range(2), repeat=2)] == [0, 1, 1, 1])
F2v = list(itertools.product(range(2), repeat=2))
refinements = []
for vals in itertools.product(range(2), repeat=4):
    qq = dict(zip(F2v, vals))
    if all((qq[((x[0]+y[0]) % 2, (x[1]+y[1]) % 2)] - qq[x] - qq[y] - om(x, y)) % 2 == 0 for x in F2v for y in F2v):
        refinements.append(qq)
SL2F2 = [Mx for Mx in (np.array(m).reshape(2, 2) for m in itertools.product(range(2), repeat=4)) if round(np.linalg.det(Mx)) % 2 == 1]
def invariant(qq):
    return all(qq[tuple(int(t) for t in (Mx @ np.array(x)) % 2)] == qq[x] for Mx in SL2F2 for x in F2v)
arf = lambda qq: 1 if sum(qq.values()) == 3 else 0          # Arf invariant = majority value on F2^2
inv_refs = [qq for qq in refinements if invariant(qq)]
check("(B4) omega mod 2 has exactly 4 quadratic refinements (3 of Arf invariant 0, 1 of Arf invariant 1); SL2(F2) (order 6) fixes only the odd one, q = p^2+pr+r^2",
      len(refinements) == 4 and sorted(arf(qq) for qq in refinements) == [0, 0, 0, 1] and len(SL2F2) == 6
      and len(inv_refs) == 1 and all(inv_refs[0][x] == q(x) for x in F2v) and arf(inv_refs[0]) == 1)
check("(B4) the 12 central elements h(0,0,k), k = 0..11, are coset representatives of H' in Heis(Z) (box [0,12)^2 x [0,144): every point in exactly one coset)",
      all(sum(1 for k in range(12) if inHp(a1, b1, s1v - k)) == 1 for a1, b1, s1v in itertools.product(range(12), range(12), range(144))))
cnt = sum(1 for a1, b1, s1v in itertools.product(range(12), range(12), range(144)) if inHp(a1, b1, s1v))
check(f"(B4) index of H' in Heis(Z) is 12: in the box [0,12)^2 x [0,144) it has {cnt} of {12*12*144} points", cnt*12 == 12*12*144)
c2 = T2*c*T2.inv()
check("(B4) c = h(1,0,-6) and T2 c T2^-1 = h(0,1,6) lie in H'; their commutator is h(0,0,12) (so G n centre contains 12Z)",
      inHp(1, 0, -6) and c2 == h(0, 1, 6) and inHp(0, 1, 6) and c*c2*c.inv()*c2.inv() == h(0, 0, 12))
# (B5) mod-D enumeration
def inv_int(Mx):
    Mi = np.round(np.linalg.inv(Mx)).astype(np.int64); assert (Mx @ Mi == np.eye(4, dtype=np.int64)).all(); return Mi
T1n = np.array(T1.tolist(), dtype=np.int64); T2n = np.array(T2.tolist(), dtype=np.int64)
def levin(M2):
    Lm = np.eye(4, dtype=np.int64); Lm[1:3, 1:3] = M2; return Lm
def heisn(pp, rr, ss):
    return np.array(h(pp, rr, ss).tolist(), dtype=np.int64)
GZgens = [levin(np.array([[0, -1], [1, 0]])), levin(np.array([[1, 1], [0, 1]])), heisn(1, 0, 0), heisn(0, 1, 0), heisn(0, 0, 1)]
def closure(gens, D):
    gens = [g % D for g in gens] + [inv_int(g) % D for g in gens]
    start = np.eye(4, dtype=np.int64) % D
    seen = {start.tobytes()}; frontier = [start]
    while frontier:
        nxt = []
        for Mx in frontier:
            for g in gens:
                P = (Mx @ g) % D; k = P.tobytes()
                if k not in seen: seen.add(k); nxt.append(P)
        frontier = nxt
    return seen
ratios = {}
for D in (2, 3, 4, 6, 8, 9, 12):
    GD = closure([T1n, T2n], D)
    ratios[D] = len(closure(GZgens, D)) / len(GD)
    if D == 12:
        G12 = GD
check(f"(B5) index of G mod D in G_Z mod D for D = 2,3,4,6,8,9,12: {[int(ratios[D]) for D in ratios]} (12 at D = 12)",
      [int(ratios[D]) for D in (2, 3, 4, 6, 8, 9, 12)] == [2, 3, 4, 6, 4, 3, 12])
heis12 = set()
for kb in G12:
    Mx = np.frombuffer(kb, dtype=np.int64).reshape(4, 4)
    if (Mx[1:3, 1:3] % 12 == np.eye(2, dtype=np.int64)).all():
        heis12.add(kb)
Hp12 = {(np.array(h(pp, rr, ss).tolist(), dtype=np.int64) % 12).tobytes()
        for pp in range(12) for rr in range(12) for ss in range(12) if inHp(pp, rr, ss) or inHp(pp, rr, ss + 12)}
check(f"(B5) direct mod-12 test of Theorem 52.1(b): the elements of G mod 12 with Levi part I are exactly H' mod 12 ({len(heis12)} = {len(Hp12)} = 144 elements)",
      heis12 == Hp12 and len(Hp12) == 144)
# (B6) ES-09 affine action
A1 = inv_int(T1n).T; A2 = inv_int(T2n).T
check("(B6) dual matrices A_j = (T_j^-1)^T are the ES-09 matrices",
      A1.tolist() == [[1, 0, 0, 0], [6, 0, 1, 0], [-6, -1, -1, 0], [-2, 1, 0, 1]] and A2.tolist() == [[1, 0, 0, 0], [0, 0, -1, 0], [-6, 1, 0, 0], [3, 0, 1, 1]])
def orbits_affine(gens, D):
    pts = [(1,) + v for v in itertools.product(range(D), repeat=3)]
    idx = {pt: i for i, pt in enumerate(pts)}
    gens = [g % D for g in gens] + [inv_int(g) % D for g in gens]
    seen = [False]*len(pts); sizes = []
    for i, pt in enumerate(pts):
        if seen[i]: continue
        st = [pt]; seen[i] = True; n = 0
        while st:
            qq = st.pop(); n += 1
            for g in gens:
                rr = tuple(int(x) for x in (g @ np.array(qq)) % D); j = idx[rr]
                if not seen[j]: seen[j] = True; st.append(rr)
        sizes.append(n)
    return sorted(sizes)
GZdual = [inv_int(g).T for g in GZgens]
orbG = {D: orbits_affine([A1, A2], D) for D in range(2, 10)}
same = all(orbG[D] == orbits_affine(GZdual, D) for D in range(2, 10))
for D in range(2, 10):
    print(f"      orbit sizes of G on the affine hyperplane mod {D}: {orbG[D]}")
check("(B6) G and G_Z have the same orbits on the affine hyperplane mod D for D = 2..9 (ES-09 orbit sizes are hull invariants)", same)
check("(B6) the orbit sizes quoted in note 52_ (D = 2: 2,6; 3: 3,24; 4: 16,48; 8: 128,384; 9: 81,648)",
      orbG[2] == [2, 6] and orbG[3] == [3, 24] and orbG[4] == [16, 48] and orbG[8] == [128, 384] and orbG[9] == [81, 648])
print(f"\nsummary: {len(res)} checks, {sum(o for _, o in res)} PASS, {len(res) - sum(o for _, o in res)} FAIL; {time.time()-T0t:.0f}s")
