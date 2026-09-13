# Bounded formalization handoff

This is an add-only mathematical continuation of the original SplitZero theta programme. Reuse the existing scalar, reconstruction, quotient, homology, source-section, and original conormal-tower library. No competing quotient type or new scalar zero is proposed. GitHub and Lean execution remain with the parallel sessions.

## 1. Polynomial-exponential division (first priority)

Input: a commutative coefficient ring R, a monic polynomial χ in R[S] of positive degree q, and elements u,t. Define the R-linear map

`D(P) = u * derivative P + (χ - t) * P`.

Prove:

- A nonzero P of degree a maps to degree a+q, with its original leading coefficient.
- Every F has a unique decomposition `F = D(Q) + Remainder`, with `degree Remainder < q`.
- The quotient by the **linear range** of D is free with basis `[1],...,[S^(q-1)]`.
- This split presentation commutes with coefficient base change.
- At u=t=0 the quotient is the original polynomial quotient by `(χ)`.

D's image is not generally an ideal at u nonzero. The regression equation `[S*(χ-t)] = -u*[1]` must remain. This prevents accidentally packaging this as an algebra quotient.

## 2. The actual t-connection and arithmetic source square

After inverting u, define `nabla_t = partial_t - S/u` on polynomial coefficients. The two commutators with D are +1 and −1; their sum is zero. It therefore descends to the actual range quotient.

In the degree-below-q frame, prove `nabla_t = partial_t - A(t)/u`, with `A(t)=A+t*e_0*e_(q-1)^T`. The constant matrix A is precisely multiplication by S on the original E. The regular operator `-u*nabla_t` obeys a t-Leibniz rule scaled by −u; reducing modulo (u,t) gives A. It is not a derivative in u.

For the existing actual finite section r and equivariant observation j with `j*r=1`, define `D_t=D+t*r*R*j`. Prove `j*D_t=A(t)*j` and `D_t*r-r*A(t)=D*r-r*A`. This keeps the same theta primitive. The induced original-metric defect is `W(t)=W(0)+t G R+conj(t) R* G`.

## 3. Residue and dual t-connection

The residue Gram in the unchanged basis is the coefficient of S^-1 in `P Q/(χ-t)` at infinity. Prove independence of t for deg P,deg Q<q. Its determinant is `(-1)^(q*(q-1)/2)`, and `A(t)^T B=B A(t)`.

This yields a bilinear duality between the connections at u and −u. It is not a Hermitian positivity assertion. Compose with the existing dagger only at the designated fibre, and retain the Jacobian contraction with χ'. The full original packet trace uses its actual inclusion and complement, not only this cyclic trace.

## 4. Logarithmic curve calculation

Use the predecessor's original invariant hull F and finite quotient E/F. For the lattice `F O + E O(-m∞)`, with the restricted constant connection, the local logarithmic operator is `w*d/dw+m`. Its hypercohomology is F in degree 0, E/F in degree 2, and zero in degree 1.

A finite exact target is the Čech differential with columns a=1,...,m−1 and rows b=1,...,m: entry −a in row b=a+1. Its kernel is zero and its cokernel is the line z^-1 dz. The boundary quotient has operator `diag(0,1,...,m−1)`, with contraction 1/a only on the positive a terms. Keep the constant kernel and cokernel.

The original support reconstruction makes each boundary zero in its receiving fibre, not external τ. Pullback z↦z^m multiplies dz/z by m. Do not erase that factor.

## 5. Analytic period proof: written, not a finite kernel claim

The note supplies explicit ray cycles, Gamma evaluation at a monomial potential, and coefficient-direction connection equations. A finite target is the commutator

`[D, partial_(c_a)+S^(a+1)/((a+1)u)] = 0`

and the flatness of its reduced matrices. Another exact target is the root-of-unity period matrix: its Gram is `d*(I+J)` and has determinant `d^d`, where d=q+1. Integration convergence, holomorphic dependence, and determinant continuation along coefficient paths are written analytic proofs; the polynomial tests do not certify them.

The resulting period matrix Π is invertible for u nonzero. The original source map is `Π*j` with inverse `r*Π^-1`, on r(E). The original Gram G remains unchanged. Its period comparison is `G^-1 Π*Π`; the quotient-volume ratio is the ratio of determinants of these comparison operators at the same u,t. This identity is not an upper bound.

## 6. Finite-field source application and remaining estimate

Let R0 be the actual finitely generated coefficient subring containing 1/(q+1)!. Each specified finite-field specialization of characteristic p>q+1 gives the Artin–Schreier family `Y^p-Y=(Φ-tS)/u`, u nonzero. Deligne §§3.7.2–3.7.4 give its rank-q degree-one pure cohomology and lissity. These are cited historical theorems, not new Lean declarations in this package.

The infinity chart is explicit: write the potential as w^(-d)b with b(0)=1/(du), adjoin v by b v^d=1, and put x_inf=w v. Then the potential is x_inf^(-d), and v/d is the inverse of the v-derivative of b v^d−1. This retains the finite étale cover and every coefficient. It is the local constant-at-infinity model in the lissity argument, not an extension over u=0.

There is no asserted comparison identifying its Frobenius with the original A. The rank-one χ=S−3/4 calibration explicitly prevents that inference. No uniform estimate for the original four-volume budget, or the singular u=0 period comparison, has been proved.

## Delivery verification

Consult CHECKS.md and the raw JSON/logs. The new finite suite passes 22 methods in both Python modes and rejects three false controls. The parent 23-method suite was also replayed in both modes. This is not a Lean certificate. The add-only patch preserves every inherited file and has no remote side effect.
