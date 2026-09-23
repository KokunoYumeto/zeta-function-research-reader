# The exact reflection index of the global Cauchy–Weil pairing

This calculation determines the full negative index of the actual time-zero Cauchy kernel and of its complete coefficient tower at one real pole. The answer is the number of distinct two-point orbits of the actual zero set under reflection in the critical line. That number is allowed to be zero, a finite positive integer, or infinity; the calculation does not assert which alternative occurs. Multiplicity, every local jet, and the full supported arithmetic receiver remain explicit.

The inputs are the complete proofs [AG1–AG24](ACTUAL_HEAT_ZERO_DISTRIBUTION_VARIATION.md), [CK1–CK19](CAUCHY_WEIL_POSITIVITY_CRITERION.md), and [HA1–HA26](HEAT_CAUCHY_ARITHMETIC_DERIVATION.md). All three files were read in full for this derivation. In particular, the convergence below uses the proved actual zero count, and the support calculation uses the full arithmetic identity rather than a replacement of its endpoint terms.

## 1. The actual zero set, its weights, and reflection

Put
\[
g(s)=2\xi_R(s),\qquad L_g(s)=g'(s)/g(s),\qquad
\mathcal U=\{z\in\mathbb C:\Re z>1\}.
\tag{NI1}
\]
Let \(\mathcal Z\) be the set of **distinct** zeros of \(g\), and let \(m_\rho\ge1\) be the order of its zero at \(\rho\). The original functional equation and real coefficients give an involution
\[
\rho\longmapsto\rho^\#=1-\bar\rho,\qquad
m_{\rho^\#}=m_\rho.
\tag{NI2}
\]
The zeros lie in \(0<\Re\rho<1\), are discrete in \(\mathbb C\), and have no finite accumulation point. AG4–AG5 gives
\[
\sum_{|\rho|\le R}m_\rho=O(R\log(R+2)),\qquad
\sum_{|\rho|>R}\frac{m_\rho}{|\rho|^2}
=O\left(\frac{\log(R+2)}R\right).
\tag{NI3}
\]
In particular, \(\sum_\rho m_\rho/(1+|\rho|^2)<\infty\). Let \(\mathcal Z_{\rm fix}\) be the fixed-point set of (NI2), and choose one representative for each two-point orbit to form \(\mathcal P\). Define
\[
\kappa_-:=\#\mathcal P,\qquad
\kappa_+:=\#\mathcal Z_{\rm fix}+\#\mathcal P,
\tag{NI4}
\]
where each count is an element of \(\{0,1,2,\ldots,\infty\}\). These are counts of distinct supports, not sums of the multiplicities. A usual off-line quartet with nonzero imaginary part contains two orbits of (NI2), one at each sign of the imaginary part.

Define the Hilbert space, with inner product conjugate-linear in its first argument,
\[
\mathcal H=\ell^2(\mathcal Z,m),\qquad
\langle a,b\rangle_{\mathcal H}
=\sum_{\rho\in\mathcal Z}m_\rho\overline{a_\rho}b_\rho.
\tag{NI5}
\]
The reflection operator and the associated Hermitian form are
\[
(Ja)_\rho=a_{\rho^\#},\quad J^2=I,
\quad J^*=J,\quad \|J\|=1,
\qquad [a,b]=\langle Ja,b\rangle_{\mathcal H}.
\tag{NI6}
\]
These operator assertions follow by changing the summation variable in (NI5) using (NI2). The zero space, if present, has the same formulas with the evident norm convention. In particular the form is nondegenerate: if \([a,b]=0\) for all \(b\in\mathcal H\), then taking \(b=Ja\) gives \(\|a\|^2=0\).

For each fixed point, \(\delta_\rho/\sqrt{m_\rho}\) is a unit vector with \(J\)-eigenvalue \(+1\). For each representative \(\rho\in\mathcal P\), the two unit vectors
\[
u_\rho^+=\frac{\delta_\rho+\delta_{\rho^\#}}{\sqrt{2m_\rho}},
\qquad
u_\rho^-=\frac{\delta_\rho-\delta_{\rho^\#}}{\sqrt{2m_\rho}}
\tag{NI7}
\]
have eigenvalues \(+1\) and \(-1\), respectively. The full collection is an orthonormal basis, since it is the indicated invertible change of basis on each disjoint one- or two-point support. Thus
\[
\mathcal H=\mathcal H_+\mathbin{\widehat\oplus}\mathcal H_-,
\quad P_\pm=(I\pm J)/2,
\quad [a,a]=\|P_+a\|^2-\|P_-a\|^2,
\quad \dim\mathcal H_\pm=\kappa_\pm.
\tag{NI8}
\]
Here an infinite dimension means countably infinite Hilbert dimension. In particular, every distinct exchanged pair contributes exactly one negative direction with its original positive multiplicity weight.

## 2. The exact Cauchy evaluation map

For \(z\notin\mathcal Z\), put
\[
v_z(\rho)=\frac1{\rho-z}.
\tag{NI9}
\]
This is an element of \(\mathcal H\). Indeed, the terms with \(|\rho|\le2|z|+1\) are finite and have nonzero denominators, while on the remaining terms \(|\rho-z|\ge|\rho|/2\), so (NI3) applies. On every compact subset of \(\mathbb C\setminus\mathcal Z\), the same bound applies uniformly to the tail, and the finite part has its denominators uniformly separated from zero.

For \(z,w\in\mathcal U\), AG10–AG11 gives the exact identity
\[
\begin{split}
K_0(z,w)
&=\frac{L_g(w)+\overline{L_g(z)}}{w+\bar z-1}
=\sum_\rho m_\rho\overline{v_z(\rho^\#)}v_w(\rho)\\
&=\langle Jv_z,v_w\rangle_{\mathcal H}.
\end{split}
\tag{NI10}
\]
The scalar series converges absolutely by Cauchy–Schwarz in (NI5). Its summands are exactly those of the original rational test \(F_z^\#F_w\), with \(F_z(s)=(s-z)^{-1}\) and \(F^\#(s)=\overline{F(1-\bar s)}\). No zero is moved or removed in (NI10).

For a set \(E\subset\mathcal U\), let \(\mathbb C^{(E)}\) denote finite coefficient families, and define the linear map
\[
V_E:\mathbb C^{(E)}\longrightarrow\mathcal H,
\qquad V_Ec=\sum_{z\in E}c_zv_z.
\tag{NI11}
\]
For every finite family,
\[
\sum_{z,w\in E}\bar c_zK_0(z,w)d_w
=[V_Ec,V_Ed].
\tag{NI12}
\]
Thus any repetitions or linear relations in a chosen finite presentation are carried by the kernel of its actual evaluation map; they do not add signed directions.

## 3. Density, including its convergence and residue proof

Suppose that \(E\subset\mathcal U\) has an accumulation point inside \(\mathcal U\). This includes every nonempty open subset and every nondegenerate real interval contained in \((1,\infty)\). We prove
\[
\overline{\operatorname{span}\{v_z:z\in E\}}^{\mathcal H}
=\mathcal H.
\tag{NI13}
\]
Let \(h\in\mathcal H\) be orthogonal to all those vectors, and form its Cauchy transform
\[
\mathcal C_h(z)=\sum_{\rho\in\mathcal Z}
\frac{m_\rho\overline{h_\rho}}{\rho-z},
\qquad z\in\mathbb C\setminus\mathcal Z.
\tag{NI14}
\]
The series is absolutely convergent at every such point by Cauchy–Schwarz. More precisely, on a compact set contained in \(|z|\le M\), for \(R>2M+1\) its tail is bounded uniformly by
\[
\sum_{|\rho|>R}
\frac{m_\rho|h_\rho|}{|\rho-z|}
\le
2\left(\sum_{|\rho|>R}m_\rho|h_\rho|^2\right)^{1/2}
\left(\sum_{|\rho|>R}\frac{m_\rho}{|\rho|^2}\right)^{1/2}.
\tag{NI15}
\]
This tends to zero. The finite remaining part is holomorphic away from its listed poles. Thus (NI14) converges normally on compact subsets of \(\mathbb C\setminus\mathcal Z\) and defines a holomorphic function there.

This domain is connected. To see this directly, join any two points of the domain by a line segment. The compact segment meets at most finitely many points of the discrete zero set. Small pairwise disjoint discs about those points can be chosen to contain no other zero and neither endpoint. Replacing the portion of the segment in each disc by an arc on its boundary gives a path avoiding the zero set. Orthogonality gives \(\mathcal C_h=0\) on \(E\). The identity theorem, first at its accumulation point and then on the connected domain, gives \(\mathcal C_h=0\) everywhere in that domain.

Fix \(\rho_0\in\mathcal Z\). Choose a disc containing that zero and no other. All terms in (NI14) other than its \(\rho_0\)-term converge normally to a holomorphic function on the disc, by the same tail estimate and the finite denominators. Consequently
\[
\operatorname{Res}_{z=\rho_0}\mathcal C_h(z)
=-m_{\rho_0}\overline{h_{\rho_0}}.
\tag{NI16}
\]
The transform is zero on the punctured disc, so its residue is zero. Since the multiplicity is positive, \(h_{\rho_0}=0\). This holds at every zero, proving \(h=0\), and the Hilbert orthogonal-complement criterion proves (NI13).

This argument is a density statement for the actual infinite zero set. It does not substitute unrestricted finite interpolation for convergence, and it does not discard a tail of that set.

## 4. Density of all powers at one real pole

Fix an arbitrary real \(\sigma>1\), and retain every vector
\[
q_j(\rho)=\frac1{(\rho-\sigma)^{j+1}},\qquad j\ge0.
\tag{NI17}
\]
Write \(\delta=\sigma-1>0\). Because \(|\rho-\sigma|\ge\delta\),
\(\|q_j\|\le\delta^{-j}\|q_0\|\). Thus for \(|Y|<\delta\) the geometric expansion is an identity in \(\mathcal H\), with absolute convergence of the vector norm series:
\[
v_{\sigma+Y}=\sum_{j=0}^\infty Y^jq_j.
\tag{NI18}
\]
Pointwise the series is the usual geometric identity; convergence in \(\mathcal H\) and continuity of coordinate evaluations make it the same vector identity. If \(h\) is orthogonal to every \(q_j\), taking its inner product with (NI18) gives \(\mathcal C_h(\sigma+Y)=0\) on a disc. Equations (NI14)–(NI16) therefore imply \(h=0\). We have proved
\[
\overline{\operatorname{span}\{q_j:j\ge0\}}^{\mathcal H}
=\mathcal H.
\tag{NI19}
\]
Equivalently, \(\mathcal C_h^{(j)}(\sigma)=j!\langle h,q_j\rangle\); (NI18) supplies the derivative justification and the factor \(j!\).

The result remains true after deleting **any fixed finite initial set of powers**. More precisely, for every integer \(J_0\ge0\),
\[
\overline{\operatorname{span}\{q_j:j\ge J_0\}}^{\mathcal H}
=\mathcal H.
\tag{NI19a}
\]
An orthogonal vector makes every Taylor coefficient of \(\mathcal C_h\) at \(\sigma\) of degree at least \(J_0\) vanish. Thus that function agrees near \(\sigma\) with a polynomial of degree less than \(J_0\), with the zero polynomial understood when \(J_0=0\). The identity theorem extends this equality to \(\mathbb C\setminus\mathcal Z\). The polynomial has zero residue at every \(\rho\), so (NI16) again forces \(h=0\). No estimate on the polynomial at infinity is needed.

In the original notation of CK14–CK16, put \(Q_j(s)=(s-\sigma)^{-j-1}\). Taking the two convergent vector expansions in (NI10) gives
\[
C_{jk}=[q_j,q_k]
=Z_0((Q_j)^\#Q_k),\qquad
C_N=(C_{jk})_{0\le j,k\le N}.
\tag{NI20}
\]
There is no additional factorial or change of signs. In detail, for small independent variables \(X,Y\), use \(z=\sigma+\bar X\), \(w=\sigma+Y\); the first argument of the inner product is conjugate-linear, so the coefficient of \(X^jY^k\) is exactly \([q_j,q_k]\). The numerator and denominator are those of CK14 unchanged.

## 5. Exact negative and positive indices on dense test spans

For a Hermitian form on a complex vector space, its negative index means the supremum of the dimensions of finite-dimensional subspaces on which the form is negative definite. The positive index is defined with positive definite in place of negative definite. For a finite Hermitian matrix these are the numbers of strictly negative and strictly positive eigenvalues, counted with algebraic multiplicity, by unitary diagonalization.

First, every negative-definite finite-dimensional subspace of \(\mathcal H\) maps injectively under \(P_-\) to \(\mathcal H_-\). Indeed, a nonzero vector in the kernel would have \([a,a]=\|P_+a\|^2\ge0\), contradicting negative definiteness. Thus its dimension is at most \(\kappa_-\) when that number is finite. Conversely (NI7) supplies a negative orthonormal family of every finite size not exceeding \(\kappa_-\). The negative index of \(\mathcal H\) is therefore exactly \(\kappa_-\), and the identical argument with signs exchanged gives positive index \(\kappa_+\).

We prove that either index is retained on **any dense linear subspace** \(D\subset\mathcal H\). For the negative case, take \(n\) different negative unit vectors \(u_1,\ldots,u_n\) from (NI7). Define \(T:\mathbb C^n\to\mathcal H\) by \(Tx=\sum_i x_i u_i\). Then \(T\) is an isometry and \([Tx,Tx]=-\|x\|^2\). By density choose \(d_i\in D\) with
\(\|d_i-u_i\|<1/(4\sqrt n)\), and set \(Dx=\sum_i x_i d_i\), using the same letter for this finite synthesis map. Its error \(E=D-T\) has operator norm less than \(1/4\), since
\(\|Ex\|\le\sum_i|x_i|\|d_i-u_i\|<\|x\|/4\).
Using \(\|J\|=1\), we obtain
\[
[Dx,Dx]\le
\bigl(-1+2\|E\|+\|E\|^2\bigr)\|x\|^2
<-\frac7{16}\|x\|^2\quad(x\ne0).
\tag{NI21}
\]
Thus the synthesis map is injective and its image is an \(n\)-dimensional negative-definite subspace of \(D\). This proves the lower bound for every finite \(n\le\kappa_-\); the upper bound follows from its inclusion in \(\mathcal H\). For positive unit vectors, the same expansion gives a lower bound \((1-2\|E\|-\|E\|^2)\|x\|^2>7\|x\|^2/16\), proving the positive statement too.

Finally, the radical of the form restricted to a dense subspace is zero. If \(a\in D\) satisfies \([a,b]=0\) for all \(b\in D\), continuity gives that identity for every \(b\in\mathcal H\). Taking \(b=Ja\) then forces \(a=0\). This does not say that each finite matrix cut out of the subspace is nonsingular; a finite restriction can have its own radical.

## 6. The index theorem for the actual kernel and coefficient tower

Combining (NI12)–(NI13), (NI19)–(NI21) proves the unconditional identity
\[
\boxed{
\begin{split}
\sup_{\substack{n\ge1\,,\ z_1,\ldots,z_n\in E}}
n_-\bigl((K_0(z_i,z_j))_{i,j=1}^n\bigr)
&=\#\mathcal P,\\
\sup_{N\ge0} n_-(C_N)&=\#\mathcal P.
\end{split}}
\tag{NI22}
\]
Here \(E\) is any subset specified in Section 3, \(\sigma>1\) in the second line is arbitrary, and \(n_-\) counts strictly negative eigenvalues. To justify directly the finite matrix passage, the finitely many vectors \(d_i\) used in (NI21) involve a common finite union of Cauchy poles, or finitely many powers up to a common maximum \(N\). Their negative Gram form is the pullback of the corresponding finite matrix by their coefficient synthesis map. Its injectivity on the negative subspace proves that matrix has at least \(n\) negative eigenvalues. Conversely, any negative eigenspace of a finite matrix maps injectively by its actual evaluation map into a negative-definite subspace of \(\mathcal H\), using (NI12) or (NI20). This proves both inequalities, including presentations with redundant coefficients.

The same proof gives
\[
\sup_{\substack{n\ge1\,,\ z_1,\ldots,z_n\in E}}
n_+\bigl((K_0(z_i,z_j))\bigr)
=\sup_{N\ge0}n_+(C_N)=\kappa_+.
\tag{NI23}
\]
Using the strengthened density (NI19a), the exact corresponding statement for every fixed tail is
\[
\sup_{N\ge J_0}n_-\bigl((C_{jk})_{J_0\le j,k\le N}\bigr)=\kappa_-,
\qquad
\sup_{N\ge J_0}n_+\bigl((C_{jk})_{J_0\le j,k\le N}\bigr)=\kappa_+.
\tag{NI23a}
\]
Indeed, repeat the construction (NI21) with the dense span in (NI19a); the finite list of approximating powers has a common largest index \(N\). This proves both identities with precisely the same upper bound from (NI8).
For \(\kappa_-<\infty\), some finite matrix attains that entire negative index. In the coefficient tower there is an \(N_0\) such that \(n_-(C_N)=\kappa_-\) for all \(N\ge N_0\): the lower-bound construction supplies one \(N_0\), larger spaces retain that negative subspace, and (NI22) supplies the upper bound. For \(\kappa_-=\infty\), the integers \(n_-(C_N)\) are unbounded. Neither statement supplies a computable universal finite cutoff deciding RH.

The original critical line is exactly the fixed set of (NI2). Consequently (NI22) strengthens CK13 and CK17 from the zero-index equivalence to the exact index:
\[
\mathrm{RH}\quad\Longleftrightarrow\quad\kappa_-=0
\quad\Longleftrightarrow\quad
n_-(C_N)=0\text{ for every }N\ge0.
\tag{NI24}
\]
All equalities concern the actual zeta zeros. They do not postulate an off-line zero or infer the absence of one. In particular, the positive real diagonal from HA24–HA26 does not obscure an existing negative direction: if \(\kappa_->0\), it is detected by an off-diagonal finite Gram matrix even when its poles are restricted to any fixed nondegenerate real interval in \((1,\infty)\).

## 7. Multiplicity and the complete local trace radical

For each actual zero keep its original local algebra and parameter
\[
A_\rho=\mathbb C[\epsilon_\rho]/(\epsilon_\rho^{m_\rho}),
\qquad \epsilon_\rho=s-\rho.
\tag{NI25}
\]
Multiplication by \(a_0+a_1\epsilon_\rho+\cdots+a_{m_\rho-1}\epsilon_\rho^{m_\rho-1}\), in the original ordered monomial basis, is triangular with every diagonal entry equal to \(a_0\). Its multiplication trace is therefore exactly \(m_\rho a_0\). Under the original involution, the Taylor coefficients at a reflected zero satisfy
\[
\left(\sum_k a_{\rho^\#,k}\epsilon_{\rho^\#}^k\right)^\#
\text{ at }\rho
=\sum_k(-1)^k\overline{a_{\rho^\#,k}}\epsilon_\rho^k.
\tag{NI26}
\]
The factor \((-1)^k\) follows from
\(1-\overline{\rho+\epsilon_\rho}=\rho^\#-\bar\epsilon_\rho\). In particular, the constant-value involution is \(a_\rho\mapsto\overline{a_{\rho^\#}}\).

To retain all jets even for an infinite zero set, define
\[
\mathcal A_{\rm tr}
=\left\{a\in\prod_{\rho\in\mathcal Z}A_\rho:
(a_\rho(0))_\rho\in\mathcal H\right\},\quad
\pi(a)_\rho=a_\rho(0),\quad
\mathcal N=\prod_{\rho\in\mathcal Z}(\epsilon_\rho)A_\rho.
\tag{NI27}
\]
No restriction is imposed on the higher coefficients. This is a complex algebra closed under (NI26): since \(m_\rho\ge1\), every \(x\in\mathcal H\) has \(\sup_\rho|x_\rho|\le\|x\|\), and hence pointwise multiplication obeys \(\|xy\|\le\|x\|\|y\|\). An identity element is not asserted for this algebra. Its evaluation has the exact split sequence
\[
0\longrightarrow\mathcal N\longrightarrow\mathcal A_{\rm tr}
\xrightarrow{\ \pi\ }\mathcal H\longrightarrow0,
\qquad
\iota(x)_\rho=x_\rho\cdot1_{A_\rho},\quad\pi\iota=I.
\tag{NI28}
\]
Both \(\pi\) and \(\iota\) preserve addition, scalar multiplication, multiplication, and the indicated involutions. The quotient retains exactly the weighted value space (NI5), while the kernel retains every higher jet. Define on \(\mathcal A_{\rm tr}\)
\[
\mathfrak T(a,b)
=\sum_\rho\operatorname{Tr}_{A_\rho}
\bigl(M_{(a^\#b)_\rho}\bigr)
=\sum_\rho m_\rho\overline{a_{\rho^\#}(0)}b_\rho(0)
=[\pi a,\pi b].
\tag{NI29}
\]
The sum is absolutely convergent by Cauchy–Schwarz. Equation (NI29) is not a claim that the individual unpaired trace sum exists for every \(a\). Its radical is exactly \(\mathcal N\): containment is immediate, and if the form vanishes against every \(b\), the section in (NI28) and nondegeneracy of (NI6) imply \(\pi a=0\). If multiplicities are unbounded, the product ideal \(\mathcal N\) need not have a common nilpotence exponent, so it is not called a nilpotent ideal here. Each of its local factors is the specified nilpotent ideal in (NI25).

The exact algebraic description, without any bounded-multiplicity assumption, is
\[
\begin{split}
\sqrt{(0)}_{\mathcal A_{\rm tr}}
&=\{a\in\mathcal N:\text{there exists }r\ge1
\text{ such that }a_\rho^r=0\text{ for every }\rho\},\\
\mathcal N^r&=\prod_\rho(\epsilon_\rho^r)A_\rho,
\qquad \bigcap_{r\ge1}\mathcal N^r=0,
\qquad \mathcal A_{\rm tr}\cong
\varprojlim_r\mathcal A_{\rm tr}/\mathcal N^r.
\end{split}
\tag{NI29a}
\]
The first equality follows because powers in the product are computed coordinatewise, and any nilpotent has zero constant at every coordinate. For the second equality, multiplication gives one containment. Conversely, for \(r\ge2\), any tuple divisible coordinatewise by \(\epsilon_\rho^r\) is the product of \(r-1\) copies of the tuple \((\epsilon_\rho)_\rho\) and a tuple in \(\mathcal N\): shift each original coefficient down by \(r-1\) powers, retaining a factor \(\epsilon_\rho\). Every factor lies in \(\mathcal N\) since its constant coordinates vanish. The case \(r=1\) is its definition. The intersection is zero since each \(m_\rho\) is finite. Finally, a compatible inverse-limit element determines each local component when \(r\ge m_\rho\), and its constant vector is already the element of \(\mathcal H\) specified at level \(r=1\). These reconstructed components give an element of \(\mathcal A_{\rm tr}\) and the inverse to the displayed map. Thus the trace radical has an exact separated, complete filtration even when it differs from the nilradical. This calculation does not assert any uniform bound, or lack of a uniform bound, for the actual zeta multiplicities.

Every rational Cauchy test and every \(Q_j\) has a well-defined Taylor class in each \(A_\rho\). These classes belong to \(\mathcal A_{\rm tr}\) by (NI9) and (NI17), and applying \(\pi\) gives exactly \(v_z\) and \(q_j\). This proves the full map from the original multiple-zero jet algebras to (NI22), including its kernel. Multiplicity supplies the weight \(m_\rho\); the local trace radical accounts for why a multiple zero does not by itself add further signed value directions. The retained higher jets can still have nonzero heat responses, as calculated in AG17 and HA21–HA22; (NI29) states their exact time-zero trace behavior only.

## 8. The complete supported arithmetic receiver

Let \(\mathscr L\) be the original finite support semilattice with top \(1_{\mathscr L}\), and let \(W_{\mathscr L}=\mathbb C^{\mathscr L}\) have basis \(\mathbf e_\lambda\). This symbol is distinct from \(L_g(s)\). Take \(F,G\) in either finite test span of Sections 2 and 4, and put \(A=F^\#G\). Its poles lie strictly outside the critical strip and \(A=O(s^{-2})\), so the proved extension AG14–AG16 applies. With the unchanged arithmetic functionals \(P_{\rm fin}\) and \(A_\infty\), it gives
\[
\begin{split}
\boldsymbol B_{\mathscr L}(F,G)
&=(A(0)+A(1))\mathbf e_{1_{\mathscr L}}
+A(0)\sum_{\lambda\ne1_{\mathscr L}}\mathbf e_\lambda,\\
\boldsymbol D_{\mathscr L}(F,G)
&=(P_{\rm fin}(h_A)-A_\infty(h_A))\mathbf e_{1_{\mathscr L}}
+A(0)\sum_{\lambda\ne1_{\mathscr L}}\mathbf e_\lambda,\\
\boldsymbol B_{\mathscr L}(F,G)-\boldsymbol D_{\mathscr L}(F,G)
&=[\operatorname{ev}F,\operatorname{ev}G]\,\mathbf e_{1_{\mathscr L}}.
\end{split}
\tag{NI30}
\]
Here \(\operatorname{ev}F=(F(\rho))_\rho\), and
\(A(0)=\overline{F(1)}G(0)\),
\(A(1)=\overline{F(0)}G(1)\). Thus both endpoints and every lower coordinate are explicitly present. Their common lower-coordinate values cancel only in the displayed **difference**, as required by the original full identity.

The precise scalar and vector maps are
\[
\begin{gathered}
j_{\rm top}:\mathbb C\longrightarrow W_{\mathscr L},\quad
x\longmapsto x\mathbf e_{1_{\mathscr L}},\qquad
\pi_{\rm top}\left(\sum x_\lambda\mathbf e_\lambda\right)=x_{1_{\mathscr L}},\\
\pi_{\rm top}j_{\rm top}=I,\quad
\ker\pi_{\rm top}=\operatorname{span}\{\mathbf e_\lambda:\lambda\ne1_{\mathscr L}\},\\
\Sigma_{\mathscr L}\left(\sum x_\lambda\mathbf e_\lambda\right)=\sum x_\lambda,
\quad \ker\Sigma_{\mathscr L}=\{x:\sum x_\lambda=0\}.
\end{gathered}
\tag{NI31}
\]
Both \(\pi_{\rm top}\) and \(\Sigma_{\mathscr L}\) recover the scalar form from the difference in (NI30), because that difference lies in the image of \(j_{\rm top}\). They have the displayed kernels, which differ whenever \(\mathscr L\) has a lower label: for such a label, \(\mathbf e_\lambda\) belongs to \(\ker\pi_{\rm top}\) and not to \(\ker\Sigma_{\mathscr L}\). For a singleton label set both maps coincide. In the case with lower labels, their agreement on the difference does not identify them on the separate boundary or arithmetic terms. The lower-coordinate pairing \(A(0)\) alone is generally not Hermitian and is not assigned a negative index.

For completeness, a top-preserving map of support labels \(f:\mathscr L\to\mathscr M\) induces the exact linear pushforward \(f_*\mathbf e_\lambda=\mathbf e_{f(\lambda)}\). Writing
\(n_\mu=\#\{\lambda\ne1_{\mathscr L}:f(\lambda)=\mu\}\), direct substitution into (NI30) yields
\[
\begin{split}
f_*\boldsymbol B_{\mathscr L}
&=(A(0)+A(1))\mathbf e_{1_{\mathscr M}}
+A(0)\sum_\mu n_\mu\mathbf e_\mu,\\
f_*\boldsymbol D_{\mathscr L}
&=(P_{\rm fin}(h_A)-A_\infty(h_A))\mathbf e_{1_{\mathscr M}}
+A(0)\sum_\mu n_\mu\mathbf e_\mu,\\
f_*(\boldsymbol B_{\mathscr L}-\boldsymbol D_{\mathscr L})
&=[\operatorname{ev}F,\operatorname{ev}G]\mathbf e_{1_{\mathscr M}}.
\end{split}
\tag{NI32}
\]
Thus even labels that map into the target top contribute with their full counts to both terms, and the exact signed trace is preserved. This is a statement about the indicated linear support map, not an assertion that every such label map has some additional geometric origin. Supported zero and the unsupported element \(\tau\) remain distinct throughout; no numerical prime norm for supported zero is inserted in these formulas.

Equations (NI22), (NI28)–(NI29), and (NI30)–(NI32) together determine the signed index, the complete local trace kernel, and the full supported arithmetic map. They identify the surviving negative directions as anti-invariant values on actual reflected zero pairs. They do not eliminate such directions by a change of representation or by the vanishing of a nilpotent trace.

## Source use and proof scope

The zero-count and entire-function input is AG1–AG8; the actual global kernel is AG10–AG11 and CK1–CK2; the coefficient conventions are CK14–CK16. The complete supported explicit formula and its rational-test extension are AG12–AG16 and HA5–HA14. The original human explicit-formula source remains Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Appendix II, Theorem 6, with original author TeX and all programme conventions retained in [SZW19–SZW38](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/3c022a0adde0a6aa3d8fc8e43ef42795d88e44b0/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md). The heat-response reference uses Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5, through the original source locators recorded in AG1 and HA1. No additional source discovery, historical priority claim, or positivity assumption enters this derivation.
