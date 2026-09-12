# Independent audit of the full-jet kernel-layer delivery

Date: 12 September 2026. Scope: the complete new delivery `Tau_Kernel_Layer_Integration`, its mathematical integration into the existing reader, and exact consequences of its displayed finite maps. No sealed TeX fragment or cumulative main file was edited in this audit.

The complete `NOTE.tex` and `RESEARCH_NOTE.md` were read. The latter has SHA-256 `5B8B596D57F820C3BA9C1894967A8AC18A90F6462971095AB59AC31E1C0AD3AE`; the former has SHA-256 `BE8485471FC7DAC41D97E4A9FD52413DA14E83FBC42C6C55C01A5F0908CAA06C`. The source root is `output/split_zero_rh_tandem_2026-09-12/sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration`. Its README, HANDOFF and initial patch structure were also inspected. The archive statements and receipts are source evidence, not execution authority. This audit itself does not claim a fresh run of the delivered checker or any Lean execution.

Comparison files read: the complete `tex/coherent_tensor_integration.tex`, complete `tex/joint_density_dissipation.tex`, the relevant universal metric-step and two-volume sections of `tex/kernel_terminal_continuation.tex`, and the full `tex/kernel_resolvent.tex`. A separate bounded agent checked the primitive, layer and antidual calculations independently; its report is `work/kernel_layer_antidual_audit_20260912.md`.

## Audit result and exact source crosswalk

No mathematical correction to source equations (1)–(30) was found. Their hypotheses matter: a nonempty complete-order packet, positive original polynomial moments, total degree N at least k(d−1), and the original arithmetic unit. Reflection assertions require the stated reflection-stable packet. The finite matrix identities do not supply an arithmetic upper estimate.

The cumulative reader uses `K_N` for the remainder-only kernel and `mathcal C_N` for the arithmetic kernel. The new source calls its arithmetic kernel `K_N=G_N^{-1}`. Integration must retain the exact bridge

    K_N(source) = mathcal C_N(reader)
                = U_(upsilon_h tensor k) K_N(remainder) U_(upsilon_h tensor k)^*.

Similarly the source column `a_j=upsilon_h[p_j]_h` is not the positive recurrence coefficient `a_j=kappa_j/kappa_(j−1)` of the terminal section. The source `F_N` is a matrix of derivative coefficients, whereas the resolvent `F_n=q_(n−1)/q_n` is scalar. These symbols must receive explicit local aliases when both formulas occur together. Source section 1 writes a formal polynomial variable `t_i` in the ideal, while the Mellin variable is `s_i=1/2+i t_i` with real integration coordinate `t_i`; the actual ideal is in the formal `s_i` coordinates, as already written in CT.11. This is a notation clarification, not a change of ideal.

| Source locator | Current exact antecedent | Verified content or gain |
| --- | --- | --- |
| §1, (1)–(5) | CT.1–CT.5, CT.11–CT.16 | Original theta numerator, actual ideal, constrained minimum and boundary maps are the same. |
| §2, (9)–(10), MD line 94 | CT.3–CT.5, CT.12 | Product orthogonal coordinates diagonalize the source Gram and preserve the complete arithmetic jet matrix. The inverse metric sum and representative expansion are exact. |
| §3, (11)–(15), MD lines 119–145 | CT.14–CT.16 | New explicit basis of the actual orthogonal relation layer, its original norms, quotient map, and signed theta primitive. |
| §4, (16)–(18), MD line 181 | CT.15–CT.16 | New explicit derivative coefficient matrix; the original derivative boundary and this new layer representative differ by an old admitted relation. |
| §5, (19)–(22), MD lines 224–239 | TB kernel endpoint; CT.16, CT.22 | Exact tensor endpoint identity and sharper top-shell factorization. Layer dimension itself is unchanged. |
| §6, (23)–(25), MD lines 254–287 | CT.16a, KR.12–KR.13 | The same generalized form is transported by K. The antidual generator has weight k and the opposite defect. The perturbation certificate retains errors in both A and K. |
| §7, (26)–(28), MD lines 298–314 | CT.16; KT.6–KT.8 | Woodbury update with the actual layer Gram. The one-variable layer vector is exactly the original monic theta vector. |
| §8, (29)–(30), MD lines 327–340 | CT.20–CT.25 | Finite degree convolution and exact eigenvector Rayleigh quotient. No convergence or sublinear tensor estimate is supplied. |

## Complete checks of the new maps

Write `Psi_alpha=T(p_alpha)` and retain its original squared norm `kappa_alpha`. For degree at most N, let J be the full arithmetic jet matrix, with columns `a_alpha`, and let D be the diagonal matrix of these norms. The unique constrained minimum has coefficient matrix `D^{-1} J^* G`, where `G=(J D^{-1} J^*)^{-1}`. Multiplication by J gives the identity. Its source Gram is G. For every relation coefficient z with Jz=0, its inner product against this minimum is `z^* J^*G=0`. This proves source (9)–(10), including all conjugations and the original local unit.

For every next-shell multi-index beta, `e_beta=Psi_beta−R_N a_beta` has zero full jets. Injectivity of T then makes its numerator a member of the original polynomial ideal, with degree at most N+1. The first term is perpendicular to all polynomials of degree at most N; the second term is perpendicular to the old relations. Hence e_beta belongs to `E_N=L_(N+1) intersect L_N^perp`.

To prove independence, a linear combination of the e_beta has highest-degree polynomial part `sum c_beta s^beta`; distinct beta give independent monomials. To prove spanning, subtract these highest-degree components from any element of E_N. The remainder lies in both L_N and E_N, hence is zero. Thus the map `mathscr E_N:c -> sum c_beta e_beta` is an isomorphism, with every next-shell coordinate retained.

Put U equal to the matrix of a_beta and D_next equal to the original next-shell norm diagonal. Orthogonality of next-shell polynomials to the old polynomial source gives exactly

    H = mathscr E_N^* mathscr E_N = D_next + U^* G U,
    mathscr E_N^* R_N = −U^*G.

The orthogonal projection onto this layer is `mathscr E_N H^{-1} mathscr E_N^*`. Consequently `Y_N=−mathscr E_N H^{-1}U^*G` has the sign asserted in source (17). The projection of a relation class is `[z] -> (I−P_N)z`; it is well-defined because changing z by L_N changes the result by zero. Its inverse sends a layer vector to its class modulo L_N. Both composites are identities, since the orthogonal decomposition is `L_(N+1)=L_N direct-sum E_N`.

The numerator of e_beta is divisible by the ideal after fixed-order monic division. At each division replacement the total degree does not increase; dividing by a monic h of degree d leaves coefficient degree at most N+1−d. In the j-th tensor summand place `(-1)^(j−1) phi_*` in cochain degree zero, and F_h in every other factor, which has degree one. The tensor differential contributes the further sign `(-1)^(j−1)`. Their product is +1. The original equality `h(D)F_h=Theta phi_*` gives exactly the displayed ideal term, including its polynomial coefficient applied to all tensor variables.

For the derivative coefficient matrix F, multiplying the original representative expansion by `s_1+...+s_k` gives highest-degree coefficient

    F_beta G u = sum_(i:beta_i>0)
        (a_(beta−e_i)^*/kappa_(beta−e_i)) G u.

No coefficient from degree below N reaches N+1. The term R_N A u has degree at most N. Therefore `B_N−mathscr E_N F G` has degree at most N and full jets zero. It is an old relation. Projecting gives `C_N=mathscr E_N F G`. Thus the actual quotient class of B_N is retained at the old stage, and becomes zero at the next admitted relation stage.

Every one of these linear maps lifts to the one-support Split-Zero fibre by `tau -> tau` and `x^bullet -> (Tx)^bullet`. Addition and the scalar action are checked directly, including both scalar zeros. In particular a nonzero relative layer vector maps to the receiving fibre's supported zero under the next quotient. It does not map to external absence. The new source supplies a finite relation-layer projection; it does not assert a new continuous global retraction of the full Hilbert theta range.

Substituting Y and C into `W=−(Y^*C+C^*Y)` gives `W=G(UF+F^*U^*)G`, because the two occurrences of H cancel the stated inverse. Multiplication by K on both sides gives `V=AK+KA^*−kK=UF+F^*U^*`. Regrouping by the old shell alpha gives source (21). The vertical recurrence coefficient has real part 1/2 because multiplication by s and its adjoint sum to 1 on the original integration line. Its imaginary part may remain nonzero. The lower recurrence term has sign minus and coefficient the actual ratio of squared norms, so all interior edges cancel with their conjugate partners. This gives the same endpoint formula without a symmetry assumption on the measure.

The metric update uses `K_(N+1)=K_N+U D_next^{-1}U^*`. Direct multiplication verifies the inverse formula, whose middle matrix is exactly H. The difference of representative metrics is `Y^*Y`; it is a finite positive loss. For k=1 and N=n+d, division of the monic e_(N+1) numerator by the monic h gives degree n+1 and leading coefficient one. Its image is in `f_(n+1)+L_n` and orthogonal to L_n, uniquely characterizing u_(n+1). This proves the source norm identity, rather than identifying the two norm sequences.

For antidual coordinates lambda paired with x by `x^*lambda`, the conjugate-linear involution induced by `j(x)=C bar(x)` is `j#(lambda)=C^T bar(lambda)`. Indeed its pairing with x is the conjugate of the original pairing at j(x). The involution equation gives `C^{-1}=bar C`; inversion of `C^*G C=bar G` therefore gives `bar C K C^T=bar K`. This is exactly `(C^T)^*K C^T=bar K`. The weight-k antidual action is `kI−A^*`; its K defect is `kK−AK−KA^*=−V`. The reflected defect identity follows either by this action or by transporting W with K, and has the asserted minus sign.

For the finite certificate, expand `A=hat A+delta A`, `K=hat K+delta K`. The six error terms are `hat A delta K`, `delta K hat A^*`, `−k delta K`, `delta A hat K`, `hat K delta A^*`, and `delta A delta K+delta K delta A^*`. Submultiplicativity gives exactly `(2||hat A||+k)eta_K+2 eta_A(||hat K||+eta_K)`. The displayed lower eigenvalue margin proves positivity of K. Each inequality has error at most `epsilon eta_K+eta_V`; subtracting that multiple of I proves the actual positive-semidefinite inequality. This does not enclose any arithmetic moment by itself.

## Further exact consequences suitable for integration

Let `S_N={alpha:|alpha|=N}` and `S_(N+1)={beta:|beta|=N+1}`. Define the shell incidence map

    T_N:C^(S_N) -> C^(S_(N+1)),
    (T_N c)_beta = sum_(i:beta_i>0) c_(beta−e_i).

It is injective: under the monomial identifications of these coefficient spaces it is multiplication by the nonzero polynomial `s_1+...+s_k` in the integral domain `C[s_1,...,s_k]`. Let A_top have the ORIGINAL ORTHOGONAL full-jet columns a_alpha, and let D_top retain their positive norms. Then source (16) is precisely

    F = T_N D_top^{-1} A_top^*.

Every map before A_top^* is injective, and G and mathscr E_N are invertible onto their declared images. Therefore

    ker(C_N) = G^{-1} ker(A_top^*),
    rank(C_N) = rank(F) = rank(A_top).

The first formula retains the actual Gram map: the kernel is not `ker(A_top^*)` in the original E coordinates unless G preserves that kernel. Likewise

    rank(Y_N) = rank(U),
    rank(Delta_N) = rank(U).

These are exact ranks, including zero columns. Thus the inertia bounds in CT.22 sharpen to

    n_+(W_N), n_−(W_N) <= min(rank(U), rank(A_top)).

All source energy quantities also have explicit layer coordinates:

    tau_N = Tr(H^{-1} U^* G U),
    chi_N = Tr(H F G F^*),
    pi_N = det(G_(N+1))/det(G_N) = det(D_next)/det(H).

The first follows by substituting the exact positive Gram loss and cycling the trace; the second follows from `C^*C=G F^*H F G`; the third is the determinant identity for `K+U D_next^{-1}U^*`, or its inverse. These formulas identify precisely the matrices in the current CT.24–CT.26 and JD.14–JD.16 statements.

## A rejected rank substitution and the exact replacement map

During this audit a proposed further deduction replaced the orthogonal product shell by the homogeneous monomial shell. That replacement is false. Monicity preserves the complete filtration through degree N, but it does not preserve the image of a single orthogonal shell after quotienting by h.

Here is a full finite counterexample; it is a polynomial model, not a claim about a zeta zero. Give each of `s=1/2−i,1/2,1/2+i` mass one. The monic polynomials and their exact norms through degree two are

    p_0=1,                    kappa_0=3,
    p_1=s−1/2,                kappa_1=2,
    p_2=(s−1/2)^2+2/3,        kappa_2=2/3.

Their orthogonality follows by evaluating the three values: p_1 takes `−i,0,i`, while p_2 takes `−1/3,2/3,−1/3`. Let `h=s−1/2`, upsilon=1, k=2, N=1. This satisfies N at least k(d−1)=0. The two full-jet orthogonal shell columns `p_1(s_1)p_0(s_2)` and `p_0(s_1)p_1(s_2)` both vanish. Hence rank A_top and rank C_N are zero. The homogeneous shell columns s_1 and s_2 both evaluate to 1/2, and its rank is one. No claimed isomorphism may erase this difference.

The exact comparison retains the lower-degree polynomial coefficients. If L_N is the rectangular matrix of coefficients of degree below N in the monic product polynomials p_alpha with |alpha|=N, and J_N^hom, J_<N^mon are the corresponding full arithmetic jet maps, then

    A_top^orth = J_N^hom + J_<N^mon L_N.

This follows by writing every original product polynomial as `s^alpha` plus its complete lower-degree terms and applying the same jet map, including upsilon. It is the correct typed relation between the two shell images.

The proposed projective-ratio computation remains valid for the homogeneous shell itself. Suppose h has no zero centre, retain `E=C[s_1,s_2]/(h(s_1),h(s_2))`, and put `z=s_1/s_2`. At the local ordered pair (rho,sigma), of multiplicities m,n, use x=s_1−rho and y=s_2−sigma. Then

    z−rho/sigma = (sigma x−rho y)/(sigma(sigma+y)).

The denominator is a unit. The power m+n−1 vanishes in `C[x,y]/(x^m,y^n)`. The preceding power has unique surviving top monomial with nonzero coefficient `binom(m+n−2,m−1) sigma^(m−1)(−rho)^(n−1) x^(m−1)y^(n−1)`, multiplied by the original inverse-unit power. Hence its nilpotent index is exactly m+n−1. Across the full ordered CRT decomposition, the minimal polynomial is

    m_z(X) = product_(distinct r=rho/sigma) (X−r)^(M_r),
    M_r = max_(rho/sigma=r) (m_rho+m_sigma−1).

This gives the exact algebra embedding `C[X]/(m_z) -> E`, X mapped to z. The homogeneous shell image is `s_2^N span(1,z,...,z^N)`; its dimension is `min(N+1,deg m_z)`, because multiplication by s_2^N is invertible and the first deg(m_z) powers are linearly independent. This does not calculate the orthogonal-shell rank without the retained lower-degree term above.

The ratio algebra is a subalgebra of the tensor algebra, not automatically a quotient or an algebra retract of it. For example, in `C[x,y]/(x^2,y^2)` the ratio nilpotent has index three. Any algebra map from this algebra to `C[t]/(t^3)` sends each of x,y into the span of t^2: writing an image as a t+b t^2, its square is a^2 t^2, so a=0. Therefore such a map cannot send the ratio nilpotent to t and cannot retract the embedded ratio algebra. This is an exact obstruction to that proposed retraction, while the displayed embedding and homogeneous-shell map remain fully valid.

## Cumulative reader implications

The source makes genuine new finite constructions. It does not replace the current analytic graph closure, and it supplies no contradiction to JD.9: G_N tends to zero while K_N becomes coercively large in every fixed retained coordinate. The equality `W=G V G` is the exact bridge to the relative form; neither absolute limit provides an upper bound for it. The new layer coordinates can now be substituted into the existing determinant dissipation and spectral-cost formulas without changing the measure, representative, generator, or nilpotent multiplicities.

The existing univariate naturality CT.7 survives exactly. For joint packets with shifted total-degree budgets, CT.17–CT.19 retain an extra orthogonal projection Z. The source correctly declines to infer equality across those different joint boundary spaces. Integration should point to the existing Z formula rather than suggest that product polynomial bases commute with packet inclusion.

No new global theta retraction, finite metric lower bound uniform in N, arithmetic quadrature enclosure, monotone relative allowance, or RH theorem has been proved by this delivery. Those statements are not needed as assumptions for any of the finite identities audited above. The next calculation should use the actual orthogonal full-jet columns and the exact layer-energy formulas, retaining the lower-shell correction whenever any homogeneous/projective comparison is made.
