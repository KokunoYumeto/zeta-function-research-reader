# Exact original norm, volume and PR15 cross-term bridge

Independent audit requested by `kernel_asymptotic_route`, 12 September 2026. This file adds a written audit only. It modifies no sealed source and runs no Lean. A second independent algebra review confirmed the identities and the initial-stage scope described below.

## Original objects and the two index systems

Retain a nonempty actual packet with all selected zero orders,

\[
h(s)=\prod_{\rho\in Z}(s-\rho)^{m_\rho},\qquad d=\deg h,
\quad E=\mathbb C[s]/(h),\quad A=M_s,\quad c=j_h1.
\]

Keep `g=2xi`, `v_h=g/h`, the original unit `upsilon=j_h(v_h)`, and `epsilon=upsilon^{-1}`. Let `U_upsilon,U_epsilon:E→E` be multiplication by these units in the unchanged monomial remainder coordinates. Thus their product in either order is the identity; no metric or coefficient is rescaled.

The source map is the actual function-valued map

\[
\mathcal T(P)=P(D)F_h,\qquad\mathcal MF_h=g/h,
\quad h(D)F_h=f_0,\quad f_0=\Theta\phi_*,\quad D=-x\partial_x.
\]

Its polynomial norm is that for

\[
d\nu_h(t)=\left|\frac{g(1/2+it)}{h(1/2+it)}\right|^2\frac{dt}{2\pi}.
\]

Write `q_j=p_j` for the exact notation correspondence between the monic polynomials in `kernel_terminal_continuation.tex` and `kernel_layer_continuation.tex`; both use this same measure and original variable s. Their unscaled squared norms are `kappa_j>0`. Set

\[
v_j=q_j(A)c,\qquad z_j=U_\upsilon v_j.
\]

The symbol z_j here is precisely the layer delivery's jet column `a_j`; it is renamed explicitly in this audit to keep that vector apart from the scalar recurrence coefficient `a_j=kappa_j/kappa_(j-1)` in KT.1.

For original theta correction level m≥−1 put N=d+m, n=N+1=d+m+1. Let

\[
K=K_{n-1}=\sum_{j=0}^{n-1}\frac{v_jv_j^*}{\kappa_j},
\qquad G_m=U_\varepsilon^*K^{-1}U_\varepsilon.
\]

For m=−1, this is the previously fixed `G_-1` and `R_-1=R_ref`: the full jet map on polynomials of degree≤d−1 is an isomorphism, so its unique inverse is also its unique constrained minimum. For m≥0, the layer delivery's `R_N,G_N` agree with the original corrected `R_m,G_m`; the constraint kernel is `h P_m`, and `T(h P_m)=span{f_0,...,f_m}`. This is the exact level dictionary.

Define original theta monic vectors and norms by

\[
u_j=Q_j(D)f_0,\qquad\mathfrak h_j=\|u_j\|_{L^2(dx)}^2,
\]

where Q_j is the original monic polynomial for `dmu=|g|²dt/(2pi)`. These are the `u_j,h_j` in PR15. Its original row is

\[
d_j=\mathfrak h_j^{-1}u_j^*R_{\rm ref}:E\longrightarrow\mathbb C.
\]

The symbol d_j equals the PR15 note's row `r_j`; the letter r without superscript below is reserved for the actual volume ratio

\[
r_j=\frac{\det G_j}{\det G_{j-1}}\qquad(j\ge0).
\]

## The delivered layer is the original unscaled theta vector

The one-variable instance of KL.7 is

\[
e_n=\mathcal Tq_n-R_mz_n.
\]

It has zero original full jet, since both terms have full jet z_n. Its numerator polynomial is monic of degree n: `Tq_n` has that degree and the numerator of `R_mz_n` has degree≤n−1. Zero full jet, with the invertible original unit retained, means that this numerator is divisible by the original monic h. Its quotient is therefore monic of degree n−d=m+1. Hence

\[
e_n=\widetilde Q_{m+1}(D)f_0
\]

for a monic polynomial `Qtilde_(m+1)` of degree m+1. The source's KL.7 orthogonality gives `e_n` perpendicular to `T(h P_m)=span{f_0,...,f_m}`. Under Mellin, this says exactly that `Qtilde_(m+1)` is orthogonal to every polynomial of degree≤m in the unchanged measure mu. Its positive polynomial Gram gives uniqueness of the monic orthogonal polynomial, so

\[
\boxed{e_n=u_{m+1}=Q_{m+1}(D)f_0.}
\]

At m=−1, n=d and the numerator is monic of degree d and divisible by h. It is exactly h, with quotient 1. Thus the initial vector is **e_d=f_0**, not a scalar multiple or a new vector. No negative-degree orthogonal polynomial is introduced.

The new polynomial q_n is perpendicular in nu_h to every old polynomial of degree≤n−1, so `Tq_n` is perpendicular to `R_mz_n`. Taking the norm of the original difference therefore gives

\[
\mathfrak h_{m+1}=\|e_n\|^2
=\kappa_n+z_n^*G_mz_n
=\kappa_n+v_n^*K^{-1}v_n.                       \tag{NV.1}
\]

The last equality follows from `U_epsilon U_upsilon=I`, with their adjoints retained. It is valid for m≥−1, including e_d.

The kernel update and determinant lemma give

\[
K_n=K_{n-1}+\frac{v_nv_n^*}{\kappa_n},\qquad
r_{m+1}=\frac{\det K_{n-1}}{\det K_n}
=\frac{\kappa_n}{\kappa_n+v_n^*K^{-1}v_n}.
\]

Every denominator is positive. Combining this with NV.1 proves

\[
\boxed{\mathfrak h_{m+1}=\frac{\kappa_{d+m+1}}{r_{m+1}}\quad(m\ge-1).} \tag{NV.2}
\]

In particular `hfrak_0=kappa_d/r_0`. Using the adjacent instance gives, for m≥0 and n=d+m+1,

\[
\boxed{\frac{\kappa_n}{\kappa_{n-1}}
=\frac{\mathfrak h_{m+1}}{\mathfrak h_m}\frac{r_{m+1}}{r_m}.} \tag{NV.3}
\]

This proves the exact link between the original mu-norm sequence and the quotient-measure nu_h-norm sequence. In particular the unscaled mu-norms remain independent of the packet; the right side of NV.2 calculates those same norms using its packet-dependent kernel and volume ratio.

## Exact original row maps and the conjugated cross term

For m≥0 the original representative has the finite expansion

\[
\mathcal MR_mu
=\frac gh\left(R_Z(u)-h\sum_{j=0}^m Q_jd_ju\right).
\]

The numerator's leading coefficient, at degree d+m=n−1, is exactly `-d_mu`, since deg R_Z<d, h and Q_m are monic, and every earlier term has smaller degree. On the other hand the original constrained minimum KL.6, with its units retained, is

\[
R_mu=\sum_{j=0}^{n-1}\mathcal Tq_j
          \frac{v_j^*K^{-1}U_\varepsilon u}{\kappa_j}.
\]

Its leading coefficient is the j=n−1 summand. Equating these coefficients proves

\[
\boxed{d_m=-\frac{v_{n-1}^*K^{-1}U_\varepsilon}{\kappa_{n-1}}.} \tag{NV.4}
\]

For the next row, `e_n=u_(m+1)` is perpendicular to the old theta relations, so `e_n^*R_ref=e_n^*R_m`. The actual layer identity KL.10 is `e_n^*R_m=-z_n^*G_m`. Consequently

\[
\boxed{d_{m+1}=-\frac{v_n^*K^{-1}U_\varepsilon}{\mathfrak h_{m+1}}.} \tag{NV.5}
\]

NV.5 also holds at m=−1 and computes d_0 correctly. NV.4 is asserted only for m≥0. At m=−1 the old numerator is R_Z and its top coefficient is the original extension row ell_Z; the tail convention d_-1=0 must not be replaced by an illicit extension of NV.4.

Write k=`kappa_(n-1)` and H=`hfrak_(m+1)`. KT.3 defines

\[
\alpha_n=\frac{v_{n-1}^*K^{-1}v_{n-1}}k,\quad
\beta_n=\frac{v_n^*K^{-1}v_n}k,\quad
\gamma_n=\frac{v_n^*K^{-1}v_{n-1}}k.
\]

In the PR15 note's order the three scalars are

\[
a_m^{\rm PR}=d_mG_m^{-1}d_m^*,\quad
b_m^{\rm PR}=d_{m+1}G_m^{-1}d_{m+1}^*,\quad
c_m^{\rm PR}=d_mG_m^{-1}d_{m+1}^*.
\]

The exact inverse transport is `U_epsilon G_m^{-1}U_epsilon^*=K`. Substitution of NV.4–NV.5 then proves, with the order of the two vectors unchanged,

\[
\boxed{a_m^{\rm PR}=\frac{\alpha_n}{k},\qquad
b_m^{\rm PR}=\frac{k\beta_n}{H^2},\qquad
c_m^{\rm PR}=\frac{\overline{\gamma_n}}H.}          \tag{NV.6}
\]

Thus **the exact identity is H c_m^PR=conjugate(gamma_n)**. In general it is not gamma_n. For example, the finite algebra data `K=I_2`, k=1, `v_(n-1)=(1,i)^T`, `v_n=(2,1)^T`, `kappa_n=3`, and `U_epsilon=[[1,i],[0,2]]` give H=8, gamma=2+i, and c=(2−i)/8. Here `G=[[1,i],[-i,5]]`, `d_m=(-1,i)`, and `d_(m+1)=(-1/4,-(1+i)/4)`, which verify the conjugation directly. This is an orientation calibration of the matrix identity, not a claim that these arbitrary columns are arithmetic theta data.

NV.6 identifies the complete two control formulas:

\[
H\left(|\Re c_m^{\rm PR}|+
\sqrt{a_m^{\rm PR}b_m^{\rm PR}-(\Im c_m^{\rm PR})^2}\right)
=|\Re\gamma_n|+\sqrt{\alpha_n\beta_n-(\Im\gamma_n)^2}.
\]

It also gives the exact cross-term invariant

\[
\alpha_n\beta_n-|\gamma_n|^2
=H^2\left(a_m^{\rm PR}b_m^{\rm PR}-|c_m^{\rm PR}|^2\right).
\]

Using the actual Gram updates, or NV.2 together with KT.7–KT.8,

\[
\alpha_n\beta_n
=\frac{\mathfrak h_{m+1}}{\mathfrak h_m}
      (r_m^{-1}-1)(1-r_{m+1}).                        \tag{NV.7}
\]

Hence this calculation retains the full subtraction term `H²|c_m^PR|²` for arbitrary packets. The trace identity gives `Re gamma_n=Re Tr A-d/2`, and therefore

\[
H\Re c_m^{\rm PR}=\Re\operatorname{Tr}A-d/2.
\]

## Both packet symmetries force the original c_m to vanish

Assume the specified divisor is closed under both `rho→conjugate(rho)` and `rho→1−conjugate(rho)`, retaining all selected multiplicities. Conjugation invariance makes h monic with real coefficients. Since `g(conjugate s)=conjugate(g(s))`, the original nu_h density is even in t. For any monic orthogonal polynomial q, the polynomial `q^c(s)=conjugate(q(conjugate s))` has the same degree, leading coefficient and lower-degree orthogonality: conjugate each pairing and change t to −t. Uniqueness forces q^c=q. Thus all q_j have real coefficients in the original s-variable. The companion matrix A, remainder vector c and vectors v_j are therefore real, as are K and its inverse. It follows from its defining formula that gamma_n is real. By NV.6 the original PR15 c_m is real as well.

Reflection invariance gives

\[
\sum_{\rho\in Z}m_\rho\Re\rho=d/2,
\]

because the involution sends each real part beta to 1−beta with the same multiplicity; fixed points already have beta=1/2. The trace of multiplication by s includes each nilpotent block's eigenvalue with its full multiplicity, so `Re Tr A=d/2`. The preceding trace identity now gives `Re gamma_n=0`. Since gamma_n is real, gamma_n=0 and

\[
\boxed{c_m^{\rm PR}=0\quad\text{for every }m\ge0.}       \tag{NV.8}
\]

Conjugation alone yields reality; reflection alone yields vanishing real part. Their conjunction proves the complete vanishing claimed here. No critical-line location has been assumed.

The rank-two formula and NV.7 now yield the source-coordinate equality

\[
\boxed{\epsilon_m^2
=\frac{\mathfrak h_{m+1}}{\mathfrak h_m}
       (r_m^{-1}-1)(1-r_{m+1})\qquad(m\ge0).}          \tag{NV.9}
\]

Equivalently, substitution of NV.3 into KT.28 gives NV.9 directly, with every original norm and volume ratio retained. Under the same two packet symmetries, PR15's displayed upper bound is therefore an exact identity.

All formulas allow zero jet columns. No division by a column, row, alpha, beta, gamma or c occurs. The only divisions use positive monic norms, positive definite Gram matrices, positive volume ratios and the fixed arithmetic unit. If v_n=0, then `r_(m+1)=1`, d_(m+1)=0 and both sides of NV.9 vanish; the analogous old-column case gives r_m=1 and d_m=0. The level m=0 uses the actual G_-1 and the independently proved `e_d=f_0`.

## Authoritative sources read

- `output/split_zero_rh_tandem_2026-09-12/tex/kernel_layer_continuation.tex`, KL.1–KL.10: original unit, minimum, layer vectors, monic quotient and layer norm.
- `output/split_zero_rh_tandem_2026-09-12/tex/kernel_terminal_continuation.tex`, KT.1–KT.8 and KT.28: original kernel scalar order, positive determinant ratios and both packet symmetries.
- `output/split_zero_rh_tandem_2026-09-12/tex/tau_boundary.tex`, TB.27–TB.31: original mu-polynomials, theta rows and actual finite control form.
- PR15 exact head `21970bbf4760d0bbca512a4a7996a2e38f968947`, staged `RESEARCH_NOTE.md` Sections 2–4: exact definitions of its h_n, r_n, a_n, b_n and c_n.

Audit outcome: the proposed norm-volume bridge is valid. The required exact cross-term formula contains a conjugation. The initial norm bridge includes m=−1, while the old-row formula begins at m=0. Under the stated two symmetries the original PR15 cross term vanishes and its relative-conditioning bound becomes the equality NV.9. These are written proofs; no extra Lean certification is asserted.
