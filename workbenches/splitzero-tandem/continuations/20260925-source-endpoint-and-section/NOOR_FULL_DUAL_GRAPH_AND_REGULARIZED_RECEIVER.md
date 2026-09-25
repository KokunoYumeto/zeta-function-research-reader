# Noor's finite jet receiver: full strong-dual graph and exact regularized continuation

Independent mathematical continuation, 25 September 2026. Proof locators **NHD0–NHD10**.

## NHD0. Scope, exact inputs and retained arithmetic

This calculation starts from the actual finite-jet injection in NHR7 and the original-topology synthesis in GSP/GSI. It computes an exact continuity criterion, constructs the complete closed graph relation and its maximal Hilbert domain, and constructs a continuous regularized receiver on the entire original strong dual. It does not infer continuity from density.

The complete incoming proof `NOOR_ORIGINAL_ZETA_JET_RECEIVER.md`, NHR0–NHR9, and its complete `SOURCE_RECEIPT.json` were read. Their SHA256 values are respectively

`37e08dee8224d95394133ef39ee2fcbcc8267195babe2ec192a58440a7a3d1c1`,

`d12304d5cc55342084470d33fe7fb33e16418660be30ac2b563a8b9c975e335b`.

The incoming source is S. Waleed Noor, *A Hardy space analysis of the Báez-Duarte criterion for the RH*, arXiv:1809.09577v4. Its receiver proof records the original-author TeX SHA256 `bc3075483547782dce36bf55a6349899a26766fcfc8ae9f265079ec74601f2d3` and exact reading coverage through source line 387. This continuation receives those verified formulas; it does not claim a new reading of the whole human paper. Programme inputs newly inspected or previously proved independently are GSP0–GSP9, GSI0–GSI12, and SDT1–SDT6, the latter at SHA256 `7f1a03a6225f1dfc22b167713c0ddbb154635b06f9479f6137b229845b67aefc`.

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All coefficients and operations below occur after the complete arithmetic reconstruction. No addition, metric or coordinate is imposed on that support, and no branch return measures are pooled.

Retain the original entire strip space \(\mathcal B\), its full nontrivial-zero ideal \(I\), and \(Q=\mathcal B/I\). In particular
\[
b_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|,
\qquad
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{NHD0.1}
\]
The complete entire multiplier has
\[
F_0(0)=F_0(1)=\frac18,
\qquad
F_0(-2a)=\frac{a(2a+1)(-1)^a\pi^a}{2\,a!}\zeta'(-2a)\ne0.
\tag{NHD0.2}
\]
All actual orders \(m_\rho\), full source derivatives, original \(\zeta\), and its unit and prime-power repetitions remain those of the source proofs.

## NHD1. The precise completed domain of the finite right-jet span

Write
\[
\mathscr Z_+=\{\rho\in\mathscr Z:1/2<\Re\rho<1\},
\quad
I_{\mathrm{right}}=\{F\in\mathcal B:F^{(a)}(\rho)=0\ (\rho\in\mathscr Z_+,\ a<m_\rho)\},
\]
\[
Q_{\mathrm{right}}=\mathcal B/I_{\mathrm{right}},\qquad N_{\mathrm{right}}=I_{\mathrm{right}}/I\subset Q.
\tag{NHD1.1}
\]
The subscript \(\mathrm{right}\) means restriction to the actual right-half-strip zero divisor. These are never the normal-shift ideal or source denoted \(I_+\) and \(Q_+\) in ADM/FOD; no spectral translation is performed here.

These ideals and subspaces are closed by continuity of all the indicated evaluations. The original quotient maps give \(Q_{\mathrm{right}}=Q/N_{\mathrm{right}}\).

The compactness, bounded lifting and strong-bidual arguments in SDT1–SDT6 apply to this specific quotient as follows. Use the exact source isomorphism \(\Theta:A\to\mathcal B\), and the closed kernel \(\Theta^{-1}I_{\mathrm{right}}\) in place of \(J\). SDT2's finite-net estimate uses only the original source norms, so it is unchanged. SDT3 lifts representatives separately for each seminorm and proves compactness of closures of bounded sets for this quotient as well. SDT4 constructs compact lifts using only a Fréchet source and closed kernel. Thus SDT5 gives bounded lifts for this quotient and for \(Q\to Q_{\mathrm{right}}\). Finally SDT6's compact absolutely convex hull argument proves its strong bidual is the original \(Q_{\mathrm{right}}\). Consequently the transpose inclusion identifies, with the exact strong subspace topology,
\[
D_{\mathrm{right}}:=(Q_{\mathrm{right}})'_\beta\simeq
N_{\mathrm{right}}^\perp\subset Q'_\beta,
\qquad (D_{\mathrm{right}})'=Q_{\mathrm{right}}.
\tag{NHD1.2}
\]
No general assertion about arbitrary quotients of Montel spaces replaces this stated application of the constructed estimates.

Let \(E_+\) be NHR7's finite span of the full derivative functionals \(\varepsilon_{\rho,a}\) at \(\mathscr Z_+\). GSP's finite-rank multiplier \(K_j\) preserves \(N_{\mathrm{right}}\), and \(K_j'\lambda\in E_+\) for every \(\lambda\in D_{\mathrm{right}}\): a block outside \(\mathscr Z_+\) lies in \(N_{\mathrm{right}}\) and is annihilated by \(\lambda\). GSP7 proves \(K_j'\lambda\to\lambda\) in the original strong topology. Conversely every member of \(E_+\) annihilates \(N_{\mathrm{right}}\), whose annihilator is closed. Thus
\[
\boxed{\overline{E_+}^{\,Q'_\beta}=D_{\mathrm{right}}.}
\tag{NHD1.3}
\]
The closure is this specified branch annihilator, not the full original dual. Left and line jets are still present in the ambient \(Q'_\beta\).

## NHD2. An exact obstruction to continuous Hardy extension

NHR's conjugate-linear injection is
\[
R\Bigl(\sum b_{\rho,a}\varepsilon_{\rho,a}\Bigr)
=\sum\overline{b_{\rho,a}}g_{\rho,a}\in H^2,
\qquad g_{\rho,0}(0)=-\frac1{\bar\rho}.
\tag{NHD2.1}
\]
If the actual set \(\mathscr Z_+\) is infinite, its isolated zeros have unbounded heights. Choose distinct \(\rho_j\) with \(|\Im\rho_j|\to\infty\) and put \(\lambda_j=\rho_j\varepsilon_{\rho_j,0}\). For every bounded \(K\subset Q\), original quotient seminorms give
\[
\sup_{x\in K}|\lambda_j(x)|
\le |\rho_j|(1+|\Im\rho_j|)^{-N}
\sup_{x\in K}q_{1,N}(x)\longrightarrow0
\quad(N\ge2).
\tag{NHD2.2}
\]
Indeed \(\varepsilon_\rho\) is unchanged by adding any member of \(I\), so the strip bound passes through the infimum defining \(q_{1,N}\). Therefore \(\lambda_j\to0\) in \(D_{\mathrm{right}}\) with its actual strong topology. But the exact constant coefficient of its Hardy image is
\[
(R\lambda_j)(0)=\bar\rho_j\left(-\frac1{\bar\rho_j}\right)=-1.
\tag{NHD2.3}
\]
Since evaluation at zero has norm one on \(H^2\), these images do not tend to zero. This proves failure of continuity on the finite span itself. In this case no continuous extension to \(D_{\mathrm{right}}\), or to the full \(Q'_\beta\), can agree with NHR7 on \(E_+\).

If \(\mathscr Z_+\) is finite, all its multiplicities are finite, and (NHD1.3) gives \(D_{\mathrm{right}}=E_+\), a finite-dimensional subspace. The finite map is continuous. Moreover the finite full-jet projector \(P_+=\sum_{\rho\in\mathscr Z_+}P_\rho\) is continuous on \(Q\), and
\[
\lambda\longmapsto R(P_+'\lambda)
\tag{NHD2.4}
\]
is a continuous conjugate-linear map on the entire original strong dual agreeing with NHR7. The empty set gives the zero map. Thus the exact criterion is
\[
\boxed{R:E_+\to H^2\text{ is continuous in the induced strong topology}
\iff\mathscr Z_+\text{ is finite}.}
\tag{NHD2.5}
\]
This is a proved criterion for the actual divisor, not a claim deciding its cardinality. Noncontinuity does not by itself settle closability: the sequence in (NHD2.3) is not asserted to converge in the Hardy norm. The closed graph is computed next rather than inferring its shape from this example.

## NHD3. The actual Hardy-to-source matching graph

For \(h\in H^2\), let \(a=\Phi^{-1}h\) in Noor's exact \(\ell^2_\omega\) and let \(Ua\) be the step function of NHR2. Define
\[
F_h(s)=\langle h,g_s\rangle
=\int_0^1(Ua)(x)x^{s-1}\,dx,
\qquad 1/2<\Re s<1.
\tag{NHD3.1}
\]
The equality follows from the orthogonal step projection in NHR2 and the unitary \(\Phi\). Cauchy–Schwarz makes the integral absolute; its derivatives are justified locally by
\[
\|\partial_{\bar s}^{j}g_s\|_{H^2}^2
\le\frac{(2j)!}{(2\Re s-1)^{2j+1}}.
\tag{NHD3.2}
\]
Thus \(F_h\) is holomorphic there and \(F_h^{(j)}(\rho)=\langle h,g_{\rho,j}\rangle\). In particular every such jet is a continuous linear functional of \(h\).

Define the following closed linear subspace of a product of original spaces:
\[
\mathscr T_+=\{(h,x)\in H^2\times Q_{\mathrm{right}}:
\varepsilon_{\rho,j}(x)=\langle h,g_{\rho,j}\rangle
\text{ for every }\rho\in\mathscr Z_+,\ j<m_\rho\}.
\tag{NHD3.3}
\]
Closedness follows from the just-proved continuity of each constraint. The complete family of right jets separates \(Q_{\mathrm{right}}\), so at most one \(x\) accompanies a given \(h\). Accordingly write \(J_+h=x\) on its domain \(\mathscr A_+\subset H^2\). Equip \(\mathscr A_+\) with the exact graph topology
\[
\|h\|_{H^2}+q^+_{A,N}(J_+h).
\tag{NHD3.4}
\]
The closed graph (NHD3.3) makes it a complete Fréchet space; inclusion into \(H^2\) and \(J_+:\mathscr A_+\to Q_{\mathrm{right}}\) are continuous. No existence of an entire source representative for an arbitrary \(F_h\) is assumed: membership means precisely that its entire right-zero jet data is represented by a member of the original \(\mathcal B\), modulo \(I_{\mathrm{right}}\).

This test domain is maximal in a precise topological sense. The functional on \(E_+\)
\[
\lambda\longmapsto\langle h,R\lambda\rangle
\tag{NHD3.5}
\]
is complex linear. It extends continuously to \(D_{\mathrm{right}}\) exactly when \(h\in\mathscr A_+\). To prove this, every continuous extension is evaluation at a unique \(x\in Q_{\mathrm{right}}\), by (NHD1.2). Testing the finite jet generators makes that condition exactly (NHD3.3). Conversely those equations give evaluation at \(J_+h\) on the finite span, hence its continuous extension. Uniqueness follows from (NHD1.3).

In the infinite-divisor case, the constant Hardy vector \(1\) is not in \(\mathscr A_+\): its required values are \(-1/\rho\), which contradict rapid decay along the unbounded right-zero sequence exactly as in (NHD2.2). This concrete exclusion does not assert that \(\mathscr A_+\) fails to be dense in \(H^2\).

## NHD4. A continuous receiver for every member of the original branch strong dual

Transpose the actual continuous matching map:
\[
\mathcal T_+=J_+':D_{\mathrm{right}}\longrightarrow(\mathscr A_+)'_\beta,
\qquad (\mathcal T_+\lambda)(h)=\lambda(J_+h).
\tag{NHD4.1}
\]
It is continuous for the strong topologies, because the image under \(J_+\) of every graph-bounded test set is bounded in \(Q_{\mathrm{right}}\). Its full source domain is \(D_{\mathrm{right}}\). The Hardy comparison is the canonical continuous map
\[
\iota:\overline{H^2}\longrightarrow(\mathscr A_+)'_\beta,
\qquad\iota(\bar y)(h)=\langle h,y\rangle.
\tag{NHD4.2}
\]
Continuity follows since graph-bounded sets are Hardy-norm bounded. Equations (NHD3.3) give exactly
\[
\mathcal T_+\lambda=\iota(\overline{R\lambda})\quad(\lambda\in E_+).
\tag{NHD4.3}
\]
Thus the receiving diagram preserves NHR7's necessary conjugation. It does not posit a Hardy vector for an arbitrary original functional.

The precise kernels are
\[
\ker\iota=\overline{\mathscr A_+^\perp},
\qquad
\ker\mathcal T_+=(\overline{J_+\mathscr A_+}^{\,Q_{\mathrm{right}}})^\perp.
\tag{NHD4.4}
\]
The bar on the first expression denotes the conjugate vector space; \(\mathscr A_+^\perp\) is already a closed Hardy subspace. Both identities follow by evaluating on all tests, with continuity allowing closure in the second. They retain any failure of injectivity instead of assuming it from the finite injection.

For Noor's original \(h_n\), the complete original-zeta identity is
\[
F_{h_n}(s)=(1-n^{1-s})\frac{\zeta(s)}s.
\tag{NHD4.5}
\]
Its full jets vanish on the actual right divisor; hence \(h_n\in\mathscr A_+\), \(J_+h_n=0\), and every received functional annihilates these tests. More generally the Hardy orthogonal complement of the closed finite received span belongs to \(\mathscr A_+\) with \(J_+=0\).

## NHD5. Exact closed graph relation and maximal Hardy domain

Let \(G\) be the closure in \(D_{\mathrm{right}}\times\overline{H^2}\) of the linear graph
\(\{(\lambda,\overline{R\lambda}):\lambda\in E_+\}\).
Then
\[
\boxed{G=\{(\lambda,\bar y):
\langle h,y\rangle=\lambda(J_+h)\text{ for every }h\in\mathscr A_+\}.}
\tag{NHD5.1}
\]
To prove equality, a continuous linear functional on the product is of the form
\(\lambda(x)+\langle h,y\rangle\), with \(x\in Q_{\mathrm{right}}\) by (NHD1.2), and \(h\in H^2\) by the Hilbert representation theorem. It vanishes on the finite graph precisely when every right jet of \(x\) equals the negative of the corresponding jet of \(F_h\). That is exactly \(h\in\mathscr A_+\) and \(x=-J_+h\). The intersection of the kernels of these annihilating functionals equals the closure of a linear subspace in a Hausdorff locally convex space, by Hahn–Banach separation. This proves (NHD5.1), not only one containment.

The vertical part is exactly
\[
G\cap(\{0\}\times\overline{H^2})
=\{0\}\times\overline{\mathscr A_+^\perp}.
\tag{NHD5.2}
\]
Thus the initial operator is closable precisely when \(\mathscr A_+\) is dense in \(H^2\). This criterion is not decided by the noncontinuity proof. No closability or nonclosability is asserted without the corresponding density result.

The exact projection of this graph onto the original source, namely the maximal Hardy domain of this closed relation, is
\[
\mathfrak D_H=\left\{\lambda\in D_{\mathrm{right}}:
\exists C<\infty\ \forall h\in\mathscr A_+,\
|\lambda(J_+h)|\le C\|h\|_{H^2}\right\}.
\tag{NHD5.3}
\]
Indeed a representing \(y\in H^2\) gives this inequality by Cauchy–Schwarz. Conversely the inequality extends the functional uniquely to \(H_0=\overline{\mathscr A_+}^{\,H^2}\), and the Hilbert representation theorem gives a unique \(y_0\in H_0\) satisfying (NHD5.1). Every Hardy solution is
\[
y=y_0+v,\qquad v\in\mathscr A_+^\perp,
\quad
\|y_0\|=\sup_{h\in\mathscr A_+,\,\|h\|\le1}|\lambda(J_+h)|.
\tag{NHD5.4}
\]
The reduced map \(\lambda\mapsto y_0\) is conjugate-linear and has closed graph in \(D_{\mathrm{right}}\times H_0\); this follows by imposing all closed equalities in (NHD5.1) and restricting to the closed subspace \(H_0\). Its domain and any multivalued vertical part are explicit, with no assumed Hardy extension.

Every vector in (NHD5.1) belongs to Noor's \(\mathcal N^\perp\), since the finite graph does and that Hardy subspace is closed; equivalently use the tests (NHD4.5). Noor's unconditional theorem therefore continues to give
\[
y\in\operatorname{dom}M^*=\mathcal D_{\delta_1},\quad
(\lambda,\bar y)\in G
\quad\Longrightarrow\quad y=0.
\tag{NHD5.5}
\]
It does not force \(\lambda=0\): the possible kernel is exactly the one retained in (NHD4.4). This is the complete-domain formulation of the adjoint-domain distinction, rather than an inference from the finite power-log examples.

## NHD6. Raw arithmetic action on the complete matching receiver

Keep Noor's unrescaled cover \(W_n\) and the original multiplier \(U_nF=n^{1-s}F\). NHR4's full jet formula implies
\[
F_{W_nh}^{(j)}(\rho)
=\left.\partial_s^j\bigl(n^{1-s}F_h(s)\bigr)\right|_{\rho}.
\tag{NHD6.1}
\]
This also follows by pairing \(W_nh\) with \(g_{\rho,j}\) and using the complete adjoint action, including its binomial coefficients and conjugations. Consequently
\[
W_n\mathscr A_+\subset\mathscr A_+,
\qquad J_+W_n=U_nJ_+.
\tag{NHD6.2}
\]
The action is continuous in the graph topology: \(W_n\) is bounded on \(H^2\), with norm \(\sqrt n\), and \(U_n\) is continuous on \(Q_{\mathrm{right}}\). Transposing gives the full-domain commuting relation
\[
\boxed{\mathcal T_+U_n'=(W_n|_{\mathscr A_+})'\mathcal T_+.}
\tag{NHD6.3}
\]
The closed graph relation also satisfies
\[
(\lambda,\bar y)\in G
\quad\Longrightarrow\quad
(U_n'\lambda,\overline{W_n^*y})\in G,
\tag{NHD6.4}
\]
by continuity and the finite intertwining relation. This gives a genuine arithmetic comparison on the complete constructed receiver.

The source companion remains \(T_n'=n(U_n')^{-1}\). Its existence on the source is unchanged. No global inverse of \(W_n^*\) is asserted: the exact Hardy identities remain
\[
W_n^*W_n=nI,\qquad W_nW_n^*=nP_n,
\tag{NHD6.5}
\]
with the original nonzero complementary projector for \(n>1\). The relation (NHD6.4) supplies the forward action actually justified by the graph; it is not replaced by a falsely invertible Hardy action.

## NHD7. Entire corrected coefficient tests with the exact endpoint factor

There is also a concrete receiver on **all** of \(Q'_\beta\), including the left and critical-line dual sectors. It will be regularized and holomorphic on the disk, without an asserted Hardy boundary norm.

For integers \(m\ge1\) define
\[
\phi_m(s)=\frac{m^{1-s}-(m+1)^{1-s}}s,
\quad \phi_0(s)=-\frac1s,
\qquad
\psi_m(s)=\phi_m(s)+\frac{8F_0(s)}s\quad(m\ge0).
\tag{NHD7.1}
\]
Every numerator of \(\phi_m\) has value \(-1\) at zero. Since \(8F_0(0)=1\), \(\psi_m\) is entire, including \(m=0\). The factor eight and the full multiplier are essential. For every actual nontrivial zero and every derivative order below its multiplicity,
\[
\psi_m^{(j)}(\rho)=\phi_m^{(j)}(\rho).
\tag{NHD7.2}
\]
This uses \(\rho\ne0\) and the full zero order of \(F_0\), not removal of the correction from the original source.

Each \(\psi_m\) has polynomial strip growth. More quantitatively, on \(|\Re s|\le A\), outside \(|s|<1\), the numerator bound gives at most a constant times \((m+1)^{A+1}\) plus the fixed strip bound of \(F_0\). Inside that disk apply the maximum principle to the entire divided function on the radius-two disk, using the numerator bound on its boundary. Combining the two gives, for a finite \(C_A\),
\[
\sup_{|\Re s|\le A}|\psi_m(s)|
\le C_A(m+1)^{A+3}.
\tag{NHD7.3}
\]
This coarse exponent works also for \(A<2\) and \(m=0\). For each fixed \(t>0\),
\[
F_{t,m}(s)=e^{ts^2}\psi_m(s)\in\mathcal B,
\qquad
b_{A,N}(F_{t,m})\le C_{A,N,t}(m+1)^{A+3},
\tag{NHD7.4}
\]
since \((1+|y|)^Ne^{-ty^2}\) is bounded and the remaining Gaussian factor is \(e^{tA^2}\). These are full original source tests. Their original inverse source is exactly
\[
a_{t,m}(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F_{t,m}(1/2+iy)u^{-iy}\,dy,
\qquad\Theta a_{t,m}=F_{t,m}.
\tag{NHD7.5}
\]
All source seminorms are finite by the established inverse-transform theorem; no metric or operation on the primitive support enters this construction.

## NHD8. A continuous full-strong-dual analytic receiver

For \(\lambda\in Q'_\beta\), define
\[
\mathcal H_t\lambda(z)=
\sum_{m=0}^\infty\overline{\lambda([F_{t,m}])}\,z^m,
\qquad |z|<1.
\tag{NHD8.1}
\]
Continuity of \(\lambda\) bounds it by one original quotient seminorm, so (NHD7.4) bounds its coefficients by a finite polynomial in \(m\). Thus the series converges uniformly on every compact subdisk and defines a holomorphic function.

The map is continuous from the full original strong dual into \(\mathcal O(\mathbb D)\) with its compact-open topology. For proof, for every \(0<r<1\) the series
\[
K_{t,z}(s)=\sum_{m\ge0}F_{t,m}(s)\bar z^m
\tag{NHD8.2}
\]
converges uniformly for \(|z|\le r\) in every original \(b_{A,N}\), by (NHD7.4). The resulting family of classes \([K_{t,z}]\) is bounded in \(Q\). Moreover
\[
\sup_{|z|\le r}|\mathcal H_t\lambda(z)|
=\sup_{|z|\le r}|\lambda([K_{t,z}])|,
\tag{NHD8.3}
\]
which is a defining strong-dual seminorm. This proves the asserted continuity with no boundary estimate inserted.

On the original finite right-jet domain the comparison is exact:
\[
\mathcal H_t\lambda=R(m_{g_t}'\lambda)
\quad(\lambda\in E_+),\qquad g_t(s)=e^{ts^2}.
\tag{NHD8.4}
\]
Indeed the coefficients of \(g_{\rho,j}\) are the complex conjugates of \(\phi_m^{(j)}(\rho)\). Apply the full Leibniz rule to \(g_t\psi_m\), and use (NHD7.2), retaining all factorial and multiplicity terms. This is exactly the transpose multiplier action followed by the conjugate-linear NHR map. In particular \(\mathcal H_t\lambda\to R\lambda\) in \(H^2\) for each \(\lambda\in E_+\), since its finite jet multiplier matrix tends to identity. No such unregularized Hardy limit is asserted for an arbitrary member of the strong dual.

Thus the actual entire source construction supplies a receiver on the whole original dual for every positive regularization parameter. Its target and topology are explicit; a finite Hardy comparison is not promoted to a global Hardy norm estimate.

## NHD9. Exact unilateral covers on the analytic receiver

On \(\mathcal O(\mathbb D)\), define the continuous coefficient operator
\[
(\mathscr W_n^*f)_m=\sum_{a=0}^{n-1}f_{nm+a}.
\tag{NHD9.1}
\]
It agrees with \(W_n^*\) on \(H^2\). For continuity on a compact subdisk \(|z|\le r<1\), choose \(R\) with \(r^{1/n}<R<1\). Cauchy's coefficient estimate on \(|z|\le R\) bounds the output by
\[
\sup_{|z|\le r}|\mathscr W_n^*f(z)|
\le\frac{\sum_{a=0}^{n-1}R^{-a}}{1-rR^{-n}}
\sup_{|z|\le R}|f(z)|.
\tag{NHD9.2}
\]
The exact telescoping identity for (NHD7.1), including the first block, is
\[
\sum_{a=0}^{n-1}\phi_{nm+a}(s)=n^{1-s}\phi_m(s).
\tag{NHD9.3}
\]
The corrected entire tests therefore retain the full representative discrepancy
\[
\sum_{a=0}^{n-1}\psi_{nm+a}(s)-n^{1-s}\psi_m(s)
=8F_0(s)\frac{n-n^{1-s}}s.
\tag{NHD9.4}
\]
The last quotient is entire because its numerator vanishes at zero. After multiplication by \(g_t\), it lies in the original ideal \(I\), with every full zero order intact. Taking the original quotient and then applying \(\lambda\) to each coefficient proves
\[
\boxed{\mathcal H_tU_n'=\mathscr W_n^*\mathcal H_t
\quad\text{on the entire original }Q'_\beta.}
\tag{NHD9.5}
\]
This comparison uses the original companion \(n^{1-s}\), the factor eight, the original \(F_0\), and the exact quotient correction. No inverse of the unilateral adjoint or scalar rescaling has been introduced.

## NHD10. What is now established and retained

The finite Hardy injection has a proved continuity criterion: it extends continuously in the original strong topology precisely when the actual right-off-line divisor is finite. The global arithmetic has not been altered to satisfy this criterion, and its cardinality has not been decided. The source completion is the exact branch annihilator (NHD1.3), not an asserted deletion of the other branches.

For the general actual divisor, (NHD3.3)–(NHD5.4) construct the maximal continuous Hardy test space, the full-domain strong-dual receiver, the exact closed graph relation and its maximal Hardy domain. They retain any vertical graph part and any source kernel. Equation (NHD5.5) preserves the exact adjoint-domain restriction in Noor's theorem on that entire graph.

Equations (NHD7.1)–(NHD9.5) additionally construct a concrete continuous holomorphic receiver on every member of the full original strong dual, with the complete arithmetic cover action and its original-source discrepancy. The endpoint correction and all original factors are necessary parts of the calculation. Nothing here asserts a new RH criterion beyond the received theorems, a positive norm on the original reciprocal-zeta pairing, or vanishing of Deligne's lifting obstruction.
