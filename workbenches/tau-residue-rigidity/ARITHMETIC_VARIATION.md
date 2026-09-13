# A signed arithmetic correction certificate on the original source quotient

13 September 2026. This is an additional written finite-dimensional theorem and research continuation. The monic residue, invariant-constituent and supported-source results have their separate Lean execution record. No asymptotic arithmetic estimate is asserted here.

## 1. Keep the arithmetic problem and both source realizations fixed

For a fixed actual zero packet h and tensor degree k, keep the original cyclic polynomial chi=chi_(h,k), all its nilpotent orders, E=C[S]/chi, the same full remainder/jet observation J_N, and the same relation inclusion B_N given by multiplication by chi. The arithmetic source is built from (2xi/h), not from a freely chosen polynomial counterexample. The Gamma reference is a comparison metric on the same finite polynomial presentation, not a replacement arithmetic quotient.

Write M_0=M_N^Gamma and M_1=M_N^ar for the two strictly positive source Gram matrices, in the same specified source coordinates. The source mass, coordinate S=k/2+ix, arithmetic Taylor unit in J_N, and all coefficient phases are retained. The following parameter s is NEW: it interpolates these two source metrics. It is neither the auxiliary exponential-family t nor the earlier representative-curve z nor the Laplace tilt theta.

For 0<=s<=1 put

  M(s)=(1-s)M_0+sM_1,    Delta M=M_1-M_0.

At each s take the unique original least-norm section R(s), characterized by

  J R(s)=I,    B* M(s) R(s)=0,    G(s)=R(s)* M(s) R(s).

At s=0 and s=1 these are exactly the reference and arithmetic sections. The positivity is automatic from the two endpoint source matrices. No spectral purity or arithmetic upper bound is assumed.

## 2. The derivative stays inside the original relation space

Let H(s)=B* M(s) B. All inverses below exist for the given full-column-rank relation inclusion. At the first admitted degree, the relation space is zero and every expression involving its projector is the zero map; no negative degree or inverse of a nonexistent moment matrix is needed.

Since J R'=0, exactness gives R'=B C for a unique coefficient map C. Differentiate B* M R=0 to obtain

  B* Delta M R + H C=0.

Thus

  R'=-B H^(-1) B* Delta M R.                                      (AV1)

This is an ORIGINAL polynomial relation. Applying the specified arithmetic source realization and the existing division-by-chi primitive puts it in the original theta boundary, not merely in an unspecified finite-jet kernel. Across s the cohomology class and full arithmetic jets are constant.

Differentiating G=R*MR kills both mixed terms by B*MR=0 and gives

  G'=R* Delta M R.                                                 (AV2)

Put Z=B* Delta M R. Differentiating (AV2), with Delta M constant and using (AV1), gives

  G''=-2 Z* H^(-1) Z <= 0.                                        (AV3)

No commutation of matrices is assumed. These identities distinguish the exact derivative from a frozen-section surrogate.

## 3. Endpoint slopes give a two-sided log-volume certificate

Let f(s)=log det G(s). The determinants are positive real. Jacobi differentiation gives

  f'=Tr(G^(-1) R* Delta M R),
  f''=Tr(G^(-1)G''-G^(-1)G'G^(-1)G') <= 0.                        (AV4)

For the sign, G'' is negative semidefinite and G' is Hermitian; the second trace is the trace of the square of G^(-1/2)G'G^(-1/2). Hence f is concave. Define the actual endpoint slopes

  d_N^Gamma = Tr((G_N^Gamma)^(-1) (R_N^Gamma)* Delta M_N R_N^Gamma),
  d_N^ar    = Tr((G_N^ar)^(-1)    (R_N^ar)*    Delta M_N R_N^ar).

Integrating the decreasing derivative over [0,1] proves

  d_N^ar <= log(V_N^ar/V_N^Gamma) <= d_N^Gamma.                    (AV5)

There is also a purely matrix proof of (AV5): the minimum principle gives G_1<=R_0*M_1 R_0, and log det X<=Tr(X-I) for a positive matrix gives the upper inequality after congruence by G_0^(-1/2). Interchanging the endpoints gives the lower inequality. The differential proof provides the exact retained relation and the curvature lost by the linear bound.

## 4. Crucially, combine the correct sides for the signed four-endpoint expression

Put a=q-1,b=q,c=2q-1,d=2q and T_N=V_N^ar/V_N^Gamma. The arithmetic correction is

  C=log(T_a)+log(T_b)-log(T_c)-log(T_d).

Equation (AV5) yields a finite computable bracket with no matrix logarithm:

  d_a^ar+d_b^ar-d_c^Gamma-d_d^Gamma
       <= C <=
  d_a^Gamma+d_b^Gamma-d_c^ar-d_d^ar.                              (AV6)

Subtracting two independently upper-bounded quantities would NOT justify this upper bound: the negative terms use the lower endpoint slopes. The current generic Gamma counterexample has Delta M=0 and all slopes zero, as it should. On the actual arithmetic source the sign and tensor-degree dependence come from its actual moment differences; positivity alone assigns neither.

For the existing four-volume strategy, a sufficient new analytic target would be an appropriate negative upper estimate for the right side of (AV6) at scale q_k log k, together with the required reference comparison. This note proves the finite bracket only. It does not infer the sign from the presence of a split base or auxiliary finite-field purity.

## 5. An exact source-density expression identifies the arithmetic input

For the same source coordinate row p_N(x), let r_(N,s)(x)=p_N(x)R_N(s), and set

  kappa_(N,s)(x)=r_(N,s)(x) G_N(s)^(-1) r_(N,s)(x)* >=0.

If the source measures have densities m_ar,m_Gamma, the finite integrals defining their moments give

  d/ds log V_N(s) = integral kappa_(N,s)(x) (m_ar-m_Gamma)(x) dx,
  integral kappa_(N,s)(x) m_s(x) dx = q.                          (AV7)

Every term is integrable: kappa is a finite polynomial expression and the original measures have the finite moments already assumed by their source matrices. There is no infinite limiting interchange here.

The four-endpoint contrast of these kappa functions has integral zero against m_s, because q+q-q-q=0. Its pairing with m_ar-m_Gamma is the exact signed correction derivative. This removes common scalar mass changes automatically while keeping their original values. It does not presume a sign for the contrast.

## 6. Connection with the residue formalization

The Lean continuation proves the actual residue duality and the nonzero constituent transverse response without assuming a favourable metric. For every nonzero proper A-invariant F,

  pi_F R inc_F = [1]_(E/F) tensor ell_F

has exact rank one. In the original source metric its coupling is

  c_F(G_N) = norm_[G_N,quotient]([1])^2 * norm_[G_N|F,dual](ell_F)^2 > 0.

This nonvanishing is an input to the previously written constituent-period curvature formula. The new AV1-AV7 continuation addresses a different quantitative issue: how the full canonical source metric changes between the reference and actual arithmetic measures. Neither calculation silently equates a residue detector with an action-compatible map to a pure Frobenius line.

## 7. Evidence and scope

The accompanying exact-rational checker tests polynomial remainder duality, repeated invariant constituents, and independent inverse-matrix derivations of AV1-AV3 on finite positive-moment fixtures. Rational logarithm enclosures test AV5-AV6. These are declared finite calibrations, not evaluations of actual zeta zero packets. Their observed execution belongs to the CI record. The general arguments AV1-AV7 are written proofs, not extra Lean declarations in this contribution.

The original SplitZero source and quotient APIs, the earlier metric restriction certificates, and the current arithmetic-input conditions remain untouched. This is a continuation of the programme, not an assertion that one failed generic implication closes it.
