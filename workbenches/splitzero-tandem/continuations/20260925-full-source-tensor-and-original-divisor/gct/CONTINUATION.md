# Full-source spectral synthesis and geometric tensor comparison

Complete continuation of the Split-Zero cohomology and original-zeta research programme. This reader contains the new proofs at the stated frozen cutoff; earlier definitions and proofs remain in the [preceding cumulative edition](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/README.md). No RH, purity, or complexity-theory endpoint is claimed. Full multiplicities, original factors, source topologies, kernels and endpoint terms remain in the proofs.

## Included complete arguments

- [The Gysin defect closure, the positive receiver, and the dual original extension](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GYSIN_DEFECT_CLOSURE_AND_POSITIVE_RECEIVER.md)
- [The actual adjoint-defect source quotient and its continuous dual](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ADJOINT_DEFECT_SOURCE_TOPOLOGY_COMPARISON.md)
- [The actual extension class in the original source and residue spaces](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md)
- [Involutions of the actual extension-class modules and their original-zeta residue maps](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/EXTENSION_CLASS_INVOLUTION_INDEPENDENT.md)
- [All continuous positive transfer forms on the original full-jet quotient](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/CONTINUOUS_POSITIVE_TRANSFER_FORMS.md)
- [Continuous positivity and the actual specialization obstruction](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/POSITIVE_SOURCE_COMPLETION_AND_SPECIALIZATION.md)
- [The full multiplier domain of the actual specialization source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md)
- [Gaussian approximation on the complete original source and its actual defect](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md)
- [Gaussian spectral synthesis on the complete original source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_SPECTRAL_SYNTHESIS.md)
- [Independent proof of Gaussian synthesis in the original source quotient](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_SPECTRAL_SYNTHESIS_INDEPENDENT.md)
- [Tensor powers of the actual specialization source and the full positive tensor receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ACTUAL_SPECIALIZATION_TENSOR_WEIGHT_COMPARISON.md)
- [Spectral synthesis on the original completed tensor source](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/COMPLETED_TENSOR_SOURCE_SYNTHESIS.md)
- [The actual tensor square on one sphere: specialization, supported boundaries and angular degree](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ACTUAL_FIXED_BASE_TENSOR_SQUARE.md)
- [Independent calculation of the actual rapid tensor receiver](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/TENSOR_RECEIVER_INDEPENDENT_CHECK.md)

# The Gysin defect closure, the positive receiver, and the dual original extension

Independent derivation with root topology strengthening, 24 September 2026. Proof locators GDC0–GDC14. The independent reviewer derived the restriction-topology argument separately; the root verified and integrated its full proof below. The final written GDC0–GDC14 received root mathematical verification, not a completed independent audit of every final line.

## GDC0. Construction order, read sources, and notation

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every coefficient operation below occurs after the complete-history arithmetic reconstruction. No addition, arithmetic value, parity, coordinate, distance or midpoint is assigned to \(\tau\). The notation \(Z_n\) continues to denote the user's information layers. Both support branches and their separate records remain present. This calculation constructs the next map from the already measured defect; it does not insert weight purity into the hypotheses.

The complete proofs RGR0–RGR12, PTQ0–PTQ11 and PSC0–PSC9 were read for this derivation, as were SDT0–SDT9, including its full bidual proof. RTT is the existing independently derived residue comparison. The current definition-source instruction and amended what-would workflow were reread. The exact versions and coverage are recorded in GDC14.

Use RGR's original coefficient extension, with its actual Fréchet topologies,
\[
0\longrightarrow J\xrightarrow{k}A\xrightarrow{q}Q\longrightarrow0,
\qquad B=A'_\beta,\quad j=q':Q'_\beta\longrightarrow B.
\tag{GDC0.1}
\]
The prime means the continuous complex-linear dual; \(\beta\) means uniform convergence on bounded sets. SDT proves that \(j\) is a strong topological embedding with closed image \(J^\perp\), and that \((Q'_\beta)'=Q\) by evaluation. In the original Mellin coordinate
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},
\qquad Q\simeq\mathcal B/\mathcal I,
\tag{GDC0.2}
\]
\(\mathcal B\) is the entire rapid-strip space and \(\mathcal I\) is the ideal vanishing to order \(m_\rho\) at every actual nontrivial zero of original \(\zeta\). We write \(F(\rho)\) for the value of the class after this specified comparison, not an assigned value of the support.

Retain the entire actual divisor \(\mathscr Z\), its multiplicities, and
\[
H=\ell^2(\mathscr Z,m),\quad \rho^\#=1-\overline\rho,
\quad (\mathsf Jy)_\rho=y_{\rho^\#},\quad
E:Q\to H,
\]
\[
A_H(y)(F)=\langle EF,\mathsf Jy\rangle_+
=\sum_\rho m_\rho F(\rho)\overline{y_{\rho^\#}}.
\tag{GDC0.3}
\]
The inner product is linear in its first variable. The map \(E\) is continuous and has dense image; \(A_H\) is continuous, injective and anti-linear. Density follows from the actual full-jet isolators realizing finite value sequences, not from a claim about finite-support density in the primal Fréchet topology.

For \(r>1\) set
\[
D_r=T_r^*-U_r,\quad U_r=rT_{1/r},\quad
d_r(\rho)=e^{-i\gamma\log r}(r^\sigma-r^{1-\sigma}),
\quad(D_ry)_\rho=d_r(\rho)y_\rho,
\tag{GDC0.4}
\]
where \(\rho=\sigma+i\gamma\) and \(0<\sigma<1\). For the conjugate Hilbert space \(\overline H\),
\[
\sigma_r(\overline y)=A_H(D_ry),\qquad a_r=j\sigma_r.
\tag{GDC0.5}
\]
These are continuous complex-linear maps on \(\overline H\). An arbitrary \(r>1\) here is a coefficient parameter; only a recovered positive integer \(n\) is asserted to be an actual geometric cover degree.

## GDC1. Exact signs and the annihilator on the original source

Let \(H_L,H_O\) be the closed subspaces supported respectively on the actual line and off-line parts of the divisor, with projections \(P_L,P_O\). Both subsets are preserved by \(\#\). The sign under reflection is
\[
d_r(\rho^\#)=-d_r(\rho).
\tag{GDC1.1}
\]
Consequently the complete functional is
\[
\sigma_r(\overline y)(F)
=\sum_\rho m_\rho F(\rho)
 \overline{d_r(\rho^\#)y_{\rho^\#}}
=-\sum_\rho m_\rho F(\rho)e^{i\gamma\log r}
 (r^\sigma-r^{1-\sigma})\overline{y_{\rho^\#}}.
\tag{GDC1.2}
\]
The minus sign in the second expression comes from (GDC1.1); it is independent of the positive Dirac orientation of the Gysin map. Both sums converge absolutely by Cauchy–Schwarz and boundedness of \(D_r\).

Define closed source subspaces
\[
N_O=\ker(P_OE)=\{F\in Q:F(\rho)=0\ \forall\rho\in\mathscr Z_O\},
\]
\[
N_L=\ker(P_LE),\qquad N_0=N_L\cap N_O=\ker E,
\qquad A_O=q^{-1}(N_O)\subset A.
\tag{GDC1.3}
\]
The subscript records the values required to vanish. In particular \(N_O\) retains all higher jets and the line values. No direct-sum source interpolation is included in its definition.

The exact preannihilator of the defect image is
\[
\boxed{\{F\in Q:\sigma_r(\overline y)(F)=0\ \forall y\in H\}=N_O.}
\tag{GDC1.4}
\]
One proof reads (GDC1.2). All its coefficients vanish on line points. At any actual off-line \(\rho\), choose \(y\) with the sole nonzero coordinate
\(y_{\rho^\#}=1/(m_\rho d_r(\rho^\#))\). Its functional is exactly \(F\mapsto F(\rho)\). Thus annihilating every image functional forces precisely the off-line value conditions, and those conditions conversely kill the entire sum. This uses actual individual isolating coordinates in \(H\), not an unrestricted holomorphic interpolation claim.

In particular \(\ker\sigma_r=\overline{H_L}\). The overline here denotes the conjugate vector space, not a closure; closures below carry a topology label.

## GDC2. The actual strong-dual closure

Write \(I_r=\sigma_r(\overline H)\subset Q'_\beta\). Then
\[
\boxed{\overline{I_r}^{\,\beta}=S_O:=N_O^\perp,\qquad
\overline{a_r(\overline H)}^{\,\beta}=jS_O=A_O^\perp\subset B.}
\tag{GDC2.1}
\]
The first inclusion into \(N_O^\perp\) follows from (GDC1.4), and this annihilator is strongly closed. If a functional in \(N_O^\perp\) lay outside the strong closure of \(I_r\), Hahn–Banach separation of that closed linear subspace would give a continuous linear functional on \(Q'_\beta\) vanishing on \(I_r\) but not on the stated functional. SDT's full bidual result identifies the separator as evaluation at some \(F\in Q\). Equation (GDC1.4) then forces \(F\in N_O\), a contradiction. This proves equality in the strong, not only weak, topology.

For the second assertion, the closed strong embedding \(j\) takes the first closure to the closure inside \(B\). A functional \(j\lambda\) annihilates \(A_O\) exactly when \(\lambda\) annihilates \(N_O\). Conversely any continuous functional on \(A\) annihilating \(A_O\) annihilates \(J\subset A_O\), hence is a unique \(j\lambda\). This proves \(jS_O=A_O^\perp\).

There is also a useful intermediate equality:
\[
\overline{A_H(H_O)}^{\,\beta}=S_O.
\tag{GDC2.2}
\]
Indeed \(I_r\subset A_H(H_O)\subset S_O\), while (GDC2.1) supplies the closure. These are closure identities. They do not declare \(I_r\) or \(A_H(H_O)\) closed, equal, or topologically isomorphic to a Hilbert space with the strong subspace topology.

## GDC3. Every nontrivial coefficient parameter has the same unclosed image

A stronger comparison than (GDC2.1) is available without changing the source. For \(r,t>1\), define a diagonal operator \(V_{r,t}\) on \(H\) by
\[
v_{r,t}(\rho)=
\begin{cases}
e^{-i\gamma\log(r/t)}\dfrac{r^\sigma-r^{1-\sigma}}{t^\sigma-t^{1-\sigma}},&\sigma\ne1/2,\\
1,&\sigma=1/2.
\end{cases}
\tag{GDC3.1}
\]
It is bounded and has bounded inverse \(V_{t,r}\). To prove this, put \(c=\sigma-1/2\). The absolute value of its off-line coefficient is
\[
\sqrt{r/t}\,\frac{\sinh(c\log r)}{\sinh(c\log t)}.
\tag{GDC3.2}
\]
The ratio has a positive continuous extension at \(c=0\), of value \(\sqrt{r/t}\log r/\log t\), and is positive on the compact interval \([-1/2,1/2]\). Its minimum there is positive and its maximum finite. The exponential in (GDC3.1) has modulus one. Assigning the actual line value one therefore keeps both bounds. No lower bound on an off-line zero's distance from the line is needed.

The same comparison has explicit bounds without taking an unspecified compact minimum. Retain the original difference as
\[
r^\sigma-r^{1-\sigma}=c\,L_r(c),\qquad
L_r(c)=\int_0^1(\log r)
\left(r^{1/2+uc}+r^{1/2-uc}\right)\,du.
\]
This follows by integrating the derivative of
\(u\mapsto r^{1/2+uc}-r^{1/2-uc}\); both endpoint terms remain. For
\(|c|\le1/2\), arithmetic-geometric mean and monotonicity in \(|uc|\) give
\[
2\sqrt r\log r\ \le L_r(c)\le(r+1)\log r.
\]
Consequently every off-line diagonal coefficient in (GDC3.1) satisfies
\[
\frac{2\sqrt r\log r}{(t+1)\log t}
\le |v_{r,t}(\rho)|
\le \frac{(r+1)\log r}{2\sqrt t\log t}.
\tag{GDC3.2a}
\]
The line value one is retained separately. These are bounds on the actual parameter-change map, not a change of the original operators.

Direct coordinate substitution gives
\[
D_r=D_tV_{r,t},\qquad V_{r,t}V_{t,u}=V_{r,u},\qquad
V_{r,t}|_{H_L}=I.
\tag{GDC3.3}
\]
All \(V_{r,t}\) commute with every coefficient dilation and transfer. In particular
\[
\boxed{I_r=I_t\quad(r,t>1).}
\tag{GDC3.4}
\]
This is equality of the actual images before closure. It does not say that the operator norms, pointwise defect sizes, or heat-weighted traces of the defects agree. At \(r=1\), \(D_1=0\), so that parameter is deliberately excluded from (GDC3.4).

## GDC4. Gysin complexes, the unseparated costalk, and parameter isomorphisms

Use the positively oriented coordinate and currents of RGR, with
\(dh_p b=\delta_pb\). Its verified defect receiver is
\[
\mathscr E_r=\operatorname{Cone}(-\delta_pa_r)[-1],
\quad
\mathscr E_r^{-1}=\mathscr T_A^{-2},\quad
\mathscr E_r^0=\mathscr T_A^{-1}\oplus i_*\overline H,\quad
\mathscr E_r^1=\mathscr T_A^0,
\]
\[
d^{-1}b=(-d_Tb,0),\qquad d^0(b,\overline y)=-d_Tb+\delta_pa_r(\overline y).
\tag{GDC4.1}
\]
The positive angular quotient gives the triangle
\[
\underline B_D[1]\to\mathscr E_r\to i_*\overline H
\xrightarrow{+\mathrm{Gys}_B a_r}\underline B_D[2].
\tag{GDC4.2}
\]
The costalk in positive Dirac coordinates is exactly
\[
i^!\mathscr E_r=[\overline H\xrightarrow{+a_r}B]\quad(\deg0,1).
\tag{GDC4.3}
\]
RGR proves this by its restriction-fibre cancellation; the literal shifted cone has differential \(-a_r\), compared with (GDC4.3) by minus identity on the target. The positive sign of (GDC4.2) and (GDC4.3) is not changed by the coefficient minus sign in (GDC1.2).

Its actual cohomology with the kernel and quotient topologies is
\[
H^0(i^!\mathscr E_r)=\overline{H_L},\qquad
H^1(i^!\mathscr E_r)=B/jI_r.
\tag{GDC4.4}
\]
The second space is retained even if unseparated. Its separated quotient is exactly
\[
\boxed{(H^1(i^!\mathscr E_r))_{\rm sep}=B/A_O^\perp.}
\tag{GDC4.5}
\]
In fact the closure of zero in (GDC4.4) is \(A_O^\perp/jI_r\). This follows by applying the open quotient map to (GDC2.1): a class belongs to the closure of zero precisely when every neighborhood of a representative intersects \(jI_r\). No completion or replacement of the unseparated cohomology has been made.

Let \(\overline V_{r,t}(\overline y)=\overline{V_{r,t}y}\). The continuous cochain isomorphism
\[
\mathscr E_r\longrightarrow\mathscr E_t,
\qquad (b,\overline y)\longmapsto(b,\overline V_{r,t}\overline y)
\tag{GDC4.6}
\]
is identity on the other current terms. The differential commutes because \(a_t\overline V_{r,t}=a_r\); its inverse uses \(V_{t,r}\). These isomorphisms satisfy the cocycle law, fix the entire nearby coefficient \(B\), and fix the supported kernel \(\overline{H_L}\). Thus the parameter-independent costalk quotient has an explicit receiver-level comparison, not merely matching dimensions.

These are the reduced local summand's formulas, in the precise sense of RGR1.9. Both original endpoint lines are restored by the same explicit direct summand as RGR10:
\[
\mathscr E_{r,\mathrm{full}}=\mathscr E_r\oplus i_*E_p'[-1],
\qquad
i^!\mathscr E_{r,\mathrm{full}}
=[\,\overline H\xrightarrow{a_r}B\,]\oplus E_p'[-1].
\tag{GDC4.7}
\]
Thus degree zero is still \(\overline{H_L}\), while degree one is
\((B/jI_r)\oplus E_p'\), and its separated version is
\((B/A_O^\perp)\oplus E_p'\). Here \(E_p\) keeps its two labelled source coordinates, value at zero and real integral. All parameter isomorphisms and receiving maps below extend by the identity on this endpoint summand. At the other pole the coordinate is \(1/z\), with its own positive angular orientation as in RGR10. Neither endpoint line is absorbed into the defect quotient.

## GDC5. The universal positive quotient occurs as a supported summand

PTQ proves that the universal bounded positive-adjoint receiver for all actual integer transfers is
\[
q_+:H\to H/H_O=:H_{\rm pos},\qquad
u:H_{\rm pos}\xrightarrow{\sim}H_L,\quad u(q_+y)=P_Ly.
\tag{GDC5.1}
\]
Its original degree remains \(n\): \((T_n^{\rm pos})^*=U_n^{\rm pos}\) and \(U_n^{\rm pos}T_n^{\rm pos}=nI\). Since \(a_r\) vanishes on \(\overline{H_L}\), the orthogonal decomposition of its domain gives the literal complex decomposition
\[
\boxed{\mathscr E_r=i_*\overline{H_L}\ \oplus
\mathscr E_r^O,\qquad
\mathscr E_r^O=\operatorname{Cone}(-\delta_pa_r|_{\overline{H_O}})[-1].}
\tag{GDC5.2}
\]
The first summand is in degree zero. Its inclusion sends \(\overline{q_+y}\) to \((0,\overline{P_Ly})\), using \(u\). Its projection sends \((b,\overline y)\) to \(\overline{q_+y}\). Their composition is identity; substitution into (GDC4.1) verifies both cochain maps. The complement has zero degree-zero costalk kernel, since \(A_H\), \(j\), and \(D_r|_{H_O}\) are injective. Its degree-one costalk is still \(B/jI_r\).

This identifies the maximal supported source on which this particular Gysin obstruction vanishes. Any vector subspace of \(\overline H\) has zero restricted obstruction exactly when it is contained in \(\overline{H_L}\), by oriented Gysin adjunction and injectivity of \(jA_H\). It is the conjugate of the PTQ receiver through (GDC5.1), not the kernel of the total residue map. The total residue map is nonzero on actual line values, as RGR4 proves.

## GDC6. The full dual-extension rows, before and after separation

The arithmetic receiver \(\mathscr K_r\) is RGR9's fibre with nearby coefficient \(Q'\), supported coefficient \(\overline H\), and variation \(+\sigma_r\). Its costalk is \([\overline H\xrightarrow{\sigma_r}Q']\). The existing original dual row produces
\[
0\to Q'/I_r\xrightarrow{[\lambda]\mapsto[j\lambda]}
B/jI_r\xrightarrow{[b]\mapsto k'b}J'\to0.
\tag{GDC6.1}
\]
This is an exact row of vector spaces with continuous maps for the indicated quotient topologies. To check its middle kernel, \(k'b=0\) gives \(b=j\lambda\); its left kernel is zero by injectivity of \(j\). Surjectivity is continuous Hahn–Banach extension from the closed subspace \(J\subset A\). The row is the actual pushout of the transpose of \(e_0\), as witnessed by \([(b,[\lambda])]\mapsto[b+j\lambda]\).

Passing to the explicitly calculated separated quotients gives another exact row,
\[
\boxed{0\to Q'_\beta/S_O\xrightarrow{\bar j}
B/A_O^\perp\xrightarrow{\bar k'}J'_\beta\to0.}
\tag{GDC6.2}
\]
The left and middle spaces here have their quotient locally convex topologies. Exactness follows from precisely the same calculation, since \(A_O^\perp=jS_O\subset jQ'\). The left map is a closed topological embedding: quotienting the closed embedded subspace \(jQ'\subset B\) by its subspace \(jS_O\) gives the induced subspace topology in \(B/jS_O\). Indeed an open set \(U\subset B\) satisfies \(q(U)\cap q(jQ')=q(U\cap jQ')\), because the quotient kernel lies in \(jQ'\). Its image is closed because \(jQ'\) is closed.

The natural vertical maps from (GDC6.1) to (GDC6.2) have kernels
\[
S_O/I_r\quad\hbox{and}\quad A_O^\perp/jI_r,
\tag{GDC6.3}
\]
which are identified by \(j\). They are the respective closures of zero and have been retained, not treated as nonexistent cohomology. The strong openness needed for the separated extension is proved directly in GDC7.

## GDC7. The separated row is the transpose of an actual restricted original extension

The inclusion \(A_O=q^{-1}N_O\) constructs the strict Fréchet row
\[
e_O:\quad0\to J\xrightarrow{k_O}A_O\xrightarrow{q_O}N_O\to0.
\tag{GDC7.1}
\]
Both subspaces are closed; \(q_O\) is onto by its preimage definition. Its quotient topology is the subspace topology of \(N_O\): if \(U\subset A\) is open, then
\(q(U\cap A_O)=q(U)\cap N_O\), since any representative of a class in \(N_O\) belongs to \(A_O\). Thus it is the pullback of the actual original extension along \(N_O\hookrightarrow Q\), with no chosen section.

Continuous restriction gives the following bijections; their strong topological inverses are proved below:
\[
\alpha:Q'_\beta/S_O\longrightarrow (N_O)'_\beta,
\qquad \alpha[\lambda]=\lambda|_{N_O},
\]
\[
\eta:B/A_O^\perp\longrightarrow (A_O)'_\beta,
\qquad\eta[b]=b|_{A_O}.
\tag{GDC7.2}
\]
They are surjective by Hahn–Banach and injective by their displayed kernels. They are continuous because a bounded subset of a closed subspace is bounded in the ambient space. Their exact commutative diagram is
\[
\begin{array}{ccccccccc}
0&\to&Q'/S_O&\xrightarrow{\bar j}&B/A_O^\perp&\xrightarrow{\bar k'}&J'&\to&0\\
&&\downarrow\alpha&&\downarrow\eta&&\Vert\\
0&\to&(N_O)'&\xrightarrow{q_O'}&(A_O)'&\xrightarrow{k_O'}&J'&\to&0.
\end{array}
\tag{GDC7.3}
\]
Every displayed map is continuous for the topologies just specified. Both rows are algebraically exact. In particular the middle separated costalk is explicitly related to the dual of a source that still contains the complete original \(J\). The following argument proves both rows strict and both vertical arrows topological isomorphisms.

The map \(q_O'\) is also a closed strong embedding. To verify this rather than assuming it from surjectivity, a bounded set of \(N_O\) has compact closure: it is a bounded subset of the Montel space \(Q\), and \(N_O\) is closed. SDT4's finite-choice compact-lift construction applies to the strict quotient (GDC7.1) of Fréchet spaces, using its increasing quotient seminorms. It lifts that compact closure to a compact subset of \(A_O\), and hence gives bounded lifts of the original bounded set. For each bounded \(C\subset N_O\) with bounded lift \(\widetilde C\subset A_O\),
\[
\sup_{x\in C}|\lambda(x)|
=\sup_{a\in\widetilde C}|(q_O'\lambda)(a)|.
\tag{GDC7.4}
\]
Together with the continuous-forward seminorm estimate this proves the strong embedding. Its image is \(J^\perp\) inside \((A_O)'\), hence closed.

Here is the required restriction-topology argument for the actual spaces. Let \(X\) be any one of \(A,Q,A_O,N_O\), with its established Fréchet topology, and let \(L\subset X\) be one of its closed subspaces used below. Every bounded subset of \(X\) has compact closure: SDT proves this for \(A,Q\), and it passes directly to their closed subspaces. The closed absolutely convex hull of a bounded subset is still bounded, because every continuous seminorm is bounded on that hull. Its closure is therefore compact as well.

The restriction
\[
R_L:X'_\beta\longrightarrow L'_\beta
\tag{GDC7.5}
\]
is continuous since bounded sets in \(L\) remain bounded in \(X\), and surjective by continuous complex Hahn–Banach extension. We prove it is open. For a compact absolutely convex \(K\subset X\), put
\[
\mathcal U_K=\{\mu\in X':\sup_{x\in K}|\mu(x)|<1\},\qquad
\mathcal V_K=\{\lambda\in L':\sup_{x\in K\cap L}|\lambda(x)|<1/2\}.
\]
Such \(\mathcal U_K\) form a base of strong neighborhoods after scaling and finite unions of bounded sets followed by closed absolutely convex hull. The set \(\mathcal V_K\) is a strong neighborhood since \(K\cap L\) is bounded in \(L\).

Fix \(\lambda\in\mathcal V_K\). There is an open absolutely convex neighborhood \(U\) of zero in \(X\) for which
\[
|\lambda(x)|<1\quad(x\in (K+U)\cap L).
\tag{GDC7.6}
\]
If not, choose a decreasing neighborhood base \(U_j\), and \(x_j=k_j+u_j\in L\) with \(k_j\in K\), \(u_j\in U_j\) and \(|\lambda(x_j)|\ge1\). Compactness supplies a subsequence \(k_j\to k\); then \(u_j\to0\), so \(x_j\to k\). Closedness gives \(k\in K\cap L\), and continuity on \(L\) contradicts \(|\lambda(k)|<1/2\). This proves (GDC7.6).

The Minkowski functional \(p\) of the open absolutely convex absorbing set \(K+U\) is a continuous seminorm. Scaling (GDC7.6) shows \(|\lambda(x)|\le p(x)\) for every \(x\in L\): test each positive \(a>p(x)\), for which \(x/a\in K+U\), and let \(a\) decrease to \(p(x)\). Complex Hahn–Banach now gives a continuous extension \(\mu\) with \(|\mu|\le p\) on \(X\). Since \(K\) is compact and lies in the open unit ball of \(p\),
\[
\sup_{x\in K}|\mu(x)|\le\max_{x\in K}p(x)<1.
\]
Thus \(\mathcal V_K\subset R_L(\mathcal U_K)\), proving strong openness. This proves
\[
X'_\beta/L^\perp\xrightarrow[\mathrm{restriction}]{\ \sim\ }L'_\beta
\tag{GDC7.7}
\]
with the actual quotient and strong dual topologies.

Restriction also admits bounded lifts of bounded sets, without a linear section. A strongly bounded family \(\mathcal C\subset L'\) is pointwise bounded. The Baire argument on the Fréchet space \(L\) makes it equicontinuous: the closed sets where \(\sup_{\lambda\in\mathcal C}|\lambda(x)|\le j\) cover \(L\), one has interior, and taking differences gives a neighborhood of zero with a uniform bound. Consequently there are a continuous seminorm \(p_X\) on \(X\) and \(C>0\) such that \(|\lambda(x)|\le C p_X(x)\) for all \(\lambda\in\mathcal C,x\in L\). Choose each Hahn–Banach extension with this same bound. On every bounded \(B_0\subset X\), their values are bounded by \(C\sup_{B_0}p_X\), so the chosen family is strongly bounded in \(X'\).

Publication source credit: Baire category is the classical input. See Terence Tao, [245B, Notes9, Theorem1](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/) (1 February2009), for complete metric spaces. The present proof supplies the actual Frechet seminorm argument.

Publication source credit: Human-source attribution: the extension of continuous linear functionals is the Hahn–Banach theorem, not a programme result. See Terence Tao, [245B, Notes6: Duality and the Hahn–Banach theorem](https://terrytao.wordpress.com/2009/01/26/245b-notes-6-duality-and-the-hahn-banach-theorem/), Theorem1 and its complex proof (26 January2009). For the locally convex use here, continuity bounds a functional by a continuous seminorm; quotienting its kernel reduces this application to that normed-space theorem. No continuous splitting of the original quotient is thereby asserted.

Apply (GDC7.7) to \((X,L)=(Q,N_O)\) and \((A,A_O)\). This proves that \(\alpha,\eta\) in (GDC7.3) are strong topological isomorphisms. Apply it also to \((A_O,J)\); then \(k_O'\) is strongly open. Together with the closed embedding \(q_O'\), both rows in (GDC7.3) are strict exact sequences of the specified locally convex spaces. In particular,
\[
\boxed{(H^1(i^!\mathscr E_r))_{\rm sep}
\ \simeq\ (A_O)'_\beta.}
\tag{GDC7.8}
\]
The unseparated cohomology \(B/jI_r\), its closure of zero, and every map in (GDC6.3) remain part of the construction. Equation (GDC7.8) does not identify that original unseparated quotient with its separated quotient.

## GDC8. The induced original residue map is exactly the positive compression

Let \(p_S:Q'\to Q'/S_O\) be the quotient. Since \(A_H(H_O)\subset S_O\),
\[
p_S A_Hy=p_S A_HP_Ly.
\tag{GDC8.1}
\]
The right-hand map is injective on \(H_L\): an element \(A_Hx\), \(x\in H_L\), annihilating \(N_O\) pairs to zero with every line-value isolator, so all coordinates of \(x\) vanish. Thus
\[
\overline{H_{\rm pos}}\longrightarrow Q'/S_O,
\quad\overline{q_+y}\longmapsto p_S A_Hy
\tag{GDC8.2}
\]
is a well-defined continuous injective linear map. It is not asserted to be a strong topological embedding or onto the entire coefficient quotient.

For \(F\in N_O\), the exact evaluation after restriction is
\[
(\alpha p_S A_Hy)(F)
=\sum_{\rho\in\mathscr Z_L}m_\rho F(\rho)\overline{y_\rho}
=\langle EF,P_Ly\rangle_+.
\tag{GDC8.3}
\]
This is a direct original-residue realization of the positive receiver, with no nonholomorphic source projector. The source \(N_O\) maps densely into \(H_L\), because every finite line-value isolator lies in \(N_O\). Its kernel is exactly \(N_0\). Thus \(N_O/N_0\), equipped with its explicit value norm, completes to \(H_L\); its Fréchet quotient topology is not equated with that norm.

For the original total map \(\sigma(\overline G)=A_HEG\), the composite \(p_S\sigma\) has exactly the kernel \(\overline{N_L}\), by (GDC8.3) and those isolators. Its strong closure in the quotient is
\[
\boxed{\overline{p_S\sigma(\overline Q)}=N_0^\perp/S_O.}
\tag{GDC8.4}
\]
To prove this, RTT/RGR8 gives \(\overline{\sigma(\overline Q)}^{\,\beta}=N_0^\perp\). This closed subspace contains \(S_O\), since \(N_0\subset N_O\). Its quotient is a closed subspace of \(Q'/S_O\); continuity of the quotient and density give exactly (GDC8.4).

The remaining quotient in the exact row
\[
0\to N_0^\perp/S_O\to Q'/S_O\to Q'/N_0^\perp\to0
\tag{GDC8.5}
\]
retains the functionals on the original value-zero source, through the strong topological restriction isomorphism \(Q'/N_0^\perp\to (N_0)'_\beta\) supplied by (GDC7.7) with \(X=Q,L=N_0\). Thus the coefficient quotient has not erased the higher jets simply because its residue part observes only values.

Evaluation of an arbitrary class of \(Q'/S_O\) is defined on \(N_O\), not on all of \(Q\). This domain is essential. On the image of the original residue map the canonical representative \(A_HP_LEG\in Q'\) does produce the full positive compression on all original tests; that representative is supplied by the proved Hilbert map. We do not extend it to an unproved projection on all \(Q'_\beta\).

## GDC9. The remaining source compatibility is preserved exactly

The restricted source and the positive source quotient are related by
\[
0\to N_O/N_0\longrightarrow Q/N_L
\longrightarrow Q/(N_L+N_O)\to0.
\tag{GDC9.1}
\]
The first map sends the same class to its class modulo \(N_L\); its kernel is \(N_L\cap N_O=N_0\). Its image is \((N_L+N_O)/N_L\), proving the last cokernel. All maps are continuous for their subspace/quotient topologies, and the last quotient is retained even if unseparated.

This is the value version of PSC's reconstruction defect. It proves the strongest immediate source map supplied by (GDC8.3) while keeping its cokernel, rather than assuming that every positive value quotient has a representative vanishing at all off-line zeros. Its image is dense after the explicitly specified Hilbert completion, since it contains every finite retained value vector. Neither surjectivity in (GDC9.1) at the first arrow nor primal topological density is inferred from that Hilbert statement.

The whole Weil form remains the exact sum
\[
W(F,G)=\langle P_LEF,P_LEG\rangle_+
+\langle P_OEF,\mathsf JP_OEG\rangle_+.
\tag{GDC9.2}
\]
The second term need not descend to \(Q/N_L\): on each actual off-line reflected pair it has the two signed values \(+2m_\rho\) and \(-2m_\rho\) of PTQ5. Their existence as formulas does not assert that such a pair exists. The restriction \(F\in N_O\) kills this term by an exact source condition. It does not prove that it is zero on the entire original source.

## GDC10. A constructed coefficient map kills the defect while retaining the positive residue

The continuous restriction
\[
R_O:B\longrightarrow(A_O)'_\beta,
\qquad R_Ob=b|_{A_O}
\tag{GDC10.1}
\]
has kernel exactly \(A_O^\perp=\overline{a_r(\overline H)}^{\,\beta}\). Therefore it kills the actual Gysin coefficient \(a_r\), and kills exactly its closed linear envelope. Unlike restriction to \(J\) alone, it retains the line-residue part in (GDC8.3), transported by the injective \(q_O'\).

There is a literal continuous-current version. Inclusion \(\iota_O:A_O\hookrightarrow A\) induces continuous maps on compactly supported smooth test forms. Their transposes give a cochain map
\[
\iota_O^\vee:\mathscr T_A\longrightarrow\mathscr T_{A_O}.
\tag{GDC10.2}
\]
It commutes with the current differential and sends \(\delta_pb\) to \(\delta_p R_Ob\). Hence
\[
\mathscr E_r\longrightarrow
\mathscr T_{A_O}[-1]\oplus i_*\overline H,
\qquad(b,\overline y)\longmapsto(\iota_O^\vee b,\overline y)
\tag{GDC10.3}
\]
is a cochain map: its target has zero attaching map, because \(R_Oa_r=0\). The coefficient space \(A_O\) is closed Fréchet and complete, so RGR's compact-test current contraction applies to it, giving the actual target \(\underline{(A_O)'}[1]\oplus i_*\overline H\). This is an exhibited receiving map, not merely a proposed future nullification.

For precision about universality, set \(B_{\rm sep}=B/A_O^\perp\). Every continuous linear map \(f:B\to K\) into a Hausdorff locally convex space that kills \(a_r\) kills its closure and factors uniquely and continuously through \(B_{\rm sep}\). The quotient topology proves continuity of the factor. Thus the separated coefficient quotient is the universal such coefficient target. In vector-space sheaves its zero attaching map gives the split receiver
\[
\mathscr E_{r,\rm sep}=\underline{B_{\rm sep}}[1]\oplus i_*\overline H.
\]
The quotient map induces an exact triangle
\[
\underline{A_O^\perp}[1]\longrightarrow\mathscr E_r
\longrightarrow\mathscr E_{r,\rm sep}
\longrightarrow\underline{A_O^\perp}[2].
\tag{GDC10.4}
\]
To verify it, use the two Gysin triangles with common supported term and the coefficient quotient \(B\to B_{\rm sep}\). Its fibre is \(A_O^\perp\) in degree zero. Cancelling the common supported term leaves that coefficient fibre shifted by one. This calculation takes place in vector-space sheaves; it does not assert exactness of an unspecified derived category of locally convex spaces. The separately constructed map (GDC10.3) gives the actual continuous-current comparison with the strong dual \((A_O)'\).

The original nonzero obstruction, if present, is thereby killed by a specified coefficient quotient with its entire kernel retained in (GDC10.4). This is not a null-homotopy of the original attaching map in its unchanged coefficient sheaf. It is the exact next construction yielded by its measured closure, together with a retained positive residue and the dual source extension (GDC7.3).

## GDC11. Every full multiplicity block and original residue factor

Let an actual zero have multiplicity \(m\). On its globally realized finite local block \(\mathbb C[t]/t^m\), the condition defining \(N_O\) is
\[
N_O|_\rho=
\begin{cases}
\mathbb C[t]/t^m,&\rho\in\mathscr Z_L,\\
t\mathbb C[t]/t^m,&\rho\in\mathscr Z_O.
\end{cases}
\tag{GDC11.1}
\]
Thus the closed defect image removes no dual jet at a line point and removes exactly the value-functional line at an off-line point. In \(Q'/S_O\), all \(m\) finite dual-jet directions at a line point and the \(m-1\) derivative directions at an off-line point remain. Independence can be checked against their actual primal full-jet isolators, which lie in \(N_O\) for exactly these stated directions. These finite-block assertions do not decompose the infinite source as an unrestricted product.

The actual residue map continues to use original \(\zeta\):
\[
\mathcal R(F,h)=\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(s)h(1-s)}{\zeta(s)}\,ds.
\tag{GDC11.2}
\]
Writing \(\zeta(\rho+t)=t^{m_\rho}u_\rho(t)\), the finite residue numerator for (GDC1.2) is exactly
\[
h_{r,C}(y)=\sum_{\rho\in C}
m_\rho(-1)^{m_\rho-1}u_\rho(0)
\overline{d_r(\rho^\#)y_{\rho^\#}}\,
e_{1-\rho,m_\rho-1},\qquad C\subset\mathscr Z\text{ finite}.
\tag{GDC11.3}
\]
Every factor is retained. The sign from reflection of the residue jet is \((-1)^{m_\rho-1}\); the additional sign of (GDC1.1) is separate. At the numerator's complementary point \(1-\rho\), the highest-jet line pairs to the value functional with exactly this full local unit factor. All derivatives of the unit remain in the original full residue pairing; (GDC11.3) records the particular rank-one numerator, not a replacement of that pairing matrix.

For a bounded test set \(K\subset Q\), the tail of the residue functionals is bounded by
\[
\sup_{F\in K}\|EF\|_+\,
\left(\sum_{\rho\notin C}m_\rho
|d_r(\rho^\#)y_{\rho^\#}|^2\right)^{1/2}.
\tag{GDC11.4}
\]
It tends to zero along all finite subsets, since \(D_ry\in H\). This proves the exact strong residue realization, without assuming that the finite primal numerators converge in \(Q\).

The coefficient comparison still retains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
\quad(k\ge1).
\tag{GDC11.5}
\]
Nothing here changes the original unit term, Euler prime-power weights, Gamma terms, endpoint terms or finite trivial-divisor sums of PSC5. The coefficient quotient's positive residue corresponds to that full arithmetic identity with its explicit off-line term retained; it supplies no replacement prime formula with that term silently omitted.

## GDC12. Exact coefficient actions and degree scope

For every recovered positive integer \(n\), the original source operators act by \(T_nF(s)=n^sF(s)\) and \(U_n=nT_{1/n}\). They preserve \(N_O,N_L,N_0,A_O\) and every full-jet ideal. Let the same notation on \(A\) denote the actual conjugate by \(\Theta\). Define on the dual coefficients
\[
\mathcal T_n^Q=n(T_{1/n}^Q)',\quad
\mathcal U_n^Q=(T_n^Q)',\qquad
\mathcal T_n^B=n(T_{1/n}^A)',\quad
\mathcal U_n^B=(T_n^A)'.
\tag{GDC12.1}
\]
All are strongly continuous, because their primal operators take bounded sets to bounded sets. The original degree remains
\(\mathcal U_n\mathcal T_n=\mathcal T_n\mathcal U_n=nI\).

The exact covariance is
\[
\sigma_r\overline T_n=\mathcal T_n^Q\sigma_r,
\qquad \sigma_r\overline U_n=\mathcal U_n^Q\sigma_r,
\qquad j\mathcal T_n^Q=\mathcal T_n^B j,
\quad j\mathcal U_n^Q=\mathcal U_n^B j.
\tag{GDC12.2}
\]
For example direct substitution into (GDC0.3) gives
\(A_HT_n=n(T_{1/n}^Q)'A_H\): the conjugated multiplier at \(\rho^\#\) is \(n^{1-\rho}\). Then \(D_rT_n=T_nD_r\) gives the first identity. Applying the same identity at \(1/n\) and retaining the leading scalar \(n\) proves the second. Naturality of \(q\) proves the last two. This proves covariance without confusing an anti-linear map with a complex-linear transpose; \(\overline T_n\) and \(\overline U_n\) act on \(\overline H\).

The images, their closures, and both rows (GDC6.1)–(GDC7.3) inherit these exact actions. The parameter comparisons \(V_{r,t}\) commute with the source actions and hence with their receiver isomorphisms. Coefficient naturality commutes with the oriented Gysin map, so all asserted diagrams hold on the fixed disk with the positive sign already proved. These coefficient comparisons do not assert an additional nonintegral cover, or drop the separate angular degree of an actual disk cover. In particular the arbitrary parameter \(r\) in the measured defect and the integer cover degree \(n\) have not been identified.

## GDC13. What this construction contributes to the lifting target

The exact common receiver is now calculated beyond its kernel: its strong closure is \(N_O^\perp\), its entire unseparated image is independent of \(r>1\), and the parameter change is a specified cochain isomorphism. Its supported kernel is canonically the conjugate of the universal positive quotient. Its separated costalk is the quotient by \(A_O^\perp\), with the original dual extension and all higher jets retained.

The next construction has also been carried out: restricting to the actual source \(A_O\) kills the closed defect coefficient, produces the concrete split receiving complex (GDC10.3), and retains the positive residue through (GDC8.3). Its exact cost is the constant coefficient kernel in (GDC10.4), together with the source compatibility quotient (GDC9.1). These are existing-object maps with proved kernels, not assumed interpolation or comaximality. They show precisely which source and quotient enter any subsequent specialization comparison.

Deligne's invariant-cycle obstruction quotient is still the separately derived \(\operatorname{im}\partial/\partial j(K)\). The present current map has its own stated source, target and attaching class; it has not been declared that arithmetic quotient. A vanishing achieved after (GDC10.1) is a proved coefficient-quotient vanishing, with its retained kernel, and does not assert weight-separated vanishing in the original coefficient. The calculation supplies an actual dual-extension and Gysin diagram to compare with that target while preserving the original positive and discarded forms. No existence of an off-line zero, absence of one, simplicity, arbitrary subset interpolation or vanishing of the original defect has been assumed.

## GDC14. Exact source coverage and version record

Complete current reads for this derivation:

- [../tau_weight_cohomology_20260924/CC_RESIDUE_GYSIN_RECEIVER_INDEPENDENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_RESIDUE_GYSIN_RECEIVER_INDEPENDENT.md), RGR0–RGR12; SHA256 `dd0c5fe172b2d4e2c18a337a1a92d06d9a523196f349ffa34bdb6cef1969e814`.
- [POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/POSITIVE_TRANSFER_UNIVERSAL_QUOTIENT.md), PTQ0–PTQ11; SHA256 `b70a8f0edf765dcfb3259735eb4a8f90a31c649ad308f55d821dcf5cccdae930`.
- [POSITIVE_QUOTIENT_SOURCE_AND_ARITHMETIC.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/POSITIVE_QUOTIENT_SOURCE_AND_ARITHMETIC.md), PSC0–PSC9; SHA256 `2d188377c6b694e363e5b32a331a8af2ef4562d2cb8aab272d0ce1149b6f1171`.
- [../tau_weight_cohomology_20260924/CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md), SDT0–SDT9, with the complete SDT6 proof reread separately to recover the tool-truncated passage; SHA256 `7f1a03a6225f1dfc22b167713c0ddbb154635b06f9479f6137b229845b67aefc`.

Retained complete independent derivation: [RESIDUE_TRACE_TRANSFER_INDEPENDENT.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/RESIDUE_TRACE_TRANSFER_INDEPENDENT.md), RTT0–RTT11; SHA256 `6a83d81039b4eb3e49c4054b4ff157896709647d6a5546751362b05a21de25b2`. The exact original-zeta residue, strong-dual topology, and Hilbert receiver formulas used from it are restated and proved in the receiving calculations above. RGR records the original Connes–Consani source provenance and its actual geometric transport; no new whole-paper reading of Connes–Consani or Deligne is claimed here.

The independent derivation initially created only this proof file. The root then verified GDC0–GDC14, corrected the displayed costalk spacing command, added the independently derived explicit parameter bounds and proved the full restriction-topology strengthening in GDC7. The pre-strengthening version is preserved under history/before_gysin_topology_strengthening_20260924. The independent review session supplied the separate mathematical derivations of the scale ratio and strong restriction theorem but ended before completing an audit of this final written version. Final-version review coverage must therefore be reported as complete root verification, with those independent constituent checks, rather than a complete independent final-version audit.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# The actual adjoint-defect source quotient and its continuous dual

Independent review and receiving calculation. Proof locators **AST0–AST9**.

## AST0. Construction stage, inputs and review coverage

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All vector spaces, arithmetic parameters, analytic coordinates and quotients below belong to the already reconstructed coefficient system. The two branches retain their separate recovered counters. No arithmetic, metric, midpoint or vector operation is assigned to the support.

The connected reconstruction, its correction-precedence table, the current construction guide, and verbatim WU062 and WU064–WU065 were reread before this calculation. The new operation is a quotient of the actual ACD specialization source, followed by continuous duality; its prerequisites are proved below. The user’s desired weight conclusion is not added as a hypothesis.

The complete written proof [GDC0–GDC14](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GYSIN_DEFECT_CLOSURE_AND_POSITIVE_RECEIVER.md), final SHA256 `5d0f471b3250e4ee894caca68232c556d64a137a49a9fe25a641db61b94f79ab`, was independently read and checked in full. Its earlier version `f9e15dff7755b0d9c79c9dd896e55966b87302051fcf8086fad90e56da126589` was also fully read; the final typography repair preserves the proof. The review checked its reflection sign, exact annihilator, strong closure, bounded parameter changes, all restriction and quotient topologies, receiver triangle, positive-residue restriction, finite multiplicities and source scope. A separate bounded independent check of GDC7 and the invoked SDT4 compact-lift construction also found no defect. This is a completed independent audit of the stated final version, in addition to its earlier root verification.

The receiving proof uses the actual maps of [ACD0–ACD8](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_ADJOINT_DEFECT_CONTINUOUS_DUAL.md), SHA256 `1373884c33e74aea9c0d48404152b16812b434b6cc4760227c8596666e919fda`, previously read and independently checked in full, and the explicit seminorm, finite-net and compact-lift arguments of [SDT1–SDT4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_STRONG_DUAL_TOPOLOGY_AND_JETS.md), reread for this extension. These are programme derivations. The human coefficient source remains Connes–Consani, *Schemes over* \(\mathbb F_1\) *and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3); the retained author TeX at [sources/CC_0903_2024_v3/author_source/announc3.tex](https://arxiv.org/abs/0903.2024v3), lines1376–1667, was read in the preceding source reconstruction. No new whole-paper reading or identification with Deligne’s étale invariant-cycle cross is claimed.

## AST1. The actual coefficient, the full original divisor and the defect

Retain the original spaces and maps
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,
\ \int_{\mathbb R}f(v)\,dv=0\},
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
p_{N,j}(a)=\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for every }N,j\ge0\},
\]
\[
\Sigma f(u)=2\sum_{k\ge1}f(ku),\quad J=\Sigma S,
\quad q:A\to Q=A/J,\quad B=A'_\beta.
\tag{AST1.1}
\]
The accepted exact-image theorem makes \(J\) closed. The Mellin comparison, with its original factor, is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta\Sigma f(s)=\zeta(s)\int_0^\infty f(v)v^s\frac{dv}{v}
\quad(\Re s>1).
\tag{AST1.2}
\]
Its entire rapid-strip quotient is \(Q\simeq\mathcal B/\mathcal I\), where \(\mathcal I\) imposes all multiplicities of the actual nontrivial zeros. The original source vector
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2}
\]
has exactly
\[
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]
\[
F_0(0)=F_0(1)=\frac18,\quad F_0(-1)=F_0(2)=\frac\pi{24},\qquad
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
\quad(k\ge1).
\tag{AST1.3}
\]
These values include the cancellations of the original pole and trivial zeros; none creates an extra quotient jet. At an actual nontrivial zero \(\rho\), writing \(z=s-\rho\), the retained local expression is
\[
F_0(\rho+z)=z^{m_\rho}
\frac{(\rho+z)(\rho+z-1)}8\pi^{-(\rho+z)/2}
\Gamma((\rho+z)/2)\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{AST1.4}
\]
Every derivative in this product uses the full Leibniz sum. Explicitly, away from its individually singular factors and then by holomorphic continuation where the whole expression is regular,
\[
F_0^{(j)}(s)=\sum_{k_0+k_1+k_2+k_3=j}
\frac{j!}{k_0!k_1!k_2!k_3!}
\left(\frac{s(s-1)}8\right)^{(k_0)}
\left(-\frac{\log\pi}{2}\right)^{k_1}\pi^{-s/2}
2^{-k_2}\Gamma^{(k_2)}(s/2)\zeta^{(k_3)}(s).
\tag{AST1.5}
\]
This entire comparison remains a comparison with original \(\zeta\), not its replacement. In its original half-plane the unit term, Euler product and logarithmic derivative remain
\[
\zeta(s)=1+\sum_{k\ge2}k^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
\tag{AST1.6}
\]

Let \(\mathscr Z\) be the actual distinct nontrivial zeros, with multiplicities \(m_\rho\), and set \(\rho^\#=1-\overline\rho\). Use
\[
H=\ell^2(\mathscr Z,m),\quad
\langle x,y\rangle_+=\sum_\rho m_\rho x_\rho\overline{y_\rho},
\quad (\mathsf Jy)_\rho=y_{\rho^\#},\quad E:Q\to H.
\tag{AST1.7}
\]
Here \((EF)_\rho=(\Theta_QF)(\rho)\), and the inner product is linear in the first variable. The proved full-jet isolators realize every finite value vector, so \(E\) is continuous with dense image. Put \(H_L=\ell^2(\mathscr Z_L,m)\), \(H_O=\ell^2(\mathscr Z_O,m)\), where the subsets denote respectively \(\Re\rho=1/2\) and \(\Re\rho\ne1/2\), and write \(P_L,P_O\) for their orthogonal projections. These definitions do not assert that either subset is empty or nonempty.

For a coefficient parameter \(t>0\), \((T_ty)_\rho=t^\rho y_\rho\) on \(H\); on \(A\) the original action is \((T_ta)(u)=a(u/t)\), descending to \(Q\) and giving the stated value action under \(E\). For the fixed coefficient parameter \(r>1\), ACD uses
\[
D_r=T_r^*-rT_{1/r},\quad
d_r(\rho)=e^{-i\Im\rho\log r}
(r^{\Re\rho}-r^{1-\Re\rho}),\quad
\beta_r=D_r^*\mathsf JE:Q\to H,\quad b_r=\beta_rq.
\tag{AST1.8}
\]
Thus, with no multiplicity factor absorbed into the vector coordinate,
\[
(\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#).
\tag{AST1.9}
\]
For \(C=\overline H\), the Riesz map is
\[
R:C\to H',\quad R(\overline y)(h)=\langle h,y\rangle_+.
\]
The exact continuous transposes are
\[
\sigma_r=\beta_r'R:C\to Q'_\beta,\quad
a_r=b_r'R=q'\sigma_r:C\to B,
\]
\[
\sigma_r(\overline y)(F)=\langle\beta_rF,y\rangle_+
=\langle EF,\mathsf JD_ry\rangle_+.
\tag{AST1.10}
\]
Continuity into strong duals follows from the estimate on every bounded test set \(K\),
\(\sup_{F\in K}|\langle\beta_rF,y\rangle_+|
\le\sup_{F\in K}\|\beta_rF\|_+\|y\|_+\).

## AST2. The specialization kernel is exactly the GDC source

Because \(r>1\), the scalar \(d_r(\rho)\) vanishes exactly on \(\mathscr Z_L\). Reflection preserves both subsets and their multiplicities. Formula (AST1.9) therefore proves
\[
\boxed{Z_r=\ker\beta_r=N_O:=\ker(P_OE),\qquad
\ker b_r=A_O:=q^{-1}N_O.}
\tag{AST2.1}
\]
Both kernels are closed in their specified Fréchet spaces, and they are independent of \(r>1\). The actual common specialization source is consequently
\[
\mathcal R:=Q/N_O\xleftarrow{\ \sim\ }A/A_O,
\qquad [a]\longmapsto[q(a)].
\tag{AST2.2}
\]
This is a topological quotient isomorphism. Indeed \(q\) and the quotient \(Q\to Q/N_O\) are open; their composite has kernel \(A_O\). An open set in \(A/A_O\) is the image of an open set in \(A\), whose composite image is open in \(Q/N_O\). The inverse is therefore continuous, without selecting any section.

In the genuine ACD restriction fibre the quotient coordinate is \((h,a)\mapsto h-b_ra\). Write \(\vartheta_p=d\arg z_p/(2\pi)\) for the positive angular form in the oriented pole coordinate. Its boundaries and their source comparison are exactly
\[
\partial_{-1}=-b_r:A\to H,\qquad
\partial_0=+1:A[\vartheta_p]\to A,
\]
\[
\operatorname{coker}\operatorname{sp}_{-1}
=A/A_O\simeq\mathcal R
\xrightarrow{\ -\overline\beta_r\ }b_rA,\qquad
\overline\beta_r([F])=\beta_rF.
\tag{AST2.3}
\]
The last arrow is a continuous bijection onto the image with its Hilbert subspace topology. It is a topological isomorphism if that image is instead given its transported quotient topology. No inverse continuity into the Hilbert subspace topology is asserted. The square with the original boundary \(-q:A\to Q\) commutes because \(b_r=\beta_rq\). Thus (AST2.2) is a refinement of the actual specialization calculation, not a quotient selected independently of that boundary.

At each actual multiplicity block \(\mathbb C[z]/z^{m_\rho}\), the kernel \(N_O\) retains the whole block on \(\mathscr Z_L\), and retains \(z\mathbb C[z]/z^{m_\rho}\) on \(\mathscr Z_O\). Accordingly \(\mathcal R\) observes one off-line value coordinate and no line coordinate on that block. All higher jets remain in the explicitly retained kernel. This local description neither replaces the full global quotient by a product nor proves unrestricted interpolation.

## AST3. The quotient topology and its full strong dual

We prove the new quotient’s bounded-compact property rather than assuming a quotient theorem for general Montel spaces. Put
\[
P_n(a)=\max_{0\le j\le n}\sup_{x\in\mathbb R}
(e^{nx}+e^{-nx})\left|\frac{d^j}{dx^j}a(e^x)\right|,
\quad
P_n^O([a])=\inf_{v\in A_O}P_n(a+v).
\tag{AST3.1}
\]
The quotient topology on \(\mathcal R=A/A_O\) is precisely the topology of these increasing seminorms. Closedness of \(A_O\) proves Hausdorffness. Completeness follows by the SDT1 successive-lift argument with \(A_O\) in place of \(J\): for a Cauchy subsequence choose lifts of successive differences with \(P_k<2^{-k}\); their series converges in \(A\) and maps to the required quotient limit.

Let \(K\subset\mathcal R\) be bounded. For each fixed \(n\), choose representatives of its elements with
\[
P_{n+1}(a_y)<1+\sup_{z\in K}P_{n+1}^O(z).
\tag{AST3.2}
\]
SDT2 proves that the set with this single \(P_{n+1}\) bound is totally bounded for \(P_n\), using both original exponential weights and one additional derivative. Its finite net maps to a finite \(P_n^O\)-net for \(K\). This holds for every \(n\), so \(K\) is totally bounded in the complete quotient metric. Its closure is compact. Thus \(\mathcal R\) is a Montel Fréchet space by this direct calculation.

The strict quotient \(\pi:Q\to\mathcal R\) therefore lifts every bounded set to a bounded set in \(Q\). Indeed take the compact closure just proved, apply SDT4’s finite-choice compact-lift construction to this strict Fréchet quotient, and intersect the resulting compact lift with the preimage of the original bounded set. The image of that bounded lift is exactly the original set. The same construction applies to \(\widetilde\pi=\pi q:A\to\mathcal R\).

Continuous descent of functionals gives algebraic bijections onto the indicated annihilators. Their strong topologies agree because for any bounded \(K\subset\mathcal R\) and an exact bounded lift \(\widetilde K\subset Q\),
\[
\sup_{x\in K}|\lambda(x)|
=\sup_{F\in\widetilde K}|(\pi'\lambda)(F)|.
\tag{AST3.3}
\]
The forward seminorm estimate follows by mapping any bounded set of \(Q\) to a bounded set of \(\mathcal R\). Thus
\[
\boxed{\pi':\mathcal R'_\beta\xrightarrow{\sim}S_O=N_O^\perp
\subset Q'_\beta,\qquad
\widetilde\pi':\mathcal R'_\beta\xrightarrow{\sim}A_O^\perp
\subset B.}
\tag{AST3.4}
\]
These are closed strong topological embeddings, and \(\widetilde\pi'=q'\pi'\). This proves the exact dual of the actual ACD source quotient.

GDC7’s independently checked restriction theorem now gives the strict exact rows
\[
0\to\mathcal R'_\beta\xrightarrow{\pi'}Q'_\beta
\xrightarrow{\mathrm{res}}(N_O)'_\beta\to0,
\]
\[
0\to\mathcal R'_\beta\xrightarrow{\widetilde\pi'}B
\xrightarrow{\mathrm{res}}(A_O)'_\beta\to0.
\tag{AST3.5}
\]
The restrictions are strongly open, not merely onto as vector maps. Their bounded dual families also have bounded lifts by the common Hahn–Banach seminorm estimate proved in GDC7. The embeddings, openness and bounded lifts used here have separate proofs; no continuous linear section is inferred.

## AST4. The actual pairing is strongly dense in this dual

The map \(\overline\beta_r:\mathcal R\to H_O\) is continuous and injective by (AST2.1). Its image is dense in \(H_O\): for a finite vector \(h\) on off-line zeros, prescribe the finite values
\(F(\rho^\#)=h_\rho/\overline{d_r(\rho)}\), with zero values elsewhere, using the already proved full-jet isolators. Formula (AST1.9) then gives exactly \(\beta_rF=h\). This proves Hilbert density, without claiming density of finite blocks in \(Q\).

Define the continuous linear transpose receiver
\[
\gamma_r:\overline{H_O}\to\mathcal R'_\beta,
\qquad
\gamma_r(\overline y)([F])=\langle\beta_rF,y\rangle_+.
\tag{AST4.1}
\]
It is injective by that density and has the exact comparison
\[
\pi'\gamma_r=\sigma_r|_{\overline{H_O}},\qquad
\widetilde\pi'\gamma_r=a_r|_{\overline{H_O}}.
\tag{AST4.2}
\]
The strong topological isomorphism in (AST3.4), together with GDC2’s proved strong closure, gives
\[
\overline{\gamma_r(\overline{H_O})}^{\,\beta}=\mathcal R'_\beta.
\tag{AST4.3}
\]
Thus the nondegenerate ACD pairing on \(\mathcal R\times\overline{H_O}\) now has its exact dual receiver. It need not exhaust that dual before closure.

Its Hilbert norm on the source is exactly
\[
\|[F]\|_r^2:=\|\overline\beta_r[F]\|_+^2
=\sum_{\rho\in\mathscr Z_O}m_\rho|d_r(\rho)|^2|F(\rho^\#)|^2
=\sum_{\rho\in\mathscr Z_O}m_\rho|d_r(\rho)|^2|F(\rho)|^2.
\tag{AST4.4}
\]
The second equality reindexes by \(\#\), using equal multiplicities and \(d_r(\rho^\#)=-d_r(\rho)\). Completion for this displayed norm is \(H_O\), via \(\overline\beta_r\). This norm topology is not equated with the original Fréchet quotient topology.

## AST5. The split dual receiver is the transpose of an actual primal subcomplex

At a pole, ACD’s actual primal object is
\[
\mathscr P_r=[\underline A^{-1}\xrightarrow{+b_r}i_*H^0].
\]
Its source kernel constructs the literal subcomplex
\[
\mathscr P_O=[\underline{A_O}^{-1}\xrightarrow{0}i_*H^0]
=\underline{A_O}[1]\oplus i_*H.
\tag{AST5.1}
\]
The map \(\mathscr P_O\to\mathscr P_r\) is inclusion on \(A_O\) and identity on \(H\). It is a chain map because \(b_r|_{A_O}=0\). Its literal quotient is the constant sheaf \(\underline{\mathcal R}[1]\), so there is a short exact sequence of the actual complexes
\[
0\to\mathscr P_O\longrightarrow\mathscr P_r
\xrightarrow{(\widetilde\pi,0)}\underline{\mathcal R}[1]\to0.
\tag{AST5.2}
\]
Each coefficient inclusion/quotient has its proved original topology. The quotient complex itself has zero differential. First define the ordinary short-exact-sequence boundary by differentiating a lifted cocycle with a positive sign. A stalk class \([a]\in H^{-1}(\underline{\mathcal R}[1])=\mathcal R\) lifts to \(a\in A=\mathscr P_r^{-1}\); its differential is \(+b_ra\in H=\mathscr P_O^0\). Changing the lift by \(v\in A_O\) changes this differential by \(b_rv=0\). Hence
\[
\delta_{\rm SES}([a])=+b_ra=+\overline\beta_r([a]).
\tag{AST5.2a}
\]
There is a separate sign in the retained mapping-cone convention. For the inclusion \(i:\mathscr P_O\to\mathscr P_r\), take
\(\operatorname{Cone}(i)^k=\mathscr P_r^k\oplus\mathscr P_O^{k+1}\),
\(d(v,u)=(dv+i u,-du)\), and last cone arrow given by positive projection to \(\mathscr P_O[1]\). The quasi-isomorphism from this cone to \(\underline{\mathcal R}[1]\) is the positive quotient on its \(\mathscr P_r\) coordinate. At the pole the cone has \(A\oplus H\) in degree \(-1\), with differential \((a,h)\mapsto b_ra+h\). The cocycle \((a,-b_ra)\) represents \([a]\), and its positive last projection is \(-b_ra\). Consequently the distinguished triangle with the literal positive quotient is
\[
\mathscr P_O\xrightarrow{i}\mathscr P_r
\xrightarrow{+\widetilde\pi}\underline{\mathcal R}[1]
\xrightarrow{\kappa_r}\mathscr P_O[1],\qquad
H^{-1}(i^*\kappa_r)=-\overline\beta_r=-\delta_{\rm SES}.
\tag{AST5.2b}
\]
Changing the quotient coordinate by \(-1_{\mathcal R}\) instead gives the isomorphic triangle with middle arrow \(-\widetilde\pi\), last arrow \(-\kappa_r\), and positive stalk boundary \(+\overline\beta_r\). Thus the positive differentiate-a-lift boundary and the stated cone projection have their exact coordinate comparison; their signs have not been identified silently.

Both signs of this map are continuous by the original quotient topology, injective, and dense in \(H_O\) by AST4. A lift of an individual class is all the calculation requires; it supplies no continuous section of \(A\to\mathcal R\). The actual localization boundary in (AST2.3) is \(-b_r\) because its restriction-fibre quotient coordinate is \(h-b_ra\). It agrees with \(H^{-1}(i^*\kappa_r)\widetilde\pi\) as a coefficient map, while the positive short-exact-sequence convention gives the negative of that map. These are distinct constructions with the stated exact relation.

Use ACD’s fine resolution with the minus de Rham differential. The inclusion of smooth \(A_O\)-valued forms into smooth \(A\)-valued forms and the identity on the point coefficient give a continuous fine-resolution map. Its literal compact-test transpose, with ACD’s degree signs \((-1,+1,-1)\) and Riesz identification, is
\[
\mathscr E_r\longrightarrow
\mathscr T_{A_O}[-1]\oplus i_*\overline H,
\qquad (u,x)\longmapsto(\iota_O^\vee u,x).
\tag{AST5.3}
\]
Here \(\mathscr E_r=\operatorname{Cone}(-\delta_pa_r)[-1]\). The target attaching map is zero because the coefficient restriction \(B\to(A_O)'\) kills \(a_r\). Explicitly \(\iota_O^\vee\delta_pa_r=\delta_p(a_r|_{A_O})=0\); hence the current differential commutes. This is exactly GDC10.3, now identified as the continuous transpose of (AST5.2)’s first map.

The compact-test contraction applies to the complete Fréchet coefficient \(A_O\), giving \(\mathscr T_{A_O}[-1]\simeq\underline{(A_O)'}[1]\). On underlying vector-space sheaves, (AST3.5) and cancellation of the common supported term give the exact receiver triangle
\[
\boxed{\underline{\mathcal R'}[1]\longrightarrow\mathscr E_r
\longrightarrow\underline{(A_O)'}[1]\oplus i_*\overline H
\longrightarrow\underline{\mathcal R'}[2].}
\tag{AST5.4}
\]
Under \(\widetilde\pi'\), its first coefficient is exactly \(A_O^\perp\), and the triangle is GDC10.4. For a direct verification of its fibre, form the two current Gysin triangles with common supported coordinate. Their comparison cancels that coordinate; compact-test contractions reduce the remaining comparison to the actual coefficient restriction \(B\to(A_O)'\), whose kernel is \(\mathcal R'\) by (AST3.5). The fibre is thus \(\underline{\mathcal R'}[1]\). No general exactness claim for strong duals of arbitrary complexes is used.

The positive costalk map is consequently
\[
[\overline H\xrightarrow{+a_r}B]
\longrightarrow[\overline H\xrightarrow{0}(A_O)'],
\qquad(x,b)\longmapsto(x,b|_{A_O}).
\tag{AST5.5}
\]
Its degree-one map is the separated quotient of the actual unseparated cohomology:
\[
B/a_rC\longrightarrow B/A_O^\perp\xrightarrow{\sim}(A_O)'_\beta,
\quad
\ker= A_O^\perp/a_rC.
\tag{AST5.6}
\]
That kernel is precisely the closure of zero in the original costalk quotient. The retained source \(\mathcal R\) and its dual kernel in (AST5.4) identify the exact cost of this split receiver.

## AST6. Parameter isomorphisms are actual transpose comparisons

For \(r,t>1\), retain GDC3’s bounded invertible diagonal map
\[
v_{r,t}(\rho)=
\begin{cases}
e^{-i\Im\rho\log(r/t)}
\dfrac{r^{\Re\rho}-r^{1-\Re\rho}}
{t^{\Re\rho}-t^{1-\Re\rho}},&\rho\in\mathscr Z_O,\\
1,&\rho\in\mathscr Z_L,
\end{cases}
\qquad V_{r,t}y=(v_{r,t}(\rho)y_\rho)_\rho.
\tag{AST6.1}
\]
Its explicit off-line modulus bounds are
\[
\frac{2\sqrt r\log r}{(t+1)\log t}
\le |v_{r,t}(\rho)|
\le\frac{(r+1)\log r}{2\sqrt t\log t};
\tag{AST6.2}
\]
on line coordinates its value is one. The nonzero constants prove bounded invertibility, even for zeros approaching the line. Put \(M_{r,t}=V_{r,t}^*\). Since \(D_r=D_tV_{r,t}\), taking Hilbert adjoints gives the exact identities
\[
\beta_r=M_{r,t}\beta_t,\qquad
b_r=M_{r,t}b_t,
\qquad \sigma_t\overline V_{r,t}=\sigma_r,
\qquad a_t\overline V_{r,t}=a_r.
\tag{AST6.3}
\]
In particular
\[
\mathscr P_t\xrightarrow{\ (1_A,M_{r,t})\ }\mathscr P_r,
\qquad
\mathscr E_r\xrightarrow{\ (1_B,\overline V_{r,t})\ }\mathscr E_t
\tag{AST6.4}
\]
are continuous cochain isomorphisms with inverses obtained by exchanging \(r,t\). The first has the same sign on its positive primal differential; the second has the same sign on its positive Gysin attaching term. They are literal continuous transposes under ACD’s pairing, because
\[
M_{r,t}'R(\overline y)(h)
=\langle M_{r,t}h,y\rangle_+
=\langle h,V_{r,t}y\rangle_+
=R(\overline V_{r,t}\overline y)(h).
\tag{AST6.5}
\]
The diagonal operators commute and satisfy the GDC cocycle identity, so these maps satisfy the corresponding compositional identities in their indicated directions. They fix \(A,A_O,Q,N_O,\mathcal R\), the entire nearby dual coefficient \(B\), and the line-supported coefficient \(H_L\) or \(\overline{H_L}\). They do not identify the numerical defect sizes for different parameters.

The localization boundary squares are now explicit:
\[
-b_r=M_{r,t}(-b_t),\qquad
1_A=1_A\,1_A,\qquad
a_r=a_t\overline V_{r,t}.
\tag{AST6.6}
\]
The induced map on the quotient \(\operatorname{coker}\operatorname{sp}_{-1}=\mathcal R\) is identity; its map between the displayed Hilbert images is \(M_{r,t}\). Its map on the dual source \(\mathcal R'\) in (AST5.4) is identity, and
\(\gamma_t\overline V_{r,t}=\gamma_r\) on \(\overline{H_O}\).

These parameter maps preserve the actual cover structures. For a recovered integer degree \(n\ge1\), \(V_{r,t}\) and \(M_{r,t}\) commute with every diagonal \(T_n,U_n\) and their Hilbert adjoints. Thus (AST6.4) commutes with the primal unit and weighted trace and the dual DCA maps, including their finite-sheet corrections. In DCA’s correction vector every occurrence of \(R_-a_r x\) equals \(R_-a_t\overline V_{r,t}x\), so all sheet coordinates commute, not merely their sums. The integer cover and its angular degree factors are retained; no geometric cover of noninteger degree is asserted.

## AST7. Both poles, the global specialization map and endpoints

At both poles use the same existing coefficient trivialization. The subcomplex construction becomes
\[
\mathscr P_O^Y=\underline{A_O}[1]\oplus i_+H\oplus i_-H
\longrightarrow
\mathscr P_r^Y=[\underline A^{-1}\xrightarrow{(b_r,b_r)}i_+H\oplus i_-H],
\tag{AST7.1}
\]
with quotient \(\underline{\mathcal R}_Y[1]\). The source and dual maps are identity on each original endpoint summand \(E_p[1]\) and \(E_p'[-1]\). Both distinct value-at-zero and integral labels remain; none enters the kernel \(N_O\) by a relabelling of a zeta endpoint.

In ACD6’s proved global finite model the parameter map is
\[
[A^{-1}\xrightarrow{(b_t,b_t)}H^0\oplus H^0\xrightarrow0A^1]
\longrightarrow
[A^{-1}\xrightarrow{(b_r,b_r)}H^0\oplus H^0\xrightarrow0A^1],
\]
\[
(1_A,M_{r,t}\oplus M_{r,t},1_A).
\tag{AST7.2}
\]
It induces identity on \(A_O\oplus E_+\oplus E_-\) in degree \(-1\), identity on \(A\) in degree one, and
\[
H\oplus(H/b_tA)\longrightarrow H\oplus(H/b_rA),
\quad(h,[k])\longmapsto(M_{r,t}h,[M_{r,t}k])
\tag{AST7.3}
\]
in degree zero. This is well defined with a continuous inverse because \(M_{r,t}b_tA=b_rA\), and quotient topology gives continuity even if these quotients are unseparated. The original global source map remains
\[
Q\longrightarrow H\oplus(H/b_rA),\qquad
F\longmapsto(\beta_rF,0),\qquad \ker=N_O.
\tag{AST7.4}
\]
Equations (AST6.3) and (AST7.3) prove its parameter compatibility on all original classes.

The dual finite global model has \(B^{-1}\), \(C^0\oplus C^0\), \(B^1\) and differential
\((x_+,x_-)\mapsto a_rx_++a_rx_-\). Its parameter map is identity on both \(B\) terms and \(\overline V_{r,t}\) on each point term. The two positive Dirac contributions remain a sum. Since GDC3 proves equality of the actual images \(a_rC=a_tC\), the degree-one quotient maps are literally identity on \(B/a_rC\), and their separated maps are identity on \((A_O)'\). Endpoints extend these statements by their identity maps. This proves preservation of the global receiving maps without declaring an anti-diagonal cancellation to be vanishing of the local attaching map.

## AST8. The restricted original extension and the surviving positive residue

The actual kernel source belongs to the strict original pullback row
\[
0\to J\to A_O\xrightarrow{q_O}N_O\to0.
\tag{AST8.1}
\]
Its continuous strong dual is, by GDC7,
\[
0\to(N_O)'_\beta\xrightarrow{q_O'}(A_O)'_\beta
\to J'_\beta\to0.
\tag{AST8.2}
\]
This row retains all of \(J\), in contrast to replacing the coefficient by a zeta value space. It also proves that the split receiver’s nearby coefficient still contains the dual of the source carrying all line values and all higher jets.

For completeness, its retained original residue is the proved exact restriction
\[
A_H(y)|_{N_O}(F)
=\sum_{\rho\in\mathscr Z_L}m_\rho F(\rho)\overline{y_\rho}
=\langle EF,P_Ly\rangle_+\qquad(F\in N_O).
\tag{AST8.3}
\]
It injects \(\overline{H_L}\) into \((N_O)'\), by testing each actual finite line-value isolator, and then into \((A_O)'\) through \(q_O'\). Precisely, \(N_O/N_0\), where \(N_0=\ker E\), with norm \(\|[F]\|=\|EF\|_+\), completes to \(H_L\) by GDC8.3. The injected \(H_L\) already is complete in its own Hilbert norm. Neither that norm nor that Hilbert image is identified with the full strong dual \((N_O)'\); the original higher-jet functionals remain present. The full source remains the exact extension \(0\to N_O\to Q\to\mathcal R\to0\); no source projector splitting this row has been constructed or assumed.

## AST9. Exact result and limits of the comparison

The actual ACD specialization source has now been identified as \(\mathcal R=Q/N_O\), with its original quotient topology. Its full strong dual is the closed GDC defect receiver \(S_O\), and its image in the original dual coefficient is \(A_O^\perp\). The original specialization map, its sign, its two-pole map and every parameter comparison commute with these identifications. The GDC split current receiver is the literal continuous transpose of the actual subcomplex (AST5.1); the discarded coefficient is retained as \(\underline{\mathcal R'}[1]\) in its exact triangle.

No existence or nonexistence of an off-line zero has entered this proof. If an actual off-line zero is present, its full-jet isolator makes its value class nonzero in \(\mathcal R\); if none is present then \(N_O=Q\) and \(\mathcal R=0\). These are exact statements about the proved receiver. They do not prove which case holds, impose a common weight, or turn the coefficient quotient into Deligne’s geometric inertia cross. What advances the comparison is the exhibited primal subcomplex, its quotient topology, its complete dual and its commuting specialization maps, all on the original arithmetic coefficients.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# The actual extension class in the original source and residue spaces

24 September 2026. Complete receiving derivation, ECR0–ECR7.

## ECR0. The constructed prerequisites and the attempted step

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The functions, complex coefficients and positive parameters in this calculation belong to the already reconstructed complete arithmetic receiver. None is an arithmetic value, parity, coordinate or addition assigned to \(\tau\). Separate branch histories and their coefficient records remain.

The complete received proofs are FOD0–FOD8 in [../tau_weight_cohomology_20260924/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md), SHA256 `0f16829aa955a3af1bd8b16d70851df5467040b9685d607a7a1b8aa3a0cae0a3`, and NEA0–NEA10 in [../tau_weight_cohomology_20260924/CC_NORMAL_EXTENSION_ANNIHILATOR.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_NORMAL_EXTENSION_ANNIHILATOR.md), SHA256 `817455b79efe7a3cdbb5310f760cfef86f5a9bc02a2498a116df0253c8f3172b`. Both were read completely for this receiving calculation. RTT0–RTT11, GTAH0–GTAH7 and GSR0–GSR4 supply the existing residue, adjoint and multiplier comparisons.

FOD proves the actual original extension
\[
e_0:\quad0\longrightarrow\mathcal I\longrightarrow\mathcal B
\longrightarrow\mathcal Q\longrightarrow0,
\qquad \mathcal Q=\mathcal B/\mathcal I,
\tag{ECR0.1}
\]
and its exact annihilator \(\mathfrak a\subset M\), the ideal of entire strip-polynomial multipliers vanishing at each actual nontrivial zeta zero \(\rho\) to multiplicity \(m_\rho\). The source ideal is \(\mathcal I=\mathcal B\cap\mathfrak a\), where \(\mathcal B\) is the entire rapid-strip space. Consequently
\[
\mathscr N_0=M e_0\simeq M/\mathfrak a,\qquad [h]\longmapsto h e_0.
\tag{ECR0.2}
\]
The symbol \(\mathscr N_0\) in this note is the cyclic extension-class module. RTT's value-zero kernel is written \(\mathcal N_{\rm jet}\) here to avoid a collision of names.

What would connect this new class module to the existing positivity calculation is a proved map into the actual source quotient and residue space, rather than assigning a norm to an unspecified Ext topology. We now construct a full family of such maps and calculate its effect on the original trace and on the measured adjoint defect.

## ECR1. Injective maps in both directions, with their full composites

For every \(t>0\), use the specified entire test function
\[
g_t(s)=\exp(t s^2).
\tag{ECR1.1}
\]
It is nowhere zero and belongs to \(\mathcal B\subset M\), because for \(|x|\le A\),
\[
(1+|y|)^N|g_t(x+iy)|
\le e^{tA^2}(1+|y|)^N e^{-ty^2},
\tag{ECR1.2}
\]
whose supremum is finite for every \(A,N\). If \(h\in M\) has growth exponent \(N_A\) on that strip, the same estimate with exponent \(N+N_A\) proves \(g_th\in\mathcal B\).

Define actual \(M\)-linear maps
\[
j:\mathcal Q\longrightarrow\mathscr N_0,
\quad [F]_{\mathcal I}\longmapsto F e_0,
\qquad
b_t:\mathscr N_0\longrightarrow\mathcal Q,
\quad h e_0\longmapsto[g_t h]_{\mathcal I}.
\tag{ECR1.3}
\]
For \(j\), the kernel condition is exactly \(\mathcal B\cap\mathfrak a=\mathcal I\). For \(b_t\), a change of representative by \(\mathfrak a\) changes the product by \(\mathcal I\), so it is well defined. If \(g_t h\in\mathcal I\), the fact that \(g_t\) is a unit in every local holomorphic ring forces the full vanishing order of \(h\) at every original zero. Hence \(h\in\mathfrak a\). Both maps are therefore injective, with every multiplicity coordinate retained. Their composites are exactly
\[
j b_t=m_{g_t}\quad\hbox{on }\mathscr N_0,
\qquad b_t j=m_{g_t}\quad\hbox{on }\mathcal Q.
\tag{ECR1.4}
\]
These are not identity maps. No topology is imposed on the ambient Ext group or on \(M/\mathfrak a\).

Neither embedding in (ECR1.3) is surjective. If \(e_0\) were in the image of \(j\), an \(F\in\mathcal B\) would have \(F(\rho)=1\) at every nontrivial zero. The unbounded imaginary parts of the actual zeta zeros and rapid strip decay contradict this. Here unboundedness follows from the established zero-count asymptotic for the original zeta, not an off-line-zero assertion. If \([g_{t/2}]\) were in the image of \(b_t\), some \(h\in M\) would satisfy
\[
h(\rho)=g_{t/2}(\rho)/g_t(\rho)=e^{-t\rho^2/2}.
\tag{ECR1.5}
\]
Writing \(\rho=\sigma+i\gamma\), its modulus is \(e^{t(\gamma^2-\sigma^2)/2}\). Since \(0<\sigma<1\) and \(|\gamma|\) is unbounded, it cannot obey a polynomial bound on the fixed zero strip. This proves the second nonsurjectivity. The same argument applied to \(g_t h=1\) modulo \(\mathfrak a\) proves that \([g_t]\) is not a unit in \(M/\mathfrak a\). Its absence of zeros does not license division in this multiplier quotient.

## ECR2. Every local jet and the exact relation between test parameters

At an actual zero \(\rho\) of multiplicity \(m\), put \(z=s-\rho\). The complete multiplier is
\[
g_t(\rho+z)=e^{t\rho^2}e^{2t\rho z}e^{tz^2},
\qquad
[z^r]g_t(\rho+z)
=e^{t\rho^2}\sum_{v=0}^{\lfloor r/2\rfloor}
\frac{(2t\rho)^{r-2v}t^v}{(r-2v)!v!}.
\tag{ECR2.1}
\]
Thus on the entire multiplicity block, the matrix of \(b_t\) in ordinary Taylor coordinates is lower triangular with entry \([z^{i-j}]g_t(\rho+z)\) for \(i\ge j\), and zero otherwise. Its determinant is \(e^{mt\rho^2}\ne0\). Its local inverse retains all coefficients of \(e^{-t\rho^2}e^{-2t\rho z}e^{-tz^2}\), truncated only at the stated length \(m\). This is a local finite-length inverse, not an inverse in \(M\) or of either global embedding.

For \(u>t>0\), the full global identity is
\[
g_u=g_{u-t}g_t,\qquad b_u=m_{g_{u-t}}b_t.
\tag{ECR2.2}
\]
All multipliers in this formula belong to \(\mathcal B\subset M\). It compares the entire family without identifying its different test functions or cancelling any factor.

## ECR3. The actual source representative

The original half-Mellin map is the already proved isomorphism
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},
\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+iy)u^{-iy}\,dy.
\tag{ECR3.1}
\]
For the extension-class representative \(h\), the actual source of \(b_t(h e_0)\) is
\[
a_{t,h}(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}e^{t(1/2+iy)^2}h(1/2+iy)u^{-iy}\,dy.
\tag{ECR3.2}
\]
Gaussian decay and polynomial strip growth prove absolute convergence after every fixed number of logarithmic derivatives; (ECR1.2) and the full inverse-Mellin estimates give every source seminorm. This is the entire actual source space \(A\), not necessarily its subspace \(J\).

For the actual generator \(e_0\), retain the elementary Gaussian integral explicitly:
\[
a_{t,1}(u)=\frac{e^{t/4}}{\sqrt{\pi t}}u^{-1/2}
\exp\!\left(-\frac{(\log u-t)^2}{4t}\right).
\tag{ECR3.3}
\]
Indeed \(e^{t(1/2+iy)^2}=e^{t/4}e^{-ty^2}e^{ity}\), and integrating \(e^{-ty^2}e^{-iy(\log u-t)}\) gives \(\sqrt{\pi/t}\exp(- (\log u-t)^2/(4t))\). Every original factor in (ECR3.1) remains. This is a chosen source test, not a replacement of the original zeta or its theta transform.

## ECR4. Exact residue and full original Weil pairing

Let \(\mathsf S:\mathcal Q\to\mathcal H_{\rm res}\) be RTT5's continuous anti-linear residue receiver. The actual map on extension classes is
\[
\mathsf S_t=\mathsf S b_t:\mathscr N_0\longrightarrow\mathcal H_{\rm res}.
\tag{ECR4.1}
\]
No continuity relative to an unspecified topology on \(\mathscr N_0\) is claimed. Introduce the value-vanishing ideal
\[
\mathfrak a_{\rm val}=\{h\in M:h(\rho)=0\text{ for all actual }\rho\}.
\tag{ECR4.2}
\]
RTT5 gives precisely
\[
\ker\mathsf S_t=\mathfrak a_{\rm val}/\mathfrak a
\quad\text{under (ECR0.2)}.
\tag{ECR4.3}
\]
The reason is \(g_t(\rho)\ne0\) for every zero. This kernel has zero constant coordinate in every multiplicity block, but we do not identify it with the global nilradical without a proof controlling all multiplicities simultaneously.

Put \(\rho^\#=1-\overline\rho\). RTT5 now gives the full exact formula
\[
\begin{aligned}
W_t(h,k)
&=\widehat{\mathcal R}\bigl(b_t(h e_0),\mathsf S_t(k e_0)\bigr)\\
&=\sum_\rho m_\rho
e^{t\{\rho^2+(1-\rho)^2\}}
h(\rho)\overline{k(\rho^\#)}.
\end{aligned}
\tag{ECR4.4}
\]
The exponential factor follows from
\(g_t(\rho)\overline{g_t(\rho^\#)}=e^{t\rho^2}e^{t(1-\rho)^2}\); it has not been replaced by one or by a real modulus. Absolute convergence follows from the Gaussian decay, polynomial multiplier bounds and the original zero-count estimate. This proves a Hermitian form by transport of the established form, or directly by exchanging \(\rho\) and \(\rho^\#\).

For completeness its complete arithmetic receiver has the original entire test
\[
A_{t,h,k}(s)=e^{t\{s^2+(1-s)^2\}}
h(s)\overline{k(1-\overline s)}.
\tag{ECR4.5}
\]
Let \(v_{t,h,k}\) be its actual logarithmic inverse transform, with
\(A(s)=\int_{\mathbb R}v(v_0)e^{-(s-1/2)v_0}\,dv_0\) and
\(\widehat v(y)=\int v(v_0)e^{-iyv_0}\,dv_0\). It belongs to the complete source test space by (ECR3.2), reflection, and the convolution proof in GIQ9, reread for this calculation. Then
\[
W_t(h,k)=A(0)+A(1)+\mathcal A_\infty(v)-P_{\rm hist}(v),
\tag{ECR4.6}
\]
where the full terms are
\[
\mathcal A_\infty(v)=\frac1{2\pi}\int_{\mathbb R}\widehat v(y)
\left(\Re\frac{\Gamma'(1/4+iy/2)}{\Gamma(1/4+iy/2)}-\log\pi\right)dy,
\]
\[
P_{\rm hist}(v)=\sum_{n\ge2}\frac{\log L_n-\log L_{n-1}}{\sqrt n}
\bigl(v(\log n)+v(-\log n)\bigr),\qquad
L_n=\operatorname{lcm}(1,\ldots,n).
\tag{ECR4.7}
\]
In particular \(A(0)=e^t h(0)\overline{k(1)}\) and
\(A(1)=e^t h(1)\overline{k(0)}\). The original pole and trivial divisor remain at every finite cutoff \(B\):
\[
V_{\zeta,B}=W_t(h,k)+\sum_{r=1}^B A(-2r)-A(1),
\qquad
G_B=\mathcal A_\infty(v)+A(0)+\sum_{r=1}^B A(-2r),
\]
\[
V_{\zeta,B}=G_B-P_{\rm hist}(v),\qquad
A(-2r)=e^{t\{4r^2+(1+2r)^2\}}h(-2r)\overline{k(1+2r)}.
\tag{ECR4.8}
\]
No divergent infinite trivial-zero sum is asserted. GIQ9 proves convergence of all the other displayed complete sums and the full source-domain extension of the explicit formula.

## ECR5. The positive value form and exact defect on the actual class module

The positive auxiliary form pulled back by the actual embedding is
\[
\langle h e_0,k e_0\rangle_t
=\sum_\rho m_\rho e^{2t\Re(\rho^2)}
h(\rho)\overline{k(\rho)}.
\tag{ECR5.1}
\]
It converges absolutely by the same estimates, and has exactly the kernel in (ECR4.3). It is positive semidefinite, since its diagonal is a sum of nonnegative terms with strictly positive coefficients. All these value-zero classes remain in the original extension-class module and in the full jet injection \(b_t\).

For every recovered \(a>0\), retain the coefficient actions
\[
T_a(h e_0)=a^s h e_0,\qquad U_a(h e_0)=a^{1-s}h e_0.
\tag{ECR5.2}
\]
Both multipliers are in \(M\), and \(b_t\) commutes with them because all these are pointwise multipliers. Thus the coefficient transfer is preserved for every \(a>0\). For \(a=n\) a positive integer, GTR's actual degree-\(n\) covering realizes this as its geometric transfer. No covering with nonintegral degree is asserted. The full coefficient identities are
\[
W_t(T_a x,y)=W_t(x,U_a y),\qquad U_aT_a=aI.
\tag{ECR5.3}
\]
These follow either by transport through \(b_t\) or directly from the full sum (ECR4.4).

On the established value Hilbert space, \(D_a=T_a^*-U_a\) has multiplier
\(e^{-i\gamma\log a}(a^\sigma-a^{1-\sigma})\), where \(\rho=\sigma+i\gamma\). Its exact pullback to the cyclic class module is
\[
\mathfrak d_{a,t}(h e_0,k e_0)
=\sum_\rho m_\rho e^{2t(\sigma^2-\gamma^2)}
(a^\sigma-a^{1-\sigma})^2h(\rho)\overline{k(\rho)}.
\tag{ECR5.4}
\]
This is \(\langle D_aE_0b_t(h e_0),D_aE_0b_t(k e_0)\rangle\), so it is positive semidefinite with its actual source map exhibited. For fixed \(a>1\), the squared factor is at most \((a-1)^2\), while \(e^{2t\sigma^2}\le e^{2t}\). These inequalities and polynomial multiplier growth prove convergence over all actual zeros. No nonholomorphic multiplier has been substituted into (ECR4.6).

For the particular actual extension generator the formula is
\[
\mathfrak d_{a,t}(e_0,e_0)
=\sum_\rho m_\rho e^{2t(\sigma^2-\gamma^2)}
(a^\sigma-a^{1-\sigma})^2.
\tag{ECR5.5}
\]
Every term is nonnegative, and for \(a>1\) its vanishing is equivalent to \(\sigma=1/2\). Thus this single actual class tests the entire measured defect; it is not a finite zero sample. This computes an exact detection property, not the vanishing of the sum. The coefficient is the full original-source Gaussian weight, including \(e^{2t\sigma^2}\).

## ECR6. What the separator and the full source extension do to this test

FOD proves \(c e_0=e_0\), \(c e_+=0\), and the decomposition of the full joint class into the low and high components, retaining its intersection kernel. By \(M\)-linearity, (ECR1.3) therefore gives
\[
b_t(c x)=b_t(x),\qquad \mathsf S_t(c x)=\mathsf S_t(x),
\qquad
\mathfrak d_{a,t}(c x,c y)=\mathfrak d_{a,t}(x,y)
\quad(x,y\in\mathscr N_0).
\tag{ECR6.1}
\]
The annihilation of the high component is consequently compatible with, and does not cancel, the surviving defect of the original component. The connecting map is the one actually proved in FOD3: pushout takes the low component to \(e_0\) and induces an isomorphism on their cyclic modules because both annihilators are \(\mathfrak a\). Composing that isomorphism with \(b_t\) and \(\mathsf S_t\) supplies the same formulas directly on the actual low source-extension component. Its full kernel \(\mathcal I\cap\mathcal I_+\) remains in that extension.

The two normal and original components have separate degree actions. Transport of the normal source by \(\lambda=s+1\) has character \(a^{s+1}\), not \(a^s\). No cancellation between their norms or trace terms follows by erasing that extra factor. The complete involution and degree comparison is calculated separately in the receiving extension-class involution note.

## ECR7. Scope and the next receiving step

This calculation places the actual extension-class module into the entire original source by explicit proper embeddings, preserves every local jet, and maps its value trace into the complete residue space. It exhibits the actual extension generator as a global test of the previously measured positive-adjoint defect. The full original-zeta arithmetic formula, pole, Gamma, endpoints and finite trivial-divisor terms remain (ECR4.6)–(ECR4.8).

The multiplier that annihilates the normal localization component leaves this original class and its defect fixed. What would advance the purity argument is therefore additional control on the original component through the actual involution and duality, with both degree actions retained. The separate extension-class involution calculation is being carried out on these modules; its result must be compared using the maps (ECR1.3) and (ECR4.1), rather than by assigning a positive form to an unconstructed Ext topology. No claim of Deligne weight purity or RH is made by the detection identity (ECR5.5).


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Involutions of the actual extension-class modules and their original-zeta residue maps

24 September 2026. Complete independent derivation ECI0–ECI13.

## ECI0. The constructed objects and the next calculation

The support remains \(\tau\langle Z_1;\text{no }Z_2\rangle\). All scalars, functions, modules and dual operations below occur after complete-history arithmetic reconstruction. The two branch counters remain separate. Addition at \(\tau\) remains retracted, and no numerical coordinate, midpoint, metric or parity is assigned to it. The current corpus-and-operation rule and `READ_FIRST_USER_CONSTRUCTION.md` were read again before selecting these operations. The amended forward-step rule asks for an actual next calculation using all established findings. Here that calculation is the involution and duality of the actual cyclic extension modules just constructed, followed by their map to the existing residue receiver.

The complete FOD0–FOD8 and NEA0–NEA10 proofs were read, together with the already checked GMS, GSR, RTT and GTAH comparisons. Their exact annihilator statements are used, not an assumption that the full normal ideal has a quotient's spectrum. Write
\[
M=\{h\text{ entire}:\text{on each bounded real strip, }h
\text{ has at most polynomial vertical growth}\},
\]
\[
\mathcal B=\{F\text{ entire}:b_{A,N}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty
\text{ for every }A,N\}.
\tag{ECI0.1}
\]
For every actual original nontrivial zero \(\rho\) of \(\zeta\), retain its full multiplicity \(m_\rho\). The ideals are
\[
\mathfrak a=\{h\in M:\operatorname{ord}_\rho h\ge m_\rho\ \forall\rho\},
\quad
\mathfrak a_+=\{h\in M:\operatorname{ord}_{\rho+1}h\ge m_\rho\ \forall\rho\},
\]
\[
\mathcal I=\mathcal B\cap\mathfrak a,
\quad\mathcal I_+=\mathcal B\cap\mathfrak a_+,
\quad\mathcal Q=\mathcal B/\mathcal I,
\quad\mathcal Q_+=\mathcal B/\mathcal I_+,
\]
\[
\mathscr C=M/\mathfrak a,
\qquad\mathscr C_+=M/\mathfrak a_+.
\tag{ECI0.2}
\]
FOD and NEA prove the identifications
\[
\mathscr C\simeq M e_0\simeq M e_{\rm low},\qquad
\mathscr C_+\simeq M e_+\simeq M e_{\rm high}\simeq M\delta.
\tag{ECI0.3}
\]
Each sends \([h]\) to the displayed actual class multiplied by \(h\). The generator \(e_0\) is the original source row, \(e_+\) is the actual normal source row, and \(\delta\) is the actual localization boundary with the shifts retained in FOD7 and NEA10. These are isomorphisms of the cyclic images only, not of full Ext groups or full source ideals. No unproved locally convex topology is assigned to \(M\), \(\mathscr C\), or \(\mathscr C_+\). Their embeddings of \(\mathcal Q\) and \(\mathcal Q_+\) remain the injective maps induced by \(\mathcal B\subset M\).

## ECI1. Conjugation, reflection, and the two distinct Weil involutions

On the original coordinate define
\[
\mathsf C h(s)=\overline{h(\overline s)},\qquad
\mathsf R_1h(s)=h(1-s),\qquad
\mathsf K_1h(s)=h^{\#_1}(s)=\overline{h(1-\overline s)}.
\tag{ECI1.1}
\]
The first and third maps are anti-linear, the second is linear, and \(\mathsf K_1=\mathsf C\mathsf R_1=\mathsf R_1\mathsf C\). Taylor expansion proves that their outputs are entire. A strip of width \(A\) is carried into one of width at most \(A+1\); imaginary parts only change sign. Thus each preserves \(M\) and is continuous on \(\mathcal B\). Each is multiplicative and involutive, with the appropriate conjugation of complex scalars.

The actual original functional equation and conjugation give the multiplicity-preserving permutations \(\rho\mapsto\overline\rho\), \(\rho\mapsto1-\rho\), and \(\rho\mapsto\rho^\#=1-\overline\rho\). Hence all three maps preserve \(\mathfrak a\) and \(\mathcal I\), and induce the corresponding maps on \(\mathscr C\) and \(\mathcal Q\). In full local jets,
\[
j_\rho(\mathsf K_1h)=
\sum_{j=0}^{m_\rho-1}
\frac{(-1)^j\overline{h^{(j)}(\rho^\#)}}{j!}(s-\rho)^j.
\tag{ECI1.2}
\]
This is the complete jet map, not only its value.

In the translated normal coordinate \(\lambda\), the corresponding maps are
\[
\mathsf R_3h(\lambda)=h(3-\lambda),\qquad
\mathsf K_3h(\lambda)=h^{\#_3}(\lambda)=
\overline{h(3-\overline\lambda)}.
\tag{ECI1.3}
\]
Conjugation remains \(\mathsf C h(\lambda)=\overline{h(\overline\lambda)}\). These preserve \(\mathfrak a_+\) and \(\mathcal I_+\), since
\[
3-\overline{(\rho+1)}=\rho^\#+1.
\tag{ECI1.4}
\]
Formula (ECI1.2) holds with \(\rho,\rho^\#\) replaced by \(\rho+1,\rho^\#+1\), with exactly the same factorials and signs. In particular \(\#_1\) must not be used as the normal involution without coordinate transport. It carries the translated divisor to \(\mathscr Z-1\), since \(1-\overline{(\rho+1)}=\rho^\#-1\). Likewise \(\#_3\) carries the unshifted divisor to \(\mathscr Z+2\). These are exact maps to other translated ideals, not identifications with the original ideal.

The induced operations on the cyclic extension modules are, for example,
\[
\mathsf K_{e_0}(h e_0)=h^{\#_1}e_0,
\qquad
\mathsf K_{e_+}(h e_+)=h^{\#_3}e_+.
\tag{ECI1.5}
\]
Well-definedness is precisely invariance of the proved annihilator ideals. On the actual original row, the anti-linear semilinear maps \(\mathsf K_1\) on its kernel, middle module and quotient commute with the inclusion and quotient maps. On the normal row the analogous statement uses \(\mathsf K_3\). Consequently these are also the maps on the cyclic classes obtained by applying those explicit semilinear exact equivalences to the rows, fixing the respective generator. No homological sign is introduced by this covariant exact operation. Transport to the low and high class modules uses the exact cyclic pushout isomorphisms (ECI0.3); it does not claim that \(\mathsf K_1\) alone preserves the full intersection ideal of the joint row.

## ECI2. Translation and every scalar degree

Retain the actual maps
\[
(Vh)(\lambda)=h(\lambda-1),\qquad
(Uk)(s)=k(s+1),\qquad UV=VU=1.
\tag{ECI2.1}
\]
They preserve polynomial strip bounds and rapid strip bounds, using strips enlarged by one. They give inverse ring isomorphisms \(M_s\leftrightarrow M_\lambda\), take \(\mathfrak a\leftrightarrow\mathfrak a_+\), and induce inverse maps \(\mathscr C\leftrightarrow\mathscr C_+\), as well as the established topological maps \(\mathcal Q\leftrightarrow\mathcal Q_+\). They are semilinear for this translation of scalars:
\[
V(hx)=(Vh)(Vx).
\tag{ECI2.2}
\]
Equivalently, equip the unshifted normal module with the actual action \(h\cdot x=h(s+1)x(s)\); then \(V\) is \(M\)-linear to the normal module in the \(\lambda\)-coordinate.

Direct substitution proves
\[
\mathsf C V=V\mathsf C,
\quad\mathsf R_3V=V\mathsf R_1,
\quad\mathsf K_3V=V\mathsf K_1.
\tag{ECI2.3}
\]
Under (ECI0.3), \(h e_0\mapsto(Vh)e_+\) is the corresponding semilinear isomorphism of cyclic extension modules. At the level of the actual rows it is induced by translating the entire original source sequence, including its kernel. It is not the identity on the scalar ring's coordinate.

Write \(L[h]=[sh]\), \(L_+[k]=[\lambda k]\), \(D_a[h]=[a^s h]\), and \(D_a^+[k]=[a^\lambda k]\), for every already recovered \(a>0\). Then
\[
L_+V=V(L+1),\qquad
D_a^+V=aVD_a,\qquad
UD_a^+=aD_aU.
\tag{ECI2.4}
\]
Their involution identities are
\[
\mathsf K_1L=(1-L)\mathsf K_1,
\qquad\mathsf K_3L_+=(3-L_+)\mathsf K_3,
\]
\[
\boxed{\mathsf K_1D_a=aD_{1/a}\mathsf K_1,
\qquad\mathsf K_3D_a^+=a^3D_{1/a}^+\mathsf K_3.}
\tag{ECI2.5}
\]
Both scalar degree factors follow by substituting the full coordinate in the exponential; neither is selected from a desired weight. On a length-\(m_\rho\) block they retain
\[
D_a=a^\rho\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}M_t^j,
\qquad
D_a^+=a^{\rho+1}\sum_{j=0}^{m_\rho-1}
\frac{(\log a)^j}{j!}M_t^j.
\tag{ECI2.6}
\]
Translation leaves the local parameter \(t\) unchanged; the reflected anti-linear jet map changes it to \(-t\) while conjugating coefficients as in (ECI1.2). These formulas retain every nilpotent term.

## ECI3. The joint class module has a componentwise involution with an explicit source representative

FOD proves \(c\in\mathfrak a_+\), \(1-c\in\mathfrak a\), and
\[
M/(\mathfrak a\cap\mathfrak a_+)\xrightarrow{\sim}
\mathscr C\oplus\mathscr C_+,
\qquad[h]\mapsto([h]_{\mathfrak a},[h]_{\mathfrak a_+}),
\tag{ECI3.1}
\]
with inverse \(([f],[g])\mapsto[cf+(1-c)g]\). The componentwise operation \((x,y)\mapsto(\mathsf K_1x,\mathsf K_3y)\) therefore induces an exact anti-linear multiplicative involution on the actual joint cyclic module. In the single quotient presentation it is
\[
[h]\longmapsto[c h^{\#_1}+(1-c)h^{\#_3}]
\quad\bmod(\mathfrak a\cap\mathfrak a_+).
\tag{ECI3.2}
\]
If a representative changes by the intersection ideal, the first component of its \(\#_1\) change vanishes in \(\mathscr C\), and the second component of its \(\#_3\) change vanishes in \(\mathscr C_+\). The separator kills the opposite components. This proves well-definedness directly. Multiplicativity and the square identity follow from (ECI3.1) on both components. In particular the two actual component idempotents represented by \(c\) and \(1-c\) are fixed.

There is an actual anti-linear continuous source representative on \(\mathcal B\):
\[
\mathsf A_cF=c\mathsf K_1F+(1-c)\mathsf K_3F.
\tag{ECI3.3}
\]
It preserves \(\mathcal K=\mathcal I\cap\mathcal I_+\), by exactly the preceding full-jet argument, and induces the componentwise involution on \(\mathcal B/\mathcal K\). Its complete square before quotient is
\[
\begin{aligned}
\mathsf A_c^2F={}&
\bigl[c c^{\#_1}+(1-c)(1-c)^{\#_3}\bigr]F\\
&+c(1-c)^{\#_1}F(s+2)
+(1-c)c^{\#_3}F(s-2).
\end{aligned}
\tag{ECI3.4}
\]
This follows by expanding the four terms and using \(\mathsf K_1\mathsf K_3F=F(s+2)\), \(\mathsf K_3\mathsf K_1F=F(s-2)\). Each cross-term multiplier vanishes to the full orders at both required divisors. The coefficient of \(F\), minus one, does as well. Thus \(\mathsf A_c^2F-F\in\mathcal K\), with the entire difference displayed. No equality \(\mathsf A_c^2=1\) on \(\mathcal B\), and no single scalar-ring involution preserving the whole original and normal row at once, has been assumed. The actual full-source extension and this explicit error remain available.

## ECI4. The dual involution on the strong residue receiver contains the functional-equation unit

Retain RTT's \(\widehat\iota:\mathcal H_{\rm res}\xrightarrow{\sim}\mathcal Q'_\beta\). The continuous anti-linear involution \(\mathsf K_1\) on \(\mathcal Q\) induces
\[
(\mathsf K_1^\vee\lambda)(F)=\overline{\lambda(\mathsf K_1F)},
\qquad\mathsf K_1^\vee:\mathcal Q'_\beta\to\mathcal Q'_\beta.
\tag{ECI4.1}
\]
The value is linear in \(F\), anti-linear in \(\lambda\), and the square is the identity. For a bounded \(B\subset\mathcal Q\), its strong seminorm is \(p_{\mathsf K_1B}(\lambda)\). Thus it is strong-continuous. Define the actual continuous involution
\[
\mathsf K_{\rm res}=\widehat\iota^{-1}\mathsf K_1^\vee\widehat\iota.
\tag{ECI4.2}
\]
This definition is on the full completion and requires no global meromorphic multiplier theorem.

Its finite-jet formula retains a nontrivial unit and sign. Original zeta has
\[
\zeta(s)=\chi(s)\zeta(1-s),\qquad
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)}.
\tag{ECI4.3}
\]
For finite-support \(g\), conjugating its residue pairing against \(\mathsf K_1F\), using \(\overline{\zeta(\overline s)}=\zeta(s)\), and then substituting \(s=1-z\), gives
\[
\begin{aligned}
(\mathsf K_1^\vee\iota g)(F)
&=\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(1-s)(\mathsf Cg)(1-s)}{\zeta(s)}\,ds\\
&=-\sum_\rho\operatorname{Res}_{s=\rho}
\frac{F(s)(\mathsf Cg)(s)\chi(s)}{\zeta(s)}\,ds.
\end{aligned}
\tag{ECI4.4}
\]
The minus sign is the derivative of the reflection. Accordingly \(\mathsf K_{\rm res}g\) is the unique finite-support class with local jets
\[
\boxed{j_\sigma(\mathsf K_{\rm res}g)
=j_\sigma\bigl[-\chi(1-s)g^{\#_1}(s)\bigr].}
\tag{ECI4.5}
\]
Every required germ of \(\chi(1-s)\) is a holomorphic unit; RD's global finite isolators realize those jets. Their derivatives are included in the product in (ECI4.5), not replaced by the unit's value. The formula does not assert that its meromorphic expression on the entire plane preserves \(\mathcal B\). The extension to the full residue completion is instead already proved by (ECI4.1)–(ECI4.2). Locally its square is also directly one, since \(\chi(1-s)\chi(s)=1\) and the two minus signs cancel.

For reference, conjugation alone on the dual, \(\lambda\mapsto(F\mapsto\overline{\lambda(\mathsf CF)})\), corresponds on finite residue classes to \(g\mapsto\mathsf Cg\). Linear reflection on the dual corresponds to local jets \(-\chi(1-s)g(1-s)\). These follow by the same computation without one of its conjugations. Thus the source involution and its actual residue-dual representative have a proved morphism retaining their functional-equation defect; they are not silently identified.

## ECI5. Every cyclic class has a canonical original-zeta trace functional

An element \([h]\in\mathscr C\) need not be in the rapid-decay quotient \(\mathcal Q\). Nevertheless the exact expression
\[
\mathsf W_M([h])(F)
=\sum_\rho m_\rho F(\rho)\overline{h(\rho^\#)},
\qquad F\in\mathcal Q,
\tag{ECI5.1}
\]
defines a continuous complex-linear functional on \(\mathcal Q\). It is anti-linear in \([h]\). To prove the assertion with its topology, let \(w_\rho=1+|\Im\rho|\). The strip bound for this particular \(h\) gives \(|h(\rho^\#)|\le Cw_\rho^d\). For every integer \(k\ge0\),
\[
E_k:\mathcal Q\to H,\qquad (E_kF)_\rho=w_\rho^kF(\rho)
\tag{ECI5.2}
\]
is continuous: its squared norm is bounded on \(\mathcal B\) by \(b_{1,k+2}(F)^2\sum_\rho m_\rho w_\rho^{-4}\), and it kills \(\mathcal I\). Choose \(k\ge d+2\). Cauchy–Schwarz gives
\[
|\mathsf W_M([h])(F)|
\le\|E_kF\|_+
\left(\sum_\rho m_\rho w_\rho^{-2k}|h(\rho^\#)|^2\right)^{1/2}<\infty.
\tag{ECI5.3}
\]
The unconditional full zero count makes the last sum finite. This proves both absolute convergence and continuity on the actual quotient. Changing \(h\) by \(\mathfrak a\), or \(F\) by \(\mathcal I\), changes no term.

Define
\[
\boxed{\mathsf S_M=\widehat\iota^{-1}\mathsf W_M:
\mathscr C\longrightarrow\mathcal H_{\rm res}.}
\tag{ECI5.4}
\]
This is an anti-linear map from the specified algebraic module; no continuity claim is made for an unassigned topology on \(\mathscr C\). Its restriction along \(\mathcal Q\hookrightarrow\mathscr C\) is exactly the already proved continuous map \(\mathsf S\) from RTT.

There is an exact strong residue realization of every value in (ECI5.4). For finite \(E\subset\mathscr Z\), put
\[
r_E(h)=\sum_{\rho\in E}
m_\rho(-1)^{m_\rho-1}u_\rho(0)
\overline{h(\rho^\#)}e_{1-\rho,m_\rho-1},
\qquad
\zeta(\rho+t)=t^{m_\rho}u_\rho(t).
\tag{ECI5.5}
\]
Its residue functional is the finite partial sum in (ECI5.1), by RTT's exact local matrix. For a bounded \(B\subset\mathcal Q\), the tail seminorm is at most
\[
\sup_{F\in B}\|E_kF\|_+
\left(\sum_{\rho\notin E}m_\rho w_\rho^{-2k}|h(\rho^\#)|^2\right)^{1/2}
\longrightarrow0.
\tag{ECI5.6}
\]
This proves strong convergence in the entire residue receiver. No density of finite-support primal classes, chosen Gaussian window, or unproved infinite residue series is needed.

Let \(\mathfrak r=\{h\in M:h(\rho)=0\ \forall\rho\}\). Global isolators tested in (ECI5.1) give the exact kernel
\[
\ker\mathsf S_M=\mathfrak r/\mathfrak a.
\tag{ECI5.7}
\]
Locally this is the higher-jet ideal in every multiplicity block. No uniform nilpotence exponent, or equality with an algebraic nilradical when multiplicities are unbounded, is asserted globally. Each original zero value survives.

## ECI6. A full-jet primal multiplier on the cyclic module, and involution covariance

The multiplier \(H_\zeta=s^2\zeta'(1-s)\) belongs to \(M\) by RTT2's full Euler–Maclaurin estimate, and \(H_\zeta(0)=-1\). The original \(F_0\in\mathfrak a\) has \(F_0(0)=1/8\). Thus
\[
[h]\longmapsto
\left[\frac{h(s)-F_0(s)h(0)/F_0(0)}s\right]
\tag{ECI6.1}
\]
is the inverse of \(L\) on the entire \(\mathscr C\). Entire division at the one removable point preserves the polynomial strip bounds, and the same local argument preserves \(\mathfrak a\). The two inverse identities follow by multiplication, exactly as in NEA7 and RTT2. This constructs
\[
\mathsf P_M=L^{-2}M_{s^2\zeta'(1-s)}\mathsf C:
\mathscr C\to\mathscr C.
\tag{ECI6.2}
\]
Its full local germ at a zero is \(\zeta'(1-s)\overline{h(\overline s)}\). If the output zero is \(\sigma\), put \(\rho=1-\sigma\), \(m=m_\rho\). Then
\[
j_\sigma(\mathsf P_Mh)=
m(-1)^{m-1}u_\rho(0)\overline{h(\overline\sigma)}(s-\sigma)^{m-1}.
\tag{ECI6.3}
\]
The proof differentiates \(\zeta(\rho-t)=(-t)^mu_\rho(-t)\) with respect to its own argument before taking the full quotient jet, as in RTT3. The coefficient is nonzero, so the block map has rank one, with the exact kernel of all positive-order input jets. Its global kernel is again \(\mathfrak r/\mathfrak a\). The map restricts to RTT's continuous \(\mathsf P\) on \(\mathcal Q\); the target is otherwise the explicitly algebraic module \(\mathscr C\).

For any \(b,h\in M\), the full convergent trace formula proves
\[
\widehat\iota\mathsf S_M(bh)
=m_{b^{\#_1}}'\widehat\iota\mathsf S_M(h).
\tag{ECI6.4}
\]
The transpose acts on the original continuous dual; its strong continuity follows because the multiplier on \(\mathcal Q\) preserves bounded sets. This is the extended exact GSR covariance, with its scalar conjugation intact.

The involution comparison is
\[
\boxed{\mathsf S_M\mathsf K_1=\mathsf K_{\rm res}\mathsf S_M.}
\tag{ECI6.5}
\]
Indeed evaluating the right side at \(F\) gives
\(\overline{\sum m_\rho\overline{F(\rho^\#)}\overline{h(\rho^\#)}}
=\sum m_\rho F(\rho)h(\rho)\), after reindexing by \(\#\). Evaluating the left side gives the same expression. Its absolute convergence follows from (ECI5.3). Thus this is a whole-module equality, not an extension inferred from finite-support density.

The local formula (ECI4.5) agrees with (ECI6.5) through the exact differentiated functional equation
\[
\zeta'(1-s)=\frac{\chi'(s)}{\chi(s)^2}\zeta(s)
-\frac{1}{\chi(s)}\zeta'(s).
\tag{ECI6.6}
\]
The first term retains the full original multiplicity and is zero only after passage to that actual jet quotient; the second term retains the minus sign and all unit derivatives. This proves the relation between the source involution, the \(\zeta'\) trace map and the residue-dual involution, without replacing the original function by its completion or treating \(\chi\) as a global entire multiplier.

## ECI7. The normal class module maps to the same existing residue receiver

Use the actual inverse translation \(U:\mathscr C_+\to\mathscr C\). Define
\[
\mathsf S_+=\mathsf S_MU:\mathscr C_+\to\mathcal H_{\rm res}.
\tag{ECI7.1}
\]
For \(X\in\mathcal Q_+\), its precise evaluation is
\[
(\widehat\iota\mathsf S_+k)(UX)
=\sum_\rho m_\rho X(\rho+1)\overline{k(\rho^\#+1)}.
\tag{ECI7.2}
\]
Thus it is a map from the actual cyclic normal-extension or boundary module, by (ECI0.3), to the original strong residue receiver, tested through the exact coordinate map \(U\). Its kernel is
\(\mathfrak r_+/\mathfrak a_+\), where \(\mathfrak r_+=V\mathfrak r\). All zero values and all original multiplicities in the normal module are retained.

For the normal involution and arbitrary multipliers,
\[
\mathsf S_+\mathsf K_3=\mathsf K_{\rm res}\mathsf S_+,
\qquad
\widehat\iota\mathsf S_+(bk)
=m_{U(b^{\#_3})}'\widehat\iota\mathsf S_+(k).
\tag{ECI7.3}
\]
These follow from \(U\mathsf K_3=\mathsf K_1U\), \(U(bk)=(Ub)(Uk)\), and (ECI6.4). Specializing to \(b(\lambda)=a^\lambda\) retains
\[
\boxed{\mathsf S_+D_a^+=a\widehat T_a\mathsf S_+,
\qquad
\widehat\iota\mathsf S_+D_a^+
=a^2(T_{1/a})'\widehat\iota\mathsf S_+.}
\tag{ECI7.4}
\]
Here \(\widehat T_a\) is the existing residue action from GTR10, satisfying \(\widehat\iota\widehat T_a=a(T_{1/a})'\widehat\iota\). The extra factor in (ECI7.4) is the actual normal translation factor in (ECI2.4).

There is an exact translated primal map as well:
\[
\mathsf P_+=V\mathsf P_MU
=(L_+-1)^{-2}
M_{(\lambda-1)^2\zeta'(2-\lambda)}\mathsf C.
\tag{ECI7.5}
\]
The only derivative pole being removed is at \(\lambda=1\), and the multiplier's value there is \(-1\). This point is outside the actual normal divisor, so the inverse of \(L_+-1\) exists on \(\mathscr C_+\) by NEA7. Every full block formula is (ECI6.3) translated by one, with the local coordinate unchanged. No additional spectrum is inserted.

## ECI8. Normal residue duality and the distinction from geometric normal transfer

The translated residue pairing on actual finite-support normal classes is
\[
\mathcal R_+(X,Y)=\sum_{\rho}
\operatorname{Res}_{\lambda=\rho+1}
\frac{X(\lambda)Y(3-\lambda)}{\zeta(\lambda-1)}\,d\lambda.
\tag{ECI8.1}
\]
It is a coordinate transport of the original residue, not a replacement arithmetic function:
\[
\mathcal R_+(VF,VG)=\mathcal R(F,G).
\tag{ECI8.2}
\]
Proof: put \(\lambda=s+1\). The denominator becomes original \(\zeta(s)\), the second numerator becomes \(G(1-s)\), and \(d\lambda=ds\). Both multiplicities and positive local residue orientations are unchanged. The completion for its corresponding bounded-set seminorms is therefore topologically isomorphic to the existing \(\mathcal H_{\rm res}\), via the extension of \(V\); this follows because \(V,U\) on the test quotients carry bounded sets to bounded sets. No extra completion is needed in (ECI7.1).

The full normal functional equation is
\[
\zeta(\lambda-1)=\chi(\lambda-1)\zeta(2-\lambda).
\tag{ECI8.3}
\]
Consequently the normal residue-dual involution has local jets
\[
Y(\lambda)\longmapsto
-\chi(2-\lambda)Y^{\#_3}(\lambda).
\tag{ECI8.4}
\]
This is exactly (ECI4.5) translated, with its full Gamma, sine, power and derivative data from (ECI4.3). Its completed action is the same transported continuous dual involution, not an assumed entire multiplier.

The normal pairing's full dilation factor is
\[
\mathcal R_+(D_a^+X,D_a^+Y)=a^3\mathcal R_+(X,Y),
\quad
W_+(D_a^+X,Y)=W_+(X,a^3D_{1/a}^+Y),
\tag{ECI8.5}
\]
where \(W_+\) is the exact value sum in (ECI7.2). In the residue integrand the multiplier is \(a^\lambda a^{3-\lambda}=a^3\). In the value formula the equality follows from \(\overline{3-\overline\lambda}=3-\lambda\). These are whole-divisor identities.

For \(a=n\) a positive integer, GTR's actual degree-\(n\) covering has normal pullback \(aT_a\) in the original source coordinate and transfer with inverse coefficients \(T_{1/a}\). For general \(a>0\), these same expressions remain the specified coefficient operators; no covering with nonintegral degree is asserted. Transporting both coefficient operators gives
\[
V(aT_a)U=D_a^+,
\qquad V T_{1/a}U=aD_{1/a}^+.
\tag{ECI8.6}
\]
Their product remains \(aI\). Therefore the normal Weil/residue adjoint operator in (ECI8.5) is precisely \(a^2\) times the displayed normal coefficient transfer, and, for positive integer \(a=n\), precisely \(n^2\) times the actual geometric normal transfer. The three identities (ECI7.4), (ECI8.5) and (ECI8.6) agree with each other; none permits deletion of that factor. This calculation concerns the degree-shifted normal class module. It does not assign its \(a^3\) factor to the original degree-one Weil pairing, whose factor remains \(a\).

## ECI9. The separator's zero and identity actions remain different after translation

FOD and NEA prove
\[
c=0\text{ on }\mathscr C_+,
\qquad c=1\text{ on }\mathscr C,
\qquad c\delta=0.
\tag{ECI9.1}
\]
The two actions are compatible with the actual translation because
\[
(Uc)(s)=c(s+1)=1-E(s)\in\mathfrak a,
\tag{ECI9.2}
\]
whereas \(c(s)-1\in\mathfrak a\). Thus translating the annihilation equation on the normal class module gives multiplication by \(Uc\), not multiplication by \(c\), on the original module. Explicitly
\[
\mathsf S_+(ck)=\mathsf S_M((Uc)(Uk))=0,
\qquad
\mathsf S_M(ch)=\mathsf S_M(h).
\tag{ECI9.3}
\]
The first vanishes because its argument is zero in \(\mathscr C\); the second retains the entire original trace. These equations are the exact connecting map between the two assertions. They do not identify their source classes or their scalar actions. In particular the normal annihilation \(c\delta=0\), which proves the actual lift in FOD7/NEA10, does not become an annihilation of original Weil values by silently removing the coordinate translation.

## ECI10. What the extension-class residue maps do to the positive-adjoint defect

On the established value Hilbert space retain GTAH's bounded operator
\[
(D_ax)_\rho=(a^{\overline\rho}-a^{1-\rho})x_\rho,
\qquad a>1.
\tag{ECI10.1}
\]
It acts on this explicitly constructed value space, not as an asserted entire multiplier on all of \(\mathscr C\). RTT6.2 proves an injective continuous anti-linear map
\[
\mathsf A:H\to\mathcal H_{\rm res},\qquad
(\widehat\iota\mathsf Ay)(F)=\langle EF,Jy\rangle,
\qquad\mathsf S=\mathsf A E.
\tag{ECI10.2}
\]
The new extension-class map restricts to exactly this map on \(\mathcal Q\subset\mathscr C\), by (ECI5.1). Every finite value vector is attained there by the actual global isolators. Consequently this extension of the domain loses no original value direction, and
\[
\mathsf A D_a^*D_a=0\quad\Longleftrightarrow\quad D_a^*D_a=0.
\tag{ECI10.3}
\]
The reverse implication is immediate; the forward implication is injectivity applied to each vector. Positivity of the Hilbert norm then gives equivalence to \(D_a=0\), exactly as in GTAH6.7.

There is a specific full-source test for every actual zero, avoiding an unproved nonholomorphic multiplier lift. Fix \(\rho\) and let \(e_{\rho,0}\) be its global full-jet isolator, viewed in \(\mathcal Q\subset\mathscr C\). Put
\[
d_\rho^2=|a^{\overline\rho}-a^{1-\rho}|^2,
\qquad h_\rho=d_\rho^2 e_{\rho,0}\in\mathcal B\subset M.
\tag{ECI10.4}
\]
Then \(E[h_\rho]=D_a^*D_a E[e_{\rho,0}]\), and evaluation on the other actual isolator gives
\[
(\widehat\iota\mathsf S_M[h_\rho])(e_{\rho^\#,0})
=m_\rho d_\rho^2.
\tag{ECI10.5}
\]
This is nonzero precisely when the displayed scalar defect is nonzero. It quantifies over the actual divisor and does not postulate an off-line zero. Translating \(h_\rho\) to \(Vh_\rho\in\mathscr C_+\) gives the same result through \(\mathsf S_+V=\mathsf S_M\). Thus neither the extension-class involution nor this residue comparison kills a nonzero positive-adjoint defect. The statement is established by the actual maps and witnesses, not by treating an RH-equivalent criterion as an achievement.

For every actual two-point orbit, the signed test also remains \(e_{\rho,0}-e_{\rho^\#,0}\), with original Weil value \(-2m_\rho\) as calculated in GTAH6.5. Both new class-module maps restrict to that same residue value. The higher-jet kernel (ECI5.7) is the exact information they remove; it contains no nonzero isolated value vector.

## ECI11. Original factors, class actions and category scope

Every source factor used above remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad
F_+(\lambda)=\frac{(\lambda-1)(\lambda-2)}8
\pi^{-(\lambda-1)/2}\Gamma((\lambda-1)/2)\zeta(\lambda-1).
\tag{ECI11.1}
\]
Their endpoints are \(F_0(0)=F_0(1)=F_+(1)=F_+(2)=1/8\), and the original trivial-zero comparison is
\[
F_0(-2r)=F_+(1-2r)
=\frac{r(2r+1)(-1)^r\pi^r}{2\,r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r),\quad r\ge1.
\tag{ECI11.2}
\]
The function in every residue denominator remains \(\zeta\) in its explicitly related coordinate. Its arithmetic is still
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad -\frac{\zeta'}\zeta(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks},
\quad\Re s>1.
\tag{ECI11.3}
\]
On the original test subspace the new trace maps are exactly RTT's map, so RTT9's complete prime, Gamma, endpoint and finite trivial-divisor identity remains unchanged. Formula (ECI5.1) on a general polynomial-growth multiplier is proved directly as a continuous spectral functional; no extension of the prime explicit formula to an unspecified larger test class is inferred.

The class-module action above is multiplication, or central postcomposition on the actual cyclic extension classes. As FOD7 and NEA10 prove, conjugation of the equivariant boundary by dilation fixes that boundary. The scalar factors in ECI2 and ECI8 concern the specified multiplier and pairing actions; they are not reassigned as conjugation weights of \(\delta\). Likewise the semilinear involutions of ECI1 are explicit coefficient and row operations, not an unproved identification with ordinary or étale Verdier duality. The residue-dual comparison they do supply is (ECI4.1)–(ECI4.5), and its relation to the actual extension modules is (ECI6.5) and (ECI7.3).

## ECI12. Exact comparison with the Gaussian source embedding

The complete ECR0–ECR7 derivation in [EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md) was read for this comparison. It constructs, for each \(t>0\), the entire source multiplier \(g_t(s)=e^{ts^2}\) and the injective \(M\)-map
\[
b_t:\mathscr C\to\mathcal Q,\qquad[h]\mapsto[g_t h],
\quad j:\mathcal Q\hookrightarrow\mathscr C,
\quad jb_t=m_{g_t}.
\tag{ECI12.1}
\]
Its coefficient-to-source estimate retains \(|g_t(\sigma+i\gamma)|=e^{t(\sigma^2-\gamma^2)}\), so multiplying a polynomial-growth representative by \(g_t\) really lands in \(\mathcal B\). The target and purpose differ from the direct trace functional of ECI5: \(b_t\) reaches the actual source quotient and hence the positive value Hilbert space, while (ECI5.4) reaches its strong dual receiver. For example the value sequence of \([1]\in\mathscr C\) is not in \(H\), since there are infinitely many actual zeros, but (ECI5.1) at \(h=1\) is a continuous functional on every original rapid test. There is no identification of those two receiving spaces.

The exact comparison is
\[
\boxed{\mathsf S b_t=\mathsf S_M m_{g_t}:\mathscr C\to\mathcal H_{\rm res}.}
\tag{ECI12.2}
\]
Indeed \(\mathsf S_Mj=\mathsf S\) by (ECI5.1); compose this equality with \(b_t\) and use (ECI12.1). Explicitly both sides evaluated against \(F\) give
\(\sum_\rho m_\rho F(\rho)\overline{g_t(\rho^\#)h(\rho^\#)}\), with absolute and strong convergence already proved. Because \(g_t\) is a unit in each actual local ring, both maps have the same value-zero kernel \(\mathfrak r/\mathfrak a\). This is not a claim that \([g_t]\) is invertible in the global multiplier quotient; ECR1 proves it is not.

The embedding also has an exact involution factor which should be retained in any dual comparison:
\[
g_t^{\#_1}(s)=e^{t(1-s)^2}=d_t(s)g_t(s),
\qquad d_t(s)=e^{t(1-2s)},
\qquad d_t^{\#_1}=d_t^{-1}.
\tag{ECI12.3}
\]
Both \(d_t\) and its inverse are in \(M\). Consequently
\[
\mathsf K_1 b_t=m_{d_t}b_t\mathsf K_1.
\tag{ECI12.4}
\]
This is equality on full source jets: it follows from multiplication of the entire functions before quotient. No coordinate or coefficient has been normalized. Conjugation alone commutes with \(b_t\), since \(g_t\) has real Taylor coefficients; reflection alone satisfies the same \(d_t\) factor as (ECI12.4).

Write \(\mathsf S_t=\mathsf S b_t\), as in ECR4. Combining (ECI6.5), (ECI12.4), and the multiplier covariance gives the complete dual version
\[
\widehat\iota\mathsf K_{\rm res}\mathsf S_t
=m_{d_t^{-1}}'\widehat\iota\mathsf S_t\mathsf K_1.
\tag{ECI12.5}
\]
The inverse factor arises from the involution on the multiplier, not an inverse of \(g_t\). For the normal class module the transported source Gaussian is \((Vg_t)(\lambda)=e^{t(\lambda-1)^2}\), and its corresponding factor is \((Vd_t)(\lambda)=e^{t(3-2\lambda)}\). These follow directly from (ECI2.3), retaining the actual shift instead of choosing a different normal Gaussian.

For two class-module inputs, (ECI12.2) gives precisely ECR's full trace
\[
\widehat{\mathcal R}(b_th,\mathsf S_tk)
=\sum_\rho m_\rho e^{t\{\rho^2+(1-\rho)^2\}}
h(\rho)\overline{k(\rho^\#)}.
\tag{ECI12.6}
\]
The positive value receiver instead has the actual modulus weight \(e^{2t(\sigma^2-\gamma^2)}\). The two weights are not substituted for each other. ECR4 proves the former's complete original prime/Gamma/endpoint formula; ECR5 proves the latter's positive defect formula through its stated Hilbert-space map. Thus the canonical residue map here and ECR's Gaussian source embedding agree by an exact morphism while preserving their different domains and purposes.

## ECI13. Exact receiving result

The new cyclic modules now have complete involution maps, including their full jets, translation, and actual row origins. Their original and normal involutions use \(1-s\) and \(3-\lambda\), respectively, with the exact translation diagram (ECI2.3). Their residue-dual involutions retain the functional-equation units and minus signs (ECI4.5), (ECI8.4). Every polynomial-growth extension class has a canonical, explicitly convergent map to the original strong residue receiver, extending RTT without changing its kernel on original tests. Its covariance retains every factor \(a\), \(a^2\), and \(a^3\) in the different specified domains.

This calculates the proposed use of the new annihilator modules rather than merely naming their resemblance to duality. The normal boundary's annihilation and the unchanged original positive-adjoint defect coexist through the proved translation (ECI9.2). The remaining attempt toward the active goal must supply additional source information controlling that retained defect; the independent positive source-pairing calculation can now use the exact involution and degree dictionary here. No pure weight, positive original Weil form, or RH conclusion is assumed.

Proof sources actually read for this continuation: [../tau_weight_cohomology_20260924/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_FULL_SOURCE_OBSTRUCTION_DECOMPOSITION.md), FOD0–FOD8; [../tau_weight_cohomology_20260924/CC_NORMAL_EXTENSION_ANNIHILATOR.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/CC_NORMAL_EXTENSION_ANNIHILATOR.md), NEA0–NEA10; [EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/EXTENSION_CLASS_TO_ORIGINAL_RESIDUE.md), ECR0–ECR7; current construction/prerequisite instructions; and the existing checked RTT, GSR, GTAH and GMS maps cited at their equation locators above. Human-source context remains the original Connes–Consani §5 construction and Deligne's Weil II §3.6, with their source-reading coverage recorded in those receiving proofs. This continuation makes no new complete-reading claim for those human papers and no public release claim.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# All continuous positive transfer forms on the original full-jet quotient

25 September 2026. Independent derivation CFP0–CFP12 and the proved analytic lemma CFPA. The inner product convention is linear in the first variable.

## CFP0. The actual source and the statement

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All numbers, coefficient spaces, arithmetic labels and operations in this proof occur after the complete arithmetic reconstruction. No coefficient value, addition, parity, coordinate or metric is assigned to \(\tau\). The original two branch records remain distinct.

Retain the source from RD1, RTT0 and PTQ6:
\[
\mathcal B=\left\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\quad(A,M\in\mathbb Z_{\ge0})\right\},
\]
\[
\mathcal I=\{F\in\mathcal B:F^{(j)}(\rho)=0
\text{ for every nontrivial zero }\rho\text{ of original }\zeta,
\ 0\le j<m_\rho\},\qquad
\mathcal Q=\mathcal B/\mathcal I.
\tag{CFP0.1}
\]
The topology is this Fréchet quotient topology. Every multiplicity \(m_\rho\) is retained. Write \(q:\mathcal B\to\mathcal Q\), and retain
\[
T_aq(F)=q(a^sF(s)),\quad Lq(F)=q(sF(s)),\quad a>0;
\qquad \mathsf U_n=nT_{1/n}\quad(n\ge1).
\tag{CFP0.2}
\]
The integer \(n\) in the transfer is the already constructed cover degree. Its coefficient inverse is not a cover of fractional degree.

**Classification.** All jointly continuous positive semidefinite Hermitian forms \(B\) on \(\mathcal Q\) satisfying
\[
B(T_nF,G)=B(F,\mathsf U_nG)
\quad\text{for every recovered integer }n\ge1
\tag{CFP0.3}
\]
are exactly
\[
\boxed{B(F,G)=\sum_{\substack{\rho\in\mathscr Z\\\Re\rho=1/2}}
m_\rho c_\rho F(\rho)\overline{G(\rho)},\qquad
0\le c_\rho\le C(1+|\Im\rho|)^d}
\tag{CFP0.4}
\]
for some finite \(C,d\ge0\) depending on the form. The weights are unique. Here and below \(F(\rho)\) means evaluation of any source representative of its class.

The proof does not assume RH, simplicity, boundedness of \(B\) for the previous value Hilbert norm, or density of the finite-support subspace in \(\mathcal Q\). In particular it extends PTQ4 beyond bounded forms on that Hilbert space. The full source, its higher jets, and all actual off-line zeros, if present, remain in the domain; the theorem determines their image in every continuous positive transfer receiver.

## CFP1. Source continuity and the positive completion

Multiplication by \(e^{ts}\) preserves \(\mathcal B\), \(\mathcal I\) and the full vanishing-jet conditions. Its action on an actual jet is multiplication by the complete jet of \(e^{ts}\), rather than the identity. Moreover,
\[
b_{A,M}(e^{ts}F)\le e^{A|t|}b_{A,M}(F),\qquad
b_{A,M}(sF)\le(A+1)b_{A,M+1}(F).
\tag{CFP1.1}
\]
For real \(t\), the identity
\(e^{hs}-1=hs\int_0^1e^{uhs}\,du\) proves continuity of \(t\mapsto e^{ts}F\) in every seminorm. The analogous second-order integral remainder proves its derivative is \(se^{ts}F\) in \(\mathcal B\). Repetition gives all derivatives. These facts pass through the quotient.

Joint continuity of \(B(qF,qG)\), positivity and Cauchy–Schwarz give integers \(A,M\) and a constant \(C_B\) such that
\[
B(qF,qF)\le C_B b_{A,M}(F)^2.
\tag{CFP1.2}
\]
Indeed continuity at the origin first bounds the form by a finite maximum of seminorms in each variable; the increasing family \(b_{A,M}\) absorbs that finite maximum. Alternatively continuity of the quadratic form supplies the same bound by scaling. Cauchy–Schwarz follows directly by applying positivity to \(x+zy\) and minimizing over \(z\in\mathbb C\).

Let \(\mathcal N_B=\{F:B(F,F)=0\}\). Cauchy–Schwarz identifies it with the full radical. Complete \(\mathcal Q/\mathcal N_B\) for the specified inner product \(B\), obtaining a Hilbert space \(H_B\). The canonical map
\[
\pi:\mathcal Q\longrightarrow H_B
\quad\text{has dense image, and}\quad
\langle\pi F,\pi G\rangle=B(F,G).
\tag{CFP1.3}
\]
The map \(\pi q\) is continuous by (CFP1.2), hence \(\pi\) is continuous by the quotient topology. This construction does not identify the original Fréchet topology with the new Hilbert norm.

## CFP2. Every integer relation gives the full continuous unitary action

The exact identities \(\mathsf U_nT_n=nI\) and (CFP0.3) give
\[
B(T_nF,T_nG)=nB(F,G).
\tag{CFP2.1}
\]
Conversely (CFP2.1), with \(G\) replaced by \(T_n^{-1}G\), gives (CFP0.3). Invertibility of \(T_n\) also proves
\(B(T_{1/n}F,T_{1/n}G)=n^{-1}B(F,G)\). Composition therefore gives
\[
B(T_aF,T_aG)=aB(F,G)\qquad(a\in\mathbb Q_{>0}).
\tag{CFP2.2}
\]
For arbitrary real \(a>0\), choose positive rationals tending to \(a\). The source continuity in CFP1 and the continuity of \(B\) give exactly the same identity. This uses the entire already recovered arithmetic family and its coefficient operations; it makes no assertion that a finite set of prime labels initiates the arithmetic reconstruction.

For every real \(t\), define the auxiliary Hilbert action on the dense source image by
\[
V_t\pi F=e^{-t/2}\pi T_{e^t}F.
\tag{CFP2.3}
\]
The radical is invariant, and (CFP2.2) shows that this is an isometry with inverse \(V_{-t}\). It extends uniquely to a unitary on \(H_B\). Source continuity proves strong continuity on the dense image; the unitary norm bound and approximation by that image prove it on all of \(H_B\). The group law follows on the dense image and hence everywhere.

The exact original action is still
\[
\boxed{\pi T_{e^t}=e^{t/2}V_t\pi.}
\tag{CFP2.4}
\]
Thus its degree is not removed or replaced. The auxiliary unitary group is the specified comparison of the original action with the positive degree character. In particular, for every source \(H\in\mathcal B\),
\[
\left.\frac d{dt}\right|_{t=0}V_t\pi q(H)
=\pi q((s-1/2)H).
\tag{CFP2.5}
\]
The derivative exists in the Hilbert norm because it already exists in the stronger source topology.

## CFP3. The complete original-zeta source integral

Retain the original even Schwartz vector and the complete summation map:
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
\Sigma f(u)=2\sum_{n\ge1}f(nu),\qquad
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u}.
\tag{CFP3.1}
\]
The two source conditions are \(f_0(0)=0\) and \(\int_{\mathbb R}f_0=0\). The second follows from
\(\int v^2e^{-\pi v^2}dv=1/(2\pi)\) and
\(\int v^4e^{-\pi v^2}dv=3/(4\pi^2)\).

For the Fourier convention \(\widehat f(y)=\int f(v)e^{-2\pi ivy}dv\), differentiation of the Gaussian transform gives
\[
\widehat{v^2e^{-\pi v^2}}(y)
=(1/(2\pi)-y^2)e^{-\pi y^2},
\]
\[
\widehat{v^4e^{-\pi v^2}}(y)
=(y^4-3y^2/\pi+3/(4\pi^2))e^{-\pi y^2}.
\tag{CFP3.2}
\]
Substitution of the two original coefficients proves \(\widehat f_0=f_0\), including cancellation of the constant coefficient. Poisson summation on this Schwartz vector, with both zero terms zero, yields
\[
\Sigma f_0(u)=u^{-1}\Sigma f_0(u^{-1}).
\tag{CFP3.3}
\]
Here the Poisson identity itself follows by periodizing a Schwartz function, computing its Fourier coefficients by termwise integration, and evaluating its absolutely convergent Fourier series at zero. Thus no unsupported zero term has been silently discarded.

Put
\[
\boxed{k(t)=\frac12e^{t/2}\Sigma f_0(e^t)
=e^{t/2}\sum_{n\ge1}
\frac\pi2 n^2e^{2t}(2\pi n^2e^{2t}-3)
e^{-\pi n^2e^{2t}}.}
\tag{CFP3.4}
\]
Equation (CFP3.3) gives \(k(-t)=k(t)\). For \(t\ge0\), the absolute value of the summand is bounded by \(C n^4e^{(9/2)t}e^{-\pi n^2e^{2t}}\). Since \(n^2x\ge(n^2+x)/2\) for \(n\ge1\), \(x\ge1\),
\[
|k(t)|\le C_0\exp\bigl((9/2)|t|-(\pi/2)e^{2|t|}\bigr).
\tag{CFP3.5}
\]
The constant \(C_0\) includes the finite sum \(\sum n^4e^{-\pi n^2/2}\) and the original two polynomial coefficients. This bound proves integrability against \(|t|^j e^{R|t|}\) for every finite \(j,R\).

The exact source transform, with original \(\zeta\) explicit, is
\[
\begin{aligned}
\int_{\mathbb R}k(t)e^{(s-1/2)t}\,dt
&=\frac12\int_0^\infty\Sigma f_0(u)u^s\frac{du}{u}\\
&=\zeta(s)\int_0^\infty f_0(v)v^s\frac{dv}{v}\\
&=\boxed{\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)=F_0(s)}.
\end{aligned}
\tag{CFP3.6}
\]
The second identity first holds on \(\Re s>1\) by absolute convergence. The Mellin integral there is
\[
\frac12\pi^{-s/2}\Gamma((s+4)/2)
-\frac34\pi^{-s/2}\Gamma((s+2)/2)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{CFP3.7}
\]
This records both Gaussian summands before their exact Gamma recursion. The left side of (CFP3.6) is entire by (CFP3.5), so the equality continues through every exceptional point. No completed zeta is used as a replacement for original \(\zeta\); \(F_0\) is this proved source multiplier.

All endpoint and trivial-zero values remain in that comparison:
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0\quad(r\ge1).
\tag{CFP3.8}
\]
At zero use \(\Gamma(s/2)=2/s+O(1)\) and \(\zeta(0)=-1/2\); at one use the original zeta residue one. At \(-2r\), use the Gamma residue \(2(-1)^r/r!\) and the original simple trivial zero. Its nonzero derivative follows directly from the original functional equation
\[
\zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s).
\tag{CFP3.9}
\]
Differentiating its simple sine zero supplies the derivative in (CFP3.8); reflection of the full product supplies the displayed value at \(1+2r\). On the open critical strip, every multiplier in (CFP3.6) is a holomorphic unit. Consequently the zeros of \(F_0\) are exactly the original nontrivial zeta zeros with their unchanged multiplicities.

To retain all derivative terms as well, write only as an auxiliary notation
\(M_0(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/8\). On every nonexceptional germ,
\[
F_0^{(r)}(s)=\sum_{j=0}^r\binom rj M_0^{(j)}(s)\zeta^{(r-j)}(s),
\]
\[
M_0^{(j)}(s)=\sum_{j_0+j_1+j_2=j}
\frac{j!}{j_0!j_1!j_2!}
\left(\frac{s(s-1)}8\right)^{(j_0)}
\left(-\frac{\log\pi}2\right)^{j_1}\pi^{-s/2}
2^{-j_2}\Gamma^{(j_2)}(s/2).
\tag{CFP3.10}
\]
The entire continuation at exceptional points is given by the integral, whose exact derivatives are \(\int t^rk(t)e^{(s-1/2)t}dt\). No Gamma, endpoint or scale derivative is replaced by a constant.

## CFP4. The source annihilator is an actual convergent group integral

For each \(F\in\mathcal B\),
\[
b_{A,M}(k(t)e^{t(s-1/2)}F)
\le |k(t)|e^{(A+1/2)|t|}b_{A,M}(F).
\tag{CFP4.1}
\]
This bound is integrable by (CFP3.5). Integrating on finite intervals and passing to the limit in every seminorm therefore defines an integral in the complete Fréchet space \(\mathcal B\). Point evaluation is continuous, so (CFP3.6) identifies that integral exactly:
\[
\int_{\mathbb R} k(t)e^{t(s-1/2)}F(s)\,dt
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s)F(s).
\tag{CFP4.2}
\]
This product belongs to \(\mathcal I\), since every required zero order occurs in the full \(F_0\) factor. It follows, after the continuous maps \(q\) and \(\pi\), that
\[
\int_{\mathbb R}k(t)V_t\pi q(F)\,dt=0.
\tag{CFP4.3}
\]
As \(k\in L^1(\mathbb R)\) and \(V_t\) is unitary, its Hilbert integral is a bounded operator of norm at most \(\|k\|_1\). Equation (CFP4.3) holds on a dense image, hence
\[
\boxed{\int_{\mathbb R}k(t)V_t\,dt=0\quad\text{on all of }H_B.}
\tag{CFP4.4}
\]
This is an annihilation of the completed receiver by the original source vector. It neither identifies \(F_0\) with original \(\zeta\) nor declares that the original source quotient is a quotient by the principal ideal \(F_0\mathcal B\). Only the proved inclusion \(F_0\mathcal B\subset\mathcal I\) has been used.

## CFP5. Spectral support and the complete atomic decomposition

The analytic lemma CFPA below is proved for any strongly continuous unitary group and any \(L^1\) annihilating kernel. Applying it to (CFP4.4) gives spectral support in
\[
\Gamma=\{\gamma\in\mathbb R:
\frac{(1/2+i\gamma)(-1/2+i\gamma)}8
\pi^{-(1/2+i\gamma)/2}
\Gamma((1/2+i\gamma)/2)\zeta(1/2+i\gamma)=0\}.
\tag{CFP5.1}
\]
All factors outside \(\zeta\) in this formula are nonzero and finite. Thus \(\Gamma\) is exactly the set of ordinates of actual critical-line zeros of original \(\zeta\). It is discrete and countable; it has finitely many elements in every compact interval because the entire nonzero source function \(F_0\) has isolated zeros.

There are mutually orthogonal projections \(P_\gamma\) with
\[
V_tP_\gamma=e^{it\gamma}P_\gamma,
\qquad x=\sum_{\gamma\in\Gamma}P_\gamma x,
\qquad \|x\|^2=\sum_{\gamma\in\Gamma}\|P_\gamma x\|^2.
\tag{CFP5.2}
\]
The series converges in norm, and every zero projection is permitted. Explicitly,
\[
P_\gamma x=\lim_{R\to\infty}\frac1{2R}
\int_{-R}^{R}e^{-it\gamma}V_tx\,dt.
\tag{CFP5.3}
\]
The proof in CFPA uses the full source integral and scalar positive measures, not any assumed density of finite original jets. The original degree action on this fibre remains
\[
\pi T_{e^t}=e^{t/2}V_t\pi,
\qquad T_{n,\gamma}=n^{1/2+i\gamma},
\qquad \mathsf U_{n,\gamma}=n^{1/2-i\gamma}.
\tag{CFP5.4}
\]

## CFP6. Division forces rank one and detects every killed jet

Fix \(\gamma\in\Gamma\), put \(\rho=1/2+i\gamma\), and retain the entire Gaussian
\[
g_\rho(s)=e^{(s-\rho)^2},\qquad g_\rho(\rho)=1.
\tag{CFP6.1}
\]
It belongs to \(\mathcal B\). For arbitrary \(F\in\mathcal B\), define
\[
H_{F,\rho}(s)=\frac{F(s)-F(\rho)g_\rho(s)}{s-\rho}.
\tag{CFP6.2}
\]
The singularity at \(\rho\) is removable. This division remains in \(\mathcal B\): outside a disk about \(\rho\), the denominator is bounded below; inside that disk, the holomorphic quotient is bounded by its value on a larger boundary circle, and each polynomial weight is bounded there. Applying this argument on every strip, with a slightly enlarged strip for that circle, proves all defining seminorms finite. No infinite interpolation assertion is needed.

Differentiate the eigenprojection identity \(P_\gamma V_t=e^{it\gamma}P_\gamma\) on the actual smooth vector \(\pi q(H_{F,\rho})\). By (CFP2.5),
\[
P_\gamma\pi q((s-1/2)H_{F,\rho})
=i\gamma P_\gamma\pi q(H_{F,\rho}).
\]
Therefore
\[
\boxed{P_\gamma\pi q(F)
=F(\rho)v_\rho,\qquad
v_\rho=P_\gamma\pi q(g_\rho).}
\tag{CFP6.3}
\]
Since \(\pi q(\mathcal B)\) is dense, the range of \(P_\gamma\) is the closure of its image on that dense set. Formula (CFP6.3) proves
\[
\operatorname{Ran}P_\gamma=\mathbb C v_\rho;
\quad\dim\operatorname{Ran}P_\gamma\in\{0,1\}.
\tag{CFP6.4}
\]
The possible zero dimension is retained. This is the required multiplicity statement for the positive receiver, not a simplicity assertion about zeta.

The original source still has its full local algebra \(\mathbb C[z]/(z^{m_\rho})\). The exact globally realized block map is
\[
\sum_{j=0}^{m_\rho-1}a_jz^j\longmapsto
\begin{cases}a_0v_\rho,&\Re\rho=1/2,\\0,&\Re\rho\ne1/2.\end{cases}
\tag{CFP6.5}
\]
To verify it globally, use the RD1 isolator \(e_{\rho,j}\), whose required jets vanish at every other actual zero. Equation (CFP6.3) and the complete decomposition (CFP5.2) give (CFP6.5). In particular the kernel on a block with \(v_\rho\ne0\) consists of all \(m_\rho-1\) higher-jet directions; when \(v_\rho=0\) or the zero is off-line, it is the entire original \(m_\rho\)-dimensional block. No source class is declared zero in \(\mathcal Q\) merely because this map kills it.

## CFP7. The exact weights and their necessary growth

By (CFP5.2) and (CFP6.3), for arbitrary original classes,
\[
B(F,G)=\sum_{\rho\in\mathscr Z_{\rm line}}
w_\rho F(\rho)\overline{G(\rho)},
\qquad w_\rho=\|v_\rho\|^2\ge0.
\tag{CFP7.1}
\]
The sum is absolutely convergent by Cauchy–Schwarz applied to the two norm-convergent orthogonal expansions. Retain the original multiplicity by defining
\[
c_\rho=w_\rho/m_\rho.
\tag{CFP7.2}
\]
This gives exactly (CFP0.4). The weights are unique: testing on the original isolator \(e_{\rho,0}\) gives \(B(e_{\rho,0},e_{\rho,0})=w_\rho\). The multiplicity has not been replaced by one; \(w_\rho\) is the total scalar mass of this receiver, while \(c_\rho\) is its coefficient relative to the original multiplicity trace.

For the continuity bound (CFP1.2), the Gaussian satisfies
\[
|g_\rho(\sigma+iy)|=e^{(\sigma-1/2)^2-(y-\gamma)^2},
\]
\[
b_{A,M}(g_\rho)\le
e^{(A+1/2)^2}(1+|\gamma|)^M
\sup_{u\in\mathbb R}(1+|u|)^M e^{-u^2}.
\tag{CFP7.3}
\]
The last supremum is finite. Since \(P_\gamma\) is an orthogonal projection,
\[
0\le m_\rho c_\rho=w_\rho
\le\|\pi q(g_\rho)\|^2
\le C'(1+|\gamma|)^{2M}.
\tag{CFP7.4}
\]
As \(m_\rho\ge1\), this proves the necessary polynomial bound on \(c_\rho\). It also proves the stronger polynomial bound on its actual atomic mass \(m_\rho c_\rho\). No uniform lower bound for zero spacing, isolator coefficients, or \(\zeta'(\rho)\) is involved.

## CFP8. Every indicated polynomial family gives a continuous form

Conversely suppose \(0\le c_\rho\le C(1+|\gamma|)^d\). The actual zero count with multiplicities is
\[
N(R)=\sum_{\rho\in\mathscr Z,\ |\Im\rho|\le R}m_\rho
=O(R\log(R+2)).
\tag{CFP8.1}
\]
This unconditional count is one of the original divisor estimates already used in RTT1. It does not impose RH. By grouping zeros into dyadic height intervals, it implies
\(\sum_\rho m_\rho(1+|\Im\rho|)^{-q}<\infty\) for every \(q>1\).
Choose an integer \(M\) with \(2M-d>2\). Then
\[
\sum_{\rho\in\mathscr Z_{\rm line}}
m_\rho c_\rho |F(\rho)|^2
\le C b_{1,M}(F)^2
\sum_{\rho\in\mathscr Z}m_\rho(1+|\Im\rho|)^{d-2M}<\infty.
\tag{CFP8.2}
\]
Cauchy–Schwarz proves absolute convergence of the two-variable form and joint continuity on \(\mathcal B\). It annihilates \(\mathcal I\) in either argument and hence gives a jointly continuous form on the quotient: take the infimum of the displayed seminorm bound over representatives in each argument. Its positivity is termwise.

For every \(n\ge1\), on a retained coordinate \(\overline\rho=1-\rho\), so
\[
\overline{n^{1-\rho}}=n^\rho.
\]
Substitution in the absolutely convergent sums gives exactly
\(B(T_nF,G)=B(F,nT_{1/n}G)\). This proves sufficiency and completes the classification.

## CFP9. Universal source kernel, without a value-norm hypothesis

For a particular weight family define
\[
\mathscr Z_c=\{\rho\in\mathscr Z_{\rm line}:c_\rho>0\},
\qquad
\mathcal K_c=\{[F]\in\mathcal Q:F(\rho)=0\text{ for every }\rho\in\mathscr Z_c\}.
\tag{CFP9.1}
\]
Equation (CFP0.4) proves that this is exactly the radical. The completion is canonically
\[
\overline{\mathcal Q/\mathcal K_c}^{,B}
\simeq\ell^2(\mathscr Z_c,m_\rho c_\rho),
\tag{CFP9.2}
\]
with map \([F]\mapsto(F(\rho))_{\rho\in\mathscr Z_c}\). The norm identity follows from the formula. Every finite sequence occurs, by the actual full-jet isolators, and finite sequences are dense in the displayed weighted Hilbert space. This proves surjectivity of the map on completions without any claim about finite-jet density in the original topology.

The intersection of radicals of **all** continuous positive forms satisfying the original transfer identities is therefore exactly
\[
\boxed{\mathcal K_{\rm all}
=\{[F]:F(\rho)=0\quad(\rho\in\mathscr Z_{\rm line})\}
=\mathcal I_{\mathscr Z_{\rm line}}^{\rm val}/\mathcal I.}
\tag{CFP9.3}
\]
Every classified form kills this space. Conversely the choice \(c_\rho=1\) is permitted by CFP8 and detects every class outside it. Thus this common kernel is proved in the actual Fréchet category, rather than inferred from boundedness in PTQ's auxiliary value norm.

At an individual original nontrivial zero, the scalar relation responsible for this kernel can also be checked directly: \(B(T_nx,T_nx)=nB(x,x)\) forces a pure eigenvector of exponent \(\rho\) to have zero norm when \(n^{2\Re\rho}\ne n\). The global argument above additionally proves that no continuous residual sector escapes this finite-coordinate calculation and that all higher jets are killed. That global assertion is precisely what finite-support computations alone do not supply.

## CFP10. Every continuous positive Hilbert receiver factors through the classified kernel

Let \(X:\mathcal Q\to K\) be a continuous linear map into a Hilbert space, with bounded receiving operators \(A_n,C_n\) such that
\[
XT_n=A_nX,\quad X\mathsf U_n=C_nX,\quad C_n=A_n^*.
\tag{CFP10.1}
\]
Its pulled-back form \(B_X(F,G)=\langle XF,XG\rangle\) is jointly continuous, positive, and satisfies (CFP0.3). Consequently
\[
X\mathcal K_{\rm all}=0,
\quad X:\mathcal Q\longrightarrow\mathcal Q/\mathcal K_{\rm all}
\longrightarrow K
\tag{CFP10.2}
\]
is a unique continuous factorization in the quotient topology. The classification supplies its exact nonnegative polynomial weights and identifies the completion of its image with (CFP9.2). The original degree relation is retained: on the closed span of \(X\mathcal Q\), the identities imply \(A_n^*A_n=nI\), since it holds on the dense image.

Thus allowing arbitrary continuous Hilbert receivers from the source creates additional polynomial weights, but creates no additional supported zero, off-line value, or nonconstant jet direction compatible with a positive adjoint. This is an exact comparison with PTQ: bounded forms on its specified \(H\) correspond to the subfamily with bounded \(c_\rho\); continuity on the stronger source permits the polynomially growing families of (CFP0.4).

## CFP11. The original Weil form and all arithmetic contributions remain

Retain the original source Weil form and its exact zero observation:
\[
W(F,G)=\sum_{\rho\in\mathscr Z}m_\rho
F(\rho)\overline{G(1-\overline\rho)}.
\tag{CFP11.1}
\]
RTT1 and the count (CFP8.1) prove joint continuity; substitution proves the original transfer identity. At a line zero its contribution is the \(c_\rho=1\) contribution in (CFP0.4). For an off-line reflected orbit, retain both actual terms
\[
m_\rho\bigl(F(\rho)\overline{G(\rho^\#)}
+F(\rho^\#)\overline{G(\rho)}\bigr),
\qquad \rho^\#=1-\overline\rho.
\tag{CFP11.2}
\]
The globally realized difference \(e_{\rho,0}-e_{\rho^\#,0}\) has value \(-2m_\rho\) under \(W\). The sum has value \(+2m_\rho\). Both statements follow by direct substitution with all other values zero. The classification therefore does not make this original form positive by a change of source topology: it identifies exactly the space that every positive transfer form would have to kill.

For completeness retain the actual arithmetic receiver from RTT9. Put
\[
A_{F,G}(s)=F(s)\overline{G(1-\overline s)},\qquad
A_{F,G}(s)=\int_{\mathbb R}h(v)e^{-(s-1/2)v}dv,
\quad\widehat h(t)=\int_{\mathbb R}h(v)e^{-itv}dv.
\]
Then the unchanged full formula is
\[
W(F,G)=A_{F,G}(0)+A_{F,G}(1)+A_\infty(h)-P_{\rm hist}(h),
\]
\[
A_\infty(h)=\frac1{2\pi}\int_{\mathbb R}\widehat h(t)
\left(\Re\frac{\Gamma'(1/4+it/2)}{\Gamma(1/4+it/2)}-\log\pi\right)dt,
\]
\[
P_{\rm hist}(h)=\sum_{n\ge2}
\frac{\log L_n-\log L_{n-1}}{\sqrt n}
\bigl(h(\log n)+h(-\log n)\bigr),\quad
L_n=\operatorname{lcm}(1,\ldots,n).
\tag{CFP11.3}
\]
The coefficient is the original \(\Lambda(n)\), with every prime-power repetition. At each finite trivial-zero cutoff \(R\), retain also
\[
V_{\zeta,R}=W(F,G)+\sum_{r=1}^RA_{F,G}(-2r)-A_{F,G}(1),
\]
\[
G_R=A_\infty(h)+A_{F,G}(0)+\sum_{r=1}^RA_{F,G}(-2r),
\qquad V_{\zeta,R}=G_R-P_{\rm hist}(h).
\tag{CFP11.4}
\]
These are the original proved RTT/GIQ identities, retained here without a divergent infinite trivial-zero sum. No weighted form with arbitrary \(c_\rho\), and no compression removing (CFP11.2), is asserted to equal their right side. The original supported endpoints and their coefficient labels remain those in that established source formula.

## CFP12. The next calculation performed: the exact source-topology kernel

The issue left by PTQ was whether its value-Hilbert boundedness excluded other continuous positive source forms carrying hidden higher jets or off-line data. CFP1–CFP10 answer that question by the full source integral, the actual unitary completion and exact Gaussian division: no such additional continuous directions exist, and the complete additional freedom is the polynomial family of weights.

This does not prove that \(\mathcal K_{\rm all}\) consists only of the original higher-jet radical. Their precise difference is retained:
\[
\mathcal N_0=\{[F]:F(\rho)=0\ \forall\rho\in\mathscr Z\}
\subset\mathcal K_{\rm all},
\qquad
\mathcal K_{\rm all}/\mathcal N_0
\cong\frac{\mathcal I_{\mathscr Z_{\rm line}}^{\rm val}}
{\mathcal I_{\mathscr Z}^{\rm val}}.
\tag{CFP12.1}
\]
The displayed isomorphism is induced by the identity on representatives; its kernel and surjectivity follow directly from the two quotients. It retains the actual off-line value data. The existing off-line value observation injects this quotient into \(H_{\rm off}\), with dense image by the full original isolators. Thus the exact obstruction exposed by extending PTQ is the same source-topological off-line observation, rather than an unknown class of unbounded positive forms. The receiver of the remaining geometric comparison is now fixed without a value-norm hypothesis.

One further exact consequence records what a faithful positive form would mean. A classified form is positive definite on the **full** \(\mathcal Q\) exactly when every actual zero lies on the line, every multiplicity is one, and every \(c_\rho\) is strictly positive. Necessity follows respectively from an off-line isolator, a higher-jet isolator, or a value isolator at a zero-weight coordinate. Sufficiency follows because a nonzero full-jet class then has a nonzero retained value. This statement is not used to demand simplicity for ordinary Weil positivity: the original Weil form is allowed its precisely identified higher-jet radical.

## CFPA. Proof of the unitary annihilator lemma used above

Here is a proof of exactly the spectral facts used in CFP5. It is included to avoid leaving a new spectral assertion implicit. Basic Fourier inversion for integrable functions, Gaussian Fourier integration, the Riesz representation theorem for finite measures, and Hilbert completion are used with their usual stated domains.

Publication source credit: Measure representation is the classical Riesz theorem. The checked statement is Terence Tao, [245B, Notes12, Theorem24](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/) (2 March2009), for positive functionals on compactly supported continuous functions. Tightness and mass control are supplied in the present argument.

Let \((V_t)_{t\in\mathbb R}\) be a strongly continuous unitary group on a Hilbert space \(H\). For \(x\in H\) set
\[
f_x(t)=\langle V_tx,x\rangle.
\tag{CFPA.1}
\]
This function is continuous, bounded by \(\|x\|^2\), and positive definite: for finite coefficients,
\[
\sum_{i,j}a_i\overline{a_j}f_x(t_i-t_j)
=\left\|\sum_i a_iV_{t_i}x\right\|^2\ge0.
\tag{CFPA.2}
\]

First prove the positive Fourier-measure representation needed here. If \(f\) is continuous positive definite, then \(f(0)\ge0\), \(f(-t)=\overline{f(t)}\), and \(|f(t)|\le f(0)\), by the two-point positive matrix. For \(\varepsilon>0\), put \(f_\varepsilon(t)=f(t)e^{-\varepsilon t^2}\). The Gaussian is a positive mixture of characters, so integrating (CFPA.2) after multiplying the coefficients by those characters proves that \(f_\varepsilon\) is positive definite. It is also integrable.

Define
\[
p_\varepsilon(\lambda)=\frac1{2\pi}
\int_{\mathbb R}f_\varepsilon(t)e^{-it\lambda}dt.
\tag{CFPA.3}
\]
This is continuous and nonnegative. To prove the sign, positive definiteness, approximation of integrals by finite sums, and the interval function \(e^{-i\lambda t}1_{[-R,R]}(t)\) show
\[
0\le\frac1{2R}\int_{-R}^R\int_{-R}^R
f_\varepsilon(t-u)e^{-i\lambda(t-u)}dt\,du
=\int_{-2R}^{2R}
\left(1-\frac{|v|}{2R}\right)
f_\varepsilon(v)e^{-i\lambda v}dv.
\]
Dominated convergence as \(R\to\infty\) proves (CFPA.3) is nonnegative. It is real because of the conjugate symmetry.

For \(\delta>0\), Fourier integration and Fubini give
\[
\int_{\mathbb R}e^{-\delta\lambda^2}p_\varepsilon(\lambda)d\lambda
=\frac1{2\sqrt{\pi\delta}}
\int_{\mathbb R}e^{-t^2/(4\delta)}f_\varepsilon(t)dt
\longrightarrow f(0)
\quad(\delta\downarrow0).
\tag{CFPA.4}
\]
Monotone convergence on the nonnegative left side proves \(\int p_\varepsilon=f(0)\). Fourier inversion, now with both transforms integrable, gives
\(f_\varepsilon(t)=\int e^{it\lambda}p_\varepsilon(\lambda)d\lambda\).

The finite positive measures \(\mu_\varepsilon=p_\varepsilon d\lambda\), of this fixed total mass, have a weakly convergent subnet as functionals on \(C_0(\mathbb R)\), by weak-star compactness. There is no loss of mass at infinity as \(\varepsilon\downarrow0\): for \(a>0\),
\[
\int\left(1-\frac{\sin(a\lambda)}{a\lambda}\right)d\mu_\varepsilon
=f(0)-\frac1{2a}\int_{-a}^a f_\varepsilon(t)dt.
\tag{CFPA.5}
\]
The right side tends uniformly to zero when \(a\downarrow0\) and \(0<\varepsilon\le1\), by continuity of \(f\) at zero. The integrand is at least \(1/2\) when \(|\lambda|\ge2/a\). Thus the measures are uniformly tight. Riesz representation gives a finite positive limiting measure \(\mu\), with total mass \(f(0)\). Tightness allows the convergence to be tested against the bounded character \(e^{it\lambda}\), by a compact cutoff and a uniformly small tail. It follows that
\[
f(t)=\int_{\mathbb R}e^{it\lambda}d\mu(\lambda),
\qquad \mu(\mathbb R)=f(0).
\tag{CFPA.6}
\]
Uniqueness follows from Gaussian smoothing: a finite complex measure with identically zero Fourier transform has zero convolution with every Gaussian, by Fubini and the Gaussian inversion formula; those Gaussian convolutions approximate the measure against every continuous compactly supported test, so the measure is zero. This proves the required representation without an unproved spectral decomposition.

Apply this result to \(f_x\), obtaining \(\mu_x\) with total mass \(\|x\|^2\). For \(h\in L^1(\mathbb R)\), the Bochner integral \(V(h)x=\int h(t)V_tx\,dt\) exists and satisfies
\[
\|V(h)x\|^2
=\int_{\mathbb R}\left|\int_{\mathbb R}h(t)e^{it\lambda}dt\right|^2d\mu_x(\lambda).
\tag{CFPA.7}
\]
Indeed expand its squared norm as a double integral with integrand \(h(t)\overline{h(u)}f_x(t-u)\), then use (CFPA.6) and Fubini. The bound \(|f_x|\le\|x\|^2\) supplies absolute integrability.

If \(V(k)=0\), (CFPA.7) proves that \(\mu_x\) is supported on the zero set of \(\varphi(\lambda)=\int k(t)e^{it\lambda}dt\). More explicitly, its complement is the union of the measurable sets \(\{|\varphi|\ge1/j\}\), each of zero measure. Suppose this zero set is a discrete countable set \(\Gamma\), as it is in (CFP5.1).

For each \(\gamma\in\Gamma\) take
\[
h_{R,\gamma}(t)=\frac1{2R}e^{-it\gamma}1_{[-R,R]}(t),
\qquad
\int h_{R,\gamma}(t)e^{it\lambda}dt
=\frac{\sin(R(\lambda-\gamma))}{R(\lambda-\gamma)},
\tag{CFPA.8}
\]
with value one at \(\lambda=\gamma\). These multipliers converge pointwise to the indicator of \(\{\gamma\}\) and are bounded by one. Formula (CFPA.7), applied to differences of the \(h_{R,\gamma}\), and dominated convergence show that \(V(h_{R,\gamma})x\) is Cauchy. Call its limit \(P_\gamma x\). Its norm is
\[
\|P_\gamma x\|^2=\mu_x(\{\gamma\}).
\tag{CFPA.9}
\]
Changing the interval of integration by a fixed translation changes its average in norm by at most \(|a|\|x\|/R\). Hence
\(V_aP_\gamma x=e^{ia\gamma}P_\gamma x\). Conversely if \(y\) is an eigenvector with this character, then \(V(h_{R,\gamma})y=y\). If \(x\) is orthogonal to all such eigenvectors, each average remains orthogonal to them, by unitarity and their eigenvector property; so its limit is zero. These facts prove that \(P_\gamma\) is exactly the orthogonal projection onto that eigenspace.

Different frequencies have orthogonal eigenspaces, because invariance of an inner product multiplies it by \(e^{it(\gamma-\eta)}\) for every \(t\). Finally (CFPA.9), countable additivity, and the support assertion give
\[
\sum_{\gamma\in\Gamma}\|P_\gamma x\|^2
=\mu_x(\Gamma)=\mu_x(\mathbb R)=\|x\|^2.
\tag{CFPA.10}
\]
Orthogonality now proves \(x=\sum P_\gamma x\) in norm. This proves every spectral statement used in CFP5, including possible zero fibres and completeness. In particular there is no undeclared continuous spectral remainder.

## Proof sources and reading scope

The full PTQ0–PTQ11 proof was read for the earlier bounded category. The relevant RTT0–RTT2, RTT5–RTT11 and RD1–RD5 were read for the actual Fréchet quotient, exact isolators, full residue and degree maps. PGF5.1–PGF5.8 and the exact Gaussian formula were read for the original Schwartz source; the preceding derivation recomputes its Fourier and Mellin constants. PSC0–PSC2 were read for the precise source kernel and quotient topology. The arithmetic identity in CFP11 is the retained proved RTT9/GIQ9 identity, not a new independent derivation of the explicit formula.

Publication source credit: Human-source attribution: the explicit formula is due to A. P. Guinand, *A summation formula in the theory of prime numbers*, Proc. London Math. Soc. (2)50 (1949),107–119, and André Weil, *Sur les formules explicites de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952),252–265. The inspected native-TeX witness is Alain Connes, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), “Riemann’s formula, von Mangoldt paper”, equations `mellin`, `bombieriexplicit`, `bombieriexplicit1`, `bombieriexplicit2` (lines463–482). The historical originals are credited through that witness; no new reading of those originals is claimed. The full logarithmic-coordinate transport and admissible-test estimates used in this programme remain in GIQ9 and the earlier complete trace derivation.

The private canonical-index title query for spectral-theorem, unitary-group and positive-definite-function sources returned no relevant exact original source for the unitary-measure argument; unrelated routing hits were not counted as reading. CFPA supplies the needed proof directly. No newly located human paper is cited as read, and no novelty claim is made for that classical analytic lemma. This note changes neither a public repository nor a publication receipt.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Continuous positivity and the actual specialization obstruction

Complete receiving calculation, CPS0–CPS8. All statements concern the actual original-zeta coefficient source, after its complete arithmetic reconstruction.

## CPS0. Definitions, construction stage and source maps

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Its addition remains retracted. No value, parity, coordinate, midpoint, metric or vector operation is assigned to it. The complete correction chains and the user's global admissibility and quotientability arguments in LATEST_DIRECT_ARGUMENTS.md were consulted before this calculation. The user's request is to derive a common receiver from all established structure, not to stipulate its faithfulness or purity. The two recovered branch histories are kept separate.

Use the actual Fréchet coefficient
\[
Q=\mathcal B/\mathcal I,\qquad
\mathcal B=\{F\text{ entire}:b_{A,M}(F)=
\sup_{|\Re s|\le A}(1+|\Im s|)^M|F(s)|<\infty
\text{ for all }A,M\},
\tag{CPS0.1}
\]
where \(\mathcal I\) requires vanishing through order \(m_\rho-1\) at every actual original nontrivial zero \(\rho\) of \(\zeta\). The Mellin source is
\[
Q\simeq A/J,\quad J=\Sigma S,\qquad
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u}.
\tag{CPS0.2}
\]
Its complete proof and source topologies are retained in RTT0–RTT1, ACD1 and AST1–AST3. The coefficient operation
\[
T_a[F]=[a^sF(s)],\qquad a>0,
\tag{CPS0.3}
\]
is continuous, preserves \(\mathcal I\), and has continuous inverse \(T_{1/a}\). Recovered integers \(n\) are genuine cover degrees, with geometric transfer \(nT_{1/n}\). General positive \(a\) is a coefficient parameter, not a noninteger cover.

Write \(\mathscr Z_L=\{\rho:\Re\rho=1/2\}\), \(\mathscr Z_O=\mathscr Z\setminus\mathscr Z_L\), and retain all multiplicities. Define the closed invariant subspaces
\[
\begin{split}
N_L&=\{F\in Q:F(\rho)=0\text{ for every }\rho\in\mathscr Z_L\},\\
N_O&=\{F\in Q:F(\rho)=0\text{ for every }\rho\in\mathscr Z_O\},\\
N_0&=N_L\cap N_O=\ker E,
\qquad E(F)=(F(\rho))_{\rho\in\mathscr Z}.
\end{split}
\tag{CPS0.4}
\]
These definitions impose conditions only on values; higher jets stay in the indicated kernels. ACD and AST calculate the actual specialization obstruction quotient as
\[
R=Q/N_O\simeq A/A_O,\qquad A_O=q^{-1}N_O.
\tag{CPS0.5}
\]
This is an existing quotient of the source, with its Fréchet quotient topology. No positive form has been selected in defining it.

## CPS1. The complete positive family and its precise radical

Let \(\mathscr P(Q)\) be the family of all continuous positive semidefinite Hermitian forms on \(Q\), linear in the first variable, satisfying
\[
B(T_nF,G)=B(F,nT_{1/n}G)
\quad(n\ge1\text{ a recovered integer};\ F,G\in Q).
\tag{CPS1.1}
\]
The complete CFP proof classifies this family without assuming any finite-support density in \(Q\):
\[
B_c(F,G)=\sum_{\rho\in\mathscr Z_L}
m_\rho c_\rho F(\rho)\overline{G(\rho)},
\quad c_\rho\ge0,\quad
c_\rho\le C(1+|\Im\rho|)^d
\tag{CPS1.2}
\]
for some finite \(C,d\) depending on the form. Conversely every such coefficient family defines a continuous form satisfying (CPS1.1). The degree factor \(n\) and all multiplicities remain in that theorem.

It follows that
\[
\bigcap_{B\in\mathscr P(Q)}\operatorname{rad}B=N_L.
\tag{CPS1.3}
\]
Indeed every form in (CPS1.2) vanishes on \(N_L\). Conversely choose \(c_\rho=1\) for every line zero. A zero diagonal value is then a sum of nonnegative numbers equal to zero, so each value \(F(\rho)\) is zero. Positivity implies that zero norm is the full radical by Cauchy–Schwarz. The argument also covers an empty line-zero set, when both sides of (CPS1.3) are all of \(Q\).

This computes a receiver radical, not the zero subspace of the original coefficient. No original jet is identified with zero in \(Q\).

## CPS2. All positive seminorms and their complete receiver

For every integer \(k\ge0\) put
\[
p_k(F)^2=\sum_{\rho=1/2+i\gamma\in\mathscr Z_L}
m_\rho(1+\gamma^2)^k|F(\rho)|^2.
\tag{CPS2.1}
\]
These are continuous seminorms on \(Q\). To verify convergence and continuity directly, choose an integer \(M\) with \(2M-2k>2\). Then
\[
p_k([F])^2\le b_{1,M}(F)^2
\sum_{\rho\in\mathscr Z_L}m_\rho(1+\gamma^2)^k
(1+|\gamma|)^{-2M}<\infty.
\tag{CPS2.2}
\]
The last convergence follows from the unconditional full zero count
\(\sum_{|\Im\rho|\le T}m_\rho=O(T\log(T+2))\), by summing over dyadic intervals. This bound on \(\mathcal B\) descends continuously through its quotient by \(\mathcal I\). Every \(p_k^2\) is a form in (CPS1.2).

Conversely, for the coefficient family of any \(B_c\), choose an integer \(k\) with \(2k\ge d\). Since
\((1+|\gamma|)^2\le2(1+\gamma^2)\), one obtains
\[
B_c(F,F)\le C2^{d/2}p_k(F)^2.
\tag{CPS2.3}
\]
Thus the topology generated by every positive form in \(\mathscr P(Q)\) is exactly the topology generated by the countable family \(p_k\). This is a proved comparison with the original Fréchet topology; equality with that original topology is not asserted.

Define the sequence space
\[
\mathcal S_L=
\left\{x=(x_\rho)_{\rho\in\mathscr Z_L}:
\|x\|_k^2=\sum_{\rho=1/2+i\gamma}m_\rho
(1+\gamma^2)^k|x_\rho|^2<\infty
\text{ for every }k\ge0\right\}.
\tag{CPS2.4}
\]
It is a complete Fréchet space: a sequence Cauchy in every displayed Hilbert norm has limits in every corresponding weighted \(\ell^2\) space, and continuity of each coordinate evaluation makes all these limits the same coordinate family. That family has every finite norm and is the simultaneous limit. The usual countable seminorm metric then proves completeness.

The map
\[
E_L:Q\longrightarrow\mathcal S_L,\qquad
F\longmapsto(F(\rho))_{\rho\in\mathscr Z_L}
\tag{CPS2.5}
\]
is continuous, has kernel \(N_L\), and has dense image. For the last assertion, the full-jet isolator \(e_{\rho,0}\) of RTT0 maps to the individual value coordinate. Hence the image contains all finite sequences. Given \(x\in\mathcal S_L\), its truncations by \(|\gamma|\le T\) converge in every \(\|\cdot\|_k\), since each defining nonnegative series converges. This proves density globally, not by a numerical test or a density assumption about primal jets.

Consequently the Hausdorff completion of \(Q/N_L\) for all its positive-form seminorms is exactly \(\mathcal S_L\), with the explicit map (CPS2.5). The original Fréchet quotient \(Q/N_L\) and this specified completion are both retained.

## CPS3. Universal Hilbert receiving property

Let \(V:Q\to K\) be any continuous linear map to a Hilbert space for which the pulled-back inner product belongs to \(\mathscr P(Q)\). The classification gives
\[
\|VF\|_K^2=B_c(F,F)\le C' p_k(F)^2
\tag{CPS3.1}
\]
with finite \(k,C'\). It follows that there is one and only one continuous linear map
\[
\widetilde V:\mathcal S_L\longrightarrow K,
\qquad V=\widetilde V E_L.
\tag{CPS3.2}
\]
To construct it, first set \(\widetilde V(E_LF)=VF\). Equality of two source images means their difference is in \(N_L\), hence has zero norm under \(V\), so this is well defined. Inequality (CPS3.1) makes the map continuous for \(\|\cdot\|_k\); extend it to the complete limit of each approximating sequence in the dense subspace \(E_LQ\). The same bound makes the extension independent of the sequence, and uniqueness follows from density.

The coefficient action on this receiver is explicit:
\[
(\widetilde T_a x)_\rho=a^{1/2+i\gamma}x_\rho,
\qquad
\|\widetilde T_a x\|_k^2=a\|x\|_k^2.
\tag{CPS3.3}
\]
It is strongly continuous in \(a>0\) in each norm, by dominated convergence on compact parameter intervals, and \(E_LT_a=\widetilde T_aE_L\). An equivariance identity for \(V\) with continuous Hilbert receiving operators extends through (CPS3.2) by this density argument. The factor \(a^{1/2}\) has not been dropped from the original transfer.

## CPS4. The existing specialization obstruction has zero positive receiver

The quotient map \(\pi:Q\to R=Q/N_O\) intertwines every \(T_a\), since \(N_O\) is invariant. Suppose \(B_R\) is any continuous positive Hermitian form on \(R\) with the actual integer transfer-adjoint identity. Pulling it back along \(\pi\) gives a form \(B\in\mathscr P(Q)\). For every actual line zero \(\rho\), the full-jet isolator \(e_{\rho,0}\) belongs to \(N_O\), because its value at every off-line zero vanishes. Its image in \(R\) is zero. Applying (CPS1.2) yields
\[
0=B_R(\pi e_{\rho,0},\pi e_{\rho,0})
=B(e_{\rho,0},e_{\rho,0})=m_\rho c_\rho.
\tag{CPS4.1}
\]
Every \(m_\rho\) is a positive integer, so every coefficient \(c_\rho\) is zero. Therefore \(B=0\). Surjectivity of \(\pi\) gives
\[
\boxed{\mathscr P(R)=\{0\}.}
\tag{CPS4.2}
\]
No existence or nonexistence of off-line zeros entered this proof. No finite primal-block density was used. It follows also that every continuous Hilbert receiving map from \(R\) whose inner product satisfies that transfer identity is the zero map: its squared norm is zero on each source element.

The original invariant-cycle obstruction remains the actual image
\[
\beta_rQ=b_rA,\qquad
\beta_r=D_r^*\mathsf JE,\qquad b_r=\beta_rq,
\tag{CPS4.3}
\]
and \([F]\mapsto-\beta_rF\) identifies the original specialization cokernel \(R\) algebraically with the signed boundary image. AST proves its original quotient topology and its dense injective Hilbert receiving map. That receiving map does not acquire the positive transfer-adjoint identity from injectivity or density. Equation (CPS4.2) computes the zero positive receiver of this exact obstruction; it does not prove \(R=0\).

## CPS5. The source subcomplex still supplies the whole positive completion

Restrict (CPS2.5) to the actual source kernel \(N_O\). Its kernel is \(N_O\cap N_L=N_0\). Its image still contains every finite line-value sequence, by the same full-jet isolators. Therefore
\[
\widehat{(N_O/N_0)}^{\,(p_k)}\xrightarrow{\sim}\mathcal S_L
\quad\text{and}\quad
\widehat{(Q/N_L)}^{\,(p_k)}\xrightarrow{\sim}\mathcal S_L
\tag{CPS5.1}
\]
are the same completion under the actual inclusion \(N_O\hookrightarrow Q\). The notation on the left specifies the seminorms inherited from (CPS2.1). It does not assert that every continuous positive form intrinsic to \(N_O\) extends to \(Q\).

This identifies the positive effect of the exact source row and its strong dual:
\[
0\longrightarrow N_O\longrightarrow Q\longrightarrow R\longrightarrow0,
\qquad
0\longrightarrow R'_\beta\longrightarrow Q'_\beta
\longrightarrow (N_O)'_\beta\longrightarrow0.
\tag{CPS5.2}
\]
The second row is the strict topological row proved in AST2, not a newly presumed exactness of arbitrary dualization. The embedding of \(R'_\beta\) is exactly \(N_O^\perp\). After \(q'\), it is \(A_O^\perp\), the strong closure of the Gysin attaching image in GDC. Thus the subcomplex whose transpose yields the split current receiver retains the entire completion (CPS5.1), while its removed coefficient quotient has precisely (CPS4.2). Both sides of the original exact row remain explicit.

## CPS6. The original form and its full complementary term

The original Weil form remains
\[
W(F,G)=\sum_{\rho\in\mathscr Z}m_\rho
F(\rho)\overline{G(1-\overline\rho)}
=W_L(F,G)+W_O(F,G),
\tag{CPS6.1}
\]
where
\[
W_L(F,G)=\sum_{\rho\in\mathscr Z_L}m_\rho
F(\rho)\overline{G(\rho)},\qquad
W_O(F,G)=\sum_{\rho\in\mathscr Z_O}m_\rho
F(\rho)\overline{G(1-\overline\rho)}.
\tag{CPS6.2}
\]
Absolute convergence follows from the full zero count and rapid strip decay, or from RTT1's Hilbert comparison. The form on \(\mathcal S_L\) with weights \(c_\rho=1\) pulls back to exactly \(W_L\). Its difference from the original form is exactly \(W_O\), with the displayed reflection and all multiplicities retained. Restriction to \(N_O\) kills \(W_O\), because both arguments have every off-line value zero. This is a direct consequence of the source restriction, not a claim that the original off-line term vanished on \(Q\).

For any actual off-line reflection pair \(\rho,\rho^\#\), use their original full-jet isolators and let \(F=e_{\rho,0}-e_{\rho^\#,0}\). Its exact original value is
\[
W(F,F)=-2m_\rho,
\quad W_L(F,F)=0,
\quad W_O(F,F)=-2m_\rho.
\tag{CPS6.3}
\]
The plus combination has value \(+2m_\rho\). These formulas apply to each member of the actual off-line divisor, without claiming such a member exists. They prove that the positive quotient has not invisibly reproduced a nonzero complementary term. They are exact global source calculations, not numerical searches.

The multiplier used in CFP's source integral is retained in full:
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\frac18,
\tag{CPS6.4}
\]
\[
F_0(-2j)=\frac{j(2j+1)(-1)^j\pi^j}{2j!}\zeta'(-2j)
\quad(j\ge1).
\tag{CPS6.5}
\]
Its full local unit at every nontrivial zero is the one in ADC1.5. These values and factors remain part of the original-zeta comparison; using its vanishing action on \(Q\) does not replace original \(\zeta\) or suppress its trivial-zero and pole data. PSC retains the exact full arithmetic trace decomposition and its endpoint and Gamma terms. Both endpoint lines in the sheaf comparison remain as ACD/AST's separate labelled summands; none is removed by (CPS0.4).

## CPS7. What the new calculation adds to the weight argument

PTQ classified bounded forms on the value Hilbert space. CFP and CPS classify every continuous positive transfer-adjoint form on the actual Fréchet source, including polynomially unbounded value weights, and compute their complete common receiver. This closes the earlier restriction to Hilbert-bounded forms. It also identifies the positive receiver of the actual specialization obstruction as zero by (CPS4.1), using the original quotient and isolators.

The original Deligne comparison is sharper than the existence of a positive receiver: DC6–DC8 derives disjoint weights from geometric inputs and kills the actual boundary image. Here ACD8 and DCA10 retain matching source and target characters on that image. CPS computes what all compatible positive receivers do to the existing image, while AST gives its exact continuous dual. The full source-to-receiver map and its radical have therefore been calculated. They are not a proof that the original boundary is null-homotopic.

The next source-derived comparison is now precise: any proposed positive geometric receiving map must be calculated before completing it, with its kernel compared to \(N_L\) and its original trace compared to (CPS6.1), including \(W_O\). This is not an assumed additional theorem. The present calculation already tests the canonical map \(E_L\) and the actual AST source restriction: both give (CPS5.1), both have the displayed kernels, and their original trace difference is (CPS6.2). No declaration of purity has been used to close that difference.

## CPS8. Proof and source coverage

The entire ADC0–ADC9 and DCA0–DCA12 proofs were read, including the complete nearby-sheet corrections, their cone homotopies, the genuine integer degree maps, the endpoint lines and the exact original specialization cross. The entire ACD0–ACD8 and AST0–AST9 comparisons were read; AST's updated review of the final GDC source is retained. The complete CFP proof is the analytic input to CPS1. RTT's original full-jet source and exact residue comparison, PTQ's bounded-form theorem, PSC's full arithmetic decomposition and GDC's strong topology are retained alongside this proof.

Human coefficient source: Alain Connes and Caterina Consani, *Schemes over* \(\mathbb F_1\) *and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). Weight comparison: Pierre Deligne, *La conjecture de Weil. II*, [IHÉS 52 (1980), §3.6](https://numdam.org/item/PMIHES_1980__52__137_0/). Existing exact reading ledgers remain authoritative; no new whole-human-paper reading is claimed here. CFP records its own exact analytic source and proof coverage. These receiving theorems do not assert a proof of RH.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# The full multiplier domain of the actual specialization source

Complete derivation. Stable proof locators **ADM0–ADM9**.

## ADM0. Construction stage and the receiving calculation

The supporting datum is \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every scalar, coefficient, quotient and analytic variable below occurs after complete-history arithmetic reconstruction. The two branches retain their own recovered counters. No arithmetic, metric, midpoint, coordinate or retracted addition is assigned to the support.

The current construction guide, the connected correction chain, and WU062/WU064–WU065 govern this operation. The source is the actual AST specialization quotient. AST0–AST9 was read completely, together with GMS1–GMS4 and GMS9–GMS11. ECI5–ECI6 and ECI9–ECI12, and ECR's original-source embedding and separator comparison, were read for the receiving maps below. These are programme proofs, not new readings of their entire human-source literature.

ECI5.2–ECI5.3 already gives the weighted evaluation maps individually; ECI5.5–ECI5.6 gives their full original residue realization and strong convergence. ECR6 and ECI9 already prove the separator's unchanged action on original tests and its different translated action. AST identifies the actual quotient topology and continuous dual. The new calculation constructs their common multiplier domain, the exact action on the literal AST complexes and continuous transposes, and the complete normal-ideal comparison with that same source.

Derived module statements use algebraic modules over the explicitly defined ring \(M\). Each specified fixed multiplier and source map is also continuous for its stated topology. No unspecified continuous derived category or bounded action on the whole Hilbert space is presumed.

## ADM1. The original source and the actual quotient

Retain
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):
f(-v)=f(v),\ f(0)=0,\ \int_{\mathbb R}f(v)\,dv=0\},
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for every }N,j\ge0\},
\]
\[
\Sigma f(u)=2\sum_{k\ge1}f(ku),\quad J=\Sigma S,\quad
q:A\to Q=A/J,\quad B=A'_\beta .
\tag{ADM1.1}
\]
The proved exact-image theorem makes \(J\) closed and \(\Sigma:S\to J\) a topological isomorphism. The original Mellin comparison is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}{\pi}
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{ADM1.2}
\]
It identifies \(A\) with the Fréchet space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{a,N}(F)=\sup_{|\Re s|\le a}(1+|\Im s|)^N|F(s)|<\infty
\text{ for all }a,N\ge0\}.
\]
It identifies \(J\) with the closed ideal \(\mathcal I\) of all full vanishing jets at every actual nontrivial zero \(\rho\) of original \(\zeta\), to order \(m_\rho\). Thus \(\mathcal Q=\mathcal B/\mathcal I\) is the Mellin presentation of \(Q\).

The retained full divisor comes from the actual source:
\[
f_0(v)=\frac{\pi}{2}v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{ADM1.3}
\]
It belongs to \(\mathcal B\), and
\[
F_0(0)=F_0(1)=\frac18,\quad F_0(-1)=F_0(2)=\frac{\pi}{24},\quad
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)\ne0.
\tag{ADM1.4}
\]
At an actual nontrivial zero, the original local expression is
\[
F_0(\rho+z)=z^{m_\rho}
\frac{(\rho+z)(\rho+z-1)}8\pi^{-(\rho+z)/2}
\Gamma((\rho+z)/2)\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{ADM1.5}
\]
Every derivative uses the full Leibniz sum of these factors. In particular
\[
(hF)^{(j)}(\rho)=\sum_{k=0}^j\binom jk
h^{(k)}(\rho)F^{(j-k)}(\rho).
\tag{ADM1.6}
\]
No value-only map replaces this complete source ideal. The original unit and prime-power repetitions remain
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_p\sum_{k\ge1}(\log p)p^{-ks}\quad(\Re s>1).
\tag{ADM1.7}
\]

Let \(\mathscr Z\) denote the distinct actual nontrivial zeros with multiplicities, \(\rho^\#=1-\overline\rho\), and
\[
H=\ell^2(\mathscr Z,m),\quad
\langle x,y\rangle_+=\sum_\rho m_\rho x_\rho\overline{y_\rho},
\quad(\mathsf Jy)_\rho=y_{\rho^\#},\quad
(EF)_\rho=(\Theta_QF)(\rho).
\tag{ADM1.8}
\]
The inner product is linear in its first variable. The original source theorems prove \(E:Q\to H\) continuous and realize every finite value vector by full-jet isolators. Write \(\mathscr Z_L,\mathscr Z_O\) for the line and off-line subsets, without assuming either empty. For the fixed recovered parameter \(r>1\), retain
\[
d_r(\rho)=e^{-i\Im\rho\log r}
(r^{\Re\rho}-r^{1-\Re\rho}),\quad
(D_ry)_\rho=d_r(\rho)y_\rho,\quad
\beta_r=D_r^*\mathsf JE,\quad b_r=\beta_rq.
\tag{ADM1.9}
\]
Thus \((\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#)\).
AST proves
\[
N_O=\ker(P_OE)=\ker\beta_r,\quad A_O=q^{-1}N_O,\quad
\mathcal R=Q/N_O\simeq A/A_O.
\tag{ADM1.10}
\]
These are closed kernels with their original quotient topologies. \(\mathcal R\) is Montel Fréchet. Its strong dual is identified topologically with \(N_O^\perp\subset Q'_\beta\), then \(A_O^\perp\subset B\); AST3 proves the needed bounded lifts. At a line zero, \(N_O\) retains the whole multiplicity block. At an off-line zero it retains every positive-order jet. Only that zero's value enters \(\mathcal R\).

## ADM2. The exact common multiplier domain

Use the original algebra
\[
M=\{h\in\mathcal O(\mathbb C):
\forall a\ge0\ \exists C_a>0,\ d_a\in\mathbb Z_{\ge0}\
|h(x+it)|\le C_a(1+|t|)^{d_a}\quad(|x|\le a)\}.
\tag{ADM2.1}
\]
GMS1 proves that each fixed multiplier acts continuously on \(\mathcal B,\mathcal I,Q\), with
\(b_{a,N}(hF)\le C_a b_{a,N+d_a}(F)\).
Equation (ADM1.6) preserves all full jets.

Put \(w_\rho=1+|\Im\rho|\), and for integers \(N\ge0\) define
\[
p_N(y)^2=\sum_\rho m_\rho w_\rho^{2N}|y_\rho|^2,\quad
H_N=\{y:p_N(y)<\infty\},\qquad H_\infty=\bigcap_{N\ge0}H_N.
\tag{ADM2.2}
\]
The increasing norms \(p_N\) give its topology. A sequence Cauchy in all these norms has a limit in each complete \(H_N\). Coordinate convergence shows these limits are the same sequence, which lies in every \(H_N\). This proves completeness and the Fréchet property.

Let \(P_T\) retain every actual zero with \(|\Im\rho|\le T\), with its full multiplicity weight. There are finitely many such zeros. Directly,
\[
p_N((1-P_T)y)\le(1+T)^{-1}p_{N+1}(y).
\tag{ADM2.3}
\]
The inclusions \(H_{N+1}\to H_N\) are compact, since their finite-rank approximants \(P_T\) converge in operator norm. A bounded subset of \(H_\infty\) has uniformly small tails in each \(p_N\), and its finite-coordinate projections are bounded in finite-dimensional spaces. It is totally bounded in each norm, hence in the Fréchet metric. Completeness makes its closure compact, proving the Montel property. The same estimate proves \(P_Ty\to y\) in \(H_\infty\), uniformly on bounded subsets. Finite-coordinate vectors are dense. The line/off-line projections are contractions and reflection is isometric in every norm, so
\[
H_\infty=H_{\infty,L}\oplus H_{\infty,O}
\tag{ADM2.4}
\]
is a direct sum of closed complemented subspaces.

For \(h\in M\), define the maximal diagonal operator on \(H\):
\[
(\mathfrak m_h^\#y)_\rho=h(\rho^\#)y_\rho,\qquad
\operatorname{Dom}\mathfrak m_h^\#
=\{y\in H:\sum_\rho m_\rho|h(\rho^\#)y_\rho|^2<\infty\}.
\tag{ADM2.5}
\]
It is densely defined and closed. Finite-coordinate vectors lie in its domain; convergence of a graph sequence in \(H\oplus H\) gives coordinatewise \(z_\rho=h(\rho^\#)y_\rho\).
The established strip \(0<\Re\rho<1\), with \(\Im\rho^\#=\Im\rho\), implies
\[
p_N(\mathfrak m_h^\#y)\le C_h p_{N+d_h}(y).
\tag{ADM2.6}
\]
Thus \(H_\infty\) is invariant and each multiplier acts continuously there, obeying all algebra identities.

Conversely \(h_N(s)=(1+s)^N\) belongs to \(M\), and
\[
|1+\rho^\#|=\sqrt{(2-\Re\rho)^2+(\Im\rho)^2}
\ge w_\rho/\sqrt2,\qquad
p_N(y)\le2^{N/2}\|\mathfrak m_{h_N}^\#y\|_H.
\tag{ADM2.7}
\]
The two inequalities prove
\[
\boxed{\ \bigcap_{h\in M}\operatorname{Dom}\mathfrak m_h^\#
=H_\infty,\qquad
\text{the full graph topology equals the }(p_N)\text{ topology}.\ }
\tag{ADM2.8}
\]
No topology on \(M\), or bounded action on all \(H\), is presumed. For the common domain, finite truncations converge in every graph seminorm by (ADM2.3)–(ADM2.6). They also form a core for each individual maximal operator: for any \(y\in\operatorname{Dom}\mathfrak m_h^\#\), the squared graph-tail norm is the sum of the tails of the two convergent series \(\sum m_\rho|y_\rho|^2\) and \(\sum m_\rho|h(\rho^\#)y_\rho|^2\), and therefore tends to zero. Replacing \(h(\rho^\#)\) by \(h(\rho)\) gives the unreflected action \(\mathfrak m_h\) on the same common domain.

## ADM3. The original source and specialization image

The already continuous \(E:Q\to H\) and GMS's full quotient multiplier give
\[
p_N(EF)\le2^{N/2}\|E((1+s)^NF)\|_H.
\tag{ADM3.1}
\]
Thus \(E:Q\to H_\infty\) is continuous without a new zero-count hypothesis. Equivalently, ECI5's original estimate is
\[
p_N(EF)\le C_4 b_{1,N+2}(\widetilde F),\qquad
C_4^2=\sum_\rho m_\rho w_\rho^{-4}<\infty
\tag{ADM3.2}
\]
for every entire representative; taking infima gives the quotient estimate.
Since \(r^x-r^{1-x}\) increases from \(1-r\) to \(r-1\) on \([0,1]\),
\[
p_N(\beta_rF)\le(r-1)p_N(EF).
\tag{ADM3.3}
\]
Consequently \(b_r:A\to H_{\infty,O}\), \(\beta_r:Q\to H_{\infty,O}\), and
\[
\overline\beta_r:\mathcal R\longrightarrow H_{\infty,O}
\tag{ADM3.4}
\]
are continuous; the latter is injective with the original quotient topology.

For a finite off-line vector \(y\), prescribe
\(F(\rho^\#)=y_\rho/\overline{d_r(\rho)}\) on its support and zero values at all other zeros, using the original full-jet isolators. Then \(\beta_rF=y\). Therefore
\[
\overline{E(Q)}^{\,H_\infty}=H_\infty,\qquad
\overline{\beta_rQ}^{\,H_\infty}=H_{\infty,O}.
\tag{ADM3.5}
\]
Its image is also dense in \(H_O\). Give \(I_r=\beta_rQ\) its transported quotient topology from \(\mathcal R\), its subspace topology in \(H_{\infty,O}\), or its subspace topology in \(H_O\). The identity maps from the first to the second and from the second to the third are continuous. Only for the first has inverse continuity of \(\overline\beta_r\) been proved. Density establishes neither surjectivity onto \(H_{\infty,O}\) nor equality of these topologies.

The exact multiplier direction is
\[
E(hF)=\mathfrak m_hEF,\qquad
\beta_r(hF)=\mathfrak m_h^\#\beta_rF.
\tag{ADM3.6}
\]
The second coordinate is \(\overline{d_r(\rho)}h(\rho^\#)F(\rho^\#)\).
Thus \(N_O,A_O,\mathcal R,I_r\) are actual \(M\)-modules and every displayed source, quotient and boundary map is \(M\)-linear. Each fixed multiplier is continuous on the source quotient and the \(H_\infty\)-subspace image topology. Continuity for the coarser Hilbert image topology is not asserted for arbitrary \(h\).

AST's exact parameter maps \(M_{r,t}=V_{r,t}^*\) and inverses have the bounded diagonal constants of AST6.2. The same constants apply to every \(p_N\). They commute with \(\mathfrak m_h^\#\), satisfy \(\beta_r=M_{r,t}\beta_t\), and fix \(\mathcal R\). This extends the actual parameter comparison to the common domain without identifying the numerical defect sizes.

## ADM4. The strong dual domain and actual transpose

Every continuous complex-linear functional on \(H_\infty\) has a unique presentation
\[
\ell_z(y)=\sum_\rho m_\rho y_\rho\overline{z_\rho},\qquad
\sum_\rho m_\rho w_\rho^{-2N}|z_\rho|^2<\infty
\text{ for some }N.
\tag{ADM4.1}
\]
Indeed continuity bounds it by \(Cp_N\) for one increasing norm; extension to the completion \(H_N\) and Hilbert Riesz give this expression. Conversely Cauchy–Schwarz gives
\[
|\ell_z(y)|\le\|z\|_{-N}p_N(y).
\tag{ADM4.2}
\]
Coordinate vectors prove uniqueness. The presentation is anti-linear in \(z\), or linear on its conjugate complex space. We use the actual strong dual topology \(H_\infty'{}_\beta\); no unproved identification with an inductive-limit topology is used.

The map \(R_\infty:\overline H\to H_\infty'{}_\beta\), \(R_\infty(\overline y)=\ell_y\), is continuous, since a bounded test set has bounded \(p_0\). Furthermore
\[
\sup_{y\in K}|\ell_{(1-P_T)z}(y)|
\le\frac{\|z\|_{-N}}{1+T}\sup_{y\in K}p_{N+1}(y).
\tag{ADM4.3}
\]
Thus finite-coordinate functionals, and hence \(R_\infty(\overline H)\), are strongly dense. This does not identify its image topology with the Hilbert topology.

The complete transpose action is
\[
h\cdot\ell=\ell\circ\mathfrak m_h^\#,\qquad
h\cdot\ell_z=\ell_{\,(\overline{h(\rho^\#)}z_\rho)_\rho}.
\tag{ADM4.4}
\]
The sequence on the right has polynomially larger weighted order. Strong continuity follows because \(\mathfrak m_h^\#\) preserves bounded sets. This action need not preserve the embedded \(\overline H\).

Form the actual transposes
\[
\sigma_{r,\infty}=(\beta_r:Q\to H_\infty)',\qquad
a_{r,\infty}=(b_r:A\to H_\infty)'=q'\sigma_{r,\infty}.
\tag{ADM4.5}
\]
They are strongly continuous and \(M\)-linear, for the transpose actions on \(Q',B\). On \(R_\infty(\overline H)\) they are exactly \(\sigma_r,a_r\), by the original pairing. Density (ADM3.5) gives
\[
\ker\sigma_{r,\infty}=\ker a_{r,\infty}
=\{\ell_z:z\text{ is supported on }\mathscr Z_L\}.
\tag{ADM4.6}
\]
They factor through the actual strong dual of \(\mathcal R\):
\[
\gamma_{r,\infty}(\ell)([F])=\ell(\beta_rF).
\tag{ADM4.7}
\]
Its restriction to functionals supported on \(\mathscr Z_O\) is injective. AST's old \(\gamma_r(\overline{H_O})\) is already strongly dense in \(\mathcal R'\), and lies in this image. Every image functional annihilates \(N_O\). Using AST's closed strong embeddings proves
\[
\overline{\operatorname{im}\gamma_{r,\infty}}^\beta=\mathcal R'_\beta,\quad
\overline{\operatorname{im}\sigma_{r,\infty}}^\beta=N_O^\perp,\quad
\overline{\operatorname{im}a_{r,\infty}}^\beta=A_O^\perp.
\tag{ADM4.8}
\]
No surjectivity or closed image is inferred.

For \(h\in M\), the sequence \(h(\rho)\) belongs to one weighted dual space, by the polynomial bound and ECI5's \(\sum m_\rho w_\rho^{-4}<\infty\). Therefore \(E'\ell_{(h(\rho^\#))_\rho}\) is exactly the old ECI5.1 functional
\(\sum m_\rho F(\rho)\overline{h(\rho^\#)}\).
Its full residue representative remains ECI5.5, with
\(m_\rho(-1)^{m_\rho-1}u_\rho(0)\overline{h(\rho^\#)}\) and
\(\zeta(\rho+z)=z^{m_\rho}u_\rho(z)\).
The new domain includes these existing maps and supplies their common receiving space; it does not replace the residue denominator.

## ADM5. The literal AST complexes and their full transpose action

On a positively oriented pole disk, define the common-domain subcomplexes
\[
\mathscr P_{r,\infty}=
[\underline A^{-1}\xrightarrow{+b_r}i_*H_\infty^0],\qquad
\mathscr P_{O,\infty}=
[\underline{A_O}^{-1}\xrightarrow0 i_*H_\infty^0].
\tag{ADM5.1}
\]
These use the same actual \(b_r\), now with its proved smaller codomain. There are literal exact sequences
\[
0\to\mathscr P_{O,\infty}\to\mathscr P_{r,\infty}
\xrightarrow{(\widetilde\pi,0)}\underline{\mathcal R}[1]\to0,
\]
\[
0\to\mathscr P_{r,\infty}\xrightarrow{(1_A,\iota)}
\mathscr P_r\to i_*(H/H_\infty)[0]\to0 .
\tag{ADM5.2}
\]
The second quotient is retained with its quotient topology; its denominator is dense. It is not declared zero, and the inclusion is not declared a quasi-isomorphism. The first sequence is strict on each nonzero coefficient quotient by AST3. The nearby coefficients and specialization source of the common-domain object are unchanged: its localization boundary is \(-b_r:A\to H_\infty\), with image \(I_r\) and source quotient \(\mathcal R\).

For \(h\in M\), give \(A,A_O,\mathcal R\) their actual source actions and \(H_\infty\) the action \(\mathfrak m_h^\#\). Equation (ADM3.6) proves that every map of the first sequence is \(M\)-linear. The second sequence remains a continuous comparison with the original Hilbert complex; arbitrary \(h\) is not declared an operator on its entire Hilbert point term.

The positive differentiate-a-lift connecting map is \(+\overline\beta_r:\mathcal R\to H_\infty\). The literal cone convention retained in AST5 instead has
\[
\mathscr P_{O,\infty}\to\mathscr P_{r,\infty}
\xrightarrow{+\widetilde\pi}\underline{\mathcal R}[1]
\xrightarrow{\kappa_{r,\infty}}\mathscr P_{O,\infty}[1],
\qquad H^{-1}(i^*\kappa_{r,\infty})=-\overline\beta_r.
\tag{ADM5.3}
\]
Indeed a lift \(a\) of a quotient class is represented by the cone cocycle
\((a,-b_ra)\); positive projection to the shifted subcomplex gives \(-b_ra\).
The full coefficient extension \(0\to A_O\to A\to\mathcal R\to0\) remains part of this triangle. Its derived connecting morphism is not replaced by its stalk map or by a presumed \(M\)-linear section.

For the continuous transpose, use the fine resolution
\[
\mathscr E_A^0\quad\longrightarrow\quad
\mathscr E_A^1\oplus i_*H_\infty\quad\longrightarrow\quad
\mathscr E_A^2
\]
in degrees \((-1,0,1)\), with \(d^{-1}f=(-df,b_rf(p))\) and
\(d^0(\omega,y)=-d\omega\).
The coefficient Poincaré contraction applies because \(H_\infty\) is complete and its point summand uses only evaluation. The compact-test dual is the current cone
\[
\mathscr E_{r,\infty}
=\operatorname{Cone}(-\delta_pa_{r,\infty})[-1],
\quad
d^{-1}v=(-d_Tv,0),\quad
d^0(u,\ell)=-d_Tu+\delta_pa_{r,\infty}\ell.
\tag{ADM5.4}
\]
The comparison from the literal Hom differential uses the same degree signs
\((-1,+1,-1)\) proved in ACD2–ACD3. Substituting
\(a_{r,\infty}=b_r'\) verifies the degree-zero square. No exactness of continuous dualization on arbitrary complexes is needed.

Its actual \(M\)-action uses the transpose of \(h_A\) on current tests and (ADM4.4) on the point dual. The equation
\(a_{r,\infty}(\mathfrak m_h^\#)'=h_A'a_{r,\infty}\)
proves the chain identity. The map
\[
\mathscr E_r\to\mathscr E_{r,\infty}
\]
is identity on the current terms and \(R_\infty:\overline H\to H_\infty'\) on the point coordinate. It is the actual continuous transpose of the second sequence's inclusion in (ADM5.2). Its underlying algebraic quotient is the retained point complex
\(i_*(H_\infty'/R_\infty\overline H)[0]\), with its actual quotient topology.

The AST transpose triangle now has the exact full-multiplier form
\[
\underline{\mathcal R'_\beta}[1]\to\mathscr E_{r,\infty}
\to\underline{(A_O)'_\beta}[1]\oplus i_*H_\infty'
\to\underline{\mathcal R'_\beta}[2].
\tag{ADM5.5}
\]
To prove it, restrict currents from \(A\) to \(A_O\) and leave the point coefficient unchanged. Its attaching term becomes zero, since \(a_{r,\infty}\) annihilates \(A_O\). Cancel the common point term in the fibre. The remaining constant-current restriction has kernel
\(A_O^\perp\simeq\mathcal R'_\beta\), by the proved strict strong-dual row AST3.5. Compact-test contractions give (ADM5.5). All maps commute with the transposed \(M\)-actions because \(A_O\) is invariant. The map from AST5.4 into this triangle is identity on its coefficient row and \(R_\infty\) on the point term. It retains the entire previous triangle and identifies the precise enlargement required by arbitrary multipliers.

Both original endpoint lines are reattached by direct summands \(i_*E_p[1]\) and \(i_*E_p'[-1]\). In the original coordinate order
\((c_0,c_1,d_0,d_1)\) the multiplier characters are
\[
(h(0),h(1),h(1),h(0)).
\tag{ADM5.6}
\]
Their continuous transposes have the same scalar characters, without complex conjugation of a complex-linear transpose. Endpoints have zero nearby term and remain separate from all zeta-value kernels.

## ADM6. The already constructed separator on this exact source

To avoid collision with the evaluation map \(E:Q\to H\), write \(E_{\rm sep}(s)\) for the entire function named \(E(s)\) in GSL/GMS. This is the same function, with its entire construction retained:
\[
G(s)=F_0(s)F_0(s+1),\quad r_0(t)=\varepsilon(1+t^2)^{-3},
\quad\chi(x+it)=\eta(x/r_0(t)),
\]
\[
v(w)=\frac{\bar\partial\chi(w)}{G(w)}
\text{ on its zero-free transition corridor},\quad v=0\text{ off it},
\]
\[
u(s)=\frac1\pi\int_{\mathbb C}\frac{e^{(s-w)^2}}{s-w}v(w)\,dA(w),
\qquad E_{\rm sep}(s)=\chi(s)-G(s)u(s).
\tag{ADM6.1}
\]
GSL proves convergence, holomorphic continuation and polynomial strip bounds with these full factors. No new cutoff or chosen value interpolant is substituted. Set
\[
c(s)=1-E_{\rm sep}(s-1)\in M.
\]
Its full jets are
\[
c-1\in(s-\rho)^{m_\rho}\mathcal O_\rho,\qquad
c\in(s-(\rho+1))^{m_\rho}\mathcal O_{\rho+1}.
\tag{ADM6.2}
\]
Thus \(c=1\) on the entire original \(Q\), including all higher jets. It follows on the actual source, not only its finite blocks, that
\[
c_{\mathcal R}=1,\quad
\mathfrak m_c^\#=1\text{ on }H_\infty,\quad
c_{\mathcal R'}=1,\quad c_{H_\infty'}=1,\qquad
\beta_r(cF)=\beta_rF.
\tag{ADM6.3}
\]
The point identity holds because \(\rho^\#\) is an actual original zero. It extends as the identity on \(H\) for this particular multiplier; it does not extend arbitrary \(h\).

Consequently
\[
c\,\kappa_{r,\infty}
=\kappa_{r,\infty}\,c_{\mathcal R}
=\kappa_{r,\infty}
\tag{ADM6.4}
\]
in the derived \(M\)-module sheaf category of the displayed complexes. This is central \(M\)-linearity of their actual connecting map, not a conjugation weight. Its stalk equation is exactly
\(\mathfrak m_c^\#(-\overline\beta_r)=-\overline\beta_r\).
The action need not be the identity on all \(A\) or \(A_O\); it is not an idempotent on the complete source complex. Its endpoint characters remain \(c(0),c(1),c(1),c(0)\), with no imposed zero or one values.

The translated normal action is different. On the same underlying source module put
\[
h\cdot_{+}F(s)=h(s+1)F(s),\quad
(\mathfrak m_{h,+}^\#y)_\rho=h(\rho^\#+1)y_\rho.
\tag{ADM6.5}
\]
Translation preserves \(M\). Every preceding domain estimate holds on the slightly larger strip, and
\[
\beta_r(h\cdot_+F)=\mathfrak m_{h,+}^\#\beta_rF.
\tag{ADM6.6}
\]
These are the actual normal twists, denoted \(Q(-1),\mathcal R(-1),H_\infty(-1)\) with this specified action. On them
\[
c(s+1)=1-E_{\rm sep}(s),\qquad
c_{Q(-1)}=c_{\mathcal R(-1)}=0,\qquad
\mathfrak m_{c,+}^\#=0 .
\tag{ADM6.7}
\]
All original zero jets vanish under the first multiplier, not just their values. The identity between underlying untwisted and twisted vector spaces is semilinear with respect to \(h(s)\mapsto h(s+1)\); it is not an \(M\)-linear identification of the two scalar actions.

The exact coordinate comparison is
\[
(VF)(\lambda)=F(\lambda-1),\qquad
V(h(s+1)F(s))=h(\lambda)VF(\lambda).
\tag{ADM6.8}
\]
Put \(\mathcal I_+=V\mathcal I\), \(\mathcal B_O=\Theta A_O\),
\(\mathcal B_{O,+}=V\mathcal B_O\). The resulting normal quotient source is
\[
\mathcal R_+=\mathcal B/\mathcal B_{O,+}
=\mathcal Q_+/(V N_O),\qquad \mathcal Q_+=\mathcal B/\mathcal I_+.
\tag{ADM6.9}
\]
Here \(V N_O\) means its image under the induced quotient isomorphism. The continuous normal specialization map is
\[
(\beta_{r,+}G)_\rho
=\overline{d_r(\rho)}G(\rho^\#+1),\qquad
\beta_{r,+}V=\beta_r .
\tag{ADM6.10}
\]
It is \(M\)-linear into \(H_\infty(-1)\). The coefficient \(d_r\) is the original adjoint discrepancy, not a newly assigned normal defect.

Every normal source factor remains
\[
F_+(\lambda)=VF_0(\lambda)
=\frac{(\lambda-1)(\lambda-2)}8\pi^{-(\lambda-1)/2}
\Gamma((\lambda-1)/2)\zeta(\lambda-1).
\tag{ADM6.11}
\]
Its values at \(1,2\) are \(1/8\), at \(0,3\) are \(\pi/24\); at \(1-2k\) they are exactly (ADM1.4). Its local full zero germ is (ADM1.5) translated by one, and
\(F_+^{(j)}(\lambda)=F_0^{(j)}(\lambda-1)\).
No factor or derivative is dropped by the comparison.

## ADM7. The full normal ideal maps onto the same actual specialization source

Let
\[
K_O=\mathcal I_+\cap\mathcal B_O,\qquad
q_R:\mathcal B\to\mathcal B/\mathcal B_O\simeq\mathcal R.
\]
There is an exact strict sequence of the actual Fréchet modules
\[
\boxed{\quad
0\to K_O\to\mathcal I_+\xrightarrow{\,q_R|_{\mathcal I_+}\,}
\mathcal R\to0.
\quad}
\tag{ADM7.1}
\]
For surjectivity, take any representative \(F\in\mathcal B\). The complete jet identities give \(cF\in\mathcal I_+\), while
\((c-1)F\in\mathcal I\subset\mathcal B_O\). Thus
\(q_R(cF)=q_R(F)\). Its kernel is exactly the displayed intersection, a closed subspace.

The complete topological quotient comparison and inverse are
\[
\mathcal I_+/K_O\xrightarrow{\sim}\mathcal R,\quad
[G]\mapsto q_R G,\qquad
[F]_{\mathcal B_O}\mapsto[cF]_{K_O}.
\tag{ADM7.2}
\]
If \(F\) changes by \(v\in\mathcal B_O\), then \(cv\in\mathcal I_+\cap\mathcal B_O\), proving well-definedness. If \(G\in\mathcal I_+\), then
\((c-1)G\in\mathcal B_O\cap\mathcal I_+\), proving the reverse composite. Both maps descend from continuous linear maps and are continuous for quotient topologies. This proves strictness of (ADM7.1), without a section of \(\mathcal I_+\to\mathcal R\).

The exact specialization comparison is
\[
\mathcal B\xrightarrow{\,m_c\,}\mathcal I_+
\xrightarrow{\,q_R\,}\mathcal R
\xrightarrow{\,-\overline\beta_r\,}H_{\infty,O},
\qquad
-\overline\beta_r\,q_R m_c
=-\beta_r q_{\mathcal I}.
\tag{ADM7.3}
\]
Here \(q_{\mathcal I}:\mathcal B\to\mathcal Q\) is the original quotient.
The same \(\overline\beta_r\), with its original sign and topology, receives both routes. All kernels remain: \(K_O\) in (ADM7.1), the original full \(\mathcal I\), and \(\mathcal B_O/\mathcal I=N_O\).

There is no silent descent of this map through the normal quotient \(\mathcal Q_+\). In fact every \(M\)-linear map
\(\mathcal Q_+\to\mathcal R\) is zero: it obeys
\(f=c_{\mathcal R}f=f c_{\mathcal Q_+}=0\).
The restriction of \(q_R:\mathcal B\to\mathcal R\) to its normal kernel \(\mathcal I_+\) is onto by (ADM7.1). Hence it descends through \(\mathcal Q_+\) exactly when \(\mathcal R=0\); this is a computed descent condition, not an assumption that either case holds. The same statement applies to the injective image of \(\mathcal R\) under \(\overline\beta_r\).

The original coefficient source is retained exactly. Transporting \(m_c\) back through \(\Theta\) gives
\[
a\longmapsto\frac{u^{-1/2}}{\pi}\int_{\mathbb R}
c(1/2+it)\Theta a(1/2+it)u^{-it}\,dt .
\tag{ADM7.4}
\]
Polynomial multiplier bounds and rapid strip decay prove absolute convergence after each fixed \(u\partial_u\) derivative; the Mellin isomorphism proves continuity for all source seminorms. This is the inverse Mellin representative of the original low-coordinate map, whose target is \(\Theta^{-1}\mathcal I_+\), not automatically \(J\).
In contrast GMS's unshifted normal source-return map is
\[
a\longmapsto \Theta^{-1}[c(s+1)\Theta a(s)]
=\Theta^{-1}[(1-E_{\rm sep}(s))\Theta a(s)]\in J.
\tag{ADM7.5}
\]
Its exact Schwartz representative is obtained by the already proved inverse
\(\Sigma^{-1}:J\to S\); both \(f(0)=0\) and \(\int f=0\) are retained. Since \(qJ=0\), applying \(b_r\) to (ADM7.5) gives zero. Equations (ADM7.3) and (ADM7.5) do different things precisely because of the displayed translation (ADM6.8). This extends the ECR6/ECI9 comparison to the literal AST source and connecting map.

There is also an exact diagram of normal coefficient rows:
\[
\begin{array}{ccccccccc}
0&\to&\mathcal I_+&\to&\mathcal B&\to&\mathcal Q_+&\to&0\\
&&\downarrow&&\Vert&&\downarrow\\
0&\to&\mathcal B_{O,+}&\to&\mathcal B&\to&\mathcal R_+&\to&0 .
\end{array}
\tag{ADM7.6}
\]
The left inclusion follows from \(\mathcal I\subset\mathcal B_O\) and \(V\).
Multiplication \(m_c:\mathcal B\to\mathcal I_+\) is a continuous lift through both actual kernels. Thus the already constructed normal lifting mechanism applies to the AST normal row too, while (ADM7.1) records its unchanged original specialization image.

## ADM8. Derived separation and the actual geometric action scope

The constructed source satisfies \(c_{\mathcal R}=1\), while
\(c_{\mathcal Q_+}=c_{\mathcal R_+}=0\).
For clarity the full algebraic contraction applies without a finite-support hypothesis. If \(X\) is annihilated by \(a\in M\), take a projective resolution \(P^\bullet\xrightarrow{\epsilon}X\) in degrees at most zero. In degree zero, \(\epsilon a_{P^0}=a_X\epsilon=0\); exactness and projectivity lift \(a_{P^0}\) through \(d_P^{-1}\), defining \(H^0:P^0\to P^{-1}\). For \(j<0\), suppose the next-degree identity is proved. Then
\(d_P^j(a_{P^j}-H^{j+1}d_P^j)=a_{P^{j+1}}d_P^j-(a_{P^{j+1}}-H^{j+2}d_P^{j+1})d_P^j=0\).
Exactness and projectivity therefore lift \(a_{P^j}-H^{j+1}d_P^j\) through \(d_P^{j-1}\), defining \(H^j\). This constructs \(d_PH+Hd_P=a_P\) in every degree. On
\(\operatorname{Hom}_M(P^\bullet,Y^\bullet)\), with
\(Df=d_Yf-(-1)^nfd_P\), the homotopy \(Sf=(-1)^nfH\) satisfies
\[
DS+SD=a_Y.
\tag{ADM8.1}
\]
The two terms containing \(d_YfH\) cancel and centrality gives \(fa_P=a_Yf\).
For \(X=\mathcal R\), take \(a=1-c\), and \(Y=\mathcal Q_+\) or \(\mathcal R_+\). For the reverse directions take \(a=c\). This proves
\[
\operatorname{RHom}_M(\mathcal R,\mathcal Q_+)
=\operatorname{RHom}_M(\mathcal Q_+,\mathcal R)=0,\qquad
\operatorname{RHom}_M(\mathcal R,\mathcal R_+)
=\operatorname{RHom}_M(\mathcal R_+,\mathcal R)=0.
\tag{ADM8.2}
\]
These are actual full modules; no bounded Hilbert functional calculus or continuous projectivity is inserted.

For either \(K=\mathcal I_+\) or \(K=\mathcal B_{O,+}\), the actual maps
\(i_K:K\hookrightarrow\mathcal B\) and \(m_c:\mathcal B\to K\) have both composites \(m_c\). On derived Hom from \(\mathcal R\), equation (ADM8.1), with \(a=1-c\), makes these composites homotopic to identity. Thus
\[
\operatorname{RHom}_M(\mathcal R,K)
\xrightarrow[\sim]{\,i_K\,}
\operatorname{RHom}_M(\mathcal R,\mathcal B)
\tag{ADM8.3}
\]
has the displayed full-source inverse \(m_c\). The kernels are still \(K\); no new source section is asserted. Conversely the original specialization boundary remains fixed as in (ADM6.4), because its source is \(\mathcal R\) itself and its point action is the unshifted reflected one.

The distinction between coefficient multipliers and geometry must also be kept in the literal complexes. On a pole disk the sheaf action is \(h(s)\) on \(A\) and \(h(\rho^\#)\) on \(H_\infty\). Its de Rham resolution uses this coefficient action in every form degree. It is not the same operation as a degree-\(n\) map of the underlying disk.

For the actual sphere cover, ACD/DCA's global cochain model is
\[
G_{r,\infty}=
[A^{-1}\xrightarrow{(b_r,b_r)}
H_\infty^0\oplus H_\infty^0\xrightarrow0 A^1],
\tag{ADM8.4}
\]
with the original four endpoint lines in degree \(-1\). Its exact extension of the geometric coefficient actions is
\[
h_A\text{ in degree }-1,\qquad
\mathfrak m_h^\#\oplus\mathfrak m_h^\#\text{ in degree }0,\qquad
\Theta^{-1}m_{h(s+1)}\Theta\text{ in degree }1.
\tag{ADM8.5}
\]
It is a genuine cochain \(M\)-action by (ADM3.6), since the last differential is zero. For \(h(s)=n^s\), the last action is \(nT_n\), the positive geometric degree; the point action is \(U_n^*\), and the source action is \(T_n\), exactly as in ACD7. The weighted geometric trace has source \(nT_{1/n}\), point \(T_n^*\), and last action \(T_{1/n}\); these are recorded separately and are not identified with substitution into the same pullback-character formula. DCA retains the full finite-sheet and raw-cut corrections. All its diagonal operators preserve \(H_\infty\), so its maps and their continuous transposes restrict or extend to the domain objects without changing any sheet coordinate. Noninteger positive parameters remain coefficient operations, not geometric covers.

The corresponding subcomplex uses \(A_O\) in degrees \(-1,1\), with the same point terms. Its quotient is
\[
\mathcal R[1]\oplus\mathcal R(-1)[-1].
\tag{ADM8.6}
\]
Here \(c\) is a true projection onto the first summand, and zero on the second. It is not an idempotent on all of \(G_{r,\infty}\) or its subcomplex. The low connecting component retains (ADM5.3), including the coefficient extension and the point boundary \(-\overline\beta_r\); the normal component comes from
\(0\to A_O(-1)\to A(-1)\to\mathcal R(-1)\to0\),
transported to the lower row of (ADM7.6).
Thus (ADM8.3) controls that actual normal comparison, while the full low source and its specialization image remain. Nothing in this calculation replaces their multiplier action by the shifted one.

## ADM9. Comparison with the existing extension-class maps and source scope

ECR1 constructs the actual \(M\)-map from the original cyclic extension-class module
\(\mathscr C=M/\mathfrak a\), where \(\mathfrak a\) is the full original-zero-jet ideal:
\[
\mathfrak b_t:\mathscr C\to\mathcal Q,\qquad
[h]\mapsto[g_t h],\qquad g_t(s)=e^{ts^2},\quad t>0.
\]
The source estimate
\(|g_t(\sigma+i\gamma)|=e^{t(\sigma^2-\gamma^2)}\)
proves its image lies in \(\mathcal B/\mathcal I\), with every jet retained. The existing map now has the exact domain comparison
\[
\mathscr C\xrightarrow{\mathfrak b_t}Q
\xrightarrow{\pi}\mathcal R
\xrightarrow{\overline\beta_r}H_{\infty,O},\qquad
(\beta_r\mathfrak b_t[h])_\rho
=\overline{d_r(\rho)}e^{t(\rho^\#)^2}h(\rho^\#).
\tag{ADM9.1}
\]
The kernel of this composite is the ideal of multiplier values vanishing on all actual off-line zeros, modulo \(\mathfrak a\). This follows directly from the nonzero exponential and from \(d_r(\rho)\ne0\) exactly off the line. Its finite-coordinate image is all finite off-line vectors: choose \(h\in\mathcal B\subset M\) by the original full-jet isolators, prescribing \(h(\rho^\#)=y_\rho/(\overline{d_r(\rho)}e^{t(\rho^\#)^2})\) on the finite support and zero jets at the remaining zeros. This divides only the prescribed finitely many values, never the whole function by the Gaussian. The image is therefore dense in \(H_{\infty,O}\). No topology is imposed on \(\mathscr C\), and no continuity claim for that unsupplied topology is made.

The multiplier covariance of (ADM9.1) is the reflected covariance (ADM3.6), since \(\mathfrak b_t\) is \(M\)-linear. Its separator calculation is the existing ECR6 identity transported through the newly specified domain: \(c\) is identity on its source quotient and its image. ECI9's normal equation instead uses \(c(s+1)\), exactly as (ADM6.7). ECI5's polynomial-growth residue functions enter the dual domain by (ADM4.1)–(ADM4.8). These are actual connecting maps to both existing approaches; the earlier separator conclusion itself is not claimed as new.

This completes the next calculation required by WU065. The common multiplier domain, its topology, its continuous dual, both literal source triangles, and the full normal-ideal/source comparison have been constructed. The normal ideal maps onto the original specialization source by (ADM7.1), with its complete kernel \(K_O\); the normal quotient and the original source are separated by (ADM8.2). The actual original connecting map remains fixed by the separator. The proof supplies no vanishing of \(D_r\), no new pure weight, and no claim that the source quotient is a finite-dimensional Deligne Frobenius module.

Source-use scope: AST0–AST9; GMS1–GMS4 and GMS9–GMS11, with its earlier full source-return formulas; the previously accepted ADC/ACD/DCA current, specialization and cover constructions; ECI5–ECI6 and ECI9–ECI12; ECR's source embedding and ECR6. The human origins remain Connes–Consani's actual summation sheaf, arXiv:0903.2024v3 §5, and Deligne's exact invariant-cycle cross reconstructed in DC. The new common-domain and receiving maps above are local programme derivations, not statements attributed to those authors. The full original factors and the user correction chain remain in the stated inputs.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Gaussian approximation on the complete original source and its actual defect

25 September 2026. Complete derivation, **GAP0–GAP9**.

## GAP0. The construction and the question being attempted

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Arithmetic, analytic coordinates, vector spaces and parameters below belong to the complete recovered coefficient system, after the global arithmetic comparison. They are not operations on this support. The separate branch counters remain separate. Addition at \(\tau\), an assigned metric there, and a midpoint expression for it are not used.

ECR1 constructs proper injective maps in both directions between the full original quotient and the cyclic original extension-class module. Their composites are Gaussian multiplication, not identity. AST2–AST6 construct the actual specialization quotient and its continuous transpose. The next question is whether those Gaussian composites recover identity in the original source topology and how the whole extension-class trace behaves in the same limit. This note proves those statements. No topology on an unspecified Ext group and no inverse Gaussian multiplier is presumed.

Inputs are the complete ECR0–ECR7 and ECI0–ECI13 proofs, GMS1–GMS3 and GMS9, AST1–AST6, and SDT's source topology. These are programme derivations. The human coefficient construction remains Connes–Consani, *Schemes over* \(\mathbb F_1\) *and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), as reconstructed with the retained author source in the earlier chapters. Deligne's invariant-cycle weight argument is the distinct cross reconstructed in DC0–DC12; none of its arithmetic purity hypotheses is inserted here. The local reading ledger specifies source versions and coverage.

Use the entire-function space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{A,N}(F):=\sup_{|x|\le A,\,y\in\mathbb R}
(1+|y|)^N|F(x+iy)|<\infty\quad(A,N\ge0)\}.
\tag{GAP0.1}
\]
Integer \(A,N\) give its Fréchet topology. Let \(M\) be the ring of entire functions of at most polynomial growth on each closed vertical strip; its exponent may depend on the strip. The ideal \(\mathfrak a\subset M\) imposes vanishing to the full multiplicity \(m_\rho\) at every actual nontrivial zero \(\rho\) of the original \(\zeta\). Set
\[
\mathcal I=\mathcal B\cap\mathfrak a,\qquad
Q=\mathcal B/\mathcal I,\qquad
\mathscr C=M/\mathfrak a=M e_0.
\tag{GAP0.2}
\]
The closed subspaces in AST are
\[
N_O=\ker(P_OE:Q\to H_O),\quad N_0=\ker E,
\quad\mathcal R=Q/N_O.
\tag{GAP0.3}
\]
All quotient topologies here are the original Fréchet quotient topologies. In particular no value norm replaces the topology of \(Q\) or \(\mathcal R\).

## GAP1. A full strip estimate and its quotient consequence

For \(0<t\le1\) put \(g_t(s)=e^{ts^2}\). Write \(s=x+iy\). For \(|x|\le A\),
\[
|g_t(s)|=e^{t(x^2-y^2)}\le e^{A^2},\qquad
g_t(s)-1=\int_0^t s^2e^{us^2}\,du.
\tag{GAP1.1}
\]
Consequently
\[
|g_t(s)-1|\le t e^{A^2}(A^2+y^2)
\le t e^{A^2}(A^2+1)(1+|y|)^2,
\]
\[
\boxed{b_{A,N}((g_t-1)F)
\le t e^{A^2}(A^2+1)b_{A,N+2}(F).}
\tag{GAP1.2}
\]
These estimates prove continuity of multiplication and convergence \(m_{g_t}\to1\) uniformly on every bounded subset of \(\mathcal B\), in every defining seminorm. They also prove that the set
\[
\{t^{-1}(g_t-1)F:0<t\le1,\ F\in K\}
\tag{GAP1.3}
\]
is bounded whenever \(K\subset\mathcal B\) is bounded.

Every ideal defined by full vanishing jets is invariant under these multipliers, and every value kernel in (GAP0.3) is invariant as well. For an invariant closed subspace \(L\subset\mathcal B\), let
\(\bar b_{A,N}([F])=\inf_{H\in L}b_{A,N}(F+H)\).
For each representative \(F+H\), the left side of (GAP1.2), with its quotient seminorm, bounds the same quotient element. Taking the infimum over \(H\) proves
\[
\bar b_{A,N}((m_{g_t}-1)[F])
\le t e^{A^2}(A^2+1)\bar b_{A,N+2}([F]).
\tag{GAP1.4}
\]
These seminorms generate the quotient topology: the original family is directed, so an image of a finite intersection of seminorm balls contains an image of one such ball. Applying this to \(L=\mathcal I\), to the inverse images of \(N_O,N_0\), and restricting to invariant closed subspaces proves the same bounded convergence on \(Q,\mathcal R,N_O,N_0\) and their specified subquotients. For a subspace followed by a quotient, use the restricted seminorms and then the same infimum argument. No continuous linear section is required.

## GAP2. The generator, every multiplicity, and the cyclic comparison

The exact semigroup identity is \(m_{g_t}m_{g_u}=m_{g_{t+u}}\). The second integral remainder gives
\[
g_t-1-ts^2=\int_0^t(t-u)s^4e^{us^2}\,du,
\]
\[
b_{A,N}((g_t-1-ts^2)F)
\le\frac{t^2}{2}e^{A^2}(A^2+1)^2b_{A,N+4}(F).
\tag{GAP2.1}
\]
Thus \(t^{-1}(m_{g_t}-1)\to m_{s^2}\) uniformly on bounded subsets of every space just listed, with its stated topology. Multiplication by \(s^2\) is itself continuous there by the same strip estimate.

At a zero of multiplicity \(m\), the entire local multiplier and all its Taylor coefficients are
\[
g_t(\rho+z)=e^{t\rho^2}e^{2t\rho z}e^{tz^2},\qquad
[z^k]g_t(\rho+z)=e^{t\rho^2}
\sum_{v=0}^{\lfloor k/2\rfloor}
\frac{(2t\rho)^{k-2v}t^v}{(k-2v)!v!}.
\tag{GAP2.2}
\]
The length-\(m\) jet matrix has these entries at position \((i,j)\) with \(k=i-j\ge0\), and zero for \(i<j\). Its determinant is \(e^{mt\rho^2}\). These are the full matrices of ECR2; only the passage to the actual length \(m\) truncates them. The convergence proved above is on the complete source, not an inference from separate convergence on finitely many jet matrices.

Retain the exact maps
\[
j:Q\hookrightarrow\mathscr C,\quad [F]\mapsto F e_0,
\qquad b_t:\mathscr C\hookrightarrow Q,\quad h e_0\mapsto[g_th].
\]
Their well-definedness and injectivity follow from full vanishing orders and the fact that \(g_t\) is a unit in each local holomorphic ring. Their exact composites are
\[
b_tj=m_{g_t}\text{ on }Q,\qquad jb_t=m_{g_t}\text{ on }\mathscr C.
\tag{GAP2.3}
\]
Equation (GAP1.4) now proves \(b_tj\to1_Q\) uniformly on bounded subsets of the actual source. There is no topology or convergence claim for \(jb_t\) on \(\mathscr C\), and no statement that either embedding is onto. The properness proofs in ECR1 remain valid.

## GAP3. The original half-Mellin source, with every factor

Retain
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty
\text{ for all }N,j\ge0\},
\]
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\quad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}F(1/2+iy)u^{-iy}\,dy.
\tag{GAP3.1}
\]
The complete source theorem proves these are continuous inverse maps \(A\leftrightarrow\mathcal B\). In ECR3 the inverse of \(g_t\) is
\[
a_{t,1}(u)=\frac{e^{t/4}}{\sqrt{\pi t}}u^{-1/2}
\exp\!\left(-\frac{(\log u-t)^2}{4t}\right).
\tag{GAP3.2}
\]
Define the following actual operator on \(A\):
\[
\boxed{
S_ta(u)=\frac{e^{t/4}}{2\sqrt{\pi t}}
\int_0^\infty (u/v)^{-1/2}
\exp\!\left(-\frac{(\log(u/v)-t)^2}{4t}\right)
a(v)\frac{dv}{v}.}
\tag{GAP3.3}
\]
Here the coefficient \(1/2\) is necessary. For multiplicative convolution
\((a*_Mb)(u)=\int a(u/v)b(v)dv/v\), absolute Fubini and \(u=wv\) give
\[
\Theta(a*_Mb)=2\Theta a\,\Theta b.
\tag{GAP3.4}
\]
Absolute Fubini is valid on every vertical line: \(a,b\in A\) have finite absolute moments of every real order, so the absolute double integral is the product of two such moments. The convolution is in \(A\). To verify this directly, move each logarithmic derivative onto the first factor and use
\((wv)^N+(wv)^{-N}\le(w^N+w^{-N})(v^N+v^{-N})\);
the remaining weighted integral of the second factor is finite, by its estimates with exponent \(N+1\) at both ends. Differentiation under the integral follows from the same bounds. Thus (GAP3.3), which is \(\tfrac12a_{t,1}*_Ma\), satisfies exactly
\[
\Theta S_t=m_{g_t}\Theta.
\tag{GAP3.5}
\]
It follows from (GAP1.2), (GAP2.1) and the continuous inverse that \(S_t\to1_A\) uniformly on bounded sets, \(S_tS_u=S_{t+u}\), and
\[
t^{-1}(S_t-1)\longrightarrow (u\partial_u)^2
\tag{GAP3.6}
\]
in that same operator topology. For the last identity, integration by parts gives \(\Theta(u\partial_u)a=-s\Theta a\), with both endpoint terms zero by the defining source estimates; applying it twice gives \(s^2\). All factors in the original formula (GAP3.3) remain. This is an approximation of test sources. It does not deform \(\zeta\), and it makes no claim about a different real-axis heat integral with an endpoint term.

The source subspace \(J\), defined in AST1 by Schwartz summation, has \(\Theta J=\mathcal I\). Thus \(S_t\) preserves \(J\) and \(A_O=q^{-1}N_O\), and induces the proved operators on \(Q=A/J\) and \(A/A_O=\mathcal R\).

## GAP4. The actual specialization map and its Hilbert receiver

Use precisely AST1's \(H=\ell^2(\mathscr Z,m)\), \(\rho^\#=1-\overline\rho\), and
\[
d_r(\rho)=e^{-i\Im\rho\log r}(r^{\Re\rho}-r^{1-\Re\rho}),
\quad(\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#),\quad r>1.
\tag{GAP4.1}
\]
Let \(G_t^\#\) be the diagonal operator with entry \(g_t(\rho^\#)\). Then
\[
\beta_rm_{g_t}=G_t^\#\beta_r,\qquad
b_rS_t=G_t^\# b_r,\qquad b_r=\beta_rq.
\tag{GAP4.2}
\]
The entry is reflected; it is not replaced by \(g_t(\rho)\) or its absolute value. Since \(0<\Re\rho^\#<1\), \(\|G_t^\#\|\le e^t\). For a fixed \(y\in H\), each coordinate of \((G_t^\#-1)y\) tends to zero and is bounded in modulus by \((e+1)|y_\rho|\). Summability with the original weights \(m_\rho\) proves strong convergence to identity on \(H\). It is uniform on compact subsets: a finite epsilon-net and the uniform operator bound reduce the assertion to the finitely many net points.

On the full \(H\) this is not convergence in operator norm. For each \(t>0\), the unbounded actual zero heights imply \(g_t(\rho^\#)\to0\) along a sequence, so \(\|G_t^\#-1\|\ge1\). This statement uses the full zero set and makes no assertion that off-line zeros exist or have unbounded heights.

For the common smooth domain
\[
H_\infty=\{y:p_N(y)^2=\sum_\rho m_\rho(1+|\Im\rho|)^{2N}|y_\rho|^2<\infty
\text{ for all }N\ge0\},
\tag{GAP4.3}
\]
the stronger estimate is
\[
p_N((G_t^\#-1)y)\le te\,p_{N+2}(y).
\tag{GAP4.4}
\]
Indeed \(|\rho^\#|^2\le1+|\Im\rho|^2\le(1+|\Im\rho|)^2\), and (GAP1.1) with \(A=1\) applies coordinatewise. The space \(H_\infty\) is complete: a sequence Cauchy in all \(p_N\) has compatible limits in the nested complete weighted Hilbert spaces, giving one coordinate vector in their intersection. Every weighted evaluation \(E_N:Q\to H\), \((E_NF)_\rho=(1+|\Im\rho|)^NF(\rho)\), is continuous by ECI5.2. Thus \(E\) and \(\beta_r\) have continuous range in \(H_\infty\). This supplies the domain needed in (GAP4.4) before it is used.

Consequently (GAP4.2) induces bounded-set convergence on the actual \(\mathcal R\) and its continuously injected specialization image with its transported source topology. It preserves the literal short exact sequence of complexes
\[
0\to[\underline{A_O}\xrightarrow0 iH]
\to[\underline A\xrightarrow{b_r}iH]
\to\underline{\mathcal R}[1]\to0.
\tag{GAP4.5}
\]
The two bracketed complexes occupy degrees \((-1,0)\). The maps are \(S_t\) on the displayed source spaces and \(G_t^\#\) on \(H\). All differentials commute by (GAP4.2). AST5's positive quotient and positive final cone projection still give connecting stalk map \(-\bar\beta_r\); its differentiate-a-lift SES convention gives \(+\bar\beta_r\). Neither sign changes in this approximation. This note does not identify the whole derived connecting morphism with just its stalk map.

## GAP5. Strong-dual convergence, with the actual bounded sets

Let \(X\) be any source, invariant subspace or quotient in GAP1 or GAP3, and let \(T_t\) denote its constructed Gaussian operator. Give \(X'\) the strong topology \(\beta(X',X)\), with seminorms \(p_K(\lambda)=\sup_{x\in K}|\lambda(x)|\) for bounded \(K\subset X\). For such \(K\), GAP1 proves that
\(D_K=\{t^{-1}(T_t-1)x:0<t\le1,x\in K\}\)
is bounded in \(X\). Hence
\[
p_K((T_t'-1)\lambda)\le t p_{D_K}(\lambda).
\tag{GAP5.1}
\]
If \(\Lambda\) is bounded in \(X'_\beta\), the right side is bounded by
\(t\sup_{\lambda\in\Lambda}p_{D_K}(\lambda)<\infty\).
This proves convergence uniformly on bounded subsets of the strong dual, not only weak convergence on individual tests. The same argument with the second remainder proves convergence of the dual difference quotient to the transpose of the full generator.

For example the exact transposed relation is
\[
m_{g_t}'\beta_r'=\beta_r'(G_t^\#)',
\qquad S_t'b_r'=b_r'(G_t^\#)'.
\tag{GAP5.2}
\]
No Hermitian conjugation is hidden in this continuous linear transpose. Under AST1's Riesz identification
\(R(\overline y)(h)=\sum m_\rho h_\rho\overline{y_\rho}\),
\((G_t^\#)'R(\overline y)=R(\overline{(G_t^\#)^*y})\),
where \(((G_t^\#)^*y)_\rho=\overline{g_t(\rho^\#)}y_\rho\).
These equations give the literal dual maps and their original multiplicity factors.

## GAP6. Every polynomial-growth class has a strong residue limit

Use ECI5's actual continuous functional
\[
\mathcal W_M(h)(F)=\sum_\rho m_\rho F(\rho)\overline{h(\rho^\#)},
\qquad h\in M,
\tag{GAP6.1}
\]
on \(Q\). It depends only on \(h\bmod\mathfrak a\); its additional kernel is the value-zero ideal modulo \(\mathfrak a\), not an assumed uniform nilradical. The complete full-jet residue receiver for this functional is the one constructed in ECI5–ECI6.

Fix \(h\), and choose \(C_h,d\) with \(|h(\rho^\#)|\le C_h w_\rho^d\), \(w_\rho=1+|\Im\rho|\). The established zero-count estimate gives \(C_0^2=\sum m_\rho w_\rho^{-4}<\infty\). For \(k\ge d+4\), (GAP1.1) and weighted Cauchy–Schwarz yield
\[
\begin{aligned}
|\mathcal W_M(g_th)(F)-\mathcal W_M(h)(F)|
&\le teC_h\sum_\rho m_\rho|F(\rho)|w_\rho^{d+2}\\
&\le teC_h C_0\|E_kF\|_H.
\end{aligned}
\tag{GAP6.2}
\]
The sum is absolutely convergent. The estimate is independent of a representative of \(F\) because it uses the continuous quotient map \(E_k\). Taking the supremum over an arbitrary bounded \(K\subset Q\) proves
\[
\boxed{\mathcal W_M(g_th)\longrightarrow\mathcal W_M(h)
\quad\text{in }Q'_\beta.}
\tag{GAP6.3}
\]
It also gives a uniform rate for any specified set of multipliers sharing the displayed \(C_h,d\). It assigns no topology to \(\mathscr C\).

In contrast, the source classes \(b_t(e_0)=[g_t]\) do not converge in \(Q\) as \(t\downarrow0\). If their limit were \([F]\), continuity of each value functional would give \(F(\rho)=1\) at every actual nontrivial zero. The strip estimate \(b_{1,1}(F)<\infty\) contradicts those values along the unbounded zero heights. Every class has a representative \(F\in\mathcal B\), so this proves nonconvergence. This does not contradict (GAP2.3): there the input lies in \(j(Q)\), whereas \(e_0\notin j(Q)\). It also does not contradict (GAP6.3), which is convergence in the explicitly different strong-dual receiver. No assertion about this sequence in the possibly zero off-line quotient \(\mathcal R\) is made.

## GAP7. Reflection, the normal coordinate and all four endpoints

Retain \(\mathsf K_1F(s)=\overline{F(1-\overline s)}\). Direct substitution gives
\[
g_t^{\#_1}(s)=e^{t(1-s)^2}=d_t(s)g_t(s),\qquad
d_t(s)=e^{t(1-2s)},\qquad d_t^{\#_1}=d_t^{-1}.
\tag{GAP7.1}
\]
Thus \(\mathsf K_1m_{g_t}=m_{d_t}m_{g_t}\mathsf K_1\) exactly at every positive \(t\). The full normal translation and transported reflection factors are
\[
(Vg_t)(\lambda)=e^{t(\lambda-1)^2},\qquad
(Vd_t)(\lambda)=e^{t(3-2\lambda)},\qquad
\mathsf K_3V=V\mathsf K_1.
\tag{GAP7.2}
\]
For a fixed strip,
\[
|d_t(s)-1|\le t e^{1+2A}(1+2A+2|y|)
\le t e^{1+2A}(3+2A)(1+|y|).
\tag{GAP7.3}
\]
This follows by integrating \((1-2s)e^{u(1-2s)}\) from zero to \(t\); its real exponential is bounded by \(e^{1+2A}\). The identical bound applies to \(d_t^{-1}-1\) using \(-(1-2s)\). Both factors therefore tend to identity uniformly on bounded sets of the spaces and strong duals already constructed. Their finite-\(t\) factors remain in the reflection identities; in particular ECI12's dual covariance uses \(m_{d_t^{-1}}'\), not \(m_{d_t}'\).

For the full simultaneous source of GMS9, the exact Gaussian action is
\[
\begin{aligned}
g_t(f,c_0,c_1)&=s_+(S_t\Sigma f)+(0,c_0,e^tc_1),\\
g_t(g,d_0,d_1)&=s_-(S_tR\Sigma g)+(0,e^td_0,d_1).
\end{aligned}
\tag{GAP7.4}
\]
Here \(s_\pm\), \(\Sigma\) and the source reflection \(R\) are the proved maps of that full source decomposition. Thus the four endpoint multipliers are exactly \((1,e^t,e^t,1)\). Continuity of the sections and restrictions, (GAP3.5), and convergence of these four scalars prove bounded-set convergence on that full source. In the separate degree-two normal term the same ring element acts by
\[
g_t(s+1)=e^{t(s+1)^2}.
\tag{GAP7.5}
\]
Apply GAP1 on the enlarged strip \(|\Re(s+1)|\le A+1\) to prove its convergence. This is not the transported original Gaussian \(Vg_t\) in (GAP7.2). Keeping those operations distinct retains GMS9's actual arithmetic degree factor.

## GAP8. The original zeta comparison is unchanged

The source factor remains
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\frac18,\quad
F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
\quad(k\ge1).
\tag{GAP8.1}
\]
At \(\rho\), the exact local unit multiplying \((s-\rho)^{m_\rho}\) is
\[
\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)
\frac{\zeta(s)}{(s-\rho)^{m_\rho}}.
\tag{GAP8.2}
\]
Every derivative of the regularized source is the full product derivative
\[
(g_tF_0)^{(j)}(s)=\sum_{v+k_0+k_1+k_2+k_3=j}
\frac{j!}{v!k_0!k_1!k_2!k_3!}g_t^{(v)}(s)
\left(\frac{s(s-1)}8\right)^{(k_0)}
\left(-\frac{\log\pi}2\right)^{k_1}\pi^{-s/2}
2^{-k_2}\Gamma^{(k_2)}(s/2)\zeta^{(k_3)}(s).
\tag{GAP8.3}
\]
At exceptional points evaluate the holomorphic full product, rather than the separately singular factors. Thus its endpoint values are \(1/8,e^t/8\), and its values at \(-2k\) are \(e^{4tk^2}\) times (GAP8.1). These are exact finite-point values, not a convergence assertion for an unrestricted infinite sum of trivial-zero contributions.

The original unit, prime repetitions, functional-equation factor and reflected Gaussian weight remain
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\quad
-\zeta'(s)/\zeta(s)=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
\quad(\Re s>1),
\]
\[
\chi(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)
=\pi^{s-1/2}\frac{\Gamma((1-s)/2)}{\Gamma(s/2)},
\quad\zeta(s)=\chi(s)\zeta(1-s),
\]
\[
g_t(\rho)\overline{g_t(\rho^\#)}
=e^{t\{\rho^2+(1-\rho)^2\}}.
\tag{GAP8.4}
\]
The last expression is not substituted by the different positive value \(|g_t(\rho)|^2\). ECR4's original explicit formula, including its prime window, Gamma integral, endpoints and stated finite trivial-divisor cutoff, remains the arithmetic receiver. No new interchange with an infinite trivial-zero sum is used in GAP6.

## GAP9. The separator on the retained specialization source

Let \(c\in M\) be the complete GMS separator, so \(c-1\in\mathfrak a\), and \(c\) vanishes to all normal shifted-zero orders. Since multiplication commutes before every quotient,
\[
cm_{g_t}=m_{g_t}c,\quad c|_Q=1_Q,\quad c|_{\mathcal R}=1_{\mathcal R},
\quad\beta_rcm_{g_t}=\beta_rm_{g_t}.
\tag{GAP9.1}
\]
Taking the proved limit gives the same identity on the entire specialization source, not just on finitely many jets. On the actual target coordinates, \(c(\rho^\#)=1\), so it is identity there too. The different transported normal operator \(c(s+1)=1-E(s)\) instead belongs to \(\mathfrak a\), and its induced map on \(Q\) and \(\mathcal R\) is zero. Both statements preserve their exact domains and shifts.

This answers the attempted approximation question: the complete original source and its strong duals admit the stated Gaussian approximation; every polynomial-growth class has its canonical strong trace limit, even though its generator has no limit in the rapid source. The earlier separator retains the specialization image in this construction. The additional calculation needed to apply the full multiplier algebra to that same boundary is its common target domain and the actual normal-ideal-to-\(\mathcal R\) map; ADM constructs these directly. No vanishing or purity is inferred from a proper embedding, a change of topology, or the existence of the approximation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Gaussian spectral synthesis on the complete original source

Complete derivation, stable locators **GSP0–GSP9**. This is programme mathematics. The independent verification is recorded separately; this file does not imply its own acceptance.

## GSP0. Construction stage, question, and prior inputs

The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). All coefficient spaces and arithmetic actions below occur after the complete-history reconstruction. Each branch retains its own recovered counter. None of the following arithmetic, spectral coordinates, seminorms, or operations is an operation on that support. Addition at the support remains retracted.

The current construction guide, connected argument and correction table were recalled, including the full WU050–WU051, WU061–WU062 and WU064–WU065 passages. The new attempt combines results already obtained: RZ's actual global resolvent and finite full-jet projectors, S3's original-source Hadamard estimate, and GAP's Gaussian approximation on the full Fréchet quotient. The question is whether the finite spectral projectors recover that quotient in its original topology, rather than only its value receiver. SDT7 explicitly established strong density of jet **functionals** without claiming this primal density. PSC3 retained the algebraic reconstruction quotient without assuming its Hausdorff quotient was zero. These are the points addressed here.

Publication source credit: The factorization theorem is due to Jacques Hadamard. The inspected author-source witness is Alain Connes, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), original rhready.tex lines526-535; its exact source hash and historical attribution are retained in the [preceding synthesis, source identity and S3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md). The full genus-one product is retained. Hadamard's 1892 original was not newly read.

The proof uses RZ1–RZ7 and its original representative corrections in ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md; GLOBAL_MELLIN_SYNTHESIS.md S2–S3 for the complete original divisor and the proved lower bound away from small zero disks; GAP1–GAP2 for bounded-set Gaussian approximation; ADM1–ADM3 for the actual specialization source; and PSC2–PSC3 for the reconstruction sequence. The underlying human-source identities and reading scopes remain those of these input proofs. This derivation is not a new claim to have read an entire human paper.

## GSP1. Original objects and all factors

Retain the original source
\[
S=\{f\in\mathcal S(\mathbb R;\mathbb C):f(-v)=f(v),\ f(0)=0,
\ \int_{\mathbb R}f(v)\,dv=0\},
\quad \Sigma f(u)=2\sum_{n\ge1}f(nu),
\]
\[
A=\{a\in C^\infty(\mathbb R_{>0}):
\sup_{u>0}(u^N+u^{-N})|(u\partial_u)^ja(u)|<\infty\ \forall N,j\ge0\},
\quad J=\Sigma S,\quad Q=A/J.
\tag{GSP1.1}
\]
The exact-image theorem proves that \(J\) is closed. The actual half-Mellin comparison is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}{\pi}
\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{GSP1.2}
\]
It identifies \(A\) with the complete Fréchet space
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{a,N}(F)=\sup_{|\Re s|\le a}(1+|\Im s|)^N|F(s)|<\infty
\ \forall a,N\ge0\}.
\tag{GSP1.3}
\]
The image of \(J\) is exactly the closed ideal \(\mathcal I\) of full vanishing jets at the actual nontrivial zeros \(\rho\) of original \(\zeta\), with orders \(m_\rho\). Write \(\mathcal Q=\mathcal B/\mathcal I\), and
\[
q_{a,N}([F])=\inf_{H\in\mathcal I}b_{a,N}(F+H).
\tag{GSP1.4}
\]
These are the original quotient seminorms. No product topology on unrestricted jets is substituted for them.

The entire source element and its original arithmetic formula remain
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)
=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{GSP1.5}
\]
Its zeros are precisely those actual nontrivial zeros, with their full orders. The exceptional values are
\[
F_0(0)=F_0(1)=\frac18,\qquad F_0(-1)=F_0(2)=\frac\pi{24},
\]
\[
F_0(-2k)=\frac{k(2k+1)(-1)^k\pi^k}{2\,k!}\zeta'(-2k)
=F_0(1+2k)\ne0\quad(k\ge1).
\tag{GSP1.6}
\]
At any \(\rho\), all local coefficients are calculated from
\[
F_0(\rho+z)=z^{m_\rho}
\frac{(\rho+z)(\rho+z-1)}8\pi^{-(\rho+z)/2}
\Gamma((\rho+z)/2)\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{GSP1.7}
\]
Every derivative of this product is its complete Leibniz sum. The original unit and repetitions are retained as
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'(s)}{\zeta(s)}=\sum_p\sum_{k\ge1}(\log p)p^{-ks}
\quad(\Re s>1).
\tag{GSP1.8}
\]
The older RZ Mellin presentation uses \(\mathcal Mk(s)=\int k(u)u^{s-1/2}du/u\). Its exact comparison is \(k(u)=u^{1/2}a(u)/2\), so \(\mathcal Mk=\Theta a\). Thus its generator \(1/2-u\partial_u\) on \(k\) corresponds to \(-u\partial_u\) on \(a\), and both correspond to multiplication by the original \(s\). This factor is not discarded when importing the RZ formulas.

## GSP2. A uniform resolvent estimate on the actual contour

Let \(L[F]=[sF]\). For \(\lambda\) outside the actual divisor, RZ3 constructs
\[
\mathscr R_\lambda F(s)
=\frac{F(s)-F_0(s)F(\lambda)/F_0(\lambda)}{\lambda-s},\qquad
R_\lambda[F]=[\mathscr R_\lambda F]=(\lambda-L)^{-1}[F].
\tag{GSP2.1}
\]
The numerator vanishes at \(s=\lambda\); its removable value is
\(-F'(\lambda)+F_0'(\lambda)F(\lambda)/F_0(\lambda)\).
The correction containing the full \(F_0\) is essential. The two identities before quotienting are
\[
(\lambda-s)\mathscr R_\lambda F=F-F_0F(\lambda)/F_0(\lambda),
\quad \mathscr R_\lambda((\lambda-s)F)=F.
\tag{GSP2.2}
\]
RZ2 proves entire division in each original seminorm. More explicitly, for \(|\Re\lambda|\le2\), put \(a'=\max(a,4)\). Its estimate gives a constant \(C_{a,N}\), independent of \(\lambda\) and \(F\), with
\[
b_{a,N}(\mathscr R_\lambda F)
\le C_{a,N}(2+|\Im\lambda|)^N
\bigl(1+|F_0(\lambda)|^{-1}\bigr)b_{a',N}(F).
\tag{GSP2.3}
\]
Indeed the numerator is bounded by
\(b_{a,N}(F)+|F_0(\lambda)|^{-1}b_{a,N}(F_0)b_{a',0}(F)\).
Outside \(|s-\lambda|<1\), division only decreases its absolute value. On the unit disk, the maximum principle for its entire divided function bounds it by half the numerator supremum on the radius-two circle, contained in \(|\Re s|\le4\); the output weight is at most \((2+|\Im\lambda|)^N\). This proves (GSP2.3) with the same input strip. Taking the infimum over representatives proves the corresponding bound for \(q_{a,N}(R_\lambda[F])\).

For completeness specify precisely the growth estimate being imported. S2–S3 proves the genus-one factorization of the complete (GSP1.5), the count \(\sum_{|\rho|\le R}m_\rho\le C(R+2)^{3/2}\), and the following bound. Let \(D_R\) be the union of radius \(R^{-2}\) disks around the zeros with \(|\rho|\le8R\). For sufficiently large \(R\),
\[
|F_0(\lambda)|^{-1}\le
\exp(CR^{3/2}\log R)
\quad(R/2\le|\lambda|\le3R,\ \lambda\notin D_R).
\tag{GSP2.4}
\]
It follows by retaining every factor in the Hadamard product: the finitely many factors have \(|1-\lambda/\rho|\ge1/(8R^3)\), their exponentials contribute at worst \(-CR^{3/2}\) to the logarithm, and the full remaining genus-one tail contributes at worst \(-CR^{3/2}\) because \(\sum_{|\rho|>8R}m_\rho|\rho|^{-2}\le CR^{-1/2}\). The affine exponential in the factorization is retained in the constant. No lower bound on distances between zeros enters this estimate.

The vertical lines \(\Re\lambda=-2,2\) have distance at least one from the divisor. Applying (GSP2.4) with \(R=|\Im\lambda|\) at large height and using the nonzero minimum on the remaining compact segments gives
\[
1+|F_0(\pm2+iy)|^{-1}\le C_0\exp(C_0\omega(y)),
\quad \omega(y)=(|y|+2)^{3/2}\log(|y|+2).
\tag{GSP2.5}
\]
The constants here depend on the original \(F_0\), not on \(F\) or an assumed RH.

## GSP3. The infinite contour gives the exact Gaussian multiplier

Put \(g_t(\lambda)=e^{t\lambda^2}\), \(t>0\). On either vertical line,
\[
|g_t(\pm2+iy)|=e^{4t-ty^2}.
\tag{GSP3.1}
\]
Equations (GSP2.3)–(GSP2.5) therefore make the following two improper integrals converge in every quotient seminorm, uniformly on bounded input sets:
\[
\mathcal C_t=
\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
-\int_{-2-i\infty}^{-2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
\right).
\tag{GSP3.2}
\]
The second sign is the positive orientation of the left side. Existence can be checked on the representatives (GSP2.1) in the complete space \(\mathcal B\) with the same estimates, then passed to the quotient. RZ4's parameter holomorphy justifies each finite contour integral.

To identify the result, retain every derivative at a given zero \(\rho\). On its order-\(m_\rho\) jet, \(R_\lambda\) acts by the Taylor jet of \(1/(\lambda-s)\). Thus the jet of (GSP3.2) is the jet of
\[
F(s)\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}\frac{g_t(\lambda)}{\lambda-s}d\lambda
-\int_{-2-i\infty}^{-2+i\infty}\frac{g_t(\lambda)}{\lambda-s}d\lambda
\right)
=g_t(s)F(s),\quad -2<\Re s<2.
\tag{GSP3.3}
\]
The scalar equality is Cauchy's formula on finite rectangles followed by the limit: the two horizontal scalar integrals tend to zero because their lengths are four and their numerators are bounded by \(e^{4t-tT^2}\). The same argument on a small disk around \(\rho\) permits every required derivative. Continuous jet functionals commute with the seminorm-convergent vector integral. Equality of all full jets is equality in the original \(\mathcal Q\), so
\[
\boxed{\mathcal C_t=m_{g_t}\quad\text{on the whole original }\mathcal Q.}
\tag{GSP3.4}
\]
This is an equality on the complete source, not only its value image. The representatives of the two sides may differ by a member of the retained original ideal \(\mathcal I=\Theta J\); no equality before that quotient has been asserted.

## GSP4. One sequence of finite full-jet operators converges on the full source

Choose, for every sufficiently large positive integer \(j\), \(R_j=j^6\). The projection of \(D_{R_j}\) onto imaginary heights has total length at most
\[
2R_j^{-2}\sum_{|\rho|\le8R_j}m_\rho\le C R_j^{-1/2}<1.
\tag{GSP4.1}
\]
The actual zero set is invariant under complex conjugation. Consequently the union of excluded height intervals is symmetric. Choose \(T_j\in[R_j,R_j+1]\) outside that union; then both horizontal segments \(\Im\lambda=\pm T_j\), \(-2\le\Re\lambda\le2\), avoid the disks. For the finitely many smaller \(j\), choose any positive zero-free contour heights. Those choices do not affect convergence. Let \(\Gamma_j\) be the positively oriented rectangle with these sides, and set
\[
K_j=\frac1{2\pi i}\int_{\Gamma_j}e^{\lambda^2/j}R_\lambda\,d\lambda.
\tag{GSP4.2}
\]
For each enclosed zero let \(P_\rho\) be the RZ full-jet projector and \(N_\rho=(L-\rho)|_{P_\rho\mathcal Q}\), with \(N_\rho^{m_\rho}=0\). The entire finite residue formula is
\[
K_j=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_{1/j}^{(a)}(\rho)}{a!}(L-\rho)^aP_\rho.
\tag{GSP4.3}
\]
It follows directly from the retained resolvent Laurent expansion
\(R_\lambda=\sum_{a=0}^{m_\rho-1}(L-\rho)^aP_\rho/(\lambda-\rho)^{a+1}+\text{holomorphic}\).
In particular all nilpotent coefficients and all original multiplicities remain. Since \(g_{1/j}(\rho)\ne0\), the restriction to each enclosed block is invertible and \(\operatorname{rank}K_j=\sum_{|\Im\rho|<T_j}m_\rho\).

Here is the full convergence estimate. On a horizontal side, (GSP2.3)–(GSP2.4) bound the output seminorm by a constant times
\[
(2+T_j)^N\exp\{-T_j^2/j+4/j+C R_j^{3/2}\log R_j\}
q_{a',N}(F).
\tag{GSP4.4}
\]
The side length is four. The exponent's negative term is at most \(-j^{11}\), whereas its positive growing term is \(6Cj^9\log j\); therefore the expression tends to zero for every fixed \(a,N\).

For the two omitted vertical tails use (GSP2.5). For all sufficiently large \(j\) and all \(y\ge T_j\),
\(C_0\omega(y)\le y^2/(2j)\), because \(\omega(y)/y^2\) decreases to zero beyond a fixed height and at \(j^6\) its product with \(j\) is \(O(j^{-2}\log j)\). Their integral is consequently bounded by a constant times
\[
q_{a',N}(F)e^{4/j}\int_{T_j}^\infty(2+y)^N e^{-y^2/(2j)}dy\longrightarrow0.
\tag{GSP4.5}
\]
For an explicit justification of the last limit, split the exponential into two equal factors, bound one by \(e^{-T_j^2/(4j)}\), and integrate the other over \([0,\infty)\). After \(y=\sqrt j\,v\), that integral is at most \(C_N j^{(N+1)/2}\) for \(j\ge1\). The exponential dominates this polynomial. These estimates use one fixed input seminorm for each fixed output seminorm and are uniform on bounded input sets.

By (GSP3.4), the difference just estimated is \(K_j-m_{g_{1/j}}\). GAP1 gives independently
\[
q_{a,N}((m_{g_{1/j}}-1)F)
\le j^{-1}e^{a^2/j}(a^2+1)q_{a,N+2}(F).
\tag{GSP4.6}
\]
Combining these estimates proves
\[
\boxed{K_j\longrightarrow1_{\mathcal Q}
\text{ uniformly on every bounded subset of the original }\mathcal Q.}
\tag{GSP4.7}
\]
No bounded zero-height scan, spectral gap, separation of neighboring zeros, or simple-zero hypothesis replaces this global limit. The finite contours define the approximating operators; their limit is proved over the complete actual divisor.

One may also write every \(K_j\) as an actual entire multiplier. RZ5 supplies \(e_\rho\in\mathcal B\) whose full jet is one at \(\rho\) and zero at every other zero. It is constructed from \(F_0(s)/(s-\rho)^{m_\rho}\) times its reciprocal Taylor polynomial at \(\rho\), retaining all coefficients (GSP1.7). Then
\[
k_j(s)=\sum_{|\Im\rho|<T_j}e_\rho(s)
\sum_{a=0}^{m_\rho-1}\frac{g_{1/j}^{(a)}(\rho)}{a!}(s-\rho)^a
\in\mathcal B\subset M,\qquad K_j=m_{k_j}\text{ on }\mathcal Q.
\tag{GSP4.8}
\]
The equality follows on every full jet. Multiplication \(m_{k_j}\) on the representative space \(\mathcal B\) is not asserted finite rank. The representative **contour** operator does have the finite-rank lift proved in RZ7:
\[
\mathscr K_jF=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_{1/j}^{(a)}(\rho)}{a!}\mathscr C_{\rho,a}F,
\quad
\mathscr C_{\rho,a}F(s)=A_\rho(s)(s-\rho)^a
\operatorname{Tay}_{\rho,<m_\rho-a}(F/A_\rho)(s),
\quad A_\rho(s)=\frac{F_0(s)}{(s-\rho)^{m_\rho}}.
\tag{GSP4.9}
\]
The Taylor division is at \(\rho\), where \(A_\rho(\rho)\ne0\). The outputs are entire original source functions. This lift annihilates \(\mathcal I\) and descends continuously from \(\mathcal Q\) to \(\mathcal B\); its quotient is \(K_j\). Its difference from \(m_{k_j}\) has image in \(\mathcal I\). The convergence proved in (GSP4.7) is in \(\mathcal Q\); no convergence \(\mathscr K_jF\to F\) in \(\mathcal B\) is asserted.

## GSP5. Closed multiplier submodules have exact full-jet synthesis

Write \(\mathcal Q_\rho=P_\rho\mathcal Q\simeq\mathbb C[z]/(z^{m_\rho})\), with \(z=L-\rho\). Equation (GSP4.7) first proves
\[
\overline{\bigoplus_{\rho\in\mathscr Z}\mathcal Q_\rho}^{\ \mathcal Q}=\mathcal Q.
\tag{GSP5.1}
\]
The direct sum means finite sums, followed by closure in the original quotient topology.

Now let \(X\) be any closed submodule for the full strip-polynomial multiplier ring \(M\). Each \(P_\rho=m_{e_\rho}\) preserves \(X\). Thus \(X_\rho=P_\rho X=X\cap\mathcal Q_\rho\) is a finite-dimensional \(\mathbb C[z]\)-submodule. There is a unique \(k_\rho\in\{0,\ldots,m_\rho\}\) with
\[
X_\rho=z^{k_\rho}\mathbb C[z]/(z^{m_\rho}).
\tag{GSP5.2}
\]
To prove this rather than assume a classification, take the least nonzero order \(k_\rho\) of any element when the submodule is nonzero. Such an element is \(z^{k_\rho}u(z)\) with \(u(0)\ne0\). Its inverse modulo \(z^{m_\rho}\) is a polynomial (the finite geometric series after its nonzero constant is factored). Polynomial multiplication therefore puts \(z^{k_\rho}\) and all higher powers in the submodule; minimality excludes lower orders. The zero submodule is the case \(k_\rho=m_\rho\).

Every \(K_j\) preserves \(X\) and has image in the finite sum of its \(X_\rho\). Conversely any class whose \(\rho\)-jet lies in \(X_\rho\) has \(K_jF\in X\) for all \(j\), and (GSP4.7) with closedness gives \(F\in X\). Hence the exact classification and its constructive limit are
\[
\boxed{X=\{[F]:F^{(a)}(\rho)=0\ (0\le a<k_\rho,\ \rho\in\mathscr Z)\}
=\overline{\bigoplus_\rho X_\rho}^{\ \mathcal Q}.}
\tag{GSP5.3}
\]
The numerical indices describe the already reconstructed coefficient jets. They are not parity labels placed on \(\tau\).

In particular this proves primal finite-jet density in \(N_O\), \(N_L\) and the all-value radical \(N_0\), as well as in the full source. Their orders are respectively: one at off-line zeros and zero at line zeros; one at line zeros and zero off the line; and one everywhere. Orders above zero remain capped by the full \(m_\rho\). It also applies to the full-jet sector kernels of PSC2. The subspaces have not been replaced by a Hilbert closure.

## GSP6. Exact consequence for the full source reconstruction defect

Use the actual sets \(\mathscr Z_L\) and \(\mathscr Z_O\), without asserting that the latter is empty. Set
\[
J_L=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho\ (\rho\in\mathscr Z_L)\},
\quad
J_O=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho\ (\rho\in\mathscr Z_O)\}.
\tag{GSP6.1}
\]
The actual intersection is \(\mathcal I\). PSC3's full reconstruction sequence remains
\[
0\longrightarrow\mathcal Q\xrightarrow{\Delta}
\mathcal B/J_L\oplus\mathcal B/J_O
\xrightarrow{([f],[g])\mapsto[f-g]}C_{\rm rec}\longrightarrow0,
\quad C_{\rm rec}=\mathcal B/(J_L+J_O).
\tag{GSP6.2}
\]
Every finite full-jet class lies in \((J_L+J_O)/\mathcal I\): an isolator at a line zero belongs to \(J_O\), and an isolator off the line belongs to \(J_L\). Equation (GSP5.1) therefore implies
\[
\boxed{\overline{J_L+J_O}=\mathcal B.}
\tag{GSP6.3}
\]
Here the closure is in \(\mathcal B\). Indeed the image of \(J_L+J_O\) is dense in the quotient; its preimage is dense because the quotient map is open and the subspace contains \(\mathcal I\). This proves the claimed source-topology statement.

It follows that the Hausdorff quotient of \(C_{\rm rec}\) is zero, and its continuous dual is zero. It does **not** follow that the algebraic vector space \(C_{\rm rec}\) is zero. The distinction is retained explicitly by (GSP6.2). The topology of a quotient by a dense proper vector subspace is non-Hausdorff; this is a property of that quotient, not a license to remove its vectors.

Moreover \(\Delta(\mathcal Q)\) is dense in the entire product in (GSP6.2). For explicit approximants to \(([f]_{J_L},[g]_{J_O})\), choose \(l_j\in J_L,o_j\in J_O\) with \(l_j+o_j\to f-g\), possible by (GSP6.3), and put \(F_j=f-l_j\). Then its first observation equals \([f]_{J_L}\) exactly, and its second tends to \([g]_{J_O}\), since \(F_j-g-o_j\to0\). The displayed product is consequently the Hausdorff completion of \(\mathcal Q\) for the topology induced by these two observations. It need not be the original quotient topology. Every compatibility class is still present in the algebraic sequence.

PSC3 proved that the inverse of \(\Delta\) on its image is continuous exactly when \(J_L+J_O\) is closed. Together with (GSP6.3), the precise remaining distinction is now whether the dense sum is the whole space; no positive completion or separation of weights has been inferred from its density.

## GSP7. The actual specialization and its continuous dual

Retain ADM's actual quotient and maps
\[
\mathcal R=\mathcal Q/N_O,\qquad
\beta_r=D_r^*\mathsf J E:\mathcal Q\to H_\infty,
\quad (\beta_rF)_\rho=\overline{d_r(\rho)}F(\rho^\#),
\]
\[
\rho^\#=1-\overline\rho,\quad
d_r(\rho)=e^{-i\Im\rho\log r}
(r^{\Re\rho}-r^{1-\Re\rho}),\quad r>1.
\tag{GSP7.1}
\]
This is the previously constructed original-source specialization. The finite contour operators preserve \(N_O\), because they are full multipliers. They induce finite-rank operators \(\overline K_j\) on \(\mathcal R\), and
\[
\overline K_j\longrightarrow1_{\mathcal R}
\text{ uniformly on bounded sets},\qquad
(\beta_rK_jF)_\rho=
\mathbf1_{\{|\Im\rho|<T_j\}}e^{(\rho^\#)^2/j}(\beta_rF)_\rho.
\tag{GSP7.2}
\]
For the first assertion, the single-input-seminorm estimates (GSP4.4)–(GSP4.6) pass through the quotient by taking infima over \(N_O\). They give the same convergence for its quotient seminorms. Alternatively AST's actual bounded lifts give bounded-set convergence directly. The second assertion is the reflected multiplier action proved in ADM3; the cutoff is reflection-invariant because \(\Im\rho^\#=\Im\rho\). Thus no source jet, reflected argument, or defect coefficient is lost before its specified quotient.

The finite-rank transposes also approximate the identity on the **full strong dual** of \(\mathcal Q\), and on that of \(\mathcal R\), uniformly on bounded subsets. Here is a direct topological proof. A strongly bounded dual set \(C\) is pointwise bounded, because singletons are bounded. A pointwise bounded family on a Fréchet space is equicontinuous: the closed sets \(\{x:\sup_{\ell\in C}|\ell(x)|\le n\}\) cover the space; Baire gives one with interior, and taking differences and scaling gives a common continuous-seminorm bound \(|\ell(x)|\le C_1p(x)\). For a bounded primal set \(D\), therefore,
\[
\sup_{\ell\in C}\sup_{x\in D}
|((K_j'-1)\ell)(x)|
\le C_1\sup_{x\in D}p((K_j-1)x)\longrightarrow0.
\tag{GSP7.3}
\]
The same proof uses \(\overline K_j\) for \(\mathcal R\). This constructs a specific common primal/dual approximation compatible with the actual source triangle, in addition to SDT7's earlier independent density argument.

All genuine integer cover coefficient actions commute with \(K_j\), because their source actions are multiplication by \(n^s\), and their traces retain \(n^{1-s}\). On a full order-\(m_\rho\) block these still act by
\[
T_n=n^\rho\sum_{a=0}^{m_\rho-1}\frac{(\log n)^a}{a!}N_\rho^a,
\qquad U_n=n^{1-\rho}\sum_{a=0}^{m_\rho-1}\frac{(-\log n)^a}{a!}N_\rho^a.
\tag{GSP7.4}
\]
The normal top-degree factor and both poles in ADM8/ACD7 remain as stated there. These commuting source maps are not an extra geometric cover or a Tate shift.

## GSP8. An actual continuous Gaussian lift and its full multiplier defect

Use the same two oriented infinite lines as in (GSP3.2), now with the original representative \(\mathscr R_\lambda\) of (GSP2.1), and call their integral \(\mathscr L_tF\in\mathcal B\). The estimates already proved give convergence in every original \(\mathcal B\) seminorm and continuity. On any \(F\in\mathcal I\), the parameter poles of \(\mathscr R_\lambda F\) disappear: the factor \(F(\lambda)/F_0(\lambda)\) is entire, and the removable diagonal is already handled by (GSP2.1). Thus every finite rectangle integral is zero. The horizontal and tail estimates for fixed \(t>0\) prove \(\mathscr L_tF=0\). Consequently this integral descends to an actual continuous map
\[
\mathcal L_t:\mathcal Q\longrightarrow\mathcal B,\qquad
q\mathcal L_t=m_{g_t},\quad q:\mathcal B\to\mathcal Q.
\tag{GSP8.1}
\]
Continuity on the quotient follows either from its definition or by taking the infimum in the input seminorm estimates. This proves an original-source lift of every Gaussian-regularized class. The underlying exact sequence is the original \(0\to\mathcal I\to\mathcal B\to\mathcal Q\to0\); a new extension has not been substituted. Its approximate sections satisfy \(q\mathcal L_t\to1\) uniformly on bounded subsets by GAP. No limit of \(\mathcal L_t\) in maps to \(\mathcal B\) has been asserted.

On the original half-Mellin source the exact lift is
\[
(\Theta^{-1}\mathcal L_tx)(u)=\frac{u^{-1/2}}\pi
\int_{\mathbb R}(\mathcal L_tx)(1/2+iy)u^{-iy}\,dy.
\tag{GSP8.2}
\]
It belongs to \(A\) by the inverse-transform estimates of (GSP1.2), and represents the actual regularized class. Its discrepancy from the original Gaussian convolution source representative is in \(J=\Sigma S\). Neither that discrepancy nor its original Schwartz preimage is discarded.

To calculate exactly what this lift does to the arithmetic action, let \(h\in M\). Define the actual continuous map
\[
\mathfrak a_t(h;x)=\mathcal L_t(hx)-h\mathcal L_tx\in\mathcal I.
\tag{GSP8.3}
\]
Its target is \(\mathcal I\), since multiplication by \(h\) commutes with \(g_t\) in (GSP8.1). Using any representative \(F\) of \(x\), the full formula is
\[
\mathfrak a_t(h;x)(s)=\frac{F_0(s)}{2\pi i}
\int_{\partial V}g_t(\lambda)\frac{F(\lambda)}{F_0(\lambda)}
\frac{h(s)-h(\lambda)}{\lambda-s}\,d\lambda.
\tag{GSP8.4}
\]
Here \(\partial V\) denotes the right line upward and the left line downward, exactly as in (GSP3.2). The divided difference has its removable value at \(\lambda=s\). The equality follows by subtracting the two representative resolvents; all terms involving \(F(s)\) cancel and the displayed full \(F_0(s)\) remains. Convergence in \(\mathcal B\) follows from the two convergent vector integrals in (GSP8.3), or directly from the polynomial strip growth of \(h\) and the same division estimate. Independence of the representative follows from \(\mathscr L_t\mathcal I=0\) and \(h\mathcal I\subset\mathcal I\).

This defect obeys the exact cocycle identity
\[
\mathfrak a_t(hk;x)=\mathfrak a_t(h;kx)+h\mathfrak a_t(k;x),
\tag{GSP8.5}
\]
as is seen by adding and subtracting \(h\mathcal L_t(kx)\). Thus continuity of the lift does not silently imply its multiplier equivariance.

For the original generator \(h(s)=s\), (GSP8.4) becomes the particularly explicit rank-one representative defect
\[
\mathfrak a_t(s;x)=-F_0\lambda_t(x),\qquad
\lambda_t([F])=\frac1{2\pi i}\int_{\partial V}
e^{t\lambda^2}\frac{F(\lambda)}{F_0(\lambda)}d\lambda.
\tag{GSP8.6}
\]
The scalar integral is absolutely convergent by (GSP2.5). It annihilates \(\mathcal I\), using the same finite-contour and tail argument, so it is a continuous functional on the original quotient. Its complete grouped residue formula is
\[
\lambda_t([F])=\lim_{j\to\infty}
\sum_{|\Im\rho|<T_j}
\operatorname{Res}_{\lambda=\rho}
\frac{e^{t\lambda^2}F(\lambda)}{F_0(\lambda)}.
\tag{GSP8.7}
\]
The convergence is uniform on bounded source sets, from the fixed-\(t\) estimates. The residue at each multiple zero uses every Taylor coefficient of the full original product (GSP1.7). For every positive integer \(k\), the complete polynomial version is
\[
\mathfrak a_t(s^k;x)
=-F_0(s)\sum_{a=0}^{k-1}s^{k-1-a}\lambda_t(L^a x).
\tag{GSP8.8}
\]
It follows from \((s^k-\lambda^k)/(\lambda-s)=-\sum_{a=0}^{k-1}s^{k-1-a}\lambda^a\), with no omitted lower terms. Formula (GSP8.4) also applies to the genuine recovered-degree multipliers \(h(s)=n^s\) and the full trace multipliers \(h(s)=n^{1-s}\).

Finally retain how this relates to the actual specialization: composing (GSP8.1) with ADM's strict quotient \(\mathcal Q\to\mathcal R\) and with \(\beta_r\) gives exactly the reflected Gaussian action of (GSP7.2), without its finite cutoff. This is a concrete regularized lift into the original analytic source, together with its calculated equivariance defect. It supplies neither an extra Tate factor nor a weight-separation assertion for the original connecting map.

## GSP9. What the attempt establishes for the lifting calculation

The previously unproved primal density is now obtained in the original topology, with a single explicit family of finite-rank full-jet operators and its continuous transpose. It classifies closed multiplier submodules by their complete local jet orders. It also determines the previously retained reconstruction defect's Hausdorff quotient: zero, with the original algebraic quotient still present. The same contour constructs an actual continuous Gaussian lift through the original source extension, and (GSP8.4) calculates its full multiplier-equivariance defect. These are derived properties of the full original source, not assumed finite-block descriptions.

The next distinction in the geometric calculation is now precise. A continuous actual lifting arrow is determined by its restrictions to all full-jet blocks, by (GSP4.7). An arrow vanishing on every such block vanishes globally, including the strong-dual comparison with (GSP7.3). For the actual \(\beta_r\), however, (GSP7.2) retains its exact coefficient \(d_r(\rho)\); the approximation does not turn this coefficient into zero. The normal separator of ADM remains identity on that original specialization source and has the distinct translated action \(c(s+1)\) on the normal coefficient. Those source and target actions have not changed under spectral synthesis.

The Deligne comparison must therefore use an actual geometric operation on these complete blocks and their convergent reconstruction. The parallel tensor calculation is testing the genuine product/transfer operation while retaining the original specialization. Neither density nor the vanishing of a Hausdorff reconstruction quotient proves the vanishing of this original connecting map. The full original-zeta arithmetic and Weil contribution stay those of PSC5, with both endpoints and every trivial-zero term in its stated domain.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Independent proof of Gaussian synthesis in the original source quotient

25 September 2026. Independent derivation and verification, **GSI0–GSI12**.

## GSI0. Exact scope and reading record

This note verifies the proposed passage from the complete original source to finite full-multiplicity spectral blocks. It does not assume primal spectral synthesis, RH, simplicity, a lower bound on spacing between zeros, or a topology defined by a product of jets. The support remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\); all coordinates, coefficients and seminorms below belong to the already recovered arithmetic source, not to that support. No arithmetic or metric on \(\tau\) is introduced.

The programme inputs actually read for this derivation are:

- [ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/ORIGINAL_ZETA_RESOLVENT_AND_PROJECTORS.md), RZ1–RZ7, SHA256 `f3553e1362b4c2c1c1556098b55ee153be9fc716a9d4c35baedcf39bd28ad755`;
- peer [GLOBAL_MELLIN_SYNTHESIS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/gct-weight-control/proofs/GLOBAL_MELLIN_SYNTHESIS.md), S2–S3, SHA256 `71376fe8074ca8a20623e4e829be5bce74455a447bbdb677156f28e561553e9f`;
- [GAUSSIAN_FULL_SOURCE_APPROXIMATION.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/identity/GAUSSIAN_FULL_SOURCE_APPROXIMATION.md), GAP0–GAP2, SHA256 `1cb89804a1ad3990c5eab65c89b2c6c748764461a012194867d2250318a04a0e`;
- [POSITIVE_QUOTIENT_SOURCE_AND_ARITHMETIC.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/geometric-positive-quotient/POSITIVE_QUOTIENT_SOURCE_AND_ARITHMETIC.md), PSC0–PSC3, SHA256 `2d188377c6b694e363e5b32a331a8af2ef4562d2cb8aab272d0ce1149b6f1171`.

These are local programme proofs. Their underlying human-source identity and previous reading coverage remain those recorded in them; no new complete reading of a human paper is claimed here. In particular the genus-one product used below is the full product of GMS S2.6, whose retained author-source locator is Connes, arXiv:2602.04022v1, [rhready.tex](https://arxiv.org/abs/2602.04022v1), lines 526–535.

Let
\[
\mathcal B=\{F\in\mathcal O(\mathbb C):
b_{A,N}(F)=\sup_{|\Re s|\le A}(1+|\Im s|)^N|F(s)|<\infty
\text{ for every integer }A,N\ge0\}.
\tag{GSI0.1}
\]
The full source multiplier is
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{GSI0.2}
\]
Its entire continuation belongs to \(\mathcal B\). The divisor of this entire multiplier is exactly the original nontrivial-zero divisor \((\mathscr Z,m_\rho)\). The canceled endpoint and trivial-zero contributions have the retained values
\[
F_0(0)=F_0(1)=\frac18,
\]
\[
F_0(-2r)=\frac{r(2r+1)(-1)^r\pi^r}{2r!}\zeta'(-2r)
=\frac{(1+2r)(2r)}8\pi^{-(1+2r)/2}
\Gamma((1+2r)/2)\zeta(1+2r)\ne0.
\tag{GSI0.3}
\]
The ideal and quotient are exactly
\[
\mathcal I=\{F\in\mathcal B:F^{(a)}(\rho)=0
\ (\rho\in\mathscr Z,\ 0\le a<m_\rho)\},\qquad
Q=\mathcal B/\mathcal I,
\tag{GSI0.4}
\]
with their original Fréchet topologies. Write
\[
q_{A,N}([F])=\inf_{H\in\mathcal I}b_{A,N}(F+H).
\tag{GSI0.5}
\]
The quotient is complete and Hausdorff by RZ2. Each full jet is continuous on it and the full family separates it. The operator \(L[F]=[sF]\) is continuous on all of \(Q\). RZ3 gives its actual continuous inverse
\[
R_\lambda[F]=[\mathscr R_\lambda F],\qquad
\mathscr R_\lambda F(s)=
\frac{F(s)-F_0(s)F(\lambda)/F_0(\lambda)}{\lambda-s}
\quad(\lambda\notin\mathscr Z).
\tag{GSI0.6}
\]
This proof retains the entire correction term; evaluation at \(\lambda\) alone generally does not descend to \(Q\).

## GSI1. A resolvent estimate with one input seminorm at every height

Fix output indices \(A,N\), and take the integer
\(A_*=\max(A,4)\). For \(|\Re\lambda|\le2\), set \(y=\Im\lambda\) and \(v(\lambda)=|F_0(\lambda)|^{-1}\). RZ2's radius-two removable-division estimate gives, with \(G=F-F_0F(\lambda)/F_0(\lambda)\),
\[
b_{A,N}(\mathscr R_\lambda F)
\le b_{A,N}(G)+\frac12(2+|y|)^N b_{A_*,0}(G).
\tag{GSI1.1}
\]
Here the radius-two disk about \(\lambda\) lies in \(|\Re s|\le4\), so \(A_*\) is independent of height. Evaluation and the two numerator estimates give
\[
b_{A,N}(G)\le b_{A,N}(F)
+v(\lambda)b_{A,N}(F_0)b_{A_*,0}(F),
\]
\[
b_{A_*,0}(G)\le
(1+v(\lambda)b_{A_*,0}(F_0))b_{A_*,0}(F).
\tag{GSI1.2}
\]
Consequently there is a finite constant \(C_{A,N}\), independent of \(\lambda\), such that
\[
b_{A,N}(\mathscr R_\lambda F)
\le C_{A,N}(2+|y|)^N(1+v(\lambda))b_{A_*,N}(F).
\tag{GSI1.3}
\]
Since \(\mathscr R_\lambda\mathcal I\subset\mathcal I\), applying this to every representative and taking the infimum proves
\[
q_{A,N}(R_\lambda x)
\le C_{A,N}(2+|y|)^N(1+v(\lambda))q_{A_*,N}(x).
\tag{GSI1.4}
\]
The same representative may be used simultaneously over any specified set of parameters. Thus (GSI1.4) also controls suprema over such sets. There is no need to lift a bounded subset of \(Q\) to a bounded subset of \(\mathcal B\).

## GSI2. Reciprocal growth on both vertical lines and good horizontal levels

GMS S2–S3 prove, with multiplicities,
\[
n(R)\le C(R+2)^{3/2},\qquad
|F_0(\lambda)|\ge\exp(-C R^{3/2}\log R)
\tag{GSI2.1}
\]
whenever \(R/2\le|\lambda|\le3R\) and \(\lambda\) is outside the disks of radius \(R^{-2}\) about zeros of modulus at most \(8R\). The constants do not depend on the direction of \(\lambda\). The estimate follows from the retained full product
\[
F_0(\lambda)=e^{a+b\lambda}
\prod_{\rho}\left(1-\frac\lambda\rho\right)e^{\lambda/\rho},
\qquad e^a=\frac18,\quad b=\frac{F_0'(0)}{F_0(0)}.
\tag{GSI2.2}
\]
No genus-one exponential or repeated zero is omitted in (GSI2.1).

Every actual nontrivial zero has \(0<\Re\rho<1\). Therefore the vertical lines \(\Re\lambda=-2\) and \(\Re\lambda=2\) stay at distance at least one from their divisor. Taking \(R=|y|\) at sufficiently large \(|y|\), and increasing a constant to cover the remaining compact portions, proves
\[
1+|F_0(\pm2+iy)|^{-1}
\le C_0\exp\bigl(C_1(|y|+2)^{3/2}\log(|y|+2)\bigr)
\quad(y\in\mathbb R).
\tag{GSI2.3}
\]

For the later simultaneous limit put \(R_j=j^6\). For each sufficiently large integer \(j\), delete from \([R_j,R_j+1]\) all intervals
\[
\{T:|T-\Im\rho|<R_j^{-2}\},\qquad
\{T:|T+\Im\rho|<R_j^{-2}\}
\quad(|\rho|\le8R_j).
\tag{GSI2.4}
\]
Their total length is at most
\[
4R_j^{-2}n(8R_j)\le C_2R_j^{-1/2}=C_2j^{-3}<1.
\tag{GSI2.5}
\]
There is consequently a \(T_j\in[R_j,R_j+1]\) outside their union. Both horizontal segments \(x\pm iT_j\), \(-2\le x\le2\), are outside every disk appearing in (GSI2.1), because their imaginary-coordinate separation alone is at least the disk radius. Their moduli lie between \(R_j/2\) and \(3R_j\) for large \(j\). Therefore, uniformly on both segments,
\[
1+|F_0(x\pm iT_j)|^{-1}
\le C_3\exp(C_4R_j^{3/2}\log R_j).
\tag{GSI2.6}
\]
This selection handles both signs explicitly; conjugation symmetry is not needed for its existence. Multiple or arbitrarily close zeros cause no problem because their total count already includes multiplicity.

## GSI3. The infinite vertical contour defines a continuous operator

For fixed \(t>0\) let \(g_t(\lambda)=e^{t\lambda^2}\), and define
\[
S_t=\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
-\int_{-2-i\infty}^{-2+i\infty}g_t(\lambda)R_\lambda\,d\lambda
\right).
\tag{GSI3.1}
\]
Both integrals point upwards in this notation; the minus sign is the downward orientation of the left edge of a positive rectangle. This \(S_t\) is a quotient operator, not a new heat deformation of \(\zeta\).

On either line,
\[
|g_t(\pm2+iy)|=e^{4t-ty^2}.
\tag{GSI3.2}
\]
Equations (GSI1.4) and (GSI2.3) bound the integrand in every output seminorm by \(q_{A_*,N}(x)\) times
\[
C_{A,N}e^{4t}(2+|y|)^N
\exp\bigl(-ty^2+C_1(|y|+2)^{3/2}\log(|y|+2)\bigr).
\tag{GSI3.3}
\]
This is integrable on \(\mathbb R\), since its positive exponent is strictly subquadratic. On compact parameter segments RZ4's continuous holomorphic family has a Riemann integral in the complete Fréchet space \(Q\). The bound just proved makes its tails Cauchy in every seminorm, so each improper integral exists in \(Q\) for every \(x\). Integrating the bound proves continuity of the resulting linear operator using the single input seminorm \(q_{A_*,N}\).

For a bounded set \(K\subset Q\), \(\sup_{x\in K}q_{A_*,N}(x)<\infty\). The same tail bound is therefore uniform on \(K\). This proves convergence in \(L_b(Q)\), the topology of uniform convergence on bounded source sets. No separate assumption that an abstract space of operators is complete is used.

## GSI4. Identification of the infinite contour without assuming synthesis

For \(0\le k<m_\rho\), the full jet of (GSI0.6) at \(s=\rho\) is
\[
\partial_s^k\mathscr R_\lambda F(\rho)
=\left.\partial_s^k\frac{F(s)}{\lambda-s}\right|_{s=\rho}.
\tag{GSI4.1}
\]
Indeed the entire correction has a zero of order at least \(m_\rho\) there, and \(\lambda\ne\rho\). Continuous evaluation may pass through the convergent integrals of GSI3.

For \(s\) in a small disk about \(\rho\) lying between the two vertical lines, scalar Cauchy integration gives
\[
\frac1{2\pi i}\left(
\int_{2-i\infty}^{2+i\infty}\frac{g_t(\lambda)}{\lambda-s}\,d\lambda
-\int_{-2-i\infty}^{-2+i\infty}\frac{g_t(\lambda)}{\lambda-s}\,d\lambda
\right)=g_t(s).
\tag{GSI4.2}
\]
To prove the improper identity, close a rectangle at heights \(\pm T\), enclosing the disk. Each horizontal integral is at most a constant depending on that disk times \(e^{4t-tT^2}/(T-|\Im s|)\); it tends to zero. The vertical integrals and their derivatives in \(s\) converge uniformly on the disk, using the positive distance from its closure to the two vertical lines. The finite Cauchy formula therefore passes to the limit with every fixed derivative.

Combining (GSI4.1)–(GSI4.2) proves that \(S_t[F]\) has every full jet equal to that of \(g_tF\). These jets separate \(Q\) by its original defining ideal. Hence
\[
\boxed{S_t=m_{g_t}\quad\text{on the entire original }Q.}
\tag{GSI4.3}
\]
This uses separation of classes by their jets, not density of finite primal jet blocks. Thus it does not assume the conclusion being established.

## GSI5. Exact finite contours retain every multiplicity coefficient

Let \(\Gamma_j\) be the positive rectangle with vertices \(\pm2\pm iT_j\). RZ7 proves the meromorphic operator expansion
\[
R_\lambda=\sum_{a=0}^{m_\rho-1}
\frac{(L-\rho)^aP_\rho}{(\lambda-\rho)^{a+1}}
+\text{a holomorphic operator family near }\rho.
\tag{GSI5.1}
\]
The actual \(P_\rho\) is multiplication modulo \(\mathcal I\) by the full-jet isolator \(e_\rho\in\mathcal B\), and its image \(Q_\rho\) has dimension \(m_\rho\). Compact contour integrals exist with the same topology by RZ4. The residue theorem, obtained by removing small circles about the finitely many poles and applying scalar Cauchy to each continuous linear functional, gives
\[
K_{j,t}:=\frac1{2\pi i}\int_{\Gamma_j}g_t(\lambda)R_\lambda\,d\lambda
=\sum_{|\Im\rho|<T_j}\sum_{a=0}^{m_\rho-1}
\frac{g_t^{(a)}(\rho)}{a!}(L-\rho)^aP_\rho.
\tag{GSI5.2}
\]
Continuous linear functionals separate the Hausdorff locally convex target, so their equalities give the operator equality. Each summand is finite rank, with image in the actual \(Q_\rho\). The scalar coefficient is exactly
\[
\frac{g_t^{(a)}(\rho)}{a!}
=e^{t\rho^2}\sum_{v=0}^{\lfloor a/2\rfloor}
\frac{(2t\rho)^{a-2v}t^v}{(a-2v)!v!}.
\tag{GSI5.3}
\]
There is no replacement of these derivatives by a value-only coefficient or an absolute value. The \(P_\rho\) themselves retain RZ5's complete multiplier derivatives, including derivatives of \(s(s-1)/8\), \(\pi^{-s/2}\), \(\Gamma(s/2)\), and \(\zeta\).

## GSI6. A single finite-rank sequence converges in the original topology

Set \(t_j=1/j\) and \(K_j=K_{j,1/j}\). Subtract (GSI5.2) from the infinite contour (GSI4.3). The difference consists of the four vertical tails and the two horizontal edges, with their contour signs. Estimates may bound their absolute seminorms individually.

For the horizontal edges (GSI1.4) and (GSI2.6) give
\[
q_{A,N}(\text{horizontal error applied to }x)
\le C_{A,N}(2+T_j)^N
\exp\left(4/j-T_j^2/j+C_4R_j^{3/2}\log R_j\right)
q_{A_*,N}(x).
\tag{GSI6.1}
\]
Both horizontal lengths are exactly four; the constant retains their sum and the \(1/(2\pi)\) contour factor. As \(R_j=j^6\) and \(R_j\le T_j\le R_j+1\), the negative term has size at least \(-j^{11}\), whereas the positive term has size \(6C_4j^9\log j\). Thus its scalar coefficient tends to zero for every fixed \(A,N\).

For the vertical tails the coefficient is bounded by
\[
C_{A,N}e^{4/j}\int_{T_j}^{\infty}
(2+y)^N\exp\left(-y^2/j+C_1(y+2)^{3/2}\log(y+2)\right)dy.
\tag{GSI6.2}
\]
The finite number of tails is absorbed in the explicit finite constant, independent of \(j\). For \(y\ge j^6\) and sufficiently large \(j\),
\[
C_1(y+2)^{3/2}\log(y+2)\le\frac{y^2}{4j}.
\tag{GSI6.3}
\]
For verification, \((y+2)^{3/2}/y^2\le C/\sqrt y\), and \(\log(y+2)/\sqrt y\) is eventually decreasing. Its supremum on this range is at most \(C\log j/j^3\), which is less than \(1/(4C_1j)\) for large \(j\). For every fixed \(N\), enlarging that lower threshold also gives
\[
N\log(2+y)\le\frac{y^2}{4j}\quad(y\ge j^6).
\tag{GSI6.4}
\]
Consequently the integrand in (GSI6.2) is at most \(e^{-y^2/(2j)}\). The elementary tail estimate
\[
\int_T^\infty e^{-y^2/(2j)}dy
\le\frac jT\,e^{-T^2/(2j)}
\tag{GSI6.5}
\]
follows by inserting \(y/T\ge1\) and integrating its derivative. This tends to zero at \(T=T_j\).

There are therefore numbers \(\varepsilon_{j,A,N}\to0\) such that
\[
q_{A,N}((K_j-m_{g_{1/j}})x)
\le\varepsilon_{j,A,N}q_{A_*,N}(x).
\tag{GSI6.6}
\]
GAP1, whose proof is the integral identity
\(g_t(s)-1=\int_0^t s^2e^{us^2}du\), gives on this exact quotient
\[
q_{A,N}((m_{g_{1/j}}-1)x)
\le\frac1j e^{A^2}(A^2+1)q_{A,N+2}(x).
\tag{GSI6.7}
\]
Combining the two inequalities proves
\[
\boxed{K_j\longrightarrow1_Q\text{ in }L_b(Q).}
\tag{GSI6.8}
\]
In particular
\[
\boxed{\overline{\bigoplus_{\rho\in\mathscr Z}^{\rm alg}Q_\rho}=Q.}
\tag{GSI6.9}
\]
The closure is in the original quotient Fréchet topology. The sum is algebraic before taking closure. Nothing here asserts convergence of unweighted partial sums, a continuous projector for an arbitrary subset of zeros, or identification with an unrestricted product of local jet rings.

## GSI7. Classification of closed multiplier submodules

Let \(M\) be the actual ring of entire functions of polynomial growth on every closed vertical strip, with a strip-dependent polynomial exponent as in GAP0. Let \(V\subset Q\) be a closed complex linear \(M\)-submodule. Since \(e_\rho\in\mathcal B\subset M\),
\[
P_\rho V\subset V,\qquad
V_\rho:=P_\rho V=V\cap Q_\rho.
\tag{GSI7.1}
\]
The second equality follows because \(P_\rho\) is identity on \(Q_\rho\). The local block is the regular module
\[
Q_\rho\simeq\mathbb C[z]/(z^{m_\rho}),\qquad z=s-\rho,
\tag{GSI7.2}
\]
by its full Taylor coefficients; \(L-\rho\) acts by multiplication by \(z\). Thus \(V_\rho\) is an ideal in this local ring: it is a complex linear subspace invariant under multiplication by \(z\), hence under all polynomials in \(z\), which are all elements of the ring.

For completeness each such ideal is \((z^{k_\rho})\), with a unique integer \(0\le k_\rho\le m_\rho\). If it is zero take \(k_\rho=m_\rho\). Otherwise take the minimum order of a nonzero member. Such a member is \(z^{k_\rho}u(z)\) with \(u(0)\ne0\). Its inverse modulo \(z^{m_\rho}\) is a finite polynomial, obtained recursively from the constant term, so the ideal contains \(z^{k_\rho}\). Every other member has order at least \(k_\rho\) by minimality; the two inclusions prove the assertion.

Define the closed submodule
\[
V(k)=\{[F]\in Q:F^{(a)}(\rho)=0
\text{ for every }\rho\text{ and }0\le a<k_\rho\}.
\tag{GSI7.3}
\]
The local classification proves \(V\subset V(k)\). If \(x\in V(k)\), every \(P_\rho x\) belongs to \(V_\rho\). Thus every term of (GSI5.2) belongs to \(V\), because \(V\) is preserved by polynomials in \(L\); hence \(K_jx\in V\). Equation (GSI6.8) and closedness give \(x\in V\). We have proved
\[
\boxed{V=V(k).}
\tag{GSI7.4}
\]
Conversely every selection \(k_\rho\in\{0,\ldots,m_\rho\}\) defines a closed \(M\)-submodule by (GSI7.3), because the defining jets are continuous and Leibniz preserves their vanishing. The local isolators prove different selections give different submodules. This is therefore a complete classification, not only a necessary local condition.

An immediate exact application is
\[
\overline{hQ}=V(k),\qquad
k_\rho=\min(m_\rho,\operatorname{ord}_\rho h)
\quad(h\in M),
\tag{GSI7.5}
\]
with \(k_\rho=m_\rho\) if \(h=0\). Indeed \(\overline{hQ}\) is a closed \(M\)-submodule. Its local projected image is precisely \(hQ_\rho\), since \(P_\rho h=hP_\rho\). This is finite dimensional and closed, so projection of any limit of \(hQ\) stays in it; conversely \(hQ_\rho\subset hQ\). The local ideal is exactly the stated order. No assertion that \(hQ\) itself is closed is made.

## GSI8. The exact consequence for the reconstruction defect

Use PSC3's actual ideals
\[
J_L=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho
\ (\Re\rho=1/2)\},\qquad
J_O=\{F\in\mathcal B:\operatorname{ord}_\rho F\ge m_\rho
\ (\Re\rho\ne1/2)\}.
\tag{GSI8.1}
\]
Each full block representative supported on the line lies in \(J_O\), and each supported off the line lies in \(J_L\). Therefore \((J_L+J_O)/\mathcal I\) contains every finite spectral sum. Equation (GSI6.9) proves it is dense in \(Q\).

The closure \(\overline{J_L+J_O}\) in \(\mathcal B\) contains \(\mathcal I\). Its quotient by \(\mathcal I\) is closed in \(Q\): its inverse image under the quotient map is that same closed subspace. Since it contains the dense image just proved, its quotient is all of \(Q\). Hence
\[
\boxed{\overline{J_L+J_O}=\mathcal B.}
\tag{GSI8.2}
\]
The retained algebraic defect
\(C_{\rm rec}=\mathcal B/(J_L+J_O)\)
thus has zero Hausdorff quotient, and every continuous linear map from it to a Hausdorff locally convex space is zero. To see the latter directly, compose such a map with \(\mathcal B\to C_{\rm rec}\); its closed kernel contains the dense sum and therefore equals \(\mathcal B\).

Its algebraic vanishing is a different assertion:
\[
C_{\rm rec}=0
\ \Longleftrightarrow\ J_L+J_O=\mathcal B
\ \Longleftrightarrow\ J_L+J_O\text{ is closed}.
\tag{GSI8.3}
\]
The first equivalence is the definition of that quotient, and the second uses (GSI8.2). The present proof establishes neither side of these equivalent extra assertions. It preserves the entire defect module. PSC3.3a now gives the further exact topological result
\[
\overline{\Delta(Q)}
=Q_{\mathscr Z_{\rm line}}^{\rm jet}
\oplus Q_{\mathscr Z_{\rm off}}^{\rm jet}.
\tag{GSI8.4}
\]
The algebraic image remains the compatible pairs in the original exact row, with its original compatibility module \(C_{\rm rec}\).

## GSI9. Verification conclusion and use in the programme

The proposed Gaussian finite-rank synthesis theorem is correct with the explicit estimates above. Its critical points are: a fixed input strip in (GSI1.4); selection excluding both signs of the horizontal height in (GSI2.4); construction of the improper integral in the actual complete quotient and uniformly on bounded inputs in GSI3; identification through separating full jets in GSI4, which avoids circular use of synthesis; and the simultaneous scale \(t_j=1/j\), \(T_j\in[j^6,j^6+1]\), whose tail domination is proved in GSI6.

The resulting classification concerns closed multiplier submodules of the original source quotient. It strengthens earlier work that proved strong-dual density but expressly left finite primal spectral density open. It does not turn a dense non-Hausdorff algebraic quotient into zero, does not establish a global line/off-line source projector, and does not identify this reconstruction defect with Deligne's lifting obstruction. Full \(F_0\), original \(\zeta\), all multiplicities, all derivative coefficients, and the endpoint and trivial-zero values remain in the formulas. No purity or RH conclusion is asserted.

## GSI10. Exact representative contour lift

There is a useful precision refinement concerning the prequotient. The operator \(m_{k_j}:\mathcal B\to\mathcal B\), where \(k_j\) is the finite isolator multiplier in GSP4.8, generally is not finite rank. But the actual representative contour operator
\[
\mathscr K_jF=\frac1{2\pi i}\int_{\Gamma_j}
g_{1/j}(\lambda)\mathscr R_\lambda F\,d\lambda
\tag{GSI10.1}
\]
is finite rank. Its exact formula is
\[
\mathscr K_jF(s)=\sum_{|\Im\rho|<T_j}
A_\rho(s)\operatorname{Tay}_{\rho,<m_\rho}
\left(\frac{g_{1/j}F}{A_\rho}\right)(s),
\qquad A_\rho(s)=\frac{F_0(s)}{(s-\rho)^{m_\rho}}.
\tag{GSI10.2}
\]
The division inside the Taylor polynomial is only a germ near \(\rho\), where \(A_\rho\ne0\). Each output term is a polynomial of degree less than \(m_\rho\) times the entire \(A_\rho\in\mathcal B\), and each coefficient is a fixed finite linear combination of the actual input jets. Thus the formula is continuous and finite rank on \(\mathcal B\).

To derive it, first take \(s\) outside the closed rectangle. The contribution of \(g_{1/j}(\lambda)F(s)/(\lambda-s)\) has no pole inside. At \(\rho\), expand \(g_{1/j}(\lambda)F(\lambda)/A_\rho(\lambda)\) in powers of \(\lambda-\rho\) in the remaining term of (GSI0.6). The expansion of \(1/(\lambda-s)\) is exactly RZ7.3, and the two minus signs give the positive Taylor expression (GSI10.2). Both sides are entire functions of \(s\), so equality outside the rectangle implies equality everywhere.

This lift annihilates \(\mathcal I\). Its image consists of the finite direct sum of RZ's representative blocks \(A_\rho\mathbb C[s]_{<m_\rho}\). Each enclosed local Gaussian is a unit in the truncated ring, so its rank is exactly \(\sum_{|\Im\rho|<T_j}m_\rho\). The direct sum is independent because each summand has zero full jets at the other zeros. In contrast \(m_{k_j}\) need not annihilate \(\mathcal I\). Their exact relation is
\[
\mathscr K_jF-k_jF\in\mathcal I,
\qquad [\mathscr K_jF]=[k_jF]=K_j[F].
\tag{GSI10.3}
\]
The same full-jet identity proves the first statement. This distinction does not modify any quotient estimate. Neither representative sequence is asserted to converge to identity on \(\mathcal B\); the contour sequence cannot do so because it annihilates the nonzero original ideal.

## GSI11. Full root-artifact review

The independent reviewer then read the entire [GAUSSIAN_SPECTRAL_SYNTHESIS.md](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_SPECTRAL_SYNTHESIS.md), GSP0–GSP8, SHA256 `8ae2e962d69360f57c80ff72e58a308bf3a2d7e00e7c54f5eb5ac2fa83389a40`. The core synthesis theorem and all stated consequences in that version agree with the independent derivation above. Its alternative height selection uses conjugation symmetry of the complete divisor; the excluded union is therefore symmetric and its one-sided measure estimate suffices for both signs. The same fixed input strip is retained throughout. GSP4.6's sharper factor \(e^{a^2/j}\) is valid directly from the integral proof of GAP1.

The additional statements in the root artifact were checked as follows.

The product \(\mathcal B/J_L\oplus\mathcal B/J_O\) is a complete Hausdorff Fréchet space, and \(\Delta\) is injective because \(J_L\cap J_O=\mathcal I\). Density, proved constructively in GSP6 and independently in (GSI8.4), therefore identifies this product with the completion of \(Q\) for the topology pulled back from those two observations. This does not identify that topology with the original quotient topology and does not assert algebraic surjectivity.

For the actual \(\mathcal R=Q/N_O\), the error bound is a sum of two terms with fixed continuous quotient seminorms, so taking infima over representatives modulo \(N_O\) proves bounded-set convergence there. The reflected formula for \(\beta_rK_j\) uses the value \(g_{1/j}(\rho^\#)\), and the cutoff is unchanged because \(\Im\rho^\#=\Im\rho\). The coefficient \(\overline{d_r(\rho)}\) is retained. Higher jets disappear only at that previously specified value observation.

Finally let \(C\) be a bounded subset of the strong dual of either original Fréchet quotient and let \(D\) be a bounded primal set. Strong boundedness implies pointwise boundedness. Baire applied to the closed sets
\(\{x:\sup_{\ell\in C}|\ell(x)|\le n\}\)
gives equicontinuity: an interior ball in one of these sets, followed by taking its difference with itself and scaling, yields a common continuous-seminorm estimate \(|\ell(x)|\le C_1p(x)\). Since \(K_j-1\to0\) uniformly on \(D\) for that seminorm, the inequality in GSP7.3 proves transpose convergence uniformly on bounded dual sets in the full strong topology. This is valid without any assumption that the original quotient equals a sequence product.

Publication source credit: Baire category is the classical input. See Terence Tao, [245B, Notes9, Theorem1](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/) (1 February2009), for complete metric spaces. The present proof supplies the actual Frechet seminorm argument.

The only requested refinement was to distinguish the two prequotient representatives as in GSI10: the multiplier lift need not be finite rank, whereas the contour lift is finite rank. The reviewed root wording did not explicitly deny finite rank of the latter, so this is an added exact statement rather than a counterexample to its theorem. No substantive error was found in the synthesis, classification, reconstruction closure or actual quotient/dual comparison.

## GSI12. Expanded lift and equivariance-defect audit

The expanded root artifact was then read in its changed portions, with GSP4.9 supplying the exact finite-rank representative lift and new GSP8 supplying the infinite-contour lift and full defect (the previous scope section is now GSP9). Reviewed SHA256: `fb436828944accd8aac94183e729f6c55054f94e21fcccda06c4b1180cba9598`.

The GSP4.9 sum equals (GSI10.2) by multiplication of the two finite Taylor expansions. In particular its coefficient of \((s-\rho)^k\) before multiplication by \(A_\rho\) is
\(\sum_{a+b=k}g_{1/j}^{(a)}(\rho)(F/A_\rho)^{(b)}(\rho)/(a!b!)\),
which is exactly the order-\(k\) Taylor coefficient of \(g_{1/j}F/A_\rho\). This resolves the representative distinction completely.

For fixed \(t>0\) the integrals in (GSI3.1) also converge before taking the quotient, with \(\mathscr R_\lambda\) in place of \(R_\lambda\), by (GSI1.3). If \(F\in\mathcal I\), the ratio \(F(\lambda)/F_0(\lambda)\) is entire. The parameter pole at any actual zero disappears in (GSI0.6); the diagonal singularity is already removable. Finite rectangle integrals therefore vanish. Passing to the same good-height rectangles at fixed \(t\) is justified by the horizontal bound \(\exp(-tT_j^2+C R_j^{3/2}\log R_j)\), which tends to zero, and the integrable vertical bound in GSI3. Thus the infinite integral annihilates \(\mathcal I\), proving the continuous descended map
\[
\mathcal L_t:Q\longrightarrow\mathcal B,
\qquad q\mathcal L_t=m_{g_t}.
\tag{GSI12.1}
\]
The exact original half-Mellin inverse in GSP8.2 retains its \(u^{-1/2}/\pi\) coefficient and returns a member of the original source. It is distinct from the source Gaussian-convolution operator of GAP3.

For \(h\in M\), direct subtraction before integration gives
\[
\mathscr R_\lambda(hF)(s)-h(s)\mathscr R_\lambda F(s)
=F_0(s)\frac{F(\lambda)}{F_0(\lambda)}
\frac{h(s)-h(\lambda)}{\lambda-s}.
\tag{GSI12.2}
\]
This verifies the sign and complete formula of GSP8.4. The right side has its removable diagonal value. Multiplication by \(h\) is continuous on \(\mathcal B\), and \(hF\in\mathcal B\), so subtraction of the two convergent vector integrals proves convergence of the whole right side in every original seminorm. The defect is \(\mathcal I\)-valued because its quotient is \(m_{g_t}m_h-m_hm_{g_t}=0\). Adding and subtracting \(h\mathcal L_t(kx)\) proves GSP8.5's cocycle identity with the stated arguments and order.

When \(h(s)=s\), the divided difference equals \(-1\). Hence
\[
\mathcal L_t(Lx)-s\mathcal L_tx=-F_0\lambda_t(x),
\qquad
\lambda_t([F])=\frac1{2\pi i}\int_{\partial V}
e^{t\lambda^2}\frac{F(\lambda)}{F_0(\lambda)}d\lambda.
\tag{GSI12.3}
\]
Absolute convergence and a single-input-seminorm bound follow from (GSI2.3); annihilation of \(\mathcal I\) follows from the same entire parameter argument and good-height limits. The grouped residue formula of GSP8.7 is therefore valid uniformly on bounded source sets. The polynomial formula follows from the exact divided difference
\[
\frac{s^k-\lambda^k}{\lambda-s}
=-\sum_{a=0}^{k-1}s^{k-1-a}\lambda^a,
\tag{GSI12.4}
\]
so all lower-degree terms in GSP8.8 are necessary and correct.

The nonzero value of this representative generator defect can be checked on every actual eigenline without any approximation. In RZ notation put \(m=m_\rho\), \(a_0=A_\rho(\rho)\ne0\), and
\(x=[E_{\rho,m-1}]=[A_\rho B_\rho(s-\rho)^{m-1}]\).
Then \(E_{\rho,m-1}/F_0=B_\rho(s)/(s-\rho)\), and \(B_\rho(\rho)=1/a_0\). The scalar contour has only this pole, so
\[
\lambda_t(x)=\frac{g_t(\rho)}{a_0}\ne0,
\qquad
\mathcal L_tx(s)=\frac{g_t(\rho)F_0(s)}{a_0(s-\rho)}.
\tag{GSI12.5}
\]
The second formula also follows by taking the fixed-\(t\) limit of (GSI10.2); all other input jets vanish. It independently verifies (GSI12.3) because \(Lx=\rho x\). This is a defect of this actual analytic lift, with its stated target \(\mathcal I\); it is not an identification with Deligne's geometric lifting obstruction. No error was found in the new lift and complete defect calculation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Tensor powers of the actual specialization source and the full positive tensor receiver

Complete independent derivation, **TWC0–TWC11**, 25 September 2026.

## TWC0. Construction stage, source use and what is being tensored

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). Every tensor product below is a tensor product of the already reconstructed coefficient spaces over \(\mathbb C\). No operation, coordinate, metric, midpoint, addition, count of copies, or extra grading is placed on that support. The complete-history reconstruction precedes the recovered scalars and cover degrees; the two branch counters and return measures remain separate. A tensor product of coefficient maps is not a pooled branch return measure and does not replace the original zeta function by a power.

Before this calculation the connected USER_ARGUMENT_RECONSTRUCTION.md and its correction-precedence table, CURRENT_CC_WEIGHT_WORK.md, READ_FIRST_USER_CONSTRUCTION.md, and CORPUS_USE_AND_PREREQUISITES.md were read. The relevant programme reading is ADM0–9, CPS0–8, DP0–9, ACD6–8 and the displayed DCA6–9 cover and endpoint comparisons. CFP's definitions and its receiving statement are used through the complete accepted CPS theorem; no new whole-file CFP reading is claimed. These are local programme proofs with their recorded human-source provenance, not fresh readings of whole human papers.

The question is the actual specialization map, not an arbitrarily chosen extension. Its original quotient topology and all retained kernels remain. The full derived connecting morphism has additional extension data; tensoring its stalk map does not erase that distinction. TWC8 explicitly computes the tensor differential of the actual local complex. TWC9 retains the genuine product-cover degree. TWC10 tests the resulting whole-domain receiver, and then constructs its exact positive quotient rather than stopping at a failed separation.

## TWC1. Original coefficient, arithmetic factors and actual map

Use the complete Fréchet space and its closed full-jet ideal
\[
\mathcal B=\{F\in\mathcal O(\mathbb C): b_{a,N}(F)=\sup_{|\Re s|\le a}(1+|\Im s|)^N|F(s)|<\infty\text{ for all }a,N\},
\qquad \mathcal Q=\mathcal B/\mathcal I.
\tag{TWC1.1}
\]
Here \(\mathcal I\) imposes every jet of order less than \(m_\rho\) at each distinct actual nontrivial zero \(\rho\) of original \(\zeta\). The original source comparison is
\[
\Theta a(s)=\frac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi\int_{\mathbb R}F(1/2+it)u^{-it}\,dt,
\quad Q=A/\Sigma S\simeq\mathcal Q.
\tag{TWC1.2}
\]
The source factor is retained in full:
\[
f_0(v)=\frac\pi2v^2(2\pi v^2-3)e^{-\pi v^2},\qquad
F_0(s)=\Theta\Sigma f_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{TWC1.3}
\]
Its values are \(F_0(0)=F_0(1)=1/8\), \(F_0(-1)=F_0(2)=\pi/24\), and
\[
F_0(-2j)=\frac{j(2j+1)(-1)^j\pi^j}{2\,j!}\zeta'(-2j)\ne0\quad(j\ge1).
\tag{TWC1.4}
\]
At each nontrivial zero its entire germ is
\[
F_0(\rho+z)=z^{m_\rho}\frac{(\rho+z)(\rho+z-1)}8
\pi^{-(\rho+z)/2}\Gamma((\rho+z)/2)
\frac{\zeta(\rho+z)}{z^{m_\rho}}.
\tag{TWC1.5}
\]
For products every derivative remains the full Leibniz sum
\[
\left(\prod_{j=1}^k F_j\right)^{(a)}
=\sum_{a_1+\cdots+a_k=a}\frac{a!}{a_1!\cdots a_k!}
\prod_{j=1}^kF_j^{(a_j)}.
\tag{TWC1.6}
\]
The original arithmetic remains
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'}\zeta(s)=\sum_p\sum_{j\ge1}(\log p)p^{-js}\quad(\Re s>1).
\tag{TWC1.7}
\]
No tensor construction below changes these formulas, suppresses a prime-power repetition, or substitutes a new zeta function.

Write \(\rho^\#=1-\overline\rho\), \(w_\rho=1+|\Im\rho|\), and let \(\mathscr Z_O\) be the actual off-line subset. It is invariant under \(\#\), with \(m_{\rho^\#}=m_\rho\). The actual quotient is
\[
\mathcal R=Q/N_O\simeq\mathcal B/\mathcal B_O,
\quad \mathcal B_O=\{F:F(\rho)=0\ (\rho\in\mathscr Z_O)\},
\quad N_O=\mathcal B_O/\mathcal I.
\tag{TWC1.8}
\]
It retains the original Fréchet quotient topology. In particular the whole line-zero blocks and all positive-order off-line jets remain in \(N_O\); they have not disappeared from \(Q\).
For the fixed recovered coefficient parameter \(r>1\), put
\[
d_r(\rho)=e^{-i\Im\rho\log r}(r^{\Re\rho}-r^{1-\Re\rho}),
\qquad \delta_\rho=\overline{d_r(\rho)}.
\tag{TWC1.9}
\]
The actual map and its entire common multiplier receiver are
\[
b=\overline\beta_r:\mathcal R\longrightarrow H_{\infty,O},\qquad
(b[F])_\rho=\delta_\rho F(\rho^\#),
\]
\[
H_{\infty,O}=\{y:p_N(y)^2=\sum_{\rho\in\mathscr Z_O}m_\rho w_\rho^{2N}|y_\rho|^2<\infty\ \forall N\}.
\tag{TWC1.10}
\]
ADM proves this map continuous and injective, with all finite-coordinate vectors in its image and dense image. It also proves every multiplier \(h\in M\) acts on it by \(h(\rho^\#)\). The local cone boundary is \(-b\), whereas the differentiate-a-lift boundary is \(+b\). We retain both conventions.

## TWC2. The complete rapid tensor receiver, with every multiplicity

Fix a recovered positive integer \(k\). For \(\boldsymbol\rho=(\rho_1,\ldots,\rho_k)\) set
\[
m_{\boldsymbol\rho}=\prod_{j=1}^km_{\rho_j},\qquad
W_{\boldsymbol\rho}=\prod_{j=1}^kw_{\rho_j},\qquad
\sigma(\boldsymbol\rho)=\sum_{j=1}^k\rho_j^\#.
\tag{TWC2.1}
\]
Define the complete Fréchet receiver
\[
\mathscr H_k=\left\{z:
P_N(z)^2=\sum_{\boldsymbol\rho\in\mathscr Z_O^k}
m_{\boldsymbol\rho}W_{\boldsymbol\rho}^{2N}|z_{\boldsymbol\rho}|^2<\infty
\quad\forall N\ge0\right\}.
\tag{TWC2.2}
\]
Completeness follows by taking limits in each weighted Hilbert space; the coordinate limits coincide. Finite-coordinate truncations converge in every \(P_N\). The map sending a simple tensor to its coordinate product satisfies
\[
P_N(y_1\otimes\cdots\otimes y_k)=\prod_{j=1}^kp_N(y_j).
\tag{TWC2.3}
\]
It extends continuously from the completed projective tensor product of \(H_{\infty,O}\).

Here that map is an isomorphism, not only a dense inclusion. Keep the original coordinate vector \(e_\rho\) of value one; its norm is \(p_N(e_\rho)=\sqrt{m_\rho}w_\rho^N\). The unconditional actual zero-count estimate gives
\(C_*^2=\sum_{\rho\in\mathscr Z_O}w_\rho^{-4}<\infty\).
The coordinate expansion of \(z\in\mathscr H_k\) obeys, in the projective seminorm generated by \(p_N\) on each factor,
\[
\sum_{\boldsymbol\rho}|z_{\boldsymbol\rho}|
\sqrt{m_{\boldsymbol\rho}}W_{\boldsymbol\rho}^{N}
\le C_*^k P_{N+2}(z).
\tag{TWC2.4}
\]
This is Cauchy–Schwarz with the two factors
\(\sqrt{m_{\boldsymbol\rho}}W_{\boldsymbol\rho}^{N+2}|z_{\boldsymbol\rho}|\)
and \(W_{\boldsymbol\rho}^{-2}\). The expansion
\(\sum z_{\boldsymbol\rho}
 e_{\rho_1}\otimes\cdots\otimes e_{\rho_k}\)
therefore converges in every projective seminorm. Seminorms with different indices on the factors are bounded by the one with their maximum. Coordinate truncations show that taking coordinates of this series returns z. Conversely, truncate each factor of a simple tensor; it converges in every original seminorm, so the tensor truncations converge in every projective seminorm by expanding the difference one factor at a time. Their finite coordinate expansions are the displayed series. Thus the reverse composite is identity on simple tensors, then on their linear span, and then on the completion by continuity. Equations (TWC2.3) and (TWC2.4) therefore give the two continuous inverse maps:
\[
H_{\infty,O}^{\widehat\otimes_\pi k}\simeq\mathscr H_k.
\tag{TWC2.5}
\]
For an empty off-line set both spaces are zero and the assertion has the same meaning. No nuclearity assertion about the original quotient is used.

## TWC3. The actual tensor source and its exact receiving map

Keep the original completed source
\(\mathscr R_k=\mathcal R^{\widehat\otimes_\pi k}\),
with the projective topology formed from its original quotient seminorms. The actual map is
\[
b_k=b^{\widehat\otimes k}:\mathscr R_k\longrightarrow\mathscr H_k,
\qquad
b_k(F_1\otimes\cdots\otimes F_k)_{\boldsymbol\rho}
=\prod_{j=1}^k\delta_{\rho_j}F_j(\rho_j^\#).
\tag{TWC3.1}
\]
Its continuity follows from (TWC2.3) and the continuity of \(b\); completeness of the target extends the algebraic tensor map. Its image contains every finite coordinate array, by choosing the original isolators independently in the factors. Hence its image is dense in \(\mathscr H_k\).

For each tuple define the continuous tensor evaluation
\(\varepsilon_{\boldsymbol\rho}=\mathrm{ev}_{\rho_1^\#}\widehat\otimes\cdots\widehat\otimes\mathrm{ev}_{\rho_k^\#}\) on \(\mathscr R_k\). The exact kernel is
\[
\mathscr K_k=\ker b_k=\bigcap_{\boldsymbol\rho}\ker\varepsilon_{\boldsymbol\rho}.
\tag{TWC3.2}
\]
Every \(\delta_\rho\) here is nonzero. Formula (TWC3.1) therefore proves both inclusions. The quotient \(\mathscr R_k/\mathscr K_k\), with its original quotient topology, injects continuously with dense image into \(\mathscr H_k\). It is not identified with that completion's topology.

On the algebraic tensor product the kernel is zero. For a finite-dimensional span of vectors in a factor, coordinate functionals separate its image under the injective map \(b\). A finite subfamily consequently has injective evaluation: add one separating functional whenever the remaining common kernel is nonzero, reducing its finite dimension each time. Applying these injective finite matrices in every factor proves injectivity on the chosen finite tensor. Every algebraic tensor belongs to such a finite product of spans, proving the claim. This argument does not presume injectivity on the completed tensor source; (TWC3.2) retains that entire kernel.

For every \(F\in\mathcal R\), the exact diagonal identity is
\[
b_k(F^{\otimes k})_{(\rho,\ldots,\rho)}
=\delta_\rho^k F(\rho^\#)^k.
\tag{TWC3.3}
\]
Thus \(b_k(F^{\otimes k})=0\) implies \(F=0\), by injectivity of \(b\). In particular tensoring never makes a nonzero actual specialization map zero. Conversely \(\mathcal R=0\) makes every map zero. This conclusion is obtained on the actual source, not from an unrelated example.

## TWC4. Product of coefficients and the exact retained defect factor

Pointwise multiplication on \(\mathcal B\) is jointly continuous, since
\[
b_{a,N}(F_1\cdots F_k)\le\prod_{j=1}^k b_{a,N}(F_j).
\tag{TWC4.1}
\]
Both \(\mathcal I\) and \(\mathcal B_O\) are ideals: for the first use the full Leibniz sum (TWC1.6), and for the second evaluate each product at each actual off-line zero. The quotient maps are open linear maps, so their products are open; descending the continuous product gives a jointly continuous product on \(Q\) and \(\mathcal R\). This supplies a continuous map
\[
\mu_k:\mathscr R_k\to\mathcal R,\qquad
F_1\otimes\cdots\otimes F_k\mapsto F_1\cdots F_k.
\tag{TWC4.2}
\]
There is no assertion that either nonunital rapid-source algebra contains the constant function one.

Retain the diagonal multiplicity rather than silently change it. Set
\[
\mathscr D_k=\{v:q_{N,k}(v)^2=\sum_{\rho\in\mathscr Z_O}
m_\rho^k w_\rho^{2kN}|v_\rho|^2<\infty\ \forall N\}.
\tag{TWC4.3}
\]
The same space results by replacing \(m_\rho^kw_\rho^{2kN}\) with the family \(m_\rho w_\rho^{2N}\), with equivalent Fréchet topologies. Indeed \(m_\rho\ge1,w_\rho\ge1\) gives one direction. The full zero count supplies a finite constant \(C\) with \(m_\rho\le Cw_\rho^2\), so
\(q_{N,k}(v)^2\le C^{k-1}p_{kN+k-1}(v)^2\), giving the other. This comparison retains the actual multiplicity factors in each formula.

The diagonal restriction \(\Delta_k:\mathscr H_k\to\mathscr D_k\),
\((\Delta_kz)_\rho=z_{(\rho,\ldots,\rho)}\), has
\(q_{N,k}(\Delta_kz)\le P_N(z)\).
With \(D_{k-1}v=(\delta_\rho^{k-1}v_\rho)_\rho\), direct substitution gives the full diagram identity
\[
\boxed{\quad\Delta_k b_k=D_{k-1}\,b\,\mu_k.\quad}
\tag{TWC4.4}
\]
It holds first on simple tensors, then on the completed source by continuity. The factors \(\delta_\rho^{k-1}\) are essential. Neither \(b\) nor \(\Delta_kb_k\) has silently become a multiplicative realization.

There is an exact receiving space in which (TWC4.4) can be inverted without a division assumption on the whole rapid space:
\[
\mathscr D_{k,\delta}=\{v:(\delta_\rho^{1-k}v_\rho)_\rho\in\mathscr D_k\},\quad
q_{N,k,\delta}(v)=q_{N,k}((\delta_\rho^{1-k}v_\rho)_\rho).
\tag{TWC4.5}
\]
This is complete, and \(D_{k-1}:\mathscr D_k\to\mathscr D_{k,\delta}\) is a topological isomorphism. Its inclusion into \(\mathscr D_k\) is continuous because \(|\delta_\rho|\le r-1\). Equation (TWC4.4) proves that the actual source map \(\Delta_kb_k\) lands continuously in this stronger space, and there
\[
D_{k-1}^{-1}\Delta_kb_k=b\mu_k.
\tag{TWC4.6}
\]
No global division by a function or a claimed inverse on all \(H_{\infty,O}\) is used. This constructs the receiver required by the product's exact defect.

The original Mellin source of multiplication is also explicit. For
\((a*_\times b)(u)=\int_0^\infty a(v)b(u/v)\,dv/v\),
absolute convergence and differentiation follow from rapid decay at both ends, and Fubini gives
\(\Theta(a*_\times b)=2(\Theta a)(\Theta b)\).
Iterating,
\[
\Theta^{-1}\left[\prod_{j=1}^k\Theta a_j\right]
=2^{1-k}(a_1*_\times\cdots*_\times a_k).
\tag{TWC4.7}
\]
The factor \(2^{1-k}\), original source, and its quotient kernels all remain.

## TWC5. Full multiplier covariance, genuine integer covers and the normal shift

For multipliers \(h_1,\ldots,h_k\in M\), the tensor source action maps through \(b_k\) to
\[
(z_{\boldsymbol\rho})\longmapsto
\left(\prod_{j=1}^kh_j(\rho_j^\#)z_{\boldsymbol\rho}\right).
\tag{TWC5.1}
\]
Each factor has strip-polynomial growth and acts continuously on \(\mathscr H_k\), with an appropriate increase of \(N\). No action on an unspecified Hilbert domain is invoked.
For the recovered integer cover degree \(n\ge1\), diagonal pullback and weighted product transfer are
\[
(A_n^{(k)}z)_{\boldsymbol\rho}=n^{\sigma(\boldsymbol\rho)}z_{\boldsymbol\rho},
\qquad
(C_n^{(k)}z)_{\boldsymbol\rho}=n^{k-\sigma(\boldsymbol\rho)}z_{\boldsymbol\rho}.
\tag{TWC5.2}
\]
They receive \(T_n^{\widehat\otimes k}\) and \((nT_{1/n})^{\widehat\otimes k}\), respectively, and
\[
C_n^{(k)}A_n^{(k)}=n^k I.
\tag{TWC5.3}
\]
This is the degree of the genuine product cover, not the degree of one copy of the cover. General \(a>0\) defines the analogous coefficient operator; it is not declared a noninteger geometric cover.

If \(j\) selected factors carry the already constructed normal action \(h(s+1)\), the same pullback exponent is \(\sigma(\boldsymbol\rho)+j\). The normal coordinate map is the factorwise translation \((VF)(\lambda)=F(\lambda-1)\). It retains each full source factor
\[
F_+(\lambda)=\frac{(\lambda-1)(\lambda-2)}8\pi^{-(\lambda-1)/2}
\Gamma((\lambda-1)/2)\zeta(\lambda-1),
\tag{TWC5.4}
\]
its derivatives \(F_+^{(a)}(\lambda)=F_0^{(a)}(\lambda-1)\), the shifted endpoint values at \(1,2,0,3\), and the values (TWC1.4) at \(1-2j\). Normal shifts cannot be added to a factor that carried the original source action.

ADM's separator \(c\) acts as identity on \(\mathcal R\) and on \(H_{\infty,O}\). Acting by it in any unshifted tensor factor therefore remains identity on both sides of (TWC3.1). Its action on a shifted factor is instead \(c(s+1)=0\) on the corresponding normal quotient. This proves the exact factorwise extension of the existing separation; it does not change the original tensor boundary's action.

## TWC6. Same-eigenvalue and reflected-pair tensor restrictions

For a source value isolator at an actual off-line \(\lambda\), write \(v_\lambda\in\mathcal R\) for its class. Then
\[
T_nv_\lambda=n^\lambda v_\lambda,\qquad
b v_\lambda=\delta_{\lambda^\#}e_{\lambda^\#}.
\tag{TWC6.1}
\]
The first identity holds in \(\mathcal R\), since all off-line values of the difference vanish; it is not a claim that a full higher-jet block in \(Q\) has been removed. On a tensor of these classes, both source and receiving eigenvalues are exactly
\[
n^{\lambda_1+\cdots+\lambda_k}.
\tag{TWC6.2}
\]
The same-eigenvalue restriction has \(n^{k\lambda}\), with weight
\(2k\Re\lambda\) under the convention \(2\log|\alpha|/\log n\), for \(n>1\).

The two-factor reflected restriction is different. Define
\[
(\Delta_\#z)_\rho=z_{(\rho,\rho^\#)}.
\tag{TWC6.3}
\]
It maps continuously into \(\mathscr D_2\) with norm at most one, because the tuple weight is exactly \(m_\rho^2w_\rho^{4N}\). Its exponent is
\[
\rho^\#+\rho=1+2i\Im\rho,
\qquad|n^{\rho^\#+\rho}|=n.
\tag{TWC6.4}
\]
The phase \(n^{2i\Im\rho}\) remains. Moreover
\[
\delta_{\rho^\#}=-\delta_\rho,\qquad
(\Delta_\# b_2(F\otimes G))_\rho
=-\delta_\rho^2 F(\rho^\#)G(\rho).
\tag{TWC6.5}
\]
Thus a reflected tensor pair has an exact common modulus while retaining the original off-line defect in its coefficient. It cannot be substituted for the same-eigenvalue tensor that appears in Deligne's amplification.

These are explicit maps on the full receiver. No tensor of a source vector with its complex conjugate has been confused with the complex-linear reflection-pair restriction. Complex conjugation would change both scalar linearity and its exponent.

## TWC7. Original full jets and the operator-trace comparison

For a finite set \(S\) of actual zeros, retain the complete quotient jet block
\[
J_S=\bigoplus_{\rho\in S}\mathbb C[z_\rho]/(z_\rho^{m_\rho}),
\qquad (T_nF)_\rho=n^\rho e^{(\log n)z_\rho}F_\rho.
\tag{TWC7.1}
\]
These blocks are quotients of the original source by finite jet evaluation; the original full-jet isolators prove surjectivity. The exponential is taken modulo the displayed power, with every resulting coefficient retained. Its matrix is triangular, giving
\[
\operatorname{Tr}(T_n\mid J_S)=\sum_{\rho\in S}m_\rho n^\rho,
\qquad
\operatorname{Tr}(T_n^{\otimes k}\mid J_S^{\otimes k})
=\left(\sum_{\rho\in S}m_\rho n^\rho\right)^k.
\tag{TWC7.2}
\]
The tensor identity follows by multiplying diagonal matrix entries; each tuple has multiplicity \(\prod_jm_{\rho_j}\). Replacing \(n\) by \(n^a\) retains every repetition \(a\ge1\).

To supply the actual map into \(\mathcal R\), define \(i_S:J_S\to Q\) by the full-jet isolators: assign the prescribed jets on \(S\), and zero full jets at every other actual zero. Two such choices differ by \(\mathcal I\), so the class is unique. The finite sum of the existing isolators realizes it continuously, and finite-jet evaluation composed with \(i_S\) is identity. Multiplying by \(n^s\) preserves the zero jets outside \(S\) and gives exactly (TWC7.1) on \(S\); hence \(i_S\) is equivariant. The composite \(J_S\xrightarrow{i_S}Q\to\mathcal R\) now is an actual defined map. It kills whole line blocks and the positive-order jets of every off-line block. Its value block at an off-line zero is one dimensional. Consequently
\[
\operatorname{Tr}(T_n\mid J_{\{\rho\}})=m_\rho n^\rho,
\quad
\operatorname{Tr}(T_n\mid J_{\{\rho\}}/(z_\rho))=n^\rho,
\quad
\operatorname{Tr}(T_n\mid (z_\rho))=(m_\rho-1)n^\rho.
\tag{TWC7.3}
\]
The middle target is the actual value receiver. Weighting its one coordinate by \(m_\rho\) in an inner product does not change its operator trace: the one-dimensional operator is \(n^\rho I\), whose trace is \(n^\rho\) independently of the weight on its inner product. Thus the existing multiplicity-weighted Weil sums are retained as those sums, not reidentified as the Hilbert operator trace of the value receiver. Formula (TWC7.3) records precisely the lost trace when passing from a full jet block to a value block, with no simplicity hypothesis.

For a conjugation-stable finite \(S\), the trace in (TWC7.2) is real, so its even powers are nonnegative. This is the exact elementary positivity step in DP4. It does not make the full infinite source trace convergent or provide a global rational cohomological determinant. No infinite determinant is introduced here without its domain and convergence.

## TWC8. The literal tensor complex and its signs

The actual local coefficient complex from ADM is
\[
P=[A^{-1}\xrightarrow{b_r}H_{\infty,O}^0],
\tag{TWC8.1}
\]
where restricting the receiver to its actual off-line summand leaves the line summand as the separately retained zero-attached term. The line term may equivalently be kept throughout as an additional direct summand in degree zero. At the two-factor stalk, its completed tensor complex has terms
\[
A\widehat\otimes A\longrightarrow
(H_{\infty,O}\widehat\otimes A)\oplus(A\widehat\otimes H_{\infty,O})
\longrightarrow\mathscr H_2
\tag{TWC8.2}
\]
in degrees \((-2,-1,0)\), with
\[
d^{-2}(a\otimes a')=(b_ra\otimes a',-a\otimes b_ra'),
\quad d^{-1}(h\otimes a',a\otimes h')=h\otimes b_ra'+b_ra\otimes h'.
\tag{TWC8.3}
\]
Both contributions to \(d^{-1}d^{-2}\) cancel exactly. The map \(b_r\widehat\otimes b_r\) is therefore not a second differential: it appears in the two opposite paths, not as their sum. In \(k\) factors the differential is
\[
d(x_1\otimes\cdots\otimes x_k)=
\sum_{j=1}^k(-1)^{|x_1|+\cdots+|x_{j-1}|}
 x_1\otimes\cdots\otimes dx_j\otimes\cdots\otimes x_k.
\tag{TWC8.4}
\]
Each pair of differentials on distinct factors cancels by its Koszul sign, proving \(d^2=0\). All maps are continuous and extend to the completed tensor products. This constructs a topological cochain complex; it does not assert exactness of completed projective tensoring on arbitrary exact sequences or replace the full derived connecting class by \(b_k\).

The signed stalk tensor of the original cone boundaries is \((-1)^kb_k\); this is a statement about their ordinary underlying linear maps. The shifted derived tensor morphism also uses the shift identifications and their Koszul signs. Equations (TWC8.2–4), rather than an unrecorded shift convention, govern its local cochain calculation.

## TWC9. The geometric product keeps all sheets, poles, degrees and endpoints

Use the actual global model
\[
G=[A^{-1}\xrightarrow{(b_r,b_r)}H_\infty^0\oplus H_\infty^0
\xrightarrow0 A^1],
\tag{TWC9.1}
\]
with the four original endpoint lines as separate degree-minus-one summands. For this common-domain version, its own two-pole Čech complex has differential
\[
(a_+,a_-)\longmapsto(b_ra_+,b_ra_-,a_+-a_-)
\]
from \(A\oplus A\) to \(H_\infty\oplus H_\infty\oplus A\), and then zero to \(A\). Its projection to (TWC9.1) is
\(p^{-1}(a_+,a_-)=a_-\),
\(p^0(h_+,h_-,c)=(h_+-b_rc,h_-)\), and \(p^1=1\).
Its inclusion is \(a\mapsto(a,a)\), \((h_+,h_-)\mapsto(h_+,h_-,0)\), and identity in degree one.
The homotopy is \(h^0(h_+,h_-,c)=(c,0)\), zero elsewhere. Substitution proves \(dh+hd=1-ip\); all maps are continuous because ADM proves \(b_r:A\to H_\infty\) continuous. Thus the ACD6 comparison is established within this precise common-domain model. It is not an equivalence between this model and the original Hilbert-valued model: the comparison quotient with point coefficients \(H/H_\infty\) remains the separate retained quotient in ADM5.2. Its genuine degree-\(n\) pullback is \(T_n\) in degree \(-1\), \(U_n^*\) on each point term, and \(nT_n\) in degree \(1\). Weighted trace is \(nT_{1/n}\), \(T_n^*\), and \(T_{1/n}\), respectively. The endpoint characters are \((1,n,n,1)\) and \((n,1,1,n)\) in the unchanged coordinate order \((c_0,c_1,d_0,d_1)\).

Take the external product of the actual finite-sheet unit and trace maps in ACD7 on the product of spheres. On an open product chart, nearby sheets are indexed by the full tuple \((j_1,\ldots,j_k)\in\{0,\ldots,n-1\}^k\). Unit is the tensor of the diagonals, and trace is the sum over every tuple with the inverse coefficient operation in each factor. On a tuple of pole stalks the same product rules give the coefficient maps (TWC5.2). Thus trace after unit is \(n^kI\); in reverse order it is the full product deck norm
\[
\bigotimes_{a=1}^k\left(\sum_{j=0}^{n-1}P_{n,a}^j\right),
\tag{TWC9.2}
\]
not \(n^kI\) on augmentation sheets. This follows by distributing the finite sums, so no sheet or prime-2 case is omitted. ACD's sheaf formulas suffice; no pullback of arbitrary singular distributions is asserted. For current comparison, transpose the full continuous tensor cochain map to its actual continuous dual. Specifically, for the full completed cochain complex \(C\), use \((C^\vee)^q=(C^{-q})'_\beta\) with
\(d_\vee^q\ell=(-1)^{q+1}\ell\circ d_C^{-q-1}\).
A degree-zero cochain map transposes componentwise. If \(F-G=dH+Hd\), its dual homotopy is
\(K^q\ell=(-1)^q\ell\circ H^{1-q}\); direct substitution gives \(d_\vee K+Kd_\vee=F^\vee-G^\vee\).
The transpose maps are strongly continuous because continuous maps send bounded sets to bounded sets. This is the proved transpose domain; a tensor product of individual current duals is not identified with that full dual without an additional isomorphism. DCA's entire raw-cut correction can also be retained in the tensor model itself: if \(f_j-g_j=dh_j+h_jd\), a homotopy for \(\bigotimes_jf_j-\bigotimes_jg_j\) is
\[
\sum_j f_1\otimes\cdots\otimes f_{j-1}\otimes h_j\otimes g_{j+1}\otimes\cdots\otimes g_k.
\]
On a homogeneous input the term with \(h_j\) has the sign \((-1)^{|x_1|+\cdots+|x_{j-1}|}\). The differential (TWC8.4) cancels all other-factor terms, leaving the telescoping sum of \(f_j-g_j\). This proves the claimed homotopy, retaining every coordinate of DCA's correction in its factor. These transposes and tensor comparisons do not presume a dual-tensor or current-product isomorphism.

The total tensor cochain model keeps each word of factor degrees \(\epsilon_a\in\{-1,0,1\}\), both choices of pole when \(\epsilon_a=0\), and each endpoint choice. If exactly \(j\) factors use the degree-one \(A\) term, pullback has the exact geometric factor \(n^j\) times the tensor of the unshifted coefficient actions. In particular the top product term carries \(n^k T_n^{\widehat\otimes k}\), and its transfer is \(T_{1/n}^{\widehat\otimes k}\). This is the top oriented degree of the product of spheres. Every endpoint word carries the product of its original displayed endpoint characters, together with the other factors' actions.

These statements are about the constructed external tensor model and its actual product-cover maps. No Künneth isomorphism for unspecified infinite-coefficient derived functors is assumed. In particular this external product's largest geometric weight increment is \(2k\), not the fixed \(+2\) of \(H_c^2\) on the single curve in Deligne DP3–DP5. Taking a \(k\)-th root does not make \(2k/k\) vanish. The same-base tensor of this particular actual complex P uses the full local tensor complex (TWC8.4), not the two-term complex (TWC8.1) with its original degrees. A different degree-zero tensor coefficient system would require its own construction and comparison; the displayed computation does not preclude such a construction.

## TWC10. Every positive form on the complete tensor receiver and its common radical

We now perform the next calculation forced by the matching characters. On \(\mathscr H_k\), consider every jointly continuous positive semidefinite Hermitian form \(B\), linear in the first variable, satisfying the actual product-transfer identity
\[
B(A_n^{(k)}x,y)=B(x,C_n^{(k)}y)\quad(n\ge1).
\tag{TWC10.1}
\]
Let
\[
\mathscr C_k=\{\boldsymbol\rho:\Re\sigma(\boldsymbol\rho)=k/2\},
\qquad (P_{\mathscr C_k}z)_{\boldsymbol\rho}=1_{\mathscr C_k}(\boldsymbol\rho)z_{\boldsymbol\rho}.
\tag{TWC10.2}
\]
This coordinate projection is continuous and contractive in every \(P_N\). Its image and kernel are complete complemented subspaces.

For a coordinate vector \(e_{\boldsymbol\rho}\), (TWC10.1), applied to \(y=A_n^{(k)}e_{\boldsymbol\rho}\), gives
\[
n^{2\Re\sigma(\boldsymbol\rho)}B(e_{\boldsymbol\rho},e_{\boldsymbol\rho})
=n^kB(e_{\boldsymbol\rho},e_{\boldsymbol\rho}).
\tag{TWC10.3}
\]
Take any already recovered integer \(n>1\); this is a test on established arithmetic, not the initial definition of a number or a unit. Outside \(\mathscr C_k\), the two scalars differ, so the coordinate has zero norm and by Cauchy–Schwarz pairs to zero with every vector. Finite-coordinate truncations of any vector in \(\ker P_{\mathscr C_k}\) converge in the full topology. Continuity therefore proves that this entire kernel lies in every such form's radical.

Conversely for each integer \(N\ge0\),
\[
B_N(x,y)=\sum_{\boldsymbol\rho\in\mathscr C_k}
m_{\boldsymbol\rho}W_{\boldsymbol\rho}^{2N}
 x_{\boldsymbol\rho}\overline{y_{\boldsymbol\rho}}
\tag{TWC10.4}
\]
is a continuous positive form and satisfies (TWC10.1), since on \(\mathscr C_k\)
\(n^{\sigma}=\overline{n^{k-\sigma}}\).
Already \(B_0\) detects every nonzero coordinate there. Thus the exact common radical is
\[
\boxed{\quad\bigcap_{B\text{ satisfying }\mathrm{(TWC10.1)}}\operatorname{rad}B
=\ker P_{\mathscr C_k}.\quad}
\tag{TWC10.5}
\]
Moreover the topology generated by all these positive-form seminorms on the quotient is exactly its inherited rapid topology. Indeed continuity of any \(B\), with increasing seminorms \(P_N\), gives \(|B(x,y)|\le C P_N(x)P_N(y)\) for some \(C,N\) by rescaling a product neighborhood of zero. Since \(B\) annihilates the complementary kernel, replace both arguments by their projected values. This bounds its seminorm by \(\sqrt C P_N(P_{\mathscr C_k}x)\). The reverse inclusion follows because every squared inherited norm is (TWC10.4). The complete common positive receiver is therefore precisely
\[
\mathscr H_{k,\mathscr C_k}=P_{\mathscr C_k}\mathscr H_k.
\tag{TWC10.6}
\]
This proves a whole-domain classification of the common radical and topology, without limiting the argument to finite blocks. It does not claim a diagonal classification of each individual form: coordinates with the same total imaginary exponent can pair nontrivially inside this receiver.

The actual source map into this receiver is
\[
\mathscr R_k\xrightarrow{b_k}\mathscr H_k
\xrightarrow{P_{\mathscr C_k}}\mathscr H_{k,\mathscr C_k},
\quad
\ker(P_{\mathscr C_k}b_k)=\bigcap_{\boldsymbol\rho\in\mathscr C_k}
\ker\varepsilon_{\boldsymbol\rho}.
\tag{TWC10.7}
\]
Its image is dense and contains every finite centered coordinate vector, by the same original source isolators. Equations (TWC10.4) pull back to continuous positive product-transfer forms on the original completed tensor source. We do not claim that every form intrinsic to \(\mathscr R_k\) is obtained in this way.

For \(k=1\), the off-line set has no centered coordinate, agreeing with CPS's zero positive receiver. For \(k=2\), every actual pair \((\rho,\rho^\#)\) lies in \(\mathscr C_2\), by (TWC6.4). The vector \(v_{\rho^\#}\otimes v_\rho\) maps to a nonzero coordinate there, with exact coefficient \(-\delta_\rho^2\), norm square \(m_\rho^2|\delta_\rho|^4\) for the individual-coordinate form. Same-eigenvalue tuples \((\rho,\ldots,\rho)\) are never in \(\mathscr C_k\) on the off-line subset. Hence the positive tensor receiver retains reflected products and kills the very same-eigenvalue powers that would amplify an off-line weight. This is a computed map and kernel on the actual divisor, not a replacement of it by hypothetical zeros.

### TWC10 continued. The original tensor Weil form on the retained sector

The original complementary Weil form descends continuously to \(\mathcal R\):
\[
W_R(F,G)=\sum_{\rho\in\mathscr Z_O}m_\rho F(\rho)\overline{G(\rho^\#)}.
\tag{TWC10.8}
\]
Indeed \(\mathcal B_O\) annihilates either slot, and the original rapid estimates prove continuity. Its tensor form extends to \(\mathscr R_k\) because the associated multilinear map is bounded by a product of continuous source seminorms. More explicitly, let \(\mathcal E_k\) be the continuous tensor of the original off-line value evaluations, constructed as in TWC3 with no \(\delta\) factor. Then
\[
W_R^{\otimes k}(z,w)=\sum_{\boldsymbol\rho}m_{\boldsymbol\rho}
 (\mathcal E_kz)_{\boldsymbol\rho}
 \overline{(\mathcal E_kw)_{\boldsymbol\rho^\#}}
=(-1)^k\sum_{\boldsymbol\rho}
\frac{m_{\boldsymbol\rho}(b_kz)_{\boldsymbol\rho^\#}
\overline{(b_kw)_{\boldsymbol\rho}}}{\prod_j|\delta_{\rho_j}|^2}.
\tag{TWC10.9}
\]
The first series converges absolutely by Cauchy–Schwarz in the full product-multiplicity Hilbert norm. Substitution of (TWC3.1) and \(\delta_{\rho^\#}=-\delta_\rho\) proves the second series and its convergence on exactly the indicated source. It is not declared continuous on the unweighted whole \(\mathscr H_k\).

Its complete receiving space with the needed topology is
\[
\mathscr H_{k,\delta}^{\mathrm{src}}=
\{y:(y_{\boldsymbol\rho}/\prod_j\delta_{\rho_j})_{\boldsymbol\rho}\in\mathscr H_k\},
\quad P_{N,\delta}(y)=P_N((y_{\boldsymbol\rho}/\prod_j\delta_{\rho_j})_{\boldsymbol\rho}).
\tag{TWC10.10}
\]
Multiplication by the nonzero product of the \(\delta\)'s is an explicit isomorphism from \(\mathscr H_k\) onto this space; its inclusion into \(\mathscr H_k\) is continuous by \(|\delta_\rho|\le r-1\). The map \(b_k\) lands continuously in it, since division gives the reflected original evaluation tensor. The second pairing in (TWC10.9) is continuous there by Cauchy–Schwarz, and the positive-sector projection preserves this space contractively in all its norms. This retains the full original tensor pairing and the exact stronger receiving topology.

For each actual off-line \(\lambda\), put
\(u=v_\lambda\otimes v_{\lambda^\#}\) and
\(v=v_{\lambda^\#}\otimes v_\lambda\).
Both map to the centered sector in (TWC10.6). Their original tensor pairings are
\[
W_R^{\otimes2}(u,u)=W_R^{\otimes2}(v,v)=0,
\quad W_R^{\otimes2}(u,v)=W_R^{\otimes2}(v,u)=m_\lambda^2,
\]
\[
\boxed{\quad W_R^{\otimes2}(u+v,u+v)=2m_\lambda^2,
\qquad W_R^{\otimes2}(u-v,u-v)=-2m_\lambda^2.\quad}
\tag{TWC10.11}
\]
These follow by evaluating the two original isolators in (TWC10.8) before tensoring. By contrast the pulled-back positive form (TWC10.4) with \(N=0\) gives, for either sign,
\[
B_0(b_2(u\pm v),b_2(u\pm v))=2m_\lambda^2|\delta_\lambda|^4.
\tag{TWC10.12}
\]
The same-modulus sector has not turned the original tensor Weil form into that positive form. Their exact difference is exhibited on the retained sector itself. This calculation does not posit an actual off-line zero; it computes the map and pairing on each such coordinate of the actual divisor, if present, and is vacuous when that divisor subset is empty.

## TWC11. The exact comparison with Deligne and the result of this attempt

DP4–DP6 reconstruct Deligne's mechanism on one fixed arithmetic curve: real local traces give nonnegative coefficients in every even tensor power; the same curve's complete \(H_c^2\) denominator supplies a fixed \(+2\); the determinant-weight sum and exterior powers then force equality of individual weights. DP5 uses the same-eigenvalue tensor \(\alpha^{2k}\), not the reflected product \(\alpha\alpha^\#\).

For the actual specialization source we have now constructed all tensor powers on their original source topology, the full common multiplier receiver, every product-cover character, the exact coefficient-product defect, and the full positive tensor projection. Their comparison gives the following proved statements together:

* The actual tensor map (TWC3.1) remains nonzero on every nonzero repeated source vector, with matching source and target characters (TWC6.2). A tensor power alone does not produce disjoint weights for this boundary.
* The fixed-modulus reflected restriction (TWC6.4) retains the coefficient \(-\delta_\rho^2\) and is not the same-eigenvalue power used in the Deligne step. The exact positive receiver (TWC10.6) includes this reflected sector and removes off-line same-eigenvalue powers by its displayed kernel.
* The full original multiplicity trace and the value-receiver operator trace are linked by (TWC7.3), rather than conflated. Every multiplicity, higher jet and original-zeta source factor remains in the corresponding source or retained kernel.
* The geometric external product has its actual \(n^k\) degree and all normal factors; its top weight increment is \(2k\). The actual same-base local tensor complex has the different degrees and differential (TWC8.4). Neither is silently assigned the fixed-curve cohomological denominator from Deligne.

The step prompted by the first limitation was carried out: instead of stopping at matching characters, TWC10 computes the entire positive tensor receiver, its complete topology, its exact source kernel and its reflected-pair image. TWC4 also constructs the stronger weighted receiver needed to recover the coefficient product without an unjustified inverse. Equations (TWC10.8–12) then recover the original tensor Weil form with its own exact receiving topology, and exhibit both signs on the centered reflected sector itself. These are new maps on the actual specialization source. They do not prove that the original derived connecting class vanishes, or identify its full tensor geometry with a finite-rank Frobenius sheaf satisfying Deligne's pole formula.

Human-source provenance: Connes–Consani's original summation sheaf, *Schemes over* \(\mathbb F_1\) *and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3), and the actual signed-chart geometry [arXiv:2609.00299v1](https://arxiv.org/abs/2609.00299v1), enter through the pinned ACD/DCA/ADM constructions. Deligne's *La conjecture de Weil. II*, [IHÉS 52 (1980), §§1.3–1.5 and §3.6](https://numdam.org/item/PMIHES_1980__52__137_0/), enters through DP and DC with their exact reading ledgers. DP uses the identified French transcription, SHA256 d6836ae15d98f2b27eb98c9bd039a7d921679becd9fa47ff4717410289dbd351, not author TeX; this proof makes no new claim to have read the entire human paper. The new tensor receiver and its positivity calculation are programme derivations, not claims attributed to those authors.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Spectral synthesis on the original completed tensor source

Complete derivation CTS0–CTS6, 25 September 2026. This calculation combines the full-source approximation GSP with the actual tensor maps TWC. It proves statements left open when those calculations were performed separately.

## CTS0. Corrected construction and exact dependencies

The supporting datum is still \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). No addition, coordinate, metric, vector or midpoint is assigned to it. All coefficient spaces and arithmetic operators below occur after the complete-history reconstruction. The separate branch counters and original return measures are unchanged. The full user argument and correction record governs these operations; the new approximation does not supply an alternative definition of arithmetic.

GSP7 proves continuous finite-rank operators \(K_j=\overline K_j:\mathcal R\to\mathcal R\) converging to identity uniformly on bounded sets in the **original** Fréchet quotient topology. Here
\[
\mathcal R=\mathcal B/\mathcal B_O=\mathcal Q/N_O,
\quad \mathcal B_O=\{F\in\mathcal B:F(\lambda)=0\ (\lambda\in\mathscr Z_O)\},
\tag{CTS0.1}
\]
and \(\mathscr Z_O\) is the actual off-critical-line subset of the nontrivial zeros of original \(\zeta\). The original full-jet quotient \(\mathcal Q=\mathcal B/\mathcal I\) remains, with every higher jet in the specified kernel of \(\mathcal Q\to\mathcal R\). GSP does not assume RH, simplicity of zeros, or identification of this quotient topology with a sequence topology.

For the original value isolator \(v_\lambda\in\mathcal R\), the formula is
\[
K_jx=\sum_{\substack{\lambda\in\mathscr Z_O\\|\Im\lambda|<T_j}}
e^{\lambda^2/j}\,\mathrm{ev}_\lambda(x)\,v_\lambda.
\tag{CTS0.2}
\]
The finite sum, its nonzero Gaussian coefficients and the convergence in the original quotient topology are proved in GSP4 and GSP7, rather than postulated here. The heights are GSP's zero-free heights \(T_j\in[j^6,j^6+1]\), with the finitely many initial choices as specified there.

TWC2–3 construct the continuous map
\[
b_k:\mathscr R_k=\mathcal R^{\widehat\otimes_\pi k}\longrightarrow\mathscr H_k,
\quad
(b_kx)_{\boldsymbol\rho}=\Bigl(\prod_{a=1}^k\delta_{\rho_a}\Bigr)
\varepsilon_{\boldsymbol\rho^\#}(x),
\tag{CTS0.3}
\]
where \(\varepsilon_{\boldsymbol\lambda}=\mathrm{ev}_{\lambda_1}\widehat\otimes\cdots\widehat\otimes\mathrm{ev}_{\lambda_k}\),
\(\rho^\#=1-\overline\rho\), and
\[
\delta_\rho=e^{i\Im\rho\log r}(r^{\Re\rho}-r^{1-\Re\rho}),\quad r>1.
\tag{CTS0.4}
\]
Every \(\delta_\rho\) on this actual off-line set is nonzero. Its magnitude is not given a positive uniform lower bound. The receiver retains the norms
\[
P_N(y)^2=\sum_{\boldsymbol\rho\in\mathscr Z_O^k}
\Bigl(\prod_a m_{\rho_a}\Bigr)\Bigl(\prod_a(1+|\Im\rho_a|)\Bigr)^{2N}
|y_{\boldsymbol\rho}|^2.
\tag{CTS0.5}
\]

The original source transform remains
\[
\Theta a(s)=\tfrac12\int_0^\infty a(u)u^s\frac{du}{u},\qquad
\Theta^{-1}F(u)=\frac{u^{-1/2}}\pi\int_{\mathbb R}F(1/2+it)u^{-it}\,dt.
\tag{CTS0.6}
\]
Its full source multiplier is
\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\tfrac18,\quad F_0(-1)=F_0(2)=\tfrac\pi{24},
\]
\[
F_0(-2a)=\frac{a(2a+1)(-1)^a\pi^a}{2a!}\zeta'(-2a)\quad(a\ge1).
\tag{CTS0.7}
\]
At a zero \(\rho\) its full germ is the product in TWC1.5, and every derivative uses TWC1.6's complete Leibniz sum. None of these factors or exceptional values is changed by tensoring the already constructed maps. The original arithmetic stays
\[
\zeta(s)=1+\sum_{n\ge2}n^{-s}=\prod_p(1-p^{-s})^{-1},\qquad
-\frac{\zeta'}\zeta(s)=\sum_p\sum_{a\ge1}(\log p)p^{-as}\quad(\Re s>1).
\tag{CTS0.8}
\]
This proof uses the local GSP and TWC derivations, not a new reading of a human paper. Their pinned CC and Deligne provenance remains in their source ledgers.

## CTS1. Equicontinuity before completed tensoring

Choose increasing continuous seminorms \(p_\ell\) defining the original Fréchet topology of \(\mathcal R\). For each fixed \(p_\ell\), convergence of \(K_jx\) implies \(\sup_jp_\ell(K_jx)<\infty\) for every \(x\). To obtain the needed uniform estimate, consider the closed sets
\[
E_m=\{x:\sup_jp_\ell(K_jx)\le m\},\qquad \mathcal R=\bigcup_{m\ge1}E_m.
\]
The Baire property gives one set with nonempty interior. Differences of two points in an interior translate give a neighborhood \(V\) of zero on which \(\sup_jp_\ell(K_jx)\le2m\). Choose \(d\) and \(\epsilon>0\) such that \(p_d(x)<\epsilon\) implies \(x\in V\). Rescale \(x\), then let the rescaling approach the boundary, to obtain
\[
\sup_jp_\ell(K_jx)\le C p_d(x)\quad(x\in\mathcal R).
\tag{CTS1.1}
\]
If \(p_d(x)=0\), apply the bound to arbitrary scalar multiples of \(x\); it forces the left side to be zero. Enlarging \(d\) and \(C\) also bounds \(p_\ell(x)\). Thus both the identity and all \(K_j\) have a common seminorm bound. This derives the required equicontinuity from the actual Fréchet approximation.

On the algebraic \(k\)-fold tensor product, let \(\pi_\ell\) be the projective seminorm obtained from \(p_\ell\) in every factor. The family is cofinal because any finite set of source seminorms is bounded by one of the increasing family, with constants retained. Taking the infimum over finite tensor representations in (CTS1.1) gives
\[
\pi_\ell(K_j^{\otimes k}x)\le C^k\pi_d(x).
\tag{CTS1.2}
\]
These maps therefore extend continuously to the Hausdorff completion \(\mathscr R_k\), uniformly with this estimate. Their ranges remain finite dimensional: each is contained in the finite tensor product of \(\mathrm{im}K_j\), which is a closed finite-dimensional subspace of the Hausdorff completed tensor space. The coordinates \(\varepsilon_{\boldsymbol\lambda}\) separate that finite span, so its embedding and the stated range identification are explicit.

## CTS2. Convergence and the complete source expansion

On a decomposable tensor the telescoping identity is
\[
K_j^{\otimes k}(x_1\otimes\cdots\otimes x_k)-x_1\otimes\cdots\otimes x_k
=\sum_{a=1}^k K_jx_1\otimes\cdots\otimes K_jx_{a-1}
\otimes(K_jx_a-x_a)\otimes x_{a+1}\otimes\cdots\otimes x_k.
\tag{CTS2.1}
\]
Each summand tends to zero in every projective seminorm: the differing factor tends to zero and every other factor is bounded in the required source seminorm. Hence there is convergence on finite algebraic sums. For an arbitrary completed tensor \(x\), first choose an algebraic tensor \(x_0\) close in \(\pi_d\) for the common bound (CTS1.2) and for the identity. Then
\[
\pi_\ell((K_j^{\widehat\otimes k}-1)x)
\le(C^k+1)\pi_d(x-x_0)+\pi_\ell((K_j^{\otimes k}-1)x_0),
\tag{CTS2.2}
\]
after enlarging the constants if necessary. The second term tends to zero, and the first can be made arbitrarily small. We have proved
\[
K_j^{\widehat\otimes k}x\longrightarrow x\quad\hbox{in the original completed projective topology.}
\tag{CTS2.3}
\]
Equicontinuity and finite nets also give uniform convergence on compact subsets. We do not need or infer uniform convergence on every bounded subset of this tensor space.

Tensoring the finite formula (CTS0.2), first on simple tensors and then on the completion by continuity, yields the exact reconstruction
\[
K_j^{\widehat\otimes k}x=
\sum_{\substack{\boldsymbol\lambda\in\mathscr Z_O^k\\|\Im\lambda_a|<T_j\ (1\le a\le k)}}
\exp\!\left(\frac1j\sum_{a=1}^k\lambda_a^2\right)
\varepsilon_{\boldsymbol\lambda}(x)
\,v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k}.
\tag{CTS2.4}
\]
Every cutoff, factor and evaluation is retained. In particular the linear span of these finite tensor blocks is dense in the original completed source.

## CTS3. The completed tensor map is injective

Suppose \(b_kx=0\). Equation (CTS0.3) and the nonzero factors (CTS0.4) give \(\varepsilon_{\boldsymbol\lambda}(x)=0\) for every actual tuple. Formula (CTS2.4) then gives \(K_j^{\widehat\otimes k}x=0\) for every \(j\). Passing to the actual source limit (CTS2.3) yields \(x=0\). Consequently
\[
\boxed{\ker b_k=0\quad\text{on }\mathcal R^{\widehat\otimes_\pi k}.}
\tag{CTS3.1}
\]
This discharges the completed-kernel question explicitly retained in TWC3.2 and TRC3. The older statements did not assert a nonzero kernel; they correctly retained it until this additional convergence theorem was available. No assumption of exactness of arbitrary completed projective tensor products is used.

TWC3 already constructs all finite-coordinate vectors in the image. Thus \(b_k\) is a continuous injective map with dense image into \(\mathscr H_k\). Formula (CTS3.1) alone proves neither surjectivity nor a topological embedding. Its stronger source-weighted receiver from TWC10.10, and the original source topology, are retained.

## CTS4. All positive transfer forms intrinsic to the tensor source

The genuine product pullback and weighted transfer on \(\mathscr R_k\) are
\[
U_n=T_n^{\widehat\otimes k},\qquad V_n=(nT_{1/n})^{\widehat\otimes k},\qquad V_nU_n=n^k1.
\tag{CTS4.1}
\]
Both are continuous by the already constructed coefficient action. Consider the family \(\mathcal P_k\) of **all** jointly continuous positive semidefinite Hermitian forms on this original completed source, linear in the first argument, such that
\[
B(U_nx,y)=B(x,V_ny)\quad(n\ge1).
\tag{CTS4.2}
\]
For a finite tensor isolator \(v_{\boldsymbol\lambda}=v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k}\), the eigenvalue is \(n^{\sum_a\lambda_a}\). Apply (CTS4.2) to \((v_{\boldsymbol\lambda},U_nv_{\boldsymbol\lambda})\). The left side is \(n^{2\Re\sum_a\lambda_a}B(v_{\boldsymbol\lambda},v_{\boldsymbol\lambda})\), and the right side is \(n^k B(v_{\boldsymbol\lambda},v_{\boldsymbol\lambda})\). Any recovered integer \(n>1\) therefore shows that
\[
\Re\sum_a\lambda_a\ne k/2
\quad\Longrightarrow\quad B(v_{\boldsymbol\lambda},v_{\boldsymbol\lambda})=0.
\tag{CTS4.3}
\]
Positivity implies Cauchy–Schwarz, proved by expanding \(B(u+tv,u+tv)\ge0\) for arbitrary complex \(t\); a zero-norm vector pairs to zero with every vector. Thus every noncentered finite tensor lies in every such form's radical.

Let
\[
\mathscr D_k^{\rm src}=\bigcap_{\substack{\boldsymbol\lambda\in\mathscr Z_O^k\\\Re\sum_a\lambda_a=k/2}}
\ker\varepsilon_{\boldsymbol\lambda}.
\tag{CTS4.4}
\]
It is closed. If \(x\) lies there, (CTS2.4) uses only noncentered finite tensors, so every approximation lies in every form's radical. Continuity and (CTS2.3) give the same for \(x\).

Conversely TWC10.4 constructs the positive product-transfer form
\[
B_0^{\rm src}(x,y)=\sum_{\substack{\boldsymbol\rho\in\mathscr Z_O^k\\\Re\sum_a\rho_a^\#=k/2}}
\Bigl(\prod_a m_{\rho_a}\Bigr)(b_kx)_{\boldsymbol\rho}
\overline{(b_ky)_{\boldsymbol\rho}}.
\tag{CTS4.5}
\]
It is jointly continuous on the original source because \(b_k\) is continuous. Its norm is zero precisely when all centered evaluations in (CTS4.4) are zero, since every multiplicity is positive and every product of \(\delta\)'s is nonzero. We conclude
\[
\boxed{\bigcap_{B\in\mathcal P_k}\operatorname{rad}B
=\mathscr D_k^{\rm src}
=\overline{\operatorname{span}\{v_{\boldsymbol\lambda}:\Re\sum_a\lambda_a\ne k/2\}}^{\,\mathscr R_k}.}
\tag{CTS4.6}
\]
For the last equality, the span is contained in the closed intersection of centered kernels; its Gaussian approximants reconstruct every vector in that intersection. This extends the common-radical theorem to **all continuous forms on the actual tensor source**, including forms not known to factor continuously through the rapid receiver. No assertion about the topology generated by that larger form family is required or inferred.

## CTS5. Retained original pairing and the fixed-base continuation

For \(k=1\), every actual off-line coordinate is noncentered, so (CTS4.6) recovers the zero positive-form family on \(\mathcal R\). For \(k=2\), each pair \((\lambda,\lambda^\#)\) is centered, with exact cover eigenvalue \(n^{1+2i\Im\lambda}\). The two finite tensors
\[
u=v_\lambda\otimes v_{\lambda^\#},\qquad v=v_{\lambda^\#}\otimes v_\lambda
\]
survive the positive common quotient whenever the actual off-line coordinate is present. Their original complementary Weil tensor pairing remains
\[
W_R^{\otimes2}(u\pm v,u\pm v)=\pm2m_\lambda^2,
\qquad B_0^{\rm src}(u\pm v,u\pm v)=2m_\lambda^2|\delta_\lambda|^4.
\tag{CTS5.1}
\]
These are TWC10.8–12's exact original-source evaluations, not two names for the same form. The completed-source injectivity now proves there is no additional unseen tensor kernel explaining their difference.

The next calculation prompted by this result, using the preceding geometric work as well, is the tensor complex **over the single existing sphere**. Its local terms are TWC8.2–4 with their Koszul signs. Its global angular class carries one sphere-degree factor, while the external product in TWC9 carries a product of those factors. The fixed-base cochain calculation is being performed on that actual complex; no fixed \(+2\) weight is assigned to a coefficient merely to copy Deligne's conclusion. CTS proves exact source reconstruction and detection, not vanishing of the original specialization or its derived connecting class.

## CTS6. Proof-use and propagation record

GSP4 and GSP7 supply the additional hypothesis already proved on the original quotient: finite-rank spectral synthesis in its Fréchet topology. CTS1–3 perform the completed tensor argument, rather than treating TWC's former kernel qualification as a reason to stop. CTS4 uses that reconstruction to remove the earlier restriction to forms continuous on a selected receiver. The remaining differences of topology and of the original Weil pairing are recorded with their exact maps and kernels.

The full proof inputs are [Gaussian spectral synthesis](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_SPECTRAL_SYNTHESIS.md), [its independent derivation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/GAUSSIAN_SPECTRAL_SYNTHESIS_INDEPENDENT.md), [the actual tensor calculation](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/ACTUAL_SPECIALIZATION_TENSOR_WEIGHT_COMPARISON.md), and [the independent tensor receiver proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260925-full-source-tensor-and-original-divisor/gct/TENSOR_RECEIVER_INDEPENDENT_CHECK.md). The cumulative edition retains them in full. Earlier TWC3/TRC3 and TWC10 scopes are strengthened by CTS3 and CTS4, respectively; their earlier text is preserved for provenance. Nothing here claims a new complete reading of CC or Deligne, an arithmetic purity theorem, or a resolution of RH.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# The actual tensor square on one sphere: specialization, supported boundaries and angular degree

Complete independent derivation, **FST0–FST7**. This supplements the frozen TWC0–11 proof; it does not change that proof or claim that the original lifting obstruction vanishes.

## FST0. Stage and actual source

The supporting datum remains \(\tau\langle Z_1;\mathrm{no}\ Z_2\rangle\). The coefficient operations below occur after complete-history arithmetic reconstruction. The two recovered branch counters and original return measures remain separate. No addition, numerical origin, metric, or coordinate operation is placed on the support. TWC0 records the connected correction-chain reading; its private reading receipt additionally records the recalled verbatim U060, U138–U141, WU050–WU055, WU061–WU062 and WU064–WU065 passages. A source tensor is not a pooled return measure.

Use the actual common-domain source complex on the sphere \(Y\), with two labelled poles \(p_+,p_-\):
\[
P=[\underline A_Y^{-1}\xrightarrow{(b_r,b_r)}i_+H_\infty\oplus i_-H_\infty],
\quad b_r=\beta_rq,
\quad(b_ra)_\rho=\delta_\rho(\Theta a)(\rho^\#),
\quad\delta_\rho=\overline{d_r(\rho)}.
\tag{FST0.1}
\]
Here \(H_\infty=H_{\infty,L}\oplus H_{\infty,O}\) retains the entire actual divisor and multiplicities; \(b_rA\subset H_{\infty,O}\) is dense there. Set \(A_O=\ker b_r\), so the actual original specialization source is \(\mathcal R=A/A_O\). Every endpoint summand is reattached explicitly in FST6.

The source and all analytic factors are the original ones in ADM1 and TWC1, including
\[
\Theta a(s)=\tfrac12\int_0^\infty a(u)u^s\,du/u,
\quad F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s),
\quad F_0(0)=F_0(1)=\tfrac18,
\]
\[
F_0(-2j)=\frac{j(2j+1)(-1)^j\pi^j}{2\,j!}\zeta'(-2j)\quad(j\ge1),
\quad F_0(-1)=F_0(2)=\pi/24.
\tag{FST0.2}
\]
All local multiplicity germs and their full Leibniz derivatives, the normal factor \(F_0(\lambda-1)\), the unit term and all prime-power repetitions remain exactly TWC1.3–7 and TWC5.4. This supplement changes the receiving geometry, not the original zeta function.

## FST1. Same-base square with its complete differential

We construct the coefficientwise completed tensor square on the **same sphere**, not the external square on \(Y\times Y\). Since the support of the two pole skyscrapers is disjoint, their mixed same-base products are zero. Put
\[
V=A\widehat\otimes_\pi A,\qquad
L=(H_\infty\widehat\otimes_\pi A)\oplus(A\widehat\otimes_\pi H_\infty),
\qquad M=H_\infty\widehat\otimes_\pi H_\infty.
\tag{FST1.1}
\]
The explicit sheaf complex is
\[
K=[\underline V_Y^{-2}\xrightarrow{(d_0,d_0)}i_+L\oplus i_-L
\xrightarrow{d_1\oplus d_1}i_+M\oplus i_-M],
\tag{FST1.2}
\]
where, in each pole chart,
\[
d_0(a\otimes a')=(b_ra\otimes a',-a\otimes b_ra'),
\quad d_1(h\otimes a',a\otimes h')=h\otimes b_ra'+b_ra\otimes h'.
\tag{FST1.3}
\]
On elementary tensors the two terms of \(d_1d_0\) cancel. Continuity and density extend that identity to the full completed domain. Thus (FST1.2) is an actual complete coefficient cochain model. It agrees with the termwise tensor of (FST0.1) on the open stratum and the two pole strata, with their restriction maps. No exactness theorem for arbitrary completed tensor products is used or required by this explicit construction. It is a literal completed projective coefficient tensor complex, not a claim to compute an unspecified derived topological tensor functor.

## FST2. The actual same-base global cochain model

The two-pole Čech complex is
\[
V\oplus V\longrightarrow L\oplus L\oplus V
\longrightarrow M\oplus M\oplus V
\tag{FST2.1}
\]
in degrees \((-2,-1,0)\). Its differentials are
\[
(x_+,x_-)\longmapsto(d_0x_+,d_0x_-,x_+-x_-),
\qquad(\ell_+,\ell_-,c)\longmapsto(d_1\ell_+,d_1\ell_-,0).
\tag{FST2.2}
\]
To obtain it, use contractibility of either pole disk for the complete constant coefficient \(V\), and the annular cohomology \(V\) in angular degrees zero and one. The coefficient Poincaré contractions integrate continuous \(V\)-valued forms over compact intervals; completeness makes these integrals exist, and the usual derivative identities prove the contraction coefficientwise. A skyscraper has only its pole-section term and no overlap restriction. Consequently the overlap contributes exactly the third \(V\) in the two successive degrees, and its restriction difference is the last component of (FST2.2). Equivalently, this is the explicit Čech cone of the two pole complexes mapping to \(V[2]\) on the overlap, retaining the annular degree-one coordinate. The cone convention is the one displayed in (FST2.2).

There is a continuous cochain equivalence to
\[
G_2=[V^{-2}\xrightarrow{(d_0,d_0)}L^{-1}\oplus L^{-1}
\xrightarrow{d_1\oplus d_1}M^0\oplus M^0\oplus V^0],
\tag{FST2.3}
\]
with zero differential into its last \(V\). The projection is
\[
p^{-2}(x_+,x_-)=x_-,\quad
p^{-1}(\ell_+,\ell_-,c)=(\ell_+-d_0c,\ell_-),\quad p^0=1.
\tag{FST2.4}
\]
The inclusion is the diagonal in degree \(-2\), \((\ell_+,\ell_-)\mapsto(\ell_+,\ell_-,0)\) in degree \(-1\), and identity in degree zero. The homotopy is \(h^{-1}(\ell_+,\ell_-,c)=(c,0)\), zero elsewhere. Substitution into (FST2.2) gives \(dh+hd=1-ip\), using \(d_1d_0=0\). Hence no unsupported Künneth statement is needed.

The angular \(V\) records the sphere's oriented degree-two class after the shift by two. Under the unshifted positive de Rham comparison, the overlap form \(\vartheta=d\arg z/(2\pi)\) with Čech restriction \(x_+-x_-\) is compared to \(d\chi_+\wedge\vartheta\), whose integral is \(-1\), for \(\chi_+\) equal to one near the zero pole and zero near infinity. Thus this raw overlap coordinate is the negative of the positive integration coordinate. Multiplying this last coordinate by \(-1\) supplies the positively integrated version. The shift by two has de Rham differential \(+d\), unlike the single-shift \(-d\) convention in ACD6. This sign change is retained; it changes neither the zero differential into that term nor its positive covering-degree factor.

The cohomology of the displayed cochain model, with actual quotient topologies, is
\[
H^{-2}(G_2)=\ker d_0,
\quad H^{-1}(G_2)=(\ker d_1\oplus\ker d_1)/\operatorname{diag}(\operatorname{im}d_0),
\]
\[
H^0(G_2)=(M/\operatorname{im}d_1)\oplus(M/\operatorname{im}d_1)\oplus V.
\tag{FST2.5}
\]
Images in these formulas are not assumed closed. In particular an algebraic quotient is not silently replaced by its Hausdorff quotient.

## FST3. The specialization source remains at the first differential

On a punctured pole disk, the complex is \(\underline V[2]\). Its universal-cover nearby coefficient is \(V[2]\), with identity monodromy; this follows from the same constant-coefficient contraction. The map on the lowest stalk cohomology is the inclusion
\[
H^{-2}(i^*K)=\ker d_0\hookrightarrow V.
\tag{FST3.1}
\]
Therefore the actual invariant-cycle cokernel for this degree is
\[
\mathcal R_{\mathrm{sq}}=V/\ker d_0,
\qquad \ker d_0=\ker(b_r\widehat\otimes1_A)\cap\ker(1_A\widehat\otimes b_r).
\tag{FST3.2}
\]
This is a separated Fréchet quotient, since both kernels are closed. The actual target and boundary can also be read directly from the unshifted specialization cone. With cone convention \(\operatorname{Cone}(i^*K\to\Psi K)\), it is
\[
V^{-3}\longrightarrow(V\oplus L)^{-2}\longrightarrow M^{-1},
\quad v\longmapsto(v,-d_0v),\quad(x,\ell)\longmapsto-d_1\ell.
\tag{FST3.4}
\]
Its continuous projection to \([L^{-2}\xrightarrow{-d_1}M^{-1}]\) is \((x,\ell)\mapsto\ell+d_0x\) and identity on \(M\); the inclusion is \(\ell\mapsto(0,\ell)\). The homotopy \(h^{-2}(x,\ell)=x\) proves \(dh+hd=1-ip\). Hence the canonical map from the nearby \(V\) into the degree-minus-two vanishing group is exactly
\[
V\xrightarrow{d_0}\ker d_1=H^{-2}(\Phi K).
\tag{FST3.5}
\]
Its image is the same actual boundary image as (FST3.2), with both summands and the minus sign in (FST1.3). It is not the map \(b_r\widehat\otimes b_r\) into degree zero.

This kernel also has the full original partial-evaluation description
\[
\ker d_0=\{z\in V:
(\mathrm{ev}_{\rho^\#}\Theta\widehat\otimes1_A)z=0,
\ (1_A\widehat\otimes\mathrm{ev}_{\rho^\#}\Theta)z=0
\text{ for every }\rho\in\mathscr Z_O\}.
\tag{FST3.3}
\]
Indeed the coordinate of \((b_r\widehat\otimes1_A)z\) is the first displayed \(A\)-valued evaluation multiplied by the nonzero \(\delta_\rho\), and its line coordinates vanish. Coordinate evaluations separate \(H_\infty\widehat\otimes_\pi A\): the finite coordinate projection \(P_T\widehat\otimes1_A\) tends to identity there. To prove that convergence, it holds on each elementary tensor; its operators are uniformly bounded for every projective seminorm because \(p_N(P_Ty)\le p_N(y)\). Approximation by finite sums then proves it on the completion. Hence zero coordinates imply the zero tensor. The other factor is identical. This proves (FST3.3) without a completed-tensor exactness or injectivity assumption.

The new invariant-cycle source is zero exactly when the original map \(b_r\) is zero. One direction is immediate. For the other, take \(a\) with \(b_ra\ne0\). Then \(a\ne0\), and \(b_ra\otimes a\ne0\): a nonzero coordinate functional on \(b_ra\) and a continuous linear functional nonzero at \(a\), supplied by separation in the Fréchet space \(A\), detect its tensor. Therefore \(d_0(a\otimes a)\ne0\), proving that its class in (FST3.2) is nonzero. This is a theorem about the actual maps, not an assumed splitting of their source extensions.

## FST4. The tensor detector becomes a top boundary, with its lifting distinction retained

Define the continuous map
\[
B_2=b_r\widehat\otimes b_r:V\to M,
\quad H_2:V\to L,
\quad H_2(a\otimes a')=(b_ra\otimes a',0).
\tag{FST4.1}
\]
Direct computation gives
\[
\boxed{\quad d_1H_2=B_2.\quad}
\tag{FST4.2}
\]
There is also the continuous right-factor homotopy \(H_2^{\mathrm R}(a\otimes a')=(0,a\otimes b_ra')\). It obeys \(d_1H_2^{\mathrm R}=B_2\), and the exact difference is \(H_2-H_2^{\mathrm R}=d_0\). The two null-homotopies retain the original first differential in their difference. Consequently the map from \(V[0]\) to a pole's degree-zero \(M\) in the actual complex \(K\), with value \(B_2\), has the explicitly displayed continuous null-homotopy. The same identity applies at either retained pole in (FST2.3). It is not a statement that the first specialization boundary \(d_0\) vanishes: FST3 computes its separate source and image.

The original source quotient map \(q_R:A\to\mathcal R\) gives a continuous tensor map \(q_R\widehat\otimes q_R:V\to\mathscr R_2\). Its algebraic tensor image is dense, because each elementary source tensor has representatives in \(A\). On that image,
\[
B_2=b_2(q_R\widehat\otimes q_R).
\tag{FST4.3}
\]
The identity holds on the whole \(V\) by continuity. For algebraic tensors from \(\mathcal R\otimes\mathcal R\), choosing representatives supplies a top boundary via (FST4.2). For an arbitrary element of its completed tensor source, the same approximation proves only
\[
b_2(\mathscr R_2)\subset\overline{\operatorname{im}d_1}^{\,M}.
\tag{FST4.4}
\]
No surjective completed lift, closed image, or descent of the homotopy is assumed.

The displayed homotopy specifically does not descend through the two source quotients merely from the formula: replacing the second representative by \(a'+a_O\), with \(a_O\in A_O\), changes it by \((b_ra\otimes a_O,0)\), a retained element of \(\ker d_1\). Replacing the first representative by an element of \(A_O\) changes it by zero. Thus the apparent ambiguity is explicitly in the earlier-degree cocycles. It is retained rather than declared absent. The full source extension from ADM5 is still present in this same-base calculation.

## FST5. The exact Hausdorff supported top receiver

TWC2's proof with the whole actual zero set identifies
\[
M\simeq\{z:\sum_{\rho,\lambda}m_\rho m_\lambda
 w_\rho^{2N}w_\lambda^{2N}|z_{\rho,\lambda}|^2<\infty\ \forall N\}.
\tag{FST5.1}
\]
Let \(P_{LL}=P_L\widehat\otimes P_L\) be the continuous coordinate projection to the line-line tuples. Since \(b_rA\subset H_{\infty,O}\), (FST1.3) gives
\(P_{LL}d_1=0\). Conversely every finite coordinate tensor with at least one off-line coordinate belongs to \(\operatorname{im}d_1\): use an original source isolator realizing that coordinate under \(b_r\), and use the other factor's coordinate vector. Finite truncations converge in every norm in (FST5.1). Hence
\[
\boxed{\quad\overline{\operatorname{im}d_1}^{\,M}=\ker P_{LL},
\qquad M/\overline{\operatorname{im}d_1}\simeq
H_{\infty,L}\widehat\otimes_\pi H_{\infty,L}.\quad}
\tag{FST5.2}
\]
This is the exact Hausdorff receiving quotient at each pole. The nonseparated kernel \(\overline{\operatorname{im}d_1}/\operatorname{im}d_1\) of the map from the actual quotient remains explicit. In particular the reflected off-line pairs that survived TWC10's positive **product-cover** receiver are among these same-base supported boundaries after Hausdorff passage. The two constructions have different exact maps; neither is replaced by the other.

## FST6. Single-cover degree, all coefficient terms and endpoints

For a recovered integer \(n\ge1\), let \(R_n\) be the coefficient operator \(T_n\) on \(A\) and \(U_n^*\) on \(H_\infty\). The original intertwining \(b_rT_n=U_n^*b_r\) makes the tensor coefficient operator \(K_n=R_n\widehat\otimes R_n\) a cochain map of each local complex (FST1.1–3). Its inverse is the tensor of the continuous coefficient inverses.

Construct the genuine **single** cover \(f_n(z)=z^n\) on the same sphere. There are \(n\) nearby sheets for the coefficient \(V\), not \(n^2\). Its unit is the \(n\)-fold diagonal with coefficient \(K_n\); its weighted trace is sheet sum with coefficient \(K_n^{-1}\). On the constant pole term this is \(nK_n^{-1}\), and on each supported pole term take the same \(nK_n^{-1}\). These choices make all differential squares commute, because \(K_n\) is a cochain map. They therefore define actual maps of the displayed sheaf complex. Trace after unit is \(nI\); reverse order is the full nearby deck norm, and \(nI\) on each supported pole term. No augmentation sheet is discarded.

On the global model (FST2.3), the coefficient terms carry pullback \(K_n\) and weighted trace \(nK_n^{-1}\). The angular term carries instead
\[
n(T_n\widehat\otimes T_n),\qquad
T_{1/n}\widehat\otimes T_{1/n},
\tag{FST6.1}
\]
whose composite is \(nI\). Pullback has positive angular degree \(n\); the angular trace of the cover, before its chosen coefficient weighting, has factor one. Switching the raw angular coordinate to the positive integration coordinate conjugates both actions by the same sign and leaves (FST6.1) unchanged.

This is not the tensor of the original two weighted trace maps: on coefficient terms that tensor is \(n^2K_n^{-1}\), whereas the constructed same-base weighted trace is \(nK_n^{-1}\). Their exact comparison factor is \(1/n\). The distinction follows from the computed sheet count and is retained, not absorbed into a renamed action. The diagram is a single-cover tensor coefficient construction, not the external product of two degree-\(n\) covers.

For endpoints let \(E=i_+E_+\oplus i_-E_-\), with original coordinate labels \((c_0,c_1,d_0,d_1)\). The full source is \(P\oplus E[1]\); its square is exactly
\[
K\oplus(P\widehat\otimes E[1])\oplus(E[1]\widehat\otimes P)
\oplus(E\widehat\otimes E)[2].
\tag{FST6.2}
\]
At a fixed pole, the first mixed complex has terms \(A\otimes E_p\to H_\infty\otimes E_p\) in degrees \((-2,-1)\), differential \(+b_r\otimes1\); the second has \(E_p\otimes A\to E_p\otimes H_\infty\) in the same degrees, differential \(-1\otimes b_r\). The last endpoint tensor is in degree \(-2\), with zero differential. Endpoint tensors at distinct poles are zero because their supports are disjoint. Each finite-dimensional endpoint factor uses its original pullback character \(e(n)\in\{1,n\}\); the same-base square pullback multiplies the factor characters, and its weighted trace is \(n\) times the inverse product, exactly as for \(K_n\). In the original ordered tensor bases \((c_0c_0,c_0c_1,c_1c_0,c_1c_1)\) and \((d_0d_0,d_0d_1,d_1d_0,d_1d_1)\), the endpoint-square unit and weighted trace lists are respectively
\[
(1,n,n,n^2),\ (n,1,1,n^{-1});\qquad
(n^2,n,n,1),\ (n^{-1},1,1,n).
\]
Each coordinatewise product is \(n\). Thus all endpoint words, both mixed signs and their actual single-cover factors are retained. The same Čech reduction leaves all these supported endpoint terms unchanged, since the contraction acts only on the two constant V copies and their overlap. They have no nearby term. At a pole \(p\), the full lowest stalk group and specialization map are exactly
\[
\ker d_0\oplus(A_O\otimes E_p)\oplus(E_p\otimes A_O)\oplus(E_p\otimes E_p)
\longrightarrow V,\qquad(z,\xi,\eta,\epsilon)\longmapsto z.
\tag{FST6.3}
\]
Finite dimensionality of \(E_p\) identifies the two mixed kernels with the displayed finite direct sums of \(A_O\). Thus the full specialization domain retains these additional kernels; its image and cokernel are unchanged from FST3. Their highest new degree is minus one, with zero differential into \(M\), so they do not alter the supported top quotient in (FST5.2).

## FST7. What the fixed-base calculation proves

The same-base tensor square now has a constructed global model, the true single-sphere angular factor \(n\), all supported terms and endpoints, and its actual invariant-cycle source. It is not an independently chosen extension. Its first specialization obstruction is (FST3.2), and it vanishes exactly when the original actual boundary vanishes. The tensor detector in the later supported degree has the different fate (FST4.2): it is already a boundary on the original coefficient source, with its quotient-lifting ambiguity retained. The exact completed supported receiver is (FST5.2).

Thus obtaining the fixed geometric \(+2\) on one sphere does not permit applying Deligne's pole argument to the vanished top detector as if that detector were a surviving eigenclass. The map, its degree and its source quotient must be carried together. The calculation has done that for the actual square. TWC10 retains the original tensor Weil pairing on its specified source; no descent of that pairing to the different quotient in FST3.2 is asserted here. It supplies concrete same-base maps beyond TWC's external-product comparison without declaring the original \(b_r\), its first specialization source, or its full derived connecting class zero.

Reading and provenance: the frozen TWC proof and independent TRC calculation; ADM's full source/domain construction; ACD6–8's actual sphere, finite-sheet unit/trace and full endpoint comparison; DCA's distinct raw-cut correction and angular conventions; and DP3–DP6's reconstruction of Deligne's fixed-curve tensor-power argument. The human origins remain Connes–Consani, [arXiv:0903.2024v3 §5](https://arxiv.org/abs/0903.2024v3), and Deligne, [La conjecture de Weil. II](https://numdam.org/item/PMIHES_1980__52__137_0/), with the previously recorded author-source versus transcription distinctions. No new whole-human-paper reading is claimed. The new same-base square is a programme derivation.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.


# Independent calculation of the actual rapid tensor receiver

Proof locators TRC0–TRC6. This note records the independent mathematical subtask assigned by the tensor-weight derivation task. It changes no global manuscript or workflow file. Reading coverage: ACTUAL_DEFECT_MULTIPLIER_DOMAIN.md, ADM1–ADM3; POSITIVE_SOURCE_COMPLETION_AND_SPECIALIZATION.md, CPS0–CPS4. The existing source-reading and user-input records remain in the parent task's durable logbook space. No new human-source reading is claimed.

## TRC0. Retained objects

Fix an integer \(k\ge1\), a recovered coefficient parameter \(r>1\), and the actual distinct off-line nontrivial-zero set \(I=\mathscr Z_O\). Keep the original multiplicities \(m_\rho\), \(w_\rho=1+|\Im\rho|\), and reflection \(\rho^\#=1-\overline\rho\). Put
\[
E=H_{\infty,O},\qquad p_N(x)^2=\sum_{\rho\in I}m_\rho w_\rho^{2N}|x_\rho|^2.
\]
The actual source is \(R=Q/N_O\) with its existing Fréchet quotient topology. Write \(\beta_r:R\to E\) for ADM3.4's injective continuous map. For any entire representative \(F\) of a source class,
\[
(\beta_r[F])_\rho=\delta_r(\rho)F(\rho^\#),\qquad
\delta_r(\rho)=\overline{d_r(\rho)}
=e^{i\Im\rho\log r}\bigl(r^{\Re\rho}-r^{1-\Re\rho}\bigr).
\tag{TRC0.1}
\]
Every \(\delta_r(\rho)\) on \(I\) is nonzero. ADM3.5 proves that \(\beta_r(R)\) contains every finitely supported vector. ADM3.2 retains the established finite constant
\[
C_4^2=\sum_{\rho\in\mathscr Z}m_\rho w_\rho^{-4}<\infty.
\tag{TRC0.2}
\]
The source topology is not replaced by a topology transported from \(E\).

## TRC1. The rapid tensor sequence space

For \(\boldsymbol\rho=(\rho_1,\ldots,\rho_k)\in I^k\), retain
\[
m_{\boldsymbol\rho}=\prod_{j=1}^k m_{\rho_j},\qquad
W_{\boldsymbol\rho}=\prod_{j=1}^k w_{\rho_j}.
\]
Define
\[
H_N^{(k)}=\left\{y:\ P_N(y)^2=
\sum_{\boldsymbol\rho\in I^k}m_{\boldsymbol\rho}
W_{\boldsymbol\rho}^{2N}|y_{\boldsymbol\rho}|^2<\infty\right\},
\qquad H_\infty^{(k)}=\bigcap_{N\ge0}H_N^{(k)}.
\tag{TRC1.1}
\]
Its topology is given by the increasing norms \(P_N\). It is exactly the topology given by all mixed exponents \((N_1,\ldots,N_k)\): each mixed norm is at most \(P_{\max_jN_j}\), and every \(P_N\) is one of the mixed norms. Thus the product weights in (TRC1.1) retain rapid decay separately in every coordinate.

Each \(H_N^{(k)}\) is a complete weighted Hilbert space. A sequence Cauchy in every \(P_N\) has a limit in each \(H_N^{(k)}\). Continuity of each coordinate evaluation identifies these limits as the same coordinate family, which belongs to all the spaces. This proves completeness of \(H_\infty^{(k)}\).

Let \(P_T^{[k]}\) retain exactly the tuples with \(|\Im\rho_j|\le T\) for every \(j\). Its range is finite dimensional. If a tuple is outside this range, at least one factor in \(W_{\boldsymbol\rho}\) exceeds \(1+T\). Hence
\[
P_N\bigl((1-P_T^{[k]})y\bigr)
\le (1+T)^{-1}P_{N+1}(y).
\tag{TRC1.2}
\]
The finite coordinate truncations converge in every norm, uniformly on bounded sets. In particular finite coordinate vectors are dense. This also proves compactness of each inclusion \(H_{N+1}^{(k)}\to H_N^{(k)}\), and the usual finite-projection/tail argument proves that bounded subsets of \(H_\infty^{(k)}\) have compact closure.

## TRC2. Completed projective tensor identification of the receiver

There is a canonical topological isomorphism
\[
J_k:E\widehat\otimes_\pi\cdots\widehat\otimes_\pi E
\longrightarrow H_\infty^{(k)},\qquad
J_k(x_1\otimes\cdots\otimes x_k)_{\boldsymbol\rho}
=\prod_{j=1}^k(x_j)_{\rho_j}.
\tag{TRC2.1}
\]
Here the left side means the Hausdorff completion of the algebraic \(k\)-fold projective tensor product. The result follows from an explicit inverse, without assuming a nuclear-space theorem.

Let \(\pi_N\) be the projective tensor seminorm induced by \(p_N\) in every factor. These seminorms are cofinal among projective tensor seminorms: each continuous seminorm of \(E\) is bounded by a constant times some increasing \(p_N\). On a decomposable tensor the nonnegative series factor exactly, giving
\[
P_N(J_k(x_1\otimes\cdots\otimes x_k))
=\prod_{j=1}^k p_N(x_j).
\tag{TRC2.2}
\]
Triangle inequalities followed by the defining infimum yield \(P_N(J_ku)\le\pi_N(u)\). Thus \(J_k\) extends to the completion.

Let \(e_\rho\) be the coordinate vector of value one at \(\rho\), with no rescaling; thus \(p_N(e_\rho)=\sqrt{m_\rho}w_\rho^N\). Define the proposed inverse by its full coordinate series
\[
\Psi_k(y)=\sum_{\boldsymbol\rho\in I^k}
y_{\boldsymbol\rho}
e_{\rho_1}\otimes\cdots\otimes e_{\rho_k}.
\tag{TRC2.3}
\]
Set \(S_O=\sum_{\rho\in I}w_\rho^{-4}\le C_4^2\), since every multiplicity is a positive integer. Cauchy–Schwarz gives, for every finite set \(A\subset I^k\),
\[
\begin{aligned}
\pi_N\!\left(\sum_{\boldsymbol\rho\in A}
y_{\boldsymbol\rho}e_{\rho_1}\otimes\cdots\otimes e_{\rho_k}\right)
&\le\sum_{\boldsymbol\rho\in A}|y_{\boldsymbol\rho}|
\prod_{j=1}^k\sqrt{m_{\rho_j}}w_{\rho_j}^N\\
&\le P_{N+2}(1_Ay)
\left(\sum_{\boldsymbol\rho\in A}\prod_{j=1}^kw_{\rho_j}^{-4}\right)^{1/2}\\
&\le S_O^{k/2}P_{N+2}(1_Ay).
\end{aligned}
\tag{TRC2.4}
\]
Consequently the series is absolutely Cauchy in each projective seminorm, has a limit in the completed tensor product, and satisfies
\(\pi_N(\Psi_ky)\le S_O^{k/2}P_{N+2}(y)\). It defines a continuous map.

Coordinate truncations prove \(J_k\Psi_k=1\). For a decomposable tensor, \(P_Tx_j\to x_j\) in every \(p_N\). Expand the difference of the products into its \(k\) terms, one factor difference at a time, and apply \(\pi_N\); the approximating factors stay bounded and the difference factor tends to zero. It follows that \(P_Tx_1\otimes\cdots\otimes P_Tx_k\to x_1\otimes\cdots\otimes x_k\). These are exactly the finite series defining \(\Psi_kJ_k\) on that tensor. Therefore \(\Psi_kJ_k=1\) on decomposable tensors, then on the algebraic tensor product, and then on its completion by continuity and density. This proves (TRC2.1). It proves no injectivity assertion for a tensor product formed from the different source \(R\).

## TRC3. The actual source tensor map

The continuous \(k\)-linear map
\[
(F_1,\ldots,F_k)\longmapsto
\left(\prod_{j=1}^k\delta_r(\rho_j)F_j(\rho_j^\#)\right)_{\boldsymbol\rho}
\]
induces a unique continuous linear map
\[
\beta_r^{[k]}:R\widehat\otimes_\pi\cdots\widehat\otimes_\pi R
\longrightarrow H_\infty^{(k)}.
\tag{TRC3.1}
\]
For each \(N\), continuity of the original \(\beta_r\) gives an original continuous source seminorm \(s_N\) and a finite constant \(C_N\) such that \(p_N(\beta_rF)\le C_Ns_N(F)\). Equation (TRC2.2) then bounds the displayed multilinear map by \(C_N^k\prod_js_N(F_j)\). The projective universal property gives a continuous map on the algebraic tensor product, and completeness of the target gives (TRC3.1). This argument retains the original source topology throughout.

For a tuple \(\boldsymbol\rho\), choose \(F_j\in R\) with \(\beta_rF_j=e_{\rho_j}\), using ADM3.5. The image of \(F_1\otimes\cdots\otimes F_k\) is the coordinate vector at that tuple. All finitely supported target vectors therefore occur in the image. TRC1 proves
\[
\overline{\operatorname{im}\beta_r^{[k]}}^{\,H_\infty^{(k)}}=H_\infty^{(k)}.
\tag{TRC3.2}
\]
Neither surjectivity nor injectivity of (TRC3.1) follows from this density assertion.

If \(\beta_r\ne0\), choose \(F\in R\) and \(\rho\in I\) with \((\beta_rF)_\rho\ne0\). Coordinate evaluation after \(\beta_r\) is a continuous linear functional \(\ell_\rho\) on the original source. The functional \((F_1,\ldots,F_k)\mapsto\prod_j\ell_\rho(F_j)\) extends continuously to its completed projective tensor product. Its value on the canonical tensor \(F\otimes\cdots\otimes F\) is \(\ell_\rho(F)^k\ne0\); hence that tensor survives completion. At \((\rho,\ldots,\rho)\), its image under \(\beta_r^{[k]}\) has exactly the same nonzero value. Thus
\[
\beta_r\ne0\ \Longrightarrow\ \beta_r^{[k]}\ne0
\quad\hbox{for every integer }k\ge1.
\tag{TRC3.3}
\]
This proof does not presume injectivity of any completed tensor map. If \(I\) is empty, \(E=0\), \(R=0\) by ADM3.4, and every displayed positive-order tensor receiver is zero.

## TRC4. Exact integer-cover covariance

Keep the genuine integer coefficient action \(T_n[F]=[n^sF]\). Its induced action on \(R\) is continuous, since \(N_O\) is invariant. Define
\[
U_n=T_n\widehat\otimes_\pi\cdots\widehat\otimes_\pi T_n,
\qquad
(V_ny)_{\boldsymbol\rho}=n^{\sum_{j=1}^k\rho_j^\#}y_{\boldsymbol\rho}.
\tag{TRC4.1}
\]
As \(0<\Re\rho_j^\#<1\), \(P_N(V_ny)\le n^kP_N(y)\) for integers \(n\ge1\). Its inverse is the similarly continuous diagonal coefficient operator with \(n^{-\sum_j\rho_j^\#}\). ADM3.6 in each factor proves on decomposable tensors, and then by continuity on the completion,
\[
\beta_r^{[k]}U_n=V_n\beta_r^{[k]}.
\tag{TRC4.2}
\]
The same calculation for general positive coefficient parameter \(a\) is valid; it does not describe a noninteger geometric cover.

## TRC5. Finite blocks and reflection-paired tensors

For any actual \(\lambda\in I\), let \(v_\lambda\in R\) be the class of the original full-jet isolator with value one at \(\lambda\) and zero values at every other actual zero. Then
\[
T_nv_\lambda=n^\lambda v_\lambda,\qquad
\beta_rv_\lambda=\delta_r(\lambda^\#)e_{\lambda^\#}.
\tag{TRC5.1}
\]
The first equality is exact in \(R\), since its difference has zero off-line values; all higher-jet information is retained in the known kernel \(N_O\), rather than discarded from \(Q\). For every finite tuple of actual off-line zeros,
\[
U_n(v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k})
=n^{\lambda_1+\cdots+\lambda_k}
v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k},
\]
\[
\beta_r^{[k]}(v_{\lambda_1}\otimes\cdots\otimes v_{\lambda_k})
=\left(\prod_{j=1}^k\delta_r(\lambda_j^\#)\right)
e_{(\lambda_1^\#,\ldots,\lambda_k^\#)}.
\tag{TRC5.2}
\]
The image coefficient is nonzero. Its target cover eigenvalue is exactly \(n^{\lambda_1+\cdots+\lambda_k}\), the same as its source eigenvalue. This applies also when different tuples have the same sum. Hence no source/target spectral separation is created on any such block.

Write \(\lambda=x+i\gamma\). A repeated tensor has exact eigenvalue and absolute value
\[
v_\lambda^{\otimes k}:\qquad n^{kx+ik\gamma},\qquad n^{kx}.
\tag{TRC5.3}
\]
The reflection-paired tensor uses \(\lambda^\#=1-x+i\gamma\), so
\[
v_\lambda\otimes v_{\lambda^\#}:\qquad
n^{1+2i\gamma},\qquad n.
\tag{TRC5.4}
\]
Its nonzero receiver coefficient is retained in full:
\[
\delta_r(\lambda^\#)\delta_r(\lambda)
=-e^{2i\gamma\log r}\bigl(r^x-r^{1-x}\bigr)^2.
\tag{TRC5.5}
\]
The minus sign and phase have not disappeared. For \(2j\) factors consisting of \(j\) copies of this pair, the eigenvalue is \(n^{j+2ij\gamma}\), its absolute value is \(n^j\), and its nonzero receiver coefficient is the \(j\)-th power of (TRC5.5).

Thus reflection-paired tensors have total real part \(k/2\) for even \(k\), even when every factor is off-line. Their existence, for an actual off-line zero, is compatible with the repeated tensor having total real part \(kx\ne k/2\). If the word weight is used with the convention \(|\alpha_n|=n^{w/2}\), these displayed values correspond respectively to \(w=2kx\) and \(w=k\); these are calculations of absolute values, not a proof of a geometric purity structure on the source.

## TRC6. Transfer factor caveat

The tensor product of the \(k\) original coefficient-transfer operators is exactly
\[
(nT_{1/n})^{\otimes k}=n^k(T_{1/n})^{\otimes k}.
\tag{TRC6.1}
\]
An identification of this tensor operation with a particular geometric transfer must retain the degree of that particular map. The product of \(k\) degree-\(n\) covers has degree \(n^k\). A degree-\(n\) map on one base carrying a tensor coefficient system has degree \(n\); its transfer is not justified by merely copying (TRC6.1). The finite-block matching in TRC5 uses only the specified genuine integer action \((T_n)^{\otimes k}\) and is independent of choosing either geometric interpretation. No new source metric, RH assumption, source tensor injectivity, or unproved purity assertion enters any of TRC0–TRC6.


## Publication source and dependency links

The source geometry is Alain Connes and Caterina Consani, *Schemes over F1 and zeta functions*, [arXiv:0903.2024v3, §5](https://arxiv.org/abs/0903.2024v3). The weight-control comparison is Pierre Deligne, *La conjecture de Weil. II*, Publications mathematiques de l'IHES52 (1980),137-252, [§§3.3.11 and3.6](https://www.numdam.org/item/PMIHES_1980__52__137_0/). Deligne material was read through the identified French transcription and separately recorded peer source-page checks, not Deligne-authored TeX. These sources are not asserted to contain the new programme derivations. The [preceding complete proof and reading record](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/36a82ecca98addb8a98b48204e349737856c7223/workbenches/splitzero-tandem/continuations/20260924-cohomology-weight-and-character-lifts/BUILD_AND_REVIEW.md) records inherited source versions and actual inspection limits. The investigator's corrected construction remains attributed in the original text above.
