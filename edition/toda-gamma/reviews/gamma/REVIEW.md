# Independent gamma convolution intake and mathematical review

Outcome: no incorrect gamma normalization, conditional projection coefficient, arithmetic amplitude, finite Gram correction, or Toda substitution was found on the inherited admitted-degree domains. Two integration clarifications are recorded below: explicitly state those degree domains, and distinguish the theta boundary from its cochain primitive. The original archive and all 38 staged files are unchanged. No patch was applied, canonical file edited, or remote mutation performed.

## Intake and source identity

The user-supplied ZIP has 816,933 bytes and SHA-256 `4b93cc5e9db76fdc6dec406c05197e2de5d7daab5957a855ee8b77711652b61a`. Its 38 regular members passed path traversal, absolute-path, Windows collision, file-kind, encrypted-entry, CRC, compressed/expanded-size, SHA-256 and staged-byte checks. The 37-entry manifest covers exactly all other members; expanded size is 1,093,024 bytes. Archive content was treated as evidence, never as authority to execute its integration instructions.

Before running its checker, read the complete user overview, complete NOTE.tex (34,859 bytes; SHA-256 `7cf984d87de405b815250b44454c4ee27c8ab46574da245b377ebc6e49327fa2`) and complete check_gamma_descent.py (10,597 bytes; SHA-256 `e9ef0ae3e01180efc2c6fb24c1ccd46567b24423990225e382ca8231058c3d74`). Also read complete HANDOFF.md, CHECKS.md, SOURCE_REVIEW.md and checks/VERIFICATION.json; later read the complete numerical seed driver and its result. The numerical driver was not executed because its main entry writes into the immutable delivered stage.

The locally read complete inherited gamma reference is independently byte-identical to a fresh read-only GitHub contents response for commit `fa4be32f87a9a90f3c02a07f7790dea95a1e7b0f`, path `workbenches/splitzero-tandem/continuations/20260912-stieltjes/tex/theta_gamma_reference.tex`: 22,656 bytes, SHA-256 `a379a1e19de4ce885680e14bda466a37b4c1eb25228c19b931d573f58be167f9`, independently computed Git blob `89cee46828a36df716a8f4610098e922bdd055ec`. This closes the archive author's stated raw-byte provenance limitation; it does not update the historical PR22 status or claim a current formal certificate.

All 35 inherited Toda manifest rows match the separate previously reviewed Toda stage. Its complete review and relevant source-domain passages were read, but its 24-test suite was not repeated. The embedded integration patch was parsed only as data: its nine new-file payloads are byte-identical to their delivered counterparts, with no deletion or modification hunks. It was never applied.

## Gamma mass, polynomial scale and the actual sum map

Put alpha=2 lambda and keep the literal finite mass c_lambda=2^(1-2 lambda) Gamma(2 lambda). The beta/Fourier calculation, including the Jacobian t=2u, gives Fourier transform c_lambda cosh(y)^(-2 lambda). Uniqueness of finite Fourier transforms consequently gives

`r_lambda^(convolution k) = (c_lambda^k / c_(k lambda)) r_(k lambda)`.

Thus the constant is `2^(k-1) Gamma(2 lambda)^k/Gamma(2 k lambda)`, the total mass is c_lambda^k, and at lambda=1/4 it is (2 pi)^(k/2). The tensor index changes the reference shape to k lambda, not the original arithmetic scaling centre S=k/2+iu. Laplace continuation gives c_lambda^k cos(theta)^(-2 k lambda) on the stated strip.

For the product finite measure and its sum pushforward, U f=f composed with the sum is an isometry. The explicit fibre integral defining C divides by the actual pushforward density, not by a probability-rescaled substitute. Fubini gives C=U*, CU=1 and UC an orthogonal projection. The complement ker C is therefore present as a genuine Hilbert-space summand. These linear maps do not make projection an algebra homomorphism.

The generating function at phi=pi/2 has real form `(1+z^2)^(-lambda) exp(t atan z)`. Its leading coefficient is t^n/n!, so b_n=n! P_n(t/2;pi/2) is monic. Its generating integral gives norm c_lambda n!(alpha)_n; differentiation gives recurrence coefficient n(n+alpha-1). This agrees with the classical [DLMF generating function](https://dlmf.nist.gov/18.23.E7) and [DLMF recurrence](https://dlmf.nist.gov/18.22.E8), after the specified t/2 and factorial changes. No claim about a new classical convolution theory is made.

Multiplication of k generating functions proves the finite multinomial addition formula. Pair a tensor product with it and divide by the pushforward norm: the conditional projection coefficient is `product (alpha)_(n_i)/(k alpha)_n`. Polynomial completeness is justified by exponential moments: an L2 function orthogonal to all polynomials has an analytic Fourier transform in a smaller strip, all derivatives at zero vanish, and Fourier uniqueness kills the function. This promotes the polynomial pairings to the actual projection identity. Pythagoras then gives exactly the residual norm in (16), including c_lambda^k and the n! factor. It is not legitimate to drop that relative component.

## Arithmetic amplitude, bounds and coefficient closure

For s=1/2+it, s(s-1)=-(t^2+1/4) and pi^(-s/2)=pi^(-1/4) exp(-it log(pi)/2). The amplitude in (18) therefore retains the correct minus sign and complex phase. The quotient g/h is entire at the selected complete-order zeros, so its gamma-divided amplitude supplies the removable values. Multiplication by its k-fold product is an isometry of the specified weighted Hilbert spaces; the polynomial source is mapped to the amplitude times the original polynomial, not to an unweighted substitute. Passing to its squared modulus is an observation for the norm, not a replacement of the amplitude map or the full Taylor unit.

Convolution of w_h=B r_lambda gives the actual density m_h,k=B_h,lambda;k r_lambda,k by the same fibre integral. Its mass is mu_h^k. For k>=2, the one-factor isolated zero sets exclude only null fibre hyperplanes, proving positivity of the sum-density multiplier; k=1 retains its isolated zeros.

The elementary zeta continuation bound is sufficient. With |t|>=max(1,2 max|rho-1/2|), monicity yields |h|>=(|t|/2)^d; the displayed estimate `25*2^(2d)/sqrt(pi) * |t|^(6-2d)` follows. It is bounded for d>=3. For smaller packets, the gamma shift contributes exactly the nonvanishing factors `(j+1/4+it/2)`; L>=max(0,3-d) gives a bounded multiplier without changing w_h. For h=1, the three-factor denominator and the bound |zeta|<=4 sqrt(t^2+1/4) prove C=1024/sqrt(pi). This analytic seed has a nonzero measure but zero finite arithmetic quotient.

Because B is bounded in the selected reference, it and its product belong to the indicated L2 spaces. Pairing against each finite addition formula gives

`integral B_h,lambda;k b_n r_lambda,k = c_lambda^k n! [z^n] A_h(z)^k`.

Dividing by c_lambda^k n!(k alpha)_n proves (25). Every coefficient calculation is finite; no unjustified product of infinite formal series is integrated. The degree-zero coefficient retains mu_h^k. Parseval and orthogonal projection give the nonnegative residual norm (26).

Tensor telescoping plus projection contraction proves (27), with the displayed factor k and all mass factors. The first L one-factor coefficients determine every pushed-forward moment through degree L. Consequently only c_0 through c_(2N) are needed for the full degree-N source Gram and the actual relation Gram, since each original relation column still has degree at most N. A truncated density need not be pointwise positive; positivity of its admitted finite Gram follows from exact equality with the genuine positive Gram, not from the truncated plot.

The scalar seed numbers were read, not freshly recomputed or interval-certified. Their driver is consistent with the stated theta recurrence and upper-incomplete-gamma recurrence; its two finite cutoffs are numerical evidence only. They are not arithmetic-packet fixtures and do not locate or certify any zero.

## Same quotient, determinant correction and Toda control

The explicit tilted gamma determinant in (28) has mass c_lambda^(kn), product of j!(2k lambda)_j, and cosine exponent -n(2k lambda+n-1). The second logarithmic derivative is n(2k lambda+n-1) sec(theta)^2, which verifies the Toda induction and (29), including n=0 and n=1.

Expanding `conj(chi)(k/2-i d_theta) chi(k/2+i d_theta)` inside the Laplace integral gives exactly |chi(k/2+iu)|^2. Both signs and coefficient conjugation are essential. Replacing the u-monomials by original S-monomials changes Gram determinants by a triangular coordinate map whose diagonal has unit modulus; it adds neither a mass factor nor a new quotient. The source/relation determinant theorem therefore gives (31), with all arithmetic dependence retained in X and Y.

For the same remainder matrix J and injective old-relation columns B_chi, subtracting the term in (32) leaves JR=1 and makes B_chi* M_h R=0. These characterize the actual arithmetic least-norm lift. The empty relation block contributes the zero correction. Evaluating the source inequality on the gamma lift and minimizing on the arithmetic side proves G_h<=C_h^k G_gamma. Taking a determinant in the actual quotient dimension q gives the exponent kq, not the polynomial source dimension.

At theta=0, dividing consecutive source norms yields precisely `(N+1)(N+2k lambda) X_(N+2) X_N/X_(N+1)^2`. The quotient-volume ratio is the gamma ratio times T_(N-1)/T_(N+1). This is exactly (34), and substitution in the inherited scalar bound gives (35). The phase derivative is retained as the derivative of log V_gamma plus log T. A one-sided upper bound on each positive T cannot bound a consecutive T ratio, and the note correctly does not make that inference.

The tail inequality (36) follows from x^r<=r! a^(-r) exp(ax), the additional exp(b(x-T)) on the tail, and the two-sided gamma Laplace bound. Its factor 2, r!, c_lambda^k and C_h^k are all required. It gives a rigorous tail interface, not a certified compact quadrature or matrix inverse enclosure. Nonempty-packet constants still need their actual compact analytic quotient enclosed before numerical certification.

### Integration clarifications

1. The delivered gamma note inherits but never explicitly restates the Toda domains. State `q>=1, N>=q-1` for full quotient lifts, (31)-(33), and `N>=q` for the volume-ratio formula and upper bound (35). At N=q-1, V_(q-2) is not the determinant of an invertible full quotient, so use the inherited direct endpoint calculation instead. Keep q=0, chi=1 as the separate zero-dimensional quotient with empty determinant one. This is a domain omission in the standalone continuation, not a changed formula on the intended domain. The parent has accepted this clarification for its integrated copy.
2. Following (32), applying V_h,k to the relation-valued difference produces the original theta boundary. Its cochain primitive is obtained from the inherited primitive map on the relation preimage. Say this explicitly instead of identifying V_h,k itself with the primitive map. No new primitive construction is needed.

## Independent verification of the parent's analytic join

This is an additional parent-authored join, not a claim already asserted by the archive. Write M_h(theta)=integral exp(theta t) w_h(t)dt. On |z|<1 choose logarithms analytic and zero at z=0. The Cayley map w=(1+iz)/(1-iz) has positive real part, and

`atan z=Log(w)/(2i),  Re(atan z)=Arg(w)/2 in (-pi/4,pi/4)`.

Also Log(1+z^2)=Log(1-iz)+Log(1+iz) on this disk. On each compact subset the generating kernel and all its derivatives are bounded by a polynomial in |t| times exp(v|t|), for some v<pi/2. The established arithmetic exponential moments justify differentiation under the integral. Its nth Taylor coefficient divided by c_lambda is integral b_n w_h/(c_lambda n!)=(alpha)_n c_h,n. Therefore the formerly coefficientwise series is the Taylor series of the holomorphic function

`A_h(z)=c_lambda^(-1) (1+z^2)^(-lambda) M_h(atan z), |z|<1`.

For real |theta|<pi/4, tan(theta) lies in that disk and 1+tan(theta)^2=sec(theta)^2, proving

`M_h(theta)=c_lambda sec(theta)^(2 lambda) A_h(tan theta)`

and hence `Z_h,k(theta)/Z_gamma,lambda,k(theta)=A_h(tan theta)^k`. There is no extra tensor rescaling or missing mass. The real-domain restriction belongs with this series evaluation; a broader continuation should be separately specified, not inferred from the Taylor radius.

The jth theta derivative at zero inserts u^j in each source/relation Gram integrand. Its degree is at most 2N+j, so the exact finite coefficient requirement is c_0 through c_(2N+j). The same finite dependence passes to quotient derivatives through finite matrix inversion on N>=q-1. This does not supply a uniform smallness estimate for those derivatives or for the consecutive correction ratio.

## Executed checks and precise limitations

The unchanged delivered checker passed all 17 methods normally and under -O using Python 3.13.9 and SymPy 1.13.1, with zero failures/errors and byte-identical result JSON. Runs took 1.793 and 1.868 seconds; peak sampled child RSS was below 79 MB under a 200,000,000-byte cap and 90-second timeout. Both deliberately false --fail-control runs exited 1 with the intended RuntimeError. This is one explicit sentinel executed in two modes before the test suite, not two mathematical formula mutations. All four fresh logs were read completely. No usage errors or retries occurred.

The independent checker does not import the delivered checker. Its direct sec(theta)^alpha moment jets check literal mass, multinomial addition, projection pairings, retained relative norm, and the parent's analytic join through order six. A complex non-diagonal finite Gram fixture checks the original quotient and arithmetic orthogonality of the corrected lift. Fifteen explicit equalities pass in each mode, along with positivity/upper-bound checks. Six altered formulas are actually rejected per mode: probability normalization, omitted addition multiplicity, omitted Pochhammer denominator, omitted inverse mass, omitted relation correction, and wrong complex conjugation. Peak Windows working sets were 80,842,752 and 80,486,400 bytes. These finite fixtures are not actual zeta packets; the analytic proof remains the mathematical evidence for the infinite statements.

No inherited 24-method Toda replay, local Lean, browser-render audit, interval arithmetic, source promotion, archive rewrite, Git mutation, or publication action was performed. This review does not certify the separate formal PR, an RH conclusion, an arithmetic asymptotic, or the outstanding small consecutive-determinant bound.
