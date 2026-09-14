# Independent review of the full mixed quadratic carrier

Date: 2026-09-13. Reviewer: `assembly_symmetry_check`.

This note verifies the complete classification of ordinary semiring ideals and primes of the original mixed quadratic double and gives an elementary proof of the integral-incomparability and dimension steps. It retains the three distinct supported zero elements `X_0`, `Y_0`, and `Z_0`.

Sources checked:

- `work/mixed_support_full_carrier_morphisms_subreview_20260913.md`, SHA256 `a2b286683f31f804d8374b5ae42a4079d9bc9a1f88872f66d1b5df07a1873bc8`.
- `output/split_zero_rh_tandem_2026-09-12/sources/Split_Support_Adelic_Weights_2026-09-11/sources/mixed_support_ledger.tex`, especially the mixed-double definition, ideal classification, prime classification, and dimension proof at lines 182–309; whole-file SHA256 `61c363cd1a5807824361988674a3baffb791a3b92ba9d09d4985ae52b791ec21`.

**Source-level verdict:** the classifications and the equality `dim D_A = dim A + 2` are correct for nonzero commutative unital rings of finite Krull dimension. No Noetherian hypothesis, field hypothesis, characteristic restriction, or invertibility of 2 is required. The complete final-byte acceptance of the authored MFC module is recorded below.

## Exact carrier and multiplication

Let `A` be a nonzero commutative unital ring. Put `B = A[t]/(t^2+1)`. Division by the monic polynomial gives a unique expression `a + tb` for every element of `B`, with `a,b in A`. In particular `A → B` is injective and `B` is free of rank two with basis `1,t`. The element `t` is a unit, with inverse `−t`.

The mixed carrier has the disjoint faces

\[
\mathbf0=(\tau,\tau),\qquad
X_a=(a^\bullet,\tau),\qquad
Y_b=(\tau,b^\bullet),\qquad
Z_{a+tb}=(a^\bullet,b^\bullet).
\]

Its multiplication has unit `X_1` and the exact table

\[
X_aX_c=X_{ac},\quad X_aY_b=Y_{ab},\quad Y_aY_b=X_{-ab},
\]
\[
X_aZ_z=Z_{az},\quad Y_aZ_z=Z_{taz},\quad Z_zZ_w=Z_{zw}.
\]

Addition inside either single face is addition of its coefficients; addition of two nonempty different faces fills their union. In particular

\[
X_a+Y_b=Z_{a+tb},\quad X_a+Z_z=Z_{a+z},\quad
Y_b+Z_z=Z_{tb+z}.
\]

The elements `mathbf0`, `X_0`, `Y_0`, and `Z_0` are four different elements. Products of two elements different from `mathbf0` remain on a nonempty face even when their ring amplitude is zero.

## Complete classification of ordinary semiring ideals

Here an ideal contains `mathbf0`, is closed under addition, and absorbs multiplication by every element of the semiring. Subtractivity is not assumed.

For a ring ideal `H` of `B`, define

\[
M_H=\{\mathbf0\}\cup\{Z_z:z\in H\}.
\]

For ring ideals `J` of `A` and `H` of `B` satisfying `JB subseteq H`, define

\[
I_{J,H}=M_H\cup\{X_a:a\in J\}\cup\{Y_a:a\in J\}.
\]

Every ordinary ideal is exactly one of `{mathbf0}`, `M_H`, or `I_{J,H}`. The parameters are unique within each family, and the three families are disjoint.

To prove this, let `I` be an ordinary semiring ideal. If its only element is `mathbf0`, the first case applies. If it contains a synchronized element but no single-face element, set

\[
H=\{z:Z_z\in I\}.
\]

This is a ring ideal without an assumption that `I` is subtractive. It is nonempty, `X_0Z_z=Z_0` supplies its ring zero, `X_{-1}Z_z=Z_{-z}` supplies additive inverses, synchronized addition supplies addition, and `Z_bZ_z=Z_{bz}` supplies multiplication by every `b in B`. Thus `I=M_H`.

Suppose instead that `I` contains a single-face element. Define `J_X={a:X_a in I}` and `J_Y={a:Y_a in I}`. The identities

\[
X_aY_1=Y_a,\qquad Y_aY_{-1}=X_a
\]

show that the two sets are equal and nonempty. Call the common set `J`. Multiplication by `X_0` supplies its ring zero; multiplication by `X_{-1}` supplies additive inverses; addition in the single face and multiplication by `X_r` show that `J` is a ring ideal of `A`. Multiplication by `Z_0` ensures that synchronized elements occur, so the preceding argument gives a ring ideal `H` of `B`. Since `X_aZ_z=Z_{az}`, absorption gives `JB subseteq H`. The four disjoint support types now show directly that `I=I_{J,H}`.

Conversely, the displayed multiplication table proves absorption for each candidate. For `I_{J,H}`, the only additional addition checks are `X_a+Y_b=Z_{a+tb}`, `X_a+Z_z=Z_{a+z}`, and `Y_b+Z_z=Z_{tb+z}`. Their amplitudes lie in `H` because `JB subseteq H`; all remaining addition checks are ring-ideal closure or addition of `mathbf0`. Thus these are all ordinary ideals. The first family has no supported elements, every `M_H` contains `Z_0` but no single-face elements, and every `I_{J,H}` contains both `X_0` and `Y_0`. This proves disjointness. Reading the amplitudes on the respective faces recovers `J` and `H`, proving uniqueness.

## Complete prime classification and every inclusion used in counting

Write

\[
P_\tau=\{\mathbf0\},\qquad M=M_B,
\]
\[
Q_{\mathfrak q}=I_{\mathfrak q\cap A,\mathfrak q}
\quad(\mathfrak q\in\operatorname{Spec}B),\qquad
T_{\mathfrak p}=I_{\mathfrak p,B}
\quad(\mathfrak p\in\operatorname{Spec}A).
\]

These are exactly the proper prime ideals.

The complement of `P_tau` is multiplicatively closed because a product of two nonempty support faces remains supported. The complement of `M` consists of the two single faces, and their multiplication table stays in those faces, so `M` is prime. For `H` properly contained in `B`, choose `z notin H`. Then `X_0` and `Z_z` are outside `M_H`, while `X_0Z_z=Z_0` belongs to it. Thus no other `M_H` is prime.

If `I_{J,H}` is prime and `H` is proper, synchronized products show that `H` is a prime ring ideal. The assumption `JB subseteq H` gives `J subseteq H cap A`. If `a in H cap A`, then `Z_a=X_aZ_1` lies in the prime but `Z_1` does not; hence `X_a` lies in the prime and `a in J`. Therefore `J=H cap A`. Conversely the complement of `Q_q` is closed under synchronized products by primality of `q`, under single-face products by primality of its contraction, and under single/synchronized products by primality of `q` and invertibility of `t`. This proves that every `Q_q` is prime.

If `H=B`, properness means `J` is proper. The complement consists of the single-face elements with coefficients outside `J`. Their three multiplication formulas show that this complement is multiplicatively closed exactly when `J` is a prime ring ideal. This proves the `T_p` family and completes the prime classification.

The full relevant inclusion relations are

\[
Q_{\mathfrak q}\subseteq Q_{\mathfrak q'}
\Longleftrightarrow \mathfrak q\subseteq\mathfrak q',\qquad
T_{\mathfrak p}\subseteq T_{\mathfrak p'}
\Longleftrightarrow \mathfrak p\subseteq\mathfrak p',
\]
\[
Q_{\mathfrak q}\subseteq T_{\mathfrak p}
\Longleftrightarrow \mathfrak q\cap A\subseteq\mathfrak p.
\]

The last inclusion is always strict when it occurs, since `Z_1` belongs to the `T` prime but not the `Q` prime. The prime `M` is strictly below every `T_p`, witnessed by `X_0`. It is incomparable with every `Q_q`: `Z_1` belongs to `M` but not `Q_q`, while `X_0` belongs to `Q_q` but not `M`. No `T` prime lies below a `Q` prime, again because of `Z_1`. Finally `P_tau` is strictly below every other prime, witnessed by `Z_0`.

These statements retain ordinary non-subtractive primes. For every `M_H`, the elements `Z_0` and `Z_0+X_0=Z_0` lie in the ideal, while `X_0` does not. Thus `M_H` is non-subtractive. For every proper `T_p`, the elements `Z_0` and `Z_0+X_1=Z_1` lie in the ideal, while `X_1` does not. Thus `T_p` is non-subtractive. Excluding them would discard exactly the extra prime branches used in the dimension proof.

## Elementary integral incomparability

Every element `u=a+tb` of `B` satisfies the monic equation

\[
u^2-2au+(a^2+b^2)=0.
\]

Thus `B` is integral over its embedded copy of `A`. This argument uses no inverse of 2.

Suppose that prime ideals `q subseteq q'` of `B` have the same contraction `p` in `A`. The domain `R=B/q` contains the domain `D=A/p`, is integral over `D`, and the ideal `I=q'/q` has zero intersection with `D`. If `I` were nonzero, choose `0 != u in I`. Among the monic equations satisfied by `u` over `D`, choose one of smallest positive degree:

\[
u^m+c_{m-1}u^{m-1}+\cdots+c_1u+c_0=0.
\]

Its constant coefficient is nonzero. Otherwise cancellation of the nonzero `u` in the domain `R` gives a monic equation of smaller degree, contradicting the choice. But the displayed equation also gives

\[
c_0=-u\bigl(u^{m-1}+c_{m-1}u^{m-2}+\cdots+c_1\bigr)
\in I\cap D=0,
\]

a contradiction. Therefore `I=0` and `q=q'`. Strict prime chains in `B` consequently contract to strict prime chains in `A`.

## Exact Krull-dimension count

Assume `dim A=d<infinity`, where dimension means Krull dimension. Since `A` is nonzero and unital, it has a maximal ideal: a union of a chain of proper ideals is still proper because it does not contain 1, so Zorn's lemma supplies a maximal proper ideal. Such an ideal is prime: if neither `a` nor `b` belongs to it, the two generated ideals are the whole ring, and multiplication of the two expressions for 1 contradicts membership of `ab`. Thus prime chains exist. The finite integer supremum defining `d` is attained by a chain

\[
\mathfrak p_0\subsetneq\cdots\subsetneq\mathfrak p_d.
\]

It gives the exact chain

\[
P_\tau\subsetneq M\subsetneq T_{\mathfrak p_0}
\subsetneq\cdots\subsetneq T_{\mathfrak p_d},
\]

of length `d+2` in the mixed double. The strictness of its first two steps is witnessed by `Z_0` and `X_0`, respectively.

For the upper bound, prepend `P_tau` to a chain if it is not already present. The inclusion relations proved above leave only an `M` branch followed by `T` primes, or a `Q` branch followed by `T` primes, with either branch possibly absent.

An `M` branch has the form `P_tau < M < T_p0 < ... < T_ps`. Its length is `s+2`, and the underlying ring chain has length `s<=d`.

A chain containing both `Q` and `T` primes has the form

\[
P_\tau<Q_{\mathfrak q_0}<\cdots<Q_{\mathfrak q_r}
<T_{\mathfrak p_0}<\cdots<T_{\mathfrak p_s}.
\]

Its length is `r+s+2`. Incomparability makes the contractions of the `Q` primes strictly increasing. The junction gives `q_r cap A subseteq p_0`. If this inclusion is equality, the combined ring chain has length `r+s`; if it is strict, that ring chain has length `r+s+1`. In either case the mixed chain length is at most `d+2`. A chain with only `Q` primes after `P_tau` has length at most `d+1`, and a chain with only `T` primes after `P_tau` has the same bound. Shorter chains cannot increase it. This proves

\[
\boxed{\dim D_A=\dim A+2}.
\]

The proof counts every ordinary prime family and never identifies `X_0`, `Y_0`, or `Z_0` with each other or with global absence.

## Authored MFC module: complete draft read

The complete draft `work/rh_counterfactual_20260913/total_object/full_mixed_carrier_attachment.tex`, MFC.1–MFC.49 and all intervening prose, was read in two untruncated portions. Both reads independently reported 43,700 bytes and SHA256 `66f758f5327d456d0a7598cac8b7088be809910fc444642fb7362bd74f1b7c8b`.

All substantive assertions in that draft were verified, including the independent Cartesian support fibres and pullback, the quadratic synchronization fibres and generated kernel congruence, the nonunital section and its unital-section obstruction, the complete ordinary ideal and prime families, the integral-localization proof of incomparability and exact dimension count, the full lattice zero fibre and each localization fibre, the higher-zero inclusion into the independent cube, every threshold fibre, both complete ideal-chain classifications, their two distinct multiplications, and all displayed coefficient and prime-contraction naturality formulas.

One precise wording repair was requested: the converse proof for `M_H` must say that a **nonempty** face multiplied by `Z_h` remains a synchronized entry. The absent face instead gives global zero, which is already in `M_H`. The author was also advised to spell out bottom and top preservation in the bounded-lattice homomorphism hypothesis of MFC.48. Both repairs were confirmed in the complete final-byte read below. No shared mathematical source was edited by this reviewer.

## Final-byte independent acceptance

The entire final source `work/rh_counterfactual_20260913/total_object/full_mixed_carrier_attachment.tex` was read, including all prose, hypotheses, displayed formulas, proofs, and tags MFC.1–MFC.49. The two untruncated reads covered lines 1–495 and 496–983. Each read independently reported the same raw byte count and SHA256, and a subsequent file-hash check agreed:

- Byte count: **44,478**.
- Line count: **983**.
- SHA256: **`5e960b547592a83952e88ff65ec22577f182c652a7be48c1da1dcbdb91df7abf`**.
- Verdict: **accepted; no unresolved mathematical or typing error found in the complete final source**.

The final read verified the Cartesian and synchronized support faces and fibres, the four distinct zero/absence elements of the quadratic double, its multiplication and associativity, synchronization and its exact kernel congruence, the nonunital full-face section and unital-section obstruction, the idempotent localization and universal property, the complete ordinary ideal and prime classifications and all inclusion relations, the integral-localization proof of incomparability and exact Krull-dimension count, the bounded-lattice construction and localization fibres, the higher-zero inclusion, every chain threshold and fibre, both complete ring-ideal-chain classifications, their lattice operations and their distinct ideal products, and all coefficient, lattice, corner, threshold, ideal-preimage, and spectral-continuity formulas.

In particular the final proof of closure for `M_H` explicitly handles every nonempty multiplier face and separately the absent multiplier, whose product is global zero. The non-subtractive witnesses for `M_H` and `T_p` are present and correct. MFC.48 explicitly requires preservation of bottom, top, joins, and meets. These hypotheses suffice for MFC.49, including its maps on localized intervals. Characteristic 2 and the absence of an inverse of 2 introduce no exception. The dimension statement uses finite Krull dimension and a nonzero unital coefficient ring exactly as stated; no hidden Noetherian or field assumption enters the proof.

This receipt records an independent mathematical and source-typing review. The author's reported LuaLaTeX compilation result is not claimed as an independently executed compilation by this reviewer.
