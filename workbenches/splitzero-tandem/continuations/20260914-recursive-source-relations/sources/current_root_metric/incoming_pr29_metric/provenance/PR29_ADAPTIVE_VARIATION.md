# Adaptive signed correction and residue-coupling control

This supplements ARITHMETIC_VARIATION.md with complete written finite-dimensional proofs. These formulas are not additional Lean claims. The parameter s always denotes the interpolation of two specified source metrics, not the period parameter t or the Laplace tilt. The intermediate density (1-s)m_Gamma+s m_ar is only an explicit comparison density on the same finite polynomial presentation; it is not claimed to be the k-fold convolution of an interpolated one-factor amplitude.

## 1. Convergent slope certificate, using finite linear algebra

Keep f_N(s)=log det G_N(s) and

  d_N(s)=Tr(G_N(s)^(-1) R_N(s)* (M_N^ar-M_N^Gamma) R_N(s)).

AV1-AV4 prove f_N'=d_N and that d_N is continuous and nonincreasing on [0,1]. Take any partition 0=s_0<...<s_r=1. Monotonicity on each interval and integration give

  L_N=sum_j (s_(j+1)-s_j)d_N(s_(j+1))
      <= log(V_N^ar/V_N^Gamma) <=
  U_N=sum_j (s_(j+1)-s_j)d_N(s_j).                                (AC1)

Each slope uses only the original two source matrices, their canonical quotient sections, and finite inverses and traces. No numerical matrix logarithm or eigenvector is required. For mesh delta,

  U_N-L_N <= delta * (d_N(0)-d_N(1)).                             (AC2)

Indeed each positive slope decrement is multiplied by an interval length at most delta, and their sum telescopes. For the uniform partition into r intervals the width is exactly (d_N(0)-d_N(1))/r. Thus the enclosure converges with an explicit finite stopping rule for each fixed source pair. This is not a uniform bound in tensor degree k; conditioning and input-moment uncertainty remain.

For the signed four-endpoint correction C, define a=q-1,b=q,c=2q-1,d=2q. Then

  L_a+L_b-U_c-U_d <= C <= U_a+U_b-L_c-L_d.                       (AC3)

Its width is the sum of the four widths. In particular, a uniform partition provides width at most r^(-1) sum_N (d_N(0)-d_N(1)), where N ranges over the four original endpoints. This targets the SIGNED arithmetic correction identified by the transfer audit; it does not make the invalid subtraction of two unrelated upper bounds.

Certified intervals for each slope can be inserted in the same orientation: use lower bounds on right-end slopes in L_N, upper bounds on left-end slopes in U_N. Positivity/invertibility of each moment and quotient matrix must itself be certified. The explicit widths from approximate slopes include their interval errors in addition to AC2.

## 2. A direct bridge to the residue coupling

Let F be a nonzero proper invariant constituent of the actual cyclic algebra E, with original inclusion iota and top residue ell_F. The formalized residue theorem gives 1 not in F and ell_F nonzero. For the same varying canonical metric G(s), define

  q(s)=min_(f in F) ||1-iota f||_(G(s))^2,
  d(s)=ell_F (iota*G(s)iota)^(-1) ell_F*,
  c_F(s)=q(s)d(s)>0.

To avoid a notation collision, this d(s) is the dual norm in this section, not the slope d_N(s) above.

Let v_Q(s)=1-iota (iota*G iota)^(-1)iota*G1 be the actual orthogonal representative of the quotient-unit class, and v_F(s)=iota (iota*G iota)^(-1)ell_F* the actual Riesz representative of the restricted residue. Then

  q=v_Q*G v_Q,   d=v_F*G v_F.

Differentiating the minimum at its orthogonal representative removes its tangential derivative. Differentiating the inverse restricted Gram gives the opposite sign for the dual norm. Therefore

  d/ds log c_F(s)
   = (v_Q*G'v_Q)/(v_Q*Gv_Q) - (v_F*G'v_F)/(v_F*Gv_F).            (AC4)

With AV2, G'=R*Delta M R, both terms are Rayleigh quotients of the ACTUAL source-metric difference on the two displayed representative directions. Common scalar mass changes cancel between the terms. In particular,

  |d/ds log c_F(s)|
   <= lambda_max(G^(-1/2)G'G^(-1/2))
      -lambda_min(G^(-1/2)G'G^(-1/2)).                          (AC5)

No equality between the period-coordinate metric and G is introduced. The previously written period curvature uses its own metric H(t)=Pi(t)*Pi(t) and its same coefficient c_F(H); comparing that to c_F(G_N) still uses the specified period/source metric operator. The point of AC4 is to identify exactly which arithmetic source directions control the residue coupling during the reference-to-arithmetic comparison.

## 3. Continued integration with the original SplitZero source

In the Lean source module the generator P on the original fibre is now carried through the identity J P=(multiplication by S) J. Every power is proved to satisfy J(P^n x)=S^n Jx. Thus the bounded residue detector is evaluated along P^n r(x), not merely after a new independent choice of coefficient representative.

The original quotient is retained before the finite observation. A nonzero detected residue response is proved nonzero in that quotient using only J r=1 and the fact that J kills ORIGINAL boundaries. No equality of the full observation kernel with those boundaries is assumed. At a nonbottom support its represented zero remains distinct from absence. Across support transitions the two already checked source-section and coefficient-operation defects remain required; the new fibrewise residues are not presumed natural for arbitrary changing packet polynomials.

The finite slope enclosures and the rank-one residue response are separate results. Neither supplies the missing arithmetic sign or a pure Frobenius realization automatically. They provide explicit original-source computations that a further arithmetic argument can use.
