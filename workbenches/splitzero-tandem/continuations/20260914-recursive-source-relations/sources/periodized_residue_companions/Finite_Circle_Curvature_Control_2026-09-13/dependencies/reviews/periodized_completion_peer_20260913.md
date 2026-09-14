# Fixed-circle completion audit: P55–P58

Source: `output/split_zero_rh_tandem_2026-09-12/sources/web_periodized_source_delivery/Tau_Periodized_Source_Control/NOTE.tex`, SHA-256 `acf63a56d5f50cfaa23f57ee52a66df261ec241ce13fd81ccac39a3bbbddd3ff`.

Scope: P55–P58, their algebraic kernel, repeated roots, the generator morphism, and the finite-degree metric limit. P9–P10, P26b, P36 and P53–P54 were read for the original objects and conventions. The upstream positivity, exponential decay and weighted polynomial density are used here; their analytic proof is being reviewed separately. No source was edited, no tests were run, and no Lean or network work was performed.

**Finding.** P55–P58 are valid with the exact stated weights. There is no gap in their fixed-circle quotient or limit argument. The precise generator of the kernel, its local primary structure, and its intertwining with the arithmetic action admit the explicit strengthening proved below. Each finite-degree metric is positive definite; its difference from the limiting matrix is also positive definite when the arithmetic space is nonzero. This does not give a positive lower bound uniform in degree.

## 1. Objects and the closed relation subspace

Retain, for fixed \(k\geq2\) and \(L>0\),

\[
S_n=\frac{k}{2}+\frac{2\pi i n}{L},\qquad
\nu_n=\frac{2\pi}{L}m_{h,k}\!\left(\frac{2\pi n}{L}\right)>0,
\qquad
H=\ell^2(\mathbb Z,\nu).
\]

The polynomial embedding is

\[
\iota:\mathbb C[S]\longrightarrow H,
\qquad \iota(P)_n=P(S_n).
\]

It is injective, because a nonzero polynomial has finitely many roots whereas the \(S_n\) are infinitely many distinct points. The exponential moment makes every polynomial square integrable. Let the retained monic polynomial be \(\chi=\chi_{h,k}\), of degree \(q\geq1\), and put

\[
Z=\mathcal Z_L=\{n:\chi(S_n)=0\},\qquad
r=|Z|,\qquad
p=p_L=\prod_{n\in Z}(S-S_n),\qquad
t=\chi/p.
\]

The roots in this product are distinct, so \(p\mid\chi\), with \(p=1\) when \(Z\) is empty. Define

\[
I=\overline{\iota(\chi\mathbb C[S])}^{\,H},\qquad
H_{Z^c}=\{f\in H:f_n=0\text{ for every }n\in Z\}.
\]

Every evaluation \(f\mapsto f_n\) is continuous, since

\[
|f_n|\leq \nu_n^{-1/2}\|f\|_H.
\]

Consequently \(I\subseteq H_{Z^c}\). For the reverse containment let \(f\in H_{Z^c}\), and define \(g_n=f_n/\chi(S_n)\) for \(n\notin Z\). On \(Z^c\), use the measure with masses

\[
\mu_n=|\chi(S_n)|^2\nu_n.
\]

Then

\[
\sum_{n\notin Z}\mu_n|g_n|^2
=\sum_{n\notin Z}\nu_n|f_n|^2<\infty.
\]

The weighted density result from P54 applies to \(\mu\): multiplying the original masses by this fixed polynomial factor preserves a finite exponential moment, possibly on a smaller positive strip. Choose polynomials \(Q_j\) with \(Q_j(S_n)\to g_n\) in \(\ell^2(Z^c,\mu)\). The identity

\[
\|\iota(\chi Q_j)-f\|_H^2
=\sum_{n\notin Z}\mu_n|Q_j(S_n)-g_n|^2
\longrightarrow0
\]

proves \(H_{Z^c}\subseteq I\). Thus

\[
I=H_{Z^c}.
\tag{C1}
\]

Let \(H_Z\) be the sequences supported on \(Z\). The decomposition \(H=H_{Z^c}\oplus H_Z\) is orthogonal in the unchanged weighted inner product. Therefore

\[
U_Z:H/I\longrightarrow \mathbb C^Z,\qquad
U_Z([f])=(f_n)_{n\in Z}
\tag{C2}
\]

is an isometry when the right side has squared norm \(\sum_{n\in Z}\nu_n|v_n|^2\). Its inverse sends \(v\) to the class of the sequence equal to \(v_n\) on \(Z\) and zero elsewhere. In particular the quotient norm is attained by that sequence. This proves the Hilbert quotient assertion in P56, including every factor \(2\pi/L\).

## 2. The kernel, its generator, and exact action maps

Set \(E=\mathbb C[S]/(\chi)\). Composition of the polynomial embedding with the quotient in (C2) gives

\[
\theta_L:E\longrightarrow\mathbb C^Z,
\qquad [P]\longmapsto(P(S_n))_{n\in Z}.
\tag{C3}
\]

This is well defined because every multiple of \(\chi\) vanishes on \(Z\). It is surjective: for \(Z\ne\varnothing\), the polynomials

\[
\ell_n(S)=\prod_{\substack{m\in Z\\m\ne n}}
\frac{S-S_m}{S_n-S_m}
\]

have \(\ell_n(S_m)=\delta_{nm}\), and the empty target case is immediate. A polynomial vanishes at all the distinct \(S_n\), \(n\in Z\), exactly when it is divisible by \(p\). Consequently

\[
K_L:=\ker\theta_L=(p)/(\chi).
\tag{C4}
\]

There is a canonical cyclic presentation of this kernel:

\[
\mu_p:\mathbb C[S]/(t)\xrightarrow{\ \sim\ }K_L,
\qquad [Q]_{(t)}\longmapsto[pQ]_{(\chi)},
\qquad t=\chi/p.
\tag{C5}
\]

If \(Q-Q'=tR\), then \(p(Q-Q')=\chi R\), proving well-definedness. Every element of \(K_L\) has this form. If \(pQ\in(\chi)=(pt)\), cancellation of the nonzero polynomial \(p\) in the integral domain \(\mathbb C[S]\) gives \(Q\in(t)\), proving injectivity. This proof also covers common roots of \(p\) and \(t\); no coprimality is asserted or used.

Let \(A:E\to E\) be the original multiplication by \(S\), let \(A_t\) be multiplication by \(S\) on \(\mathbb C[S]/(t)\), and let

\[
D_Z:\mathbb C^Z\to\mathbb C^Z,
\qquad (D_Zv)_n=S_nv_n.
\]

Direct multiplication proves the typed identities

\[
A\mu_p=\mu_pA_t,\qquad
\theta_LA=D_Z\theta_L.
\tag{C6}
\]

Thus \(K_L\) is \(A\)-invariant, and the complete comparison is the exact sequence of \(\mathbb C[S]\)-modules

\[
0\longrightarrow \mathbb C[S]/(\chi/p)
\xrightarrow{\mu_p}\mathbb C[S]/(\chi)
\xrightarrow{\theta_L}\mathbb C^Z\longrightarrow0,
\tag{C7}
\]

with \(S\) acting on the right by \(D_Z\). In particular

\[
\dim K_L=q-r,\qquad \operatorname{rank}\theta_L=r.
\]

The Hilbert generator has a matching exact map. On \(H\), define the closed multiplier

\[
T_Lf=(S_nf_n)_n,\qquad
\mathcal D(T_L)=\left\{f:\sum_n\nu_n|S_nf_n|^2<\infty\right\}.
\]

It is closed because convergence in its graph implies coordinatewise convergence of both \(f_n\) and \(S_nf_n\). The coordinate projection \(Q_Z:H\to H_Z\) preserves its domain and satisfies

\[
Q_ZT_Lf=T_LQ_Zf,\qquad f\in\mathcal D(T_L).
\tag{C8}
\]

Every element of \(H_Z\) lies in this domain because \(Z\) is finite. Under \(U_Z\), the induced generator on \(H/I\) is precisely \(D_Z\). In addition, \(T_L\iota(P)=\iota(SP)\), so (C6) is the same action map induced from the actual Fourier sampling, not an independently selected action. The source differential retains eigenvalues \(S_n=k/2+2\pi in/L\). Its quadratic polynomial has the exact quotient action

\[
\theta_L(A^2-kA)=(D_Z^2-kD_Z)\theta_L,
\qquad
S_n(S_n-k)=-\frac{k^2}{4}-\frac{4\pi^2n^2}{L^2}.
\tag{C9}
\]

## 3. Full repeated-root calculation

Write the unchanged factorization

\[
\chi(S)=\prod_{j=1}^d(S-\lambda_j)^{m_j},
\qquad \lambda_j\ne\lambda_\ell\ (j\ne\ell).
\]

The Chinese remainder map, with all Taylor constants retained, is

\[
[P]\longmapsto
\left(\sum_{a=0}^{m_j-1}\frac{P^{(a)}(\lambda_j)}{a!}\varepsilon_j^a\right)_{j=1}^d
\in\bigoplus_j\mathbb C[\varepsilon_j]/(\varepsilon_j^{m_j}).
\tag{C10}
\]

For completeness, the map (C10) is bijective by an explicit inverse. Put \(H_j(S)=\chi(S)/(S-\lambda_j)^{m_j}\), and let \(V_j(\varepsilon_j)\) be the Taylor polynomial through degree \(m_j-1\) of \(1/H_j(\lambda_j+\varepsilon_j)\). The denominator is nonzero at \(\varepsilon_j=0\), so these coefficients exist. The class of

\[
e_j(S)=H_j(S)V_j(S-\lambda_j)
\]

has local value \(1\) modulo \((S-\lambda_j)^{m_j}\) and local value \(0\) at every other primary factor. The inverse sends local polynomials \(F_j(\varepsilon_j)\) to \([\sum_j e_j(S)F_j(S-\lambda_j)]_{(\chi)}\). The composites are identities: their remainders vanish at each pairwise coprime primary factor and hence are divisible by their product \(\chi\).

On the \(j\)-th primary block the generator is multiplication by \(\lambda_j+\varepsilon_j\). If \(\lambda_j=S_n\) for some \(n\in Z\), then \(\theta_L\) keeps precisely its constant coefficient. The local kernel is

\[
\varepsilon_j\mathbb C[\varepsilon_j]/(\varepsilon_j^{m_j}).
\tag{C11}
\]

This includes the entire nonconstant jet subspace, with dimension \(m_j-1\). If \(\lambda_j\) is unsampled, \(\theta_L\) is zero on that entire primary block, whose contribution to the kernel has dimension \(m_j\).

The generator map (C5) gives the local multiplicities exactly. At a sampled root,

\[
p(\lambda_j+\varepsilon_j)=\varepsilon_j u_j(\varepsilon_j),\qquad
u_j(0)=\prod_{\substack{\ell:\lambda_\ell\text{ sampled}\\\ell\ne j}}
(\lambda_j-\lambda_\ell)\ne0.
\]

It maps the \(t\)-primary block \(\mathbb C[\varepsilon_j]/(\varepsilon_j^{m_j-1})\) isomorphically onto (C11) by multiplication by \(\varepsilon_j u_j\). For \(m_j=1\) this source block is zero. At an unsampled root, \(p(\lambda_j+\varepsilon_j)\) is a unit, and (C5) maps the full \(t\)-primary block isomorphically onto the full \(\chi\)-primary block. Thus the kernel's arithmetic action has block lengths \(m_j-1\) at sampled roots and \(m_j\) at unsampled roots, all at the original eigenvalues \(\lambda_j\).

## 4. The exact finite-degree metric limit

For \(N\geq q-1\), keep the specified basis of \(\mathcal P_N\), its original sampled Gram \(M_N(L)\), and the same surjective remainder map \(J_N:\mathcal P_N\to E\). Equation P26b is exactly

\[
c^*M_N(L)c=\sum_{n\in\mathbb Z}\nu_n|P_c(S_n)|^2.
\tag{C12}
\]

This Gram is positive definite for every finite \(N\) and every \(L>0\): if the right side is zero, positivity of every mass implies \(P_c(S_n)=0\) for infinitely many distinct points, hence \(P_c=0\), hence \(c=0\). This is also explicitly proved immediately after P26b in the source; it does not depend on the sufficient large-\(L\) comparison bound P34.

Thus \(K_N(L)=J_NM_N(L)^{-1}J_N^*\) and \(G_N(L)=K_N(L)^{-1}\) both exist and are positive definite. To verify their minimizing interpretation directly, fix \(e\in E\) and set

\[
c_e=M_N(L)^{-1}J_N^*G_N(L)e.
\]

Then \(J_Nc_e=e\). If \(J_Nc=e\), write \(c=c_e+h\) with \(J_Nh=0\). The cross term vanishes since

\[
h^*M_N(L)c_e=h^*J_N^*G_N(L)e=0.
\]

Therefore

\[
e^*G_N(L)e
=\min_{P\in\mathcal P_N,\ [P]=e}\|\iota(P)\|_H^2.
\tag{C13}
\]

Let \(R_e\) be the unchanged unique remainder polynomial of degree at most \(q-1\) representing \(e\). The admissible affine spaces are exactly

\[
R_e+\chi\mathcal P_{N-q},
\]

where \(\mathcal P_d=\{0\}\) for \(d<0\). They increase with \(N\), and their union is \(R_e+\chi\mathbb C[S]\). Taking the decreasing infima in (C13) and then using (C1)–(C2) gives

\[
\lim_{N\to\infty}e^*G_N(L)e
=\operatorname{dist}_H(\iota(R_e),I)^2
=\sum_{n\in Z}\nu_n|R_e(S_n)|^2.
\tag{C14}
\]

Let \(J_Z\) evaluate the retained remainder basis at the \(S_n\), \(n\in Z\), and define the coordinate matrix

\[
G_\infty(L)=J_Z^*\operatorname{diag}(\nu_n)_{n\in Z}J_Z.
\tag{C15}
\]

For every \(e\), (C13)–(C14) give

\[
e^*G_N(L)e\geq e^*G_{N+1}(L)e\geq e^*G_\infty(L)e,
\]

so these are Loewner inequalities in the original remainder coordinates. Put \(B_N=G_N(L)-G_\infty(L)\succeq0\). Each diagonal entry of \(B_N\) tends to zero by (C14); hence \(\operatorname{tr}B_N\to0\), and the matrix bound \(\|B_N\|_{\mathrm{op}}\leq\operatorname{tr}B_N\) proves matrix convergence in these same coordinates. This proves P58, without exchanging \(L\) and \(N\) limits.

Since all \(\nu_n>0\), (C15) gives

\[
\operatorname{rad}G_\infty(L)=\ker J_Z=K_L=(p)/(\chi).
\tag{C16}
\]

There is a strict finite-degree strengthening. For \(e\ne0\), its minimizing polynomial \(P_e\in\mathcal P_N\) in (C13) is nonzero. At sampled roots it has the forced values \(P_e(S_n)=R_e(S_n)\). Thus

\[
e^*\bigl(G_N(L)-G_\infty(L)\bigr)e
=\sum_{n\notin Z}\nu_n|P_e(S_n)|^2>0.
\tag{C17}
\]

Strict positivity follows because \(Z^c\) is infinite and a nonzero polynomial cannot vanish at all its nodes. Therefore \(G_N(L)-G_\infty(L)\succ0\) for every finite \(N\geq q-1\) when \(q\geq1\). This strict inequality is compatible with convergence to zero as \(N\to\infty\); no uniform positive bound follows.

Finally, \(G_\infty(L)\) has rank \(r\). It is positive definite exactly when \(r=q\), equivalently \(\chi=p_L\): every root is sampled and all roots are simple. If \(Z\) is empty, then \(p_L=1\), \(K_L=E\), and \(G_N(L)\to0\). If \(\chi=1\), the original arithmetic space is zero and the same quotient and kernel statements hold trivially. The complete multiple-root and unsampled components remain explicitly represented by (C5), (C10)–(C11), and (C16).

## Recommended inclusion

Retain P55–P58 unchanged. Add (C5)–(C11) as the exact cyclic and generator description of their kernel, and (C17) if a finite-degree strengthening is useful. The large-\(L\) approximation P34–P37 and the fixed-\(L\) limit P58 have different parameter paths; the proofs above keep \(L\) fixed throughout and give no estimate uniform in \(N\). This audit establishes the discrete quotient and its arithmetic/Fourier generator map (C6)–(C9) in full.
