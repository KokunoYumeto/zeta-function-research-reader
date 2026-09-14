# Independent review of the constituent period curvature

## Exact edition and result

The complete captured source is `SC1_SC37_CAPTURE.tex`: 21,469 bytes,
SHA256 `0aedbaf3481f3a8e88c91ec786a44cd26869f0b0988d927a43ffaf54ad906e20`.
It was copied from `workspace:/work/sga_constituent_period_curvature_20260913.tex` and the two byte hashes agreed at capture. The entire SC1–SC37 edition was read. The owner source was not edited.

No mathematical correction was found in the reviewed identities. The reported typographical powers `^{,2}` in SC36 are **not present in this captured edition**: both denominators already have the ordinary power `^{2}`.

The central result is a calculation for a fixed proper nonzero invariant constituent of the original cyclic algebra. Its period subspace has a rank-one normal derivative away from `t=0`, zero normal derivative at `t=0`, and nonzero normal acceleration there. The curvature coefficient is strictly positive. This does not identify the period metric with the original theta metric: their exact congruence, and every term required when differentiating the moving metric, remain in the calculation.

All 13 methods passed in ordinary and optimized Python. The four substantive mutations each produced exactly one intended assertion failure and no errors in both modes. Each ordinary/optimized pair has byte-identical machine receipts. Execution was sequential.

The execution seal is `EXECUTION_RECEIPT.json`, produced by `run_review.py`. The final ordinary and optimized receipts and their full logs are identified by that seal. `normal.json` is an earlier development run, not the final execution seal.

The owner later made a layout edition, captured separately as `SC1_SC37_LAYOUT_CAPTURE.tex`, SHA256 `f7cbbb2da3a97722c9f9128602b4de64ad1ab9cfccdbb03e8ee9363321f7de63`. Its complete two-hunk diff was read: SC10 and SC11 are wrapped in `gathered` environments, and SC10's prose describing the zero intersection is written explicitly as `C e0 intersect I(F)={0}` inside `E`. The mathematical assertions and all tested formulas are unchanged. `LAYOUT_ONLY_DIFF.txt` retains this exact comparison. The execution remains pinned to the original captured bytes; it is not mislabelled as an execution against different bytes.

## Proof review

### The actual constituent and its coefficient row, SC9–SC14

An `A=M_S`-invariant subspace of `E=C[S]/(chi)` is an ideal because invariance under `A` gives invariance under every polynomial in `A`. Its inverse image in `C[S]` is `(g)` for a monic divisor `g` of the original `chi`. With `chi=g h`, cancellation in `C[S]` proves that multiplication by `g` identifies `C[S]/(h)` with this ideal. This retains repeated factors and their complete local modules.

The ordered vectors `g,Sg,...,S^(p-1)g` have increasing monic leading degrees. The last has degree `q-1`; therefore the original top-coefficient row restricted to the ideal is nonzero and, in that particular ideal frame, is the last coordinate. In an independently chosen constituent frame it is the literal row `L=ell I`, not a replacement row. A proper ideal does not contain the unit. These two facts establish both nonzero factors of the normal map.

For `Y=Pi I`, the ODE `Pi'=-Pi(A+t e0 ell)/u` and the exact invariance `AI=I A_F` give

`Y'=-Y A_F/u-t Pi e0 L/u`.

The orthogonal complement projection kills precisely the first term. Since `Pi` is invertible, the projection of `Pi e0` outside `Pi I(F)` is nonzero. Hence `NY'=-t zL/u` has exactly the stated image and kernel. Differentiating the same ODE at zero gives the `-Pi e0L/u` acceleration term with its original sign; `Pi A^2 I/u^2` is tangent. The source lift in SC8 and SC14 follows by inserting the original `j_E r_N=I_E`; its extra parameter terms cancel without changing the original source relation primitive.

### Curvature, SC15–SC18

For the holomorphic matrix `Y`, the four Gram jets are

`H=Y*Y`, `H_t=Y*Y'`, `H_bar=Y'*Y`, `H_tbar=Y'*Y'`.

Differentiating the inverse and determinant, with the original multiplication order, gives `Tr(H^-1 Y'* N Y')`. Substitution of the rank-one normal map gives

`|t|^2 ||z||^2 L H^-1 L* / |u|^2`.

The scalar multiplying `|t|^2` is strictly positive for every parameter: `z` and `L` are nonzero and `H` is positive definite. All entries are real analytic, so the displayed local cubic remainder follows from the first real derivative bound on a compact disk. The dual determinant-line convention in SC17 has the stated sign; `i dt wedge dbar(t)=2 dx wedge dy` accounts for its orientation and factor. Empty and full constituents have zero normal map and are explicitly excluded from the strictly positive proper-constituent coefficient.

### Both metrics and all derivative terms, SC19–SC25

The comparison operator `B=G_F^-1 H` is positive and self-adjoint in the `G_F` metric: `G_F B=H=B* G_F`. It need not be Euclidean Hermitian and no commutation of `G_F` and `H` is used. The inverse in SC22 is ordered correctly: `B^-1 G_F^-1=H^-1`.

With `Q=Pi^-1`, the ODE gives `Q'=(A+tR)Q/u`. Thus the moving target metric is `M=Q* G_N Q`, and its derivative is `M_t=Q* G_N(A+tR)Q/u`, not the same expression with the two middle factors reversed. The two first-derivative product-rule terms cancel. The complete mixed derivative has four terms,

`Y'* M_t Y + Y* M_tbar Y + Y'* M Y' + Y* M_bar Y'`,

and their sum is zero. This is the coordinate-level relation between the constant pulled-back theta Gram and the nonzero curvature measured in the fixed period target metric. The weighted projector is idempotent and weighted-self-adjoint; its normal-unit squared norm is exactly the original theta Schur complement, with positive mass retained.

### The neighboring minors, SC31–SC37

The exact basis comparison `IC=J_g` gives `H_g=C* H C`, `LC=e_last*`, and the full scalar `h_g=|det C|^2 det H`. The scalar is constant in `t`; it is not dropped from the metric equality.

The Gram determinant of `[Pi J_g,Pi e0]` is `h_g ||z||^2` by the literal lower-right Schur complement. The last diagonal entry of `H_g^-1` is `h_-/h_g` by the cofactor formula. These give the complete neighboring-minor expression `h_+ h_-/h_g^2`, including the empty determinant `h_-=1` at `p=1`.

For each original inclusion `J`, taking the determinant of `(J*G_N J)^-1 J*Pi*Pi J` gives the exact factorization `h_J=v_(N,J)b_(N,J)`. Both squared denominator factors in SC36 follow directly; none of the original source masses or frame determinants has been normalized away.

At codimension one, expansion along the final `e0` column gives `det J_+=(-1)^(q-1)`. The remaining minor has diagonal entries one. The complex determinant identity retains this sign before passing to the squared Gram determinant. SC37 then uses the already established full period determinant. This finite review does not independently evaluate that contour integral.

### Derived collision fibre, SC26–SC30

The total algebra `C[t,S]/(chi(S)-t)` is `C[S]`, with `t` acting by the original `chi`. Multiplication by the nonzero polynomial `chi'` is injective there. Monic division gives the free `C[t]` modules in SC27. The stated alternating diagonal resolution remains exact by cancellation of its two monic factors; its diagonal differential is `0,chi',0,chi',...`.

At `t=t0`, the full kernel/cokernel sequence is therefore exactly the one in SC28. On representatives, the equation `(chi-t0)v=chi' w` sends the kernel class of `v` to the annihilator class of `w`. Changing `v` by `chi' a` changes `w` by `(chi-t0)a`. Cancellation proves injectivity, the same equation proves surjectivity, and multiplication by `S` commutes with the construction. No odd/even module or nilpotent factor is discarded. The derivative's local term divisible by `x^m` is explicitly removed only after passing to the stated local quotient; the invertible remaining factor and the original local coordinate are retained.

### Period determinant inputs, SC1–SC6

The source explicitly reuses XD convergence and determinant results. This review checked the ODE's reduction sign, the retained potential and frame, and the gamma-product algebra displayed in this edition. In SC6a the root-of-unity matrix gives `|det V|^2=d^(q+1)`, and the complete power of `d` is `(q+1)+q-2q-1=0`. The displayed classical gamma multiplication formula therefore gives `(2 pi |u|)^q`. The finite checker verifies the root-of-unity Gram at `d=2,3,4`; it does not numerically integrate contours or independently establish the gamma multiplication formula.

## Independent finite fixtures

Five exact fixtures use `(q,p)=(2,1),(3,2),(4,2),(4,1),(4,3)`. Their original polynomials include a complex double root, a triple root, and two distinct double factors. None is replaced by its square-free part. All fixtures use nonreal `t`, nonreal nonzero `u`, an arbitrary invertible non-unit complex period-frame value, and a non-unit complex constituent frame.

The nonidentity Gram is the literal finite fixture's `G=7 C* C`. It is also recovered independently from a nontrivial source quotient: `B=[I,0]` and `O=[[G+v v*,v],[v*,1]]` give `(B O^-1 B*)^-1=G`. This is a finite test realization of the displayed source formula, **not a measurement of an arithmetic theta source**. The mass seven and all frame determinants are retained.

The period jets are ODE-implied jets at arbitrary invertible frame values. A separate determinant calculation multiplies truncated bivariate polynomials and sums over permutations; it derives the mixed logarithmic determinant derivative without using an inverse/trace curvature formula. This is then compared with both SC15 and SC16.

The 13 test methods cover:

1. The exact source pin and corrected SC36 powers.
2. Invariant ideals, injective inclusion, unit exclusion, and the literal top row.
3. The Hermitian projection, nonzero normal unit, signed normal map and kernel.
4. Zero normal tangent and nonzero rank-one acceleration.
5. Independent determinant jets, trace curvature, and strict positive coefficient.
6. Nonidentity source quotient Gram and the unchanged parameter-defect primitive.
7. The theta congruence, weighted projection, Schur norm, and inverse-factor order.
8. Both first-derivative cancellations and all four mixed derivative terms.
9. Neighboring minors, non-unit basis scalar, empty minor, and complex determinant sign.
10. Both original theta volume factors and both squared comparison denominators.
11. Full and empty constituents.
12. Representative-level Tor maps at a triple collision and two simultaneous double collisions, retaining nonzero `t0`, derivative scales, full kernels and `S`-equivariance.
13. The finite root-of-unity Gram and complete gamma-product power count.

Four targeted mutations change actual tested mathematics: reversing the normal-map sign, reversing the moving-metric factor order, omitting the lower neighboring minor, and multiplying the Tor representative by an incorrect scalar. Each failed the corresponding equality. These are not unconditional failure-plumbing controls. Final ordinary and optimized runs were sequential; all paired machine receipts agreed byte for byte.

## Scope and handoff

This review supplies a complete written check of the captured SC1–SC37 formulas and exact finite checks of the specified maps. It supplies no new Lean execution, no contour evaluation, no interval-certified numerical value, no uniform arithmetic estimate, and no remote publication. It does not certify a later changed owner edition. The inherited analytic contour/determinant results remain attached to their own XD proof provenance.
