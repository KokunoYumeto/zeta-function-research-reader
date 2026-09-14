# Complete single-primary proof read and backward-propagation receipt

Reader: single_primary_dependency_audit, 2026-09-13.

The complete 1,162-line source and the complete SINGLE_PRIMARY_HANDOFF.md were read. The bounded reread of source lines 471–705 recovered the only interval omitted by the first tool output, so this receipt records a complete body read, not a search-only review.

Source: workspace:/work/rh_counterfactual_20260913/total_object/single_primary_boundary_control.tex.

Verified SHA256: 80dcbc843df223a8b65fd92f728deba1b28e540c748e08dabbdf47a6f28958ea.

This receipt does not edit that source, the sealed handoff, any historical calculation, or any cumulative manuscript. The parent owns the actual backward patches. No substantive error was found in the stated complex or finite-field calculation. The finite-field claims are explicitly about a specified coefficient specialization; the proof does not construct such a specialization for every prime.

## 1. Scope that every replacement must carry

The complex calculation fixes a selected actual nontrivial zero rho of g=2 xi and its complete order m, with

\[
n=m+1,\quad h(s)=(s-\rho)^m,\quad t=0,\quad
\Phi_h(s)=\frac{(s-\rho)^n-(-\rho)^n}{n}
=\frac{y^n}{n}+c,\quad y=s-\rho,\quad c=-\frac{(-\rho)^n}{n}.
\]

The original coordinate is s, with ascending monomial basis, and Phi_h(0)=0. The displayed translation is an exact coordinate map with its inverse and constant; it does not authorize replacing Phi_h by y^n/n. For an actual nontrivial complex zero, rho and hence c are nonzero. The source explicitly handles c=0 after finite-field specialization.

Locators: SP.1–5, lines 13–76; SPF.1–5, lines 656–720.

The complex connection and all period statements concern this complete single-primary packet at t=0. They do not compute distinct-critical-value Stokes matrices, variation in nonzero t, or an arbitrary mixed tensor invariant space. The coefficient-space labels remain the original labels at every nonbottom support object; represented zero stays represented zero at that object. The calculation does not send the marked fibre to external absence. Locators: lines 623–647.

The finite-field section retains a coefficient ring R containing rho, 1/n!, and the entire original Taylor class j_h(g/h) and its inverse. Its input is a specified homomorphism alpha:R -> F_(Q0), of characteristic p>n. All coefficients use that same map. It then uses only the explicit constant extension

\[
k=\mathbf F_Q,\qquad Q=Q_0^d,\qquad
d=\operatorname{ord}_{(\mathbf Z/n\mathbf Z)^\times}(Q_0),
\]

so n divides Q−1, and coefficients are still mapped by the composite of alpha with this constant extension. It fixes ell different from p, geometric Frobenius, a nontrivial additive character on F_(Q0), and its trace pullbacks. A later patch must not silently replace p>n by a different prime condition, invent a map alpha, or identify this ell-adic coefficient field with the finite residue field. Locators: SPF.1–4, lines 656–705.

## 2. Exact connection and full periods replace a determinant-only subcase

The Pascal matrix from original s coefficients to y coefficients is

\[
P_{ab}=\binom ba\rho^{b-a}\quad(a\le b),\qquad
(P^{-1})_{ab}=\binom ba(-\rho)^{b-a},\qquad
e_s=e_yP,\qquad \det P=1.
\]

The inverse follows by composing the two original binomial substitutions. The original differential is

\[
L_u=u\partial_s+(s-\rho)^m.
\]

Its leading-degree term proves both injectivity on C[u,s] and the unique remainder of degree less than m. Therefore the degree-one cohomology is free in the original remainder basis and its u=0 fibre is E_h ds, with the full multiplicity m.

The exact division is

\[
\Phi_h(s)s^b=h(s)\frac{(s-\rho)s^b}{n}+cs^b,\qquad
q_b'=\frac{(b+1)s^b-b\rho s^{b-1}}n.
\]

Subtracting L_u q_b gives the full differential-remainder correction. Consequently

\[
C_s=cI_m,\quad (B_s)_{bb}=\frac{b+1}n,\quad
(B_s)_{b-1,b}=-\frac{b\rho}n,\qquad
\nabla_u=\partial_u-\frac{cI_m}{u^2}+\frac{B_s}u,
\]

with all other B_s entries zero. Its chain lift includes

\[
\nabla_u^1=\partial_u-\Phi_h/u^2,\qquad
\nabla_u^0=\partial_u-\Phi_h/u^2+1/u,\qquad
\nabla_u^1L_u=L_u\nabla_u^0.
\]

The exact diagonal conjugation is

\[
PB_sP^{-1}=\operatorname{diag}(\beta_a),\qquad
\beta_a=(a+1)/n,\qquad \operatorname{Tr}B_s=m/2.
\]

Locators: SP.3–9, lines 34–125.

For the actual ordered oriented contours Gamma_j=−ell_0+ell_j specified by the branch of log u, retain

\[
\zeta=e^{2\pi i/n},\quad
W_{ja}=\zeta^{j(a+1)}-1,\quad
d_a=n^{\beta_a-1}e^{\pi i\beta_a}\Gamma(\beta_a),\quad
D(u)=\operatorname{diag}(d_a u^{\beta_a}).
\]

The complete period matrix is

\[
\Pi_s(u)=e^{c/u}W D(u)P.
\]

The source proves the equality for the original contours, rather than assigning it to translated contours without a map: the endpoint connectors under translation by a rho have length at most |rho| and exponential real part −R^n/(n|u|)+O(R^(n−1))+O(1), uniformly for a in [0,1]; both connector integrals vanish and the two junction paths cancel. Radial substitution then evaluates each oriented ray with the stated Gamma factors and phases.

The full determinant remains

\[
\det\Pi_s
=K_m u^{m/2}e^{mc/u},\qquad
K_m=n^{-m/2}e^{\pi im/2}
\left(\prod_{a=0}^{m-1}\Gamma(\beta_a)\right)\det W\ne0.
\]

Invertibility of W is proved by the degree bound for the polynomial sum a_r(z^r−1), which vanishes at all n roots of unity. The complete period matrix, not merely its determinant, is now available to every earlier calculation whose hypotheses reduce to this exact primary subcase.

Locators: SP.10–15, lines 127–224.

Suggested replacement formula for an earlier statement that only the determinant has been evaluated: insert the displayed Pi_s formula with P, W, d_a and the retained c, and cite the oriented contour proof SP.10–15. Preserve the old determinant result as its exact determinant consequence and its provenance, rather than presenting it as the strongest currently known primary calculation.

## 3. Actual boundary monodromy and the exact marked-fibre bridge

The transported ordered cycles satisfy

\[
\Gamma_j\longmapsto\Gamma_{j+1}-\Gamma_1\quad(1\le j<m),
\qquad \Gamma_m\longmapsto-\Gamma_1.
\]

Hence

\[
M_{\rm cyc}
=W\operatorname{diag}(\zeta,\ldots,\zeta^m)W^{-1},\quad
M_{\rm cyc}^n=I,\quad \ker(M_{\rm cyc}-I)=0.
\]

The horizontal coefficient equation has the exact fundamental matrix

\[
H_s(u)=P^{-1}e^{-c/u}
\operatorname{diag}(u^{-\beta_a}).
\]

Its coefficient monodromy is the inverse-character convention. It also has zero invariants. Both conventions and their directions must remain explicit in an earlier chapter.

On u=v^n, the actual connection is

\[
\partial_v-nc\,v^{-n-1}I_m+
v^{-1}\operatorname{diag}(1,\ldots,m).
\]

The meromorphic change x_y=diag(v^−1,...,v^−m)z removes the displayed integer residues and retains the common irregular scalar with horizontal solution e^(−c/v^n). The remaining exact solution is single-valued, so the finite-cover unipotent logarithm is N_boundary=0. All columns have that same exact exponential; the source proves there are no additional Stokes factors in this one-critical-value subcase by agreement of its explicit solutions on overlapping sectors. This result does not extend without calculation to distinct critical values.

For the ordinary local system, j_* at zero is the invariant space and vanishes. The circle complex [C^m --(M−I)--> C^m] has zero kernel and cokernel, so both local invariant and coinvariant groups vanish. Locators: SP.16–21, lines 226–330.

The marked fibre still has arithmetic multiplication

\[
A_s=P^{-1}(\rho I_m+J_m)P,\qquad
N_{\rm ar}=P^{-1}J_mP,\quad J_m^m=0,\quad J_m^{m-1}\ne0,
\]

where (J_m)_(a+1,a)=1. For m=1 this explicitly means J_1=0 and J_1^0=I_1. The exact relation to the computed boundary is

\[
[B_s,A_s]=N_{\rm ar}/n,\qquad
[\nabla_u,A_s]=N_{\rm ar}/(nu).
\]

With D_0=diag(d_a) and K_0=WD_0J_mD_0^−1W^−1,

\[
\Pi_s A_s\Pi_s^{-1}=\rho I_m+u^{1/n}K_0,\qquad
M_{\rm cyc}K_0M_{\rm cyc}^{-1}=\zeta K_0.
\]

These are exact morphism and commutator formulas between the marked action and its period transport. A backward patch saying that the two nilpotents differ must include these formulas, rather than ending at the difference.

The marked lattice has the exact finite-cover map

\[
e^{-c/v^n}\Pi_s(v^n)
=WD_0\operatorname{diag}(v,v^2,\ldots,v^m)P.
\]

After the displayed constant invertible changes its image is direct sum v^(a+1) C{v}. Its cokernel is direct sum C{v}/(v^(a+1)), of length m(m+1)/2. The image lattice itself has an m-dimensional quotient modulo v, while its inclusion into the ambient constant lattice induces zero modulo v. This is the calculated mechanism relating the retained marked fibre and vanishing local-system invariants, with the irregular scalar still present.

Locators: SP.22–24, lines 332–390; SP.32–33, lines 529–563.

Suggested replacement for an earlier generic “boundary inertia is uncomputed” statement: retain that statement for the general family, but replace its primary t=0 branch with the full M_cyc, H_s, finite-cover connection, N_boundary and lattice map above. Update every downstream use that inferred boundary vanishing erased the marked source: the displayed lattice quotient and nonhorizontal period action calculate exactly what remains.

## 4. The original full Taylor unit and theta maps must travel with the update

Write

\[
v_h=g/(s-\rho)^m,\qquad
a_j=\frac{v_h^{(j)}(\rho)}{j!}
=\frac{g^{(m+j)}(\rho)}{(m+j)!},\quad a_0\ne0.
\]

The original marked unit and its inverse are the complete matrices

\[
U_s=P^{-1}\sum_{j=0}^{m-1}a_jJ_m^jP,\qquad
U_s^{-1}=P^{-1}\sum_{j=0}^{m-1}b_jJ_m^jP,
\]

\[
b_0=a_0^{-1},\qquad
b_r=-a_0^{-1}\sum_{j=1}^r a_jb_{r-j}.
\]

The latter recursion proves the finite series product equals I, since all terms of degree m or greater vanish. None of the Taylor coefficients can be replaced by only a_0.

In the original function spaces, retain D=−x partial_x, Theta phi=2 sum_(r>=1) phi(rx), the original seed

\[
\phi_*=(4\pi^2x^4-6\pi x^2)e^{-\pi x^2},\qquad
\mathcal M\Theta\phi_*=g,\qquad \mathcal MF_h=v_h.
\]

The source square is

\[
\alpha_h(P)=P(D)\phi_*,\quad
\mathcal T_h(P)=P(D)F_h,\quad
\Theta\alpha_h(P)=\mathcal T_h(hP),\quad
J_h\mathcal T_h(P)=U_s[P]_s.
\]

It gives the degree-one map sigma_h U_s:E_h -> Q_ar. The exact source representatives under Pascal translation are

\[
\mathcal T_h(y^b)=(D-\rho)^bF_h,\qquad
(\mathcal T_h(s^b))_b=(\mathcal T_h(y^a))_aP.
\]

At general u the differential on the image of alpha_h is the specified deformation

\[
\Theta+u\mathcal T_h\partial_s\alpha_h^{-1}.
\]

Its chain square with L_u is the comparison to preserve, rather than substituting the undeformed Theta at u≠0.

The entire unit transport has the exact formulas

\[
\Pi_sU_s\Pi_s^{-1}
=\sum_{j=0}^{m-1}a_j u^{j/n}K_0^j,\qquad
[\nabla_u,U_s]
=\frac1{nu}P^{-1}\left(\sum_{j=1}^{m-1}j a_jJ_m^j\right)P.
\]

For v_pol=sum a_j(s−rho)^j, its multiplication on representatives satisfies

\[
v_{\rm pol}L_uQ=L_u(v_{\rm pol}Q)-u v_{\rm pol}'Q.
\]

If v_pol p=hq+r with deg p<m, then its differential remainder is r−u q′; the constant coefficient extension U_s returns r. This exact difference is essential when pushing the improved unit calculation through earlier family/cohomology statements.

Locators: SP.25–31, lines 392–527.

Suggested replacement for an earlier unsupported “multiplication by the full unit is a cohomology endomorphism for all u” assertion: state the actual constant coefficient extension U_s in the specified remainder basis, then include the derivative defect and corrected differential remainder above. At u=0 the multiplication statement is exact. The correction is a concrete calculated term, and must propagate into any connection or metric formula that used the former assertion.

## 5. Original metric, full period comparison, and higher-source kernel

The unchanged source Gram is

\[
(G_\theta)_{ab}
=\frac1{2\pi}\int_{\mathbf R}
\overline{(1/2+it)}^{\,a}(1/2+it)^b
|v_h(1/2+it)|^2\,dt.
\]

Its positive definiteness follows from Mellin–Plancherel for the original L²(dx) source and the nonvanishing of the entire product Pv_h for nonzero P. The complete comparison now reads

\[
T_{\rm per}(u)
=G_\theta^{-1}\Pi_s(u)^*\Pi_s(u)
=e^{2\operatorname{Re}(c/u)}
G_\theta^{-1}P^*D(u)^*W^*WD(u)P.
\]

Its positivity and self-adjointness are in G_theta. The explicit scalar cancels from the ratio of its extreme eigenvalues, but the original G_theta, P, W and all d_a remain in that ratio. A determinant-only estimate must not replace this available matrix; conversely the determinant must not be treated as already controlling the extreme eigenvalue ratio.

For the enlarged original polynomial source C[s]_(<=N), N>=m−1, the exact differential remainder J_(u,N) has

\[
\ker J_{u,N}=L_u(C[s]_{\le N-m}),\qquad
\operatorname{Per}_N=\Pi_sJ_{u,N}.
\]

When N=m−1 the relation space is zero. The relation-period integral vanishes because it is u times the integral of d(e^(Phi_h/u)Q) on the original contours; all ends decay and the common junction contributions cancel. Thus the enlarged period Gram has exact rank m and this full kernel, rather than being positive definite on more than m source columns.

Locators: SP.34–36, lines 565–621.

Suggested replacement for an earlier enlarged-source positive-definiteness statement: use the exact rank/kernel/factorization above, and apply positive definiteness only after the displayed remainder quotient or to its original m-dimensional frame. The metric must still be transported through J_(u,N), rather than assigning a new unrelated norm.

## 6. Finite-field exact decomposition, conductor, and weight

On the specified coefficient specialization and constant extension, the actual sheaf is

\[
\mathcal F=R^1\pi_{s!}\mathcal L_\psi(\Phi_h(s)/u).
\]

The exact source translation T(y,u)=(y+rho,u), with inverse (s−rho,u), gives

\[
T^*\mathcal L_\psi(\Phi_h/u)
=\mathcal L_\psi(y^n/(nu))\otimes\pi_y^*\mathcal L_\psi(c/u).
\]

The power map q:y -> z=y^n has the full sheaf decomposition

\[
q_*\overline{\mathbf Q}_\ell
\simeq\overline{\mathbf Q}_{\ell,\mathbf A^1}
\bigoplus_{\chi^n=1,\ \chi\ne1}j_!\mathcal K_\chi.
\]

The proof includes the ramified zero stalk: only the trivial projector has a nonzero stalk there. Explicit projectors are e_chi=(1/n)sum_zeta lambda_chi(zeta)D_zeta, with image the lambda_chi^−1 deck eigenline and geometric Frobenius trace chi. The trivial summand has zero compact-support cohomology after its nonconstant Artin–Schreier factor; each nontrivial summand has only H_c^1, of dimension one, with geometric Frobenius −G_k(chi,psi).

Locators: SPF.5–17, lines 707–906.

The resulting isomorphism of the actual parameter sheaf is

\[
\mathcal F
\simeq\mathcal L_\psi(c/u)\otimes
\bigoplus_{\chi^n=1,\ \chi\ne1}
\mathcal A_{-\chi(n)G_k(\chi,\psi)}\otimes\mathcal K_\chi(u).
\]

It is a sheaf isomorphism constructed by the power-map projectors, source scaling w=az, compact-support base change and projection formula. The preceding equivalent expression has Kummer factor K_(chi^−1)(1/(nu)); the inversion and constant chi(n) must not be dropped. The Gauss sum is unscaled.

Every extension-field trace retains

\[
-G_{k_r}(\chi_r,\psi_r)=(-G_k(\chi,\psi))^r,
\]

and local eigenvalues

\[
\psi_r(c/u)\,
(-\chi(n)G_k(\chi,\psi))^r\chi_r(u).
\]

Locators: SPF.18–21, lines 908–980.

At u=0, write psi(x)=vartheta(Tr_(k/Fp)(b x)). When c≠0 the explicit Artin–Schreier extension z^p−z=bc/u has degree p, ramification index p, v_E(z)=−1, and

\[
v_E(\sigma_a(z^{-1})-z^{-1})=2.
\]

It has lower ramification groups G_0=G_1=Fp, G_2=1, hence break one. The common nontrivial wild character forces V^(P0)=V^(I0)=0 and Swan_0(F)=m. If c=0, the Artin–Schreier factor is trivial, all the displayed Kummer characters are nontrivial, and V^(I0)=0 with Swan_0(F)=0.

The explicit finite cover is u=v^n followed by z^p−z=bc/v^n. It kills all geometric inertia; c=0 requires only the Kummer cover, while c≠0 gives the degree np composite. The restricted representation has N=0 and its invariants are then all m dimensions. Thus original-inertia invariants 0 and restricted-inertia invariants m refer to the two exact groups and cannot be exchanged.

Locators: SPF.22–27, lines 982–1094.

The source proves |G_k(chi,psi)|²=Q by expanding the unscaled square, substituting x=ty, and using both character orthogonality identities. Therefore every displayed local eigenvalue has absolute value Q^(r/2), proving pointwise weight one and its descent to the original constant field. No half Tate twist or scalar rescaling is used.

Locators: SPF.28–29, lines 1096–1145.

Suggested replacement for “only a general purity bound is available for the primary family”: include this full direct-sum decomposition, exact Frobenius constants, Swan cases and cover, and derive weight one from the exact Gauss square. Preserve the older general purity theorem as a theorem for the larger family. Do not assign these finite-field eigenvalues to original complex arithmetic dilation without the required specific comparison map.

## 7. Audit-derived tensor check: one-factor vanishing cannot propagate unchanged

This paragraph is an elementary consequence proved here from the complete one-factor matrices; the sealed SP source itself only warns about tensor characters. It is included to specify a concrete backward-propagation guard, not to claim this receipt contains the later full mixed-support tensor calculation.

Take the k-fold tensor of this SAME complex local system over the SAME punctured u-disc, so a circuit acts simultaneously on all factors. With a_i in {1,...,m}, its eigencharacters are zeta^(a_1+...+a_k). Therefore its invariant projector in the corresponding marked coefficient frame is

\[
Q_0=(P^{\otimes k})^{-1}
\operatorname{diag}\!\left[
a_1+\cdots+a_k\equiv0\pmod n
\right]P^{\otimes k}.
\]

This is the invariant projector for the marked coefficient monodromy; the horizontal convention inverts all characters and yields the same zero-sum selector. The corresponding period-coordinate projector is obtained by the actual period conjugation, not by identifying the two coefficient frames.

The number of invariant ordered tensor characters is exactly

\[
d_k=\frac1n\sum_{r=0}^{n-1}
\left(\sum_{a=1}^{n-1}\zeta^{ra}\right)^k
=\frac{m^k+m(-1)^k}{m+1}.
\]

The first equality is root-of-unity orthogonality applied to each ordered tuple. The inner sum is m for r=0 and −1 for every r≠0, proving the second. In particular d_1=0 and d_2=m, for every m>=1. The elementary example m=1 has one-factor monodromy −1 and two-factor monodromy +1.

For the top marked monomial y^(m−1) in every factor, the character is zeta^(km); it is invariant exactly when n divides k, since gcd(m,m+1)=1. This statement is about the specified marked coefficient class. Transport to the original theta-image coordinates requires the complete conjugation by U_s^(tensor k), preserving every Taylor coefficient. It is not valid to apply Q_0 directly to a differently framed arithmetic class.

For tensor order r on the specified finite-field diagonal, the source decomposition gives the same exact tensor map

\[
\mathcal F^{\otimes r}
\simeq\mathcal L_\psi(rc/u)\otimes
\bigoplus_{\chi_1,\ldots,\chi_r\ne1,\ \chi_i^n=1}
\mathcal A_{\prod_i[-\chi_i(n)G_k(\chi_i,\psi)]}
\otimes\mathcal K_{\prod_i\chi_i}(u).
\]

This follows by distributing tensor product over the displayed finite sum and using the proved Artin–Schreier and Kummer torsor tensor laws. The symbol G_k here uses the finite field k as in SPF; the tensor order is the integer r.

If the residue scalar rc is nonzero, the same nontrivial common wild character proves zero original-inertia invariants. If rc=0, the invariant summands are exactly the ordered character tuples of product one, with dimension d_r, and their Frobenius eigenvalues are the complete displayed products. In particular for c≠0 and p dividing the tensor order, the common additive character dies and one-factor wild vanishing no longer applies. These formulas follow from SPF.19 and its explicit inertia proofs without any new sheaf comparison assumption.

This calculation is for the diagonal tensor in u. An exterior product over independent u_i has inertia group I_0^k and a different invariant problem. The exact restriction to the diagonal is the morphism that changes that problem.

## 8. Backward update instructions and provenance boundary

The parent should search the live cumulative sources for the six classes of old statements above, then patch only the exact branches to which these source hypotheses apply. Retain the full historical text and hashes as provenance. Preserve general statements still correct for the larger packet family, and add the new single-primary computations where they sharpen an old unspecified or determinant-only subcase.

Every earlier use of one-factor boundary vanishing must be audited through its exact tensor parameter map, original unit map, support label and marked-lattice map. The fully proved primary data now allow explicit calculations instead of a generic promise to compute inertia; they do not justify replacing the entire mixed-support programme by the single-primary calculation.

The supplied handoff independently records a clean compilation, symbolic checks and finite-field trace checks. This reader did not rerun those already passed checks, did not inspect their full raw output, and does not claim to have done so. This receipt's acceptance is based on the complete source proof read, the precise identity checks above, and the verified source hash.
