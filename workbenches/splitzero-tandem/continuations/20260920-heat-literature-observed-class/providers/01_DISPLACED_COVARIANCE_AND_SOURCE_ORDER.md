# Displaced lower covariance and matched native return through order q

19 September 2026. New calculation on the original fixed simple-quartet, five-orbit conductor domain. The independently retained proper source is identified separately in Section 9. The argument imports the preceding absolute-Gamma baseline and LRC full monic-norm bounds at their written-proof status; it is not an independent proof audit of every analytic provider.

## 1. Original parameters and fixed endpoint constants

Retain
\[
a\equiv1\pmod4,\quad q=(a+1)^2,\quad Q=(a-7)^2,
\quad\Delta=q-Q=16a-48,\quad v=\operatorname{ord}_0E_A,
\]
with the actual nonzero conductor coefficient and original period/branch. The source order is exactly s=1 or s=a. Put
\[
\ell=(s-1)/4,\quad n=Q+\ell,\quad m=\Delta-v,
\quad H=2\Delta-v-\ell.
\tag{D1}
\]
The lower root grid is degree a-8. Its affine centre remains (a-8)/2, while its source order remains s. Its original cutoffs are q-v-1,q-v,2q-v-1,2q-v.

Use the original EIQ measure for V(x)=pi sqrt(x)-2 log(x), without changing its energy convention. Write its endpoints as u^2,v_e^2:
\[
uK(\kappa)=2,\quad v_eE(\kappa)=4,\quad
\kappa^2=1-u^2/v_e^2.
\]
Define
\[
w=(u+v_e)/2,\quad z=uv_e,\quad c=(v_e^2-u^2)/4,
\]
\[
L=6\log w-2\log z-2,\quad
\lambda=8-4\log w-2\log c,\quad F=-\lambda/2-3+L,
\]
\[
C_B=9-8\log2+F,\quad C_\Gamma=2L-8\log2+4,
\]
\[
C_\sigma=F+6-\tfrac32L-6\log2+2\log\pi,
\quad M_{-1}=\frac{u^2+v_e^2-4uv_e}{2u^2v_e^2}.
\tag{D2}
\]
These are the constants in the preceding absolute-Gamma proof and the original ECL identities. For the row calculation set
\[
a_0=\log(4/\pi),\quad
 a_1=2(1-\log2)-\lambda/4=C_B/2-C_\Gamma/4,
\]
\[
b_1=\tfrac12\log c-\log2,
\quad C_\partial=2C_B-8a_1+4a_0,
\]
\[
K_2=C_B-4a_1+2b_1-2\log2
=2\log(w^2/z)-4\log2,
\quad\eta_h=(\gamma^2-\delta^2)/3.
\tag{D3}
\]

## 2. The exact covariance-to-minimum relation

The distinct-root evaluation map is VJ_N, with the original complete remainder J_N. Its value covariance is V G_N^{-1} V^*. In the complex-linear numerator convention the covariance can be its entrywise conjugate; its positive determinant is the same. Thus
\[
\log\det K_N=2\log|\det V|-\log\det G_N.
\]
The fixed Vandermonde factor cancels under the original signs (-,-,+,+). No covariance is identified with a minimum Gram itself.

Let R_r be the determinant of the complete rank-r relation Gram for the lower polynomial, in source order s. The four original cutoffs give exactly
\[
\mathcal C^-_{a,s}
=\log R_{m+q}+\log R_{m+q+1}
-\log R_m-\log R_{m+1}
-\sum_{r=m}^{m+q}c_{r-m}\log h_{Q+r,s},
\tag{D4}
\]
where c_0=c_q=1 and the other c_r=2. The rank-r relation Gram is the full attained one, not a product of trial norms.

## 3. Row functions and the low-rank endpoint expansion

On the same real polynomial coordinate use the power-exponential measure
\[
d\nu_n(y)=|y|^{2n-1/2}e^{-\pi|y|/2}\,dy.
\]
Let h_r(n) be its monic squared norm and define
\[
\tau_r(n)=\log h_r(n)
-\log\{\Gamma(n+r+1)\Gamma(n+r+1/2)\},
\]
\[
T_R(n)=2\sum_{r=0}^{R-1}\tau_r(n)+\tau_R(n).
\tag{D5}
\]
This reference is introduced through the exact Gamma factors and bounded root comparison in Section 5; its mass is not substituted into the original source without those factors.

The retained LRC monic-norm bound, with r=0,1 separately given by the scalar Gamma moments, is
\[
\tau_r(n)=2n\psi(r/n)
+O\!\left(1+\log^+\frac n{r+1}\right),\quad0\le r\le2n,
\tag{D6}
\]
\[
\psi(t)=(1+t)(1-\log(1+t))
-\frac t4\lambda(2/t,\pi/t).
\]
For t>0 its exact endpoint equations are u_tK=2 and v_tE=2(1+t). They imply
\[
\psi'(t)=\log\frac{\kappa_t}{E(\kappa_t)}
=\tfrac12\log c_t-\log(1+t).
\tag{D7}
\]
In particular psi(0)=a_0, psi(1)=a_1, psi'(1)=b_1.

The low expansion needed here is
\[
\boxed{\psi(t)=a_0+\tfrac t4\log t
+(a_0-\tfrac14)t+O(t^{3/2}).}
\tag{D8}
\]
Indeed the defining elliptic equations give
\[
\kappa_t^4=16t+O(t^{3/2}),\quad
w_t=\frac4\pi[1+3t/4+O(t^{3/2})],
\quad c_t=(4/\pi)^2\sqrt t[1+O(\sqrt t)].
\]
The exact Robin identity reduces psi to
\[
\psi(t)=\log w_t+\tfrac t2\log c_t-(1+t)\log(1+t),
\]
which proves (D8), including its linear constant.

## 4. Use the absolute baseline and only the displaced O(a) rows

The preceding absolute-Gamma calculation, with no root grid inserted, gives the complete reference centre
\[
T_n(n)-T_0(n)=C_Bn^2+C_\sigma n+O(\log(n+2)).
\tag{D9}
\]
This is the ordinary real-power reference centre for every integer n. Its parity blocks have sizes floor(n/2),ceil(n/2); the four blocks from ranks n,n+1 retain the same order-n coefficient. The Gamma mass cancels between each source monic norm and its relation norm.

The displaced row interval is exactly
\[
T_{m+q}-T_m
=(T_n-T_0)+(T_{n+H}-T_n)-(T_m-T_0).
\tag{D10}
\]
Only |H|+m=O(a) rows are newly estimated. Their combined D6 error is O(a log a), rather than an error independently charged on q rows.

Taylor expansion at one gives, with oriented sums also covering negative H,
\[
T_{n+H}-T_n
=4nHa_1+2H^2b_1+O(H^3/n+|H|\log(n+2)).
\tag{D11}
\]
At the low endpoint retain the trapezoidal identities
\[
\sum_{r=0}^{m}c_r r=m^2,\qquad
\sum_{r=0}^{m}c_r r\log r
=m^2\log m-m^2/2+O(\log(m+2)),
\]
where the weights refer to the interval 0,...,m and 0 log 0=0. Equations D6 and D8 give
\[
\boxed{T_m-T_0=4nma_0+\tfrac12m^2\log(m/n)
+(2a_0-\tfrac34)m^2
+O(m^{5/2}/\sqrt n+m\log(n+2)).}
\tag{D12}
\]
The coefficient -3/4 contains the low-rank quadrature contribution. It cannot be recovered by treating all low ranks as a nonsingular t=1 expansion.

## 5. Restore the original Gamma order, mass, and roots

For ell=(s-1)/4 the exact original Gamma density is
\[
w_s(y)=\frac{(2\pi)^{s/2}}{\sqrt2\Gamma(s/2)}
\prod_{j=0}^{\ell-1}[y^2+(2j+1/2)^2]\,\sigma(y).
\tag{D13}
\]
The Gamma tail factor sqrt(2), together with (D13), gives the same scalar (2pi)^{s/2}/Gamma(s/2) as in its original source norm
\[
h_{Q+r,s}=\frac{(2\pi)^{s/2}}{\Gamma(s/2)}
\Gamma(n+r-\ell+1)\Gamma(n+r+\ell+1/2).
\tag{D14}
\]
These scalars cancel at the monic-ratio level. Expanding the paired Gamma factors relative to ell=0 gives the full source contribution
\[
-2\ell^2\log2+O(a).
\tag{D15}
\]
The linear-in-ell term is O(a), and the third remainder is O(ell^3/n)=O(a). The residual positive Gamma polynomial in (D13) has log size O(ell^3/y^2) on the original outer support, giving the same O(a) determinant cost. Its inner contribution is bounded by the retained complete-polynomial localization, not dropped.

The actual lower roots have second moment
\[
\sum\omega^2=\eta_h Q(Q-1).
\]
In the literal square coordinate x=(y/n)^2 their multiplier is
\[
\log\frac{|Q_{a-8}(n\sqrt x)|^2}{n^{2Q}x^Q}
=-\frac{\eta_h Q(Q-1)}{n^2x}+O_h(Qa^4/n^4).
\]
The original analytic-factor determinant expansion in the full parity blocks therefore contributes
\[
-2\eta_h\frac{Q(Q-1)}n M_{-1}+O_h(a+\log n).
\tag{D16}
\]
The two low ranks contribute O_h(a), not a new order-q term. This is the full opposite-root moment; no eigenvalue or multiplicity is removed. The complete root and tail restoration uses the preceding full-form bounds before taking either minimum.

## 6. The evaluated lower covariance

Combining D9--D16 gives
\[
\boxed{\begin{aligned}
\mathcal C^-_{a,s}={}&C_Bn^2+4n(Ha_1-ma_0)
+\frac{m^2}{2}\log(n/m)+2H^2b_1\\
&-(2a_0-\tfrac34)m^2-2\ell^2\log2+C_\sigma n
-2\eta_h\frac{Q(Q-1)}n M_{-1}\\
&+O_{h,v}(a^{3/2}+a\log(a+2)).
\end{aligned}}
\tag{D17}
\]
The convention at m=0 is m^2 log(n/m)=0. The original lower application has m>0 on its admitted eventual domain. The remainder is o(q).

For a direct coefficient formula put epsilon=0 at s=1 and epsilon=1 at s=a, and define
\[
Z(v)=1024(a_1-2b_1)-176C_\partial
+4v(a_1-a_0)-192+512\log2,
\]
\[
Z_\Delta=4C_\partial+16(2b_1-a_1).
\tag{D18}
\]
Then
\[
\boxed{\begin{aligned}
\mathcal C^-_{a,s}={}&C_Bq^2+
[-16C_\partial+\epsilon C_\Gamma/4]a q
+128q\log a\\
&+q[C_\sigma-2\eta_hM_{-1}
-\epsilon C_\Gamma/4+\epsilon K_2/16
-Z(v)-\epsilon Z_\Delta]+o_h(q).
\end{aligned}}
\tag{D19}
\]
The previously evaluated +128 term is retained. Equation D19 evaluates its remaining order-q coefficient, including the fixed conductor order.

## 7. Gamma-order conversion through k^2

For the original full packet at any fixed primary multiplicity m_0, retain q=[1+k(m_0-1)](k+1)^2 and ell=(k-1)/4. The exact order-one/order-k difference is
\[
\boxed{\mathcal B_k[w_k]-\mathcal B_k[\sigma]
=\ell q C_\Gamma+\ell^2K_2+O_h(k\log(q+2)).}
\tag{D20}
\]
Here w_k is the original order-k Gamma source, not the one-factor arithmetic density w_h.

For a direct verification, the high parity-block exponent shift gives
2q ell L+2ell^2 L_alpha. The exact source product subtracts
4q ell(2log2-1)+4ell^2log2. The low scalar moment costs O(ell log q); the third energy remainder and Gamma polynomial cost O(ell^3/q); the root cross correction costs O_h(ell k^2/q). The original ECL derivative is L_alpha=log(w^2/z). This proves D20 with all roots and low moments retained.

The coefficient has a determined strict negative sign:
\[
\boxed{-4\log2<K_2<2\log(121/160)<0.}
\tag{D21}
\]
To prove the upper bound let r=u/v_e. The defining equation is rK/E=1/2, increasing in r. The tan-coordinate integral gives K<=2+log(1/r), while E>=1. At r=1/10 this is strictly less than 1/2 because log10<3. Hence r>1/10 and
1<(1+r)^2/(4r)<121/40. Substitution in K2 proves D21.

The exact original correction conversion is
\[
\delta_{k,k}^{ar}=\delta_{k,1}^{ar}
-\ell qC_\Gamma-\ell^2K_2+O_h(k\log q).
\tag{D22}
\]
On the simple stratum, the preceding signed arithmetic value yields
\[
\delta_{k,k}^{ar}=-\tfrac14C_\Gamma kq
+q[\tfrac{\log2}{\pi}I_h-\tfrac74C_\Gamma-K_2/16]+o_h(q).
\]
For fixed m_0>=2 the order-q coefficient is -(4m_0-9/4)C_Gamma. The reference difference and correction difference cancel in the unchanged full action.

## 8. The complete correlated native return, not separate allocations

Retain the original exact NCT/TAC identity
\[
\mathcal B_a^{(s)}=\mathcal C^-_{a,s}
+\mathcal Re^C+\mathcal T_{a,s}+F_{L_a}^{(s)}+\Xi_{a,s}.
\]
Give the complete last four terms the single name N_{a,s}; none is removed. The natural upper baseline from D20 and the preceding absolute-Gamma coefficient is
\[
\mathcal B_a^{(s)}=C_Bq^2+\epsilon C_\Gamma aq/4
+q[C_\sigma-2\eta_hM_{-1}-\epsilon C_\Gamma/4
+\epsilon K_2/16]+o(q).
\]
Subtract D19 in that exact identity. The complete correlated result is
\[
\boxed{N_{a,s}=16C_\partial aq-128q\log a
+[Z(v)+\epsilon Z_\Delta]q+o_h(q).}
\tag{D23}
\]
This does not assign Z(v) to T, Xi, the conductor transport, or a flag separately. Each remains in its original position in the sum.

## 9. Actual degree-k ambient return at the proper-source displaced cutoffs

The same derivation applies directly to the following two original applications; it is not a replacement of their row families. Keep s=1 or k, ell=(s-1)/4,
\[
q_k=(k+1)^2,\quad Q_k=(k-7)^2,\quad
\Delta_k=16k-48,\quad b=q_{k+4}-q_k=8k+24.
\]
For an actual root degree R, width w, and cutoff decrement d, the four cutoffs are w-d-1,w-d,2w-d-1,2w-d. In D17 substitute
\[
n=R+\ell,\qquad m=w-d-R,\qquad H=m+w-n,
\]
and replace Q(Q-1) by R(R-1). Only m,H=O(k) displaced rows are used in these applications. The upper source has (R,d)=(q_k,0); the literal lower source has (R,d)=(Q_k,v). The standard width is q_k and the actual proper-source width is q_k+b. Its source order and degree remain k.

Let N_{k,s}^{disp} be the upper-minus-lower complete ambient matched return at that displaced width, and N_{k,s}^{std} its standard-width value. Then
\[
\boxed{N_{k,s}^{disp}-N_{k,s}^{std}
=-128q_k\log k+C_{disp}q_k+o_h(q_k),}
\tag{D24}
\]
\[
\boxed{C_{disp}=1024(a_1-2b_1)-192
+256\log2+288\log3.}
\tag{D25}
\]
This coefficient is independent of the two source orders and the fixed conductor order at this precision.

The nonlogarithmic degree-two terms are
\[
4b\Delta_k(2a_1-a_0)-8b(2\Delta_k-v)b_1
+2(2a_0-\tfrac34)(\Delta_k-v)b,
\]
whose q_k coefficient is 1024(a_1-2b_1)-192. The full low-rank logarithmic difference is
\[
\tfrac12\left[b^2\log(q_k/b)
-(\Delta_k-v+b)^2\log\frac{q_k}{\Delta_k-v+b}
+(\Delta_k-v)^2\log\frac{q_k}{\Delta_k-v}\right]+o(q_k).
\]
Its two coefficients are -128q_k log k and
(256log2+288log3)q_k. This proves D24 without discarding either low interval.

The PRD value V_Q^p is a restriction followed by minimization on the original Z_R values, not this ambient matched return. The exact independent source and target-J Schur terms remain in M^p. D24 must not be used as their value.

## Evidence and remaining metric problems

The calculation uses the preceding absolute-Gamma proof, the original EIQ/ECL endpoint identities, LRC monic estimates, and NCT/TAC/PRD equalities. The new steps are the oriented low/high displaced-row summations, the second Gamma-order coefficient, and their exact return through the original signs. No growing arithmetic kernel was replaced by a constant-density model.

The original absolute observation-kernel determinant, the separate native directional flags, the independent proper-source scalar on Z_R, the preservation of its specific coefficient-cone subspaces, and the projected U,V signs remain additional tasks. The other notes in this package address original-map ranks, support, and observability, without assigning their unknown metrics.
