# Exact coefficient bound for the original prime-power window

For the original von Mangoldt function, including every prime power, define
\[
S(a)=\sum_{\substack{n\ge2\\|\log n-a|\le1/32}}
\frac{\Lambda(n)}{\sqrt n},
\qquad \frac{583}{800}\le a\le\log256.
\tag{FPC1}
\]
All logarithms are natural. The exact maximum on this entire real interval is
\[
\boxed{
\max_a S(a)=M_*:=
\frac{\log227}{\sqrt{227}}+
\frac{\log229}{\sqrt{229}}+
\frac{\log233}{\sqrt{233}}+
\frac{\log239}{\sqrt{239}}+
\frac{\log241}{\sqrt{241}}.
}
\tag{FPC2}
\]
Its certified rational enclosure is
\[
\frac{1783796246}{10^9}<M_*<\frac{1783796247}{10^9}
<\boxed{\frac{223}{125}}<2.
\tag{FPC3}
\]
This calculation is finite arithmetic. It does not evaluate or truncate any zeta-zero sum.

## The exact finite range and ratio reduction

For \(0<x<1\), comparison of the exponential series with the geometric series gives \(e^x<1/(1-x)\). Therefore
\[
n\le e^{a+1/32}\le256e^{1/32}
<256\frac{32}{31}=\frac{8192}{31}<265.
\tag{FPC4}
\]
Thus all contributing indices satisfy \(n\le264\). Both primes 257 and 263 must be retained. In fact \(e^{1/32}>1+1/32\) gives \(256e^{1/32}>264\), so the exact integer upper cutoff is 264.

The first index 2 never occurs. The elementary logarithm series gives
\[
\log2=2\sum_{j\ge0}\frac{(1/3)^{2j+1}}{2j+1}
<\frac23+\frac{2(1/3)^3}{3(1-1/9)}
=\frac{25}{36}<\frac{279}{400}
=\frac{583}{800}-\frac1{32}.
\tag{FPC5}
\]
The strict series bound follows because each denominator after the first term is at least 3, and those after that are strictly larger. Non-prime-power indices have coefficient zero and are preserved with that numerical value.

Any two indices \(m\le n\) in the same window obey
\[
\frac nm\le e^{1/16}<\frac{16}{15}.
\tag{FPC6}
\]
Let \(\mathcal P\) be the set of all prime powers at most 264. If a window has a nonzero coefficient, let \(m\ge3\) be its smallest contributing prime power. Its contribution is bounded above by the full positive sum on the exact rational superset
\[
U_m=\{n\in\mathcal P:m\le n,\ 15n<16m\}.
\tag{FPC7}
\]
This leaves exactly 71 cases, one for each member of \(\mathcal P\setminus\{2\}\). A window containing no prime power has value zero.

## Rational bounds for every individual weight

The companion checker uses integer arithmetic, exact fractions, and integer square roots. It uses no floating-point value of a logarithm, exponential, square root, or zero of zeta.

For \(0\le z\le1/3\), integrating a finite geometric expansion of \(2/(1-z^2)\) proves
\[
L_N(z):=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}
\le \log\frac{1+z}{1-z}
\le L_N(z)+\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\tag{FPC8}
\]
Use \(N=16\). For an integer prime \(p\), put \(k=\lfloor\log_2p\rfloor\), evaluated by its integer bit length, and
\[
z_p=\frac{p-2^k}{p+2^k}\in[0,1/3).
\]
Then
\[
\log p=k\log2+\log\frac{1+z_p}{1-z_p}.
\tag{FPC9}
\]
Apply FPC8 to both logarithms, and round the lower bound down and the upper bound up to denominator \(10^{12}\). Denote the resulting rational bounds by \(\lambda_p^-\) and \(\lambda_p^+\).

For each prime power \(n=p^j\), compute the integer
\[
b_n=\operatorname{isqrt}(n\,10^{18}).
\]
Set \(r_n^-=b_n/10^9\). If \(b_n^2=n10^{18}\), set \(r_n^+=r_n^-\); otherwise set \(r_n^+=(b_n+1)/10^9\). By the defining integer-square-root inequalities,
\[
(r_n^-)^2\le n\le(r_n^+)^2,
\qquad
\frac{\lambda_p^-}{r_n^+}
\le\frac{\Lambda(n)}{\sqrt n}
\le\frac{\lambda_p^+}{r_n^-}.
\tag{FPC10}
\]
Every denominator is positive. The checker records all 72 prime-power indices, their prime bases, and all six rational log, square-root, and weight bounds in the accompanying JSON.

The enumeration itself is exhaustive: trial division through the integer square root decides every prime \(p\le264\), and repeated integer multiplication generates every \(p^j\le264\). Every prime power has exactly one such prime base. The complete resulting set has 72 members, including \(243=3^5\), \(256=2^8\), 257 and 263.

## The complete finite comparison and attainment

Adding the upper bounds in FPC10 on each exact set FPC7 yields the following certified comparisons:
\[
\sum_{n\in U_m}\frac{\Lambda(n)}{\sqrt n}
<\frac{1511}{1000}\quad(m\ne227),
\tag{FPC11}
\]
whereas
\[
U_{227}=\{227,229,233,239,241\},
\quad
\frac{1783796246}{10^9}<M_*<\frac{1783796247}{10^9}.
\tag{FPC12}
\]
The lower bound in FPC12 exceeds \(1511/1000\), so this proves the maximum over all 71 supersets exactly. These are exact rational comparisons, not decimal estimates. Their full fractions and all constituent indices are provided in the JSON. The full 71-case table displays each packet and an outward-rounded upper bound with denominator \(10^9\).

Selected packet bounds, including the packet containing 257 and 263, are

| Minimum | Complete ratio packet | Certified upper bound |
|---:|:---|---:|
| 227 | 227, 229, 233, 239, 241 | \(1783796247/10^9\) |
| 191 | 191, 193, 197, 199 | \(1510503007/10^9\) |
| 229 | 229, 233, 239, 241, 243 | \(1494205679/10^9\) |
| 251 | 251, 256, 257, 263 | \(1081820789/10^9\) |

The superset maximum occurs in an actual window of the original width. Choose
\[
a_*^{\rm win}=\frac{\log227+\log241}{2}.
\tag{FPC13}
\]
For every prime in the displayed five-prime packet,
\[
|\log p-a_*^{\rm win}|
\le\frac12\log\frac{241}{227}
<\frac12\frac{14}{227}<\frac1{32}.
\tag{FPC14}
\]
Here \(\log(1+x)<x\), and \(224<227\) proves the final rational inequality. Also \(227\cdot241<256^2\), so \(a_*^{\rm win}<\log256\). For the lower endpoint, \(\log227>\log4=2\log2>4/3>583/800\), using the first positive term of the logarithm series. Thus FPC13 is admissible. Its window contains the whole five-prime packet, while FPC11–FPC12 already exclude any larger sum. It attains exactly \(M_*\), proving FPC2 and the uniform bound FPC3.

## Reproduction files

- `check_finite_prime_window_coefficients.py`: the complete rational-only enumeration and all asserted comparisons.
- `FINITE_PRIME_WINDOW_COEFFICIENT_CERTIFICATE.json`: every individual rational enclosure and every one of the 71 packet sums.
- `FINITE_PRIME_WINDOW_PACKETS.md`: the complete human-readable packet table, with rational upper bounds.

Run the Python checker in this directory. It reproduces the JSON and the complete packet table, and fails if any stated comparison fails. The exact maximum is the symbolic sum FPC2; its rational enclosure is FPC3. No source window, prime-power coefficient, or endpoint has been replaced.


# Exact rational packet table

Each upper bound is the displayed integer divided by $10^9$. It is an outward rounding of the exact upper fraction in the companion JSON.

| Minimum prime power | All prime powers in its ratio superset | Upper numerator over $10^9$ |
|---:|:---|---:|
| 3 | 3 | 634284101 |
| 4 | 4 | 346573591 |
| 5 | 5 | 719762516 |
| 7 | 7 | 735484905 |
| 8 | 8 | 245064536 |
| 9 | 9 | 366204097 |
| 11 | 11 | 722992628 |
| 13 | 13 | 711388957 |
| 16 | 16, 17 | 860441965 |
| 17 | 17 | 687155170 |
| 19 | 19 | 675500630 |
| 23 | 23 | 653795740 |
| 25 | 25 | 321887583 |
| 27 | 27 | 211428034 |
| 29 | 29 | 625291138 |
| 31 | 31, 32 | 739294578 |
| 32 | 32 | 122532268 |
| 37 | 37 | 593631249 |
| 41 | 41, 43 | 1153540161 |
| 43 | 43 | 573577641 |
| 47 | 47, 49 | 839588912 |
| 49 | 49 | 277987165 |
| 53 | 53 | 545361537 |
| 59 | 59, 61 | 1057193623 |
| 61 | 61, 64 | 612986861 |
| 64 | 64, 67 | 600328359 |
| 67 | 67, 71 | 1019571991 |
| 71 | 71, 73 | 1008047325 |
| 73 | 73 | 502160296 |
| 79 | 79, 81, 83 | 1098700093 |
| 81 | 81, 83 | 607098802 |
| 83 | 83 | 485030770 |
| 89 | 89 | 475794504 |
| 97 | 97, 101, 103 | 1380386597 |
| 101 | 101, 103, 107 | 1367634487 |
| 103 | 103, 107, 109 | 1357762463 |
| 107 | 107, 109, 113 | 1345804284 |
| 109 | 109, 113 | 894064869 |
| 113 | 113 | 444715238 |
| 121 | 121, 125, 127, 128 | 853061211 |
| 125 | 125, 127, 128, 131 | 1061018700 |
| 127 | 127, 128, 131 | 917066197 |
| 128 | 128, 131 | 487214102 |
| 131 | 131, 137, 139 | 1264826923 |
| 137 | 137, 139 | 838878955 |
| 139 | 139 | 418536617 |
| 149 | 149, 151, 157 | 1221772044 |
| 151 | 151, 157 | 811832789 |
| 157 | 157, 163, 167 | 1198547906 |
| 163 | 163, 167, 169, 173 | 1384116861 |
| 167 | 167, 169, 173 | 985143554 |
| 169 | 169, 173, 179 | 976824721 |
| 173 | 173, 179, 181 | 1165922166 |
| 179 | 179, 181 | 774124661 |
| 181 | 181, 191, 193 | 1145259138 |
| 191 | 191, 193, 197, 199 | 1510503007 |
| 193 | 193, 197, 199 | 1130461840 |
| 197 | 197, 199 | 751645111 |
| 199 | 199, 211 | 743669539 |
| 211 | 211, 223 | 730528112 |
| 223 | 223, 227, 229, 233 | 1438337443 |
| 227 | 227, 229, 233, 239, 241 | 1783796247 |
| 229 | 229, 233, 239, 241, 243 | 1494205679 |
| 233 | 233, 239, 241, 243 | 1135135222 |
| 239 | 239, 241, 243, 251 | 1126789316 |
| 241 | 241, 243, 251, 256, 257 | 1162009892 |
| 243 | 243, 251, 256, 257 | 808703063 |
| 251 | 251, 256, 257, 263 | 1081820789 |
| 256 | 256, 257, 263 | 733057292 |
| 257 | 257, 263 | 689735593 |
| 263 | 263 | 343593738 |
