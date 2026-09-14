---
title: "Arithmetic endpoint bounds on the original τ-base source"
subtitle: "A uniform polynomial-norm estimate; integration with the four-volume criterion"
author: "Owner-directed SplitZero analytic continuation"
date: "13 September 2026"
---

# 1. Result and exact source boundary

The formalization session's endpoint criterion selects an actual member of the
canonical arithmetic family. This continuation proves one of its previously
unproved analytic inputs. For the **unchanged arithmetic measure**, a fixed
finite packet $h$, and integers $n\ge k\ge3$, there is a finite constant $C_h$,
independent of $n$ and $k$, such that

$$
 \boxed{\left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}
       \le C_h n.}                                                    \tag{1}
$$

The norms are the original monic polynomial norms for $m_{h,k}=w_h^{*k}$;
the total mass remains $\mu_h^k$. No root-location hypothesis is used in this
bound. The proof retains a compact-source mass, a lower convolution constant,
and both exponential moments. These constants are defined explicitly below;
they have not been numerically enclosed.

For the packet consisting exactly of a hypothetical nonreal off-line quartet,
let

$$
 q_k=[1+k(m-1)](k+1)^2,
 \quad
 L_{h,k}=2\delta[1+k(m-1)](k+1)
                 \left\lfloor\frac{(k+1)^2}{4}\right\rfloor.             \tag{2}
$$

The existing exterior theorem gives $L_{h,k}\le\epsilon_{h,k,N}$ at every
admitted degree. Combining (1) with the other session's endpoint theorem gives

$$
 \boxed{\min_{q_k\le N<2q_k}\epsilon_{h,k,N}
 \le C_hq_k\sinh\!\left(\frac{\mathcal B_{h,k}}{2q_k}\right),\qquad
 \mathcal B_{h,k}=\log\frac{V_{q_k-1}V_{q_k}}
                              {V_{2q_k-1}V_{2q_k}}.}                    \tag{3}
$$

Consequently such a quartet forces

$$
 \boxed{\mathcal B_{h,k}\ge
 2q_k\operatorname{arsinh}\!\left(\frac{\delta k}{2C_h}\right),\qquad
 \liminf_{k\to\infty}\frac{\mathcal B_{h,k}}{q_k\log k}\ge2.}           \tag{4}
$$

The upper bound for this four-volume quantity is not proved here. In particular,
(1) does not establish RH. It completes the polynomial-norm input in (3) on a
specific admissible window and leaves the source/relation-volume comparison
with its exact maps. Section 9 expresses that remaining quantity as two positive
block log-determinants of actual new relation layers.

The finite quotient, canonical source, residue action and rank-two control are
inputs from the preceding analytic notes. The new proofs in Sections 3--7 use
only their explicitly defined arithmetic measure. The endpoint theorem is the
formalizer's written result, not attributed to this continuation. Its finite
telescopes are reported kernel-checked; the analytic estimates below have written
proofs, not new Lean certificates.

# 2. The base, source, and both kinds of quotient

Retain the original marked coefficient square

$$
\begin{array}{ccc}
 G(\mathbb Z)&\xrightarrow{G(j)}&G(\mathbb C)\\
 p_{\mathbb Z}\downarrow&&\downarrow p_{\mathbb C}\\
 \mathbb Z&\xrightarrow{j}&\mathbb C.
\end{array}                                                          \tag{5}
$$

Here $G(R)=\{\tau\}\sqcup\{r^\bullet:r\in R\}$, $e_R=0_R^\bullet$,
$p_R(\tau)=0_R$, and $p_R(r^\bullet)=r$. The target of $p_{\mathbb Z}$ is
infinite. The construction remains over the original pointed base
$\mathfrak b_\tau$; no new scalar zero is adjoined at a tensor degree or at a
polynomial relation layer.

Keep $C_+=[V\xrightarrow{\Theta}\mathscr B]$ in degrees $0,1$,
$Q=\mathscr B/\Theta V$, and $D=-x\partial_x$. The source spaces and the Fourier
transform remain those of the earlier theta construction. In particular,

$$
 g(s)=2\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
 \mathcal M\Theta\phi_*=g.                                            \tag{6}
$$

Let $h$ be a fixed finite product of zeros of $g$, with the full order of each
selected zero retained, and write $d=\deg h$. Define

$$
 v_h=g/h,\quad
 w_h(t)=\frac{|v_h(1/2+it)|^2}{2\pi},\quad
 \mu_h=\int_{\mathbb R}w_h(t)\,dt,\quad m_{h,k}=w_h^{*k}.               \tag{7}
$$

The quotient $v_h$ is entire, including at the selected centres. It is not the
meromorphic expression evaluated before removing its actual removable factors.
For $h=1$, the same analytic definitions are meaningful, but the finite arithmetic
packet is zero. Only the nonempty case is used for the finite Gram inverses below.

The source map is

$$
 \mathcal V_{h,k}:\mathbb C[S]\longrightarrow\mathscr B^{\widehat\otimes k},
 \qquad P\longmapsto P(D_1+\cdots+D_k)(F_h^{\otimes k}),\qquad
 \mathcal MF_h=v_h.                                                    \tag{8}
$$

The original cyclic module is $E_{h,k}=\mathbb C[S]/(\chi_{h,k})$. Its
arithmetic inclusion keeps the Taylor unit:

$$
 \eta_{h,k}[P]=\upsilon_h^{\otimes k}P(A_k)1,\quad
 \upsilon_h=j_h(g/h),\quad A_k=\sum_iM_{s_i}.                           \tag{9}
$$

The supplied source identities are

$$
 J^{(k)}\mathcal V_{h,k}=\eta_{h,k}\pi_\chi,\qquad
 q^{(k)}\mathcal V_{h,k}=\sigma_h^{\otimes k}\eta_{h,k}\pi_\chi.          \tag{10}
$$

The actual norm of (8) is

$$
 \|\mathcal V_{h,k}P\|^2
 =\int_{\mathbb R}|P(k/2+iu)|^2m_{h,k}(u)\,du.                          \tag{11}
$$

For $\mathcal P_n=\mathbb C[S]_{\le n}$, the monic norm is the quotient norm
of the leading-coefficient map

$$
 0\longrightarrow\mathcal P_{n-1}\longrightarrow\mathcal P_n
 \xrightarrow{\operatorname{lc}_n}\mathbb C\longrightarrow0,
 \qquad
 \omega_{h,k,n}=\inf_{\operatorname{lc}_nP=1}\|\mathcal V_{h,k}P\|^2.
                                                                         \tag{12}
$$

The arithmetic quotient is the other specified map from the same source:

$$
 0\longrightarrow\mathcal P_{n-q}
 \xrightarrow{\times\chi}\mathcal P_n
 \xrightarrow{\pi_\chi}E_{h,k}\longrightarrow0,\qquad q=\deg\chi,
                                                                         \tag{13}
$$

for $n\ge q-1$, with the preceding relation space zero at $n=q-1$.
Multiplication by the monic $\chi$ carries
$\mathcal P_{n-q}/\mathcal P_{n-q-1}$ isomorphically to
$\mathcal P_n/\mathcal P_{n-1}$, with leading coefficient unchanged.
The map $\pi_\chi$ kills that very relation. Thus (12), (13), and multiplication
by $\chi$ specify the relation between the degree-line norm and the arithmetic
quotient metric. One norm is not substituted for the other.

At each admitted original support label $\lambda$, the lifted quotient is
$(\lambda,P)\mapsto(\lambda,[P]_\chi)$. An original relation has image
$(\lambda,0)$; external absence has image $\tau$. Its norm before this projection
remains available through (11).

# 3. A quantitative local arithmetic mass lemma

## 3.1 Uniform polynomial growth on a fixed strip

There is a constant $C_0\ge1$ such that, for $|T|\ge10$, the function

$$
 f_T(z)=\zeta(1/2+iT+iz)                                                \tag{14}
$$

is holomorphic on and inside the ellipse

$$
 z=\frac12(w+w^{-1}),\qquad |w|=8,
                                                                         \tag{15}
$$

and has modulus at most $M_T=C_0(1+|T|)^6$ there.

The ellipse has real and imaginary semiaxes $65/16$ and $63/16$. Hence its
image in the $s$-plane lies in
$-55/16\le\Re s\le71/16$ and $|\Im s-T|\le65/16$. The pole of $\zeta$ is
outside this set when $|T|\ge10$.

For $\Re s\ge1/4$, use the identity

$$
 \zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.              \tag{16}
$$

It follows by summing the steps of $\lfloor x\rfloor$ for $\Re s>1$ and then
by analytic continuation for $\Re s>0$, $s\ne1$. Its integral is bounded by
$1/\Re s$, giving $O(1+|T|)$ on the indicated part of the ellipse.
For $\Re s\le1/4$, the functional equation

$$
 \zeta(s)=2^s\pi^{s-1}\sin(\pi s/2)\Gamma(1-s)\zeta(1-s)              \tag{17}
$$

and the vertical-strip gamma estimate give
$O((1+|T|)^{3/2-\Re s})$. On the stated strip this exponent is below $5$.
The common power $6$ in (14) is therefore a valid upper bound with one fixed
constant. The gamma estimate and functional equation are the classical inputs
recorded in DLMF §§5.11 and 25.4; none assumes RH.

Every disc of radius one about a point of $[-1,1]$ lies inside the ellipse.
The maximum principle and Cauchy's derivative formula therefore also give

$$
 \sup_{x\in[-1,1]}|f_T'(x)|\le M_T.                                    \tag{18}
$$

## 3.2 Propagate a nonzero value to the critical-line interval

Put

$$
 r_*=(3+\sqrt{13})/2<4,\qquad
 z_*=-3i/2=\tfrac12(-ir_*+(-ir_*)^{-1}),\qquad
 c_* =\zeta(2)^{-1}.                                                    \tag{19}
$$

The absolutely convergent reciprocal Dirichlet series gives
$|1/\zeta(2+iT)|\le\zeta(2)$, so $|f_T(z_*)|\ge c_*>0$.
Let $m_T=\max_{[-1,1]}|f_T|$.

Apply the maximum principle on $1\le|w|\le8$ to
$f_T((w+w^{-1})/2)$. Equivalently subtract from its logarithmic modulus the
harmonic function linear in $\log|w|$ with boundary values $\log m_T$ and
$\log M_T$. Zeros are handled by the usual subharmonic maximum principle.
At $w=-ir_*$ this gives

$$
 c_*\le m_T^{\vartheta}M_T^{1-\vartheta},\qquad
 \vartheta=1-\frac{\log r_*}{\log8}>\frac13.
                                                                         \tag{20}
$$

Here $0<c_*<1$ and $M_T\ge1$. Consequently

$$
 m_T\ge c_*^3M_T^{-2}.                                                 \tag{21}
$$

This is the three-circles argument with every coordinate map and radius fixed.
No polynomial approximation to $\zeta$ or assumption about its zeros is used.

Choose a point attaining $m_T$. By (18), on a one-sided subinterval of length
$m_T/(2M_T)\le1/2$ inside $[-1,1]$, the modulus is at least $m_T/2$. Thus

$$
 \int_{T-1}^{T+1}|\zeta(1/2+it)|^2\,dt
 \ge \frac{m_T^3}{8M_T}
 \ge \frac{c_*^9}{8C_0^7}(1+|T|)^{-42}.                                \tag{22}
$$

For $T\in[-10,10]$, the integral in (22) is continuous and strictly positive:
otherwise $\zeta$ would vanish on an interval and hence identically on its
holomorphic domain. Its minimum on that compact interval is positive.
Combining it with (22) proves the all-real statement

$$
 \boxed{\exists c_\zeta>0\quad
 \int_{T-1}^{T+1}|\zeta(1/2+it)|^2\,dt
 \ge c_\zeta(1+|T|)^{-42}\quad(T\in\mathbb R).}                         \tag{23}
$$

The exponent $42$ is deliberately an explicit sufficient exponent, not an
optimal local mean-square estimate. The proof is a classical analytic
propagation argument specialized here to the needed arithmetic interval.

# 4. A lower envelope for the actual convolution, after three factors

## 4.1 Local mass of the unchanged $g/h$

The gamma estimate, with a positive lower constant valid also on compact sets,
implies

$$
 |\Gamma(1/4+it/2)|^2
 \ge c_\Gamma(1+|t|)^{-1/2}e^{-\pi|t|/2}.                              \tag{24}
$$

Let
$H_h=\prod_{\rho\in Z}(1+|\rho-1/2|)^{m_\rho}$, so
$|h(1/2+it)|\le H_h(1+|t|)^d$.
The entire identity $g=hv_h$ makes this bound valid at selected centres as well:
$|g|\le H_h(1+|t|)^d|v_h|$. The factors in (6), including
$|s(s-1)|^2=(t^2+1/4)^2$, then give a positive constant $c_h^{(0)}$ with

$$
 w_h(t)\ge c_h^{(0)}e^{-\alpha_0|t|}(1+|t|)^{-2d}
                   |\zeta(1/2+it)|^2,\qquad \alpha_0=\pi/2.            \tag{25}
$$

Equation (25) is a weaker bound than the available factor
$(1+|t|)^{7/2-2d}$; it follows by an inequality, not by changing the density.
On $[T-1,T+1]$, its exponential and polynomial weights are bounded below by
$e^{-\alpha_0}e^{-\alpha_0|T|}$ and
$2^{-2d}(1+|T|)^{-2d}$, respectively. Hence (23) proves

$$
 \int_{T-1}^{T+1}w_h(t)\,dt
 \ge c_h^{(1)}e^{-\alpha_0|T|}(1+|T|)^{-B_h},\qquad B_h=42+2d.          \tag{26}
$$

## 4.2 The positive compact convolution factor

The function $w_h$ is continuous, bounded, integrable, and positive outside a
discrete set. Thus $m_{h,2}=w_h*w_h$ is continuous and strictly positive at every
real point. Indeed its integrand is positive almost everywhere; continuity
follows from translation continuity in $L^1$ and boundedness of the other
factor. Define the **actual** compact quantities

$$
 b_h=\min_{|v|\le1}m_{h,2}(v)>0,\qquad
 \vartheta_h=\int_{-1}^{1}w_h(v)\,dv>0.                                 \tag{27}
$$

Both are determined by the original density; neither is assigned the value one.
Restricting a nonnegative convolution integral gives

$$
 m_{h,3}(u)\ge
 b_h\int_{u-1}^{u+1}w_h(t)\,dt
 \ge c_h e^{-\alpha_0|u|}(1+|u|)^{-B_h},\quad c_h=b_hc_h^{(1)}>0.
                                                                         \tag{28}
$$

The omitted part is the nonnegative integral over $|v|>1$ and remains part of
$m_{h,3}$. We use a lower bound, not a new compactly supported density.

For $k\ge3$, restrict the remaining $k-3$ variables to $[-1,1]$ and use (28).
Their sum has absolute value at most $k-3$. This gives the central analytic
estimate

$$
 \boxed{
 m_{h,k}(u)\ge
 c_h\vartheta_h^{k-3}
 e^{-\alpha_0(|u|+k-3)}
 (1+|u|+k-3)^{-B_h}
 \quad(k\ge3,\ u\in\mathbb R).}                                       \tag{29}
$$

All mass and tensor factors are explicit. For $k=3$ the factor
$\vartheta_h^0$ is the empty product. No statement for $k=1,2$ is inferred by
using a negative exponent. The amplification below only needs $k\ge3$.

# 5. Upper moments and exact lower monic norms

Fix $0<b<\pi/2$ and retain both one-factor Laplace values

$$
 M_h(\pm b)=\int e^{\pm bt}w_h(t)\,dt>0.                               \tag{30}
$$

They are finite by the original gamma decay. Fubini and positivity give

$$
 \int e^{b|u|}m_{h,k}(u)\,du
 \le M_h(b)^k+M_h(-b)^k.                                                \tag{31}
$$

The elementary exponential-series inequality
$x^j\le j!b^{-j}e^{bx}$ for $x\ge0$ yields

$$
 \omega_{h,k,j}
 \le (2j)!b^{-2j}\bigl(M_h(b)^k+M_h(-b)^k\bigr).                       \tag{32}
$$

The trial polynomial is $(S-k/2)^j$, whose value on $S=k/2+iu$ is $i^ju^j$.
Its phase has modulus one and remains in the source map; the generator $A=M_S$
has not been shifted to define a different spectral problem.

For every leading coefficient of modulus one, the exact least squared norm of
a degree-$j$ polynomial on $[-L,L]$ with Lebesgue measure is

$$
 \mathfrak l_j(L)=
 \frac{2L^{2j+1}}{2j+1}
       \left(\frac{2^j(j!)^2}{(2j)!}\right)^2.                           \tag{33}
$$

To check all constants, Rodrigues' formula gives the Legendre polynomial
$P_j(x)$ with leading coefficient $(2j)!/(2^j(j!)^2)$ and squared norm
$2/(2j+1)$. Its scaled monic version on $[-L,L]$ is the unique minimizer:
subtract it from any competing monic polynomial, and the difference has lower
degree and is orthogonal to it. For the source coordinate $S=k/2+iu$, multiply
this minimizer by the retained leading phase $i^j$. This proves (33) at the
original type. See also DLMF §§18.3 and 18.5.

Restricting (11) to $[-L,L]$ and using (29) proves

$$
 \boxed{
 \omega_{h,k,j}\ge
 c_h\vartheta_h^{k-3}
 e^{-\alpha_0(L+k-3)}(1+L+k-3)^{-B_h}\,\mathfrak l_j(L)
 \quad(k\ge3,L>0).}                                                    \tag{34}
$$

The observation has the explicit isometric splitting into the inside and outside
interval components. Addition recovers the full source function, and their
squared norms add. In the split lift each zero component is the supported zero
at its label. The outside component has not been declared absent.

# 6. The norm-window estimate is proved

Set $j=n$ and $L=n$ in (34), and use $j=2n$ in (32). The exact finite bound is

$$
 \boxed{
 \left(\frac{\omega_{h,k,2n}}{\omega_{h,k,n}}\right)^{1/(2n)}
 \le\left[
 \frac{(4n)!b^{-4n}(M_h(b)^k+M_h(-b)^k)
       e^{\alpha_0(n+k-3)}(1+n+k-3)^{B_h}}
      {c_h\vartheta_h^{k-3}\mathfrak l_n(n)}
       \right]^{1/(2n)}.}                                              \tag{35}
$$

For $n\ge k\ge3$, this is at most $C_hn$. Here is one explicit sufficient
constant, with $M_* =\max\{1,M_h(b),M_h(-b)\}$:

$$
 \boxed{
 C_h=64b^{-2}\exp(\alpha_0)\,2^{B_h/2}
       \exp\!\left(\frac{B_h}{2\exp(1)}\right)
       \sqrt{M_*\max(1,c_h^{-1})\max(1,\vartheta_h^{-1})}.
 }                                                                     \tag{36}
$$

Proof of the uniform estimate: $\binom{2n}{n}\le4^n$ in (33) gives
$\mathfrak l_n(n)\ge2n^{2n+1}/((2n+1)4^n)$.
Also $(4n)!\le(4n)^{4n}$, $M_h(b)^k+M_h(-b)^k\le2M_*^k$,
$n+k-3\le2n$, and $1+n+k-3\le2n$. After taking the $2n$-th root the factorial
and monic factors contribute at most $64n$. The mass factors contribute at most
the square root in (36); the exponential contributes at most
$\exp(\alpha_0)$. Finally $n^{1/n}\le\exp(1/\exp(1))$ gives
$(2n)^{B_h/(2n)}\le2^{B_h/2}\exp(B_h/(2\exp(1)))$.
This proves (1).

The constant is intentionally not optimized. Its dependence on the fixed packet
is allowed; its independence of the polynomial and tensor degrees is what is
needed. Defining it via positive compact minima does not claim to have provided
a numerical interval enclosure for those minima.

For a general source window the same two inequalities give, without asymptotic
notation,

$$
 \left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}
 \le\left[
 \frac{(2(n+r))!b^{-2(n+r)}(M_h(b)^k+M_h(-b)^k)
       e^{\alpha_0(L+k-3)}(1+L+k-3)^{B_h}}
      {c_h\vartheta_h^{k-3}\mathfrak l_n(L)}
       \right]^{1/(2r)}.                                               \tag{37}
$$

# 7. Compose the proved bound with the formalizer's endpoint theorem

For a nonempty cyclic packet $E_{h,k}$, let $G_N$ be its original canonical
quotient metric, $V_N=\det G_N>0$, and $\epsilon_{h,k,N}$ the original
rank-two control allowance. The new endpoint theorem supplied by PR #23 is

$$
 \min_{0\le j<r}\epsilon_{h,k,n+j}
 \le
 \left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}
 \sinh\!\left(\frac1{2r}
       \log\frac{V_{n-1}V_n}{V_{n+r-1}V_{n+r}}\right),\qquad n\ge q.
                                                                         \tag{38}
$$

Its proof multiplies the local Toda bounds, applies concavity of
$\log\sinh x$, and uses the two exact telescopes. The zero-contraction case is
handled before taking logarithms. This result is credited to the parallel
formalization/research session. The proof and the distinction between checked
finite components and written Jensen assembly are retained in its source.

Choose $n\ge\max(q,k)$ and $r=n$. Equations (1) and (38) yield the actual
canonical selection estimate

$$
 \boxed{
 \min_{n\le N<2n}\epsilon_{h,k,N}
 \le C_hn\sinh\!\left(\frac1{2n}
                 \log\frac{V_{n-1}V_n}{V_{2n-1}V_{2n}}\right).
 }                                                                     \tag{39}
$$

The chosen index is a member of the existing canonical family. The source
representative, Taylor unit, kernel, action and trace are not chosen again after
selecting this index.

For the packet consisting exactly of the quartet in (2), $q_k\ge k$ and
$L_{h,k}/q_k\ge\delta k/2$. The earlier exterior bound holds at every admitted
index, including the one selected by (39). Since $\sinh$ is increasing on
$[0,\infty)$, (4) follows. Moreover
$\operatorname{arsinh}(ak)=\log k+O_a(1)$ for every fixed $a>0$,
which proves the stated threshold $2$.

A proved upper bound with
$\limsup\mathcal B_{h,k}/(q_k\log k)<2$ would contradict (4). Such an upper
bound is **not** an output of this note. The previous sufficient target
$\mathcal B_{h,k}=o(q_k\log k)$ remains sufficient, but (4) specifies the
larger quantitative threshold against which a future upper estimate can be
compared. No repeated cost-free exterior operation is used: the multiplicity
correction in the new formalization is retained.

# 8. The remaining four volumes retain their finite jet maps

The previous source/relation determinant identity remains

$$
 V_N=\frac{\mathfrak D_{N+1}}{\mathfrak B_{N-q+1}}.
                                                                         \tag{40}
$$

In the parallel full-jet transfer coordinates (PR #24), let
$a=N-q+1$, let $\mathsf F_a$ be its $2q$ by $2q$ raw confluent-jet matrix,
and let $\mathsf V$ be its raw-derivative Vandermonde matrix, with every
factorial retained. Its established identity is

$$
 V_N=\left(\prod_{j=a}^{a+q-1}\omega_{h,k,j}\right)
                       \frac{\det\mathsf V}{\det\mathsf F_a}.           \tag{41}
$$

For the window $n=r=q$, the four transfer indices are exactly
$0,1,q,q+1$. Put $\Omega_j=\prod_{i=j}^{j+q-1}\omega_{h,k,i}$. Then

$$
 \boxed{
 \exp\mathcal B_{h,k}
 =\frac{\Omega_0\Omega_1}{\Omega_q\Omega_{q+1}}
   \frac{\det\mathsf F_q\det\mathsf F_{q+1}}
        {\det\mathsf F_0\det\mathsf F_1}.
 }                                                                     \tag{42}
$$

The common Vandermonde cancels in this explicit ratio, not inside any underlying
map. The transfer matrices and their inverses still need their actual arithmetic
control; the fixed width alone gives no such bound.

The empty packet has $q=0$, $V_N=1$ as an empty determinant, and no positive-rank
inverse or quartet estimate. The analytic inequalities (23)--(37) still apply
to its theta seed, but are not statements about a nonexistent finite packet.

# 9. The volume window is also two explicit retained-boundary costs

There is a second useful representation of the same remaining quantity, with no
reference-density change. Fix $i<j$, both admissible. In the original monic
polynomial basis put

$$
 F_{i,j}=[b_{i+1},\ldots,b_j],\qquad
 \Omega_{i,j}=\operatorname{diag}(\omega_{i+1},\ldots,\omega_j),
 \qquad b_a=[p_a]_\chi.                                                 \tag{43}
$$

The kernel update is the actual sum
$K_j=K_i+F_{i,j}\Omega_{i,j}^{-1}F_{i,j}^*$, where $K_i=G_i^{-1}$.
The matrix determinant lemma gives

$$
 \boxed{\frac{V_i}{V_j}
 =\det\!\left(I_{j-i}+\Omega_{i,j}^{-1}F_{i,j}^*G_iF_{i,j}\right).}       \tag{44}
$$

This determinant has positive real value. Its factors are $1+\lambda_a$, where
$\lambda_a\ge0$ are the generalized eigenvalues of the Hermitian pair
$(F_{i,j}^*G_iF_{i,j},\Omega_{i,j})$. No non-Hermitian matrix is asserted positive
in an unspecified Euclidean metric.

Let $T_{i,j}$ have columns $\mathcal V_{h,k}p_{i+1},\ldots,
\mathcal V_{h,k}p_j$. The original boundary-layer isomorphism is

$$
 \mathfrak b_{i,j}=T_{i,j}-R_iF_{i,j}:
 \mathbb C^{j-i}\xrightarrow{\sim}
 \mathcal D_j\cap\mathcal D_i^\perp,
 \qquad
 \mathfrak b_{i,j}^*\mathfrak b_{i,j}
 =\Omega_{i,j}+F_{i,j}^*G_iF_{i,j}.                                     \tag{45}
$$

Its jets vanish; its highest polynomial coefficients give injectivity. Any new
boundary can be reduced by these highest coefficients to an old boundary, and
orthogonality then gives surjectivity. These statements prove the displayed map
with the same original relation spaces, not only a dimension count.
The representative update is

$$
 R_j=R_i+
 \mathfrak b_{i,j}
 (\Omega_{i,j}+F_{i,j}^*G_iF_{i,j})^{-1}F_{i,j}^*G_i.                    \tag{46}
$$

Every correction in (46) is an original theta boundary. Its split quotient image
is $e$ at the receiving fibre, and the input relation remains available in (45).
Its cochain primitives are the same fixed-order divisions and tensor signs as
in the previous cyclic source construction.

Apply (44) to $(i,j)=(q-1,2q-1)$ and $(q,2q)$. This proves

$$
 \boxed{\mathcal B_{h,k}
 =\sum_a\log(1+\lambda_a^{(0)})
   +\sum_a\log(1+\lambda_a^{(1)}).}                                    \tag{47}
$$

In particular

$$
 \mathcal B_{h,k}\le
 \operatorname{Tr}(\Omega_{q-1,2q-1}^{-1}F^*G_{q-1}F)
 +\operatorname{Tr}(\Omega_{q,2q}^{-1}F^*G_qF),                          \tag{48}
$$

where each $F$ has its own indicated source and target from (43).
When this trace bound is too large, (47) retains the full logarithmic cost rather
than replacing it by its linear upper bound. The analytic norm estimate in (1)
does not bound (47); it supplies the other factor in (39).

# 10. Deligne reading and what has actually been transferred

The six supplied S20 parts were reassembled in this turn. Their individual
chunk hashes matched, and the assembled archive has 216,580,466 bytes and
SHA-256 `e2005bf31e1fcf362765f73c315c855e0f504f24f34d3a0ab188049da522b7c8`.
This verifies the supplied bytes, not every transcription claim in them.

I read the TeX for Definition 1.3.5, Lemmas 3.2.10--3.2.12, the tensor argument
3.2.13, and Corollary 3.3.6 in the nested source files. I compared those exact
passages with the supplied top-level French/English frozen page records at
printed pages 158, 203, and 206. No PDF text extraction or OCR was used.
The source review records a genuine inherited transcription fault: old
`fr_seg2.tex` writes a weight bound $\le2$ at 3.2.10, whereas the controlling
page record says $<2$; only the latter, with integrality, implies $\le1$.
The old file also corrupts the explicit squared-eigenvalue step in 3.2.13.
Those old files remain unmodified; they are not used as authority for these
comparisons. No claim of a full independent audit of Weil II is made.

Deligne's determinant/rank operation and the upper/dual-lower architecture remain
attached to the programme's specified exterior and residue maps. Here the
additional estimate is a characteristic-zero analytic estimate for the actual
source, (1), followed by the endpoint selection (39). This is not a statement
that the new base satisfies Deligne's finite-field hypotheses. The remaining
volume estimate has not been inferred from purity, positivity of a Gram, or the
mere existence of the support.

The new result is therefore a completed analytic component of the current route:
its two endpoint monic norms have the required $O_h(q_k)$ scale on the actual
quartet window. The other session's four-volume theorem now leaves the explicitly
specified relation-volume cost as the remaining quantitative input on that
window.

# 11. Proof and computation status

Sections 3--7 contain the new written analytic argument. Sections 8--9 contain
explicit finite comparisons and a handoff for checking them using the existing
quotient and matrix library. The standard complex-analysis, gamma and Legendre
facts used in the argument are proved to the extent needed or referenced below.
No general novelty claim is made for these classical ingredients.

The accompanying checker tests finite exact identities: coordinate factors,
Legendre extremal norms, the local algebra in the interval argument, convolution
moments on declared Laplace models, source quotients, block updates, raw
confluent-jet endpoint factors, the volume telescope, and retained support cases.
These tests do not certify the analytic inequalities by sampling them. There is
no new Lean certificate and no interval-certified value of $C_h$.

This continuation makes no remote changes. The integration files are add-only,
and the parallel formalization branches and the reader's existing sources are
left untouched.

# References and pinned inputs

- Deligne, P. *La conjecture de Weil. II*. Publications Mathématiques de l'IHÉS
  **52** (1980), 137--252. Supplied S20 source and current page-local records;
  the selected reading and discrepancies are itemized in `SOURCE_REVIEW.md`.
- NIST Digital Library of Mathematical Functions: §§25.4 (zeta functional
  equation), 5.11 (gamma estimates), 18.3 and 18.5 (Legendre polynomials).
  Public source pages consulted: https://dlmf.nist.gov/25.4,
  https://dlmf.nist.gov/5.11, https://dlmf.nist.gov/18.3,
  https://dlmf.nist.gov/18.5.
- Original programme: the delivered *Tau Gamma Convolution Descent*,
  *Tau Toda Volume Control*, *Tau Cyclic Sum Control*, and *Tau Exterior Trace
  Amplification* notes. Their definitions of the source, action, unit and
  canonical quotient are retained; this is not a complete replay of all their
  upstream analytic claims.
- Parallel endpoint criterion: PR #23,
  `c720f40530eed2f5969dbabe94dfd3fddc0f507f`,
  `workbenches/tau-toda-volume-formal/ENDPOINT_CRITERION.md`.
- Parallel confluent transfer: PR #24,
  `dfcbba5cbf7fec8c9301fe242c13e741d762013e`,
  `workbenches/tau-confluent-transfer/RESEARCH_NOTE.md`.
- Inspected main: `b32ca2128e0deb0eec6eafb860776a5d6a28dcbb`, after its
  merge of the original-Gram exterior/trace contribution.
