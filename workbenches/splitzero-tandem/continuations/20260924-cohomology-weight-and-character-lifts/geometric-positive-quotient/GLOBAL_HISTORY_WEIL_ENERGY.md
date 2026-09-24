# Global retained-history energy in the supported original-zeta Weil form

24 September 2026. Independent derivation receiving M6–M7 of PRIME_MONODROMY_STACKED_HISTORY.md and WU1–WU8 of WEIL_UNIT_DIFFERENCE_LIFT.md. Every formula below holds for every test in the stated space; no prime cutoff, numerical interval, or sampled inequality is used to infer a global assertion. The integer index N in the retained history ranges over all positive integers. Its nonzero increments occur at prime powers, not only at primes.

The user's Z_0,Z_1,Z_2 notation and the absence of intrinsic integer parity at tau are unchanged. No addition at tau is introduced. The symbols U=[tau], f_1=[1] and U-f_1 below belong to the existing formal coefficient algebra, where their operations have already been defined; they are not operations on the user's original tau.

## GHE1. Source, conventions, and what was already proved

Let F belong to C_c^infinity(R;C), put

\[
h=F^\#*F,\qquad F^\#(v)=\overline{F(-v)},\qquad
M_F(s)=\int_{\mathbb R}F(v)e^{-(s-1/2)v}\,dv,
\]
\[
H(s)=M_h(s)=\overline{M_F(1-\bar s)}M_F(s),\qquad
\widehat F(y)=\int_{\mathbb R}F(v)e^{-iyv}\,dv.
\tag{GHE1}
\]

Convolution and conjugation give the formula for H by compact Fubini. Set

\[
N_F=\|F\|_2^2,\qquad Q_F(t)=h(t)+h(-t),\qquad
E_F(t)=\|F(\cdot+t)-F\|_2^2=2N_F-Q_F(t).
\tag{GHE2}
\]

Indeed h(t)=integral conjugate(F(u))F(u+t) du. Thus Q_F is real and even, Q_F(0)=2N_F, and Q_F has compact support. E_F is smooth and nonnegative, E_F(t)=O(t^2) at zero, and E_F(t)=2N_F once |t| exceeds the diameter of the support of F. The estimate at zero follows either from Taylor's theorem or from
F(u+t)-F(u)=integral_0^t F'(u+v)dv and Cauchy–Schwarz. In particular E_F'(0)=0. Compact support here defines an unrestricted test space; no common bound on the support of F is imposed.

The retained original-zeta proof OZC1–OZC22 gives

\[
W_\zeta(h)=H(0)+H(1)+A_\infty(h)-P(h)
=\sum_\rho m_\rho H(\rho),
\tag{GHE3}
\]
\[
A_\infty(h)=\frac1{2\pi}\int_{\mathbb R}|\widehat F(y)|^2
\left[\Re\frac{\Gamma'(1/4+iy/2)}{\Gamma(1/4+iy/2)}-\log\pi\right]dy,
\]
\[
P(h)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}Q_F(\log n).
\tag{GHE4}
\]

The symbol rho ranges over actual nontrivial zeros of the original zeta, each with its actual multiplicity. The zero sum is absolutely convergent by compact smoothness and the unconditional zero count O(T log(T+2)); no location on the critical line is assumed. The arithmetic prime sum is finite for each F because Q_F is compactly supported, with no fixed prime bound common to the space.

The original Gamma factors and divisor are retained by

\[
j(s)=\frac{\zeta'(s)}{\zeta(s)},\quad
B(s)=\pi^{-s/2}\Gamma(s/2),\quad
\kappa(s)=-\tfrac12\log\pi+\tfrac12\frac{\Gamma'(s/2)}{\Gamma(s/2)},
\]
\[
j(s)+j(1-s)=-\kappa(s)-\kappa(1-s),\qquad
\operatorname{div}\zeta=\sum_\rho m_\rho[\rho]+\sum_{m\ge1}[-2m]-[1].
\tag{GHE5}
\]

For every integer b>=0, the exact retained finite-cutoff records are

\[
T_b(H)=\sum_{m=1}^b H(-2m),\quad
V_{\zeta,b}(H)=\sum_\rho m_\rho H(\rho)+T_b(H)-H(1),
\]
\[
G_b(H)=\frac1{2\pi i}\int_{\Re s=-2b-1}
H(s)[\kappa(s)+\kappa(1-s)]\,ds
=A_\infty(h)+H(0)+T_b(H),
\]
\[
V_{\zeta,b}=G_b-P,\qquad
W_\zeta=V_{\zeta,b}-T_b+H(1).
\tag{GHE6}
\]

All contours point upward. The residues at the original pole 1, trivial zeros -2m, and Gamma pole 0 have precisely the signs displayed. Increasing b adds H(-2b-2) to V, T and G, so the last map is compatible with the complete directed system. No convergence of the isolated infinite trivial-zero sum is asserted or needed. Every rewrite of P or A_infinity below substitutes into every finite-b identity in GHE6, not only into its scalar last line.

The translation-energy identity for the Gamma term was already present in FREE_PACKET_COST_REVIEW.md, FPR1–FPR3; it is rederived in GHE4 below with both endpoints retained. GLOBAL_CHEBYSHEV_RETURN.tex, GC1–GC31, already gives the distributional prime-history return for one particular compact endpoint-filtered kernel. The new calculation here treats the whole quadratic test space and makes its exact energy, Stieltjes boundaries, endpoint resolvent and support maps simultaneous. It makes no priority claim for the classical explicit formula or the von Mangoldt identity.

## GHE2. The complete retained history as a Stieltjes measure

For x>=1 and t>=0 define

\[
L_n=\operatorname{lcm}(1,\ldots,n),\quad L_1=1,
\qquad A(t)=\log L_{\lfloor e^t\rfloor}.
\tag{GHE7}
\]

M6 gives, by unique factorization,

\[
\log L_n-\log L_{n-1}=\Lambda(n),\qquad
A(t)=\sum_{2\le n\le e^t}\Lambda(n),\qquad
dA=\sum_{n\ge2}\Lambda(n)\delta_{\log n}.
\tag{GHE8}
\]

A is right-continuous, locally of bounded variation, A(0)=0, and has no atom at zero. Every atom log(p^a) has mass log p; all powers a>=1 remain. The no-jump stages of the retained clock stack are still present in L_n. Their zero increment is not an absent layer.

Here is the exact map from the user's temporal first appearances to this repeated measure. Retain the full step-time measure nu_step=sum_(n>=1) delta_n, and mark within it the first-appearance measure nu_first=sum_p delta_p. The index n is the original integer step; the marked steps p create new prime lines. For a>=1 let P_a(x)=x^a. Then the repeated weighted receiver is

\[
\mu_{\rm step}=\sum_{a\ge1}(P_a)_*
\big((\log x)\nu_{\rm first}\big)
=\sum_p\sum_{a\ge1}(\log p)\delta_{p^a}.
\tag{GHE8a}
\]

This sum of measures is locally finite: p^a<=X requires a<=log(X)/log(2) and p<=X. The map ell(x)=log x has inverse exp, and its measure pushforward gives

\[
\ell_*\mu_{\rm step}
=\sum_p\sum_{a\ge1}(\log p)\delta_{a\log p}=dA.
\tag{GHE8b}
\]

Every mass remains log p under the pushforward. The original primitive orbit period is log p; its a-th return is at a log p. The event p^a for a>1 is a repeated return on the existing p-line, not a new prime-line first appearance. An integer step which is not a prime power remains in nu_step even though its mass in mu_step is zero. Thus the pair (nu_step,nu_first) keeps every step and its marked first appearances, while GHE8a–GHE8b specify the full map receiving the original prime weights. For comparison with the Euler series, log zeta(s)=sum_(p,a) p^(-as)/a on Re(s)>1. Its negative derivative multiplies each term by a log p, leaving exactly log p rather than a log p or (log p)/a. This verifies the retained multiplicity factor directly.

With phi_F(t)=e^(-t/2)Q_F(t), GHE4 becomes the exact equality

\[
P(h)=\int_{(0,\infty)}\phi_F(t)\,dA(t).
\tag{GHE9}
\]

For an arbitrary real T>0 the finite-endpoint Stieltjes identity is

\[
\int_{(0,T]}\phi_F\,dA
=\phi_F(T)A(T)-\phi_F(0)A(0)
-\int_0^T A(t)\phi_F'(t)\,dt.
\tag{GHE10}
\]

This follows by writing A as the finite sum of its step jumps on [0,T], integrating each step against phi_F', and adding; it also covers a jump exactly at T because A(T) is the right-continuous value and the interval on the left includes T. The initial term is explicitly zero because A(0)=0, not because Q_F(0) vanishes. Choose T beyond the support of Q_F; then both phi_F(T) and its derivatives vanish, and the displayed expression is independent of all further increases of T. Consequently

\[
\boxed{P(h)=\int_0^\infty A(t)e^{-t/2}
\left[\frac{Q_F(t)}2+E_F'(t)\right]dt.}
\tag{GHE11}
\]

The sign follows from phi_F'=e^(-t/2)(-E_F'-Q_F/2). Every integral in GHE9–GHE11 is an ordinary convergent Stieltjes or Lebesgue integral, with every prime-power jump retained. The bracket is compactly supported, since Q_F and E_F' vanish together outside the correlation support. Thus GHE11 is global in the test space and makes no estimate at large t.

## GHE3. Both endpoints and their positive resolvent component

The two endpoint contributions are

\[
H(0)+H(1)=2\Re\big(\overline{M_F(1)}M_F(0)\big)
=\int_0^\infty Q_F(t)(e^{t/2}+e^{-t/2})dt.
\tag{GHE12}
\]

The second equality pairs t with -t in the compact integral for H. In particular no positive diagonal endpoint form is substituted for its actual off-diagonal expression.

Define the actual correlation resolvent

\[
\mathcal R(F)=\int_0^\infty Q_F(t)e^{-t/2}dt
=\iint_{\mathbb R^2}\overline{F(u)}F(v)e^{-|u-v|/2}\,du\,dv.
\tag{GHE13}
\]

Its Fourier expression, with all constants, is

\[
\boxed{\mathcal R(F)=\frac1{2\pi}\int_{\mathbb R}
\frac{|\widehat F(y)|^2}{y^2+1/4}\,dy.}
\tag{GHE14}
\]

Indeed integral_R exp(-|t|/2)exp(-iyt)dt equals
1/(1/2+iy)+1/(1/2-iy)=1/(y^2+1/4). Fourier inversion and Plancherel prove GHE14. It is strictly positive for F nonzero, because its multiplier is everywhere positive and the Fourier transform is injective on L^2. It is only a specified part of the endpoints; GHE12 also retains the growing exponential part.

## GHE4. The full Gamma energy, including its negative constant

Put

\[
k_\infty(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
c_\infty=\psi(1/4)-\log\pi
=-\gamma_E-3\log2-\frac\pi2-\log\pi,
\tag{GHE15}
\]

where psi is Gamma'/Gamma, distinct from the history function A. Then

\[
\boxed{A_\infty(h)=c_\infty N_F+
\int_0^\infty k_\infty(t)E_F(t)dt.}
\tag{GHE16}
\]

To verify every term, the convergent digamma integral in OZC22 gives

\[
A_\infty(h)=-(\gamma_E+\log\pi)N_F+
\int_0^\infty
\frac{2e^{-2t}N_F-e^{-t/2}Q_F(t)}{1-e^{-2t}}dt.
\tag{GHE17}
\]

Insert Q_F=2N_F-E_F. The coefficient of N_F is
-(gamma_E+log pi)+integral_0^infinity 2(e^(-2t)-e^(-t/2))/(1-e^(-2t))dt, which is exactly psi(1/4)-log pi under x=2t in the same digamma integral. Each of these combined integrals converges at zero because its numerator vanishes there; no divergent summands are integrated separately. At infinity the exponentials give convergence. The energy integral converges at zero because E_F(t)=O(t^2) and k_infinity(t)=1/(2t)+O(1), and at infinity because E_F is bounded and k_infinity decreases exponentially.

For the evaluation of psi(1/4), the Gamma reflection and duplication identities imply psi(3/4)-psi(1/4)=pi and psi(1/4)+psi(3/4)=2psi(1/2)-2log2. The same duplication at 1/2, with psi(1)=-gamma_E, gives psi(1/2)=-gamma_E-2log2. Solving these two linear equations yields GHE15. These constants were already checked in FPR3 and are retained here rather than absorbed into an unspecified potential.

## GHE5. The exact all-test energy with every retained history increment

Combining GHE3, GHE11, GHE12 and GHE16 gives

\[
\boxed{\begin{aligned}
W_\zeta(F^\#*F)={}&
2\Re\big(\overline{M_F(1)}M_F(0)\big)
+c_\infty N_F+\int_0^\infty k_\infty(t)E_F(t)dt\\
&-\int_0^\infty A(t)e^{-t/2}
\left[\frac{Q_F(t)}2+E_F'(t)\right]dt.
\end{aligned}}
\tag{GHE18}
\]

There is no independent bound on the support of F in this theorem. The last integral is the exact retained all-clock history, not a density approximation. Its smooth kernel contains the derivative E_F' with its displayed sign, so monotonicity of A and nonnegativity of E_F alone do not turn it into a nonnegative energy.

An exact original-coordinate version is obtained without losing the Jacobian: let x=e^t, and put mathsfA(x)=log L_floor(x). Then

\[
P(h)=\int_{(1,\infty)}x^{-1/2}Q_F(\log x)\,d\mathsf A(x)
=\int_1^\infty\mathsf A(x)x^{-3/2}
\left[\frac{Q_F(\log x)}2+E_F'(\log x)\right]dx.
\tag{GHE19}
\]

The endpoint at x=1 is zero because mathsfA(1)=0; the full finite endpoint at X is X^(-1/2)Q_F(log X)mathsfA(X), inherited from GHE10. These are inverse coordinate maps, t=log x and x=e^t, on the original history source.

## GHE6. A discrepancy defined by the actual endpoint cancellation

Two useful discrepancy functions retain different amounts of the exact endpoint data:

\[
R(t)=A(t)-(e^t-1),\qquad
D(t)=A(t)-(e^t+t-1)=R(t)-t.
\tag{GHE20}
\]

Both are right-continuous, locally of bounded variation, and have value zero at t=0. They are definitions on the actual history, not asymptotic assumptions about it. Their measures are

\[
dR=\sum_{p,a\ge1}(\log p)\delta_{a\log p}-e^t dt,
\]
\[
dD=\sum_{p,a\ge1}(\log p)\delta_{a\log p}-(e^t+1)dt.
\tag{GHE21}
\]

Every atom and the entire continuous subtraction are displayed. Substitution into GHE9 and GHE12 proves

\[
\boxed{W_\zeta(F^\#*F)
=A_\infty(F^\#*F)+\mathcal R(F)
-\int_{(0,\infty)}e^{-t/2}Q_F(t)\,dR(t),}
\tag{GHE22}
\]
\[
\boxed{W_\zeta(F^\#*F)
=A_\infty(F^\#*F)
-\int_{(0,\infty)}e^{-t/2}Q_F(t)\,dD(t).}
\tag{GHE23}
\]

For GHE22, the e^t dt contribution to P is exactly integral Q_F(t)e^(t/2)dt; subtracting it from GHE12 leaves the positive resolvent GHE13, with its full factor. For GHE23, the additional dt contribution supplies that remaining resolvent as well. Thus no endpoint is erased by declaring it zero or by replacing zeta by a completed function.

Integration by parts retains the same boundary terms as GHE10, with R or D in place of A. Since R(0)=D(0)=0, their lower boundary terms vanish. The upper terms vanish only because Q_F is compactly supported. Explicitly,

\[
\int e^{-t/2}Q_F(t)dR(t)
=\int_0^\infty R(t)e^{-t/2}
\left[Q_F(t)/2+E_F'(t)\right]dt,
\tag{GHE24}
\]

and identically for D. Inserting GHE16 into GHE23 supplies a full history-discrepancy energy formula with no hidden boundary. This is different from treating R or D as small: no bound for either function was used.

The whole continuous part in GHE22 also has an exact Fourier multiplier:

\[
A_\infty(F^\#*F)+\mathcal R(F)
=\frac1{2\pi}\int_{\mathbb R}|\widehat F(y)|^2
\left[\Re\psi(1/4+iy/2)-\log\pi+
\frac1{y^2+1/4}\right]dy.
\tag{GHE25}
\]

Its three summands are retained; positivity of the resolvent alone is not positivity of their sum. This identifies a concrete exact receiving term which can be used by any proposed global estimate on R.

## GHE7. Global sign information actually supplied by the history

The measures dR and dD are neither nonnegative nor nonpositive. At every prime-power point their mass is log p>0. On every nonempty open interval avoiding those discrete points, their densities are respectively -e^t and -(e^t+1), strictly negative. Such an interval exists around each non-jump t and can be chosen inside any open interval not reduced to a point. Nonnegative smooth test functions supported near an atom make the positive atomic contribution dominate as their supports shrink; nonnegative tests supported inside a jump-free interval have strictly negative value. This proves the assertion about the actual measures, globally and without a finite prime experiment.

This result does not assert a negative value of W_zeta. The test cone in GHE22–GHE23 is the specific autocorrelation cone phi_F=e^(-t/2)Q_F(t), and these functions need not be pointwise nonnegative. The exact map from F to this cone is GHE1–GHE2. The history measure's two signs therefore locate a signed correlation problem; they are not an RH disproof or a proof of positivity. The infinite-observation isomorphisms of M3–M5 preserve the jump sizes in GHE8 but supply no inequality for this remaining integral.

One tempting positive-energy manipulation can be decided completely. For nonzero F, neither of the separate expressions

\[
\int_0^\infty e^{-t/2}E_F(t)dA(t),\qquad
2N_F\int_0^\infty e^{-t/2}dA(t)
\tag{GHE26}
\]

is finite. For sufficiently large t, E_F(t)=2N_F. Moreover

\[
\int_0^\infty e^{-t/2}dA(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}=+\infty.
\tag{GHE27}
\]

Here is an elementary proof using only the original zeta pole. If the sum were finite, then for every real sigma>=1 its nonnegative terms would dominate sum Lambda(n)n^(-sigma). The latter equals -zeta'/zeta(sigma) when sigma>1. The original Laurent expansion zeta(s)=1/(s-1)+g(s), with g holomorphic near 1, gives -zeta'/zeta(sigma)=1/(sigma-1)+O(1), unbounded as sigma decreases to 1. This contradicts domination by the fixed finite sum, proving GHE27.

At every finite T, the valid identity is

\[
-\int_{(0,T]}e^{-t/2}Q_F(t)dA(t)
=\int_{(0,T]}e^{-t/2}E_F(t)dA(t)
-2N_F\int_{(0,T]}e^{-t/2}dA(t).
\tag{GHE28}
\]

The left side stabilizes exactly once T exceeds the correlation support. The right side has two separately divergent quantities whose same-cutoff difference is that stable value. Keeping only the first, apparently positive, term changes the form by the entire divergent diagonal term. Equations GHE26–GHE28 give the exact space of admissible paired expressions: keep the pair with its common cutoff and take its difference, whose value is the already convergent left side. This is a constructed receiving map on the retained pair, not a discarded calculation.

Thus the clock growth provides the exact original arithmetic form and a nonzero positive resolvent contribution, but does not yet provide the sign of the full form. The unresolved quantity is explicitly the correlation integral in GHE22 or GHE23, with its actual source R or D. No positivity assumption has been inserted in place of a calculation.

## GHE8. Every supported-zero coordinate and both coefficient sections

Let mathcal L be the existing finite support lattice with basis e_lambda, and let C_rec be WU1's coefficient algebra with independent basis U=[tau], N_n=[n] for nonzero integers n, N_0=0, multiplication Uc=c and N_nN_m=N_nm. Its involution conjugates scalar coefficients and fixes the displayed basis. Put f_1=N_1, Q_1=U-f_1. Then f_1^2=f_1, Q_1^2=Q_1, Q_1f_1=0. Arithmetic evaluation ev sends U to 1 and N_n to n; it sends Q_1 to zero. All of these are identities of the formal coefficient algebra, not restored addition at tau.

For the scalar quadratic test h retain, before coefficient extension,

\[
\begin{aligned}
\boldsymbol B(h)&=\mathbf e_{1_{\mathcal L}}(H(0)+H(1))
+\sum_{\lambda\ne1_{\mathcal L}}\mathbf e_\lambda H(0),\\
\boldsymbol Z(h)&=\mathbf e_{1_{\mathcal L}}\sum_\rho m_\rho H(\rho),\\
\boldsymbol D_A(h)&=\mathbf e_{1_{\mathcal L}}
\left(\int e^{-t/2}Q_F(t)dA(t)-A_\infty(h)\right)
+\sum_{\lambda\ne1_{\mathcal L}}\mathbf e_\lambda H(0).
\end{aligned}
\tag{GHE29}
\]

These obey bold B-bold Z=bold D_A coordinatewise by GHE3 and GHE9. The lower supported coordinates remain H(0)=conjugate(M_F(1))M_F(0), even when that amplitude happens to be zero. A zero amplitude does not remove its label.

The exact endpoint-discrepancy receiving map becomes

\[
\boldsymbol B(h)-\boldsymbol D_A(h)
=\mathbf e_{1_{\mathcal L}}
\left(A_\infty(h)-\int e^{-t/2}Q_F(t)dD(t)\right).
\tag{GHE30}
\]

At every lower coordinate the two explicitly retained terms H(0)-H(0) give zero. At the top coordinate GHE23 gives the displayed value. The vector records in GHE29 are kept alongside this linear map; GHE30 is not a replacement of their source by a scalar. The original-zeta finite-divisor triples in GHE6 are carried in the same way, coordinate by coordinate, with every trivial-zero term and pole term retained.

For a marked coefficient c=U or c=f_1, tensor every term of GHE29–GHE30 with c. On the diagonal coefficient tests FU and Ff_1 the corresponding values are W_zeta(h)U and W_zeta(h)f_1. Their difference is W_zeta(h)Q_1, while arithmetic evaluation returns W_zeta(h) from each. This follows directly from c*c=c and WU6; none of the Stieltjes rewrites changes these products or the kernel of ev. Thus no sign flip has appeared through forgetting the formal coefficient direction.

More generally the formulas above are diagonal identities of sesquilinear forms and extend to cross terms by polarization. The total Weil form, the Gamma term and the prime term are Hermitian; an individual endpoint H(0) and its lower-support copies need not be real and are not asserted to be Hermitian. The following polarization identity works for every complex sesquilinear form, including those individual endpoint forms. For a conjugate-linear first slot it is
 B(F,G)=(q(F+G)-q(F-G))/4
 -i(q(F+iG)-q(F-iG))/4.
Applying this equality to every displayed quadratic term proves the cross identity with the same constants. For Phi=sum_i F_i c_i and Psi=sum_j G_j d_j in the algebraic coefficient tensor product, define each receiver by the finite sum of B(F_i,G_j)c_i* d_j. Every infinite zero sum and Gamma integral then occurs in a fixed finite-dimensional coefficient span and converges coordinatewise as in GHE3–GHE4. This proves the entire coefficient/support extension, including every mixed term, rather than only its two marked diagonal sections.

## GHE9. Relation to the existing Chebyshev and residue-norm calculations

The existing GC source uses, on the whole real axis,
 Z_GC(t)=e^(-t/2)(psi_classical(e^t)-e^t), with psi_classical(e^t)=0 below log 2. On t>=0 the exact map to the present source is

\[
R(t)=e^{t/2}Z_{GC}(t)+1,\qquad
D(t)=e^{t/2}Z_{GC}(t)+1-t.
\tag{GHE31}
\]

At t=0, Z_GC(0)=-1; both boundary values R(0)=D(0)=0 follow. Differentiating the first identity in distributions gives
 dR=e^(t/2)(D_t+1/2)Z_GC, which is precisely dA-e^t dt by GC8. Therefore GHE22 is an all-quadratic-test receiving map of the same full signed arithmetic source, not a different prime model. The +1 and -t terms explain exactly the endpoint adjustments and must not be suppressed.

TAU_WEIL_NORM_RECONSTRUCTION.md concerns a historically specified different prime-residue weight N_pr(n)=product_(p|n)(p+1)^(v_p(n)). That note's TN19 proves
 P-P_tau=(1/(2pi))integral |hat F(y)|^2 2Re r_tau(1/2+iy)dy,
where

\[
r_\tau(s)=\sum_p\left(\frac{\log p}{p^s-1}
-\frac{\log(p+1)}{(p+1)^s-1}\right).
\tag{GHE32}
\]

Consequently the same form in that receiver has Gamma multiplier
Re psi(1/4+iy/2)-log pi-2Re r_tau(1/2+iy), with its original endpoints and P_tau. The current all-clock history gives the original n-weight exactly by GHE8. It does not license replacement by p+1 without the full correction GHE32. No historical source multiplication rule from TN is imposed on the current parityless tau; this paragraph only records the existing analytic receiving map and its complete correction.

## GHE10. The remaining history discrepancy retains every original zero

The discrepancy in GHE22 has an exact global transform, not merely a description by its signs. For Re(s)>1 define

\[
\mathscr R(s)=\int_0^\infty R(t)e^{-st}dt,
\qquad \mathscr D(s)=\int_0^\infty D(t)e^{-st}dt.
\tag{GHE33}
\]

These converge absolutely and locally uniformly: A(t)<=e^t t for t>=log 2, because each nonnegative Lambda(n)<=log n<=t and there are at most e^t terms. Hence R and D are O((1+t)e^t). The same bound with any fixed power of t justifies differentiation under the integral on compact subsets of Re(s)>1. Stieltjes integration by parts retains the finite upper term e^(-sT)A(T), which tends to zero on this half-plane, and the lower term A(0)=0. It gives

\[
s\int_0^\infty A(t)e^{-st}dt
=\int_0^\infty e^{-st}dA(t)
=-\frac{\zeta'(s)}{\zeta(s)}.
\]
\[
\boxed{\mathscr R(s)=-\frac1s\frac{\zeta'(s)}{\zeta(s)}
-\frac1{s-1}+\frac1s,\qquad
\mathscr D(s)=-\frac1s\frac{\zeta'(s)}{\zeta(s)}
-\frac1{s-1}+\frac1s-\frac1{s^2}.}
\tag{GHE34}
\]

Each rational term has its displayed source: -e^t, +1, and -t respectively. All remain in the formula. Conversely the exact arithmetic return is

\[
-\frac{\zeta'(s)}{\zeta(s)}
=s\mathscr R(s)+\frac{s}{s-1}-1
=s\mathscr D(s)+\frac{s}{s-1}-1+\frac1s.
\tag{GHE35}
\]

The original Laurent constant at one is gamma_E, as follows from
lim_(n to infinity)(sum_(k=1)^n 1/k-log(n+1))=gamma_E in the convergent integral subtraction defining the holomorphic part of zeta. Thus
-zeta'/zeta(1+epsilon)=epsilon^(-1)-gamma_E+O(epsilon). Substitution into GHE34, with 1/(1+epsilon) kept through its constant term, yields

\[
\mathscr R(1)=-\gamma_E,\qquad
\mathscr D(1)=-\gamma_E-1
\tag{GHE36}
\]

as values of the analytic continuations. These statements do not claim convergence of the integrals GHE33 at s=1. The original pole at one has been accounted for by its explicit -1/(s-1) term and the boundary constant +1/s, not forgotten.

At every actual nontrivial zero rho of multiplicity m_rho, the meromorphic continuations in GHE34 have residues

\[
\operatorname{res}_{s=\rho}\mathscr R(s)
=\operatorname{res}_{s=\rho}\mathscr D(s)
=-\frac{m_\rho}{\rho}\ne0.
\tag{GHE37}
\]

Indeed zeta'/zeta has residue m_rho, while rho is neither 0 nor 1 and all the displayed rational corrections are holomorphic there. The source's multiplicity is recovered exactly as -rho times this residue. Thus the same discrepancy whose Stieltjes pairing remains in GHE22 carries every original nontrivial zero, with multiplicity, before any compact test is chosen. The transforms retain a precise inverse arithmetic map GHE35. This is a proved global spectral connection for the actual retained-history source; it does not fix the real parts of its poles or their corresponding Weil signs.

## Reading and proof provenance

Actually read for this derivation: PRIME_MONODROMY_STACKED_HISTORY.md M1–M9; WEIL_UNIT_DIFFERENCE_LIFT.md WU1–WU8; ORIGINAL_ZETA_COMPACT_WEIL_RECONSTRUCTION.md OZC1–OZC28, with its source theorem locators; TAU_WEIL_NORM_RECONSTRUCTION.md TN1–TN6; FREE_PACKET_COST_REVIEW.md FPR1–FPR3 and the beginning of FPR2; and the complete local programme TeX GLOBAL_CHEBYSHEV_RETURN.tex GC1–GC31. The latter file already contains its two historical sign/tail-residue corrections; no obsolete version was used. Existing programme discovery used the source-reading ledger and filename/content search before derivation. No new external literature or PDF reading was needed.

The underlying human explicit-formula source is Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, arXiv:math/9811068v1](https://arxiv.org/abs/math/9811068v1), Appendix II, Theorem 6, through the retained complete OZC proof. No fresh full reading of that author source is claimed here. The supported-coordinate source is [SZW33–SZW38, pinned public proof](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/76f421965914beb133df797835f940849844dc4f/workbenches/splitzero-tandem/branches/tau-zero-prime-positivity/SUPPORTED_ZERO_PRIME_WEIL_DERIVATION.md).

This derivation proves the global all-test Stieltjes/energy formulas, the exact endpoint resolvent, their full source and support maps, and the divergence of the separated positive-prime-energy expression. It does not prove nonnegativity of the full Weil form, and no RH conclusion follows from the sign calculations made here.
