# Independent check of the mass-to-prime theta receiver

Date: 2026-09-23. Read all definitions and proofs MRT1–20 in MASS_THETA_PRIME_RECEIVER.tex. Independently read the complete FR15–25 source-coordinate passage, quotient proof, receiver inverse, and seminorm proof in the local original-zeta-return NOTE.tex. The source locators and published edition are those supplied in MRT1. The calculations below verify the actual objects, not a replacement quotient.

## MPC1. Moment splitting and the full algebraic quotient

Keep \(H=\mathcal S(\mathbb R)^{\rm even}\), \(m_H(h)=(h(0),\int_{\mathbb R}h)\), \(H_0=\ker m_H\), \(R=\mathbb C[\mathbb Q_{>0}^{\times}]\), and \(I=\ker\operatorname{aug}\). With \(G(y)=e^{-\pi y^2}\), the full Gaussian integrals are \(\int G=1\) and \(\int y^2G=1/(2\pi)\). Hence
\[
h_0=(1-2\pi y^2)G,\qquad h_1=2\pi y^2G
\]
have moments \((1,0)\), \((0,1)\). Define the exact right inverse \(s(u_0,u_1)=u_0h_0+u_1h_1\). Every \(h\) decomposes uniquely as
\[
h=(h-s(m_H(h)))+s(m_H(h)),
\qquad h-s(m_H(h))\in H_0.
\tag{MPC1}
\]

All group-ring tensor sums are finite. The actual moment-zero source is
\[
M_0=\ker(\operatorname{aug}\otimes m_H:R\otimes H\to\mathbb C^2).
\]
Applying MPC1 coefficientwise gives the exact \(R\)-module decomposition
\[
M_0=(R\otimes H_0)\oplus(I\otimes\mathbb C^2).
\tag{MPC2}
\]
Indeed the first summand has zero moment identically, and the second condition is exactly zero augmentation in each of the two moment coordinates. Multiplication by \(I\) gives
\[
IM_0=(I\otimes H_0)\oplus(I^2\otimes\mathbb C^2).
\tag{MPC3}
\]
Since \(R/I\cong\mathbb C\), the quotient is therefore
\[
Q_0=M_0/IM_0\cong H_0\oplus(I/I^2)\otimes\mathbb C^2.
\tag{MPC4}
\]
This is an algebraic quotient, with no topology imposed.

For each prime \(p\), let \(\ell_p\) correspond to \([t_p-1]\). The identity
\[
t_{ab}-1=(t_a-1)+(t_b-1)+(t_a-1)(t_b-1)
\]
gives additivity of the class, and \(t_{p^{-1}}-1=-t_{p^{-1}}(t_p-1)\) gives its negative at \(p^{-1}\), since multiplication by \(t_{p^{-1}}\equiv1\pmod I\) acts identically modulo \(I^2\). Prime factorization of a positive rational proves
\[
[t_a-1]=\sum_p v_p(a)[t_p-1].
\tag{MPC5}
\]
The functionals \(D_p(t_a)=v_p(a)\), extended linearly, vanish on \(I^2\): on its spanning products \((t_a-1)(t_b-1)\), the value is \(v_p(ab)-v_p(a)-v_p(b)=0\). They take value \(\delta_{pq}\) on \(t_q-1\), proving independence. Thus
\[
I/I^2\cong\bigoplus_p\mathbb C\ell_p
\tag{MPC6}
\]
with exactly the asserted coefficients and no missing rational denominator factor.

For \(c=[\sum_a t_a\otimes h_a]\), the quotient coordinates are
\[
\Phi c=\sum_a h_a,\qquad
\beta c=\sum_p\ell_p\otimes\sum_a v_p(a)m_H(h_a).
\tag{MPC7}
\]
Their first coordinate lies in \(H_0\) by the defining equation of \(M_0\). To verify descent directly, replace a representative \(c_0\in M_0\) by \((t_r-1)c_0\). Its first coordinate is zero, and its \(p\)-boundary coordinate is
\(v_p(r)\sum_a m_H(h_a)=0\).
The ideal \(I\) is spanned by these group differences, so both maps annihilate all of \(IM_0\).

An inverse sends \((h,\sum_p\ell_p\otimes u_p)\) to
\[
[1\otimes h]+\sum_p[(t_p-1)\otimes s(u_p)].
\tag{MPC8}
\]
MPC7 verifies one composite. The direct decomposition MPC4 and basis MPC6 verify the other. Replacing \(s(u_p)\) by any other moment lift changes it by an element of \(H_0\); multiplying that difference by \(t_p-1\) puts it in \(I\otimes H_0\subset IM_0\). Thus the map \(b\) used in MRT5 and MRT10 is independent of moment lifts.

## MPC2. Actual spherical coordinates and the periodization kernel

FR16 uses \(\alpha_a f(x)=f(a^{-1}x)\) simultaneously at all places. Its finite part is
\(\eta_a=\bigotimes_p1_{p^{v_p(a)}\mathbb Z_p}\), whose additive Haar integral is \(\prod_pp^{-v_p(a)}=a^{-1}\). Its real part is \(h(x/a)\), with real integral \(a\int h\). Their product is unchanged. For an initial finite-place representative \(\eta_a\otimes f_a\), the correct inverse real coordinate is \(h_a(x)=f_a(ax)\), and its moments are
\[
m_H(h_a)=\left(f_a(0),a^{-1}\int_{\mathbb R}f_a(x)\,dx\right).
\tag{MPC9}
\]
The factor \(a^{-1}\) in FR20 is therefore correct.

The finite spherical basis is also exact. A compactly supported, locally constant \(\mathbb Z_p^\times\)-invariant function has values \(c_k\) on valuation \(k\), vanishes for sufficiently negative \(k\), and is constant for sufficiently positive \(k\). It equals the finite sum
\(\sum_k(c_k-c_{k-1})1_{p^k\mathbb Z_p}\).
On valuation \(l\), the sum telescopes to \(c_l\); at zero it telescopes to its eventual constant. Finite linear independence follows by the same shell differences. Taking the restricted tensor product gives the \(\eta_a\) basis used above. The relation of the sign \(-1\) kills odd real functions and fixes even ones, because its difference acts by \(-2\) on the odd part. Thus the stated even component is the correct algebraic source.

For the section \(s(h)\), the finite factors in adelic periodization restrict the nonzero rational index to nonzero integers. On \(\alpha_a s(h)\), they instead restrict it to \(a\mathbb Z\setminus\{0\}\); writing the rational index as \(an\), the real evaluation becomes \(h(nx)\). The original modulus factor remains \(x^{1/2}\), because the simultaneous rational norm is one. Positive and negative integers give the exact factor two:
\[
\mathcal E(c)(x)=x^{1/2}\,2\sum_{n\ge1}(\Phi c)(nx).
\tag{MPC10}
\]
Consequently every class \(b(v)\) has \(\Phi=0\) and periodization zero.

For completeness, injectivity of this periodization on \(H_0\) follows from the exact inverse
\[
h(x)=\frac12\sum_{n\ge1}\mu(n)\Theta h(nx),\qquad
\Theta h(x)=2\sum_{m\ge1}h(mx),\quad x>0.
\]
Absolute convergence of the double sum follows from
\(\sum_{m,n}|h(mnx)|\le C_Bx^{-B}\sum_{m,n}(mn)^{-B}<\infty\)
for \(B>2\). The divisor sum of \(\mu\) leaves only the \(mn=1\) term. Smooth even extension determines the rest of \(h\). Therefore the kernel of \(\mathcal E\) on \(Q_0\) is precisely \(b(\mathcal B)\).

The FR25 weight is positive and has its original measure \(dx/x\) and compact-unit mass one; replacing that mass by \(c_K\) multiplies every squared seminorm by \(c_K\). For \(h\in H_0\), Poisson summation has no endpoint moment terms, so \(x^{1/2}\Theta h(x)\) decays faster than every power at both multiplicative ends; the stated weighted integral is finite. Its vanishing forces the continuous function \(\mathcal E(c)\) to vanish identically. Thus its kernel is exactly \(b(\mathcal B)\). Nonzero boundary coordinates cannot descend through its Hausdorff quotient, regardless of their coordinate continuity in a different source norm.

## MPC3. The heat-source moment map and its completion

For a finite even sequence \(a\), retain the full kernel
\[
k_T(y)=(4\pi T)^{-1/2}e^{-y^2/(4T)},\qquad T>0.
\]
The finite translated sum \(A_Ta(y)=\sum_na_nk_T(y-n)\) is an even Schwartz function, and direct evaluation and integration give
\[
m_H(A_Ta)=\left(\sum_na_nk_T(n),\sum_na_n\right)
=(q_T(a),m(a)).
\tag{MPC11}
\]
Its prime class is admitted because \(t_p-1\) has augmentation zero. MPC7 gives exactly
\[
(\Phi,\beta)[(t_p-1)\otimes A_Ta]
=(0,\ell_p\otimes(q_T(a),m(a))).
\tag{MPC12}
\]

Write \(k_0=k_T(0)\), \(k_1=k_T(1)\). Their actual values give \(k_0>k_1>0\). The coefficients
\[
a_0=\frac{u_0-k_1u_1}{k_0-k_1},\qquad
a_1=a_{-1}=\frac{k_0u_1-u_0}{2(k_0-k_1)}
\tag{MPC13}
\]
have \(a_0+2a_1=u_1\) and \(k_0a_0+2k_1a_1=u_0\), proving the claimed surjectivity from an actual finite even source.

On the even top-support graph completion, the coordinates are \((a,0,m)\), with exact norm \(\|a\|_2^2+|m|^2\). Put \(d=1/(4\pi T)\), so \(k_T(n)=\sqrt d\,e^{-\pi dn^2}\). Its exact squared sample norm is
\[
\sum_n k_T(n)^2=d\,\vartheta(2d),\qquad
\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}.
\tag{MPC14}
\]
Thus \(q_T\) extends continuously to even \(\ell^2\), with exact norm \(\sqrt{d\vartheta(2d)}\). Equality is attained on a scalar multiple of the real even sample vector itself. The complete pair map
\[
F_T(a,0,m)=(q_T(a),m)
\tag{MPC15}
\]
has exact operator norm \(\sqrt{\max\{d\vartheta(2d),1\}}\) for the Euclidean norm on its two coordinate values. The statement is about these two specified scalar coordinates, not a chosen norm on \(Q_0\).

Even finite graph sources are dense: truncate on symmetric finite sets and put the missing mass uniformly on a sufficiently large finite collection of opposite pairs. The correction has the prescribed sum and arbitrarily small squared norm, exactly as in MCB6. It follows that
\[
\widehat B_{p,T}(a,0,m)=b(\ell_p\otimes F_T(a,0,m))
\tag{MPC16}
\]
is the coordinate-continuous extension in MRT10. A general completed \(a\) need not give a Schwartz function or a convergent total sum. Formula MPC16 does not claim either: it constructs a genuine algebraic quotient class using the explicit Schwartz lift MPC8 of its two scalar coordinates.

The supported-zero extension sends \((a,0,m)\) to \((m\delta_0,0,m)\), so
\[
F_T\widehat E=J_TF_T,\qquad
J_T=\begin{pmatrix}0&\sqrt d\\0&1\end{pmatrix}.
\tag{MPC17}
\]
This proves MRT11 with exactly its stated boundary-summand domain. The matrix is idempotent, has image \(\mathbb C(\sqrt d,1)\), kernel \(\mathbb C(1,0)\), and Euclidean norm \(\sqrt{d+1}\). In particular the completed pure-mass state maps from \((0,1)\) to \((\sqrt d,1)\) under this actual receiving action. All these classes have periodization seminorm zero by MPC10, and their nonzero boundary coordinates remain nonzero by MPC4–8.

## MPC4. The admitted Gaussian coefficient family

For \(x>0\), let \(a_n^x=e^{-\pi n^2x}\). It is even and absolutely summable. Its finite truncations converge in the exact graph norm to \((a^x,0,\vartheta(x))\), because both the squared tails and absolute mass tails vanish. This distinguishes it from the unweighted infinite comb.

The function \(A_Ta^x\) is Schwartz. Each derivative of a translated kernel is a polynomial in \(y-n\) times its Gaussian. For every nonnegative integer \(M\), the inequality
\[
1+|y|\le(1+|n|)(1+|y-n|)
\]
bounds its weighted supremum by a fixed finite Gaussian-polynomial bound times \((1+|n|)^M e^{-\pi n^2x}\), which is summable. Uniform convergence of all these weighted derivatives proves the claim. Hence the class may be represented directly by this Schwartz function, and its quotient equals the completed-coordinate class by MPC12 and the uniqueness in MPC4.

Multiplying the two full Gaussian factors gives
\[
q_T(a^x)=\sqrt d\,\vartheta(x+d),\qquad m(a^x)=\vartheta(x).
\tag{MPC18}
\]
After \(\widehat E\), the moment pair is \((\sqrt d\,\vartheta(x),\vartheta(x))\). Before minus after is therefore
\[
\left(\sqrt d[\vartheta(x+d)-\vartheta(x)],0\right).
\tag{MPC19}
\]
Its first coordinate is strictly negative for every \(x,d>0\): the zero integer term cancels, and each of the positive terms at \(n\ne0\) strictly decreases under \(x\mapsto x+d\). Absolute convergence permits their comparison. Thus the prime-boundary class difference is genuinely nonzero.

## MPC5. Both Mellin coordinates and the original zeta factors

The single marked integer-zero coefficient has moment pair \((\sqrt d,1)\), independent of \(x\). Retain it separately. The remaining pair is
\[
\left(\sqrt d[\vartheta(x+d)-1],\vartheta(x)-1\right).
\tag{MPC20}
\]
For \(\Re s>1\), absolute integration term by term gives
\[
\int_0^\infty[\vartheta(x)-1]x^{s/2-1}\,dx
=2\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{MPC21}
\]
Indeed the integers \(n,-n\) give exactly two, and substitution \(u=\pi n^2x\) gives \(\pi^{-s/2}n^{-s}\Gamma(s/2)\). Absolute convergence reduces to \(\sum_{n\ge1}n^{-\Re s}<\infty\). On this domain \(\Gamma(s/2)\) is finite and nonzero, so multiplying by the full factor \(\pi^{s/2}/(2\Gamma(s/2))\) recovers the original \(\zeta(s)\). No completed function replaces it.

For the first coordinate, the same calculation is absolutely valid already for \(\Re s>0\):
\[
\int_0^\infty\sqrt d[\vartheta(x+d)-1]x^{s/2-1}\,dx
=2\sqrt d\,\pi^{-s/2}\Gamma(s/2)
\sum_{n\ge1}e^{-\pi dn^2}n^{-s}.
\tag{MPC22}
\]
The Gaussian factor makes the sum absolutely convergent for every real part, while the remaining integral at \(x=0\) requires \(\Re s>0\). The series on the right is entire in \(s\), since every derivative contributes a power of \(\log n\), dominated by the fixed Gaussian uniformly on compact \(s\)-sets. The Gamma factor is retained and has its own meromorphic behavior.

On the common domain \(\Re s>1\), subtraction of MPC21 from MPC22 with the full factor \(\sqrt d\) proves the Mellin transform of MPC19:
\[
2\sqrt d\,\pi^{-s/2}\Gamma(s/2)
\left[\sum_{n\ge1}e^{-\pi dn^2}n^{-s}-\zeta(s)\right]
\ell_p\otimes(1,0).
\tag{MPC23}
\]
This is exactly MRT20, including sign, factors, and prime direction.

The separate constant has no Mellin convergence half-plane on \((0,\infty)\): convergence at zero requires \(\Re s>0\), while convergence at infinity requires \(\Re s<0\). Its handling through Poisson summation must identify both original zero terms. Writing \(\psi=(\vartheta-1)/2\), Poisson gives
\[
\psi(x)=x^{-1/2}\psi(1/x)+\tfrac12(x^{-1/2}-1).
\]
Integration on \((0,1)\) against \(x^{s/2-1}\) gives
\[
\tfrac12\int_0^1 x^{(s-1)/2-1}\,dx
-\tfrac12\int_0^1x^{s/2-1}\,dx
=\frac1{s-1}-\frac1s.
\tag{MPC24}
\]
The term \(1/(s-1)\) comes from the zero Fourier coefficient \(x^{-1/2}\); the term \(-1/s\) comes from the zero source coefficient \(1\). Both are present and have distinct source origins. The remaining integral is the entire integral in LH15, with its complete prefactor \(\pi^{s/2}/\Gamma(s/2)\).

## Check result and one wording repair

No algebraic quotient, coefficient-map, Gaussian-constant, sign, or convergence-domain error was found in MRT1–20. The extensions to completed states use actual Schwartz moment lifts, rather than assuming all completed heat functions are Schwartz. The nonzero boundary classes really lie in the exact kernel of the original periodization seminorm, with no new quotient norm introduced.

The endpoint sentence in MRT6 should name both source origins instead of attributing both terms to the marked constant alone: the zero Fourier coefficient gives \(1/(s-1)\), and the zero source term gives \(-1/s\), as proved in MPC24. This is a precision repair to provenance of the terms; the displayed analytic formulas are correct.
