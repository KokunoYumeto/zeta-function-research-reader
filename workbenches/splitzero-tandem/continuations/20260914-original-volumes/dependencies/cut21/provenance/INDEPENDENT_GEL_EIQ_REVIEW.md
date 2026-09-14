# Independent review of the full Gamma ensemble leading return

Review scope: complete mathematical reading of GEL1–19 and EIQ1–33, plus direct rereading of the original LET19–21 definitions and transfer signs. This review did not run Lean, build a PDF, or inspect remote material. It does not claim those operations occurred.

Status: ACCEPTED. The three requested presentation repairs are installed and directly reread: GEL7 defines the bounded-above kernel on every probability, GEL5 specifies 0 < eta < 2, and the header identifies the actual provider. The final source also propagates WGP finite expansions and RWB analytic positivity; the complete WGP1–14 and RWB1–27 proofs were additionally read and checked for these new claims.

## Original source and scale

For t = q^2 x, the original pushforward density becomes q sigma(q sqrt(x)) x^(-1/2) dx. Multiplication of omega by B_q yields exactly this density. Thus the power q^(2an + 2n(n-1)) in GEL3 includes precisely the t^a factors and the squared Vandermonde; the remaining Jacobian and source mass are in B_q. The parity dimensions sum to n+(n+1)+n+n=4n+1=2q+1, which independently checks GEL14's coefficient.

The Euler-product comparison is correct: the decreasing logarithmic summand gives I <= S <= I+log(1+b^2/lambda^2). At lambda=1/4 this yields the powers -3/4 and +1/4, exponential exp(-pi |y|/2), and upper factor exp(1/2). The B_q upper exponent -(pi q/2-3/2)sqrt(x) and the lower compact-support factor both retain the original scale. Real exponents a > -1/2 are precisely the integrable domain at zero.

## Equilibrium provider

All 33 EIQ statements were read. The endpoint derivative has the strictly negative sign ((t-1)(t-r^2))/(r^2 t); the endpoint ratio ranges from 1 to 0. The arcsine endpoint identities retain the constants 0 and 2pi. The positive density is sqrt((b-x)(x-a)) h(x)/(2pi), with h(x)=beta/(2pi x) integral sqrt(s)/((x+s)R_s) ds. Its mass calculation gives -alpha/2+beta v E/(2pi)=1.

The branch R(x) is negative to the left and positive to the right. Hence the proved Cauchy transform gives U'=R h and the strict Euler inequality on both exterior components, including the component adjacent to zero. The signed logarithmic-energy argument uses a correct Gaussian integral with constant 1/sqrt(4pi t), and proves strict positivity for every nonzero zero-mass difference. Its integrability justification covers the competitors used in the variational comparison. This establishes the global minimizer rather than merely a candidate density.

The Fourier calculation of L_s preserves the term -2 R_s log(1-eta zeta_s). The elementary integral EIQ26 then follows with coefficient beta/(4pi). Fixed-interval coordinates and uniformly dominated derivatives establish parameter continuity; the two-sided variational squeeze has derivative partial_alpha F=+L. The scale identity for the beta parameter and the first square-root moment have the correct factors 2.

## Ensemble convergence and moving shifts

The Q_n comparison to V_(alpha-epsilon,beta-3epsilon) is valid: the difference b sqrt(x)-a log(x) has b >= 2epsilon and 0 <= a <= 2epsilon, and log(x) <= sqrt(x) for x >= 1. The compactified kernel truncations are continuous; the bound r(x)+r(y) proves uniform endpoint decay. The diagonal correction is exactly M/n. Compactness followed by monotone convergence proves convergence of the truncated maxima to the actual equilibrium value.

The lower-bound change to the equilibrium probability and Jensen's inequality preserve n(n-1) pair terms, the original source prefactor, and the entropy term. All required logarithms are integrable because the support is finite and positive and the density is bounded with square-root endpoint decay. The prefactor is O(n log q+n log n), hence negligible on the n^2 scale.

The finite-shift result uses convex secants at four fixed exponents. It does not differentiate an asymptotic error. Moving a/n -> 2 and shifts l/n -> 0 are covered; after multiplication by n l the result is exactly GEL13. This remains correct for the separate size n+1 and exponent q+1 occurrences.

## Low endpoint, original row products and final sign

The direct Gamma moment bounds imply log(mu_a)=2a log(a)+O(a), uniformly for integer a>=1. Convex secants at q/2,q,2q,4q therefore bound the original low-moment logarithmic ratio by O(l log q). The two product row intervals each have q terms; removing the j shift costs at most 8l^2, and the left/right Riemann sums cost O(l). These terms are all o(q l) along the original packet.

Substitution in the unchanged LET19 definition gives W_k/(q l) -> 2L-4(2log(2)-1). The leftover 2l log(q) is explicitly retained before being shown o(q l). LET20 has the correct sign: T-W is bounded by its proved O(k) errors, while R^0-R^sigma=-T. The arithmetic receiver retains B_ar=B_0+delta_sigma-T with no invented growth estimate for the other summands.

The established remainder is o(q l). Neither an o(q) remainder nor a completed estimate for the other arithmetic summands follows from this review. This scope matches the source's explicit theorem.

## Final propagation delta and source pins

GEL17a reproduces WGP10 exactly, including each signed quadrature contribution. GEL17b reproduces WGP13 exactly: the third-order logarithmic contribution is -(l^4+l^2/4)/q^2, and its remaining positive fourth-order bound is 7(192l^5+80l^3-2l)/(1440q^3). At m=1 the displayed third-order contribution tends to -1/256. The finite enclosure is preserved before passing to the leading limit.

The entire RWB proof was independently read for GEL18a. Differentiating the original Gamma product gives yL(y)-(pi/2)|y| in [-1/2,3/2]. The inverse-square identity on P_j^(a+1), its Cauchy–Schwarz bound, and the even/odd polynomial derivative identity yield the stated lower bound for c_j^(a) with both the a and j dependence. The low coefficient uses the opposite, upper bound in the negatively signed term. Counting the 2q+1 positive coefficients and preserving both source-product row intervals gives the finite RWB20 lower remainder. The original multiplication operator provides the RWB24 upper bound, hence W<=6lq. These facts transfer to the existing leading limit and prove 4log(27/(8pi))<=C_Gamma<=6, with strict positivity established by the rational analytic lower bound. No numerical quadrature or unproved determinant estimate is used for this conclusion.

Final reviewed SHA256 values:

- GEL complete revised source: `2014e7fefdcd963b70b00fb89d597e24c0826582a2541dd1ff44d63051979fc1`.
- EIQ complete equilibrium provider: `a0a0346a19d0e035a186590dbbd69881cdf7a30e8fef602d47bba0932f175e731`.
- WGP complete product source: `e6122af0f0cc54028ceee5383c97070e7738d9d8ec1a5bc5481b349761e5fbfe`.
- RWB complete recurrence source: `580f282cb2be5225383da4913dec33810d5482a5d02097ed594173f0bc70b87f`.
- LET source, with LET19–21 directly reread for this review: `a31250b693b9e687481bc7bfa7638707013930c4bfb9b6a8f39c201779d02a44`.

The EIQ section uses a locally bound elliptic modulus k in (0,1). GEL denotes that modulus by kappa; the original packet k=4l+1 is a separate explicitly scoped symbol. The cumulative assembly should retain this dictionary or spell out the local binding.

