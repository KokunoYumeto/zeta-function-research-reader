# Independent review of the Gaussian arithmetic boundary return

Mathematical verification, 2026-09-23.

## GABR1. Source, actual reading, and scope

The source reviewed is [Gaussian arithmetic boundary return](GAUSSIAN_ARITHMETIC_BOUNDARY_RETURN.md), SHA-256

DB4B2E894DCE8DDB3564CE449A7CA6F0DE5DF9DE139F0099F27271FBA5D4B31B.

Its entire text, sections GAB1–19 and displayed formulas GAB1–49, was read. The independent derivation below verifies the Mellin–Barnes collision terms, the separated meromorphic pole data, the exact parameter-shift equation, the return of every local zero with its multiplicity and original local unit, and the finite signed-measure realization. The source's GAB10–22, GAB25–31, and GAB46–49 are the principal receiving formulas. The full receiver prefactors in GAB32–40 were also checked against these calculations.

The first complete reading used the actual file-byte version with SHA-256 BC74059DD1E51693DD88DE1444C9644380E1FD8A3AC4F4E6EF49718E4471F690, obtained with Get-FileHash. An intermediate version, BAE9486E35CD32E554621B50AF7A3FD1907F9E2B576C78A68CB6F45A7C431729, changed only “entire subtracted function” to “complete subtracted meromorphic function” in the paragraph following GAB18. The amended paragraph and its neighboring formula were reread. Reversing that one byte-string replacement in the intermediate version reproduced exactly the predecessor byte hash BC74059DD1E51693DD88DE1444C9644380E1FD8A3AC4F4E6EF49718E4471F690. The amendment correctly describes the poles already retained in GAB21 and in GABR20 below; no mathematical formula changed in that step. The final version identified above adds section GAB18, formulas GAB46–49, and a corresponding seventh conclusion, moving the conclusions to section GAB19. The entire added section and revised conclusions were read. Its measure calculation is independently proved in GABR9 below.

The collision, residue, shift, and local-zero calculations were first derived independently before reading the source. This review did not independently reread the upstream MRT manuscript or the Connes paper. Reading their citations in the reviewed source is not recorded as reading those works. No external novelty claim, positivity theorem, or critical-line theorem is made here.

Retain the parameter dictionary
\[
 T>0,\qquad d=\frac1{4\pi T},\qquad
 \lambda=\pi d=\frac1{4T}>0.
 \tag{GABR1}
\]
The function under review is exactly
\[
 Z_\lambda(s)=\sum_{n=1}^{\infty}e^{-\lambda n^2}n^{-s}
             =Z_d(s)\quad(\lambda=\pi d).
 \tag{GABR2}
\]
The second notation on the right is the notation of the reviewed source. The logarithm of positive \(\lambda\) is real. Complex-parameter statements use \(\Re\lambda>0\) and \(-\pi/2<\arg\lambda<\pi/2\).

## GABR2. The uniform original-zeta expansion needed in the root argument

For fixed \(\Re\lambda>0\), the series in GABR2 and its \(s\)-derivatives converge normally on compact \(s\)-sets: if \(\Re s\ge-A\), the \(r\)-th derivative is bounded by
\[
 \sum_{n\ge1} e^{-(\Re\lambda)n^2}n^A(\log n)^r<\infty.
\]
Thus \(Z_\lambda\) is entire in \(s\). Its derivative with respect to \(\lambda\) can also be taken term by term for \(\lambda\) in compact subsets of that half-plane.

For
\[
 c>\max\left(0,\frac{1-\Re s}{2}\right),
\]
Mellin inversion of the Euler Gamma integral gives
\[
 Z_\lambda(s)=\frac1{2\pi i}
 \int_{c-i\infty}^{c+i\infty}
       \Gamma(z)\lambda^{-z}\zeta(s+2z)\,dz.
 \tag{GABR3}
\]
The interchange follows by summing \(n^{-\Re s-2c}\), whose exponent is greater than one. The Gamma bound needed for its absolute convergence follows by rotating its Euler-integral ray: for \(a>0\) and \(0<\omega<\pi/2\),
\[
 |\Gamma(a+it)|\le
 \Gamma(a)(\cos\omega)^{-a}e^{-\omega|t|}.
 \tag{GABR4}
\]
The small ray-closing arc vanishes because \(a>0\), and the large arc vanishes because its real part is at least \(r\cos\omega\). The full recurrence
\[
 \Gamma(z)=\frac{\Gamma(z+J)}
                   {z(z+1)\cdots(z+J-1)}
\]
extends the bound, with a polynomial factor, to each fixed finite real strip away from the Gamma poles.

For completeness, original zeta has the necessary polynomial vertical bound without use of a completed replacement. Set \(P_1(x)=\{x\}-1/2\), and let \(P_{r+1}\) be its successive bounded, one-periodic, mean-zero primitives. The counting integral and repeated integration by parts give
\[
 \zeta(w)=\frac12+\frac1{w-1}
 +\sum_{r=2}^{M}(w)_{r-1}P_r(1)
 -(w)_M\int_1^\infty P_M(x)x^{-w-M}\,dx,
 \tag{GABR5}
\]
where \((w)_j=w(w+1)\cdots(w+j-1)\). The last integral converges for \(\Re w>1-M\). Its absolute value is at most
\[
 \frac{\|P_M\|_\infty}{\Re w+M-1}.
\]
Consequently GABR5 gives a polynomial bound on every closed vertical strip strictly in that half-plane, away from \(w=1\). Increasing \(M\) covers every finite real strip. This also checks the signs and indices of the source's Euler-summation formula.

Fix \(N\ge0\), \(0<\alpha<1\), and a compact set
\[
 K\subset\{s:\Re s<1+2(N+\alpha)\}.
\]
Move the contour in GABR3 to \(\Re z=-N-\alpha\). The moving zeta pole is \(z=(1-s)/2\), with residue \(1/2\) in the variable \(z\). The other crossed poles are \(z=0,-1,\ldots,-N\). Off the positive odd points, this gives the exact equality
\[
 Z_\lambda(s)=
 \frac12\Gamma\!\left(\frac{1-s}{2}\right)
              \lambda^{(s-1)/2}
 +\sum_{k=0}^{N}\frac{(-\lambda)^k}{k!}\zeta(s-2k)
 +R_{N,\alpha}(\lambda,s),
 \tag{GABR6}
\]
\[
 R_{N,\alpha}(\lambda,s)=\frac1{2\pi i}
 \int_{-N-\alpha-i\infty}^{-N-\alpha+i\infty}
       \Gamma(z)\lambda^{-z}\zeta(s+2z)\,dz.
 \tag{GABR7}
\]
The strict bound on \(\Re s\) keeps the moving zeta pole to the right of the new line. On every fixed sector
\[
 0<|\lambda|\le1,\qquad
 |\arg\lambda|\le\frac\pi2-\eta,\qquad \eta>0,
\]
choose \(\omega=\pi/2-\eta/2\) in GABR4. Gamma decay dominates both the polynomial bound in GABR5 and \(e^{(\Im z)\arg\lambda}\). The horizontal contour integrals therefore vanish, and the left contour has the bound
\[
 \sup_{s\in K}|R_{N,\alpha}(\lambda,s)|
 \le C_{K,N,\alpha,\eta}|\lambda|^{N+\alpha}.
 \tag{GABR8}
\]
The same bounds give holomorphy in \(s\) of GABR7 on the stated strict half-plane.

Define
\[
 S_\lambda(s)=
 \frac12\Gamma\!\left(\frac{1-s}{2}\right)
                   \lambda^{(s-1)/2},\qquad
 Y_\lambda(s)=Z_\lambda(s)-S_\lambda(s).
 \tag{GABR9}
\]
On any compact set avoiding the positive odd integers, choose \(N\ge2\) sufficiently large for GABR6. The higher finite terms are bounded there. Hence the proved compact-uniform expansion is
\[
 Y_\lambda(s)=\zeta(s)-\lambda\zeta(s-2)+O(|\lambda|^2).
 \tag{GABR10}
\]
On a compact subset of the open critical strip, \(N=2\) already suffices; in that case the fully retained formula is
\[
 Y_\lambda(s)=\zeta(s)-\lambda\zeta(s-2)
             +\frac{\lambda^2}{2}\zeta(s-4)
             +R_{2,\alpha}(\lambda,s).
 \tag{GABR11}
\]
Thus the estimate used in the local-zero argument is proved, rather than assumed as an extra hypothesis. The finite expansion and its contour remainder do not assert convergence of an infinite series in \(\lambda\).

## GABR3. Full Laurent calculation at every colliding pole

Fix \(j\ge0\), put \(s_j=1+2j\), and set \(z=-j+h\). Let \(H_0=0\) and \(H_j=\sum_{r=1}^{j}1/r\). The three local factors are
\[
 \Gamma(-j+h)=\frac{(-1)^j}{j!}
       \left(\frac1h+H_j-\gamma+O(h)\right),
 \tag{GABR12}
\]
\[
 \zeta(s_j+2z)=\zeta(1+2h)
                =\frac1{2h}+\gamma+O(h),
 \tag{GABR13}
\]
\[
 \lambda^{-z}=\lambda^j
       \left(1-h\log\lambda+O(h^2)\right).
 \tag{GABR14}
\]
For GABR12, retain the recurrence explicitly:
\[
 \Gamma(-j+h)=
 \frac{\Gamma(1+h)}{h\prod_{r=1}^{j}(h-r)}
 =\frac{(-1)^j}{j!h}
   (1-\gamma h+O(h^2))
   \prod_{r=1}^{j}(1-h/r)^{-1}.
\]
The finite product contributes \(1+H_jh+O(h^2)\). The \(j=0\) case uses the empty product. GABR13 follows from the residue-one Laurent expansion of original zeta, whose constant term is the harmonic-sum limit \(\gamma\). Thus the two appearances of Euler's constant arise from different factors with the indicated signs.

Multiplying all three factors, before taking the residue, gives
\[
 \Gamma(-j+h)\lambda^{j-h}\zeta(1+2h)
 =\frac{(-\lambda)^j}{j!}
 \left[
   \frac1{2h^2}
   +\frac{\gamma+(H_j-\gamma)/2-(\log\lambda)/2}{h}
   +O(1)
 \right].
 \tag{GABR15}
\]
The double-pole coefficient is \((- \lambda)^j/(2j!)\), and its residue is
\[
 \boxed{\frac{(-\lambda)^j}{2j!}
                 \bigl(H_j+\gamma-\log\lambda\bigr).}
 \tag{GABR16}
\]
Therefore, for \(N\ge j\), the complete collision expansion is
\[
 Z_\lambda(1+2j)=
 \sum_{\substack{0\le k\le N\\k\ne j}}
       \frac{(-\lambda)^k}{k!}\zeta(1+2j-2k)
 +\frac{(-\lambda)^j}{2j!}
       (H_j+\gamma-\log\lambda)
 +R_{N,\alpha}(\lambda,1+2j).
 \tag{GABR17}
\]
The remainder is exactly GABR7 and has the same bound GABR8.

There is a second check directly in the variable \(s\). Write \(s=s_j+\delta\). The two separated terms have expansions
\[
 S_\lambda(s_j+\delta)
 =\frac{(-\lambda)^j}{j!}
   \left[-\frac1\delta
        +\frac{H_j-\gamma-\log\lambda}{2}
        +O(\delta)\right],
 \tag{GABR18}
\]
\[
 \frac{(-\lambda)^j}{j!}\zeta(s_j+\delta-2j)
 =\frac{(-\lambda)^j}{j!}
       \left[\frac1\delta+\gamma+O(\delta)\right].
 \tag{GABR19}
\]
Their sum has a removable singularity, with value GABR16. Neither of the separated summands is finite there.

## GABR4. The global pole tower and the exact retained map

For each fixed \(\lambda>0\), \(S_\lambda\) is meromorphic on the whole \(s\)-plane. Its only poles are the positive odd integers. Equations GABR18 and GABR2 give
\[
 \operatorname{Res}_{s=1+2j}S_\lambda(s)
       =-\frac{(-\lambda)^j}{j!},\qquad
 \operatorname{Res}_{s=1+2j}Y_\lambda(s)
       =\frac{(-\lambda)^j}{j!}.
 \tag{GABR20}
\]
Every displayed residue is nonzero for fixed \(\lambda>0\), so every listed pole is present and simple. At \(s=1\), the residue of \(Y_\lambda\) is one. At \(s=3,5,\ldots\), its further residues tend to zero as \(\lambda\downarrow0\), but the poles remain present for each positive parameter.

Let \(\mathcal M(\mathbb C)\) denote the field of meromorphic functions on the \(s\)-plane. The precise comparison is the automorphism
\[
 \mathcal T:\mathcal M(\mathbb C)^2\longrightarrow
                \mathcal M(\mathbb C)^2,\qquad
 \mathcal T(F,G)=(F-G,G),
 \tag{GABR21}
\]
\[
 \mathcal T^{-1}(U,G)=(U+G,G).
 \tag{GABR22}
\]
Applied to \((Z_\lambda,S_\lambda)\), it gives
\((Y_\lambda,S_\lambda)\). The second coordinate remains in the object. Its inverse restores the cancellation in GABR18–19 and returns the entire function \(Z_\lambda\). This automorphism does not equate the divisor of \(Z_\lambda\) with the divisor of \(Y_\lambda\).

## GABR5. Exact dynamics, including the principal parts

Termwise differentiation of the normally convergent Gaussian series gives
\[
 \partial_\lambda Z_\lambda(s)
   =-\sum_{n\ge1}e^{-\lambda n^2}n^{2-s}
   =-Z_\lambda(s-2).
 \tag{GABR23}
\]
The complete sector has the same equation:
\[
 \begin{aligned}
 \partial_\lambda S_\lambda(s)
 &=\frac{s-1}{4}
       \Gamma((1-s)/2)\lambda^{(s-3)/2}\\
 &=-\frac12\Gamma((3-s)/2)\lambda^{(s-3)/2}\\
 &=-S_\lambda(s-2).
 \end{aligned}
 \tag{GABR24}
\]
The middle equality uses
\(\Gamma((3-s)/2)=((1-s)/2)\Gamma((1-s)/2)\), with its sign retained. Subtracting proves
\[
 \boxed{\partial_\lambda Y_\lambda(s)=-Y_\lambda(s-2).}
 \tag{GABR25}
\]
These are meromorphic identities in \(s\). At \(s=1\), the left principal part has zero derivative since the residue is constantly one, and the right side has no pole there. At \(s=1+2j\), \(j\ge1\), the left residue is
\[
 \partial_\lambda\frac{(-\lambda)^j}{j!}
       =\frac{(-1)^j\lambda^{j-1}}{(j-1)!},
\]
and the right residue is
\[
 -\frac{(-\lambda)^{j-1}}{(j-1)!}
       =\frac{(-1)^j\lambda^{j-1}}{(j-1)!}.
\]
Thus the pole tower also satisfies the equation exactly. In the original parameter \(d\), GABR1 gives
\[
 \partial_dY_d(s)=-\pi Y_d(s-2).
 \tag{GABR26}
\]
This is the dynamics induced by the integer coefficient \(e^{-\pi d n^2}\).

## GABR6. Shifted nonvanishing at each nontrivial zero

Let \(\rho\) be any nontrivial zero of original zeta, with
\[
 0<\Re\rho<1.
\]
The full reflection identity, as derived from theta and its separate endpoints in source GAB23–24, is
\[
 \zeta(w)=\pi^{w-1/2}
          \frac{\Gamma((1-w)/2)}{\Gamma(w/2)}
          \zeta(1-w).
 \tag{GABR27}
\]
At \(w=\rho-2\), every factor has an explicit nonzero value:
\[
 \zeta(\rho-2)
 =\pi^{\rho-5/2}
   \frac{\Gamma((3-\rho)/2)}{\Gamma((\rho-2)/2)}
   \zeta(3-\rho)\ne0.
 \tag{GABR28}
\]
Indeed \(-1<\Re((\rho-2)/2)<-1/2\), so the denominator Gamma factor is finite and nonzero. The numerator argument has real part between one and \(3/2\), so it is also finite and nonzero. The power of \(\pi\) is nonzero. Finally \(\Re(3-\rho)>2\), where the absolutely convergent Euler product of original zeta is nonzero. No claim of simple zeros or of \(\Re\rho=1/2\) enters this proof.

Gamma's nonvanishing and its poles are, for example, read directly from the reciprocal product
\[
 \Gamma(z)^{-1}
 =ze^{\gamma z}\prod_{n\ge1}(1+z/n)e^{-z/n}.
\]
Away from the indicated zeros, the logarithmic tails are \(O(n^{-2})\), so normal convergence gives no further zeros of the product. This is the same Gamma fact used in the source, with no lost factor in GABR28.

## GABR7. Rouché proof of the complete local zero return

Let the multiplicity of \(\rho\) be \(m\ge1\). Choose \(r>0\) so that the closed disc \(|s-\rho|\le r\) lies in \(0<\Re s<1\), contains no other zero of zeta, and has no zeta zero on its boundary. Retain the original factorization
\[
 \zeta(s)=(s-\rho)^m u(s),\qquad
 u(\rho)=\frac{\zeta^{(m)}(\rho)}{m!}\ne0.
 \tag{GABR29}
\]
The function \(u\) is holomorphic and nonzero on a sufficiently small such disc; its value is not replaced by one.

Set \(\mu=\lambda^{1/m}>0\). Equations GABR10–11, uniformly for bounded complex \(w\), give
\[
 \begin{aligned}
 F_\lambda(w)
 &:=\frac{Y_\lambda(\rho+\mu w)}{\lambda}\\
 &=w^m u(\rho+\mu w)-\zeta(\rho+\mu w-2)+O(\lambda)\\
 &=u(\rho)w^m-\zeta(\rho-2)+O(\mu).
 \end{aligned}
 \tag{GABR30}
\]
The last estimate follows from Taylor estimates on fixed compact discs, and from \(\lambda\le\mu\) for \(0<\lambda\le1\) and \(m\ge1\). It is uniform on each bounded \(w\)-set.

The polynomial
\[
 P(w)=u(\rho)w^m-\zeta(\rho-2)
 \tag{GABR31}
\]
has exactly \(m\) distinct, nonzero roots \(\omega_1,\ldots,\omega_m\), because GABR28 and GABR29 show that both coefficients are nonzero. Their full equation is
\[
 \omega_j^m=\frac{\zeta(\rho-2)}{u(\rho)}.
 \tag{GABR32}
\]
Choose disjoint closed discs \(D_j\) about these roots, containing no other root of \(P\). The minimum of \(|P|\) on the union of their boundaries is positive. By GABR30, for small enough positive \(\lambda\), \(|F_\lambda-P|<|P|\) on each boundary. Rouché's theorem gives exactly one zero counted with multiplicity in each \(D_j\). Therefore this zero \(w_j(\lambda)\) is simple.

To obtain the stated error rather than only convergence, make the discs smaller if necessary. On each disc,
\[
 P(w)=(w-\omega_j)V_j(w),\qquad
 \min_{w\in D_j}|V_j(w)|=c_j>0,
\]
because the other polynomial roots lie outside that disc. At the root of \(F_\lambda\), GABR30 gives
\[
 |P(w_j(\lambda))|\le C_j\mu.
\]
Consequently
\[
 |w_j(\lambda)-\omega_j|
       \le C_j\mu/c_j.
 \tag{GABR33}
\]
Returning to \(s=\rho+\mu w\) proves
\[
 \boxed{
 s_j(\lambda)=\rho+\lambda^{1/m}\omega_j
                  +O(\lambda^{2/m}),\qquad j=1,\ldots,m.
 }
 \tag{GABR34}
\]
In the original parameter this is
\[
 s_j(d)=\rho+(\pi d)^{1/m}\omega_j
                  +O((\pi d)^{2/m}).
 \tag{GABR35}
\]
There are no further returning zeros in the chosen fixed \(s\)-disc: GABR10 gives \(Y_\lambda\to\zeta\) uniformly on its boundary, so a second application of Rouché gives exactly \(m\) zeros there, counted with multiplicity. The zeros already obtained from the \(D_j\) lie in that disc for small \(\lambda\) and exhaust this count.

For \(m=1\), this specializes, with its full original unit, to
\[
 s(\lambda)=\rho+
      \lambda\frac{\zeta(\rho-2)}{\zeta'(\rho)}
      +O(\lambda^2).
 \tag{GABR36}
\]
This proof uses sectorial or positive-parameter asymptotics. It does not assert a holomorphic extension of \(Y_\lambda\) through \(\lambda=0\), and it does not require an implicit-function theorem at that boundary point.

## GABR8. Raw zeros, full moment factors, and exact scope

At the original zero itself, GABR10 and GABR28 give
\[
 Y_\lambda(\rho)=-\lambda\zeta(\rho-2)+O(\lambda^2),
 \qquad
 \frac{Y_\lambda(\rho)}{\lambda}\longrightarrow
                 -\zeta(\rho-2)\ne0.
 \tag{GABR37}
\]
By contrast, the raw function has
\[
 Z_\lambda(\rho)
 =\frac12\Gamma((1-\rho)/2)\lambda^{(\rho-1)/2}
        -\lambda\zeta(\rho-2)+O(\lambda^2).
 \tag{GABR38}
\]
The modulus of its first term tends to infinity, because the Gamma coefficient is nonzero and \((\Re\rho-1)/2<0\). More generally, on a compact set \(K\) inside the open critical strip,
\[
 |S_\lambda(s)|
 \ge c_K\lambda^{(\sup_K\Re s-1)/2}\longrightarrow\infty,
\]
while \(Y_\lambda\) is uniformly bounded there by GABR10. Thus \(Z_\lambda\) has no zeros on \(K\) for all sufficiently small positive \(\lambda\). GABR34 describes zeros of the retained coordinate \(Y_\lambda\), not raw zeros of \(Z_\lambda\).

For the source's actual first Mellin moment, retain every factor:
\[
 I_d(s)=2\sqrt d\,\pi^{-s/2}\Gamma(s/2)Z_d(s).
 \tag{GABR39}
\]
Its sector image is
\[
 \begin{aligned}
 \mathcal S_d(s)
 &=2\sqrt d\,\pi^{-s/2}\Gamma(s/2)
      \frac12\Gamma((1-s)/2)(\pi d)^{(s-1)/2}\\
 &=\pi^{-1/2}\Gamma(s/2)\Gamma((1-s)/2)d^{s/2}.
 \end{aligned}
 \tag{GABR40}
\]
On \(0<\Re s<1\), for each \(d>0\), the multiplier
\(2\sqrt d\,\pi^{-s/2}\Gamma(s/2)\) is holomorphic and nonzero. Its exact inverse is its reciprocal. Therefore
\[
 I_d(s)-\mathcal S_d(s)
 =2\sqrt d\,\pi^{-s/2}\Gamma(s/2)
   \bigl[\zeta(s)-\pi d\,\zeta(s-2)+O(d^2)\bigr].
 \tag{GABR41}
\]
At each nontrivial zero, its first nonzero residual coefficient is
\[
 -2\pi\,\pi^{-\rho/2}\Gamma(\rho/2)\zeta(\rho-2)
 \quad\hbox{at order }d^{3/2},
 \tag{GABR42}
\]
which is nonzero by GABR28. At a nonzero value of zeta in the strip, the first residual order is \(d^{1/2}\), with coefficient
\(2\pi^{-s/2}\Gamma(s/2)\zeta(s)\ne0\). The raw \(I_d(s)\) tends to zero throughout the strip because its leading sector is of order \(d^{\Re s/2}\). These statements agree with source GAB37–40.

The independent check therefore finds no sign or multiplicity correction needed in the collision, pole-tower, shift-equation, or local-zero formulas reviewed here. The actual zero detector retains the entire singular sector and the full moment multiplier. It detects zeros throughout the critical strip; these calculations do not impose a real-part constraint or a positive Weil form.

## GABR9. Independent check of the added finite signed-measure realization

This section checks source GAB46–49 in its final byte version identified in GABR1. For \(d>0\), work on the Borel space \(X=(0,\infty)\), and set \(N=\mathbb N_{>0}\), \(N^c=X\setminus N\). Define
\[
 A_d=\sum_{n\ge1}e^{-\pi d n^2}\delta_n,\qquad
 C_d=e^{-\pi d u^2}\,du,\qquad
 \mu_d=A_d-C_d.
 \tag{GABR43}
\]
The atomic measure has finite total mass \(Z_d(0)\). The substitution \(v=\pi d u^2\) yields, with every differential factor retained,
\[
 \begin{aligned}
 \int_0^\infty e^{-\pi d u^2}u^{-s}\,du
 &=\frac12(\pi d)^{(s-1)/2}
       \int_0^\infty e^{-v}v^{(1-s)/2-1}\,dv\\
 &=\frac12(\pi d)^{(s-1)/2}\Gamma((1-s)/2)
   =S_{\pi d}(s).
 \end{aligned}
 \tag{GABR44}
\]
The integral is absolutely convergent exactly on \(\Re s<1\): its absolute integrand has the power \(u^{-\Re s}\) near zero, and Gaussian decay at infinity. In particular
\[
 C_d(X)=\frac12(\pi d)^{-1/2}\Gamma(1/2)
       =\frac1{2\sqrt d}.
 \tag{GABR45}
\]

The two positive measures are mutually singular. Indeed \(A_d(N^c)=0\) and \(C_d(N)=0\). Consequently their signed difference has the Jordan components
\[
 \mu_d^+=A_d,\qquad \mu_d^-=C_d,\qquad
 |\mu_d|=A_d+C_d.
 \tag{GABR46}
\]
Here \(N\) and \(N^c\) form the measurable partition used by these formulas; a point of the topological support of \(C_d\) can still belong to \(N\). The claim is mutual singularity of measures and does not require disjoint topological supports.

The exact restriction maps can be stated on a complete domain and codomain. Let \(\mathcal M_f(X)\) be the real vector space of finite signed Borel measures on \(X\), and let \(\mathcal M_f(N)\) and \(\mathcal M_f(N^c)\) mean the subspaces concentrated on those respective measurable sets. Then
\[
 \begin{aligned}
 D:\mathcal M_f(N)\oplus\mathcal M_f(N^c)&\longrightarrow
                              \mathcal M_f(X),\\
 (A,C)&\longmapsto A-C,
 \end{aligned}
 \qquad
 D^{-1}(\nu)=\bigl(\nu|_N,-\nu|_{N^c}\bigr).
 \tag{GABR47}
\]
Both composite maps are the identity because restrictions to the partition sum to the original measure and the cross restrictions vanish. In fact
\(\|A-C\|_{\mathrm{TV}}=\|A\|_{\mathrm{TV}}+\|C\|_{\mathrm{TV}}\)
on this domain, since the two variation measures are mutually singular. This proves the stated inverse maps without discarding the positive measures in the ordered pair \((A_d,C_d)\).

For \(\sigma=\Re s<1\), the full absolute Mellin bound is
\[
 \begin{aligned}
 \int_X |u^{-s}|\,d|\mu_d|(u)
 &=\sum_{n\ge1}e^{-\pi d n^2}n^{-\sigma}
   +\int_0^\infty e^{-\pi d u^2}u^{-\sigma}\,du\\
 &=Z_d(\sigma)
   +\frac12(\pi d)^{(\sigma-1)/2}
                         \Gamma((1-\sigma)/2)<\infty.
 \end{aligned}
 \tag{GABR48}
\]
Subtracting the two absolutely convergent Mellin integrals therefore gives exactly
\[
 \int_X u^{-s}\,d\mu_d(u)
       =Z_d(s)-S_{\pi d}(s)=Y_d(s),\qquad \Re s<1.
 \tag{GABR49}
\]
In particular this is an ordinary absolutely convergent signed-measure integral at every point in the critical strip; no cancellation convention at \(u=0\) is required. Its meromorphic continuation beyond that half-plane still has the poles in GABR20.

The parameter derivative is a derivative in total variation. To check this directly, fix \(d_0>0\) and take real \(h\) with \(|h|\le d_0/2\). Taylor's theorem gives for every \(u>0\)
\[
 \left|
 e^{-\pi(d_0+h)u^2}-e^{-\pi d_0u^2}
       +h\pi u^2e^{-\pi d_0u^2}
 \right|
 \le\frac{\pi^2h^2}{2}u^4e^{-\pi d_0u^2/2}.
 \tag{GABR50}
\]
The right side is summable over positive integers and integrable over the half-line. Divide by \(|h|\), sum or integrate, and let \(h\to0\). This proves the full identities
\[
 \partial_d A_d=-\pi u^2A_d,\qquad
 \partial_d C_d=-\pi u^2C_d,\qquad
 \partial_d\mu_d=-\pi u^2\mu_d.
 \tag{GABR51}
\]
All measures on the right are finite. If the difference quotient is also multiplied by \(u^{-s}\), its dominating Taylor remainder is integrable near zero when \(\Re s<1\), since it is bounded by a constant times \(u^{4-\Re s}\). The first derivative itself has power \(u^{2-\Re s}\) there. Both are Gaussian at infinity. Therefore the weighted differentiation is justified, not inferred solely from the unweighted total-variation statement. Taking the Mellin moment of GABR51 gives
\[
 \partial_dY_d(s)
 =-\pi\int_Xu^{2-s}\,d\mu_d(u)
 =-\pi Y_d(s-2),\qquad \Re s<1,
 \tag{GABR52}
\]
and the earlier meromorphic identity supplies its continuation.

Finally the integer-zero source mentioned in MRT is outside \(X=(0,\infty)\). If a finite measure on this space is extended by zero to \([0,\infty)\), its restriction to \(\{0\}\) remains zero. A separately retained component \(m\delta_0\) is recovered from a combined measure by restriction to \(\{0\}\), while the other two components are recovered by the restrictions to \(N\) and \(N^c\) in GABR47. Thus neither the continuous measure nor the discrete positive-integer measure identifies that marked source with an unsupported label. The added measure formulas GAB46–49 pass this independent check.
