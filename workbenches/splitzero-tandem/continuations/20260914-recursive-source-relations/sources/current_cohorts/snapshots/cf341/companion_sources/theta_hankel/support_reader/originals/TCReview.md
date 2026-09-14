# Independent review of the theta error bounds and finite rational witness

Date: 2026-09-13. The complete source tau_theta_hankel_error_control_20260913.tex, TC1–TC28, was read at SHA-256 55f7a9cce6f22b11a30321a7ba726f300a990e78c39780a43b7fdd692c7935e5. This review independently checks the tail estimates, finite algebra, explicit degree cutoff, coefficient rounding, and interval detection of a negative witness. The integration was not rerun, and the source was not edited.

**Finding.** The mathematical formulas TC1–TC26 are consistent with the retained source identities, and TC23 and TC25 give the claimed margins, including their endpoint cases. The finite positive-definiteness implication in TC27 follows from the stated exact pivot certificates; their complete numerical endpoint replay is the separate parent review. The displayed TC28 decimal enclosure matches its display string in certificate_dimension16_1024.json.

One prose correction was reported: “No coefficient is removed by the rounding rule” can be read as asserting that a nonzero coefficient never rounds to zero, which is false. The precise statement is: every original coefficient slot is included in the error estimate; nearest-grid rounding may produce zero. The theorem should explicitly specify rounding to a nearest multiple of \(1/H\), with either choice allowed at a tie. These changes clarify the already used bound \(1/(2H)\); no displayed inequality needs alteration.

## 1. Retained integral and complete positive tail bounds

The review uses the workbench's original reflection and Mellin identities stated before TC2, with \(g=2\xi\). There are two distinct factors of two: one in \(f_0=2\sum\phi_*\), and one from reflection of the even moment. Their product gives the factor four in TC2. Expanding
\[
y^Je^{y/2}(16x_n^2-24x_n)e^{-x_n},\qquad
x_n=\pi n^2e^{2y},
\]
gives exactly
\[
4y^J(4\pi^2n^4e^{9y/2}-6\pi n^2e^{5y/2})
e^{-\pi n^2e^{2y}}.
\tag{TR1}
\]
Thus TC2 and the callback TC9 agree with their original constants.

For \(y\ge0,n\ge1\), \(x_n\ge\pi>3/2\), so
\[
0\le y^Je^{y/2}(16x_n^2-24x_n)e^{-x_n}
\le16\pi^2n^4y^Je^{9y/2-\pi n^2e^{2y}}.
\tag{TR2}
\]
For the polynomial \(y^0\), its value at zero is one. For \(J>0\), the vanishing factor at zero creates no exception to the inequality.

For \(n=N+\ell\), \(\ell\ge0\), the elementary bounds
\((N+\ell)^4\le N^4e^{4\ell/N}\) and
\((N+\ell)^2\ge N^2+2N\ell\) imply
\[
\sum_{n=N}^{\infty}n^4e^{-\pi n^2e^{2y}}
\le
\frac{N^4e^{-\pi N^2e^{2y}}}
{1-e^{4/N-2\pi Ne^{2y}}}
\le\frac{N^4e^{-\pi N^2}}{1-r_N}.
\tag{TR3}
\]
Here \(r_N=e^{4/N-2\pi N}\in(0,1)\): \(4/N-2\pi N\le4-2\pi<0\) for \(N\ge1\). Multiplication by (TR2), bounding \(y^J\le L^J\) and \(e^{9y/2}\le e^{9L/2}\), and integrating over an interval of length \(L\) prove exactly
\[
T_{J,N,L}
=\frac{16\pi^2L^{J+1}e^{9L/2}N^4e^{-\pi N^2}}{1-r_N}.
\tag{TR4}
\]

For the omitted interval \(y>L\), use (TR3) with \(N=1\), retaining its exponential numerator. This gives
\[
I_J(y)\le\frac{16\pi^2}{1-r_1}
y^Je^{9y/2-\pi e^{2y}},\qquad r_1=e^{4-2\pi}.
\tag{TR5}
\]
For \(y=L+v\), \(v\ge0\), the inequalities
\((L+v)^J\le L^Je^{Jv/L}\) and
\(e^{2(L+v)}\ge e^{2L}(1+2v)\) yield
\[
y^Je^{9y/2-\pi e^{2y}}
\le L^Je^{9L/2-\pi e^{2L}}
e^{-(2\pi e^{2L}-9/2-J/L)v}.
\tag{TR6}
\]
Integrating when \(\lambda_J(L)=2\pi e^{2L}-9/2-J/L>0\) proves exactly
\[
Y_{J,L}
=\frac{16\pi^2L^Je^{9L/2-\pi e^{2L}}}
{(1-r_1)\lambda_J(L)}.
\tag{TR7}
\]
The first tail covers \(0\le y\le L,n\ge N\), and the second covers \(y>L,n\ge1\); their interiors are disjoint. The positive integrands permit Tonelli before integrability is established. The finite bounds then prove convergence and TC4.

At \(N=20,L=4,J\le64\), the exact denominator signs follow already from \(\pi>3\), \(e^8>41\):
\[
\frac4N-2\pi N<-\frac{599}{5},\qquad
4-2\pi<-2,\qquad
\lambda_J(4)>246-\frac92-16=\frac{451}{2}>0.
\tag{TR8}
\]
Thus the quoted actual-parameter sign check is correct.

For fixed \(J\), first choose \(L\) large enough to make \(Y_{J,L}\) arbitrarily small; its double-exponential decay dominates the polynomial and exponential factors. For that fixed \(L\), increase \(N\) to make \(T_{J,N,L}\) arbitrarily small. This is a sequential choice of \(L\), then \(N\), not a claim that the first tail tends to zero with \(L\) while \(N\) remains fixed.

The finite integrand is entire in complex \(y\): \(y^J\) has a nonnegative integer exponent, and all remaining operations are finite sums, products, and compositions of exponentials. There are no branch cuts, absolute values, or conjugations in the callback. Its analyticity therefore meets the recorded analytic-ball callback contract, including at \(y=0,J=0\).

## 2. Recurrence, interval propagation, and finite matrix signs

The retained entire-function identity \(F(z^2)=g(1/2+iz)\), together with the even moments, gives \(a_j=(-1)^jM_{2j}/(2j)!\). Extracting the coefficient of \(w^n\) from
\[
F(w)\sum_{n\ge0}b_nw^n=-F'(w)
\]
gives
\[
a_0b_n+\sum_{j=1}^{n}a_jb_{n-j}=-(n+1)a_{n+1},
\tag{TR9}
\]
which is TC11. The original \(a_0=M_0>0\) is retained in this recurrence.

Each interval operation encloses its exact operation. Induction on \(n\), with a positive lower bound for \(a_0\), therefore encloses every exact \(b_n\). Repeated use of an interval variable can increase enclosure width, but cannot invalidate containment.

For the exact symmetric matrix, the recursion TC13 successively constructs a unit lower triangular \(L\) and diagonal \(D\). At stage \(j\), the formula for \(L_{ij}\) gives
\[
A_{ij}=\sum_{k<j}L_{ik}D_kL_{jk}+L_{ij}D_j
\quad(i>j),
\]
and the pivot formula gives the same equality for \(i=j\), since \(L_{jj}=1\). Symmetry supplies the other half. Thus \(A=LDL^{\mathsf T}\). If all interval pivots have positive lower endpoints, induction proves that the exact pivots are positive and every division is defined. Hence for \(v\ne0\)
\[
v^*Av=\sum_jD_j|(L^{\mathsf T}v)_j|^2>0.
\tag{TR10}
\]
The vector is nonzero after the invertible triangular map. This proves the stated positive-definiteness implication.

For a real rational vector \(c\), let \(\gamma_n=\sum_{r+s=n}c_rc_s\). Expanding the complete quadratic form gives
\[
c^{\mathsf T}H_dc=\sum_{n=0}^{2d}\gamma_nb_n.
\tag{TR11}
\]
This includes off-diagonal cross terms twice in the coefficient convolution when their indices differ. If \(b_n\in[\ell_n,u_n]\), choosing \(u_n\) when \(\gamma_n\ge0\) and \(\ell_n\) when \(\gamma_n<0\) maximizes that term. Therefore TC15 is a valid rational upper bound. No square-modulus form is substituted for this real bilinear form.

## 3. Reciprocal-zero map and the full polynomial form

The source imports the workbench's absolutely summable reciprocal-zero expansion TC16. All deductions below retain those exact multiplicities and its full infinite tail. The coordinate map in TC17 is verified directly:
\[
-\frac1{(\delta+i\gamma)^2}
=\frac{\gamma^2-\delta^2+2i\gamma\delta}
{(\gamma^2+\delta^2)^2}.
\tag{TR12}
\]
Replacing \(\rho\) by \(1-\rho\) changes \(\rho-1/2\) to its negative and leaves the square unchanged. At a zero, \(\rho-1/2\ne0\), because the source value \(g(1/2)=M_0\) is positive. The map \(w=-(\rho-1/2)^2\) has nonzero derivative there. It preserves the local zero order, so the two reflected source zeros correspond to one zero of \(F\) of that same order. This is the exact multiplicity map used in TC16–TC17.

The finiteness of \(S_*=\sum_jm_j|\beta_j|\) implies \(\sup_j|\beta_j|<\infty\), since \(m_j\ge1\). Put \(R_*=\max\{1,\sup_j|\beta_j|\}\). For \(P(X)=\sum p_rX^r\),
\[
|P(\beta_j)|\le\sum_r|p_r|R_*^r=\|P\|_{R_*}.
\tag{TR13}
\]
Thus \(\mathcal Q(P)=\sum_jm_j\beta_jP(\beta_j)^2\) converges absolutely. It is real for real \(P\) because the reciprocal set and multiplicities are conjugation stable. Finite expansion of \(P^2\) gives TC19 exactly.

For real polynomials \(P,E\), the identity \((P+E)^2-P^2=2PE+E^2\), applied termwise in that absolutely convergent series, gives
\[
|\mathcal Q(P+E)-\mathcal Q(P)|
\le S_*\|E\|_{R_*}(2\|P\|_{R_*}+\|E\|_{R_*}).
\tag{TR14}
\]
This verifies TC20 without dropping any reciprocal zero or multiplicity.

## 4. Separator, explicit cutoff, and all edge cases

Fix a nonreal reciprocal zero \(\beta\), its conjugate, and their common multiplicity \(m\). Let \(r=|\beta|/2>0\). In TC21, “all other” excludes both selected points. Every element of \(\mathcal A\) contributes at least \(r\) to \(S_*\), so \(\#\mathcal A\le S_*/r\) and the set is finite. It is conjugation stable. Therefore \(B\) has real coefficients and \(B(\beta)\ne0\). The empty product is one if \(\mathcal A\) is empty.

Either choice of \(c\) with \(\beta c^2=-1\) is nonzero. Set \(w_N,u_N,v_N\) as in TC24. They satisfy
\[
u_N+v_N\beta
=\Re w_N-(\Re\beta)v_N+v_N(\Re\beta+i\Im\beta)
=w_N.
\tag{TR15}
\]
Consequently \(P_N(\beta)=c\), and real coefficients give \(P_N(\overline\beta)=\overline c\). The two selected summands of \(\mathcal Q(P_N)\) are each exactly \(-m\). Every other reciprocal zero of modulus at least \(r\) is a root of \(B\), so its entire weighted summand is zero, including its multiplicity.

For \(|X|\le r\), the literal product gives \(|B(X)|\le B_0\). Also
\[
\begin{aligned}
|u_N+v_NX|
&\le |\Re w_N|+(|\Re\beta|+r)|v_N|\\
&\le |w_N|\left(1+\frac{|\Re\beta|+r}{|\Im\beta|}\right).
\end{aligned}
\tag{TR16}
\]
Multiplication by \(|X|^N|B(X)|\), and using
\(|w_N|=|c|/(|\beta|^N|B(\beta)|)\), gives
\[
|P_N(X)|\le C_*2^{-N}.
\tag{TR17}
\]
This includes \(N=0\), with \(X^0\) the constant polynomial one. The full remaining reciprocal tail therefore has absolute contribution at most \(C_*^2T_*4^{-N}\), yielding
\[
\mathcal Q(P_N)\le-2m+C_*^2T_*4^{-N}.
\tag{TR18}
\]

If \(T_*=0\), the last term is zero for every \(N\ge0\). If \(T_*>0\), set \(A=C_*^2T_*/m>0\) and \(x=\log A/\log4\). When \(x\ge0\), \(1+\lfloor x\rfloor>x\), so every \(N\ge N_*\) satisfies \(N>x\). When \(x<0\), \(N\ge0>x\), regardless of whether the inner integer in TC23 is zero or negative. Hence in both cases
\[
A4^{-N}<1,\qquad C_*^2T_*4^{-N}<m.
\tag{TR19}
\]
In particular TC23 gives the claimed weak bound \(\mathcal Q(P_N)\le-m\). At \(A=4^s\) with integer \(s\ge0\), the chosen cutoff is \(s+1\), not \(s\); the boundary case is therefore safe. The formula is conservative by one degree at that boundary, and is mathematically valid as printed.

## 5. Rational coefficient accuracy and interval detection

The polynomial \(P_N\) has real coefficients and degree at most \(D=N+\#\mathcal A+1\). Retain all \(D+1\) coefficient slots, inserting exact zeros above its actual degree if necessary. For a positive integer \(H\), round each coefficient to a nearest element of \(H^{-1}\mathbb Z\). Either nearest element is allowed at a tie. The error polynomial \(E=\widetilde P_N-P_N\) then has
\[
|e_r|\le\frac1{2H},\qquad
\eta:=\|E\|_{R_*}\le
\frac{\sum_{r=0}^{D}R_*^r}{2H}.
\tag{TR20}
\]
Every denominator in TC25 is positive: \(m>0\), \(S_*>0\) because it includes the selected pair, and \(2\|P_N\|_{R_*}+1>0\). The finite geometric sum is positive. Thus a sufficiently large positive integer \(H\) always satisfies TC25.

The two bounds in TC25 give \(\eta\le1\) and
\(\eta\le m/[2S_*(2\|P_N\|_{R_*}+1)]\). By (TR14),
\[
\begin{aligned}
|\mathcal Q(\widetilde P_N)-\mathcal Q(P_N)|
&\le S_*\eta(2\|P_N\|_{R_*}+\eta)\\
&\le S_*\eta(2\|P_N\|_{R_*}+1)\le m/2.
\end{aligned}
\tag{TR21}
\]
Together with (TR18)–(TR19), this proves
\(\mathcal Q(\widetilde P_N)\le-m/2<0\).
The error estimate includes a coefficient that rounds from a nonzero value to zero; such rounding is permitted and does not invalidate the proof.

For clarity, the eventual finite-interval claim has a direct quantitative margin. Write \(c\) for the rational coefficient vector of \(\widetilde P_N\), define \(\gamma_n\) as in (TR11), and set \(A_c=\sum_n|\gamma_n|\). The polynomial is nonzero because its form is negative, so its square is nonzero and \(A_c>0\). If rational enclosing intervals for every required \(b_n\) have width at most \(m/(4A_c)\), then their signed upper bound satisfies
\[
U(c)-\mathcal Q(\widetilde P_N)
\le\sum_n|\gamma_n|(u_n-\ell_n)
\le m/4,
\qquad U(c)\le-m/4<0.
\tag{TR22}
\]
This proves an explicit sufficient finite enclosure width. There is no need to assume cancellation or independent errors.

For finitely many required coefficients, shrinking the moment intervals shrinks the resulting \(b_n\) intervals: TC11 uses finitely many additions, products, and reciprocals, and one can first restrict the \(a_0\) interval to have lower endpoint at least \(M_0/2>0\). Every such interval operation is continuous at those exact inputs; induction in \(n\) proves convergence of enclosure widths to zero. The positive tail bounds can be made arbitrarily small by the sequential choice of \(L,N\) established above.

The finite integral itself admits arbitrarily small validated errors. One direct existence proof uses the entire finite integrand \(f\) on \([0,L]\). On all unit complex discs about that interval, a finite bound for \(|f|\) is
\[
K=(L+2)^J e^{(L+1)/2}
\sum_{n=1}^{N-1}
\left(16\pi^2n^4e^{4(L+1)}+24\pi n^2e^{2(L+1)}\right)
e^{\pi n^2e^{2(L+1)}}.
\tag{TR23}
\]
Indeed \(\Re y\le L+1\), \(|y|\le L+2\), and
\(|e^{-\pi n^2e^{2y}}|\le e^{\pi n^2e^{2\Re y}}\).
Cauchy's derivative estimate on each unit circle gives \(|f'(x)|\le K\) for \(x\in[0,L]\). Composite midpoint quadrature on a uniform mesh of width \(h=L/s\) has error at most \(KLh/4\), by integrating \(K|x-x_{\mathrm{mid}}|\) on each interval. Finite evaluations of the explicit exponential expression can be enclosed to arbitrary accuracy; outward rational bounds for \(K\) suffice. If \(N=1\), the finite integrand is zero and this step is immediate. This proves the finite integration approximation needed for (TR22), independently of any fixed evaluation limit of the particular integration run.

## 6. Relation to the recorded finite certificate

For dimension \(16\), \(d=15\). The unshifted matrix uses \(b_0,\ldots,b_{30}\), and the shifted one uses \(b_1,\ldots,b_{31}\). TC11 computes these from \(a_0,\ldots,a_{32}\), hence exactly the stated \(33\) even moments \(M_0,M_2,\ldots,M_{64}\). The index ranges are consistent. Positivity of both sets of sixteen exact pivots proves TC27 by (TR10); every smaller leading matrix is positive definite by restriction of the same positive quadratic form.

The parent performs the complete rational endpoint and replay audit. This subreview supplies the independent mathematical derivation and does not turn a finite-dimensional sign result into a claim at larger dimensions. Likewise the separator theorem constructs and bounds the witness associated with each specified nonreal reciprocal zero; it asserts no universal cutoff and supplies no nonreal zero of the actual zeta function.
