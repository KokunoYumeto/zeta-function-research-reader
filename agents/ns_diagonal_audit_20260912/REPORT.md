# Exact diagonal-to-arithmetic handoff audit

Date: 2026-09-12. Scope: local content-level audit and explicit repairs, not a new certification of the imported source existence theorem. No canonical file was edited and no remote record was changed.

## Reviewed content and identities

The following were personally read in full:

- `tex/satellites/29q_ns_diagonal_generator.tex`, 9,610 bytes, SHA-256 `7b57a3296614429f7bff731ec77cd54c2b0548e18bf3b19ee9093869cf21adee`.
- `tex/satellites/29n_ns_diffusion_hidden_mellin.tex`, 16,675 bytes, SHA-256 `ea02b8428c482b749bd34708cdf036a56439823c7e952b34cce8239161fe8681`.
- `tex/satellites/29o_ns_actual_second_radial.tex`, 19,259 bytes, SHA-256 `5f57b2aaee949b0163cb614ff253b12e2ea74069ad3a3e0e870c747f56f0b623`.
- `tex/satellites/29p_ns_finite_radial_recursion.tex`, 18,230 bytes, SHA-256 `e2ac77ee6dd576a7b2849a5513f946bc2a120738d421332075359cb746f058a9`.
- `agents/ns_higher_radial_20260909/DIAGONAL_GENERATING_OPERATOR.md`, 21,744 bytes, SHA-256 `ea2916ee70f74fae3a7885a97f814119608aa4a1b535ffd3de578701b176450d`.
- `tex/satellites/29l_ns_axis_arithmetic_jet.tex`, including the differentiated Euler--Maclaurin proof.

These hashes identify the inputs to this report, not a requirement that the parent preserve defective wording. The primary release's existence theorem is imported. This reviewer did not reread the 166-page primary PDF and does not promote earlier reviewers' reading to personal coverage.

The audit found a repairable, concrete type error in 29q's final handoff, not an obstruction to the source-to-arithmetic map. The convergent kernel and cutoff formulas agree with the detailed generating-operator note. The omitted lower-order source term is explicitly calculable and must travel through the same arithmetic map.

## 1. The operator is A_h; W_h is its Mellin multiplier

For a physical radial function a, retain exactly

    phi_a(x) = a(x) - 2^h a(2x),
    psi_a(x) = phi_a(x) - (1/2) phi_a(x/2),
    A_h a(x) = sum_{m>=1} psi_a(mx),
    W_h(s) = zeta(s)(1-2^(s-1))(1-2^(h-s)).

The identity proved in 29n, equation `ndm:product`, is

    mathfrak G_a(s) = M(A_h a)(s) = W_h(s) M(a)(s).             (1)

The expression `M(W_h a)` at reviewed 29q line 199 is not this identity: W_h is a function of the arithmetic Mellin variable s, whereas a is a function of the physical radial variable sigma. Replacing it by (1) repairs the actual map and identifies its existing inverse. It is not appropriate to interpret W_h as a newly defined source-side multiplier.

## 2. Preserve the nonzero axial constants by extending the domain

At fixed preterminal z,t, the selected W_rho[f] and G_rho[g] are locally finite polynomials in sigma. They have axis values f and g, respectively. In particular the source angular g=b_1 is strictly positive. The source-order cutoffs rho_j=chi(c_j q) do not supply compact support in sigma, because q and hence rho_j are independent of sigma. Thus they are not members of the old D_0=C_c^infty([0,infinity)) intersect {a(0)=0}.

There is an exact extension, with no removal or rescaling of the axis data:

    D = C_c^infty([0,infinity));   A_h : D -> D.

For a_0=a(0), the two filters satisfy

    phi_a(0)=(1-2^h)a_0,
    psi_a(0)=(1-2^h)a_0/2,
    integral_0^infinity psi_a(x) dx=0.

The last equality follows by substitution in the second filter for every compact a, without any endpoint assumption. Euler--Maclaurin consequently gives

    (A_h a)(0) = -psi_a(0)/2 = (2^h-1)a_0/4 = W_h(0)a_0.     (2)

All positive endpoint derivative identities from 29l remain unchanged. For completeness, for j>=1 use f_j(v)=v^j psi_a^(j)(v). Its integral is (-1)^j j! integral psi_a=0 by repeated integration by parts. The powers of v kill the boundary terms even when psi_a(0) is nonzero. For r<j, f_j^(r)(0)=0; for r>=j it is r! psi_a^(r)(0)/(r-j)!. The Euler--Maclaurin remainder after dividing the j-th differentiated sum by x^j is O(x^(2M-1-j)) for an arbitrarily large M. The fundamental theorem of calculus then identifies these limits as actual successive endpoint derivatives, exactly as in 29l. Hence

    (A_h a)^(j)(0)=W_h(-j)a^(j)(0), j>=1,

and (2) handles j=0. Compact support follows because the filtered input has compact support and the sum vanishes when x exceeds that support. This proves A_h D subset D.

The initial Mellin integral half-plane is now Re s>0, uniformly over D; it is sharp when a_0 is nonzero. Absolute summation proving (1) starts on Re s>1. Taylor subtraction with indices 0,...,N then continues both sides meromorphically and proves (1) everywhere. The extra local pole is a_0/s. Since

    W_h(0)=(2^h-1)/4 > 0,

define the additional coordinate by

    c_{h,0}=W_h(0), E_0(mathfrak G)=Res_{s=0} mathfrak G,
    E_0(mathfrak G_a)=c_{h,0}a_0.                              (3)

Index zero is a residue, NOT an instance of the positive-even regular-value case. For n>=1, retain precisely the old c_{h,n} and E_n. The inverse of every coefficient remains a_n=E_n/c_{h,n}, including n=0 with (3).

All three source-side inverse formulas from 29n survive unchanged:

    psi_a(x)=sum_{m>=1} mu(m) (A_h a)(mx),
    phi_a(x)=sum_{ell>=0} 2^(-ell) psi_a(x/2^ell),
    a(x)=-sum_{k>=1} 2^(-kh) phi_a(x/2^k).                    (4)

The first is finite at each x>0 and is a divisor cancellation; its extension at zero is the recovered smooth function, not a termwise Mobius sum at zero. The second and third truncation remainders are 2^(-L-1)phi_a(x/2^(L+1)) and 2^(-Kh)a(x/2^K). Their j-th derivatives gain factors 2^(-(L+1)j) and 2^(-Kj); bounded derivatives and h>0 imply smooth convergence on compact half-line intervals. Thus (4) proves the inverse on the actual range A_h D, preserving the nonzero axis value and all smooth flat remainders.

### Boundary terms in transported differentiation

For a in D the raw integration-by-parts proofs below require Re s>1, rather than the Re s>0 available for 2sigma a'' on the smaller old domain:

    M(a')(s)=-(s-1) a-hat(s-1),
    M(2sigma a'')(s)=2s(s-1) a-hat(s-1).                      (5)

Both are exact meromorphic identities afterwards. The removable values encode, rather than discard, the new boundary data:

    M(a')(1)=-a_0,
    M(2sigma a'')(1)=2a_0,
    M(2sigma a'')(0)=-2a_1.

The last transform has zero residue at zero because 2sigma a'' vanishes at zero. More generally, for the two scalar radial operators L_a^rad=2sigma d_sigma^2+2(a+1)d_sigma, a=0,1, the multiplier is

    M(L_a^rad v)(s)=2(s-1)(s-a-1) v-hat(s-1),

and its n-th ordinary coefficient is 2(n+1)(n+a+1)v_{n+1}, including n=0. These formulas were independently checked by helper `check_nonzero_axis_mellin`; they do not assume away a boundary term.

## 3. A compact radial representative with every original cutoff retained

Fix a compact preterminal parameter patch inside the given central slab. Choose epsilon>0 smaller than a common physical radial neighborhood there. This is an analysis partition, not a new source parameter or a replacement source field. One explicit plateau is

    e(v)=exp(-1/v) for v>0, e(v)=0 for v<=0,
    kappa_epsilon(sigma)=e(2-sigma/epsilon) /
                         [e(2-sigma/epsilon)+e(sigma/epsilon-1)].

It equals one for sigma<=epsilon and zero for sigma>=2epsilon. Take epsilon constant on the patch, so kappa has no z or t derivative. The source's rho_j(q) remain unchanged. Define

    w_d = kappa_epsilon W_rho[w_0],
    g_d = kappa_epsilon G_rho[b_1],
    B_d = sigma g_d.                                         (6)

The first two belong to D; B_d belongs to D_0. Their exact coefficients are

    E_j(M A_h w_d)=c_{h,j} rho_j alpha_j[w_0], j>=0,
    E_j(M A_h g_d)=c_{h,j} rho_j beta_j[b_1], j>=0,
    E_n(M A_h B_d)=c_{h,n} rho_{n-1} beta_{n-1}[b_1], n>=1.   (7)

For the actual angular-momentum channel the shift n=j+1 is essential. The reviewed 29q's beta_j formula applies to G_rho, not to B=sigma G_rho. Equations (3), (4), (6), and (7) provide the exact forward map and both the whole-function and coefficient inverses.

This localization must not lose the physical source outside its support. Define

    B_rem = B_actual - B_d.

Both terms and B_rem are in D_0, and the exact global arithmetic identity is

    M A_h B_actual = M A_h B_d + M A_h B_rem.                  (8)

The latter retains every lower source order, all original radial extensions, the annular representatives, and final localization terms. It is not an estimate. The same construction works for the full axial angular average on D.

Changing epsilon or its plateau changes (6), but two plateau choices agree near the axis. Their difference is compactly supported away from zero, so its Mellin transform is entire. Multiplication by W_h gives no residue at nonpositive integers and zero regular value at each negative even integer. Thus all coordinates (7) are independent of this partition, while the full functions remain partition-dependent in exactly the way canceled by (8). No claim that endpoint coefficients determine a whole smooth function is needed.

For scalar V and kappa=kappa_epsilon, the exact cutoff commutators are

    L_a(kappa V)-kappa L_a V
      =4sigma kappa' V_sigma
       +[2sigma kappa''+2(a+1)kappa']V, a=0,1;

    L_B(kappa B)-kappa L_B B
      =4sigma kappa' B_sigma+2sigma kappa'' B,

where L_a also contains partial_zz and L_B=2sigma partial_sigma_sigma+partial_zz. These terms, in addition to the rho commutators already proved in 29q, must be retained before applying M A_h.

If an actual compact divergence-free vector representative is desired, simply multiplying all vector components by kappa is not correct. Write Psi_rho=integral_0^sigma W_rho ds and use

    Psi_d=kappa Psi_rho,
    u_z,d=partial_sigma Psi_d=kappa W_rho+kappa' Psi_rho,
    r u_r,d=-partial_z Psi_d=kappa R_rho,
    r u_theta,d=kappa B_rho.                                 (9)

Then partial_sigma(r u_r,d)+partial_z u_z,d=0 identically. It agrees with the selected vector field where kappa=1, is compact radially, and preserves the source field by adjoining u_actual-u_d. The apparent radial 1/r is smooth because its numerator vanishes to order sigma. The extra kappa' Psi_rho in (9) is required, not optional.

## 4. First omitted source term, including arithmetic and force accounting

Use H,R from 29o `nsr:HR`, with the original source variables and constants. From beta_1[b_1]=-b_1,zz/4 and the physical chain rule,

    b_1,zz=2 q^(-2+h) R/(nu C).

The selected angular coefficient and actual one are consequently

    [sigma^2] B_d = -rho_1 q^(-2+h)R/(2nu C),
    b_2,actual = [q^(-2-h)H-rho_1 q^(-2+h)R]/(2nu C),
    [sigma^2] B_rem = q^(-2-h)H/(2nu C).                     (10)

The last term is strictly negative because the complete expression in 29o `nsr:H-sign` is

    H=varphi[(h-3-j_0 eta)/L
            -Lambda H_*^2/(H_*^2+sigma_*^2)]<0.

Here varphi>0, L>0, h-3+j_0<0; the square need not be nonzero. No new source parameter choice was made. Applying (7)--(8) proves

    E_2(M A_h B_rem)
      = d_h q^(-2-h)H/(2nu C),
    d_h = 7(2^(h+2)-1)zeta(3)/(32pi^2)>0.                    (11)

Thus the omitted source term is exactly carried by the regular Mellin value at -2. It is not absent simply because the selected field has the same axis value or its uncut generating field is harmonic.

For the selected cutoff field, the coefficient of sigma in its full angular equation is

    f_1,diag = b_1,t + w_0 b_1,z - b_1 w_0,z
               -nu(4b_2,diag+b_1,zz)
             = 2 q^(-2-h)H/C + r_f,actual,

because 29o proves

    r_f,actual=2(rho_1-1)q^(-2+h)R/C.

The extra selected residual is precisely 4nu times the missing coefficient in (10). In the late constant-cutoff region r_f,actual=0 but the extra term remains nonzero. Adding the missing source coefficient supplies its exact radial diffusion contribution; no nonlinear transport or force is deleted.

For the complete fields, keep the original angular averages when forming P,Q,F. If u_actual=u_d+v, their exact quadratic complements include all cross terms:

    P_actual-P_d = <r^2(u_d,r v_theta+v_r u_d,theta+v_r v_theta)>,
    Q_actual-Q_d = <r(u_d,z v_theta+v_z u_d,theta+v_z v_theta)>.

These equations remain valid outside the inner axisymmetric region, since only u_d was chosen axisymmetric. They explain how the complete nonlinear hierarchy accompanies (8), rather than assigning an invented closed equation to the selected diagonal.

## Checks and scope

A bounded SymPy calculation checked exactly: (i) the expanded rational H identity, (ii) the full-minus-selected coefficient (10), (iii) the angular residual/force equality, and (iv) the general scalar cutoff commutator. All four returned True. This is supplementary algebraic regression; the displayed derivations, not a finite test, establish the formulas. No large calculation or Lean job was launched.

The concrete recommendation is to replace the final handoff of 29q by (1)--(8), with D and its n=0 residue explicitly defined, and to carry (10)--(11) into the full-source arithmetic comparison. This keeps the existing convergent diagonal result and extends the actual map instead of rejecting it for a domain mismatch. It does not provide an off-critical zero or a negative full Weil pairing; the exact negative quantity currently established here is (11), with the full source and its force retained.

## Post-repair review: parent 29q and new 29r

The parent subsequently made the canonical edits. This reviewer read the repaired 29q handoff and the whole new 29r. Reviewed final identities:

- `tex/satellites/29q_ns_diagonal_generator.tex`: 10,594 bytes, SHA-256 `ede92835eafe7ef739271070ea3c49e1ffef87ee995a09e2e8bb3cf52d30a123`.
- `tex/satellites/29r_ns_all_axis_mellin.tex`: 14,443 bytes, SHA-256 `213df6f6d5c2328625b5435209c690002a5b41957951a1f011d1182db3787813`.

Result: PASS for the displayed statements and their proofs. The original handoff defects are repaired. The parent also adopted the two minor precision corrections raised during review: the original Mellin integrals have Re s>0, while the absolute product proof starts at Re s>1; and the second inverse's j-th derivative remainder has the precise additional factor 2^(-(L+1)j).

The full Lagrange residue change of variables was read, including the integration-by-parts identity for the coefficient residue. Its even and odd axial formulas agree with A+D=1 and A-1=-D. The source angular formula is the derivative of d(u)^k phi(u) followed by the same inverse, with the original logarithmic derivative and the factor (n-1)! retained. The powers of nu and tau follow from each physical z derivative contributing (sqrt(nu) tau^D)^(-1). The physical zeroth residue is consequently exactly

    Res_{s=0} M A_h Z_actual(s,0,1-tau)
       = (2^h-1) sqrt(nu) j_0 tau^(-A)/4.

This is the residue of the actual axial average, not only of the selected representative, because their zeroth source values agree and the exact remainder has zero zeroth coefficient.

For an independent algebraic check of the new coefficient formulas, a second route recursively applied

    v_n = [2(-A-(n-1)D) eta v_(n-1) + (1-eta^2)v_(n-1)'] /
          (1-2h eta^2),       v_0=4eta+j_0,

and compared v_n(0)/n! with the closed formula in `nax:axial-coefficients`. It passed at n=0,...,6 as exact symbolic identities in h,j_0, not floating-point samples. For the angular channel the same ordered recursion with exponent -k-(n-1)D was applied to the arbitrary polynomial germ 1+p_1 eta+...+p_6 eta^6. At n=1,...,5 its value at zero agreed exactly with

    (n-1)! [u^(n-1)] {phi'(u)d(u)^(k+nD)
                        -2ku phi(u)d(u)^(k-1+nD)}.

This checks the coefficient formula before specializing phi to the source differential equation, independently of that specialization. All five identities passed symbolically.

The dangerous endpoint convention was also tested directly from the local Laurent terms: `-(s-1) a-hat(s-1)` tends to -a_0 at s=1; `2s(s-1) a-hat(s-1)` tends to 2a_0 there and -2a_1 at s=0. These are regular limits, while E_0 is a residue. Substitution of a zero prefactor before taking the Laurent product would fail each nonzero example. The canonical new zeroth coordinate uses the correct residue convention.

In total this report's supplementary runs produced 16 exact symbolic equality checks and the three boundary limits above. One initial shell quoting attempt failed before mathematical evaluation; the corrected in-memory command ran successfully. The route passed `topic_literature_route.schema.json` validation. No analytic theorem is claimed from those finite checks alone; the complete proofs above and in the reviewed source are the mathematical evidence. Primary NS existence remains imported, and no formal Lean certificate is claimed.

## Final 29r approval after the axial-average regularity insertion

The entire current `tex/satellites/29r_ns_all_axis_mellin.tex` was personally reread at **14,865 bytes**, SHA-256 **`f9b04d6346a5d66f3eec6049fcee652794a4d62bab029935bf9b277d1d10fe95`**. This supersedes the previous 14,443-byte review identity for the current canonical chapter; it does not erase that prior review's chronology.

The exact new content is the paragraph proving that the axial angular average extends smoothly in sigma=r^2/2 and remains compactly supported. Removing only the insertion from `the latter at the axis by its smooth extension.` through the following `Define` reconstructs exactly the previously reviewed 14,443-byte chapter with SHA-256 `213df6f6d5c2328625b5435209c690002a5b41957951a1f011d1182db3787813`. This reconstruction was checked directly in memory without writing or changing a canonical file. There is no other mathematical delta.

The added proof is correct. More explicitly, at fixed preterminal z,t, let v(x_1,x_2)=u_z(x_1,x_2,z,t). Angular averaging its transverse Cartesian Taylor polynomial kills every odd total degree. The even-degree angular moments give

    <v(r cos(theta),r sin(theta))>
      = sum_{m=0}^N r^(2m) (Delta_perp^m v)(0) /
                      [4^m (m!)^2] + remainder
      = sum_{m=0}^N sigma^m (Delta_perp^m v)(0) /
                      [2^m (m!)^2] + remainder.

These are finite Taylor statements; they require no analyticity. Taylor expansion through degree 2N+1 has differentiated radial remainder O(r^(2N+2-j)) for each fixed required derivative j, uniformly in angle on compact parameter sets. On r>0, partial_sigma=r^(-1)partial_r. Its k-th iterate is a finite linear combination of r^(j-2k)partial_r^j, 1<=j<=k, so the differentiated remainder is O(r^(2N+2-2k)). Taking N>=k yields a vanishing remainder for every chosen finite k. The derivative limits extend continuously to the axis, and the fundamental theorem of calculus identifies them successively as actual sigma derivatives. In particular the zeroth value is v(0), as used in the residue map. Applying the same argument after any fixed z,t derivatives preserves parameter smoothness.

For compact parameter patches, the imported compact spatial support confines r and hence sigma to a common bounded interval. Angular averaging cannot enlarge that radial support. This establishes the asserted membership of Z_actual in D with its full endpoint value retained; it is not a new cutoff or an omission of any radial remainder. No objection or additional canonical correction is needed.

**Final current canonical 29r: PASS.** The review now covers the complete file at the final hash above, including the previously unbound axial-average regularity paragraph. The final 29s review remains unchanged in `AXIAL_SINGULARITY_REVIEW.md`.
