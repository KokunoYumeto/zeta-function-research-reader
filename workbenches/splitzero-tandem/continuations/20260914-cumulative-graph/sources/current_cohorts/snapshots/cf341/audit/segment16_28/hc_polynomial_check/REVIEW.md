# Independent check of HC6-HC8 polynomial estimates

Status: accepted. No concrete defect was found in the coordinate map, quotient determinant, Legendre coefficient bound, degree-2q remainder, or scalar estimates HC6-HC8.

Source inspected: `shared_thread_audit/segment55_67/actual_compatible_bounds.tex`, lines 85-211; original definitions from `actual_holonomy_counterfactual.tex`, lines 14-56 and 93-105. This audit changes no source mathematics or packet.

## Original packet and coordinate isomorphism

Retain the complete original quartet divisor h|g with g=2xi, its full order m, c=k/2, ell_k=1+k(m-1), q=ell_k(k+1)^2 and

\[
\chi(S)=\prod_{a,b=0}^{k}\bigl(S-c-(2a-k)\delta-i(2b-k)\gamma\bigr)^{\ell_k}.
\]

For every degree N, define the invertible linear map

\[
\Phi_N:\mathbb C[S]_{\le N}\longrightarrow\mathbb C[x]_{\le N},\qquad
\Phi_N(P)(x)=P(c+iTx),\quad
\Phi_N^{-1}(f)(S)=f((S-c)/(iT)).
\]

The inverse exists because T=Dq>0. Its quotient map is induced by
\(\chi_T(x)=(iT)^{-q}\chi(c+iTx)\). The individual roots are exactly

\[
z_{ab}=\frac{(2b-k)\gamma}{T}-i\frac{(2a-k)\delta}{T},
\]

with their original multiplicity ell_k. Their moduli satisfy
\(|z_{ab}|^2\le k^2(\delta^2+\gamma^2)/T^2=r^2\). Since q>=k and D>=2R_0, r<=1/2.

Substitution u=Tx gives the exact source-norm identity

\[
\int_{\mathbb R}|P(c+iu)|^2m_{h,k}(u)\,du
=\int_{\mathbb R}|\Phi_N(P)(x)|^2T m_{h,k}(Tx)\,dx.
\]

The measure mass is unchanged. If z=(zeta-c)/(iT), the raw derivative jet satisfies
\(\Phi_N(P)^{(d)}(z)=(iT)^d P^{(d)}(\zeta)\), with no deleted derivative orders or multiplicities.

The coefficient quotient basis in HT7 is \(1,S,\ldots,S^{q-1}\). In that basis and \(1,x,\ldots,x^{q-1}\), the quotient matrix Q_T has entries

\[
(Q_T)_{j,l}=\begin{cases}\binom{l}{j}c^{l-j}(iT)^j,&j\le l,\\0,&j>l,\end{cases}
\qquad 0\le j,l<q.
\]

Thus \(\det Q_T=(iT)^{q(q-1)/2}\). For quotient metrics the exact norm identity gives
\(\widetilde G_N=Q_T^{-*}G_NQ_T^{-1}\), so

\[
\det\widetilde G_N=T^{-q(q-1)}\det G_N.
\]

This factor is independent of N and cancels in each stated volume ratio. It is the coefficient-basis factor; raw-jet bases have their own Jacobian. The source explicitly uses coefficient bases, so the printed exponent is correct.

## Legendre coefficient 1-norm

Write the Rodrigues polynomial as

\[
L_j(x)=\frac{1}{2^j j!}\frac{d^j}{dx^j}(x^2-1)^j
=2^{-j}\sum_{l=\lceil j/2\rceil}^{j}(-1)^{j-l}\binom jl\binom{2l}{j}x^{2l-j}.
\]

Consequently

\[
\|L_j\|_{\mathrm{coeff},1}
=2^{-j}\sum_{l=\lceil j/2\rceil}^{j}\binom jl\binom{2l}{j}
\le 2^{-j}\binom{2j}{j}\sum_{l=0}^{j}\binom jl
=\binom{2j}{j}\le4^j.
\]

With \(\int_{-1}^{1}L_j^2=2/(2j+1)\), the coefficient \(a_j\) in \(f=\sum_{j=0}^{N}a_jL_j\) satisfies

\[
|a_j|=\frac{|\langle f,L_j\rangle|}{\|L_j\|_2^2}
\le\sqrt{\frac{2j+1}{2}}\|f\|_2.
\]

Hence

\[
\|f\|_{\mathrm{coeff},1}
\le\|f\|_2\sum_{j=0}^{N}\sqrt{\frac{2j+1}{2}}4^j
\le\sqrt{\frac{2N+1}{2}}\frac{4^{N+1}-1}{3}\|f\|_2
=A_N\|f\|_2.
\]

This proves the exact displayed A_N as an upper-bound constant, for complex as well as real f.

## Exact monic division through degree 2q

List all q roots z_a with repetitions and let
\(E(t)=\prod_{a=1}^{q}(1-z_at)\), \(E(t)^{-1}=\sum_{j\ge0}h_jt^j\). Expansion of each geometric series gives

\[
|h_j|\le\binom{q+j-1}{j}r^j,\qquad
\|\chi_T\|_{\mathrm{coeff},1}\le(1+r)^q.
\]

For every integer s>=0 let \(Q_s(x)=\sum_{j=0}^{s}h_jx^{s-j}\). Since the truncated inverse obeys
\(E(t)\sum_{j=0}^{s}h_jt^j=1+\sum_{d=s+1}^{s+q}e_dt^d\), multiplication by \(x^{q+s}\) at \(t=x^{-1}\) shows

\[
\chi_T(x)Q_s(x)=x^{q+s}+\sum_{d=s+1}^{s+q}e_dx^{q+s-d}.
\]

Every exponent in the displayed sum is below q. Therefore Q_s is exactly the Euclidean quotient, and \(R_s=x^{q+s}-\chi_TQ_s\) is exactly the remainder. The two degree supports are disjoint, so

\[
1+\|R_s\|_{\mathrm{coeff},1}
=\|\chi_TQ_s\|_{\mathrm{coeff},1}
\le(1+r)^q\sum_{j=0}^{s}\binom{q+j-1}{j}r^j
\le(1+r)^q(1-r)^{-q}=B_q(r).
\]

In particular \(\|R_s\|_{\mathrm{coeff},1}\le B_q(r)-1\le B_q(r)\), including s=q, the required monomial of degree 2q. For monomials of degree below q the remainder coefficient norm is one, and B_q(r)>=1. Linearity gives
\(\|\operatorname{rem}_{\chi_T}f\|_{\mathrm{coeff},1}\le B_q(r)\|f\|_{\mathrm{coeff},1}\)
for every degree at most 2q.

The maps commute exactly:
\(\operatorname{rem}_{\chi_T}\Phi_N(P)=\Phi_{q-1}(\operatorname{rem}_{\chi}P)\).
Indeed writing P=chi Q+R with deg R<q gives
\(\Phi_N(P)=(iT)^q\chi_T\Phi(Q)+\Phi(R)\), and deg Phi(R)<q.

For v of degree below q, the pointwise bound
\(|v(u/T)|^2\le\|v\|_{\mathrm{coeff},1}^2\max(1,|u/T|^{2q-2})\)
then proves the source upper bound in HC6, while restriction to |u|<=T gives its source lower bound. Therefore
\(\|\operatorname{rem}_{\chi}P\|_{H_{q-1}}^2\le C_N\|P\|_{H_N}^2\)
for both N=2q-1 and N=2q. Applying this to the least quotient lift proves the displayed Hermitian comparisons and hence HC7; applying it to a nonzero polynomial below degree q proves C_N>=1.


For completeness, the Legendre orthogonality and norm used above follow from j integrations by parts in Rodrigues formula: the derivatives of (x^2-1)^j of order below j vanish at both endpoints, and therefore the integral of L_j against every polynomial of degree below j is zero. The leading coefficient is 2^{-j} binom(2j,j), so

\[
\int_{-1}^{1}L_j(x)^2\,dx
=2^{-j}\binom{2j}{j}\int_{-1}^{1}x^jL_j(x)\,dx
=2^{-2j}\binom{2j}{j}\int_{-1}^{1}(1-x^2)^j\,dx.
\]

Writing I_j=integral_{-1}^{1}(1-x^2)^j dx, integration of the derivative of x(1-x^2)^j gives (2j+1)I_j=2j I_{j-1} for j>=1, and I_0=2. Hence
\(I_j=2^{2j+1}(j!)^2/(2j+1)!\), which gives the stated norm 2/(2j+1).

## Scalar inequalities HC6-HC8

A second independent scalar review accepted all numerical estimates. Retain k>=3, m>=1, q=ell_k(k+1)^2>=16, T=Dq and n=2q-2. Since bD>=2,
\(n!/(bT)^n\le(2q)^n/(2q)^n=1\).
The pointwise inequality \(1\le(e^{bu}+e^{-bu})/2\) gives
\(\mu_h\le(M_h(b)+M_h(-b))/2\le X\), so \(M_k\le2X^k\) and \(U_k(T)\le3X^k\).
The underlying convolution moment bound is exact in scale: positivity and
\(|u|^n\le n!b^{-n}(e^{bu}+e^{-bu})\)
give
\(\int |u|^nm_{h,k}(u)du\le n!b^{-n}(M_h(b)^k+M_h(-b)^k)\).

The two Legendre constants obey

\[
A_{2q-1}^2=\frac{4q-1}{18}(4^{2q}-1)^2\le\frac{2q}{9}256^q,
\]
\[
A_{2q}^2=\frac{4q+1}{18}(4^{2q+1}-1)^2
\le\frac{32q+8}{9}256^q\le\frac{40q}{9}256^q.
\]

Thus the exact quotient of C_{2q} by C_{2q-1} is

\[
\rho_q=\frac{4q+1}{4q-1}\left(\frac{4^{2q+1}-1}{4^{2q}-1}\right)^2.
\]

Since r<=1/2,

\[
\log B_q(r)^2=2q\int_0^r\frac{2\,dt}{1-t^2}
\le\frac{16qr}{3}=\frac{16kR_0}{3D}.
\]

Substitution into C_{2q-1} yields

\[
C_{2q-1}\le\frac{2}{3c_hD}X^k\vartheta_h^{-(k-3)}
e^{\alpha(Dq+k-3)}(1+Dq+k-3)^B256^q
e^{16kR_0/(3D)}.
\]

Now \(\vartheta_h^{-(k-3)}\le K^k\): if theta_h>=1 the left side is at most one, and if theta_h<1 it is K^{k-3}<=K^k. Also
\(e^{\alpha(k-3)}\le e^{\alpha k}\),
\(1+Dq+k-3\le1+(D+1)q\), and
\(2/(3c_hD)\le C_{\rm env}\).
Taking the logarithm and multiplying by q gives the exact expression \(\mathcal U_k\) as an upper bound. The coefficient 40q/9 in the degree-2q estimate is twenty times 2q/9, so it gives \(q\log C_{2q}\le\mathcal U_k+q\log20\). This proves HC8 from HC7 without any assertion that rho_q<=20.

## Verdict

Accepted within the delegated scope. All original coordinates, c, T, q, roots, full multiplicities, and source measure are preserved by explicit invertible maps. No correction to HC6-HC8 is required by this check.
