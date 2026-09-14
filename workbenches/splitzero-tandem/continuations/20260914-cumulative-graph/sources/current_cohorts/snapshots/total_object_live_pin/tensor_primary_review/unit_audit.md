# Full arithmetic unit on the tensor invariant block

This bounded independent audit retains the complete actual Taylor coefficients. It proves the coefficient action, all nonvanishing criteria, the finite inverse, the exact offblock correction, and the corresponding period-coordinate maps. It does not assume that any particular higher Taylor coefficient is nonzero.

Assignment, verbatim:

> New bounded fullunit tensor audit, own tensor_primary_review/unit_audit.md only. V=C[y1,..,yk]/yi^m,N=m+1, T=sumNi,Q0 projector degree k+|alpha| divisibleN. Full actual unit U_k=product_i sum_{j=0}^{m-1}a_jNi^j,a0≠0. Derive exact Q0 U_k Q0 coefficients, nonzero criterion for each monomial Ni^nu using d_min=(-k modN), inverse finite Neumann series with nilpotency via degree≥N, and exact relation to compression of U_k^-1; find identity exposing offblock correction, no generic claim when actual coefficients may vanish. Coordinates period Pi_k=e^{kc/u}W^⊗ D^⊗ P^⊗, period unit action product sum a_j u^{j/N}K_i^j. Verify exact projector commutator. Parent/source global edits forbidden.

## 1. The full tensor algebra and its projectors

Fix integers \(k,m\geq1\), and retain \(N=m+1\). Define
\[
 V=\mathbb C[y_1,\ldots,y_k]/(y_1^m,\ldots,y_k^m),\qquad
 e_\alpha=y_1^{\alpha_1}\cdots y_k^{\alpha_k},
 \quad 0\leq\alpha_i<m.
\tag{UTA1}
\]
The ordered tensor monomials \(e_\alpha\) form a basis: successive monic division in the independent variables gives their spanning property and uniqueness. Let \(N_i\) be multiplication by \(y_i\). They commute and satisfy \(N_i^m=0\), while
\[
 N^\nu e_\alpha:=
 \left(\prod_{i=1}^kN_i^{\nu_i}\right)e_\alpha
 =
 \begin{cases}
 e_{\alpha+\nu},&\alpha_i+\nu_i<m\text{ for all }i,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{UTA2}
\]
Put \(L_{\max}=k(m-1)\), \(|\alpha|=\sum_i\alpha_i\), and
\[
 \zeta=e^{2\pi i/N},\qquad
 M e_\alpha=\zeta^{k+|\alpha|}e_\alpha,\qquad
 Q_r e_\alpha=
   {\bf1}_{\,k+|\alpha|\equiv r\ (\mathrm{mod}\ N)}e_\alpha
 \quad(0\leq r<N).
\tag{UTA3}
\]
Thus \(Q_rQ_t=\delta_{rt}Q_r\), \(\sum_rQ_r=I_V\), and
\[
 Q_0=\frac1N\sum_{j=0}^{N-1}M^j.
\tag{UTA4}
\]
The last equality follows on every basis vector from the finite geometric sum of a power of \(\zeta\).

Write \(Q=Q_0\), \(F=QV\), and let \(d=(-k\bmod N)\) denote the unique integer in \(\{0,\ldots,N-1\}\) congruent to \(-k\). The degrees occurring in \(F\) are exactly
\[
 d,\ d+N,\ \ldots,\ d+\ell N,\qquad
 \ell=\left\lfloor\frac{L_{\max}-d}{N}\right\rfloor,
\tag{UTA5}
\]
when \(d\leq L_{\max}\); if \(d>L_{\max}\), then \(F=0\). To prove the existence assertion, for any capacities \(c_1,\ldots,c_k\geq0\), every integer between zero and \(\sum_i c_i\) is the sum of integers \(0\leq b_i\leq c_i\). Induction proves this: for target \(t\), take \(b_k=\max(0,t-\sum_{i<k}c_i)\), which is at most \(c_k\), and realize \(t-b_k\) using the induction hypothesis. Apply this with \(c_i=m-1\). This argument also supplies the capacity test below.

All restrictions and inverse formulas on \(F\) below are used in the case \(F\neq0\). For \(F=0\), every displayed compression to \(F\) is the unique map of the zero vector space and contributes no class.

## 2. Exact monomial criterion and full unit coefficients

For \(0\leq\nu_i<m\), let \(r=|\nu|\). By (UTA2),
\[
 QN^\nu Q\,e_\alpha
 =
 {\bf1}_{\,k+|\alpha|\equiv0}\,
 {\bf1}_{\,\alpha_i+\nu_i<m\ \forall i}\,
 {\bf1}_{\,k+|\alpha|+r\equiv0}\,e_{\alpha+\nu}.
\tag{UTA6}
\]
Consequently the precise nonzero criterion is
\[
 \boxed{\quad
 QN^\nu Q\neq0
 \iff
 r\equiv0\pmod N
 \quad\text{and}\quad
 d\leq L_{\max}-r.
 \quad}
\tag{UTA7}
\]
Indeed the congruences in (UTA6) force \(r\equiv0\). The remaining source exponents have independent capacities \(m-1-\nu_i\), with total \(L_{\max}-r\). They include a degree congruent to \(d\) precisely when they include the least nonnegative such degree \(d\), by the capacity argument after (UTA5). This proves both directions. If any \(\nu_i\geq m\), the monomial is zero already on \(V\) and is excluded from (UTA7).

The rank, including all multiplicities, is the integer
\[
 \operatorname{rank}(QN^\nu Q)
 =
 \sum_{j\geq0}
 [z^{d+jN}]
       \prod_{i=1}^k(1+z+\cdots+z^{m-1-\nu_i})
\tag{UTA8}
\]
when \(r\equiv0\pmod N\); it is zero otherwise. Each admissible source basis vector has a distinct nonzero target under translation by \(\nu\), proving that the count is the rank.

Retain the actual arithmetic unit coefficients
\[
 a_j=\frac{v_h^{(j)}(\rho)}{j!},
 \qquad
 0\leq j<m,\qquad a_0\neq0,
 \qquad
 U=\prod_{i=1}^k\left(\sum_{j=0}^{m-1}a_jN_i^j\right).
\tag{UTA9}
\]
For \(v_h=g/(s-\rho)^m\), this is
\(a_j=g^{(m+j)}(\rho)/(m+j)!\). Commutativity gives the literal expansion
\[
 U=\sum_{0\leq\nu_i<m}a_\nu N^\nu,
 \qquad a_\nu=\prod_{i=1}^k a_{\nu_i}.
\tag{UTA10}
\]
Hence its compression \(A=QUQ|_F\) is
\[
 A=a_0^k I_F+
 \sum_{\substack{0\leq\nu_i<m\\
                  |\nu|>0,\ |\nu|\equiv0\ (\mathrm{mod}\ N)\\
                  d+|\nu|\leq L_{\max}}}
          a_\nu QN^\nu Q|_F.
\tag{UTA11}
\]
All matrix coefficients are exact. If \(\alpha,\beta\) label basis vectors of \(F\), then
\[
 A_{\beta\alpha}
 =
 \begin{cases}
 \displaystyle\prod_i a_{\beta_i-\alpha_i},
                 &\beta_i\geq\alpha_i\text{ for all }i,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{UTA12}
\]
For any fixed matrix entry \((\beta,\alpha)\), at most one monomial \(N^\nu\) contributes, namely \(\nu=\beta-\alpha\). Therefore the nonzero operators in (UTA7) are linearly independent: each has at least one entry equal to one, and that entry lies in no other monomial operator's support. A term in (UTA11) is nonzero exactly when (UTA7) holds and the actual product \(a_\nu\) is nonzero. This is not an assumption on the coefficients.

The original total nilpotent \(T=\sum_iN_i\) is retained. The multinomial theorem gives
\[
 T^q=\sum_{|\nu|=q}\frac{q!}{\nu_1!\cdots\nu_k!}N^\nu.
\tag{UTA13}
\]
Thus \(QT^qQ=0\) unless \(q\equiv0\pmod N\), and for a nonnegative multiple \(q\) of \(N\), it is nonzero exactly when \(d+q\leq L_{\max}\). Existence of a monomial satisfying this condition follows by the same capacity argument; its multinomial coefficient is nonzero and the monomial entry supports are disjoint. In particular \(QTQ=0\). This does not set any \(N_i\), \(T\), or the higher compressions \(QT^{jN}Q\) equal to zero on the whole tensor algebra.

## 3. The finite inverse and the exact role of nilpotence

Put \(a=a_0^k\) and
\[
 H=a^{-1}A-I_F.
\tag{UTA14}
\]
Every summand of \(H\) raises total degree by a positive multiple of \(N\), hence by at least \(N\). A vector of \(F\) starts in degree at least \(d\), so \(H^{\ell+1}\) has no possible target degree by (UTA5). Therefore
\[
 H^{\ell+1}=0,\qquad
 \boxed{\quad A^{-1}=a^{-1}\sum_{p=0}^{\ell}(-H)^p.\quad}
\tag{UTA15}
\]
Multiplication by \(I_F+H\) telescopes to \(I_F+(-1)^\ell H^{\ell+1}=I_F\), proving both left and right inverse assertions. No convergence or completion is involved. The integer \(\ell+1\) is a proved upper bound for the nilpotence index; particular arithmetic coefficients can lower that index.

Here are full coefficients and an exact test for such additional vanishing. Let \(\mathcal R\) denote the finite set of nonzero multiindices occurring in the sum (UTA11), and set
\[
 b_\nu=\frac{a_\nu}{a}\quad(\nu\in\mathcal R),\qquad
 C_{p,\mu}
 =\sum_{\substack{\nu^{(1)},\ldots,\nu^{(p)}\in\mathcal R\\
                  \nu^{(1)}+\cdots+\nu^{(p)}=\mu}}
               \prod_{j=1}^p b_{\nu^{(j)}}.
\tag{UTA16}
\]
For \(p=0\), take \(C_{0,0}=1\) and \(C_{0,\mu}=0\) for \(\mu\neq0\). Empty sums are zero. A monomial whose degree is a multiple of \(N\) commutes with \(Q\), so successive multiplication gives
\[
 H^p=\sum_{\substack{0\leq\mu_i<m\\
                     |\mu|\equiv0\ (\mathrm{mod}\ N)\\
                     d+|\mu|\leq L_{\max}}}
             C_{p,\mu} QN^\mu Q|_F.
\tag{UTA17}
\]
To justify the use of \(\mathcal R\) at every intermediate step, a monomial with positive degree divisible by \(N\) and \(d+|\nu|>L_{\max}\) cannot be part of a nonzero product of such monomials, because the final degree can only increase. A coordinate exponent reaching \(m\) likewise remains at least \(m\). Thus the omitted terms cannot contribute later.

By the linear independence proved after (UTA12), \(H^p\neq0\) exactly when at least one admissible \(C_{p,\mu}\) is nonzero. Thus, with \(F\neq0\), its precise nilpotence index is
\[
 1+\max\{p\in\{0,\ldots,\ell\}:
             \text{some admissible }C_{p,\mu}\neq0\}.
\tag{UTA18}
\]
In particular, the coefficients of the exact inverse are
\[
 A^{-1}
 =\sum_{\mu\ \mathrm{admissible}}
       c_\mu QN^\mu Q|_F,\qquad
 c_\mu=a^{-1}\sum_{p=0}^{\ell}(-1)^p C_{p,\mu}.
\tag{UTA19}
\]
Here “admissible” means precisely the three conditions in the sum (UTA17), and includes \(\mu=0\). Formulas (UTA16)--(UTA19) retain every possible coefficient cancellation instead of assigning a generic nilpotence index.

## 4. Compression of the original inverse

Define the actual one-factor inverse Taylor coefficients recursively by
\[
 \widetilde a_0=a_0^{-1},\qquad
 \widetilde a_j
 =-a_0^{-1}\sum_{r=1}^j a_r\widetilde a_{j-r},
 \quad1\leq j<m.
\tag{UTA20}
\]
Coefficient multiplication shows that
\((\sum a_jz^j)(\sum\widetilde a_jz^j)=1\bmod z^m\):
the constant coefficient is one, and the coefficient of each positive degree below \(m\) is zero by (UTA20). Consequently
\[
 U^{-1}
 =\prod_{i=1}^k\left(\sum_{j=0}^{m-1}
                           \widetilde a_jN_i^j\right),
 \qquad
 \alpha:=QU^{-1}Q|_F
 =\sum_{\mu\ \mathrm{admissible}}
              \left(\prod_i\widetilde a_{\mu_i}\right)
                         QN^\mu Q|_F.
\tag{UTA21}
\]
Comparison with (UTA19) yields a fully explicit difference:
\[
 \alpha-A^{-1}
 =\sum_{\mu\ \mathrm{admissible}}
       \left[
         \prod_i\widetilde a_{\mu_i}
         -a^{-1}\sum_{p=0}^{\ell}(-1)^p C_{p,\mu}
       \right]QN^\mu Q|_F.
\tag{UTA22}
\]
Its constant coefficient is zero. The difference vanishes exactly when every displayed admissible coefficient is zero, by disjoint entry supports.

There is an equivalent exact block identity which displays the paths outside the invariant block. Let \(R=I_V-Q\), \(G=RV\), and write
\[
 U=
 \begin{pmatrix}A&B\\ C&D\end{pmatrix}
 \quad\text{on }F\oplus G,
 \qquad
 U^{-1}=
 \begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}.
\tag{UTA23}
\]
This defines each block, for example \(B=QUR|_G:G\to F\) and \(C=RUQ|_F:F\to G\). No orthogonality is assumed. The diagonal block \(D\) equals \(aI_G\) plus an operator which raises total degree by at least one. Its positive-degree part therefore has power \(L_{\max}+1\) zero. The same finite geometric argument as in (UTA15) proves that \(D\) is invertible.

Block multiplication \(UU^{-1}=U^{-1}U=I_V\) gives
\[
 \boxed{\quad
 \alpha-A^{-1}
 =-A^{-1}B\gamma
 =-\beta C A^{-1}.
 \quad}
\tag{UTA24}
\]
Indeed \(A\alpha+B\gamma=I_F\) and \(\alpha A+\beta C=I_F\), and multiplication by \(A^{-1}\) gives the identities.

More explicitly,
\[
 \begin{pmatrix}I_F&-BD^{-1}\\0&I_G\end{pmatrix}
 \begin{pmatrix}A&B\\ C&D\end{pmatrix}
 =
 \begin{pmatrix}A-BD^{-1}C&0\\ C&D\end{pmatrix}.
\tag{UTA25}
\]
The left side is invertible, since both factors are invertible, and \(D\) is invertible. Therefore \(S=A-BD^{-1}C\) is invertible. One can see this directly by applying the invertible block matrix to \((x,-D^{-1}Cx)\): a nonzero vector \(x\) in \(\ker S\) would give a nonzero kernel vector; finite-dimensionality then gives surjectivity. Solving its block equations yields
\[
 \alpha=(A-BD^{-1}C)^{-1},\qquad
 \gamma=-D^{-1}C\alpha,
\tag{UTA26}
\]
and hence
\[
 \boxed{\quad
 \alpha-A^{-1}
     =A^{-1}BD^{-1}C\,\alpha,\qquad
 \alpha=A^{-1}\iff BD^{-1}C=0.
 \quad}
\tag{UTA27}
\]
These are exact identities for the actual coefficients. The factors \(B\) and \(C\) both have positive degree, since the scalar part of \(U\) has zero offdiagonal blocks. The finite inverse of \(D\) never lowers degree. Therefore a nonzero term in \(BD^{-1}C\) raises degree by a positive amount; because it begins and ends in \(F\), that amount is a positive multiple of \(N\). It is at least \(N\), with all intermediate visits to \(G\) retained by the block projections.

Neither \(B\neq0\) nor \(C\neq0\), nor even both together, is by itself asserted to make \(BD^{-1}C\) nonzero. Formula (UTA22), or equivalently (UTA27), is the exact test including actual coefficient cancellations.

## 5. The precise projector commutator

The coefficient formula on the whole tensor basis is
\[
 ([Q,U])_{\beta\alpha}
 =
 \begin{cases}
 \left(
 {\bf1}_{\,k+|\beta|\equiv0}
 -
 {\bf1}_{\,k+|\alpha|\equiv0}
 \right)\displaystyle\prod_i a_{\beta_i-\alpha_i},
 &\beta_i\geq\alpha_i\text{ for all }i,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{UTA28}
\]
In the blocks (UTA23), this is precisely
\[
 [Q,U]=QU-UQ
 =\begin{pmatrix}0&B\\-C&0\end{pmatrix}.
\tag{UTA29}
\]
For a single multiindex \(\nu\) with \(0\leq\nu_i<m\), set \(r=|\nu|\), \(L_\nu=L_{\max}-r\), and let
\[
 d_r=(-k-r\bmod N)\in\{0,\ldots,N-1\}.
\]
The exact monomial commutator test is
\[
 [Q,N^\nu]\neq0
 \iff
 r\not\equiv0\pmod N
 \quad\text{and}\quad
 \bigl(d\leq L_\nu\ \text{or}\ d_r\leq L_\nu\bigr).
\tag{UTA30}
\]
For proof, the coefficient of \(e_{\alpha+\nu}\) is the target indicator minus the source indicator. If \(r\equiv0\), those indicators agree. If \(r\not\equiv0\), they cannot both be one, and their difference is nonzero exactly when the source has degree congruent to \(d\), or the target has degree congruent to \(d\), equivalently the source has degree congruent to \(d_r\). The admissible source degrees are every integer in \([0,L_\nu]\), by the capacity argument. This proves (UTA30).

The nonzero monomial commutators also have disjoint matrix-entry supports for distinct \(\nu\). Consequently
\[
 [Q,U]=0
\quad\Longleftrightarrow\quad
 a_\nu=0\text{ for every }\nu\text{ satisfying (UTA30)}.
\tag{UTA31}
\]
This is an exact criterion for the actual unit; it imposes no unproved generic nonvanishing condition. The operators themselves satisfy
\[
 MN_iM^{-1}=\zeta N_i,\qquad
 Q_r N^\nu=N^\nu Q_{r-|\nu|\bmod N},
\tag{UTA32}
\]
as is checked on each \(e_\alpha\), including vectors killed by \(N^\nu\).

## 6. Complete period-coordinate transport

Use the original one-factor Pascal matrix \(P\), Fourier-difference matrix \(W\), phase constant \(c=-(-\rho)^N/N\), and all gamma constants:
\[
 d_a=N^{(a+1)/N-1}e^{\pi i(a+1)/N}
          \Gamma\!\left(\frac{a+1}{N}\right),\qquad
 D_0=\operatorname{diag}(d_0,\ldots,d_{m-1}),
\]
\[
 D(u)=D_0\operatorname{diag}
       (u^{1/N},u^{2/N},\ldots,u^{m/N}),
 \qquad
 \Pi_k(u)=e^{kc/u}
             W^{\otimes k}D(u)^{\otimes k}P^{\otimes k}.
\tag{UTA33}
\]
The branch of every power of \(u\) is the original branch in the one-factor periods. The gamma constants are nonzero because the defining gamma integrals are positive and finite for \((a+1)/N\in(0,1)\). Thus \(D_0\) is invertible.

Write \(P_k=P^{\otimes k}\), \(W_k=W^{\otimes k}\), and \(D_{0,k}=D_0^{\otimes k}\). The tensor unit in the original coefficient coordinates is \(U_s=P_k^{-1}UP_k\), and the original-coordinate projector is \(Q_s=P_k^{-1}QP_k\). Since every \(D(u)^{\otimes k}\) is diagonal in the same monomial basis as \(Q\),
\[
 Q_{\mathrm{per}}:=\Pi_kQ_s\Pi_k^{-1}=W_kQW_k^{-1}.
\tag{UTA34}
\]
In particular this period-coordinate projector is constant in \(u\). Its monodromy expression is
\[
 M_{\mathrm{per}}=W_kMW_k^{-1},\qquad
 Q_{\mathrm{per}}=\frac1N\sum_{j=0}^{N-1}
                                   M_{\mathrm{per}}^j.
\tag{UTA35}
\]

Define the constant nilpotent matrices in period coordinates by
\[
 K_i=W_kD_{0,k}N_iD_{0,k}^{-1}W_k^{-1}.
\tag{UTA36}
\]
This definition retains every gamma ratio. For one factor,
\(D_0ND_0^{-1}e_a=(d_{a+1}/d_a)e_{a+1}\) for \(a<m-1\), and it kills the last vector. On the chosen branch,
\[
 D(u)^{\otimes k}N_i
       \bigl(D(u)^{\otimes k}\bigr)^{-1}
 =u^{1/N}D_{0,k}N_iD_{0,k}^{-1}.
\tag{UTA37}
\]
Indeed the ratio of the diagonal powers at \(\alpha+e_i\) and \(\alpha\) is exactly \(u^{1/N}\). Conjugating (UTA9) now gives the requested full period-unit action:
\[
 \boxed{\quad
 U_{\mathrm{per}}(u)
 :=\Pi_k U_s\Pi_k^{-1}
 =\prod_{i=1}^k
        \left(\sum_{j=0}^{m-1}a_j u^{j/N}K_i^j\right)
 =\sum_\nu a_\nu u^{|\nu|/N}K^\nu.
 \quad}
\tag{UTA38}
\]
The scalar \(e^{kc/u}\) cancels in this conjugation, but remains unchanged in the period matrix (UTA33). The factors \(K_i\) commute and satisfy \(K_i^m=0\), by their common conjugation of the original \(N_i\).

Let \(J(u)=W_kD(u)^{\otimes k}\). Then \(U_{\mathrm{per}}=J UJ^{-1}\), while \(Q_{\mathrm{per}}=JQJ^{-1}\). Thus the full projector commutator is exactly
\[
 \boxed{\quad
 [Q_{\mathrm{per}},U_{\mathrm{per}}]
 =J(u)[Q,U]J(u)^{-1}
 =\sum_\nu a_\nu u^{|\nu|/N}
                   [Q_{\mathrm{per}},K^\nu].
 \quad}
\tag{UTA39}
\]
The scalar part \(e^{kc/u}\) and Pascal factors have already canceled by their explicit conjugation; none are being assigned a changed value. For each \(u\neq0\) on the branch, \(J(u)\) is invertible, so (UTA30)--(UTA31) are also exact nonzero criteria for the period commutator.

Since \(D_{0,k}\) commutes with \(M\), (UTA32) gives
\[
 M_{\mathrm{per}}K_iM_{\mathrm{per}}^{-1}
       =\zeta K_i.
\tag{UTA40}
\]
Consequently the compression is
\[
 Q_{\mathrm{per}}U_{\mathrm{per}}Q_{\mathrm{per}}
 =aQ_{\mathrm{per}}
 +\sum_{\nu\in\mathcal R}
       a_\nu u^{|\nu|/N}
             Q_{\mathrm{per}}K^\nu Q_{\mathrm{per}}.
\tag{UTA41}
\]
Each exponent \(|\nu|/N\) here is a positive integer. Thus this compressed expression is single-valued, even though the full expression (UTA38) can have fractional powers. Analytic continuation of the full expression satisfies the precise equivariance
\[
 U_{\mathrm{per}}^{\mathrm{cont}}
 =M_{\mathrm{per}}U_{\mathrm{per}}M_{\mathrm{per}}^{-1},
\tag{UTA42}
\]
because continuation multiplies \(u^{|\nu|/N}\) by \(\zeta^{|\nu|}\), exactly the factor obtained by (UTA40).

All inverse and block identities (UTA15)--(UTA27) transport by \(J(u)\), restricted to \(F\) and its complement. This follows from conjugation preserving products, inverses, and each specified projection. Formula (UTA41) is an ambient endomorphism; its restriction to \(Q_{\mathrm{per}}V\) has inverse equal to the conjugate of \(A^{-1}\). The compression of \(U_{\mathrm{per}}^{-1}\), restricted to the same image, is the conjugate of \(\alpha\); their difference is the conjugate of the full operator (UTA22) or (UTA27).

Finally, two different typed maps must retain their stated direction. Formula (UTA38) is the unit endomorphism on period vectors, obtained by conjugating \(U_s\). If instead the arithmetic source coordinates are \(q_s=U_sx_s\), then the period map applied to \(q_s\) is
\[
 q_s\longmapsto \Pi_k U_s^{-1}q_s.
\tag{UTA43}
\]
This follows by substituting \(x_s=U_s^{-1}q_s\) in the original period map. It is consistent with (UTA38) and does not exchange a unit with its inverse. As in the one-factor audit, these are exact maps of the retained coefficient realization; multiplication on arbitrary twisted de Rham representatives retains its separate derivative correction.

The pulled-back projector in these actual source-weighted coordinates is consequently
\[
 Q_{\theta}
 =(\Pi_kU_s^{-1})^{-1}Q_{\mathrm{per}}(\Pi_kU_s^{-1})
 =U_sQ_sU_s^{-1}.
\tag{UTA44}
\]
Its image is exactly \(U_s(Q_sV_s)\): applying the operator to \(U_sx\) with \(Q_sx=x\) fixes that vector, while any value of the operator has this form. This image has not been silently identified with \(Q_sV_s\).

For the original arithmetic sum action
\[
 A_k=k\rho I+P_k^{-1}TP_k,
\]
the commutativity of the \(N_i\) implies \(U_sA_k=A_kU_s\). Conjugating the commutator and using \(QTQ=0\) from (UTA13) therefore gives
\[
 [Q_\theta,A_k]
      =U_s[Q_s,A_k]U_s^{-1},\qquad
 Q_\theta A_kQ_\theta=k\rho Q_\theta.
\tag{UTA45}
\]
These equalities are verified by direct multiplication, using \(U_s^{-1}U_s=I\) at each adjacent pair. Thus the unit-weighted source projector and the original nilpotent arithmetic action remain related by an explicit invertible map on the full tensor space.

For this repeated full unit, (UTA31) has a sharper exact specialization. For \(m\geq2\) and \(k\geq2\),
\[
 UF\subseteq F
 \iff [Q,U]=0
 \iff Q_\theta=Q_s
 \iff a_1=\cdots=a_{m-1}=0.
\tag{UTA46}
\]
To prove the nontrivial direction, any \(a_j\neq0\) with \(1\leq j<m\) supplies the single-coordinate increment \(\nu=je_i\) with coefficient \(a_ja_0^{k-1}\neq0\). For \(k=2\), \(d=m-1\) and \(L_{\max}-j\geq m-1\). For \(k\geq3\),
\[
 L_{\max}-j\geq(k-1)(m-1)\geq2m-2\geq m\geq d.
\]
The capacity argument therefore gives a source monomial in \(F\) on which this increment is nonzero. Its target lies in residue \(j\neq0\bmod N\). No other increment contributes to the same matrix entry, so \(UF\) is not contained in \(F\), and \([Q,U]\neq0\). Conversely, if every positive coefficient is zero, then \(U=a_0^kI_V\) and every displayed assertion follows. The projector equality is equivalent to commutation by (UTA44). For \(k=1\), \(F=0\); for \(m=1\), the unit is already scalar, so those cases are treated directly rather than by the outgoing-entry argument.

## Audit conclusion

The exact compressed coefficients are (UTA11)--(UTA12), with the complete necessary and sufficient monomial test (UTA7). The finite inverse is (UTA15), its actual coefficient cancellation test is (UTA16)--(UTA19), and its difference from compression of the original inverse is proved both coefficientwise in (UTA22) and by the offblock identity (UTA27). The precise projector commutator is (UTA28)--(UTA32), with complete period and source-weighted transport (UTA33)--(UTA46). None of these formulas treats a possibly vanishing arithmetic Taylor coefficient as nonzero.

## Independent receipt for the parent TPR proof

The complete current tensor_primary_review.tex, TPR.1--34, was read once, with the requested detailed check of TPR.5--6 and TPR.28--34. The marked pullback \(Q_{s,r}=S^{-1}Q_rS\), period projector \(E_r=W_kQ_rW_k^{-1}\), and \(\Pi_k^{-1}E_r\Pi_k=Q_{s,r}\) agree with (UTA33)--(UTA35). The positive powers \(u^{j/N}\) in TPR.29 are the correct ones for \(\Pi_kU_s\Pi_k^{-1}\), and each retained gamma ratio occurs in the specified \(K_i\).

TPR.30 has the correct shift sign \(Q_0J^\nu=J^\nu Q_{-|\nu|}\). Its coordinate support and actual coefficient \(\prod_i a_{\nu_i}\) agree with (UTA6)--(UTA12); distinct increments have disjoint matrix-entry support. TPR.31 proves an upper bound for the positive-degree part's nilpotence and uses the correct alternating inverse coefficients without declaring the index to be exact for arbitrary actual unit coefficients.

The sign of TPR.32 is correct. Namely \(UU^{-1}=I\), after left and right compression by \(Q\), gives \(A\alpha+B\gamma=I_F\). Therefore \(I_F-A\alpha=B\gamma=QU(I-Q)U^{-1}Q|_F\), exactly its displayed identity. The coefficient test (UTA22) and Schur formula (UTA27) independently retain every possible cancellation in that defect.

Finally TPR.33 uses the actual direction \(q_s=U_sx_s\), so its period map is \(\Pi_kU_s^{-1}\) and its source-weighted projector is \(U_sQ_{s,0}U_s^{-1}\), not \(Q_{s,0}\) by an unstated identification. TPR.34 follows by the actual commutativity of \(U_s\) and \(A_k\), as proved in (UTA44)--(UTA45). No error was found in these checked formulas or in the complete surrounding tensor calculation.

A separate bounded subagent independently rederived the monomial capacity test, nilpotence bound, finite Schur formula, period conjugation, and exact commutator coefficient support without reading this note. Its findings agree with (UTA7), (UTA15), (UTA27), (UTA30), and (UTA38)--(UTA39).

The subsequently added TPR.35 was read separately. Its stronger equivalence with \(U_yV_0\subseteq V_0\) is correct: the single-coordinate increment has coefficient \(a_ja_0^{k-1}\), its capacity inequalities hold for every \(m\geq2,k\geq2\), and its target has nonzero residue. Its complete proof is reproduced independently in (UTA46). The parent also checked the present UTA1--43 derivation; its sole codomain correction was applied to (UTA41), whose scalar term is now the ambient \(aQ_{\mathrm{per}}\), with inverse statements explicitly restricted to \(Q_{\mathrm{per}}V\).
