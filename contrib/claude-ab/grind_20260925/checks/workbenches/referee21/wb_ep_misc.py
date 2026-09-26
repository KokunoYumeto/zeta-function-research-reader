# Referee 21 (wbreader): Erdos 817 checks from the definitions (independent code).
import math, itertools
def H(A):
    s = 1
    for a in A: s |= s << a
    return s                     # bit x set <=> x is a subset sum
def T(A):
    s = 1
    for a in A: s |= (s << a) | (s << (2*a))
    return bin(s).count("1")
def has_kap_int(bits, k, maxv):
    # integer k-AP with step d >= 1 inside the set encoded by bits
    for d in range(1, maxv//(k-1)+1):
        acc = bits
        for j in range(1, k): acc &= bits >> (j*d)
        if acc: return True
    return False
def has_kap_mod(vals, k, q):
    R = {v % q for v in vals}
    return any(all((x+j*d) % q in R for j in range(k)) for x in R for d in range(1, q))
def elems(bits):
    out=[]; i=0
    while bits:
        if bits & 1: out.append(i)
        bits >>= 1; i += 1
    return out
# small-value witnesses
for A in ([2,29,45,74,77,79], [1,3,39,180,219,243,246]):
    b = H(A); print(A, " 4-admissible:", not has_kap_int(b, 4, sum(A)), " |T| =", T(A))
# refined lower bound at n = 7: 19(M^2-1) <= 192 * sum_{j<7} (N-j)^2
M7 = 19**2*3
Nmin = next(N for N in range(1, 1000) if 192*sum((N-j)**2 for j in range(7)) >= 19*(M7**2-1))
print("n=7: M_7 =", M7, " refined bound gives N >=", Nmin, "; plain Thm 3.6 bound:", math.ceil(math.sqrt(19*(M7**2-1)/(192*7))))
# refined table n <= 6 and the plain bound
for n in range(1, 8):
    q, r = divmod(n, 3); Mn = 19**q*3**r
    Nref = next(N for N in range(1, 1000) if 192*sum((N-j)**2 for j in range(n)) >= 19*(Mn**2-1))
    print(f" n={n}: M_n={Mn}, ceil sqrt bound={math.ceil(math.sqrt(19*(Mn**2-1)/(192*n)))}, refined={Nref}, Clankers={math.ceil((19**(n/3)+n*(n-1)-1)/(2*n))}, paper={math.ceil((19**(n/3)-1)/(2*n))}")
# c_r constants
c0 = math.sqrt(19/192)
print("c_r:", [round(c0*(3/19**(1/3))**r, 3) for r in range(3)])
# Korsky-type rates min_p p^{2/(min(p,k)-1)}
for k in (4,5,6):
    rates = {p: p**(2/(min(p,k)-1)) for p in (3,5,7,11,13)}
    pbest = min(rates, key=rates.get); print(f" k={k}: best p={pbest}, rate={rates[pbest]:.3f}")
print(" 19^(1/3)=%.4f 97^(1/6)=%.4f 93^(1/6)=%.4f 1651^(1/10)=%.4f" % (19**(1/3), 97**(1/6), 93**(1/6), 1651**(1/10)))
# negative results 1-3
print("neg1 |T({1,2,3})| =", T([1,2,3]))
print("neg2 {1,2}: 4-AP", has_kap_int(H([1,2]),4,3), " 5-AP", has_kap_int(H([1,2]),5,3))
B = [2,7]; HB = elems(H(B))
print("neg3 H({2,7}) =", HB, " modular 3-AP mod 11:", has_kap_mod(HB, 3, 11))
for L in range(1,5):
    lang = [sum(dg*11**i for i, dg in enumerate(ds)) for ds in itertools.product(HB, repeat=L)]
    bits = 0
    for v in lang: bits |= 1 << v
    print("   base-11 language length", L, " integer 3-AP:", has_kap_int(bits, 3, max(lang)))
# B* bases 71..96 (k=5) and 71..92 (k=6): two-digit language H(B*) + q H(B*) contains an integer AP
Bs = [1,4,5,17,21,22]; HBs = elems(H(Bs))
def lang_bits(q, L):
    vals = [sum(dg*q**i for i, dg in enumerate(ds)) for ds in itertools.product(HBs, repeat=L)]
    bits = 0
    for v in vals: bits |= 1 << v
    return bits, max(vals)
f5 = [q for q in range(71, 97) if not has_kap_int(*lang_bits(q, 2)[:1], 5, lang_bits(q,2)[1])]
f6 = [q for q in range(71, 93) if not has_kap_int(*lang_bits(q, 2)[:1], 6, lang_bits(q,2)[1])]
print("B*: bases 71..96 WITHOUT an integer 5-AP in the 2-digit language:", f5, "; bases 71..92 without a 6-AP:", f6)
b97, mx97 = lang_bits(97, 2); b93, mx93 = lang_bits(93, 2)
print("B* base 97, 2 digits, 5-AP:", has_kap_int(b97, 5, mx97), "; base 93, 2 digits, 6-AP:", has_kap_int(b93, 6, mx93))
# Pell numbers: gap condition a_j > S_{j-1} + S_{j-2} and no 5-AP in subset sums
P = [1,2,5,12,29,70,169]
S = [0]+list(itertools.accumulate(P))
print("Pell gap condition:", all(P[j] > S[j] + (S[j-1] if j >= 1 else 0) for j in range(len(P))), " no 5-AP:", not has_kap_int(H(P), 5, sum(P)), " has 4-AP:", has_kap_int(H(P), 4, sum(P)))
# A#: 5-AP 0,257,...,1028 and distances
Ash = sorted(b-a for a, b in itertools.combinations([0,4,7,41,257], 2)); hb = H(Ash)
print("A# =", Ash, " S =", sum(Ash), " 5-AP 0..1028:", all((hb >> (257*j)) & 1 for j in range(5)), " |H| =", bin(hb).count('1'))
# the digit set mod 19
Dg = elems(H([1,7,8])); print("D =", Dg, " 4-AP mod 19:", has_kap_mod(Dg, 4, 19))
# f_m and the variance constants
print("f3..f5:", [3**m-2**m for m in (3,4,5)], " f_{m+3}-19f_m = 8*3^m+11*2^m:", all((3**(m+3)-2**(m+3)) - 19*(3**m-2**m) == 8*3**m+11*2**m for m in range(1,40)))
from fractions import Fraction as Fr
kap = lambda m: Fr(8*3**m-3*2**m, 12*(3**m-2**m))
print("16/19-kappa_m formula ok:", all(Fr(16,19)-kap(m) == Fr(5*(8*3**m-27*2**m), 228*(3**m-2**m)) for m in range(1,40)), " kappa_3 =", kap(3))
