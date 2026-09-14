# Paired root arguments and a complete finite coefficient certificate

This supplement leaves the earlier 416-check fixture and its receipt unchanged. It directly checks the two rational identities in EW.21, then constructs a complete coefficient-interval-to-endpoint certificate for the explicitly specified auxiliary positive multiplier below. The supplementary script depends on the pinned earlier script for exact rational matrix operations and positive-root enclosure, and reads the pinned earlier receipt for its fifteen saved positive windows. Both dependency hashes are checked during every execution.

The written mathematical source is `gamma_endpoint_window_bridge_20260913.tex`, particularly EW.21 and EW.37–EW.45. Every input in the present calculation is rational, including all masses, the original relation polynomial, and the two nonzero one-factor coefficient radii. This is a finite auxiliary Gamma measure calculation, with no assertion about unprovided arithmetic coefficient intervals.

## 1. Direct checks of the two paired root arguments

For each saved window `2 <= n < n+r <= 7`, retain the original Schur block `W` of size `r+1`, its quotient correction `Z=F*G_(n-1)F`, and their leading `r` by `r` blocks `W_r,Z_r`. Define

\[
 p=\det W_r,\quad s=\det W,\quad w=W_{00},\quad
 e=w+Z_{00},\quad D=\det(W_r+Z_r)\det(W+Z).
\]

The supplementary calculation computes these five scalars from the stored matrix entries. It compares the following expressions with the separately stored original monic norm ratio `U` and four-volume ratio `R`:

\[
 \frac{D}{p^2e}=U\mathcal R,
 \qquad
 \frac{s^2e}{w^2D}=\frac U{\mathcal R}.
\]

These are thirty direct exact rational equalities over the fifteen windows. Their proof uses the previously established identities, with all original coordinates retained:

\[
 U=\frac{s}{pw},\qquad
 \mathcal R=\frac{Dw}{pse}.
\]

Multiplying these two displayed fractions gives the first expression. Dividing the first fraction by the second gives the second expression. Every denominator is positive because `W` and its prefix are positive definite, `Z` is positive semidefinite, and `w>0`.

The selected values computed directly from the full matrices are:

| (n,r) | p | s | w | e | D |
|---|---:|---:|---:|---:|---:|
| (2,1) | 81 | 196830 | 81 | 549/4 | 897873579/8 |
| (2,2) | 196830 | 21045063600 | 81 | 549/4 | 99629792861132511 |
| (3,2) | 259815600 | 1666769037120000 | 2430 | 5958 | 32381243389082649334965649920/3721 |

Their resulting pairs `(U R,U/R)` are respectively

\[
 \left(\frac{20191}{162},\frac{145800}{20191}\right),\quad
 \left(\frac{3073295611}{164025},\frac{285797160000}{3073295611}\right),\quad
 \left(\frac{295913127219469}{13676070375},
       \frac{95316740085600000}{295913127219469}\right).
\]

Every corresponding value for the other twelve windows is stored in the supplementary receipt.

## 2. The original finite coefficient box and an interior positive multiplier

Set

\[
 \lambda=1,\quad k=2,\quad c=k/2=1,\quad c_\lambda=\frac12,
 \quad C_k=\frac14,\quad n=2,\quad r=1,\quad m=n+r=3,
\]

\[
 \chi(S)=(S-1)^2-2=S^2-2S-1,\qquad q=2,\qquad
 \epsilon=10^{-12}.
\]

For the positive multiplier `A+B t^2`, the monic Gamma polynomial `b_2^(1)=t^2-2` gives the exact coefficient expansion

\[
 A+Bt^2=(A+2B)b_0^{(1)}+B b_2^{(1)}.
\]

Thus `c_0=A+2B`, `c_2=B`, and every other coefficient is exactly zero. The coefficient centre and radii, through the complete required degree `2m=6`, are

\[
 \widehat c=(3/2,0,1/4,0,0,0,0),\qquad
 e=(\epsilon,0,\epsilon,0,0,0,0).
\]

The specified interior actual multiplier has

\[
 A=1+\epsilon,\qquad B=\frac14-\frac\epsilon4,
\]

\[
 c_0=\frac32+\frac\epsilon2,
 \qquad c_2=\frac14-\frac\epsilon4.
\]

Both coefficients lie strictly inside their respective nonzero intervals. Also `A>0` and `B>0`, so this actual multiplier is positive everywhere. In fact every point of the coefficient box describes a positive multiplier: `B=c_2 >= 1/4-epsilon>0` and `A=c_0-2c_2 >= 1-3 epsilon>0`. Multiplication by a polynomial preserves every Gamma polynomial moment and belongs to `L^2(r_1 dt)` because the Gamma reference has exponential tails.

The one-factor reference remains

\[
 r_1(t)=\frac{|\Gamma(1+it/2)|^2}{2\pi},\qquad \int r_1=\frac12.
\]

The actual one-factor weighted mass and the literal sum mass are

\[
 \mu_0(w)=\frac34+\frac\epsilon4,\qquad
 \mu_0(w*w)=\left(\frac34+\frac\epsilon4\right)^2.
\]

Neither mass is reassigned to one.

## 3. Complete tensor coefficient radii

Here `alpha=2`, so `(alpha)_j=(j+1)!`. The central generating polynomial and the nonnegative error polynomial are

\[
 \widehat A(z)=\frac32+\frac32z^2,
 \qquad E_+(z)=\epsilon+6\epsilon z^2.
\]

The central coefficients are nonnegative, so `A_+=widehat A`. EW.37 gives

\[
 e_j^{(2)}=[z^j]\bigl((\widehat A+E_+)^2-\widehat A^2\bigr).
\]

Expanding the two factors completely gives

\[
 e_0^{(2)}=3\epsilon+\epsilon^2,\qquad
 e_2^{(2)}=21\epsilon+12\epsilon^2,\qquad
 e_4^{(2)}=18\epsilon+36\epsilon^2,
\]

and every other degree through six has radius exactly zero. The terms quadratic in `epsilon` are retained.

For the specified interior input, its generating polynomial is

\[
 A_{\rm actual}(z)=\frac32+\frac\epsilon2
                  +\left(\frac32-\frac{3\epsilon}2\right)z^2.
\]

Its square has the exact nonzero coefficients

\[
 \begin{aligned}
 d_0&=\frac94+\frac{3\epsilon}2+\frac{\epsilon^2}4,\\
 d_2&=\frac92-3\epsilon-\frac{3\epsilon^2}2,\\
 d_4&=\frac94-\frac{9\epsilon}2+\frac{9\epsilon^2}4.
 \end{aligned}
\]

The script verifies their enclosure degree by degree. It also constructs all four coefficient-box corners independently, converts each back to its positive `A,B`, and computes each actual convolution. The corner with both `c_0,c_2` increased by `epsilon` attains all three positive tensor coefficient radii. This supplies concrete tests of the quadratic error terms in addition to the multinomial proof.

## 4. Monic test expansion and independent original-S Gram

The sum reference has parameter `k lambda=2`, mass `C_k=1/4`, and monic polynomials generated exactly by

\[
 b_0=1,\quad b_1=u,\quad
 b_{j+1}=u b_j-j(j+3)b_{j-1}.
\]

For each `0 <= a,b <= 3`, first expand the full complex polynomial

\[
 (1-iu)^a(1+iu)^b
 =\sum_{\ell=0}^a\sum_{j=0}^b
 \binom a\ell\binom bj(-1)^\ell i^{\ell+j}u^{\ell+j}.
\]

The program separately preserves its real and imaginary coefficient vectors. It then subtracts the leading coefficient times the monic `b_j`, descending from degree six to degree zero. This finite algorithm terminates with zero remainder, which is checked separately for every test. Its result is the full complex vector `L_(ab,j)` satisfying

\[
 (1-iu)^a(1+iu)^b=\sum_{j=0}^6 L_{ab,j}b_j(u).
\]

The real part has only even indices and the imaginary part only odd indices, as checked in all sixteen tests. The density is even and every odd `d_j` is exactly zero. Thus its imaginary test integral vanishes exactly, with no bound or discarded phase replacing that identity.

The coefficient-side Gram and its rational entry radii are

\[
 \widehat H_{ab}=\frac14\sum_{j=0}^6j!L_{ab,j}\widehat d_j,
 \qquad
 \varepsilon_{ab}=\frac14\sum_{j=0}^6j!|L_{ab,j}|e_j^{(2)}.
\]

For these tests each coefficient is purely real or purely imaginary. Therefore its modulus is the absolute value of its nonzero coordinate; the program's rational bound `abs(real)+abs(imag)` is exact here. The full conjugation of the first original factor is retained.

Independently, the program constructs one-factor moments from the reference Jacobi recurrence with parameter `1` and mass `1/2`. If `rho_j` are those moments, multiplication by the actual multiplier gives `w_j=A rho_j+B rho_(j+2)`. It then uses the complete binomial sum

\[
 \mu_j=\sum_{\ell=0}^j\binom j\ell w_\ell w_{j-\ell}.
\]

For the specified actual input the moments required for `H_3` are exactly

\[
 \begin{aligned}
 \mu_0&=\frac9{16}+\frac{3\epsilon}8+\frac{\epsilon^2}{16},\\
 \mu_2&=\frac92-\frac{\epsilon^2}2,\\
 \mu_4&=117-54\epsilon-7\epsilon^2,\\
 \mu_6&=5472-4320\epsilon+352\epsilon^2,
 \end{aligned}
\]

with odd moments zero. Expanding the same full complex original-S tests against these moments gives a second Gram construction. The script compares every one of its sixteen entries with the coefficient-side calculation, for both centre and actual input. It also compares all seven measured Gamma-polynomial moments with `(1/4)j!d_j`.

The central matrix is the original

\[
 H_0=\frac1{16}\begin{pmatrix}
 9&9&-63&-207\\9&81&81&-1863\\
 -63&81&2025&2025\\-207&-1863&2025&93393
 \end{pmatrix}.
\]

The actual matrix, in precisely these coordinates, is

\[
 H_{\rm actual}=H_0+\epsilon H_1+\epsilon^2H_2,
\]

\[
 H_1=\frac18\begin{pmatrix}
 3&3&3&3\\3&3&3&435\\3&3&-429&-429\\
 3&435&-429&-35853
 \end{pmatrix},\qquad
 H_2=\frac1{16}\begin{pmatrix}
 1&1&9&25\\1&-7&-7&113\\9&-7&-127&-127\\
 25&113&-127&5273
 \end{pmatrix}.
\]

This gives every actual entry as an explicit rational number after substituting the specified `epsilon`.

## 5. Entry radii, positive source envelope, and unchanged quotient

The propagated entry-radius matrix is exactly

\[
 (\varepsilon_{ab})=\frac\epsilon4
 \begin{pmatrix}
 3&3&51&159\\3&57&57&1941\\
 51&57&2055&2055\\159&1941&2055&114861
 \end{pmatrix}
 +\frac{\epsilon^2}4
 \begin{pmatrix}
 1&1&27&83\\1&29&29&1687\\
 27&29&1745&1745\\83&1687&1745&127997
 \end{pmatrix}.
\]

Use the original four source-coordinate weights equal to one. The complete diagonal row-sum bound is

\[
 \Delta=\operatorname{diag}\left(
 54\epsilon+28\epsilon^2,
 \frac{1029}2\epsilon+\frac{873}2\epsilon^2,
 \frac{2109}2\epsilon+\frac{1773}2\epsilon^2,
 29754\epsilon+32878\epsilon^2\right).
\]

For any vector `x`, symmetry of the entry radii and `2|x_a||x_b| <= |x_a|^2+|x_b|^2` give

\[
 |x^*(H-H_0)x|\le\sum_{a,b}\varepsilon_{ab}|x_a||x_b|
 \le x^*\Delta x.
\]

Consequently every source in the stated coefficient box satisfies

\[
 H^-:=H_0-\Delta\preceq H\preceq H_0+\Delta=:H^+.
\]

The exact lower pivots at `epsilon=10^-12` are

\[
 \begin{aligned}
 &\frac{140624999986499999999993}{250000000000000000000000},\\
 &\frac{1265624999718609375013697859375018988500000006111}
 {281249999972999999999986000000000000000000000000},\\
 &\frac{68343749978488171876355321531242138861406229071265234359481763499996388399}
 {843749999812406250009131906250012659000000004074000000000000000000000000},\\
 &\frac{27679218735463626095105940890669242315975722100616684487233945427094373901613962319692633519790369613}
 {11390624996414695312725886921873689810234371511877539059913627249999398066500000000000000000000000}.
 \end{aligned}
\]

Every numerator and denominator is a positive integer. These are successive leading determinant ratios, hence the pivots in symmetric Schur elimination. The invertible congruence taking `[[a,b*],[b,C]]` to `diag(a,C-bb*/a)` proves inductively that `H^->0`. The upper matrix is positive because its difference from the lower is `2 Delta>0`. The receipt also records and checks all pivots for the actual matrix, the upper matrix, and both strictly positive differences `H_actual-H^-` and `H^+-H_actual`.

At degrees `N=1,2,3`, use the principal matrices and the same exact reduction modulo `chi=S^2-2S-1`. In the original basis `(1,S)`,

\[
 J_1=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
 J_2=\begin{pmatrix}1&0&1\\0&1&2\end{pmatrix},\quad
 J_3=\begin{pmatrix}1&0&1&2\\0&1&2&5\end{pmatrix}.
\]

Compute the quotient forms from

\[
 G_N(H)=(J_NH_N^{-1}J_N^*)^{-1},\qquad V_N(H)=\det G_N(H).
\]

The relation and quotient coordinates remain unchanged at the centre, actual source, and both envelope endpoints. Minimizing each source inequality over the same representatives of a quotient vector gives `G_N^- <= G_N <= G_N^+`; positive-form order gives the determinant inequalities. All endpoint quotient matrices are only `2` by `2`. The receipt contains every rational entry and checks positive pivots of both actual quotient differences and all three volume enclosures.

Likewise the monic costs at `j=2,3` are the exact source determinant ratios `omega_j(H)=det H_j/det H_(j-1)`. Minimizing over the same monic polynomial affine set proves `omega_j^- <= omega_j <= omega_j^+`. These inequalities are checked strictly for the specified actual input.

## 6. The coefficient-box endpoint certificate

Retain all four volume endpoints in the expressions

\[
 U_- =\frac{\omega_3^-}{\omega_2^+},\quad
 U_+ =\frac{\omega_3^+}{\omega_2^-},\qquad
 \mathcal R_- =\frac{V_1^-V_2^-}{V_2^+V_3^+},\quad
 \mathcal R_+ =\frac{V_1^+V_2^+}{V_2^-V_3^-}.
\]

The computation certifies `0<U_-<U_actual<U_+` and `1<R_-<R_actual<R_+`. Every rational value is recorded in the receipt. No lower clamp at one is needed for this coefficient box.

For `r=1`, the original endpoint is

\[
 \mathcal E(U,\mathcal R)=
 \frac{\sqrt{U\mathcal R}-\sqrt{U/\mathcal R}}2.
\]

Equivalently it is `(sqrt(U)/2)(sqrt(R)-1/sqrt(R))`. Both factors are nonnegative when `U>0,R>=1`, and the expression is increasing in each variable. Hence the lower endpoint at `(U_-,R_-)` and the upper endpoint at `(U_+,R_+)` enclose the endpoint of every actual multiplier in the original coefficient box.

Each positive square root is enclosed by exact integer bisection with dyadic denominator `2^80`. If a radicand is `a/b`, the program finds an integer `ell` such that `ell^2 b <= a 2^160 < (ell+1)^2 b`. The interval `[ell/2^80,(ell+1)/2^80]` follows by monotonicity of the positive square function. The endpoint difference uses the lower first root minus the upper second root, and vice versa, retaining the factor `1/2`. All root comparisons are checked as exact rational inequalities.

The final certified interval for the entire input coefficient box is

\[
 \boxed{
 \mathcal E\in
 \left[
 \frac{10247872526420120792621067}{2417851639229258349412352},
 \frac{5123936275655574722801253}{1208925819614629174706176}
 \right].}
\]

For the specified interior multiplier, the separately computed exact rational radicands give the much narrower interval

\[
 \mathcal E_{\rm actual}\in
 \left[
 \frac{5123936269431539144503519}{1208925819614629174706176},
 \frac{160123008419735598265735}{37778931862957161709568}
 \right].
\]

The broad coefficient-box interval strictly contains this actual interval, as checked by integer cross multiplication. The chain starts at the actual one-factor coefficient intervals and proceeds through the original sum Gram and fixed quotient. Its conclusion is not obtained by assuming an arbitrary source-matrix error radius.

## 7. Executed scope and genuine formula rejections

Each supplementary invocation executes 331 uniquely labelled checks: **329 mathematical checks and two immutable-dependency hash checks**. The count is composed as follows:

| Group | Count |
|---|---:|
| Immutable dependency pins | 2 |
| Direct paired-root rational identities | 30 |
| Full complex test expansion and parity | 32 |
| Interior coefficient box and complete tensor radii | 23 |
| Independent coefficient/moment Grams and masses | 60 |
| Symmetric entry radii and actual entry enclosure | 32 |
| Four positive coefficient corners and their exact errors | 100 |
| Positive source and source-difference pivots | 20 |
| Fixed-quotient and monic-cost enclosures | 17 |
| Positive-root and final endpoint certificates | 15 |
| Total | 331 |

Normal Python and optimized Python each executed the unchanged calculation and four changed formulas. All ten jobs reached the full suite. The unchanged jobs each passed with zero failures and exit code zero. The deliberate changes produced the following failures in each mode and then exited with code one:

| Changed formula | Failures per mode |
|---|---:|
| Replace `p^2` by `p` in `D/(p^2 e)` | 15 |
| Replace `w^2` by `w` in `s^2 e/(w^2 D)` | 15 |
| Omit the complete `E_+^2` contribution from the tensor radii | 27 |
| Replace the literal `C_k=1/4` by `1` in coefficient-to-Gram evaluation | 32 |

The quadratic-radius change is rejected by actual coefficient-corner and entry errors, in addition to its explicit coefficient formula checks. The mass change is rejected by comparison with separately computed literal convolution moments. No startup guard, assertion, or intentional exception provides these formula rejections. Optimization repeats the same checks; it does not enlarge their mathematical scope.

The pinned prior 416-check suite is a dependency and remains unchanged. The supplementary thirty direct identities close its stated EW.21 verification gap, while the remaining new mathematical checks certify the explicit coefficient pipeline above. This does not claim a growing-degree arithmetic estimate.

## 8. Independent review and immutable pins

A separate reviewer read the complete supplementary script and receipt, made no edits, and did not rerun the replay. The review found no defect in the stated scope. It independently examined the recorded rational data using permutation determinants, LDL elimination, moments derived from the formal equation `M'=alpha tan(theta) M`, and positive-root power comparisons. That examination passed 258 separate predicates. These review predicates are not added to the script's 329 mathematical checks.

The reviewer confirmed all ten saved stdout hashes by reconstructing the actual Windows CRLF output, confirmed stderr hashes, checked that every label is unique within each job, and verified that ordinary and optimized mathematical result objects agree. It also verified that both prior fixture dependencies retain their original hashes.

The final supplementary executable and receipt pins are:

- `gamma_endpoint_window_bridge_supplement_20260913.py`: SHA-256 `a0aff980586a0b7acb884a88ed1f0711cbfb3fb4b71e96a5afbce68581a4b509`.
- `gamma_endpoint_window_bridge_supplement_20260913.json`: SHA-256 `59b0c682b860e024070a1ac307f600a0bd55566aeba83808a9dee73a42250c6a`.

The unchanged dependencies remain:

- `gamma_endpoint_window_bridge_fixture_20260913.py`: SHA-256 `56be6cbd66ffd5272440e95f01104a0154bf0c4b5a2bab1d0a60cb7945071048`.
- `gamma_endpoint_window_bridge_fixture_20260913.json`: SHA-256 `f3703011aa38548fa5a0bf8d9a79a6ffe7464ddfc5bf31d0b4852d1eac7c7f48`.
