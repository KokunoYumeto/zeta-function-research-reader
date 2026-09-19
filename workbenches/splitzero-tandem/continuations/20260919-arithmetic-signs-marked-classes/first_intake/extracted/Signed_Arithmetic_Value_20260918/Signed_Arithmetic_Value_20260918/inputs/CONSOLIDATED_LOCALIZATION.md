# Signed arithmetic baseline: consolidation and localization

18 September 2026. A written mathematical continuation on the original fixed-packet domain. The two incoming continuations are retained verbatim in `inputs/`. This note identifies their overlap exactly, preserves the stronger statements, and proves additional endpoint and degree-band estimates. It does not claim that the full signed arithmetic coefficient has been evaluated.

## Result reached

Write the original signed baseline as

\[
\delta_k=\mathcal B_k[m_k]-\mathcal B_k[\sigma],\qquad
\mathcal B_k[\nu]=\log\det G_{q-1}[\nu]+\log\det G_q[\nu]
-\log\det G_{2q-1}[\nu]-\log\det G_{2q}[\nu].
\]

Let \(C_k=[-kb,kb]\), with \(b\) the original boundary-tilted mean. Define the outer-only density, including its exact central value, by

\[
\omega_k(y)=
\begin{cases}\sigma(y),&y\in C_k,\\
\mathfrak M^{-k}m_k(y),&y\notin C_k.
\end{cases}
\]

The new decomposition, with all four original signs, is

\[
\boxed{\delta_k=\delta_k^{\rm out}+\widehat\Phi_{q,k}+\mathfrak e_k,
\qquad \delta_k^{\rm out}=\mathcal B_k[\omega_k]-\mathcal B_k[\sigma],}
\tag{R1}
\]

\[
\boxed{\widehat\Phi_{q,k}\ge0,\quad
|\mathfrak e_k|\le E_k=O_h(k(\log q)^2)=o_h(q).}
\tag{R2}
\]

Here \(\widehat\Phi_{q,k}\) is given in Section 8 by four explicit Gamma determinants of size

\[
r=O_h(k\log q)=o(q).
\]

Its entries use only the fixed one-factor tilted mass \(M(\theta)\), the original Gamma polynomials, and finite integrals on \(C_k\). The actual convolution density outside \(C_k\) remains solely in \(\delta_k^{\rm out}\). No original arithmetic kernel is substituted by rank or by an asserted isometry.

There is a further bound on the central endpoint contribution

\[
\delta_k^{\rm cen,end}:=\mathcal B_k[m_k]-\mathcal B_k[\omega_k]:
\]

\[
\boxed{\delta_k^{\rm cen,end}=O_h(k^2),\qquad
\liminf\frac{\delta_k^{\rm cen,end}}{k^2}\ge0.}
\tag{R3}
\]

Consequently its coefficient at the \(q\log k\) scale is zero, with an \(O_h(q)\) remainder, on every fixed multiplicity stratum. On each fixed stratum \(m_0\ge2\), this entire central endpoint contribution is \(o_h(q)\). On the simple stratum \(m_0=1\), its order-\(q\) value is reduced to \(\widehat\Phi_{q,k}\) with an \(o(q)\) error, but that limiting value is not calculated in this note.

The outer term in (R1) is still unevaluated at the requested scales. In particular this note does not assign the full baseline's \(q\log k\) coefficient or its order-\(q\) coefficient.

---

## 1. Original source, exact coordinates, and consolidation

Retain the original stipulated quartet, its complete multiplicity, its full arithmetic amplitude, and its original tensor orders:

\[
\rho=\tfrac12+\delta+i\gamma,\quad 0<\delta<\tfrac12,\quad\gamma>2,
\qquad h(s)=\prod_{z\in\{\rho,\bar\rho,1-\rho,1-\bar\rho\}}(s-z)^{m_0},
\]

\[
v_h=2\xi/h,\qquad w_h(y)=|v_h(1/2+iy)|^2/(2\pi),\qquad m_k=w_h^{*k},
\]

\[
k=4l+1\ge5,\quad e=1+k(m_0-1),\quad q=e(k+1)^2,\quad c=k/2,
\]

\[
\chi_k(S)=\prod_{a,b_0=0}^k
\bigl(S-c-(2a-k)\delta-i(2b_0-k)\gamma\bigr)^e.
\]

This retains the programme's stipulated packet; it does not supply or assert an actual numerical off-critical zero.

The reference source is

\[
\sigma(y)=\frac{|\Gamma(1/4+iy/2)|^2}{2\pi},\quad
\sigma(\mathbb R)=\sqrt{2\pi},\quad\alpha=\pi/2.
\]

The original change of polynomial coordinates is

\[
\mathcal U_N:P(S)\longmapsto P(c+iy),\qquad
Q(y)=i^{-q}\chi_k(c+iy).
\tag{C1}
\]

Its inverse is substitution \(y=(S-c)/i\); its coefficient determinant has modulus one. Moreover

\[
\mathcal U_N(\chi_kP)=i^q Q\,\mathcal U_{N-q}P.
\]

Thus it carries the complete relation ideal, every remainder class and the degree cutoffs to their displayed real-coordinate versions. The phase has modulus one. We use the corresponding source norm, not an independent norm on the transported coefficients. For monic norms, the additional phase \(i^{-\deg P}\) restores real-coordinate monicity exactly. The original full-unit inclusion is transported by this coefficient isomorphism; its arithmetic coefficients are not set to one.

Let \(H_N[\nu]\) be the Gram of \(1,y,\ldots,y^N\), \(J_N\) the remainder map modulo \(Q\), and

\[
G_N[\nu]=(J_NH_N[\nu]^{-1}J_N^*)^{-1}.
\]

The original monic source/relation frame gives

\[
\det G_N[\nu]=\frac{\det H_N[\nu]}{\det H_N^{\rm rel}[\nu]},
\tag{C2}
\]

where the relation frame is \(Q,yQ,\ldots,y^{N-q}Q\). Empty determinants are one. Its frame determinant is one; both cross blocks remain in the Schur complement. Equivalently,

\[
\mathcal B_k[\nu]=\sum_{j=0}^q c_j
\log\frac{\nu_j[\nu]}{\gamma_{q+j}[\nu]},\quad
c_0=c_q=1,\quad c_j=2\ (0<j<q),\quad \sum c_j=2q.
\tag{C3}
\]

Here \(\nu_j\) and \(\gamma_{q+j}\) are the attained monic relation and source norms, respectively. We use (C2) and (C3), rather than redefining the original baseline.

### Exact dictionary between the incoming calculations

Use

\[
M(\theta)=\int e^{\theta y}w_h(y)\,dy,\quad L=\log M,
\quad \mu=L',\quad V=L'',\quad
\mathfrak M=M(\alpha),\quad b=\mu(\alpha),
\]

and let \(\theta(t)\) invert \(\mu\) on \([-\alpha,\alpha]\). For \(0\le t\le b\), define

\[
D(t)=L(\alpha)-L(\theta(t))-(\alpha-\theta(t))t.
\tag{C4}
\]

The first continuation's \(\ell_h,a_h,v_h^{\rm tilt},\mu_h\) are respectively the second continuation's \(L,\mu,V,b\). Their rate functions satisfy the literal equality

\[
\boxed{F_h^{\rm cen}(t)=-D(|t|).}
\tag{C5}
\]

The integral coefficients are also equal, without a limiting identification:

\[
\boxed{\mathscr C_h=\mathfrak I_h^{\rm cen}
=\int_0^\alpha\mu(\theta)^2\,d\theta=:I_h,}
\]

\[
\boxed{\mathscr B_h=\mathfrak J_h^{\rm cen}
=\int_0^\alpha V(\theta)
\log\frac{\mu(\theta)}{4\pi V(\theta)}\,d\theta=:J_h.}
\tag{C6}
\]

The second integral converges at zero because \(\mu(\theta)\) is comparable to \(\theta\) there. Both incoming notes therefore calculate the same central density profile and the same two coefficients. The first retains a stronger explicit remainder and a source-to-quotient comparison; the second supplies a complete standalone proof and the sharper relation-kernel weight count \(2q\) instead of the valid larger count \(2q+1\). All are retained below, once.

### Consolidated source estimate

The local estimate in the incoming ACW10--11 is

\[
p_\theta^{*k}(k\mu(\theta))
=\frac{1+\varepsilon_{k,\theta}}{\sqrt{2\pi kV(\theta)}},
\quad p_\theta(y)=\frac{e^{\theta y}w_h(y)}{M(\theta)},
\quad |\varepsilon_{k,\theta}|\le\epsilon_k=O_h(k^{-1/8}).
\tag{C7}
\]

The exact inverse accounting is

\[
m_k(x)=M(\theta)^k e^{-\theta x}p_\theta^{*k}(x).
\tag{C8}
\]

This follows from the original addition map \(\sum y_j=x\). It retains the mass \(M(\theta)^k\). At the auxiliary Hilbert-space level the isometry is
\(F\mapsto M(\theta)^{1/2}e^{-\theta y/2}F\) from \(L^2(w_hdy)\) to \(L^2(p_\theta dy)\); it is not asserted to preserve polynomial degree.

Put \(c_\sigma(y)=\sigma(y)e^{\alpha|y|}\sqrt{1+|y|}\). On \(|t|\le b\),

\[
\ell_k(kt):=\log\frac{m_k(kt)}{\mathfrak M^k\sigma(kt)}
=-kD(|t|)+\tfrac12\log(|t|+k^{-1})
-\tfrac12\log(2\pi V(\theta(t)))-\log c_\sigma(kt)
+\log(1+\varepsilon_{k,\theta(t)}).
\tag{C9}
\]

The full origin term is present. With \(L_k^{\rm loc}=-\log(1-\epsilon_k)\) on \(\epsilon_k\le1/2\), the consolidated finite bound is

\[
\left|\int_{-kb}^{kb}\ell_k(y)dy+k^2I_h-kJ_h\right|
\le 2kbL_k^{\rm loc}+(kb+1)\log(kb+1)-kb\log(kb)
+2C_\Gamma^0+4\log^+(kb),
\tag{C10}
\]

\[
C_\Gamma^0=\max\{|\log(c_\Gamma/\sqrt2)|,
|\log(C_\Gamma/\sqrt2)|\}.
\]

In particular the error in (C10) is \(O_h(k^{7/8}+\log k)\), which implies the second note's \(o(k)\) remainder. To recover (C10) from the standalone note, use the complex Stirling bound
\(|R_\Gamma(z)|\le1/(6|z|)\) for \(\Re z>0\) in the principal term at \(z=1/4+iy/2\). Direct substitution gives

\[
|\log c_\sigma(y)-\tfrac12\log2|\le2/y\quad(y\ge1).
\]

The original Gamma envelopes control \([0,1]\). The exact integral
\(k\int_0^b\log(1+(kt)^{-1})dt
=(kb+1)\log(kb+1)-kb\log(kb)\)
and (C9) prove the bound. The rate-area identity is
\(2\int_0^bD(t)dt=I_h\), proved by Fubini or integration by parts using \(\mu'=V\).

The source-coordinate approximation in the first note is retained as well. Define \(\bar m_k\) from (C7)--(C8) by omitting \(1+\varepsilon\) on \(C_k\), and by setting \(\bar m_k=m_k\) outside \(C_k\). The identity on every original affine remainder fibre gives

\[
(1-\epsilon_k)G_N[\bar m_k]\preceq G_N[m_k]
\preceq(1+\epsilon_k)G_N[\bar m_k],
\]

\[
|\mathcal B_k[m_k]-\mathcal B_k[\bar m_k]|
\le2q\log\frac{1+\epsilon_k}{1-\epsilon_k}=o(q).
\tag{C11}
\]

(C10) is not assigned as a determinant coefficient. The additional work below controls an actual endpoint determinant response.

---

## 2. Retained source constants and local-error formula

The only arithmetic envelope inputs used are RTM1--3 and the original three-factor lower bound:

\[
e^{\alpha|y|}w_h(y)\le C(1+|y|)^{-p},\quad
p=8m_0-9/2,\quad
w_h^{*3}(y)\ge c_h e^{-\alpha|y|}(1+|y|)^{-B},
\quad B=42+8m_0,\quad M_*=B/2,
\tag{L1}
\]

\[
c_\Gamma e^{-\alpha|y|}(1+|y|)^{-1/2}\le\sigma(y)
\le C_\Gamma e^{-\alpha|y|}(1+|y|)^{-1/2},
\quad c_\Gamma=\sqrt2e^{-7/6},\quad C_\Gamma=\sqrt{2\sqrt5}e^{2/3}.
\]

The global upper convolution envelope is

\[
m_k(y)\le\frac C{c_\Gamma}k^{p+1}\mathfrak M^{k-1}\sigma(y).
\tag{L2}
\]

For clarity, the finite local-error constants from the standalone note are reproduced. Let \(\eta=1/4\), \(M_0=M(0)\), and

\[
V_* =\frac{2C}{M_0}{\rm B}(3,p-3),\quad
H_* =2^{1+\eta}\left[\frac{2C}{M_0}{\rm B}(3+\eta,p-3-\eta)+b^{2+\eta}\right],
\]

\[
a_* =\min\left\{\tfrac14,\frac{c_he^{-2\alpha}2^{-B}}{\mathfrak M^3}\right\},
\quad\beta=2a_*,\quad v_*=\beta/9,
\]

\[
\xi_0=\min\left\{1,(2V_*)^{-1/2},
(v_*/(16H_*))^{1/\eta}\right\},\quad
r_*=(1-\beta\xi_0^2/7)^{1/3},\quad
C_2=\frac{4\pi(C/M_0)^2}{2p-1},\quad C_0=4H_*+V_*^2/8.
\]

For an integer \(n\ge2\), put \(a_n=v_*(n-1)/4\) and

\[
A_n^{\rm loc}=\frac1{2\pi}\left[
C_0n\,\Gamma((3+\eta)/2)a_n^{-(3+\eta)/2}
+C_2r_*^{n-2}+
\frac{2e^{-nv_*\xi_0^2/2}}{nv_*\xi_0}\right],
\quad\epsilon_n=\sqrt{2\pi nV_*}\,A_n^{\rm loc}.
\tag{L3}
\]

These retain \(v_*\le V(\theta)\le V_*\). They are local-limit constants, not the arithmetic upper-envelope symbol in (L2).

The Fourier proof of (C7) establishes slightly more than its displayed mean value. The same absolute error holds at every shifted evaluation point:

\[
\boxed{\left|p_\theta^{*n}(n\mu(\theta)+x)
-\frac{e^{-x^2/(2nV(\theta))}}{\sqrt{2\pi nV(\theta)}}\right|
\le A_n^{\rm loc},\quad x\in\mathbb R.}
\tag{L4}
\]

Indeed, Fourier inversion inserts the factor \(e^{-i\xi x}\), of modulus one, into the very same integrable difference estimated in ACW6--10. No additional moment or large-deviation hypothesis is needed.

## 3. Closing the transition gap and extracting the full central rate

Define

\[
W_k(y)=\begin{cases}kD(|y|/k),&|y|\le kb,\\0,&|y|>kb,
\end{cases}\quad
D_0=D(0)=L(\alpha)-L(0)>0,\quad\Lambda_k=kD_0.
\tag{L5}
\]

Then \(0\le W_k\le\Lambda_k\). Define the exact remaining factor

\[
\psi_k(y)=\frac{m_k(y)}{\mathfrak M^k\sigma(y)}e^{W_k(y)}.
\quad\text{Thus}\quad
\boxed{\mathfrak M^{-k}m_k=\psi_k e^{-W_k}\sigma.}
\tag{L6}
\]

This factorization changes neither the source nor the packet. Its significance is the new whole-line polynomial bound proved next.

Set \(n=k-3\), \(V_b=V(\alpha)\), and
\(a_G=e^{-1/2}/(2\sqrt{2\pi})\). Work on the explicit cofinal range

\[
\epsilon_k\le1/2,\qquad
\epsilon_{k-3}\le e^{-1/2}/2,\qquad
k\ge V_b/b^2.
\tag{L7}
\]

By (L4), the tilted convolution places mass at least \(a_G\) in

\[
I_n=[nb-\sqrt{nV_b},nb].
\]

On this interval the Gaussian density is at least
\(e^{-1/2}/\sqrt{2\pi nV_b}\), and the error is at most half this value. Integrating over the length \(\sqrt{nV_b}\) proves the mass bound.

For every \(y\ge kb\) and \(z\in I_n\),

\[
0<y-z\le y+\sqrt{nV_b}\le2y.
\]

Apply the original three-factor lower bound within the exact convolution and retain the full tilted mass. This gives

\[
\boxed{m_k(y)\ge c_h a_G\mathfrak M^{k-3}e^{-\alpha y}(1+2y)^{-B},
\qquad y\ge kb.}
\tag{L8}
\]

Evenness gives the negative half-line. In contrast to the old positive-width guard beyond the boundary-tilted mean, this bound starts at \(|y|=kb\) itself. In particular there is no untreated interval between the saddle window and the retained tail.

Divide (L8) by the upper Gamma envelope and use
\(1+2y\le\sqrt5\sqrt{1+y^2}\). Define

\[
c_{\rm tail}=\frac{c_h a_G}{\mathfrak M^3C_\Gamma 5^{M_*}},
\quad
c_{\rm core}=\frac1{2\sqrt{2\pi V_*}C_\Gamma},
\quad
C_{\rm core}=\frac{3\sqrt{b+1}}{2\sqrt{2\pi v_*}c_\Gamma}.
\]

From (C9), on the core,
\(c_{\rm core}k^{-1/2}\le\psi_k\le C_{\rm core}\). Set

\[
c_- =\min\{1,c_{\rm tail},c_{\rm core}\},\qquad
c_+=\max\{1,C_{\rm core},C/(c_\Gamma\mathfrak M)\}.
\]

Then the exact whole-line result is

\[
\boxed{c_-k^{-1/2}(1+y^2)^{-M_*}\le\psi_k(y)
\le c_+k^{p+1}.}
\tag{L9}
\]

The factor \(\omega_k/\sigma\) satisfies the same bounds: it is one on \(C_k\), and equals \(\psi_k\) off \(C_k\). This statement retains the actual zeta-dependent density on the whole outer line. The original exponential-in-\(k\) variation is now in the explicit factor \(e^{-W_k}\), not hidden in a comparison constant.

## 4. Polynomial comparison also holds after inserting the rate

Write \(d=2q\) and \(d\tau_t=e^{-tW_k}\sigma(y)dy\), \(0\le t\le1\). Impose the explicit eventual guard

\[
\Lambda_k\le d\log16.
\tag{L10}
\]

For every polynomial \(P\) of degree at most \(d\),

\[
\boxed{\int y^2|P|^2d\tau_t\le272(d+1)^2\|P\|_{\tau_t}^2.}
\tag{L11}
\]

Here is a proof retaining the whole tail. The original Gamma recurrence bounds multiplication by \(y\) on degree \(j\) by \(2(j+1)\). Hence

\[
\|y^{d+1}P\|_\sigma^2\le[4(d+1)]^{2d+2}\|P\|_\sigma^2.
\]

On \(|y|>16(d+1)\), this bounds the second-moment tail by

\[
16(d+1)^2\,16^{-d}\|P\|_\sigma^2
\le16(d+1)^2e^{\Lambda_k}16^{-d}\|P\|_{\tau_t}^2.
\]

The inner part is at most \(256(d+1)^2\|P\|_{\tau_t}^2\). Guard (L10) proves (L11). This argument does not infer a tail estimate merely by dropping the core suppression.

Jensen's inequality for \(x\mapsto(1+x)^{-M_*}\), applied to the measure \(|P|^2d\tau_t/\|P\|_{\tau_t}^2\), now proves

\[
L_k\|P\|_{\tau_t}^2\le\|P\|_{\psi_k\tau_t}^2
\le U_k\|P\|_{\tau_t}^2,
\]

\[
L_k\|P\|_{\tau_t}^2\le\|P\|_{(\omega_k/\sigma)\tau_t}^2
\le U_k\|P\|_{\tau_t}^2,
\tag{L12}
\]

where

\[
L_k=c_-k^{-1/2}[1+272(d+1)^2]^{-M_*},\quad
U_k=c_+k^{p+1},\quad\kappa_k=U_k/L_k\ge1.
\tag{L13}
\]

Thus \(\log\kappa_k=O_h(\log q)\). The same scalar inequalities hold on every fixed restriction and every attained quotient of these polynomial spaces: apply them to every representative in its specified affine fibre before taking the minimum. This is the comparison used in the next section; no metric equality is asserted.

## 5. A fixed Taylor-jet kernel sees exponentially little central mass

Let \(b_j\) be the original Gamma monic polynomials, and

\[
\gamma_j=\sqrt{2\pi}\,j!(1/2)_j
=\sqrt{2\pi}(2j)!/4^j,\quad \varphi_j=b_j/\sqrt{\gamma_j}.
\]

Their exact generating function, equivalently derived by summing their recurrence, is

\[
\sum_{j\ge0}\frac{b_j(z)}{j!}t^j
=(1+t^2)^{-1/4}\exp(z\arctan t).
\tag{L14}
\]

This is the original-coordinate Meixner--Pollaczek generating function; it is also DLMF 18.23.7 after \(\lambda=1/4,x=z/2,\varphi=\pi/2\).

Cauchy's estimate on \(|t|=(d+1)/(d+2)\), together with
\(|\arctan t|\le\frac12\log(2(d+2))\), gives, for \(|z|\le Z\),

\[
\sum_{j=0}^d|\varphi_j(z)|^2
\le\frac{e^2(d+1)^2\sqrt{d+2}}{\sqrt{2\pi}}
[2(d+2)]^Z.
\tag{L15}
\]

The factorial estimate used here is
\((j!)^2/\gamma_j\le(2j+1)/\sqrt{2\pi}\), and
\(\sum_{j=0}^d(2j+1)=(d+1)^2\). This preserves the original Gamma mass.

Let \(K=kb\), and let \(\mathcal J_rP\) be the first \(r\) Taylor coefficients at zero. Its kernel is the literal subspace

\[
Z_{N,r}=y^r\mathcal P_{N-r}\subset\mathcal P_N.
\tag{L16}
\]

For \(P\in Z_{N,r}\), \(N\le d\), apply Cauchy's coefficient formula on \(|z|=2K\) and sum the geometric tail on \(|y|\le K\). Equation (L15) and the full mass \(\sqrt{2\pi}\) give

\[
\boxed{\int_{C_k}|P|^2d\sigma\le a_{k,r}\|P\|_\sigma^2,\qquad
 a_{k,r}=4^{1-r}\mathcal A_{q,k},}
\tag{L17}
\]

\[
\mathcal A_{q,k}=e^2(d+1)^2\sqrt{d+2}[2(d+2)]^{2K}.
\]

There is also an operator version. Let \(B_N\) restrict a polynomial in the Gamma orthonormal frame to \(L^2(C_k,\sigma dy)\), and let \(\widetilde B_{N,r}\) first truncate its Taylor series below degree \(r\), then restrict. The same calculation proves

\[
\|B_N-\widetilde B_{N,r}\|\le\sqrt{a_{k,r}},\qquad
\operatorname{rank}\widetilde B_{N,r}\le r.
\tag{L18}
\]

Choose the explicit integer

\[
\boxed{r=\left\lceil 1+
\frac{\log\mathcal A_{q,k}+2\Lambda_k+2\log\kappa_k
+10\log q+\log256}{\log4}\right\rceil.}
\tag{L19}
\]

Use its explicit eventual guard \(r\le q\). Then

\[
a:=a_{k,r}\le\frac{e^{-2\Lambda_k}}{256\kappa_k^2q^{10}},
\quad r=O_h(k\log q)=o(q).
\tag{L20}
\]

This Taylor map is an auxiliary estimate and computational compression. It is not the programme's period observation and is not identified with its kernel. Its exact relation to each determinant is the Schur factorization used next.

## 6. Transfer the nonlinear central loss through the actual metrics

For \(g=1\) or \(g=\psi_k\), define the full source loss

\[
D_N(g)=\log\det H_N[g\sigma]-\log\det H_N[ge^{-W_k}\sigma]\ge0.
\tag{L21}
\]

Decompose \(\mathcal P_N\) by the exact sequence

\[
0\longrightarrow Z_{N,r}\longrightarrow\mathcal P_N
\xrightarrow{\mathcal J_r}\mathbb C^r\longrightarrow0.
\]

The quotient metric is the attained one,
\(G_{N,r}^{\rm jet}[\nu]=(\mathcal J_rH_N[\nu]^{-1}\mathcal J_r^*)^{-1}\).
Its Schur complement retains both cross factors and the full high-monomial Gram inverse. The determinant factors into the restriction determinant and this quotient determinant, in a fixed monic frame.

On the restriction \(Z_{N,r}\), insertion of \(e^{-W_k}\) loses at most \(a\) of the Gamma norm, and at most \(\kappa_k a\) of the \(\psi_k\sigma\) norm, by (L12) and (L17). Put \(f(x)=-\log(1-x)\) for \(0\le x<1\). The two restriction losses lie between zero and \((N+1-r)f(\kappa_k a)\).

On the jet quotient, (L12) bounds the relative determinant at both \(t=0\) and \(t=1\) in the same interval \([r\log L_k,r\log U_k]\). Subtracting those endpoints, before taking absolute values, gives

\[
\boxed{|D_N(\psi_k)-D_N(1)|
\le r\log\kappa_k+(N+1-r)f(\kappa_k a).}
\tag{L22}
\]

This is a comparison of the nonlinear, finite-amplitude central loss. It is not a first variation at the Gamma source.

Define

\[
\Phi(g)=D_{2q-1}(g)+D_{2q}(g)-D_{q-1}(g)-D_q(g).
\]

Adding the four estimates proves

\[
|\Phi(\psi_k)-\Phi(1)|
\le4r\log\kappa_k+(6q+2)f(\kappa_k a).
\tag{L23}
\]

### Remove the central prefactor, without changing the outer density

The two densities \(\psi_k\sigma\) and \(\omega_k\) agree off \(C_k\). On \(C_k\) their difference has absolute value at most \(2U_k\sigma\). On \(Z_{N,r}\), (L17) and (L12) therefore bound the relative change by \(2\kappa_k a\). On the jet quotient the relative spectrum lies in \([\kappa_k^{-1},\kappa_k]\), giving absolute log determinant at most \(r\log\kappa_k\). Thus their full source determinant difference, at each endpoint, is bounded by

\[
r\log\kappa_k+(N+1-r)f(2\kappa_k a).
\tag{L24}
\]

The original relation part is included in Section 7. Equations (L22)--(L24) are why a polynomial bound on the remaining factor suffices: it is charged on \(r=O(k\log q)\) quotient coordinates, not on all \(q\) coordinates independently.

## 7. Retain the original relation determinant and its sign

Set

\[
R=k\sqrt{\delta^2+\gamma^2},\quad Y=2^{-16}q,\quad
B_\chi=\frac{qR^2}{Y^2-R^2},
\]

\[
\eta_0=\frac{\sqrt{2\pi}}{c_\Gamma}
\frac{(2q+1)(4q+1)\sqrt{1+2q}}q16^{-q},\qquad
\eta_\Gamma=\frac{e^{B_\chi}\eta_0}{1-\eta_0}.
\tag{L25}
\]

Use the original cofinal guards \(q\ge100,R\le Y/4,K\le Y\). For every polynomial \(P\) of degree at most \(q\), the retained full-primary estimate is

\[
\int_{C_k}|QP|^2d\sigma\le\eta_\Gamma\|QP\|_\sigma^2.
\tag{L26}
\]

It follows by pairing the original opposite roots outside \([-Y,Y]\) and by the full shifted-Legendre expansion on \([q,2q]\) inside. The inner polynomial bound is

\[
|P(y)|^2\le\frac{(2q+1)(4q+1)100^{2q}}q
\int_q^{2q}|P(t)|^2dt,
\]

while the reference power norm is at least
\(c_\Gamma q^{2q}e^{-\pi q}(1+2q)^{-1/2}\int_q^{2q}|P|^2\).
The inner multiplier is at most \([(9/4)2^{-32}q^2]^q\), and
\((9/4)e^\pi10^4 2^{-32}<1/16\). These bounds give (L26) with both inner contributions and the full mass retained. This is also ACW27--29 in the frozen standalone note.

By (L12), the central fraction in the \(\psi_k\sigma\) relation norm is at most \(\kappa_k\eta_\Gamma\). Hence insertion of \(e^{-W_k}\) changes each attained monic relation norm by a factor in
\([1-\kappa_k\eta_\Gamma,1]\). Its full weighted loss is

\[
0\le\Psi^{\rm rel}(\psi_k)
:=\sum_{j=0}^qc_j\log\frac{\nu_j[\psi_k\sigma]}
{\nu_j[\psi_ke^{-W_k}\sigma]}
\le2q f(\kappa_k\eta_\Gamma).
\tag{L27}
\]

The exact source/relation identity gives the signed equation

\[
\mathcal B_k[\psi_ke^{-W_k}\sigma]-\mathcal B_k[\psi_k\sigma]
=\Phi(\psi_k)-\Psi^{\rm rel}(\psi_k).
\tag{L28}
\]

Thus the relation contribution has not been assigned zero or the wrong sign.

For the central prefactor comparison between \(\psi_k\sigma\) and \(\omega_k\), the analogous relative relation-Gram error is at most \(2\kappa_k\eta_\Gamma\). The sum of the four relation dimensions is \(2q+2\). Its absolute signed log-determinant contribution is bounded by

\[
(2q+2)f(2\kappa_k\eta_\Gamma).
\tag{L29}
\]

Use the explicit eventual guard \(2\kappa_k\eta_\Gamma\le1/2\). Both (L27) and (L29) are exponentially small: \(\eta_\Gamma=\exp[-q\log16+O_h(\log q+1)]\), and \(\kappa_k\) is polynomial in \(q,k\).

## 8. Four explicit Gamma matrices, with a finite total error

The Gamma loss \(D_N(1)\) can be evaluated with no source interpolation. Define the central moment matrix

\[
M_{W,k}[i,j]=\int_{-K}^{K}
(1-e^{-W_k(y)})y^{i+j}\sigma(y)dy,
\qquad0\le i,j<r.
\tag{L30}
\]

Let

\[
T_{r,N}[j,n]=[y^j]\varphi_n(y),\qquad
E_{r,N}=T_{r,N}T_{r,N}^*,\quad 0\le n\le N.
\tag{L31}
\]

All entries in \(T\) come from (L14) or the exact Gamma recurrence. All entries in \(M_{W,k}\) come from the fixed function (C4) on a finite interval. Define

\[
\widehat D_N=-\log\det(I_r-M_{W,k}^{1/2}E_{r,N}M_{W,k}^{1/2}),
\]

\[
\boxed{\widehat\Phi_{q,k}
=\widehat D_{2q-1}+\widehat D_{2q}-\widehat D_{q-1}-\widehat D_q.}
\tag{L32}
\]

The square root can be avoided in a determinant computation using
\(\det(I_r-M_{W,k}E_{r,N})\), by Sylvester's determinant identity. Its positive self-adjoint representative is the displayed one; a non-Hermitian coordinate matrix is not silently treated as Hermitian.

To prove the approximation, let \(C_N\) be the Gamma compression of multiplication by \((1-e^{-W_k})1_{C_k}\). Then
\(D_N(1)=-\log\det(I-C_N)\), and \(I-C_N\succeq e^{-\Lambda_k}I\).
By (L18), its Taylor approximation \(\widetilde C_N=T^*M_{W,k}T\) satisfies

\[
\|C_N-\widetilde C_N\|\le2\sqrt a+a.
\]

Put \(z_k=e^{\Lambda_k}(2\sqrt a+a)\). Equation (L20) gives \(z_k<1/2\), so the approximate matrix is positive and

\[
|D_N(1)-\widehat D_N|\le(N+1)f(z_k).
\tag{L33}
\]

For example, conjugate the difference by \((I-C_N)^{-1/2}\); its norm is at most \(z_k\), so every eigenvalue of the relative matrix lies in \([1-z_k,1+z_k]\). This proves (L33) without assuming a small inverse norm independent of the rate depth.

Both \(D_N(1)\) and \(\widehat D_N\) increase with \(N\). For the latter, \(E_{r,N}\) increases in the positive order. For the former, write \(I-C_N\) in successive Gamma coordinates; its new Schur complement is at most one, or use compression interlacing. Hence \(\Phi(1)\ge0\) and \(\widehat\Phi_{q,k}\ge0\).

Combining (L23), (L24), (L27)--(L29), and (L33) yields (R1) with the fully explicit radius

\[
\boxed{\begin{aligned}
E_k={}&8r\log\kappa_k+(6q+2)
\{f(\kappa_k a)+f(2\kappa_k a)+f(z_k)\}\\
&+(2q+2)f(2\kappa_k\eta_\Gamma)
+2qf(\kappa_k\eta_\Gamma).
\end{aligned}}
\tag{L34}
\]

Every quantity on this right-hand side is given above. It contains no original growing Gram inverse. The prescribed rank gives

\[
E_k=O_h(k(\log q)^2)=o_h(k^2)=o_h(q).
\tag{L35}
\]

The pointwise relative approximation in (C11) is not being charged again; (L34) is a direct estimate on the actual source. In particular it is stronger at this stage than multiplying the earlier local-limit error by an assumed constant kernel density.

## 9. The central degree-band response is only \(O_h(k^2)\)

The rank \(r=O(k\log q)\) establishes the transfer, but a separate exact recurrence argument improves the size of the response itself. This is essential for the scale conclusion in (R3).

The Gamma orthonormal recurrence is

\[
y\varphi_n=a_{n+1}\varphi_{n+1}+a_n\varphi_{n-1},\qquad
a_n=\sqrt{n(n-1/2)}.
\tag{L36}
\]

Consider either original degree band \(n=n_0,\ldots,n_0+q-1\), where \(n_0=q\) or \(q+1\). Relative to the two initial functions \(\varphi_{n_0},\varphi_{n_0-1}\), write

\[
\varphi_n(y)=A_n(y)\varphi_{n_0}(y)+B_n(y)\varphi_{n_0-1}(y).
\tag{L37}
\]

These coefficients are obtained by the actual transfer matrices

\[
\begin{pmatrix}\varphi_{n+1}\\\varphi_n\end{pmatrix}
=\begin{pmatrix}z/a_{n+1}&-a_n/a_{n+1}\\1&0\end{pmatrix}
\begin{pmatrix}\varphi_n\\\varphi_{n-1}\end{pmatrix}.
\]

At \(z=0\) each transfer has norm one because \(a_n<a_{n+1}\). Its norm at \(z\) is at most \(1+|z|/a_{n+1}\). There are fewer than \(q\) factors, and \(a_{n+1}\ge q\), so

\[
|A_n(z)|,|B_n(z)|\le e^{|z|}.
\tag{L38}
\]

This removes the common high-degree oscillation by an exact two-function representation, not by an asymptotic kernel substitution.

Truncate \(A_n,B_n\) below Taylor degree \(s\), applying Cauchy's formula on \(|z|=2K\). The restriction map from this Gamma-orthonormal degree band to \(L^2(C_k,\sigma dy)\) then has a rank-at-most \(2s\) approximation, with operator error at most

\[
\nu_s=2^{2-s}\sqrt q\,e^{2K}.
\tag{L39}
\]

Indeed each coefficient tail is at most \(2^{1-s}e^{2K}\); the \(q\) coefficient columns cost \(\sqrt q\), and the two initial functions each have full Gamma norm one. The approximation range is spanned by
\(y^j\varphi_{n_0},y^j\varphi_{n_0-1}\), \(j<s\). No orthogonality of these range functions is assumed. These are auxiliary output functions for the restriction operator, not replacement representatives at the original degree cutoff.

### Retain the complete lower-degree Schur inverse

Let \(V_L,V_H\) be the low-degree and band restriction maps multiplied by \(\sqrt{1-e^{-W_k}}\). The full suppressed source Gram is \(I-V^*V\). Its attained band Gram is exactly

\[
\boxed{S=I-V_H^*\mathcal A_LV_H,\qquad
\mathcal A_L=I+V_L(I-V_L^*V_L)^{-1}V_L^*.}
\tag{L40}
\]

Here the complete preceding source Gram inverse remains. It satisfies
\(\|\mathcal A_L\|\le e^{\Lambda_k}\), and the minimum definition gives
\(S\succeq e^{-\Lambda_k}I\). Thus both possible amplifications of a band approximation must be paid.

Choose

\[
\boxed{s=\left\lceil 2+
\frac{2K+2\Lambda_k+(11/2)\log q+\log8}{\log2}\right\rceil.}
\tag{L41}
\]

Then \(\nu_s\le e^{-2\Lambda_k}q^{-5}/8\). Replacing only \(V_H\) by its rank-\(2s\) approximation changes the matrix in (L40) by at most
\(e^{\Lambda_k}\nu_s(2+\nu_s)\). Relative to \(S\), its norm is at most

\[
u_k=e^{2\Lambda_k}\nu_s(2+\nu_s)\le3q^{-5}/8<1/2.
\]

The approximate band Gram is positive, at least
\(e^{-\Lambda_k}(1-u_k)I\), and differs from the identity in at most \(2s\) directions. Therefore

\[
0\le-\log\det S\le2s\{\Lambda_k+f(u_k)\}+qf(u_k).
\tag{L42}
\]

The lower bound follows from \(S\preceq I\). For the upper bound, bound the at most \(2s\) approximate eigenvalue losses by \(\Lambda_k+f(u_k)\), then use the full \(q\)-dimensional relative log-determinant bound. This argument explicitly preserves the lower-space coupling in (L40).

Each of the two differences making up \(\Phi(1)\) is the loss (L42) on its original band. Hence

\[
\boxed{0\le\Phi(1)\le4s(\Lambda_k+1)+2qf(u_k)=O_h(k^2).}
\tag{L43}
\]

Equations (L33)--(L35) prove (R3). More quantitatively,

\[
\boxed{0\le\liminf\frac{\delta_k^{\rm cen,end}}{k^2}
\le\limsup\frac{\delta_k^{\rm cen,end}}{k^2}
\le\frac{8D_0(b+D_0)}{\log2}.}
\tag{L44}
\]

This is a signed asymptotic interval, not a computed limiting coefficient. It follows directly from \(s/k\to(2b+2D_0)/\log2\), \(\Lambda_k/k=D_0\), and \(E_k/k^2\to0\).

### The scale conclusions on the original multiplicity strata

For every fixed \(m_0\), \(q\ge(k+1)^2\), so

\[
\boxed{\frac{\delta_k^{\rm cen,end}}{q\log k}\longrightarrow0,
\qquad \delta_k^{\rm cen,end}=O_h(q).}
\tag{L45}
\]

On the simple stratum, \(q=(k+1)^2\), (L44) is an explicit nonnegative limiting interval at the \(q\) scale. On every fixed stratum \(m_0\ge2\),
\(q\asymp_{m_0}k^3\), and

\[
\boxed{\delta_k^{\rm cen,end}=o_h(q),\qquad
\delta_k=\delta_k^{\rm out}+o_h(q).}
\tag{L46}
\]

Unlike the incoming unweighted area comparison, (L45)--(L46) are proved for the actual endpoint quotient-determinant contribution with its full relation determinant retained.

## 10. Endpoint accounting, the earlier spatial split, and the receiver

The outer-only density is explicitly \(\omega_k\), and

\[
\delta_k^{\rm out}+\delta_k^{\rm cen,end}
=\mathcal B_k[m_k]-\mathcal B_k[\sigma].
\tag{L47}
\]

The mass cancellation used here is exact: \(G_N[A\nu]=A G_N[\nu]\), so four signs cancel \(q\log A\). It is equivalently the scalar coefficient map \(P\mapsto\sqrt A P\), with the same map on remainder values, between source measures \(\nu\) and \(A^{-1}\nu\).

An isolated spatial central integral along the earlier diagonal interpolation is not identified with this central endpoint difference. Their exact relation can be given. Let

\[
f_C=1_{C_k}\ell_k,\quad f_O=1_{\mathbb R\setminus C_k}\ell_k,
\quad F(a,b_0)=\mathcal B_k[\sigma e^{af_C+b_0f_O}].
\]

The earlier central spatial term is \(\int_0^1F_a(t,t)dt\), whereas the endpoint central term is \(\int_0^1F_a(t,1)dt\). Consequently

\[
\boxed{\delta_k^{\rm cen,end}-\delta_k^{\rm cen,diag}
=\int_0^1\int_t^1F_{ab_0}(t,b_0)\,db_0dt.}
\tag{L48}
\]

The mixed derivative is determined by the original source and relation kernels. For a single full source determinant, differentiation twice gives

\[
\partial_a\partial_{b_0}\log\det H_N
=\operatorname{Tr}(H_N^{-1}H_{N,ab_0})
-\operatorname{Tr}(H_N^{-1}H_{N,b_0}H_N^{-1}H_{N,a}).
\]

The first term is zero since \(f_Cf_O=0\). The second is the negative of
\(\iint f_C(y)f_O(z)|K_N(y,z)|^2d\nu(y)d\nu(z)\).
The relation expression uses its full relation kernel; (C2) and the four signs give \(F_{ab_0}\). This explicitly records the path-interchange contribution, rather than presuming that the earlier two spatial pieces are individually path independent.

The complete action receives the new result as

\[
\boxed{J_k^{\rm action}=\mathcal B_k[\sigma]
+\delta_k^{\rm out}+\widehat\Phi_{q,k}
+\mathfrak e_k+W_k^{\rm mono}-P_{k,-}-P_{k,+}.}
\tag{L49}
\]

Here \(W_k^{\rm mono}\) denotes the programme's original monic-window term; it is distinguished from the explicitly defined rate function \(W_k(y)\). Every complementary term and both penalty terms remain. No favourable sign has been assigned to \(\delta_k^{\rm out}\), and the known positive canonical baseline is not removed.

## 11. What remains to be evaluated

There are now two precisely separated value calculations.

The outer correction is exactly \(\mathcal B_k[\omega_k]-\mathcal B_k[\sigma]\), with the actual convolution outside \([-kb,kb]\). The original unequal upper and lower tail powers have not been converted into a sharp arithmetic tail coefficient. Its \(q\log k\) and \(q\) terms remain to be evaluated.

On the simple stratum, the remaining central order-\(q\) value is that of the explicit matrices (L30)--(L32). This note proves an \(o(q)\) transfer and a signed \(O(q)\) interval, not a limit formula for those matrices. On higher fixed multiplicity strata that matrix contribution is \(o(q)\), by (L43), and is no longer needed for the order-\(q\) coefficient.

In particular, the density-area value \(-I_h\) is not inserted as the baseline coefficient. No unproved constant-density limit for the source band has been used. No current geometric purity theorem is applied without a constructed metric comparison. The new estimates are source and determinant calculations and do not constitute programme closure.

## Source record and verification scope

Imported arithmetic inputs are the original RTM envelopes, the full even source and packet, SXR's source/relation identity, and the original Gamma recurrence and mass. Their upstream analytic proofs have not received a new exhaustive audit. The incoming central local-limit proof is retained in full, with its constants reproduced and the one additional shifted-point consequence proved above.

The generating-function convention and the complex Stirling bound were checked against the NIST DLMF, Sections 18.23 and 5.11. The degree-band transfer, whole-line prefactor comparison, Taylor-jet localization, nonlinear endpoint transfer, finite determinant error, and the \(O(k^2)\) band estimate are derived in this note.

The executable checks are auxiliary exact matrix and polynomial diagnostics. They do not evaluate an actual off-critical xi packet, prove every analytic inequality by computation, or supply an independent review or formal verification of this derivation. Original inputs are frozen with hashes; their earlier check counts are not counted as new analytic results.


### Executed auxiliary diagnostics

The new checker passed 88 exact checks and rejected five deliberately false formulas. Its ordinary and `python -O` outputs are byte-identical. The original checker was replayed unchanged: all 39 checks and four false-formula controls agree with the original JSON receipt and with its optimized run. These statements report the actual executions recorded in `checks/EXECUTION_RECEIPT.json`; they do not upgrade the written analytic derivation to an independent or formal verification.
