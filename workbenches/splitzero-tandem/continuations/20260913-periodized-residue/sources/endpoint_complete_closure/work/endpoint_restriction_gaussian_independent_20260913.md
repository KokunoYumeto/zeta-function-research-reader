# Independent Gaussian calibration and logarithmic certificate derivation

Date: 13 September 2026. Scope: Section 9, equations (59)–(65), of the supplied *Canonical restriction and the arithmetic endpoint volume*, together with the trace certificate (48)–(49) used there. The source is `sources/web_endpoint_restriction_delivery/Tau_Endpoint_Restriction_Control/NOTE.tex`, SHA-256 `ff4cc53cb4d3b10a9547a8a2365db7fd5d874bf1ecf7dd8542b8d1f05f433ef6`.

This is a paper derivation. No mathematical test, compiler, or Lean run was performed; the supplied source was not edited. The general operator constructions are being reviewed separately by the parent reviewer. All calculations below use the specified source measure, full two-dimensional quotient, and the original monic polynomial coordinates.

## 1. The original source and all monic norms

Set

\[
 d\nu(x)=\frac{7}{\sqrt{2\pi}}e^{-x^2/2}\,dx,
 \qquad S=1+ix,\qquad z=S-1,
 \qquad E=\mathbb C[S]/(z^2).
\]

The measure has mass \(7\), and its second moment is also \(7\). In particular the statement that its variance is one concerns the quotient of those two retained moments; the mass has not been assigned the value one. Polynomial norms are

\[
 \langle P,Q\rangle_\nu
 =\int_{\mathbb R}\overline{P(1+ix)}Q(1+ix)\,d\nu(x).
\]

Let

\[
 \operatorname{He}_n(x)
 =(-1)^n e^{x^2/2}\frac{d^n}{dx^n}e^{-x^2/2}.
\]

Repeated differentiation proves that this is a monic polynomial of degree \(n\). Repeated integration by parts has no boundary term, since every derivative of the Gaussian is a polynomial times the same Gaussian. Consequently, for a polynomial \(Q\) of degree below \(n\),

\[
 \int\operatorname{He}_n(x)Q(x)\,d\nu(x)
 =\int Q^{(n)}(x)\,d\nu(x)=0.
\]

Putting \(Q=\operatorname{He}_n\) instead gives

\[
 \int\operatorname{He}_n(x)^2\,d\nu(x)
 =n!\int d\nu(x)=7n!.
\]

Define the polynomial in the original \(S\) coordinate by

\[
 p_n(S)=i^n\operatorname{He}_n((S-1)/i).
\]

Its leading coefficient is exactly one. The evaluation map on the source line sends it to \(i^n\operatorname{He}_n(x)\), so Hermitian orthogonality gives the exact original squared norm

\[
 \omega_n=\|p_n\|_\nu^2=7n!.
\]

For completeness, the generating identity

\[
 e^{tx-t^2/2}=\sum_{n\ge0}\operatorname{He}_n(x)t^n/n!
\]

follows by applying the Taylor expansion of \(e^{-y^2/2}\) at \(y=x\) to \(y=x-t\). Its derivative in \(t\), followed by coefficient comparison, gives
\(\operatorname{He}_{n+1}=x\operatorname{He}_n-n\operatorname{He}_{n-1}\).
Multiplication by \(i^{n+1}\) and substitution \(x=z/i\) therefore yield the original-coordinate recurrence, including its plus sign:

\[
 p_0=1,\qquad p_1=z,\qquad p_{n+1}=zp_n+n p_{n-1}.
\]

In particular,

\[
 p_2=z^2+1,\qquad p_3=z^3+3z,
 \qquad p_4=z^4+6z^2+3.
\]

No polynomial in this calculation is divided by its norm.

## 2. The full quotient and its coordinate maps

The coordinate isomorphism

\[
 \mathbb C^2\longrightarrow E,
 \quad(a,b)^T\longmapsto [a+bz]
\]

has inverse \([P]\mapsto(P(1),P'(1))^T\). This is well-defined because the kernel of the unfactored map \(P\mapsto(P(1),P'(1))\) is exactly \((S-1)^2\mathbb C[S]\): Taylor division gives
\(P=P(1)+P'(1)(S-1)+(S-1)^2Q\).
The derivative coordinate is therefore retained literally.

The specified coordinate relation to the original basis is

\[
 (1,S)C=(1,z),\qquad
 C=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\]

Thus an \((1,z)\)-column becomes an \((1,S)\)-column by multiplication by \(C\); this statement fixes the direction of the basis map. In the \((1,z)\) coordinates,

\[
 b_0=\binom10,\quad b_1=\binom01,\quad
 b_2=\binom10,\quad b_3=\binom03,\quad b_4=\binom30.
\]

Multiplication by \(S=1+z\) is

\[
 A=\begin{pmatrix}1&0\\1&1\end{pmatrix}=I+N,
 \quad N=\begin{pmatrix}0&0\\1&0\end{pmatrix},
 \quad N^2=0,\quad N\ne0.
\]

The map onto the reduced quotient \(E/(z)\) is explicitly \((a,b)\mapsto a\), with kernel \(\mathbb C\cdot[z]\); it would discard the second coordinate. None of the matrices below is obtained by taking that further quotient. The relation \(b_2=b_0\) proves that the admitted exterior minor with indices \(\{0,2\}\) is zero while the two-dimensional quotient remains present.

## 3. All four kernel and Gram matrices

In these coordinates the formula being calibrated is

\[
 K_j=\sum_{d=0}^{j}\frac{b_db_d^*}{\omega_d},\qquad G_j=K_j^{-1}
 \quad(j\ge1).
\]

The literal mass appears in each denominator. Direct substitution of the five columns and the norms gives

\[
\begin{aligned}
 K_1&=\operatorname{diag}(1/7,1/7),\\
 K_2&=K_1+\operatorname{diag}(1/14,0)
      =\operatorname{diag}(3/14,1/7),\\
 K_3&=K_2+\operatorname{diag}(0,9/42)
      =\operatorname{diag}(3/14,5/14),\\
 K_4&=K_3+\operatorname{diag}(9/168,0)
      =\operatorname{diag}(15/56,5/14).
\end{aligned}
\]

Inversion yields

\[
\begin{array}{c|c|c}
 j&G_j&V_j=\det G_j\\\hline
 1&\operatorname{diag}(7,7)&49\\
 2&\operatorname{diag}(14/3,7)&98/3\\
 3&\operatorname{diag}(14/3,14/5)&196/15\\
 4&\operatorname{diag}(56/15,14/5)&784/75.
\end{array}
\]

Every matrix is positive definite. The equalities do not replace the literal mass with a normalized source.

## 4. Return spectra, gaps, traces, and total loss

The specified return map has type

\[
 T_{i,j}:(E,G_j)\longrightarrow(E,G_i),\qquad T_{i,j}=K_iG_j.
\]

Its underlying coordinate endomorphisms for the two windows are exactly

\[
 T_{1,3}=\operatorname{diag}(2/3,2/5),
 \qquad T_{2,4}=\operatorname{diag}(4/5,2/5).
\]

The proposed common gap has a literal matrix certificate:

\[
 K_1-\tfrac25K_3=\operatorname{diag}(2/35,0)\succeq0,
 \qquad
 K_2-\tfrac25K_4=\operatorname{diag}(3/28,0)\succeq0.
\]

The complementary endomorphisms and all moments needed for \(p=2\) are

\[
\begin{array}{c|c|c|c|c}
 &H=I-T&s_1&s_2&s_3\\\hline
 (1,3)&\operatorname{diag}(1/3,3/5)&14/15&106/225&854/3375\\
 (2,4)&\operatorname{diag}(1/5,3/5)&4/5&2/5&28/125.
\end{array}
\]

Consequently the losses are

\[
 \mathcal L_{1,3}=\log\frac{V_1}{V_3}=\log\frac{15}{4},
 \qquad
 \mathcal L_{2,4}=\log\frac{V_2}{V_4}=\log\frac{25}{8},
\]

and their sum is exactly

\[
 \mathcal B=\log(375/32).
\]

The older trace estimate on the same inputs has the stated values:

\[
\begin{aligned}
 \operatorname{Tr}(K_1^{-1}(K_3-K_1))&=1/2+3/2=2,\\
 \operatorname{Tr}(K_2^{-1}(K_4-K_2))&=1/4+3/2=7/4.
\end{aligned}
\]

## 5. Exact upper constants before any decimal observation

Put \(L=\log(5/2)\). For \(p=2\) and \(g_0=2/5\), the coefficient (48) is

\[
 c_2(3/5)=\frac{125}{27}\left(L-\frac{39}{50}\right).
\]

Substituting the trace moments into (49), with every rational term retained, gives

\[
\begin{aligned}
 U_{13}
 &=\frac{14}{15}+\frac{53}{225}
    +\frac{854}{3375}\frac{125}{27}
        \left(L-\frac{39}{50}\right)\\
 &=\frac{62}{243}+\frac{854}{729}L,\\
 U_{24}
 &=\frac45+\frac15
    +\frac{28}{125}\frac{125}{27}
        \left(L-\frac{39}{50}\right)\\
 &=\frac{43}{225}+\frac{28}{27}L.
\end{aligned}
\]

The second lines are exact equalities with the preceding original trace expressions; no remainder is omitted. In particular,

\[
 U_{13}+U_{24}=\frac{2711}{6075}+\frac{1610}{729}L.
\]

For each eigenvalue \(x\) of either \(H\), \(0\le x\le3/5\). Expanding \(-\log(1-x)\) and bounding each coefficient of the tail by the corresponding power of \(3/5\) proves

\[
 -\log(1-x)\le x+\frac{x^2}{2}+c_2(3/5)x^3.
\]

Taking the sum over the two eigenvalues proves that the exact \(U_{13},U_{24}\) above are upper bounds for their respective losses.

## 6. Explicit rational logarithmic certificate

For \(0\le t<1\), integration of the geometric series gives

\[
 \log\frac{1+t}{1-t}
 =2\sum_{a=0}^{m-1}\frac{t^{2a+1}}{2a+1}+E_m(t),
 \qquad
 0\le E_m(t)\le\frac{2t^{2m+1}}{(2m+1)(1-t^2)}.
\]

The latter follows term by term from \(2a+1\ge2m+1\) for every remaining index \(a\ge m\). No floating-point logarithm enters the following certificate.

Use \(\log(5/2)=\log2+\log(5/4)\), for which the two \(t\)'s are \(1/3\) and \(1/9\). Define the explicit rational numbers

\[
 S=2\sum_{a=0}^{20}\frac{1}{(2a+1)3^{2a+1}}
   +2\sum_{a=0}^{10}\frac{1}{(2a+1)9^{2a+1}},
\]

\[
 R=\frac{9}{172\cdot3^{43}}
       +\frac{81}{920\cdot9^{23}}.
\]

Thus \(S\le L\le S+R\). Here the powers in the tail can be written explicitly as
\(3^{43}=328256967394537077627\) and
\(9^{23}=8862938119652501095929\).
The finite rational comparisons are

\[
 \frac{916290731874155065}{10^{18}}<S,
 \qquad
 S+R<\frac{916290731874155066}{10^{18}}.
 \tag{R1}
\]

For an entirely integral form of this small certificate, set

\[
 P=\prod_{a=0}^{20}(2a+1),\quad D=3^{42}P,
\]

\[
 N=2\sum_{a=0}^{20}\frac{P}{2a+1}3^{41-2a}
   +2\sum_{a=0}^{10}\frac{P}{2a+1}3^{40-4a}.
\]

Then \(S=N/D\), all displayed quotients defining \(N\) are integers, and (R1) consists precisely of the two positive-denominator comparisons

\[
 10^{18}N>916290731874155065D,
\]

\[
 \frac{916290731874155066D-10^{18}N}{10^{18}D}
 >\frac{9}{172\cdot328256967394537077627}
  +\frac{81}{920\cdot8862938119652501095929}.
\]

These expressions provide the finite rational arithmetic in the proof; they are not a claim that a checker was executed. In particular they imply the slightly wider, convenient upper bound

\[
 L<\ell_+=\frac{91629073187415507}{10^{17}}.
\]

Let the stated target be the exact rational
\(T=2469887624578038/10^{15}\).
Substituting \(\ell_+\) into the total, all denominators are positive, and the comparison is explicit:

\[
\begin{aligned}
 \frac{2711}{6075}+\frac{1610}{729}\ell_+
 &=\frac{4501370195793474156750}{18225\cdot10^{17}},\\
 T&=\frac{4501370195793474255000}{18225\cdot10^{17}},\\
 T-\left(\frac{2711}{6075}+\frac{1610}{729}\ell_+\right)
 &=\frac{98250}{18225\cdot10^{17}}>0.
\end{aligned}
\]

Therefore

\[
 \boxed{\mathcal B\le U_{13}+U_{24}<2.469887624578038<15/4.}
\]

This proves the strict improvement against the original total trace upper bound \(2+7/4=15/4\).

## 7. The printed decimals are rounded observations

The source explicitly says that its exact logarithmic enclosures certify the comparison rather than its printed rounded values. That qualification matters: both decimals in (65) are strictly smaller than their exact \(U\)'s. To see this using (R1), put

\[
 \ell_- =916290731874155065/10^{18}<L.
\]

The exact differences at this lower endpoint are

\[
 \left(\frac{62}{243}+\frac{854}{729}\ell_-\right)
       -1.32854908781965490
 =\frac{3410}{729\cdot10^{18}}>0,
\]

\[
 \left(\frac{43}{225}+\frac{28}{27}\ell_-\right)
       -1.14133853675838303
 =\frac{250}{675\cdot10^{18}}>0.
\]

Thus neither printed decimal should be used as a rational upper endpoint. For readers needing standalone decimal upper endpoints, the wider pair

\[
 U_{13}<1.32854908781965492,
 \qquad U_{24}<1.14133853675838304
\]

follows from \(L<\ell_+\), again by positive-denominator rational comparison. Their sum is \(2.46988762457803796\), still strictly below the stated target. The exact expressions in Section 5 remain the preferred mathematical statement. The source's two displayed values are compatible with its description as rounded observations; the direction of rounding supplies no counterexample to the exact upper certificate or the total bound.

The approximate total in (64) is also consistent: the same series at \(t=1/7\) encloses \(\log(4/3)\), while
\(\log(375/32)=3L-\log(4/3)\). The exact determinant calculation above already proves the claimed total independent of that decimal observation.

## Finding

The mass-seven Gaussian norms, the nilpotent quotient and all remainder columns, the four kernel matrices, both return spectra, the literal gap certificates, the exact total \(\log(375/32)\), and the strict total upper comparison are valid. The two decimals in (65) must remain labeled as rounded observations; the exact upper bounds are the logarithmic expressions proved here.
