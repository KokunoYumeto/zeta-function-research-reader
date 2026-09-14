# Independent finite Hankel certificate attachment review

Date: 13 September 2026. Scope: TC1–28, the actual dimension-16 certificate, and the exact finite-degree consequences for the counterfactual separator. This review changes no mathematical source or certificate input. Its only additions are this report, an exact rational checker, and that checker's receipt. The root task owns the complete user-input transcript and global research log.

The assigned task was: “Bounded independent subtask: read full work/tau_theta_hankel_error_control_20260913.tex TC1–28 and metadata/code/exactendpointreceipt under work/theta_certified_hankel_20260913. Parent task attach actualH15>0,H15shift>0 to totaloriginalobject and determine exactly what excludes about offcriticalseparator polynomial TC21–26. Calculate degree restriction and quantitative tail lower conditions (e.g. degree≤15 no negative form; 2m≤tailbound, rational degreecertificate threshold). Do not rerun costlyquadrature, no browsingunlessnecessary, no sourceedits. Check certificatehash869ebacd... actualschema/32pivots signs via exactrational read-only. Save total_object/HANKEL_FINITE_CERTIFICATE_ATTACHMENT_REVIEW.md. Mainagent(me) readingWBR packetmorphisms and TO/CAU/AG, writingadditivesource.”

The parent subsequently requested an explicit positive coefficient-norm margin from the stored triangular factors, both unshifted and shifted separator constructions, and reproducible endpoint checks. These are proved below.

## 1. Complete source read and endpoint audit

Read in full:

- `work/tau_theta_hankel_error_control_20260913.tex`, TC1–28, including both tail proofs, every factor in the moment recurrence, the complete separator construction, and the finite-certificate conclusion.
- `work/theta_certified_hankel_20260913/certify_theta_hankel.py`, all 163 lines, including endpoint export, entire callback, positive tail addition, coefficient recurrence, ordered unpivoted LDL recursion, input validation and source pinning.
- The method proof `CERTIFIED_ORIGINAL_THETA_HANKEL.md`, the complete `INDEPENDENT_TAIL_REVIEW.md`, `seal_exact_endpoints.py`, `EXACT_ENDPOINT_RECEIPT.json`, `CALCULATION_HANDOFF.json`, and `API_CONTRACT.txt` in that directory.
- The separate complete exact-integer recurrence checker `work/theta_certified_hankel_exact_rational_review_20260913.py`. Its stored receipt records the original certificate pin and a successful independent integer-interval recurrence; this review did not repeat that recursion or integration.

The newly executed checker is `hankel_certificate_attachment_exact_check.py` in this report's directory. It uses only Python standard-library integers and `Fraction`, reads all source inputs without modification, and writes `HANKEL_FINITE_CERTIFICATE_ATTACHMENT_EXACT.json`. It imports neither FLINT nor any numerical quadrature package. Reproduction is:

```powershell
python work/rh_counterfactual_20260913/total_object/hankel_certificate_attachment_exact_check.py
```

The exact independently recomputed certificate SHA-256 is

```text
869ebacd3f82e46c3fe5fac1f07bcbaae7f4c333e1a5ba2e0ffcb1f91884a0fc
```

The reviewed integrator source SHA-256 is

```text
a97486edc2fc1f05f155a9539ad280433be39a8f6924efbc8c1c1c4d71033950
```

Both pins agree with the stored exact-endpoint receipt, and the integrator pin agrees with the certificate's actual `source_sha256`. The actual schema contains `moments`, `a`, `b`, and `matrices`; each matrix has `rows` and a full `L` array. Each row has `dimension`, `pivot`, and `leading_determinant`. Signs were decided from `lower.numerator/lower.denominator`, never from a decimal display or a status string alone.

The checks prove that all 1400 exported intervals have positive dyadic denominators and ordered exact rational endpoints. There are 33 moments at precisely \(J=0,2,\ldots,64\), 264 finite integral pieces on the eight exact half-unit intervals for each moment, 33 \(a\)-coefficient intervals, and 32 \(b\)-coefficient intervals. Each finite piece's imaginary interval contains zero. The original \(a_0\) and all 33 tail decay denominators have positive lower endpoints. The run has dimension 16, working precision 1024 bits, target 850 bits, first omitted theta term 20, and retained interval length 4.

Both matrices contain precisely 16 successful ordered pivot rows, with dimensions 1 through 16. All 32 pivot lower endpoints and all 32 leading-determinant lower endpoints are strictly positive. In each stored \(L\), the diagonal is exactly 1 and the upper triangle is exactly 0. These checks reproduce the finite conclusion

\[
H_{15}=(b_{r+s})_{0\le r,s\le15}>0,
\qquad
H_{15}^{(1)}=(b_{r+s+1})_{0\le r,s\le15}>0.
\tag{HA1}
\]

The proof connecting the stored intervals to the exact theta integrals is the complete TC1–13 argument and the reviewed code. It retains \(g=2\xi\), both theta/reflection factors two, \(a_j=(-1)^jM_{2j}/(2j)!\), and the original division by \(a_0=M_0\). No zero ordinate enters the finite computation. The parent's independent whole-object review supplies the packet and support morphisms surrounding these already identical coefficient definitions.

## 2. New exact positive lower bounds from the unchanged factors

For \(\nu=0,1\), write the actual exact decomposition certified by TC13 as

\[
H_{15}^{(\nu)}=L_\nu D_\nu L_\nu^{\mathsf T},
\qquad L_\nu=I+E_\nu,
\tag{HA2}
\]

where \(E_\nu\) is strictly lower triangular. For each exported \(L_{\nu,ij}\), the maximum of the absolute values of its two rational endpoints bounds the absolute value of the exact entry. Summing those maxima along each off-diagonal row and column, then comparing the resulting exact fractions, gives separately for each matrix

\[
\|E_\nu\|_\infty<\frac1{64},
\qquad \|E_\nu\|_1<\frac1{64}.
\tag{HA3}
\]

These are exact strict rational comparisons. For orientation only, the respective maximum row/column upper sums are approximately \(0.013975636691632525/0.013864398166547352\) for shift 0 and \(0.014096202300891493/0.013982978039218483\) for shift 1. The exact fractions are in the receipt.

The same check verifies each individual diagonal pivot lower bound, not merely the last one:

\[
(D_0)_{jj}>6\cdot10^{-107},
\qquad
(D_1)_{jj}>7\cdot10^{-111},
\qquad 0\le j\le15.
\tag{HA4}
\]

For completeness, the norm inequality needed here follows directly from Cauchy–Schwarz. For any matrix \(E\) and vector \(x\),

\[
\begin{aligned}
\|Ex\|_2^2
&\le\sum_i\left(\sum_j|E_{ij}|\right)
                  \left(\sum_j|E_{ij}|\,|x_j|^2\right)\\
&\le\|E\|_\infty\|E\|_1\|x\|_2^2.
\end{aligned}
\tag{HA5}
\]

Apply this to \(E_\nu^{\mathsf T}\), whose 1- and infinity-norms are interchanged. For \(p\ne0\), the reverse triangle inequality and (HA3) give

\[
\|L_\nu^{\mathsf T}p\|_2
\ge\|p\|_2-\|E_\nu^{\mathsf T}p\|_2
>\frac{63}{64}\|p\|_2.
\tag{HA6}
\]

Set the following exact positive rational numbers, retaining their original scale:

\[
\gamma_0=\left(\frac{63}{64}\right)^2 6\cdot10^{-107},
\qquad
\gamma_1=\left(\frac{63}{64}\right)^2 7\cdot10^{-111}.
\tag{HA7}
\]

Substitute (HA4) and (HA6) into (HA2). For every nonzero real coefficient vector \(p\in\mathbb R^{16}\), this proves

\[
p^{\mathsf T}H_{15}^{(\nu)}p>
\gamma_\nu\|p\|_2^2>0.
\tag{HA8}
\]

The same calculation applies to complex vectors with the conjugate transpose, since the matrices and triangular factors are real. No congruence is performed on the coefficient vector in the asserted bound: it is the Euclidean norm of the original monomial coefficients. For degree below 15, append exact zero coefficients; this embeds the original smaller form as its leading principal restriction and retains (HA8).

## 3. Exact unshifted and shifted reciprocal forms

Use exactly the reciprocal zero coordinate in TC17:

\[
\beta=-\frac1{(\rho-1/2)^2}
=\frac{\gamma^2-\delta^2+2i\gamma\delta}
       {(\gamma^2+\delta^2)^2},
\qquad \rho=\frac12+\delta+i\gamma.
\tag{HA9}
\]

Here the ordinate \(\gamma\) in (HA9) is distinct from the new indexed rational constants \(\gamma_0,\gamma_1\) in (HA7). For every original real polynomial \(P(X)=\sum_{r=0}^d p_rX^r\), TC16 gives the two exact maps

\[
\mathcal Q_\nu(P)
:=\sum_jm_j\beta_j^{\nu+1}P(\beta_j)^2
=\sum_{r,s=0}^d p_rp_s b_{r+s+\nu}
=p^{\mathsf T}H_d^{(\nu)}p,
\qquad\nu=0,1.
\tag{HA10}
\]

To justify the shifted sum as well, let \(R_*\\) be exactly TC18 and put

\[
S_\nu=\sum_jm_j|\beta_j|^{\nu+1}.
\]

Then \(S_0=S_*\) and \(S_1\le R_*S_*<\infty\). For fixed \(P\), 
\(|P(\beta_j)|\le\|P\|_{R_*}\), so each sum in (HA10) is absolutely convergent. Expanding the finite product \(P(\beta_j)^2\) and applying TC16 proves the equality, with the indicated unshifted or shifted index. Conjugation stability proves that both sums are real. Consequently (HA8) is a rigorous restriction on the complete reciprocal sums, not only on a selected finite packet.

In particular, every real or rational nonzero polynomial of degree at most 15 has strictly positive values for both forms. A negative witness for either form has actual degree at least 16.

## 4. The counterfactual separator and its complete tail

Choose a nonreal reciprocal zero \(\beta\) and its conjugate, each with its actual multiplicity \(m\ge1\). Retain TC21 exactly:

\[
r=\frac{|\beta|}{2},\qquad
\mathcal A=\{\alpha:\alpha\text{ is another distinct reciprocal zero},\ |\alpha|\ge r\},
\]

where “another” excludes both \(\beta\) and \(\overline\beta\). Write \(a=\#\mathcal A\),

\[
B(X)=\prod_{\alpha\in\mathcal A}(X-\alpha),\qquad
B_0=\prod_{\alpha\in\mathcal A}(r+|\alpha|),\qquad
T_\nu=\sum_{|\beta_j|<r}m_j|\beta_j|^{\nu+1}.
\tag{HA11}
\]

Absolute summability makes \(\mathcal A\) finite; conjugation stability makes \(B\) real; and excluding the selected pair gives \(B(\beta)\ne0\). The original \(T_0=T_*\). Termwise comparison gives \(T_1\le rT_0\); it is strict when \(T_0>0\), because then at least one strictly positive summand has \(|\beta_j|<r\).

For each \(\nu\in\{0,1\}\), choose either of the two square roots \(c_\nu\) satisfying

\[
\beta^{\nu+1}c_\nu^2=-1,
\qquad |c_\nu|^2=|\beta|^{-\nu-1}.
\tag{HA12}
\]

The choice \(\nu=0\) is precisely TC22–24. Define the shifted companion with the same interpolation map and every original factor retained:

\[
\begin{aligned}
C_\nu&=\frac{|c_\nu|B_0}{|B(\beta)|}
\left(1+\frac{|\Re\beta|+r}{|\Im\beta|}\right),\\
w_{\nu,N}&=\frac{c_\nu}{\beta^NB(\beta)},\qquad
v_{\nu,N}=\frac{\Im w_{\nu,N}}{\Im\beta},\\
u_{\nu,N}&=\Re w_{\nu,N}-(\Re\beta)v_{\nu,N},\\
P_{\nu,N}(X)&=X^NB(X)(u_{\nu,N}+v_{\nu,N}X).
\end{aligned}
\tag{HA13}
\]

All coefficients of \(P_{\nu,N}\) are real. Direct substitution yields \(u_{\nu,N}+v_{\nu,N}\beta=w_{\nu,N}\), hence \(P_{\nu,N}(\beta)=c_\nu\ne0\) and \(P_{\nu,N}(\overline\beta)=\overline c_\nu\). The selected terms of \(\mathcal Q_\nu\) therefore sum to exactly (-2m), with the actual multiplicities intact. Every other term of modulus at least \(r\) vanishes because \(B\) vanishes there.

For every complex \(X\) with \(|X|\le r\), one has \(|B(X)|\le B_0\) and

\[
\begin{aligned}
|u_{\nu,N}+v_{\nu,N}X|
&\le |w_{\nu,N}|+
      (|\Re\beta|+r)\frac{|w_{\nu,N}|}{|\Im\beta|},\\
|P_{\nu,N}(X)|&\le C_\nu2^{-N}.
\end{aligned}
\tag{HA14}
\]

Define the actual signed residual sum

\[
\mathcal T_{\nu,N}
=\sum_{|\beta_j|<r}m_j\beta_j^{\nu+1}P_{\nu,N}(\beta_j)^2.
\tag{HA15}
\]

It is real by conjugation, and the absolutely convergent sum satisfies the exact identity and bound

\[
\mathcal Q_\nu(P_{\nu,N})=-2m+\mathcal T_{\nu,N},
\qquad
|\mathcal T_{\nu,N}|\le C_\nu^2T_\nu4^{-N}.
\tag{HA16}
\]

Thus the full residual, not an unsigned replacement for it, is related explicitly to the complete original form.

## 5. Degree restriction and quantitative lower tail requirement

Because \(B\) is monic of degree \(a\), define

\[
\epsilon_{\nu,N}=\begin{cases}1,&v_{\nu,N}\ne0,\\0,&v_{\nu,N}=0.\end{cases}
\]

In the second case \(u_{\nu,N}\ne0\), since \(w_{\nu,N}\ne0\). Thus no cancellation of the leading coefficient remains unaccounted for, and the exact degree is

\[
d_{\nu,N}:=\deg P_{\nu,N}=N+a+\epsilon_{\nu,N},
\qquad d_{\nu,N}\le D_N:=N+a+1.
\tag{HA17}
\]

Whenever the actual degree \(d=d_{\nu,N}\le15\), (HA8) applies to its original coefficients \(p=(p_0,\ldots,p_d)\). Equations (HA16) and (HA8) prove

\[
C_\nu^2T_\nu4^{-N}
\ge\mathcal T_{\nu,N}
>2m+\gamma_\nu\sum_{j=0}^{d}|p_j|^2.
\tag{HA18}
\]

Evaluation at \(\beta\) and Cauchy–Schwarz give, with the original powers retained,

\[
|\beta|^{-\nu-1}=|c_\nu|^2
=\left|\sum_{j=0}^{d}p_j\beta^j\right|^2
\le\left(\sum_{j=0}^{d}|p_j|^2\right)
     \left(\sum_{j=0}^{d}|\beta|^{2j}\right).
\tag{HA19}
\]

The finite positive denominator is never replaced by a normalized quantity. Substitution gives the proved quantitative restriction

\[
\boxed{
C_\nu^2T_\nu4^{-N}
>2m+
\frac{\gamma_\nu|\beta|^{-\nu-1}}
     {\displaystyle\sum_{j=0}^{d_{\nu,N}}|\beta|^{2j}}
\qquad(d_{\nu,N}\le15).
}
\tag{HA20}
\]

One may replace the upper summation index by any known degree bound \(D\\) with \(d_{\nu,N}\le D\le15\), obtaining a weaker valid bound. The strict sign comes from the strictly certified bounds (HA3)–(HA4), not from assuming a strict remainder estimate. In particular, even the weaker upper estimate \(C_\nu^2T_\nu4^{-N}\le2m\) is impossible in this degree range.

For the original TC construction, \(C_0=C_*\), \(T_0=T_*\). If \(a\le14\), choose the nonnegative integer \(N=14-a\), so \(D_N=15\) and the finite certificate applies regardless of the leading-linear-coefficient phase. This yields

\[
C_*^2T_*
>4^{14-a}\left(2m+
\frac{\gamma_0|\beta|^{-1}}
     {\displaystyle\sum_{j=0}^{15}|\beta|^{2j}}\right).
\tag{HA21}
\]

The analogous statement holds with \(C_1,T_1,\gamma_1,|\beta|^{-2}\). If \(a=15\), only the possible phase \(v_{\nu,0}=0\) gives a degree-15 separator, and (HA20) applies precisely in that case. If \(a\ge16\), every \(P_{\nu,N}\) has degree at least 16, so these two finite matrices supply no inequality of the form (HA20) for this family. These distinctions follow from the exact degree formula, rather than treating the nominal upper bound as an equality.

For \(T_\nu>0\), define the same explicit integer as in TC23,

\[
N_{\nu,*}=\max\left\{0,1+\left\lfloor
\frac{\log(C_\nu^2T_\nu/m)}{\log4}\right\rfloor\right\}.
\tag{HA22}
\]

For \(N\ge N_{\nu,*}\), one has \(C_\nu^2T_\nu4^{-N}<m\). Indeed, if \(N_{\nu,*}>0\), then \(N_{\nu,*}>\log_4(C_\nu^2T_\nu/m)\). If \(N_{\nu,*}=0\), the defining maximum forces that logarithm to be negative. In both cases the strict inequality follows; increasing \(N\) preserves it. For \(T_\nu=0\), take \(N_{\nu,*}=0\); the tail then vanishes exactly. Consequently (HA16) gives a negative form, and the actual finite result forces

\[
\deg P_{\nu,N}\ge16\quad(N\ge N_{\nu,*}),\qquad
N_{\nu,*}+a+1\ge16.
\tag{HA23}
\]

Equivalently \(N_{\nu,*}\ge\max\{0,15-a\}\); if \(v_{\nu,N_{\nu,*}}=0\), the stronger \(N_{\nu,*}+a\ge16\) holds. When \(T_\nu=0\), (HA23) says \(a+1\ge16\), with \(a\ge16\) in the zero-linear-coefficient phase. The finite certificate supplies these actual restrictions, without bounding \(a\), \(T_\nu\), or the unknown reciprocal set universally.

## 6. What the shifted certificate also says about the very same TC polynomial

There is a second exact use of \(H_{15}^{(1)}>0\) that does not change \(c_0\) or \(P_{0,N}\). In \(\mathcal Q_1(P_{0,N})\), the selected terms are

\[
m\beta^2c_0^2+m\overline\beta^2\overline{c_0}^2
=-m\beta-m\overline\beta=-2m\Re\beta.
\tag{HA24}
\]

Its residual signed sum has absolute value at most \(C_*^2T_1 4^{-N}\le rC_*^2T_*4^{-N}\). If \(\deg P_{0,N}\le15\), (HA8) therefore proves, simultaneously with (HA18),

\[
C_*^2T_*4^{-N}
>\max\left\{
2m+\gamma_0\|p\|_2^2,
\frac{2m\Re\beta+\gamma_1\|p\|_2^2}{r}
\right\}.
\tag{HA25}
\]

The maximum is well-defined even if the second numerator is negative. In particular its elementary strict lower bound is

\[
C_*^2T_*4^{-N}>
\max\left\{2m,\frac{4m\Re\beta}{|\beta|}\right\}.
\tag{HA26}
\]

The shifted term strengthens this elementary bound exactly when \(\Re\beta/|\beta|>1/2\). The exact coefficient lower estimate (HA19) with \(\nu=0\) can be inserted in both entries of (HA25). This is an additional relation on the original TC polynomial; it is distinct from constructing the shifted separator \(P_{1,N}\) in (HA13).

## 7. Rational rounding and the minimal unresolved dimension

For \(\nu=0,1\), the exact polynomial identity \((P+E)^2-P^2=2PE+E^2\) and the absolutely convergent definition (HA10) give

\[
|\mathcal Q_\nu(P+E)-\mathcal Q_\nu(P)|
\le S_\nu\|E\|_{R_*}
\left(2\|P\|_{R_*}+\|E\|_{R_*}\right).
\tag{HA27}
\]

For any \(P=P_{\nu,N}\) for which (HA16) gives \(\mathcal Q_\nu(P)\le-m\), take the nominal bound \(D=N+a+1\). Round every original coefficient slot through degree \(D\) to a nearest multiple of (1/H), where the positive integer \(H\) obeys

\[
\frac{\sum_{j=0}^{D}R_*^j}{2H}
\le\min\left\{1,
\frac{m}{2S_\nu(2\|P\|_{R_*}+1)}\right\}.
\tag{HA28}
\]

The coefficient error has \(R_*\)-norm at most the left side, so (HA27) proves \(\mathcal Q_\nu(\widetilde P)\le-m/2<0\). Original zero slots remain exactly zero, including slots above the actual degree of \(P\). The finite certificate therefore imposes the actual restriction

\[
\deg\widetilde P\ge16,
\tag{HA29}
\]

even when a nonzero leading coefficient might otherwise have rounded to zero. Such rounding cannot reduce a negative witness into a certified positive degree range. For \(\nu=0\), (HA28) is exactly TC25, not a new coefficient convention.

For a real rational polynomial of actual degree \(d\), its unshifted form uses exactly \(b_0,\ldots,b_{2d}\) in the original monomial matrix. The recurrence through \(b_{2d}\) requires \(a_0,\ldots,a_{2d+1}\), hence moments through \(M_{4d+2}\). Its shifted form uses \(b_1,\ldots,b_{2d+1}\), whose recurrence requires moments through \(M_{4d+4}\). All intermediate even moments and the original \(a_0\) are retained. Thus the first degree not settled by the completed matrices is \(d=16\), with matrix dimension 17: the unshifted form requires moments through \(M_{66}\), and the shifted form through \(M_{68}\). This describes the full-matrix recurrence representation; a specially sparse coefficient vector may omit some individual products but does not change the degree restriction.

For every rational vector of degree at most 15, TC15's rational upper enclosure is at least the exact positive value in (HA8). Therefore no outward enclosure computed correctly from these same coefficients can have a strictly negative upper endpoint at these degrees. For degree at least 16, the completed finite certificate gives no sign conclusion by itself. A verified negative upper endpoint at such a degree would supply the actual negative witness, whereas the present positive certificate supplies neither an off-critical zero nor positivity at every degree.

## 8. Stronger original-threshold restriction from the shifted separator

The two separately constructed separators in (HA13) retain the same \(B_0,B(\beta),r\). Formula (HA12) therefore proves the exact scalar relation

\[
C_1^2=\frac{C_0^2}{|\beta|},\qquad
C_1^2T_1\le\frac12 C_0^2T_0.
\tag{HA30}
\]

The second inequality is \(T_1\le rT_0\) and \(r=|\beta|/2\), with both factors retained. If the shifted separator \(P_{1,N}\) has actual degree \(d_{1,N}\le15\), its bound (HA20) consequently forces

\[
C_0^2T_04^{-N}
>4m+
\frac{2\gamma_1|\beta|^{-2}}
     {\displaystyle\sum_{j=0}^{d_{1,N}}|\beta|^{2j}}.
\tag{HA31}
\]

This differs from (HA25): (HA31) uses the shifted polynomial with prescribed value \(c_1\), while (HA25) applies the shifted form to the unshifted polynomial with value \(c_0\).

In particular, for \(a\le14\), take \(N=14-a\). The nominal degree of the shifted polynomial is 15 regardless of its phase, so

\[
C_0^2T_0>4m\,4^{14-a},\qquad
\log_4(C_0^2T_0/m)>15-a.
\tag{HA32}
\]

This shows \(T_0>0\). Insert the strict logarithmic inequality into the original, unshifted TC23 integer definition \(N_*=N_{0,*}\): its floor is at least (15-a), and hence

\[
\boxed{N_*\ge16-a,\qquad N_*+a+1\ge17\quad(a\le14).}
\tag{HA33}
\]

The last expression is the nominal degree bound of that specific TC23 construction. Its actual degree may still be 16 when \(v_{0,N_*}=0\). This does not strengthen the unrestricted negative-witness dimension threshold beyond 17 and proves no positivity statement for \(H_{16}\). If \(a=15\), the shifted polynomial has degree at most 15 only when \(N=0\) and \(v_{1,0}=0\); in that phase, the same argument gives \(N_*\ge2\). For \(a\ge16\), this low-degree argument has no index to which it applies.

The boundary phase can be retained exactly as well. For \(a\le14\), put \(M=15-a\). If \(v_{1,M}=0\), the shifted polynomial has actual degree \(M+a=15\), so (HA31) at \(N=M\) gives \(N_*\ge M+2=17-a\). Combined with (HA33), the exact statement is

\[
N_*\ge16-a+\mathbf1_{\{v_{1,15-a}=0\}}
\qquad(a\le14).
\tag{HA34}
\]

For \(a=15\), the unshifted boundary phase \(v_{0,0}=0\) gives \(C_0^2T_0>2m\) from (HA18), and hence \(N_*\ge1\); the shifted boundary phase gives \(N_*\ge2\) as above. The two boundary phases cannot both occur at the same \(N\): they would make both nonzero \(w_{0,N}\) and \(w_{1,N}\) real, so \(c_1/c_0=w_{1,N}/w_{0,N}\) would be real. But (HA12) gives \((c_1/c_0)^2=1/\beta\notin\mathbb R\), a contradiction. This proves the phase exclusion from the original complex coordinate.

## 9. Acceptance and limits of the attachment

The full TC1–28 method and complete supplied integration/recurrence code agree on the original objects and constants. The independently checked hash, schema, ordered dyadic endpoints and 32 strict pivot signs accept the dimension-16 attachment. The additional exact rational factor bounds prove (HA7)–(HA8), and the complete separator calculation proves (HA17)–(HA34), including the shifted companion, the unchanged-polynomial cross-check, and the stronger restriction on the original TC23 integer.

These facts exclude every negative real or rational polynomial witness of actual degree at most 15 and force the explicit full-tail lower bounds above on every off-critical separator that fits that range. The logical passage from one off-critical reciprocal pair to a finite negative witness retains its parameter-dependent degree. There is no universal degree cutoff proved here and no RH contradiction or disproof claimed by these two finite positive matrices.

## 10. Full attachment-source review and original packet maps

At the parent's additional request, read the complete `certified_hankel_attachment.tex`, HCA.1–29, including HCA.19a, HCA.27a and HCA.27b, and checked the packet attachment against the complete original AG1–13 constructions in `arithmetic_gluing.tex`, TO.1–7 in `total_object.tex`, and CAU.11–13 in `coherent_assembly.tex`. Also read the complete `work/tau_genus_zero_product_proof_20260913.tex`, GF1–13.

The following exact maps and constants check:

- The source moment map is on the original \(\mathscr B\) and retains the nonzero boundary \(f_0\); its first coordinate \(M_0>0\) proves that this observation does not descend through the theta quotient. The finite recurrence is correctly typed as a rational map on \(a_0\ne0\), rather than a linear cochain morphism.
- The full unit \(\varepsilon_h=(j_h(g/h))^{-1}\) is retained in the actual section \(s_h\), its Mellin transform, its full-jet inverse, and its explicit \(D\)-boundary. The literal equality \(s_H\iota_{hH}=s_h\) follows from the old-section numerator \(b\,r_h(\varepsilon_hu)\), its degree bound, and the complete unit identity in AG12. This is valid for ambient critical packets as well as the offcritical part, since the original range proof covers the open strip.
- The actual reciprocal action \(T_h=-(A_h-\tfrac12I)^{-2}\) has the full Taylor coefficients \((-1)^{j+1}(j+1)(\rho-\tfrac12)^{-j-2}\). Its stated inverse uses the unique nilpotent square root with constant term one; coefficient comparison gives the inverse exactly. The derivative coefficient is nonzero, so no nilpotent jet is lost before the trace. Naturality with both the inclusion and restriction arrows follows by commuting their actual \(A-\tfrac12\) action with its inverse twice.
- The representative boundary in HCA.10–11 is a literal polynomial quotient because the two numerator classes agree after the same full unit. Its Mellin transform is exactly \(gK_{P,h}\), giving the displayed full theta boundary by Mellin injectivity.
- Each reciprocal fibre consists of precisely the two reflected original points, with equal full multiplicity. The complete reciprocal algebra therefore acts on two copies, and the scalar trace has exactly the factor one half and weight \(m_\beta\beta^{\nu+1}\). The bilinear scalar radical is precisely the ideal of classes vanishing at every reciprocal node: Lagrange interpolation at a node with nonzero value proves the converse. This scalar radical statement does not discard the original nilpotent action.
- Compressed traces on the old idempotent summand remain equal; uncompressed traces add the new packet. This is the correct trace law under divisor growth. No constant uncompressed trace is asserted.
- The GF proof establishes reciprocal summability and the genus-zero product with the unchanged mass. The selected-circle lower product bound, circle mean zero count, dyadic sums, and Fourier coefficient estimate for the real part of the zero-free logarithm all check. Absolute summability justifies the global half-trace and its independence of packet exhaustion. Both critical and offcritical nodes contribute to this actual global sum; the offcritical direct-sum action is the one already present in \(T_UQ\).
- The strict norm margin, degree-15 cone of sums of squares plus \(X\) times sums of squares, exact full-tail inequalities, same-polynomial shifted estimate, coordinate equivalence \(\Re\beta/|\beta|>1/2\iff\gamma^2>3\delta^2\), degree bookkeeping, and rational-witness threshold all check.

One literal error was found in the initial attachment source: its affine estimate immediately before HCA.25 omitted the plus sign between \(|w_{\nu,N}|\) and \((|\Re\beta|+r)|w_{\nu,N}|/|\Im\beta|\). The parent corrected it to the sum proved in (HA14). The opening locator of \(Q=\mathscr B/\Theta V\) was also corrected from TO.2 to TO.5. The complete corrected HCA source at SHA-256 `E1C1634E9A6BDA043764BA045EAF1E5D4A1A781BA42611B3E92F84577666A751` has no remaining defect in the reviewed statements. Later additive refinements are recorded separately in the final attachment review receipt.

The separator, shifted-form and degree calculations also received an independent subagent review. It independently caught the same missing-plus error and verified the new scalar relation (HA30) and the strict integer floors (HA33)–(HA34). No source inputs were edited by either reviewer.

The final additive HCA.27c and HCA.29a were then read completely at source SHA-256 `54465ACF93BBD3BB13F4670C258FBCAED7AFAB4D92DE0DFBA899617DD232DB3F`. They correctly retain the two separately phased polynomials, the exact factor one half, the strict positive coefficient margin, the nominal-degree floor for a at most 14, and the additional actual-degree boundary phase for a at most 15. Their proof agrees with (HA30)–(HA34). The final attachment has no remaining mathematical defect in the reviewed claims; this exact source hash is approved by the companion source-review receipt.

The parent's portability revision of the exact checker, adding explicit `--input-dir` and `--method-tex` arguments, was read in full. All exact checks are unchanged. The default workspace calculation was then repaired to resolve the parent path followed by `../../..`, avoiding an index error when the checker is moved to a shallow directory and explicit paths are supplied. The explicit-relative invocation passed again; no original certificate, integration source, TC proof or HCA proof was changed by this checker repair. The regenerated endpoint receipt and final source-review receipt contain the current checker hash.
