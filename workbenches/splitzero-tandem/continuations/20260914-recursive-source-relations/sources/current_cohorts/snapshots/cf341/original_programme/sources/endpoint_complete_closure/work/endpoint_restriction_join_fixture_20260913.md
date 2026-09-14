# Exact lower-source gap and two-pair restriction certificates

This is a complete finite calculation for the explicitly declared auxiliary source below. It joins the lower-source comparison in AU.11–29 to the restriction and trace construction in equations (24), (34), and (47)–(51) of the supplied restriction note. The original coordinate is `S=1+iu`, the relation is `chi(S)=S^2-2S-1`, the quotient has dimension two, and the source mass is exactly `9/16`.

The result is an explicit lower gap `108/763` obtained from a positive source comparison and an exact remainder operator norm. The actual sharp gap is `135/331`. Both apply to the two pairs `(1,3)` and `(2,4)`. Their trace certificates are computed with exact rational logarithm enclosures. These are finite conclusions for this specified source; no estimate for a growing arithmetic quartet family is inferred.

## 1. Source, lower source, and literal masses

For positive integer `lambda` define

\[
r_\lambda(u)=\frac{|\Gamma(\lambda+iu/2)|^2}{2\pi},
\qquad c_\lambda=2^{1-2\lambda}\Gamma(2\lambda).
\]

The measures used here are

\[
w(t)=\left(1+\frac{t^2}{4}\right)r_1(t)=r_2(t),
\quad m=w*w=\frac1{70}r_4,
\quad v=r_1*r_1=\frac13r_2,
\quad d\nu=\frac{54}{35}v(u)\,du.
\tag{F.1}
\]

Here is the measure identity with its constants. Euler's gamma integral gives `Gamma(z+1)=z Gamma(z)` by integration by parts when `Re z>0`. Multiplying this equality by its conjugate proves the first equality in (F.1). The change from two positive gamma-integral variables to their sum and ratio, with Jacobian equal to the sum, gives

\[
\Gamma(a)\Gamma(b)
=\Gamma(a+b)\int_0^1x^{a-1}(1-x)^{b-1}\,dx,
\quad \Re a,\Re b>0.
\]

Set `a=lambda+iu/2`, `b=lambda-iu/2`, and then `x=e^t/(1+e^t)`. This gives

\[
|\Gamma(\lambda+iu/2)|^2
=\Gamma(2\lambda)\int_\mathbb R
       (2\cosh(t/2))^{-2\lambda}e^{iut/2}\,dt.
\]

After `t=2y`, Fourier inversion, with convention `hat f(t)=integral f(u)e^{-itu}du`, proves

\[
\widehat r_\lambda(t)
=2\Gamma(2\lambda)(2\cosh t)^{-2\lambda}
=c_\lambda(\cosh t)^{-2\lambda}.
\tag{F.2}
\]

All inversions and moment differentiations used here are legitimate. The integrand `(2 cosh y)^(-2lambda)` and every derivative decay exponentially on the real axis. For each `0<a<pi/2`, it is holomorphic on the closed strip `|Im y|<=a`; shifting the Fourier integral up or down inside that strip bounds `r_lambda(u)` by a constant times `exp(-a|u|)`. The vertical sides of a rectangular contour tend to zero because the integrand decays exponentially in `|Re y|`, uniformly in that strip. Thus every polynomial moment exists, the Fourier transform extends to imaginary arguments near zero, and its moment-generating function is

\[
\int e^{tu}r_\lambda(u)\,du=c_\lambda(\cos t)^{-2\lambda},
\qquad |t|<\pi/2.
\]

Multiplying (F.2) proves

\[
r_a*r_b=\frac{c_ac_b}{c_{a+b}}r_{a+b}.
\]

The constants are `c_1=1/2`, `c_2=3/4`, and `c_4=315/8`. Consequently the masses of `w,m,v,nu` are respectively

\[
\boxed{\frac34,\quad\frac9{16},\quad\frac14,\quad\frac{27}{70}.}
\tag{F.3}
\]

Two applications of the gamma recurrence give the pointwise identity

\[
m(u)=\left(\frac{54}{35}+\frac{39u^2}{280}
                       +\frac{3u^4}{1120}\right)v(u).
\tag{F.4}
\]

Indeed `r_4/r_2=(4+u^2/4)(9+u^2/4)` and `(r_4/70)/(r_2/3)` multiplies that product by `3/70`. Every coefficient in (F.4) is retained. Since `v(u)>0`, this proves `dnu<=m(u)du` and hence the contraction

\[
\mathbb C[S]_{\le j}\longrightarrow\mathbb C[S]_{\le j},
\quad P\longmapsto P,
\quad \|P\|_\nu^2\le\|P\|_m^2.
\tag{F.5}
\]

The forms in (F.5) integrate `|P(1+iu)|^2`. The polynomial map, quotient map, and original coordinate are unchanged.

The even moments of `m` through degree eight are

\[
(9/16,\ 9/2,\ 117,\ 5472,\ 385272),
\]

and those of `v` are

\[
(1/4,\ 1,\ 14,\ 376,\ 16064).
\tag{F.6}
\]

The `nu` moments are the latter multiplied by `54/35`; all odd moments are zero. These values follow by differentiating the functions in (F.2). The executable constructs them by the equivalent finite multiplication recurrence

\[
u b_j=b_{j+1}+j(j+\alpha-1)b_{j-1},
\qquad \alpha=2\lambda,
\]

starting from `b_0=1`, retaining the coefficient of `b_0` and multiplying by the literal mass. On the finite degrees needed here it also verifies them by two independent constructions: binomial convolution of `(1+t^2/4)r_1` moments, and the full three-term density (F.4). The monic-polynomial orthogonality needed below is verified directly against every Gram entry, so no unchecked infinite recurrence is used as a finite matrix certificate.

## 2. Complete original-coordinate matrices

The polynomial space has ordered basis `1,S,...,S^N`. Its conjugate-linear-first Gram is

\[
(H_N)_{ab}
=\sum_{x=0}^a\sum_{y=0}^b
 \binom ax\binom by(-1)^x i^{x+y}m_{x+y}.
\tag{F.7}
\]

The imaginary terms vanish for the stated even source and are separately accumulated and checked in the executable. The full largest matrices are

\[
H_4=\frac1{16}
\begin{pmatrix}
9&9&-63&-207&1449\\
9&81&81&-1863&-5751\\
-63&81&2025&2025&-89343\\
-207&-1863&2025&93393&93393\\
1449&-5751&-89343&93393&6526089
\end{pmatrix},
\tag{F.8}
\]

\[
H_4^\nu=\frac1{70}
\begin{pmatrix}
27&27&-81&-297&891\\
27&135&135&-1485&-4725\\
-81&135&1755&1755&-41985\\
-297&-1485&1755&45495&45495\\
891&-4725&-41985&45495&1906875
\end{pmatrix}.
\tag{F.9}
\]

Every smaller source form is the corresponding leading principal submatrix. The polynomial relation yields

\[
J_1=I_2,\quad
J_2=\begin{pmatrix}1&0&1\\0&1&2\end{pmatrix},\quad
J_3=\begin{pmatrix}1&0&1&2\\0&1&2&5\end{pmatrix},\quad
J_4=\begin{pmatrix}1&0&1&2&5\\0&1&2&5&12\end{pmatrix}.
\tag{F.10}
\]

These are the maps to coefficients in `E=C[S]/(chi)` with basis `(1,S)`. The recurrence for their columns is `J_{:,a}=2J_{:,a-1}+J_{:,a-2}`, exactly the relation `S^2=2S+1`.

For each degree define

\[
K_N=J_NH_N^{-1}J_N^*,\qquad G_N=K_N^{-1},
\qquad R_N=H_N^{-1}J_N^*G_N,\qquad V_N=\det G_N.
\tag{F.11}
\]

Positivity of the density proves `H_N>0`. Surjectivity of `J_N` proves `K_N>0`. Direct multiplication gives `J_NR_N=I` and `R_N^*H_NR_N=G_N`. For any `z` with `J_Nz=0`, `z^*H_NR_N=z^*J_N^*G_N=0`. Therefore every representative `R_Nx+z` has squared norm `x^*G_Nx+z^*H_Nz`, proving its minimum property on the original quotient fibre.

For transparent scalar calculations introduce the explicitly typed coordinate isomorphism

\[
\mathbb C[x]/(x^2-2)\xrightarrow{\sim}E,
\quad[x]\longmapsto[S-1],\qquad
C=\begin{pmatrix}1&-1\\0&1\end{pmatrix},
\quad (1,S)C=(1,S-1).
\tag{F.12}
\]

Its inverse substitutes `S=x+1`. Its determinant is one. The source observation of `x` is still `iu`, with its sign and phase retained. A quotient form transforms by `G_x=C^*G_SC`; its inverse transforms by `K_x=C^{-1}K_SC^{-*}`. No measure is changed by these identities.

The following finite polynomials and norms follow by substitution into (F.6)–(F.9). They are monic in `S`; writing them in `x=S-1` is only (F.12).

| Degree | Original source polynomial | Squared norm | Remainder in `(1,x)` |
|---:|---|---:|---|
| 0 | `1` | `9/16` | `1` |
| 1 | `x` | `9/2` | `x` |
| 2 | `x^2+8` | `81` | `10` |
| 3 | `x^3+26x` | `2430` | `28x` |
| 4 | `x^4+56x^2+240` | `106920` | `356` |

| Degree | Lower-source polynomial | Squared norm | Remainder in `(1,x)` |
|---:|---|---:|---|
| 0 | `1` | `27/70` | `1` |
| 1 | `x` | `54/35` | `x` |
| 2 | `x^2+4` | `108/7` | `6` |
| 3 | `x^3+14x` | `1944/7` | `16x` |
| 4 | `x^4+32x^2+72` | `7776` | `140` |

Let `P_N` have these original `S` coefficient columns and let `O_N` be the diagonal of their squared norms. The checked identity is the full matrix equation `P_N^*H_NP_N=O_N`. Its inverse and (F.11) give

\[
K_N=(J_NP_N)O_N^{-1}(J_NP_N)^*.
\tag{F.13}
\]

Thus the inverse quotient form is the sum of each listed remainder outer product divided by its original norm. Explicitly,

\[
\begin{aligned}
K_{1,x}&=\operatorname{diag}(16/9,2/9),&
K_{2,x}&=\operatorname{diag}(244/81,2/9),\\
K_{3,x}&=\operatorname{diag}(244/81,662/1215),&
K_{4,x}&=\operatorname{diag}(56102/13365,662/1215),\\
K_{3,x}^\nu&=\operatorname{diag}(133/27,763/486),&
K_{4,x}^\nu&=\operatorname{diag}(3619/486,763/486).
\end{aligned}
\tag{F.14}
\]

The full original-basis matrices and least representatives at all four degrees are included as rational entries in the JSON. Equations (F.8)–(F.11) are their complete finite construction. Their quotient volumes are

\[
V_1=81/32,\quad V_2=729/488,\quad
V_3=98415/161528,\quad V_4=16238475/37139524.
\tag{F.15}
\]

## 3. A proved gap from the exact remainder operator

Let `B=H_1`, the norm on the unique representative of degree below two. In (F.12),

\[
B_x=C^*BC=\operatorname{diag}(9/16,9/2).
\]

Consider the actual remainder operator

\[
\mathcal R_j:(\mathbb C[S]_{\le j},H_j^\nu)
\longrightarrow(\mathbb C[S]_{\le1},B),\qquad
P\longmapsto\operatorname{rem}_\chi P,
\quad j=3,4.
\tag{F.16}
\]

Its coefficient matrix is exactly `J_j`. Its squared norm is the greatest eigenvalue of `B^{1/2}J_j(H_j^nu)^{-1}J_j^*B^{1/2}`. To see this, the substitutions `a=(H_j^nu)^{1/2}v` and `b=B^{1/2}J_jv` transport its norm ratio to the Euclidean operator `B^{1/2}J_j(H_j^nu)^{-1/2}`. For a matrix `L`, its greatest squared singular value is the greatest eigenvalue of `LL^*`: the nonzero spectra of `L^*L` and `LL^*` coincide by the maps `L` and `L^*`, and maximization of the positive Hermitian quadratic form is diagonalization by an orthonormal eigenbasis.

By (F.14), these positive eigenvalues are exactly

\[
\begin{array}{c|cc}
j&\text{first}&\text{second}\\\hline
3&133/48&763/108\\
4&3619/864&763/108.
\end{array}
\]

Both first entries are smaller than the second: the differences are `1855/432` and `2485/864`. Consequently

\[
\boxed{\|\mathcal R_3\|^2=\|\mathcal R_4\|^2=\frac{763}{108}.}
\tag{F.17}
\]

This norm is attained. In the original `S` coefficient basis use

\[
f_3(S)=-\frac{245}{36}+\frac{791}{108}S
                      -\frac79S^2+\frac7{27}S^3,
\qquad f_4=f_3\in\mathbb C[S]_{\le4}.
\tag{F.18}
\]

This is `f_j=(H_j^nu)^{-1}J_j^*B(-1,1)^T`; the two expressions agree by direct multiplication of the matrices (F.8)–(F.10). The norm and remainder norm are

\[
\|f_j\|_\nu^2=\frac{763}{24},\qquad
\|\operatorname{rem}_\chi f_j\|_B^2=\frac{582169}{2592},
\]

whose ratio is `763/108`. This supplies a concrete extremizing polynomial, in addition to the complete matrix certificate

\[
\frac{763}{108}H_j^\nu-J_j^*BJ_j\succeq0.
\tag{F.19}
\]

The JSON records every principal minor of (F.19), including its zero minors. For a Hermitian matrix, nonnegativity of all principal minors implies positive semidefiniteness: the coefficients of `det(tI+A)` are the sums of its principal minors of each size, so this polynomial is strictly positive for `t>0`; a negative eigenvalue of `A` would give a positive root. This proves the exact PSD validation criterion used here without a floating-point eigenvalue.

The source contraction (F.5) now gives

\[
\|\operatorname{rem}_\chi P\|_B^2
\le\frac{763}{108}\|P\|_\nu^2
\le\frac{763}{108}\|P\|_m^2.
\tag{F.20}
\]

Apply this to the actual least representative `R_jx`. Its remainder is `x`, so

\[
G_j\succeq\frac{108}{763}B.
\]

The degree-one remainder is an admitted representative for every `i>=1`, hence `G_i<=B` by the minimum property. Therefore for `(i,j)=(1,3),(2,4)`,

\[
\boxed{G_j\succeq\frac{108}{763}G_i,
\qquad K_i\succeq\frac{108}{763}K_j.}
\tag{F.21}
\]

The inverse inequality follows by conjugating the first by `G_i^{-1/2}`, inverting its positive eigenvalues, and transporting back. The gap `108/763` is thus obtained from the explicitly proved source comparison and exact remainder norm. Its construction uses the low-degree actual form `B` and the declared comparison moments through degree eight.

## 4. Restriction in the original polynomial coordinates

Define the typed restriction on the same quotient by

\[
T_{i,j}:(E,G_j)\longrightarrow(E,G_i),\qquad T_{i,j}=K_iG_j.
\tag{F.22}
\]

For `x,y in E`, `x^*G_jy=x^*G_iT_{i,j}y`; this proves it is the adjoint of identity transport `(E,G_i)->(E,G_j)`. In the original `(1,S)` coordinates the two return maps are

\[
T_{1,3}=\begin{pmatrix}36/61&3681/20191\\0&135/331\end{pmatrix},
\quad
T_{2,4}=\begin{pmatrix}20130/28051&2876145/9284881\\0&135/331\end{pmatrix}.
\tag{F.23}
\]

The coordinate matrices in (F.12) diagonalize these endomorphisms by `T_x=C^{-1}T_SC`, giving spectra

\[
\{36/61,135/331\},\qquad\{20130/28051,135/331\}.
\tag{F.24}
\]

Both eigenvalues in each pair lie in `(0,1)`. The smallest is `135/331` for both pairs, and hence this is the exact best scalar in `K_i>=gK_j` for these actual source forms. It is stronger than (F.21), through the strictly positive difference `135/331-108/763`.

Let `L_{i,j}` pad original polynomial coefficients with zeros. Since `P_j^*H_jP_j=O_j`, the orthogonal projection from degree `j` to degrees at most `i` is the endomorphism

\[
Q_{i,j}=P_j\operatorname{diag}(\underbrace{1,\ldots,1}_{i+1},0,\ldots,0)P_j^{-1}.
\tag{F.25}
\]

Its range is `L_{i,j}P_i`; direct multiplication proves `Q^2=Q` and `Q^*H_j=H_jQ`. In the two original `S` coordinate spaces these are

\[
Q_{1,3}=\begin{pmatrix}
1&0&-9&0\\0&1&2&-23\\0&0&0&0\\0&0&0&0
\end{pmatrix},
\]

\[
Q_{2,4}=\begin{pmatrix}
1&0&0&27&-189\\0&1&0&-29&0\\0&0&1&3&-50\\
0&0&0&0&0\\0&0&0&0&0
\end{pmatrix}.
\tag{F.26}
\]

In monic polynomial coordinates the first `i+1` rows of the degree-`j` least lift are `O_i^{-1}(J_iP_i)^*G_j`; multiplication of the degree-`i` lift by `T_{i,j}` gives precisely that expression because `G_iK_i=I`. Transporting by the original coefficient matrices therefore proves

\[
\boxed{L_{i,j}R_iT_{i,j}=Q_{i,j}R_j.}
\tag{F.27}
\]

Its Gram is `G_jK_iG_j`. For an eigenvector `v` of `T` with eigenvalue `g`, this becomes

\[
\frac{\|Q_{i,j}R_jv\|_{H_j}^2}{\|R_jv\|_{H_j}^2}=g,
\quad
\frac{\|(I-Q_{i,j})R_jv\|_{H_j}^2}{\|R_jv\|_{H_j}^2}=1-g.
\tag{F.28}
\]

The second equation follows from orthogonal decomposition by (F.25). The same original representative determines both quantities.

Writing `D=L_{i,j}R_i-R_j` and `H=I-T_{i,j}`, equation (F.27) gives the exact correction

\[
D=L_{i,j}R_iH-(I-Q_{i,j})R_j,
\quad J_jD=0,
\quad D^*H_jD=G_i-G_j.
\tag{F.29}
\]

The remainder equation follows from `J_jL_{i,j}R_i=J_jR_j=I`. For the Gram identity, `R_j` is orthogonal to every relation in `ker J_j` by (F.11), so `L_{i,j}R_i=R_j+D` is an orthogonal sum. The return maps compose by `K_iG_jK_jG_l=K_iG_l`.

The quotient multiplication action is retained as

\[
A=\begin{pmatrix}0&1\\1&2\end{pmatrix}.
\]

For `W_N=A^*G_N+G_NA-2G_N` and `mathsf H_N=K_NW_N`, expansion gives

\[
AT-TA=\mathsf H_iT-T\mathsf H_j.
\tag{F.30}
\]

Indeed the two terms `K_i A^*G_j` and the two terms `2K_iG_j` cancel. This records the exact action defect of the return map. Each finite matrix equation (F.27), (F.29), and (F.30) is checked in the literal original coordinates.

## 5. Full finite logarithmic certificates

The determinant identity in (F.22) is

\[
\det T_{i,j}=V_j/V_i.
\]

Since the two positive eigenvalues are (F.24), put `s_a=Tr(I-T)^a`. Expansion of `-log g=sum_{a>=1}(1-g)^a/a` proves

\[
\mathcal L_{i,j}=\log(V_i/V_j)=\sum_{a\ge1}\frac{s_a}{a}.
\tag{F.31}
\]

For any of the proved lower gaps `g_0`, let `r=1-g_0`. Each loss eigenvalue `x=1-g` satisfies `0<=x<=r<1`. The exact tail comparison is

\[
\sum_{a=p+1}^\infty\frac{x^a}{a}
=x^{p+1}\sum_{a=p+1}^\infty\frac{x^{a-p-1}}a
\le x^{p+1}\frac{-\log g_0-\sum_{a=1}^p r^a/a}{r^{p+1}}.
\]

Thus

\[
\sum_{a=1}^p\frac{s_a}{a}\le\mathcal L_{i,j}
\le U_p(H,g_0):=\sum_{a=1}^p\frac{s_a}{a}
+\frac{-\log g_0-\sum_{a=1}^p r^a/a}{r^{p+1}}s_{p+1}.
\tag{F.32}
\]

For these finite pairs, the executable computes every trace through power six directly by matrix multiplication and independently from the rational spectrum. Its exact first three values are:

| Pair | `s_1` | `s_2` | `s_3` |
|---|---:|---:|---:|
| `(1,3)` | `20231/20191` | `211421561/407676481` | `2275697407691/8231395827871` |
| `(2,4)` | `8119847/9284881` | `37102062682217/86209015184161` | `184216076205697661987/800440447112127969841` |

The two determinant ratios and their product are

\[
\frac{V_1}{V_3}=\frac{20191}{4860},\quad
\frac{V_2}{V_4}=\frac{9284881}{2717550},\quad
\boxed{\frac{V_1V_2}{V_3V_4}=\frac{3073295611}{216513000}.}
\tag{F.33}
\]

All logarithms in (F.31)–(F.32) have rational arguments. The executable uses exact rational enclosures. For `1<=y<=2`, put `t=(y-1)/(y+1)`. Integrating the geometric series `2/(1-t^2)=2 sum_{a>=0}t^(2a)` from zero gives

\[
2\sum_{a=0}^{M-1}\frac{t^{2a+1}}{2a+1}
\le\log y\le
2\sum_{a=0}^{M-1}\frac{t^{2a+1}}{2a+1}
+\frac{2t^{2M+1}}{(2M+1)(1-t^2)}.
\tag{F.34}
\]

The upper tail follows by replacing all positive denominators by the first denominator and summing the geometric series. For `z>=1`, finite multiplication writes `z=2^e y` with `1<=y<2`, and `log z=e log 2+log y` transports the two intervals. For `z<1`, `log z=-log(1/z)` reverses interval endpoints. These are exact scalar logarithm identities; the source measures remain (F.1). The script uses `M=90`, checks loss widths below `10^-70`, and checks certificate widths below `10^-65`. Every enclosure endpoint and exact tail coefficient is retained in the JSON.

For a compact rational display, all following intervals have denominator `10^15`. Their endpoints were obtained by outward integer rounding of the saved exact fractions, retaining the correct inequalities:

| Quantity | Lower numerator | Upper numerator |
|---|---:|---:|
| `log(V_1 V_2/(V_3 V_4))` | `2652855161899890` | `2652855161899891` |
| Sum of `p=2` upper certificates using `108/763` | `2934134222167925` | `2934134222167926` |
| Sum of `p=2` upper certificates using `135/331` | `2666680039877747` | `2666680039877748` |

The exact old direct trace bound is

\[
\operatorname{Tr}(G_1(K_3-K_1))+
\operatorname{Tr}(G_2(K_4-K_2))
=\frac{1159}{540}+\frac{334321}{181170}
=\frac{1446331}{362340}.
\tag{F.35}
\]

To prove it bounds the loss, diagonalize `G_i^{1/2}K_jG_i^{1/2}`, whose eigenvalues are `1/g`; the scalar inequality `log x<=x-1` for `x>=1` follows by integrating `1/t<=1` from one. Summing gives (F.35). Exact rational comparison verifies that each new `p=2` total upper bound is strictly below (F.35), and that the sharp-gap certificate is strictly below the lower-source-gap certificate.

The cost of using the explicit lower-source gap can also be inspected pair by pair. The intervals below again have denominator `10^15` and enclose the excess `U_2-mathcal L`:

| Pair and gap | Lower numerator | Upper numerator |
|---|---:|---:|
| `(1,3)`, lower-source `108/763` | `155314375058502` | `155314375058503` |
| `(2,4)`, lower-source `108/763` | `125964685209532` | `125964685209533` |
| `(1,3)`, actual `135/331` | `9359847652264` | `9359847652265` |
| `(2,4)`, actual `135/331` | `4465030325591` | `4465030325592` |

The script additionally computes the exact (F.32) enclosures for `p=1,3,5`. Each is checked against the independently enclosed determinant logarithm. These finitely many calculations make no claim about a uniform gap in a tensor-degree limit.

## 6. Complete executable replay and provenance

Only these three files were authored for this lane:

- `endpoint_restriction_join_fixture_20260913.py`: complete standard-library rational calculation and subprocess driver.
- `endpoint_restriction_join_fixture_20260913.json`: all matrices, principal minors, witnesses, trace coefficients, logarithm enclosures, check labels, full stdout/stderr, actual commands, timings, return codes, and hashes for every subprocess.
- This Markdown proof and local continuity record.

The complete positive run contains **303 distinct mathematical checks**. The driver ran the positive calculation and seven changed calculations in both ordinary Python and `python -O`: **16 actual complete subprocess jobs**. Every job reaches all 303 checks. Assertions are not used as tests, and no changed computation is rejected by a startup guard or deliberately raised exception. The changed computations fail at the following counts, identically in both modes:

| Changed calculation | Failed checks |
|---|---:|
| Set the actual source mass to one | 20 |
| Set the lower-source mass to one | 30 |
| Replace `K_iG_j` by the reverse `K_jG_i` | 36 |
| Truncate original monomial coefficients in place of the orthogonal projection | 8 |
| Use the smaller comparison eigenvalue as the remainder norm cap | 24 |
| Replace trace of a power by power of the trace | 23 |
| Use denominator `r^p` in place of `r^(p+1)` in the logarithmic tail coefficient | 24 |

Each unchanged run has zero failures and exit code zero; each changed run has the listed positive failure count and exit code one. The driver separately checks full counts, unique labels, outcomes, return codes, empty stderr, and equality of complete result objects between ordinary and optimized modes. These execution/provenance checks and repeated runs do not increase the count of distinct mathematical checks.

The mathematical inputs were read completely before construction:

- `arithmetic_volume_upper_route_20260913.tex`, SHA256 `21aaedc3585887fa7d2cb3e37e68d14415829a4b213566f7a08f4619835ef38b`.
- Supplied `Tau_Endpoint_Restriction_Control/NOTE.tex`, SHA256 `ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6`.
- Earlier auxiliary-source proof `gamma_endpoint_window_bridge_fixture_20260913.md`, SHA256 `05108b93cfd1e15e782f171f37569e3d77c8c4775b1bf8349f4021a0eb4315ed`.

No existing executable was imported into this fixture. An independent mathematical reviewer derived the same source moments, remainder kernels, comparison eigenvalues, both original-coordinate return matrices, and exact trace values without importing this script or writing files.

The completed independent read-only audit found no defect. It read all 415 script lines and inspected the normal result and all 16 replay outcomes. Its separate calculation passed **170 audit predicates** without importing or running this fixture script. It reconstructed the original `S` Grams, all four kernels and least lifts, and the projections directly from `L H_i^{-1} L^* H_j`, independently of the monic-basis implementation. It verified the extremizer (F.18), all six trace powers, and the four `p=2` certificates. A separate 1,024-term rational logarithm series without range reduction produced intervals contained in every audited saved logarithm/certificate interval. Every stdout/stderr hash, Windows CRLF reconstruction, unique check label, complete job count, return code, and ordinary/optimized equality matched; all 88 driver provenance checks passed. These 170 audit predicates remain separate from the fixture's 303 mathematical checks. The reviewer wrote no files.

Final executable SHA256: `88bcee664a3812dd914e5d164de37d48f4388307e2359062ace360e988d9df14`.

Final replay JSON SHA256: `a8205b83417feb94baf903f53f9bdd0d2e38cf325fc28ceaac6a098530b4075d`.

### Assigned work, verbatim

> New bounded independent task while I derive restriction-AU join: read full work/arithmetic_volume_upper_route_20260913.tex and new restriction full NOTE once intake path available (ask root/arithmetic_endpoint_intake). Construct meaningful exact rational fixtures validating two-pair restriction T=KiGj, projection, spectral trace finite upper certificate, explicit remainder-comparator g0 for (q-1,2q-1),(q,2q), retaining literal source mass. Prefer existing EW auxiliary source S=1+iu chi=S²−2S−1,mass9/16, or actual new Gaussian nilpotent mass7. Do full derivation of finite g0 from exact polynomial remainder norm and source lower form, and compare bound's gap and trace certificate. Send formulas early; only new work/endpoint_restriction_join_fixture_20260913.{py,md,json} files. Full exact output, actual complete mutations not assertions, independent ordinary+optimized if apt. No edits to frozen files, no Lean or publication. Do not assume a uniform gap.

The selected source is the first explicit option. The parent received early exact comparator and spectral formulas, followed by the replay counts and upper-bound comparison. Existing frozen files, inherited intake checks, Lean calculations, and publication are outside this independent lane and were not changed.
