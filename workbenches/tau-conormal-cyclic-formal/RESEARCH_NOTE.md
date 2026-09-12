# Original conormal and cyclic relation towers

## Scope and source reconciliation

This add-only continuation starts from main at `a4494fba4968db837a8af6fcb952c8688cd5d1da`. It retains the merged Codex quotient/homotopy/boundary implementation, the merged finite-frontier implementation, and the reviewed sum-connection note. It uses the owner's attached **Handoff: sum-generated arithmetic control**, especially targets 1, 2, 4 and 8. The current upload is an analytic/algebraic continuation with a separately reported 24-method finite checker; it is not a Lean certificate. The local execution service failed before its ZIP could be opened, so neither the ZIP manifest nor that checker has been independently rerun here.

Two actual GitHub corrections are incorporated, not merely acknowledged:

* Commit `600ab7a527f7a626c162bf0199d093d454b86c14` makes the nonempty hypothesis explicit in the monic-freeness argument and calculates h=1 separately. Every positive-depth relation ideal for h=1 is the whole polynomial ring. The corresponding underlying quotients are zero, while the split lift still retains tau and supported zero. The analytic theta seed and its mass do not disappear. `ConormalTower.top_level_zero` checks the full-ideal quotient at every level.
* Commit `7aec03a93b66d3d97fbf6f7042f58bb2c1019543` corrects the completed integration audit to 68 selected declarations and enables the existing frontier workflow on main and relevant pull requests. This branch inherits those files unchanged. The current 68-target audit, not the historical 66-target description, is rerun by the added workflow.

The original scalar G, e, tau, arithmetic projection to the infinite ring, reconstructed carriers, quotient transports and theta normalization g=2 xi are unchanged. No claim about a global arithmetic small-control estimate follows from the present algebraic results.

## 1. An actual derivative between consecutive original quotients

Let R and A be commutative rings, A an R-algebra, I an ideal of A, and D an R-derivation of A. Then

    D(I^(r+1)) is contained in I^r,  r >= 0.

Proof: use induction on r and the additive generation of an ideal product by products. For a in I^(r+1), b in I, the Leibniz terms a D(b) and b D(a) both lie in I^(r+1): the first by the ideal property, the second by the induction hypothesis. At r=0 the target ideal is the whole ring.

`SplitZeroConormalTower.lean` implements that proof as `deriv_mem_pow`. It then uses the merged `SplitZero.RelationLayer.derivative` to construct

    delta_r : A/I^(r+1) ->_R A/I^r,  [x] |-> [D x].

It separately constructs the quotient projection p_r between the same types and proves

    p_r delta_(r+1) = delta_r p_(r+1).

The derivative is not an endomorphism of A/I. These are coefficient-linear maps on the actual original quotient types, not new quotient carriers. At a retained relation z in I,

    delta_1([z a]) = [a D(z)].

For the full arithmetic multiplier u, the implemented formula is

    delta_r([u x]) = [u D(x)] + [x D(u)].

It applies in particular to the retained Taylor unit, without assigning the unit the value one or deleting its derivative. The definitions work for arbitrary commutative rings and do not assume characteristic zero or squarefreeness.

## 2. The exact cyclic pullback, before a polynomial is used to describe it

Fix S in A. At each depth define the actual coefficient submodule

    K_r = {P in R[X] : P(S) belongs to I^r}.

The implementation calls this `cyclicLevel`; it is literally the comap of the original relation submodule along `Polynomial.aeval S`. Its constructed quotient map is

    alpha_r : R[X]/K_r ->_R A/I^r,  [P] |-> [P(S)].

`evaluation_injective` proves injectivity by the two original quotient equality criteria. No assumed injectivity of polynomial evaluation is required. This implementation is a linear map; its usual algebra-homomorphism packaging is not claimed as a new bundled declaration.

If D(S)=1, Mathlib's formal polynomial chain rule gives

    D(P(S)) = P'(S).

Thus P in K_(r+1) implies P' in K_r. The code constructs the cyclic derivative and proves the full square

    R[X]/K_(r+1) --d/dX--> R[X]/K_r
          | alpha_(r+1)          | alpha_r
          v                      v
       A/I^(r+1) ------D------> A/I^r.

The actual unit comparison is also proved:

    delta_r([u P(S)]) = [u P'(S)] + [D(u) P(S)].

The final term need not be in the cyclic image. The equation retains its larger target. Most importantly, K_r is not replaced by K_1^r. The explicit annihilator calculation below explains the difference.

## 3. Exact local maximum, including an attaining monomial

Here the base field is C. Let k>=1, d>=1, r>=1 and write the complete packet polynomial as

    h(s) = product_rho (s-rho)^(m_rho).

For a root tuple bold-rho=(rho_1,...,rho_k), put m_i=m_(rho_i) and y_i=s_i-rho_i. Locally the ideal (h(s_i)) is (y_i^(m_i)), because each remaining factor is a unit. In the quotient by its r-th power the monomial basis is precisely

    y^a such that sum_i floor(a_i/m_i) < r.

Write a_i=m_i q_i+t_i with 0<=t_i<m_i. Its total degree satisfies

    sum_i a_i <= sum_i(m_i-1) + (r-1) max_i m_i.

The proof uses sum_i q_i <= r-1 and bounds each m_i by its maximum. This bound is attained: choose j with m_j=max_i m_i, let every t_i=m_i-1, let q_j=r-1, and let every other q_i=0.

`SplitZeroCyclicDepth.lean` formalizes the quotient/remainder predicate, the degree bound, that explicit exponent vector, and attainment. The floor-sum formulation is linked through Euclidean division. This is an all-index, all-depth result, not a finite calibration. The additional algebraic identification of these monomials with the polynomial quotient and the characteristic-zero multinomial step below have written proofs, not an additional Lean certificate in these two modules.

Let N=y_1+...+y_k. Its exact nilpotency index is

    L_r(bold-rho) = 1 + sum_i(m_i-1) + (r-1) max_i m_i.

Indeed every monomial of total degree L_r is killed. The attaining monomial at degree L_r-1 has coefficient

    (L_r-1)! / product_i a_i!

in N^(L_r-1), a nonzero positive integer in characteristic zero. Distinct surviving monomials cannot cancel. This proves both vanishing and minimality.

The proof also counts the local dimension as

    (product_i m_i) * binomial(k+r-1,k).

The q_i with sum less than r give the binomial factor, and their remainders give the product factor.

## 4. Collisions require a maximum at every depth

Set S=sum_i s_i. At a collided sum lambda, take the maximum over all root tuples with that sum:

    ell_(lambda,r) = max_(sum rho_i=lambda) L_r(bold-rho).
    chi_r(X) = product_lambda (X-lambda)^(ell_(lambda,r)).

The Chinese-remainder decomposition and the exact local nilpotency prove

    I^r intersect C[S] = (chi_r(S)).

The same annihilator is obtained in the variable-permutation invariant subalgebra because every polynomial in S is already invariant. Thus alpha_r identifies the cyclic algebra C[X]/(chi_r) with its actual image, with no squarefree simplification.

The maximizing tuple can change with depth. In the declared calibration packet with roots 0,1,2 of multiplicities 5,4,1, respectively, the sum lambda=2 in tensor degree two has

    ell_(2,r) = max(5r,4r+3).

At depths 1,...,5 the orders are 7,11,15,20,25. A tuple chosen only at depth one is insufficient for the whole tower. This is an algebraic test packet, not a statement about actual zeta zeros.

For every lambda,

    ell_(lambda,r+1) >= ell_(lambda,r)+1,
    ell_(lambda,r) <= r ell_(lambda,1).

The first follows by retaining a maximizing tuple from depth r; its next slope is a positive multiplicity. For the second, note max_i m_i <= 1+sum_i(m_i-1) for every tuple. Hence

    chi_r divides chi_(r+1),
    chi_r divides chi_(r+1)',
    chi_r divides chi_1^r.

The last divisibility supplies the stated surjection C[X]/(chi_1^r) -> C[X]/(chi_r), not an equality. For h(s)=(s-rho)^2 and k=2,

    chi_r(X)=(X-2rho)^(2r+1),
    chi_1(X)^r=(X-2rho)^(3r).

They differ as soon as r>1. The derivative maps C[X]/chi_(r+1) -> C[X]/chi_r are onto over C: integrate any polynomial representative, then take its source class. Their kernel dimensions are deg(chi_(r+1))-deg(chi_r).

For the empty packet h=1, handled separately as required by the GitHub correction, I=P, K_r=C[X], and chi_r=1 for all positive depths. The cyclic arithmetic quotient is zero. No maximum over an empty tuple set or inverse of a zero-dimensional Gram matrix is used to define it. The original nonzero analytic seed remains available as an analytic object.

## 5. Explicit equivariant retraction of the cyclic summand (written proof)

This checks the handoff's retraction formula, including its inverse factor. On a lambda-primary part M of the symmetric finite algebra, let N=S-lambda, N^ell=0, and let w be the lambda-component of the retained arithmetic unit U. Exact maximality gives N^(ell-1)w != 0. Choose the stated top-monomial coefficient functional theta with theta(N^(ell-1)w) != 0. If it is realized first on an ordered root component, it can be restricted to the invariant subspace; the component of the symmetric vector is still detected.

Define

    pi0(v) = sum_(j=0)^(ell-1) theta(N^(ell-1-j)v) X^j mod X^ell.

Coefficient comparison gives pi0(Nv)=X pi0(v): the constant term on the left is theta(N^ell v)=0 and the other coefficients shift exactly. Put c=pi0(w). Its constant coefficient is nonzero, so it is invertible modulo X^ell. Explicitly, if c=c0(1+n), the inverse is c0^(-1) sum_(j=0)^(ell-1)(-n)^j.

Then pi=c^(-1)pi0 satisfies

    pi(P(N)w)=P(X) mod X^ell.

Therefore the unit-weighted cyclic injection eta has an S-equivariant left inverse. Summing over lambda constructs the full retraction, and ker(pi) is an invariant complement. This is a module splitting, not an assertion that pi is an algebra map or that the summands are orthogonal for the canonical arithmetic Gram. All cross terms under that splitting remain.

This cyclic summand retains each amplified value k rho; collided repeated pure tensors need not equal the particular cyclic eigenvector. The cyclic residue trace and the full symmetric trace have their distinct multiplicities. No part of the present calculation identifies those traces or drops the U-dagger U factor in the ambient arithmetic pairing.

## 6. Formal versus analytic scope

The new formal outputs are the ideal-power derivative, actual quotient transitions, exact cyclic pullback/injection, derivative square, unit rule, full-ideal case, and the all-degree attained monomial ceiling. Existing SplitZero support maps lift their coefficient maps at the original labels. No duplicate scalar construction or alternative homology core is introduced.

The exact chi_r annihilator, local basis/multinomial identification and the retraction in Sections 3-5 are supplied here as complete written arguments. Their finite calibrations are separate Python tests. The new upload's analytic cyclic convolution measure, canonical Gram, differentiated moments, rank-two control and full trace comparison remain its separately stated inputs and targets. This work does not independently certify that archive, an analytic moment enclosure, or a tensor-uniform small-control bound.

## Reproduction

Run the added `SplitZero conormal cyclic tower` workflow on this branch. It installs unchanged Lean 4.31.0 and Mathlib `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`, rebuilds all inherited modules, checks every new source with `--trust=0 -DwarningAsError=true`, imports the combined sources, and rejects any selected transitive axiom outside propext, Classical.choice and Quot.sound. It reuses the previously tested axiom parser. The original core's byte pin is checked by the inherited prepare script.

The new finite checker directly multiplies the nilpotent sum in explicit local monomial quotients. It tests attainment and its literal multinomial coefficient, collided maxima, derivative divisibility, local dimensions and the h=1 branch, in normal and optimized Python with deliberate-failure controls. These finite tests do not replace the general Lean proofs or the written polynomial arguments. The final PR record identifies the exact completed run; no pending run is a certificate.
