# Independent audit of the marked equilibrium provider

Date: 2026-09-14. Reviewer: delegated `verify_formulas` agent.

**Accepted final inputs:**

- `MACROSCOPIC_MARKED_EQUILIBRIUM.tex`, 19,177 bytes, SHA-256
  `8ce2d8a2587fffdf3bff1fbddb68c7ad140cb1a1dddbbbfa2daf36762f44108c`.
- `endpoint_existence.tex`, 12,724 bytes, SHA-256
  `94a36d5eacafd7944a9dd2bdbafe1fbbd226ca139431d2651a9989d3a52504d0`.

The main provider was read in full, including KME1–24 and KME22a, and its
final notation changes and added KME25 were separately read and checked. The
endpoint argument was previously constructed and checked directly; its
final parameter-derivative and Jacobian notation was rechecked against
the indicated final bytes. No builds were performed.

## Correction found and resolved

The first main input had the original packet symbol `c` in the expectation
formula immediately before KME22a: its last term was `-c M_kappa(kappa^2)`.
This coefficient must be `kappa`. The parent repaired it, and the corrected
display was read in the final input identified above. The boxed KME22a
already had the correct `kappa/2` coefficient. The final endpoint input
also correctly uses `partial_kappa` for both lower-limit derivatives and
uses `mathcal J_kappa` for its endpoint Jacobian. It thereby retains the
original packet centre `c=k/2` and the edge logarithmic integral `J_kappa`
as their actual separate quantities.

## Density, global energy, and entropy

KME6 follows with the stated coefficient from the first actual endpoint
equation. Its positive integral proves strict positivity on the whole
positive x domain. The mass in KME9 is exactly one: the m terms cancel by
the first equation and the remaining expression is -1+B_kappa/2.
KME8 has the correct removable value at z=-s; substitution into the
Cauchy transform produces KME10 with the stated sign and factor one half.
Its integral representation has continuation off exactly the support cut.
The sign of the branch outside the support and positivity of H_kappa give
the full exterior variational inequality, including the interval next to
zero.

The Gaussian positivity argument retains the correct half factor and
Fourier coefficient. Its truncated scalar kernels have the required
absolute logarithmic domination. Finite energy supplies the signed
measure integrability needed in the expansion. The resulting equality
criterion proves unique global minimization, not merely stationarity.

The fixed-interval probability density has the correct factor (b-a)^2.
The compact parameter bounds established by the endpoint proof and the
positive integral for H_kappa supply upper and positive lower bounds for
the other density factors. The probability reference omega has mass one
under x=t^2, and the displayed Radon–Nikodym derivative in KME17 is exact.
The square-root endpoint factors make both stated absolute entropy and
logarithmic interaction integrals finite uniformly over the parameter
interval.

## Elementary endpoint integrals and all energy constants

For KME18–19, the angular averages of log(x+z), x log(x+z), and
log(x+z)/(x+s) are respectively

    log(C_z),
    m log(C_z) + d theta_z,
    [log(C_z) + 2 log(1-theta_z theta_s)] / D_s.

Combining these with the displayed polynomial division gives exactly
Q_s(z). In particular the term -d theta_z has the correct sign and
depends on z. The positive H_kappa representation and the endpoint
equation then produce the coefficient one half in KME20.

At the right edge the logarithm is
log(d/2) - 2 sum_{j>=1} cos(j phi)/j. Its first angular cosine average
is -1. Consequently the corresponding x-logarithm average is
m log(d/2)-d, and the last denominator average has
+2 log(1+theta_s). These give exactly the edge Q expression in KME21.
The Abel-limit justification is adequate: for r near one the negative
logarithm is bounded by a constant plus 2|log(phi)|; away from r=1 it
is uniformly bounded. All remaining endpoint singularities are integrable.

The dilation x -> r x changes the pair interaction by exactly -log(r).
Its minimizing derivative therefore gives integral x V'_lambda = 1,
and hence the arctangent expectation is exactly 3. With the corrected
coefficient the potential expectation is

    6 + 2 kappa - 2 M_kappa(0) - kappa M_kappa(kappa^2).

Together with ell_kappa=V_lambda(b)-2J_kappa and the integrated Euler
equality, this proves every constant and sign in KME22a.
The scalar integral in KME23 independently preserves the additive term
-2 kappa log(kappa)+2 kappa. It yields KME22 with the stated convention
at zero. The exact two-minimizer comparison gives
dF_lambda/dlambda=2 M_{2lambda}(4lambda^2), including the factor two,
the right derivative at zero, and the integrated identity in KME24.
No additional displayed algebra errors were found in the accepted input.

## Exploratory quadrature

`KME_EXPLORATORY_QUADRATURE.py` and its emitted JSON record a separate
35-decimal-digit mpmath calculation of the two endpoint systems and KME22a.
The full run took approximately 0.55 seconds. It observed

    F_0          = -2.99473470406767666890732015924
    F_(1/4)      = -2.34401877092453046529699203491
    correction   =  0.541931858730318060277587077923
    Psi_(1/4)    =  0.108784074412828143332741046407

The correction used exactly
2[H(5/2)-H(3/2)-H(2)+H(1)], with H(z)=z^2 log(z)/2-3z^2/4.
These decimal values are **exploratory observations, not interval
enclosures, certified signs, or proof certificates**. Proof acceptance
above rests on the displayed exact calculations, not those values. The
scope of this audit is the full equilibrium provider and its energy
formulas; it makes no claim about a finite-degree remainder or a limiting
determinant interchange outside the provider.

## Final delta: packet symbols and the convexity estimate

The earlier complete proof read accepted main input
`712181bd695410af112723c7db23e65bc4dbaf0f7b493f3b463a1040f1ceef85`.
The subsequent notation delta writes the local midpoint and half-width
as m_end and d_end, preserving the original packet m and d. All occurrences
in the transforms, Q functions, angular integrals, and the edge expression
were checked; the edge coefficient remains exactly d_end/2=(b-a)/4.
The script uses local computational variables m,d for these explicitly
defined endpoint quantities; its original at-execution input hash is
retained in the JSON, since these notation changes do not change its
mathematical formulas. The numerical run was not repeated for re-pinning.

The added KME25 differentiates the objective for fixed compactly supported
probability measures. A first version omitted the finite-logarithmic-energy
restriction, which would include atomic measures with objective -infinity
and no ordinary second derivative. That omission was reported and repaired.
The final input above was then read and its exact hash verified. It restricts
the differentiated class to finite logarithmic energy. The actual proved
equilibrium measures belong to this class, so the supremum over the class
is exactly F_lambda for every parameter. Each real objective has second
derivative 16 lambda integral 1/(x+4lambda^2) dmu >= 0. Taking its supremum
preserves the convexity inequality. The established right derivative at
zero is 2M_0(0), and the convex secant inequality therefore yields exactly
F_lambda-F_0 >= 2lambda M_0(0). This final addition is accepted.
