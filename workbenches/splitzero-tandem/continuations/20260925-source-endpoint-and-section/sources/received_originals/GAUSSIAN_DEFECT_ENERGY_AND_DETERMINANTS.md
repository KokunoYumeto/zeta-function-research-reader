# Gaussian energy and determinant receivers of the actual specialization map

25 September 2026. Complete independent derivation GDE0–GDE13. Inner products are linear in their first variable.

Prior programme result: GTAH5.1–GTAH5.3 in `GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md` already distinguish the ordinary Hilbert trace from the original multiplicity trace and prove the positive defect trace with weight \(e^{-t\gamma^2}\). The present calculation receives that result through the actual holomorphic source multiplier \(e^{ts^2}\). Its additional content is the full reflected source and target energies, nonsymmetric square and Fredholm determinants, exact transfer covariance and degree trace, and convergence on the complete source. The earlier positive Gaussian defect is not being claimed as a new result here.

## GDE0. The original source and the operator being calculated

The support is still \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Coefficients, arithmetic labels, integrals and real parameters here occur only after the complete-history arithmetic reconstruction. No coordinate, numerical value, parity, metric, or retracted addition is assigned to that support. The two branch histories remain separate.

Retain the actual full-jet source \(Q=\mathcal B/\mathcal I\), where \(\mathcal B\) consists of entire functions rapidly decreasing on every closed vertical strip and \(\mathcal I\) imposes the complete original nontrivial-zeta zero jets. Write \(\mathscr Z\) for the distinct actual zeros, \(m_\rho\) for their original multiplicities, \(\rho=\sigma+i\gamma\), and \(\rho^\#=1-\overline\rho\). The original functional equation gives
\[
0<\sigma<1,\qquad m_{\rho^\#}=m_\rho,
\qquad m_{\overline\rho}=m_\rho.
\tag{GDE0.1}
\]
Explicitly, the source seminorms are \(q_{a,b,N}(F)=\sup_{a\le\Re s\le b}(1+|\Im s|)^N|F(s)|\), for real finite \(a\le b\) and integers \(N\ge0\); \(Q\) has the quotient topology. The closed subspace \(\mathcal I\) consists of all \(F\in\mathcal B\) satisfying \(F^{(j)}(\rho)=0\) for every \(\rho\in\mathscr Z\) and \(0\le j<m_\rho\). Define \(\mathscr Z_L=\{\rho\in\mathscr Z:\Re\rho=1/2\}\), \(\mathscr Z_O=\mathscr Z\setminus\mathscr Z_L\), and \(N_O=\{[F]\in Q:F(\rho)=0\text{ for every }\rho\in\mathscr Z_O\}\). These value conditions are well-defined on the full-jet quotient; they do not impose vanishing of the higher jets in that quotient.
Use precisely the Hilbert space, evaluation and reflection from GAP/ADM:
\[
H=\ell^2(\mathscr Z,m),\quad
\langle x,y\rangle=\sum_\rho m_\rho x_\rho\overline{y_\rho},
\quad (\mathsf Jx)_\rho=x_{\rho^\#},\quad (EF)_\rho=F(\rho).
\tag{GDE0.2}
\]
The evaluation is continuous into the full common domain
\[
H_\infty=\{x:p_N(x)^2=\sum_\rho m_\rho(1+|\gamma|)^{2N}|x_\rho|^2<\infty
\quad\forall N\ge0\}.
\tag{GDE0.3}
\]
Write \(H_L\) and \(H_O\) for the closed coordinate subspaces supported on \(\mathscr Z_L\) and \(\mathscr Z_O\), and \(P_O\) for the orthogonal projection onto \(H_O\). Also write \(H_{\infty,O}=H_\infty\cap H_O\), with its induced seminorms.
For \(r>1\), retain all phases and scalars:
\[
\ell_r=\log r,\quad \Delta_r(\sigma)=r^\sigma-r^{1-\sigma},
\quad d_r(\rho)=e^{-i\gamma\ell_r}\Delta_r(\sigma),
\quad D_rx=(d_r(\rho)x_\rho)_\rho,
\]
\[
g_t(s)=e^{ts^2},\quad (G_tx)_\rho=e^{t\rho^2}x_\rho,
\quad t>0,
\qquad \beta_r=D_r^*\mathsf JE.
\tag{GDE0.4}
\]
Thus the actual regularized specialization is
\[
\boxed{B_{r,t}=D_r^*\mathsf JG_t:H\to H,
\qquad B_{r,t}E=\beta_r m_{g_t}.}
\tag{GDE0.5}
\]
Its output at \(\rho\) is exactly
\(\overline{d_r(\rho)}e^{t(\rho^\#)^2}x_{\rho^\#}\).
This is GAP4/ADM9's reflected source multiplier, not an absolute-value replacement. A sign \(-\beta_r\) in the literal specialization cone gives \(-B_{r,t}\); its positive energy below is unchanged, and the odd trace below remains zero. The full source extension in that cone is not identified with this Hilbert operator.

## GDE1. Domain and trace ideals, including the actual multiplicity operator

The exact elementary bounds are
\[
|\Delta_r(\sigma)|\le r-1,\qquad
|g_t(\rho)|=e^{t(\sigma^2-\gamma^2)}\le e^t e^{-t\gamma^2}.
\tag{GDE1.1}
\]
The original zero count with multiplicities satisfies
\(N(R)=\sum_{|\gamma|\le R}m_\rho=O((1+R)\log(2+R))\).
It follows by division into integer height intervals that for every \(a>0\) and every finite \(k\ge0\),
\[
\sum_\rho m_\rho(1+|\gamma|)^k e^{-a\gamma^2}<\infty.
\tag{GDE1.2}
\]
All count estimates concern the complete original divisor, not a computed zero sample. They also imply the pointwise bound
\(m_\rho\le C(1+|\gamma|)\log(2+|\gamma|)\), by taking the full count at a height containing that point.

Let \(e_\rho\) be the coordinate vector with value one at \(\rho\). Its squared norm is \(m_\rho\), so
\[
u_\rho=m_\rho^{-1/2}e_\rho
\tag{GDE1.3}
\]
is an orthonormal basis. A diagonal operator with coefficient \(a_\rho\) has ordinary Hilbert trace \(\sum_\rho a_\rho\), not \(\sum_\rho m_\rho a_\rho\). The weighted inner product does not insert a multiplicity into this ordinary trace.

The separate multiplicity operator is the positive self-adjoint diagonal operator
\[
(\mathsf Mx)_\rho=m_\rho x_\rho,
\qquad \operatorname{Dom}\mathsf M
=\{x:\sum_\rho m_\rho^3|x_\rho|^2<\infty\}.
\tag{GDE1.4}
\]
All its powers are defined by the corresponding weighted square sums. Because its coefficients have polynomial growth and because of the Gaussian bound, \(G_t\) maps \(H\) into every \(\operatorname{Dom}\mathsf M^k\) and into \(H_\infty\). Products \(\mathsf M^kG_t\) extend to bounded operators with coefficients \(m_\rho^ke^{t\rho^2}\). They are trace class: their singular-value sums \(\sum m_\rho^k|g_t(\rho)|\) converge by (GDE1.2) and the polynomial bound on \(m_\rho\). This argument includes all products below, also after multiplication by any fixed polynomial in \(\gamma\).

Reflection commutes with \(\mathsf M\) on its exact domain because \(m_{\rho^\#}=m_\rho\); every diagonal operator here also commutes with it on its domain. In particular \(B_{r,t}\), \(\mathsf M B_{r,t}\), and every stated multiplicity-weighted quadratic product have trace-class bounded extensions. Whenever defined here, write
\[
\operatorname{Tr}_{\zeta}(K)=\operatorname{Tr}_H(\mathsf M K).
\tag{GDE1.5}
\]
This is the original divisor-weighted observation. It is not called the ordinary Hilbert trace and is not presumed cyclic for arbitrary operators that fail to commute with \(\mathsf M\).

## GDE2. The complete positive energy and its source pairing

The full reflection relations are
\[
d_r(\rho^\#)=-d_r(\rho),\quad
\mathsf JD_r\mathsf J=-D_r,\quad
\mathsf JD_r^*\mathsf J=-D_r^*,
\quad P_r=D_r^*D_r=D_rD_r^*,\quad \mathsf JP_r\mathsf J=P_r.
\tag{GDE2.1}
\]
The coefficient of \(P_r\) is \(\Delta_r(\sigma)^2\). Taking the Hilbert adjoint of the actual ordered product gives
\[
B_{r,t}^*=G_t^*\mathsf JD_r,
\]
\[
\boxed{A_{r,t}=B_{r,t}^*B_{r,t}=G_t^*P_rG_t,
\qquad a_{r,t}(\rho)=\Delta_r(\sigma)^2e^{2t(\sigma^2-\gamma^2)}.}
\tag{GDE2.2}
\]
The Gaussian phase and the phase of \(d_r\) cancel because this is the specifically defined positive product; those phases remain in \(B_{r,t}\). The other ordered product is
\[
B_{r,t}B_{r,t}^*=\mathsf JA_{r,t}\mathsf J,
\qquad a_{r,t}(\rho^\#)
=\Delta_r(\sigma)^2e^{2t((1-\sigma)^2-\gamma^2)}.
\tag{GDE2.3}
\]
Both are positive trace class. Their source pairing is exactly
\[
\begin{aligned}
\mathcal E_{r,t}(F,G)
&=\langle\beta_rm_{g_t}F,\beta_rm_{g_t}G\rangle\\
&=\langle A_{r,t}EF,EG\rangle\\
&=\sum_\rho m_\rho\Delta_r(\sigma)^2
e^{2t(\sigma^2-\gamma^2)}F(\rho)\overline{G(\rho)}.
\end{aligned}
\tag{GDE2.4}
\]
To check the original reflection, the norm before reindexing is the sum with coefficient
\(m_\rho|d_r(\rho)|^2|g_t(\rho^\#)|^2\) and values at \(\rho^\#\). Reindexing by the actual multiplicity-preserving bijection gives precisely (GDE2.4). No support coordinate is changed or omitted.

Continuity on the entire original \(Q\) follows from the continuous evaluation into \(H\). Positivity and the nonzero Gaussian give
\[
\ker B_{r,t}=\ker B_{r,t}^*=\ker A_{r,t}=H_L,
\quad\overline{\operatorname{Ran}B_{r,t}}
=\overline{\operatorname{Ran}A_{r,t}}=H_O,
\]
\[
\operatorname{rad}\mathcal E_{r,t}=N_O=\ker\beta_r.
\tag{GDE2.5}
\]
The range closures follow either from the orthogonal-kernel identity or by solving each finite off-line coordinate separately. The original isolators show that the regularized source image contains every finite off-line value vector, hence is dense in \(H_O\) and in \(H_{\infty,O}\). None of these statements asserts surjectivity of that image or equality of its transported source topology with a Hilbert topology.

## GDE3. Both traces and the exact reflected-pair contributions

The two trace observations are
\[
\boxed{\operatorname{Tr}_H A_{r,t}
=\sum_{\rho\in\mathscr Z}a_{r,t}(\rho),\qquad
\operatorname{Tr}_{\zeta}A_{r,t}
=\sum_{\rho\in\mathscr Z}m_\rho a_{r,t}(\rho).}
\tag{GDE3.1}
\]
The ordinary trace is \(\|B_{r,t}\|_{\mathrm{HS}(H)}^2\). The divisor trace is
\[
\operatorname{Tr}_{\zeta}A_{r,t}
=\|\mathsf M^{1/2}B_{r,t}\|_{\mathrm{HS}(H)}^2.
\tag{GDE3.2}
\]
This follows since \(\mathsf M\) commutes with \(B_{r,t}\), with the domain and bounded extensions already proved in GDE1. It does not follow merely from the original norm weighting.

For each off-line reflection orbit choose either representative \(\rho=\sigma+i\gamma\); the following expression is independent of that choice. Its divisor contribution is
\[
\boxed{m_\rho\Delta_r(\sigma)^2e^{-2t\gamma^2}
\left(e^{2t\sigma^2}+e^{2t(1-\sigma)^2}\right).}
\tag{GDE3.3}
\]
Every factor is strictly positive on that actual orbit. The ordinary contribution is the same formula without \(m_\rho\). At line zeros the contribution is exactly zero. Thus, for each fixed \(r>1,t>0\), the following equalities have exactly the same truth value:
\[
\operatorname{Tr}_H A_{r,t}=0,\quad
\operatorname{Tr}_{\zeta}A_{r,t}=0,\quad
\beta_r=0,\quad H_O=0.
\tag{GDE3.4}
\]
Here \(\beta_r=0\Rightarrow H_O=0\) uses the actual full-source isolators. The calculation does not assert these equalities hold; it identifies the exact noncancelling contribution of every possible original off-line orbit.

For \(0<t\le1\), (GDE1.2) and the full count yield a finite constant \(C_r\) such that
\[
\operatorname{Tr}_{\zeta}A_{r,t}
\le C_r(1+t^{-1/2})\log(2+t^{-1}).
\tag{GDE3.5}
\]
For a direct estimate, bound the coefficients by \((r-1)^2e^2e^{-2t\gamma^2}\), express the Gaussian count as
\(\int_0^\infty4tu e^{-2tu^2}N(u)du\), and use the stated bound on \(N\). Substitution \(u=v/\sqrt t\) gives a constant times \((1+t^{-1/2})\log(2+t^{-1})\), because all resulting Gaussian moments and their logarithmic weights are integrable. This is an upper bound only; no lower bound for off-line displacements is assumed.

## GDE4. Fredholm determinants with each multiplicity correctly typed

The ordinary positive Fredholm determinant is
\[
\mathcal D_H(z;r,t)=\det_H(I+zA_{r,t})
=\prod_{\rho\in\mathscr Z}(1+za_{r,t}(\rho)).
\tag{GDE4.1}
\]
The divisor determinant is the different entire product
\[
\boxed{\mathcal D_\zeta(z;r,t)
=\prod_{\rho\in\mathscr Z}(1+za_{r,t}(\rho))^{m_\rho}.}
\tag{GDE4.2}
\]
Both products converge locally uniformly in \(z\): on compact \(z\)-sets the sums of the absolute factor increments, counted with the displayed repetitions, are finite by GDE3. The standard expansion by finite products consequently converges to the stated entire Fredholm functions. For real \(z\ge0\), every factor is positive and
\[
\log\mathcal D_H=\sum_\rho\log(1+za_\rho),\qquad
\log\mathcal D_\zeta=\sum_\rho m_\rho\log(1+za_\rho).
\tag{GDE4.3}
\]
Their logarithmic derivatives are respectively
\[
\sum_\rho\frac{a_\rho}{1+za_\rho},\qquad
\sum_\rho\frac{m_\rho a_\rho}{1+za_\rho}.
\tag{GDE4.4}
\]
Domination by the trace sums proves differentiation for \(z\ge0\), and on any compact complex set avoiding the determinant zeros. In particular the derivatives of both determinants at zero are the two traces in (GDE3.1). For \(|z|\|A\|<1\), the branches of \(\log\mathcal D_H\) and \(\log\mathcal D_\zeta\) that are zero at \(z=0\) respectively equal the absolutely convergent expansions
\(\sum_{k\ge1}(-1)^{k+1}z^k\operatorname{Tr}_H(A^k)/k\) and
\(\sum_{k\ge1}(-1)^{k+1}z^k\operatorname{Tr}_{\zeta}(A^k)/k\).

For a literal ordinary Fredholm realization of (GDE4.2), define the counted carrier
\[
\widehat H=\bigoplus_{\rho\in\mathscr Z}\mathbb C^{m_\rho},
\quad (\widehat A v)_{\rho,j}=a_\rho v_{\rho,j},\quad 1\le j\le m_\rho.
\tag{GDE4.5}
\]
It is trace class with \(\operatorname{Tr}_{\widehat H}\widehat A=\sum m_\rho a_\rho\), and its ordinary determinant is exactly (GDE4.2). The actual comparison with \(H\) is the isometric embedding
\[
V:H\to\widehat H,\quad (Vx)_{\rho,j}=x_\rho,
\qquad \widehat A V=VA.
\tag{GDE4.6}
\]
Reflection on \(\widehat H\) keeps \(j\) and sends \(\rho\) to \(\rho^\#\); multiplicities agree. The scalar lifts of \(D,G,B\) obey the same identity and yield \(\widehat A=\widehat B^*\widehat B\). The image of \(V\) is the one-dimensional constant-vector line in each multiplicity block. Its orthogonal complement has \(m_\rho-1\) additional scalar copies. Thus
\[
\operatorname{Tr}_{\widehat H}\widehat A
=\operatorname{Tr}_H A+\sum_\rho(m_\rho-1)a_\rho.
\tag{GDE4.7}
\]
This is a counted value carrier, not a claim that the full nilpotent jet action is scalar. The original source jet still maps through its constant value and has all higher jets in the kernel of \(\beta_r\). The copied carrier records the original divisor multiplicity separately from that source rank.

In particular one must not confuse (GDE4.2) with
\[
\det_H(I+z\mathsf M A)=\prod_\rho(1+zm_\rho a_\rho).
\tag{GDE4.8}
\]
Their first derivatives agree, but their higher coefficients and logarithmic derivatives generally differ. All three displayed objects have specified domains and meanings.

For every \(z>0\), either positive determinant equals one exactly when its positive energy trace is zero. The resolvent observation
\[
R_{r,t}(z)=A_{r,t}(I+zA_{r,t})^{-1},\qquad
R_{r,t}(z)_\rho=\frac{a_\rho}{1+za_\rho}
\tag{GDE4.9}
\]
is trace class and gives (GDE4.4). The full off-line projection is recovered by
\[
\operatorname*{s-lim}_{z\to+\infty}zR_{r,t}(z)=P_O.
\tag{GDE4.10}
\]
This follows coordinatewise with bound one and dominated convergence against the squared coordinates of each vector. It does not require a spectral gap and is not a trace-norm limit when the off-line projection has infinite rank.

## GDE5. What cyclicity actually cancels

For the basis (GDE1.3), \(B_{r,t}\) sends each coordinate to its reflected coordinate. It has no diagonal entry at an off-line point. At a line point its diagonal entry is zero because \(d_r=0\). Therefore
\[
\boxed{\operatorname{Tr}_H B_{r,t}=0,
\qquad\operatorname{Tr}_{\zeta}B_{r,t}=0.}
\tag{GDE5.1}
\]
These are legitimate absolutely convergent traces by GDE1. They do not calculate the squared norm in GDE3.

Both ordered positive products have equal ordinary trace by Hilbert–Schmidt cyclicity. The multiplicity-weighted assertion has a valid domain proof too: put \(X=\mathsf M^{1/2}B\). It is Hilbert–Schmidt, and the commuting-domain calculation gives
\(X^*X=\mathsf M B^*B\), \(XX^*=\mathsf M BB^*\). Hence
\[
\operatorname{Tr}_{\zeta}(B^*B)=\operatorname{Tr}_{\zeta}(BB^*),
\quad\operatorname{Tr}_{\zeta}(B^*B-BB^*)=0.
\tag{GDE5.2}
\]
No unbounded operator was moved through a trace without this reduction.

The commutator's exact coefficient is
\[
a_\rho-a_{\rho^\#}
=\Delta_r(\sigma)^2e^{-2t\gamma^2}
\left(e^{2t\sigma^2}-e^{2t(1-\sigma)^2}\right).
\tag{GDE5.3}
\]
This is antisymmetric under \(\rho\mapsto\rho^\#\). The cancellation in (GDE5.2) removes precisely this antisymmetric term. The symmetric energy is
\[
\tfrac12(A+\mathsf JA\mathsf J),
\qquad\text{coefficient }\tfrac12(a_\rho+a_{\rho^\#}),
\tag{GDE5.4}
\]
whose trace is the unchanged positive trace of \(A\). Formula (GDE3.3) shows explicitly what remains after the cyclic cancellation.

For the original indefinite reflection pairing the ordered product is instead
\[
B^*\mathsf JB=-G_t^*P_r\mathsf JG_t.
\tag{GDE5.5}
\]
It is again off-diagonal on every actual off-line pair, and has ordinary and divisor trace zero. Its source form is
\[
\langle BEF,\mathsf JBEG\rangle
=-\sum_\rho m_\rho\Delta_r(\sigma)^2
g_t(\rho)\overline{g_t(\rho^\#)}
F(\rho)\overline{G(\rho^\#)}.
\tag{GDE5.6}
\]
This exact operator and pairing relate the positive energy to the original reflection; their different trace is not an identification of the two forms.

## GDE6. The full nonsymmetric determinant and its surviving quadratic term

Put
\[
c_{r,t}(\rho)=\overline{d_r(\rho)}^{2}g_t(\rho)g_t(\rho^\#)
=\Delta_r(\sigma)^2
e^{t\{\sigma^2+(1-\sigma)^2-2\gamma^2\}}
e^{2i\gamma(\ell_r+t)}.
\tag{GDE6.1}
\]
This satisfies \(c(\rho^\#)=c(\rho)\) and \(c(\overline\rho)=\overline{c(\rho)}\). Direct multiplication gives
\[
B_{r,t}^{2}=-M_{c_{r,t}}.
\tag{GDE6.2}
\]
On each reflected off-line pair the exact block, in the orthonormal basis, is
\[
\begin{pmatrix}
0&\overline{d_r(\rho)}g_t(\rho^\#)\\
-\overline{d_r(\rho)}g_t(\rho)&0
\end{pmatrix},
\quad
\det(I+zB|_{\{\rho,\rho^\#\}})=1+z^2c_{r,t}(\rho).
\tag{GDE6.3}
\]
Thus the ordinary and counted determinants of the actual \(B\) are the convergent products
\[
\det_H(I+zB)=\prod_{\{\rho,\rho^\#\}\subset\mathscr Z_O}
(1+z^2c_{r,t}(\rho)),
\]
\[
\det_{\zeta}(I+zB)=\prod_{\{\rho,\rho^\#\}\subset\mathscr Z_O}
(1+z^2c_{r,t}(\rho))^{m_\rho}.
\tag{GDE6.4}
\]
Each orbit is used once. Their convergence follows from the Gaussian coefficient bound and (GDE1.2); it is also the ordinary trace-class determinant calculation on \(H\) and \(\widehat H\). All odd power traces vanish, while
\[
\operatorname{Tr}_{\zeta}(B^{2k})
=(-1)^k\sum_\rho m_\rho c_{r,t}(\rho)^k
\tag{GDE6.5}
\]
and the ordinary formula omits the multiplicity. Conjugate symmetry makes these even-power traces real, but not necessarily nonnegative; their full phases remain in (GDE6.1).

The precise relation to the positive determinant on the same orbit is
\[
|c_{r,t}(\rho)|^2=a_\rho a_{\rho^\#},
\qquad
(1+za_\rho)(1+za_{\rho^\#})
=1+z(a_\rho+a_{\rho^\#})+z^2|c_{r,t}(\rho)|^2.
\tag{GDE6.6}
\]
Thus the zero first derivative of the determinant of \(I+zB\) is the proved off-diagonal trace cancellation. Its quadratic term and the strictly positive linear energy coefficient in (GDE6.6) survive. No square-root branch for the two block eigenvalues is required.

## GDE7. The exact geometric degree calculation

Retain on \(H\) the actual original diagonal operators
\[
(T_nx)_\rho=n^\rho x_\rho,\quad
(U_nx)_\rho=n^{1-\rho}x_\rho,
\quad T_nU_n=U_nT_n=nI.
\tag{GDE7.1}
\]
They are bounded and invertible for each fixed recovered integer \(n\). Their reflected adjoint relation gives exactly
\[
B_{r,t}T_n=U_n^*B_{r,t},\qquad
B_{r,t}U_n=T_n^*B_{r,t}.
\tag{GDE7.2}
\]
These follow by moving the diagonal factor through \(G_t,D_r\) and using \(\mathsf JT_n=U_n^*\mathsf J\); the second is identical with \(T,U\) interchanged. They are the actual specialization covariance, not an assertion that its positive energy has a transfer adjoint.

In particular the energy covariance and its cyclic trace are exactly
\[
T_n^*A_{r,t}T_n=B_{r,t}^*U_nU_n^*B_{r,t},
\]
\[
\boxed{\operatorname{Tr}_\zeta(T_n^*A_{r,t}T_n)
=\operatorname{Tr}_\zeta(U_n^*B_{r,t}B_{r,t}^*U_n)
=\operatorname{Tr}_\zeta(U_nB_{r,t}B_{r,t}^*U_n^*).}
\tag{GDE7.2a}
\]
For the domain justification, \(X=\mathsf M^{1/2}B_{r,t}\) is Hilbert–Schmidt by GDE1 and GDE3, \(U_n\) is bounded, and \(U_n\) commutes with \(\mathsf M\) on its full domain. Apply \(\operatorname{Tr}(Y^*Y)=\operatorname{Tr}(YY^*)\) to \(Y=U_n^*X\). The final equality holds because \(U_n\), \(U_n^*\), and \(B_{r,t}B_{r,t}^*\) are diagonal. This argument also proves the ordinary trace identity without \(\mathsf M\).

The source trace in (GDE7.2a) has coefficient \(n^{2\sigma}a_\rho\). The target trace has coefficient \(n^{2(1-\sigma)}a_{\rho^\#}\), including the full reflected Gaussian
\(a_{\rho^\#}=\Delta_r(\sigma)^2e^{2t((1-\sigma)^2-\gamma^2)}\).
Reindexing by \(\rho\mapsto\rho^\#\), with \(m_{\rho^\#}=m_\rho\), proves their equality directly. Replacing \(B_{r,t}B_{r,t}^*\) in this identity by \(A_{r,t}\) changes the receiver and is not an allowed use of cyclicity.

The original defect itself retains both cross terms from the degree relation:
\[
\boxed{P_r=(T_r-U_r^*)(T_r^*-U_r)
=T_rT_r^*+U_r^*U_r-2rI.}
\tag{GDE7.3}
\]
For coefficient parameters \(r\) this is the same diagonal identity; when \(r\) is an integer its \(r\) is the actual degree. Gaussian multiplication makes every term trace class, and consequently
\[
\operatorname{Tr}_{\zeta}A_{r,t}
=\operatorname{Tr}_{\zeta}(G_t^*T_rT_r^*G_t)
+\operatorname{Tr}_{\zeta}(G_t^*U_r^*U_rG_t)
-2r\operatorname{Tr}_{\zeta}(G_t^*G_t).
\tag{GDE7.4}
\]
The complete coefficient is \(r^{2\sigma}+r^{2(1-\sigma)}-2r\), which is exactly \(\Delta_r(\sigma)^2\). The geometric product identity has therefore already been applied, and leaves precisely the energy being measured.

The positive source energy's transfer discrepancy is calculated directly:
\[
\begin{aligned}
&\mathcal E_{r,t}(T_nF,G)-\mathcal E_{r,t}(F,U_nG)\\
&\quad=\sum_\rho m_\rho a_\rho
\bigl(n^\rho-n^{1-\overline\rho}\bigr)
F(\rho)\overline{G(\rho)},
\end{aligned}
\tag{GDE7.5}
\]
and its quadratic degree discrepancy has coefficient \(a_\rho(n^{2\sigma}-n)\). Its trace is a fully convergent trace-class calculation. On a reflected orbit take \(\delta=\sigma-1/2>0\) as representative. The divisor contribution is exactly
\[
\boxed{2m_\rho n\Delta_r(\sigma)^2
e^{-2t\gamma^2+t/2+2t\delta^2}
\left[\cosh\bigl(2\delta(t+\log n)\bigr)
-\cosh(2t\delta)\right].}
\tag{GDE7.6}
\]
To verify it without deleting either member, start with
\(m_\rho\Delta_r(\sigma)^2e^{-2t\gamma^2}
[e^{2t(1/2+\delta)^2}(n^{1+2\delta}-n)
+e^{2t(1/2-\delta)^2}(n^{1-2\delta}-n)]\)
and expand both exponentials. The two retained terms are respectively
\(m_\rho n\Delta_r^2e^{-2t\gamma^2+t/2+2t\delta^2}
e^{2t\delta}(e^{2\delta\log n}-1)\) and its negative-exponent counterpart. Their exact sum is (GDE7.6).

For \(n>1\) and this actual off-line orbit the bracket is strictly positive. Thus the degree-adjusted positive trace is not forced to cancel by the geometric transfer; its remaining terms have been calculated explicitly. Its zero value is again equivalent to absence of the whole actual off-line sector. The ordinary trace has the same expression without \(m_\rho\).

## GDE8. Functional equation and all different Gaussian weights

The original functional equation is
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{GDE8.1}
\]
Together with original conjugation it proves the multiplicity-preserving reflection used throughout. Applied to the trace it gives exactly the pair sum (GDE3.3), not a negative sign for one member. The four relevant weights remain distinct and have proved places:
\[
\begin{array}{c|c}
\text{actual specialization output at }\rho&g_t(\rho^\#)\\
\text{positive source energy at }\rho&|g_t(\rho)|^2=e^{2t(\sigma^2-\gamma^2)}\\
\text{square }B^2&g_t(\rho)g_t(\rho^\#)\\
\text{original reflected Weil pairing}&
g_t(\rho)\overline{g_t(\rho^\#)}
=e^{t\{\rho^2+(1-\rho)^2\}}.
\end{array}
\tag{GDE8.2}
\]
For example \(|g_t(\rho^\#)|^2=e^{2t(1-2\sigma)}|g_t(\rho)|^2\). This exact nonconstant factor is why simply replacing a reflected Gaussian by the unreflected positive weight would change a trace. GDE2 and GDE5 prove the actual maps between these observations.

The complete original source multiplier still is
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=1/8,\quad F_0(-1)=F_0(2)=\pi/24,
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2k!}\zeta'(-2k).
\tag{GDE8.3}
\]
GAP8 retains the full local unit and every derivative. In this regularization the exact derivative is
\[
(g_tF_0)^{(j)}(s)=
\sum_{v+k_0+k_1+k_2+k_3=j}
\frac{j!}{v!k_0!k_1!k_2!k_3!}g_t^{(v)}(s)
\left(\frac{s(s-1)}8\right)^{(k_0)}
\left(-\frac{\log\pi}{2}\right)^{k_1}\pi^{-s/2}
2^{-k_2}\Gamma^{(k_2)}(s/2)\zeta^{(k_3)}(s).
\tag{GDE8.4}
\]
At exceptional points one evaluates the full holomorphic continuation. Thus the original endpoints become \(1/8,e^t/8\), and each original trivial-zero comparison value is multiplied by \(e^{4tk^2}\). The four separate source endpoint coordinates have factors \((1,e^t,e^t,1)\), exactly as GAP7. These are separate labelled source summands; they are not additional nontrivial-zero coordinates in the Hilbert trace. No convergence of an unrestricted infinite sum over these growing trivial-point values is asserted.

The trace \(\operatorname{Tr}_{\zeta}A\) contains \(\sigma\) and \(\overline\rho\) through its positive norm. It is therefore not inserted as a holomorphic test into the original prime explicit formula. The actual holomorphic/reflected trace bridge requires its own proved map; (GDE5.6), (GDE7.4) and (GDE8.2) provide exact receiving expressions for that calculation. The original zeta unit, pole, Gamma factors and prime-power terms have not been declared zero by this energy construction.

## GDE9. Zero-time limit on the entire original source

Let \(B_{r,0}=D_r^*\mathsf J\) and \(A_{r,0}=P_r\), bounded operators on \(H\). The Gaussian factors converge coordinatewise to one and are uniformly bounded for \(0<t\le1\), so
\[
B_{r,t}\xrightarrow{s}B_{r,0},\qquad
A_{r,t}\xrightarrow{s}P_r\quad\text{on }H.
\tag{GDE9.1}
\]
These limits are stronger on the actual common smooth domain. The exact source estimate in GAP1 and \(0<\sigma<1\) give
\[
p_N((G_t-I)x)\le te\,p_{N+2}(x),
\quad
p_N((B_{r,t}-B_{r,0})x)\le(r-1)te\,p_{N+2}(x).
\tag{GDE9.2}
\]
For the positive operator use
\(|e^{2t(\sigma^2-\gamma^2)}-1|
\le2te^2(1+\gamma^2)\), to obtain
\[
p_N((A_{r,t}-P_r)x)
\le2te^2(r-1)^2p_{N+2}(x).
\tag{GDE9.3}
\]
Since \(E:Q\to H_\infty\) is continuous, these estimates prove convergence uniformly on every bounded subset of the complete original \(Q\), and on its invariant source kernels and quotients as in GAP. The source pairing consequently tends to
\[
\mathcal E_{r,0}(F,G)=\sum_\rho m_\rho\Delta_r(\sigma)^2
F(\rho)\overline{G(\rho)}=\langle\beta_rF,\beta_rG\rangle,
\tag{GDE9.4}
\]
uniformly on bounded pairs of source sets. It has the same exact radical \(N_O\). Thus the Gaussian approximation does not make a nonzero specialization value disappear.

The first derivative on this full domain is also specified:
\[
\left.\frac d{dt}\right|_{0+}A_{r,t}
=M_{2\Delta_r(\sigma)^2(\sigma^2-\gamma^2)}
\quad\text{as }H_\infty\to H_\infty,
\tag{GDE9.5}
\]
with bounded-set convergence. The second integral remainder of the real exponential is bounded by a constant times \(t^2(1+|\gamma|)^4\), proving the assertion in each \(p_N\). The full source Gaussian still has GAP2's complete triangular jet matrix; only the value observation passes to (GDE9.5).

Operator-norm convergence in (GDE9.1) is more restrictive:
\[
A_{r,t}\to P_r\text{ in norm}
\quad\Longleftrightarrow\quad P_r\text{ is compact}
\quad\Longleftrightarrow\quad
\Delta_r(\sigma)^2\to0\text{ along }|\gamma|\to\infty.
\tag{GDE9.6}
\]
Necessity follows since every \(A_{r,t}\) is compact and a norm limit of compact operators is compact. For a diagonal operator compactness is exactly uniform smallness of its coefficients outside finite sets: finite-coordinate projections prove sufficiency, and an infinite sequence of orthonormal coordinates proves necessity. Under that condition, split the diagonal difference into finitely many coordinates and a uniformly small tail, using the uniform Gaussian bound, to obtain norm convergence. The same argument proves the corresponding statement for \(B_{r,t}\to B_{r,0}\). No such asymptotic condition is assumed.

## GDE10. Trace and determinant limits at zero time

Strong source convergence alone does not exchange an infinite trace with a limit. Here the exact coefficients supply the complete answer. Retain the comparison
\[
e^{-2t}a_{r,t}(\rho)
=\Delta_r(\sigma)^2e^{-2t(1-\sigma^2+\gamma^2)}.
\tag{GDE10.1}
\]
Since \(1-\sigma^2+\gamma^2>0\), these nonnegative coefficients increase to \(\Delta_r(\sigma)^2\) as \(t\downarrow0\). Monotone convergence, with both original trace conventions, gives
\[
\lim_{t\downarrow0}\operatorname{Tr}_H A_{r,t}
=\sum_\rho\Delta_r(\sigma)^2\in[0,\infty],
\]
\[
\lim_{t\downarrow0}\operatorname{Tr}_{\zeta}A_{r,t}
=\sum_\rho m_\rho\Delta_r(\sigma)^2\in[0,\infty].
\tag{GDE10.2}
\]
The factor \(e^{2t}\) tends to one and is retained in obtaining these limits. Finite sums on the right are exactly the respective trace-class conditions on \(P_r\) and \(\mathsf M P_r\). In those cases dominated convergence gives trace-norm convergence of the corresponding positive diagonal operators. Otherwise the respective traces tend to \(+\infty\). No finite sum, zero sum, or divergent case is presumed.

For fixed \(z>0\), the two positive determinants have the corresponding limits
\[
\lim_{t\downarrow0}\mathcal D_H(z;r,t)
=\prod_\rho(1+z\Delta_r(\sigma)^2),
\]
\[
\lim_{t\downarrow0}\mathcal D_\zeta(z;r,t)
=\prod_\rho(1+z\Delta_r(\sigma)^2)^{m_\rho},
\tag{GDE10.3}
\]
where either product is allowed to be \(+\infty\). If the respective trace sum is finite, dominate the logarithms by \(ze^2\Delta_r^2\) and pass to the limit. If it is infinite, \(\Delta_r^2\le(r-1)^2\) gives
\(\log(1+z\Delta_r^2)\ge z\Delta_r^2/(1+z(r-1)^2)\), so the limiting logarithmic series diverges. Every finite partial logarithmic sum is a lower bound on the complete one and converges termwise, forcing the full limit to infinity. This is an exact infinite-product argument, not a finite-height test.

## GDE11. Parameter comparison and an infinitesimal nonnormality calculation

For \(r,q>1\) put
\[
\kappa_{r,q}(\sigma)=
\frac{r^\sigma-r^{1-\sigma}}{q^\sigma-q^{1-\sigma}},\quad\sigma\ne1/2,
\qquad
\kappa_{r,q}(1/2)=\frac{\sqrt r\log r}{\sqrt q\log q}.
\tag{GDE11.1}
\]
It is a positive continuous function on \([0,1]\), invariant under \(\sigma\mapsto1-\sigma\). The removable value follows by differentiating the numerator and denominator. The derivative bounds
\(2\sqrt r\log r\le\Delta_r'(\sigma)\le(r+1)\log r\) give
\[
\frac{2\sqrt r\log r}{(q+1)\log q}
\le\kappa_{r,q}(\sigma)
\le\frac{(r+1)\log r}{2\sqrt q\log q}.
\tag{GDE11.2}
\]
The exact maps are
\[
B_{r,t}=M_{e^{i\gamma(\log r-\log q)}\kappa_{r,q}}B_{q,t},
\qquad A_{r,t}=M_{\kappa_{r,q}^2}A_{q,t}.
\tag{GDE11.3}
\]
Both comparison multipliers and inverses are bounded on \(H\) and on every common-domain norm. Thus the same original specialization kernel is retained, with explicit two-sided energy and trace bounds given by the squares of (GDE11.2). For \(z\ge0\), determinant comparisons follow factorwise, for example
\(\mathcal D_\zeta(z\kappa_{\min}^2;q,t)
\le\mathcal D_\zeta(z;r,t)
\le\mathcal D_\zeta(z\kappa_{\max}^2;q,t)\).

For \(u>t>0\), the exact time factor is
\[
A_{r,u}=M_{e^{2(u-t)(\sigma^2-\gamma^2)}}A_{r,t}
\le e^{2(u-t)}A_{r,t}.
\tag{GDE11.4}
\]
Its inverse on off-line coordinates is uniformly bounded exactly when that actual off-line set has bounded heights, equivalently is finite. This follows from the exact exponential and the finite count at bounded height. Empty off-line sets give zero receivers. In particular a reverse global energy bound is not asserted merely because every individual Gaussian value is nonzero.

The normality defect has a finite first-order operator limit on the original smooth domain. From (GDE2.3),
\[
\frac{B_{r,t}B_{r,t}^*-B_{r,t}^*B_{r,t}}t
\longrightarrow M_{2\Delta_r(\sigma)^2(1-2\sigma)}
\quad\text{on }H_\infty,
\tag{GDE11.5}
\]
uniformly on bounded sets. Indeed subtract the two full real exponentials, whose common \(-\gamma^2\) derivative cancels; the remainder is bounded by \(Ct(1+|\gamma|)^4\) in the scaled difference. For every \(t>0\), \(B_{r,t}\) is normal exactly when the off-line sector is empty, since its two positive square coefficients agree only at \(\sigma=1/2\). At \(t=0\) the bounded operator \(D_r^*\mathsf J\) is normal even without that condition, because both squares equal \(P_r\). Thus (GDE11.5) records a surviving infinitesimal operator; its reflected-pair trace cancellation is not its vanishing. No trace is assigned to its zero-time limit unless its absolute trace sum converges.

One exact small-parameter comparison also retains the original degree: with \(\delta=\sigma-1/2\),
\[
\frac{\Delta_r(\sigma)^2}{r(\log r)^2}
=4\left(\frac{\sinh(\delta\log r)}{\log r}\right)^2
\longrightarrow4\delta^2\quad(r\downarrow1).
\tag{GDE11.6}
\]
The convergence is uniform for \(|\delta|\le1/2\). For fixed \(t>0\), (GDE1.2) therefore permits it in both trace sums and in the corresponding trace-class operators. The limiting divisor trace is
\(4\sum m_\rho\delta^2e^{2t(\sigma^2-\gamma^2)}\). This is a computed displacement moment with the full Gaussian, not an assertion that the moment is zero.

## GDE12. The calculated noncancellation and its exact receiver

The trace-class receiver is attached to the actual original specialization map by (GDE0.5); its source pairing and exact source radical are (GDE2.4)–(GDE2.5). Its two traces and their Fredholm realizations retain the distinction between a value coordinate and the original divisor multiplicity. The ordinary off-diagonal trace, the commutator trace and every odd power trace vanish for proved reasons. The positive energy and the even block determinant coefficients remain, with their exact reflected Gaussian factors. The full original degree relation leaves (GDE7.4), and the degree-adjusted trace has the explicit positive reflected-orbit term (GDE7.6).

The source approximation reaches the unregularized actual boundary on all of \(Q\), with a quantified common-domain rate. It does not shrink its kernel or make its surviving off-line values zero. The determinant and resolvent recover that same sector through (GDE4.10). Thus the contemplated cyclicity, transfer-degree and functional-equation cancellations have each been performed; their exact remaining object is \(A_{r,t}\), with (GDE3.3) as its divisor-weighted orbit contribution. A further original-zeta trace identity must calculate that remaining expression, rather than replace it with the trace of \(B\) or of an antisymmetric commutator.

## GDE13. Source reading and verification scope

Read the current definition-source directive and all of GAP0–GAP9 in `../tau_weight_cohomology_20260924/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md`, SHA256 `1cb89804a1ad3990c5eab65c89b2c6c748764461a012194867d2250318a04a0e`. This supplies the actual full-source Gaussian, its half-Mellin convolution, source convergence, all reflected weights, every endpoint factor and the exact separator action.

Read all of ADM0–ADM9 in `../tau_weight_cohomology_20260924/ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md`, SHA256 `cefa50caadcb598df0936191e98a1a6beaf1495d932d86527cca110519b9db7e`. This supplies the exact common domain, its dual, actual specialization quotient and covariances, normal translation, geometric degree/transfer scope and the complete source factor. All of its stated source/human-paper dependencies remain those of that proof; no new complete human-paper reading is claimed.

Read the complete GTAH5 and the receiving discussion in GTAH6–GTAH7 in `GEOMETRIC_TRANSFER_POSITIVE_ADJOINT_DEFECT.md`, SHA256 `dd27d0022c6cc0b82fc0cabcc5d43aed84d18fe762f382ba3be16e2fa50dc739`. GTAH5.1 proves the ordinary-versus-original-divisor trace distinction and its finite local-jet trace receiver; GTAH5.2–GTAH5.3 prove the positive defect trace and bounds for \(e^{-t\gamma^2}\). Those results precede and are preserved by GDE1–GDE4. No complete reading of other GTAH sections is claimed in this calculation.

The trace-class, counted-trace, determinant, cyclicity, parameter and limit calculations above are independent derivations from these actual operators. No finite-height numerical experiment, RH assumption, simplicity assumption, retracted support arithmetic, publication operation or source-topology replacement was used.
