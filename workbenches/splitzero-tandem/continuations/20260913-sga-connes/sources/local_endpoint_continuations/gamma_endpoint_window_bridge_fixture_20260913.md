# Exact auxiliary arbitrary-window endpoint fixture

The complete computation below retains the original coordinate `S = 1 + i u`, the quotient basis `(1,S)`, the relation `chi(S) = (S-1)^2-2 = S^2-2S-1`, and the literal measure masses. Its input is the explicitly specified auxiliary Gamma weight from GMT.32. It supplies finite exact examples and a replayable rational calculation for the arbitrary-window formulas. It makes no assertion that this weight comes from an actual zeta packet.

The only authored executable is `gamma_endpoint_window_bridge_fixture_20260913.py`. It uses Python's standard-library `Fraction`, integer arithmetic, and exact matrix elimination. No floating-point number enters a mathematical inequality, determinant, root certificate, or equality check. The associated JSON records the complete normal calculation and all deliberately changed calculations, together with the actual subprocess commands, return codes, timestamps, and stdout/stderr hashes.

## 1. Literal source and independent moment constructions

Set

\[
 \lambda=1,\quad k=2,\quad c=k/2=1,\quad
 r_1(t)=\frac{|\Gamma(1+it/2)|^2}{2\pi},\quad
 c_1=\frac12,\quad C_2=c_1^2=\frac14,
\]

\[
 B(t)=1+\frac{t^2}{4},\qquad w(t)=B(t)r_1(t),\qquad
 m(u)=\int_{\mathbb R}w(t)w(u-t)\,dt.
\]

The source mass is `9/16`, because the one-factor weighted mass is `3/4`. The map from the two original real coordinates to the sum is `(t_1,t_2) -> (t_1,u=t_1+t_2)`, with determinant one. No average of the two coordinates or division by either measure mass occurs.

The moment generator is the monic Jacobi recurrence

\[
 t b_j^{(\lambda)}(t)
 =b_{j+1}^{(\lambda)}(t)+j(j+2\lambda-1)b_{j-1}^{(\lambda)}(t),
 \qquad b_0^{(\lambda)}=1.
\]

Starting with the coefficient vector of `b_0`, the program repeatedly applies this multiplication map. If `v_j` is the coefficient of `b_j`, the next coefficient vector receives `v_j` at index `j+1` and `j(j+2 lambda-1)v_j` at index `j-1`. Orthogonality gives the integral as the coefficient of `b_0` times the original mass. Thus each generated moment is an exact finite consequence of the recurrence and its original mass.

For the one-factor reference, the even moments through degree eight are

\[
 \left(\frac12,1,8,136,3968\right).
\]

Write `rho_j` for its moments. Multiplication by the written `B` gives

\[
 w_j=\rho_j+\frac14\rho_{j+2}.
\]

The literal two-factor binomial expansion gives, for every integer `d >= 0`,

\[
 m_d=\sum_{j=0}^d\binom dj w_jw_{d-j}.
\]

The even source moments through degree fourteen are exactly

\[
 \left(\frac9{16},\frac92,117,5472,385272,
       37369152,4730516352,753280837632\right).
\]

All odd moments vanish. The program constructs the original one-factor reference through degree sixteen before multiplying by `B` and computing these convolution moments.

A second finite route uses the degree-four polynomial in the Gamma sum density. The parameter of the sum reference is `2`, its mass remains `1/4`, and its monic polynomials obey the recurrence with `2 lambda = 4`. The complete polynomial is

\[
 B_2(u)=\frac{54}{35}+\frac{39}{280}u^2+\frac3{1120}u^4.
\]

Indeed `b_2^(1)=t^2-2` gives the one-factor coefficients `c_0=3/2` and `c_2=1/4`. The coefficient generating polynomial is `A(z)=3(1+z^2)/2`, so its twofold power has coefficients `(d_0,d_2,d_4)=(9/4,9/2,9/4)`. Substituting

\[
 b_2^{(2)}(u)=u^2-4,\qquad
 b_4^{(2)}(u)=u^4-32u^2+72
\]

into `d_0+d_2 b_2^(2)/(4)_2+d_4 b_4^(2)/(4)_4` gives the stated `B_2`. Consequently

\[
 m_d=\frac{54}{35}\rho_d^{\Sigma}
       +\frac{39}{280}\rho_{d+2}^{\Sigma}
       +\frac3{1120}\rho_{d+4}^{\Sigma},
\]

where `rho^Sigma` is generated independently with parameter `2` and mass `1/4`. All fifteen degrees `0,...,14` agree with the literal convolution calculation. Independently, all fifteen reference moments from the literal two-factor convolution agree with that parameter-`2` recurrence.

There is an additional exact Gamma-function description of this auxiliary input. Integration by parts in the absolutely convergent Euler gamma integral gives `Gamma(z+1)=z Gamma(z)` for `Re z>0`, so at `z=1+it/2` it gives

\[
 w(t)=(1+t^2/4)r_1(t)=r_2(t).
\]

The general literal Gamma convolution identity retains its masses:

\[
 r_a*r_b=\frac{c_a c_b}{c_{a+b}}r_{a+b},\qquad
 c_a=2^{1-2a}\Gamma(2a).
\]

It follows by multiplication of the Fourier transforms `c_a(cosh y)^(-2a)` and `c_b(cosh y)^(-2b)`, followed by uniqueness of the Fourier transform of an integrable function. In the present case `c_1=1/2`, `c_2=3/4`, and `c_4=315/8`. Consequently

\[
 r_1*r_1=\frac13r_2,\qquad
 w*w=r_2*r_2=\frac1{70}r_4.
\]

Their pointwise density ratio is exactly

\[
 \frac{(r_4/70)(u)}{(r_2/3)(u)}
 =\frac3{70}(4+u^2/4)(9+u^2/4)
 =\frac{54}{35}+\frac{39}{280}u^2+\frac3{1120}u^4.
\]

This identity supplies an independent whole-measure explanation of the computed coefficient polynomial. Each measure and its original mass remain explicit.

## 2. Original-coordinate Gram, quotient, and source norms

For `0 <= a,b <= N`, the conjugate-linear-first source Gram is

\[
 (H_N)_{ab}=\int (1-iu)^a(1+iu)^b m(u)\,du
 =\sum_{\ell=0}^a\sum_{j=0}^b
 \binom a\ell\binom bj(-1)^\ell i^{\ell+j}m_{\ell+j}.
\]

The program retains both real and imaginary components of this expansion and verifies that each imaginary component is zero for the symmetric input. It does not replace `S` by `u`. In particular

\[
 H_3=\frac1{16}
 \begin{pmatrix}
 9&9&-63&-207\\
 9&81&81&-1863\\
 -63&81&2025&2025\\
 -207&-1863&2025&93393
 \end{pmatrix}.
\]

The complete `H_7`, including every entry, is in the JSON. The displayed moment formula is its complete finite construction.

For `q=2`, reduction modulo the original relation obeys

\[
 J_0=(1,0)^{\mathsf T},\quad J_1=(0,1)^{\mathsf T},\quad
 J_j=2J_{j-1}+J_{j-2}\quad(j\ge2).
\]

The columns of the matrix `J_N` are these exact two-entry vectors. The relation matrix `B_N` has columns `chi,chi S,...,chi S^(N-2)`; its three nonzero entries in each successive column are `(-1,-2,1)`. Thus `J_N B_N=0`. All the following matrices use these coordinates:

\[
 K_N=J_NH_N^{-1}J_N^*,\quad G_N=K_N^{-1},\quad
 R_N=H_N^{-1}J_N^*G_N,\quad V_N=\det G_N.
\]

The replay checks `J_N R_N=I_2`, `R_N^*H_N R_N=G_N`, and the exact determinant-line formula

\[
 V_N=\frac{\det H_N}{\det(B_N^*H_NB_N)}
\]

at every degree `N=1,...,7`, with the empty denominator determinant equal to one at `N=1`. The source norms have their original mass:

\[
 \omega_0=\frac9{16},\qquad
 \omega_j=\frac{\det H_j}{\det H_{j-1}}\quad(j\ge1).
\]

Their exact values are:

| Degree j | Original monic squared norm omega_j | Quotient volume V_j |
|---:|---:|---:|
| 1 | 9/2 | 81/32 |
| 2 | 81 | 729/488 |
| 3 | 2430 | 98415/161528 |
| 4 | 106920 | 16238475/37139524 |
| 5 | 6415200 | 2679348375/10549111519 |
| 6 | 500385600 | 3134837598750/15879949388971 |
| 7 | 49037788800 | 122258666351250/915851227747369 |

All leading principal determinant ratios of `H_7` are positive. They are exactly its successive pivots under symmetric elimination. The program also records all reference quotient volumes, with the unchanged reference mass `1/4`.

The measure identity above also proves the source norm formula for every degree. The monic coordinate map is

\[
 p_j(S)=i^j b_j^{(4)}((S-1)/i).
\]

Because `b_j^(4)` is monic, `p_j` has leading coefficient one in `S`. At the original coordinate `S=1+iu`, its value is `i^j b_j^(4)(u)`. The factor has modulus one, so the exact orthogonality integral against `r_4/70` gives

\[
 \omega_j=\frac{c_4}{70}j!(8)_j
          =\frac9{16}j!(8)_j\qquad(j\ge0).
\]

These are the original monic costs, because subtracting any polynomial of lower degree from `p_j` changes its squared norm by the nonnegative squared norm of that lower-degree difference, using orthogonality. Therefore the minimum monic cost is precisely the displayed value. In particular every auxiliary window has the exact all-degree norm ratio

\[
 \frac{\omega_{n+r}}{\omega_n}=(n+1)_r(n+8)_r.
\]

The fixture script computes the finite costs from original-coordinate determinants; the formula above supplies their exact analytic explanation and was checked independently against the saved values.

## 3. All fifteen arbitrary windows and their exact maps

The covered windows are every pair

\[
 2\le n<n+r\le7,\qquad r\ge1.
\]

Split `H_(n+r)` after degrees `0,...,n-1`, preserving the order `S^n,...,S^(n+r)` of the new block:

\[
 H_{n+r}=\begin{pmatrix}H_-&C\\C^*&D\end{pmatrix},\quad
 W=D-C^*H_-^{-1}C,\quad
 F=J_D-J_-H_-^{-1}C,\quad
 Z=F^*G_-F.
\]

The map `(x,y) -> (x-H_-^{-1}Cy,y)` is triangular with determinant one and gives the orthogonal decomposition with forms `H_-` and `W`. Applying the fixed quotient reduction gives

\[
 K_{n+r}=K_{n-1}+FW^{-1}F^*.
\]

Every window checks this matrix identity directly against the independently computed quotient inverses.

Let `W_r,Z_r` be the leading `r` by `r` blocks, and let `W_1,Z_1` be their leading scalar blocks. Define

\[
 T=\frac{\det(W+Z)}{\det W},\quad
 T_{\rm prefix}=\frac{\det(W_r+Z_r)}{\det W_r},\quad
 T_{\rm first}=\frac{W_{00}+Z_{00}}{W_{00}}.
\]

The replay compares these block calculations with the separately computed quotient volumes, proving the finite equalities

\[
 T=\frac{V_{n-1}}{V_{n+r}},\quad
 T_{\rm prefix}=\frac{V_{n-1}}{V_{n+r-1}},\quad
 T_{\rm first}=\frac{V_{n-1}}{V_n}.
\]

Consequently the exact four-volume ratio is

\[
 \mathcal R=\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}
           =\frac{T T_{\rm prefix}}{T_{\rm first}}.
\]

The first original monic norm is `omega_n=W_00`. The last monic norm is `omega_(n+r)=det W/det W_r`. These two independently evaluated norm identities are checked for every window, including `r>1`.

For the three requested windows, the exact scalar data are:

| (n,r) | U = omega_(n+r)/omega_n | R | T | T_prefix | T_first |
|---|---:|---:|---:|---:|---:|
| (2,1) | 30 | 20191/4860 | 20191/4860 | 61/36 | 61/36 |
| (2,2) | 1320 | 3073295611/216513000 | 9284881/1603800 | 20191/4860 | 61/36 |
| (3,2) | 2640 | 295913127219469/36104825790000 | 10549111519/1793583000 | 9284881/2717550 | 331/135 |

For `(2,1)` the full matrices are

\[
 W=\begin{pmatrix}81&243\\243&3159\end{pmatrix},\quad
 F=\begin{pmatrix}10&2\\0&28\end{pmatrix},\quad
 Z=\begin{pmatrix}225/4&675/4\\675/4&16137/4\end{pmatrix}.
\]

For `(2,2)` they are

\[
 W=\begin{pmatrix}
 81&243&-4050\\243&3159&-2430\\-4050&-2430&348300
 \end{pmatrix},\quad
 F=\begin{pmatrix}10&2&-256\\0&28&112\end{pmatrix},
\]

\[
 Z=\begin{pmatrix}
 225/4&675/4&-810\\675/4&16137/4&11682\\-810&11682&68112
 \end{pmatrix}.
\]

For `(3,2)` they are

\[
 W=\begin{pmatrix}
 2430&9720&-218700\\9720&145800&-340200\\
 -218700&-340200&28771200
 \end{pmatrix},\quad
 F=\begin{pmatrix}-28&244&2712\\28&112&-932\end{pmatrix},
\]

\[
 Z=\begin{pmatrix}
 3528&14112&-117432\\
 14112&6009732/61&-15821388/61\\
 -117432&-15821388/61&302597388/61
 \end{pmatrix}.
\]

The JSON contains the full corresponding matrices and the source projection coefficients for all fifteen windows.

## 4. Rational certification of positive roots and endpoint values

Define the endpoint expression, with the factor `1/2` retained, by

\[
 \mathcal E(U,\mathcal R)
 =\frac{(U\mathcal R)^{1/(2r)}-(U/\mathcal R)^{1/(2r)}}2.
\]

Every root denotes the positive real root. For a positive rational number `a/b` and exponent `p=2r`, set `D=2^80`. Integer bisection finds `ell` satisfying

\[
 \ell^p b\le aD^p<(\ell+1)^p b.
\]

It follows, by strict monotonicity of the positive integer power map, that the root belongs to `[ell/D,(ell+1)/D]`. If equality holds at the lower bound, the program instead returns a point interval. Both power inequalities and the width at most `2^-80` are checked by exact rational arithmetic for each of the two roots in every window. Endpoint subtraction uses the lower first root minus the upper second root, and the upper first root minus the lower second root, each divided by two. This produces a root-free rational certificate for the expression defined above; it does not assert the expression itself is rational.

Write `D_1=2^81=2417851639229258349412352`. The following exact endpoint intervals have width `2/D_1=2^-80`:

\[
 \begin{aligned}
 \mathcal E_{2,1}&\in
 \left[\frac{10247872538865635114774367}{D_1},
       \frac{10247872538865635114774369}{D_1}\right],\\
 \mathcal E_{2,2}&\in
 \left[\frac{10389869524335068487703313}{D_1},
       \frac{10389869524335068487703315}{D_1}\right],\\
 \mathcal E_{3,2}&\in
 \left[\frac{9540698076122146697497573}{D_1},
       \frac{9540698076122146697497575}{D_1}\right].
 \end{aligned}
\]

Their respective pairs of root radicands are

\[
 \begin{aligned}
 (2,1):&\quad \left(\frac{20191}{162},\frac{145800}{20191}\right),
 &p=2,\\
 (2,2):&\quad \left(\frac{3073295611}{164025},
                    \frac{285797160000}{3073295611}\right),
 &p=4,\\
 (3,2):&\quad \left(\frac{295913127219469}{13676070375},
                    \frac{95316740085600000}{295913127219469}\right),
 &p=4.
 \end{aligned}
\]

At each of the five `r=1` windows, the independent algebraic identity

\[
 \mathcal E^2=\frac U4\left(\mathcal R+\frac1{\mathcal R}-2\right)
\]

is also certified by squaring the two nonnegative rational endpoint bounds and comparing them with its exact rational right side.

## 5. Fixed-degree positive matrix envelope and endpoint propagation

Set `delta=10^-6` in the original degree-seven source coordinates. The full lower and upper matrices are

\[
 H^{\rm lo}=H_7-\delta I_8,\qquad H^{\rm hi}=H_7+\delta I_8.
\]

Every leading principal determinant ratio of both matrices is recorded as an exact positive rational number in the JSON. Symmetric elimination proves that the matrices are positive definite: the successive congruences replace a block `[[a,b*],[b,C]]` by `diag(a,C-bb*/a)`, and each recorded pivot `a` is positive. These are checks of the entire eight-dimensional forms, not only the diagonal entries.

The envelope describes any compatible family of principal source matrices obtained from an unknown Hermitian matrix between these two fixed matrices. It is an auxiliary finite matrix certificate. No numerical error bound for an unprovided arithmetic measure is asserted.

For each degree `j`, denote the monic cost and quotient volume obtained from the corresponding principal submatrix by `omega_j^lo, omega_j^hi` and `V_j^lo,V_j^hi`. The minimum over the same monic affine set gives

\[
 \omega_j^{\rm lo}\le\omega_j^{\rm actual}\le\omega_j^{\rm hi}.
\]

Likewise, minimizing over the same representatives of each fixed quotient vector gives `G_j^lo <= G_j^actual <= G_j^hi` in positive-form order; conjugation by a positive square root and multiplication of positive eigenvalues gives the determinant inequalities for `V_j`. All denominators below are positive by the pivot certificates and by the full-rank reduction map.

Consequently

\[
 U_{\rm lo}=\frac{\omega_{n+r}^{\rm lo}}{\omega_n^{\rm hi}},\quad
 U_{\rm hi}=\frac{\omega_{n+r}^{\rm hi}}{\omega_n^{\rm lo}},
\]

\[
 \mathcal R_{\rm lo}=
 \frac{V_{n-1}^{\rm lo}V_n^{\rm lo}}
      {V_{n+r-1}^{\rm hi}V_{n+r}^{\rm hi}},\quad
 \mathcal R_{\rm hi}=
 \frac{V_{n-1}^{\rm hi}V_n^{\rm hi}}
      {V_{n+r-1}^{\rm lo}V_{n+r}^{\rm lo}}
\]

enclose the original `U` and `R`. The exact computation verifies `1 < R_lo` for all fifteen windows. On `U>0,R>=1`, write `a=1/(2r)` and

\[
 \mathcal E(U,R)=\tfrac12 U^a(R^a-R^{-a}).
\]

Both factors are nonnegative. Increasing `U` increases the first factor; increasing `R` increases `R^a` and decreases `R^-a`, hence increases the second factor. Therefore this expression is increasing in each variable on the stated domain. Evaluating its rational root bounds at `(U_lo,R_lo)` and `(U_hi,R_hi)` supplies a certified endpoint interval for every actual matrix in the envelope. The computation also checks that these intervals strictly contain the much narrower central endpoint intervals above.

For the selected windows the resulting endpoint enclosures are exactly:

\[
 \begin{aligned}
 (2,1):\quad&
 \left[\frac{5123879173730631898336841}{1208925819614629174706176},
       \frac{1280998341368256213434749}{302231454903657293676544}\right],\\
 (2,2):\quad&
 \left[\frac{2597450225134194679640063}{604462909807314587353088},
       \frac{5194969074204960115983475}{1208925819614629174706176}\right],\\
 (3,2):\quad&
 \left[\frac{2385151986263501223322793}{604462909807314587353088},
       \frac{9540788207550856677053757}{2417851639229258349412352}\right].
 \end{aligned}
\]

The JSON records every rational `U_lo,U_hi,R_lo,R_hi` and every endpoint interval, including the twelve other windows.

## 6. Actual replay and deliberate formula changes

The complete suite has 416 distinct checks per invocation:

| Check group | Count |
|---|---:|
| Masses and two independent moment constructions | 36 |
| Complete original-S degree-three Gram | 1 |
| Eight pivots each for source, lower, upper | 24 |
| Five quotient identities or positivity checks at seven degrees | 35 |
| Ten exact Schur, norm, ratio, and endpoint checks at fifteen windows | 150 |
| Seven root checks at fifteen windows and five independent quadratic checks | 110 |
| Four endpoint-envelope checks at fifteen windows | 60 |
| Total | 416 |

Both normal Python and `python -O` ran the positive calculation and each of six deliberately changed formulas. Every one of these fourteen subprocesses executed the complete 416-check suite. The changes and rejection counts per invocation were:

| Deliberate change | Failed checks in normal mode | Failed checks in -O mode |
|---|---:|---:|
| Replace the one-factor reference mass 1/2 by 1 | 23 | 23 |
| Omit all interior terms in the tensor binomial sum | 8 | 8 |
| Remove Z from the Schur determinant update | 60 | 60 |
| Multiply by T_first in place of dividing by it | 15 | 15 |
| Square det(W_prefix) in the final monic norm denominator | 15 | 15 |
| Remove the factor 1/2 in the endpoint expression | 35 | 35 |

The unchanged runs each had zero failures and exit code zero. Each changed run had exit code one after its mathematical checks. No mutation is rejected by a startup guard, an assertion removed by `-O`, or an intentional exception. The observed equality of counts across modes is recorded in the receipt. Repeating the suite under different modes or mutations does not increase the count of distinct mathematical checks.

The finite checks support precisely this specified auxiliary weight and these fifteen windows. The arbitrary-degree identities and all arithmetic conclusions belong to the complete mathematical proofs into which these computations are being integrated.

## 7. Independent read-only audit and file pins

A separate reviewing agent read the complete script and saved receipt without editing either file or rerunning the replay. The audit found no defect on the supported domain. In addition to reviewing the original-coordinate maps and Schur formulas, it constructed Gamma moments independently from the formal differential equation

\[
 M'(\theta)=\alpha\tan(\theta)M(\theta),\qquad M(0)=c,
\]

and matched all 62 one-factor and two-factor moments recorded in the unchanged calculation. This equation follows by differentiating `M(theta)=c(cos theta)^(-alpha)`; its formal coefficient recurrence is independent of the Jacobi multiplication used by the fixture script. The audit also matched all saved source monic norms with `(9/16) j!(8)_j` and passed 264 separate rational predicates on the saved root and envelope data, including 120 root predicates. These audit predicates are reported separately from the fixture's 416 checks.

The reviewer reconstructed every saved stdout hash using the actual Windows CRLF output convention, verified the stderr hashes, and checked that the paired ordinary and optimized result objects are equal. All 416 labels are unique within each job, and all fourteen jobs reach the full suite.

The final executable and receipt pins are:

- `gamma_endpoint_window_bridge_fixture_20260913.py`: SHA-256 `56be6cbd66ffd5272440e95f01104a0154bf0c4b5a2bab1d0a60cb7945071048`.
- `gamma_endpoint_window_bridge_fixture_20260913.json`: SHA-256 `f3703011aa38548fa5a0bf8d9a79a6ffe7464ddfc5bf31d0b4852d1eac7c7f48`.

The separate audit performed its calculations transiently and made no additional files. Its bounded findings and observed counts are recorded here; the complete deterministic fourteen-job replay remains in the pinned JSON.
