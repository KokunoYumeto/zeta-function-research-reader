# Independent review of PACKET_SURVIVAL.tex

Reviewed source: `work/rh_counterfactual_20260913/shared_thread_audit/segment16_28/PACKET_SURVIVAL.tex`, all 311 lines in the initial reviewed version. No author-source edits were made. The semiring, synchronization, and signed-Frobenius portion also received an independent bounded check.

## Verdict

The trace retraction, mixed-support localization, signed coefficient Frobenius, full-primary arithmetic action, and tensor pairing calculation are mathematically correct under the hypotheses stated. The actual-zero condition is retained: the construction starts from the full divisor polynomial of a packet of actual zeros in the counterfactual. It does not turn a symmetric auxiliary polynomial into a zeta-zero packet.

One explicit type correction is required in the tensor-amplification paragraph, initially lines 265–274: **all tensor powers there must be stated to be over `C`**. The nonzero claim is true over `C` but can fail over `E_Z`, and the immediately preceding maps are stated to be `E_Z`-linear. This is a substantive ambiguity, not a reason to discard the construction. A complete justification and exact replacement text are below.

A second clarification would make the arithmetic action completely reviewable in this fragment: display the original dilation on `Q` and its intertwining with `A_a`. The source's existing arithmetic packet theorem supplies it, and the calculation below proves it directly from that theorem. It requires no changed arithmetic condition or additional hypothesis about zeros.

## 1. The trace retraction retains the nonreduced coefficient ring

Since `t^n+1` is monic, `B_n=E_Z[t]/(t^n+1)` is free of rank `n` over `E_Z`, even when `E_Z` has nilpotents. Every element has the unique remainder `sum_(i=0)^(n−1) b_i t^i`.

For `1<=i<n`, multiplication by `t^i` takes each basis position `j` to `(i+j) mod n`, with sign `(-1)^floor((i+j)/n)`. No diagonal position occurs. Multiplication by `b_0` is the scalar matrix `b_0 I_n`. Matrix trace over the commutative ring `E_Z` therefore gives exactly

`Tr_(B_n/E_Z)(M_b)=n b_0`, and `r_n(b)=b_0`.

Thus `r_n iota_n=id` is valid with all primary nilpotents present. Division by `n` is permitted because `E_Z` is a complex algebra. The trace map is a module map, not a ring homomorphism, exactly as the text states. This relative trace retraction does not rescale the arithmetic derivative-residue trace form.

## 2. The mixed-support synchronization and unit are correct

The map that remembers both mask and amplitude is injective because each coefficient is either absent `tau` or the uniquely specified supported scalar with that amplitude. Supported cancellation produces `e`, not absence, so the support assertion must use the original semiring rules rather than ordinary vector cancellation.

Let `E_n=(1^bullet,e,...,e)`. It has amplitude one and full support. If an input has any active coefficient at index `j`, every output position receives an active term from the unique complementary index of `E_n`, including its supported wrap sign. Therefore multiplication by `E_n` makes the whole vector supported and preserves its amplitude. It fixes the wholly absent vector. This proves `E_n²=E_n` and identifies its image exactly with `G(B_n)`.

The localization is unital with image unit `E_n`. If a unital semiring map makes `E_n` invertible, idempotence forces its image to equal one, and hence forces the images of `b` and `E_n b` to agree. This proves the stated localization universal property. The text correctly does not call the image's inclusion into the old semiring unital.

The support-preserving lift of an `E_Z`-linear map sends an ordinary zero result to the supported zero. It respects both module addition and all absent-scalar/absent-input cases. Consequently the lifted retract is exact and preserves every nonzero amplitude class. When `n=1`, `E_1` is already the original unit, `B_1` is canonically `E_Z`, and the localization and retraction are identities. No exceptional case has been lost.

## 3. The stated n/q domain is sufficient and the specialization comparison is exact

The assumptions are `n>=1`, `q` an odd prime power, and `gcd(q,n)=1`. These imply `gcd(q,2n)=1`. Oddness is needed because the retained relation is `t^n=−1`: `(t^q)^n=(-1)^q=−1`.

The map on `Z[t]/(t^n+1)` fixes integer coefficients and sends `t` to `t^q`. Some positive `r` satisfies `q^r=1 mod 2n`, so its r-th iterate is the identity. This proves invertibility without discarding the sign in the defining polynomial.

Its matrix is precisely the signed permutation

`t^i -> (-1)^floor(qi/n) t^(qi mod n)`.

Over `F_q`, this is the q-power Frobenius because scalar q-powers are unchanged. The map from `Z` to `F_q` is the characteristic-p reduction followed by inclusion of the prime field; no characteristic-zero field embedding is used. Over `C`, the same integral matrix is extended coefficient-linearly and does not raise complex scalars to q-th powers. The text is correct to distinguish these two specializations.

For the full unsynchronized semiring, the signed slot permutation respects multiplication because reducing exponent `i+j` before or after multiplying it by q gives the same parity of wrap sign when q is odd. More explicitly, putting `s=floor((i+j)/n)`, the first route has exponent `s+floor(q(i+j−sn)/n)=floor(q(i+j)/n)−(q−1)s`, whereas multiplying the images has exponent `floor(q(i+j)/n)`; their difference is even. Absence is absorbed and supported signs stay supported. It fixes `E_n`, permutes masks, and descends to the synchronized map. Index zero stays zero, and no other index maps to zero, proving both `Psi_q iota_n=iota_n` and `r_n Psi_q=r_n`. The signed lift on the unsynchronized semiring need not equal taking the semiring q-th power; the text correctly asserts the q-power equality only after specialization to the amplitude ring over `F_q`.

Finite order implies all complex eigenvalues are roots of unity and the operator is diagonalizable because `X^r−1` has distinct roots in characteristic zero. This is a finite coefficient statement. It is not a proof that a global arithmetic Frobenius is this coefficient map; the fragment does not assert that identification.

## 4. The full jet action and weight defect survive exactly

On `E_rho=C[z_rho]/(z_rho^m)`, multiplication by the retained exponential is exactly

`A_a=a^rho sum_(j=0)^(m−1) (log a)^j N_rho^j/j!`.

The exponential uses the real logarithm of positive `a`. There is no branch choice or loss of a Jordan term. If `a!=1`, write

`exp((log a)N)-I=N C`,

where `C=(log a)I+sum_(j=2)^(m−1)(log a)^j N^(j−1)/j!` is invertible and commutes with N. Hence `(NC)^k=N^k C^k` and the nilpotence index is unchanged. For `m=1`, N is zero and the exponential reduces to the original scalar directly.

The socle vector `v_rho=e_rho(x−rho)^(m−1)` is nonzero and killed by `x−rho` in its primary summand. Thus `A_a v_rho=a^rho v_rho`. The constant coefficient inclusion is a split injection, and its image is fixed by `Psi_q`. Therefore `A_a^B Psi_q` has the unchanged actual arithmetic eigenvalue `a^rho` on `iota_n(v_rho)`.

The coefficient factors commute with the arithmetic factors because `A_a^B` is multiplication by an element of `E_Z` and `Psi_q` is `E_Z`-linear. On each coefficient eigenspace, the complete operator is `omega a^rho exp((log a)N)`, exactly as displayed. Since `|omega|=1`, a counterfactual `rho=1/2+delta+i gamma` gives

`|omega a^rho|²/a=a^(2delta)` and `log(|omega a^rho|²/a)=2delta log a`.

For `a>1`, this is strictly greater than one precisely when `delta>0`. At `a=q`, the coefficient pure factor does not erase the arithmetic weight defect. This is a correct obstruction to inferring arithmetic purity from purity of the attached coefficient operator alone.

## 5. Required tensor-base correction

As written, the paragraph beginning “Tensor powers retain it as well” leaves the tensor base unstated. The proof is correct for finite-dimensional complex vector spaces:

`(r_n)^(tensor_C k) (iota_n(v_rho)^(tensor_C k))=v_rho^(tensor_C k)`.

To prove this target is nonzero, choose a complex linear functional `ell:E_Z->C` that is one on `v_rho` (for example, its top local coefficient in the rho summand). Then `ell^(tensor_C k)(v_rho^(tensor_C k))=1`. Thus the input is nonzero as well. The tensor-product operator has eigenvalue `a^(k rho)` and gives the displayed logarithmic defect `2k delta log a`.

It is not legitimate to read these tensor powers as being over `E_Z`. For `m>=2`, the multiplication isomorphism `E_Z tensor_(E_Z) E_Z -> E_Z` sends `v_rho tensor v_rho` to

`v_rho²=e_rho(x−rho)^(2m−2)=0`,

because `2m−2>=m` in that primary factor. The claimed nonzero amplification would then fail. The exact suggested replacement is:

> All tensor products in this amplification paragraph are over `C`. For every integer `k>=1`, the vector `iota_n(v_rho)^(tensor_C k)` is nonzero: its image under `(r_n)^(tensor_C k)` is `v_rho^(tensor_C k)`, and applying the k-fold tensor power of the rho-primary top-coefficient functional gives one. The k-fold tensor operator `(A_a^B Psi_q)^(tensor_C k)` has eigenvalue `a^(k rho)` on this vector.

This retains the original nonreduced packet and adds only the missing domain. It does not simplify the packet or its zero multiplicity.

## 6. The original arithmetic action can be connected explicitly

The fragment imports `sigma_Z:E_Z->Q` and `J_Z:Q->E_Z` from the original actual packet theorem. To show that the exponential action is the original action on that cohomology, retain the original source spaces `V`, `B`, `Theta`, and `Q=B/Theta V`, and define for `a>0`

`Lambda_a F(u)=F(u/a)` and `Lambda_a^V phi(u)=phi(u/a)`.

Both preserve their original spaces, the zero source moments, and smooth/rapid-decay requirements; `Theta Lambda_a^V=Lambda_a Theta` follows termwise. Hence `Lambda_a` descends to Q. Changing variables in the Mellin integral gives

`M(Lambda_a F)(s)=a^s M(F)(s)`.

Therefore `J_Z Lambda_a=A_a J_Z`. The dilation commutes with `D=−u d/du`, so it preserves `Q[h_Z(D)]`. The original packet theorem identifies this whole torsion subspace with `sigma_Z(E_Z)` and makes the restricted J_Z its inverse. Consequently

`Lambda_a sigma_Z=sigma_Z A_a`.

This proves the precise action comparison that supports the word “original.” It is a useful standalone clarification, not an additional RH assumption. If the cumulative source already states it with these directions, a precise reference is enough; if not, the displayed calculation can be included. The mere abstract identity `J_Z sigma_Z=1` alone would not imply this action compatibility.

## 7. The derivative-residue trace and positive coefficient factor are not conflated

For symmetry-stable actual Z, the stated arithmetic trace has the full multiplicity weights and the dagger `rho -> 1−conjugate(rho)`. Its negative vector has exactly two nonzero evaluations, +1 and −1, and hence value `−2m`. The derivative insertion into the original g-residue cancels the constant factor in `g=2xi`; no factor has silently been dropped in this finite trace.

On `C_n=C[t]/(t^n+1)`, the roots `r_j=exp((2j+1)pi i/n)` are distinct, and evaluation is an invertible Vandermonde map. Thus `H_n(c,d)=sum_j conjugate(c(r_j))d(r_j)` is positive definite. The map `r_j -> r_j^q` is a permutation, so `Psi_q` preserves H_n. In particular `H_n(1,1)=n`, not one.

Under the expressly complex tensor-product identification `B_n=E_Z tensor_C C_n`, the arithmetic vector is `f tensor 1`. Its value under the specified tensor form is therefore exactly

`(T_Z tensor H_n)(f tensor 1,f tensor 1)=T_Z(f,f)H_n(1,1)=−2mn`.

The text correctly does not identify an uncomputed global polarization with this tensor form. The surviving negative vector and the preserved arithmetic action are valid inputs to any later actual comparison. They are not themselves a proof of a global Deligne upper estimate or of a counterfactual contradiction.

## Disposition

Approve the local construction after making the tensor base explicit. Preserve the stated odd-q/coprimality domain, the separate spectral and cyclic coordinates, the actual full zero orders, the synchronization unit, the relative trace factor n, and the distinction between coefficient purity and arithmetic weight. Add or reference the actual dilation intertwiner when integrating this fragment into the cumulative proof.
