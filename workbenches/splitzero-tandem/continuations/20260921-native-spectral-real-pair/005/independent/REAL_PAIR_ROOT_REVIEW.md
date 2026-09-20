# Independent derivation of the certified positive real pair

Date: 21 September 2026. This review covers the complete real-pair root certificate, its original-unit conjugation, and its period and symbol orders. The reviewed arithmetic source is `certify_real_pair.py`, SHA-256 `bb50ba841052d305fc1a66bbfab9095af816f4c8b05eb3f5a1fa578dab883bbe`, with the matching `REAL_PAIR_CERTIFICATE.json`. The bounded replay is `independent/check_real_pair_root.py`; it does not rewrite the source or its main receipt.

The original definitions and coefficient bounds read for this review are FPZ1–7 in `public_unit_phase_20260921_001/FABLE_TO_ORIGINAL_CONDUCTOR.tex`, UPP1–8 in `UNIT_PHASE_PERSISTENCE_BODY.tex`, and RPCJ1–23 in `independent/REAL_PAIR_COLLISION.tex`. The arithmetic provenance is Fredrik Johansson, *Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic*, original author source arXiv:1611.02831v1, the sections on features, radii and magnitude bounds, and precision and bounds cited by FPZ and UPP. This bounded review checks the mathematical use of inclusion arithmetic and replays Python-FLINT 0.9.0 at 768 bits; it does not claim a new reading of every section of Johansson's paper.

The conclusions below concern the specified geometric quartet. They make no identification of that quartet with zeros of the Riemann zeta function.

## RPR1. Exact original objects and the real rectangle

Retain

\[
\delta=\tfrac14,\quad \gamma=3,\quad \beta=\tfrac{143}{8},\quad
\eta=\tfrac{21025}{256},\quad
w=(\delta+i\gamma,\delta-i\gamma,-\delta+i\gamma,-\delta-i\gamma),
\quad \rho_a=\tfrac12+w_a.
\]

Let \(V_{ar}=w_a^r\), with \(1\le a\le4\) and \(0\le r\le3\). Let \(\zeta=e^{2\pi i/5}\) and
\(D_j=\operatorname{diag}(\zeta^{-j},\zeta^{-2j},\zeta^{-3j},\zeta^{-4j})\).
For these same row and column indices, the complete original matrix is

\[
\mathcal R(z)=\sum_{n\ge0}R_nz^n,\qquad
(R_n)_{ar}=\sum_{\substack{p,h\ge0\\2p+4h=5n+r+1-a}}
\frac{(\beta/3)^p\eta^h}{p!h!}
(-5)^{p+h-n}(a/5)_{p+h-n}.
\tag{RPR1}
\]

All centers and widths in the following display are exact rational numbers specified by terminating decimals:

\[
\begin{aligned}
c_z&=0.02211947780866184513200791639903555836071244787217846841,\\
c_x&=-1.466817440463494183975448871845763045856183562396293859,\\
r_z&=r_x=10^{-15},\\
\mathcal B&=[c_z-r_z,c_z+r_z]\times[c_x-r_x,c_x+r_x]\subset\mathbb R^2.
\end{aligned}
\tag{RPR2}
\]

Write \(J_{\rm ph}=\operatorname{diag}(1,-1,-1,1)\), \(W(x)=I+ixJ_{\rm ph}\). For real \(x\), every nonzero real \(\alpha\) gives the actual conjugate-unit matrix

\[
a=\alpha(1+ix),\qquad U=\alpha W(x)=\operatorname{diag}(a,\bar a,\bar a,a).
\]

The scalar \(\alpha\) cancels with its own inverse in the original conjugation. In particular no change to the unit magnitude is needed to obtain the matrix identity: for a prescribed positive magnitude \(m\), one can retain it by using \(\alpha=\pm m/\sqrt{1+x^2}\).

The exact rational family is defined wherever \(x\ne\pm i\):

\[
\begin{aligned}
W(x)^{-1}&=(I-ixJ_{\rm ph})/(1+x^2),\\
M_j(z,x)&=W(x)^{-1}V\mathcal R(z)^{-1}D_j\mathcal R(z)V^{-1}W(x),\\
t(\xi)&=(e^{\rho_a\xi})_a,\quad Q_0(v)=v_1v_4-v_2v_3,\\
f_j(\xi,z,x)&=Q_0(M_j(z,x)t(\xi)),\quad d_j(z,x)=f_j(0,z,x),\\
E_A(\xi,z,x)&=\prod_{j=1}^4 f_j(\xi,z,x),\quad
\mu_n(z,x)=\partial_\xi^nE_A(0,z,x).
\end{aligned}
\tag{RPR3}
\]

The previous small disk \(|x|<1\) from UPP2 does not contain this center. Formula RPR3 itself extends to the displayed domain by its exact inverse identity. On the entire interval used here, the replay proves \(1+x^2>3\). Thus it is defined on a complex neighborhood of the real rectangle once invertibility of \(\mathcal R\) is proved below. All original matrix orders, coordinates, factors, signs, and the \(1/2\) in each \(\rho_a\) are retained.

## RPR2. Every omitted coefficient is enclosed

For a contributing pair in RPR1 put \(m=p+h\) and \(L=m-n\). The defining constraint gives \(4m\ge5n-3\), so \(m\ge n\) for every nonnegative integer \(n\). Therefore \(L\ge0\). Since \(0<a/5<1\), factorwise comparison gives \((a/5)_L\le L!\). Also

\[
\frac{n!L!}{p!h!}=\frac{\binom mp}{\binom mn}\le2^m,
\quad 2m\le5n+3,\quad 2^m\le4\,6^n.
\]

For \(K=11/2\) the inequalities \(5\beta/3\le K^2\), \(5\eta\le K^4\), and \(K\ge1\) hold exactly. Hence a summand has absolute value at most

\[
5^{-n}\frac{K^{2p+4h}2^m}{n!}
\le4K^3\frac{(6K^5/5)^n}{n!}.
\]

For fixed \(n,a,r\), each \(h\) determines at most one \(p\), and the number of choices is at most
\(\lfloor(5n+3)/4\rfloor+1\le2n+2\). With \(C_R=4K^3\) and \(T_R=6K^5/5\), this proves

\[
|(R_n)_{ar}|\le C_R(2n+2)T_R^n/n!.
\tag{RPR4}
\]

This majorant proves entire convergence, including termwise differentiation on every bounded disk. Let \(N=650\), let \(\varrho\) be the upper modulus bound on the outward period ball, and put \(w=T_R\varrho\). For the three series, the absolute majorants indexed by \(n\) are

\[
C_R(2n+2)\frac{w^n}{n!},\qquad
C_R(2n+2)T_R\frac{w^{n-1}}{(n-1)!},\qquad
C_R(2n+2)T_R^2\frac{w^{n-2}}{(n-2)!}.
\]

For \(n\ge N+1\), their successive-term ratios are bounded respectively by

\[
q_0=\frac{2w}{N+2},\qquad q_1=\frac{3w}{N+1},\qquad
q_2=\frac{w(N+3)}{N(N+2)}.
\]

Indeed the exact ratios are \(w(n+2)/(n+1)^2\), \(w(n+2)/(n(n+1))\), and \(w(n+2)/((n+1)(n-1))\). The first two satisfy the stated upper bounds directly. The last is \(w(1+1/(n+1))/(n-1)\), a decreasing positive expression, so its maximum starts at \(n=N+1\). Each \(q_h<1\) is checked with outward arithmetic. Summing the three geometric majorants gives precisely

\[
\begin{aligned}
\tau_0&=\frac{C_R(2N+4)w^{N+1}}{(N+1)!(1-q_0)},\\
\tau_1&=\frac{C_R(2N+4)(N+1)T_Rw^N}{(N+1)!(1-q_1)},\\
\tau_2&=\frac{C_R(2N+4)N(N+1)T_R^2w^{N-1}}{(N+1)!(1-q_2)}.
\end{aligned}
\tag{RPR5}
\]

The recorded values satisfy
\(\tau_0<2.099\cdot10^{-161}\),
\(\tau_1<9.485\cdot10^{-157}\), and
\(\tau_2<1.349\cdot10^{-152}\).
Each bound is added to both real and imaginary parts of every matrix entry, which contains the disk error and therefore the complete complex tail.

The script's Pochhammer recurrence starts at one and multiplies successively by \(-(a+5(\ell-1))\); its \(\ell\)-th value is exactly \((-5)^\ell(a/5)_\ell\). Its enumeration of \(h\), parity test for \(2p\), and \(\ell=p+h-n\) therefore gives every coefficient of RPR1. Simultaneous Horner recursion, in the order used by the script,

\[
P_2\leftarrow zP_2+2P_1,\qquad
P_1\leftarrow zP_1+P_0,\qquad
P_0\leftarrow zP_0+R_n,
\]

follows by differentiating one Horner step twice. Thus, after the three tails are added, the matrix balls enclose \(\mathcal R,\mathcal R',\mathcal R''\), not substitutes for those functions.

## RPR3. Center rounding, Taylor enclosure, and complete invertibility

The input constructors for \(c_z,c_x,r_z,r_x\) return enclosing balls; they do not generally return the exact rational singleton. In this replay the center radii are less than \(4.187\cdot10^{-234}\) and \(1.271\cdot10^{-232}\). The outward period-box radius is slightly larger than the requested exact width, approximately \(1.0000000036275\cdot10^{-15}\). None of these enclosing balls is silently substituted for the exact rectangle RPR2.

The point evaluation contains the value at the exact rational center. The outward box contains RPR2. The complete second derivative is evaluated on that containing interval. For any exact point \(z\) in it and the exact center \(c_z\), the segment \(c_z+t(z-c_z)\), \(0\le t\le1\), stays inside the interval. The integral identities are

\[
\begin{aligned}
\mathcal R(z)&=\mathcal R(c_z)+\mathcal R'(c_z)(z-c_z)
+(z-c_z)^2\int_0^1(1-t)\mathcal R''(c_z+t(z-c_z))\,dt,\\
\mathcal R'(z)&=\mathcal R'(c_z)+(z-c_z)\int_0^1
\mathcal R''(c_z+t(z-c_z))\,dt.
\end{aligned}
\tag{RPR6}
\]

The ball difference used by the script contains the exact difference \(z-c_z\), including both center-rounding errors. If \(h\) bounds its modulus and \(L_{ar}\) bounds the modulus of the complete second derivative entry, the remainders are bounded by \(L_{ar}h^2/2\) and \(L_{ar}h\). This proves its Taylor enclosures without discarding center errors.

Let \(B_R\) be the exact complex dyadic midpoint matrix of the enclosed center inverse. The replay independently forms \(I-B_R\mathcal R(\mathcal B_z)\). The four row-sum bounds are, respectively, less than

\[
1.249\cdot10^{-11},\quad1.287\cdot10^{-12},\quad
1.002\cdot10^{-12},\quad1.205\cdot10^{-13}.
\tag{RPR7}
\]

Consequently, for every exact \(z\) in the period interval, \(\|I-B_R\mathcal R(z)\|_\infty<1\). The geometric operator series makes \(B_R\mathcal R(z)\) invertible. Since both factors are square, each factor is invertible. This proves invertibility of the complete original matrix everywhere needed, independently of accepting a finite approximate inverse as an existence proof. Invertibility also holds on an open complex neighborhood by continuity of its nonzero determinant.

## RPR4. Exact derivatives used in the real Jacobian

Write \(A_R=\mathcal R^{-1}\), \(C_j=A_RD_j\mathcal R\). Differentiating \(A_R\mathcal R=I\) gives

\[
(A_R)_z=-A_R\mathcal R_zA_R,\qquad
(A_R)_{zz}=2A_R\mathcal R_zA_R\mathcal R_zA_R-A_R\mathcal R_{zz}A_R.
\]

The product rule, without commuting any factors, then gives

\[
\begin{aligned}
(C_j)_z&=A_RD_j\mathcal R_z-A_R\mathcal R_zA_RD_j\mathcal R,\\
(C_j)_{zz}&=A_RD_j\mathcal R_{zz}-2A_R\mathcal R_zA_RD_j\mathcal R_z
+2A_R\mathcal R_zA_R\mathcal R_zA_RD_j\mathcal R
-A_R\mathcal R_{zz}A_RD_j\mathcal R.
\end{aligned}
\tag{RPR8}
\]

Conjugating these formulas by \(W^{-1}V\) and \(V^{-1}W\) proves the script's \(z\)-derivatives of \(M_j\). Moreover
\(W^{-1}W_x=(xI+iJ_{\rm ph})/(1+x^2)\). The scalar term commutes with \(M_j\), so

\[
\begin{aligned}
(M_j)_x&=i[M_j,J_{\rm ph}]/(1+x^2),\\
(M_j)_{zx}&=i[(M_j)_z,J_{\rm ph}]/(1+x^2),\\
(M_j)_{xx}&=-\bigl([[M_j,J_{\rm ph}],J_{\rm ph}]
+2ix[M_j,J_{\rm ph}]\bigr)/(1+x^2)^2.
\end{aligned}
\tag{RPR9}
\]

The last line follows by differentiating the first line, using that first line for \((M_j)_x\). Define the symmetric complex bilinear form
\(b(v,w)=v_1w_4+v_4w_1-v_2w_3-v_3w_2\), so \(Q_0(v)=b(v,v)/2\). For \(y=M_j\mathbf1\) and \(h=M_j(\rho_a)_a\), direct differentiation gives

\[
d_j=b(y,y)/2,\quad (d_j)_z=b(y,y_z),\quad(d_j)_x=b(y,y_x),
\quad(f_j)_\xi=b(y,h).
\tag{RPR10}
\]

A further product rule gives exactly the script's six second and mixed derivative expressions. This verifies every derivative entering the real Jacobian and the period/symbol checks. The quadratic is bilinear in the original coordinates; no Hermitian quadratic has been substituted.

## RPR5. Contraction on the exact rational rectangle

Define the real map

\[
F(z,x)=(\operatorname{Re}d_1(z,x),\operatorname{Im}d_1(z,x))^T.
\]

Its real Jacobian has columns \(((d_1)_z^{\rm Re},(d_1)_z^{\rm Im})^T\) and \(((d_1)_x^{\rm Re},(d_1)_x^{\rm Im})^T\), because the two input variables are real. Let the fixed exact dyadic preconditioner be

\[
P=2^{-64}\begin{pmatrix}
3218485790678941&-57245565561083039\\
-5877924768298298697&-18277625187819728703
\end{pmatrix}.
\tag{RPR11}
\]

Its determinant is enclosed in a strictly negative interval about \(-0.001161715807428054\), so it is invertible. In the replay each entry has zero ball radius. Define \(T(q)=q-PF(q)\), where \(q=(z,x)^T\), and use the norm
\(\|v\|_r=\max(|v_1|/r_z,|v_2|/r_x)\).
Let \(E\) be the interval matrix \(I-PDF(\mathcal B)\) obtained from the complete derivative enclosures. Put

\[
\kappa_i=\sum_{j=1}^2\sup|E_{ij}|\,r_j/r_i,
\qquad
\lambda_i=|(PF(c))_i|/r_i+\kappa_i.
\tag{RPR12}
\]

The script evaluates enclosing balls for these expressions; their strict upper comparisons therefore apply to the exact rational radii in RPR2. The complete computation proves

\[
\kappa_1\le\lambda_1<4.578\cdot10^{-9},\qquad
\kappa_2\le\lambda_2<1.829\cdot10^{-6}.
\tag{RPR13}
\]

For \(q,q'\in\mathcal B\), integrate the derivative of \(T\) on their joining segment. That segment is in \(\mathcal B\), so each coordinate of \(T(q)-T(q')\) is bounded by the corresponding row sum in RPR12. Thus
\(\|T(q)-T(q')\|_r\le\kappa\|q-q'\|_r\), with \(\kappa=\max_i\kappa_i<1\).
Taking \(q'=c\) also gives
\(|T(q)_i-c_i|/r_i\le\lambda_i<1\). Hence \(T\) sends the closed rectangle strictly into itself.

For completeness, start at any \(q_0\in\mathcal B\) and put \(q_{n+1}=T(q_n)\). The successive differences satisfy
\(\|q_{n+1}-q_n\|_r\le\kappa^n\|q_1-q_0\|_r\). The geometric sum proves the sequence is Cauchy. The closed rectangle is complete, so its limit \(q_*\) belongs to \(\mathcal B\); continuity gives \(T(q_*)=q_*\). If there were two fixed points their distance would be at most \(\kappa\) times itself, forcing equality. Since \(P\) is invertible, fixed points of \(T\) are exactly zeros of \(F\). This proves a unique real pair

\[
(z_*,x_*)\in\operatorname{int}\mathcal B,\qquad d_1(z_*,x_*)=0.
\tag{RPR14}
\]

The period interval is positive. Therefore \(u_*=1/z_*>0\) is an original positive real period, and the complete reciprocal enclosure is
\(u_*\in[45.20902385898\pm3.31\cdot10^{-12}]\).

## RPR6. Exact conjugation and the two orders

Let \(S\) be the permutation matrix exchanging primary indices \(1,2\) and \(3,4\). This is distinct from \(J_{\rm ph}\). The coefficient formula RPR1 is real, so
\(\overline{\mathcal R(\bar z)}=\mathcal R(z)\). The original ordered roots give \(\bar V=SV\); the original unit gives \(\bar U=SUS\); and \(\overline{t(\bar\xi)}=St(\xi)\). Finally a direct substitution gives \(Q_0(Sv)=-Q_0(v)\).

Fix the actual real unit at \(x_*\) and put \(L(z)=U^{-1}V\mathcal R(z)^{-1}\). Then

\[
\overline{L(\bar z)}=SL(z),\qquad
\overline{M_j(\bar z,x_*)}=SM_{5-j}(z,x_*)S.
\]

The first equality follows by multiplying
\(\bar U^{-1}\bar V=(SU^{-1}S)(SV)=SU^{-1}V\); the second also uses \(\bar D_j=D_{5-j}\). Substitution into the quadratic gives the precise sign

\[
f_{5-j}(\xi,z,x_*)=-\overline{f_j(\bar\xi,\bar z,x_*)}.
\tag{RPR15}
\]

In particular \(d_4(z_*,x_*)=0\). The complete enclosures exclude zero from \(d_2\) and \(d_3\), from \((d_1)_z\), and from \((f_1)_\xi\). More explicitly the certified intervals contain

\[
\begin{aligned}
d_2&\in[0.05410876\pm1.84\cdot10^{-9}]
+i[-0.31535702\pm5.02\cdot10^{-9}],\\
(d_1)_z&\in[852.90399\pm1.90\cdot10^{-6}]
+i[-274.28648\pm1.91\cdot10^{-6}],\\
(f_1)_\xi&\in[17.1783460\pm3.61\cdot10^{-8}]
+i[-6.8131052\pm4.44\cdot10^{-8}].
\end{aligned}
\tag{RPR16}
\]

These are enclosing intervals for the exact values; each listed value is nonzero by one of its real or imaginary component bounds. Put \(G=f_1f_2\) and define
\(G^\#(\xi,z)=\overline{G(\bar\xi,\bar z,x_*)}\). The two minus signs in RPR15 cancel, so
\(E_A(\xi,z,x_*)=G(\xi,z,x_*)G^\#(\xi,z)\).
At the root let

\[
A=G_z(0,z_*,x_*)=d_2(d_1)_z\ne0,\qquad
B=G_\xi(0,z_*,x_*)=d_2(f_1)_\xi\ne0.
\tag{RPR17}
\]

For fixed \(x_*\), Taylor's theorem in the original inverse period gives
\(G(0,z_*+\tau,x_*)=A\tau+O(\tau^2)\). Since \(z_*\) is real, the corresponding holomorphic conjugate series begins \(\bar A\tau\). Multiplication proves

\[
\mu_0(z_*+\tau,x_*)=|A|^2\tau^2+O(\tau^3),\qquad |A|^2>82176.
\tag{RPR18}
\]

This is a complex analytic expansion; it is not restricted to real approaches. Thus the complete period zero has multiplicity exactly two. Likewise at the fixed real period,

\[
E_A(\xi,z_*,x_*)=|B|^2\xi^2+O(\xi^3),\qquad
|B|^2>34.96,
\]

so \(\mu_0=\mu_1=0\), \(\mu_2=2|B|^2>69.92\), and the symbol order in the original \(\xi\) coordinate is exactly two. The exact change
\(z-z_*=-(u-u_*)/(uu_*)\) has nonzero derivative at \(u_*\); hence the period multiplicity in the original \(u\) coordinate is also two, with leading coefficient \(|A|^2/u_*^4\).

## RPR7. Exact-zero substitutions, complete jets, and generic inverse coefficient

For \(v_{j,n}=M_j(\rho_a^n)_a\), the quadratic product rule proves, for every nonnegative integer \(n\),

\[
\partial_\xi^nf_j(0,z,x)=\frac12\sum_{k=0}^n\binom nk
b(v_{j,k},v_{j,n-k}).
\tag{RPR19}
\]

This is exactly the script's factor-jet formula through order five. At the certified root it is correct to set the zeroth jets of factors 1 and 4 to exact zero: RPR14–15 already prove those equalities. This substitution gives root-specific enclosures. It must not be described as an enclosure of these zeroth jets at every point of the surrounding rectangle.

The product rule gives \(G_n=\sum_{k=0}^n\binom nk f_{1,k}f_{2,n-k}\). Conjugation at the real root then proves the exact complete moment formula

\[
\mu_n(z_*,x_*)=\sum_{k=0}^n\binom nk G_k\overline{G_{n-k}}.
\tag{RPR20}
\]

Complex conjugation exchanges the summands indexed by \(k\) and \(n-k\), so this expression is real for every \(n\). Nonzero imaginary interval widths in the receipt are enclosure widths, not imaginary parts of the exact moments. Formula RPR20 gives \(\mu_0=\mu_1=0\) exactly and \(\mu_2=2|B|^2\), agreeing with the separate order proof.

For the generic inverse coefficient in RPCJ11–16, retain

\[
c=|A|^2,\quad b=|B|^2,\quad R=2\operatorname{Re}(A\bar B),\quad
d=-iR,\quad e=-b.
\]

Then, with no sign changes,

\[
\Delta=d(d^2-2ce)=(-iR)(2cb-R^2).
\tag{RPR21}
\]

The complete enclosure proves \(R>3382\) and \(2cb-R^2<-5695694\). Hence \(\Delta\ne0\), selecting the generic case of RPCJ16 and RPCJ22. The leading degree-three inverse coefficient is \(-\Delta/c^4\), before multiplication by the unchanged \(\rho_3/\rho_0\); its modulus is enclosed by
\([4.224828\cdot10^{-10}\pm7.04\cdot10^{-17}]\). The checks therefore certify the nonzero coefficient needed for the five/three inverse-pole split, in addition to the root and the two exact orders.

## Review conclusion

No mathematical defect remains in the reviewed stable certificate for the real pair, full-series enclosures, complete-matrix inversion, center treatment, real-unit conjugation, or exact period/symbol orders. The proof needs the extended domain of RPR3 and the root-specific interpretation of the zero jet substitutions, both supplied above. The independent replay passes every original check and the additional enclosure assertions. This is a bounded mathematical review of the stated functions and point, not an arithmetic identification of the geometric quartet.
