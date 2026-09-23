# Original zeta, the complete Cauchy correction, and the reflected index

This calculation starts with the meromorphic function \(\zeta\), its signed divisor, and the original rational tests. Its raw divisor pairing is generally not Hermitian. The fixed Gamma and endpoint divisor supplies an explicitly retained correction. The correction, together with the original pairing, reconstructs the Cauchy–Weil form and all its finite-jet and exterior blocks. At the previously admissible real poles \(\sigma=3,5,\ldots\), the reflected test has a pole at a trivial zero. Ordinary evaluation there is undefined. We give an extension in the original local coordinate, prove its residue formula with the full local units, and calculate its difference from a parameter finite part.

The earlier CK, NI and FJ results apply to the compensated receiver proved below. They do not assign a positive or negative index to the uncorrected original-zeta pairing. No Riemann-hypothesis sign is proved here.

## 1. Original function, factors, and test domains

Retain all factors
\[
C(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2),\qquad
r(s)=\frac{\zeta'(s)}{\zeta(s)},\qquad
q(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
\tag{OZK1}
\]
The products and quotients are meromorphic identities. In particular the Gamma pole and polynomial zero at 0 remain separate factors even though their product is a unit there. The precise local units and fractional lattices are UZ6–UZ24, read in full for this calculation. They prove
\[
\operatorname{div}C=[1]-\sum_{m\ge1}[-2m],\qquad
\operatorname{div}\zeta=\sum_{\rho\in\mathcal Z}m_\rho[\rho]
 +\sum_{m\ge1}[-2m]-[1].
\tag{OZK2}
\]
Here \(\mathcal Z\) consists of distinct nontrivial zeros, with their original positive multiplicities. The sums of divisors are locally finite. The actual zero estimate is
\(\sum_{|\rho|>R}m_\rho/|\rho|^2=O(\log(R+2)/R)\), by AG1–AG5. Nothing in (OZK2) identifies supported zero with either a complex coordinate or the unsupported element.

Let \(\mathscr A\) be the space of rational functions \(A(s)=O(s^{-2})\) at infinity whose finite poles avoid \(\mathcal Z\). The subspace \(\mathscr A^\circ\) also excludes poles at \(1,-2,-4,\ldots\). On this latter domain the ordinary signed-divisor trace and the completion-divisor trace are
\[
\begin{aligned}
R_\zeta(A)&=\sum_\rho m_\rho A(\rho)+\sum_{m\ge1}A(-2m)-A(1),\\
E_C(A)&=A(1)-\sum_{m\ge1}A(-2m),\\
Q_\zeta(A)&=R_\zeta(A)+E_C(A)=\sum_\rho m_\rho A(\rho).
\end{aligned}\tag{OZK3}
\]
All sums converge absolutely: the nontrivial sum uses the displayed zero estimate, the real sum has tail \(O(m^{-2})\), and the omitted bounded region contains finitely many points. The last equality is a calculation with both retained divisor terms. It is not permission to delete either of them.

For \(\Re z,\Re w>1\), the original Cauchy tests are
\[
F_z(s)=(s-z)^{-1},\quad
F^\#(s)=\overline{F(1-\bar s)},\quad
A_{z,w}(s)=F_z^\#(s)F_w(s)
=-\frac1{(s-(1-\bar z))(s-w)}.
\tag{OZK4}
\]
Their poles avoid \(\mathcal Z\). They belong to \(\mathscr A^\circ\) exactly when \(z\notin\{3,5,7,\ldots\}\); the other pole \(w\) cannot be a fixed divisor point on this domain. The original single-pole algebra and all its powers are
\[
\mathcal R_\sigma=\operatorname{span}_{\mathbb C}\{Q_j:j\ge0\},
\quad Q_j(s)=(s-\sigma)^{-j-1},\quad \sigma>1,
\quad A_{jk}=Q_j^\#Q_k.
\tag{OZK5}
\]
They are proper rational functions; each product \(A_{jk}\) belongs to \(\mathscr A\). We retain every \(\sigma>1\), including resonant odd integers.

## 2. Defined finite parts at the resonant poles, with every unit

For a meromorphic germ in the fixed coordinate \(h=s-a\), define
\(\operatorname{FP}_a A=[h^0]A(a+h)\). This is the constant Laurent coefficient, not a value of a function with a pole. For a meromorphic function \(f\) which is not identically zero, write its unique local factorization in this coordinate as
\[
f(a+h)=h^{n_a}u_{f,a}(h),\quad u_{f,a}(0)\ne0,\qquad
\frac{f'}f=\frac{n_a}{h}+\frac{u_{f,a}'}{u_{f,a}}.
\tag{OZK6}
\]
If \(A=\sum_{k=-p}^\infty a_kh^k\) and
\(u_{f,a}'/u_{f,a}=\sum_{l\ge0}b_lh^l\), direct multiplication gives
\[
\operatorname{Res}_a(Af'/f)
=n_a a_0+\sum_{l=0}^{p-1}a_{-l-1}b_l.
\tag{OZK7}
\]
Thus its divisor contribution and its regular-unit contribution are different specified functionals of the same germs. On a bounded contour enclosing finitely many divisor points and test poles, subtracting the second term of (OZK7) at each test pole from the full logarithmic-derivative integral yields the sum of \(n_a\operatorname{FP}_aA\). This proves a local-contour definition of the extension; it does not interpret undefined ordinary evaluation as a scalar.

In particular at \(a=-2m\), \(m\ge1\), UZ12–UZ14 gives the complete unit
\[
\begin{aligned}
C(a+h)&=h^{-1}c_m(h),\\
c_m(h)&=\kappa_m\left(1-\frac h{2m}\right)
\left(1-\frac h{2m+1}\right)\pi^{-h/2}\Gamma(1+h/2)
\prod_{l=1}^{m}\left(1-\frac h{2l}\right)^{-1},\\
\kappa_m&=(-1)^m\frac{2m(2m+1)\pi^m}{m!},\qquad
\zeta(a+h)=h\,u_m(h).
\end{aligned}\tag{OZK8}
\]
Both \(u_m\) and \(c_m\) are units. The analytic product is
\(C\zeta=c_mu_m\), not the product of two scalar fibre values. Hence
\[
r(a+h)=h^{-1}+u_m'/u_m,\quad
q(a+h)=-h^{-1}+c_m'/c_m,\quad
r+q=(c_mu_m)'/(c_mu_m).
\tag{OZK9}
\]
At 1, with \(h=s-1\), the corresponding factors are
\(\zeta=h^{-1}u_1\),
\(C=h c_1\),
\(c_1(h)=\tfrac12(1+h)\pi^{-(1+h)/2}\Gamma((1+h)/2)\),
\(u_1(0)=1\), \(c_1(0)=1/2\).
The orders are \(-1,+1\), and the two regular-unit logarithmic derivatives again add. At zero the whole unit is
\(C(h)=(h-1)\pi^{-h/2}\Gamma(1+h/2)\), with value \(-1\). These equations preserve all Gamma and endpoint contributions.

Extend (OZK3) to \(\mathscr A\) by replacing each fixed-point evaluation with its just-defined finite part:
\[
\begin{aligned}
R_\zeta^{\rm fp}(A)&=\sum_\rho m_\rho A(\rho)
 +\sum_{m\ge1}\operatorname{FP}_{-2m}A-\operatorname{FP}_1A,\\
E_C^{\rm fp}(A)&=\operatorname{FP}_1A
 -\sum_{m\ge1}\operatorname{FP}_{-2m}A,\\
Q_\zeta(A)&=R_\zeta^{\rm fp}(A)+E_C^{\rm fp}(A).
\end{aligned}\tag{OZK10}
\]
Only finitely many summands differ from ordinary evaluations, so absolute convergence persists. The identities (OZK7)–(OZK9) prove that the two original logarithmic-derivative contour calculations add with all their unit terms. The full unit is required for this calculation even though the signed-divisor receiver afterwards records only the order and constant Laurent coefficient.

A useful global residue expression makes the extra collision term explicit. Write \(\mathcal P(A)\) for the test poles and \(n_f(a)=\operatorname{ord}_a f\). For \(f=\zeta,C\),
\[
T_f^{\rm fp}(A)
=-\sum_{a\in\mathcal P(A)}\operatorname{Res}_a(Af'/f)
+\sum_{a\in\mathcal P(A)}n_f(a)\operatorname{FP}_aA.
\tag{OZK11}
\]
Here \(T_\zeta=R_\zeta\), \(T_C=E_C\). To prove this globally, differentiating the reciprocal Gamma product of UZ6 gives the normally convergent expansion
\[
q(s)=\frac1{s-1}-\frac{\gamma+\log\pi}{2}
 +\sum_{m\ge1}\left(\frac1{2m}-\frac1{s+2m}\right).
\tag{OZK12}
\]
The \(1/s\) term of (OZK1) and the \(-1/s\) term from Gamma are accounted for by this derived equality. For \(r+q\), AG7 supplies a normally convergent genus-one expansion over \(\mathcal Z\). Subtracting (OZK12) supplies the expansion for the original \(r\), with its pole at 1, all trivial zeros, all nontrivial zeros, and its constant. Constant terms contribute zero to \(\sum_{a\in\mathcal P(A)}\operatorname{Res}_a A\). For each divisor point not in the test pole set, the residues of \(A(s)/(s-x)\) at the test poles sum to \(-A(x)\). For a point inside that pole set they sum to zero, since they then include all finite poles and the rational function has zero residue at infinity. The added term in (OZK11) restores exactly its specified constant Laurent coefficient. Normal convergence on finitely many small circles justifies every residue interchange. At resonant points the last two collision terms for \(\zeta,C\) cancel because their orders are opposite, and their complete local units add as in (OZK9).

## 3. Exact raw kernel and complete correction matrix

Set \(a=1-\bar z\), \(d_{z,w}=w+\bar z-1=w-a\). At a nonresonant point, evaluation of the two test residues in (OZK11) gives
\[
\begin{aligned}
R_\zeta(A_{z,w})&=\frac{r(w)-r(a)}{w-a},\\
E_C(A_{z,w})&=\frac{q(w)-q(a)}{w-a}
=A_{z,w}(1)-\sum_{m\ge1}A_{z,w}(-2m),\\
Q_\zeta(A_{z,w})&=
\frac{r(w)+q(w)-r(a)-q(a)}{w-a}.
\end{aligned}\tag{OZK13}
\]
The original functional equation gives
\((r+q)(1-\bar z)=-\overline{(r+q)(z)}\). Consequently the last line equals the earlier CK kernel, but now with every original derivative term retained as
\[
Q_\zeta(A_{z,w})=
\frac{\zeta'(w)/\zeta(w)+\overline{\zeta'(z)/\zeta(z)}
+q(w)+\overline{q(z)}}{w+\bar z-1}.
\tag{OZK14}
\]
The separate raw term in (OZK13) uses \(r(1-\bar z)\), not its unsupported replacement by \(-\overline{r(z)}\).

At \(a=-2m\), write \(r(a+h)=h^{-1}+r_a^{\rm reg}(h)\),
\(q(a+h)=-h^{-1}+q_a^{\rm reg}(h)\), as calculated in (OZK9). Formula (OZK11) gives instead
\[
R_\zeta^{\rm fp}(A_{z,w})
=\frac{r(w)-r_a^{\rm reg}(0)}{w-a},\qquad
E_C^{\rm fp}(A_{z,w})
=\frac{q(w)-q_a^{\rm reg}(0)}{w-a}.
\tag{OZK15}
\]
For verification, the direct test constant at that point is
\(\operatorname{FP}_a A_{z,w}=(w-a)^{-2}\). In the residue sum this cancels the extra \(-(w-a)^{-2}\) arising from the pole of \(r\), while the two signs reverse for \(q\). Their sum in (OZK15) is (OZK14). Thus all original real Cauchy poles are included by a defined calculation.

Now fix \(\sigma>1\), put \(d=2\sigma-1\), and define
\(R_{jk}=R_\zeta^{\rm fp}(A_{jk})\),
\(E_{jk}=E_C^{\rm fp}(A_{jk})\),
\(C_{jk}=R_{jk}+E_{jk}\). The exact correction in the original power basis is
\[
\begin{aligned}
D_{jk}(\sigma)&:=R_{jk}-C_{jk}=-E_{jk}\\
&=\sum_{m\ge1} b_{m,jk}(\sigma)
 -\frac1{(-\sigma)^{j+1}(1-\sigma)^{k+1}},\\
b_{m,jk}(\sigma)&=
\frac1{(2m+1-\sigma)^{j+1}(-2m-\sigma)^{k+1}}
\quad (\sigma\ne2m+1),\\
b_{m,jk}(2m+1)&=
\frac{(-1)^{j+k}}{(4m+1)^{j+k+2}}
\binom{j+k+1}{j+1}.
\end{aligned}\tag{OZK16}
\]
Every index is an integer \(j,k\ge0\); no factorial is suppressed. At a resonant point, \(A_{jk}(a+h)=(-1)^{j+1}h^{-j-1}(-d+h)^{-k-1}\). The binomial series for the last factor shows its constant coefficient is the term with power \(h^{j+1}\), precisely the last line. The remaining series has tail \(O(m^{-j-k-2})\), proving convergence.

This correction cannot be assigned an inertia as if it were Hermitian. For every real nonresonant \(\sigma>1\), direct subtraction gives the strict result
\[
R_{01}-R_{10}=D_{01}-D_{10}
=\sum_{m\ge1}\frac{4m+1}
 {(2m+1-\sigma)^2(2m+\sigma)^2}
+\frac1{\sigma^2(\sigma-1)^2}>0.
\tag{OZK17}
\]
Indeed \(A_{01}(x)-A_{10}(x)=(1-2x)/((1-x-\sigma)^2(x-\sigma)^2)\). At \(-2m\) this is positive; subtracting its value at 1 adds the final positive term. The compensated \(C_{01}=C_{10}\) is real. Thus the full raw original-zeta matrix is genuinely non-Hermitian in this original basis. A negativity claim for that raw form cannot be substituted for Weil negativity.

Finite part in the original variable and finite part in the moving pole parameter are also different. At \(a=-2m\), use the antiholomorphic coordinate \(X=\bar z-\sigma\), with real base \(\sigma=2m+1\), so \(z=\sigma+\bar X\); its divisor summand is
\(-X^{-1}(a-w)^{-1}\), whose constant coefficient in \(X\) is zero. Its direct \(s\)-coordinate finite part at \(X=0\) is \((w-a)^{-2}\). For the whole basis, direct \(s\)-finite-part entry minus the nonnegative \((X,Y)\) Laurent coefficient, with \(Y=w-\sigma\), equals the last line of (OZK16). The raw kernel has a parameter pole there and is not assigned a convergent Taylor expansion at that pole. In contrast \(R+E\) has its singular terms cancelled by the proved identities (OZK9), (OZK15), and has the holomorphic parameter germ (OZK14).

The passage retaining both original quantities is the invertible triangular map
\[
(R,E)\longmapsto(R+E,E),\qquad
(Q,E)\longmapsto(Q-E,E).
\tag{OZK18}
\]
It acts entrywise on every finite matrix and on the entire coefficient tower. Keeping only \(Q\) would have a kernel; (OZK18) keeps the original correction as an independent component and has the displayed inverse.

## 4. Reconstructed coefficient tower with full arithmetic derivatives

On \(\sigma>1\) the Euler product gives the absolutely convergent derivative series
\[
\begin{aligned}
r_n&=\frac{r^{(n)}(\sigma)}{n!}
=\frac{(-1)^{n+1}}{n!}\sum_{l\ge2}\Lambda(l)(\log l)^n l^{-\sigma},\\
q_n&=\frac{q^{(n)}(\sigma)}{n!}
=(-1)^n\left(\sigma^{-n-1}+(\sigma-1)^{-n-1}\right)
-\mathbf1_{n=0}\frac{\log\pi}{2}
+\frac{\psi^{(n)}(\sigma/2)}{2^{n+1}n!},\qquad \ell_n=r_n+q_n.
\end{aligned}\tag{OZK19}
\]
The series may be differentiated on compact subsets of \(\Re s>1\), using uniform domination by \(\sum\Lambda(l)(\log l)^n l^{-1-\epsilon}\). Expanding only the now proved compensated germ gives
\[
\begin{aligned}
C_{jk}={}&\sum_{n=0}^{j}(r_n+q_n)
\frac{(-1)^{j+k-n}\binom{j+k-n}{k}}{d^{j+k-n+1}}\\
&+\sum_{n=0}^{k}(r_n+q_n)
\frac{(-1)^{j+k-n}\binom{j+k-n}{j}}{d^{j+k-n+1}}.
\end{aligned}\tag{OZK20}
\]
This follows from the geometric denominator series of (OZK14) at \(z=w=\sigma\), retaining the two occurrences of the constant numerator coefficient. The coefficients of the rational tests are \(Q_j\) because
\((s-\sigma-Y)^{-1}=\sum_{j\ge0}Y^jQ_j(s)\). The square-summable zero tail and the distance from \(\sigma\) to the critical strip justify termwise parameter derivatives of the compensated zero sum. Equations (OZK16), (OZK19), (OZK20) compute \(R,E,C\) independently of undefined raw Taylor coefficients at resonances.

For example, the full first determinant is
\[
\det(R_{jk}+E_{jk})_{0\le j,k\le1}
=\frac{4(r_0+q_0)^2-d^2(r_1+q_1)^2}{d^4}.
\tag{OZK21}
\]
This is obtained from entries \(C_{00}=2\ell_0/d\),
\(C_{01}=C_{10}=\ell_1/d-2\ell_0/d^2\),
\(C_{11}=-2\ell_1/d^2+4\ell_0/d^3\). The raw determinant \(\det R\) is a different determinant. All larger determinants are those of the explicitly specified entry sums, not the sum of separate determinants.

## 5. Exact indices and full jets, reconstructed from the original trace

Let \(\mathcal H=\ell^2(\mathcal Z,m)\), with its conjugate-linear-first inner product, and let \((Jv)_\rho=v_{1-\bar\rho}\). The original functional equation, with its multiplier (OZK1), proves equality of the paired multiplicities and \(J^*=J=J^{-1}\). Direct substitution in (OZK10) gives
\[
R_\zeta^{\rm fp}(F^\#G)+E_C^{\rm fp}(F^\#G)
=\langle J\operatorname{ev}F,\operatorname{ev}G\rangle_{\mathcal H},
\qquad (\operatorname{ev}F)_\rho=F(\rho).
\tag{OZK22}
\]
Every critical-line point contributes one positive direction. On a distinct exchanged pair of weight \(m\), the vectors
\((\delta_\rho\pm\delta_{\rho^\#})/\sqrt{2m}\) have signs \(+1,-1\). Denote the counts of these signs by \(\kappa_+,\kappa_-\); they count distinct reflected supports, not multiplicity sums.

For completeness, the evaluation range of the original powers is dense. If \(h\in\mathcal H\) is orthogonal to every \((\rho-\sigma)^{-j-1}\), its Cauchy transform
\(\sum_\rho m_\rho\bar h_\rho/(\rho-z)\) converges normally away from the discrete zero set. On a compact \(|z|\le M\), its tail after \(|\rho|>R>2M+1\) is bounded by
\(2(\sum_{|\rho|>R}m_\rho|h_\rho|^2)^{1/2}(\sum_{|\rho|>R}m_\rho/|\rho|^2)^{1/2}\).
All its derivatives vanish at \(\sigma\), so the identity theorem on the connected complement of the zero set makes it identically zero there. Its residue at \(\rho\) is \(-m_\rho\bar h_\rho\), proving \(h=0\). If any finite initial set of powers is deleted, the same argument makes the transform a polynomial near \(\sigma\), then throughout its domain; its residues still vanish. The identical argument works for Cauchy poles in any set with an accumulation point in \(\Re z>1\). The compensated extension (OZK15) includes any resonant poles of such a set.

Each finite negative orthonormal family in \(\mathcal H\) can be approximated by evaluation vectors so closely that its Gram matrix remains negative definite. In detail, for an isometric negative column operator \(U:\mathbb C^n\to\mathcal H\), an approximating column operator \(V\) with \(\|V-U\|<1/4\) satisfies
\(V^*JV\le(-1+2\|V-U\|+\|V-U\|^2)I<-7I/16\).
Conversely a negative subspace injects into the negative spectral space of \(J\), because a vector with zero negative projection has nonnegative value. This proves both inequalities in
\[
\begin{aligned}
\sup_{N\ge J_0}n_\pm((R_{jk}+E_{jk})_{J_0\le j,k\le N})&=\kappa_\pm
\quad(J_0\ge0),\\
\mathrm{RH}&\Longleftrightarrow
(R_{jk}+E_{jk})_{0\le j,k\le N}\succeq0
\text{ for every }N\ge0.
\end{aligned}\tag{OZK23}
\]
The plus-index proof uses positive orthonormal vectors and the bound \(1-2\|V-U\|-\|V-U\|^2>7/16\). A finite list of approximants uses a common finite number of powers, proving the finite-section claims. For finite \(\kappa_-\) some finite section attains it and all larger sections retain it. For infinite \(\kappa_-\), these finite negative indices are unbounded. No universal finite decision cutoff follows. This proves the CK and NI index statements on the reconstructed original-zeta receiver, while (OZK17) prevents applying them to raw \(R\).

All nontrivial local algebras are literally the same ideals in their original stalks:
\[
\mathcal O_\rho/(\zeta)_\rho
=\mathcal O_\rho/(C\zeta)_\rho
\simeq\mathbb C[v]/(v^{m_\rho}),\qquad v=s-\rho,
\tag{OZK24}
\]
because \(C\) is a unit at every \(\rho\in\mathcal Z\). This is a proof about ideals, not an assertion that units have no derivatives. In these algebras multiplication by \(a_0+a_1v+\cdots\) has trace \(m_\rho a_0\), and the reflected coefficient map is \(a_{\rho,k}\mapsto(-1)^k\overline{a_{\rho^\#,k}}\). Define the algebra of all local jets whose constant vector is in \(\mathcal H\). Its evaluation map onto \(\mathcal H\) has the constant section and kernel
\(\mathcal N=\prod_\rho(v)\mathbb C[v]/(v^{m_\rho})\).
The compensated multiplication-trace form is (OZK22), with radical exactly \(\mathcal N\). Indeed its constant quotient is nondegenerate and every higher coefficient has zero multiplication trace. Moreover
\(\mathcal N^r=\prod_\rho(v^r)\mathbb C[v]/(v^{m_\rho})\),
\(\bigcap_r\mathcal N^r=0\), and the algebra is the inverse limit of these quotients: each finite local component stabilizes once \(r\ge m_\rho\), while the constant vector is already fixed at \(r=1\). The full raw receiver has the additional fixed-divisor data in (OZK10), which are not elements of this nontrivial-zero quotient.

## 6. Finite prescribed jets and every complementary block

Take a finite reflection-stable \(S\subset\mathcal Z\), with retained orders \(r_a=r_{a^\#}\ge1\), and let
\[
\begin{aligned}
P_S(s)&=\prod_{a\in S}(s-a)^{r_a},\quad d_S=\sum_{a\in S}r_a,
\quad W_S(s)=P_S(s)/(s-\sigma)^{d_S},\\
j_SF&=(\sum_{k<r_a}F^{(k)}(a)v_a^k/k!)_{a\in S},\qquad
\mathcal J_S=\bigoplus_{a\in S}\mathbb C[v_a]/(v_a^{r_a}).
\end{aligned}\tag{OZK25}
\]
The map is onto: for jets \(f\), the Chinese remainder theorem gives a unique polynomial \(N_f\) of degree below \(d_S\) with
\(N_f\equiv(s-\sigma)^{d_S}f_a(s-a)\pmod{(s-a)^{r_a}}\).
Then \(N_f/(s-\sigma)^{d_S}\) is a proper rational section. Divisibility of the numerator proves \(\ker j_S=W_S\mathcal R_\sigma\). On \(\mathcal Z\setminus S\), both \(W_S\) and its inverse are bounded: they approach 1 at infinity and have no zeros or poles on the finitely many remaining supports in any bounded region. Hence the Cauchy-transform proof in Section 5 proves that exterior evaluations of this exact kernel are dense. Adding the section shows that \((j_SF,F|_{\mathcal Z\setminus S})\) has dense image in \(\mathcal J_S\oplus\ell^2(\mathcal Z\setminus S,m)\), with its first coordinate achieved exactly.

Put \(B_S(f,g)=\sum_{a\in S}m_a\bar f_{a^\#,0}g_{a,0}\). For any specified Hermitian matrix \(H\) on these finite jets, the reconstructed whole form is exactly
\[
R_\zeta^{\rm fp}(F^\#G)+E_C^{\rm fp}(F^\#G)+H(j_SF,j_SG)
=(B_S+H)(j_SF,j_SG)
 +\langle J_{\rm ext}F|_{\rm ext},G|_{\rm ext}\rangle.
\tag{OZK26}
\]
Consequently its negative index is
\(\kappa_{{\rm ext},-}+n_-(B_S+H)\), and its positive index is
\(\kappa_{{\rm ext},+}+n_+(B_S+H)\).
To prove equality rather than merely an upper bound, approximate any finite definite spectral family of the bounded direct-sum operator \(A=(B_S+H)\oplus J_{\rm ext}\) by the just-proved dense rational image. The error in its Gram matrix is at most
\(\|A\|(2\|U\|\|V-U\|+\|V-U\|^2)\), which can be made less than half its least definite eigenvalue. The upper bound follows from injection into the corresponding spectral subspace. This includes all higher local coefficients, which may enter \(H\), and the full exterior sign count.

The original raw form on the left without \(E_C\) instead equals the right side minus \(E_C(F^\#G)\). The latter is an infinite fixed-divisor correction and is generally not Hermitian. It cannot be represented by changing only the finite local block \(B_S\).

For a finite coefficient matrix split into any two specified sets of indices, retain each block \(R_{ab}\), \(E_{ab}\), \(C_{ab}=R_{ab}+E_{ab}\). On the domain where the displayed block \(C_{11}\) is invertible, its exact complementary block is
\[
\mathcal S=(R_{22}+E_{22})
 -(R_{21}+E_{21})(R_{11}+E_{11})^{-1}(R_{12}+E_{12}).
\tag{OZK27}
\]
Multiplying the full Hermitian matrix on the right by
\(T=\left(\begin{smallmatrix}I&-C_{11}^{-1}C_{12}\\0&I\end{smallmatrix}\right)\)
and on the left by \(T^*\) gives \(\operatorname{diag}(C_{11},\mathcal S)\). Thus its determinant is \(\det C_{11}\det\mathcal S\) and its inertia is the sum of the two inertias, with every original term in (OZK27). This statement has the indicated matrix domain; no inverse is assigned to a singular block. It is not the sum of separate raw and Gamma Schur complements.

At a height cutoff \(T\ge\max(1,2\max_l|\Im z_l|)\), retain the full \(E_C\) and all raw trivial zeros while truncating only the nontrivial divisor. The difference between the reconstructed full matrix and that cutoff matrix is bounded by
\[
4n\sum_{|\Im\rho|>T}\frac{m_\rho}{|\Im\rho|^2}
\le8n\sum_{|\rho|>T}\frac{m_\rho}{|\rho|^2}.
\tag{OZK28}
\]
Each rank-one summand has norm at most \(4n/|\Im\rho|^2\) because its two evaluation vectors each have norm at most \(2\sqrt n/|\Im\rho|\). The second inequality uses \(0<\Re\rho<1\). This is an operator-norm tail estimate, not a sign for the complement.

## 7. Original-zeta heat equation and the retained collision coefficients

The source heat kernel has its original factor \(8\), while the original zeta coordinate is explicitly
\[
\zeta_t(s)=\frac{8}{\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)}
\int_0^\infty e^{tu^2}\Phi(u)\cosh(2(s-\tfrac12)u)\,du,
\quad \zeta_0=\zeta.
\tag{OZK29}
\]
The full \(\Phi\) is the original UZ2 series, with its constants \(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\) and exponential \(e^{-\pi n^2e^{4u}}\). Direct differentiation and the fixed factor give
\[
\partial_t\zeta_t=\tfrac14[\zeta_t''+2q\zeta_t'+(q'+q^2)\zeta_t],
\quad r_t=\zeta_t'/\zeta_t,\quad
\partial_t r_t=\tfrac14\partial_s[r_t'+r_t^2+2qr_t+q'+q^2].
\tag{OZK30}
\]
These are UZ26–UZ32 with their derivation retained. At every real time the integral is positive on the real axis. Thus the simple trivial zeros and the simple pole at 1 of the returned family remain, with their time-dependent local units, and neither real Cauchy test pole meets a moving nontrivial zero. Every fixed rational matrix is holomorphic on a complex time neighbourhood of that real time, by the finite-pole residue formula and AG1–AG9. In particular, including the resonant finite-part definition,
\[
R_{jk}(t)=C_{jk}(t)+D_{jk}(\sigma),\qquad
\partial_t^nR_{jk}(t)=\partial_t^nC_{jk}(t)\ (n\ge1),
\tag{OZK31}
\]
where \(D_{jk}\) is the exact time-independent matrix (OZK16). The zeroth terms are different. For complex Cauchy poles the common time neighbourhood is restricted to those on which their actual pole values remain nonzero, as in AG6; a fixed complex right half-plane for all negative times is not asserted.

For a fixed finite contour around an original nontrivial zero \(\rho\) of multiplicity \(m\), write
\(\zeta(\rho+v)=v^m u_\zeta(v)\),
\(a_\zeta=u_\zeta'(0)/u_\zeta(0)\), and
\(a=a_\zeta+q(\rho)\). The singular part of the bracket in (OZK30) is
\(m(m-1)v^{-2}+2m(a_\zeta+q(\rho))v^{-1}\).
Its differentiated residue proves directly on the original zeta coordinate
\[
\dot R_{\rho,0}(A)
=-\frac{m(m-1)}4A''(\rho)
-\frac m2\bigl(a_\zeta+q(\rho)\bigr)A'(\rho).
\tag{OZK32}
\]
The holomorphic Gamma terms in this disc have zero divisor integral, but their derivative \(q(\rho)\) survives in (OZK32). The unit comparison is \(u_{C\zeta}(v)=C(\rho+v)u_\zeta(v)\); it proves every higher unit derivative by the product rule as well. On a critical-line zero, the original functional equation makes \(a\) purely imaginary; it need not make \(a_\zeta\) purely imaginary.

For (OZK33)–(OZK35), fix a critical-line zero \(\rho=1/2+i\gamma\), with \(\gamma\in\mathbb R\), and real time \(t\). Reflection fixes this stalk and acts by \(v\mapsto-\bar v\). At an off-line zero it instead pairs two distinct stalks, whose complete paired block is governed by (OZK22) and (OZK26), not by the following single-stalk matrix. For the original fixed-test coefficients \(F(\rho+v)=f_0+f_1v+f_2v^2+\cdots\), put \(b_m=m(m-1)/2\). Substituting the exact two derivatives of \(F^\#G\) into (OZK32) gives
\[
M^{[1]}_\rho(t)=
\begin{pmatrix}
m&-tm(a_\zeta+q(\rho))/2&-tb_m\\
tm(a_\zeta+q(\rho))/2&tb_m&0\\
-tb_m&0&0
\end{pmatrix}.
\tag{OZK33}
\]
For \(m\ge2,t\ne0\), the \((0,2)\) block has one sign of each kind and inverse with zero \((0,0)\) entry. Its Schur complement is exactly \(tb_m\), so the determinant is \(-t^3b_m^3\), with inertia \((2,1,0)\) for positive \(t\), \((1,2,0)\) for negative \(t\). The vector \((tb_m/m,0,1)\) has value \(-t^2b_m^2/m\). This is a statement about the first Taylor matrix. It is not a negative value of the actual full positive-time cluster.

For \(m=1\), the second-derivative coefficient \(b_m\) is zero. The upper two-by-two determinant is \(-t^2|a_\zeta+q(\rho)|^2/4\). When \(t(a_\zeta+q(\rho))\ne0\), that block has one sign of each kind and the third coordinate is zero. When this product is zero, the inertia is \((1,0,2)\). These conclusions follow from the displayed matrix, including its unit derivative; multiplicity one does not justify setting that derivative to zero.

The exact counterpart for an off-line point \(\rho\) uses \(\rho^\#=1-\bar\rho\ne\rho\). Their multiplicities agree, and their full regular-unit coefficients satisfy \(a_{\rho^\#}=-\bar a_\rho\), with \(a_\rho=a_{\zeta,\rho}+q(\rho)\), by the original functional equation. Let \(M(a,t)\) denote the displayed matrix (OZK33) with its full coefficient replaced by \(a\). Reflection sends the three-jet at one point to the conjugated jet at the other, with signs \((1,-1,1)\). Applying (OZK32) at both points therefore gives the paired block, in the ordering \((f_\rho,f_{\rho^\#})\),
\[
\begin{pmatrix}0&M(a_\rho,t)^*\\M(a_\rho,t)&0\end{pmatrix},
\qquad a_{\rho^\#}=-\bar a_\rho.
\tag{OZK33a}
\]
For \(m\ge2\) and real \(t\ne0\), \(\det M=-t^3b_m^3\ne0\). Write \(M=U\Sigma V^*\) with positive diagonal singular values \(\Sigma\). Conjugating the paired block by \(\operatorname{diag}(V,U)\) gives \(\left(\begin{smallmatrix}0&\Sigma\\\Sigma&0\end{smallmatrix}\right)\), with one positive and one negative eigenvalue per singular value. Thus its inertia is \((3,3,0)\). This is the paired first Taylor form; the critical-line actual-cluster calculations below keep their specified domain.

The actual leading roots in \(v=i\xi/2\) follow from applying the displayed heat equation to the leading order \(v^m\). Its second derivative term alone has the smallest scaling degree under \(v=O(\sqrt t)\); the regular connection terms and full unit determine the next orders. The resulting leading polynomial in \(\xi/\sqrt t\) is
\(P_m(y)=\sum_{j=0}^{\lfloor m/2\rfloor}(-1)^jm!y^{m-2j}/(j!(m-2j)!)\).
Its second and fourth power sums, by Newton's identities, are \(2m(m-1)\) and \(4m(m-1)(2m-3)\). Therefore for the same prescribed test vector and the precise proper-rational section in (OZK25), the actual local value is
\[
R_{\rho,t}(F_t^\#F_t)
=\frac{m(m-1)(m-2)}4t^2+O(t^3).
\tag{OZK34}
\]
Indeed the retained negative coefficient is \(-b_m^2/m\); the additional \((2,2)\) entry contributes \(p_4/16\), and their sum is the displayed value. Terms with higher bounded test coefficients have degree at least five in \(\xi\), or have an extra factor \(t\) from \(f_0\). Their symmetric power sums are analytic in \(t\); odd degrees begin at the next integer power. This gives the stated remainder, exactly as the contour Taylor argument in FJ20–FJ22.

For a double zero the full unit enters the first nonzero result. Set \(\delta=\rho-\sigma\), prescribe \((f_0,f_1,f_2)=(t/2,0,1)\), and take the section (OZK25) of order three. At time zero it is \(\delta^3v^2/(\delta+v)^3\), so \(f_3(0)=-3/\delta\). Substitution in (OZK30) gives
\(v_\pm=\pm i\sqrt{t/2}-(a_\zeta+q(\rho))t/2+O(t^{3/2})\).
The leading polynomial has distinct real roots in \(\xi\), and the real implicit function theorem preserves their reality for small positive time. The exact returned local form is thus a sum of squared values, and substitution yields
\[
\begin{aligned}
R_{\rho,t}(F_t^\#F_t)
&=\left|-(a_\zeta+q(\rho))+\frac3{2\delta}\right|^2t^3+O(t^4),\\
\left|-(a_\zeta+q(\rho))+\frac3{2\delta}\right|^2
&\ge\frac{9(\sigma-1/2)^2}{4|\rho-\sigma|^4}>0.
\end{aligned}\tag{OZK35}
\]
The inequality uses the proved imaginary character of \(a_\zeta+q(\rho)\), and the original real part of \(1/\delta\). Analyticity of the contour trace removes half-integer powers from the remainder. The fixed-divisor correction of the whole test still belongs to (OZK31); it does not belong to this small nontrivial cluster. Equations (OZK26)–(OZK28) retain its exterior complementary block separately.

## 8. All support labels and exact endpoint compensation

For the original finite bounded distributive support lattice \(L\), the SZW10 carrier over meromorphic amplitudes is
\[
G_L(\mathcal M)=\{(f,1_L):f\in\mathcal M\}
\cup\{z_\lambda=(0,\lambda):\lambda\ne1_L\},\qquad
e=(0,1_L),\quad\tau=z_{0_L}.
\tag{OZK36}
\]
Only top-labelled elements can have nonzero amplitudes. The coordinate space
\(W_L=\bigoplus_{\lambda\in L}\mathbb C\mathbf e_\lambda\) is instead a space of trace values on labels; arbitrary complex function values on lower points are not nonzero amplitudes in (OZK36). Scalar section maps such as UZ44 fix every \(z_\lambda\), so an output with zero top amplitude is \(e\), not \(\tau\).

For all Cauchy tests above, including resonant ones, the inverse Mellin test on the critical strip is the exponential-polynomial inverse in AG13–AG15. Its poles remain strictly outside that strip, so the rational-test extension of the full arithmetic formula remains valid. It retains the original signed prime functional and archimedean functional, and gives
\[
\begin{aligned}
P_{\rm fin}(h)&=\sum_p\sum_{k\ge1}(\log p)p^{-k/2}
\{h(k\log p)+h(-k\log p)\},\\
A_\infty(h)&=\frac1{2\pi}\int_{\mathbb R}\widehat h(t)
\{\Re\psi(1/4+it/2)-\log\pi\}\,dt,\qquad
\widehat h(t)=\int_{\mathbb R}h(v)e^{-itv}\,dv.
\end{aligned}\tag{OZK36a}
\]
Both converge absolutely on these rational inverse-Mellin tests: they decay exponentially with rate strictly greater than \(1/2\), and their critical-line transforms are \(O((1+|t|)^{-2})\), whereas the digamma factor is \(O(\log(2+|t|))\). Explicitly, for (OZK4), \(h(v)=(w+\bar z-1)^{-1}e^{-(\bar z-1/2)v}\) on \(v\ge0\) and \((w+\bar z-1)^{-1}e^{(w-1/2)v}\) on \(v\le0\). Integrating each half-line gives (OZK4) on \(1-\Re z<\Re s<\Re w\); the equality outside this strip is meromorphic continuation, not convergence of the integral there. Higher powers are obtained by the corresponding parameter derivatives, which preserve these estimates after a small decrease of the exponential rate. In these full formulas the support receiver is
\[
\begin{aligned}
\boldsymbol B_L(A)&=(A(0)+A(1))\mathbf e_{1_L}
 +A(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol D_L(A)&=(P_{\rm fin}(h_A)-A_\infty(h_A))\mathbf e_{1_L}
 +A(0)\sum_{\lambda\ne1_L}\mathbf e_\lambda,\\
\boldsymbol R_L(A)&=R_\zeta^{\rm fp}(A)\mathbf e_{1_L},\qquad
\boldsymbol E_L(A)=E_C^{\rm fp}(A)\mathbf e_{1_L},\\
\boldsymbol B_L-\boldsymbol R_L
&=\boldsymbol D_L+\boldsymbol E_L,\qquad
\boldsymbol B_L-\boldsymbol R_L-\boldsymbol E_L=\boldsymbol D_L.
\end{aligned}\tag{OZK37}
\]
Thus using the full original-zeta divisor changes the arithmetic companion by the displayed \(\boldsymbol E_L\). Keeping the old arithmetic companion while silently replacing the nontrivial trace by the raw trace would fail by exactly this vector. Lower coordinates have identical values on the two original terms and remain labelled; their equality is not a deletion of their carrier points.

Projection onto the top coefficient and summation over all labels both recover \(Q_\zeta\) from \(\boldsymbol R_L+\boldsymbol E_L\). Their kernels on \(W_L\) differ: the former is the span of lower basis vectors, the latter is the hyperplane where coordinate sum is zero. The invertible triangular comparison (OZK18), applied to the two top coefficients and the identity on every lower coordinate, proves the exact support-preserving relation. Under a top-preserving label map \(f:L\to M\), each lower coefficient acquires its full count \(\#\{\lambda\ne1_L:f(\lambda)=\mu\}\) at label \(\mu\) on both sides of (OZK37); direct substitution proves the equality after pushforward as well.

Finally, imposing \(F^{(j)}(0)=F^{(j)}(1)=0\) for \(j<r\) gives the exact test subspace
\(s^r(s-1)^r(s-\sigma)^{-2r}\mathcal R_\sigma\).
Its multiplier and inverse are bounded on \(\mathcal Z\), so Section 5 proves density and the same compensated index \(\kappa_-\). It kills both endpoint values in (OZK37), but does not kill the fixed trivial-zero sum in \(E_C\). More generally finite interpolation at 0,1 and the exterior-density argument give, for every specified Hermitian endpoint matrix \(H_e\),
\[
\operatorname{ind}_-\{R_\zeta^{\rm fp}+E_C^{\rm fp}+H_e\}
=\kappa_-+n_-(H_e).
\tag{OZK38}
\]
The pairings on the left are applied to \(F^\#G\), and the endpoint form to \((F(0),F(1))\). For the previously studied matrix
\(\left(\begin{smallmatrix}1/2&-5/6\\-5/6&1/2\end{smallmatrix}\right)\), its eigenvalues are \(-1/3,4/3\), so the index is \(\kappa_-+1\). This reconstructs the FJ endpoint statement with the entire original-zeta correction retained. It supplies no sign theorem for RH.

## Sources and exact reading scope

The complete local factors, invertible sheaf, original-zeta heat equation and rational divisor map are [UZ1–UZ53](FAITHFUL_UNCOMPLETED_ZETA_HEAT.md). The present calculation read and used CK1–CK19, NI1–NI32 and FJ1–FJ29a in full; these are [the Cauchy criterion](CAUCHY_WEIL_POSITIVITY_CRITERION.md), [the reflection index](CAUCHY_REFLECTION_INDEX_DERIVATION.md), and [the finite-jet/complement proof](FINITE_JET_COMPLEMENT_AND_HEAT_TRUNCATION.md). AG1–AG17 was read here for the growth, rational-residue and arithmetic-test domains. The new calculations are the raw logarithmic-derivative kernel, its complete correction matrix and resonant finite-part extension, the non-Hermitian defect, the full-factor heat and local-unit reconstruction, and the supported companion identity (OZK37). The earlier arguments are rederived above on those original-function receivers.

Human source definitions enter through Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, [arXiv:1801.05914v5 author source](https://arxiv.org/src/1801.05914v5), equations `hoz`, `sas`, `phidef`, `htdef`, with UZ1–UZ4 retaining their exact factors. The underlying explicit formula is Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, [arXiv:math/9811068v1 author source](https://arxiv.org/src/math/9811068v1), Appendix II, Theorem 6, in the conventions proved in [SZW19–SZW38, pinned proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c022a0adde0a6aa3d8fc8e43ef42795d88e44b0/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). These links identify the human sources already read and applied by the source proofs; this reconstruction did not newly read their full papers. The exact Gamma product needed in (OZK12) is derived in UZ6 and differentiated here. No historical novelty is asserted for Cauchy-transform density, Hermite interpolation, elementary inertia, or classical equivalent RH criteria.




## Original-zeta Gaussian and affine receiving maps

The complete extension OZG1–55 proves that Gaussian convolution of the test at every positive time makes the original trivial-zero scalar sum diverge for every real translation. Its admissible replacement retains each cutoff trace and the Gamma boundary with the identical finite sum U_N; OZG20–27 gives both maps and the inverse. The full coefficient tower, its raw non-Hermitian correction and exact compensated negative index are OZG28–39. No compact-support prime window is assumed after smoothing; all prime powers and Gamma terms, with explicit error bounds, are OZG40–52. This extension acts on the tests while fixing the original zeta zeros.

The different affine change of the actual original heat family is OZR1–36. Its multiplier is exp(chi) C(phi)/C, with the full inverse, exceptional units and local jets. The original generator contains every q derivative term. The signed divisor comparison is OZR19–24; its Cauchy logarithmic kernel has an additional growth contribution 2a. OZR33 proves the exact full negative index after that contribution is retained. The full support carrier and every lower coordinate are OZG53–55 and OZR34–36. These are the receiving maps for these specified extensions; the original preceding test, time and domains remain those stated in its proof.
