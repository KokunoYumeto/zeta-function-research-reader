# Original zeta reflection, full zero jets, and the retained arithmetic defect

24 September 2026. Independent derivation for the current reconstruction. The original Riemann zeta function remains the working function throughout. No claim of novelty or proof of RH is made.

## OZR0. Scope, source, and the user's order

The latest user argument restricts admissible deviations to structures that still recover the entire arithmetic and the same original zeta function. Separate branches use their own recovered counters. Consequently no selected numerical prime or integer is an input to the construction discussed here. The integer parameter introduced in OZR6 is used only after the whole arithmetic has been recovered. No counters from distinct branches are added or identified here. No arithmetic on the supporting datum τ〈Z1; no Z2〉 is defined.

This derivation calculates a symmetry of the actual original zeta function and its actual zero algebras. It constructs no alternative zeta function, invented zero set, or proposed off-critical zero. It calculates the reflection quotient explicitly; it does not identify that quotient with an unspecified larger quotient in the user's construction.

Human source: Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, [arXiv:2602.04022v1](https://arxiv.org/abs/2602.04022v1), original author `rhready.tex`, formula labelled `smallxi` and the functional-equation paragraph, local lines 526–545. The routed canonical source IDs are `PUBUNIT-171DAC50D1C3B7A2438B39AE` and `PUBUNIT-90A9C2A0907A753437719FD9`. The exact local source SHA-256 is `7f1888d82b42263faca4264f3f9fc77e5750c348640f85db0ac4569fe88ebab2`. Reading in this derivation covered lines 491–556 and the title/author metadata. The source's completed function supplies the functional equation; it does not replace the original zeta function in any receiver below. No Deligne theorem is imported by this file.

The precise source identity used is

\[
 C(s)\zeta(s)=C(1-s)\zeta(1-s),\qquad
 C(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2).
 \tag{OZR0.1}
\]

The factor \(C\), including both endpoint factors and the Gamma factor, stays explicit. OZR2 also calculates the exceptional points where it is not a holomorphic unit.

## OZR1. Conjugation and reflection on the original function

Put

\[
 S=\{s\in\mathbb C:0<\operatorname{Re}s<1\},\qquad
 r(s)=1-\overline s.
 \tag{OZR1.1}
\]

The map \(r:S\to S\) is an antiholomorphic involution. For a holomorphic function on an \(r\)-stable open set, define

\[
 (Hf)(s)=\overline{f(r(s))}.
 \tag{OZR1.2}
\]

Conjugating the absolutely convergent Dirichlet series on \(\operatorname{Re}s>1\) gives \(\overline{\zeta(\overline s)}=\zeta(s)\). Uniqueness of meromorphic continuation extends this equality to the original meromorphic zeta function. Thus

\[
 H\zeta(s)=\zeta(1-s).
 \tag{OZR1.3}
\]

The same real-type identity holds for \(C\): the Gamma integral on the positive real half-plane commutes with conjugation, and continuation preserves that identity. The other displayed factors of \(C\) have the same property, with the real logarithm used in \(\pi^{-s/2}=\exp(-s\log\pi/2)\).

On \(S\), neither endpoint factor vanishes and Gamma has neither a pole nor a zero. Hence \(C\) is a holomorphic unit there. Define the full ratio

\[
 A(s)=\frac{C(1-s)}{C(s)}
 =\frac{\frac12(1-s)((1-s)-1)\pi^{-(1-s)/2}\Gamma((1-s)/2)}
 {\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)}.
 \tag{OZR1.4}
\]

No endpoint factors have been removed from this formula. Substituting (OZR1.3) into (OZR0.1) proves

\[
 \zeta=A\,H\zeta \quad\hbox{on }S.
 \tag{OZR1.5}
\]

Real type and \(r^2=1\) give

\[
 HA(s)=\frac{C(s)}{C(1-s)}=A(s)^{-1}.
 \tag{OZR1.6}
\]

These are identities of functions on the stated domain, with no assumption on zero locations.

## OZR2. Endpoint, trivial-zero, and boundary data

The local Gamma facts used here are \(\Gamma(z)=z^{-1}+O(1)\) at zero and

\[
 \Gamma(-n+z)=\frac{(-1)^n}{n!z}+O(1),\qquad n\geq1.
 \tag{OZR2.1}
\]

The first follows from \(\Gamma(1+z)=z\Gamma(z)\) and \(\Gamma(1)=1\); applying that recurrence \(n+1\) times proves the second, including its sign and factorial. Gamma has no zeros: its Euler product

\[
 \frac1{\Gamma(z)}=z e^{\gamma z}
 \prod_{j=1}^{\infty}(1+z/j)e^{-z/j}
 \tag{OZR2.2}
\]

converges locally uniformly, since the logarithm of each tail factor is \(O(j^{-2})\) on compact sets, and away from \(0,-1,-2,\ldots\) the convergent tail is nonzero. Its zeros are exactly those displayed points, all simple. Formula (OZR2.2) is the usual Euler product for the Gamma function; it is not a zeta completion or a replacement zeta function.

At zero the original factors of \(C\) have the limit

\[
 C(0)=\lim_{s\to0}\frac12 s(s-1)\pi^{-s/2}
       \left(\frac2s+O(1)\right)=-1.
 \tag{OZR2.3}
\]

Thus the apparent singularity of \(C\) at zero is removable; the factor \(s\) and the Gamma pole have both been accounted for. At one,

\[
 C(s)=\frac12(s-1)+O((s-1)^2).
 \tag{OZR2.4}
\]

For \(n\geq1\), the residue at \(-2n\) is

\[
 R_n:=\operatorname{Res}_{s=-2n}C(s)
 =\frac12(-2n)(-2n-1)\pi^n\frac{2(-1)^n}{n!}.
 \tag{OZR2.5}
\]

All these residues are nonzero. These are all poles of \(C\); its only zero after removal of the singularity at zero is its simple zero at one.

For completeness the residue of the original zeta function at one can be read directly from its original Dirichlet series. For \(\operatorname{Re}s>1\), integration of the counting function gives

\[
 \zeta(s)=s\int_1^\infty\lfloor x\rfloor x^{-s-1}\,dx
 =\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx.
 \tag{OZR2.6}
\]

The second integral and its derivatives converge locally uniformly on \(\operatorname{Re}s>0\), because \(0\leq\{x\}<1\) and powers of \(\log x\) remain integrable against \(x^{-1-\delta}\) for every \(\delta>0\). Hence the residue at one is exactly one. Equations (OZR0.1), (OZR2.3), and (OZR2.4) then give

\[
 \lim_{s\to1}C(s)\zeta(s)=\frac12,
 \qquad \zeta(0)=-\frac12.
 \tag{OZR2.7}
\]

Indeed the source entire continuation of \(C\zeta\) has value \(1/2\) at both endpoints by its functional equation; division by \(C(0)=-1\) gives the last value.

At \(-2n\), the right side of (OZR0.1) has the nonzero value

\[
 C(1+2n)\zeta(1+2n),\qquad
 C(1+2n)=\frac12(1+2n)(2n)
 \pi^{-(1+2n)/2}\Gamma((1+2n)/2).
 \tag{OZR2.8}
\]

It is nonzero because every factor of \(C(1+2n)\) is positive and the convergent Dirichlet series \(\zeta(1+2n)\) is positive. Division by the simple pole of \(C\) proves that the original zeta function has a simple zero at \(-2n\), and retains its exact derivative:

\[
 \zeta'(-2n)=
 \frac{\frac12(1+2n)(2n)\pi^{-(1+2n)/2}
             \Gamma((1+2n)/2)\zeta(1+2n)}
 {\frac12(-2n)(-2n-1)\pi^n\frac{2(-1)^n}{n!}}.
 \tag{OZR2.9}
\]

The numerator and denominator retain all original endpoint and Gamma contributions.

Consequently \(A\) is a holomorphic unit on the reflection-stable open set

\[
 U=\mathbb C\setminus
 \bigl(\{0,-2,-4,\ldots\}\cup\{1,3,5,\ldots\}\bigr).
 \tag{OZR2.10}
\]

Its excluded local behavior is

\[
\begin{aligned}
 A(s)&=\tfrac12s+O(s^2) &&(s\to0),\\
 A(s)&=-\frac2{s-1}+O(1) &&(s\to1),\\
 A(s)&=\frac{C(1+2n)}{R_n}(s+2n)
            +O((s+2n)^2) &&(s\to-2n),\\
 A(s)&=-\frac{R_n}{C(1+2n)}\frac1{s-(1+2n)}+O(1)
             &&(s\to1+2n),\quad n\geq1.
\end{aligned}
 \tag{OZR2.11}
\]

For example \(H\zeta(s)=-1/s+O(1)\) at zero, so its pole times the displayed zero of \(A\) gives \(\zeta(0)=-1/2\). At one, \(H\zeta(s)=-1/2+O(s-1)\), so the displayed pole of \(A\) gives the residue one of \(\zeta\). At \(-2n\) a zero of \(A\) creates the original trivial zero; at \(1+2n\) the pole of \(A\) cancels the reflected trivial zero. A holomorphic zero-jet isomorphism must therefore not be asserted between those exceptional points. The meromorphic functional equation remains valid there with exactly these orders.

On either boundary line \(\operatorname{Re}s=0\) or \(\operatorname{Re}s=1\), every point other than the endpoints \(0,1\) belongs to \(U\); the holomorphic-unit calculations extend to a neighborhood of each such point. This statement neither assumes nor proves a zero-free boundary theorem.

## OZR3. The unital algebra map and the weighted involution

On \(\mathcal O(S)\), \(H\) is additive, conjugate-linear over \(\mathbb C\), multiplicative, unital, and involutive. For example

\[
 H(fg)=(Hf)(Hg),\quad H1=1,\quad H^2f=f.
 \tag{OZR3.1}
\]

Each identity follows by substitution into (OZR1.2). Define

\[
 Tf=A\,Hf.
 \tag{OZR3.2}
\]

Equations (OZR1.5) and (OZR1.6) prove

\[
 T\zeta=\zeta,\qquad T^2f=A(HA)H^2f=f.
 \tag{OZR3.3}
\]

Nevertheless

\[
 T1=A,\qquad T(fg)=A^{-1}(Tf)(Tg).
 \tag{OZR3.4}
\]

The function \(A\) is not identically one: approaching one through the real interval inside \(S\), (OZR2.11) gives its pole. Therefore \(T\) is not a unital algebra automorphism on \(\mathcal O(S)\). It is a conjugate-linear involution on that vector space which fixes the specified function \(\zeta\). The distinction is an exact product formula, not an assertion that the two maps are unrelated. It is \(H\), not an unweighted treatment of \(T\), that gives the unital algebra comparisons below.

## OZR4. Full derivative transport, including derivatives of the multiplier

A Taylor expansion or induction on the derivative gives

\[
 (Hf)^{(j)}(s)=(-1)^j\overline{f^{(j)}(r(s))}.
 \tag{OZR4.1}
\]

Differentiating (OZR1.5) by the product rule, for every integer \(n\geq0\), gives the complete identity

\[
 \zeta^{(n)}(s)=\sum_{j=0}^n
 \binom nj A^{(n-j)}(s)(-1)^j
 \overline{\zeta^{(j)}(r(s))},\qquad s\in S.
 \tag{OZR4.2}
\]

The derivatives of \(A\) may themselves be written without dropping any factor of \(C\). On \(S\), set \(\psi=\Gamma'/\Gamma\) and

\[
 L_j(s)=(-1)^{j-1}(j-1)!\left(\frac1{s^j}+\frac1{(s-1)^j}\right)
       -\mathbf1_{j=1}\frac{\log\pi}{2}
       +2^{-j}\psi^{(j-1)}(s/2),\quad j\geq1.
 \tag{OZR4.3}
\]

These are the \(j\)-th derivatives of any local holomorphic logarithm of the original \(C\). The constant factor \(1/2\) remains in \(A\); its logarithmic derivatives are zero. Put

\[
 B_j(s)=(-1)^jL_j(1-s)-L_j(s).
 \tag{OZR4.4}
\]

For \(k\geq1\), repeated differentiation of the exponential of a local logarithm proves

\[
 A^{(k)}(s)=A(s)k!
 \sum_{\substack{q_1,\ldots,q_k\geq0\\q_1+2q_2+\cdots+kq_k=k}}
 \prod_{j=1}^k\frac{B_j(s)^{q_j}}{(j!)^{q_j}q_j!}.
 \tag{OZR4.5}
\]

One proof is to expand
\(A(s+h)=A(s)\exp(\sum_{j\geq1}B_j(s)h^j/j!)\)
and collect the coefficient of \(h^k\); each displayed tuple records exactly all choices contributing that degree. For \(k=0\), the formula is \(A^{(0)}=A\). In particular

\[
 \frac{A'(s)}{A(s)}=
 -\left(\frac1{1-s}+\frac1{(1-s)-1}-\frac{\log\pi}{2}
              +\frac12\psi((1-s)/2)\right)
 -\left(\frac1s+\frac1{s-1}-\frac{\log\pi}{2}
              +\frac12\psi(s/2)\right).
 \tag{OZR4.6}
\]

Both endpoint contributions, both Gamma derivative contributions, and both powers-of-pi contributions remain displayed. Equations (OZR4.2)–(OZR4.6) specify every derivative term in the original-zeta comparison.

## OZR5. Actual zero algebras and all multiplicities

Let

\[
 Z=\{\rho\in S:\zeta(\rho)=0\}.
 \tag{OZR5.1}
\]

These are actual zeros of the original function. Since \(\zeta\) is not the zero function, its zeros in \(S\) are isolated and each has a finite multiplicity \(m_\rho\geq1\). At \(\rho\), its original Taylor expansion is

\[
 \zeta(\rho+z)=z^{m_\rho}u_\rho(z),\qquad
 u_\rho(z)=\sum_{j=0}^{\infty}
       \frac{\zeta^{(m_\rho+j)}(\rho)}{(m_\rho+j)!}z^j,
 \quad u_\rho(0)\ne0.
 \tag{OZR5.2}
\]

The unit \(u_\rho\) is retained as the explicitly displayed function; it has not replaced the original zeta function.

Let \(\mathcal O_\rho\) be the ring of holomorphic germs at \(\rho\), and define the full zero algebra

\[
 J_\rho=\mathcal O_\rho/(\zeta).
 \tag{OZR5.3}
\]

For a germ \(f\) at \(\rho\), the formula

\[
 H_\rho f(s)=\overline{f(r(s))}\quad(s\hbox{ near }r\rho)
 \tag{OZR5.4}
\]

is a unital conjugate-linear ring isomorphism \(\mathcal O_\rho\to\mathcal O_{r\rho}\), inverse to \(H_{r\rho}\). Since

\[
 H_\rho\zeta=A^{-1}\zeta
 \tag{OZR5.5}
\]

near \(r\rho\), and \(A\) is a unit there, the principal ideal generated by the original \(\zeta\) maps exactly onto the corresponding principal ideal. Therefore it induces a unital conjugate-linear algebra isomorphism

\[
 h_\rho:J_\rho\xrightarrow{\ \sim\ }J_{r\rho},
 \qquad h_{r\rho}h_\rho=1.
 \tag{OZR5.6}
\]

The isomorphism preserves the full multiplicity, not just the set of zero locations. Explicitly, with \(w=s-r\rho\),

\[
 h_\rho\left(\left[\sum_{j=0}^{m_\rho-1}c_jz^j\right]\right)
 =\left[\sum_{j=0}^{m_\rho-1}(-1)^j\overline{c_j}w^j\right].
 \tag{OZR5.7}
\]

To justify these coordinates, (OZR5.2) and invertibility of \(u_\rho\) show that the kernel of Taylor truncation is exactly \((\zeta)=(z^{m_\rho})\). Thus every class has precisely the displayed \(m_\rho\) coefficients. This is an explicitly proved coordinate map on the original quotient, not deletion of \(u_\rho\) from any analytic formula.

Alternatively (OZR4.2) evaluated at \(r\rho\) shows that derivatives of orders below \(m_\rho\) vanish there, while

\[
 \zeta^{(m_\rho)}(r\rho)
 =(-1)^{m_\rho}A(r\rho)
       \overline{\zeta^{(m_\rho)}(\rho)}\ne0.
 \tag{OZR5.8}
\]

Hence \(r\rho\in Z\) and \(m_{r\rho}=m_\rho\). For every \(\ell\geq0\), all higher terms remain

\[
 \zeta^{(m_\rho+\ell)}(r\rho)=
 \sum_{j=m_\rho}^{m_\rho+\ell}
 \binom{m_\rho+\ell}{j}A^{(m_\rho+\ell-j)}(r\rho)
 (-1)^j\overline{\zeta^{(j)}(\rho)}.
 \tag{OZR5.9}
\]

Terms below \(m_\rho\) in (OZR4.2) are exactly zero by definition of multiplicity; no nonzero contribution has been suppressed.

Multiplication by \(A\) after \(h_\rho\) gives the corresponding quotient map induced by \(T\). It is conjugate-linear and invertible, and obeys the weighted product identity (OZR3.4). Its value at the unit is \([A]\), so the unital algebra map used here remains \(h_\rho\); no assertion is made that \([A]\ne1\) in every individual zero algebra.

## OZR6. Recovered arithmetic characters and the complete nilpotent action

At the stage after the whole arithmetic has been reconstructed, as stipulated in OZR0, let \(a>1\) be any positive integer in that recovered arithmetic. Its real logarithm \(\log a>0\) gives the entire, nonvanishing function

\[
 E_a(s)=a^s=\exp(s\log a).
 \tag{OZR6.1}
\]

For every actual \(\rho\in Z\), its scalar value transforms as

\[
 E_a(r\rho)=a^{1-\overline\rho}
           =\frac a{\overline{a^\rho}}.
 \tag{OZR6.2}
\]

This calculation is downstream of whole arithmetic recovery and does not select a prime to construct that arithmetic.

Let \(F_{a,\rho}\) be multiplication by \([E_a]\) on \(J_\rho\), and set

\[
 V_{a,\rho}=aF_{a,\rho}^{-1}.
 \tag{OZR6.3}
\]

Invertibility follows from nonvanishing of \(E_a\). Both operators keep all infinitesimal terms. In the exact coordinates of (OZR5.7),

\[
\begin{aligned}
 F_{a,\rho}&=a^\rho\sum_{j=0}^{m_\rho-1}
                   \frac{(\log a)^j}{j!}M_z^j,\\
 V_{a,\rho}&=a^{1-\rho}\sum_{j=0}^{m_\rho-1}
                   \frac{(-\log a)^j}{j!}M_z^j,
 \qquad M_z^{m_\rho}=0,
\end{aligned}
 \tag{OZR6.4}
\]

where \(M_z\) is multiplication by \(z=s-\rho\). The finite sums are exact because the remaining terms belong to the original ideal \((\zeta)=(z^{m_\rho})\). Multiplication of the two original exponential functions proves

\[
 F_{a,\rho}V_{a,\rho}=V_{a,\rho}F_{a,\rho}=a\,1_{J_\rho}.
 \tag{OZR6.5}
\]

Since \(HE_a=aE_a^{-1}\), the full jet isomorphism satisfies

\[
 h_\rho F_{a,\rho}=V_{a,r\rho}h_\rho,
 \qquad
 h_\rho V_{a,\rho}=F_{a,r\rho}h_\rho.
 \tag{OZR6.6}
\]

For an explicit check, (OZR5.7) sends \(M_z\) to \(-M_w\) and scalar \(a^\rho\) to \(\overline{a^\rho}\). The right side has scalar \(a^{1-r\rho}=\overline{a^\rho}\) and precisely the powers \((-\log a)^jM_w^j/j!\). Every coefficient agrees. Thus (OZR6.2) and (OZR6.6) retain both the eigenvalue reflection and all multiplicity terms.

The exact diagram is

\[
\begin{array}{ccc}
 J_\rho&\xrightarrow{F_{a,\rho}}&J_\rho\\
 {\scriptstyle h_\rho}\downarrow&&\downarrow{\scriptstyle h_\rho}\\
 J_{r\rho}&\xrightarrow{V_{a,r\rho}}&J_{r\rho}.
\end{array}
 \tag{OZR6.7}
\]

Its vertical maps are conjugate-linear unital algebra isomorphisms; its horizontal maps are the stated multiplication operators. No change to the recovered integer \(a\) occurs in the diagram.

## OZR7. The reflection-invariant defect on actual zeros

For \(\rho\in Z\), write \(x_a(\rho)=|a^\rho|^2>0\) and define

\[
 \Delta_a(\rho)=|a^\rho|^2+
        \frac{a^2}{|a^\rho|^2}-2a.
 \tag{OZR7.1}
\]

The individual summands, the factor \(a^2\), and the term \(-2a\) remain present. Expanding a square gives the additional exact identity

\[
 \Delta_a(\rho)=\frac{(|a^\rho|^2-a)^2}{|a^\rho|^2}\geq0.
 \tag{OZR7.2}
\]

By (OZR6.2),

\[
 x_a(r\rho)=\frac{a^2}{x_a(\rho)}.
 \tag{OZR7.3}
\]

Substitution into the full formula proves

\[
 \Delta_a(r\rho)=\frac{a^2}{x_a(\rho)}
          +\frac{a^2}{a^2/x_a(\rho)}-2a
        =\Delta_a(\rho).
 \tag{OZR7.4}
\]

Finally, writing \(\rho=\beta+i\gamma\), the original exponential gives
\(x_a(\rho)=\exp(2\beta\log a)\). Since \(\log a>0\),

\[
 \Delta_a(\rho)=0
 \ \Longleftrightarrow\ x_a(\rho)=a
 \ \Longleftrightarrow\ \operatorname{Re}\rho=\frac12
 \ \Longleftrightarrow\ r\rho=\rho.
 \tag{OZR7.5}
\]

This is an exact test on each actual zero. It proves neither that any actual zero has positive defect nor that all actual zeros have zero defect.

## OZR8. Exact descent retains the defect and the zero algebras

Let \(Q=Z/\langle r\rangle\) be the set of reflection orbits, with quotient map \(q:Z\to Q\). Each orbit consists of either one actual zero or two actual zeros, and multiplicity is constant on the orbit by OZR5. Define

\[
 \overline\Delta_a(q(\rho))=\Delta_a(\rho),\qquad
 \overline m(q(\rho))=m_\rho.
 \tag{OZR8.1}
\]

Equations (OZR7.4) and (OZR5.8) prove that both definitions are independent of the representative. Since \(q\) is onto, these are the unique functions satisfying

\[
 \Delta_a=\overline\Delta_a\circ q,
 \qquad m=\overline m\circ q.
 \tag{OZR8.2}
\]

In particular the quotient does not make the defect zero: it retains its exact value. Explicitly,

\[
 \{\overline\Delta_a=0\}
   =q\bigl(\{\rho\in Z:r\rho=\rho\}\bigr).
 \tag{OZR8.3}
\]

The reverse inclusion and forward inclusion both follow from (OZR7.5), applied to any representative. Equation (OZR8.3) concerns the actual zero set; it asserts no existence of an orbit outside this locus.

There is also a descent algebra retaining the full jet data. For each actual orbit \(O\in Q\), put

\[
 R_O=\prod_{\rho\in O}J_\rho,
 \qquad (\iota f)_\rho=h_{r\rho}(f_{r\rho}),
 \qquad B_O=R_O^{\iota}.
 \tag{OZR8.4}
\]

This finite product and its fixed subalgebra are algebra constructions on zero jets. They are not addition of the user's branch counters. The map \(\iota\) is a unital involution of real algebras, because the component maps in (OZR5.6) are unital, multiplicative, and mutually inverse. Thus \(B_O\) is well defined.

For an orbit with two distinct representatives \(\rho,r\rho\), projection onto the first component gives a real-algebra isomorphism

\[
 B_O\xrightarrow{\ \sim\ }J_\rho,
 \qquad f\longmapsto f_\rho,
 \qquad g\longmapsto(g,h_\rho g)
 \tag{OZR8.5}
\]

as inverse. The formula proves injectivity and surjectivity and preserves addition, multiplication, and the unit. Choosing the other representative changes this presentation by the exact map \(h_\rho\), not by an identification of recovered counters.

For a one-point orbit \(O=\{\rho\}\), the original coordinate \(z=s-\rho\) obeys \(h_\rho z=-z\). Therefore a class \(\sum_{j=0}^{m_\rho-1}c_jz^j\) is fixed exactly when

\[
 c_j=(-1)^j\overline{c_j}\quad(0\leq j<m_\rho).
 \tag{OZR8.6}
\]

Every even coefficient is real, and every odd coefficient is purely imaginary. Equivalently the map

\[
 \mathbb R[u]/(u^{m_\rho})\longrightarrow B_O,
 \qquad u\longmapsto i(s-\rho)
 \tag{OZR8.7}
\]

is a real-algebra isomorphism: \(h_\rho(iz)=iz\), and each coefficient satisfying (OZR8.6) has a unique expression \(c_j=b_ji^j\) with \(b_j\in\mathbb R\). The original coordinate and the exact change of coordinate are both displayed. Nilpotent orders and all \(m_\rho\) coefficients remain recorded in either case.

The defect enters this descended algebra as the real scalar

\[
 \overline\Delta_a(O)\,1_{B_O}.
 \tag{OZR8.8}
\]

Its component in every original zero algebra is exactly \(\Delta_a(\rho)\,1_{J_\rho}\). The unit of each \(J_\rho\) is nonzero because \(\zeta\) lies in its maximal ideal, so the original ideal is proper. Consequently the scalar in (OZR8.8) is zero exactly when its real coefficient is zero. This proves retention in the algebra, not only in the quotient's underlying set.

Recovery of the entire complex jet algebra from the descended real algebra is also explicit. The map

\[
 \Phi_O:B_O\otimes_{\mathbb R}\mathbb C\longrightarrow R_O,
 \qquad b\otimes\lambda\longmapsto\lambda b
 \tag{OZR8.9}
\]

is a complex-algebra isomorphism. For \(x\in R_O\), put

\[
 b(x)=\frac{x+\iota x}{2},\qquad
 c(x)=\frac{x-\iota x}{2i}.
 \tag{OZR8.10}
\]

Conjugate-linearity and \(\iota^2=1\) give \(\iota b(x)=b(x)\) and \(\iota c(x)=c(x)\), so both belong to \(B_O\). Direct substitution gives \(x=b(x)+ic(x)\). Conversely every tensor is uniquely of the form \(b\otimes1+c\otimes i\) with \(b,c\in B_O\); when \(b+ic=0\), applying \(\iota\) also gives \(b-ic=0\), hence \(b=c=0\). Thus the inverse of (OZR8.9) is

\[
 x\longmapsto b(x)\otimes1+c(x)\otimes i.
 \tag{OZR8.11}
\]

The forward map preserves multiplication and the unit by its formula, so its proved inverse is an algebra inverse. This recovers every component and all its nilpotents, with the original label set supplied by the same orbit \(O\) in (OZR8.4).

Both cases in (OZR8.5)–(OZR8.7) describe actual orbits whenever those orbits occur; the two-point calculation does not claim that the actual zero set contains such an orbit. Every branch counter remains the already reconstructed counter stipulated in OZR0.

## OZR9. The calculated relation to the proposed argument

The same original zeta function has the exact weighted reflection (OZR1.5). Its original zero ideals have the unital conjugate-linear comparison (OZR5.6), with every multiplicity and every derivative contribution retained. Recovered arithmetic character operators have the full comparison (OZR6.6). The resulting reflection quotient exists as the explicitly constructed set and real algebras in OZR8, and retains the invariant defect (OZR8.8).

For these exact objects, the statement that \(\overline\Delta_a\) vanishes on every actual reflection orbit is equivalent, by (OZR7.5) and surjectivity of \(q\), to every zero in \(S\) having real part \(1/2\). The calculation does not establish that vanishing. Existence of this quotient establishes descent of the observed defect; it is not itself a vanishing calculation.

This is a proved part of the requested study of deviations preserving the original zeta function. It leaves the user's broader class of admissible constructions and its specified counter quotients intact. It supplies exact maps and a retained observable for that study, without substituting a timing example, changing the arithmetic, assuming RH, claiming an actual off-critical zero, or transferring a Deligne theorem without its hypotheses and receiving map.

In particular this file does not assert that reflection is an automorphism of a stronger marked arithmetic structure in which every individual operator \(F_{a,\rho}\) must be fixed. The proved formula is the exact interchange with \(V_{a,r\rho}\) in (OZR6.6). Any comparison with such a stronger structure must retain that formula, the weighted behavior of \(T\), and the unital behavior of \(H\) together.
