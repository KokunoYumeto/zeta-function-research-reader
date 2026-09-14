# Handoff: two source moments bound the original relation-block volume

## Parallel integration

Read main `952ef9fee1e1419b6858d920354de8fa99430b7d` and PR #25 at
`66fac5e7885a40cd4873e74b754907320f05b067`, including its full research note.
Retain its phase-dependent exact product, the independent first-degree theorem,
the written comparable norm-window theorem, and per-block threshold 2 / combined
threshold 4. This contribution does not redo those formalizations or claim new
Lean executions. No remote branch has been modified.

The general trace / trace-square determinant optimization is classical (Grone,
Johnson, Marques de Sá, Wolkowicz, 1984). The new application carries the actual
source, theta relations, supported quotient, and arithmetic action into it.

## 1. Existing library inputs

For the unchanged fixed arithmetic quotient E of dimension q, use

    B_N=[b_0,...,b_N], O_N=diag(omega_0,...,omega_N),
    K_N=B_N O_N^-1 B_N*, G_N=K_N^-1,
    R_N=O_N^-1 B_N* G_N.

The original remainder B_N and ambient arithmetic inclusion eta remain attached.
For q-1<=i<=j put

    F=[b_(i+1),...,b_j], Omega=diag(omega_(i+1),...,omega_j),
    D=K_j-K_i=F Omega^-1 F*.

Keep e / tau via the existing reconstruction and internal coequalizer. Do not
introduce another scalar core. Empty arithmetic packet is q=0, det=1; q=1 has a
separate exact scalar log bound. Main moment formulas with q-1 denominators use
q>=2.

## 2. Source cost and its operator type

I_ij:(E,G_i)->(E,G_j) is the coordinate identity. Its adjoint T=K_i G_j has
reverse Hilbert type. Form Q=T I_ij as an endomorphism of (E,G_i), then

    Z=Q^-1-I=D G_i=F Fdagger,
    Fdagger=Omega^-1 F* G_i.

Z is positive G_i-self-adjoint. Its spectrum is lambda>=0 and the old restriction
spectrum is g=1/(1+lambda). The ratio is det(I+Z)=V_i/V_j.

Do not assert A-normality or A-invariance of a Z-eigenspace. With the original
control H_i and H_j transported by the actual identity,

    [A,Z]=Hhat_j(I+Z)-(I+Z)H_i.

This follows by inversion of the existing return commutator.

## 3. Two source moments and the exact exterior map

    t1=tr Z=sum_n b_n*G_i b_n/omega_n,
    t2=tr Z^2=sum_(n,m) |b_n*G_i b_m|^2/(omega_n omega_m),
    area2=(t1^2-t2)/2
          =sum_(n<m) det Gram_Gi(b_n,b_m)/(omega_n omega_m).

The actual map Phi=R_i F goes from (C^(j-i),Omega) to the earlier source.
Then t1=HS(Phi)^2 and area2=HS(wedge^2 Phi)^2, using unscaled exterior bases
with determinant Grams. A tensor alternation has its literal 2! and must be
related by the quotient / alternating map, not called an identical metric.

The source relation is b=T_new-L_ij R_i F, with

    B_j b=0, b* O_j b=Omega+F*G_iF.

Both norm contributions are evaluated before b maps to the receiving fibre zero.
An admitted dependent exterior pair has represented zero area; its index is not
external absence.

## 4. New bounded theorem for the same cost

For q>=2 define

    d=sqrt((q*t2-t1^2)/(q-1)),
    a=(t1+(q-1)*d)/q, b=(t1-d)/q.

Positivity gives 0<=b<=a and the identities

    a+(q-1)b=t1, a^2+(q-1)b^2=t2.

Cauchy--Schwarz on all other eigenvalues proves lambda_max<=a. Therefore the
restriction gap g_min>=1/(1+a) is a derived quantity, not an extra premise.

The sharp bound with only the two traces is

    det(I+Z)<=(1+a)(1+b)^(q-1).

Complete proof in NOTE: the quadratic matching log(1+x), its derivative at b,
and its value at a majorizes log(1+x) on [0,a]. The exact positive error is

    (a-x)(x-b)^2 int_(1,infinity)
        1/((s+x)(s+b)^2(s+a)) ds.

A quadratic trace is fixed by q,t1,t2. Equality has one a and q-1 copies of b;
the zero-variance case is all b. This is the classical optimal moment problem,
not a new universal determinant theorem.

The full remainder is retained at the actual metric type. A bounded further
consequence is

    C3=tr((aI-Z)(Z-bI)^2)>=0,
    log det(I+Z)<=log(1+a)+(q-1)log(1+b)-C3/(3(1+a)^3).

## 5. Finite certificate with no independent gap

A proved trace upper cap A0>=t1^+ bounds the nonnegative spectrum. Choose rational
0<=B0<A0 and use the same Hermite polynomial with nodes A0,B0. Its trace is a
rational combination of q,t1,t2,log(1+A0),log(1+B0). Rational interval arithmetic
bounds it from enclosures for t1,t2. The executable helper retains every sign and
uses a rational logarithm enclosure. It does not certify omitted arithmetic
moment errors.

## 6. Composition with the new consecutive theorem

Its original local propagation gives, r=j-i,

    min_(i<=N<j) epsilon_N
       <=(omega_j/omega_i)^(1/(2r)) (V_i/V_j)^(1/(2r)).

Our direct composition replaces the last factor by

    [(1+a)(1+b)^(q-1)]^(1/(2r)).

For the two length-q quartet blocks, the supplied norm bound gives a fixed
C_h^win q. The existing lower budget therefore requires

    (D_h k)^(2q) <= (1+a)(1+b)^(q-1)

on each block. Do not claim its opposing arithmetic estimate yet.

A simple original-area upper bound avoids the square root entirely:

    det(I+Z)<=(1+t1)(1+2 area2/((q-1)t1))^(q-1), t1>0.

The forced lower counterpart is

    2 area2/((q-1)t1)
       >= [(D_h k)^(2q)/(1+t1)]^(1/(q-1))-1.

This turns the remaining problem into control of actual independent pair areas,
not just the largest correction or an independently chosen positive metric.
It is not a bound on every eigenvalue and not a new RH theorem.

## 7. Execution scope

The 22 new exact finite methods pass normally and with -O, including deliberate
failure of a formula omitting the cross-pairing. The 31 inherited manifest
entries verify; the prior 19-method restriction checker passes both modes.
No new Lean runtime, zeta-zero certificate, or arithmetic quadrature enclosure
was executed. An initial overly tight numerical calibration expectation was
repaired by using the actual trace-derived cap and a better specified rational
interpolation node; theorem statements were not weakened. Exported rational
intervals are outward rounded to a stated dyadic precision.
