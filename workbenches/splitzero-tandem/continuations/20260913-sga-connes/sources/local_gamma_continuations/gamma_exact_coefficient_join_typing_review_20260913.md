# Independent source, coordinate, cochain, and determinant review

The inspected standalone chapter is `work/gamma_exact_coefficient_join_20260913.tex`, 40,111 bytes, final SHA256 `270d7f89e6ac2b147fdbdb5d223125b3744239d43c5485c53740c47ed8d223ec`. The GC.1–GC.9 and GC.38–GC.59 proof text was read directly and completely, including the revised endpoint conventions and support carrier, at the preceding hash `ef6a252b14d386b8fc063d22d1fbd0c9868b63fe66f25a88c7b2efc00e4ab8dc`; the subsequent Cauchy-bound wording identifying the kernel derivative was then read directly and the final file hash verified. GC.10–GC.37 was also read directly to establish the definitions and coefficient identities used by the assigned range. The independent analytic-generating review of GC.24–GC.30 belongs to a separate reviewer; this report does not represent that review as its own work.

Result: the assigned mathematical claims are valid with the written hypotheses and exact index domains. The author installed the concrete corrections below before this source pin. No unresolved mathematical defect was found in the assigned range. This is a source review with explicit finite algebraic tests; it does not certify a growing-packet estimate, actual zero locations, an interval calculation for a chosen packet, or the visual layout of the cumulative PDF. This reviewer did not edit the chapter, cumulative sources, publication stage, or frozen editions.

## 1. Repairs verified in the final source

The first inspected draft omitted the index conventions at the bottom of the Toda induction. The final version sets `p_{-1}=0`, `a_0=0`, and `c_0=0`; states the norm ratio and polynomial derivative for `j≥1`; proves the derivative of `p_0=1` separately; and restricts the determinant quotient containing `D_{n-1}` to `n≥1`. These are needed because `D_{-1}` and `h_{-1}` are not defined.

The first draft claimed that a fixed finite coefficient list does not determine a nonzero-tilt value, without proving such non-determination inside the restricted class of actual zero packets. The final version states exactly what is established: GC.42 gives each zero-tilt derivative from a finite list, and GC.43 gives the all-orders Taylor map and analytic continuation to the full strip. No unsupported uniqueness or non-uniqueness claim remains.

The final support paragraph now defines the carrier, the linear support lift, the supported zeros, and preservation of identities and composition. Its assertion about the image of a relation therefore has an explicit domain and target. The observed TeX defects in GC.2, GC.5, GC.15, GC.33, and GC.38 have also been corrected in the pinned source.

## 2. GC.1–GC.5: exact source and seed constants

The scalar coordinates are `s=1/2+it` and `S=k/2+iu`, where `u=Σt_i` and `k≥1`. For the conjugate-linear-first convention, the first Gram factor is consequently `(c−iu)^i`, with `c=k/2`, not `(c+iu)^i`. Coefficientwise conjugation and evaluation conjugation are explicitly distinguished by the identity `overline(P(c+iu)) = overline P(c−iu)`.

For `D=−x∂_x`, the domain `V` consists of even Schwartz functions satisfying both `φ(0)=0` and `∫φ=0`. The target `B` imposes rapid bounds at both multiplicative ends under every nonnegative power of D. For any `A>1` and `x≥1`, the Schwartz bound gives

`Σ_{n≠0}|D^jφ(nx)| ≤ C_A x^(−A) Σ_{n≠0}|n|^(−A)`.

Poisson summation gives `Θφ(x)=x^(−1)Σ_{n≠0} φhat(n/x)`, because both zero terms vanish by the two stated conditions. Applying the same bound with `1/x≥1` proves an arbitrarily high positive power of x at zero. The evenness and Schwartz properties are preserved by D. Integration by parts gives `∫Dφ=∫φ=0`; evaluating `−xφ'(x)` at zero gives zero. Thus `D:V→V` is defined and `DΘ=ΘD:V→B` is a genuine chain map on the complex in degrees zero and one.

For `F∈B`, the integrand `F(x)x^(s−1)` and every logarithmic s derivative are absolutely integrable locally uniformly in s. This proves an entire Mellin transform. The boundary term in `∫(−xF')x^(s−1)dx` is `−F(x)x^s|_0^∞=0`, giving the exact sign `M(DF)=s MF`.

Direct differentiation of a Gaussian gives

`D(D−1)e^(−πx²)=(4π²x⁴−6πx²)e^(−πx²)`.

The two whole-line Gaussian integrals are each 3, so the seed belongs to V. The n=0 term of the theta sum is killed by `D(D−1)`. The Fourier convention retains `2π`, and its Gaussian Fourier transform is exactly `e^(−πy²)` with value 1 at zero. Poisson inversion therefore gives `θ(1/x)=xθ(x)`. For `RF=x^(−1)F(1/x)`, direct differentiation yields `DR=R(1−D)`; substituting twice yields `D(D−1)R=RD(D−1)`. Hence `f_0(1/z)=z f_0(z)` has precisely the orientation and factor written in GC.4.

For `Re s>1`, the n and −n terms contribute a factor two and `y=πn²x²` contributes a factor one-half. Their product is one, leaving

`π^(−s/2)ζ(s)[4Γ(s/2+2)−6Γ(s/2+1)]`.

The bracket equals `[4(s/2+1)(s/2)−6(s/2)]Γ(s/2)=s(s−1)Γ(s/2)`. Thus the seed transform is `g=2ξ`, with no missing factor two or sign. The integral, rather than an assumed continuation of an interchange outside its domain, supplies the entire extension.

## 3. GC.6–GC.9: analytic quotient, inverse Mellin map, and strip

The selected multiplicity hypothesis is essential and is present: each selected zero is used at its entire order. If `g(s)=(s−ρ)^m a_ρ(s)` with `a_ρ(ρ)≠0`, division by the packet removes the factor `(s−ρ)^m` exactly. The other packet factors are nonzero at ρ. Therefore `v_h=g/h` extends holomorphically at ρ and is nonzero there. It is a nonzero entire function.

On a closed narrower sector `|arg z|≤β<π/4`, every fixed derivative of the theta seed decays faster than any inverse power at infinity. The inversion identity gives the corresponding bound at zero. For `t≥0`, rotating the Mellin contour to `z=e^(iβ)x` contributes `e^(iβs)`, whose modulus is `e^(−βt)`; for `t<0`, the opposite ray contributes `e^(βt)`. The two circular arcs vanish at both ends uniformly on a bounded interval of `Re s`. Repeated logarithmic integration by parts supplies every requested polynomial power. At large |t| the monic packet has a positive constant times `|t|^d` as a lower bound, uniformly on that same interval. The remaining compact rectangle uses the analytically cancelled quotient. These facts prove exactly GC.6, without an unstated estimate for an uncancelled singular expression.

The `1/(2π)` in GC.7 is Fourier inversion in `log x`, under the Mellin convention already fixed. Entirety and the uniform vertical bounds make the horizontal sides of the contour rectangle tend to zero. Hence the inverse is independent of σ. Differentiating by D inserts the factor `σ+it`; the integral remains absolutely convergent for every power. For `x→∞`, taking σ arbitrarily large gives arbitrarily fast decay. For `x→0`, taking σ arbitrarily negative gives arbitrarily fast vanishing. Thus `F_h∈B`. Mellin injectivity then proves `h(D)F_h=f_0=Θφ_0` on the actual source, rather than defining that equality as a quotient convention.

Squaring the GC.6 bound proves integrability of `|t|^j e^(θt) w_h(t)` on any compact substrip of `|Re θ|<π/2`: choose β strictly between half that compact real width and `π/4`. Domination proves holomorphy and the derivative formula in GC.9. The factor `1/(2π)` remains in the density. Nonzero entire `v_h` has only isolated zeros on the vertical line, so the density is positive almost everywhere and its total mass is strictly positive.

## 4. GC.38–GC.43: original S map and exact finite coefficient indices

Let `L_{aj}=binom(j,a)c^(j−a)i^a` for `a≤j`. This is the coefficient map from an S-polynomial to the same polynomial evaluated at `S=c+iu`, written in the u basis. Its column j is the full binomial expansion of `(c+iu)^j`. For coefficient vectors p and q, the integral of `overline(p(c+iu))q(c+iu)` therefore equals `p*L*HLq`. This proves the congruence `M=L*HL` with the actual conjugate transpose and the original translation c.

The diagonal entries of L are `1,i,…,i^N`, so `det L=i^(N(N+1)/2)`. Thus `det M=overline(det L) det H det L=det H`. The equality of determinants follows from the proved coordinate map; no entrywise identity of the two matrices is asserted. These formulas also hold entrywise at complex tilt because L is a constant matrix; positive definiteness is used only at real tilt, as the chapter states.

For `r≥0`, the polynomial

`u^r(c−iu)^i(c+iu)^j`

has degree `i+j+r`. Expanding in the monic real-coefficient family `b_n^(kλ)` is an invertible triangular operation on polynomials of that degree. The finite moment identity GC.23, obtained by the product generating coefficient and Fubini, is

`∫b_n^(kλ)(u)m_{h,k}(u)du = c_λ^k n! d_{h,k,n}`.

Consequently the derivative in GC.42 has exactly the coefficient `e_{ijr,n} n! d_{h,k,n}` and the full mass factor `c_λ^k`. The upper index is `i+j+r`, and its largest value over the N-degree Gram is `2N+r`. The finite convolution formula for d uses only indices whose sum is n, so no one-factor coefficient beyond `c_{h,2N+r}` enters. This is exact for each derivative.

For `|θ|<π/2`, the absolute exponential series is `e^(|θ||u|)`, integrable against the absolute polynomial integrand by GC.6. Tonelli applied to that majorant and dominated termwise integration prove the all-orders identity GC.43. Its disc is contained in the full holomorphic strip. On the rest of the strip the original Laplace integral defines the unique analytic continuation. This proves an exact map from the full coefficient sequence to the tilted entries while making only the stated finite-jet claim for a finite list.

## 5. GC.44–GC.48: local unit, cyclic annihilator, and cochain sign

For a nonempty packet, the algebra `E_h=C[s]/(h)` is finite-dimensional and nonzero. The powers of `a=s_1+…+s_k` in `E_h^⊗k` are linearly dependent, so the kernel ideal of `C[S]→E_h^⊗k` is nonzero. Its unique monic generator χ has degree at least one, because the image of the constant one is the nonzero tensor unit. The induced map `C[S]/(χ)→E_h^⊗k` is injective by its defined kernel.

At each local factor, write the full jet of `v_h` as `v_0+n`, where `v_0≠0` and n lies in the nilpotent maximal ideal of order m. Its inverse is the finite expression

`v_0^(−1) Σ_{j=0}^{m−1}(−n/v_0)^j`.

The Chinese remainder product therefore makes the complete residue `υ_h` a unit. Tensoring the multiplication isomorphism retains every nilpotent coefficient. Multiplication by `υ_h^⊗k` composed with the proved cyclic injection gives GC.44. The tensor Mellin transform of GC.45 is `P(Σs_i)∏v_h(s_i)`; taking the same complete local jets yields exactly that arithmetic injection composed with the monic quotient. There is no modulus-squared map in this jet calculation.

Successive monic division first in `s_1`, then in `s_2`, and so on gives a final remainder of degree less than d in every variable. Its tensor-algebra residue is zero because χ annihilates a. Those remainder monomials are a basis of the tensor algebra. Thus the remainder polynomial is literally zero, proving `χ(Σs_i)=Σh(s_i)Q_i` with the specified division order.

In the tensor cochain complex, a summand with φ_0 in factor i and F_h in the other factors has total degree `k−1`. The first `i−1` factors all have degree one. Its sole nonzero differential therefore has the Koszul sign `(−1)^(i−1)`, which multiplies the same sign written in GC.47. D is a degree-zero chain map by Section 2 above, so it commutes with that differential and with the other factor operators. Applying the differential leaves `h(D_i)F_h` in factor i, by GC.8. Summing the proved polynomial identity yields GC.48, with a positive boundary sign and domain degree `k−1`, target degree k. This also covers `k=1`, whose primitive has degree zero and no alternating sign.

## 6. GC.49–GC.54: finite relation space and canonical section difference

For `N≥q−1`, set `m=N−q+1`. A polynomial of degree at most N is divisible by χ exactly when its multiplier has degree at most `N−q=m−1`. Monicity makes multiplication injective; the first q monomials map onto the quotient. This proves the exact sequence with source relation dimension m, middle dimension `N+1=q+m`, and quotient dimension q.

The original multiplication matrix B has entries `[S^i](χS^j)`, dimensions `(N+1)×m`, and no tilt dependence. Thus differentiating `B*MB` differentiates only M. Its integrand is `u^r overlineχ(c−iu)χ(c+iu)(c−iu)^i(c+iu)^j`. For `0≤i,j<m` its degree is at most `r+2q+2(m−1)=r+2N`. The upper index agrees with the source derivative. At m=0 there are no relation entries; the empty Gram determinant is one and no inverse of it is required.

At real admitted tilt, positivity of M and surjectivity of J imply positivity and invertibility of `JM^(−1)J*`. With `G=(JM^(−1)J*)^(−1)` and `R=M^(−1)J*G`, direct multiplication gives `JR=I`. For `z∈ker J`,

`z*MRv = z*J*Gv = (Jz)*Gv = 0`.

Every other section value differs by a relation vector. The squared norm is the orthogonal sum of the minimum lift norm and that relation norm. This proves the minimum property and its uniqueness in each original metric.

For m>0, `K=(B*M_hB)^(−1)B*M_hR_Γ` has type `C→C^m`; identify its output with the polynomial multiplier of degree at most `m−1`. Then `J(R_Γ−BK)=I`, and multiplication by `B*M_h` gives zero. Uniqueness of the arithmetic minimum section yields `R_h=R_Γ−BK`. In particular the sign in GC.53 is negative. Applying the linear analytic polynomial map yields

`V(R_hu_0−R_Γu_0)=−V(χκ_{u_0})=d_tot(−P_{χ,h,k}(κ_{u_0}))`.

The rightmost primitive has degree `k−1`; its displayed differential has degree k. This is the exact comparison of the two actual sections before passing to the quotient. At `N=q−1`, both sections are the unique degree-less-than-q representatives, their difference is zero, and the specified zero K has a zero-dimensional target.

The final carrier is explicitly ` {τ} ⊔ ⨆_ℓ({ℓ}×E_ℓ)`. A family of linear maps gives `τ↦τ` and `(ℓ,v)↦(ℓ,L_ℓv)`. Composition follows by substituting `L'_ℓL_ℓv`; the identity follows by substituting `I v`. A vector in the kernel of the original quotient goes to `(ℓ,0)=e_ℓ`, whereas external absence goes to τ. This proves the claimed support morphism without identifying e with τ or discarding the original relation vector.

## 7. GC.55–GC.59: determinant orientation, all indices, and Toda induction

The quotient-first column list is `1,S,…,S^(q−1),χ,χS,…,χS^(m−1)`. The degrees are successively `0,…,N` and the leading coefficients are all one, so its coefficient matrix is triangular with determinant one. Each minimum section column has the same quotient as its corresponding initial monomial. Replacing that column only subtracts a relation-column combination and leaves the determinant one. The new source Gram is block diagonal with quotient Gram G and relation Gram B. Taking determinants therefore proves

`det M = det G det B`, and `V_N=D_{N+1}/B_{N−q+1}`.

Repeating the same argument in the reference metric and dividing gives GC.55 with `T_N=X_{N+1}/Y_{N−q+1}`. At `N=q−1`, the denominator is `B_0=1`; no degree-`q−2` full quotient is introduced.

For the positive real-tilted u measure, let p_j be monic orthogonal polynomials and h_j their norms. The degree-zero conventions in the final source make all expressions well typed. For j≥1, pairing `up_j` with `p_{j−1}` gives `a_j=h_j/h_{j−1}`. Differentiating h_j and using that `∂_θp_j` has degree at most `j−1` gives `h'_j=b_j h_j` for all j≥0. Differentiating its orthogonality to degrees ≤j−2 yields zero pairings for `∂_θp_j`. The pairing at degree `j−1` is `−h_j`, so `∂_θp_j=−a_jp_{j−1}`. Together with `p_0=1`, this gives `c'_j=−a_j`, `b_j=c_j−c_{j+1}`, and `b'_j=a_{j+1}−a_j`, including j=0 under the written conventions.

For n≥1, the logarithmic derivative telescopes:

`(log D_n)''=Σ_{j=0}^{n−1}b'_j=a_n=D_{n+1}D_{n−1}/D_n²`.

The n=0 determinant is separately one. The reference n=1 determinant is `c_λ^k(cos θ)^(−kα)`. For the proposed reference determinant,

`D_n^Γ=c_λ^(kn) [∏_{j=0}^{n−1}j!(kα)_j](cos θ)^(−n(kα+n−1))`,

the second logarithmic derivative is `n(kα+n−1)sec²θ`. Its consecutive determinant ratio is the same expression: the mass factors cancel with exponent zero, the factorial/Pochhammer ratio is `n(kα+n−1)`, and the cosine exponent is −2. Given the exact values at n=0 and n=1, the determinant identity computes the next D uniquely as `D_n² (log D_n)''/D_{n−1}`. Positive induction proves all n. Thus GC.56 is not an unproved ansatz for the tilted moments.

In GC.57, replacing multiplication by u by `∂_θ` inside the original absolutely convergent Laplace integral gives the weight `overlineχ(c−iu)χ(c+iu)r_{λ,k}(u)`. Applying `∂_θ^(i+j)` gives its u moment of degree `i+j`. The relation analogue of L maps its u basis to the original S multiplier basis and has determinant of modulus one. The determinant in GC.57 is therefore exactly the original S relation determinant, including complex coefficients of χ.

For zero tilt, the norm ratio `a_{N+1}=D_{N+2}D_N/D_{N+1}²` divided by its reference has factor `Q_N=X_{N+2}X_N/X_{N+1}²`. Substituting GC.56 gives `(N+1)(N+kα)Q_N`. The adjacent-volume identity requires both `V_{N−1}` and `V_{N+1}`; hence its domain is `N≥q`, exactly as written. The single-volume logarithmic derivative requires only `N≥q−1` and is GC.59. Each logarithm there is of a positive real-tilt determinant, so its differentiation introduces no complex branch choice.

For h=1, the quotient is the zero algebra and χ=1. Multiplication by χ is the identity on each source degree, so `B_{N+1}=D_{N+1}` and all zero-dimensional quotient volume determinants equal one. The quotient section and correction have zero-dimensional domain. The analytic density and its original mass remain nonzero. Per support fibre, the zero vector space still gives the two distinct carrier elements τ and e. These statements use no nonexistent packet unit or positive-dimensional quotient in the empty case.

## 8. Independent exact fixtures and counterexamples to wrong signs

`work/gamma_exact_coefficient_join_typing_fixtures_20260913.py` has SHA256 `b87b189da75b5847ab0a5cace29ec00cb290a26e9c269c2daf3bb4efdac2710a`. It completed with exit zero both normally and under Python optimization. Each execution produced 37 exact checks and the same two rejected wrong-formula controls. The normal receipt `work/gamma_exact_coefficient_join_typing_fixtures_20260913.json` and optimized receipt `work/gamma_exact_coefficient_join_typing_fixtures_20260913_optimized.json` both have SHA256 `5ec693cb1492f7e6192533532c58c98913b2a7b7d94f58079e58e83ac3d479f2`. The checker uses explicit exceptions, so optimization does not disable its tests.

The positive-measure fixture has `λ=1/2`, `k=2`, `c=1`, `N=3`, and polynomial `χ=(S−1)²−2`. Its one-factor reference transform is sec θ; multiplying that density by `1+t²` gives transform `sec θ+(sec θ)''=2 sec³θ`. The original two-factor sum transforms are therefore `sec²θ` and `4 sec⁶θ`. All moments used by the tests are exact series derivatives. The changed source mass is four and is retained. The fixture verifies all sixteen original S-integrand entries, the full congruence determinant phase, original multiplication and quotient columns, minimum sections, relation orthogonality, determinant ratio, and zero-column endpoint. The resulting nonzero correction matrix is

`K = [[23/259, 131261/2283085], [0, 276/8815]]`.

It proves within this exact fixture that replacing `R_h=R_Γ−BK` by the positive-sign version fails: `R_h−R_Γ−BK=−2BK` is a nonzero matrix. This is a formula counterexample with the source and target fixed, not a claim that the two sections are unrelated.

A separate nonreduced algebra fixture uses `h(s)=(s−1)²(s−2)`, k=2, and `χ(S)=(S−2)³(S−3)²(S−4)`. Successive monic division gives zero remainder. Direct companion tensor matrices show that χ annihilates the sum action and that the first six sum powers applied to the tensor unit have rank six. Thus all displayed nilpotent orders and the degree-six cyclic injection are exercised. Multiplication by the complete local unit `υ=2+s` has determinant 36 and retains rank six after tensor multiplication.

A three-factor fixture uses `h(s)=(s−1)²` and `χ(S)=(S−3)^4`. Its successive divisions have zero final remainder, and the written primitive signs cancel the tensor differential signs exactly. Omitting the primitive signs leaves a nonzero discrepancy. This tests the middle negative sign in an actual three-factor polynomial identity.

All fixture centres and relation polynomials are declared algebra/positive-measure test inputs. None is asserted to be an actual zeta zero packet. The general claims are supported by the proofs above; these finite checks are supplementary and specifically exercise the original coordinates, full masses, nilpotent structures, and signs.

An independently delegated determinant review also completed 32 exact checks for k=3, λ=1/4, c=3/2, tan θ equal to 0 and 1/2, source sizes 1–4, quotient degrees N=1–3, and the empty packet at N=0–2. It retained the full reference mass symbolically and used the complex relation `χ=S²+(1+2i)S+(3−i)` to exercise conjugation. Its inspected proof concerns GC.55–GC.59; the final index repairs above were checked again by this reviewer in the pinned chapter. The exact executed code was preserved as `work/gamma_toda_index_check_20260913.py`, SHA256 `8f48e6361e619b98ecd5e41e33b26428fffc1b48ee5f54b08395374e21c016aa`, and its prior observed execution is recorded in `work/gamma_toda_index_check_20260913.json`, SHA256 `3b162f3cbdc883d5e480f2d2a079dd6e8c5d2c38cbd90a90b6a0130a585f9fd5`. Both files were read directly by this reviewer. This particular preserved script uses assertions and must run without `-O`; its receipt claims only the actual normal run. It is not counted as an optimized or mutation-tested checker.

## 9. Complete inspection of the author's finite checker and its fourteen runs

The complete source `work/gamma_exact_coefficient_join_check_20260913.py`, SHA256 `76c8d17278b976e06ddf2c15e94c8b476dbf67dd47af9d54bd15df6a677bcaec`, was read. It produces exactly 143 records: 27 generating-coefficient/mass identities, 2 finite inverse-series identities, 16 original-coordinate/determinant-phase identities, 81 finite Gram-derivative identities, 8 ordered-division/cochain identities, and 9 section/quotient/volume identities.

The generating tests compare recurrence polynomials with independently expanded `c_λ^(−1)(1+z²)^(−α/2)M(arctan z)` through degree seven at three distinct α values. The finite Gram tests use generic moments, form the exact finite coefficient power, and compare it with the multinomial convolution-moment expression for k=1,2,3 and i,j,r=0,1,2. Thus the two calculations have different representations. The largest tested derivative polynomial has degree six. The abstract complex positive Gram fixtures verify section and volume algebra at N=1,2,3; their matrices are declared fixtures, not claimed gamma moment matrices. The checker does not claim to test the infinite-strip analyticity, convergence, or actual zero packet values.

Each of the six mutation options changes a displayed formula inside its normal calculation and selects one record of the same 143-record suite. The factorial mutation multiplies the degree-four coefficient by its factorial a second time. The mass mutation removes the symbolic reference mass divisor. The coordinate mutation reverses the powers of i in the original S substitution. The phase mutation reverses the determinant phase. The derivative mutation deletes the highest required degree at i=j=r=2. The cochain mutation reverses the middle primitive sign for k=3. All selected expressions are nonzero generic polynomial discrepancies, so these controls test formula content.

The actual execution receipt `work/gamma_exact_coefficient_join_build_20260913/checks/replay_receipt.json`, SHA256 `faceb7c8c2a385b0260ebb306ec2c00f3c94c8e78f84c2f77bf4e2a1f4133701`, was read completely. Its fourteen stored result files and fourteen stored log files were independently opened and compared to their recorded hashes. For every result, all 143 unique record names were inspected by the verification script; the failed names were recomputed from the actual record booleans and compared with the expected mathematical mutation and the declared failed-name list. The normal and optimized runs have zero failures and recorded exit zero. Each of the six mutations in each mode has precisely its one intended failure and recorded exit one. The passing records are identical across normal and optimized modes, as are corresponding mutant records.

The independent inspection is reproducible using `work/gamma_exact_coefficient_join_replay_review_20260913.py` and its emitted `work/gamma_exact_coefficient_join_replay_review_20260913.json`. That script completed with exit zero. It reads the actual source/result/log hashes and verifies the record cardinalities, uniqueness, selected mutation flags, exact failure names, and recorded exit codes. It does not claim to have launched a second set of fourteen author-checker executions. There is no new Lean run or arithmetic interval certificate in this review.
