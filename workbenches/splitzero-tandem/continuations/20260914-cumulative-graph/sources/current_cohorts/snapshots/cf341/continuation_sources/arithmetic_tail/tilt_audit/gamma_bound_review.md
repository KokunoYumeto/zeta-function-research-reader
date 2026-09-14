# Explicit bound for the retained Gamma factor

## Task and provenance

This bounded review was assigned by the `balanced_audit` lane. Its requested
object is exactly

\[
\left|\Gamma\!\left(\frac14+\frac{it}{2}\right)\right|^2,
\qquad t\in\mathbb R,\quad |t|\ge1.
\]

The assignment requests an explicit constant in front of
\(|t|^{-1/2}e^{-\pi|t|/2}\), independently of RH. No original argument,
coefficient, or phase is changed below. The existing shared-thread transcript
and user-input provenance remain upstream; this file is a mathematical review,
not a replacement transcript. Only this review file was written by this lane.

A bounded local search for `Stirling`, `Binet`, and Gamma remainder statements
in `work/rh_counterfactual_20260913` did not locate a usable explicit remainder
proof. Large transcript matches were excluded from the subsequent bounded
search; no full reading of those matches is asserted. The external formulas
actually inspected are NIST DLMF 5.9.10_2 and the first paragraph of 5.11(ii).
The proof below derives every estimate from the exact Binet integral.

## Exact analytic starting identity

For \(\Re z>0\), take the holomorphic branch of \(\log\Gamma(z)\) that is real
on the positive real axis, and the principal \(\log z\) on the right
half-plane. Binet's integral identity is

\[
\log\Gamma(z)
=\left(z-\frac12\right)\log z-z+\frac12\log(2\pi)+R(z),
\tag{G1}
\]
\[
R(z)=\int_0^\infty e^{-zu}
 \left(\frac{1}{e^u-1}-\frac1u+\frac12\right)\frac{du}{u}.
\tag{G2}
\]

This exact identity, with its right-half-plane domain and logarithmic branch
convention, is the classical starting identity used here; it is given in
[NIST DLMF 5.9.10_2](https://dlmf.nist.gov/5.9.E10_2), which attributes it to
Whittaker and Watson (1927), section 12.31. It is not an asymptotic assertion.

## Elementary bound on the Binet kernel

For \(u>0\), define the real kernel

\[
K(u)=\frac1u\left(\frac{1}{e^u-1}-\frac1u+\frac12\right).
\]

We prove

\[
0\le K(u)\le\frac1{12}\qquad(u>0).
\tag{G3}
\]

Put \(x=u/2>0\) for this kernel calculation. The identity
\(\coth x=(e^{2x}+1)/(e^{2x}-1)\) gives exactly

\[
K(u)=\frac{\coth x-1/x}{4x}.
\tag{G4}
\]

Set

\[
F(x)=x\cosh x-\sinh x,
\qquad
G(x)=(x^2+3)\sinh x-3x\cosh x.
\]

Both functions vanish at zero. Their derivatives are

\[
F'(x)=x\sinh x\ge0,
\qquad
G'(x)=x^2\cosh x-x\sinh x=xF(x)\ge0.
\]

Consequently \(F(x)\ge0\) and \(G(x)\ge0\) for \(x\ge0\). Dividing the
first inequality by the positive number \(x\sinh x\) gives
\(\coth x-1/x\ge0\). Dividing the second by the positive number
\(3x\sinh x\) gives

\[
\coth x\le\frac1x+\frac{x}{3}.
\]

Substitution in (G4) proves both inequalities in (G3). In particular, if
\(a=\Re z>0\), (G2) is absolutely convergent and

\[
|R(z)|
\le\int_0^\infty e^{-au}K(u)\,du
\le\frac1{12}\int_0^\infty e^{-au}\,du
=\frac1{12a}.
\tag{G5}
\]

At the original argument \(z=1/4+it/2\), this gives

\[
\left|R\!\left(\frac14+\frac{it}{2}\right)\right|\le\frac13,
\qquad
2\Re R\!\left(\frac14+\frac{it}{2}\right)\le\frac23.
\tag{G6}
\]

## Explicit estimate at the original argument

Let \(t\in\mathbb R\setminus\{0\}\), and retain

\[
z=\frac14+\frac{it}{2},\qquad
r=|z|=\sqrt{\frac1{16}+\frac{t^2}{4}},\qquad
\phi=\arg z=\arctan(2t),\qquad T=|t|.
\tag{G7}
\]

Since \(\log z=\log r+i\phi\), twice the real part of (G1), followed by
exponentiation, gives the exact identity

\[
|\Gamma(z)|^2
=2\pi r^{-1/2}
 \exp\!\left(-t\arctan(2t)-\frac12+2\Re R(z)\right).
\tag{G8}
\]

The function \(\arctan\) is odd, so
\(t\arctan(2t)=T\arctan(2T)\). For \(T>0\), the two positive angles
\(\arctan(2T)\) and \(\arctan(1/(2T))\) sum to \(\pi/2\). Moreover

\[
\arctan v=\int_0^v\frac{dw}{1+w^2}\le v
\qquad(v\ge0).
\]

It follows, keeping the constant \(-1/2\) from (G8), that

\[
-t\arctan(2t)-\frac12
=-\frac{\pi T}{2}
 +T\arctan\!\left(\frac1{2T}\right)-\frac12
\le-\frac{\pi T}{2}.
\tag{G9}
\]

Also, \(r\ge T/2>0\), hence

\[
r^{-1/2}\le\sqrt2\,T^{-1/2}.
\tag{G10}
\]

Combining the exact identity (G8) with (G6), (G9), and (G10) proves

\[
\boxed{
\left|\Gamma\!\left(\frac14+\frac{it}{2}\right)\right|^2
\le C_G |t|^{-1/2}e^{-\pi|t|/2},
\qquad C_G=2\pi\sqrt2\,e^{2/3}.
}
\tag{G11}
\]

The proof holds for every real \(t\ne0\), and therefore covers the requested
closed domain \(|t|\ge1\), including both endpoints. There is no assertion at
\(t=0\) in (G11), because its right side contains \(|t|^{-1/2}\).

## Audit of the proposed Stirling-remainder route

The alternative remainder estimate proposed in the assignment is also valid:
the first paragraph of
[NIST DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii) bounds the remainder after
the main logarithmic Stirling term by

\[
|R(z)|\le
\frac{\sec^2(\tfrac12\arg z)}{12|z|}.
\tag{G12}
\]

Here the first omitted Bernoulli term is \(B_2/(2z)=1/(12z)\), with
\(B_2=1/6\). On \(\Re z>0\), one has \(|\arg z|<\pi/2\), whence
\(\sec^2(\arg z/2)<2\). At the retained argument with \(|t|\ge1\),
\(|z|\ge|t|/2\ge1/2\). Thus (G12) implies

\[
|R(z)|\le\frac1{6|z|}\le\frac13,
\]

and (G8)--(G10) again give exactly (G11). This paragraph verifies the stated
literature bound and its substitution; (G1)--(G11) already supply a complete
proof of the explicit inequality from the exact Binet identity, without
depending on (G12).

## Global two-sided comparison for the original density

The parent lane subsequently requested a two-sided density comparison on the
entire real line, including zero. Define the original density and fixed decay
constant by

\[
\sigma(t)=\frac{\left|\Gamma\!\left(\frac14+\frac{it}{2}\right)\right|^2}{2\pi},
\qquad \alpha=\frac\pi2.
\tag{G13}
\]

Then, for every \(t\in\mathbb R\),

\[
\boxed{
c_\Gamma e^{-\alpha|t|}(1+|t|)^{-1/2}
\le \sigma(t)
\le C_\Gamma e^{-\alpha|t|}(1+|t|)^{-1/2},
}
\tag{G14}
\]
\[
\boxed{
c_\Gamma=\sqrt2\,e^{-7/6},
\qquad
C_\Gamma=\sqrt{2\sqrt5}\,e^{2/3}.
}
\tag{G15}
\]

Here \(C_\Gamma\) is the global density constant; it is different from the
constant \(C_G\) of the Gamma-factor estimate (G11).

To prove (G14), take any \(t\in\mathbb R\), write \(x=|t|\), and retain

\[
z=\frac14+\frac{it}{2},
\qquad r=|z|=\sqrt{\frac1{16}+\frac{x^2}{4}}>0.
\tag{G16}
\]

The derivation of the exact identity (G8) does not divide by \(t\) and is
valid at \(t=0\) as well. Thus, using the oddness of \(\arctan\),

\[
\sigma(t)
=r^{-1/2}\exp\!\left(-x\arctan(2x)-\frac12+2\Re R(z)\right).
\tag{G17}
\]

We first bound the exponent. For \(x\ge0\),
\(0\le\arctan(2x)\le\pi/2\), so

\[
-x\arctan(2x)-\frac12
\ge-\alpha x-\frac12.
\tag{G18}
\]

For \(x>0\), (G9) proves
\(-x\arctan(2x)-1/2\le-\alpha x\). At \(x=0\), this is the direct
inequality \(-1/2\le0\); no expression containing \(1/x\) is evaluated.
Using both signs of the remainder bound (G6) therefore gives, on all of
\(x\ge0\),

\[
-\alpha x-\frac76
\le -x\arctan(2x)-\frac12+2\Re R(z)
\le -\alpha x+\frac23.
\tag{G19}
\]

We next compare the retained modulus with \(1+x\). The exact squared
differences are

\[
\frac{(1+x)^2}{4}-r^2
=\frac{3+8x}{16}\ge0,
\tag{G20}
\]
\[
r^2-\frac{(1+x)^2}{20}
=\frac{(4x-1)^2}{80}\ge0.
\tag{G21}
\]

Since every modulus and comparison denominator here is strictly positive,
the two differences give

\[
\frac{1+x}{2\sqrt5}\le r\le\frac{1+x}{2},
\qquad
\sqrt2(1+x)^{-1/2}\le r^{-1/2}
\le\sqrt{2\sqrt5}(1+x)^{-1/2}.
\tag{G22}
\]

Exponentiation of (G19) preserves its order. Multiplying its lower bound by
the lower positive bound for \(r^{-1/2}\) in (G22), and its upper bound by
the upper positive bound in (G22), proves (G14) with exactly (G15), using
the identity (G17). In particular, (G18)--(G22) hold directly at \(x=0\),
where \(z=1/4\), \(r=1/4\), and the exact exponent is
\(-1/2+2\Re R(1/4)\). The proof includes the origin without taking a
singular limit.

All analytic input for this global comparison is already contained in
(G1)--(G6); its additional estimates (G18)--(G22) have been proved above.

## Scope

The estimates are for the literal Gamma factor and density above. They assume no zero of
zeta, no zero-free region, no RH, no polynomial packet, and no asymptotic
uniformity in a moving real part of the Gamma argument. Numerical samples are
unnecessary for this proof and were not substituted for it. No Lean, Lake, or
Elan process was run.
