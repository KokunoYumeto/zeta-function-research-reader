# Evaluated original source kernel, regular correction, and full-quartet endpoint

Research continuation, 19 September 2026.

## Provenance and scope

The receiving source is `KokunoYumeto/zeta-function-research-reader`, commit
`1445091fd84d47b3908f56d4db1f8a28acd134da`, particularly the complete proof
`workbenches/splitzero-tandem/continuations/20260919-original-heat-source-endpoint/ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex`.
The input equations used here are EG1–9 (original source and unit), EG20–33
(regular correction), EG39–41 (complete left minimum), EG44–50 (critical
metric), and EG56–57 (physical action). The current calculation evaluates
matrices retained there as integrals. It does not insert this source metric
in place of the native polynomial-convolution quotient metric or PRD target.

All scalar products are conjugate-linear in the first argument. Independent
variables `z,w` below are inserted as `z=conjugate(rho), w=sigma` only after
holomorphic differentiation. Every zero multiplicity remains in the matrices.

## 1. The original one-parameter source and a scalar function

Retain
\[
\phi(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
\Phi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{SK1}
\]
On the strip \(\mathcal S=\{0<\Re s<1\}\), define the actual function
\[
f_s(x)=x^{-s}\int_x^\infty\phi(y)y^{s-1}dy,
\qquad g_s(x)=f_s(x)/\Phi(s).
\tag{SK2}
\]
The Gaussian integral gives, without a limiting interpretation,
\[
f_s(x)=x^{-s}\pi^{-s/2}
\{2\Gamma(s/2+2,\pi x^2)-3\Gamma(s/2+1,\pi x^2)\}.
\]
The factor \(\Phi\) is nonzero on \(\mathcal S\).

Define the holomorphic scalar
\[
\boxed{\displaystyle
\mathfrak Z(s)=\frac{[s(s-1)]^2}{4}
 B_{1/2}\!\left(\frac{1-s}{2},\frac{s}{2}\right)
+\frac{\sqrt2}{4}\left(s^3-\frac32s^2-\frac14s+\frac38\right).}
\tag{SK3}
\]
The incomplete beta integral is the ordinary integral over \([0,1/2]\),
with positive real base and the usual real logarithms. Thus its parameters
have no unassigned branch on this strip. Then
\[
\boxed{\mathfrak Z(s)=\int_0^\infty\phi(x)f_s(x)dx,\qquad
\mathfrak Z(s)+\mathfrak Z(1-s)=\Phi(s)\Phi(1-s).}
\tag{SK4}
\]

### Proof, including the original Gamma mass

Set \(\sigma(y)=|\Gamma(1/4+iy/2)|^2/(2\pi)\), of mass \(\sqrt{2\pi}\).
Euler's beta integral, after \(u=e^{2t}\), gives
\[
\int_{\mathbb R}e^{iyt}(\cosh t)^{-1/2}dt
=\frac1{\sqrt2}B(1/4+iy/2,1/4-iy/2)
=\frac{|\Gamma(1/4+iy/2)|^2}{\sqrt{2\pi}}.
\]
Fourier inversion therefore gives
\(\int e^{-ity}\sigma(y)dy=\sqrt{2\pi}(\cosh t)^{-1/2}\).
For \(\Re s<1/2\), Laplace integration followed by
\(u=e^{-2t}\), then \(v=u/(1+u)\), gives
\[
\int_{\mathbb R}\frac{\sigma(y)}{1/2+iy-s}dy
=\sqrt\pi B_{1/2}((1-s)/2,s/2).
\]
In the exact physical Parseval convention,
\[
\frac{|\Phi(1/2+iy)|^2}{2\pi}
=\frac{(y^2+1/4)^2}{4\sqrt\pi}\sigma(y).
\]
Write \(t=1/2+iy\), so \((y^2+1/4)^2=[t(t-1)]^2\). The first four
\(t\)-moments of \(\sigma/\sqrt{2\pi}\), obtained by differentiating its
just-proved transform, are \(1,1/2,-1/4,-5/8\). Polynomial division gives
\[
\frac1{\sqrt{2\pi}}\int
\frac{[t(t-1)]^2-[s(s-1)]^2}{t-s}\,d\sigma
=s^3-\frac32s^2-\frac14s+\frac38.
\]
This proves SK3–4 first for \(\Re s<1/2\) by Parseval applied to
\(\Phi(t)/(t-s)\). The physical cross integral \(\int\phi f_s\) is
holomorphic throughout \(\mathcal S\): at zero its absolute bound is
\(O(x^{2-\Re s})\), locally uniformly in \(s\), and at infinity the
Gaussian tail dominates every derivative. The beta expression is also
holomorphic there. Analytic uniqueness extends their equality. In
particular the right-strip value is this explicitly proved continuation;
it is not obtained by reusing the unchanged critical-line resolvent across
its pole.

The beta symmetry identity
\(B_{1/2}(a,b)+B_{1/2}(b,a)=B(a,b)\) and the exact polynomial identity
\(R(s)+R(1-s)=0\) prove the second identity in SK4. Its constant is
\([s(s-1)]^2\Gamma(s/2)\Gamma((1-s)/2)/(4\sqrt\pi)\), exactly
\(\Phi(s)\Phi(1-s)\).

As an independent physical integral check, direct Gaussian integration gives
\[
\int_0^\infty\phi(x)\phi(vx)dx
=\frac{-18v^6+69v^4-18v^2}{2(1+v^2)^{9/2}}.
\]
Integrating this against \(v^{s-1}dv\) on \([1,\infty)\) gives the equivalent
three-beta expression
\[
\mathfrak Z(s)=\tfrac14\{-18B_{1/2}((7-s)/2,(s+2)/2)
+69B_{1/2}((5-s)/2,(s+4)/2)
-18B_{1/2}((3-s)/2,(s+6)/2)\}.
\]
Both expressions evaluate the same original cross integral.

## 2. All finite cutoff entries, including resonances

Put \(a=z+w-1\), \(\epsilon=e^{-T}\), \(T\ge0\), and
\[
E_T(a)=\begin{cases}(e^{aT}-1)/a,&a\ne0,\\T,&a=0.\end{cases}
\]
The numerator in
\[
\boxed{\displaystyle
\mathscr F(z,w)=
\frac{\Phi(z)\Phi(w)-\mathfrak Z(z)-\mathfrak Z(w)}
{(z+w-1)\Phi(z)\Phi(w)}}
\tag{SK5}
\]
vanishes on \(z+w=1\) by SK4. Consequently \(\mathscr F\) is holomorphic
on \(\mathcal S^2\). This is a removable divided difference, not a pole
assigned zero. For example,
\[
\mathscr F(z,1-z)=
\frac{\Phi(z)\Phi'(1-z)-\mathfrak Z'(1-z)}{\Phi(z)\Phi(1-z)}.
\]
Its higher derivatives at the resonance are evaluated by the convergent
local series
\[
\mathscr F(z,w)=\frac1{\Phi(z)\Phi(w)}
\sum_{n\ge0}
\frac{\Phi(z)\Phi^{(n+1)}(1-z)-\mathfrak Z^{(n+1)}(1-z)}{(n+1)!}
a^n.
\tag{SK6}
\]

The full Gaussian Taylor coefficients are
\(c_n=2n(2n+1)(-\pi)^n/n!\), so \(\phi(x)=\sum_{n\ge1}c_nx^{2n}\).
The regular part of SK2 is exactly
\[
f_s(x)=\Phi(s)x^{-s}-\sum_{n\ge1}\frac{c_nx^{2n}}{s+2n}.
\tag{SK7}
\]
For each bounded \(x\)-interval the latter series and all required
parameter derivatives converge absolutely. Define
\[
\begin{aligned}
B(z,w;T)={}&-\Phi(z)\sum_{n\ge1}
\frac{c_n\epsilon^{2n+1-z}}{(w+2n)(2n+1-z)}\\
&-\Phi(w)\sum_{n\ge1}
\frac{c_n\epsilon^{2n+1-w}}{(z+2n)(2n+1-w)}\\
&+\sum_{n,m\ge1}
\frac{c_nc_m\epsilon^{2n+2m+1}}
{(z+2n)(w+2m)(2n+2m+1)},\qquad
\mathscr B(z,w;T)=\frac{B(z,w;T)}{\Phi(z)\Phi(w)}.
\end{aligned}
\tag{SK8}
\]
Every single and double sum is absolutely convergent, including at \(T=0\).
Then the complete original cutoff kernel is
\[
\boxed{\displaystyle
\mathscr K_T(z,w):=\int_{\epsilon}^{\infty}g_z(x)g_w(x)dx
=E_T(z+w-1)+\mathscr F(z,w)-\mathscr B(z,w;T).}
\tag{SK9}
\]

### Proof

For \(\Re z,\Re w<1/2\), Parseval and the exact two-factor partial fraction
give
\[
\int_0^\infty f_z(x)f_w(x)dx
=\frac{\mathfrak Z(z)+\mathfrak Z(w)}{1-z-w}.
\]
Subtract the integral of \(\Phi(z)\Phi(w)x^{-z-w}\) on \((0,1)\).
The remaining physical integral is holomorphic on all of \(\mathcal S^2\):
the cross terms are bounded near zero by \(x^{2-\Re z}\) and
\(x^{2-\Re w}\), and the regular square by \(x^4\). Its value is
\(\Phi(z)\Phi(w)\mathscr F(z,w)\), first on the open left polydomain
and then everywhere by holomorphic uniqueness. The resonance is removable
by SK4. The original singular integral on \((\epsilon,1)\) is exactly
\(\Phi(z)\Phi(w)E_T(a)\). Expanding the omitted regular integral on
\((0,\epsilon)\) with SK7 and integrating term by term gives precisely
SK8, with both negative cross sums and the positive double sum. This proves
SK9 at every cutoff, not only asymptotically.

### An explicit truncation error

Let \(A(\epsilon)=(4t^2+6t)e^t\), \(t=\pi\epsilon^2\), and, for \(L\ge20\),
\[
 r_L=\frac{\pi\epsilon^2(2L+5)}{(L+1)(2L+3)}<1,
\quad A_L=\frac{2(L+1)(2L+3)\pi^{L+1}\epsilon^{2L+2}}
{(L+1)!(1-r_L)}.
\]
The ratio of successive absolute coefficients is decreasing after \(L+1\);
hence \(\sum_{n>L}|c_n|\epsilon^{2n}\le A_L\), while the full sum is
\(A(\epsilon)\). Truncate both indices of SK8 at \(L\), obtaining \(B_L\).
Since the real parts of each first denominator exceed two and those of
\(2n+1-z\) also exceed two,
\[
\boxed{\displaystyle
|B-B_L|\le\frac{A_L}{4}
\{ |\Phi(z)|\epsilon^{1-\Re z}+|\Phi(w)|\epsilon^{1-\Re w}\}
+\frac{\epsilon A(\epsilon)A_L}{10}.}
\tag{SK10}
\]
The last term counts the union of both missing-index sets in the double
sum and retains its denominator at least twenty. Divide by
\(|\Phi(z)\Phi(w)|\) for \(\mathscr B\). For any closed parameter polydisks
inside \(\mathcal S^2\), take the supremum of this bound there and divide
by the two Cauchy radii to the derivative orders. This gives the corresponding
bound for every divided-derivative entry, with no omitted factorial.

## 3. Return to every original primary, unit, and finite Gram

For the full actual finite zero divisor, use the original principal-part
map \(a=\mathsf U_Zu\),
\[
a_{\rho,j}=[z^{m_\rho-j-1}]
\frac{\sum_{l<m_\rho}u_{\rho,l}z^l}{2\zeta_\rho(z)},
\qquad \zeta(\rho+z)=z^{m_\rho}\zeta_\rho(z).
\tag{SK11}
\]
Its determinant and inverse are the original EG6–8 ones. The principal-part
basis source is exactly
\[
g_{\rho,j}(x)=\frac1{j!}\partial_\rho^j g_\rho(x).
\tag{SK12}
\]
To check this, its Mellin transform is the same derivative of
\(\Phi(s)/(\Phi(\rho)(s-\rho))\). That function has singular part
\((s-\rho)^{-1}\) and a jointly holomorphic remainder near the diagonal.
Its divided derivative has singular part \((s-\rho)^{-j-1}\). The rational
factor after removing \(\Phi(s)\) is proper and has only that original
primary. This identifies it with the unique EG principal-part source;
other original zero jets of \(2\zeta\mathcal M g_{\rho,j}\) vanish to
full multiplicity. Hence the actual source is
\(\psi_u=\sum_{\rho,j}a_{\rho,j}g_{\rho,j}\).

Define a full matrix, with all \(0\le i<m_\rho\), \(0\le j<m_\sigma\), by
\[
\mathsf K_T[(\rho,i),(\sigma,j)]
=\left.\frac{\partial_z^i\partial_w^j}{i!j!}
\mathscr K_T(z,w)\right|_{z=\bar\rho,w=\sigma}.
\]
Then the original physical Gram, in its original divided-jet coordinates, is
\[
\boxed{\Gamma_Z(T)=\mathsf U_Z^*\mathsf K_T\mathsf U_Z.}
\tag{SK13}
\]
Equations SK3, SK5–10, SK11 and SK13 evaluate every entry by special-function
derivatives and an absolutely convergent, explicitly bounded series. No
unspecified source integral or growing Gram inverse remains in those entries.

In particular the formerly integral matrices of EG28–30 are now
\[
(F_Z)_{\rho i,\sigma j}
=\frac{\partial_z^i\partial_w^j\mathscr F(\bar\rho,\sigma)}{i!j!},
\quad (B_Z^{\rm reg}(T))_{\rho i,\sigma j}
=\frac{\partial_z^i\partial_w^j\mathscr B(\bar\rho,\sigma;T)}{i!j!}.
\tag{SK14}
\]
On the right divisor, the complete finite constant \(K_Z=F_Z-\widehat G_Z\)
is the divided-derivative matrix of
\[
\boxed{\displaystyle
\mathscr H(z,w)=
\frac{\mathfrak Z(z)+\mathfrak Z(w)}{(1-z-w)\Phi(z)\Phi(w)}.}
\tag{SK15}
\]
On the left divisor, the same explicit meromorphic function gives its
positive limiting Gram:
\[
\boxed{\displaystyle
(L_-)_{\rho i,\sigma j}
=\frac{\partial_z^i\partial_w^j\mathscr H(\bar\rho,\sigma)}{i!j!},
\qquad \Gamma_{--}(\infty)=\mathsf U_-^*L_-\mathsf U_-.}
\tag{SK16}
\]
These are consequences of SK9: on the left, \(E_T(a)\to-1/a\); on the
right, subtract the exact growing singular Gram. Equality of the formulas
is analytic continuation with these explicitly different receiving
operations, not equality of the positive left metric and the right cutoff
metric.

## 4. Both physical source cross terms are also evaluated

Set
\[
\begin{aligned}
\mathfrak Z_T(w)={}&\mathfrak Z(w)
-\Phi(w)\sum_{n\ge1}\frac{c_n\epsilon^{2n+1-w}}{2n+1-w}\\
&+\sum_{n,m\ge1}\frac{c_nc_m\epsilon^{2n+2m+1}}
{(w+2m)(2n+2m+1)}.
\end{aligned}\tag{SK17}
\]
Multiplying SK7 by the full Gaussian series and integrating its omitted
zero interval proves \(\mathfrak Z_T(w)=\int_\epsilon^\infty\phi f_w\).
The divided-derivative rows
\[
\ell_{\rho,j}=\frac1{j!}\partial_\rho^j\frac1{\Phi(\rho)},\qquad
h_{T,\rho,j}=\frac1{j!}\partial_\rho^j\frac{\mathfrak Z_T(\rho)}{\Phi(\rho)}
\tag{SK18}
\]
are therefore precisely the principal-part highest-coefficient row and
physical source cross row. Their original-coordinate versions are obtained
by right multiplication by \(\mathsf U_Z\). The exact action identity is
\[
\boxed{\displaystyle
A_Z^*\Gamma_Z(T)+\Gamma_Z(T)A_Z-\Gamma_Z(T)
=\mathsf U_Z^*\{\epsilon g(\epsilon)^*g(\epsilon)
-\ell^*h_T-h_T^*\ell\}\mathsf U_Z.}
\tag{SK19}
\]
This is EG57 with all three rows evaluated. The two cross terms are not
replaced by the positive endpoint outer product. Absolute convergence and
Cauchy bounds give all derivative truncation estimates. The single-index
omission in SK17 is at most
\(|\Phi(w)|\epsilon^{1-\Re w}A_L/2\), and the double-index omission at most
\(\epsilon A(\epsilon)A_L/5\).

## 5. The first signed correction after the full quartet minimum

Retain the original quartet \(1/2\pm\delta\pm i\gamma\), \(0<\delta<1/2\),
\(\gamma>0\), with full common multiplicity \(m\). In each half order the
roots by heights \(+\gamma,-\gamma\), and retain all principal slots
\(0,\ldots,m-1\). Write \(G_+=\widehat G_{Z_+}\), and let \(J_+,J_-\)
insert the two highest-slot coordinates into the right and left halves.
Put
\[
H_+=J_+^*G_+^{-1}J_+,\quad H_-=J_-^*L_-^{-1}J_-,\quad
D_\gamma(T)=\operatorname{diag}(e^{i\gamma T},e^{-i\gamma T}).
\]
The full left inverse is taken before extracting these two entries.
The coefficient
\[
\boxed{\displaystyle
C_m(T)=\frac{\operatorname{Tr}
[H_+D_\gamma(T)H_-D_\gamma(T)^*]}{((2m-1)!)^2}>0}
\tag{SK20}
\]
is completely determined by SK16 and the original Cauchy matrix. Its bounds
\[
\frac{2\lambda_{\min}(H_+)\lambda_{\min}(H_-)}{((2m-1)!)^2}
\le C_m(T)\le
\frac{2\|H_+\|\|H_-\|}{((2m-1)!)^2}
\]
are uniform in \(T\). In particular no phase can make this coefficient
zero. Its right factor is explicitly
\[
H_+=\begin{pmatrix}a_m&t_m\\\bar t_m&a_m\end{pmatrix},\qquad
a_m=(2\delta)^{2m-1}\left(\frac{\delta^2+\gamma^2}{\gamma^2}\right)^m,
\quad t_m=\frac{(2\delta)^{2m}(2\delta+2i\gamma)^{2m-1}}{(2i\gamma)^{2m}}.
\tag{SK21}
\]
The diagonal follows by deleting the highest slot in the confluent Cauchy
determinant. For the off-diagonal, take the Hermite interpolation numerator
for a highest jet at the opposite root and evaluate its highest reflected
pole, exactly as EG14–15. It yields the displayed power and phase; in
particular \(|t_m|/a_m=\delta/\sqrt{\delta^2+\gamma^2}<1\).
The left entries can equivalently be written using cofactors of the fully
evaluated matrix SK16. Its size is \(2m\), independent of the tensor degree.

Let \(Q_+(T)\) be the **original** attained right-value quotient EG39, with
its entire left block. Let
\[
D_0(T)=4m\delta T-4m\log\left(2\left|\frac{\zeta^{(m)}(\rho)}{m!}\right|\right)
+2m^2\log\frac{\gamma}{2\delta\sqrt{\delta^2+\gamma^2}}.
\]
Then
\[
\boxed{\displaystyle
\log\det Q_+(T)=D_0(T)
-e^{-2\delta T}T^{4m-2}C_m(T)
+O_Z(e^{-2\delta T}T^{4m-3}).}
\tag{SK22}
\]
Thus the old error scale is now an evaluated, strictly negative leading
correction, not merely a bound for a possible Schur loss.

### Proof, retaining the resonant cross block

Use the original right transformation \(E_{+,T}=e^{T(A_{{\rm pp},+}-I/2)}\).
For a pair with the same height the transformed singular cross entry is
\[
e^{-\delta T+i\gamma_\rho T}
\int_0^T\frac{(-(T-t))^i t^j}{i!j!}dt
=e^{-\delta T+i\gamma_\rho T}
\frac{(-1)^iT^{i+j+1}}{(i+j+1)!}.
\]
For opposite heights, expansion or integration by parts gives a polynomial
of degree at most \(i+j\) multiplying the same decreasing exponential;
all original frequency denominators are \(\pm2i\gamma\ne0\). The regular
cross matrix is bounded by SK14, and multiplication by \(E_{+,T}^{-*}\)
costs at most \(e^{-\delta T}\sum_{j<m}T^j/j!\). Consequently the entire
transformed cross block is
\[
X(T)=\frac{(-1)^{m-1}e^{-\delta T}T^{2m-1}}{(2m-1)!}
J_+D_\gamma(T)J_-^*
+O_Z(e^{-\delta T}T^{2m-2}).
\]
The left block is
\(L_-+O_Z(e^{-2\delta T}T^{2m-2})\), with a bounded inverse tending to
\(L_-^{-1}\). The unminimized transformed right metric differs from
\(G_+\) by \(O_Z(e^{-2\delta T}T^{2m-2})\), by the exact finite correction.
Insert all three in the full Schur complement. Its leading correction is
negative and its trace relative to \(G_+\) is the term in SK22. The next
cross term has size \(O_Z(e^{-2\delta T}T^{4m-3})\). The logarithm's
quadratic remainder is \(O_Z(e^{-4\delta T}T^{8m-4})\), smaller than that
error. Finally restore the unchanged determinants of \(\mathsf U_+\) and
\(E_{+,T}\), giving \(D_0(T)\). This proof never removes the left minimum.

## 6. The full quartet's relative arithmetic spectrum

The left limiting Gram is SK16. Define its two evaluated rows
\[
\ell_{\rho,j}=\partial_\rho^j(1/\Phi(\rho))/j!,\quad
h_{\rho,j}=\partial_\rho^j(\mathfrak Z(\rho)/\Phi(\rho))/j!,
\quad \rho\in Z_-,
\]
and
\[
\boxed{\displaystyle
s_m=\sqrt{(\ell L_-^{-1}\ell^*)(h L_-^{-1}h^*)}\ \ge 2m\delta.}
\tag{SK23}
\]
All entries are now given by beta derivatives; this is a fixed \(2m\)-matrix
calculation, not an unknown growing native projection.
For the **whole original quartet** metric, the limiting relative weight
spectrum is
\[
\boxed{\displaystyle
\{4m\delta,\ -2m\delta+s_m,\ -2m\delta-s_m,
\underbrace{0,\ldots,0}_{4m-3}\}.}
\tag{SK24}
\]
The error in the ordered spectrum is
\(O_Z(e^{-\delta T}(1+T)^{2m-1})\). Coincident eigenvalues are treated
by their ordered min–max values, not by chosen eigenvectors.
In particular the limit of its positive trace is \(2m\delta+s_m\),
with excess \(s_m-2m\delta\) above the full-primary trace minimum
\(4m\delta\).

For a simple quartet let \(\alpha=1/2-\delta+i\gamma\) and
\(\mathfrak Z(\alpha)=u+iv\). Then the remaining scalar has the closed value
\[
\boxed{\displaystyle
s_1=\frac{2\delta\gamma\sqrt{u^2+v^2}}
{\sqrt{\gamma^2u^2-\delta^2v^2}}.}
\tag{SK25}
\]
The denominator is strictly positive; it is the determinant of the two
independent original left sources times explicit positive factors.

### Proof

Apply the simultaneous congruence
\(\mathsf U_Z^{-1}\operatorname{diag}(E_{+,T}^{-1},I)\).
It commutes with the transformed block arithmetic action. The metric tends
to \(\operatorname{diag}(G_+,L_-)\), with its cross block bounded above.
The right relative weight has one eigenvalue \(4m\delta\), by its exact
Cauchy displacement. On the left, the physical endpoint outer product tends
to zero and SK19 gives exactly \(-\ell^*h-h^*\ell\). Conjugation symmetry
of the original roots, \(\Phi\), and \(\mathfrak Z\) makes
\(\ell L_-^{-1}h^*\) real. Its real part is \(2m\delta\), by taking the
trace of the left action identity. Cauchy–Schwarz gives SK23. The nonzero
eigenvalues of this rank-at-most-two relative form are therefore
\(-2m\delta\pm s_m\). This proves SK24, including the possible zero branch.
The stated matrix convergence and the positive limiting block metric give
the ordered spectral error by finite-dimensional min–max.

For SK25 it is convenient to use the exactly congruent unnormalized basis
\((f_\alpha,f_{\bar\alpha})\). Its limiting Gram is
\[
L^{f}=\begin{pmatrix}u/\delta&\bar Z/(\delta+i\gamma)\\
Z/(\delta-i\gamma)&u/\delta\end{pmatrix},\quad Z=u+iv,
\]
with rows \(\ell^f=(1,1)\), \(h^f=(Z,\bar Z)\). Direct inversion gives
\[
\ell^f(L^f)^{-1}(\ell^f)^*=\frac{2\delta\gamma}{u\gamma-\delta v},
\quad h^f(L^f)^{-1}(h^f)^*=\frac{2\delta\gamma|Z|^2}{u\gamma+\delta v}.
\]
Their product proves SK25. Positivity gives \(u>0\) and
\(u^2\gamma^2-\delta^2v^2>0\). The change of basis is diagonal
multiplication by \(1/\Phi\), so it preserves the two displayed dual norms.

## 7. Critical primary: evaluate the retained coefficient and its next term

For one actual critical primary \(\rho=1/2+i\gamma\) of full multiplicity
\(m\), write \(P=|\Phi(\rho)|^2\), and put
\[
\boxed{\displaystyle
f_{00}=\frac{\Phi'(\rho)}{\Phi(\rho)}-
\frac{\mathfrak Z'(\rho)}{P}\ \in\mathbb R,\qquad
f_{01}=\frac12\left(\frac{\Phi''(\rho)}{\Phi(\rho)}-
\frac{\mathfrak Z''(\rho)}{P}\right)
-f_{00}\frac{\Phi'(\rho)}{\Phi(\rho)}.}
\tag{SK26}
\]
They are respectively \(\mathscr F(\bar\rho,\rho)\) and
\(\partial_w\mathscr F(\bar\rho,\rho)\), by SK6. Differentiating SK4
and using \(1-\rho=\bar\rho\) verifies the reality of \(f_{00}\).
The original critical determinant now has the expansion
\[
\boxed{\begin{aligned}
\log\det\Gamma_\rho(T)={}&m^2\log T
-2m\log\left(2\left|\frac{\zeta^{(m)}(\rho)}{m!}\right|\right)
+\log\prod_{j=0}^{m-1}\frac{j!}{(m+j)!}\\
&+\frac{m^2f_{00}}{T}
-\frac{m^2(m^2-1)\Re f_{01}+\frac12m^4f_{00}^2}{T^2}
+O_\rho(T^{-3}).
\end{aligned}}\tag{SK27}
\]
For \(m=1\) the first numerator term at order \(T^{-2}\) is zero;
there is no fictitious second jet in its Gram.

Indeed the exact critical metric is
\(D_TH_mD_T+F_\rho-B^{\rm reg}(T)\), with
\((H_m)_{ij}=1/[i!j!(i+j+1)]\) and
\(D_T=\operatorname{diag}(T^{j+1/2})\). Its first two normalized corrections
are \(f_{00}e_0e_0^*/T+(f_{01}e_0e_1^*+\bar f_{01}e_1e_0^*)/T^2\).
The exact inverse entries are
\((H_m^{-1})_{00}=m^2\),
\((H_m^{-1})_{01}=-m^2(m^2-1)/2\), by the Cauchy determinant/inverse
or the shifted Legendre basis. The first two terms of
\(\operatorname{Tr}\log(I+X)\) give SK27. All other normalized entries
are \(O(T^{-3})\), and SK10 makes the regular tail exponentially smaller.
The unchanged original unit determinant restores the zeta factor.

## 8. Exact finite spectrum: a fully specified cubic

The full physical identity SK19 also evaluates the finite spectral problem
without a `4m`-degree characteristic polynomial. In principal-part coordinates
put
\[
Y_T=[\sqrt\epsilon\,g(\epsilon)^*,\ \ell^*,\ h_T^*],\qquad
J=\begin{pmatrix}1&0&0\\0&0&-1\\0&-1&0\end{pmatrix},\qquad
M_T=Y_T^*\mathsf K_T^{-1}Y_T\succeq0.
\]
These are precisely the three evaluated physical rows, with the complete
original Gram inverse; no cross row is deleted. The relative weight is
congruent to \(\mathsf K_T^{-1/2}Y_TJY_T^*\mathsf K_T^{-1/2}\).
Its nonzero eigenvalues are the nonzero eigenvalues of \(JM_T\): the
identity \(\det(I+UV)=\det(I+VU)\) follows by eliminating either diagonal
block in \(\left(\begin{smallmatrix}I&U\\-V&I\end{smallmatrix}\right)\).
This proves the full characteristic identity
\[
\det(\lambda I-W_{\rm rel}(T))
=\lambda^{4m-3}\det(\lambda I_3-JM_T).
\]
The trace of the original relative weight is
\(2\Re\operatorname{Tr}A_Z-4m=0\), so \(\operatorname{Tr}(JM_T)=0\).
Also \(\det(JM_T)=-\det M_T\). Consequently, with
\(p_T=\tfrac12\operatorname{Tr}((JM_T)^2)>0\), its three remaining
values are exactly the three real roots of
\[
\boxed{\lambda^3-p_T\lambda+\det M_T=0.}
\tag{SK28}
\]
The strict positivity of \(p_T\) follows because the original right and
left eigenvectors have weight values \(\pm2\delta\) times their positive
norms; the Hermitian weight is not zero. Its other `4m-3` eigenvalues
are **exactly zero at every finite cutoff**, not only in the endpoint
limit. The cubic has the explicit real evaluation
\[
\lambda_j=2\sqrt{p_T/3}\cos\left[
\frac13\arccos\left(-\frac{3\sqrt3\det M_T}{2p_T^{3/2}}\right)
-\frac{2\pi j}3\right],\qquad j=0,1,2.
\]
The argument belongs to `[-1,1]` because the original relative matrix is
Hermitian. When \(\det M_T=0\), this formula includes the third zero;
when \(M_T\succ0\), inertia of the displayed `J` gives two positive
and one negative nonzero value. The finite matrix SK13 and all rows SK18
have already been evaluated. This cubic is a source-endpoint spectrum,
not the spectrum of a substituted native quotient.

## 9. High-height value of the simple-quartet excess

The scalar SK25 also has an explicit high-height expansion for the same
analytically defined source family, with fixed \(0<\delta<1/2\). This
statement concerns evaluation of that family as the height parameter grows;
it does not assert the existence of zeta zeros along such a path. Its result is
\[
\boxed{\displaystyle
s_1=\sqrt{\frac{22}{195}}
\left(\gamma^2+\delta^2-\frac{499}{26}\right)
+O_\delta(\gamma^{-2}).}
\tag{SK29}
\]
Here is a direct derivation with a finite resolvent remainder. Let
\(d\mu(y)=|\Phi(1/2+iy)|^2dy/(2\pi)\), and
\(\mu_{2j}=\int y^{2j}d\mu\). The exact transform used for SK3 gives
\[
\mu_0=33\sqrt2/64,\quad \mu_2=585\sqrt2/128,\quad
\mu_4=22455\sqrt2/256,\quad
\mu_6=1452915\sqrt2/512,\quad
\mu_8=141390945\sqrt2/1024.
\]
All odd moments vanish. On the left root \(\alpha=1/2-\delta+i\gamma\),
put \(z=\delta-i\gamma\). Finite geometric division in
\(1/(z+iy)\), including its last term, gives
\[
\mathfrak Z(\alpha)=\frac{\mu_0}{z}-\frac{\mu_2}{z^3}
+\frac{\mu_4}{z^5}-\frac{\mu_6}{z^7}+R_8,
\qquad |R_8|\le\frac{\mu_8}{\delta|z|^8}.
\]
This uses the original spectral measure and \(|z+iy|\ge\delta\), so
it bounds the full real line, including \(y\) near \(\gamma\).
Writing \(\mathfrak Z(\alpha)=u+iv\), elementary expansion yields
\[
\begin{aligned}
u={}&\mu_0\delta\gamma^{-2}
+\delta(3\mu_2-\mu_0\delta^2)\gamma^{-4}
+\delta(5\mu_4-10\mu_2\delta^2+\mu_0\delta^4)\gamma^{-6}
+O_\delta(\gamma^{-8}),\\
v={}&\mu_0\gamma^{-1}+(\mu_2-\mu_0\delta^2)\gamma^{-3}
+(\mu_4-6\mu_2\delta^2+\mu_0\delta^4)\gamma^{-5}
+O_\delta(\gamma^{-7}).
\end{aligned}
\]
Thus
\[
\gamma^2u^2-\delta^2v^2=
4\delta^2\mu_0\mu_2\gamma^{-4}
\left[1+\left(\frac{2\mu_2}{\mu_0}+\frac{2\mu_4}{\mu_2}
-3\delta^2\right)\gamma^{-2}+O_\delta(\gamma^{-4})\right].
\]
Substitute this and the corresponding expansion of \(|u+iv|^2\) into
SK25. Taking the positive square root gives
\(s_1=\sqrt{\mu_0/\mu_2}(\gamma^2+\delta^2-\mu_4/\mu_2)
+O_\delta(\gamma^{-2})\). The displayed moments yield SK29. In
particular this explicit original source metric has a quadratic high-height
positive-trace excess; a positive norm alone does not remove that calculated
arithmetic defect.

## 10. What is and is not completed

SK13 evaluates the finite original inverse-source Gram in every primary
slot; SK14–18 evaluate its regular and physical cross matrices; SK22
calculates the signed first correction of its full left-block quotient;
SK24–25 calculate the full-quartet relative endpoint spectrum; SK26–27
replace the critical coefficient formerly named by an integral and give
its next term. SK28 evaluates the full finite relative spectrum by a cubic;
SK29 gives the simple-family high-height coefficient with a finite moment
remainder.

The quotient in SK22 is exactly the source-endpoint right-value quotient
\(E_Z/E_{Z_-}\), through EG39. Its invertible comparison to Beurling is
EG53, and its nonzero boundary remains EG55. Neither map identifies it
with PRD's degree-k values `Z_R` and target `J` minimum. The original native
kernel return and the native same-class current numerators are not assigned
these endpoint values.

### Exact receiver back to the original one-factor minimum

The bridge to the original polynomial presentation is the original theta
map itself, not an identification of Gram matrices. Let \(d=\deg h_Z\),
\(f_0=\Theta\phi_*\), and \(R_Zu=\Theta\psi_u\). On the original
one-factor finite source its full quotient value is exactly
\[
\boxed{\displaystyle
u^*H_N^{(1)}u=
\min_{P\in\mathbb C[S]_{\le N-d}}
\|\Theta(\psi_u+P(D)\phi_*)\|_{L^2(dx)}^2.}
\tag{SK30}
\]
The polynomial space is zero at \(N=d-1\). To prove the equation, every
original representative in the same finite coefficient fibre is
\(R_Zu+P(D)f_0\), and \(D\Theta=\Theta D\) on the original Gaussian
source and the displayed inverse sources. Thus it equals exactly the
function inside this minimum. Its source coordinates are the same \(u,P\)
as in HG1–2. Before applying \(\Theta\), the finite physical-cutoff norm
of \(\psi_u\) is the evaluated SK13. After applying \(\Theta\), the
whole-line norm and the entire polynomial minimum in SK30 remain.
This displays the precise remaining operation rather than substituting
an endpoint Gram for the original attained theta metric. The original
HM multinomial and tensor maps then define the native convolution source.

## Classical references used

- NIST DLMF §5.12, Euler beta integral and gamma quotient (5.12.1):
  https://dlmf.nist.gov/5.12
- NIST DLMF §8.17, incomplete beta integral and complement (8.17.1, 8.17.4):
  https://dlmf.nist.gov/8.17
- NIST DLMF §1.14, Fourier/Mellin inversion and Parseval conventions:
  https://dlmf.nist.gov/1.14
- The pinned programme EG/HG proof above supplies the exact original
  source, arithmetic unit, cutoff and quotient maps. New deductions are
  proved here; no independent re-audit of its entire upstream corpus is claimed.
