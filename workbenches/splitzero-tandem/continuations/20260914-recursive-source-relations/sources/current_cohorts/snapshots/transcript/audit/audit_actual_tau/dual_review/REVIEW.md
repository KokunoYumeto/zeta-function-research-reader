# Independent review of the complete reversed support dual

Date: 2026-09-13. Assignment: review the entire `FULL_SUPPORT_DUAL.md` against the full retained Tau Base source, focusing on signs, the complete opposite support diagram, bottom reconstruction, strict sections, projective roofs, actions and continuous duals. Do not edit the source. Parent owns incorporation. The task's exact user inputs and durable workflow are retained in `work/tau_f1_transcript_audit_20260913/USER_INPUTS.md` and its sibling goal and logbook; this bounded review adds no new user instructions.

## Reading and provenance

Read completely:

- Reviewed proof `FULL_SUPPORT_DUAL.md`, SHA-256 `57ce1600010ecf1f51365710a693a4b8f85f49ca104b0dc6b1f61187b6aceb5a` at the reviewed revision.
- `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Base_Cohomology_2026-09-12/NOTE.md`, source SHA-256 `d03e71ad18f187bd89880cb8ca6fc9c5d6f260b3de8e8e5702c27db97e7b63c3`.
- `output/tau_f1_transcript_audit_2026-09-13/sources/turns/A1694.md`, SHA-256 `a87bff4960c0a1742734e9e711780e0533ea76ba6f46ceab1fea115a2fd66f18`.
- `output/split_zero_rh_tandem_2026-09-12/sources/Tau_Global_Comparison_2026-09-12/NOTE.tex`, SHA-256 `50284fcebae0dc859ac398a00839a29e15be60c008e02314ac1f35c31950ed01`.
- `output/split_zero_rh_tandem_2026-09-12/current_source_20260913_deligne/tex/support_diagrams.tex`, SHA-256 `7586ac17247456a55bdacfcf8b46c196c29eafd3b57846a71792e918704e069b`.

Independent child `roof_check` separately verified Sections 5–6 and derived the Ext calculation below. No original source was edited, no Lean process was started, and no remote operation was performed.

## Findings requiring author attention

There is no identified mathematical sign, exactness, cohomology, reconstruction, or naturality error in the reviewed proof. Two concrete exposition repairs are needed:

1. The standalone deliverable must include the actual global retraction proof or bundle and pin the complete Tau Global Comparison note above. The original Tau Base note alone does not construct the continuous map used in Sections 3, 5 and 7. The later proof has now been read completely and validates that dependency. Its estimates retain the factor \((1-\|A_\alpha B_\beta\|)^{-1}\), with the original cutoffs retained.
2. Repair the many bare parenthesized LaTeX fragments to actual inline math, including malformed one-sided endings such as `(a\Lambda\)`. This is a rendering defect, not a mathematical objection.

Specify explicitly that each projective \(P_v(C)\) in the roof carries the pointwise action \(c\mapsto a^{w-1}cU_a\). Add the exact strengthening below if desired; it computes the derived scope of the already displayed defect.

## Verified cochain and support data

Put \(b=J_0\), \(x=+\), \(y=-\), \(t=\varnothing\) in the reversed diamond. The active degree-minus-one stalks are \(\mathscr B^\vee\). The differentials are
\[
\delta_b\ell=(\ell\Theta,-\ell\Theta\mathcal F),\qquad
\delta_x\ell=\ell\Theta,\qquad
\delta_y\ell=-\ell\Theta\mathcal F.
\]
The arrows from \(b\) to the two leaves are identity in degree minus one and the two coordinate projections in degree zero; all target stalks at \(t\) are zero. Thus every arrow commutes with these differentials, and the two composites to \(t\) agree.

The isomorphism of \(H^{-1}\) with \(Q^\vee\) is precomposition with \(q\), with inverse \(\ell\mapsto([F]\mapsto\ell(F))\). The two leaf degree-zero cokernels vanish using the actual lifts \(a\Lambda\) and \(-b\mathcal F^{-1}\Lambda\). At the joint stalk the quotient map is \(\pi_0(a,b)=a\mathcal F+b\), whose inverse on the quotient is represented by \((0,c)\); subtracting this representative leaves \(\delta_b(a\Lambda)\). These give the stated whole cohomology diagram without losing its joint degree-zero class.

The nonzero functional example is valid. For
\[
\phi_*(x)=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},
\]
integration of \(\partial_x(x^3e^{-\pi x^2})\) gives
\(\int x^4e^{-\pi x^2}dx=(3/(2\pi))\int x^2e^{-\pi x^2}dx\). Thus both moments vanish, while \(\phi_*(1)=2\pi(2\pi-3)e^{-\pi}\ne0\).

In the opposite support semilattice the join is original intersection and the bottom is \(J_0\). The reconstruction with a nonzero bottom fibre therefore has global zero \((J_0,0)\), with \(e(J_0,v)=(J_0,0)\) even for nonzero \(v\). This is allowed by the full reconstruction theorem and does not violate the semimodule axioms. Adjoining a distinct lower zero fibre and collapsing its zero to \((J_0,0)\) preserves bottom, joins and all fibre maps. The sole extra identification is the two zero vectors; no nonzero bottom vector is removed.

## The roof and the precise derived action defect

Let \(C=V^\vee\), \(N=Q^\vee\), let \(H\) have stalk \(N\) at \(b,x,y\), zero at \(t\), and identity arrows between active stalks. Let \(Z_C\) have stalk \(C\) at \(b\) only. For each vertex \(v\), the covariant projective diagram \(P_v(C)\) has value \(C\) at \(w\ge v\) and zero elsewhere. Evaluation proves
\(\operatorname{Hom}(P_v(C),X)=\operatorname{Hom}_E(C,X_v)\), an exact functor over the field \(E\).

The resolution in degrees \(-2,-1,0\) is
\[
P_t(C)\xrightarrow{(1,-1)}P_x(C)\oplus P_y(C)
\xrightarrow{(1,1)}P_b(C)\xrightarrow{\epsilon}Z_C.
\]
Its stalk sequence is identity followed by augmentation at \(b\), the identity-to-zero resolution at either leaf, and the anti-diagonal/sum sequence \(0\to C\to C^2\to C\to0\) at \(t\). Therefore it is exact at every stalk.

The reviewed lift has degree-zero components \((0,c),0,c,0\) at \(b,x,y,t\). Its only nonzero degree-minus-one generator is
\[
f_y^{-1}(c)=-c\mathcal F^{-1}\Lambda.
\]
The decisive chain equation is
\[
\delta_y f_y^{-1}(c)
=c\mathcal F^{-1}\Lambda\Theta\mathcal F=c.
\]
All equations at \(t\) have zero target. The projective-source construction proves support naturality, and \(\pi f=\epsilon\). These verify the roof and the combined quasi-isomorphism stated in the proof.

For scaling, equip the resolution projectives with the pointwise action
\[
T_a^C(c)=a^{w-1}cU_a.
\]
Then \(g_a=T_a^D f-fT_a^{\mathcal R}\) has degree zero equal to zero, is zero on the plus degree-minus-one generator, and on the minus generator equals
\[
g_{a,y}^{-1}(c)
=a^w c\mathcal F^{-1}
(U_{1/a}\Lambda-\Lambda U_{1/a})
=q^\vee d_a(c).
\]
The sign follows by subtracting
\(-a^{w-1}cU_a\mathcal F^{-1}\Lambda\) from
\(-a^wc\mathcal F^{-1}\Lambda U_{1/a}\), and using
\(U_a\mathcal F^{-1}=a\mathcal F^{-1}U_{1/a}\). Precomposition with \(\Theta\) is zero by \(\Lambda\Theta=1\), so the factorization through \(q\) is exact.

Applying \(\operatorname{Hom}(-,H)\) to the projective resolution gives
\[
\operatorname{Hom}(C,N)\xrightarrow{h\mapsto(h,h)}
\operatorname{Hom}(C,N)^2\longrightarrow0.
\]
Consequently
\[
\operatorname{Ext}^1(Z_C,H)
=\operatorname{Hom}(C,N)^2/\operatorname{diag}
\xrightarrow{\sim}\operatorname{Hom}(C,N),
\qquad[(u,v)]\mapsto v-u.
\]
The inverse sends \(d\) to \([(0,d)]\). The computed action difference has exactly the class \([(0,d_a)]\), hence the class \(d_a\).

For a direct nullhomotopy check, a degree-minus-one homotopy \(k:\mathcal R\to D\) can have only \(k^0:P_b(C)\to D^{-1}\). Naturality forces its active components to be the same map \(\ell:C\to\mathscr B^\vee\). The degree-zero equation \(0=\delta k^0\) forces \(\ell\Theta=0\). The degree-minus-one equations then require
\((\ell,\ell)=(0,q^\vee d_a)\), which forces \(d_a=0\). Conversely, \(d_a=0\) makes the actual difference map zero. Thus this chosen section's equivariance in the derived category is characterized exactly by its computed \(d_a\); this calculation makes no claim about all possible choices of section.

The defect has a further exact morphism to the original global theta cocycle. For the actual continuous section \(s:Q\to\mathscr B\), put \(k_b=\Lambda U_b s\). The identity
\(F=\Theta\Lambda F+s qF\) gives
\[
\Lambda U_bF=U_b\Lambda F+k_bqF,
\qquad U_b\Lambda-\Lambda U_b=-k_bq.
\]
Therefore
\[
\boxed{d_a(c)=-a^wc\mathcal F^{-1}k_{1/a}.}
\]
This is a transpose of the actual global cocycle, with its minus sign, reciprocal scaling parameter, Fourier inverse and weight factor all retained.

## Continuous-dual topology

For scalar target \(W=E\), the topological splitting yields an explicit isomorphism, not an appeal to exactness of arbitrary locally convex duals:
\[
\mathscr B'_b\longrightarrow V'_b\oplus Q'_b,
\qquad \ell\longmapsto(\ell\Theta,\ell s),
\]
\[
(\alpha,\lambda)\longmapsto\alpha\Lambda+\lambda q.
\]
The two composites are identities because \(\Lambda\Theta=1\), \(qs=1\), \(\Lambda s=0\), \(q\Theta=0\), and \(\Theta\Lambda+sq=1\). For a continuous linear map \(T:X\to Y\), a bounded subset \(B\subset X\) maps to a bounded subset \(T(B)\subset Y\), and
\(p_B(T'\ell)=p_{T(B)}(\ell)\). Thus its transpose is continuous for the strong topologies. This proves continuity of both displayed inverses and every fixed dual transport used in the proof.

In particular, \(q'\) identifies \(Q'_b\) topologically with the annihilator of \(\Theta V\), with inverse \(\ell\mapsto\ell s\). At the joint degree-zero cokernel the continuous maps \(\pi_0\) and \(c\mapsto[(0,c)]\) are inverse; the relation subspace is the closed kernel of \(\pi_0\). The leaf differentials have the displayed continuous right inverses, so their cokernels really vanish in this topology.

For completeness, each Mellin derivative used by the finite residue map is continuous on the stated \(\mathscr B\). If \(r=\Re\rho\), \(n>|r|\) is an integer, and \(j\ge0\), splitting the integral at one gives
\[
|\mathcal MF^{(j)}(\rho)|
\le j!\left(
\frac{p_{n,0}(F)}{(n-r)^{j+1}}
+\frac{p_{-n,0}(F)}{(n+r)^{j+1}}
\right).
\]
Indeed the two integrals are
\(\int_1^\infty x^{r-n}(\log x)^j\,dx/x=j!/(n-r)^{j+1}\)
and
\(\int_0^1x^{r+n}|\log x|^j\,dx/x=j!/(n+r)^{j+1}\).
The whole finite jet map is continuous, and it descends by the quotient topology because it annihilates \(\Theta V\). Its transpose and the finite residue pairing therefore give the claimed continuous injection into \(Q'_b\). No nilpotent jet is discarded by this estimate.

The algebraic derived-category roof remains an algebraic statement. The continuous maps above verify the topologies of its coefficients and the cohomology transports; they do not invent a derived category of all locally convex spaces.

## Completion status

All findings and exact formulas were sent to the parent. The review did not change its proof source. The two authoring repairs, the precise projective action, and the Ext/cocycle strengthening are available for incorporation. No theta weight bound or vanishing of the global action cocycle has been inferred from this calculation.

The parent then requested a standalone retraction supplement. It has been written at audit_actual_tau/RETRACTION_PROOF.md, using an explicit smooth even cutoff with support radius \(1/4\) and plateau radius \(1/8\). Its Hilbert–Schmidt estimate proves \(\|T\|\le1/2\), giving inverse bound \(2\); all exterior derivative, Schwartz and moment estimates are included. The independent child has read the entire supplement and verified all constants, domains, quotient inverse identities and the final defect sign. Its suggestion to supply the cocycle identity explicitly was incorporated. Thus the standalone retraction dependency gap is resolved by an actual proof file rather than an additional assumption.
