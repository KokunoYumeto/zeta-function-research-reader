# Independent audit of the theta two-Stieltjes-space proof

Audit date: 12 September 2026. Reviewer: arithmetic-moment subagent. Author/integration owner: parent task.

The complete final source, all SP.1–SP.31, all four theorem proofs, the local branch calculations, both unbounded-operator domains, the minimum-metric identification, the endpoint, and the final support lifts pass mathematical review. Two wording corrections were reported to the author and are already present in the final audited source. I made no edits to the author's TeX.

The final audited source is **output/split_zero_rh_tandem_2026-09-12/tex/theta_stieltjes_pair.tex**, SHA256 **3695e48f9aa13b9197548ab845998ddb69a4299dbebcf23947f20e211369ac4c**. The audit copy is **work/theta_stieltjes_pair_review_20260912/source.tex**. This report spells out the calculations checked; its verdict concerns these exact bytes.

## Source history and resolved corrections

The first complete source read had SHA256 **19d46e9436de4d0236468552c31109a67bb7a759eb264b6937e5dce45e8c5743**.

1. After SP.11 the initial phrase “The last component is a unit in \(A_H\)” could literally denote the displayed zero odd component. The corrected source explicitly says “The element \(V\bmod H\) is a unit in \(A_H\).” The mathematical unit used in every subsequent formula was already \(V\bmod H\), and the correction now states that type without ambiguity.
2. The initial eta-series attribution named the arithmetic input. The complete paired-series proof actually appears in the historical packet ghost section. The final source references its existing label **sec:historical-packet-ghost**. The proof establishes exactly the asserted absence of real nontrivial zeros in \(0<s<1\).

The intermediate source after the first correction had SHA256 **93314578edac665746884e8d2a1a9abdf0d2925bda4ede279e2757c128fce781**. The final source hash above contains both corrections. There are no outstanding mathematical corrections from this audit.

Original source witnesses consulted:

| File in the same tex directory | SHA256 |
|---|---|
| tau_boundary.tex | 312edbd818647b27f0acc7c79dc6caff07b5cbf5ef6f13c0a851c73700518e69 |
| kernel_layer_continuation.tex | 5742b64a22e1361388388f82a4af7a8ad1cc6de056312a4d2c2a196f64b1fbd2 |
| split_zero_carriers.tex | 49ed53151068f726e5e392a36d076c95e4e050e163c204d85fd3b179a4a25805 |
| historical_packet_ghost.tex | eb0475e1820a69626982bf114300d2a770eb30f4d8ee6f208f998e876cf40bd9 |
| arithmetic_input.tex | a50b0fb587b644c4ea94dba45b2b423d038f2bfbe7fef188543939ba850e58d2 |

The retained source conventions are the conjugate-linear first inner-product argument; \(g=2\xi\); Mellin Plancherel measure \(dt/(2\pi)\); the original monomial basis \(1,s,\ldots,s^{d-1}\); complete local zero orders; the actual unit \(\upsilon=j_h(g/h)\); and the fixed-section metric at correction index \(-1\). The calculations below keep each of these.

## SP.1–SP.3: the quadratic coordinate and full packet polynomial

Write the original centre as \(\rho=1/2+\alpha\). Reflection replaces \(\alpha\) by \(-\alpha\), preserving its complete order \(m_\rho\). Since no selected centre equals \(1/2\), each reflection pair contains two distinct centres. Its original polynomial contribution is

\[
 (s-\rho)^{m_\rho}(s-(1-\rho))^{m_\rho}
 =(z^2-\alpha^2)^{m_\rho}
 =(-1)^{m_\rho}(x+\alpha^2)^{m_\rho},
 \quad z=s-\tfrac12,\quad x=-z^2.
\]

Consequently \(d=2D\), where \(D=\sum_{\{\rho,1-\rho\}}m_\rho\), and

\[
 H(x)=\prod_{\{\rho,1-\rho\}}(x-r_\rho)^{m_\rho},
 \quad r_\rho=-\alpha^2,\qquad h(s)=(-1)^D H(x).
\]

Equal \(r\)'s give equal or opposite \(\alpha\)'s, hence precisely the same reflection pair. Thus no additional centres or multiplicities merge. Every factor order in \(H\) is exactly the original order at either corresponding branch. The total algebra dimension is restored by the two branches, giving \(2D=d\). Since \(\alpha\ne0\), \(H(0)\ne0\). Conjugation permutes these paired factors and therefore gives real coefficients of the monic \(H\).

The real-zero input is valid with the original zeta factors. For \(0<s<1\),

\[
 \eta(s)=\sum_{n\ge1}\big((2n-1)^{-s}-(2n)^{-s}\big)>0,
 \qquad
 \zeta(s)=\frac{\eta(s)}{1-2^{1-s}}<0.
\]

The source proves analytic continuation of this identity by the uniformly convergent paired series on compact subsets of \(\Re s>0\). The remaining factors \(s(s-1)\), \(\pi^{-s/2}\), and \(\Gamma(s/2)\) are nonzero on this interval. Hence \(g(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\ne0\), including \(s=1/2\). This justifies every use of nonzero \(\alpha\) and nonzero \(\gamma\) below.

## SP.4–SP.7: algebra isomorphism, original basis and determinant

The homomorphism on generators is

\[
 \mathcal T:\mathbb C[s]/(h)\to
 \mathbb C[x,z]/(H(x),z^2+x),\qquad [s]\mapsto\tfrac12+z.
\]

Its inverse is \([x]\mapsto-(s-1/2)^2\), \([z]\mapsto s-1/2\). SP.3 sends the relation \(h=0\) to zero; the inverse sends \(H(x)\) and \(z^2+x\) to zero. Both compositions fix their algebra generators and units. Every target class has a unique representative \(a(x)+zb(x)\), with both degrees below \(D\), by monic division first in \(z\), then in \(x\). The underlying module is \(A_H\oplus zA_H\), and the actual product is

\[
 (a,b)(c,e)=(ac-xbe,ae+bc).
\]

This product, including the minus sign, is needed for the algebra claim and is explicitly present.

For the source column \(s^n\), \(0\le n<2D\), expand

\[
 (\tfrac12+z)^n
 =\sum_{2j\le n}\binom n{2j}2^{-(n-2j)}(-x)^j
 +z\sum_{2j+1\le n}\binom n{2j+1}
       2^{-(n-2j-1)}(-x)^j.
\]

These are exactly SP.6. Every power in the target lies below degree \(D\), so the displayed columns require no undeclared further remainder. In the interlaced order \(1,z,x,zx,\ldots\), the diagonal is \((-1)^{\lfloor n/2\rfloor}\). Its product is

\[
 (-1)^{2\sum_{j=0}^{D-1}j}=(-1)^{D(D-1)}=1.
\]

The permutation to all even columns followed by all odd columns has \(\sum_{j=0}^{D-1}(D-1-j)=D(D-1)/2\) inversions. Thus

\[
 \det T=(-1)^{D(D-1)/2},
\]

with every power of \(1/2\) retained in the off-diagonal entries. The inverse columns are the original polynomials \((-(s-1/2)^2)^j\) and \((s-1/2)(-(s-1/2)^2)^j\). Finally

\[
 (\tfrac12+z)(a+zb)=\tfrac12a-xb+z(a+\tfrac12b)
\]

proves

\[
 TAT^{-1}=\tfrac12I_{2D}+
 \begin{pmatrix}0&-X\\I_D&0\end{pmatrix}
\]

in the exact basis claimed. This is a similarity of the complete original multiplication operator, including all Jordan data.

## SP.8–SP.11: local nilpotents, branch inverses and the actual unit

At \(r=-\alpha^2\), with full order \(m\), put \(B_r=\mathbb C[\eta]/(\eta^m)\), \(\eta=x-r\). The finite binomial polynomial

\[
 Z_r=\alpha\sum_{j=0}^{m-1}\binom{1/2}{j}
             (-\eta/\alpha^2)^j
\]

has square \(Z_r^2=\alpha^2-\eta=-x\) modulo \(\eta^m\). Every omitted binomial term has degree at least \(m\) and therefore vanishes in this exact algebra. Its constant coefficient is \(\alpha\ne0\), so it is a unit; its inverse is a finite power-series inverse in the same quotient.

Evaluation at \(z=\pm Z_r\) gives the unital algebra map

\[
 a+zb\longmapsto(a+Z_rb,a-Z_rb).
\]

The displayed inverse

\[
 (u,v)\longmapsto (u+v)/2+z(u-v)/(2Z_r)
\]

recovers \(a,b\), and the two evaluations recover \(u,v\). Both compositions and the factors \(2Z_r\) are exact. The idempotents \((1\pm z/Z_r)/2\) map respectively to \((1,0)\) and \((0,1)\).

For the first original branch \(s=1/2+\alpha+w\), the local coordinate relation is

\[
 \eta=-2\alpha w-w^2,\qquad
 w=Z_r(\eta)-\alpha.
\]

The first substitution into the second squares to \((\alpha+w)^2\) and has constant term \(\alpha\); uniqueness of the truncated square root with that constant term gives \(Z_r(-2\alpha w-w^2)=\alpha+w\). In the other order,

\[
 -2\alpha(Z_r-\alpha)-(Z_r-\alpha)^2
 =\alpha^2-Z_r^2=\eta.
\]

Thus both compositions are identities in the respective length-\(m\) local algebras. The nonzero linear coefficient \(-2\alpha\) also proves preservation of vanishing orders. Replacing \(\alpha\) by \(-\alpha\) gives the second branch with its corresponding sign. The calculation holds at \(m=1\) and at every repeated order.

The even entire function \(g(1/2+z)\) has coefficients \(g^{(2n)}(1/2)/(2n)!\). Substituting \(x=-z^2\) yields exactly

\[
 \Phi(x)=\sum_{n\ge0}
 \frac{(-1)^n g^{(2n)}(1/2)}{(2n)!}x^n.
\]

For any fixed \(|x|\), choose \(|z|=\sqrt{|x|}\); absolute convergence of the entire even series gives absolute convergence of this series. Hence \(\Phi\) is entire. The local isomorphisms just proved show that its order at \(r_\rho\) is exactly \(m_\rho\). Therefore

\[
 V(x)=(-1)^D\Phi(x)/H(x),\qquad g(s)/h(s)=V(x)
\]

is the entire quotient with the original sign and factor \(g=2\xi\). At every root of \(H\), its value is nonzero because exactly the complete order was removed. Thus \(V\bmod H\in A_H^\times\). Its multiplication matrix \(U_V\) includes its full Taylor class, and

\[
 \mathcal T(\upsilon)=(V\bmod H,0).
\]

In particular the multiplication operator of the unit on \(A_H\oplus zA_H\) is \(\operatorname{diag}(U_V,U_V)\). This is the precise unit retained in both SP.22 kernels.

## SP.12–SP.16: measures, constants, Hilbert inverse and domains

The original measures are

\[
 d\mu(t)=|g(1/2+it)|^2\,dt/(2\pi),\qquad
 d\nu_h(t)=|v_h(1/2+it)|^2\,dt/(2\pi).
\]

They agree with TB.2 and KL.3. Their polynomial moments and strict polynomial positivity follow from the arithmetic Mellin decay and the discrete zero sets, as proved there. Dividing by the fixed \(h\) preserves the tail decay and the removable quotient is bounded on compact sets.

At \(z=it\), \(x=t^2\). For an integrable test function \(F\),

\[
 \int_\mathbb R F(t^2)|v_h(1/2+it)|^2\,\frac{dt}{2\pi}
 =\int_0^\infty F(x)\frac{|V(x)|^2}{2\pi\sqrt x}\,dx.
\]

The two preimages \(t=\pm\sqrt x\) each have Jacobian \(1/(2\sqrt x)\), so their sum is \(1/\sqrt x\); there is no omitted factor two. Replacing \(v_h,V\) by \(g,\Phi\) proves the \(\lambda_0\) formula. Since \(\Phi=(-1)^D HV\),

\[
 d\lambda_0=|H|^2d\lambda_h.
\]

Near zero, both displayed densities are locally integrable because their numerators are continuous and \(x^{-1/2}\) is integrable. Their measures have no atom there.

For either pair of measures,

\[
 \mathcal U(a,b)(t)=a(t^2)+itb(t^2)
\]

has norm

\[
 \|\mathcal U(a,b)\|_\nu^2
 =\|a\|_\lambda^2+\|b\|_{x\lambda}^2.
\]

The cross terms cancel when the values at \(t\) and \(-t\) are added. The inverse formulas

\[
 a(x)=\frac{f(\sqrt x)+f(-\sqrt x)}2,\qquad
 b(x)=\frac{f(\sqrt x)-f(-\sqrt x)}{2i\sqrt x}
\]

hold almost everywhere. Null-set representatives cause no ambiguity, because the pushforward identity carries the corresponding null sets to null sets. Applying the same norm calculation to the parity projections shows both inverse components belong to their stated spaces. This proves surjectivity, not merely an isometric embedding.

Multiplication by \(s\) gives

\[
 (a,b)\mapsto(a/2-xb,a+b/2).
\]

Its original domain is \(f,tf\in L^2(\nu)\), since \(|s|^2=1/4+t^2\). The parity norm calculation gives

\[
 \|tf\|_\nu^2=\|a\|_{x\lambda}^2+\|b\|_{x^2\lambda}^2.
\]

Together with the domain of \(\mathcal U\), this is precisely SP.16:
\(a\in L^2(\lambda)\cap L^2(x\lambda)\) and
\(b\in L^2(x\lambda)\cap L^2(x^2\lambda)\).
Reflection gives \((a,b)\mapsto(a,-b)\) without conjugating the amplitudes.

Multiplication by the original \(h\) is an onto isometry from \(L^2(\mu)\) to \(L^2(\nu_h)\): the identity \(|h|^2|v_h|^2=|g|^2\) proves its norm, and division by \(h\) almost everywhere gives its inverse with the same norm. Its two-component form is multiplication by \((-1)^D H\) on each component. Its action on polynomial subspaces still raises the original \(s\)-degree by \(2D\), exactly as KL.23 states. The infinite-dimensional isometry and this finite-degree map are related explicitly, with no replacement of the finite source family.

## SP.17–SP.21: monicity, both norms and Christoffel ratios

Strict polynomial positivity gives the two real monic families \(P_n\) for \(\lambda_h\) and \(R_n\) for \(x\lambda_h\). Their norms are the unaltered integrals

\[
 p_n=\int|P_n|^2d\lambda_h,\qquad
 u_n=\int x|R_n|^2d\lambda_h.
\]

The real moment matrices give real polynomial coefficients. In particular \(p_0=\lambda_h((0,\infty))\) and \(u_0=\int x\,d\lambda_h\); both original masses remain present.

Because \(x=-(s-1/2)^2\), the leading coefficient in \(s\) of
\((-1)^nP_n(x)\) and \((-1)^n(s-1/2)R_n(x)\) is one. Their degrees are \(2n\) and \(2n+1\), respectively. Their even/odd lower-degree inner products vanish by the corresponding half-line orthogonality and mixed parity. Uniqueness of the original monic family therefore gives SP.18, including

\[
 \kappa_{2n}=p_n,\qquad \kappa_{2n+1}=u_n.
\]

For \(n>0\), \(P_n(0)=0\) would give \(P_n=xQ\) with \(Q\) a nonzero degree-\((n-1)\) polynomial. Its forbidden orthogonality equation is

\[
 0=\int P_n\overline Q\,d\lambda_h
   =\int x|Q|^2d\lambda_h>0.
\]

The case \(n=0\) has \(P_0(0)=1\). Thus the ratio \(c_n=P_{n+1}(0)/P_n(0)\) is defined at every \(n\). The quotient

\[
 \frac{P_{n+1}-c_nP_n}{x}
\]

is monic of degree \(n\), and pairing it with a lower-degree polynomial for the measure \(x\lambda_h\) gives zero by the original two orthogonality relations. Hence this quotient is exactly \(R_n\). Since \(R_n-P_n\) has lower degree,

\[
 \int R_nP_n\,d\lambda_h=p_n,\qquad
 \int R_nP_{n+1}\,d\lambda_h=0.
\]

Therefore

\[
 u_n=\int R_n(P_{n+1}-c_nP_n)\,d\lambda_h=-c_np_n,
\]

and positivity proves \(c_n<0\). Taking successive original norms proves

\[
 a_{2n+1}=-c_n,\qquad
 a_{2n}=\frac{p_n}{-c_{n-1}p_{n-1}}\quad(n\ge1).
\]

The identical proof for \(\lambda_0\) gives SP.21. The identification with the existing \(\mathfrak h_j\) is exact: KL.22 defines them as the squared norms of the original monic orthogonal theta vectors for \(\mu\). Thus \(\mathfrak h_{2n}=p_n^0\), \(\mathfrak h_{2n+1}=u_n^0=-c_n^0p_n^0\), with both displayed adjacent ratios and all constants unchanged.

## SP.22–SP.24: the full actual minimum, endpoint and relative spectrum

The source map is \(p\mapsto\upsilon j_hp\), not bare remainder. The original constraint for target \(u\) is therefore \(j_hp=\upsilon^{-1}u\), exactly TB.10. Consequently its minimum metric in the original coordinates is TB.8 at \(N=d+m\).

Under \(\mathcal T\), the even polynomial column has full residue

\[
 ((-1)^nU_VP_n(X)c_H,0)=((-1)^nf_n,0),
\]

and the odd one has full residue

\[
 (0,(-1)^nU_VR_n(X)c_H)=(0,(-1)^ne_n).
\]

Both \(P_n(X)\) and \(R_n(X)\) act on all \(D\) coefficients of \(A_H\), and \(U_V\) contains all original local unit coefficients. No evaluation at centres occurs. The signs cancel in each column outer product, giving exactly SP.22 with denominators \(p_n,u_n\).

At the endpoint \(N=2D-1\),

\[
 n_e=\lfloor N/2\rfloor=D-1,\qquad
 n_o=\lfloor(N-1)/2\rfloor=D-1.
\]

The first \(D\) monic polynomials in each family form a triangular basis of \(A_H\). The invertible \(U_V\) preserves spanning, so both kernels are strictly positive even at this endpoint. This includes \(D=1,N=1\), where each sum has its one positive \(n=0\) column.

The coefficient-space minimum formula is proved directly: for source Gram \(M>0\) and surjection \(J\),

\[
 p=M^{-1}J^*(JM^{-1}J^*)^{-1}y
\]

has image \(y\) and is \(M\)-orthogonal to \(\ker J\). Every other preimage is \(p+w\), \(Jw=0\), and its squared norm is the squared norm of \(p\) plus \(w^*Mw\). Thus the minimum metric is \((JM^{-1}J^*)^{-1}\), including the original actual unit inside \(J\).

Applied to the preceding columns, this proves

\[
 G' :=T^{-*}G_N^{\rm src}T^{-1}
      =\operatorname{diag}(G_e,G_o).
\]

Since \(G_N^{\rm src}=T^*G'T\) and \(|\det T|^2=1\), the determinant is exactly \(\det G_e\det G_o\). At \(N=d-1\), remainder is an isomorphism and the unique numerator is \(\operatorname{rem}_h(\upsilon^{-1}u)\). This is the fixed \(R_{\rm ref}\), so the index \(m=-1\) is correct and introduces no negative-degree theta polynomial or unavailable source correction.

With \(A'=\tfrac12I+\left(\begin{smallmatrix}0&-X\\I&0\end{smallmatrix}\right)\), multiply the two blocks:

\[
 (A')^*G'+G'A'-G'
 =\begin{pmatrix}0&G_o-G_eX\\G_o-X^*G_e&0\end{pmatrix}.
\]

Thus SP.24 has both adjoints and the sign of \(X\) in the correct positions. The relative matrix in these coordinates is

\[
 S'=\begin{pmatrix}0&B\\B^*&0\end{pmatrix},\qquad
 B=G_e^{-1/2}(G_o-G_eX)G_o^{-1/2}.
\]

For a fully explicit relation to the original relative matrix, let

\[
 Q=(G')^{1/2}T(G_N^{\rm src})^{-1/2}.
\]

Then \(Q^*Q=I_{2D}\), and its square dimension makes it unitary. Substituting \(G_N^{\rm src}=T^*G'T\) gives

\[
 Q(G_N^{\rm src})^{-1/2}W_N(G_N^{\rm src})^{-1/2}Q^*=S'.
\]

This proves preservation of the whole relative spectrum, in addition to the Rayleigh-quotient argument given in the source. If \(Bv=\sigma u\), \(B^*u=\sigma v\), the vectors \((u,v)\), \((u,-v)\) have eigenvalues \(\sigma,-\sigma\). The remaining kernel is \(\ker B^*\oplus\ker B\), of dimension \(2\dim\ker B\) because \(B\) is square. Therefore every sign, multiplicity and zero in SP.24 is retained, and the original allowance is \(\|B\|\).

## SP.25–SP.27: positive comparison, nilpotents and both updates

The declared matrices are

\[
 R=G_e^{-1/2}G_oG_e^{-1/2}>0,\qquad
 L=G_e^{1/2}XG_e^{-1/2}.
\]

Their exact product relation is

\[
 B=(R-L)G_e^{1/2}G_o^{-1/2},
\]

and

\[
 (G_e^{1/2}G_o^{-1/2})(G_e^{1/2}G_o^{-1/2})^*
   =G_e^{1/2}G_o^{-1}G_e^{1/2}=R^{-1}.
\]

Hence \(BB^*=(R-L)R^{-1}(R-L)^*\), which proves SP.26 with its original coordinate order. No commutation of \(G_e,G_o,X\) is used.

The equality \(\epsilon_{N-d}=0\) is equivalent to \(B=0\), hence exactly \(G_o=G_eX\). Under this equality \(L=R>0\), so \(X\) is similar through \(G_e^{1/2}\) to the positive Hermitian matrix \(R\). Its spectrum is positive real and it is diagonalizable. The minimal polynomial of the original \(X=M_x\) is \(H\): if \(p(X)=0\), applying it to \(c_H\) gives \([p]=0\), so \(H\mid p\); conversely \(H(X)=0\). Diagonalizability forces \(H\) squarefree. Therefore a retained order \(m_\rho>1\) forces a strictly positive allowance at every finite \(N\). This statement keeps the actual nilpotent algebra and does not assert a lower bound on the limit of the allowances.

For \(N=2j\), \(n_e=j,n_o=j-1\); the next degree adds only the odd column \(e_j\) with norm \(u_j\). For \(N=2j+1\), \(n_e=n_o=j\); the next degree adds only the even column \(f_{j+1}\) with norm \(p_{j+1}\). These are the two updates stated before SP.27.

For the changing block \(K>0\), actual full column \(v\), and actual norm \(k>0\),

\[
 K+vv^*/k=K^{1/2}(I+ww^*)K^{1/2},
 \qquad w=K^{-1/2}v/\sqrt k.
\]

The determinant of \(I+ww^*\) is \(1+\|w\|^2=1+v^*K^{-1}v/k\), including \(v=0\). Taking inverse block determinants and retaining the unchanged block proves SP.27 exactly. At the endpoint \(N=2D-1\), the first admitted update is the even one, with full column \(f_D\) and norm \(p_D\), as required by its degree \(2D\).

## SP.28–SP.31: actual tesserine coordinates and the spectral bound

For the original \(\rho=\beta+i\gamma\), let \(\delta=\beta-1/2\). Then

\[
 -(\rho-\tfrac12)^2
 =\gamma^2-\delta^2-2i\delta\gamma,
\]

proving SP.28. The original group-algebra element is

\[
 Q(\rho)=\rho\,1+(1-\rho)\sigma+
       \overline\rho\,\kappa+(1-\overline\rho)\sigma\kappa.
\]

Evaluation at \((\sigma,\kappa)=(\pm1,\pm1)\) gives respectively
\(2,0,4\delta,4i\gamma\), exactly as proved in the carrier section. Their product satisfies

\[
 -\frac{c_{-+}c_{--}}4
 =-\frac{(4\delta)(4i\gamma)}4
 =-4i\delta\gamma=r_\rho-\overline{r_\rho}.
\]

The factor four and imaginary sign in SP.30 are correct. Since the actual \(\gamma\ne0\), \(r_\rho\) is real exactly when \(\delta=0\), and then \(r_\rho=\gamma^2>0\). The complete root correspondence in SP.2 therefore proves that all roots of \(H\) are positive real exactly when the selected packet is critical, with all its original multiplicities. This equivalence imposes no squarefreeness; squarefreeness arises separately from the exact finite metric equation \(G_o=G_eX\) above.

For every retained root, a nonzero eigenvector of \(A=M_s\) exists even at a repeated order: take \((s-\rho)^{m_\rho-1}\) in its original local factor and zero in the other CRT factors. On that vector,

\[
 u^*W_Nu=(\overline\rho+\rho-1)u^*G_N^{\rm src}u
        =2\delta\,u^*G_N^{\rm src}u.
\]

The positive denominator and the relative Hermitian norm yield

\[
 2|\delta|=|c_{-+}|/2\le\epsilon_{N-d}.
\]

This is precisely the claimed one-factor spectral bound. No tensor multiplicity coefficient is silently inserted, and the complete order remains in the eigenvector and the full operator.

## Exact support lifts and their target carriers

For every unital algebra homomorphism \(f:A\to B\), define
\(G(f)(\tau)=\tau\) and \(G(f)(a^\bullet)=f(a)^\bullet\).
For two supported amplitudes, ring addition and multiplication verify both semiring operations; if either input is \(\tau\), the additive-identity and absorbing-product rules verify the remaining cases. The unit is the supported algebra unit. An algebra inverse lifts to a two-sided semiring inverse.

Apply this construction to SP.4 and SP.9 with their specified target multiplications. The latter target is \(G(B_r\times B_r)\): a pair of amplitudes has one common external support. Its displayed comparison map

\[
 G(B_r\times B_r)\longrightarrow G(B_r)\times G(B_r),
 \quad \tau\mapsto(\tau,\tau),\quad
 (u,v)^\bullet\mapsto(u^\bullet,v^\bullet)
\]

preserves operations and unit componentwise. It is injective because the both-absent point and both-supported amplitudes are recovered uniquely. Its image is exactly the common-support fibre product: masks \((0,0)\) and \((1,1)\). The mixed-support masks \((1,0)\), \((0,1)\) remain present in the product target and are explicitly outside this image. In particular a zero amplitude in one supported coordinate does not change its mask.

Character evaluation at \((-1,+1)\) is a unital algebra homomorphism \(\mathbb C[K_4]\to\mathbb C\). Its lift sends the supported original \(Q(\rho)\) to \(c_{-+}(\rho)^\bullet\). At \(\delta=0\) this is the supported zero \(e=0_\mathbb C^\bullet\), while \(\tau\) still maps to external \(\tau\). The final paragraph therefore has the correct synchronized target, exact embedding into independently supported coordinates, and the correct critical supported-zero value. These conclusions agree with the carrier section's original definition of \(G\).

## Final audit scope

All SP.1–SP.31 and every accompanying claim were checked against the source types and calculations above. The complete theorem bodies preserve the original arithmetic function, actual measures, full unit, exact centre and degree shifts, signs, nilpotents, eigenvalue multiplicities, initial metric, and support observations. The two reported textual corrections are resolved in the final source hash.

This is an analytic and algebraic source audit. I did not modify the TeX or rebuild the main/frozen edition. Parent owns the subsequent cumulative compilation and visual PDF review. The report does not assert an asymptotic theta norm estimate: SP proves the exact half-line representation and the displayed finite identities.
