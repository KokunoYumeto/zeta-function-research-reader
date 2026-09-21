# The actual outgoing polynomial under source activation
## A sharp activation profile and the complete four-cutoff minimum return

21 September 2026. Additive research continuation.

## Result and scope

Fix the original common-multiplicity quartet, its full arithmetic unit, its
ordered tensor source and the same tensor section at every cutoff. Write
\(e=1+k(m_0-1)\), \(q=e(k+1)^2\), \(k\equiv1\pmod4\), and
\(\ell=\log(q/k)\). All asymptotics hold at fixed original packet, weights and
section data. Constants do not hide a moving root or period.

For \(0<b<1\), set
\[
 \alpha_k(b)=e^{-2bq\ell},\qquad
 \Psi_b(s)=b\psi((1+s-b)/b).
 \tag{A1}
\]
For \(b\ge1\) set \(\Psi_b(s)=\psi(s)\), and set \(\Psi_0=0\).
The original function is
\[
 \psi(t)=(1+t)(1-\log(1+t))
       -\frac t4\lambda(2/t,\pi/t).
\]
It uses the Euler constant of \(V_t(x)=(\pi/t)\sqrt{x}-(2/t)\log x\).
Define \(\mathfrak F(u)=\int_0^u\psi(t)\,dt\).

The new full source-minimum coefficient is
\[
 {\cal C}(b)=
 \begin{cases}
 0,&b=0,\\
 4b^2[\mathfrak F(2/b-1)-\mathfrak F(1/b-1)],&0<b<1,\\
 C_B,&b\ge1,
 \end{cases}
 \qquad C_B=4\mathfrak F(1).
 \tag{A2}
\]
For the unchanged four signs \(+,+,-,-\) at \(q-1,q,2q-1,2q\),
\[
 {\cal R}\log\det G_N(\alpha_k(b))
       ={\cal C}(b)q^2+o_h(q^2),
 \qquad
 {\cal R}\Delta_N(\alpha_k(b))
       =[C_B-{\cal C}(b)]q^2+o_h(q^2).
 \tag{A3}
\]
Here \(\Delta_N(\alpha)=\log\det G_N-\log\det G_N(\alpha)\).
These are actual source and joint-minimum metrics, not an assigned action
allowance. The complete original observation has the same leading coefficient
when its kernel has the original rank \(8k-16\). Its individual current phase
is not determined by these determinant identities.

The proof derives a sharp norm for the specific outgoing polynomial, not just
a comparison of ambient metric condition numbers. For \(n=N+1\), let
\(p_n\) be the real-\(y\) monic source polynomial, \(\omega_n=\|p_n\|_\mu^2\),
and \(f_n=[p_n/\sqrt{\omega_n}]\). Then
\[
 \frac1q\log\|f_n\|_{G_N(\alpha_k(b))}
   =\Psi_b((n-q)/q)+o_h(1),\qquad b>0.
 \tag{A4}
\]
The error is uniform throughout the original window. On compact subintervals
of \(0<b<1\) it is
\(O_h(1/\ell+k\log^2(q+2)/q)\).

For any sequence with \(-\log\alpha_k=o(q\ell)\), a separate elementary
construction proves
\[
 \sup_{q-1\le N\le2q}\log^+\|M\|_{G_N(\alpha_k)}=o_h(q).
 \tag{A5}
\]
Consequently both full and actual observed heat gaps vanish at every time
\(e^{-2\sigma q}\), \(\sigma>0\). No condition comparing a fixed activation
exponent with \(\sigma\) remains.

## 1. Original objects and finite input bounds

Use
\[
 S=c+iy,\quad c=k/2,\quad
 d\mu(y)=w_h^{*k}(y)\,dy,\quad
 Q(y)=i^{-q}\chi_k(c+iy).
\]
All roots of \(Q\), repeated with their original orders, have modulus at most
\(R=k\sqrt{\delta^2+\gamma^2}\). The value space is
\(\mathbb C[y]/(Q)\), with its original physical injection
\(U_h^{\otimes k}\beta\). The change from \(S\)-monic to \(y\)-monic
polynomials is \(p_n^{(y)}(y)=i^{-n}p_n^{(S)}(c+iy)\).

Let \(T=G_{k,1}\), and let \({\cal R}\) be the fixed supplied tensor section.
Use \(n_*=2q+2\). The preceding coercivity and section results give finite
positive constants \({\bf L},{\bf B}\) such that
\[
 \|[F]\|_T\le\sqrt{\bf L}\,\|F\|_\mu,\qquad \deg F\le n_*,
 \quad
 \|{\cal R}v\|^2\le{\bf B}\|v\|_T^2,
 \tag{A6}
\]
and the first inequality also holds for the full tensor value of every
polynomial of separate degree at most \(n_*\).
Their logarithms are \(O_h(k\log^2(q+2))=o_h(q)\).
In particular
\[
 {\bf L}^{-1}T\preceq G_N^J\preceq{\bf B}T,\qquad
 \|M\|_T\le K_T:=R+e/2=O_h(k).
 \tag{A7}
\]
The second bound retains the full nilpotent weighted shifts.

The original scalar arithmetic/Gamma comparison supplies
\[
 c_-\|P\|_\sigma^2\le\|P\|_\mu^2\le c_+\|P\|_\sigma^2,
 \quad
 \log(c_+/c_-)=O_h(k\log^2(q+2)),
 \tag{A8}
\]
through degree \(n_*\), with
\(\sigma(y)=|\Gamma(1/4+iy/2)|^2/(2\pi)\) and
\(M_\sigma=\sqrt{2\pi}\).
One can take the following coefficient bounds, on the eventual guard \(q\ge8\):
\[
 g_-= \frac{c_-M_\sigma e^{-2q}}
 {(n_*+1)(2n_*+1)6^{2n_*}},\qquad
 g_+=c_+M_\sigma(n_*+1)5^{2n_*}.
 \tag{A9}
\]
Then
\[
 g_-\|\operatorname{coef}P(q\cdot)\|_2^2
 \le\|P\|_\mu^2
 \le g_+\|\operatorname{coef}P(q\cdot)\|_2^2.
\]
For the upper bound, multiplication by \(y/q\) has Gamma norm at most five
through these degrees, and sum the squared monomial norms. For the lower
bound the scaled monic Gamma polynomials have roots in \([-5,5]\), coefficient
one-norm at most \(6^j\), and orthonormalizing factor at most
\(M_\sigma^{-1/2}e^q\sqrt{2j+1}\). The sum of squared coefficient norms of
that orthonormal basis bounds the inverse coefficient Gram.

Retain the complete Hermite bound from the preceding proof:
\[
 \|\operatorname{coef}r(k\cdot)\|_2
 \le\nu_-^{-1/2}\|[r]\|_T,\quad \deg r<q,\qquad
 -\log\nu_-=O_h(q).
 \tag{A10}
\]
For specificity, with \(d_{\rm sep}=2\min(\delta,\gamma)\),
\(b_0=\min(1,d_{\rm sep})\), \(R_0=\sqrt{\delta^2+\gamma^2}\), it suffices to set
\[
 V_-=qe\,e^{4q+4ek}b_0^{-(q-e)}(1+R_0)^{q-1}
          \max(1,4k/d_{\rm sep})^{e-1},\quad
 \nu_-=a_{\min}^k k^{-2(e-1)}V_-^{-2}.
\]
This is the full confluent interpolation map. No jet or unit coefficient
has been replaced by a reduced-root value.

The activated covariance is exactly
\[
 C_N(\alpha)=G_N(\alpha)^{-1}
 =(1-\alpha)G_N^{-1}+\alpha(G_N^J)^{-1}.
 \tag{A11}
\]
Its physical norm is the complete minimum on \(X_N\oplus Z_N\),
\(Z_N=(I-P_{X_N})\operatorname{im}{\cal R}\), with squared norm
\(\|x\|^2+\alpha^{-1}\|z\|^2\).
At \(\alpha=1\) this is the unchanged joint-source norm; at \(0<\alpha<1\)
the displayed penalty is part of the source definition.

## 2. The exact auxiliary Taylor-matching minimum

For \(1\le L<n\), define
\[
 \nu_{n-L}^{(L)}
 =\min_{\substack{U\ {\rm monic}\\\deg U=n-L}}
       \int |y|^{2L}|U(y)|^2\,d\mu(y),\qquad
 J_{n,L}=\sqrt{\nu_{n-L}^{(L)}/\omega_n-1}.
 \tag{A12}
\]
Then
\[
 J_{n,L}
 =\min_{\substack{\deg P<n\\
   P^{(j)}(0)=\phi_n^{(j)}(0),\,0\le j<L}}\|P\|_\mu,
 \qquad \phi_n=p_n/\sqrt{\omega_n}.
 \tag{A13}
\]
Indeed the residual is \(y^LU/\sqrt{\omega_n}\) with \(U\) monic.
Conversely every such residual gives an admitted \(P\).
Since \(\phi_n\) is orthogonal to every polynomial of degree less than \(n\),
its residual norm squared is \(1+\|P\|^2\).
This proves A12--A13 before any asymptotic or quotient substitution.

A useful fully elementary upper bound is
\[
 J_{n,L}\le
 \sqrt{c_+/c_-}\,2^L\sqrt{2n+1}.
 \tag{A14}
\]
Use the Gamma monic polynomial of degree \(n-L\) for \(U\), apply the
Gamma multiplication bound \(L\) times, and compare its norm and
\(\omega_n\) by A8. The remaining factorial ratio is bounded by \(2n+1\).

## 3. Quantitative return to the actual quotient

Write
\(\rho_N(\alpha)=\|f_n\|_{G_N(\alpha)}\), \(n=N+1\).
Set
\[
 d_+(L,\alpha)
 =\sqrt{\frac{{\bf B}{\bf L}}{\alpha}}
       \sqrt{\frac{g_+}{g_-}}(K_T/q)^L,
 \tag{A15}
\]
\[
 d_1(L,\alpha)
 =\sqrt{\frac{g_+{\bf L}}{\nu_-}}\,
       \sqrt\alpha\,(q/k)^{L-1},
 \tag{A16}
\]
\[
 d_2(L)=
 \sqrt{\frac{g_+L(n_*+1)}{g_-}}
 \left(\frac2{1-R/q}\right)^q
 (R/q)^{q-L+1}.
 \tag{A17}
\]
On \(R<q/2\), \(1\le L<q\), the exact finite bounds are
\[
 \boxed{
 \frac{(J_{n,L}-d_2(L))_+}{1+d_1(L,\alpha)+d_2(L)}
 \le\rho_N(\alpha)
 \le J_{n,L}+d_+(L,\alpha)\sqrt{1+J_{n,L}^2}.
 }\tag{A18}
\]

For the upper bound take the minimizer in A13 and put
\(R_L=y^LU_{n-L}/\sqrt{\omega_n}\).
The vector \(P_L+{\cal R}[R_L]\) has exactly the original full tensor value
\(f_n\). Splitting its section term into \(X_N\) and its full orthogonal
normal part gives penalized norm at most
\(\|P_L\|+\alpha^{-1/2}\|{\cal R}[R_L]\|\).
By A6--A9,
\[
 \|[R_L]\|_T
 \le K_T^L\sqrt{\bf L}\,\|U_{n-L}/\sqrt{\omega_n}\|_\mu
 \le \sqrt{\bf L}\sqrt{g_+/g_-}(K_T/q)^L\|R_L\|_\mu .
\]
This proves the upper bound with every source cross term represented by
the physical orthogonal splitting, rather than set to zero.

For the lower bound let \(P+z\) be the actual minimum in A11. Then
\(\|P\|\le\rho_N\), \(\|z\|\le\sqrt\alpha\,\rho_N\), and
\[
 r=\operatorname{rem}_Q(\phi_n-P),\qquad
 \|r\|_T\le\sqrt{{\bf L}\alpha}\,\rho_N.
\]
Let \(\Pi_L\) mean literal Taylor truncation below degree \(L\). A9--A10
give \(\|\Pi_Lr\|_\mu\le d_1\rho_N\).

For any polynomial \(F\) through degree \(n_*\), divide \(F=QH+r_F\).
On \(|y|=q\), the Laurent coefficients of \(F/Q\) give
\[
 |[y^j]H|
 \le \sup_{|y|=q}|F(y)|q^{-q-j}(1-R/q)^{-q}.
\]
The original root coefficients satisfy
\(|[y^t]Q|\le\binom qtR^{q-t}\), including all multiplicities.
Therefore every scaled coefficient below degree \(L\) of \(QH\) is
bounded by
\[
 \sup_{|y|=q}|F(y)|
 \left(\frac2{1-R/q}\right)^q(R/q)^{q-L+1}.
\]
Using A9 and Cauchy--Schwarz for the coefficient vector proves
\[
 \|\Pi_L(F-\operatorname{rem}_QF)\|_\mu\le d_2(L)\|F\|_\mu.
\]
Apply this to \(F=\phi_n-P\).
The polynomial \(P+\Pi_LF\) matches the first \(L\) jets of \(\phi_n\).
Consequently
\[
 J_{n,L}\le(1+d_1+d_2)\rho_N+d_2,
\]
which proves A18.

The auxiliary ideal \((y^L)\) has not replaced the original relation
\((Q)\). The term A17 is the full original-relation correction that permits
return from Taylor matching to the original quotient.

## 4. Evaluate the auxiliary minimum

Uniformly for \(L/q\) in a compact subset of \((0,1)\) and \(q\le n\le2q+1\),
\[
 \boxed{
 \log J_{n,L}
 =L\psi((n-L)/L)
 +O_h(k\log^2(q+2)+\log(q+2)).
 }\tag{A19}
\]
The source comparison A8 contributes only
\(\log(c_+/c_-)\), not the determinant dimension.

Here are the Gamma asymptotic details. Put \(r=n-L=2h+\varepsilon\),
\(\varepsilon\in\{0,1\}\), and use the exact parity substitution
\(y=L\sqrt x\).
The original Gamma density gives a prefactor \(L^{2n+1/2}\) and the
potential
\[
 V_t(x)=\frac\pi t\sqrt x-\frac2t\log x,\qquad t=r/L,
\]
with the retained bounded-parameter factor
\[
 x^{\varepsilon+\varepsilon/t-3/4}
          e^{-\pi\varepsilon\sqrt x/(2t)}.
\]
On the equilibrium interval this factor is bounded above and below.
The global Gamma upper envelope bounds the full complementary integral;
the Gamma lower envelope on the interval supplies the matching lower bound.

The monic norm for degree \(h\) in this potential has logarithm
\(-h\lambda(2/t,\pi/t)+O(\log(h+2))\), uniformly on compact positive
\(t\)-intervals. A direct proof uses the arcsine probability of the
equilibrium support for the lower bound: Jensen gives
\(2h\log\operatorname{cap}-h\int V_t\,d\omega+O(1)
=-h\lambda+O(1)\).
For the upper bound choose midpoint equilibrium quantiles as the zeros
of a monic polynomial. Truncating \(\log|x-y|\) at distance \(1/h\),
the quantile discrepancy and its total variation give an \(O(\log h)\)
error uniformly on bounded \(x\)-intervals. The Euler inequality bounds
the exponential by \(e^{-h\lambda}\); near zero the positive logarithmic
barrier and at infinity the square-root barrier bound the remaining
integrals. Uniform support separation and bounded equilibrium densities
hold on compact positive \(t\)-intervals. Thus no fixed-parameter
asymptotic is evaluated at a moving singular endpoint.

Restoring the exact scaling and subtracting
\(\log\gamma_n=2n\log n-2n+O(\log(n+2))\) gives
\[
 \log(\nu_r^{(L),\Gamma}/\gamma_n)
 =2L\psi(t)+O(\log(q+2)).
\]
The function \(\psi(t)\) is positive for finite \(t\).
Thus subtracting one in A12 has exponentially small relative effect,
and A19 follows.

The original equilibrium constants can all be evaluated in a fixed
one-dimensional elliptic family. Let
\[
 u_tK(\kappa_t)=2,\quad
 v_tE(\kappa_t)=2(1+t),\quad
 r_t=u_t/v_t,\quad \kappa_t^2=1-r_t^2.
\]
The Euler constant gives the equivalent formula
\[
 \psi(t)=\log(1+r_t)+t\log\kappa_t-(1+t)\log E(\kappa_t).
 \tag{A20}
\]
The exact profile identities are
\[
 \psi'(t)=\log(\kappa_t/E(\kappa_t))<0,\quad
 f(t)=2\psi(t)-2(1+t)\psi'(t)
     =\log\frac{1+r_t}{1-r_t}>0.
 \tag{A21}
\]
Here \(\psi(0)=\log(4/\pi)\), \(\psi(t)\to0\) as \(t\to\infty\).
These are the same Euler and profile conventions as the earlier EIQ
calculation. They also follow by differentiating A20 and the two
endpoint equations. The endpoint expansion gives the integrable
\(f(t)=-\frac12\log t+O(1)\) at zero.

## 5. Sharp outgoing norm and the subcritical domain

For fixed \(0<b<1\), apply A18 with
\(L_+=\lceil(b+\epsilon)q\rceil\) for its upper bound and
\(L_-=\lfloor(b-\epsilon)q\rfloor\) for its lower bound.
All logarithms of the factors in A15--A17 other than their explicit
powers are \(O_h(q)\).
Thus \(d_+(L_+)\), \(d_1(L_-)\), and \(d_2(L_-)\) tend to zero
exponentially in \(q\ell\). Equation A19 bounds the two logarithmic
norms by \((L_\pm/q)\psi(n/L_\pm-1)+o(1)\).
Letting \(\epsilon\downarrow0\) proves A4.

For a finite uniform error on \(b\) in a fixed compact subinterval of
\((0,1)\), choose
\[
 L_\pm=bq+O_h(q/\ell)
\]
with signs such that \(d_+(L_+)\le e^{-q}\) and
\(d_1(L_-)\le e^{-q}\).
These integers exist by the explicit A15--A16; A17 is still exponentially
small since \(q-L_-\) is a fixed positive fraction of \(q\).
Since
\[
 \frac{\partial}{\partial L}
      [L\psi(n/L-1)]=\tfrac12f(n/L-1),
\]
its derivative is uniformly bounded on this parameter domain.
This proves the error stated after A4. The full source mass is still
present in each monic norm before the ratio in A12.

At \(b>1\), the supplied largest relative metric eigenvalue
\(\exp[2(q-1)\ell+O_h(q)]\) makes
\(\alpha_k(b)\|G_N^{1/2}\Omega_NG_N^{1/2}\|\to0\).
Thus the metric is relatively canonically close, and the original
canonical monic profile proves A4. At \(b=1\), monotonicity of the
fixed-vector norm in \(\alpha\), sandwiched against each fixed \(b'<1\)
and the canonical norm, proves the same limit. No estimate is
differentiated at \(b=1\).

There is an independent elementary proof for every activation sequence
\(a_k=-\log\alpha_k=o(q\ell)\).
Let
\[
 L_k=\left\lceil
 \frac{a_k/2+\tfrac12\log({\bf B}{\bf L}g_+/g_-)}
 {\log(q/K_T)}
 \right\rceil_+ .
\]
For large \(k\), enlarge it to at least one. It is \(o(q)\), lies below
\(n\), and makes \(d_+(L_k,\alpha_k)\le1\).
By A14 and A18,
\[
 \rho_N(\alpha_k)
 \le 1+2\sqrt{c_+/c_-}\,2^{L_k}\sqrt{2n+1}
 =e^{o_h(q)}
 \tag{A22}
\]
uniformly in \(N\).
This uses no EIQ norm asymptotic.

## 6. The actual arithmetic operator, not only its metric

Let \(u_N=[\phi_N]\), \(n=N+1\), and
\(a_n=\sqrt{\omega_n/\omega_{n-1}}\).
Compression of real multiplication in the actual minimum-section space
gives the exact decomposition
\[
 M=C_N+a_nf_nu_N^{*G_N},\qquad
 C_N^{\dagger_{G_N}}=C_N,\quad
 \|C_N\|_{G_N}\le C_hq,\quad \|u_N\|_{G_N}\le1.
 \tag{A23}
\]
It follows directly from the one outgoing coefficient of \(yP\);
the \(S\)-coordinate version has the corresponding factors of \(i\).

The full covariance blend admits the coisometry
\[
 {\cal J}_\alpha(x_0,x_J)=\sqrt{1-\alpha}\,x_0+\sqrt\alpha\,x_J
\]
from \(E_{G_N}\oplus E_{G_N^J}\) to \(E_{G_N(\alpha)}\).
Its adjoint is the actual minimum section. Compressing
\(\operatorname{diag}(M,M)\) gives
\[
 M=B_{\alpha,N}
   +(1-\alpha)a_nf_nu_N^{*G_N(\alpha)},
 \tag{A24}
\]
\[
 B_{\alpha,N}=(1-\alpha)C_NG_N^{-1}G_N(\alpha)
       +\alpha M(G_N^J)^{-1}G_N(\alpha),
\]
\[
 \|B_{\alpha,N}\|_{G_N(\alpha)}
 \le\max\{C_hq,\|M\|_{G_N^J}\}=e^{o_h(q)}.
 \tag{A25}
\]
The first operator need not be selfadjoint, and the remaining rank-one
operator need not be nilpotent.

Its norm has the same logarithmic exponent as A4. To check that no
exponential factor has been lost from \(u_N\), use the original central
sum-grid point \(z_*=\gamma-i\delta\), present for every odd \(k\).
Christoffel--Darboux and the source mass give
\[
 |\phi_N(z_*)|
 \ge\frac{\delta}{a_NM_h(0)^{k/2}}.
\]
The zero-jet weight there is at least \(a_{\min}^k\), and
\(G_N(\alpha)\succeq G_N^J\succeq{\bf L}^{-1}T\). Hence
\[
 \|u_N\|_{G_N(\alpha)}
 \ge {\bf L}^{-1/2}
      \frac{\delta a_{\min}^{k/2}}{a_NM_h(0)^{k/2}}
 =e^{-o_h(q)}.
 \tag{A26}
\]
The original monic comparison bounds \(a_n\) above and below by
polynomial factors times \(e^{o(q)}\).

For fixed \(b>0\), A24 therefore has exactly one exponentially large
singular scale:
\[
 q^{-1}\log s_1(M;G_N(\alpha_k(b)))=\Psi_b(s_N)+o_h(1),
 \quad s_j(M;G_N(\alpha_k(b)))\le e^{o_h(q)}\ (j\ge2).
 \tag{A27}
\]
For subcritical activation A22 instead gives A5. The actual observed
minimum-section compression has norm at most the full norm, so the
subcritical conclusion applies to it too, without imposing invariance
of the observation kernel.

## 7. The complete determinant return by an exact rank-two update

This is the step that evaluates the original large receiver.
Since the same section \(Y_k\) is fixed at all cutoffs,
\[
 G_{N+1}^{-1}-G_N^{-1}=f_nf_n^*.
\]
Let \(z_n=(I-P_{X_N+Y_k})\phi_n\). If \(z_n\ne0\), define
\(g_n=\operatorname{value}(z_n)/\|z_n\|\); otherwise set \(g_n=0\).
The actual joint covariance update is
\[
 (G_{N+1}^J)^{-1}-(G_N^J)^{-1}=g_ng_n^*.
\]
This formula also covers a nonzero orthogonal source vector with zero value.
For the SAME \(\alpha\) at adjacent cutoffs,
\[
 C_{N+1}(\alpha)-C_N(\alpha)
  =(1-\alpha)f_nf_n^*+\alpha g_ng_n^*.
 \tag{A28}
\]

Put \(u=\sqrt{1-\alpha}\,G_N(\alpha)^{1/2}f_n\) and
\(v=\sqrt\alpha\,G_N(\alpha)^{1/2}g_n\). The exact local determinant ratio is
\[
 e^{D_N(\alpha)}
 =(1+\|u\|^2)(1+\|v\|^2)-|u^*v|^2,
 \quad
 D_N(\alpha)=\log\det G_N(\alpha)-\log\det G_{N+1}(\alpha).
 \tag{A29}
\]
Its full complex cross term remains. Positive semidefiniteness and
\(G_N(\alpha)\preceq\alpha^{-1}G_N^J\) prove
\[
 \boxed{
 0\le D_N(\alpha)-\log[1+(1-\alpha)\rho_N(\alpha)^2]
 \le D_N^J.
 }\tag{A30}
\]
Here \(D_N^J=\log\det G_N^J-\log\det G_{N+1}^J\).
In the second inequality the upper remainder is
\(\log(1+\alpha g_n^*G_N(\alpha)g_n)\le
\log(1+g_n^*G_N^Jg_n)\), precisely \(D_N^J\).

Sum A30 with \(w_{q-1}=w_{2q-1}=1\) and all interior weights two.
The total upper remainder is the complete joint four-return,
at most \(2q\log({\bf B}{\bf L})=o_h(q^2)\).
Using A4 now proves A2--A3.
For \(b\) in a compact subset of \((0,1)\), a valid remainder is
\[
 O_h(q^2/\ell+kq\log^2(q+2)).
 \tag{A31}
\]
The same argument for a partial window gives
\[
 \log\frac{\det G_{q-1}(\alpha_k(b))}
              {\det G_{q-1+\lfloor sq\rfloor}(\alpha_k(b))}
 =2q^2\int_0^s\Psi_b(t)\,dt+o_h(q^2).
 \tag{A32}
\]
The determinant-increment measures converge to
\(2\Psi_b(s)\,ds\).
This is a statement about the complete determinant, not the earlier
single-class norm-loss measure.

The coefficient \({\cal C}\) is continuous, strictly increasing and
strictly convex on \(0<b<1\), and constant on \(b\ge1\). Indeed
\[
 {\cal C}'(b)=2\int_0^1
 f((1+s-b)/b)\,ds>0.
\]
The original endpoint identity
\(\int_0^1f(s)\,ds=C_\partial/2\) gives
\[
 {\cal C}'(1^-)=C_\partial,\qquad
 C_B-{\cal C}(b)=C_\partial(1-b)+o(1-b).
 \tag{A33}
\]
Since \(rK/E=1/(1+t)\), \(K\sim\log(4/r)\), \(E\to1\) at \(r\to0\),
\[
 \lim_{b\downarrow0}
 \frac{\log(1/b)}{b^2}{\cal C}(b)=2\log2.
 \tag{A34}
\]
These are asymptotics of the evaluated fixed profile. Substitution of
an arbitrary moving \(b_k\to0\) into A31 is not asserted; A22 supplies the
independent subcritical theorem.

## 8. Return to the actual observation

Let \(I_K\) be the actual fixed kernel inclusion, of rank \(m=8k-16\)
on the original simple five-orbit domain, and put
\[
 Q_N(\alpha)=
 (\Lambda G_N(\alpha)^{-1}\Lambda^*)^{-1}.
\]
The previous common-coefficient bounds give uniform mutual comparisons
of all canonical \(G_N\) by factors \(e^{O_h(q)}\). All joint metrics are
mutually comparable by \({\bf B}{\bf L}=e^{o_h(q)}\).
Taking inverses and the same positive covariance combination proves the
same \(e^{O_h(q)}\) comparison for all \(G_N(\alpha)\), uniformly in
\(0\le\alpha\le1\).

The exact determinant factorization through the fixed kernel gives
\[
 {\cal R}\log\det G_N(\alpha)
 ={\cal R}\log\det(I_K^*G_N(\alpha)I_K)
  +{\cal R}\log\det Q_N(\alpha).
\]
All frame factors cancel under the original four signs. Monotonicity
of A28 and the mutual comparison imply
\[
 0\le{\cal R}\log\det(I_K^*G_N(\alpha)I_K)
 \le O_h(mq)=o_h(q^2).
\]
Therefore
\[
 \boxed{
 {\cal R}\log\det Q_N(\alpha_k(b))
       ={\cal C}(b)q^2+o_h(q^2).
 }\tag{A35}
\]
The original kernel, its period and its matrix \(\mathsf V^{-1}\pi^T\)
are retained. This does not evaluate its own finer \(kq\) coefficient.

## 9. Full heat and spectral-polynomial consequences

For \(\sigma>0\), set \(\tau_k=e^{-2\sigma q}\).
The holomorphic heat trace is \(q+o(1)\), because the original spectrum
has modulus \(O_h(k)\); all repeated-root derivatives remain in the
operator and their strictly triangular contributions have zero trace.
Equation A27 gives
\[
 \frac1q\log\det(I+\tau_kM^{\dagger_{G_N(\alpha_k(b))}}M)
 \longrightarrow2(\Psi_b(s_N)-\sigma)_+.
 \tag{A36}
\]
The convergence includes the threshold, since
\(0\le\log(1+e^u)-u_+\le\log2\).
Away from that threshold,
\[
 \Re\operatorname{Tr}e^{-\tau_kM^2}
 -\operatorname{Tr}e^{-\tau_kM^\dagger M}
 \longrightarrow1_{\{\Psi_b(s_N)>\sigma\}}.
 \tag{A37}
\]
Write \(a_0(b)=\Psi_b(0)\), \(a_1(b)=\Psi_b(1)\).
The same-time four-cutoff heat gap is two for
\(a_1(b)<\sigma<a_0(b)\), and zero on the other open regions.
At threshold equality the logarithmic determinant limit A36, not an
unsupported heat value, is the stated result.

For every \(-\log\alpha_k=o(q\ell)\), A5 implies that both heat traces
tend their common dimension at every \(\sigma>0\), for the full source
and for the ACTUAL observed minimum-section compression.
In particular \(\alpha=e^{-2\theta q}\) works for every fixed
\(\theta,\sigma>0\), with no ordering condition \(\theta<\sigma\).

Retain the attachment's exact positive spectral polynomial:
\[
 \det(aI+M^{\dagger_{G_N(\alpha)}}M)
 =\mathscr P_N(a,\alpha)/\det(I+\alpha\mathsf K_N).
\]
Its exact handoff is
\[
 \log\frac{\mathscr P_N(a,\alpha)}{\mathscr P_N(a,0)}
 -\Delta_N(\alpha)
 =
 \log\det(I+a^{-1}M^{\dagger_{G_N(\alpha)}}M)
 -\log\det(I+a^{-1}M^{\dagger_{G_N}}M).
\]
At \(a=e^{2\sigma q}\), its four-cutoff return divided by \(q\) tends to
\[
 \boxed{
 4\{(a_0(b)-\sigma)_+-(a_1(b)-\sigma)_+
 -(a_0-\sigma)_++(a_1-\sigma)_+\}.
 }\tag{A38}
\]
This evaluates the correlated order-\(q\) spectral expression while
A3 retains the larger order-\(q^2\) metric correction. No separate
order-\(q\) expansion of \(\Delta_N\) is inferred.

The sharp outlier profile A27--A38 concerns the full original action.
A fixed-rank observation can remove that one outlier, so its sharp
fixed-\(b\) singular profile is NOT claimed here. What has been proved
for the actual observation is the determinant return A35 and the
subcritical heat collapse from the full norm estimate.

## 10. Source status and remaining receivers

Imported inputs: the original one-factor coercivity and full jet estimates,
the fixed tensor section and its complete normal-source minimum, the original
Gamma/EIQ conventions and canonical monic profile, and the original fixed
observation maps. Source-version anchor: repository commit
5992ad50c0f2a06921f1fcaded7b4e38097c0739, including MR8--12 for the actual
kernel, and the supplied COMPLETE_PROOFS (4).md for its spectral polynomial.

New deductions: the finite Taylor-matching comparison A18; its uniform
arithmetic exponent A4; the explicit subcritical construction A22; the exact
activated one-outgoing-direction decomposition A24; the rank-two minimum
update A28--A30; the full coefficient curve A2--A3 and its observed version;
and the complete regularizer/activation phase diagram A36--A38.

All source and target coordinates have explicit inverses or their actual
kernels. The original \(Q\) is retained in A17 and the full units in the
tensor value constraint. No actual zeta zero, period, moment table, or
projected-current sign is assigned by an auxiliary test.

The canonical consecutive projected-current phase and independent proper-source
minimum remain distinct receivers. The result evaluates the activated source
minimum and its change back to the canonical metric; it does not remove the
calculated correction from a putative RH closing inequality.
