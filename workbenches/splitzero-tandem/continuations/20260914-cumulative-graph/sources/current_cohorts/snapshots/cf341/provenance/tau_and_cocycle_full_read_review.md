# Full-read review of the tau fibre and original scaling cocycle companions

## Result

Both fragments were read in full and checked on the original spaces, coordinates, actions, units, and measures. No defect was found in the relative-fibre or adjoint signs, the finite residue orientation, the global retraction argument, the finite Duhamel cocycle, the exact finite/global coboundary, the shifted minus-face extension sign, or the original `dx` boundary identities.

Two small but precise presentation repairs were reported to the parent and directly to the owner task, **Tau F1 · Transcript Audit and Calculations** (`01a09b53-02be-7c42-9d5f-fd38418a2c01`): explicitly type the Gaussian moment projection on the even Schwartz space; explicitly substitute the corrected infinitesimal boundary when passing from the finite representative `R` to the global representative `R^s`. These do not invalidate the proved Duhamel or retraction formulas, and their exact repairs follow from identities already in the fragments.

No owned proof fragment was edited by this reviewer. No Lean process was started.

## Complete read evidence

The first attempted raw read of the tau fragment was truncated and was **not** accepted as full-read evidence. The entire file was then read again in the following untruncated consecutive physical-line blocks:

| File | Physical lines | Read coverage | SHA256 of reviewed bytes |
|---|---:|---|---|
| `output/tau_f1_transcript_audit_2026-09-13/proofs/tau_exact_continuation_fragment.tex` | 1043 | 1–220, 221–440, 441–660, 661–880, 881–1043 | `57c8c522ba8d543ab8adf26ec9a21d797272cdc6d18ff7403f1c9a578998e11b` |
| `output/tau_f1_transcript_audit_2026-09-13/proofs/theta_scaling_cocycle.fragment.tex` | 1129 | 1–220, 221–440, 441–660, 661–880, 881–1100, 1101–1129 | `2a715b324d298bdfac4b32ed8adc4f36c7bdfb08a1e3977f165cb5504c51d902` |

Blank lines are included in these physical counts. PowerShell `Measure-Object -Line` returned smaller counts because it excluded blank lines; the complete `Get-Content` arrays supplied the physical counts recorded above.

A second reviewer independently read every line of the cocycle fragment, checked the same SHA256, and separately verified its shift sign (28a). The source `arithmetic_input.tex` had already been read in full in this review task's preceding balanced-kernel audit; A1–A19 were available for the exact source comparison.

## Relative tau fibre, adjoints, and topology

1. **Cone and fibre conventions.** The specified cone differential gives the fibre differential `(d_C c, -d_D y-fc)`. Accordingly the original relative fibre has differential `(r_+u-r_-v,-tr_+u)`. Its degree-zero kernel, degree-one quotient, and both exact presentations (2.9)–(2.11) have the correct maps. The negative connecting arrow in the rotated distinguished triangle and the separately chosen positive injection in (2.10) are consistent.

2. **Two restriction representatives.** `f_+-f_-=t delta`, and the explicitly stated fibre map `(m,s) -> (m,s+tm)` intertwines their differentials in the indicated direction. Naturality follows from the actual diagram squares, with no changed stalk.

3. **Injective adjoint.** The right adjoint of evaluation is the indicated lower-supported injective diagram `I_x(W)`. Its differential `(ell r_+,-ell r_-)` matches internal Hom in degree minus one. The bounded-complex correction `ell_p=(-1)^(n+1)a_p` in (3.6) gives exactly (3.7)–(3.8). The stalkwise quasi-isomorphism `S_eta W[1] -> K_tau(W)` is natural and retains the plus/minus signs.

4. **Relative dual.** The complex `R_tau(W)=Cone(-alpha_+)` gives differential `(ell r_+-wtr_+,-ell r_-)`. The kernel diagram (4.5)–(4.6) and its nonsplit extension (4.7) are correct. The claimed nonsplitting is witnessed by the incompatible actual plus and minus arrows. When the sigma stalk is zero, the extra Hom term is exactly zero, so the claimed reduction to the original adjoint is valid.

5. **Actual masks.** The calculation correctly retains the full original `V` at every present leg. The two singleton fibres have zero degree-zero cohomology; the joint fibre has the cycle `(F psi,psi)`. All nonempty masks have the same actual quotient `Q=B/Theta V`, and their degree-one transport is identity. This avoids the earlier improper extrapolation to arbitrary smaller source labels.

6. **Finite interpolation.** The displayed Riesz density is the one for `dx`, with the exponent `rho+bar(sigma)-1` after logarithmic substitution. Its Gram quadratic form, independence proof, interpolation section, and Mellin-jet seminorm bound retain the correct density and factorials. The full finite-jet kernel remains in (6.10)–(6.16).

7. **Continuous theta retraction.** The Möbius inverse is justified away from zero by the stated summable derivative bounds. The cutoff operator `T` is Hilbert–Schmidt with the displayed squared norm. If its norm were one, compactness would give a norm-attaining vector, equality in both contractions would force simultaneous compact spatial/Fourier support, and the entire inverse Fourier integral would force that vector to vanish. Thus `||T||<1` is proved. The smoothing estimate for `T:L^2 -> S` and `Phi=Y+T Phi` give actual Schwartz-valued continuity. On theta inputs, `Y Theta=(1-T)` and the retained moment projection give `Lambda Theta=1`. Closedness, the global section, and the completed tensor contraction follow without assuming exactness of completion.

8. **Scaling and dual action.** The original source action is `(U_a,a U_(1/a))`; its second-leg scalar and Fourier sign are necessary and correct. The induced dual action has weight one, `(U_a ell)(v)=a ell(U_(1/a)v)`. The global cocycle retains its full source-valued defect.

9. **Residue orientation.** The reflected Laurent coefficient of order minus one changes sign. The raw residue pairing is therefore skew-Hermitian, exactly as asserted; the perfectness determinant and full unit coefficients are correct. Contraction by `g'` gives the Hermitian trace pairing with radical equal to the packets with zero constant term. No positivity has been inferred from the raw residue form.

10. **Tensor signs and fibres.** The product differential, telescoping representative homotopy, and explicit composable-fibre cone map (9.8) check directly. The adjoint correction is `(-1)^(p(p-1)/2)` in degree minus `p`, hence minus one for two top-degree factors. Both algebraic and completed tensor cohomology preserve the original `V[0]` contribution and the full top-degree quotient.

## Finite and global scaling cocycle

1. The source integral in (13) converges in every actual Schwartz seminorm, with the displayed bound and orientation for negative time. Differentiating `U_(e^(t-r)) R T_r` produces **minus** the transported infinitesimal boundary, so integration gives exactly `U_(e^t)R-R T_t=Theta c_t`.

2. The cocycle law `c_(t+s)=U_(e^t)c_s+c_t T_s`, its inverse-time formula, and both derivatives in (17) are correct. The topological block representation is the integrated form of the original nontrivial extension, with no lost boundary.

3. The full nilpotent expansion retains all Taylor coefficients of the original unit. The two changes of variables in the incomplete-gamma formula give exactly the coefficients `2` and `-3`, and preserve interval orientation at negative time. Differentiation in the auxiliary complex parameter of the kernel gives the stated generalized-zero terms without differentiating the arithmetic zero.

4. The entire Mellin boundary expression `(exp(ts)R_Z(u)(s)-R_Z(T_tu)(s))/h(s)` follows from the literal polynomial division identity. Every required jet vanishes, so its apparent poles are removable. No substitute arithmetic multiplier enters the calculation.

5. The plus homotopy `(c_a,0)` and minus homotopy `(0,-F c_a)` give the same boundary and have the stated nonzero joint difference `(c_a,F c_a)`. The singleton-to-joint naturality obstruction is exactly this difference. Nonvanishing of `c_a` for every `a!=1` follows from the absence of nonzero dilation eigenvectors in `B`, proved using its original power-decay seminorms.

6. The shifted minus-face extension class in (28a) is **positive** `[F psi]`, as written. The free resolution shifted by minus one has differential `-h`; its degree-zero lift is `-w=F psi`, and projection keeps that value. Nullhomotopies change it by an `h(1-D)` multiple. Fourier and the original jet unit prove its nonzero class.

7. The finite/global replacement `R^s=R-Theta b_Z` gives exactly `c_a^s=c_a-U_a b_Z+b_Z a^A` and derivative `k_D sigma=phi_* ell-D b_Z+b_Z A`. The cochain difference and both face signs in (34) are correct.

8. The evaluated tensor homotopy contains its factor `(-1)^(j-1)` exactly once. The tensor differential cancels it, giving the displayed telescoping boundary. The detected plus/minus difference survives in degree `k-1`; the projection onto the original `H^0` factor and quotient factors records its class.

9. With the retained measure `dx`, dilation has mass `a`. Expansion of `R a^A=U_a R-B_a` gives the positive `B_a^* B_a` term in the formulation using `U_aR`, and the negative version using `Ra^A`; these agree. The infinitesimal matrix has mass term `-G` and two negative boundary cross terms. The finite integral in (43) and the tensor mass `a^k`, `-kG_k`, and integral in (46) are correct.

## Exact requested repairs

### 1. Domain of the Gaussian moment projection

In the cocycle fragment near original lines 753–761, the formula for `P_V` is a projection onto `V` only when its domain is the **even** Schwartz space. On arbitrary Schwartz functions, the odd function `x exp(-pi x^2)` has zero value and integral and is therefore fixed by that formula, although it is not in `V`.

The construction already lands in the correct domain: `U F` is even by its use of `|x|`, the fixed cutoffs are even, Fourier preserves evenness, and `T` commutes with reflection. Consequently `Y F` and every term of `(1-T)^(-1)Y F` are even; the smoothing argument gives an even Schwartz function. State this explicitly and type the map as `P_V:S_even -> V`. The tau fragment already says `Phi` preserves evenness; the same explicit domain would also remove any ambiguity in its projection sentence.

### 2. Infinitesimal boundary of the global representative

In the cocycle fragment near original lines 1041–1047, the instruction to replace `R` by `R^s` and `c_a` by `c_a^s` to obtain (41)–(43) should display the corresponding replacement in (42):

`B_D^s=Theta k_D sigma=Theta(phi_*ell-D b_Z+b_Z A)`.

Then the literal formula is

`W^s=A^*G^s+G^s A-G^s=-(R^s)^* B_D^s-(B_D^s)^*R^s`.

It is not generally the formula obtained by replacing only `R` in `-R^*f_0 ell-ell^* f_0^*R`. The earlier exact identity (33) supplies the missing correction. The finite and integrated identities remain valid with this complete substitution.

### Optional completed-tensor precision

For the nonzero tensor detection near original lines 959–962, choose **continuous** separating functionals if the assertion is read after projective completion. The retraction already proves `Q` is Hausdorff locally convex, and `V` is a Hausdorff Schwartz subspace, so continuous separation applies. On the algebraic tensor the existing linear-functionals argument is sufficient. No counterexample to the claimed nonvanishing was found.

## Communication and provenance

The two precise repairs above were sent to the root by collaboration message and directly to the existing owner task using its inspected task id. That message asked the owner to update its own source/fragment and notify the parent; it did not edit either fragment or create a new task.

Delegated request (verbatim):

> Read/review in full the dedicated peer task's two completed fragments output/tau_f1_transcript_audit_2026-09-13/proofs/tau_exact_continuation_fragment.tex and theta_scaling_cocycle.fragment.tex (read entire bodies, no truncated claims). Need bounded check of exact relative tau fibre/adjoint signs, original Duhamel finite/global cocycle and sourcepairing. These will be inherited companion chapters in our final reader; report precise defects to owner and me. Save full-read evidence/review own file under shared_thread_audit. Root is assembling original-source reconstruction in parallel.
