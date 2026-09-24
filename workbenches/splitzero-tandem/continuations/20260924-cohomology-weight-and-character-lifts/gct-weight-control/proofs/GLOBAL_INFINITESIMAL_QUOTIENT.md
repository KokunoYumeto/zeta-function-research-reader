# Global infinitesimal maps of the actual zeta quotient and its Weil form

24 September 2026. Independent derivation for the all-zero calculation. No bounded range of integers or zeros is used. Every zero below is an actual nontrivial zero of the original Riemann zeta function, with its actual multiplicity. No off-line zero is postulated to exist.

The starting quotient is M9 of [Prime monodromy and stacked history](PRIME_MONODROMY_STACKED_HISTORY.md). The incoming trace radical and global reflection index are NI25–NI29 and NI1–NI24 of [Cauchy reflection index](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/32acd0df89ae22c96d2bc30372e4426a31ce4506/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/CAUCHY_REFLECTION_INDEX_DERIVATION.md). Their trace-radical calculation is an input, not a new result here. The new work constructs its exact receiving map from M9, proves the global source-ideal defect of spectral differentiation, identifies the actual reflected-pair specialization of the quadratic collision family, and classifies positive invariant forms on all actual finite-support jet packets.

Throughout, addition at the source element tau remains retracted. Coefficient expressions U=[tau], f=[1], U-f occur only in the already defined formal coefficient algebra of WU1. They never define subtraction or addition of source tau.

## GIQ1. Original quotient, every actual zero, and all its jets

Let A and S_0^even be the exact spaces in M9. Write

\[
I=\overline{\mathcal E(S_0^{\rm even})}^{\mathcal A},\qquad
Q=\mathcal A/I,\qquad
F_k(s)=\mathcal M k(s)=\int_0^\infty k(u)u^{s-1/2}\frac{du}{u}.
\tag{GIQ1.1}
\]

Let Z be the set of distinct nontrivial zeta zeros, let m_rho be their orders, and put rho^#=1-conjugate(rho). The original functional equation gives m_(rho^#)=m_rho. For every rho define

\[
A_\rho=\mathbb C[t_\rho]/(t_\rho^{m_\rho}),\qquad
j_\rho(k)=\sum_{r=0}^{m_\rho-1}\frac{F_k^{(r)}(\rho)}{r!}t_\rho^r.
\tag{GIQ1.2}
\]

Every coefficient in GIQ1.2 is continuous on A and vanishes on I, by M9. Thus j_rho descends to Q. This is an actual jet observation of the original zeta source quotient, with local parameter s-rho; it is not a separately chosen collision algebra.

For any finite set R of distinct actual zeros, the joint map j_R:Q -> product_(rho in R) A_rho is surjective. Here is a proof that also specifies its domain. In logarithmic coordinate v=log u, the jet functionals on C_c^infinity(R) are integrals against

\[
v^r e^{(\rho-1/2)v}/r!\quad(\rho\in R,\ 0\le r<m_\rho).
\tag{GIQ1.3}
\]

These functions are linearly independent. To prove this, suppose sum_rho p_rho(v)e^((rho-1/2)v)=0 with degree p_rho<m_rho. Fix rho_0 and apply the differential operator product_(rho!=rho_0)(d/dv-(rho-1/2))^(m_rho). It kills all other summands. On the remaining polynomial it acts, after removing the nonvanishing exponential, as a product of operators d/dv+(rho_0-rho). Each has nonzero constant term and is invertible on the finite-dimensional space of polynomials of degree less than m_(rho_0): its matrix in ascending monomials is triangular with that nonzero constant diagonal. Thus p_(rho_0)=0. This holds for every rho_0. A nonzero linear combination of GIQ1.3 cannot integrate to zero against every compact smooth test, since continuity of that function supplies a small test supported where it is nonzero. Hence the joint functionals are independent. A linear map into a finite-dimensional space is onto exactly when no nonzero functional annihilates its image; this proves surjectivity. All these tests belong to A. Passing to Q preserves the joint image because I is killed.

This statement covers every finite selection from the entire actual divisor and all its actual multiplicities. It does not assert surjectivity to an unrestricted infinite product.

## GIQ2. The full global jet receiver and a dense exact value map

Let H=ell^2(Z,m), with inner product conjugate-linear in the first variable, and let Jx at rho equal x at rho^#. The previously proved form is

\[
[x,y]=\langle Jx,y\rangle_H
=\sum_\rho m_\rho\overline{x_{\rho^\#}}y_\rho.
\tag{GIQ2.1}
\]

The full jet algebra A_tr and its trace-radical kernel N are exactly NI27–NI29:

\[
\mathcal A_{\rm tr}
=\{(a_\rho)_\rho\in\prod_\rho A_\rho:
(a_\rho(0))_\rho\in H\},\qquad
\pi(a)_\rho=a_\rho(0),\qquad
\mathcal N=\ker\pi.
\tag{GIQ2.2}
\]

The maps from the actual theta-Mellin quotient are

\[
j:Q\longrightarrow\mathcal A_{\rm tr},\quad [k]\longmapsto(j_\rho(k))_\rho,
\qquad E_0=\pi j:Q\longrightarrow H.
\tag{GIQ2.3}
\]

They are well defined. To check the only summability assertion, integration by parts in v gives, for every integer b>=0,

\[
|F_k(\sigma+i\gamma)|\le C_b(k)(1+|\gamma|)^{-b}
\quad(0\le\sigma\le1),
\tag{GIQ2.4}
\]

where C_b(k) is bounded by finitely many defining seminorms of A. Indeed apply b derivatives to k(e^v)e^((sigma-1/2)v); the product rule gives finitely many logarithmic derivatives of k with factors of absolute value bounded uniformly for sigma in [0,1], and the weighted seminorms make their integrals finite. The bounded gamma range follows directly from the same integrable bound. Combining GIQ2.4 with the unconditional count sum_(|rho|<=R)m_rho=O(R log(R+2)) proves square summability and continuity of E_0 on A. Consequently

\[
B_Q(q,r):=[E_0q,E_0r]
\tag{GIQ2.5}
\]

is a well-defined continuous Hermitian form on Q.

The image E_0(Q) is dense in H. This additional assertion is important: the comparison does not merely reach a possibly smaller collection of signed directions. Fix z with Re z>1. In v-coordinate set

\[
K_{z,R}(v)=-e^{-(z-1/2)v}\mathbf1_{(0,R)}(v).
\]

It is used only to construct smooth approximations; it is not asserted to belong to A. Its Mellin values are

\[
\int K_{z,R}(v)e^{(\rho-1/2)v}dv
=\frac{1-e^{(\rho-z)R}}{\rho-z}.
\tag{GIQ2.6}
\]

Choose a nonnegative smooth mollifier phi of compact support in [-1,1] and integral 1, and put phi_delta(v)=delta^(-1)phi(v/delta). The convolution K_(z,R)*phi_delta is compact smooth, so its multiplicative-coordinate version belongs to A. Its value vector is GIQ2.6 multiplied at each rho by

\[
\Phi_\delta(\rho)=\int\phi_\delta(v)e^{(\rho-1/2)v}dv,
\quad |\Phi_\delta(\rho)|\le e^{\delta/2},\quad
\Phi_\delta(\rho)\longrightarrow1.
\tag{GIQ2.7}
\]

The last convergence is pointwise in rho. The value vector v_z(rho)=1/(rho-z) belongs to H by NI3 and NI9. Since |1-e^((rho-z)R)|<=2, dominated convergence in the weighted square sum shows that the smoothed vectors approach GIQ2.6 as delta tends to zero. Then

\[
\left\|\left(\frac{e^{(\rho-z)R}}{\rho-z}\right)_\rho\right\|_H
\le e^{-(\Re z-1)R}\|v_z\|_H\longrightarrow0.
\tag{GIQ2.8}
\]

Thus every original Cauchy vector v_z lies in the closure of E_0(Q). NI13 proves that their span is dense in H; its normally convergent Cauchy transform and residue proof apply to the entire actual zero set. This proves the claimed density without a zero cutoff.

It follows that

\[
\operatorname{rad}B_Q=\ker E_0=j^{-1}(\mathcal N).
\tag{GIQ2.9}
\]

One containment follows from GIQ2.5. For the other, if B_Q(q,r)=0 for every r, density makes JE_0q orthogonal to all of H, hence E_0q=0. The map Q/ker(E_0) -> H is an injective isometry for the positive auxiliary norm ||E_0q||_H and has dense image. Its completion is H, while its Weil form is the exact generally indefinite form J of GIQ2.1. This is the constructed radical quotient and completion; no positive Weil norm has been assumed.

In particular the negative index of B_Q is exactly the number of distinct two-point orbits of rho -> rho^#, with infinity allowed, by NI21's proved density argument. Thus the new source quotient sees every old negative direction, not merely a selected finite packet.

## GIQ3. The actual dilation generator preserves the source ideal and the full form

Set D=u d/du on A and L=1/2-D. Direct differentiation of the defining theta sum gives

\[
L\mathcal E(f)=\mathcal E(-x f'(x)).
\tag{GIQ3.1}
\]

The function -x f' is even Schwartz, vanishes at 0, and has integral equal to integral f=0 by integration by parts; the boundary term x f(x) is zero at both infinities. Therefore L preserves E(S_0^even). It is continuous on A by its defining seminorms, so it preserves I and descends to Q. No characterization of I by its zero set is needed for this assertion.

Integration by parts with all boundary terms zero gives

\[
F_{Lk}(s)=sF_k(s),\qquad
j_\rho(Lq)=(\rho+t_\rho)j_\rho(q).
\tag{GIQ3.2}
\]

Thus the full local generator is multiplication by rho+t_rho, not merely the scalar rho. Every nilpotent Jordan term is retained. The centered generator C=L-1/2 has multiplier (rho-1/2)+t_rho, and

\[
V_a k(u)=k(u/a),\qquad
j_\rho(V_a q)
=a^{\rho-1/2}\sum_{r=0}^{m_\rho-1}
\frac{(\log a)^r t_\rho^r}{r!}\,j_\rho(q)
\quad(a>0).
\tag{GIQ3.3}
\]

M8.3 proves V_a preserves the exact source image and its closure, with inverse V_(1/a). Since conjugate(rho^#-1/2)=-(rho-1/2),

\[
B_Q(V_aq,V_ar)=B_Q(q,r),\qquad
B_Q(Cq,r)+B_Q(q,Cr)=0.
\tag{GIQ3.4}
\]

Both follow term by term in the absolutely convergent value sum, and the generator identity also follows by its explicit multiplier without differentiating an infinite sum.

For completeness the source reflection also descends. Poisson summation in M9 gives E(f)(1/u)=E(hat(f))(u); conjugating gives E(f)^#=E(conjugate(hat(f))). Fourier transformation and conjugation preserve the even Schwartz subspace with both f(0)=0 and integral f=0. The map k -> k^# is continuous on A by interchanging its two endpoint seminorms, so it preserves I. Its Mellin action is F_(k^#)(s)=conjugate(F_k(1-conjugate(s))), and on jets it is exactly t_rho^r -> (-1)^r t_(rho^#)^r with coefficient conjugation, as retained in NI26. Thus the involution used in GIQ2 is received from the source itself.

Every polynomial P(L) preserves I by GIQ3.1 and continuity. Its full local multiplier is P(rho+t_rho), retaining all derivative terms. Its exact form defect is

\[
B_Q(P(L)q,P(L)r)-B_Q(q,r)
=\sum_\rho m_\rho
\bigl(\overline{P(\rho^\#)}P(\rho)-1\bigr)
\overline{F_q(\rho^\#)}F_r(\rho).
\tag{GIQ3.4a}
\]

The sum converges absolutely because multiplying GIQ2.4 by a polynomial still gives arbitrarily rapid vertical decay. This distinguishes preservation of the source ideal from preservation of the form by a complete formula; neither property is inferred from the other. For C=L-1/2 the corresponding first-order defect vanishes by GIQ3.4, and its entire dilation flow preserves the form as proved.

The full arithmetic formula is preserved as well, not only its value side. For compact smooth multiplicative tests define k^#(u)=conjugate(k(1/u)) and multiplicative convolution. Then (V_a k)^#=V_(1/a)k^# and

\[
(V_a k)^#*(V_a l)=k^#*l.
\tag{GIQ3.5}
\]

To verify this, Mellin factors are respectively a^(-(s-1/2))F_k^#(s) and a^(s-1/2)F_l(s), so their product is unchanged; alternatively a direct substitution in the convolution integral gives the same equality. Mellin injectivity on the central line follows from Fourier injectivity in v=log u. Put h(v)=(k^#*l)(e^(-v)); then its original convention H(s)=integral h(v)e^(-(s-1/2)v)dv equals this Mellin product. Because h itself is unchanged, every endpoint, every prime-power term, the complete Gamma integral, every finite trivial-zero cutoff, and every support coefficient in M7 and WU2–WU3 is individually unchanged. This proves an actual source-ideal-preserving global operation with the exact full Weil form.

## GIQ4. Spectral differentiation has a nonzero global source-ideal defect

Let Rk(u)=(log u)k(u). It is continuous A -> A, because |log u| is bounded by a constant times u+u^(-1), and logarithmic derivatives satisfy the product rule. Its Mellin action is

\[
F_{Rk}(s)=F_k'(s).
\tag{GIQ4.1}
\]

Unlike L, R does not preserve I. This is proved at every actual zero by the same single original source kernel, with every completion factor displayed. Take the exact M9/C6 kernel

\[
f_0(x)=\frac\pi2 x^2(2\pi x^2-3)e^{-\pi x^2},\quad
k_0=\mathcal E(f_0),\quad
F_{k_0}(s)=b(s)\zeta(s),\quad
b(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\tag{GIQ4.2}
\]

The kernel is even Schwartz, has f_0(0)=integral f_0=0, and its Fourier self-duality and exact factor 1/8 were proved in C6. The multiplier b is holomorphic and nowhere zero throughout 0<Re s<1. Hence F_(k_0) has exact order m_rho at every actual rho. For its image under R,

\[
j_\rho(Rk_0)
=\frac{F_{k_0}^{(m_\rho)}(\rho)t_\rho^{m_\rho-1}}{(m_\rho-1)!}
=\frac{b(\rho)\zeta^{(m_\rho)}(\rho)t_\rho^{m_\rho-1}}{(m_\rho-1)!}\ne0.
\tag{GIQ4.3}
\]

All lower coefficients are zero. Since every element of I has zero such jet, Rk_0 is not in I although k_0 is in I. This proof applies to every multiplicity, including m_rho=1 where the surviving term is the value.

Define the actual defect map

\[
\partial_R:I\longrightarrow Q,\qquad h\longmapsto[Rh].
\tag{GIQ4.4}
\]

It is continuous and nonzero, with all local measurements specified in GIQ4.3. For a source h=E(f), the general coefficient is

\[
j_\rho(\partial_R\mathcal E(f))
=\frac{\zeta^{(m_\rho)}(\rho)}{(m_\rho-1)!}
\left(\int_0^\infty f(v)v^\rho\frac{dv}{v}\right)t_\rho^{m_\rho-1}.
\tag{GIQ4.5}
\]

This follows by differentiating the exact identity F_(E(f))=zeta times its source Mellin factor, with all derivatives below m_rho zero. The integral is defined on this strip as in M9. This constructs what failure to descend exposes: a nonzero source-to-quotient connecting map at every zero. It does not delete the corresponding classes.

Consequently a formal spectral translation s -> s+epsilon, with epsilon^2=0, acts on A tensor C[epsilon]/epsilon^2 by 1+epsilon R, but it does not act on Q tensor C[epsilon]/epsilon^2: it sends k_0 to a nonzero class epsilon[Rk_0] although k_0 is zero in Q. This is a precise first-order failure at the original divisor, not a comparison with an unrelated example.

## GIQ5. All local infinitesimal reparametrizations preserving the divisor

The preceding failure is exactly the constant part of a general local tangent calculation. In the analytic germ ring O_rho=C{t}, the original local zeta ideal is (t^m), because zeta=t^m times a holomorphic unit. For a germ b(t), the derivation b(t)d/dt preserves this ideal exactly when b(0)=0. Indeed it sends t^m to m t^(m-1)b(t); in characteristic zero this is divisible by t^m exactly when t divides b. Leibniz then proves preservation of the whole ideal. Thus the full preserving space is

\[
t\mathbb C\{t\}\frac d{dt}.
\tag{GIQ5.1}
\]

This is a classification at every actual zero, not an assumption about which vector fields preserve it. In the quotient A_rho every algebra endomorphism fixing complex scalars sends t to a nilpotent b_1t+...+b_(m-1)t^(m-1); conversely every such choice defines an endomorphism. It is invertible exactly when b_1!=0 for m>=2, by triangularity on successive powers, and at m=1 the sole endomorphism is the identity. All these maps fix the constant observation, so on the global product of actual local algebras they preserve the form NI29 exactly. They act nontrivially on higher jets, and none with image of t different from t commutes with the full original multiplication operator rho+t: applying a proposed intertwining identity to 1 proves that assertion.

These are maps of the exact local receiving algebras. No lift of an arbitrary independently chosen family of local endomorphisms to a continuous operator on Q is asserted. GIQ3 supplies the actual global lift for dilations; GIQ4 proves a specific global failure for translations. Both share the exact diagram GIQ2.3.

For the global jet trace form, any linear operator T whose constant map is unchanged, pi T=pi, satisfies T^*B_tr T=B_tr. This follows directly from B_tr(a,b)=[pi a,pi b]. The statement includes every locally nilpotent modification with zero constant component, irrespective of whether the multiplicities admit a uniform upper bound. If T is invertible on a vector space carrying the form, its pullback preserves both positive and negative indices: T maps a negative-definite subspace isomorphically to one of the original form, and T^(-1) proves the reverse inequality. These are global exact invariance assertions; they do not claim that arbitrary different measured currents coincide with the trace form.

## GIQ6. The quadratic collision is the exact actual reflected-pair algebra

Take any two-point orbit of the actual reflection and choose the member with real part greater than 1/2. Write

\[
\rho_+=c+\delta,\quad \rho_-=c-\delta,\quad
c=\tfrac12+i\gamma,\quad \delta>0,\quad
m=m_{\rho_+}=m_{\rho_-}.
\tag{GIQ6.1}
\]

This labels every such actual orbit and does not establish that any exists. Its full polynomial algebra and coordinate are

\[
A_{\rm pair}=\mathbb C[w]/((w^2-\delta^2)^m),\qquad w=s-c.
\tag{GIQ6.2}
\]

Chinese remainders give the exact full-jet isomorphism to A_(rho_+) times A_(rho_-), with w sent to (delta+t_+, -delta+t_-). The factors are coprime since 2delta!=0; the Taylor inverse is the one explicitly proved in WP14–WP15. The actual antilinear involution is w^#=-w. Passing only to its value quotient gives

\[
A_{\rm pair}/\sqrt{0}=\mathbb C[w]/(w^2-\delta^2)
\simeq\mathbb C^2,\quad a+bw\longmapsto(a+b\delta,a-b\delta).
\tag{GIQ6.3}
\]

The inverse sends (x,y) to (x+y)/2+(x-y)w/(2delta). Multiplicity remains m, and the exact Weil form pulled back by this map is

\[
m\bigl(\overline{a-b\delta}(c'+e\delta)
+\overline{a+b\delta}(c'-e\delta)\bigr)
=2m\overline a c'-2m\delta^2\overline b e.
\tag{GIQ6.4}
\]

Thus WRF51's negative quadratic coefficient is exactly the actual reflected-pair coefficient after the explicit specialization d=delta. All local jets remain in GIQ6.2, with precisely the known trace radical. The finite joint maps GIQ1.2 are surjective, and GIQ2 shows that the complete quotient detects all such signed directions. The connection is therefore to actual zero evaluations, not to an arbitrarily placed auxiliary root.

The formal sign change of that coefficient has an exact defect. Write B_u=C[r]/(r^2-u), with the antilinear involution r^#=-r, and let u=delta^2>0. There is a complex-algebra isomorphism

\[
\phi:B_u\longrightarrow B_{-u},\qquad r\longmapsto i r'.
\tag{GIQ6.5}
\]

It preserves the defining equation because (i r')^2=-(-u)=u and has inverse r' -> -i r. But it does not preserve the actual involution:

\[
\phi(r)^\#-\phi(r^\#)=2i r'.
\tag{GIQ6.6}
\]

The target reflected form pulled back by phi is diag(2m,+2mu), whereas the original form is diag(2m,-2mu), in the original basis 1,r. Its full difference is

\[
(\phi^*B_{-u}-B_u)(a+br,c'+er)=4mu\overline b e.
\tag{GIQ6.7}
\]

This is the precise information changed by the sign flip. Moreover the full spectral coordinate on the source is c+r, while its transported image is c+i r'. It is not the new-coordinate operator c+r'. Replacing the former by the latter changes the spectral points from c+-delta to c+-i delta. Keeping the actual source coordinate keeps its old eigenvalues. The geometric identification and the different coordinate replacement are both explicit.

The infinitesimal collision itself has an exact receiver in the actual multiplicity algebra. For m_rho>=2 the quotient A_rho -> C[eta]/eta^2, t_rho -> eta, is surjective. There is also an injective map C[eta]/eta^2 -> A_rho sending eta to t_rho^ceil(m_rho/2). The image squares to zero and is nonzero by its exponent, and 1 and that monomial are independent. At m_rho=1 there is no nonzero square-zero element in A_rho. The first map keeps the initial jet; the second chooses the displayed deeper jet. They are different maps and are not mutually inverse for general multiplicity. No multiple zero has been assumed to exist.

## GIQ7. The complete measured collision operator is retained

The measured collision of OC1–OC17 has a different, explicitly positive source metric. Preserve its actual observed columns u,v, a=u^*u, r=u^*v, Delta=ad-|r|^2>0, epsilon>0, b=epsilon sqrt(Delta), and orthonormal vectors g,h. With the parameter named z here to avoid confusion with the original zeta variable s, the complete operator is

\[
M_B(z)=C_B+F_B(z),\quad C_B=C_B^*,\quad
F_B(z)|_{g,h}=\begin{pmatrix}az+\epsilon r&0\\b&0\end{pmatrix}.
\tag{GIQ7.1}
\]

At z_*=-epsilon r/a it is C_B+N with N=b h g^*, N^2=0!=N. The exact dual-number isomorphism sends eta to N; the underlying two-dimensional regular module has basis h,g/b, because N h=0 and N(g/b)=h. This describes its relation to the maps in GIQ6 without claiming that its positive observation metric is the Weil metric.

In the original orthonormal basis g,h the full measured current is

\[
i(M_B(z)-M_B(z)^*)
=\begin{pmatrix}-2\Im(az+\epsilon r)&-ib\\ib&0\end{pmatrix},
\quad\det=-\epsilon^2\Delta.
\tag{GIQ7.2}
\]

Thus at collision its trace is zero and it still has two nonzero eigenvalues of opposite signs. The determinant does not disappear with the nilpotent algebra trace. On the unchanged full space, including C_B, write

\[
p_z(\lambda)=\det(\lambda I-M_B(z)),\quad
q_z(\lambda)=u^*\operatorname{adj}(\lambda I-M_B(z))u.
\]

The exact original rank-one identities are

\[
p_z(\lambda)=p_t(\lambda)-(z-t)q_t(\lambda),\qquad q_z=q_t,
\tag{GIQ7.3}
\]

and, where the indicated inverses exist,

\[
G_z=G_t+\frac{(z-t)G_tuu^*G_t}{1-(z-t)u^*G_tu}.
\tag{GIQ7.4}
\]

Column multilinearity proves GIQ7.3: terms with two rank-one columns vanish, and the one-column terms are the displayed adjugate contraction. Multiplication of GIQ7.4 by lambda I-M_B(t)-(z-t)uu^* proves its inverse identity. Consequently moving to z_* changes the full characteristic polynomial by -z_*q_0 unless that exact term is zero; keeping only Tr(N)=0 cannot show the full divisor was preserved. This is the strongest proved comparison available from these source data, with C_B and the metric retained. An identification of their marked periods with the global zeta operator would need an actual intertwiner beyond the dual-number algebra map; no such intertwiner is supplied or presumed here.

## GIQ8. Global classification of positive dilation-invariant jet forms

Construct the actual finite-support jet space

\[
J_{\rm alg}=\bigoplus_{\rho\in Z} A_\rho,
\quad T_b|_{A_\rho}
=e^{b(\rho-1/2)}\sum_{r=0}^{m_\rho-1}\frac{b^r t_\rho^r}{r!},
\quad b\in\mathbb R,
\tag{GIQ8.1}
\]

where the formula acts by multiplication. This is the exact jet action GIQ3.3 on all actual finite packets, each of which is reached by the surjection GIQ1.2. There is no arbitrary replacement of the source eigenvalues or multiplicities.

All positive semidefinite Hermitian forms H on J_alg invariant under every T_b are exactly

\[
H(x,y)=\sum_{\Re\rho=1/2}c_\rho\overline{x_\rho(0)}y_\rho(0),
\qquad c_\rho\ge0.
\tag{GIQ8.2}
\]

The sum is finite for each pair of inputs because they have finite support. Here is a complete classification proof. Positivity implies the Cauchy–Schwarz inequality by applying positivity to x+zy as a quadratic in the complex scalar z; in particular zero-norm vectors are in the radical. Invariance makes that radical invariant under T_b and its inverse. On each finite collection of blocks, quotient by the restricted radical; the induced form is positive definite and T_b is unitary there.

On a single rho-block, write alpha=Re(rho)-1/2. For a fixed x its squared norm under T_b has the form e^(2alpha b)P_x(b), where P_x is a real polynomial obtained by expanding the finite nilpotent exponential. Invariance says this equals the constant H(x,x) for all real b. If alpha!=0, a nonzero constant would force a polynomial to equal a nonconstant real exponential; differentiating more times than its degree disproves that equality. Hence the entire block has zero norm and lies in the global radical by Cauchy–Schwarz.

If alpha=0, the induced nilpotent operator N=M_t on the positive quotient must be zero. Otherwise choose x with maximal r>=1 for which N^r x!=0 in that quotient. The vector e^(bN)x is a polynomial in b of degree r with nonzero leading vector N^r x/r!. Its squared norm has leading coefficient ||N^r x||^2/(r!)^2>0, so is unbounded as |b| tends to infinity. This contradicts unitarity. Therefore t A_rho is radical, and only its constant coordinate remains. For two different critical-line zeros rho=.5+i gamma and eta=.5+i gamma', their remaining constant vectors acquire phases e^(i gamma b), e^(i gamma' b). Invariance gives H(x,y)=e^(i(gamma'-gamma)b)H(x,y) for all real b, so H(x,y)=0 because gamma!=gamma'. Each remaining one-dimensional form is multiplication by a nonnegative constant. This proves necessity of GIQ8.2. Substitution directly proves sufficiency.

The maximal quotient admitting such forms with every permitted coefficient strictly positive is therefore the explicit map

\[
J_{\rm alg}\longrightarrow\mathbb C^{(Z_{\rm line})},\quad
x\longmapsto(x_\rho(0))_{\Re\rho=1/2},
\tag{GIQ8.3}
\]

whose kernel consists of all off-line blocks and all critical-line higher jets. Taking weights c_rho=m_rho gives a positive invariant form on this quotient. This construction is not a proof of RH: the actual Weil form does not descend through removal of a two-point off-line block, since its matrix there is m[[0,1],[1,0]] and is nondegenerate. It does descend through the higher-jet kernel while keeping all value blocks, and that is precisely GIQ2.9 and NI29.

For the full value Hilbert space H, the positive form obtained by replacing J with I has the exact defect

\[
\langle x,y\rangle_H-[x,y]
=2\langle P_-x,P_-y\rangle_H,
\qquad P_-=(I-J)/2.
\tag{GIQ8.4}
\]

This follows by expanding I-J=2P_- and the orthogonal projection identity. It measures every actual negative reflection direction, including an infinite collection. Any proposed positive repair must account for this full defect in the original prime/Gamma/endpoint identity; it cannot disappear under a trace-radical modification, because those leave E_0 unchanged.

## GIQ9. Coefficients, support, and the full arithmetic comparison

Let C_rec be the exact WU1 coefficient algebra, with basis U=[tau] and N_n=[n] for n!=0, f=N_1, Q_c=U-f. The equations f^2=f, Q_c^2=Q_c, fQ_c=0 are coefficient identities. Let W_L be the vector space on the actual support labels, retaining every one. Tensor GIQ2.3 algebraically with C_rec and W_L. The maps are coordinatewise on finite coefficient expansions. Their kernels are the tensor products of the indicated scalar kernels, because a basis expansion has finitely many independent coordinates. Thus all exact jet, value, source-defect and full-operator formulas retain these records separately.

The two sections q -> q tensor U and q -> q tensor f have the same arithmetic image under ev(U)=1, ev(N_n)=n; their difference q tensor Q_c remains injective, recovered by the coefficient functional U -> 1, N_n -> 0. Neither the jet radical nor the positive invariant quotient identifies U with f. The classical form defect GIQ8.4 lifts separately with U, f, or Q_c, and arithmetic evaluation recovers exactly the first two while killing the third. This is the proved coefficient map, not a modification of the original zeta divisor.

For any compact smooth pair of tests with product transform A(s)=overline(F(1-conjugate(s)))G(s), retain the exact original identity

\[
\sum_\rho m_\rho A(\rho)
=A(0)+A(1)+A_\infty(h_A)-P_{\rm hist}(h_A),
\tag{GIQ9.1}
\]

where

\[
P_{\rm hist}(h)
=\sum_{n\ge2}\frac{\log L_n-\log L_{n-1}}{\sqrt n}
(h(\log n)+h(-\log n)),
\]
\[
A_\infty(h)=\frac1{2\pi}\int\widehat h(t)
\left(\Re\frac{\Gamma'(1/4+it/2)}{\Gamma(1/4+it/2)}-\log\pi\right)dt,
\quad L_n=\operatorname{lcm}(1,\ldots,n).
\tag{GIQ9.2}
\]

The nontrivial-zero compensation is not substituted for the raw divisor: for every finite cutoff B the retained triple is V_(zeta,B)=Z(A)+sum_(j=1)^B A(-2j)-A(1), G_B=A_infinity+A(0)+sum_(j=1)^B A(-2j), and V_(zeta,B)=G_B-P_hist. No infinite trivial-zero sum is asserted where it fails to converge.

The full formula also extends to the entire source test space used above; this is not left as a prospective application. In logarithmic coordinates A is the space of smooth K with every derivative bounded after multiplication by e^(N|v|), for every N. This equivalence follows from e^(N|v|)<=e^(Nv)+e^(-Nv)<=2e^(N|v|). Let chi be a smooth cutoff equal to 1 on [-1,1] and zero outside [-2,2], and put chi_R(v)=chi(v/R) for R>=1. Then chi_R K tends to K in every one of those seminorms: the product rule bounds the discarded tails by a constant times e^(-R) using the next stronger weighted seminorm, and derivatives of chi_R are uniformly bounded. Thus compact smooth tests are dense in A.

Convolution preserves this space. For each N,j, use e^(N|v|)<=e^(N|v-w|)e^(N|w|) inside the integral for (K*L)^(j). The weighted supremum of K^(j) times the weighted L^1 norm of L bounds the result. The latter norm is bounded by the weighted supremum of L with exponent N+1 times integral e^(-|w|)dw=2. These estimates also justify differentiation under the integral and continuity. Reflection preserves the same seminorms. Thus every pair k,l in A has its actual h_A in this logarithmic test space.

Every functional in GIQ9.1 is continuous there. The zero sum is continuous by the integration-by-parts bound GIQ2.4 and the unconditional zero count. Endpoint and each fixed finite trivial-zero evaluation are continuous Mellin evaluations. For the prime sum, retain the global estimate

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\bigl(|h(\log n)|+|h(-\log n)|\bigr)
\le 2\sup_v e^{|v|}|h(v)|\sum_{n\ge2}\frac{\log n}{n^{3/2}}<\infty.
\tag{GIQ9.2a}
\]

This uses the exact elementary bound Lambda(n)<=log n, not a prime cutoff. For the Gamma integral, the retained digamma factor on this vertical line is O(log(2+|t|)); its polynomially weighted integral against the rapidly decreasing Fourier transform is bounded by finitely many L^1 norms of h and its derivatives, each controlled by A's seminorms. This is the same source Gamma bound used in the original compact explicit formula. Therefore the identity on compact tests passes by the displayed cutoff approximation to every h in A, with all constants and original terms still present. Applying it to k^#*l proves that B_Q in GIQ2.5 is the continuous full original-zeta arithmetic pairing on the new quotient, for every pair in its actual source domain.

For a change of tests that preserves every zero value, subtracting their two proved instances of GIQ9.1, on either its compact or its just-proved full A domain, yields the exact arithmetic compensation

\[
\Delta(P_{\rm hist}-A_\infty)=\Delta A(0)+\Delta A(1).
\tag{GIQ9.3}
\]

At every lower support label the boundary and arithmetic records both change by Delta A(0); at the top they change by the complete expressions in GIQ9.3. Thus bold(B)-bold(D) is unchanged at every coordinate, although its separate terms need not be. Simultaneous dilation is the stronger case GIQ3.5, where the test itself is unchanged and every term is unchanged individually. A sign-changing modification such as GIQ6.5 or J -> I instead changes the actual value form by GIQ6.7 or GIQ8.4, so it cannot be called the same original-zeta Weil receiver unless those explicit defects are retained.

The established global conclusion is exact: the new theta-Mellin quotient reaches every original reflected value direction and every finite actual jet packet; source-preserving dilation is an isometry of the existing Weil form; spectral translation has the displayed nonzero source-to-quotient defect; infinitesimal changes that fix the reduced values preserve their signed form; and the quadratic sign flip changes either the involution or the spectral coordinate. These statements close the indicated comparison gap. They do not establish absence of actual off-line pairs or positivity of the complete arithmetic form.

## Read proof sources and scope

- M9 of PRIME_MONODROMY_STACKED_HISTORY.md, read in full together with M1–M8: definitions of A, I, E, Mellin, the kernel and coefficient extension.
- CAUCHY_REFLECTION_INDEX_DERIVATION.md, read in full: NI1–NI24 supplies the actual global weighted zero space, all-zero Cauchy density and signed index; NI25–NI29 supplies the already proved local trace radical; NI30–NI32 retains the support map. Its original-zeta reconstruction header governs the earlier completed notation.
- WEIL_PACKET_DERIVATION.md, complete equations WP1–WP57 and accompanying arguments read: exact primary jets, affine coordinate, multiplication, reflection and existing packet signature. No novelty is claimed for these inputs.
- WEIL_REFLECTION_FROBENIUS_DEFECT_DERIVATION.md, sections 1–2, 9–10, and equations WRF53–WRF74 with their supplied argument read: common integral quadratic, distinct coefficient realizations, and original heat sign. Only the polynomial complex specialization is used here; no complex-to-p-adic coefficient map is introduced.
- OBSERVED_COLLISION.md, read in full: OC1–OC17 fixes the original metric, nonzero measured area, nilpotent operator, C_B, current, characteristic polynomial and resolvent.
- WEIL_UNIT_DIFFERENCE_LIFT.md, WU1–WU4 and the opening definition of WU5 read: exact formal coefficients and original-zeta arithmetic identity.

This derivation makes no literature-priority claim. Its proofs are symbolic for the entire actual zero divisor, all multiplicities, every dilation parameter and the complete winding history. No finite numerical interval is used as evidence for RH.
