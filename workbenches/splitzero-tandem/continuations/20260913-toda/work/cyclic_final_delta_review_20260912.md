# Independent final cyclic delta review — 12 September 2026

Scope: the added CV.11–CV.12 calculation, E33–E36 quartet and canonical-measure calculation, and cumulative R26–R32. Earlier CV.1–CV.10, E1–E32 and CC results were already independently reviewed; I read their definitions and the exact portions needed to recompute the new uses. This report is a mathematical derivation, with no Lean execution, numerical certificate, or renewed claim about the earlier source audit. No manuscript or build input was modified by this reviewer.

The source hashes at initial review were:

- `work/cyclic_control_determinant_increments_20260912.tex`: SHA256 `d597d88b84d2e9eee502863c362a65d3f30997ba954bd44e393c040d8984d6c5`.
- `work/exterior_trace_equality_continuation_20260912.tex`: SHA256 `313c321537673bf629e10a673daaacd5d74d234efcaadee0210a8c56909a921e`.
- `output/split_zero_rh_tandem_2026-09-12/tex/research_conclusion.tex`: SHA256 `08cab9a1979f58697f04cba10c3ab49f84a6a3bd7f2a45d6c25ea788f0409874`.
- Supporting CM text `work/cyclic_sum_metric_connection_20260912.tex`: SHA256 `7f58291e609995d05f99249a19d8835d2e12c7c7c182b1890b9a4d158511bb3c`.

## Result and two requested precision repairs

The new numerical constants, algebraic signs, exact quartet degree threshold, canonical Gram calculation, and literal exterior factorials are correct. Two local clarifications were sent to the root before sealing:

1. In CV.12, the displayed sum of the `b_j` is the **cyclic reduction** of the projected polynomial. Its actual full arithmetic jet is the image of that vector under the already defined map `eta = U_k alpha`. Writing both typed equalities makes the comparison exact rather than leaving “finite jet” ambiguous.
2. The new R26 subsection should explicitly retain `k >= 2` for the full relative-fibre limit and `d = deg h >= 1` for the nonzero relation observation. NN deliberately includes the empty packet `h=1`; there the arithmetic target is zero and this observation is zero. The nonzero argument written in R26 treats exactly `d=1` and `d>1`.

These are scope and map-typing repairs; they change no displayed arithmetic identity. A final delta check can record their installation without repeating the entire review.

## CV.11–CV.12: direct recomputation in the original form

Write `P_N` for the original polynomial space of degree at most `N`, with the original integral form on `S=k/2+iu`; use the monic orthogonal basis `p_j` and its squared norms `omega_j > 0`. Let `q=deg chi >= 1`, `C=C[S]/(chi)`, and `T_{q-1}:P_{q-1}->C` be polynomial reduction. The vectors `b_j=T p_j`, for `0<=j<q`, form a basis because their coordinate matrix `B` in the fixed monomial remainders is triangular with diagonal one. Thus

`K = B diag(omega_j^{-1}) B*`, and `G = B^{-*} diag(omega_j) B^{-1}`.

Multiplying on the left by `B*` and the right by `B` gives `b_i* G b_j = delta_ij omega_j`. This proves the stated canonical-section identity using the original source norms, without assigning mass one or changing the remainder coordinates.

Both `chi` and `p_q` are monic of degree `q`, so their difference has degree at most `q-1` and has a unique expansion `sum gamma_j p_j`. Taking the integral pairing with `p_j`, conjugate-linear in its first argument, yields exactly

`gamma_j = integral conjugate(p_j) chi m / omega_j`.

Reduction gives `b_q=-sum gamma_j b_j`. Hence with `N=q-1` the original definitions imply

`a=omega_N`, `c=b_N*G b_q=-gamma_N omega_N`, and `d=b_q*G b_q=sum |gamma_j|^2 omega_j`.

Substitution in `epsilon^2=(ad-|c|^2)/omega_N^2` cancels exactly the `j=N` summand and gives

`epsilon^2 = sum_{j=0}^{q-2}|gamma_j|^2 omega_j / omega_{q-1}`.

Orthogonality of `p_q,p_0,...,p_{q-1}` separately gives

`||chi||^2 = omega_q + sum_{j<q}|gamma_j|^2 omega_j`,

which proves the second CV.12 expression with both subtraction signs as written. Since `omega_N` is a strictly positive real number, `Re(c)=0` entails `Re(gamma_N)=0`, not a license to delete that coefficient. For `q=1`, the projection space is `P_{-1}=0`; the sum is empty and the control is zero as stated.

The original projection `P_{q-2}` satisfies `P_{q-2}chi=sum_{j<q-1}gamma_j p_j`. The complete typed source diagram is

`P_{q-2}chi -> T(P_{q-2}chi)=sum gamma_j b_j in C -> eta(sum gamma_j b_j) in E_h^{tensor k}`,

where the last vector equals `J^{(k)} V_{h,k}(P_{q-2}chi)`. The original source isometry gives `||V_{h,k}P_{q-2}chi||^2=sum_{j<q-1}|gamma_j|^2 omega_j`. Meanwhile `T chi=0` and `J^{(k)}V_{h,k}chi=eta(0)=0`. Since `eta` is injective for a nonempty packet, the two displayed observations vanish together, but their domains and codomains remain different.

For completeness, if fixed-order monic division gives `chi(S)=sum_i h(s_i)Q_i`, its actual tensor primitive is the sum of `Q_i(D_1,...,D_k)` applied to the original tensor with `F_h` in every factor except factor `i`, where it has `(-1)^{i-1}phi_*`. The differential on that factor contributes its own `(-1)^{i-1}` because the preceding `i-1` factors have degree one. Their product is `+1`, and `h(D)F_h=Theta phi_*` gives the boundary `+V_{h,k}chi`. The projection polynomial need not remain in the relation ideal; the explicitly computed full jet above retains precisely that change.

## E33–E34: exact quartet sums, local lengths, and thresholds

Let the four distinct roots be `1/2 + epsilon delta + i eta gamma`, with `delta,gamma>0`, each of order `m`. An ordered `k`-tuple has margins `a` equal to the number of positive real signs and `b` equal to the number of positive imaginary signs. The four occupation numbers are `(t,a-t,b-t,k-a-b+t)`. Their nonnegativity is exactly

`max(0,a+b-k) <= t <= min(a,b)`.

For every `0<=a,b<=k` this interval contains an integer: if `a+b<=k`, use zero as lower endpoint; otherwise `a+b-k<=a,b` since both margins are at most `k`. Thus every grid point occurs. Equality of two complex sums implies both `delta(2a-2a')=0` and `gamma(2b-2b')=0`, hence both margins agree. The distinct sum set therefore has exactly `(k+1)^2` elements, regardless of collisions between occupation vectors with the same margins.

On each ordered CRT local factor the sum nilpotent is `z_1+...+z_k` with `z_i^m=0`. Its power of degree `k(m-1)` has the unique surviving exponent vector `(m-1,...,m-1)` and nonzero coefficient `(k(m-1))!/((m-1)!)^k`. The next power vanishes because one exponent must be at least `m`. Its nilpotency length is exactly `ell_k=1+k(m-1)`. All factors at a fixed sum have this same length, so the cyclic minimal polynomial has that exponent at every grid point. Consequently `q=ell_k(k+1)^2`, and the actual full cyclic interpolation map is admitted for `N>=q-1`.

At each grid point the real defect is `2 Re(lambda_{a,b})-k=2 delta(2a-k)`. Its positive part occurs exactly for `a>k/2`. For even `k=2n`, the sum of `2a-k` over those margins is `2(1+...+n)=n(n+1)`; for odd `k=2n+1` it is the sum of the first `n+1` positive odd integers, namely `(n+1)^2`. These are both `floor((k+1)^2/4)`. Multiplication by the number `k+1` of imaginary margins, the full block length `ell_k`, and `2 delta` proves E34 with its exact factor.

For even `k` and `m>1`, the `a=k/2` blocks have real part `k/2` and length `ell_k>1`; multiplication by `S` on each cyclic local ring `C[X]/(X^{ell_k})` has one full Jordan block of that length. Since `L>0`, the previously proved E24–E25 result applies and makes the inequality strict at every admitted degree. For a larger packet the original ordered quartet local factors are retained CRT summands. Their lengths can only be increased by the maximum over further factors at the same sum. Thus this quantity remains a lower bound, but the admission degree is the actual `deg chi_{h,k}-1`; no equality for the larger packet degree follows.

## E35–E36: canonical positive-measure equality example

Retain the stated mass `mu`, scale `sigma`, vertical coordinate `S=1/2+iu`, and Gaussian measure. Its mass, first moment and second moment are `mu,0,mu sigma^2`. Therefore `p_0=1`, `p_1=iu`, `p_2=(iu)^2+sigma^2` are the original monic orthogonal polynomials through degree two: orthogonality against `1` uses the second moment, and orthogonality against `iu` uses the odd moments. In particular `omega_0=mu`, `omega_1=mu sigma^2`.

For `chi=(S-1/2)^2-sigma^2`, reduction gives `b_2=2 sigma^2 b_0`. The fixed coordinate matrix `B=[[1,-1/2],[0,1]]` and the canonical Gram written in E35 thus give `a=mu sigma^2`, `d=4mu sigma^4`, and `c=0`. Hence `epsilon^2=4sigma^2`. There is one positive root `1/2+sigma`, with defect `2sigma` and multiplicity one, so `L=2sigma=epsilon`. This is a valid specified canonical moment example; it asserts no identification of its roots or measure with the arithmetic ones.

## R26–R32: propagation of maps, metrics, and exterior data

For the literal constant frame inclusion `E_{LM}`, differentiation of `j_LE_{LM}=j_M` followed by the definitions `j'=j Gamma+N` gives `N_M=j_L(Gamma_LE-E Gamma_M)+N_LE`. Since `j_L*N_L=0`, taking the original Gram gives exactly R26. Its tangent contribution has a plus sign and retains the complete `W_L` form. The density limit concerns `k>=2` and each fixed source. It supplies no uniform bound for a varying minimum representative.

For `d>=1`, the relation `sum_i h(s_i)` is in the original ideal, and differentiation of the full amplitude unit kills its term multiplied by that relation after reduction. What remains is `(U_k/k) sum_i[h'(s_i)]`. At `d=1`, the sum is the scalar `k`; at `d>1`, the standard monomials `s_i^{d-1}` are distinct and have nonzero coefficient `d`, so the vector is nonzero. Multiplication by the retained unit preserves nonvanishing. At `h=1`, the target is zero instead. These cases require the explicit domain qualification noted above.

R27 is the exact congruence identity for the original two positive forms: insert `B_M=G_*^{-1/2}G_MG_*^{-1/2}` into its displayed quadratic expression to obtain `x*G_Mx`. The minimum construction gives `G_M<=G_*` through inclusion of admitted sources. Neither this ordering nor the fixed-source normal limit supplies an estimate of the varying `B_M`.

R28 retains the local exponents, invariant target, and unit-twisted retraction from CC. The quoted derivative formula includes both the cyclic and complementary components. For the operator decomposition, let `Q_r=I-eta_r Pi_r`. A quotient action on `A_r/eta_r C_r` is defined exactly when `M eta_r C_r` is contained in `eta_r C_r`, equivalently `Q_r M eta_r=0`. This is precisely the lower-left-zero criterion in R28. Its lower-right block is always a compression, and becomes the induced quotient operator exactly under that criterion. The trace remains the sum of both diagonal compressions, with the cross maps retained.

For R29, the unscaled alternating tensor has inner product `p! det(<v_i,w_j>)`: expansion of both alternating sums gives `p!` identical determinant contributions. Therefore the representative Gram and its control form both carry the same literal `p!`, which cancels only in the numerical operator allowance, not in the specified forms. The additive exterior action of a Hermitian defect with eigenvalues `epsilon,-epsilon,0,...,0` has eigenvalues that are sums of distinct entries, hence lies between `-epsilon` and `epsilon`. On the determinant line of the full positive generalized subspace the additive multiplication eigenvalue is its full trace, including all nilpotent block dimensions, giving R29.

The original block primitive has summands `(-1)^{k(j-1)} R^{tensor(j-1)} tensor K^{prim} tensor R^{tensor(p-j)}`. Each preceding `R` factor is in degree `k`; applying the tensor differential to its single primitive factor produces the same sign. The product is `+1`; differentials on all other, top-degree factors vanish. Thus its boundary is exactly the additive generator difference in the original source. A cochain idempotent commuting with the differential gives inverse maps `x -> (ex,(1-e)x)` and `(u,v)->u+v`, and therefore splits cohomology. An ordinary trace is asserted only on the explicitly retained finite invariant arithmetic packet.

R30 uses precisely the counted quartet formula above and states the larger-packet threshold correctly. R31 copies the proved original-metric slack and Sylvester maps with their correct signs: the block commutation equation for `Q=[[I,X],[0,0]]` is `BX-XD=T`, and differentiating `e^{-tB} T e^{tD}` gives minus its Sylvester image. Integration from zero to infinity therefore gives `BX-XD=+T`. The strict real spectral gap ensures convergence even with all finite nilpotent polynomial factors. The equivalence `L=epsilon <=> P=Q <=> T=0` retains its `L>0` qualification.

Finally, the four Gram determinants in R32 have coefficients `+,+,-,-`. Expanding each by the finite column determinant identity cancels subsets containing neither special index and subsets containing exactly one, and retains exactly those containing both `N,N+1`. This proves the displayed positive minor sum, including the first admitted degree where the smaller Gram is singular. The adjoint exterior source vector has squared norm `Delta_N`; applying the unscaled alternating tensor and original source isometry gives `q! Delta_N`. CV.12 supplies its compatible first-degree control formula. None of these equalities estimates the stated growing-degree expression `omega_{N+1}Delta_N/(k^6 omega_N D_N)`.

## Final repaired-delta acceptance

After the root installed the two clarifications, I reread both changed passages directly from disk. The CV text now separately states `T_{q-2}(P_{q-2}chi)=sum gamma_j b_j` and `J^{(k)} V_{h,k}P_{q-2}chi=eta(sum gamma_j b_j)`, with the zero source convention for `q=1`. The reduction map is the same polynomial remainder map restricted to the indicated source; no surjectivity or Gram inverse is being asserted at that smaller degree. R26 now explicitly states `k>=2`, `d>=1`, and then separately retains the `h=1` zero arithmetic observation together with its analytic and graph maps. Both requested repairs are accepted.

Accepted repaired hashes:

- CV source SHA256 `ce8bfb4ddc2c21c2651cb25e0f77183f70e222ffc052bc1d0d0b6d62029f39b9`.
- Cumulative conclusion SHA256 `682bf395ac6bbfd01f02428fd6bf4121ac9162b4c001b0b99be4c623bfee5521`.
- E source remains SHA256 `313c321537673bf629e10a673daaacd5d74d234efcaadee0210a8c56909a921e`.

The bounded final mathematical delta is accepted with no remaining defect found. This does not certify PDF layout, build completion, publication, earlier unaudited sections, or any growing-degree arithmetic asymptotic.
