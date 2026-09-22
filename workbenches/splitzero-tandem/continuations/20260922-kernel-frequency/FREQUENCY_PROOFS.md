# Sharp finite frequency bounds in the original metric

This independent derivation reads and verifies FD1–9 of the supplied frequency bridge. Every finite assertion there is valid with the full original kernel, including its zero-energy intersection. The improvements proved here are sharp phase bounds using the entire angle spectrum, a sharp first-derivative bound using that spectrum, and a sharper trace-only bound for every ordinary derivative. No arithmetic asymptotic or period-dependent value is assumed.

## 1. Spaces, full metrics and analytic determinants

Let \(E=\mathbb C^q\) carry its actual positive metric \(G\), let \(\Lambda:E\to\mathbb C^n\) be the original onto observation, and retain the full fixed kernel frame \(I_K:\mathbb C^m\to E\), \(K=\ker\Lambda\), \(m=q-n\). For the original word \(T:E\to E\), set
\[
 H=G^{-1}T^*GT,\quad V=\ker T,\quad
 Q=(\Lambda G^{-1}\Lambda^*)^{-1},\quad L=G^{-1}\Lambda^*Q,\quad
 H_K=I_K^*GI_K,\quad
 J_B=LQ^{-1/2},\quad J_K=I_KH_K^{-1/2}.
 \tag{SF1}
\]
A coordinate star is conjugate transpose; physical adjoints use \(G\). An alternative fixed kernel isometry \(I_KV_K\), where \(V_K^*H_KV_K=I\), equals the displayed \(J_K\) followed by the exact unitary \(H_K^{1/2}V_K\). All compressed matrices then change by that same unitary conjugacy, preserving the spectra, determinants, phases and generalized inequalities below. The original frame determinant remains in \(H_K\).
Direct multiplication gives \(J_B^*GJ_B=I_n\),
\(J_K^*GJ_K=I_m\), \(J_B^*GJ_K=0\). The map
\(\mathcal U=[J_B,J_K]\) is therefore an isometry with inverse
\(\mathcal U^*G\). It transports the original metric exactly; it does not assign a different metric to any original coefficient frame.

In this specified frame write
\[
 \mathcal U^*GH\mathcal U=
 \begin{pmatrix}B&C^*\\ C&A\end{pmatrix}\succeq0,\qquad
 P=P_{V^{\perp_G}}^G,\quad \Gamma=J_K^*GPJ_K,\quad \tau=\operatorname{Tr}\Gamma.
 \tag{SF2}
\]
Here \(A\succeq0\); no inverse of \(A\) is required. The full angle spectrum is
\(1\ge\gamma_1\ge\cdots\ge\gamma_m\ge0\). Its zero multiplicity is
\(t=\dim(K\cap V)\), since its quadratic form is
\(\|PJ_Kx\|_G^2\). Its unit multiplicity is
\(a=\dim(K\cap V^{\perp_G})\). Set \(p=m-t\),
\(\nu=\operatorname{rank}T\), and \(d=q-\nu\).
All determinants below retain \(m,n,q\), including their zero-energy factors.

On the slit plane \(\Omega=\mathbb C\setminus(-\infty,0]\), define
\[
 Y(z)=J_B^*Gz(zI+H)^{-1}J_B,\quad
 R_K(z)=J_K^*Gz(zI+H)^{-1}J_K,\quad
 \Sigma(z)=C^*(zI+A)^{-1}C .
 \tag{SF3}
\]
The same measured response in original value coordinates is
\(\mathscr Y(z)=\Lambda z(zI+H)^{-1}L\); thus
\(Y=Q^{1/2}\mathscr YQ^{-1/2}\).
Both \((zI+A)\) and the full \((zI+H)\) are invertible on \(\Omega\). The complementary Schur determinants give
\[
 \det Y(z)=\frac{\det(I_m+A/z)}{\det(I_q+H/z)},\qquad
 \det R_K(z)=\frac{\det(I_n+B/z)}{\det(I_q+H/z)}.
 \tag{SF4}
\]
For example, the top block of \((zI+\mathcal U^*GH\mathcal U)^{-1}\) is
\([zI+B-C^*(zI+A)^{-1}C]^{-1}\); its determinant is
\(\det(zI+A)/\det(zI+H)\), and multiplication by \(zI_n\) gives the first equality. The second follows by reversing the two blocks. These scalar determinants have neither a zero nor a pole on \(\Omega\).

Take the logarithms continued from positive \(z\), tending to zero as real \(z\to+\infty\):
\[
 h(z)=\log\det(I_q+H/z)-\log\det(I_n+B/z),\quad
 L_A(z)=\log\det(I_m+A/z),\quad D(z)=L_A(z)-h(z).
 \tag{SF5}
\]
For real \(z>0\), the complete observed Schur form is
\(zI+B-\Sigma(z)>0\), and
\[
 D(z)=-\log\det\!\left[
 I-(zI+B)^{-1/2}\Sigma(z)(zI+B)^{-1/2}\right].
\]
This is the original dynamic determinant; it has not replaced \(\Sigma(z)\) by its zero-frequency value. The finite elimination is the Feshbach–Schur construction of Geneviève Dusson, Israel Michael Sigal and Benjamin Stamm, [arXiv:2105.02058v1, Theorem1.2](https://arxiv.org/abs/2105.02058v1), whose original TeX theorem and maps were read previously at lines398–489. All finite identities needed here are proved above and below.

Because \(0\prec z(zI+H)^{-1}\preceq_G I\), one has \(0\prec R_K(z)\preceq I\). Its kernel-block Schur expression also gives
\(R_K(z)\succeq z(zI+A)^{-1}\). Monotonicity of the determinant on positive matrices proves
\[
 0\le h(z)\le L_A(z),\qquad 0\le D(z)\le L_A(z).
 \tag{SF6}
\]
This proves FD1–2, including the semidefinite case.

## 2. Stieltjes density, ordinary derivatives and the dynamic determinant

List all positive eigenvalues of \(H\) and \(B\), with multiplicity, as
\(\lambda_j\) and \(\beta_j\). Their decreasing lists satisfy
\(\beta_j\le\lambda_j\), after zero padding, by restriction min–max. Therefore the nonnegative integer-valued density
\[
 \xi(s)=\#\{j:\lambda_j>s\}-\#\{j:\beta_j>s\},\qquad 0\le s\le u,
 \tag{SF7}
\]
is defined whenever \(u\ge\|H\|_G\). Interlacing also gives
\(0\le\xi(s)\le m\): intersecting the spectral subspace of \(H\) above \(s\) with the observed subspace loses at most its codimension \(m\); on that intersection the quadratic form remains strictly above \(s\), so min–max gives at least \(\#\{\lambda_j>s\}-m\) observed eigenvalues above \(s\). Direct integration of each factor,
\(\log(1+\lambda/z)=\int_0^\lambda(z+s)^{-1}ds\), proves
\[
 h(z)=\int_0^u\frac{\xi(s)}{z+s}\,ds,\qquad z\in\Omega.
 \tag{SF8}
\]
First prove this for positive \(z\); analytic continuation on the connected slit plane then proves it everywhere. Repeated energies give their actual jump multiplicities. Zero energies give zero intervals, not discarded dimension factors. This establishes exactly the Stieltjes assertion FD6.

For positive \(z\), write \(Z=z(zI+H)^{-1}\) and \(\dot Z=z\,dZ/dz=Z-Z^2\). Compression gives
\[
 R_K-R_K^2-\dot R_K
 =J_K^*GZ(I-J_KJ_K^*G)ZJ_K\succeq0.
\]
Here the right-hand side is the full squared norm of the complementary observed component. Since \(\dot R_K\succeq0\), multiply by \(R_K^{-1/2}\), take traces, and use
\(P H=H\) to obtain
\[
 0\le-zh'(z)=\operatorname{Tr}(R_K^{-1}\dot R_K)
 \le\operatorname{Tr}(I-R_K)
 \le \tau\,\frac{u}{z+u}.
 \tag{SF9}
\]
The identity \(D=L_A-h\) then gives FD5, including its derivative sign.

Here is the sharp trace-only improvement for all ordinary derivatives. For each integer \(n\ge1\), define the increasing concave scalar function
\(g_n(x)=1-(1+x/z)^{-n}\) on \([0,u]\). Differentiation of the finite logarithms in SF5 gives
\[
 (-1)^n z^nh^{(n)}(z)
 =(n-1)!\,[\operatorname{Tr}g_n(H)-\operatorname{Tr}g_n(B)].
\]
For an orthonormal eigenbasis \(b_j\) of \(B\), its eigenvalue is the mean of the spectral variable of \(H\) in the actual unit vector \(J_Bb_j\). Scalar concavity gives
\(g_n(\langle HJ_Bb_j,J_Bb_j\rangle_G)
\ge\langle g_n(H)J_Bb_j,J_Bb_j\rangle_G\).
Sum these inequalities and use the full \(J_B,J_K\) resolution. Positivity follows independently from SF8. Thus
\[
 \boxed{\;
 0\le(-1)^n z^nh^{(n)}(z)
 \le(n-1)!\operatorname{Tr}[J_K^*Gg_n(H)J_K]
 \le(n-1)!\tau\left[1-\left(\frac z{z+u}\right)^n\right].
 \;}
 \tag{SF10}
\]
Since \(1-(1-t)^n\le nt\) for \(0\le t\le1\), this proves and strengthens FD7. The final constant is sharp for every \(n,z,u\): take a reducing positive kernel direction with energy \(u\), so \(\Gamma=1\) there and \(h=\log(1+u/z)\). Orthogonal copies and all additional zero or observed directions are retained. No matrix concavity of \(g_n\) was assumed; the scalar Jensen argument is sufficient for the trace.

The complete dynamic determinant is completely monotone, as stated in the source:
\[
 D(z)=\int_0^\infty e^{-zt}\frac{N(t)}t\,dt,\qquad
 N(t)=\operatorname{Tr}e^{-tH}-\operatorname{Tr}e^{-tA}
      -\operatorname{Tr}e^{-tB}\ge0 .
 \tag{SF11}
\]
To verify the identity, apply
\(\log(z+\lambda)-\log z=\int_0^\infty e^{-zt}(1-e^{-t\lambda})dt/t\)
to every eigenvalue; the dimensions cancel because \(q=m+n\).
The scalar function \(e^{-tx}\) is convex. Apply Jensen in every eigenvector of \(A\) and \(B\), in their actual embedded orthogonal subspaces, to prove \(N(t)\ge0\).
At zero, the constant and linear terms cancel, and
\[
 N(t)=t^2\operatorname{Tr}(CC^*)+O(t^3).
\]
At infinity it is bounded by \(q+m+n\). Thus the integral and every differentiated integral converge for \(z>0\), proving
\((-1)^jD^{(j)}(z)\ge0\) for all integers \(j\ge0\).
The case \(C=0\) gives exactly \(D=0\). FD's complete-monotonicity claim therefore needs no transversality or asymptotic.

The word “Stieltjes” applies to \(h\). It does not extend to \(D\) in general. For the exact positive energy
\(H=\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\),
\(A=B=1\),
\[
 D(z)=2\log(1+1/z)-\log(1+2/z)
 =\int_0^1\frac{ds}{z+s}-\int_1^2\frac{ds}{z+s}.
 \tag{SF12}
\]
For \(1<x<2\), its boundary imaginary part at \(z=-x+i0\) is \(+\pi\). Any Stieltjes transform of a positive measure has nonpositive imaginary part in the upper half-plane, so this \(D\) is not one. Its complete monotonicity remains true by SF11. This identifies the exact difference without weakening the valid source assertion.

## 3. Positive-real-frequency bounds using every original angle

For \(0\le\gamma\le1\), \(x\ge0\), put
\[
 b_\gamma(x)=\log\frac{1+x}{1+(1-\gamma)x},\quad
 d_\gamma(x)=\frac{\gamma x}{(1+x)(1+(1-\gamma)x)},\quad
 f_\gamma(x)=\arctan x-\arctan((1-\gamma)x).
 \tag{SF13}
\]
They vanish at \(\gamma=0\). The symbols \(d_\gamma,f_\gamma\) are scalar functions, not dimensions or physical source coordinates.

Let \(0<l\le u\) be any actual positive-energy bounds
\(lP\preceq_GH\preceq_GuP\); a floor is needed only for the lower bounds in this section. The identity
\(R_K(z)=I-J_K^*GH(zI+H)^{-1}J_K\) gives
\[
 \sum_{j=1}^m b_{\gamma_j}(l/z)
 \le h(z)\le\sum_{j=1}^m b_{\gamma_j}(u/z)
 \le\tau\log(1+u/z).
 \tag{SF14}
\]
Indeed \(H(z+H)^{-1}\) lies between \(lP/(z+l)\) and \(uP/(z+u)\). The two endpoint comparison matrices are functions of the fixed \(\Gamma\), so their determinant logarithms are exactly the displayed sums. The final inequality follows because the convex function
\(\gamma\mapsto-\log(1-\gamma u/(z+u))\) lies below its chord on \([0,1]\). Equality in the two spectral bounds occurs for \(H=lP\) or \(H=uP\), respectively.

We need a generalized Rayleigh-quotient argument that keeps noncommuting blocks. For a nonzero coefficient vector \(v\), put
\(\gamma(v)=v^*\Gamma v/(v^*v)\).
If \(\gamma(v)>0\), the spectral measure of \(H_+/z\) in \(PJ_Kv\), divided by \(\|PJ_Kv\|_G^2\), is a probability measure \(\mu_v\) on \([l/z,u/z]\). Then
\[
 \frac{v^*\dot R_Kv}{v^*R_Kv}
 =\frac{\gamma(v)\int t(1+t)^{-2}\,d\mu_v(t)}
 {1-\gamma(v)\int t(1+t)^{-1}\,d\mu_v(t)} .
 \tag{SF15}
\]
This is a weighted mean of \(d_{\gamma(v)}(t)\): use the strictly positive denominator weight
\(1-\gamma(v)t/(1+t)\) in the measure. At \(\gamma(v)=0\), the ratio is zero.
For fixed \(t\), \(d_\gamma(t)\) increases in \(\gamma\).
Differentiation in \(t\) shows its sign change at
\(t=(1-\gamma)^{-1/2}\) for \(0<\gamma<1\); at \(\gamma=1\) it increases.
Define
\[
 d_\gamma^-=\min\{d_\gamma(l/z),d_\gamma(u/z)\},\quad
 d_\gamma^+=d_\gamma\!\left(
 \operatorname{clip}_{[l/z,u/z]}((1-\gamma)^{-1/2})\right),
 \tag{SF16}
\]
where the \(\gamma=1\) maximum is at \(u/z\), and both values at \(\gamma=0\) are zero. Taking the infimum or supremum of increasing functions preserves monotonicity in \(\gamma\).

For the \(j\)-th decreasing generalized eigenvalue of
\((\dot R_K,R_K)\), take in min–max the span of the first \(j\) eigenvectors of \(\Gamma\) for the lower bound and the span of its last \(m-j+1\) eigenvectors for the upper bound. SF15 therefore gives the ordered comparison and its trace consequence:
\[
 d_{\gamma_j}^-\le
 \lambda_j(R_K^{-1/2}\dot R_KR_K^{-1/2})
 \le d_{\gamma_j}^+,\qquad
 \sum_jd_{\gamma_j}^-\le-zh'(z)\le\sum_jd_{\gamma_j}^+ .
 \tag{SF17}
\]
If only \(u\) is known, use \(l=0\) in the scalar interval, giving a zero lower bound and the same maximum formula with \([0,u/z]\).
The proof does not diagonalize \(\Gamma\) and \(H\) together.

For every \(n\ge1\), SF8 also gives
\[
 (-1)^nz^nh^{(n)}(z)\le n![-zh'(z)].
\]
Indeed \(z^{n-1}\le(z+s)^{n-1}\) in the nonnegative density integral. Combining with SF10 and SF17 yields the available sharper upper bound
\[
 (-1)^nz^nh^{(n)}(z)
 \le\min\left\{
 n!\sum_jd_{\gamma_j}^+,\,
 (n-1)!\tau[1-(z/(z+u))^n]\right\}.
 \tag{SF18}
\]
Neither expression assumes an unevaluated arithmetic estimate.

## 4. Sharp imaginary-frequency spectrum bounds

Fix \(\omega>0\) and write \(R_K(i\omega)=X+iY_K\). Functional calculus on the full original \(H\) gives
\[
 X=I-J_K^*G\frac{H^2}{\omega^2+H^2}J_K\succ0,\qquad
 Y_K=J_K^*G\frac{\omega H}{\omega^2+H^2}J_K\succeq0 .
 \tag{SF19}
\]
For example \(X\succeq\omega^2/(\omega^2+u^2)I\); zero energies contribute exactly one. Consequently
\[
 \phi(\omega):=-\Im h(i\omega)
 =\operatorname{Tr}\arctan(X^{-1/2}Y_KX^{-1/2})\ge0 .
 \tag{SF20}
\]
To justify the branch, factor the determinant into
\(\det X\det(I+iX^{-1/2}Y_KX^{-1/2})\).
Each latter eigenvalue lies in the open right half-plane. Along the continuous path from \(\omega=+\infty\) both sides have phase tending to zero, so their unwrapped logarithms agree. This is a sum of matrix eigenphases, not a principal scalar argument of a determinant.

For the same actual \(v\) as in SF15, now use the probability spectral measure of \(H_+/\omega\). One obtains
\[
 \frac{v^*Y_Kv}{v^*Xv}
 =\frac{\gamma(v)\int t(1+t^2)^{-1}\,d\mu_v(t)}
 {1-\gamma(v)\int t^2(1+t^2)^{-1}\,d\mu_v(t)} .
 \tag{SF21}
\]
It is a weighted mean of
\(k_\gamma(t)=\gamma t/[1+(1-\gamma)t^2]\),
using the positive denominator weight
\(1-\gamma t^2/(1+t^2)\).
The function \(k_\gamma(t)\) increases in \(\gamma\); its maximum in \(t\) occurs at \(t=(1-\gamma)^{-1/2}\) for \(0<\gamma<1\). Also
\(\arctan k_\gamma(t)=f_\gamma(t)\) from SF13, since the angle difference belongs to \([0,\pi/2)\).

Define \(x_-=l/\omega\), \(x_+=u/\omega\), and
\[
 F_\gamma^-=\min\{f_\gamma(x_-),f_\gamma(x_+)\},\qquad
 F_\gamma^+=f_\gamma\!\left(
 \operatorname{clip}_{[x_-,x_+]}((1-\gamma)^{-1/2})\right).
 \tag{SF22}
\]
At \(\gamma=1\), the maximum is \(f_1(x_+)=\arctan x_+\); at \(\gamma=0\) both bounds are zero. Apply the same generalized min–max argument as in SF17, then the increasing scalar arctangent. Every ordered eigenphase and their full sum satisfy
\[
 \boxed{\quad
 F_{\gamma_j}^-\le
 \arctan\lambda_j(X^{-1/2}Y_KX^{-1/2})
 \le F_{\gamma_j}^+,\qquad
 \sum_jF_{\gamma_j}^-\le\phi(\omega)\le\sum_jF_{\gamma_j}^+ .
 \quad}
 \tag{SF23}
\]
No commutation of the positive-energy compression with the angle matrix was assumed or inserted.

Using only \(u\), put \(x=u/\omega\) and
\[
 F_\gamma(x)=
 f_\gamma\!\left(\min\{x,(1-\gamma)^{-1/2}\}\right).
\]
The endpoint conventions remain as above. In particular
\[
 F_\gamma(x)=
 \begin{cases}
 \arctan x-\arctan((1-\gamma)x),&
 x\le(1-\gamma)^{-1/2},\\
 \arcsin(\gamma/(2-\gamma)),&
 x\ge(1-\gamma)^{-1/2},\quad 0\le\gamma<1,
 \end{cases}
\]
and \(F_1(x)=\arctan x\). Hence the strengthened FD9 is
\[
 \boxed{\quad
 0\le
 \sum_j\arctan(\alpha_j/\omega)-[-\Im D(i\omega)]
 =\phi(\omega)
 \le\sum_{j=1}^mF_{\gamma_j}(u/\omega)
 \le\tau\arctan(u/\omega).
 \quad}
 \tag{SF24}
\]
The first equality follows directly from SF5, with the full positive eigenvalues \(\alpha_j\) of \(A\) and the same analytic branch.

For the final inequality, at fixed \(t\ge0\) the function
\(f_\gamma(t)=\arctan t-\arctan((1-\gamma)t)\) is convex in \(\gamma\):
its second derivative is
\(2(1-\gamma)t^3/[1+(1-\gamma)^2t^2]^2\ge0\).
Its endpoints are \(0,\arctan t\), so
\(f_\gamma(t)\le\gamma\arctan t\le\gamma\arctan x\) for \(0\le t\le x\).
Taking the supremum proves the claim. It is strictly stronger than the input's bound for \(x>0,\tau>0\), because
\(\arctan x<2x/(1+x)\).
One exact proof differentiates their difference:
\(2/(1+x)^2-1/(1+x^2)=(x-1)^2/[(1+x)^2(1+x^2)]\ge0\);
the difference vanishes at zero and has a positive integral for every \(x>0\).

## 5. Sharpness, trace-only refinements and finite-frequency moments

The bounds SF17 and SF23 are sharp with the entire admissible angle spectrum and all dimensions fixed. Here is the complete realizing map. For each \(\gamma_j\in(0,1)\), take an orthogonal two-dimensional block with one observed coordinate \(b_j\), one kernel coordinate \(k_j\), and
\[
 G_j=I_2,\quad \Lambda_j=(1,0),\quad I_{K,j}=e_2,\quad
 v_j=\sqrt{1-\gamma_j}\,e_1+\sqrt{\gamma_j}\,e_2,\quad
 H_j=\lambda_jv_jv_j^*,\quad T_j=\sqrt{\lambda_j}\,v_jv_j^* .
 \tag{SF25}
\]
Its angle is exactly \(\gamma_j\), and
\[
 R_{K,j}(z)=\frac{z+(1-\gamma_j)\lambda_j}{z+\lambda_j},\quad
 \phi_j(\omega)=f_{\gamma_j}(\lambda_j/\omega),\quad
 -zh_j'(z)=d_{\gamma_j}(\lambda_j/z).
 \tag{SF26}
\]
A unit angle uses a single positive kernel coordinate with \(H=\lambda_j\).
A zero angle uses a single zero-energy kernel coordinate. If \(r\) is the count of angles strictly between zero and one, these blocks use \(m+r\) total dimensions, \(p\) positive energies, and \(t+r\) zero energies. Add \(\nu-p\) positive observed coordinates and \(d-t-r\) zero observed coordinates. Both counts are nonnegative for every actual angle spectrum: the map \(P|_K\) has rank \(p\le\nu\); the nonzero singular values strictly below one of \(P_V|_K\) require \(r\) dimensions in \(V\ominus(K\cap V)\), so \(r\le d-t\). The final total dimension is \(q\), its kernel dimension is \(m\), its word rank is \(\nu\), and its zero intersection is \(t\).

In SF25 choose \(\lambda_j\) independently to be \(l\), \(u\), or the critical point in the scalar interval, as appropriate. Then every lower or upper eigenphase in SF23 is attained simultaneously, and every corresponding derivative bound in SF17 is attained simultaneously. The optimizing energy selection for a specified phase or derivative is an auxiliary exact construction, not a claim about the fixed native word. Any nonunitary physical coordinate map \(S\) transports these examples by
\[
 G\mapsto S^*GS,\quad T\mapsto S^{-1}TS,\quad
 \Lambda\mapsto\Lambda S,\quad I_K\mapsto S^{-1}I_K.
 \tag{SF27}
\]
An additional invertible observation coordinate map \(O\) changes
\(\Lambda\mapsto O\Lambda\), \(Q\mapsto O^{-*}QO^{-1}\), \(L\mapsto LO^{-1}\).
All claimed phases and generalized eigenvalues are invariant under these actual maps. Thus the sharpness is about full original-metric data, not a suppression of their metrics.

The sharp scalar comparison used in the input, at its chosen positive point \(z=\omega\), is
\[
 \frac{\omega}{s^2+\omega^2}
 \le c(x)\frac{\omega}{(s+\omega)^2},\quad 0\le s\le u,\quad
 c(x)=
 \begin{cases}(1+x)^2/(1+x^2),&0\le x\le1,\\2,&x\ge1,\end{cases}
 \qquad x=u/\omega.
 \tag{SF28}
\]
Differentiate \((1+y)^2/(1+y^2)\) to locate its maximum at \(y=1\).
This constant is sharp for this comparison of the two scalar kernels; SF9 then gives
\(\phi\le c(x)\tau x/(1+x)\). It improves the input only for \(x<1\).
The stronger SF24 uses the original compression and angle data, which the scalar comparison does not encode. Thus the input's factor two is valid and sharp for its intermediate kernel inequality, but is not sharp for the final finite frequency theorem.

There are useful bounds even when only the trace and no individual angle is available. For fixed \(x\), the function \(F_\gamma(x)=\sup_{0\le t\le x}f_\gamma(t)\) is convex and vanishes at zero. Given only \(m\) and \(\tau\), write \(\tau=j+\rho\), \(j=\lfloor\tau\rfloor\), \(0\le\rho<1\). Then
\[
 \phi(\omega)\le j\arctan x+F_\rho(x)\le\tau\arctan x.
 \tag{SF29}
\]
To prove the first bound, take two angle entries strictly between zero and one. With their sum fixed, the sum of their values under a convex function is maximized at one endpoint of the allowed interval, making one entry zero or one. Repeating finitely many times leaves \(j\) unit entries and at most one fractional entry \(\rho\). This proves the inequality; SF25 realizes equality whenever these are the retained angles, so it is sharp over the class with only \(m,\tau,u\) specified.

If a known angle margin satisfies \(\gamma_j\le g<1\), convexity on \([0,g]\) gives
\[
 \phi(\omega)\le\frac{\tau}{g}F_g(u/\omega)
 \le\frac{\tau}{g}\arcsin\frac{g}{2-g}\quad(g>0).
 \tag{SF30}
\]
For \(g=0\), all angles and the phase are zero. This is a finite every-direction bound; no arithmetic small-angle rate is inserted. The frequency-uniform full-spectrum version is
\(\phi\le\sum_{\gamma_j<1}\arcsin(\gamma_j/(2-\gamma_j))+a\pi/2\).

The Stieltjes density supplies an additional receiver involving actual finite energy moments. Define, for every integer \(r\ge0\),
\[
 \mu_r=\int_0^u s^r\xi(s)\,ds
 =\frac{\operatorname{Tr}H^{r+1}-\operatorname{Tr}B^{r+1}}{r+1}\ge0 .
 \tag{SF31}
\]
In particular \(\mu_0=\operatorname{Tr}A\), by the full block trace.
Since
\(\phi(\omega)=\int_0^u\omega\xi(s)/(s^2+\omega^2)\,ds\), one has
\[
 \frac{\omega\,\operatorname{Tr}A}{u^2+\omega^2}
 \le\phi(\omega)\le\frac{\operatorname{Tr}A}{\omega}.
 \tag{SF32}
\]
The upper bound may be intersected with SF23 or SF24. It uses an evaluated original compression trace, not an assumed scalar spectrum.

For \(r\ge1\), the finite geometric identity, with no requirement that \(u<\omega\), gives
\[
 \phi(\omega)=\sum_{j=0}^{r-1}
   \frac{(-1)^j\mu_{2j}}{\omega^{2j+1}}
   +(-1)^r\mathcal E_r(\omega),\qquad
 0\le\mathcal E_r(\omega)\le\frac{\mu_{2r}}{\omega^{2r+1}} .
 \tag{SF33}
\]
Indeed the exact remainder in the scalar kernel is
\((-1)^rs^{2r}/[\omega^{2r-1}(\omega^2+s^2)]\).
Integrate it against the nonnegative \(\xi\). This yields alternating directed intervals from actual original matrix moments. It does not claim small error when \(\omega\) is too small; the displayed finite remainder decides that question.

All zero intersections remain explicit. The limit of the density at zero is
\(\xi(0+)=\nu-\operatorname{rank}B=a\).
For proof, \(B\) is the Gram of \(TJ_B\), so
\(\ker B\) corresponds to \(K^{\perp_G}\cap V\).
More directly, the range of \(P_{V^{\perp_G}}|_{K^{\perp_G}}\) has orthogonal complement \(V^{\perp_G}\cap K\) inside \(V^{\perp_G}\). Composing this projection with the invertible \(H_+^{1/2}\) preserves its rank. Rank–nullity therefore gives
\(\operatorname{rank}B=\nu-\dim(K\cap V^{\perp_G})\).
Therefore
\[
 \lim_{\omega\downarrow0}\phi(\omega)=a\pi/2,\qquad
 \lim_{\omega\to\infty}\omega\phi(\omega)=\operatorname{Tr}A .
 \tag{SF34}
\]
The first equality also follows by counting the arctangent factors in SF5; the second follows by dominated convergence in SF32's integral. In particular an angle strictly below one contributes no nonzero low-frequency phase limit, although it can attain a positive maximum at a finite frequency.

## 6. Complex sectors and the original four-sign receiver

For \(z=re^{i\theta}\), \(r>0\), \(|\theta|<\pi\), put
\(c_\theta=\cos(\theta/2)>0\).
The exact identity
\(|z+s|^2-c_\theta^2(r+s)^2
=\sin^2(\theta/2)(r-s)^2\)
proves \(|z+s|\ge c_\theta(r+s)\).
SF8 and its differentiated integral therefore give
\[
 |h(z)|\le c_\theta^{-1}h(r)
 \le c_\theta^{-1}\sum_j b_{\gamma_j}(u/r),
\]
\[
 r^n|h^{(n)}(z)|
 \le c_\theta^{-n-1}
 \min\!\left\{
 n!\sum_j d_{\gamma_j}^+,\,
 (n-1)!\tau[1-(r/(r+u))^n]\right\},\quad n\ge1 .
 \tag{SF35}
\]
Here the \(d_\gamma^+\) interval in SF16 uses \(r\) in place of \(z\).
These prove and strengthen the sector estimates FD8.

At each original cutoff \(N\in\{q-1,q,2q-1,2q\}\), all preceding objects are built from the actual \(G_N,L_N,I_K,T_k\). Let
\(P_N(\omega)=\sum_j\arctan(\alpha_{j,N}/\omega)\),
\(D_N^\phi(\omega)=-\Im D_N(i\omega)\), and let
\(a_N(\omega),b_N(\omega)\) denote the two spectral sums in SF23, or any improved lower and upper bounds obtained by intersecting SF23, SF29 and SF32–33. Then
\[
 a_N\le P_N-D_N^\phi\le b_N .
\]
For the unchanged signs
\(\mathcal R f=f_{q-1}+f_q-f_{2q-1}-f_{2q}\), the exact directed return is
\[
 a_{q-1}+a_q-b_{2q-1}-b_{2q}
 \le \mathcal RP_N-\mathcal RD_N^\phi
 \le b_{q-1}+b_q-a_{2q-1}-a_{2q}.
 \tag{SF36}
\]
Thus the improvement propagates to the original phase bridge without choosing favorable signs for the separate errors. Every scalar in the interval is a specified finite function of the actual retained angle spectrum, positive spectral bounds or finite moment data. If these inputs are not evaluated, the receiver stays symbolic.

The sealed original metric and spectral morphisms used here are [021 MR1–29](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/MATRIX_RECOVERY_PROOFS.md#L7) and [021 SD38–54](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/e40b46fde72c245dd79ef5691f59c21d6cbf0c75/workbenches/splitzero-tandem/continuations/20260922-original-observation-recovery/SCALAR_RECOVERY_PROOFS.md#L385). The full operator, attained section, kernel frame and zero intersection are retained here exactly as there. The present proof does not import FD10 or any later arithmetic application to establish its finite inequalities.

## 7. Verification scope

The companion exact checker tests logarithmic identities through their rational derivatives, the full Stieltjes moments, positive spectral-density multiplicities, scalar critical points, the positive-definite real-frequency and imaginary-frequency pencils, noncommuting complex metrics, sharp constructions, intersections, zero words, and the full physical/observation coordinate maps. Explicit negative controls reject the claims that the valid dynamic determinant is always Stieltjes, that its complex-frequency blocks may be changed by conjugating the frequency, or that pointwise angle/energy compressions commute. The tests use exact rational or algebraic arithmetic and supplement the complete proofs; they do not evaluate native arithmetic periods.
