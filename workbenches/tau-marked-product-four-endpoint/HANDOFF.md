# Marked-product and signed-endpoint handoff

This is a continuation of the original tau-based programme, not a no-go result
for F1 geometry. The preceding audit remains a constraint on particular
auxiliary purity implications. The original marked base and its two
observations are reconstructed in NOTE Sections 2–3.

## Inputs and integration

The resumed intake read the original `SplitZeroTauBase.lean`,
`TAU_RECOVERY_MATHEMATICS.md`, and
`workbenches/tau-split-integration/RESEARCH_NOTE.md` at mathematical integration
867454a00c64291c4498a36769ccd36508c63458. The subsequently observed publication
head was aea6471ac6cf36f7c5e660d8698dce6b0606196e. These are pins, not a claim to
have inspected every later commit. The current integration's distinction
between section defects and coefficient-action defects is retained in (45).

## New exact targets

1. **External family on the original packet h.** For d=deg h, the k-fold
   complex has differential sum_i (u partial_i+h(s_i)-t_i) ds_i wedge.
   Leading-term reduction splits each factor; tensoring gives a free rank-d^k
   top module in degree k. Its coefficient specialization at u=t_i=0 is the
   original full E_h tensor k. The literal chain map at that fibre is
   P -> P(D)phi_* in degree zero and P -> P(D)F_h in degree one.
   Top cohomology map contains multiplication by the complete Taylor unit.
   The positive-characteristic exponential family has weight k by the actual
   Deligne theorem, not weight one relabelled k.

2. **Cyclic relation away from the marked fibre.** Fixed-order division
   chi(S)P=sum_i h(s_i)Q_i gives
   [chi(S)P]=sum_i[t_i Q_i-u partial_i Q_i] in the full product family.
   This term must not be dropped. At the marked fibre it is zero. The full
   tensor family, its cyclic inclusion and its quotient remain.

3. **One common arithmetic/Gamma source.** Let M(x)=M_gamma+x(M_ar-M_gamma)
   on P_(2q), with exactly the same J and B=multiplication by chi. Its
   quotient sections satisfy
   C'_N=-B(B*MB)^-1 B*DeltaM C_N,
   G'_N=C_N*DeltaM C_N,
   G''_N=-2 C_N*DeltaM B(B*MB)^-1 B*DeltaM C_N.
   These are original relation-valued source derivatives. All four degrees
   are restrictions of the same top matrix, not independently chosen forms.

4. **Signed correction without separate endpoint estimates.** With
   L_N(u)=v_N C_N G_N^-1 C_N* v_N*,
   Delta_hk=integral_0^1 integral (m_ar-m_gamma)
      (L_(q-1)+L_q-L_(2q-1)-L_(2q)) du dx.
   The signed kernel equals an actual relation-shell density minus an actual
   source-shell density. Each has mu_x-mass 2q. The exact source identity
   hv_h=g turns the original relation norm into the full i,j cross-pairing
   sum in (46); this is an arithmetic input, not generic positivity.

5. **Finite signed numerical enclosure.** In the original top M_gamma
   metric, let delta=||M_gamma^-1 DeltaM|| and
   a=min(1,lambda_min(M_gamma^-1 M_ar))>0. For m midpoint intervals,
   absolute integration error <= (8q+4)/(12m^2)*(delta/a)^3.
   Arithmetic moment rounding and tail errors must additionally be enclosed.
   The constant is finite and calculated for the supplied source; no uniform
   asymptotic control of it is asserted.

6. **Original first-pair calculation.** For h=(S-1/2)^2+gamma^2,
   |h|^2 w_h=w_1. Equations (73)–(76) give all four canonical quotient
   volumes from the five even moments of w_h, with exact arithmetic seed
   relations. `numerics/first_pair.py` is a numerical illustration only;
   its files, when present, are not interval or root certificates.

## Scope that must remain

- G(R), its support and amplitude maps, the infinite integer quotient, and
  the original support transports remain. No general replacement semiring
  tensor or derived six-functor library is asserted.
- Polynomial packet subcomplexes are D-stable; full dilations are compared
  in the original V and B through the explicit source primitive (22).
- The analytic parameter family specializes over tau. Its parameter origin
  is not silently identified with the absolute base point or with the
  Boolean localization at P_tau.
- The finite-field family is pure of weight k on u!=0; its Frobenius is not
  assumed to intertwine the original real dilation action.
- The original quotient and the larger kernel of a finite observation stay
  separate through their displayed quotient map.
- No opposing uniform four-volume upper estimate, RH, GRH, or failure of the
  entire F1 programme is asserted.

## Reproduction

Run `python checks/check_math.py` and `python -O checks/check_math.py`.
`checks/EXECUTION.json` records only runs actually captured in this package.
The negative control must fail with the explicit e=tau message.
The tests are exact finite symbolic fixtures, not asserted zeta packets.
There is no new Lean execution in this continuation.
