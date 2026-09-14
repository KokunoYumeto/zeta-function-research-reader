# Independent arithmetic amplification rate review

Date: 2026-09-13. Scope: bounded calculation for the original hypothetical actual quartet; no source files were edited and no RH verdict is made.

The assignment received verbatim was:

> Independent bounded review/calculation: read full work/rh_counterfactual_20260913/continuation2/combined_arithmetic_restriction.tex CA1–29 and arithmetic_tail/arithmetic_tail_windows.tex TW1–21. Actual quartet q=ell(k+1)^2,L=2δell(k+1)floor((k+1)^2/4). Determine exact scales of existing upper bounds/endpoint constraints relative L, identify any actual proved o(L) upper of SAME normalized boundaryepsilon (not scalar Gram). Give formulas, no generic proofobligation. Parent (me) reading fixedpacket/HG and assembling arithmetic_amplification_match.tex. No edits to sources, save total_object/ARITHMETIC_AMPLIFICATION_RATE_REVIEW.md. No web required since direct derivation from read sources. No RHverdict.

## Source receipt and meaning of the conclusion

Read completely, including all proofs, CA1–29 and TW1–21. To identify and transfer to the actual normalized boundary, also read completely HT1–18, HC1–15, and CV.1–12, including the exterior-minor additions CV.10a. The hashes of the files read are:

| File, relative to `workspace:/` | SHA256 |
|---|---|
| `work/rh_counterfactual_20260913/continuation2/combined_arithmetic_restriction.tex` | `EE8FB79B97F2BFD367D9758661BA067DE98C4AE2A8AA97FB147B5DC34557DA35` |
| `work/rh_counterfactual_20260913/continuation2/arithmetic_tail/arithmetic_tail_windows.tex` | `E2ABF620498569E6FE6BD767D7BA68576960AEF20EE30A6BF282AA16EE27640C` |
| `output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/HC.tex` | `A723E14FEFB7ECB3B7B79A122C8F98CC631E42FDD30FEDA64F7446BF9872A141` |
| `output/tau_split_zero_counterfactual_reconstruction_20260913/proof_inputs/HT.tex` | `74F8B45052C6F10D3D0ECD8A861336E2B66B19FD94ED26921889C22BF932C449` |
| `output/tau_split_zero_counterfactual_reconstruction_20260913/original_programme/tex/cyclic_control_determinant_increments.tex` | `06B526EA602E396C00A85BEDAB0FD59B8170F5E73CC5102C18AB892B86B0359D` |

The calculations below establish that the proved fixed-reference comparison envelopes have positive leading order relative to the full trace amplification, while the original elementary four-volume upper envelope is much larger. The exact volume-to-control morphism is explicitly calculated below. No bound in the audited sources proves an upper estimate tending to zero relative to the same normalized boundary control's trace floor. This concerns the listed estimates; it is not an assertion that all further arithmetic methods fail or that their actual scalar correction attains its present error envelope.

## 1. Exact amplification, with both parities and all orders

Retain the original fixed actual hypothetical quartet

\[
\tfrac12\pm\delta\pm i\gamma,\qquad
0<\delta<\tfrac12,\quad \gamma>0,\quad m\ge1,
\]

with all four factors of their full common order \(m\). For each integer \(k\ge3\), retain

\[
c=k/2,\quad \ell=1+k(m-1),\quad q=\ell(k+1)^2,
\]

\[
\chi(S)=\prod_{a,b=0}^k
\bigl(S-c-(2a-k)\delta-i(2b-k)\gamma\bigr)^\ell,
\quad
\mathcal L=2\delta\ell(k+1)\left\lfloor\frac{(k+1)^2}{4}\right\rfloor.
\]

No sum coordinate or quotient frame is changed. Direct cancellation of the displayed factors gives

\[
\frac{\mathcal L}{qk}
=\begin{cases}
\displaystyle\frac{\delta(k+1)}{2k},&k\text{ odd},\\[4pt]
\displaystyle\frac{\delta(k+2)}{2(k+1)},&k\text{ even}.
\end{cases}
\tag{R1}
\]

Indeed the floor is \((k+1)^2/4\) for odd \(k\), and \(k(k+2)/4\) for even \(k\). In particular

\[
\mathcal L\sim\frac\delta2 kq,
\quad
\begin{array}{c|cc}
 &q&\mathcal L\\\hline
m=1 & k^2(1+o(1))& (\delta/2)k^3(1+o(1))\\
m\ge2 &(m-1)k^3(1+o(1))& (\delta(m-1)/2)k^4(1+o(1)).
\end{array}
\tag{R2}
\]

The same exact cancellation gives

\[
\frac{q^2}{\mathcal L}
=\begin{cases}
2\ell(k+1)/\delta,&k\text{ odd},\\[3pt]
2\ell(k+1)^3/[\delta k(k+2)],&k\text{ even}.
\end{cases}
\tag{R3}
\]

Thus \(q^2/\mathcal L\sim 2q/(\delta k)\) diverges with order \(k\) for \(m=1\) and \(k^2\) for \(m\ge2\).

## 2. The comparison constants have an explicit strictly positive linear term

Use precisely TW1–TW8:

\[
\alpha=\pi/2,\quad p=8m-9/2,\quad B=42+8m,\quad M=B/2,
\]

\[
M_\alpha=\int_{\mathbb R}e^{\alpha u}w_h(u)\,du,
\quad \vartheta_h=\int_{-1}^1w_h(u)\,du,
\quad w_h(u)=\frac{|(2\xi/h)(1/2+iu)|^2}{2\pi},
\]

\[
a_k=\frac{c_h\vartheta_h^{k-3}e^{-\alpha(k-3)}(k-2)^{-B}}
{C_\Gamma 2^{B/2}},\quad
A_k=\frac{C_h}{c_\Gamma}k^{p+1}M_\alpha^{k-1},\quad
D_n=[1+4(n+M)^2]^M.
\]

All constants are those of the actual arithmetic envelope; none is a freely chosen metric. Define the real number

\[
d_h=\alpha+\log(M_\alpha/\vartheta_h).
\tag{R4}
\]

It satisfies \(d_h>\alpha>0\). To verify the strict inequality, evenness and nonnegativity of \(w_h\) give

\[
M_\alpha=\int_{\mathbb R}\cosh(\alpha u)w_h(u)\,du.
\]

The nonzero entire quotient \(2\xi/h\) has isolated zeros on the integration line, so \(w_h>0\) almost everywhere. On \([-1,1]\), \(\cosh(\alpha u)\ge1\), and the integral outside this interval is strictly positive. Therefore \(M_\alpha>\vartheta_h\), proving the claim.

Set

\[
H_m=p+1+B=16m+77/2,
\]

\[
C_0=-\log M_\alpha+3(\log\vartheta_h-\alpha)
+\log\frac{C_hC_\Gamma}{c_\Gamma c_h}+\frac B2\log2.
\]

Taking the logarithms of the literal constants gives the exact identity, for every \(k\ge3\),

\[
\log(A_k/a_k)
=k d_h+H_m\log k+C_0+B\log(1-2/k).
\tag{R5}
\]

Define the CA13 and CA20 quantities without changing them:

\[
\Lambda_k=\log(A_k/a_k)+\log D_{2q},\qquad
E_k=2\log(A_k/a_k)+\log D_{q-1}+\log D_q.
\]

For fixed \(M\), direct extraction of the leading factor inside \(D_n\) proves

\[
\log D_{2q}=B\log q+B\log4+O_h(1/q),
\]

\[
\log D_{q-1}+\log D_q=2B\log q+2B\log2+O_h(1/q).
\tag{R6}
\]

For example \(1+4(2q+M)^2=16q^2[1+M/q+(4M^2+1)/(16q^2)]\); multiplying its logarithm by \(M\) proves the first equality. The second follows from the corresponding factorizations with \(q-1\) and \(q\). Since \(\log(1+x)=O(x)\) as \(x\to0\), the remainders have the stated orders.

Put \((\nu_m,r_m)=(2,1)\) for \(m=1\), and \((\nu_m,r_m)=(3,m-1)\) for \(m\ge2\). The exact formula for \(q\) gives
\(\log q=\nu_m\log k+\log r_m+O_h(1/k)\).
Equations (R5)–(R6) now prove

\[
\Lambda_k=k d_h+(H_m+B\nu_m)\log k
+C_0+B\log r_m+B\log4+O_h(1/k),
\tag{R7}
\]

\[
E_k=2k d_h+2(H_m+B\nu_m)\log k
+2C_0+2B\log r_m+2B\log2+O_h(1/k).
\tag{R8}
\]

In particular, \(\Lambda_k/k\to d_h\), \(E_k/k\to2d_h\), and
\(E_k-2\Lambda_k\to-B\log4\).

## 3. Exact scales of the existing comparison upper envelopes

CA14 proves

\[
|\Delta_\sigma|=|B_{\rm ar}-B_\sigma|
\le L_q(D_*)\le(2q-1)\Lambda_k.
\]

Combining (R1), (R7), and \((2q-1)/q\to2\) proves the explicit limit

\[
\boxed{\frac{(2q-1)\Lambda_k}{\mathcal L}\longrightarrow
\frac{4d_h}{\delta}>0.}
\tag{R9}
\]

The two separate CA12 scalar error envelopes have this same leading limit: their numerators are respectively
\(qE_k\) and
\(q[2\log(A_k/a_k)+\log D_{2q-1}+\log D_{2q}]\),
both equal to \(2d_h qk+O_h(q\log k)\) by (R5)–(R8).
This is a statement about the proved envelopes. It does not imply any lower bound of this order for \(|\Delta_\sigma|\) or for the more precise computable spectral sum \(L_q(D_*)\).

The improved nonlinear angle upper envelope in CA17b has the same exact leading overhead. Write, as there,

\[
\widehat\Psi_q(t)=(4q-2)\log\cosh(t/2),\qquad
a_\sigma=\widehat\Phi_q(B_\sigma)\ge0,
\]

\[
U_{\rm angle}=\widehat\Psi_q(a_\sigma+\Lambda_k).
\]

For real \(t,x\ge0\), the addition formula gives

\[
\cosh x\le\frac{\cosh(t+x)}{\cosh t}
=\cosh x+\tanh t\sinh x\le e^x,
\]

and \(\cosh x\ge e^x/2\). Taking logarithms at
\(t=a_\sigma/2\), \(x=\Lambda_k/2\) yields the finite bounds

\[
(2q-1)\Lambda_k-(4q-2)\log2
\le U_{\rm angle}-B_\sigma
\le(2q-1)\Lambda_k.
\tag{R10}
\]

Since \(q/\mathcal L\to0\), (R9) proves

\[
\boxed{\frac{U_{\rm angle}-B_\sigma}{\mathcal L}
\longrightarrow\frac{4d_h}{\delta}.}
\tag{R11}
\]

This conclusion is uniform in the nonnegative input \(B_\sigma\) to this particular formula. It does not use, or furnish, an asymptotic evaluation of the actual fixed-Gamma determinant at growing \(k,q\).

The smaller scalar errors and thresholds have different scales. Equations (R1), (R8) prove

\[
\frac{E_k}{\mathcal L}\to0,
\qquad
\frac{4q\log(\delta e k/8)-E_k}{\mathcal L}\to0.
\tag{R12}
\]

For the second assertion, divide its first term by \(qk\); its size is
\(4\log(\delta e k/8)/k\to0\). These are scalar window terms, not the normalized boundary control; the exact connection to that control is proved next.

## 4. Same original normalized boundary and its exact endpoint transfer

Let \(G_N\) be the canonical quotient Gram for the original measure
\(m_{h,k}(u)\,du\), and let \(A=M_S\) on the original increasing-power frame of \(E=\mathbb C[S]/(\chi)\). The quantity relevant to the trace amplification is

\[
H_N=G_N^{-1/2}(A^*G_N+G_NA-kG_N)G_N^{-1/2},
\qquad \varepsilon_N=\|H_N\|_{\rm op}.
\tag{R13}
\]

Here \(p_j\) is the actual monic orthogonal polynomial of degree \(j\) in \(S\),
\(\omega_j=\int|p_j(c+iu)|^2m_{h,k}(u)\,du\),
\(b_j=[p_j]_\chi\), and
\(K_N=\sum_{j=0}^N b_jb_j^*/\omega_j=G_N^{-1}\).
Write \(V_N=\det G_N\) in the original increasing-power frame and
\(B_{\rm ar}=\log[V_{q-1}V_q/(V_{2q-1}V_{2q})]\).
In the original isometric polynomial realization the ambient Hilbert space is
\(L^2(\mathbb R,m_{h,k}(u)\,du)\), and \(D\) is multiplication by
\(c+iu\), with domain \(\{f:uf\in L^2(m_{h,k})\}\).
All polynomial lifts belong to this domain. Its adjoint is multiplication by
\(c-iu\) on the same domain, so \(D^*+D=kI\) there. Under the original
isometric source map this is precisely the sum differential on the original theta representatives.

The exact original boundary \(\mathscr B_N=DR_N-R_NA\), with
\(R_N^*R_N=G_N\), satisfies

\[
H_N=-(U_N^*T_N+T_N^*U_N),\quad
U_N=R_NG_N^{-1/2},\quad T_N=\mathscr B_NG_N^{-1/2}.
\tag{R14}
\]

The signs follow by inserting \(DR_N=R_NA+\mathscr B_N\) into
\(D^*+D=kI\) in the original source pairing. Thus (R13) is the same relative boundary measured in HT8–HT14, not the unnormalized Gram or an arbitrary matrix surrogate.

For completeness, the reason the full trace gives \(\varepsilon_N\ge\mathcal L\) at every admitted degree is exact and finite. The orthogonal-polynomial recurrence gives

\[
AK_N+K_NA^*-kK_N
=\frac{b_{N+1}b_N^*+b_Nb_{N+1}^*}{\omega_N},\quad K_N=G_N^{-1}.
\]

Its congruence is \(H_N\), so \(H_N\) is Hermitian of rank at most two. Its trace is \(2\operatorname{Re}\operatorname{Tr}A-kq=0\). The orthogonal projection onto the image under \(G_N^{1/2}\) of the complete primary spaces with \(a>k/2\) has trace pairing

\[
2\delta\ell(k+1)\sum_{a>k/2}(2a-k)=\mathcal L.
\]

The finite sum equals \(\lfloor(k+1)^2/4\rfloor\). A trace-zero Hermitian matrix of rank at most two has eigenvalues \(\varepsilon_N,-\varepsilon_N\) and zeros; its trace pairing with any orthogonal projection is at most \(\varepsilon_N\). Hence

\[
\varepsilon_N\ge\mathcal L>0\qquad(N\ge q-1).
\tag{R15}
\]

Use exactly the endpoint weights of HC2:

\[
w_{q-1}=w_{2q-1}=1,\quad w_N=2\ (q\le N\le2q-2),\quad \sum_Nw_N=2q.
\]

Let

\[
\Omega_k=\log\frac{\omega_{2q-1}\omega_{2q}}{\omega_{q-1}\omega_q},
\quad P_k=P_-+P_+\ge0,\quad
B_{{\rm crit},k}=4q\log\mathcal L-\Omega_k.
\]

HC2 is the exact identity

\[
B_{\rm ar}=\sum_Nw_N\log(\varepsilon_N^2+\phi_N^2)-\Omega_k+P_k.
\]

Subtracting \(B_{{\rm crit},k}\), and using the exact sum of the weights, proves

\[
\boxed{B_{\rm ar}-B_{{\rm crit},k}
=P_k+\sum_Nw_N\log\frac{\varepsilon_N^2+\phi_N^2}{\mathcal L^2}\ge0.}
\tag{R16}
\]

Every term after \(P_k\) is nonnegative by (R15). This equality is the exact morphism between the scalar four-volume expression and the same normalized boundary control, including its phases and endpoint penalties.

Define the weighted geometric mean of the actual controls and their minimum:

\[
\varepsilon_{\rm gm}=\prod_{N=q-1}^{2q-1}\varepsilon_N^{w_N/(2q)},\qquad
\varepsilon_* =\min_{q-1\le N\le2q-1}\varepsilon_N.
\]

Since \(\log\varepsilon_N^2\le\log(\varepsilon_N^2+\phi_N^2)\), (R16) gives

\[
\boxed{
\mathcal L\le\varepsilon_*\le\varepsilon_{\rm gm}
\le\exp\!\left(\frac{B_{\rm ar}+\Omega_k-P_k}{4q}\right)
=\mathcal L\exp\!\left(\frac{B_{\rm ar}-B_{{\rm crit},k}-P_k}{4q}\right).}
\tag{R17}
\]

Each individual control also has a precise bound from the same identity: discard all the other nonnegative summands in (R16) and then discard \(\phi_N^2\) in the retained summand to obtain

\[
\boxed{\varepsilon_N\le\mathcal L
\exp\!\left(\frac{B_{\rm ar}-B_{{\rm crit},k}-P_k}{2w_N}\right).}
\tag{R18}
\]

These are finite bounds on the correct normalized controls. Substitution of any established scalar upper envelope \(B_{\rm cap}\ge B_{\rm ar}\) gives valid explicit upper expressions in (R17)–(R18). By (R16) those resulting expressions cannot be below \(\mathcal L\) when they retain a valid upper bound on the actual counterfactual data.

TW16–TW19 give, at these exact growing endpoints,

\[
\Omega_k=4q\log(4q/e)+O_h(k+\log q),\qquad
e^{\Omega_k/(4q)}=\frac{4q}{e}(1+o(1)).
\tag{R19}
\]

The first follows by adding the two finite errors in TW16 and using the bounded factorial-window error in TW18. Its error divided by \(q\) tends to zero, so exponentiation proves the second. Therefore

\[
B_{{\rm crit},k}
=4q\log(\delta e k/8)
+4q\log\frac{2\mathcal L}{\delta kq}
+O_h(k+\log q),
\tag{R20}
\]

where the trace correction retains its exact parity:

\[
\frac{2\mathcal L}{\delta kq}
=\begin{cases}1+1/k,&k\text{ odd},\\1+1/(k+1),&k\text{ even}.
\end{cases}
\tag{R21}
\]

In particular \(B_{{\rm crit},k}/\mathcal L\to0\). Equations (R16)–(R21) show explicitly why such a vanishing scalar ratio does not furnish a vanishing boundary-control ratio: the original control is recovered through a logarithmic window with a norm factor asymptotic to \(4q/e\), followed by exponentiation.

## 5. Size of the original elementary upper bound after that transfer

Retain HC6–HC8's literal positive constants

\[
a=\alpha D+\log256>0,\quad
b=\log(XK)+\alpha+16R_0/(3D),
\]

and its upper envelope

\[
\widehat{\mathcal U}_k
=2a q^2+2b kq+2Bq\log(1+(D+1)q)
+2q\log C_{\rm env}+q\log20.
\tag{R22}
\]

All constants here are fixed for the actual packet. Since \(k/q\to0\) and \(\log q/q\to0\), its ratio to \(q^2\) tends to \(2a\). Equations (R2)–(R3) give

\[
\frac{\widehat{\mathcal U}_k}{\mathcal L}
\sim\frac{4a q}{\delta k}\longrightarrow+\infty.
\tag{R23}
\]

Use this actual proved upper bound in (R17) and discard only the nonnegative penalty \(P_k\). The resulting upper expression for
\(\varepsilon_{\rm gm}/\mathcal L\) is

\[
F_k=\frac{e^{\Omega_k/(4q)}}{\mathcal L}
\exp\!\left(\frac{\widehat{\mathcal U}_k}{4q}\right)
=\frac{8}{\delta e k}(1+o(1))
\exp\!\left(\frac{\widehat{\mathcal U}_k}{4q}\right).
\tag{R24}
\]

Here (R1) and (R19) justify every factor. Substitution of (R22) proves

\[
\log F_k=\frac a2q+O_h(k+\log q)\longrightarrow+\infty.
\tag{R25}
\]

Thus this transfer is a proved upper on the correct object, but its explicit rate grows exponentially in \(q\). The CA21 minimum furnishes a potentially sharper, fully specified finite upper by replacing \(\widehat{\mathcal U}_k\) in (R24) by that minimum. The CA sources do not evaluate its growing-packet input \(B_\sigma\) to an opposing rate, and (R9)–(R11) quantify the guaranteed comparison overhead it carries.

## 6. Exact pointwise endpoint and boundary-energy checks

At the first admitted degree, CV.11 expands the same monic annihilator in the actual orthogonal basis,

\[
\chi=p_q+\sum_{j=0}^{q-1}\gamma_jp_j,
\qquad \gamma_j=\langle p_j,\chi\rangle/\omega_j.
\]

The original normalized control is exactly

\[
\varepsilon_{q-1}^2
=\frac{\sum_{j=0}^{q-2}|\gamma_j|^2\omega_j}{\omega_{q-1}}
=\frac{\|\chi\|^2-\omega_q-|\gamma_{q-1}|^2\omega_{q-1}}
{\omega_{q-1}}.
\tag{R26}
\]

The proof uses the inverse reduction isomorphism at degree \(q-1\):
\(b_i^*G_{q-1}b_j=\delta_{ij}\omega_j\), and
\(b_q=-\sum_{j<q}\gamma_jb_j\). Substituting those pairings into
\(\varepsilon^2=(ad-|c|^2)/\omega_{q-1}^2\) cancels exactly the top coefficient contribution, and orthogonality gives the second equality. The cross coefficient has not been set to zero. Neither TW15 nor its two long-window consequences estimate this subtracted projection norm or justify differencing its monic-norm errors at adjacent degrees.

The energy upper from HC12 likewise retains its actual extra factors:

\[
\frac{\varepsilon_N^2}{2}
\le\|\mathscr B_NG_N^{-1/2}\|_{\rm HS}^2
\le(1+\sqrt{\beta_N})^2J_N^D,
\]

\[
\beta_N=e^{e_N},\quad e_N=\log(V_N/V_{N+1}),\quad
J_N^D=\|DR_NG_N^{-1/2}\|_{\rm HS}^2.
\tag{R27}
\]

The first inequality is the orthogonal Hermitian/skew-Hermitian decomposition in HT14. The second is the quotient minimum and triangle calculation of HC12. Thus

\[
\varepsilon_N\le\sqrt2(1+e^{e_N/2})\sqrt{J_N^D}.
\tag{R28}
\]

This is another exact upper expression on the same normalized control. The audited statements do not bound its right side by \(o(\mathcal L)\); its full endpoint contraction and derivative-source energy are explicitly retained. The identity \(\sum_Nw_Ne_N=B_{\rm ar}\) and (R16) connect these endpoint factors to the very same finite arithmetic volumes.

The old convolution-reference condition number has a different explicitly proved role. CA29 gives a lower bound of order \(k\log k\) for its logarithm: the lower coefficient is \(1/2\) for \(m=1\) and \(1\) for \(m\ge2\). This is a spectral-spread lower bound on the old relative moment operator, not an upper bound on (R13). CA29 assigns no orientation of the window projections in that operator's eigenvectors and hence no sign to the scalar four-volume correction.

## Review finding

Within the fully read source set, all comparisons retain the literal actual quartet, multiplicity \(\ell\), original sum coordinate \(S\), full unitful observation, and actual arithmetic norm. The finite upper envelopes and their endpoint maps are compatible with the lower bound on the same normalized control. Their quantitative consequences are (R9), (R11), (R17)–(R18), and (R24)–(R28). No actual proved \(o(\mathcal L)\) upper for \(\varepsilon_N\), uniformly over the admitted growing packet or even for the window minimum \(\varepsilon_*\), is present in those estimates. The positive trace bound (R15) applies at every such degree; the small scalar errors (R12) are connected to it by the explicit calculation (R16)–(R21).

No fixed-\(k\) kernel asymptotic was substituted at \(N\) proportional to the growing \(q(k)\), and no conditional theorem was introduced in this review.

Independent arithmetic cross-check: the child reviewer `scale_crosscheck` separately verified (R1)–(R9), including the exact constants. Its durable derivation is `work/rh_counterfactual_20260913/continuation2/fixed_packet_kernel/amplification_rate_review/scale_crosscheck/REVIEW.md`. In its abstract arithmetic check, positivity of an arbitrary input-constant ratio was not assumed; the actual arithmetic positivity used here is proved in the paragraph following (R4).

Final independent full-report review: `scale_crosscheck` read R1–R28 and checked CA17a–b, HC2, and HC12a directly. Its returned finding was: “PASS R1–R28: no mathematical error found.” It separately confirmed the uniform nonlinear excess (R10), the original minus sign (R14), the complete primary trace (R15), and the exact denominators \(4q\) and \(2w_N\) in (R17)–(R18). No source edits were requested.
