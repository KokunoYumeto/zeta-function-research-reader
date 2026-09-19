# The full native-to-arithmetic coefficient metric return

19 September 2026. This is the joint metric comparison on the original coefficient space, not a replacement of the native common-kernel restriction by a different subspace. It combines the full arithmetic-image estimate in Note 8 with the supplied complete native value LRC24.

## 1. Both forms on the identical original coefficients

Retain a=k+4, q=(a+1)^2, m=16a-48-v, the original L_a, M=I_4 tensor L_a, and the original four cutoffs

    (N_0,N_1,N_2,N_3)=(q-1,q,2q-1,2q).

The signs of the native return are (-1,-1,+1,+1). Denote this operation by R_native. On C^(4m) define

    Gcal_N=M* diag(G_N[m_a],4) M,
    Dcal_N=diag(D_(a,N-v)^(s),4),  s=1 or a,
    T_N=Gcal_N^(-1/2) Dcal_N Gcal_N^(-1/2).              (N1)

Gcal_N is the literal arithmetic pullback. Dcal_N is the complete native Gamma coefficient form after the lower-evaluation minimum. They have the same coefficients, but their definitions and all original source masses remain those stated in (N1).

Set

    F_ar=logdet Gcal_(q-1)+logdet Gcal_q
         -logdet Gcal_(2q-1)-logdet Gcal_(2q).

Note 8 proves

    0<=F_ar<=-8m log(1-beta_a),
    beta_a=exp[-c q+O_h(a+log q)]

on its explicit eventual guards. The coefficient 8m is twice the dimension 4m; it is not an inserted tensor-order factor.

## 2. Evaluate the complete relative determinant

The actual one-copy native return is

    Tnative_(a,s)
      =R_native logdet D_(a,N-v)^(s)
      =16 C_partial a q-128q log a+O_actual(q).

This is the supplied LRC24 value, with both source orders and the fixed actual conductor retained. Taking determinants in (N1) gives the exact relation

    R_native logdet T_N=4 Tnative_(a,s)+F_ar.            (N2)

Thus the finite interval is

    4 Tnative_(a,s)
      <=R_native logdet T_N
      <=4 Tnative_(a,s)-8m log(1-beta_a),               (N3)

and the evaluated leading and logarithmic terms are

    R_native logdet T_N
      =64 C_partial a q-512q log a+O_actual,h(q).        (N4)

The same calculation at the original boundary energies Gamma_0 or Gamma_1 is especially transparent. Those are fixed positive forms for this entire window; their definitions use the two complete cutoff differences. Consequently

    R_native logdet(Gamma_i^(-1/2) Dcal_N Gamma_i^(-1/2))
      =4 Tnative_(a,s),  i=0,1.                        (N5)

The fixed boundary determinant cancels between the four cutoffs. It is not set to one in any individual metric. These formulas evaluate the full coefficient-metric return through its q log a term. They do not evaluate its remaining order-q coefficient, nor any individual native flag allocation.

## 3. An exponential lower bound for every uniform comparison constant

For one copy, the native forms increase with the cutoff. Let L_{a,s} be the larger of the largest generalized eigenvalues on the two original links

    D_(a,2q-1-v)^(s) relative to D_(a,q-1-v)^(s),
    D_(a,2q-v)^(s) relative to D_(a,q-v)^(s).

Both have dimension m. Each determinant ratio is no greater than L_{a,s}^m, so

    L_{a,s} >= exp(Tnative_(a,s)/(2m)).                 (N6)

The explicit dimension m=16a-48-v and the native value yield

    liminf_(a->infinity) q^(-1) log L_{a,s}
       >=C_partial/2>0.                               (N7)

The same eigenvalues, each repeated four times, occur in Dcal. Arithmetic pullback forms decrease with N, because they are attained minima in nested original source fibres.

Let 0<alpha_a<=beta'_a be any constants satisfying the actual uniform form comparison at all four cutoffs

    alpha_a Gcal_N <= Dcal_N <= beta'_a Gcal_N.          (N8)

Such constants exist at each finite a, since there are four positive pairs. On either low-to-high link, monotonicity of Gcal gives

    Dcal_high <= beta'_a Gcal_high
              <= beta'_a Gcal_low
              <= (beta'_a/alpha_a) Dcal_low.

Therefore every pair of constants in (N8) obeys the explicit bound

    beta'_a/alpha_a >= exp(Tnative_(a,s)/(2m)),
    liminf q^(-1) log(beta'_a/alpha_a)>=C_partial/2.     (N9)

These inequalities are unchanged by any single fixed invertible coefficient map applied by congruence to both sequences. Thus the exponential comparison cost is not a basis artifact. They do not bound every individual relative eigenvalue from below, and do not claim that all directions grow at the same rate.

## 4. Consequence for the original programme

The arithmetic coefficient-image returns are exponentially small, while the native full return is of order a q. Equations (N2)–(N9) give their exact joint determinant relation and a mandatory exponential uniform condition cost. This is the quantitative comparison needed before replacing one metric by the other in a projected calculation.

The original common kernel I*G_N I and the independent degree-k PRD value metric Q_N are not substituted by Gcal_N. Native restrictions and attained quotients can distribute (N4) differently; the actual angular projectors still determine that distribution. No scalar in (N4) is assigned to an individual member of the seven-term tuple, and it is not introduced as an additional term in the full canonical action.
