# Complete root review of the residue continuation

The root reviewer read the entire delivered NOTE.tex, RC1–53, and the entire new residue_constituent_extension_20260913.tex, initially RCX1–39 and then the final RCX1–40. The accepted mathematical source has SHA-256 `449d2107fb97369eeb27dfcc0151012da831222a25432cc5b3e1894ff06defc0`. The review includes the explicit Q4 addition, the tensor-degree typing repair and the complete FC comparison paragraph. No mathematical correction remains in this scope. This is a written mathematical review, not a new numerical or Lean execution.

## Endomorphism reconstruction and source lift

The power basis is justified by monic division over the actual commutative coefficient ring, including zero divisors. The residue matrix has its stated zero triangle and antidiagonal ones, so its determinant is exactly the column-reversal sign. For a coefficient matrix T, the matrix of the proposed sum of A^i R A^j is K times the residue matrix. Consequently K=T B_res^-1 gives the displayed inverse, with no discriminant inversion. The inverse residue rows give the actual dual coordinate rows, so the matrix units multiply with the stated Kronecker delta and sum to the identity. Monic division and the adjugate inverse commute with base change.

The source lift r_N T j_E is multiplicative because j_E r_N=I. Its identity is the actual idempotent r_N j_E; it is a unital representation in that corner, and j_E applied on the left and r_N on the right recover T. The original boundary is killed by j_E, so every lifted endomorphism kills the same boundary. The written scope does not assert boundedness of the observation on a larger Hilbert completion.

## Metric variation and all determinant factors

For a proper nonzero invariant constituent, the original unit lies outside the constituent and the restricted residue row is nonzero, by its cyclic orbit and the invertible residue form. Both factors of the coefficient are therefore strictly positive. The residual vector is orthogonal to the constituent; the vector representing the restricted residue dual belongs to it. Their squared norms are exactly the two factors q_M and d_M.

Along an actual differentiable positive-form path, the two residual-derivative terms vanish because the derivative stays in the constituent. Differentiating the inverse restricted form gives the negative dual contribution. Thus the logarithmic derivative is the difference of the two stated Rayleigh quotients, exactly Tr((Q_r-Q_w) M^-1 dot M). The two projections are orthogonal and have eigenvalues +1 and -1 on their respective lines. The spectral-spread bound and its equality conditions follow without deleting either vector length.

For the original straight path from G_i to G_j, the relative derivative has eigenvalues (lambda-1)/(1+s(lambda-1)); their order is preserved because the derivative with respect to lambda is positive. Integrating the extreme difference gives log(lambda_max/lambda_min). The product of eigenvalues in (0,1] is at most the least one, proving the complete endpoint chain in RCX21 with its correct directions.

The monic ideal frame J_g=I C retains C. Its last residue coordinate is one and earlier coordinates zero. The quotient-unit factor is the Schur complement ratio v_+/v_g; the residue dual factor is the last inverse cofactor v_-/v_g. This verifies RCX23–24, including p=1, the empty determinant and the explicit |det C| squared factor.

## Mixed jets, real derivatives and every ordered term

The global curvature equation follows from the normal period derivative and the complete log-Gram derivative. Differentiation at zero shows all mixed derivatives of total degree below four vanish, as do the (3,1) and (1,3) terms. The (2,2) derivative is the stated positive coefficient, and its Taylor coefficient has the required divisor 2!2!=4.

The real-axis derivative is the sum of the two Wirtinger derivatives. The second derivative contains twice the real part of the pure holomorphic second jet. The fourth derivative contains twice the real part of the pure fourth jet plus six times the mixed coefficient. The trace-log expansion in RCX32 has exactly the coefficients 1, -4, -3, 12, -6; cyclicity of trace, rather than commutation of its matrix arguments, combines the ordered words.

Root requested and independently computed the explicit fourth period derivative:

\[
Q_4=A_t^4/u^4-(R A_t^2+2 A_t R A_t+3 A_t^2R)/u^3+3R^2/u^2.
\]

Differentiating Q3 gives the three first ordered cubic-denominator terms and 3R²/u²; multiplying -A_t Q3/u supplies A_t^4/u^4 and the two additional ordered terms. The final source displays this full computation and retains R²=I in the q=1 case. Root also requested replacing the inaccurate phrase “real cochain degree” by the original tensor degree k≥1, with the separate real-parameter matrix identity explicitly stated. Both repairs are present in the accepted source.

The forced period equation retains +u Pi R. The source equation follows from the same j_E and its generator intertwining. The full quadratic primitive retains D_0 K, K A_t and -k K; in particular t K R remains. This agrees with the independently accepted LC12a.

## Translation and finite sampling

The Pascal substitution has determinant one, preserves the highest coefficient and the original unit, and therefore conjugates R to itself. The contour substitution keeps the scalar exponential, all polynomial columns and the connectors with their orientations. The connector estimate makes their integrals vanish. The stated period and constituent Grams follow with every factor of the scalar modulus retained. All derivatives of total order at least two of its affine holomorphic log modulus vanish, whereas the real first derivative retains the exact trace shift 2p Re(a).

The final RCX40 paragraph is the same computation as FC9. Its constrained minimum and inverse-restricted-form bounds give alpha/beta and beta/alpha with the full source factors retained. It is correctly crosswalked as shared mathematics, not a second discovery.

The historical translation source mismatch is already resolved by the separately sealed exact geometry-margin substitution. This review does not turn that typography history into a new mathematical objection. The complete raw source notes remain retained. No uniform arithmetic upper bound or RH conclusion is asserted by this acceptance.
