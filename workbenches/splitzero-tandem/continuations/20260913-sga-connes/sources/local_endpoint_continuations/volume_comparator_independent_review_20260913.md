# Independent complete review of the scalar volume comparator

Date: 13 September 2026.

## Read scope and result

I read `volume_comparator_review_20260913.md` completely, including every displayed equation VC.1–43 and all eight sections. I then reread the complete revised file after the first corrections and read the complete final file again, including the added displays VC.15a–15b. The final audited comparator SHA-256 is `47ac2b43904ec43f3ce19d7c74ba760a29ce4d7a3e411132fe81ec0b27af6104`. The mathematical review below covers the original source, the finite polynomial and quotient maps, every inequality in the coefficient and moment estimates, the determinant exponent, and the asymptotic coefficient.

The finite comparison and all stated growth coefficients are correct. The review identified squared-power serialization errors, a type-description error after VC.32, and two further coordinate/notation identifications. The author corrected all of them, and the complete final file contains those repairs. No unresolved mathematical finding remains in this audited version. No parent tests were run or rerun for this review.

The principal audited calculations are

\[
B_q(r)=\left(\frac{1+r}{1-r}\right)^q,
\qquad
\log B_q(r)^2\le\frac{16}{3}qr
=\frac{16R_0}{3D}k,
\tag{AR.1}
\]

\[
C_{k,q}=\frac{U_k(T)A_{2q-1}^2B_q(r)^2}{T\lambda_k(T)},
\qquad
0\le\log\frac{V_q}{V_{2q-1}}\le q\log C_{k,q},
\tag{AR.2}
\]

and

\[
\limsup_{k\to\infty}\frac{1}{q_k^2}
\log\frac{V_{q_k}}{V_{2q_k-1}}
\le\alpha D+\log256.
\tag{AR.3}
\]

These statements retain the original measure, monic annihilator, root multiplicities, source degrees, and quotient dimension.

## 1. VC.1–6: original objects, finite constants, and the target comparison

**VC.1.** For the complete quartet, the summed support consists of points

\[
\zeta_{a,b}=k/2+(2a-k)\delta+i(2b-k)\gamma,
\qquad 0\le a,b\le k.
\]

The positivity of \(\delta\) and \(\gamma\) makes these \((k+1)^2\) points distinct. With the retained local length \(\ell=1+k(m-1)\), the given annihilator has degree \(q=\ell(k+1)^2\). Its root in the original \(u\) chart is

\[
u_{a,b}=(2b-k)\gamma-i(2a-k)\delta,
\qquad |u_{a,b}|^2\le k^2(\gamma^2+\delta^2).
\]

Thus \(\rho=kR_0\) is a valid radius, including every multiplicity. For \(k\ge3\), \(q\ge(k+1)^2\ge16\) and \(q\ge k\).

**VC.2–3.** I checked these definitions and the lower envelope against the supplied `Tau_Arithmetic_Endpoint_Bounds/NOTE.tex`, including its displayed source definition (7), the local-mass and convolution constants in (24)–(29), and exponential moments in (30)–(34). The source has exactly the factor \(1/(2\pi)\); its tensor mass is \(\mu_h^k\). The bound used here is the supplied theorem

\[
m_k(u)\ge c_h\vartheta_h^{k-3}
e^{-\pi(|u|+k-3)/2}(1+|u|+k-3)^{-42-2\deg h}.
\]

In particular \(\alpha=\pi/2\), the exponent of \(\vartheta_h\) is \(k-3\), and the power \(B_h\) is fixed with the packet. The current review checks the exact use of these inherited analytic theorems; it does not claim a new independent proof of every upstream zeta estimate.

**VC.4.** Because \(D\ge2R_0\) and \(q\ge k\),

\[
0\le r=\frac{kR_0}{Dq}\le\frac{k}{2q}\le\frac12.
\]

Also \(D\ge2/b\) gives \(bT=bDq\ge2q\). The constants \(T\), \(\lambda_k(T)\), and the exponential moments are positive, and all quantities in the definition of \(C_{k,q}\) are finite. The denominator \(T\lambda_k(T)\) is exactly the one obtained after the change of variable in VC.31; neither its Jacobian \(T\) nor its lower-envelope factor is missing.

**VC.5.** In coefficient coordinates,

\[
H_j:\mathbb C^{j+1}\to\mathbb C^{j+1},\qquad
J_j:\mathbb C^{j+1}\to\mathbb C^q,
\qquad K_j,G_j:\mathbb C^q\to\mathbb C^q.
\]

The exponential-moment input makes every entry of \(H_j\) finite. The positive density makes \(z^*H_jz>0\) for every nonzero polynomial coefficient vector: a nonzero polynomial has only finitely many zeros on the source line. The identity restriction of remainder on degrees below \(q\) makes \(J_j\) surjective. Hence \(K_j=J_jH_j^{-1}J_j^*\) and \(G_j=K_j^{-1}\) are positive definite, and \(V_j>0\).

**VC.6.** Its two inequalities are the correct kernel order and determinant order for the least-lift metrics. The complete verification of their exponent is given in section 6 below. In particular the matrix size is \(q\), while the larger source space has dimension \(2q\); the determinant exponent is therefore \(q\).

## 2. VC.7–15: exact affine, quotient, jet, and matrix transport

**VC.7–8.** Affine substitution \(P(S)\mapsto P(c+iTx)\) is complex linear and invertible for the stated \(T>0\). The inverse displayed in the note is exact. With \(u=Tx\), the change of measure is \(m_k(u)\,du=T m_k(Tx)\,dx\). This proves the norm equality and preserves total mass \(\mu_h^k\).

**VC.9–12.** The scalar unit is exactly \((iT)^q\). It follows that the image of the original principal ideal is the target principal ideal, and the quotient substitution is an algebra isomorphism. The target remainder is the substituted original remainder because its degree remains below \(q\) and its difference from the substituted polynomial is divisible by the target monic annihilator. This is a complete proof of the commuting remainder identity, with no division by a root difference.

**VC.13.** The repeated chain rule gives the raw-jet multiplier \((iT)^d\) at derivative order \(d\). Keeping Taylor coordinates instead gives the same multiplier and retains the original factorial \(d!\). Root multiplicities determine the full range \(0\le d<\operatorname{ord}_\lambda\chi\), exactly as written.

**VC.14.** In increasing-degree bases the affine coefficient matrix is triangular, with diagonal \((iT)^a\), \(a=0,\ldots,j\). Its determinant is therefore \((iT)^{j(j+1)/2}\). This matrix must carry notation distinct from the scalar coefficient-bound constant \(A_N\); that notation issue was reported and is recorded in the resolution seal.

**VC.15.** Write \(\mathsf A_j\) here for the affine matrix to keep the types explicit. The norm equality and remainder identity give

\[
H_j=\mathsf A_j^*\widetilde H_j\mathsf A_j,
\qquad
\widetilde J_j\mathsf A_j=\mathsf A_{q-1}J_j.
\]

Substituting
\(\widetilde H_j^{-1}=\mathsf A_jH_j^{-1}\mathsf A_j^*\)
and
\(\widetilde J_j=\mathsf A_{q-1}J_j\mathsf A_j^{-1}\)
gives

\[
\widetilde K_j=\mathsf A_{q-1}K_j\mathsf A_{q-1}^*,
\quad
\widetilde G_j=\mathsf A_{q-1}^{-*}G_j\mathsf A_{q-1}^{-1}.
\]

Consequently

\[
\det\widetilde G_j
=|\det\mathsf A_{q-1}|^{-2}V_j
=T^{-q(q-1)}V_j.
\tag{AR.4}
\]

The factor is independent of the source degree \(j\); thus it cancels in the ratio of the two specified volumes. All inverses and congruences have the correct order.

For an additional explicit connection to raw-jet coordinates, let \(\Gamma\) be the \(q\)-by-\(q\) matrix whose row \((\lambda,d)\) and column \(a\), \(0\le a<q\), is

\[
\Gamma_{(\lambda,d),a}=
\begin{cases}a!\lambda^{a-d}/(a-d)!,&a\ge d,\\0,&a<d.\end{cases}
\]

A polynomial in \(\mathcal P_{q-1}\) has zero image under \(\Gamma\) precisely when it is divisible by \(\chi\): Taylor expansion gives each root factor with its multiplicity. Degree then forces the polynomial to vanish, so \(\Gamma\) is invertible. The original raw-jet map in degree \(j\) is exactly \(\Gamma J_j\), because the difference between a polynomial and its remainder is divisible by \(\chi\). Its kernel metric and quotient metric are therefore

\[
K_j^{\rm jet}=\Gamma K_j\Gamma^*,
\qquad G_j^{\rm jet}=\Gamma^{-*}G_j\Gamma^{-1},
\qquad V_j^{\rm jet}=|\det\Gamma|^{-2}V_j.
\tag{AR.5}
\]

This proves directly that the scalar comparator controls the same degree-to-degree volume ratio in raw-jet coordinates. The original derivative and multiplicity data remain in \(\Gamma\), and the phase transport remains the diagonal map in VC.13.

**Final added VC.15a–15b.** I read both additions and their complete surrounding proof in the final comparator. Its matrix \(E\) is exactly the matrix denoted \(\Gamma\) in this review. The derivative entries retain the factorial \(j!/(j-a)!\), the zero entries have the correct range \(j<a\), and the Taylor-divisibility argument proves invertibility at every retained root length. The identity \(F_j=EJ_j\) and all three congruence/determinant formulas therefore agree with (AR.5). The final added conclusion that the constant and the degree-to-degree determinant ratio are preserved is proved by the degree independence of \(E\).

## 3. VC.16–21: the complete Legendre estimate

**VC.16–18.** The coefficient estimate uses Lebesgue measure \(dx\) on \([-1,1]\). Rodrigues' formula has denominator \(2^jj!\), leading coefficient \((2j)!/[2^j(j!)^2]\), and all required endpoint terms vanish on repeated integration by parts. The intermediate integral is

\[
\int_{-1}^1(1-x^2)^j\,dx
=\frac{2^{2j+1}(j!)^2}{(2j+1)!}.
\]

Multiplication by the displayed leading coefficient divided by \(2^j\) gives exactly \(2/(2j+1)\). The elementary integration-by-parts derivation of the beta integral in the text covers all nonnegative integers, including \(j=0\).

**VC.19–20.** Leibniz's rule gives the stated finite sum with coefficients \(2^{-j}\binom ja^2\). Each product \((x-1)^{j-a}(x+1)^a\) has coefficient norm at most \(2^j\). The outer \(2^{-j}\) cancels this bound, leaving \(\sum_a\binom ja^2=\binom{2j}{j}\le4^j\). All inequalities hold for the coefficient \(\ell^1\) norm as defined.

**VC.21.** The expansion coefficient of \(L_j\) is
\((2j+1)\int L_jf/2\). Since \(L_j\) is real, Cauchy–Schwarz applies to complex \(f\) with the same formula for its modulus. It gives \(\sqrt{(2j+1)/2}\|f\|_2\). Summing the coefficient norms over \(0\le j\le N\) gives exactly

\[
A_N=\sqrt{\frac{2N+1}{2}}\frac{4^{N+1}-1}{3}.
\]

Thus VC.16 is established with its full constant and the original degree \(N=2q-1\).

## 4. VC.22–27: the radius-sensitive monic-division estimate

**VC.22–24.** The product of the elementary and complete homogeneous series is one in the formal power-series ring. Its coefficients in positive degrees through \(s\) vanish. Accordingly \(\chi_TQ_s\) has leading monomial \(x^{q+s}\), and its next \(s\) coefficients vanish down through degree \(q\). The remainder formula in VC.24 follows by monic division. When \(s=0\), the list of intermediate coefficients is empty, and the same assertion remains valid.

**VC.23.** The elementary bound counts the \(a\)-element subsets of a \(q\)-element list. The complete homogeneous bound counts weak compositions of \(j\) into \(q\) parts. Both retain the repeated-root list, so multiplicities require no separate limiting argument.

**VC.25.** The identity

\[
\|\operatorname{rem}_{\chi_T}x^{q+s}\|_1
=\|\chi_TQ_s\|_1-1
\]

is exact because the leading coefficient is one and all other surviving degrees are below \(q\). The product norm bound then gives

\[
\|\operatorname{rem}_{\chi_T}x^{q+s}\|_1
\le(1+r)^q\sum_{j=0}^{s}\binom{q+j-1}{j}r^j-1.
\]

For \(0\le r<1\), the infinite positive series equals \((1-r)^{-q}\), as follows by multiplying \(q\) convergent geometric series. Thus the last expression is at most \(((1+r)/(1-r))^q-1\), which is in turn at most the stated \(B_q(r)\). The estimate therefore has ample room at the high-degree columns; the low-degree identity columns require the bound by at least one.

**VC.26–27.** For degrees below \(q\), the column norm is exactly one. Since \(B_q(r)\ge1\), combining all columns using linearity yields the stated operator bound. Keeping the finite sum instead gives exactly the optional maximum in VC.27. The endpoint \(r=0\) also checks: \(\chi_T=x^q\), the higher-degree remainder columns vanish, and the full operator norm is one.

## 5. VC.28–32: moments, Jacobian, and the scalar operator bound

**VC.28.** Selecting the \(2a\)-th term from the nonnegative Taylor series of \(e^{b|u|}\) proves the first inequality; \(e^{b|u|}\le e^{bu}+e^{-bu}\) proves the second. The factorial is exactly \((2a)!\).

**VC.29.** The convolution pushforward of the product measure and Tonelli's theorem give the two exponential moments \(M_h(\pm b)^k\) and the total mass \(\mu_h^k\), with every factor retained.

**VC.30.** For a degree-\((q-1)\) polynomial,

\[
|v(x)|^2\le\|v\|_1^2\max\{1,|x|^{2q-2}\}.
\]

The maximum is bounded by \(1+|x|^{2q-2}\). Integrating at \(x=u/T\) gives precisely

\[
U_k(T)=\mu_h^k+
\frac{(2q-2)!}{(bT)^{2q-2}}
\bigl(M_h(b)^k+M_h(-b)^k\bigr).
\]

**VC.31.** For \(|u|\le T\), both decreasing factors of the lower envelope in VC.3 are at least their values at \(T\), because \(B_h>0\). Thus \(m_k(u)\ge\lambda_k(T)\) there. Restricting the original norm to this interval and setting \(u=Tx\) gives exactly \(T\lambda_k(T)\|\Psi_TP\|_2^2\).

**VC.32.** Apply VC.30 to the target remainder, then VC.26 to its coefficient norm, then VC.16 to the original target polynomial, and finally VC.31. The resulting squared operator constant is exactly (AR.2): one factor \(U_k(T)\), one factor \(A_N^2\), one factor \(B_q(r)^2\), and the denominator \(T\lambda_k(T)\).

The exact type identification in the final prose is as follows. Let \(\iota_j:\mathbb C^{j+1}\to\mathcal P_j\) send a coefficient vector to its polynomial, and let \(\kappa:\mathbb C[S]/(\chi)\to\mathbb C^q\) send a quotient class to the coefficient vector of its unique degree-below-\(q\) representative. Define \(\mathcal J_j=J_j\iota_j^{-1}\), and let \(s:\mathbb C^q\to\mathcal P_{q-1}\) send \(y\) to \(\sum_{a=0}^{q-1}y_aS^a\). Then \(\mathcal J_j\) is \(\kappa\) composed with the abstract quotient map restricted to \(\mathcal P_j\), \(\mathcal J_{q-1}s=I_{\mathbb C^q}\), and the estimated operator is exactly \(s\mathcal J_N\). Also \(\pi s=\kappa^{-1}\) for the abstract quotient map \(\pi\). Its induced section bound follows by minimizing the norm over lifts, as carried out in VC.35. I read all these final definitions and identities and checked their domains and codomains. This typing removes the original ambiguity without changing any inequality.

As a useful consistency check derived from the proof itself, choose any nonzero \(P\) of degree below \(q\). The remainder is \(P\), and its degree-\((q-1)\) and degree-\(N\) source norms are equal. VC.32 therefore implies \(1\le C_{k,q}\) directly.

## 6. VC.33–35: least lifts, positive-matrix order, and the exponent \(q\)

**VC.33.** The matrix
\(R_j=H_j^{-1}J_j^*K_j^{-1}\)
has type \(\mathbb C^q\to\mathbb C^{j+1}\). Direct multiplication gives \(J_jR_j=I\). For any \(z\in\ker J_j\), \(z^*H_jR_j=0\).

**VC.34.** Every lift of \(y\) is uniquely \(R_jy+z\), \(z\in\ker J_j\). The vanishing cross term and
\(R_j^*H_jR_j=K_j^{-1}\)
give exactly the stated Pythagorean identity. The minimum lift norm is \(y^*G_jy\).

**VC.35.** Degree inclusion preserves the original polynomial norm and enlarges the lift set, giving \(G_{j+1}\preceq G_j\). Inserting the least degree-\(N\) lift in VC.32 gives

\[
y^*G_qy\le y^*G_{q-1}y
\le\|\operatorname{rem}_\chi R_Ny\|_{H_{q-1}}^2
\le C_{k,q}y^*G_Ny.
\]

The middle inequality is in fact equality in the present coefficient coordinates, since \(J_{q-1}=I\) and the remainder coefficients are \(y\); the written weaker inequality is correct. Together with monotonicity this yields

\[
C_{k,q}^{-1}G_q\preceq G_N\preceq G_q.
\]

Set \(Z=G_q^{-1/2}G_NG_q^{-1/2}\). Every eigenvalue of the positive \(q\)-by-\(q\) matrix \(Z\) lies in \([C_{k,q}^{-1},1]\). Hence every eigenvalue of \(Z^{-1}\) lies in \([1,C_{k,q}]\). Congruencing back gives

\[
K_q\preceq K_N\preceq C_{k,q}K_q.
\]

Moreover

\[
1\le\frac{V_q}{V_N}=\frac{1}{\det Z}
\le C_{k,q}^{q}.
\tag{AR.6}
\]

Taking logarithms proves VC.6 with exponent exactly \(q\). No commutativity of the original matrices was used.

## 7. VC.36–43: complete constants and asymptotic coefficient

**VC.36–37.** Put \(E_k=M_h(b)^k+M_h(-b)^k\). The identity

\[
E_k=\int 2\cosh(bu)m_k(u)\,du\ge2\mu_h^k
\]

is valid for asymmetric densities as well. Since \(bT\ge2q\), each factor in \((2q-2)!/(bT)^{2q-2}\) is at most one, so
\(U_k\le\mu_h^k+E_k\le3E_k/2\le3X^k\).

**VC.38.** With \(N=2q-1\), the exact square of the Legendre coefficient constant is

\[
A_{2q-1}^2=\frac{4q-1}{18}(16^q-1)^2
\le\frac{2q}{9}256^q.
\tag{AR.7}
\]

Also \(\vartheta_h^{-(k-3)}\le K^k\): if \(\vartheta_h\ge1\), the left side is at most one; if \(0<\vartheta_h<1\), the power \(k-3\) is at most \(k\).

**VC.39.** The derivative of \(g(t)=\log((1+t)/(1-t))\) is
\(g'(t)=2/(1-t^2)\le8/3\) on \([0,1/2]\), and \(g(0)=0\). Therefore

\[
\log B_q(r)^2=2qg(r)
\le\frac{16}{3}qr
=\frac{16R_0}{3D}k.
\]

The square on \(B_q\) contributes the factor two. This is the stated logarithmic cost of order \(k\); it does not produce a new term proportional to \(q\) in \(\log C_{k,q}\).

**VC.40.** Before taking logarithms, inserting the verified bounds in the exact constant gives

\[
C_{k,q}\le
\frac{2}{3c_hD}(XK)^k256^q
\exp\left(\alpha Dq+\alpha(k-3)+\frac{16R_0}{3D}k\right)
(1+Dq+k-3)^{B_h}.
\tag{AR.8}
\]

The prefactor is obtained from \(3\cdot(2q/9)/(Dq c_h)\); the source-degree factor \(q\) cancels against \(T=Dq\) at precisely this step. Replacing \(2/(3c_hD)\) by its maximum with one, bounding \(e^{-3\alpha}\le1\), and using
\(1+Dq+k-3\le1+(D+1)q\)
gives exactly VC.40. Its coefficient of \(q\) is therefore

\[
\boxed{\alpha D+\log256.}
\]

The envelope prefactor must have notation distinct from the already defined scalar \(A_0=1/\sqrt2\) obtained by putting degree zero in the Legendre formula. This is a notation correction only, recorded in the final seal.

**VC.41.** Multiplying the complete upper bound on \(\log C_{k,q}\) by the determinant exponent \(q\) gives exactly the four terms in VC.41: respectively \(q^2\), \(kq\), \(q\log(1+(D+1)q)\), and \(q\) times the logarithm of the fixed prefactor.

**VC.42.** For fixed \(m\), \(q_k=[1+k(m-1)](k+1)^2\). Hence \(k/q_k\to0\), \(\log q_k/q_k\to0\), and \(1/q_k\to0\). Dividing VC.41 by \(q_k^2\) makes each of its last three terms tend to zero, leaving (AR.3). Every constant in that limit is fixed with the packet and \(b\).

**VC.43 and the following comparison.** I read the complete owner's `FOUR_VOLUME_THRESHOLD.md`. Its equation (7) is exactly the lower estimate quoted as VC.43, with source window \(n=q,r=q-1\), original degrees \(q\) and \(2q-1\), and the constant \(C_h^{\rm bal}\). In particular the factor \(2(q-1)\) is retained.

On dividing the upper envelope by \(q\log k\), its leading term is \((\alpha D+\log256)q/\log k\). For \(m=1\), \(q/k^2\to1\); for \(m>1\), \(q/k^3\to m-1\). Thus both asymptotic expressions in the text have the correct coefficient. The lower estimate has limiting coefficient at least two at scale \(q\log k\), whereas the explicit scalar upper envelope grows faster at that scale. This comparison supplies no contradictory upper bound for the original quartet. The exact links to the original quotient and to raw-jet coordinates are (AR.4)–(AR.6).

## 8. Source pins and resolution seal

- Supplied arithmetic analytic input: `Tau_Arithmetic_Endpoint_Bounds/NOTE.tex`, SHA-256 `f776e7934f026342f48732a74f14d57470b8aae1cef76ebdee5f831bd49dedf8`. Read scope for this audit is the explicitly identified definitions and analytic-input passages above.
- Owner's complete lower-bound continuation: `FOUR_VOLUME_THRESHOLD.md`, SHA-256 `9ff55c84d74db85306e7a68c70fe7b08d8e642e8ac1a3e6137649f68e102fc3a`. The complete file was read.
- Independent finite-division proof used as a cross-check: `volume_remainder_bound_review_20260913.md`, SHA-256 `56bee5eba5f951570428939169f69020a5c2b71c2ffc5ceaa18d26a2fe43049d`. The radius-sensitive infinite-series estimate in VC.25–26 was additionally verified directly above.
- Final comparator: `volume_comparator_review_20260913.md`, SHA-256 `47ac2b43904ec43f3ce19d7c74ba760a29ce4d7a3e411132fe81ec0b27af6104`. The complete final file was read, including VC.15a–15b.

The findings and their verified resolutions are:

1. Nine displayed squared quantities originally carried the serialization `^{,2}`. The final file uses `^{2}` in those positions, with unchanged mathematical values.
2. The prose following VC.32 originally called the estimated remainder operator a right inverse. The final paragraph gives the actual coefficient, polynomial, abstract quotient, and section maps \(\iota_j\), \(\kappa\), \(\mathcal J_j\), and \(s\), and identifies the estimated composition \(s\mathcal J_N\) exactly.
3. The affine coefficient matrix originally shared the notation \(A_j\) with the scalar Legendre constant. The final matrix notation is \(\mathsf A_j\) throughout its definition, determinant, congruences, and inverse congruence. The scalar \(A_N\) remains unchanged.
4. The envelope prefactor originally reused \(A_0\). It is now \(C_0=\max\{1,2/(3c_hD)\}\) in VC.36 and in both subsequent logarithmic bounds, so it is distinct from the scalar Legendre constants.
5. The final additions VC.15a–15b explicitly prove the raw-jet/remainder congruence and its degree-independent determinant multiplier. Their complete formulas and proofs were independently read and agree with (AR.5).

All five items are resolved in the sealed final version. The changes preserve the numerical constant in VC.4, the inequalities in VC.6, the logarithmic remainder estimate in VC.39, and the leading coefficient in VC.40–42.

This review contains written verification of all VC.1–43 claims within their stated provenance. It adds no numerical enclosure of the inherited source constants, reports no Lean result, and makes no claim to have executed the comparator's tests.
