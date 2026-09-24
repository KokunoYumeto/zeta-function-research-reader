# Independent mathematical check of the global polynomial dual defect

24 September 2026. PGC0–PGC7. The complete manuscript [GLOBAL_POLYNOMIAL_DUAL_DEFECT.md](GLOBAL_POLYNOMIAL_DUAL_DEFECT.md), PGD0–PGD7, was read and checked. The checked file has SHA256 ec1ea5fe1dbd49e91f2a24e19b5ad7232a67a10f45c193e70b8897f2331a41e8. No mathematical correction was required.

## PGC0. Scope, source and prerequisites

This is an independent verification of the new multiplier quotient, nonzero polynomial class, corrected rational representatives and complete real orbit. It uses the already checked original quotient and residue construction GZR, the continuous-dual comparison ASD, and the division theorem SCL. It does not claim a new complete reading of every human source in those dependencies.

The source remains \(Z_0\), \(Z_1/\tau\), and the supplied \(Z_2\) integer data under B1–B5 and their retained retractions. The arithmetic constant function \(1\) used by PGD is not primitive \(\tau\). All additive and rational operations in this verification occur in the explicitly constructed receiving algebras after the retained global arithmetic reconstruction.

Human provenance remains Connes–Consani's coefficient geometry, Meyer's analytic framework, Hadamard's complete factorization and Deligne's weight-separated lifting argument, with the exact source identities and prior reading coverage recorded in PGD0, GZR0 and ASD0. This check verifies PGD's receiving construction; it establishes neither geometric purity nor an RH counterexample.

## PGC1. The larger multiplier domain and the actual continuous dual

For fixed \(H\in\mathcal M\), the bound
\[
 |H(\sigma+it)|\le C_A(1+|t|)^{d_A}
\]
gives
\(b_{A,N}(HF)\le C_A b_{A,N+d_A}(F)\).
Therefore \(\mathcal B\) is an ideal in the multiplier algebra \(\mathcal M\), not merely a subset. The full-jet vanishing subspace \(\mathcal J\) is also an ideal: multiplication by an entire germ preserves its prescribed vanishing order.

The contour formula
\[
 \lambda_H([F])=\frac1{2\pi i}
 \left(\int_{\Re s=2}^{\uparrow}
       -\int_{\Re s=-1}^{\uparrow}\right)
 \frac{H(s)F(1-s)}{\zeta(s)}\,ds
\]
uses the unchanged original denominator and both upward orientations. On those edges \(1-s\) has real part \(-1\) or \(2\), so the exact input seminorm \(b_{2,d+2}(F)\) controls the reflected numerator. The integral of \((1+|t|)^{-2}\) is \(2\); multiplying by \(1/(2\pi)\) on each edge gives precisely PGD1.5's constant
\(C\zeta(2)(1+4\pi^2)/\pi\).

For \(F\in I\), the entire numerator \(H(s)F(1-s)\) belongs to \(\mathcal B\) and has every original zero jet required by \(I\). The established rapid-division theorem therefore applies to that actual numerator. It makes the quotient by \(\zeta\) holomorphic and rapidly decreasing on the stated closed strip; the horizontal edges vanish. This proves descent to the original \(Q\) and continuity through its quotient seminorm, rather than asserting an algebraic functional belongs to the continuous dual.

## PGC2. The exact multiplier kernel and the quotient injection

Testing \(\lambda_H\) on the actual isolator \(E_{a,j}\), with \(b=1-a\), \(m=m_a\), yields
\[
 \lambda_H([E_{a,j}])
 =(-1)^j[t^{m-1-j}]\frac{H(b+t)}{u_b(t)}.
\]
The finite-pole contour argument remains valid with this first operand: its whole numerator \(H(s)E_{a,j}(1-s)\) lies in \(\mathcal B\). Multiplication by \((s-b)^m\) removes the sole possible pole and puts the numerator in \(I\); the same rapid-division estimate justifies the contour limit. This avoids applying a two-\(\mathcal B\)-operand theorem without checking its actual numerator.

Since \(u_b(0)\ne0\), vanishing of the displayed values for all \(0\le j<m\) is equivalent to the full \(m\)-jet of \(H\) at \(b\) vanishing. Reflection permutes the actual zeros. Conversely \(H\in\mathcal J\) makes every tested product belong to \(I\), so the complete kernel is exactly \(\mathcal J\).

It follows without a closure or dual-surjectivity assumption that
\[
 \lambda_H\in\mathcal D_LQ
 \ \Longleftrightarrow\
 \exists F\in\mathcal B:\lambda_H=\lambda_F
 \ \Longleftrightarrow\
 H-F\in\mathcal J
 \ \Longleftrightarrow\
 H\in\mathcal B+\mathcal J.
\]
This proves the stated injection
\[
 \mathcal M/(\mathcal B+\mathcal J)
 \hookrightarrow(\chi\otimes Q')/\mathcal D_LQ.
\]
The upper row in PGD3.2 is exact because
\(\mathcal B\cap\mathcal J=I\). The lower row is the specified actual image quotient. The diagram is an exact diagram of receiving vector spaces and equivariant maps; no multiplication on the whole dual is claimed.

## PGC3. The Gamma-integral proof of infinitely many zeros

The finite-zero alternative in the retained full Hadamard product gives
\(\log|F_*(\sigma)|\le O(\sigma)+O(\log\sigma)\) on positive real \(\sigma\), with the complete constants explicitly retained in PGD4.2.

For \(x\ge2\) and \(v\in[x,x+1]\), both
\(v^{x-1}\ge x^{x-1}\) and \(e^{-v}\ge e^{-x-1}\).
Thus Euler's Gamma integral gives exactly
\[
 \Gamma(x)\ge x^{x-1}e^{-x-1}.
\]
Together with the original \(\zeta(\sigma)\ge1\), this proves PGD4.3 with every factor of
\[
 F_*(\sigma)=
 \frac{\sigma(\sigma-1)}8\pi^{-\sigma/2}
 \Gamma(\sigma/2)\zeta(\sigma)
\]
present. After division by \(\sigma\log\sigma\), the upper bound under the finite-zero assumption tends to \(0\), whereas the lower bound tends to \(1/2\). This is a contradiction.

An infinite zero set in the bounded critical strip has unbounded imaginary parts because a nonzero entire function has finitely many zeros in each compact rectangle. Thus the proof requires neither Stirling's formula nor RH, simple zeros or any numerical zero experiment.

## PGC4. Polynomial nonvanishing and the exact rational action

If \(P\ne0\) and \([\lambda_P]=0\), PGC2 forces \(F(\rho)=P(\rho)\) at every actual zero for some \(F\in\mathcal B\). Along unbounded zero heights, \(F(\rho)\to0\). A nonzero constant does not tend to zero. For degree \(d\ge1\), the leading term gives
\(|P(z)|\ge |p_d||z|^d/2\) for all sufficiently large \(|z|\).
Neither case is compatible with the equality. Thus the polynomial map is injective, and the explicitly defined \(c_\zeta=[\lambda_1]\) is nonzero.

The generator calculation is exact:
\[
 (1-L^t)\lambda_H=\lambda_{sH},
\]
because applying \(1-L\) to the test function at \(1-s\) multiplies it by \(s\). Thus the variable of the rational-function action is the actual twisted generator \(G=1-L^t\), not an untwisted operator silently substituted for it.

SCL's bijectivity of every nonzero polynomial in \(G\) makes
\(P(G)Q(G)^{-1}c_\zeta\) defined. Cross multiplication proves independence of the fraction representation. A nonzero rational function acts by a bijection on the cokernel, so it cannot kill \(c_\zeta\). This proves the entire embedded \(\mathbb C(s)\)-line, including its nonvanishing.

## PGC5. Every rational class has the stated entire representative

For a denominator root \(a\) of order \(k_a\), the Hermite conditions mean the derivatives of orders \(0\le j<k_a\). Their total number is \(d=\deg Q\). The evaluation map on polynomials of degree below \(d\) has zero kernel, since a polynomial in that kernel is divisible by the full denominator, including every multiplicity. Equal finite dimensions therefore give the unique interpolation polynomial \(T_{P,Q}\).

The condition
\(T_{P,Q}-e^{-s^2}P=O((s-a)^{k_a})\)
implies
\(e^{s^2}T_{P,Q}-P=O((s-a)^{k_a})\),
because \(e^{s^2}\) is entire and nonzero. Consequently
\[
 B_{P,Q}=e^{s^2}T_{P,Q}\in\mathcal B,\qquad
 H_{P,Q}=(P-B_{P,Q})/Q
\]
is entire. The Gaussian identity
\(|e^{(\sigma+it)^2}|=e^{\sigma^2-t^2}\)
proves the required rapid decrease of \(B_{P,Q}\) on every bounded strip.

Taylor division at \(a\) gives
\(H_{P,Q}(a)=(P-B_{P,Q})^{(k_a)}(a)/Q^{(k_a)}(a)\);
the two factors \(k_a!\) cancel because they occur in both leading Taylor coefficients. For every higher coefficient, division by the nonzero leading denominator coefficient gives the usual uniquely determined Taylor recursion. No pole coefficient has been discarded.

At large \(|t|\) in a bounded vertical strip, a degree-\(d\) polynomial denominator has a uniform lower bound \(c(1+|t|)^d\). Outside that large region and the finitely many root disks, it has a positive compact lower bound; inside the disks the quotient is holomorphic and bounded on their closures after a harmless enlargement. These estimates prove \(H_{P,Q}\in\mathcal M\). They also prove that changing the interpolating \(\mathcal B\)-function with the same full jets changes \(H_{P,Q}\) by an actual member of \(\mathcal B\).

Finally
\[
 Q(G)\lambda_{H_{P,Q}}
 =\lambda_{QH_{P,Q}}
 =\lambda_P-\mathcal D_L[B_{P,Q}]
\]
retains the exact correction. Taking the actual cokernel and its previously constructed inverse proves PGD5.5. There is no hidden division by a meromorphic function on the original test-space domain.

## PGC6. Complete real orbit, source labels and cone scope

For the original twisted action,
\[
 (T_r^\diamond\lambda_H)([F])
 =r\,\lambda_H([r^{-s}F(s)])
 =\lambda_{r^sH}([F]).
\]
The factor in the contour is exactly
\(r\,r^{-(1-s)}=r^s\).
Each \(r^sH\) belongs to \(\mathcal M\) because \(r>0\) and
\(|r^{\sigma+it}|=r^\sigma\) is bounded on every bounded strip.
This verifies the full real action directly; prime actions are its actual instances \(r=p\).

For \(H=r^s\), the values at every nontrivial zero satisfy
\(|r^\rho|\ge\min(1,r)>0\).
They cannot be the values of an element of \(\mathcal B\) along unbounded zero heights. Therefore each orbit class remains nonzero. PGD correctly makes no assertion that the orbit stays inside the particular rational-function line.

The maps preserve the existing receiving support labels by their exact linear lifts. The primitive source \(\tau\) is not an amplitude or the function \(1\). The faithful extra closed copies and all other cohomology groups of ASD14 remain. The actual algebraic cokernel is now proved nonzero, while its weak-* Hausdorff quotient remains zero; these two statements concern the explicitly different quotient constructions and do not contradict one another.

## PGC7. Result of the check

Every requested part of PGD0–PGD7 is verified: the larger multiplier quotient injection, the elementary Gamma-integral argument, the full multiplicity tests, the explicit polynomial nonzero class, the whole embedded rational-function line with entire Hermite-corrected representatives, and the complete real/prime orbit. All constants, derivative orders, signs and operation domains checked above agree with the stated proof. No correction to PGD was required.

The conclusion is the constructed nonzero infinite-dimensional receiving object in the actual comparison cone. It is not an unidentified RH counterexample, a contradiction of primitive \(Z_1/\tau\), or a replacement for the requested geometric weight separation. This bounded independent check ends here.

