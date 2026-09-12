# Independent arithmetic-moment and truncation audit — 12 September 2026

Audit scope: the exact original source `phi_*`, the Gram entries of `D^j Theta(phi_*)` in `L^2(dx)`, the incomplete-gamma double sum, and a certified finite-square truncation. No main TeX file was edited by this audit. The source and Mellin conventions were checked against `output/split_zero_rh_tandem_2026-09-12/tex/tau_boundary.tex`.

## 1. Original source, polynomial coefficients, and reflection

Put `D=-x d/dx`, `phi_*(x)=(4*pi^2*x^4-6*pi*x^2) exp(-pi*x^2)`, `f_j=D^j Theta(phi_*)`, and `Theta(phi)(x)=2 sum_{n>=1} phi(nx)`. Define real polynomials

\[
P_0(z)=4z^2-6z,\qquad
P_{j+1}(z)=2z(P_j(z)-P'_j(z)),\qquad
Q_j(z)=\sum_{k=0}^j\binom jk(-1)^kP_k(z).
\]

Then `deg P_j=deg Q_j=j+2=:d_j`, since the leading coefficient of `P_j` is `2^(j+2)` and that of `Q_j` is `(-1)^j 2^(j+2)`. Direct differentiation gives

\[
f_j(x)=2\sum_{n\geq1}P_j(\pi n^2x^2)e^{-\pi n^2x^2}.
\tag{1}
\]

For the Fourier convention with kernel `exp(-2*pi*i*x*xi)`, the transforms of `x^2 exp(-pi*x^2)` and `x^4 exp(-pi*x^2)` are respectively

\[
\left(\frac1{2\pi}-\xi^2\right)e^{-\pi\xi^2},\qquad
\left(\xi^4-\frac{3\xi^2}{\pi}+\frac3{4\pi^2}\right)e^{-\pi\xi^2}.
\]

Therefore `hat(phi_*)=phi_*` exactly; both its value at zero and its integral vanish. Poisson summation gives `f_0(1/x)=x f_0(x)`. Applying `D_x` to `F(1/x)` gives `-(DF)(1/x)`, whereas `D_x(xF(x))=x(D-1)F(x)`. Induction consequently gives

\[
f_j(1/x)=x(1-D)^jf_0(x)
=2x\sum_{n\geq1}Q_j(\pi n^2x^2)e^{-\pi n^2x^2}.
\tag{2}
\]

All derivatives of (1) converge locally uniformly by Gaussian domination. Equation (2) gives rapid decay of every Euler derivative at zero; (1) gives rapid decay at infinity. Thus these are the original source functions in the stated strong Schwartz space, not replacement finite functions.

## 2. Exact Gram double series

Write `P_i(z)=sum_a p_ia z^a`, `Q_i(z)=sum_a q_ia z^a`, and `H_ij=int_0^infinity f_i(x) f_j(x) dx`. These functions are real, so this agrees with the convention that the first Hilbert argument is conjugate-linear. Substitution `x=1/y` in the interval `(0,1)` and (2) give

\[
H_{ij}=\int_1^\infty
\left[f_i(x)f_j(x)+(1-D)^if_0(x)(1-D)^jf_0(x)\right]dx.
\tag{3}
\]

For `L>=0` and `lambda>0`, the substitution `t=lambda*x^2` gives, retaining the lower endpoint,

\[
I_L(\lambda):=\int_1^\infty x^{2L}e^{-\lambda x^2}dx
=\tfrac12\lambda^{-L-1/2}\Gamma(L+1/2,\lambda).
\tag{4}
\]

Expansion in (3) therefore proves

\[
H_{ij}=2\sum_{n,m\geq1}\sum_{a,b}
(p_{ia}p_{jb}+q_{ia}q_{jb})\pi^{a+b}n^{2a}m^{2b}
[\pi(n^2+m^2)]^{-a-b-1/2}
\Gamma(a+b+1/2,\pi(n^2+m^2)).
\tag{5}
\]

In particular the factor `2` in (5) is correct: the two original theta series contribute `4`, and (4) contributes `1/2`. Absolute convergence justifying all integrations and sums follows directly. For `x>=1`, `n,m>=1`,

\[
(n^2+m^2)x^2\geq (n^2+m^2)/2+x^2.
\]

Thus the sum of absolute polynomial-Gaussian summands is bounded by a finite constant times `x^(2(d_i+d_j)) exp(-pi*x^2)`, because each sum `sum n^(2d) exp(-pi*n^2/2)` converges. This majorant is integrable on `[1,infinity)`.

## 3. Geometric tail certificate and its exact admissibility

For each `j` set

\[
C_j=\sum_a|p_{ja}|\pi^a,\qquad
D_j=\sum_a|q_{ja}|\pi^a.
\]

For a positive integer `N`, define

\[
r_{j,N}=\left(\frac{N+2}{N+1}\right)^{2d_j}e^{-\pi(2N+3)}.
\]

**The geometric formula requires `r_{j,N}<1`.** This is an admissibility condition, not a consequence of `N>=1` alone. For example `j=18,N=1` gives `(3/2)^40 exp(-5*pi)>1`. The parent's explicit convenient choice

\[
N\geq\max(d_i,d_j)
\tag{6}
\]

is sufficient: `log r_{j,N}<2d_j/(N+1)-pi(2N+3)<0`. One may accept smaller `N` after rigorously proving `r_{i,N},r_{j,N}<1` in the interval calculation.

For admissible `N`, put

\[
T_j=\frac{(N+1)^{2d_j}}{1-r_{j,N}},\quad
A_{j,N}^{\rm fin}=\sum_{n=1}^{N}n^{2d_j}e^{-\pi(n^2-1)},\quad
A_j=A_{j,N}^{\rm fin}+T_je^{-\pi((N+1)^2-1)}.
\]

The ratio of successive terms of `n^(2d_j) exp(-pi*n^2*x^2)`, for `x>=1`, is bounded by

\[
\left(\frac{n+1}{n}\right)^{2d_j}e^{-\pi(2n+1)}.
\]

This bound decreases strictly in `n`, because the derivative of its logarithm on positive real `n` is `-2d_j/[n(n+1)]-2*pi<0`. Therefore the full and tail Gaussian sums obey

\[
\sum_{n\geq1}n^{2d_j}e^{-\pi n^2x^2}\leq A_je^{-\pi x^2},\qquad
\sum_{n>N}n^{2d_j}e^{-\pi n^2x^2}
\leq T_je^{-\pi(N+1)^2x^2}.
\tag{7}
\]

Let `H_ij[N]` denote (5) with both theta indices restricted to `1,...,N`, retaining the complete coefficient sums. Since `a<=d_j` and `n,x>=1`,

\[
|P_j(\pi n^2x^2)|\leq C_jn^{2d_j}x^{2d_j},\qquad
|Q_j(\pi n^2x^2)|\leq D_jn^{2d_j}x^{2d_j}.
\]

Use the exact product decomposition `ab-a_Nb_N=(a-a_N)b+a_N(b-b_N)` in each term of (3), and then (7). This proves the slightly sharper asymmetric estimate

\[
|H_{ij}-H_{ij}[N]|\leq
4(C_iC_j+D_iD_j)
(T_iA_j+A_{i,N}^{\rm fin}T_j)
I_{d_i+d_j}(\pi((N+1)^2+1)).
\tag{8}
\]

Swapping `i,j` yields a second valid bound; the smaller of the two remains valid. Since `A_{i,N}^{fin}<=A_i`, the proposed symmetric expression

\[
4(C_iC_j+D_iD_j)(T_iA_j+A_iT_j)
I_{d_i+d_j}(\pi((N+1)^2+1))
\tag{9}
\]

is correct whenever the two ratios are admissible. Equation (8) avoids counting the tail-tail estimate twice, while (9) is simpler to present and execute. No sign of an actual polynomial coefficient was changed in (5); absolute values occur only in the independently stated error bound.

An optional all-`N` version is obtained without modifying the truncation itself. Choose `M_j>=N` with `r_{j,M_j}<1`, and replace `T_j` everywhere by

\[
\widetilde T_{j,N}=
\sum_{n=N+1}^{M_j}n^{2d_j}e^{-\pi(n^2-(N+1)^2)}
+\frac{(M_j+1)^{2d_j}e^{-\pi((M_j+1)^2-(N+1)^2)}}{1-r_{j,M_j}}.
\]

For every `x>=1`, split the tail after `M_j`; the finite head is bounded at `x=1` after factoring `exp(-pi*(N+1)^2*x^2)`, and the remaining series is geometric. This proves (7) with this replacement, hence (8) and (9), for every positive `N`. Choice (6) suffices for the main readily executable theorem, so this extension is optional.

## 4. Exact Gram identities useful for independent checks

Integration by parts has no endpoint term because of the proved rapid decay. As `D=-x*d/dx`,

\[
H_{i+1,j}+H_{i,j+1}=H_{ij}\qquad(i,j\geq0).
\tag{10}
\]

Indeed the left side is `-int x (f_i f_j)' dx=int f_i f_j dx`. Thus `H_10=H_01=H_00/2`, and `H_20=H_02=H_00/2-H_11`. These are identities of the exact original integrals; finite-square approximations need only satisfy them within their combined rigorous tail radii.

There is a full triangular Gram relation. Define

\[
K_j=(D-\tfrac12)^jf_0
=\sum_{a=0}^j\binom ja(-\tfrac12)^{j-a}f_a,
\quad
B_{ja}=\binom ja(-\tfrac12)^{j-a}\quad(a\leq j).
\]

The matrix `B` is real triangular with diagonal `1`; its inverse is `B^{-1}_{ja}=binom(j,a)(1/2)^(j-a)`. Hence `C=BHB^T` exactly, preserving every original coordinate through this explicit invertible map. The operator `D-1/2` is skew symmetric on the present functions by (10), so repeated integration by parts gives

\[
\langle K_i,K_j\rangle=(-1)^i\langle K_0,K_{i+j}\rangle.
\]

For odd `i+j` this is zero: transposing the real inner product gives its negative. For `i+j=2q`, the same identity with `i=j=q` gives

\[
C_{ij}=\begin{cases}
0,&i+j\text{ odd},\\
(-1)^{i+q}\|K_q\|_{L^2(dx)}^2,&i+j=2q.
\end{cases}
\tag{11}
\]

This offers independent exact linear relations throughout every finite Gram block, together with nonnegative signs on the specified even quantities. It records an explicitly invertible coordinate relation; it does not replace the original `f_j` coordinates in formula (5).

There is also an exact boundary identity for the finite-square approximations themselves. Define the finite functions

\[
F_{j,N}(x)=2\sum_{n=1}^NP_j(\pi n^2x^2)e^{-\pi n^2x^2},\qquad
T_{j,N}^{\rm fun}(x)=2\sum_{n=1}^NQ_j(\pi n^2x^2)e^{-\pi n^2x^2}.
\]

These satisfy `DF_{j,N}=F_{j+1,N}` and `(1-D)T_{j,N}^{fun}=T_{j+1,N}^{fun}` exactly. Integration by parts separately on the two products in (3), with the finite functions, gives

\[
H_{i+1,j}[N]+H_{i,j+1}[N]-H_{ij}[N]
=F_{i,N}(1)F_{j,N}(1)
-T_{i,N}^{\rm fun}(1)T_{j,N}^{\rm fun}(1).
\tag{12}
\]

The signs follow from `[-xF_i F_j]_1^infinity=F_i(1)F_j(1)` and `[xT_i T_j]_1^infinity=-T_i(1)T_j(1)`. The full functions have equal values on the two sides at `x=1` by (2), recovering (10). Equation (12) is an exact check of the incomplete-gamma finite sum before its tail interval is added. It also proves that `H_10[N]=H_00[N]/2` exactly for every `N`, since `P_0=Q_0`.

Finally, the entire infinite Gram matrix is related to its first row by the exact formula

\[
H_{ij}=\sum_{k=0}^i(-1)^k\binom ik H_{0,j+k}.
\tag{13}
\]

This follows by transferring `D^i` through the inner product using `D^*=1-D` on these original functions, or by induction in (10). It gives an additional coefficient-level validation route without assuming any finite-dimensional truncation has the full-source adjoint relation.

## Audit conclusion

The source reflection, coefficient recurrence, exact double-series factor, incomplete-gamma endpoint, and proposed truncation bound are correct with explicit ratio admissibility. The simple cutoff `N>=max(i,j)+2` guarantees it. The strongest low-cost improvement is (8); the structural independent check is (10), supplemented by the complete invertible triangular relation (11). No numerical experiment is being asserted as a proof here.

## 5. Review of integrated TeX and Arb implementation

The complete files `tex/arithmetic_moments.tex` and `scripts/check_arithmetic_moments.py` in the tandem output package were read. The audited script SHA-256 is `85236c1060345c99bd6a8395b1c61cd24e5dce3b55c90b38131ebfc65ec3c0a7`. The TeX after the two mathematical/typesetting corrections below and insertion of the numerical tables had SHA-256 `2d997b8d9a8a8da041ac75a4156a09575c0b79248aa9b306d7ba51199b1ca539`; subsequent wording changes should be pinned by the final execution receipt.

The theorem proof, including positivity and injectivity of the original half-domain Gram map, agrees with the calculations above. The displayed limiting estimate `I_L(lambda)<=exp(-lambda)/(2(lambda-L))` for `lambda>=2L` follows exactly from the two stated elementary inequalities and is valid in the theorem's positive-degree range. Both the full-source and finite-boundary identities have the correct endpoint signs.

Two issues were reported and their corrections inspected in the actual TeX: the missing backslash before `qquad` in (AM.18), and the operator-domain wording. The corrected text uses `\langle DF,H\rangle=\langle F,(1-D)H\rangle` on the specified strong Schwartz domain and calls `D-1/2` skew-symmetric there. This records precisely the domain used in the proof, without identifying the adjoint of that restriction with a closed operator on the same domain.

The interval implementation was checked at the following exact interfaces:

1. The recurrence is evaluated over Python integers, with all original coefficient slots retained. The finite sum uses `4*c*n^(2a)*m^(2b)*pi^(a+b)*I_(a+b)`, giving exactly the factor `2` in (AM.8) after the integral definition is inserted.
2. The installed primary runtime documentation for python-flint `0.9.0` states that `lam.gamma_upper(s)` has argument `lam` and order `s`, hence evaluates the required upper incomplete gamma `Gamma(s,lam)`. A focused semantic check verified `arb(3).gamma_upper(1)` overlaps `exp(-3)`. The code uses the unregularized default.
3. All `pi`, exponential, power, incomplete-gamma, finite-sum, ratio and tail calculations remain Arb ball operations. The positive-integer coefficients are exact. The code tests the strict interval predicate `ratio<1` before division by `1-ratio`, so inability to certify the tail denominator fails the run.
4. The installed documentation states that `.upper()` returns an exact floating-point value rounded toward positive infinity, and that the constructor radius is rounded upward when necessary. Thus `val + arb(0,bound.upper())` encloses the entire exact finite sum plus every possible tail error with absolute value bounded by the theorem. Focused probes using the `(0,0)` and `(5,5)` bounds verified that the upper endpoint is exact and that the constructed radius is at least that endpoint. No float conversion is used in this certificate path.
5. An interval matrix containing each true `H_ij` also contains the true finite Gram matrix, even if shared dependencies and symmetry are not represented internally. Arb's determinant encloses determinants of such input values; losing the correlations can widen the answer but cannot exclude the true determinant. The strictly positive determinant balls therefore certify the stated exact determinants are positive. Their successive ball quotients enclose `Delta_(k+1)/Delta_k` because the denominator has already been certified positive. The Schur-complement proof correctly identifies this quotient with the original monic squared norm.
6. The exact linear Gram and finite-boundary identities are tested by checking whether their residual intervals contain zero. These are consistency checks on the independent certificate calculations, not replacements for the analytic proofs. The script avoids Python `assert`, so its checks remain present under `-O`.
7. The output uses `arb.str(..., radius=True, more=True)` and retains its radius. The installed documentation identifies this as a parseable decimal ball whose radius accounts for the decimal conversion, rather than a midpoint-only output.

No broad checker rerun was performed by this audit: the foregoing few semantic probes addressed the specific runtime interfaces. During the review the owner refreshed the normal and optimized receipts after adding the table-containment checks; both final receipts were read and each records 132/132 passing checks with the parameters `max_order=5`, `cutoff=7`, `precision_decimal_digits=110`.

The newly inserted numerical tables were independently checked against the stored certificate. For each of six printed moments and six printed norms, directed interval comparisons show the exact printed interval strictly contains the stored Arb ball. All 36 printed-certificate tail bounds are strictly below `2.961369e-63`; the `(0,0)` tail bound is strictly below `1.150030e-83`. A minor prose correction was requested to say the six leading principal determinants are *recorded in the companion certificate*, since the paper's table displays the norms rather than those six determinants.

The owner's final added table-check block was separately inspected. Its predicate `(value-arb(c)).abs_upper() < arb(r)` certifies containment in the interval whose centre and radius are the exact displayed decimals: the left side is an outward upper bound including centre-conversion error, and the strict ball comparison tests it against a lower bound for the radius. The two added tail comparisons have the same directed meaning. All earlier arithmetic algorithms are unchanged.

The final source hashes were independently obtained from the files and matched against both execution receipts:

- `scripts/check_arithmetic_moments.py`: `8eb82b8e0a62cd39b4f00b63eafca6a72bda7277404c6c9f72db28b0eb982470`.
- `tex/arithmetic_moments.tex`: `9523452478397aea57c8e0c88ad88c814a0e7c5372b7398111e03eb438720379`.

The final text also fixes the principal-determinant table wording. No remaining error was found in the arithmetic moment theorem, interval enclosure implementation, or printed numerical intervals.
