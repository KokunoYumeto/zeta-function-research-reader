# Full original word spectrum, rectangle product, and observed heat

Independent derivation, 21 September 2026. This file proves the received full-word continuation from the actual original polynomial and complete attained metrics. It uses the literal unpaired-root argument IC19–34 of the retained collision proof; it does not use the received complex-translation norm shortcut. The inherited equilibrium input and its EIQ source status are exactly those recorded in IC23–33. The present derivation does not replace that source status with a claim of an independent EIQ proof.

The exact original period matrix, conductor pivot, source measure, native comparison constants, and J1–J7 joint-source assumptions remain those of IC1–18. Every constant may depend on the fixed original quartet, divisor, and nonzero pivot. The variable is the original physical coordinate \(S=k/2+iy\). No origin, leading coefficient, period, or logarithm branch is changed.

## 1. Exact word, quotient, and all positive modes

Let \(k\ge9\), \(k\equiv1\pmod4\), \(0<\delta<1/2\), \(\gamma>2\), and set
\[
n=k-7,\quad d=n^2,\quad q=(k+1)^2=(n+8)^2,\quad
\Delta=q-d=16n+64=16k-48,\quad m=8k-16.
\tag{FW1}
\]
For the actual largest nonzero lexicographic conductor coefficient \(a_{r_*s_*}\), retain
\[
\omega_{ab}=(2b-k)\gamma-i(2a-k)\delta,\qquad
\mathcal I=\{r_*,\ldots,r_*+n-1\}\times\{s_*,\ldots,s_*+n-1\},
\]
\[
\partial=\{0,\ldots,k\}^2\setminus\mathcal I,\quad
D(y)=\prod_{\mathcal I}(y-\omega_{ab}),\quad O(y)=\prod_\partial(y-\omega_{ab}),
\quad Q_k=DO,\quad T=D(M).
\]
The full root-value map identifies \(E_k=\mathbb C[y]/(Q_k)\) with \(\mathbb C^q\). All nodes are distinct. In these coordinates \(T\) has exactly \(d\) zero diagonal entries and \(\Delta\) nonzero entries \(D(\omega)\), \(\omega\in\partial\). Thus
\[
V=\ker T=O\mathcal P_{<d},\qquad W=\operatorname{im}T=D\mathcal P_{<\Delta},
\qquad E_k=V\oplus W.
\tag{FW2}
\]
This is a direct sum in the original coefficient vector space; its metric need not be orthogonal. The exact conductor argument IC4–7 gives \(K\cap V=0\) and, in the same root order,
\[
I_K=\binom F{I_\Delta}J_\partial,\qquad
F=-A_\mathcal I^{-1}A_\partial,\quad
\det A_\mathcal I=a_{r_*s_*}^{d},\quad \operatorname{rank}J_\partial=m.
\tag{FW3}
\]
The transpose defining the conductor is complex-linear transpose, as in IC4. The full invariant equations still determine \(\operatorname{im}J_\partial\); it is not replaced by the whole conductor kernel. The conductor order \(v=\operatorname{ord}_0E_A\), including its positive-order strata, is unchanged.

Write \(G=G_N\) in full root-value coordinates, \(\pi=\pi_\partial\), and
\[
B=(\pi G^{-1}\pi^*)^{-1},\quad
W_G=G|_W\text{ in boundary-value coordinates},\quad
D_\partial=\operatorname{diag}_{\omega\in\partial}D(\omega).
\]
The minimum section \(s=G^{-1}\pi^*B\) satisfies \(\pi s=I\), \(s^*Gs=B\), and \(\operatorname{im}s=V^{\perp_G}\): all three identities follow by multiplying the displayed matrices, and \(Gs\) annihilates \(\ker\pi=V\). The map \(T\) on this section is the boundary-value map \(b\mapsto D_\partial b\), with target norm \(W_G\). Consequently the entire nonzero spectrum of \(T^{\dagger_G}T\) is
\[
\operatorname{spec}^+(T^{\dagger_G}T)
=\operatorname{spec}\bigl(B^{-1/2}D_\partial^*W_GD_\partial B^{-1/2}\bigr),
\tag{FW4}
\]
and its remaining \(d\) eigenvalues are exactly zero. In particular,
\[
\det{}^+(T^{\dagger_G}T)=|\operatorname{Res}(O,D)|^2\frac{\det W_G}{\det B}.
\tag{FW5}
\]
Our resultant convention for monic \(O\) is \(\operatorname{Res}(O,D)=\prod_{O(\omega)=0}D(\omega)\). The factor \(\operatorname{Res}(Q_k,D)\) is zero and is never substituted here.

Let \(\mathsf V_O\) evaluate coefficient polynomials of degree below \(\Delta\) at every boundary root. A class \(Dp\) has all its degree-at-most-\(N\) representatives exactly of the form \(D(p+Oh)\), because every representative vanishes on every root of \(D\). Therefore
\[
D_\partial^*W_GD_\partial=\mathsf V_O^{-*}\mathfrak G_N\mathsf V_O^{-1},\quad
\mathfrak G_N[p]=\min_{\deg(p+Oh)\le N-d}\int_{\mathbb R}|D(y)|^2|p(y)+O(y)h(y)|^2d\mu_k(y).
\tag{FW6}
\]
The four quotient degrees are exactly \(\Delta-1,\Delta,q+\Delta-1,q+\Delta\). Their original source degrees remain \(q-1,q,2q-1,2q\).

Use the complete proved bounds IC19–34, including their eventual finite guards, full Gamma source mass \(M_\sigma=\sqrt{2\pi}\), native constants \(\ell_k,u_k\), and unpaired root comparison. Put
\[
a_0=\log(4/\pi),\quad c_L=2q\log q+(2a_0-2)q,\quad
c_H=c_L-C_\partial q/2.
\]
With the explicit IC31 error \(\varepsilon_k=O_{h,\varpi}(k\log(q+2))\), IC32 states
\[
e^{c_{L/H}-\varepsilon_k}I_\Delta\preceq\mathfrak G_N
\preceq e^{c_{L/H}+\varepsilon_k}I_\Delta.
\tag{FW7}
\]
This is an estimate of every quadratic form before any restriction. In particular it is applicable to all \(\Delta\) directions at once, rather than being inferred from a determinant or a fixed number of singular values.

Here are explicit extra constants that turn FW7 into the complete original-word singular estimate. Put \(R=k\sqrt{\delta^2+\gamma^2}\),
\[
A=\frac{\Delta e^2}{M_\sigma}(2q+1)^{3/2}(4q+1)^{R+1},\quad
B_0=\Delta M_\sigma\left(\frac{2\Delta+R}{2\delta}\right)^{2(\Delta-1)},
\]
\[
b_-=\ell_k/A,\quad b_+=u_kB_0,\quad
C_V=\max\{1,\Delta\max(1,R)^{\Delta-1}\},\quad
C_{V^{-1}}=\max\left\{1,\sqrt\Delta\left(\frac{1+R}{2\delta}\right)^{\Delta-1}\right\}.
\]
IC12–13 proves \(b_-I\preceq B\preceq b_+I\). The Frobenius norm of \(\mathsf V_O\) is at most \(C_V\). Each inverse column is a full Lagrange polynomial, whose coefficient one-norm is at most \(((1+R)/(2\delta))^{\Delta-1}\), so \(\|\mathsf V_O^{-1}\|\le C_{V^{-1}}\). Set
\[
\mathcal E_k=\varepsilon_k+2\log C_V+2\log C_{V^{-1}}
+\max\{|\log b_-|,|\log b_+|\}=O_{h,\varpi}(k\log(q+2)).
\tag{FW8}
\]
Applying these norm inequalities to FW4 and FW6 proves, for every index without exception,
\[
e^{c_{L/H}-\mathcal E_k}\le s_j(T;G_N)^2\le e^{c_{L/H}+\mathcal E_k},
\qquad 1\le j\le\Delta.
\tag{FW9}
\]
The return signs remain \(\mathcal Rf=f_{q-1}+f_q-f_{2q-1}-f_{2q}\). Summing the logarithms gives
\[
\left|\mathcal R\log\det{}^+(T^{\dagger}T)-\Delta C_\partial q\right|
\le4\Delta\mathcal E_k=O_{h,\varpi}(k^2\log(q+2))=o(kq).
\tag{FW10}
\]

## 2. Exact rectangle potential and finite root-product error

For \(a,b\ge0\) define
\[
\mathscr F(a,b)=ab\log(a^2+b^2)-3ab+a^2\arctan(b/a)+b^2\arctan(a/b),
\tag{FW11}
\]
with continuous endpoint values. Its first derivative is
\(\mathscr F_a=b\log(a^2+b^2)-2b+2a\arctan(b/a)\), and \(\mathscr F_{ab}=\log(a^2+b^2)\). Both \(\mathscr F(a,0)\) and \(\mathscr F(0,b)\) vanish. Integrating this mixed derivative proves
\(\mathscr F(a,b)=\int_0^a\int_0^b\log(x^2+y^2)\,dy\,dx\), including the integrable corner singularity by passage to the limit.

Define, without changing any original source measure,
\[
U(z)=\frac1{4\delta\gamma}\int_{-\gamma}^{\gamma}\int_{-\delta}^{\delta}
\log((\Re z-s)^2+(\Im z-t)^2)\,dt\,ds.
\]
For \(0\le x\le\gamma\), \(0\le y\le\delta\), its edge profiles are
\[
u_H(x)=\frac{\mathscr F(\gamma+x,2\delta)+\mathscr F(\gamma-x,2\delta)}{4\delta\gamma},\quad
u_V(y)=\frac{\mathscr F(2\gamma,\delta+y)+\mathscr F(2\gamma,\delta-y)}{4\delta\gamma}.
\tag{FW12}
\]
These follow by splitting the rectangle at the vertical or horizontal line through the edge point. Their common corner value is
\[
u_C=\log[4(\gamma^2+\delta^2)]-3+
\frac\gamma\delta\arctan(\delta/\gamma)+\frac\delta\gamma\arctan(\gamma/\delta).
\tag{FW13}
\]

Let \(R_0=\sqrt{\delta^2+\gamma^2}\) and \(z_*=(2s_*-8)\gamma-i(2r_*-8)\delta\). The interior roots are exactly
\[
z_*+\gamma(2j+1-n)-i\delta(2i+1-n),\quad 0\le i,j<n.
\]
Thus \((\omega-z_*)/n\), for \(\omega\in\partial\), is outside the closed rectangle and has distance at least \(\delta/n\) from it. Its interior root grid consists of the centres of the \(n^2\) equal rectangular cells. Put
\[
E_n=2\left\lceil(2R_0/\delta+1)^2\right\rceil\log(3R_0/\delta)
+(4R_0/\delta+1)^2\left[1+\left\lceil\log_2(5n)\right\rceil\right].
\tag{FW14}
\]
Then, at every boundary root, including the nearest ones,
\[
\left|\log|D(\omega)|^2-2d\log n-dU((\omega-z_*)/n)\right|\le E_n.
\tag{FW15}
\]
To prove this finite assertion, let \(a=R_0/n\) be a cell radius. The centres have separation at least \(2\delta/n\). The number within distance \(2a\) of the evaluation point is at most \(\lceil(2R_0/\delta+1)^2\rceil\), by packing disjoint disks of radius \(\delta/n\). On such a cell all distances lie between \(\delta/n\) and \(3a\); the maximum oscillation of the logarithm is therefore \(2\log(3R_0/\delta)\).

For a farther centre at distance \(r>2a\), the first Taylor term averages to zero and the Hessian norm of \(\log|z-w|^2\) is \(2/|z-w|^2\). The average remainder is at most \(a^2/(r-a)^2\le4a^2/r^2\). In an annulus \(2^{j+1}a<r\le2^{j+2}a\), disk packing bounds the number of centres by \((2^{j+2}R_0/\delta+1)^2\). The whole annular error is at most \((4R_0/\delta+1)^2\). The greatest centre distance is at most \(2R_0+15R_0/n\); divided by \(2a\) it is at most \(n+15/2\le5n\) for \(n\ge2\). Summing these annuli and the near cells proves FW14–15. No boundary point is omitted.

## 3. Complete resultant expansion and phase

Write \(r=\gamma/\delta\), and define the average of the two full edge profiles by
\[
\bar u=\frac12\left(\frac1\gamma\int_0^\gamma u_H(x)dx+
\frac1\delta\int_0^\delta u_V(y)dy\right).
\]
An exact primitive of \(\mathscr F(a,b)\) in its first argument, vanishing at zero, is
\[
\mathscr J(a,b)=\frac{ba^2}{2}\log(a^2+b^2)-\frac{11}{6}ba^2
+\frac{a^3}{3}\arctan(b/a)+ab^2\arctan(a/b)-\frac{b^3}{6}\log(1+a^2/b^2).
\tag{FW16}
\]
Differentiation cancels its rational terms and gives \(\partial_a\mathscr J=\mathscr F\). Substituting FW12, changing \(a=\gamma\pm x\), and then using FW16 proves
\[
\bar u=\log[4(\gamma^2+\delta^2)]-\frac{11}{3}
+\frac43[r\arctan(r^{-1})+r^{-1}\arctan r]
-\frac16[r^{-2}\log(1+r^2)+r^2\log(1+r^{-2})].
\tag{FW17}
\]
The normal derivative on the top face is
\[
g_H(x)=U_y(x,\delta)=\frac1{4\delta\gamma}
\int_{x-\gamma}^{x+\gamma}\log\left(1+\frac{4\delta^2}{s^2}\right)ds.
\]
Its endpoint logarithmic singularity is integrable. The vertical-face derivative is obtained by interchanging \(\delta,\gamma\). Integrating these derivatives along their face gives
\[
L_H=\frac\delta{2\gamma}\int_{-\gamma}^\gamma g_H(x)dx
=\tfrac12\log(1+r^{-2})-\frac1{2r^2}\log(1+r^2)+\frac2r\arctan r,
\]
\[
L_V=\tfrac12\log(1+r^2)-\frac{r^2}{2}\log(1+r^{-2})+2r\arctan(r^{-1}).
\tag{FW18}
\]
For a direct integration, interchange the two integrals to replace the face average by \(\int_0^{2\gamma}(2\gamma-s)\log(1+4\delta^2/s^2)ds\); use integration by parts on its constant and linear factors. This yields the displayed expressions. Their logarithmic terms cancel in \(rL_H+r^{-1}L_V\), and the two arctangents sum to \(\pi/2\); hence that combination is exactly \(\pi\).

For integer \(j\in\{0,\ldots,8\}\), set
\[
A_j=j^2+(8-j)^2,\qquad
B_j=\frac{j(4j^2-1)+(8-j)(4(8-j)^2-1)}3.
\]
There are \(8n\) horizontal noncorner boundary points, \(8n\) vertical ones, and \(64\) corner points. The horizontal outward layer displacements from the scaled rectangle are \((2j-1)\delta/n\), with \(r_*\) layers on one side and \(8-r_*\) on the other; vertical displacements use \(\gamma\) and \(s_*\). Their sums of odd layer indices and their squares are precisely \(A_{r_*},B_{r_*}\) and \(A_{s_*},B_{s_*}\).

Set
\[
L=2\sqrt{\frac\pi{\delta\gamma}},\quad B_g=\frac\pi{\delta\gamma},
\]
\[
C_g=\frac43 B_g(\gamma^2+\delta^2)
+2L(\delta A_{r_*}+\gamma A_{s_*})
+\tfrac12B_g(\delta^2B_{r_*}+\gamma^2B_{s_*})+960LR_0,
\]
\[
B_{r_*,s_*}^{\rm pivot}=64(u_C-\bar u)+A_{r_*}L_H+A_{s_*}L_V.
\tag{FW19}
\]
The complete finite expansion is
\[
\left|\log|\operatorname{Res}(O,D)|^2-
\left(2\Delta d\log n+\Delta d\bar u+dB_{r_*,s_*}^{\rm pivot}\right)\right|
\le\Delta E_n+nC_g.
\tag{FW20}
\]
Here is the full layer error argument. Rearrangement of the radial decreasing function \(1/|z-w|\), or the layer-cake area bound \(|\mathcal A\cap B(z,t)|\le\min(|\mathcal A|,\pi t^2)\), gives
\(\int_\mathcal A|z-w|^{-1}dw\le2\sqrt{\pi|\mathcal A|}\). Thus \(|\nabla U|\le L\) everywhere, by integration of its locally integrable derivative. On the exterior of a horizontal face, integrating \(U_{yy}\) first in its normal direction and then in its tangential direction bounds it in absolute value by \(B_g\); the resulting boundary terms are differences of integrals \(2a/(s^2+a^2)\), each at most \(2\pi\). The same holds for vertical faces. Along a face its tangential second derivative is also at most \(B_g\), directly from FW11, where \(\mathscr F_{aa}=2\arctan(b/a)\).

The composite midpoint error in the sum of \(n\) face values is at most \(B_g\gamma^2/(6n)\) horizontally and \(B_g\delta^2/(6n)\) vertically. There are eight layers of each kind, producing the first term of \(C_g/n\). The function \(g_H\) is even and decreases on \((0,\gamma)\), since \(\log(1+4\delta^2/s^2)\) decreases with \(|s|\). Therefore its total variation is at most \(2L\). For a function of bounded variation on an interval, the error of the sum of its midpoint values relative to \(n\) times its mean is at most its total variation: prove this cell by cell by bounding the difference from a midpoint value by the variation within that cell. Consequently the linear normal terms contribute at most \(2L\delta A_{r_*}/n\) and \(2L\gamma A_{s_*}/n\). Taylor's normal remainder contributes at most \(B_g(\delta^2B_{r_*}+\gamma^2B_{s_*})/(2n)\). Every one of the 64 corner points lies within \(15R_0/n\) of its corner, contributing at most \(960LR_0/n\).

The face main term is \(8n\mu_H+8n\mu_V=16n\bar u\). The normal main terms are \(A_{r_*}L_H+A_{s_*}L_V\), and the corners give \(64u_C\). Since \(\Delta=16n+64\), their sum is \(\Delta\bar u+B_{r_*,s_*}^{\rm pivot}\). Multiplying this potential sum by \(d=n^2\), then adding all \(\Delta\) errors in FW15, proves FW20. Its remainder is \(O_{\delta,\gamma}(n\log(n+1))=o(q)\). The pivot dependence is retained through its entire order-\(q\) term.

For the exact complex phase, define
\[
N_r(u)=[\min(r+n-1,k-u)-\max(r,-u)+1]_+,
\quad c_{uv}=N_{r_*}(u)N_{s_*}(v)-(n-|u|)_+(n-|v|)_+.
\]
The first product counts all pairs whose interior point has displacement \((u,v)\) to a point in the full square; the subtracted product counts precisely those whose second point is also interior. Hence \(c_{uv}\) is a nonnegative integer, \(c_{00}=0\), and \(\sum c_{uv}=d\Delta\). Each corresponding root difference is exactly \(2\gamma v-2i\delta u\), so
\[
\operatorname{Res}(O,D)=\prod_{\substack{-k\le u,v\le k\\(u,v)\ne(0,0)}}
(2\gamma v-2i\delta u)^{c_{uv}}.
\tag{FW21}
\]
Reflection of the first coordinate conjugates every difference, giving \(\mathfrak R_{8-r,s}=\overline{\mathfrak R_{r,s}}\). Reflection of the second gives negative conjugates, whose total sign is \((-1)^{d\Delta}=1\), so \(\mathfrak R_{r,8-s}=\overline{\mathfrak R_{r,s}}\) also. If \(r=4\), the odd original grid has no real-axis boundary roots; its conjugate pairing yields positive products \(|D(\omega)|^2\). If \(s=4\), it has no imaginary-axis boundary roots, and its negative-conjugate pairs yield the same positive products because \(d=n^2\) is even. Thus these central-pivot resultants are strictly positive; no positivity is assigned to general pivot phases.

For the declared algebraic fixture \(k=9\), \(r_*=s_*=4\), \(\delta=1/4\), \(\gamma=3\), direct multiplication gives
\[
D(y)=y^4-\frac{143}{8}y^2+\frac{21025}{256},\quad
D(9+i/4)=5166+648i,\quad |D(9+i/4)|^2=27107460.
\tag{FW22}
\]
This checks a literal root polynomial, not a numerical xi-zero or period evaluation.

## 4. Joint metric profile, spectral ordering, heat, and every exterior rank

Retain the actual complete J1–J7 joint metric in root values:
\[
\mathbf L_k^{-1}\mathsf T_k\preceq G_N^J\preceq\mathbf B_k\mathsf T_k,
\qquad \mathsf T_k=\operatorname{diag}(W_\omega),\quad
\kappa_J=\mathbf L_k\mathbf B_k,\quad \log\kappa_J=O_h(k\log^2(q+2)).
\tag{FW23}
\]
The original tuple weights \(W_\omega\) remain unchanged. Since \(\mathsf T_k\) commutes with the root-diagonal word, every Rayleigh quotient for \(T^{\dagger_{G_N^J}}T\) lies between \(\kappa_J^{-1}\) and \(\kappa_J\) times the corresponding \(\mathsf T_k\) quotient. The min–max principle, retaining its entire \(d\)-dimensional kernel, therefore pairs the increasingly ordered positive eigenvalues \(\lambda_j^J\) with the increasingly ordered numbers \(h_j=\log|D(\omega_j)|^2\) so that
\[
|\log\lambda_j^J-h_j|\le\log\kappa_J,\qquad 1\le j\le\Delta.
\tag{FW24}
\]
This is an ordered comparison; a particular root is not asserted to be an eigenvector of the native joint adjoint. For the boundary-quotient endomorphism the same proof holds at every activation, using IC14–15's \(\kappa_\partial\), since its entire metric lies between \(b_-I\) and \(b_+I\).

Define
\[
\nu=\tfrac12(u_H)_*\frac{dx}{\gamma}\bigg|_{[0,\gamma]}
+\tfrac12(u_V)_*\frac{dy}{\delta}\bigg|_{[0,\delta]}.
\tag{FW25}
\]
Each horizontal layer is the same \(n\)-point midpoint rule along a full horizontal face, displaced by at most \(15R_0/n\); the corresponding assertion holds vertically. Reflection of each full face replaces it by the half-face measures in FW25. The 64 corners have total mass \(64/\Delta\). Thus FW15 and FW24 give
\[
\frac1\Delta\sum_{j=1}^\Delta\delta_{(\log\lambda_j^J-2d\log n)/d}\ \Longrightarrow\ \nu,
\tag{FW26}
\]
uniformly over the four source cutoffs. The same law holds for the boundary-quotient word at every activation, with uniform comparison constants from IC15.

For complete endpoint and quantile information, FW11 yields
\[
u_H''(x)=\frac{2\arctan(2\delta/(\gamma+x))+2\arctan(2\delta/(\gamma-x))}{4\delta\gamma}
\ge c_H^*=\frac{\arctan(\delta/\gamma)}{\delta\gamma}>0,
\]
\[
u_V''(y)\ge c_V^*=\frac{\arctan(\gamma/\delta)}{\delta\gamma}>0.
\tag{FW27}
\]
Both first derivatives vanish at their midpoint. Thus both profiles increase strictly away from it and reach \(u_C\) only at the corner. In fact \(u_H(0)<u_V(0)\) whenever \(\gamma>\delta\), a stronger domain than needed here. To see this, write \(r=\gamma/\delta>1\). The difference \(\mathscr F(2r,1)-\mathscr F(r,2)\) equals
\[
2\int_0^r\int_0^1\log\frac{4x^2+y^2}{x^2+4y^2}\,dy\,dx.
\]
The integral over \([0,1]^2\) vanishes by exchanging the two variables. The integral over \((1,r]\times[0,1]\) is strictly positive. Multiplication by the positive scaling factor proves the desired order, and FW27 gives \(u_V(0)<u_C\).

Let \(X(t)\) be zero for \(t\le u_H(0)\), equal to \(\gamma\) for \(t\ge u_C\), and the unique inverse value \(u_H(X(t))=t\) between these endpoints. Define \(Y(t)\) for \(u_V\) in the same way. The distribution function and its clipped integral are exactly
\[
F_\nu(t)=\tfrac12[X(t)/\gamma+Y(t)/\delta],
\tag{FW28}
\]
\[
A_H(x)=\frac{\mathscr J(\gamma+x,2\delta)-\mathscr J(\gamma-x,2\delta)}{4\delta\gamma},\quad
A_V(y)=\frac{\mathscr J(\delta+y,2\gamma)-\mathscr J(\delta-y,2\gamma)}{4\delta\gamma},
\]
\[
\Phi(t)=\int(u-t)_+d\nu(u)
=\frac{A_H(\gamma)-A_H(X(t))-t(\gamma-X(t))}{2\gamma}
+\frac{A_V(\delta)-A_V(Y(t))-t(\delta-Y(t))}{2\delta}.
\tag{FW29}
\]
Indeed \(A_H'=u_H\) and \(A_V'=u_V\) by FW16; the positive part integrates only above the indicated inverse point. These formulas preserve all endpoints, including the interval where only the horizontal face contributes. The measure has no atoms, since each profile is strictly increasing on its positive half-interval.

The following explicit transport error will also control all spectral sums:
\[
\epsilon_k^{\rm tr}=\frac{\log\kappa_J+E_n}{d}
+\frac{15LR_0}{n}+\frac{L(\gamma+\delta)}{2n}
+\frac{64}{\Delta}[u_C-u_H(0)].
\tag{FW30}
\]
To prove it, first use the ordered coupling FW24 and the pointwise coupling FW15. Move each displaced boundary point to its face midpoint, costing at most \(15LR_0/n\). Couple the midpoint to the uniform measure in its original interval; its mean distance is \(\gamma/(2n)\) horizontally or \(\delta/(2n)\) vertically. These contribute no more than the displayed midpoint term. Finally couple each corner's value \(u_C\) to a copy of \(\nu\), costing at most its support diameter. This constructs a probability coupling whose mean absolute difference is at most FW30, rather than merely claiming weak convergence.

At \(\widehat\tau_k(t)=n^{-2d}e^{-td}\), the elementary inequalities
\(0\le d^{-1}\log(1+e^{dv})-v_+\le(\log2)/d\) yield, for every real \(t\),
\[
\left|\frac1{\Delta d}\log\det(I+\widehat\tau_k(t)T^{\dagger_{G_N^J}}T)-\Phi(t)\right|
\le\epsilon_k^{\rm tr}+\frac{\log2}{d}.
\tag{FW31}
\]
The determinant contains every zero mode, each contributing the factor one.

For an explicit uniform heat estimate put
\[
a_k=\frac{\log\kappa_J+E_n}{d}+\frac{15LR_0}{n}+\frac{L\max(\gamma,\delta)}{n},
\quad h_k=\frac{2\log(n+1)}d,
\]
\[
\omega_\nu(h)=\frac12\left[\frac1\gamma\sqrt{2h/c_H^*}+\frac1\delta\sqrt{2h/c_V^*}\right].
\]
FW27 implies \(|X(t+h)-X(t)|\le\sqrt{2h/c_H^*}\): integrate \(u_H''\ge c_H^*\), use \(u_H'(0)=0\), and then \(x_2^2-x_1^2\ge(x_2-x_1)^2\). The same proves the vertical bound. The midpoint coupling above, omitting only the corner mass, has displacement at most \(a_k\). Comparing \(e^{-\exp(d(u-t))}\) to the step function outside \([t-h_k,t+h_k]\) proves
\[
\sup_t\left|\frac{\operatorname{Tr}e^{-\widehat\tau_k(t)T^{\dagger_{G_N^J}}T}-d}{\Delta}-F_\nu(t)\right|
\le\omega_\nu(a_k+h_k)+\frac{64}{\Delta}+e^{-dh_k}+e^{-e^{dh_k}}
=O_{h,\varpi}\!\left(\frac{\log(q+2)}{\sqrt k}\right).
\tag{FW32}
\]
This includes both endpoint values. Every one of the \(d\) null directions contributes the subtracted constant exactly.

For \(1\le r_e\le\Delta\), set \(\theta=r_e/\Delta\) and choose \(t_\theta\in[u_H(0),u_C]\) with \(F_\nu(t_\theta)=1-\theta\). At the endpoints use the displayed interval endpoints. For an increasingly ordered list, the sum of its largest \(r_e\) entries divided by \(\Delta\) is exactly \(\inf_t[\theta t+\Delta^{-1}\sum_j(u_j-t)_+]\); inspection of its one-sided derivatives proves the identity even at repeated values. FW30 bounds the difference of the two objective functions uniformly in \(t\), and hence bounds the difference of their infima. Therefore
\[
\left|\frac{\log\|\wedge^{r_e}T\|_{G_N^J}^2-2r_ed\log n}{\Delta d}
-[\theta t_\theta+\Phi(t_\theta)]\right|\le\epsilon_k^{\rm tr}.
\tag{FW33}
\]
This bound is uniform in every rank \(1\le r_e\le\Delta\). For \(r_e>\Delta\), the exterior map is exactly zero. It includes the complete growing-rank determinant at \(r_e=\Delta\).

## 5. Entire primary-angle spectrum and its exact determinant

The attained metric satisfies \(0<B\preceq W_G\), because the boundary-supported vector is one allowed lift of its boundary values. Define
\[
\mathcal A=W_G^{-1/2}BW_G^{-1/2},\qquad 0<\mathcal A\preceq I_\Delta.
\tag{FW34}
\]
The restriction \(P_{V^{\perp_G}}|_W\) has squared norm \(B\) and domain norm \(W_G\); hence its squared singular values are exactly the eigenvalues of \(\mathcal A\). This gives the precise metric projection realizing the primary-angle matrix.

By FW5,
\[
-\log\det\mathcal A=\log\det{}^+(T^{\dagger_G}T)-\log|\operatorname{Res}(O,D)|^2.
\tag{FW35}
\]
There is also a complete ordered directional estimate. FW6–8 imply
\(e^{c-\alpha}I\preceq D_\partial^*W_GD_\partial\preceq e^{c+\alpha}I\), where \(\alpha=\varepsilon_k+2\log C_V+2\log C_{V^{-1}}\). Congruence by \(D_\partial^{-1}\) and comparison with \(b_-I\preceq B\preceq b_+I\) bound the generalized eigenvalues of \((B,W_G)\) between \(e^{-c\pm\mathcal E_k}\) times the ordered \(|D(\omega)|^2\). Thus if \(\lambda_j(\mathcal A)\) and \(h_j\) are both increasingly ordered as in FW24,
\[
\left|-\log\lambda_j(\mathcal A)-(c_{L/H}-h_j)\right|\le\mathcal E_k.
\tag{FW36}
\]
The negative logarithms in this display are decreasing with \(j\); reversing one ordering without the other would be incorrect. FW15, FW25, and FW36 supply the received complete nonconstant angular distribution.

Combining the finite determinant bounds gives
\[
\left|-\log\det\mathcal A-
\{\Delta[c_{L/H}-2d\log n-d\bar u]-dB_{r_*,s_*}^{\rm pivot}\}\right|
\le\Delta\mathcal E_k+\Delta E_n+nC_g.
\tag{FW37}
\]
The \(dB^{\rm pivot}\) term is exactly present, but the native minimum error \(\Delta\mathcal E_k=O(k^2\log q)\) is larger than order \(q\); FW37 does not assert an independently resolved order-\(q\) angular expansion. Since the resultant is identical at all four cutoffs, it cancels exactly from the return, giving
\[
\left|\mathcal R[-\log\det\mathcal A]-\Delta C_\partial q\right|\le4\Delta\mathcal E_k.
\tag{FW38}
\]

## 6. Original observed heat and its strict return sign

Give \(B_{\rm obs}=E_k/K\) its actual attained observation metric, with minimum section \(L_N\). Under the isometry \(L_N:B_{\rm obs}\to K^{\perp_G}\), the operator \(\Lambda XL_N\) is the orthogonal compression of \(X\) to \(K^{\perp_G}\). Let \(P_V\) be the metric-orthogonal projection onto \(V\), and put
\[
Y_0=\Lambda P_VL_N,\quad
Y_N(\tau)=\Lambda e^{-\tau T^{\dagger_G}T}L_N,\quad
H_K=I_K^*GI_K,\quad \widehat H_K=J_\partial^*BJ_\partial,
\]
\[
\Gamma=H_K^{-1/2}\widehat H_KH_K^{-1/2}.
\tag{FW39}
\]
For every \(x\in K\), the squared norm of its projection onto \(V^{\perp_G}\) is exactly its attained boundary norm. Thus \(\Gamma\) is the matrix of \(P_KP_{V^{\perp_G}}|_K\) in an orthonormal kernel frame. FW3 gives \(0<\Gamma\preceq I_m\). Trace cyclicity gives the exact identity
\[
\operatorname{Tr}_{B_{\rm obs}}Y_0
=\operatorname{Tr}_E(P_{K^\perp}P_V)
=d-\operatorname{Tr}_E(P_KP_V)
=d-m+\operatorname{Tr}\Gamma.
\tag{FW40}
\]
This calculation uses the orthogonal projection, with every observation cross term. It does not substitute the coordinate projection onto the interior block.

Since the positive spectral subspace of \(T^{\dagger_G}T\) is exactly \(V^{\perp_G}\), FW9 and functional calculus give
\[
e^{-\tau e^{c_N+\mathcal E_k}}(I-Y_0)
\preceq Y_N(\tau)-Y_0
\preceq e^{-\tau e^{c_N-\mathcal E_k}}(I-Y_0).
\tag{FW41}
\]
Write \(\eta_L=2a_0-2\), \(\eta_H=\eta_L-C_\partial/2\), and \(\tau_k(b)=q^{-2q}e^{-bq}\). For fixed \(\eta_H<b<\eta_L\), the low endpoint heat tends to \(Y_0\), whereas the high endpoint heat tends to \(I\). The total trace errors tend to zero: they are bounded at low endpoints by \(q\exp[-\exp((\eta_L-b)q-\mathcal E_k)]\), and at high endpoints by \(q\exp((\eta_H-b)q+\mathcal E_k)\), using \(1-e^{-x}\le x\). Therefore
\[
\mathcal R\operatorname{Tr}_{B_{\rm obs}}Y_N(\tau_k(b))
=-2\Delta+\operatorname{Tr}\Gamma_{q-1}+\operatorname{Tr}\Gamma_q+o(1).
\tag{FW42}
\]
Since \(0<\Gamma\preceq I_m\), this gives
\[
-32k+96+o(1)\le\mathcal R\operatorname{Tr}_{B_{\rm obs}}Y_N(\tau_k(b))
\le-16k+64+o(1).
\tag{FW43}
\]
The sign is eventually strictly negative in the original observation. No individual native kernel-angle eigenvalue has been assigned a limiting average.

The full holomorphic heat retains its phases exactly:
\[
\operatorname{Tr}e^{-\tau T^2}=d+\sum_{\omega\in\partial}e^{-\tau D(\omega)^2}.
\tag{FW44}
\]
All original roots have modulus at most \(R\), so \(\max_\partial|D(\omega)|^2\le(2R)^{2d}\). At \(\tau_k(b)\) its product with time is \(\exp[-2q\log(q/n)+O_h(q)]\to0\), even after multiplication by \(\Delta\). The inequality \(|e^{-z}-1|\le|z|e^{|z|}\) proves that FW44 is \(q+o(1)\). It is in fact source-independent and cancels exactly from the four-return. The canonical positive heat tends to \(d\) at both low endpoints and \(q\) at both high endpoints. Hence
\[
\mathcal R[\Re\operatorname{Tr}e^{-\tau_k(b)T^2}-\operatorname{Tr}e^{-\tau_k(b)T^{\dagger}T}]
=2\Delta+o(1).
\tag{FW45}
\]
FW24 instead bounds the joint positive modes by \(\kappa_J(2R)^{2d}\), so its positive heat is \(q+o(1)\) at this same time and its heat-gap return tends to zero. These positive-energy heat conclusions do not assign a sign to the separate complex projected current.

## 7. Exact kernel determinant from relative observed heat

Let \(B_V=\Lambda V\). By \(K\cap V=0\), its dimension is \(d\). Let \(J_V\) be any isometry from this inherited observed subspace into \(B_{\rm obs}\). Choose orthonormal frames \(U_K\) and \(U_V\) for \(K,V\), and put \(C=U_K^*GU_V\). The matrix of \(P_KP_{V^\perp}|_K\) is \(I_m-CC^*\), hence is unitarily equivalent to \(\Gamma\). The map \(P_{K^\perp}U_V\) has Gram \(I_d-C^*C\), and its image is the isometric image of \(B_V\). Its product with its adjoint is exactly the compression defining \(Y_0\). Therefore the positive eigenvalues of \(Y_0\) are those of \(I_d-C^*C\), and
\[
\det(J_V^{\dagger}Y_0J_V)=\det(I_d-C^*C)=\det(I_m-CC^*)=\det\Gamma.
\tag{FW46}
\]
The middle equality follows by block Gaussian elimination of \(\left(\begin{smallmatrix}I_m&C\\C^*&I_d\end{smallmatrix}\right)\), so it holds at every finite dimension. For \(d\ge m\), the positive spectrum consists of \(d-m\) units and the \(m\) eigenvalues of \(\Gamma\). For \(d<m\), \(\Gamma\) contains at least \(m-d\) unit eigenvalues, which are removed to obtain the \(d\) positive eigenvalues of \(Y_0\). In both cases \(Y_0\) has exactly \(\Delta-m\) zero eigenvalues in the observed space. No small finite dimension is excluded from the determinant identity.

For a lower bound on every positive eigenvalue, full-root interpolation gives
\[
G_N^{\rm val}\preceq u_kB_{\rm full}I_q,\qquad
B_{\rm full}=qM_\sigma\left(\frac{2q+R}{2\delta}\right)^{2(q-1)}.
\]
The proof is the same full Lagrange construction as IC13 with all \(q\) roots: each denominator is at least \((2\delta)^{q-1}\), and each numerator factor obeys the original Gamma multiplication recurrence. Every resulting lift has degree \(q-1\le N\). FW3 and the boundary lower bound then give
\[
H_K\preceq u_kB_{\rm full}(1+\|F\|^2)J_\partial^*J_\partial,\qquad
\widehat H_K\succeq(\ell_k/A)J_\partial^*J_\partial.
\]
Thus
\[
\Gamma\succeq\vartheta_kI_m,\qquad
\vartheta_k=\min\left\{1,\frac{\ell_k}{u_kAB_{\rm full}(1+\|F\|^2)}\right\}>0.
\tag{FW47}
\]
The exact strip elimination bound IC6, \(\|F\|\le\sqrt q(A_1/|a_*|)^{10k}\), retains the actual pivot and proves \(-\log\vartheta_k=O_{h,\varpi}(q\log(q+2))\). FW46 shows that the compressed \(Y_0\) also has every eigenvalue at least \(\vartheta_k\).

Take one fixed \(b<\eta_H\) at all four cutoffs. The positive correction \(Y_N(\tau_k(b))-Y_0\) has rank at most \(\Delta\) and operator norm at most \(e^{-\tau_k(b)e^{c_N-\mathcal E_k}}\), by FW41. Compressing to the \(d\)-dimensional \(B_V\), conjugating by its positive \(Y_0\), and multiplying its eigenvalues proves the relative determinant bound
\[
0\le\log\det[J_V^\dagger Y_N(\tau_k(b))J_V]-\log\det\Gamma
\le r_0\log\left(1+\frac{e^{-\tau_k(b)e^{c_N-\mathcal E_k}}}{\vartheta_k}\right),
\quad r_0=\min(d,\Delta).
\tag{FW48}
\]
Every quantity is the actual native one. The right side is at most \(\exp[-\exp(cq)+O_{h,\varpi}(q\log q)]\) for some fixed \(c>0\), because \(\eta_H-b>0\) and \(\mathcal E_k=o(q)\). This accuracy is relative to the smallest retained eigenvalue; absolute convergence alone would not establish a logarithmic determinant receiver.

Finally, the definition in FW39 gives exactly
\(\log\det H_K=\log\det\widehat H_K-\log\det\Gamma\). IC16 bounds the complete fixed-frame boundary return by \(0\le\mathcal R\log\det\widehat H_K\le2m\log\kappa_\partial\). If \(\epsilon_N^{\rm heat}\) is the right side of FW48, then
\[
\left|\mathcal R\log\det H_K+
\mathcal R\log\det[J_V^\dagger\Lambda e^{-\tau_k(b)T^{\dagger}T}L_NJ_V]\right|
\le2m\log\kappa_\partial+\sum_N\epsilon_N^{\rm heat}=o(kq).
\tag{FW49}
\]
This recovers the original kernel allocation with a completely specified relative heat error. In the retained original allocation formula
\[
\mathcal R\log\det H_K=(16k-48-v)qC_\partial+\mathcal R\log\det S_N+o(kq),
\]
it supplies an exact receiver for the same remaining native projection determinant. It does not evaluate that determinant's leading coefficient. The complete \(\Delta\)-direction word spectrum, the \(m\)-direction native kernel correlations, and the complex-current phases all remain connected by the displayed exact maps; neither of the latter two is replaced by an inferred sign or average.

## Sources, verification, and mathematical scope

The complete literal-root source proof and its finite constants are IC19–34 in the sibling `collision_derivation/COLLISION_PROOFS.md`; the accompanying ledger records its exact DCR, OOQ, OSP, native-source, and original-author TeX editions. The public receiving proofs are [DCR9–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7230c00b9f07dd222b2aea95427d67918f3a8cac/workbenches/splitzero-tandem/continuations/20260921-local-covariance-activation/009/CONDUCTOR_DIVISOR_COVARIANCE_RETURN.tex#L139), [OOQ1–40](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/09_INPUT_CUMULATIVE_PROOFS.tex#L23179), [OCF1–26](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/5992ad50c0f2a06921f1fcaded7b4e38097c0739/workbenches/splitzero-tandem/continuations/20260920-original-kernel-mixed-determinants/providers/ORIGINAL_CONDUCTOR_STRIP_FRAME.tex), and [MF1–3](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/cb9705da84d6f8689611914ed9659298e620ba0a/workbenches/splitzero-tandem/continuations/20260921-moving-rational-family/ACTIVATED_RATIONAL_PROOFS.md).

The Gamma polynomial formulas retain T. H. Koornwinder, R. Wong, R. Koekoek and R. F. Swarttouw, with W. P. Reinhardt, [DLMF18.23.E7 original TeX](https://dlmf.nist.gov/18.23.E7.tex) and [DLMF18.22.E8 original TeX](https://dlmf.nist.gov/18.22.E8.tex), and R. A. Askey and R. Roy, [DLMF5.8.E3 original TeX](https://dlmf.nist.gov/5.8.E3.tex). Their use here is inherited through the explicitly proved IC source comparison; the source-use ledger distinguishes this from a new independent reading of every earlier source. The originating ES–Fable announcement remains credited to Levent Alpöge, crediting Akhil Mathew and Claude Fable 5; Tao's exposition is a separately credited source, with no new result here attributed to that exposition.

The new independent calculations are FW1–49. The finite checker and machine-readable receipt test exact root products, displacement multiplicities, reflected phases, literal Gram and projection identities, rectangle derivatives, finite error bounds, and sorted spectral comparisons. Auxiliary positive matrix fixtures test these finite identities without claiming to evaluate native xi moments, conductor periods, or the separate complex current.

The executed `WORD_CHECKS.json` receipt records **633 exact checks and 187 numerical checks**, all passed. The exact source versions, actual reading coverage, proof receivers, inherited source status, and runtime are recorded in `WORD_SOURCE_USE_LEDGER.md` and `WORD_SOURCE_IDENTITIES.json`.


The preceding complete proofs are published at a fixed edition: [FI1–17; FR1–4](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/FINITE_INVARIANT_PROOFS.md), [CI1–26; CL1–18](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/CUTOFF_INNOVATION_PROOFS.md), [IC1–42](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/75256b0237884bdef0074c2ac6310de1ea32ec26/workbenches/splitzero-tandem/continuations/20260921-invariant-collision/COLLISION_PROOFS.md). All original source versions and human citations are retained in the accompanying source bank.
