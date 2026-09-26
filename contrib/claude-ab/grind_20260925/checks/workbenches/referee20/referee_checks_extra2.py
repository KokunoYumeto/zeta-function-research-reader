#!/usr/bin/env python3
"""817 negative result 4 (B*, bases 71..96 at k=5, 71..92 at k=6) via bitset AP search on 2- and 3-digit languages."""
import itertools, time
T0 = time.time()
def H(A):
    S = {0}
    for a in A: S |= {s + a for s in S}
    return sorted(S)
Bs = [1, 4, 5, 17, 21, 22]; HB = H(Bs)
def lang_bits(q, L):
    bits = 0
    for digs in itertools.product(HB, repeat=L):
        bits |= 1 << sum(dg * q**i for i, dg in enumerate(digs))
    return bits
def has_ap_bits(S, k, maxv):
    for d in range(1, maxv // (k - 1) + 1):
        T = S
        for j in range(1, k):
            T &= S >> (j*d)
            if not T: break
        if T: return True
    return False
res = {}
for k, qs in ((5, range(71, 98)), (6, range(71, 94))):
    for q in qs:
        found = None
        for L in (1, 2, 3):
            S = lang_bits(q, L); maxv = S.bit_length()
            if has_ap_bits(S, k, maxv): found = L; break
        res[(k, q)] = found
print("k=5: every base 71..96 has an integer 5-AP within 3 digits:", all(res[(5, q)] for q in range(71, 97)),
      "| base 97:", res[(5, 97)], "| digit lengths used:", sorted({res[(5, q)] for q in range(71, 97)}))
print("k=6: every base 71..92 has an integer 6-AP within 3 digits:", all(res[(6, q)] for q in range(71, 93)),
      "| base 93:", res[(6, 93)], "| digit lengths used:", sorted({res[(6, q)] for q in range(71, 93)}))
print(f"total {time.time()-T0:.1f}s")
