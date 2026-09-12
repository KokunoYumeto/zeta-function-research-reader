# Audit of the actual kernel layer and consecutive derivative quotients

Date: 2026-09-12. Scope: the complete `tex/kernel_layer_continuation.tex` continuation, KL.1–KL.20. Also read the full delivered `sources/web_kernel_layer_delivery/Tau_Kernel_Layer_Integration/NOTE.tex` and the preceding CT joint tensor construction. No sealed fragment, cumulative main, or other source was edited by this auditor. The separate projective comparison is excluded.

## Original source, unit, and minimum

The arithmetic source multiplier is the unchanged product of `g/h` in the original coordinates `s_j=1/2+i t_j`. Each factor is nonzero except on a discrete set, so the source map is injective on polynomials and the product polynomial Gram is positive. The complete reduction map is followed by the actual unit `upsilon_h^⊗k`; its kernel therefore remains the original polynomial ideal. Its intertwining with the summed multiplication operator follows because this unit commutes with each coordinate multiplication.

The standing range must be the integer `N >= k(d-1)`. Within that range the complete tensor remainder monomials belong to the total-degree source, so the full jet map is onto and the inverse metric in KL.6 exists. The source author has added this explicit standing assumption following audit feedback. It also holds at the two following degrees needed by KL.19–20.

Product orthogonality retains the exact norm product `kappa_alpha`, and the monic basis change preserves total degree. The coefficients in KL.6 solve the original full-jet constrained minimum, with conjugate-linear first inner product; every zero-jet coefficient vector is orthogonal to the minimizing vector. Hence the source representative and metric agree with the earlier CT representative, including the quotient class.

A dimensional clarification was requested for the comparison after KL.6: for general tensor degree define the remainder-only kernel using the full tensor columns `r_alpha=⊗_j [p_{alpha_j}]_h`. Its matrix is `K_N^rem=sum r_alpha r_alpha*/kappa_alpha`, on `E_h^⊗k`; then `mathcal K_N=U K_N^rem U*`, where `U=U_(upsilon_h^⊗k)`. The prior univariate `K_N` is recovered when `k=1`. This avoids using a univariate matrix in a tensor congruence.

## Actual next-layer frame and primitives

In KL.7, `T(p_beta)` is orthogonal to every old polynomial and `R_N a_beta` is orthogonal to the admitted old relation space. Their difference has zero full jet. Its degree-`N+1` numerator has exactly the monomial `s^beta` as leading part. Injectivity of the original source map proves independence, and subtraction of all those leading coefficients leaves precisely an old relation; orthogonality then proves spanning. Thus KL.8 identifies the actual layer, its coefficient space and the relation quotient, with the stated inverse projection.

The fixed-order monic division in KL.9 retains every lower coefficient of `h` and of the numerator. Each quotient polynomial has degree at most `N+1-d`. Applying its Euler polynomial to the tensor with `(-1)^(i-1) phi_*` in factor `i` gives the required original primitive: the preceding `i-1` factors have cochain degree one, so the differential supplies a second `(-1)^(i-1)` and the resulting term is positive. These signs agree with the source complex `[V -> B]` in degrees zero and one.

The old/new orthogonality gives `E_N*E_N=D_(N+1)+U_N*G_N U_N` and `E_N*R_N=-U_N*G_N`. The resulting projection `Y_N=P_(actual layer) R_N` has exactly rank `U_N`. Explicitly naming this projection before its formula was requested for readability and typing.

## Incidence, derivative image and ranks

The coefficient incidence map in KL.12 is multiplication by the unchanged polynomial `ell(z)=sum z_j` in the stated homogeneous coefficient variables. It is injective by the polynomial integral-domain property. It is not multiplication by the original Mellin coordinates; the source connects them by their exact leading-coefficient map.

Multiplying the degree-at-most-`N` numerator of `R_N` by the summed Mellin coordinate yields the new leading coefficients `T_N D_N^(-1) A_N*G_N`. Subtracting the corresponding actual layer frame leaves a zero-jet polynomial of degree at most `N`. This proves KL.13 as an equality of maps after orthogonal projection, and as the indicated equality of original quotient classes.

The frame and incidence maps are injective and the diagonal norm matrix and original metric are invertible. Therefore `rank C_N=rank A_N` and `ker C_N=mathcal K_N ker A_N*`, exactly as in KL.14. The weight is the original `W_N=A*G_N+G_N A-kG_N`, and the Green identity gives `W_N=-(Y_N*C_N+C_N*Y_N)`. The product-rank and sum-rank inequalities yield KL.15 with both actual top-column ranks. The explicit weight definition was requested because the earlier CT text uses a different degree letter.

## Complete quotient of the layer

The last-variable division by `ell=z_k+sum_(i<k) z_i` in KL.16–17 retains degree and gives the unique decomposition `f=ell q+iota r`, with `r=f(z_1,...,z_(k-1),-sum_(i<k)z_i)`. The minus sign is correct. Evaluation proves the displayed section and cokernel; polynomial injectivity proves uniqueness of `q`.

Since `G_N` is invertible, `im C_N=E_N T_N Z_N` for `Z_N=im(D_N^(-1) A_N*)`. Changing a layer representative by this subspace changes only `q` by an element of `Z_N`. This proves both well-defined maps and inverse identities in KL.18. The two dimensions are exactly `binomial(N+k-1,k-1)-rank A_N` and `binomial(N+k-1,k-2)`; their sum is the full next-layer dimension minus `rank C_N`. For `k=1`, the latter summand is zero and the incidence map is an isomorphism of the one-dimensional shells.

## Derivative between the consecutive quotients

The summed Euler derivative preserves the original polynomial ideal and raises total degree by at most one. Thus changing a representative by `L_N` changes its derivative by `L_(N+1)`, proving the domain and target of KL.19. In the actual layer coordinates the new leading vector is `T_(N+1)` times the old leading vector; this proves KL.20. Incidence injectivity proves derivative injectivity, and the explicit incidence remainder gives its full cokernel `H'_(N+2)`.

For explicit retention of lower terms, the auditor requested the layer-dependent notation `e_beta^(N)` and `e_(beta+e_i)^(N+1)`. The exact difference is

```
D^(k)e_beta^(N) - sum_i e_(beta+e_i)^(N+1)
 = T[(sum_i b_(beta_i))p_beta
       - sum_(i:beta_i>0) (kappa_(beta_i)/kappa_(beta_i-1)) p_(beta-e_i)]
   - D^(k)R_N a_beta
   + R_(N+1) sum_i a_(beta+e_i),
```

where the actual vertical-line recurrence is `s p_j=p_(j+1)+b_j p_j-(kappa_j/kappa_(j-1))p_(j-1)` and `b_j+conjugate(b_j)=1`. This retains all lower product-polynomial terms, norms and signs. Its degree is at most `N+1`, its jet vanishes, and fixed-order division supplies its original theta primitive. The same argument establishes KL.20 without an unrecorded deletion in the original test space.

Finally, the ordinary admission map should have its target written explicitly. With the same domain and target as KL.19 it is `[f] -> [f]=0` from `L_(N+1)/L_N` to `L_(N+2)/L_(N+1)`. The derivative map has matrix KL.20. This states the two exact maps, rather than relying on the phrase “next admitted quotient.”

The requested clarifications do not change the substantive layer quotient or derivative-injectivity results. The author incorporated every requested KL.1–KL.20 clarification. The complete revised source was re-read: the tensor-sized remainder kernel, original Y/W definitions, layer-indexed recurrence residual with its exact norm ratios, and typed zero admission map are all correct. This reviewed edition has SHA256 `00A8371A19E17051BD2BAA7AAABEE16681A241CA273FB53DFD97133DB1625369`. No outstanding correction remains in KL.1–KL.20. A subsequently planned univariate norm/volume bridge is outside this edition and requires its own appended review.
