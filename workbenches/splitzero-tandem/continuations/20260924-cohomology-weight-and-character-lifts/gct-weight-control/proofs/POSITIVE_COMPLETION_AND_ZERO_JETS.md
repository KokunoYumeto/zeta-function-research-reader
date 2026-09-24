# The positive geometric completion and the original-zeta zero jets

24 September 2026. Independent derivation PCJ0–PCJ9, followed by the root derivation PCJ10 connecting the original-zeta residue trace. Proof locators PCJ0–PCJ10.

This note computes the exact operator-norm completion of the integral adjoint algebra in its specified faithful degree-zero geometric representation. It classifies its continuous characters and calculates exactly what happens to every finite original-zeta jet under that norm. It neither constructs an unknown intertwiner nor assumes that the original-zeta receiving space inherits the geometric norm.

The supporting datum remains \(\tau\langle Z_1;\text{no intrinsic }Z_2\rangle\). All norms, coordinates, sums and products below belong to the displayed geometric Hilbert space, coefficient algebra, torus, or zero-jet algebra. None is assigned to tau.

## PCJ0. Sources and the retained degree-zero metric

Read `work/tau_weight_cohomology_20260924/INTEGRAL_FROBENIUS_TRANSFER_ALGEBRA.md`, FT8–FT10, in full. The integral coefficient algebra and its original-zeta action are the already proved IAR0–IAR9 and AT5; the local trace and jet comparisons are JTR0–JTR8. No assertion from a pending intertwiner argument is used.

Fix the source reference prime \(p_0\) and retain both original periods

\[
A=\log p_0>0,\qquad B=2\pi>0.
\tag{PCJ0.1}
\]

The degree-zero Hilbert receiver is exactly

\[
\mathcal H_{\mathrm{geom}}^0
=\left\{\sum_{r\in\mathbb Q_{>0}}a_r e_r:
AB\sum_r r|a_r|^2<\infty\right\},
\qquad
\|a\|^2=AB\sum_r r|a_r|^2.
\tag{PCJ0.2}
\]

The source geometric operators satisfy, for every positive integer \(n\),

\[
\mathfrak F_n e_r=e_{nr},\qquad
\mathfrak V_n e_r=n e_{r/n},
\qquad
\mathfrak F_n^\dagger=\mathfrak V_n,
\qquad
\mathfrak F_n\mathfrak V_n=nI.
\tag{PCJ0.3}
\]

The label \(r\) here is the scale index, not the reference prime. The reference area \(AB\) and the scale weight \(r\) both remain in the norm.

Retain the integral algebra

\[
\mathcal H_{\mathbb Z}
=\mathbb Z[b_n,n b_{1/n}:n\ge1]
\subseteq\mathbb Q[\mathbb Q_{>0}^{\times}],
\]

\[
C_{a/b}=b b_{a/b}\quad(\gcd(a,b)=1),\qquad
F_p=b_p,\quad V_p=p b_{1/p},\quad F_pV_p=p.
\tag{PCJ0.4}
\]

Its complex scalar extension

\[
\mathcal A=\mathbb C\otimes_{\mathbb Z}\mathcal H_{\mathbb Z}
\cong\mathbb C[\mathbb Q_{>0}^{\times}]
\tag{PCJ0.5}
\]

retains every rational group index. The involution conjugates complex coefficients and obeys \(b_r^*=r b_{1/r}\), equivalently \(C_r^*=C_{1/r}\). The equality in (PCJ0.5) is the scalar-extension isomorphism, not a replacement of the original integral ring or its special fibres.

## PCJ1. Exact Fourier map with both source periods retained

Let

\[
\mathbb T=\prod_{p\text{ prime}}S^1,
\qquad
dm=\prod_{p\text{ prime}}\frac{d\theta_p}{2\pi},
\qquad z_p=e^{i\theta_p}.
\tag{PCJ1.1}
\]

The measure is the product of the displayed circle measures of mass one. Their finite cylinder measures are consistent and define the product Borel probability measure. The countable product is a compact metrizable space. A compatible metric is obtained by enumerating the primes and summing \(2^{-j}|z_{p_j}-w_{p_j}|\); compactness follows from the coordinatewise diagonal subsequence argument. Every nonempty basic open cylinder has positive measure, because each of its finitely many arc factors has positive measure. Thus \(m\) has full support.

For a positive rational \(r\), let \(v_p(r)\in\mathbb Z\) be its prime valuations and set

\[
z^{v(r)}=\prod_p z_p^{v_p(r)}.
\tag{PCJ1.2}
\]

Only finitely many exponents are nonzero. Unique prime factorization identifies the index group with \(\bigoplus_p\mathbb Z\). Integrating each circle factor proves

\[
\int_{\mathbb T}\overline{z^{v(r)}}z^{v(s)}\,dm
=\begin{cases}1,&r=s,\\0,&r\ne s.\end{cases}
\tag{PCJ1.3}
\]

These characters are a complete orthonormal family in \(L^2(\mathbb T,m)\). Here is a density justification. A continuous function on the compact product is uniformly continuous. Freezing all coordinates after the first \(N\) at one changes the compatible metric by a quantity tending uniformly to zero. Thus continuous cylinder functions uniformly approximate every continuous function. On each finite torus, products of the circle Fejér kernels approximate continuous functions uniformly: the kernels are nonnegative trigonometric polynomials of integral one; their mass outside any fixed neighbourhood of the identity tends to zero, by the formula

\[
K_N(\theta)=\frac1N\left|\sum_{j=0}^{N-1}e^{ij\theta}\right|^2
=\frac1N\frac{\sin^2(N\theta/2)}{\sin^2(\theta/2)}.
\]

The second formula bounds the mass away from zero by a constant times \(N^{-1}\); splitting the convolution into a small neighbourhood and its complement proves the approximation by uniform continuity. The product kernel gives the finite-torus assertion, with its exceptional tails bounded by the union of the coordinate tails. Therefore finite trigonometric polynomials are uniformly dense in \(C(\mathbb T)\). Continuous functions are dense in \(L^2\) for this finite Borel measure on a compact metric space: regular approximation of Borel indicators by closed and open sets, followed by continuous distance cutoffs, proves this for indicators, and simple functions then prove it for all \(L^2\) functions. This establishes the asserted completeness.

Define on finite-support vectors

\[
\boxed{
Ue_r=\sqrt{ABr}\,z^{v(r)}.}
\tag{PCJ1.4}
\]

Orthogonality gives the full equality

\[
\left\|U\left(\sum_r a_re_r\right)\right\|_{L^2(m)}^2
=AB\sum_r r|a_r|^2.
\tag{PCJ1.5}
\]

It follows by completion and character completeness that \(U\) is a unitary map from (PCJ0.2) onto \(L^2(\mathbb T,m)\). The factors \(A=\log p_0\), \(B=2\pi\), and every scale weight \(r\) appear explicitly in this map; no source area has been set to one.

## PCJ2. Original generators and the norm of every finite algebra element

Extend the geometric action to \(\mathcal A\). For a positive rational \(r=a/b\), the element \(b_r\) acts by the shift
\(S_r e_q=e_{rq}\). This follows from \(b_r=b_a b_b^{-1}\), with the bounded inverse on the complex Hilbert space from FT10. The integral generator remains \(C_r=b b_r\); its action is \(bS_r\), not the bare inverse declared integral.

Computing on every basis vector gives

\[
US_rU^{-1}=M_{\sqrt r\,z^{v(r)}},
\tag{PCJ2.1}
\]

where \(M_f\) denotes multiplication by \(f\) on \(L^2(\mathbb T,m)\). Indeed \(Ue_{rq}=\sqrt{ABrq}\,z^{v(r)+v(q)}\), which is \(\sqrt r\,z^{v(r)}Ue_q\). In particular,

\[
\boxed{
U\mathfrak F_pU^{-1}=M_{\sqrt p\,z_p},\qquad
U\mathfrak V_pU^{-1}=M_{\sqrt p\,z_p^{-1}},}
\tag{PCJ2.2}
\]

\[
\boxed{U\Psi_{\mathrm{geom}}(C_{a/b})U^{-1}
=M_{b\sqrt{a/b}\,z^{v(a/b)}}
=M_{\sqrt{ab}\,z^{v(a/b)}}.}
\tag{PCJ2.3}
\]

The degree factors \(p\) and denominator factors \(b\) have not been dropped: (PCJ2.2) follows from \(p\sqrt{1/p}=\sqrt p\), and (PCJ2.3) displays both forms of its exact coefficient.

For any finite element \(D=\sum_r c_rC_r\in\mathcal A\), define its retained Fourier polynomial

\[
f_D(z)=\sum_r c_r\operatorname{den}(r)\sqrt r\,z^{v(r)}.
\tag{PCJ2.4}
\]

Then the exact operator norm is

\[
\boxed{\|\Psi_{\mathrm{geom}}(D)\|
=\max_{z\in\mathbb T}|f_D(z)|.}
\tag{PCJ2.5}
\]

For the proof, multiplication has norm at most that maximum. If the maximum is \(M>0\), continuity gives a nonempty open set on which \(|f_D|>M-\varepsilon\). It has positive measure by full support; its indicator, divided by the square root of its measure, is an \(L^2\) unit vector on which the multiplication norm is at least \(M-\varepsilon\). Letting \(\varepsilon\) decrease to zero proves equality. The case \(M=0\) is immediate. Thus a supremum over the torus is the operator norm, not merely a spectral bound.

The representation is faithful. If \(f_D=0\), multiply by each conjugate character and integrate using (PCJ1.3). The result is \(c_r\operatorname{den}(r)\sqrt r=0\) for every \(r\), forcing all coefficients to vanish. The involution corresponds exactly to complex conjugation of \(f_D\), because \(C_r^*=C_{1/r}\) and their coefficients \(\operatorname{den}(r)\sqrt r\) agree after inversion.

## PCJ3. The complete operator algebra and all its characters

The Fourier image of \(\mathcal A\) is precisely the finite trigonometric polynomial algebra: every character \(z^{v(r)}\) is the image of \((\operatorname{den}(r)\sqrt r)^{-1}C_r\), and every finite image is such a polynomial. The density proof in PCJ1 and the exact norm identity therefore give

\[
\boxed{\overline{\Psi_{\mathrm{geom}}(\mathcal A)}^{\|\cdot\|}
\cong C(\mathbb T),}
\tag{PCJ3.1}
\]

acting faithfully by multiplication on \(L^2(\mathbb T,m)\). Its unit is the constant function one and its involution is pointwise conjugation. The area factor disappears from operator-norm ratios only through the explicit unitary calculation (PCJ1.4)–(PCJ2.5); it remains in the source norm and the source-to-target map.

Every continuous nonzero complex character of this completed algebra is evaluation at a unique point of \(\mathbb T\). To prove the classification, let \(\chi:C(\mathbb T)\to\mathbb C\) be such a character. Nonzeroness gives \(\chi(1)=1\). For any \(f\), the value \(\chi(f)\) belongs to \(f(\mathbb T)\): otherwise \(f-\chi(f)\) has a continuous reciprocal, contradicting that its character value is zero. In particular \(|\chi(f)|\le\|f\|_\infty\). The coordinate function \(z_p\) and its inverse therefore satisfy

\[
|\chi(z_p)|\le1,\quad |\chi(z_p^{-1})|\le1,
\quad \chi(z_p)\chi(z_p^{-1})=1,
\]

so \(\lambda_p:=\chi(z_p)\) has modulus one. The point \(\lambda=(\lambda_p)_p\) lies in \(\mathbb T\). Multiplicativity proves that \(\chi\) is evaluation at \(\lambda\) on every trigonometric polynomial; continuity and density prove the same on every continuous function. Conversely every evaluation is a continuous character of norm one. Distinct points differ in a coordinate function, so the point is unique.

## PCJ4. The exact continuity criterion for original-zeta scalar characters

For any complex \(\rho\), the original arithmetic scalar character on the algebraic receiver is

\[
\chi_\rho(b_r)=r^\rho,
\qquad
\chi_\rho(C_{a/b})=b(a/b)^\rho.
\tag{PCJ4.1}
\]

This is an algebraic character for every \(\rho\), since the real logarithm of positive rational numbers respects products. No continuity is part of its algebraic definition.

**Theorem.** The character (PCJ4.1) extends continuously to the geometric operator-norm completion if and only if \(\Re\rho=1/2\).

**Proof.** Under the completion isomorphism, \(F_p\) is \(\sqrt p\,z_p\). Any continuous extension must therefore be evaluation at a point with

\[
z_p=\frac{p^\rho}{\sqrt p}=p^{\rho-1/2}.
\tag{PCJ4.2}
\]

Such a point has every coordinate of modulus one if and only if \(\Re\rho=1/2\), already forced by any one prime. Conversely if \(\rho=1/2+i\gamma\), define

\[
z_\rho=(e^{i\gamma\log p})_p\in\mathbb T.
\]

Its evaluation on the Fourier polynomial of \(C_{a/b}\) is exactly

\[
b\sqrt{a/b}\prod_p e^{i\gamma\log p\,v_p(a/b)}
=b(a/b)^{1/2+i\gamma}.
\]

Thus evaluation extends (PCJ4.1), with all prime phases and the original denominator coefficient retained. \(\square\)

Here are explicit discontinuity witnesses using both adjoint partners. Fix a prime \(p\) and let \(k\) tend through the positive integers. The algebra elements

\[
A_k=p^{-k/2}F_p^k,
\qquad B_k=p^{-k/2}V_p^k
\tag{PCJ4.3}
\]

each have geometric operator norm one, by their Fourier images \(z_p^k\) and \(z_p^{-k}\). They are scalar multiples in the complexified algebra of the original operators; no integral generator is changed. Their character values are

\[
\chi_\rho(A_k)=p^{k(\rho-1/2)},
\qquad
\chi_\rho(B_k)=p^{k(1/2-\rho)}.
\tag{PCJ4.4}
\]

If \(\Re\rho>1/2\), the first absolute value tends to infinity. If \(\Re\rho<1/2\), the second does. Equivalently,

\[
p^{-k\rho}F_p^k\longrightarrow0
\quad\text{in geometric norm when }\Re\rho>1/2,
\]

\[
p^{-k(1-\rho)}V_p^k\longrightarrow0
\quad\text{in geometric norm when }\Re\rho<1/2,
\tag{PCJ4.5}
\]

while their corresponding character values remain exactly one. These sequences prove failure of continuity directly, including the complete degree factor in the inverse partner.

The criterion applies to every actual original-zeta zero as a specified character. It does not establish that those characters are continuous in this particular geometric norm.

## PCJ5. Full finite jets and polynomial growth on the critical line

For a complex parameter \(\rho\) and positive integer \(m\), retain the full local algebra

\[
J_{\rho,m}=\mathbb C[t]/(t^m),\qquad N:t^j\longmapsto t^{j+1}.
\tag{PCJ5.1}
\]

The original arithmetic jet representation is

\[
\pi_{\rho,m}(b_r)=r^\rho
\sum_{j=0}^{m-1}\frac{(\log r)^j}{j!}N^j.
\tag{PCJ5.2}
\]

At an actual zero, \(m\) is its full multiplicity. For each prime set \(q_p=\log p>0\). In particular

\[
\pi_{\rho,m}(F_p)=p^\rho e^{q_pN},
\quad
\pi_{\rho,m}(V_p)=p^{1-\rho}e^{-q_pN},
\tag{PCJ5.3}
\]

where the exponentials are finite Taylor polynomials and their product is \(pI\). Every nilpotent coefficient remains.

The local jet map from \(\mathcal A\) onto \(J_{\rho,m}\), represented on itself by multiplication, is surjective. Indeed \(p^{-\rho}\pi(F_p)-I=e^{q_pN}-I\) has zero constant term, and its truncated formal logarithm gives

\[
N=\frac1{q_p}\sum_{j=1}^{m-1}\frac{(-1)^{j+1}}j
\bigl(p^{-\rho}\pi(F_p)-I\bigr)^j.
\tag{PCJ5.4}
\]

Thus its image contains \(N\) and every polynomial in \(N\), which is the full local algebra. All divisions in (PCJ5.4) are by specified nonzero complex scalars.

**Theorem.** The full jet representation has a bounded finite-dimensional extension to \(C(\mathbb T)\) if and only if \(m=1\) and \(\Re\rho=1/2\).

**Proof.** If a bounded extension existed, its image would still lie in the finite-dimensional local image algebra: that subspace is closed and already contains the image of the dense source algebra. Composing with constant-term evaluation there would extend \(\chi_\rho\) continuously. PCJ4 therefore requires \(\Re\rho=1/2\). Now assume that equality, and put \(\rho=1/2+i\gamma\). The norm-one elements in (PCJ4.3) have jet images

\[
\pi(A_k)=e^{ik\gamma q_p}
\sum_{j=0}^{m-1}\frac{(kq_p)^j}{j!}N^j,
\]

\[
\pi(B_k)=e^{-ik\gamma q_p}
\sum_{j=0}^{m-1}\frac{(-kq_p)^j}{j!}N^j.
\tag{PCJ5.5}
\]

Give \(J_{\rho,m}\) its explicit Euclidean norm in the basis \(1,t,\ldots,t^{m-1}\). Applying either operator to the unit vector \(1\) shows

\[
\|\pi(A_k)\|,\ \|\pi(B_k)\|
\ge\frac{(kq_p)^{m-1}}{(m-1)!}.
\tag{PCJ5.6}
\]

For \(m>1\) this tends to infinity, contrary to boundedness on the geometric unit ball. Every other fixed finite-dimensional norm is equivalent to this one, so no change of target norm repairs the divergence. If \(m=1\), the jet is just the scalar character and PCJ4 supplies the extension exactly on the line. \(\square\)

The displayed growth is a proof for all iterates, not a bounded check. It occurs even when the scalar character lies on the required line. Consequently nontrivial jets cannot be silently included in a bounded Hilbert or finite-dimensional representation merely because their scalar values satisfy the modulus condition.

## PCJ6. The nilpotent ideal and all finite receiving quotients

The local nilpotent ideal and reduced quotient are

\[
\mathfrak n=(t)\subseteq J_{\rho,m},
\qquad
J_{\rho,m}\xrightarrow{\ t\mapsto0\ }\mathbb C,
\qquad\ker=\mathfrak n.
\tag{PCJ6.1}
\]

Every ideal of \(J_{\rho,m}\) is \((t^j)\) for some \(0\le j\le m\). To prove this, select a nonzero element of least nonzero Taylor order \(j\) in a nonzero ideal. It is \(t^j\) times a unit, because its remaining polynomial has nonzero constant term. Thus the ideal contains \(t^j\); every one of its other elements has order at least \(j\), giving the reverse inclusion. The zero ideal is \((t^m)\).

Therefore any nonzero unital quotient retaining a jet of length at least two has the same polynomial-growth obstruction as PCJ5. On \(\Re\rho=1/2\), the largest receiving quotient with a bounded extension is exactly the reduced scalar quotient (PCJ6.1). Off that line, no nonzero unital quotient has a bounded extension, because its scalar quotient would contradict PCJ4.

This does not claim simplicity of actual zeta zeros. The original full jet algebra and its nilpotent ideal remain the algebraic receiver (PCJ5.1)–(PCJ5.3). The result identifies the obstruction to extending that representation in this particular positive geometric norm. Passing to (PCJ6.1) is an explicit quotient with a named kernel, not an equality of the original objects.

At a critical-line parameter, the jet involution obtained from the weighted adjoint is

\[
\sum_{j=0}^{m-1}a_jt^j\longmapsto
\sum_{j=0}^{m-1}(-1)^j\bar a_jt^j.
\tag{PCJ6.2}
\]

It preserves the ideal \(\mathfrak n\), and the reduced quotient carries complex conjugation. The full indefinite or degenerate Weil adjoint identity may retain the higher jets; the positive-norm extension result above is a different, fully specified comparison.

## PCJ7. Exact closure of the jet kernel in the geometric completion

Let \(I_{\rho,m}\) be the kernel of the surjective algebra map in PCJ5, viewed as an ideal in the dense trigonometric algebra \(\mathcal A\subset C(\mathbb T)\). Then

\[
\boxed{
\overline{I_{\rho,m}}^{\|\cdot\|}
=\begin{cases}
\{f\in C(\mathbb T):f(z_\rho)=0\},&\Re\rho=1/2,\\
C(\mathbb T),&\Re\rho\ne1/2.
\end{cases}}
\tag{PCJ7.1}
\]

**Proof off the line.** For any prime \(p\), the polynomial
\(g=F_p-p^\rho b_1\) has a zero of order at least one at the parameter \(\rho\), hence \(g^m\in I_{\rho,m}\). Its torus function is \(\sqrt p\,z_p-p^\rho\). Off the line its two terms have unequal moduli, so it is nowhere zero on the compact torus and has a continuous reciprocal. The closure of an ideal in a dense algebra is an ideal of the completion: approximate each continuous multiplier uniformly by algebra elements and pass to the limit. Thus the closure containing \(g^m\) also contains \((g^m)^{-1}g^m=1\), proving it is the whole algebra.

**Proof on the line.** Every member of \(I_{\rho,m}\) vanishes at \(z_\rho\), so its closure is contained in the displayed maximal ideal. Conversely take \(f\in C(\mathbb T)\) with \(f(z_\rho)=0\) and fix \(\varepsilon>0\). The compact set
\(K_\varepsilon=\{z:|f(z)|\ge\varepsilon\}\) does not contain \(z_\rho\). If this set is empty, the zero function is already an approximant with error less than \(\varepsilon\). Otherwise, for each of its points some prime coordinate differs from that of \(z_\rho\), so for that prime the function \(g_p=F_p-p^\rho b_1\) is nonzero there. Finitely many such nonzero sets cover \(K_\varepsilon\). Every \(g_p^m\) lies in \(I_{\rho,m}\); therefore the finite sum

\[
h=\sum_{p\text{ in that cover}}|g_p^m|^2
\]

also lies in the ideal, because each conjugate factor is a trigonometric polynomial available for multiplication. The function \(h\) is nonnegative and has a strictly positive minimum \(\delta\) on \(K_\varepsilon\). For \(\eta>0\), the function
\(f h/(h+\eta)\) belongs to the closed ideal. Its uniform distance from \(f\) is at most \(\varepsilon\) outside \(K_\varepsilon\), and at most \(\|f\|_\infty\eta/\delta\) on that set. Letting \(\eta\) decrease and then \(\varepsilon\) decrease proves that \(f\) belongs to the closed ideal. This establishes the reverse inclusion. \(\square\)

This identifies the receiving quotient in the completion itself:

\[
C(\mathbb T)/\overline{I_{\rho,m}}
\cong\begin{cases}\mathbb C,&\Re\rho=1/2,\\0,&\Re\rho\ne1/2.\end{cases}
\tag{PCJ7.2}
\]

Algebraically, before completion, \(\mathcal A/I_{\rho,m}\cong J_{\rho,m}\) remains the entire jet algebra. The quotient seminorm is the infimum of the norm over representatives differing by an element of \(I_{\rho,m}\); this infimum equals the distance to its norm closure. On the line that distance is exactly \(|f(z_\rho)|\): evaluation gives the lower bound, and \(f-f(z_\rho)1\) lies in the closed maximal ideal for the upper bound. Off the line the closure is the entire completion, so the distance is zero. Thus the quotient seminorm has kernel \((t)\) on a critical-line jet and is identically zero off the line. Equations (PCJ6.1) and (PCJ7.1) give the complete connecting maps.

The coefficient algebra \(\mathcal A\) itself has no nilpotents: it is a Laurent polynomial domain on each finite prime set. Completion is faithful on \(\mathcal A\), as PCJ2 proves. The nilpotents discussed here belong to its local receiving quotients, not to an unmentioned global nilpotent ideal discarded from the source algebra.

## PCJ8. The actual original-zeta receiver and its retained information

At an actual nontrivial zero \(\rho\), take its true multiplicity \(m_\rho\). The original-zeta receiver already supplies the algebraic action (PCJ5.2), including all its nilpotent coefficients, through the full quotient and the source comparison

\[
F_0(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

This comparison retains its Gamma, pi and endpoint factors and their original zero and pole contributions; it is not a replacement of \(\zeta\) by \(F_0\). The present norm calculation does not change that comparison or its exceptional-point analysis. The ordinary trace pairing may have a radical on higher jets; their algebraic presence is unchanged by that fact.

For the scalar part, PCJ4 establishes the exact equivalence

\[
\chi_\rho\text{ is continuous in the positive geometric operator norm}
\quad\Longleftrightarrow\quad \Re\rho=\frac12.
\tag{PCJ8.1}
\]

For the complete finite block, PCJ5 establishes

\[
\pi_{\rho,m_\rho}\text{ has a bounded finite-dimensional extension}
\quad\Longleftrightarrow\quad
\Re\rho=\frac12\ \text{and}\ m_\rho=1.
\tag{PCJ8.2}
\]

These are proved comparisons of two specified topologies and receiving maps. Equation (PCJ8.2) is stronger than the scalar condition and must not be substituted for RH: it includes simplicity. In particular RH, by itself, would not justify a bounded extension of a nontrivial full jet. The scalar quotient and every higher jet remain explicitly distinguished by their quotient map.

The original full period-weighted Hilbert representation has no nonzero point eigenvectors for \(\mathfrak F_n\), as FT10 proves. Its continuous characters are instead evaluations on its operator algebra, which act on one-dimensional receiving quotients. Nothing here inserts such characters as eigenvectors of that Hilbert space. This keeps the state-space and operator-algebra comparisons exact.

## PCJ9. Result and limits

The completed geometric operator algebra is exactly \(C(\prod_pS^1)\), reached by the Fourier map with coefficient \(\sqrt{ABr}\). The original generators remain \(\sqrt p\,z_p\) and \(\sqrt p\,z_p^{-1}\), and the integral rational-label basis remains \(\sqrt{ab}\,z^{v(a/b)}\). Their norm is the full torus supremum.

Every scalar original-zeta character has an exact continuity test and explicit off-line discontinuity sequences. Every finite higher jet has an exact polynomial-growth obstruction, even on the line, together with its nilpotent ideal, reduced quotient, and completed kernel. Thus the whole algebraic zero record is retained while the positive-norm receiving object is determined precisely.

No map assigning the geometric norm to the original-zeta quotient has been assumed or constructed in this calculation. In particular it has not proved continuity of the actual zero characters, positivity of the complete original Weil form, simplicity of zeros, or RH. It supplies the exact norm and exact receiving criterion for any further comparison, with the original periods, degree factors, phases, and multiplicities intact.

## PCJ10. The original-zeta residue trace retains multiplicity without a bounded higher-jet action

This section computes the trace of the entire jet before taking any quotient. For every positive integer \(m\), every complex \(\rho\), and every finite element \(a=\sum_r c_r b_r\in\mathcal A\), put

\[
h_a(s)=\sum_r c_r r^s,\qquad
\mathcal T_{\rho,m}(a)=\operatorname{Tr}_{J_{\rho,m}}\pi_{\rho,m}(a),
\qquad J_{\rho,m}=\mathbb C[t]/(t^m).
\tag{PCJ10.1}
\]

The function \(h_a\) is entire; powers use the real logarithm of the positive rational \(r\). The representation in PCJ5 acts by multiplication by \(h_a(\rho+t)\bmod t^m\). On the ordered basis \(1,t,\ldots,t^{m-1}\), multiplication by any positive power of \(t\) has zero diagonal. The constant coefficient occurs on all \(m\) diagonal entries. Thus the exact trace of this full operator, with every higher coefficient still in the matrix, is

\[
\boxed{\displaystyle
\mathcal T_{\rho,m}(a)=m h_a(\rho)=m\chi_\rho(a).}
\tag{PCJ10.2}
\]

This is a trace identity on the original \(m\)-dimensional algebra, not an identification of that algebra with a one-dimensional space. Its factor \(m\) records the full length of the original block.

For an actual nontrivial zero \(\rho\) of the original \(\zeta\), use its actual multiplicity \(m=m_\rho\). Choose a disc containing no other zero and no pole, and write the exact local factorization

\[
\zeta(s)=(s-\rho)^m u_\rho(s),\qquad u_\rho(\rho)\ne0,
\qquad
\frac{\zeta'(s)}{\zeta(s)}=
\frac{m}{s-\rho}+\frac{u_\rho'(s)}{u_\rho(s)}.
\tag{PCJ10.3}
\]

Shrinking the disc makes \(u_\rho\) nonzero throughout it. Expanding the holomorphic functions in powers of \(s-\rho\), the coefficient of \((s-\rho)^{-1}\) in \(h_a(s)\zeta'(s)/\zeta(s)\) is exactly \(m h_a(\rho)\). Termwise integration on any circle inside that disc consequently gives

\[
\boxed{\displaystyle
\frac{1}{2\pi i}\oint_{|s-\rho|=\epsilon}
h_a(s)\frac{\zeta'(s)}{\zeta(s)}\,ds
=m h_a(\rho)=\mathcal T_{\rho,m}(a).}
\tag{PCJ10.4}
\]

The contour is positively oriented. This formula uses the original zeta function. It is a local residue calculation; it does not replace a contour enclosing other zeros, the pole at one, or the contributions of a completed function. Those contributions remain in the complete explicit formula of PRI7.

The trace functional in (PCJ10.2) has a bounded extension to the exact positive completion \(C(\mathbb T)\) precisely when \(\Re\rho=1/2\). Indeed division by the nonzero integer \(m\) reduces boundedness exactly to PCJ4. On the line its unique extension, its norm, and its positive-square values are

\[
\mathcal T_{\rho,m}(f)=m f(z_\rho),\qquad
\|\mathcal T_{\rho,m}\|=m,\qquad
\mathcal T_{\rho,m}(f^*f)=m|f(z_\rho)|^2\ge0.
\tag{PCJ10.5}
\]

The upper norm bound follows from evaluation, and the constant function one attains it. Density gives uniqueness. This holds for every \(m\), including every \(m>1\); it imposes no simplicity requirement. It differs from the boundedness of the full operator representation in PCJ5, whose nilpotent coefficients have the displayed polynomial growth.

For completeness, positivity itself has an exact global test on the original coefficient algebra. Write \(\rho=\sigma+i\gamma\), choose any prime \(p\), and define the particular test element

\[
a_{p,\rho}=F_p-\sqrt p\,e^{i\gamma\log p}b_1,
\qquad
a_{p,\rho}^*=V_p-\sqrt p\,e^{-i\gamma\log p}b_1.
\tag{PCJ10.6}
\]

This is an element and its adjoint in \(\mathcal A\); the original generators remain \(F_p,V_p\), with \(F_pV_p=p\). The phase and the positive square root are explicit coefficients of this test, not changed definitions of the generators. Evaluating both factors and multiplying gives

\[
\begin{aligned}
\chi_\rho(a_{p,\rho})
&=e^{i\gamma\log p}(p^\sigma-\sqrt p),\\
\chi_\rho(a_{p,\rho}^*)
&=e^{-i\gamma\log p}(p^{1-\sigma}-\sqrt p),\\
\boxed{\displaystyle
\mathcal T_{\rho,m}(a_{p,\rho}^*a_{p,\rho})
=m(p^{1-\sigma}-\sqrt p)(p^\sigma-\sqrt p).}
\end{aligned}
\tag{PCJ10.7}
\]

When \(\sigma\ne1/2\), the two real factors have opposite signs because the function \(x\mapsto p^x\) is strictly increasing and \(\sigma,1-\sigma\) lie on opposite sides of \(1/2\). The value in (PCJ10.7) is therefore strictly negative. At \(\sigma=1/2\), all positive squares have nonnegative trace by (PCJ10.5). Thus for every parameter and every multiplicity the trace is positive exactly on the critical line, with an explicit negative square at every off-line parameter. No finite range of parameters was used.

Finally, the information which the trace cannot detect is also explicit. On a critical-line jet use the already proved involution
\(x(t)^*=\sum_j(-1)^j\bar x_jt^j\). The full trace pairing on that algebra is

\[
\operatorname{Tr}_{J_{\rho,m}} M_{x^*y}
=m\bar x_0y_0,
\qquad
\operatorname{rad}\bigl((x,y)\mapsto\operatorname{Tr}M_{x^*y}\bigr)=(t).
\tag{PCJ10.8}
\]

The displayed equality follows from the same diagonal calculation. Every element of \((t)\) pairs to zero with everything, and any \(x_0\ne0\) pairs nontrivially with \(y=1\), proving the stated radical. The exact map is the constant-coefficient quotient \(J_{\rho,m}\twoheadrightarrow\mathbb C\), while \(m\) remains the trace of the identity and the whole original jet is retained separately. The labelled-zero correction in ZR continues to apply: none of these scalar trace maps replaces a support record.

This supplies a multiplicity-preserving trace comparison to the positive completion without requiring a bounded representation on higher jets. It does not establish positivity of the complete Weil sum: (PCJ10.7) is a residue-block calculation, and the other zero blocks and all explicit-formula terms still require their actual receiving maps. No continuity or positivity of the actual original-zeta trace was inserted as an assumption.
