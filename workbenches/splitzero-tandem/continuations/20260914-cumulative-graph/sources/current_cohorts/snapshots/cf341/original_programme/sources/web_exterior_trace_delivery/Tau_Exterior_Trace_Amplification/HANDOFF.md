# Formalization handoff — exterior trace amplification

This handoff is for the parallel formalization/GitHub session. No remote source was changed by this continuation. Reuse the original scalar, support, quotient, HomOver and projected-homology library.

## Pinned inputs

- Repository main inspected at `a4494fba4968db837a8af6fcb952c8688cd5d1da`.
- Actual PR #20 note correction: nonempty monic-freeness; for h=1 every algebraic I-adic quotient is zero, while G(0) retains e and tau and the analytic amplitude remains g.
- Current frontier metric theorem requires the actual commutation assumptions for inverse compression. This note never applies that theorem to an oblique CRT projector without those hypotheses.
- Delivered cyclic-sum source: archive SHA-256 `e0e4d0ecda69e4738dcb4cdd3b750e623d863eac8b44f353737393e720a840a7`; NOTE.tex SHA-256 `2cdfd5b25631464f9500dc5fd07c4c8f5c927c8877eb1bf076307ec5dcbc2e8c`.

## Finite algebraic targets, in dependency order

### 1. Gram adjoint and rank-two positive-trace budget

For positive-definite Hermitian G, arbitrary A, and real weight k, set

    sharp(A) = G^-1 A* G
    H = sharp(A) + A - k I.

From rank(H)<=2 and trace(H)=0, derive its G-self-adjoint spectral values +/-eps and zero. Preserve eps=0. For an A-invariant subspace Vplus with original column inclusion C, use the actual orthogonal projection

    P = C(C*GC)^-1 C*G.

Derive

    Tr(PH) = 2 Re Tr(A|Vplus) - k dim(Vplus) <= eps.

This is the direct finite version of the new estimate. It does not need Lean exterior-power machinery before the numerical consequence can be certified. The order proof uses rank-one spectral projectors or the finite-dimensional extremal-trace theorem with its actual metric conversion.

### 2. Exact comparison of two projectors

For the CRT projector Qplus with the same range as P, prove

    Qplus P=P, P Qplus=Qplus, (P-Qplus)^2=0,
    Tr(P A)=Tr(Qplus A).

Do not identify Qplus with P. For eps>0 define Fplus/Fminus by the explicit polynomials in H. Prove the slack identity in NOTE section 7.

### 3. Additive exterior action and its metric

Define additive exterior action A^[p] by replacing one factor at a time. It is the derivative of wedge^p(exp(tA)), not the multiplicative map wedge^p(A).

The induced Gram is the compound matrix of minors G^[p]. Prove

    (A^[p])* G^[p] + G^[p] A^[p] - kp G^[p] = G^[p] H^[p].

For rank-two traceless H its additive exterior action has eigenvalues +/-eps and zero, with +/- multiplicity binomial(q-2,p-1). Cases p=q and eps=0 are explicit.

### 4. Original tensor inclusion and signs

The unscaled Alt_p map has

    wedge_quotient Alt_p = p! id,
    Alt_p* (G tensor ... tensor G) Alt_p = p! G^[p].

The actual source representative is R_p=R^tensor p Alt_p. Keep p!, all primitive coefficients and the tensor weight kp.

On p blocks each of cohomological degree k, use

    A_(p,k) = (1/p!) sum_pi sign(pi)^(k+1) T_pi.

T_pi includes its Koszul sign sign(pi)^k in top degree. The product is sign(pi). Reuse the existing character-twisted Reynolds/chain idempotent interface, not a duplicate projector implementation.

### 5. Primitive propagation

Given DR-RA=dK with R in degree k and K in degree k-1, prove

    K_p = sum_j (-1)^(k(j-1)) R^(tensor(j-1)) tensor K tensor R^(tensor(p-j)) Alt_p,
    D_tot R_p - R_p A^[p] = d K_p.

Lift using the existing support-changing total-map interface. Active zero results remain labelled zeros. The single scalar tau is not iterated; no averaging of different labels without their orbit-join map.

### 6. Determinant line and all full generalized eigenspaces

For the sum of full generalized eigenspaces with Re(lambda)>k/2, the determinant line is invariant and A^[p] acts by their trace, with multiplicities. Derive

    L = sum_{Re(lambda)>k/2} ell_lambda(2 Re(lambda)-k) <= eps.

Retain the complement and its trace. The determinant map does not replace the full nilpotent module.

### 7. Exact quartet count

For delta,gamma>0 and full root quartet 1/2 +/- delta +/- i gamma, prove the k-fold distinct sum grid with (k+1)^2 points. The constructive occupancy table uses any integer

    max(0,a+b-k) <= t <= min(a,b).

Every block length is ell=1+k(m-1). Hence

    q=ell(k+1)^2,
    pplus=ell(k+1)ceil(k/2),
    L=2 delta ell(k+1)floor((k+1)^2/4).

All formulas include even and odd k. No genericity/linear-independence hypothesis about ordinates is used.

## Analytic boundary

The new result is an amplification lower bound on the canonical arithmetic allowance. It does NOT establish a subcubic upper bound. The actual analytic object remains

    eps_(h,k,N) = sqrt(a_N d_N - |c_N|^2)/omega_N,
    N >= [1+k(m-1)](k+1)^2 - 1 for a full quartet.

For a contradiction argument h can remain fixed; constants may depend on h. A proven eps=o(k^3) for this actual family would suffice. It has not been proved in this package. The entire original mass, full-jet unit, relation degree and inverse interpolation matrix remain inputs.

## Evidence

The 22-method SymPy script checks finite exact algebraic examples and identities, including nonnormal operators and repeated jets. The Gaussian measure in those tests has literal mass 7^k. Its root fixtures are not asserted to be zeta zeros. No Lean build was executed here.
