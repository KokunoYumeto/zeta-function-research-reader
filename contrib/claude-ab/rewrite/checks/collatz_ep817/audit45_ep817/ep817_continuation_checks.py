#!/usr/bin/env python3
"""Independent audit checks of finite certificates in the EP817 continuation notes:
  EP-04  notes/general-k-capacity.md           (Theorem 3 blocks, carry graph, witnesses)
  EP-05  research/graphical_obstructions/...   (A_sharp mod 1651, bad radices, families)
  EP-08  research/finite_period/...            (radix-ten minima a_m, attainers)
Written for this audit from the notes' statements; no workbench code is imported.
Exact integer arithmetic only."""
import itertools, time, sys
from collections import Counter, deque

t0 = time.time()
def say(*a):
    print(" ".join(str(x) for x in a), flush=True)

def H(A):
    s = {0}
    for a in A:
        s |= {x + a for x in s}
    return s

def mod_kAP_free(D, q, k):
    """No (x, e) with e != 0 mod q and x + i e mod q in D for i < k (repetition allowed)."""
    Dm = {d % q for d in D}
    assert len(Dm) == len(D)          # injective reduction (needs max D < q)
    for x in Dm:                       # first term must be in D
        for e in range(1, q):
            if all((x + i * e) % q in Dm for i in range(1, k)):
                return False, (x, e)
    return True, None

def int_kAP_free(S, k):
    bits = 0
    for x in S: bits |= 1 << x
    top = max(S)
    for d in range(1, top // (k - 1) + 1):
        acc = bits
        for i in range(1, k):
            acc &= bits >> (i * d)
            if not acc: break
        if acc:
            x = (acc & -acc).bit_length() - 1
            return False, (x, d)
    return True, None

def language(D, q, t):
    L = {0}
    for j in range(t):
        L = {x + q ** j * d for x in L for d in D}
    return L

# ============================================================ EP-04
say("=== EP-04 general-k capacity certificates")
Bs = [1, 4, 5, 17, 21, 22]
Ds = H(Bs)
say(f"B_* = {Bs}, S = {sum(Bs)}, |H(B_*)| = {len(Ds)} (note: 38)")
listed = [0,1,4,5,6,9,10,17,18,21,22,23,25,26,27,28,30,31,32,38,39,40,42,43,44,45,47,48,49,52,53,60,61,64,65,66,69,70]
say(f"H(B_*) equals the listed 38-element set: {sorted(Ds) == listed}")
for (q, k, B) in [(19, 4, [1, 7, 8]), (23, 5, [1, 3, 4, 7]), (47, 6, [1, 2, 6, 7, 14]), (97, 5, Bs), (93, 6, Bs)]:
    D = H(B); ok, w = mod_kAP_free(D, q, k)
    L2 = language(D, q, 2); ok2, w2 = int_kAP_free(L2, k)
    say(f"  (q={q}, k={k}, B={B}): S={sum(B)}<q: {sum(B)<q}; |H|={len(D)}; modular {k}-AP-free: {ok}; "
        f"two-level language ({len(L2)} values) integer {k}-AP-free: {ok2}")
    assert ok and ok2
# chain histograms (longest chain of the step-e translation graph on D mod q, per step e)
for q, expect in [(97, {2: 6, 3: 28, 4: 62, 5: 0}), (93, {2: 4, 3: 18, 4: 68, 5: 2})]:
    Dm = {d % q for d in Ds}; hist = Counter()
    fullcycle = 0
    for e in range(1, q):
        best = 0; covered = 0
        for x in Dm:
            if (x - e) % q in Dm:      # not a chain start
                continue
            ln = 0; y = x
            while y in Dm:
                ln += 1; y = (y + e) % q
            best = max(best, ln); covered += ln
        if covered < len(Dm): fullcycle += 1   # some full coset cycle lies inside D
        hist[best] += 1
    say(f"  mod {q}: steps with a full coset cycle inside D: {fullcycle}")
    say(f"  longest-chain histogram mod {q}: {dict(sorted(hist.items()))}; note says {expect}: "
        f"{all(hist.get(a,0)==b for a,b in expect.items()) and sum(hist.values())==q-1}")
say(f"  97 < 5^3: {97 < 5**3};  93^5 = {93**5} < 7^12 = {7**12}: {93**5 < 7**12};  97^2 < 23^3: {97**2 < 23**3}")
say(f"  47^6 vs 93^5 (93^(1/6) < 47^(1/5) iff 93^5 < 47^6): {93**5} < {47**6}: {93**5 < 47**6}")
# Theorem 3 finite bound: first n generators of union_j q^j B_*
for q, k in [(97, 5), (93, 6)]:
    for n in range(1, 25):
        j, s = (n - 1) // 6, 1 + (n - 1) % 6
        gens = sorted(q ** jj * b for jj in range(j + 1) for b in Bs)[:n]
        assert max(gens) == Bs[s - 1] * q ** j and len(set(gens)) == n
    say(f"  q={q}: first n generators have max w_s*q^j for n<=24 (ordering by level holds)")
# stated witnesses
for (q, k, row, d) in [(93, 5, [9, 990, 1971, 2952, 3933], 981), (92, 6, [1, 967, 1933, 2899, 3865, 4831], 966)]:
    L2 = language(Ds, q, 2)
    ok = all(row[i + 1] - row[i] == d for i in range(k - 1)) and all(x in L2 for x in row)
    say(f"  witness q={q}, k={k}: {row} is a {k}-AP of step {d} inside the two-level language: {ok}")
    assert ok
row = [0, 77, 154, 231, 308]
say(f"  k=5 base-22 witness for {{1,3,4,7}}: {all(x in language(H([1,3,4,7]),22,2) for x in row)}")

def carry_graph_accepts(D, q, k, maxstates=10**6):
    """Ordinary digits D subset [0,q-1]: BFS on states (c_1..c_{k-1}, flag); True iff (0..0,True) reachable."""
    Ds_ = set(D); start = (tuple([0] * (k - 1)), False)
    seen = {start}; dq = deque([start]); edges = 0
    while dq:
        (cs, fl) = dq.popleft()
        for a in D:
            for e in range(q):
                nc = []
                ok = True
                for i in range(1, k):
                    v = a + i * e + cs[i - 1]
                    if v % q not in Ds_: ok = False; break
                    nc.append(v // q)
                if not ok: continue
                edges += 1
                st = (tuple(nc), fl or e != 0)
                if st == (tuple([0] * (k - 1)), True):
                    return True, seen, edges
                if st not in seen:
                    seen.add(st); dq.append(st)
    return False, seen, edges

acc, seen, edges = carry_graph_accepts([0, 2, 7, 9], 11, 3)
say(f"  carry-graph example B={{2,7}}, q=11, k=3: accepting reachable={acc}; reachable states={sorted(seen)}; "
    f"valid edges from reachable states={edges} (note: 3 states, 14 edges)")
okD, w = mod_kAP_free([0, 2, 7, 9], 11, 3)
say(f"  ... while D mod 11 has a modular 3-AP: {not okD} (e.g. start/step {w})")
L = language([0, 2, 7, 9], 11, 4); say(f"  direct: base-11 words of length 4 with digits {{0,2,7,9}} are 3-AP-free: {int_kAP_free(L,3)[0]}")
# nearby bases for B_*: every q in 71..96 fails at k=5, every q in 71..92 fails at k=6 (full carry graph)
fails5 = [q for q in range(71, 97) if carry_graph_accepts(sorted(Ds), q, 5)[0]]
fails6 = [q for q in range(71, 93) if carry_graph_accepts(sorted(Ds), q, 6)[0]]
say(f"  full carry graph: k=5 fails for {len(fails5)}/26 bases in 71..96; k=6 fails for {len(fails6)}/22 bases in 71..92")
say(f"  and k=5 at q=97, k=6 at q=93 are safe: {not carry_graph_accepts(sorted(Ds),97,5)[0]}, {not carry_graph_accepts(sorted(Ds),93,6)[0]}")
# composition lemma sanity: C = A u R B with R = 2S(A)+1
for A_, B_ in [([1, 7, 8], [1, 7, 8]), ([1, 4, 5], [1, 3]), ([2, 29, 45, 74, 77, 79], [1])]:
    R = 2 * sum(A_) + 1; C = A_ + [R * b for b in B_]
    ok = int_kAP_free(H(C), 4)[0] and len(H(C)) == len(H(A_)) * len(H(B_)) and 2 * sum(C) + 1 == R * (2 * sum(B_) + 1)
    say(f"  composition A={A_}, B={B_}: C 4-admissible, |H(C)|=|H(A)||H(B)|, cost product: {ok}")
say(f"  [EP-04 done {time.time()-t0:.1f}s]")

# ============================================================ EP-05
say("=== EP-05 graphical obstructions")
marks = [0, 4, 7, 41, 257]
As = sorted(t2 - t1 for t1, t2 in itertools.combinations(marks, 2))
say(f"A_sharp = distances of {marks} = {As}; distinct: {len(set(As))==10}; S = {sum(As)}")
assert As == [3, 4, 7, 34, 37, 41, 216, 250, 253, 257]
Dsh = H(As)
mult = Counter()
for r in range(11):
    for U in itertools.combinations(As, r): mult[sum(U)] += 1
hist = Counter(mult.values())
say(f"  |H(A_sharp)| = {len(Dsh)} (note: 291); fibre-size histogram {dict(sorted(hist.items()))} (note: 1:120,2:60,4:60,8:30,14:20,24:1)")
ok, w = mod_kAP_free(Dsh, 1651, 6)
say(f"  1651 = 13*127: {13*127==1651}; H(A_sharp) mod 1651 has no nonzero-step 6-AP: {ok}")
assert ok
say(f"  1651^3 = {1651**3} < 93^5 = {93**5}: {1651**3 < 93**5}")
say(f"  5-AP 0,257,514,771,1028 in H(A_sharp): {all(x in Dsh for x in (0,257,514,771,1028))}")
L2 = language(Dsh, 1651, 2)
say(f"  two-level language (|L2|={len(L2)}) integer 6-AP-free: {int_kAP_free(L2, 6)[0]}")
for n in range(1, 31):
    j, s = (n - 1) // 10, 1 + (n - 1) % 10
    gens = sorted(1651 ** jj * a for jj in range(j + 1) for a in As)[:n]
    assert max(gens) == As[s - 1] * 1651 ** j <= 257 * 1651 ** ((n + 9) // 10 - 1)
say("  g_6(n) <= a_s 1651^j <= 257*1651^(ceil(n/10)-1) generator bookkeeping checked for n <= 30")
# bad radices 1103..1650: explicit nonconstant integer 6-AP in the two-level language D + qD
Dl = sorted(Dsh); Dset = set(Dl)
ret = {}
for c in itertools.product((-1, 0, 1), repeat=4):
    found = None
    for r0 in Dl:
        for r1 in Dl:
            r = [r0, r1]; okr = True
            for i in range(4):
                nxt = 2 * r[-1] - r[-2] - c[i]
                if nxt not in Dset: okr = False; break
                r.append(nxt)
            if okr: found = r; break
        if found: break
    ret[c] = found
say(f"  return sections r(c) in D^6 with second differences -c exist for {sum(v is not None for v in ret.values())}/81 carries")
bad_ok = 0; bad_list = []
for q in range(1103, 1651):
    Dm = set(Dl)  # D subset [0, q-1] since S = 1102 < q
    got = None
    for x in Dl:
        for e in range(1, q):
            if (x + e) % q not in Dm or (x + 2 * e) % q not in Dm: continue
            row = [(x + i * e) % q for i in range(6)]
            if all(v in Dm for v in row):
                c = tuple((row[i] - 2 * row[i + 1] + row[i + 2]) // q for i in range(4))
                assert all((row[i] - 2 * row[i + 1] + row[i + 2]) % q == 0 for i in range(4))
                if ret.get(c) is not None:
                    y = [row[i] + q * ret[c][i] for i in range(6)]
                    if len(set(y)) > 1 and all(y[i + 1] - y[i] == y[1] - y[0] for i in range(5)):
                        got = y; break
        if got: break
    if got:
        # confirm membership in H(A_sharp u q A_sharp) = D + q D
        assert all((v % q) in Dm and (v // q) in Dm for v in got)
        bad_ok += 1
    else:
        bad_list.append(q)
say(f"  radices q = 1103..1650: explicit nonconstant integer 6-AP in D + qD found for {bad_ok}/548; without: {bad_list[:10]}")
# family (7.1)-(7.2): six-term progression for (0,a,b,c=5b-3a,z)
cnt = 0
for a in range(1, 8):
    for b in range(a + 1, 16):
        if b == 2 * a: continue
        c = 5 * b - 3 * a
        for z in range(2 * c + 1, 2 * c + 40):
            ms = [0, a, b, c, z]
            dist = [t2 - t1 for t1, t2 in itertools.combinations(ms, 2)]
            assert len(set(dist)) == 10
            Hh = H(dist)
            y = [z - c, z - b, z + c - 2 * b, z + 2 * b + c - 3 * a, z + b + 2 * c - 3 * a, z + 3 * c - 3 * a]
            assert all(v in Hh for v in y) and all(y[i + 1] - y[i] == c - b for i in range(5))
            cnt += 1
say(f"  family (7.1)-(7.2): {cnt} parameter choices (a<=7, b<=15, 39 values of z each) all have distinct weights and the stated 6-AP")
# classification of appended marks z = 42..356 for prefix (0,4,7,41)
cls = Counter(); free_z = []
for z in range(42, 357):
    dist = [t2 - t1 for t1, t2 in itertools.combinations([0, 4, 7, 41, z], 2)]
    if len(set(dist)) < 10: cls["repeated weights"] += 1; continue
    if int_kAP_free(H(dist), 6)[0]: cls["6-AP-free"] += 1; free_z.append(z)
    else: cls["has 6-AP"] += 1
say(f"  z=42..356 classification: {dict(cls)} (note: 270 with 6-AP, 6 repeated, 39 free); z=257 free: {257 in free_z}")
spot = [z for z in (357, 400, 1000, 2500) if int_kAP_free(H([t2 - t1 for t1, t2 in itertools.combinations([0,4,7,41,z],2)]), 6)[0]]
say(f"  spot checks z in (357,400,1000,2500) 6-AP-free: {spot}")
# tournament scores: |Sigma_m| and Theorem 5.2 packets for m <= 5
def scores(m):
    E = list(itertools.combinations(range(m), 2)); S = set()
    for mask in range(1 << len(E)):
        sc = [0] * m
        for idx, (i, j) in enumerate(E):
            # base tournament: vertex i has score i (higher index wins); choosing an edge reverses it
            if (mask >> idx) & 1: sc[i] += 1
            else: sc[j] += 1
        S.add(tuple(sc))
    return S
sizes = {m: len(scores(m)) for m in range(2, 7)}
say(f"  |Sigma_m| for m=2..6: {sizes} (note: 2,7,38,291,2932)")
for m in range(2, 6):
    Sg = scores(m); dirs = {tuple(t[i] - s[i] for i in range(m)) for s in Sg for t in Sg} - {tuple([0] * m)}
    okall = True
    for r in dirs:
        mx, mn = max(r), min(r)
        for i in [p for p in range(m) if r[p] == mx]:
            for j in [p for p in range(m) if r[p] == mn]:
                al = [0] * m; al[j] += 1; al[i] -= 1
                hit = False
                for s in Sg:
                    if all(tuple(s[p] - h * al[p] for p in range(m)) in Sg for h in range(1, m)) and \
                       tuple(s[p] + r[p] + al[p] for p in range(m)) in Sg:
                        hit = True; break
                okall &= hit
    say(f"  Theorem 5.2 packets exist for all {len(dirs)} nonzero score differences at m={m}, every argmax/argmin choice: {okall}")
say(f"  [EP-05 done {time.time()-t0:.1f}s]")

# ============================================================ EP-08
say("=== EP-08 finite-period: radix-ten dictionary A=(10,{1,3}), B=(10,{2,4}), arity q=5")
def Hq(A, q):
    s = {0}
    for a in A:
        s = {x + c * a for x in s for c in range(q)}
    return s
XA, XB = Hq([1, 3], 5), Hq([2, 4], 5)
say(f"  H_5 digits: A -> {sorted(XA)[:3]}..{max(XA)} ({len(XA)} values), B -> {len(XB)} values (a_1 = 13)")
for lvl in ([1, 3], [2, 4]):
    say(f"  level {lvl}: binary image {sorted(H(lvl))} modular-5-AP-free mod 10: {mod_kAP_free(H(lvl), 10, 5)[0]}")
# carry automaton: state = set of possible carries; count distinct integers sum 10^j x_j
def step_table(X):
    tab = {}
    for S in [frozenset(s) for r in range(1, 4) for s in itertools.combinations(range(3), r)]:
        out = Counter()
        for o in range(10):
            S2 = frozenset((x + c) // 10 for c in S for x in X if (x + c) % 10 == o)
            if S2: out[S2] += 1
        tab[S] = out
    return tab
TA, TB = step_table(XA), step_table(XB)
def count_word(w):
    st = Counter({frozenset([0]): 1})
    for ch in w:
        T = TA if ch == "A" else TB; nst = Counter()
        for S, c in st.items():
            for S2, k in T[S].items(): nst[S2] += c * k
        st = nst
    return sum(c * len(S) for S, c in st.items())
def direct_count(w):
    A_w = []
    for j, ch in enumerate(w):
        A_w += [10 ** j * a for a in ([1, 3] if ch == "A" else [2, 4])]
    return len(Hq(A_w, 5))
agree = all(count_word(w) == direct_count("".join(w)) for m in range(1, 6) for w in itertools.product("AB", repeat=m))
say(f"  automaton count equals direct enumeration of H_5(A_w) for all words of length <= 5: {agree}")
def formula(m):
    if m == 0: return 1
    if m == 1: return 13
    r, s = divmod(m, 3)
    return 893 ** r if s == 0 else (93 ** 2 * 893 ** (r - 1) if s == 1 else 93 * 893 ** r)
MMAX = 16
# DFS over words keeping prefix state
mins = {}
def dfs(st, m):
    if m >= 1:
        val = sum(c * len(S) for S, c in st.items())
        mins[m] = min(mins.get(m, 10 ** 30), val)
    if m == MMAX: return
    for T in (TA, TB):
        nst = Counter()
        for S, c in st.items():
            for S2, k in T[S].items(): nst[S2] += c * k
        dfs(nst, m + 1)
dfs(Counter({frozenset([0]): 1}), 0)
ok = all(mins[m] == formula(m) for m in range(1, MMAX + 1))
say(f"  exact minima a_m for m=1..{MMAX} over all 2^m words: {[mins[m] for m in range(1, 8)]}...; equal to FP3 formula: {ok}")
gf = [1, 13, 93, 0, -2960]
coef = [0] * 12
for i in range(12):
    coef[i] = (gf[i] if i < len(gf) else 0) + (893 * coef[i - 3] if i >= 3 else 0)
say(f"  generating function coefficients {coef[:8]} match formula: {all(coef[i]==formula(i) for i in range(12))}")
att = {"BA": 93, "BAA": 893, "BABA": 93 ** 2, "BAABAA": 893 ** 2, "BABAA": 93 * 893, "AAB": None}
for w, v in att.items():
    say(f"  word {w}: |H_5| = {count_word(w)}" + (f" (expected {v})" if v else ""))
say(f"  (AAB)^r counts r=1..4: {[count_word('AAB'*r) for r in range(1,5)]}; 2301*893^(r-1): {[2301*893**(r-1) for r in range(1,5)]}")
say(f"  93^3 = {93**3} > 893^2 = {893**2}: {93**3 > 893**2}; t_L=(8*10^L+37)/9 for L=2,3: {(8*100+37)//9}, {(8*1000+37)//9}")
# FP1 fibre bound C^{-1}F(u)F(v) <= F(uv) <= F(u)F(v), C = q-1, on the q=5 radix-ten words
worst = 1.0
for m1 in range(1, 5):
    for m2 in range(1, 5):
        for u in itertools.product("AB", repeat=m1):
            for v in itertools.product("AB", repeat=m2):
                Fu, Fv, Fuv = count_word(u), count_word(v), count_word(u + v)
                assert Fu * Fv <= 4 * Fuv and Fuv <= Fu * Fv
                worst = max(worst, Fu * Fv / Fuv)
say(f"  cut inequality (2.2) holds on all word pairs up to length 4+4; largest fibre-mean kappa = {worst:.4f} <= C = 4")
say(f"  893^(1/6) = {893**(1/6):.5f}; 97^(1/6) = {97**(1/6):.5f} (the note: 893^(1/6) is larger, not a new record)")
say(f"done in {time.time()-t0:.1f}s")
