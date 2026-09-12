# Exact axial coefficients of the actual source traces

Local mathematical continuation, 9 September 2026. This note is not included
in the frozen411-page publication snapshot. It contains full derivations;
independent review and later reader integration are pending.

## Sources and exact reading scope

The released166-page Navier--Stokes manuscript, printed author OpenAI,
SHA256 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f,
AppendixB, pp144--147, gives the original axis data (B.1),(B.3),(B.12).
Parent read those complete pages here, including the source kernel (B.11).
The entire existence theorem remains imported, not certified by this note.

The existing literature index routed Richard P. Stanley, *Enumerative
Combinatorics*, volume2, second edition, Cambridge,2024,
DOI10.1017/9781009262538, publication unit
PUBUNIT-4BF2B5664C54337A26C7F5DC. Parent read the title/copyright/contents
and complete printed pp37--44 (PDF55--62), including Theorem5.4.2,
all three proofs and Corollary5.4.3. We use the classical Lagrange
inversion formula in the form (5.65), and give its residue derivation
below. The book is a cited private reading source, not an upload payload.
An indexed OS mirror path did not resolve; the indexed `used often` path
did. No index rebuild was performed. The other two search hits were not read.

## 1. Original coordinate map and local inverse

Keep the source's fixed h, A=1/2+h, D=1/2-h, k=1+h,
nu>0, C, j0, Lambda, sigma_* and chosen source thresholds.
In particular A+D=1, 0<h<1/100 and 0<j0<=1/20.
Fix an actual preterminal time tau=1-t>0 in the central localized slab.
The original physical equations are

    tau=q(1-eta^2),     z=sqrt(nu) q^D eta.

Introduce the dimensionless coordinate x=z/(sqrt(nu) tau^D) while
retaining its exact inverse z=sqrt(nu) tau^D x and every scale factor.
Then

    x=f(eta)=eta(1-eta^2)^(-D),
    eta=x(1-eta^2)^D,     q=tau/(1-eta^2).                  (1)

Near eta=0 the powers use the holomorphic logarithm of 1-eta^2
which is zero at zero. We have f(0)=0 and f'(0)=1. Hence the complex
inverse-function theorem gives a unique holomorphic inverse eta(x)
on some disk about0. It is the actual real inverse from the source:
both inverses take0 to0 and solve (1), and the real inverse is unique.
Oddness follows because -eta(-x) solves the same inverse problem.
This supplies a genuine convergent Taylor expansion at each fixed
tau>0, not only a formal inverse. No time-uniform radius is asserted.

For any holomorphic F near0 and integer n>=1, (1) gives

    [x^n] F(eta(x))
       = (1/n)[u^(n-1)] F'(u)(1-u^2)^(Dn).                (2)

Here is a proof. A sufficiently small contour in the x plane maps
bijectively to a contour about u=0. Changing variable x=f(u) in the
coefficient residue gives Res F(u)f'(u)f(u)^(-n-1) du.
The residue of the derivative of F(u)f(u)^(-n) is zero. Therefore
the preceding residue equals (1/n)Res F'(u)f(u)^(-n) du, which is
exactly the right side of (2). This proves the needed Lagrange formula
with all domains and the branch specified. For n=0 the answer is F(0).

## 2. Closed formulas for every axial-velocity derivative

The actual axial trace is

    w0(z,t)=sqrt(nu) tau^(-A) W(x),
    W(x)=(1-eta(x)^2)^A (4eta(x)+j0).                    (3)

Write W(x)=sum_(n>=0) a_n x^n. Then a0=j0, a1=4 and, for j>=1,

    a_(2j)   = j0 (-1)^j A/j * binom((2j-1)D,j-1),
    a_(2j+1) = 4 (-1)^j/j * binom(2jD,j-1).              (4)

Every binomial here is the finite polynomial
binom(beta,l)=product_(m=0)^(l-1)(beta-m)/l!, with binom(beta,0)=1.
No gamma-function division at an exceptional argument is involved.

Proof of the even formula: the term 4eta(1-eta^2)^A is odd in x,
so only j0(1-eta^2)^A contributes. Its u derivative is
-2Aj0 u(1-u^2)^(A-1). Equation (2) with n=2j yields

    a_(2j)= -Aj0/j * [u^(2j-2)](1-u^2)^(A-1+2jD).

Since A-1=-D, the exponent is (2j-1)D. The binomial series gives
(4), including its sign. Proof of the odd formula: A+D=1 and (1)
imply the exact identity eta(1-eta^2)^A=x(1-eta^2).
For j>=1, the odd coefficient in (3) is thus -4[x^(2j)]eta(x)^2.
Applying (2) to F(u)=u^2 gives

    [x^(2j)]eta(x)^2=(1/j)[u^(2j-2)](1-u^2)^(2jD),

which is the second formula in (4). The constant and linear terms
follow immediately from eta(0)=0 and eta'(0)=1. This proves all cases.

Restoring the original physical coordinate, for every integer n>=0,

    partial_z^n w0(0,t)
       = n! nu^((1-n)/2) tau^(-A-nD) a_n.                (5)

Thus no viscosity or time factor disappears upon using x. This is
an exact trace of the actual localized cutoff-summed field, through
the axis-identification proof in Section33, not an arbitrary axis datum.

## 3. All derivatives of the angular trace, without changing its profile

Keep exactly

    d(u)=1-u^2, L(u)=1-2hu^2,
    H(u)=Du+d(u)(4u+j0),
    zeta_*(u)=-L(u)H(u)/(H(u)^2+sigma_*^2),
    phi(u)=exp(Lambda integral_0^u zeta_*(v)dv).

These are source (B.1),(B.3). Their complex domain contains a disk
about0: the rational denominator is nonzero at0, and the source has
already chosen a simply connected holomorphic neighborhood. On that
disk phi'=Lambda zeta_* phi and phi(0)=1.
The actual angular trace is

    b1(z,t)=(2/C) tau^(-k) G(x),
    G(x)=d(eta(x))^k phi(eta(x)).

For every n>=1, (2) proves the exact finite coefficient formula

    partial_z^n b1(0,t)
      =(2/C) nu^(-n/2) tau^(-k-nD) (n-1)!
        * [u^(n-1)] phi(u) d(u)^(k-1+nD)
                         (Lambda d(u) zeta_*(u)-2ku).    (6)

Indeed differentiate d^k phi by the product rule before applying
(2). For n=0 the value is (2/C)tau^(-k). Formula (6) needs only
finitely many coefficients of the explicitly specified rational
function and exponential. For completeness they can be obtained
without symbolic integration: expand zeta_*=sum z_l u^l and solve

    phi_0=1,
    (m+1)phi_(m+1)=Lambda sum_(l=0)^m z_l phi_(m-l).

The z_l follow by multiplying the rational numerator by the inverse
denominator series with its nonzero constant. These recurrences
are finite, uniquely determined and retain every original parameter.

## 4. Exact highest-radial axial coefficient at the physical origin

Section34 proves that the n=j correction summand in the ordinary
coefficient [sigma^j]u_z equals

    rho_j(q) (-1)^j/(2^j(j!)^2) partial_z^(2j)w0,
    sigma=r^2/2,  rho_0=1, rho_j(q)=chi(c_jq) for j>0.

At z=0, q=tau. Combining this identity with (4),(5) gives for j>=1

    w_j^highest(0,t)
      =rho_j(tau) j0 A (2j)!/[2^j(j!)^2 j]
         *binom((2j-1)D,j-1)
         *nu^(1/2-j) tau^(-A-2jD).                     (7)

This identifies one exact summand of the actual finite radial
coefficient. All lower correction orders remain in the full formula
(1229) of the frozen411-page reader. It neither discards their
contribution nor claims that (7) is the entire coefficient.
The analogous highest angular summand follows by substituting n=2j
from (6) into rho_j(-1)^j partial_z^(2j)b1/[2^j j!(j+1)!].
These are exact constructive source-to-coefficient maps. They do
not imply a sign for the full Weil quadratic form or a zeta-zero location.

## Verification boundary

The accompanying checker constructs the inverse in (1) by finite
coefficient iteration, independently forms (3), and compares all
coefficients through degree16 at three rational h values with (4).
Those51 exact rational checks are finite regressions; the proof of
all orders is (2)--(5), not an inference from the51 samples.
No Lean run, full-source certification, publication or deletion occurs.
