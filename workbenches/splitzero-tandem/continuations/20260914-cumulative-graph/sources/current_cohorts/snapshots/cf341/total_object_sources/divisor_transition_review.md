# Divisor transitions for the original total object

This bounded audit retains \(g=2\xi\), \(D=-x\partial_x\), \(Q=\mathscr B/\Theta V\), and the original balanced sheaf \(\mathcal M\to\mathcal N=\mathcal O/(g)\). No offcritical root or new RH theorem is asserted. The assignment was to derive the transitions for finite invariant divisors \(h\mid h'\mid g\), including full multiplicities, inverse Mellin sources, tensor packets, and metrics. Only this report was written.

Read source pins, relative to the workspace:

- BK: work/rh_counterfactual_20260913/shared_thread_audit/segment29_40/original_balanced_kernel.tex, lines 129–187 (BK.8–11), 238–259 (BK.15–16), 264–299 (BK.17–20), 368–396 (BK.24).
- OCQ: work/rh_counterfactual_20260913/continuation2/coherent_comparison/original_coherent_comparison.tex, lines 38–117 (OCQ.2–7), 204–218 (OCQ.13), 390–415 (OCQ.26–27), 458–465 (OCQ.30), 537–564 (OCQ.34–35).
- Original source injection: work/rh_counterfactual_20260913/shared_thread_audit/segment41_54/conormal_source_header.tex, lines 89–119.
- Actual metric and cyclic observation: work/rh_counterfactual_20260913/continuation2/combined_arithmetic_restriction.tex, lines 1–38 (CA1–3), 60–79 (CA6), 91–116 (CA8–10).

An independent subagent checked the metric and residue examples. No global source, browser, or external reference was used.

## 1. Two directions, with different maps

Let \(A=\mathbb C[s]\), let \(h,h'\) be the actual monic polynomials of finite effective subdivisors, and keep
\[
h'=rh,\qquad E_h=A/(h),\quad E_{h'}=A/(h').
\]
There are canonical \(A\)-linear maps
\[
\pi_{h',h}:E_{h'}\twoheadrightarrow E_h,\quad[P]_{h'}\mapsto[P]_h,
\qquad
\iota_{h,h'}:E_h\hookrightarrow E_{h'},\quad[P]_h\mapsto[rP]_{h'}.
\tag{DT1}
\]
The first is a unital algebra map; the second generally is only a module map. Its well-definedness is \(rh=h'\), and its injectivity follows by cancelling \(r\) in \(rP=rhB\). Their composites are
\[
\pi\iota=M_{[r]_h},\qquad \iota\pi=M_{[r]_{h'}}.
\tag{DT2}
\]
They are generally not identity maps. There is an exact sequence
\[
0\to E_h\xrightarrow{\times r}E_{h'}\to E_r\to0,
\tag{DT3}
\]
with last map reduction modulo \(r\). Separately, the kernel of \(\pi:E_{h'}\to E_h\) is \((h)/(h')\), identified with \(E_r\) by multiplication by \(h\). Every removed multiplicity is retained.

For \(h''=r'h'\), injections compose by \(\times(r'r)\) and projections by reduction. Divisibility therefore gives a covariant directed system of modules using \(\iota\), and a contravariant inverse system of algebras using \(\pi\). Reversing either direction or identifying the two maps changes the object.

## 2. Local units, nilpotents, and overlap

At \(\rho\), retain \(z=s-\rho\) and
\[
g=u(z)z^m,\quad h=a(z)z^n,\quad h'=a'(z)z^{n'},\quad
r=b(z)z^{n'-n},\quad a'=ba,
\tag{DT4}
\]
with all units nonzero at zero and \(0\le n\le n'\le m\). The injection multiplies by the actual \(b(z)z^{n'-n}\); its image is the top \(n\) nilpotent levels. The projection retains Taylor levels below \(n\). CRT splits distinct centers, not depth at one center.

In particular \(O/(z^{n'})\) is not \(O/(z^n)\oplus O/(z^{n'-n})\) when \(0<n<n'\): the proposed sum is killed by \(z^{\max(n,n'-n)}\), while the first module has nilpotence order \(n'\). The projection \(O/(z^{n'})\to O/(z^n)\) has no \(O\)-linear section. Such a section would take \(1\) to \(v\equiv1\pmod{z^n}\), whereas \(z^n v\ne0\pmod{z^{n'}}\).

For overlapping divisors \(h_1,h_2\), put \(d=\gcd(h_1,h_2)\), \(l=\operatorname{lcm}(h_1,h_2)\). The exact quotient-map sequence is
\[
0\to E_l\to E_{h_1}\oplus E_{h_2}
\xrightarrow{(a,b)\mapsto a-b}E_d\to0.
\]
The corresponding injection-map sequence is
\[
0\to E_d
\xrightarrow{x\mapsto((h_1/d)x,-(h_2/d)x)}
E_{h_1}\oplus E_{h_2}
\xrightarrow{(a,b)\mapsto(l/h_1)a+(l/h_2)b}E_l\to0.
\tag{DT5}
\]
For the second, the composition vanishes; the complementary factors are coprime, proving surjectivity, and dimensions plus injectivity of the first map prove exactness. For the first, \((h_1)\cap(h_2)=(l)\) gives injectivity, and congruent representatives modulo \(d\) can be solved by Bézout, proving exactness. Direct-sum CRT occurs only for \(d=1\).

## 3. Original inverse Mellin sources and theta injections

Keep \(\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2}\), \(b_*=\Theta\phi_*\), and \(\mathcal Mb_*=g\). The proved Euler inverses in BK.8–11 give the unique \(F_h\in\mathscr B\) with
\[
h(D)F_h=b_*,\qquad \mathcal MF_h=g/h.
\tag{DT6}
\]
Existence follows since all required jets of \(g\) vanish; injectivity of every \(D-\rho\) gives uniqueness. Hence
\[
\boxed{F_h=r(D)F_{h'},\qquad g/h=r(g/h').}
\tag{DT7}
\]
Indeed both sides solve \(h(D)F=b_*\). No asymptotic or multiplicity truncation is involved.

For **every** finite divisor, including partial depths, define
\[
\tau_h:E_h\longrightarrow Q[h(D)],\qquad
[P]_h\longmapsto[P(D)F_h].
\tag{DT8}
\]
Changing \(P\) by \(hB\) changes the representative by the original theta boundary \(\Theta(B(D)\phi_*)\). The BK.11 boundary homomorphism sends this class to \([P]_h\), because \(H_{P(D)\phi_*}=P\). Since \(j_hg=0\), BK.11 proves \(\tau_h\) is an isomorphism onto \(Q[h(D)]\). No inverse of a truncated \(g/h\) jet is needed.

The exact two transitions are
\[
\boxed{\tau_{h'}\iota_{h,h'}=\tau_h,\qquad
r(D)\tau_{h'}=\tau_h\pi_{h',h}.}
\tag{DT9}
\]
The first is the inclusion \(Q[h]\subset Q[h']\); the second is multiplication \(Q[h']\to Q[h]\). On literal polynomial sources \(\mathcal T_hP=P(D)F_h\), the first uses \(\times r\) and satisfies \(\mathcal T_{h'}(rP)=\mathcal T_hP\). On relations it sends \(hB\) to \(h'B\), preserving exactly the theta primitive \(B(D)\phi_*\).

## 4. Coherent embedding and the unit obstruction

The coherent map corresponding to \(\tau_h\) is
\[
\mu_h:\mathcal O/(h)\xrightarrow{\sim}\mathcal N[h],
\qquad[P]_h\mapsto[(g/h)P]_g.
\tag{DT10}
\]
In (DT4) it is multiplication by the **full unit** \(u/a\) and \(z^{m-n}\), with image \(z^{m-n}O/z^mO\), of length \(n\). Thus it is injective at every depth, and
\[
\mu_{h'}\iota_{h,h'}=\mu_h
\]
by \((g/h')r=g/h\).

This differs from the jet observation back into \(E_h\):
\[
J_h\tau_h=M_{\upsilon_h},\qquad \upsilon_h=j_h(g/h).
\tag{DT11}
\]
The original normalized formula \(\sigma_h=\tau_hM_{\upsilon_h^{-1}}\) works exactly when \(h\) includes the full actual multiplicity at each included center. At (DT4), \(\upsilon_h\) has order \(m-n\) modulo \(z^n\), hence is a unit precisely for \(n=m\). If \(n<m\), its rank and nullity are
\[
\operatorname{rank}M_{\upsilon_h}=\max(2n-m,0),\qquad
\dim\ker M_{\upsilon_h}=\min(n,m-n).
\tag{DT12}
\]
For example \(g=uz^2,h=z\) gives \(\upsilon_h=0\), although \(\mu_h(1)=[uz]\ne0\) and \(\tau_h\ne0\). Extending the unit inverse or a claimed invertible weighted cyclic factor to all effective subdivisors is therefore invalid. The original CA1–3 formulas assumed complete quartet multiplicities and are not contradicted within that scope.

For full-depth divisors, enlargement adds disjoint centers and \(\gcd(h,r)=1\). The normalized transition is
\[
J^{\rm norm}_{h,h'}=
M_{\upsilon_{h'}}\iota_{h,h'}M_{\upsilon_h^{-1}}.
\tag{DT13}
\]
It satisfies \(\sigma_{h'}J^{\rm norm}_{h,h'}=\sigma_h\). On old CRT factors \(\upsilon_h=r\upsilon_{h'}\), so it is the identity; on new factors it is zero. It is CRT extension by zero into an idempotent corner, generally not a unital algebra embedding into the larger algebra. It is different from the unnormalized \(\times r\).

## 5. A directed sheaf system retaining the kernel and support

Let \(U\) be the specified invariant offcritical open set. Include \(h=1\) for the empty divisor. Finite invariant effective subdivisors are directed by least common multiple, taking maximum depth at each center. This remains a divisor of \(g\).

Set \(\mathcal N_h=\mathcal N[h]\), with the inclusions above. At each actual zero some finite invariant divisor includes its full multiplicity, so the colimit stalk is the whole stalk of \(\mathcal N_U\). Away from zeros all these stalks are zero. Therefore
\[
\varinjlim_h\mathcal N_h=\mathcal N_U
\tag{DT14}
\]
as sheaves. If \(U\) has no zeros, the result is simply zero.

For the original \(\beta:\mathcal M_U\to\mathcal N_U\) define
\[
\mathcal M_h=\beta^{-1}(\mathcal N_h).
\]
The exact preimage sequences and their canonical OCQ.6–7 splitting are
\[
0\to\mathcal K_U\to\mathcal M_h\to\mathcal N_h\to0,\qquad
\mathcal M_h=\mathcal K_U\oplus j(\mathcal N_h),\qquad
\varinjlim_h\mathcal M_h=\mathcal M_U.
\tag{DT15}
\]
Transitions retain the identity on \(\mathcal K_U\) and inclusion on the torsion summand. Replacing the preimage nodes by finite \(\mathcal N_h\) alone would remove the original nonzero kernel and its derived observations. Any retained diagonal or preimage extension is transported by its literal pullback along \(\mathcal N_h\hookrightarrow\mathcal N_U\), not by a claim that the kernel disappears.

The split-support extension of OCQ.34 sends external \(\tau\) to external \(\tau\), and a supported kernel to its supported zero. These are distinct fibers throughout.

This is a **sheaf colimit**. If the zero set in an open set is infinite, the global section \([1]\) has nonzero germs at all zeros and belongs to no single finite-support node. Finite global packet sections form their direct sum, while sheaf gluing permits locally finite sections. Thus one must not identify the global finite direct limit with all global sections merely by (DT14).

## 6. Both degrees of the derived transitions

For \(C_h=[A\xrightarrow{h}A]\) in degrees \(-1,0\), the lifts are
\[
C_h\to C_{h'}:\ (f^{-1},f^0)=(1,r),\qquad
C_{h'}\to C_h:\ (f^{-1},f^0)=(r,1).
\tag{DT16}
\]
Their chain identities are \(h'=rh\). Tensoring with \(Q\), the first induces inclusion \(Q[h]\to Q[h']\) in degree \(-1\) and \(\times r:Q/hQ\to Q/h'Q\) in degree zero. The second induces \(\times r:Q[h']\to Q[h]\) in degree \(-1\) and reduction \(Q/h'Q\to Q/hQ\) in degree zero.

Over \(O\), each kernel complex \([K\xrightarrow h K]\) contracts by the actual inverse of \(h\) on \(K\). These statements concern derived tensor; they do not remove the different derived Hom classes retained in OCQ.15–25.

## 7. Full tensor transitions and exact cyclic collision orders

The natural tensor transition is
\[
\iota_{h,h'}^{\otimes k}:E_h^{\otimes k}\hookrightarrow E_{h'}^{\otimes k},
\quad P(\boldsymbol s)\mapsto R(\boldsymbol s)P(\boldsymbol s),
\quad R=\prod_{i=1}^k r(s_i).
\tag{DT17}
\]
It commutes with every \(s_i\), total \(S=\sum_i s_i\), and permutations. Tensoring (DT9) gives exact compatibility with the ordered original theta quotient and sources \(F_h^{\otimes k}\).

For a general \(h=\prod_\rho(s-\rho)^{n_\rho}\), the annihilator of \(1^{\otimes k}\) under total \(S\) is
\[
\boxed{\chi_{h,k}(S)=\prod_{\lambda\ {\rm distinct}}
(S-\lambda)^{L_\lambda},\quad
L_\lambda=\max_{\rho_1+\cdots+\rho_k=\lambda}
\left(1+\sum_i(n_{\rho_i}-1)\right).}
\tag{DT18}
\]
In the ordered tuple block, \(s_i=\rho_i+z_i\), \(z_i^{n_{\rho_i}}=0\). The total nilpotent \(\sum_i z_i\) has exact order \(1+\sum_i(n_{\rho_i}-1)\): the last nonzero power has coefficient
\[
\frac{(\sum_i(n_{\rho_i}-1))!}{\prod_i(n_{\rho_i}-1)!}\ne0
\]
on \(\prod_i z_i^{n_{\rho_i}-1}\), and all terms in the next power vanish. The cyclic annihilator over tuple blocks is the least common multiple, proving (DT18). Colliding sums use the maximum order, not a sum of multiplicities or duplicate product factors.

One has \(\chi_{h,k}\mid\chi_{h',k}\). Tensor reduction gives the canonical quotient \(\mathbb C[S]/\chi_{h',k}\to\mathbb C[S]/\chi_{h,k}\). But the tensor injection sends the old generator to \(R\), and \(R\) need not be a polynomial in \(S\) in the larger packet:

- If \(h=z^2,h'=z^3,k=2\), the image is \(xy\) in \(\mathbb C[x,y]/(x^3,y^3)\). A polynomial in \(x+y\) with that value would require degree-two part \(c(x+y)^2=cx^2+2cxy+cy^2=xy\), impossible.
- If \(h=(s-a)(s-c)\), \(h'=h(s-b)\), \(a+c=2b\), and the centers are distinct, then \(R=(s_1-b)(s_2-b)\) is nonzero at \((a,c)\) and zero at \((b,b)\). These tuples have the same total \(S\).

There is a source-specific version for full invariant packets enlarged by a disjoint orbit: old \((\rho,1-\rho)\) and new \((\sigma,1-\sigma)\) both have sum \(1\), but \(R\) is nonzero at the former and zero at the latter. This describes any such actual nesting if present, without asserting any offcritical zero exists.

Consequently the compatible directed transport nodes are the **full tensor packets**. A cyclic subobject must retain its chosen generator: its image is the cyclic submodule generated by the transported \(R\), not automatically the distinguished submodule generated by \(1\). A formal injection \(\times(\chi_{h',k}/\chi_{h,k})\) between cyclic quotient modules does not by itself intertwine the original arithmetic observations.

## 8. Exact metric compatibility and exact failures

The original one-factor weights satisfy, with \(s=1/2+iu\),
\[
w_h(u)=\frac{|(g/h)(s)|^2}{2\pi}
=|r(s)|^2w_{h'}(u).
\]
Hence
\[
\|P\|_h^2=\|rP\|_{h'}^2,\qquad
H_{h,N}=S_r^*H_{h',N+\deg r}S_r.
\tag{DT19}
\]
The actual \(\times r\) source map is an exact isometry with the degree shift. It preserves the original masses through this multiplication rather than an unauthorized normalization.

The one-variable quotient metrics also obey
\[
\iota^*G_{h',N+\deg r}\iota=G_{h,N}.
\tag{DT20}
\]
Indeed every target lift is \(rP+h'B=r(P+hB)\), and its degree bound is exactly the original bound shifted by \(\deg r\). Thus entire affine fibers correspond, and the minima coincide using (DT19). Equal unshifted degree bounds or the identity map on coefficients do not have this property.

Unrelated coefficient metrics have no such functoriality. For \(h=s-2,h'=(s-2)(s-3)\), the vector \(1\) maps to \(s-3\), with Euclidean coefficient norms \(1,\sqrt{10}\). This example does not replace the original metric; it disproves inferring an isometry from an unspecified positive metric.

On full ordered tensor sources,
\[
\int|P(\boldsymbol s)|^2\prod_iw_h(u_i)d\boldsymbol u
=\int|R(\boldsymbol s)P(\boldsymbol s)|^2
\prod_iw_{h'}(u_i)d\boldsymbol u.
\tag{DT21}
\]
Rectangular degree flags and tensor products of the one-variable quotient metrics inherit the tensor product of (DT20). For arbitrary multivariate flags, however, the target affine fiber can be larger than the image of the source fiber, so quotient norm equality requires proof.

Here is a strict counterexample with a product moment metric. Take \(h=z,h'=z^2,k=2\), so \(R=xy\). Let each variable have probability distribution \(\mu=N(1,1)\). Equip the old constant source with the metric inherited by \(\times xy\); its squared norm is
\[
\int x^2y^2\,d\mu(x)d\mu(y)=4.
\]
In the target total-degree-\(\le2\) space, modulo \((x^2,y^2)\), the target fiber is \(xy+a x^2+b y^2\). Using
\(\mathbb E X=1,\mathbb E X^2=2,\mathbb E X^3=4,\mathbb E X^4=10\),
its relation Gram and cross vector are
\[
\begin{pmatrix}10&4\\4&10\end{pmatrix},\qquad(4,4).
\]
Thus the minimizing lift is \(xy-\frac27(x^2+y^2)\), with squared norm
\[
4-\frac{16}{7}=\frac{12}{7}<4.
\tag{DT22}
\]
The source embedding is exactly isometric, while the quotient norm drops because new relation directions are allowed. The rectangular degree-\(\le1\) bound in each variable excludes these relation directions and retains norm \(4\). This is an exact counterexample to arbitrary flag-level quotient functoriality, not an assertion about the sign of the actual arithmetic moments.

Most importantly, (DT21) cannot be restricted to the original total-\(S\) polynomial sources without the cyclic compatibility that fails in section 7.

## 9. Residue, trace, and reflection

For the bilinear residue pairing
\[
B_h(f,x)=\sum_{\rho\mid h}\operatorname{Res}_\rho\frac{fx}{h}\,ds,
\]
the exact identities are
\[
B_{h'}(\iota f,x)=B_h(f,\pi x),\qquad
B_{h'}(\iota f,\iota x)=B_h(f,rx).
\tag{DT23}
\]
These follow by cancelling the actual ratio \(r\) in \(h'=rh\). Thus the injection is not a residue isometry: \(h=z,h'=z^2\) gives \(B_h(1,1)=1\), whereas \(B_{h'}(z,z)=0\).

For the actual coherent embedding \(\mu_h\), the ambient pairing restricts to
\[
\operatorname{Res}\frac{(g/h)f\,(g/h)x}{g}\,ds
=\operatorname{Res}\frac{g}{h^2}fx\,ds.
\tag{DT24}
\]
At \(g=uz^m,h=az^n\), the retained coefficient is \(u/a^2\), and the possible pole order is \(2n-m\). Its rank is \(\max(2n-m,0)\), with radical dimension \(\min(n,m-n)\); if the pole order is positive, its first that-many powers form a nondegenerate anti-triangular block with nonzero unit coefficient. Thus the ambient perfect residue pairing can become degenerate on partial torsion layers.

For ordinary multiplication trace,
\[
T_h(f,x)=\operatorname{Tr}_{E_h}M_{fx}
=\sum_\rho n_\rho f(\rho)x(\rho),
\]
one instead has
\[
T_{h'}(\iota f,x)=T_h(f,r\pi x),\qquad
T_{h'}(\iota f,\iota x)=T_h(f,r^2x).
\tag{DT25}
\]
At roots of \(r\) both sides vanish; where \(r\ne0\), the multiplicity is unchanged, proving the identity. The actual OCQ.30 form uses the multiplicities of \(g\); these cannot be freely replaced by a subdivisor's truncated depths. Nilpotent vectors can have zero ordinary trace observations while retaining nonzero coherent classes and residue duals.

For the original reflected operation, an invariant monic divisor obeys
\[
h^\dagger(s)=\overline{h(1-\bar s)}
=(-1)^{\deg h}h(s),\qquad
r^\dagger=(-1)^{\deg r}r.
\tag{DT26}
\]
Each transformed monic factor contributes its minus sign. Full quartet divisors have degrees divisible by four, hence sign \(+1\); other cases require retaining the displayed scalar. The reflected/Hermitian versions of (DT23)–(DT25) follow by inserting this exact dagger, not by assuming every injection is unitary.

## Conclusion for assembly

Use multiplication-by-ratio injections for finite divisor modules, the exact \(\tau_h\) theta torsion identification, and \(\mu_h\) coherent annihilator identification. Keep the kernel in every preimage extension and use sheaf colimits for the total object. Quotient reductions are separate opposite-direction maps. Keep full tensor nodes, original source metrics, and each cyclic subobject's transported generator. Use normalized \(\sigma_h\) only on the full-depth subposet where its inverse unit exists. These statements prove compatibility inside the original arithmetic construction and produce no new purity or RH conclusion.
