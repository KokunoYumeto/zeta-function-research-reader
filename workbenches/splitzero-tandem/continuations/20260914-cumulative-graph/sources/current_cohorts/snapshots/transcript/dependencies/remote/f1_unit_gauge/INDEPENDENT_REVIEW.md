# Independent review of the actual-unit formal gauge

Date: 2026-09-13. Read `ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md` completely,
UG1--19 and its scope/source paragraphs. The original tau-base note,
`arithmetic_input.tex`, and original exponential comparison were read in
full in the adjoining independent scaling work. This review does not edit
the root note, run its fixtures, or claim a Lean or analytic-convergence
result.

## Disposition and one domain clarification

Accept UG1--18 and the formal construction. The pole inverse has the
correct order, the coefficientwise completions are essential and correctly
specified, and the explicit retract proves the claimed quasi-isomorphism.
The tensor map retains the complete direct Taylor units and recovers the
original eta without an assumption that their tensor product is a function
of the sum coordinate alone.

UG19's residue identity is correct on the original reflection-stable
packet used in the tau-base residue construction. That domain should be
explicit here: UG1 otherwise admits any full-order selected packet, while
dagger is not automatically a well-defined endomorphism of its quotient.
The two equivalent precise typings are:

- use the already retained reflection-stable packet, so dagger maps
  `E_h` to `E_h`; or
- for arbitrary h, put `h^dagger(s)=(-1)^d conjugate(h(1-conjugate(s)))`
  (the monic reflected polynomial) and take the first argument from
  `E_{h^dagger}`, so its dagger lies in `E_h`.

No change to the full-order arithmetic source or formal gauge is needed.
This is the exact domain of the existing residue arrow, not a new analytic
hypothesis. The issue and the tensor-completion convention below were
reported to the parent before writing this review.

## Coefficientwise quotient and its inverse

Let `A=C[s]`, `A_nu=C[s,nu^{-1}]`, and `M=A_nu/A`. A rational function
has a unique decomposition into a polynomial and a proper rational
function; two proper representatives differing by a polynomial are equal.
Thus the stated section sigma is well defined, including when different
denominator powers represent the same rational function. Applying this
section to each `(u,t)` coefficient proves surjectivity in UG5 without
assuming a uniform denominator. The constant-nu case gives `M=0`.

Since `gcd(h,nu)=1`, `hP/nu^n` being polynomial forces `nu^n|P`.
Conversely `a_n h+b_n nu^n=1` gives an inverse class
`[a_nP/nu^n]`. These prove injectivity and surjectivity of `M_h` on M,
and uniqueness makes its inverse H independent of all Bezout choices.
This inverse acts on the additional pole quotient, not on `E_h`.
Differentiation descends to M, but no commutation with H is needed.

Writing `E=u partial_s-t`, the exact factorization is

`D_M=M_h(I+HE)`.

Thus the inverse must be `(I+HE)^{-1}H`, which is precisely UG8.
The powers of `HE` raise parameter order; at any fixed coefficient only
finitely many terms contribute. Both inverse identities follow by finite
geometric sums modulo each parameter power, then coefficientwise
completion. This does not use a norm-convergent Neumann series or reorder
H and the derivative.

## Explicit retraction and formal finite cohomology

Using `pi D=D_M pi` and `J D_M=D_M J=I`, one gets

`KD=sigma pi`, `r^0=I-sigma pi`, `pi r^1=0`.

The remaining formulas follow by multiplication:
`r^1D=Dr^0`, `ri=I`, and `ir=I-dK-Kd`. The degree-zero and
degree-one occurrences of K are correctly typed. Thus no assumption
about exactness of a completed cohomology functor is replacing the
displayed deformation retraction. The mapping-cone description has the
same quotient and the contractible identity-cone kernel.

The completed original polynomial complex also retains its expected
finite coefficient basis. At the lowest parameter order, divide by h;
the `u partial_s-t` term only affects higher orders. Recursive monic
division therefore constructs the unique degree-below-d formal remainder
and its formal preimage, coefficient by coefficient. The lowest-order
nonzero term of a putative kernel would be killed by the injective
polynomial multiplier h, so the differential remains injective. Hence its
cohomology is the coefficientwise completed free rank-d module. Unbounded
s-degrees or pole orders across formal coefficients are allowed exactly
as stated in UG4.

## Gauge, special fibre, and scaling

Direct Leibniz differentiation gives

`nu D nu^{-1}=u partial_s+h-t-u nu'/nu`.

Both the minus sign and factor u are correct. Multiplication by nu in
both degrees is an isomorphism only on the explicitly localized complex,
with inverse the same rational `nu^{-1}`. At `u=t=0`, both target
differentials are h, but this cochain map still multiplies by nu.
Its induced map under the original quotient identification is therefore
exactly multiplication by `upsilon_h`, not identity.

For the composite to the gauge target, an explicit inverse up to homotopy
is `r M_{nu^{-1}}`; its homotopy is `M_nu K M_{nu^{-1}}`.
This also supplies a direct way to tensor the composite itself.

The operator `L=u partial_t-s` commutes with multiplication by nu and
its inverse, because these depend only on s. Therefore its commutation
with D transfers to `D^nu` with no additional term. The inclusions and
gauge map strictly intertwine L and its formal a-adic exponential. It is
correct not to demand that the particular proper-part retraction strictly
intertwine L. The coefficient matrix in the transported frame `nu s^j`
is consequently the same formal `C_a`; an entire evaluation of that
finite matrix does not claim analytic convergence of the rational formal
gauge. The note keeps these domains distinct.

## Precise tensor-completion interpretation and homotopy

The tensor statement is valid with independent parameter pairs and the
completed tensor product defined by the cofinal rectangular truncations
`(u_i,t_i)^{n_i}` in the finitely many factors. Each such quotient is the
ordinary tensor product over C of its factor truncations. These rectangular
filtrations are cofinal with total parameter-adic truncation, so they give
the same coefficientwise formal product. Calling every total-degree
truncation a literal tensor product would be inaccurate; the rectangular
convention is the precise one under which UG7's tensor paragraph operates.

There is no need to infer inverse-limit exactness abstractly. Let
`P_i=i_i r_i` and use the root's homotopies `K_i`. For two factors set

`K_tot=K_1 tensor I+P_1 tensor K_2`,

with the graded convention
`(P_1 tensor K_2)(x tensor y)=(-1)^{degree x}P_1x tensor K_2y`.
Since P is a cochain map, direct expansion gives

`dK_tot+K_tot d=(I-P_1) tensor I+P_1 tensor(I-P_2)`
` =I-P_1 tensor P_2`.

For k factors the sum has `P_1,...,P_{j-1}` before `K_j` and identities
after it, with these same tensor signs. The terms telescope to
`I-tensor_i P_i`. All maps preserve parameter order, so this identity
holds at each compatible rectangular truncation and hence coefficientwise
in the completed product. The gauge-conjugated homotopies give the same
statement for the targets with `D_i^nu`.

Specialization yields `M_{upsilon_h}^{tensor k}` on the whole original
tensor packet. Composing with `[P]->P(sum A_i)1` is exactly eta.
All same-sum occupancies remain in the tensor module and no cyclic
polynomial formula for the tensor unit is used.

## Residue scope, support, and limits of this review

With the dagger domain fixed as above, `g=h(g/h)` proves UG19: the
complete inverse Taylor unit differs from the inverse germ by a multiple
of h, so the residue difference is holomorphic. Its transpose and
inverse-transpose transports keep the actual source inverse units;
they do not assert a positive pairing or a globally invertible extension
on every analytic deformed fibre.

Every operation is on the declared linear coefficient fibre, followed by
its support-preserving lift. Inverting nu is not inverting the supported
zero e. The formal pole contraction does not identify represented zero
with tau or pass from tau-base pushforward to the generic skeleton.
No specialization of UG8 at a nonzero complex u, no analytic period
assertion, no metric estimate, and no tensor-growth bound is certified by
this review. The affirmative result is the explicit formal quasi-isomorphism
with its actual arithmetic unit and all the displayed kernels retained.

## Final acceptance of the revised note

The preceding domain-clarification discussion is the historical review
record, not an outstanding objection. On 2026-09-13 I reread the revised
Section 7 and Section 8, including the full signed tensor homotopy and
the explicit original reflection-stable packet restriction. Both comments
are resolved in the text. In the tensor discussion above, "UG7's tensor
paragraph" means Section 7, not the equation labelled UG7.

The exact accepted root artifact is
`ACTUAL_TAYLOR_UNIT_FORMAL_GAUGE.md`, SHA-256:

`9ded2486160b76bf65f92d44b73cdd0c59a3ca7e5334f88682e10592d5a45b2f`.

Final disposition: accept UG1--19 and the stated formal construction,
with no outstanding mathematical correction. Independent parameter pairs
and cofinal rectangular truncations make every tensor identity
coefficientwise well defined; the displayed Koszul signs give
`dK_total+K_total d=I-tensor_i P_i`. Section 8 now has exactly the domain
on which the original dagger and residue-dual arrow are defined, while
the preceding gauge proof retains its greater generality. No assumption
of analytic convergence, positivity, or global invertibility of the
original arithmetic residue unit is added by this acceptance.

This final seal is a proof review. The parent's separately reported exact
fixtures and negative controls were not rerun by this reviewer.
